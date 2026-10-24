# Finite verification

The executable checks verify the explicit circuits and the interval identities used in the capacity proofs. The universal lower bounds are analytical results. Exhaustive finite checks do not replace those proofs, establish a sharp constant, or certify originality.

## Reproduce the checks

From the repository root, use Python 3.10 or later:

```bash
python verification/run_all.py
```

Only the Python standard library is required. To record the printed output in a file:

```bash
python verification/run_all.py --output verification/results.json
```

The [recorded result](results.json) was obtained by this command. It reports the Python version, finite domains, and actual case counts. A check failure raises an exception and gives a nonzero process exit status.

The two programs can also be run individually:

```bash
python verification/routing.py
python verification/check_geometry.py
```

## What the routing checks cover

[routing.py](routing.py) generates every SWAP layer in the [constructions](../science/constructions.md). Its legality check rejects a repeated register within a layer, an unknown register, a self-SWAP, or a gate spanning more than one ring edge. Four deliberately invalid circuits check these failure paths.

Each data and ancillary register starts with a distinct symbolic input label. The program composes all SWAPs and compares the resulting complete permutation with the required data translation and opposite ancillary permutation. A SWAP circuit implements the same register permutation on arbitrary quantum states and references, so this is an exact check of each generated unitary, without a restriction to computational-basis input states. Restoration of an initialized state follows separately from its invariance under the verified ancillary permutation.

The checks also count depth and gates directly and compare them with the formulas. Balanced cases verify both the ancillary budget and the uniform upper bound $`D\le6F(n,k,m)`$.

| Domain | Cases |
|---|---:|
| Every nonempty anchor subset for $`2\le n\le9`$, every $`1\le k<n`$ | 7,136 |
| Every path rotation for $`2\le n\le64`$ | 2,016 |
| Balanced circuits for $`2\le n\le32`$, $`0\le m\le2n`$, $`1\le k\le\lfloor n/2\rfloor`$ | 11,440 |
| Balanced maximum-gap identities | 527 |
| Deliberately invalid layers rejected | 4 |

Across the generated circuits, **408,047 layers** and **3,652,359 SWAPs** are checked. The finite domains include one anchor, dense anchors, wraparound segments, unequal gaps, more allocated work than sites, and the ancilla-free branch.

Optional command-line limits change the routing domains:

```bash
python verification/routing.py --max-n 9 --path-max-n 64 --balanced-max-n 32
```

The arbitrary-subset enumeration is exponential in its first limit.

## What the geometry checks cover

[check_geometry.py](check_geometry.py) checks every ring size $`4\le n\le100`$ and every pair $`1\le D,k\le\lfloor n/4\rfloor`$. It verifies the exact proof's decrease of mixed data factors and the approximate proof's increase of the target rank exponent. It also verifies patch homogeneity, disjointness, the charged one-sided window, and the multiplicity with which every site appears after translating the cut.

| Identity or boundary | Cases |
|---|---:|
| Ring sizes | 97 |
| $`(n,D,k)`$ entropy-count and rank-count identities | 20,225 |
| Cut-patch geometries | 1,225 |
| Translated-window multiplicity identities | 1,225 |
| Rank cases with $`D=\lfloor n/4\rfloor`$ | 1,225 |
| Rank cases with $`k=\lfloor n/4\rfloor`$ | 1,225 |
| Both equalities at once | 97 |
| Touching disjoint patches with $`n=4D`$ | 25 |
| Injective causal neighborhoods with $`4D<n`$ | 1,200 |

The equality $`D=\lfloor n/4\rfloor`$ is permitted by the capacity proofs. The index-based gap proof uses the different, strict condition $`4D<n`$ to leave an injective neighborhood and a seam. The program checks both conventions explicitly.

## Proof dependencies that are not numerical checks

The [exact proof](../science/exact_capacity.md) uses an exact circuit factorization, data processing for mutual information, and finite-dimensional entropy inequalities. Its allowance for arbitrary mixed and correlated initialized work follows from the written patch lemma.

The [approximate proof](../science/approximate_capacity.md) uses a flat input rank, a bound on the target's largest eigenvalue, and a rank-projector measurement. Its error threshold and cancellation of arbitrary borrowed dimensions follow from those analytical comparisons.

The [placement proof](../science/placement.md) uses the local QCA-index stability theorem of Ranard, Walter, and Witteveen. The geometry program checks the finite interval used in the lift; it does not numerically verify the external theorem.

The [related-work account](../references/RELATED_WORK.md) identifies the primary sources and separates inherited ingredients from the capacity statement. Literature comparison, proof checking, and executable finite validation supply different kinds of evidence.
