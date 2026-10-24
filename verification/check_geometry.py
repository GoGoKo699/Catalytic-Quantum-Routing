#!/usr/bin/env python3
"""Check the finite-ring geometry used by the capacity and placement proofs.

Run from the repository root:
    python verification/check_geometry.py

Only the Python standard library is required.  Every n from 4 through 100 is
checked, with every 1 <= D,k <= floor(n/4).  The main count is the number of
(n,D,k) triples.  Cut x=0 suffices for the domain-wall geometry by translation;
the one-sided window multiplicity is separately checked at every cut.

These finite checks verify interval identities and rank exponents.  They do
not replace the analytical entropy, spectral, or QCA-index arguments.
"""

from __future__ import annotations

import json


MIN_N = 4
MAX_N = 100


def require(condition: bool, message: str) -> None:
    """Keep verification active even if Python is invoked with -O."""
    if not condition:
        raise AssertionError(message)


def arc(n: int, start: int, stop: int) -> set[int]:
    """Sites in a half-open cyclic interval, using integer representatives."""
    require(0 <= stop - start <= n, "interval length must lie in [0,n]")
    return {site % n for site in range(start, stop)}


def check_geometry() -> dict[str, int]:
    counts = {
        "minimum_n": MIN_N,
        "maximum_n": MAX_N,
        "ring_sizes": 0,
        "geometry_cases": 0,
        "rank_count_cases": 0,
        "depth_boundary_rank_cases": 0,
        "shift_boundary_rank_cases": 0,
        "joint_boundary_rank_cases": 0,
        "touching_patch_geometry_cases": 0,
        "injective_gap_neighborhood_cases": 0,
        "window_count_cases": 0,
    }
    residues: set[int] = set()

    for n in range(MIN_N, MAX_N + 1):
        counts["ring_sizes"] += 1
        residues.add(n % 4)
        q, ell = n // 4, n // 2
        sites = set(range(n))
        left = set(range(ell))
        right = sites - left

        # For the approximate proof this is the TARGET mixed arc.  For the
        # exact proof the same arc is the INPUT pure arc.
        profile = arc(n, -q, ell - q)
        require(len(profile) == ell, f"n={n}: profile length")
        require(len(profile & left) == ell - q,
                f"n={n}: target mixed-data count")

        for depth in range(1, q + 1):
            label = f"n={n}, D={depth}"
            counts["geometry_cases"] += 1
            patch_x = arc(n, -depth, depth)
            patch_y = arc(n, ell - depth, ell + depth)

            require(len(patch_x) == len(patch_y) == 2 * depth,
                    f"{label}: patch cardinalities")
            require(not patch_x & patch_y, f"{label}: disjoint patches")
            require(patch_x <= profile, f"{label}: mixed target patch")
            require(not patch_y & profile, f"{label}: pure target patch")
            require(len(patch_x & left) == depth,
                    f"{label}: x patch left half")
            require(len(patch_x & right) == depth,
                    f"{label}: x patch traced-out half")
            require(len(patch_y & left) == depth,
                    f"{label}: y patch left half")
            require(len(patch_y & right) == depth,
                    f"{label}: y patch right half")
            require(patch_x & right == arc(n, -depth, 0),
                    f"{label}: charged one-sided window")

            # The endpoint D=q is included.  When n is divisible by four,
            # the patches meet at their boundaries and cover the entire ring
            # without sharing a site; otherwise exactly n mod 4 sites remain.
            if depth == q:
                require(len(sites - (patch_x | patch_y)) == n % 4,
                        f"{label}: boundary complement")
                if n % 4 == 0:
                    counts["touching_patch_geometry_cases"] += 1
                    require(patch_x | patch_y == sites,
                            f"{label}: touching patches cover the ring")
                    require(patch_x == profile,
                            f"{label}: touching mixed patch")
                    require(patch_y == sites - profile,
                            f"{label}: touching pure patch")

            # Each site appears in precisely D translated one-sided windows.
            # Thus summing the local inequalities gives D*M for every
            # initialized-capacity profile, not only a uniform profile.
            multiplicities = [0] * n
            for cut in range(n):
                window = arc(n, cut - depth, cut)
                require(len(window) == depth,
                        f"{label}, cut={cut}: window cardinality")
                for site in window:
                    multiplicities[site] += 1
            require(multiplicities == [depth] * n,
                    f"{label}: translated window multiplicities")
            counts["window_count_cases"] += 1

            # The index proof uses a different strict boundary condition:
            # 4D<n leaves an injective causal neighborhood and a seam.
            if 4 * depth < n:
                block_pair = arc(n, depth, 3 * depth)
                neighborhood = {
                    (site + offset) % n
                    for site in block_pair
                    for offset in range(-depth, depth + 1)
                }
                require(len(block_pair) == 2 * depth,
                        f"{label}: two blocked sites")
                require(neighborhood == arc(n, 0, 4 * depth),
                        f"{label}: exact causal neighborhood")
                require(len(neighborhood) == 4 * depth < n,
                        f"{label}: injective neighborhood with seam")
                counts["injective_gap_neighborhood_cases"] += 1

            for shift in range(1, q + 1):
                case = f"{label}, k={shift}"
                counts["rank_count_cases"] += 1

                # Approximate theorem: define the target first, then translate
                # its data profile by -k to obtain the input.
                approximate_input = arc(n, -q - shift, ell - q - shift)
                input_mixed = len(approximate_input & left)
                target_mixed = len(profile & left)
                require(input_mixed == ell - q - shift,
                        f"{case}: approximate input mixed count")
                require(target_mixed - input_mixed == shift,
                        f"{case}: target/input rank exponent difference")

                # Exact theorem: the pure input arc moves by +k.  The left
                # entropy then loses exactly k maximally mixed data factors.
                exact_output_pure = arc(n, -q + shift, ell - q + shift)
                exact_input_mixed = ell - len(profile & left)
                exact_output_mixed = ell - len(exact_output_pure & left)
                require(exact_input_mixed == q,
                        f"{case}: exact input mixed count")
                require(exact_output_mixed == q - shift,
                        f"{case}: exact output mixed count")
                require(exact_input_mixed - exact_output_mixed == shift,
                        f"{case}: exact entropy-count difference")

                if depth == q:
                    counts["depth_boundary_rank_cases"] += 1
                if shift == q:
                    counts["shift_boundary_rank_cases"] += 1
                    require(input_mixed == ell - 2 * q,
                            f"{case}: maximal-shift input boundary")
                    require(exact_output_mixed == 0,
                            f"{case}: maximal-shift output boundary")
                if depth == q and shift == q:
                    counts["joint_boundary_rank_cases"] += 1

    require(residues == {0, 1, 2, 3}, "all four residue classes were checked")
    expected = {
        "ring_sizes": 97,
        "geometry_cases": 1225,
        "rank_count_cases": 20225,
        "depth_boundary_rank_cases": 1225,
        "shift_boundary_rank_cases": 1225,
        "joint_boundary_rank_cases": 97,
        "touching_patch_geometry_cases": 25,
        "injective_gap_neighborhood_cases": 1200,
        "window_count_cases": 1225,
    }
    for key, value in expected.items():
        require(counts[key] == value, f"coverage count {key}: {counts[key]}")
    return counts


def main() -> None:
    result = {"status": "passed", **check_geometry()}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
