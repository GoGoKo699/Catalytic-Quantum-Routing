# Catalytic Quantum Routing

## How much reusable workspace makes a quantum shift fast?

Translating every quantum register around a ring by one site is a local target operation, yet a circuit without initialized work needs depth proportional to the ring size. A second set of registers can carry an opposite flow and make the translation shallow. This project quantifies the intermediate regime: the optimal depth when the amount of initialized work and the translation distance both vary.

The data occupy an $`n`$-site ring and move by $`k`$ sites, where $`1\le k\le\lfloor n/2\rfloor`$. Gates are unitary and geometrically nearest-neighbor. There are $`m`$ initialized ancillary qubits, with placement chosen as part of the implementation, and arbitrarily many borrowed registers. Initialized work must return to its specified state; borrowed work must undergo the identity channel, including preservation of its reference correlations.

## Main result

Define

```math
F(n,k,m)=
\min\!\left\{n,\;
k\max\!\left(1,\frac{n}{m+1}\right)\right\}.
```

The optimal exact depth satisfies

```math
\frac{F(n,k,m)}{12}
\le D_{\mathrm{ex}}^*(n,k,m)
\le 6F(n,k,m).
```

This converse permits arbitrary fixed mixed and spatially entangled initialized states, as well as arbitrary borrowed work. The upper bound uses a pure product state and explicit SWAP circuits.

For product-pure initialized work, the same scaling survives any joint output diamond error $`\epsilon<1`$, with the sharper lower bound

```math
\frac{F(n,k,m)}4
\le D_{\mathrm p}^*(n,k,m;\epsilon)
\le6F(n,k,m).
```

The diamond norm is unhalved, so its maximum channel distance is two. The error includes initialized-work return and all output correlations. The constants are safe finite-size bounds, not claimed optimal constants.

### The capacity mechanism

In the shallow regime $`D,k\le\lfloor n/4\rfloor`$, the exact converse gives

```math
12Dm\ge nk.
```

For product-pure work at error below one, every backward interval of $`D`$ sites must contain at least $`k`$ initialized qubits, giving $`Dm\ge nk`$. This condition counts capacity, rather than only the distance to the nearest initialized site.

For example, take $`n=L^2`$ and $`k=m=L`$. With evenly placed work, both the travel distance and the largest spacing between initialized sites are of order $`L`$. The capacity bound still forces depth of order $`L^2`$. This is the intermediate regime that the total-workspace theorem resolves.

## Circuits and physical resources

Two exact constructions give the upper bound:

| Construction | Initialized qubits used | Depth | SWAP gates |
|---|---:|---:|---:|
| Stable block exchange on a path | $`0`$ | $`n-1`$ | $`k(n-k)`$ |
| Counterflow through balanced anchors | $`a=\min(m,n)`$ | $`k(\lceil n/a\rceil+1)`$ | $`k(n+a)`$ |

The implementation uses the shallower circuit. For an arbitrary anchor pattern with largest cyclic spacing $`g`$, the counterflow schedule has depth $`k(g+1)`$. Its complete action is a data translation and the opposite permutation of the anchor registers. Any initialized state invariant under that ancillary permutation is returned, including identical mixed product states.

Layers contain gates on disjoint registers; different registers at one physical site may participate simultaneously. On-site gates count toward depth. The model has no intermediate measurements, resets, teleportation, or long-range gates. The [construction account](science/constructions.md) also explains the constant overhead for ancillas attached as side leaves.

## Read the scientific account

The connected account is organized by scientific topic:

| Page | What it establishes |
|---|---|
| [Model and optimal depth](science/model.md) | Complete channel contracts, optimization variables, and finite bounds |
| [Exact initialized capacity](science/exact_capacity.md) | Cut factorization and an entropy bound valid for arbitrary fixed catalysts |
| [Capacity at nonzero error](science/approximate_capacity.md) | A local rank obstruction for product-pure work with joint return |
| [Constructions](science/constructions.md) | Explicit schedules, ancillary permutations, depth, and gate counts |
| [Spatial placement](science/placement.md) | A dimension-independent empty-interval obstruction and local capacity conditions |
| [Interpretation and boundaries](science/interpretation.md) | Resource regimes, borrowed work, mixed-state return, and excluded extensions |
| [Related work](references/RELATED_WORK.md) | Closest primary sources, inherited mechanisms, and the precise comparison |
| [Verification](verification/README.md) | Runnable finite checks, recorded outputs, and their evidential limits |

[Science overview](science/README.md) provides a continuous reading route. [llms.txt](llms.txt) identifies the authoritative statements and assumptions for automated readers.

## Scope and attribution

The shift obstruction, the pure/mixed domain-wall method, and the dense inverse-copy construction have established predecessors. The contribution developed here is their capacity accounting for variable $`n,k,m`$, with explicit return contracts and a matching sparse construction. The [source comparison](references/RELATED_WORK.md) attributes those ingredients and records the bounded literature check.

Exact return of a mixed catalyst means restoration of its complete physical state. It does not require preservation of an inaccessible external purification. Arbitrary borrowed work has that stronger reference-preserving identity contract. The general fixed-error capacity theorem is restricted to product-pure initialized work; a separate small-error gap theorem permits arbitrary initialized states without requiring their return.

The frontier optimizes placement. A matching characterization for every prescribed irregular capacity profile is not asserted. The numerical checks verify finite schedules and witness geometry; the general lower bounds rest on the written proofs.

## Reproduce the finite checks

Python 3.10 or later and its standard library are sufficient:

```bash
python verification/run_all.py
```

The checks exhaust small anchor patterns, verify larger path and balanced circuits, and test the finite-ring geometry used in the lower bounds. See [verification details](verification/README.md) for the exact domains and recorded results.

## Purpose

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

See [LICENSE](LICENSE).
