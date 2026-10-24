#!/usr/bin/env python3
"""Generate and verify nearest-neighbor cyclic-routing SWAP schedules.

No state-vector simulation is needed: a SWAP network is completely specified by
its permutation of distinct input register labels.  The verifier also checks
register-disjoint layers, spatial locality, and the claimed resource counts.

Run from the repository root:
    python verification/routing.py

Only the Python standard library is required.
"""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Mapping, Sequence

Register = tuple[str, int]
Gate = tuple[Register, Register]
Layer = tuple[Gate, ...]


def _require_int(name: str, value: int, minimum: int) -> None:
    if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")


def _anchors(n: int, anchors: Iterable[int]) -> tuple[int, ...]:
    values = tuple(anchors)
    if not values:
        raise ValueError("at least one anchor is required")
    if any(not isinstance(x, int) or isinstance(x, bool) for x in values):
        raise ValueError("anchor sites must be integers")
    if any(x < 0 or x >= n for x in values):
        raise ValueError("anchor sites must lie in range(n)")
    if len(set(values)) != len(values):
        raise ValueError("anchor sites must be distinct")
    return tuple(sorted(values))


@dataclass(frozen=True)
class Plan:
    """An explicit circuit on data registers and its active ancillary registers."""

    n: int
    steps: int
    anchors: tuple[int, ...]
    kind: str
    layers: tuple[Layer, ...]

    @property
    def depth(self) -> int:
        return len(self.layers)

    @property
    def swaps(self) -> int:
        return sum(len(layer) for layer in self.layers)

    @property
    def layout(self) -> dict[Register, int]:
        result = {("S", i): i for i in range(self.n)}
        result.update({("A", j): site for j, site in enumerate(self.anchors)})
        return result


def cyclic_gaps(n: int, anchors: Iterable[int]) -> tuple[int, ...]:
    """Clockwise distances between successive distinct anchors."""
    _require_int("n", n, 2)
    sites = _anchors(n, anchors)
    return tuple(
        (sites[(j + 1) % len(sites)] - site) % n or n
        for j, site in enumerate(sites)
    )


def counterflow(n: int, anchors: Iterable[int], steps: int = 1) -> Plan:
    """Implement T_data**steps tensor C_ancilla**(-steps).

    Ancillary register A_j is at the j-th anchor in increasing cyclic order.
    The circuit acts on arbitrary ancillary inputs; exact state return follows
    separately when their joint state is invariant under C_ancilla**steps.
    """
    _require_int("n", n, 2)
    _require_int("steps", steps, 0)
    sites = _anchors(n, anchors)
    gaps = cyclic_gaps(n, sites)
    a = len(sites)

    initial: Layer = tuple(
        (("S", site), ("A", j)) for j, site in enumerate(sites)
    )
    sweep: list[Layer] = []
    for r in range(1, max(gaps)):
        gates: list[Gate] = []
        for j, gap in enumerate(gaps):
            if r < gap:
                endpoint = sites[(j + 1) % a]
                gates.append(
                    (("S", (endpoint - r) % n),
                     ("S", (endpoint - r + 1) % n))
                )
        sweep.append(tuple(gates))

    final: Layer = tuple(
        (("A", j), ("S", (site + 1) % n))
        for j, site in enumerate(sites)
    )
    one_step = (initial, *sweep, final)
    return Plan(n, steps, sites, "counterflow", one_step * steps)


def path_rotation(n: int, steps: int) -> Plan:
    """Right-rotate by steps using stable block exchange on the open path.

    For 1 <= steps < n the schedule has n-1 nonempty layers and
    steps*(n-steps) SWAPs.  Zero steps returns the empty circuit.
    """
    _require_int("n", n, 2)
    _require_int("steps", steps, 0)
    if steps >= n:
        raise ValueError("path-rotation steps must be smaller than n")
    if steps == 0:
        return Plan(n, 0, (), "path", ())

    u, v = n - steps, steps
    layers: list[Layer] = []
    for r in range(1, n):
        gates: list[Gate] = []
        for i in range(1, u + 1):
            j = r - u + i
            if 1 <= j <= v:
                left = i + j - 2
                gates.append((("S", left), ("S", left + 1)))
        layers.append(tuple(gates))
    return Plan(n, steps, (), "path", tuple(layers))


def balanced_anchors(n: int, active: int) -> tuple[int, ...]:
    _require_int("n", n, 2)
    _require_int("active", active, 1)
    if active > n:
        raise ValueError("at most one active register per anchor is selected")
    return tuple(j * n // active for j in range(active))


def balanced_rotation(n: int, allocated: int, steps: int) -> Plan:
    """Choose the shallower counted construction, breaking ties by SWAP count.

    Up to min(allocated,n) initialized registers are used.  Additional allocated
    registers are identity wires and are omitted from the returned active layout.
    """
    _require_int("n", n, 2)
    _require_int("allocated", allocated, 0)
    _require_int("steps", steps, 1)
    if steps > n // 2:
        raise ValueError("use the shorter direction: steps must be <= floor(n/2)")
    path = path_rotation(n, steps)
    if allocated == 0:
        return path
    active = min(allocated, n)
    catalytic = counterflow(n, balanced_anchors(n, active), steps)
    return min((path, catalytic), key=lambda plan: (plan.depth, plan.swaps))


def frontier(n: int, allocated: int, steps: int) -> Fraction:
    """Exact rational value of min(n, k*max(1,n/(m+1)))."""
    _require_int("n", n, 2)
    _require_int("allocated", allocated, 0)
    _require_int("steps", steps, 1)
    if steps > n // 2:
        raise ValueError("frontier uses 1 <= steps <= floor(n/2)")
    return min(
        Fraction(n),
        Fraction(steps) * max(Fraction(1), Fraction(n, allocated + 1)),
    )


def validate_layers(
    n: int,
    layout: Mapping[Register, int],
    layers: Sequence[Layer],
) -> None:
    """Reject a nonlocal gate, unknown wire, repeated wire, or empty layer."""
    for number, layer in enumerate(layers):
        if not layer:
            raise ValueError(f"layer {number} is empty")
        used: set[Register] = set()
        for left, right in layer:
            if left not in layout or right not in layout:
                raise ValueError(f"layer {number} refers to an unknown register")
            if left == right or left in used or right in used:
                raise ValueError(f"layer {number} uses a register twice")
            distance = abs(layout[left] - layout[right])
            if min(distance, n - distance) > 1:
                raise ValueError(f"layer {number} contains a nonlocal gate")
            used.update((left, right))


def output_labels(plan: Plan) -> dict[Register, Register]:
    """Map every output register to its input label."""
    validate_layers(plan.n, plan.layout, plan.layers)
    labels = {register: register for register in plan.layout}
    for layer in plan.layers:
        for left, right in layer:
            labels[left], labels[right] = labels[right], labels[left]
    return labels


def expected_labels(plan: Plan) -> dict[Register, Register]:
    expected = {
        ("S", i): ("S", (i - plan.steps) % plan.n)
        for i in range(plan.n)
    }
    if plan.kind == "counterflow":
        a = len(plan.anchors)
        expected.update({
            ("A", j): ("A", (j + plan.steps) % a)
            for j in range(a)
        })
    elif plan.kind != "path":
        raise ValueError(f"unknown plan kind: {plan.kind}")
    return expected


def check_plan(plan: Plan) -> None:
    observed = output_labels(plan)
    expected = expected_labels(plan)
    if observed != expected:
        mismatch = {
            str(wire): {"observed": observed[wire], "expected": expected[wire]}
            for wire in expected if observed[wire] != expected[wire]
        }
        raise AssertionError(
            f"incorrect {plan.kind} permutation for "
            f"n={plan.n}, anchors={plan.anchors}, steps={plan.steps}: {mismatch}"
        )
    if plan.kind == "counterflow":
        depth = plan.steps * (max(cyclic_gaps(plan.n, plan.anchors)) + 1)
        swaps = plan.steps * (plan.n + len(plan.anchors))
    elif plan.steps == 0:
        depth = swaps = 0
    else:
        depth = plan.n - 1
        swaps = plan.steps * (plan.n - plan.steps)
    if (plan.depth, plan.swaps) != (depth, swaps):
        raise AssertionError("resource count does not match the proved formula")


def check_rejections() -> int:
    """Check that the legality verifier rejects four distinct invalid layers."""
    layout = {("S", i): i for i in range(4)}
    invalid = (
        (((("S", 0), ("S", 2)),),),  # nonlocal
        (((("S", 0), ("S", 1)), (("S", 0), ("S", 3))),),  # shared wire
        (((("S", 0), ("A", 0)),),),  # unknown wire
        (((("S", 0), ("S", 0)),),),  # self-SWAP
    )
    for layers in invalid:
        try:
            validate_layers(4, layout, layers)
        except ValueError:
            continue
        raise AssertionError("the layer verifier accepted an invalid layer")
    return len(invalid)


def verify_finite(
    max_n: int = 9,
    path_max_n: int = 64,
    balanced_max_n: int = 32,
) -> dict[str, int]:
    """Exhaustive finite domains, with no random sampling."""
    for name, value in (
        ("max_n", max_n),
        ("path_max_n", path_max_n),
        ("balanced_max_n", balanced_max_n),
    ):
        _require_int(name, value, 2)

    counts = {
        "counterflow_cases": 0,
        "path_rotation_cases": 0,
        "balanced_frontier_cases": 0,
        "balanced_gap_cases": 0,
        "layers_checked": 0,
        "swaps_checked": 0,
        "invalid_layer_rejections": check_rejections(),
    }

    def record(plan: Plan, category: str) -> None:
        check_plan(plan)
        counts[category] += 1
        counts["layers_checked"] += plan.depth
        counts["swaps_checked"] += plan.swaps

    for n in range(2, max_n + 1):
        for a in range(1, n + 1):
            for anchors in itertools.combinations(range(n), a):
                for steps in range(1, n):
                    record(counterflow(n, anchors, steps), "counterflow_cases")

    for n in range(2, path_max_n + 1):
        for steps in range(1, n):
            record(path_rotation(n, steps), "path_rotation_cases")

    for n in range(2, balanced_max_n + 1):
        for active in range(1, n + 1):
            gap = max(cyclic_gaps(n, balanced_anchors(n, active)))
            if gap != (n + active - 1) // active:
                raise AssertionError("balanced placement has the wrong maximum gap")
            counts["balanced_gap_cases"] += 1
        for allocated in range(0, 2 * n + 1):
            for steps in range(1, n // 2 + 1):
                plan = balanced_rotation(n, allocated, steps)
                record(plan, "balanced_frontier_cases")
                if plan.depth > 6 * frontier(n, allocated, steps):
                    raise AssertionError("the uniform upper bound D <= 6F failed")
                if allocated == 0 and plan.anchors:
                    raise AssertionError("an ancilla-free plan used initialized work")
                if len(plan.anchors) > allocated:
                    raise AssertionError("plan exceeded the initialized-register budget")

    return counts


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=9)
    parser.add_argument("--path-max-n", type=int, default=64)
    parser.add_argument("--balanced-max-n", type=int, default=32)
    args = parser.parse_args()
    counts = verify_finite(args.max_n, args.path_max_n, args.balanced_max_n)
    print(json.dumps({
        "status": "passed",
        "domains": {
            "all_anchor_subsets_up_to_n": args.max_n,
            "all_path_rotations_up_to_n": args.path_max_n,
            "balanced_frontier_up_to_n": args.balanced_max_n,
            "allocated_registers": "0 through 2*n in balanced-frontier cases",
        },
        **counts,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
