# Related work and attribution

Primary-source check: **24 October 2026**. This is a targeted comparison with the closest results located, not an exhaustive novelty claim. Bibliographic records are in [references.bib](references.bib). The [model](../science/model.md) and its return conditions are essential to every comparison below.

## The question being compared

The problem is to translate all unknown data on an $`n`$-site ring by $`k`$ sites, using geometrically nearest-neighbor unitary gates, while returning the available work. The variable resource is the **total initialized capacity**: $`m`$ ancillary qubits, with placement optimized as part of the implementation. Arbitrarily large borrowed registers are allowed, but their identity channel, including correlations with external references, must be preserved.

A fixed initialized catalyst has a different contract. Its complete physical state must return and decouple from the data and borrowed registers. Preservation of an inaccessible purification of that fixed state is not assumed. In particular, a translation-invariant mixed state can be a reusable catalyst. Initialization here does not mean purity, and the number of occupied work sites need not equal $`m`$.

The finite resource statement established in this repository is

```math
D_*(n,k,m)=\Theta\!\left(
\min\left\{n,\;k\max\left(1,\frac{n}{m+1}\right)\right\}
\right),
\qquad 1\le k\le\lfloor n/2\rfloor.
```

The exact version permits arbitrary fixed mixed and spatially entangled catalysts. The constant-error version assumes product-pure initialized work and measures the **joint output** error, including work return, in diamond norm. These are distinct theorems. The comparison sought below is a matching lower and upper bound in all three variables under these contracts, rather than the already established facts that a shift obstructs shallow circuits or that a second copy can cancel its flow.

## Closest primary sources

| Source and verified location | Established result relevant here | Relationship to the present statement |
|---|---|---|
| <a id="yls2024"></a> **Yin, Lucas, and Stephen (2024)**, [*Frobenius light cone and the shift unitary*](https://arxiv.org/html/2402.07990v2), §§2.2–2.3, Lemma 2.5, Eqs. (25)–(39); §3.4. BibTeX: `YinLucasStephen2024`. | A finite-ring shift obstruction using a pure/mixed domain wall, a cut-circuit decomposition, and a reduced-state spectral comparison. The paper also explicitly recalls the depth-two construction for a shift paired with its inverse. | This is the closest proof-level predecessor. The witness and spectral strategy are credited to this work. The additional accounting here concerns initialized Hilbert-space capacity inside the cut neighborhoods, arbitrary borrowed memory, and variable translation distance. |
| <a id="gnvw2012"></a> **Gross, Nesme, Vogts, and Werner (2012)**, [*Index theory of one dimensional quantum walks and cellular automata*](https://arxiv.org/html/0910.3675v2), §4, Proposition 1; §7.3, Theorem 9. BibTeX: `GrossNesmeVogtsWerner2012`. | The one-dimensional QCA index distinguishes shifts from locally implementable automata. Proposition 1 already gives local implementability of an automaton together with its inverse on a second copy. | The index obstruction and doubled construction are inherited. The classification does not itself specify the finite-ring optimum when the total initialized capacity and its placement vary. |
| <a id="rww2022"></a> **Ranard, Walter, and Witteveen (2022)**, [*A converse to Lieb–Robinson bounds in one dimension using index theory*](https://arxiv.org/html/2012.00741v2), Proposition 4.10. BibTeX: `RanardWalterWitteveen2022`. | Two nearest-neighbor QCAs have equal index if their automorphisms differ by at most $`1/192`$ in operator-map norm on an appropriate pair of neighboring cells. The threshold has no local Hilbert-space dimension factor. | This is the external stability theorem used in the separate [placement argument](../science/placement.md). It is not the proof of the finite-capacity throughput bound. |
| <a id="snz2025"></a> **Stephen, Nandkishore, and Zhang (2025)**, [*Many-body quantum catalysts for transforming between phases of matter*](https://arxiv.org/html/2410.23354v2), §II.2, Eq. (5), Theorem 1 and Eq. (6). BibTeX: `StephenNandkishoreZhang2025`. | An inverse copy of a QCA makes a finite-depth circuit; a suitable invariant state on that copy is returned and therefore acts as a catalyst. Their framework treats transformations between symmetry-protected phases. | The catalytic interpretation of the inverse-copy construction is prior work. The comparison here concerns a variable amount of spatially distributed work and circuit depth for a prescribed finite-ring translation, without a protecting symmetry. |
| <a id="bcgs2023"></a> **Bapat, Childs, Gorshkov, and Schoute (2023)**, [*Advantages and limitations of quantum routing*](https://arxiv.org/html/2206.01766v1), §§2–3 and §4.1. BibTeX: `BapatChildsGorshkovSchoute2023`. | General graph-based bounds for gate and Hamiltonian routing. Section 4.1 gives an ancillary-assisted separation on a vertex-barbell graph, with one associated ancilla per data qubit and negligible-time data–ancilla swaps in that Hamiltonian model. | General quantum routing and ancilla-assisted speedups are established. The graph, interaction-time convention, and dense ancillary allocation differ from the variable-capacity nearest-neighbor ring problem. |
| <a id="devulapalli2024"></a> **Devulapalli, Schoute, Bapat, Childs, and Gorshkov (2024)**, [*Quantum routing with teleportation*](https://arxiv.org/html/2204.04185v2), §II, Theorem 3.5, and §VII. BibTeX: `DevulapalliEtAl2024`. | Routing with measurements and classical communication, using local ancillary registers. The paper explicitly identifies the ancillary-count/routing-time tradeoff as a further question. Its sparse-routing parameter counts moved data tokens. | This is a close resource question in a different operational model. Here all data move, initialized capacity is variable, and routing is coherent and unitary. The present theorem does not settle the general teleportation-assisted tradeoff. |
| <a id="styliaris2025"></a> **Styliaris, Trivedi, Pérez-García, and Cirac (2025)**, [*Matrix-product unitaries: Beyond quantum cellular automata*](https://quantum-journal.org/papers/q-2025-02-25-1645/pdf/), Example 24 and §7. BibTeX: `StyliarisEtAl2025`. | Example 24 implements a family of phase matrix-product unitaries with $`N-2`$ initialized $`D`$-level ancillas, returning them for every input. The outlook emphasizes the effect of ancillas on QCA circuit complexity. | Ancilla-assisted implementation and return are not new mechanisms. The inspected construction and discussion do not supply the variable-$`m`$ cyclic-translation frontier or its local capacity converse. |
| <a id="folkertsma2026"></a> **Folkertsma, Mertz, Strelchuk, and Subramanian (2026)**, [*Fast Cliffords When Your Quantum Memory Is Full*](https://arxiv.org/html/2609.40144v1), §§2.1–2.2 and main results. BibTeX: `FolkertsmaEtAl2026`. | Arbitrary unknown work, including external correlations, can be restored while compressing Clifford circuits to logarithmic depth. Section 2.1 explicitly allows interactions between arbitrary pairs of qubits. | This is a relevant contemporary result about the borrowed-memory contract. Its interaction model has no geometric restriction. The local lower bound here does not imply that borrowed work is useless for general circuit parallelization. |

For broader orientation, Farrelly's [*A review of Quantum Cellular Automata*](https://arxiv.org/html/1904.13318v2), especially §§1.1, 5.1 and 5.2, explains the distinction between circuits and shifts, the inverse-copy construction, and one-dimensional index theory. The source for an invoked theorem remains the corresponding primary paper above (`Farrelly2020`).

## Attribution of the proof ingredients

The [exact capacity proof](../science/exact_capacity.md) and the [product-pure finite-error proof](../science/approximate_capacity.md) begin with the finite pure/mixed domain-wall approach of Yin, Lucas, and Stephen. In particular, their Eqs. (37)–(39) already compare a flat nonzero spectrum on one side of a cut against a smaller upper bound on the target state's largest eigenvalue. That argument must not be presented as a newly introduced witness.

The extension developed here charges the initialized registers in the causal neighborhoods of the cuts. For exact implementation, a local entropy-capacity estimate applies even when those registers are mixed and correlated across the ring. Averaging over cuts yields, in the shallow regime stated in the proof,

```math
12Dm\ge nk.
```

For product-pure work, a one-sided initialized dimension factor controls how much the target spectrum can change under the boundary circuit. A rank projection then gives the stronger local necessity: every relevant $`D`$-site interval contains at least $`k`$ initialized qubits when the joint diamond error is below one. Summing these local constraints gives $`Dm\ge nk`$. The arbitrary-correlated-catalyst exact theorem and the product-pure robust theorem should not be conflated.

The [upper construction](../science/constructions.md) is a sparse scheduling of opposite flows. Its dense endpoint is the established doubled-QCA construction, and return of an invariant catalyst follows the mechanism identified by Stephen, Nandkishore, and Zhang. The explicit contribution is the sparse anchor schedule, its charged depth, and its match to the lower bound as $`n,k,m`$ vary. Uniform mixed product states also return under the ancillary permutation; no claim that catalyst purity is necessary follows.

The [fixed-placement theorem](../science/placement.md) has a different role. An interval containing no initialized register allows the circuit to be compared locally with a shift. Ranard–Walter–Witteveen Proposition 4.10 supplies the dimension-independent contradiction. This theorem allows arbitrary initial catalyst correlations and does not need catalyst return, but it concerns empty spatial intervals. It does not by itself count multiple initialized qubits at one site or establish the $`nk`$ throughput factor.

The original GNVW QCA index is multiplicative, with the identity assigned one. The logarithmic convention used in Ranard–Walter–Witteveen is additive, with the identity assigned zero. Statements about trivial index must be read in the relevant convention.

## What separates the resource statement from its endpoints

The no-workspace endpoint, the dense-workspace endpoint, and a propagation bound do not determine the intermediate frontier. For example, when $`k=m=\sqrt n`$, both travel distance and the spacing between evenly distributed initialized sites are of order $`\sqrt n`$. The capacity inequality nevertheless forces depth of order $`n`$, matching the construction. This is the regime in which a total-workspace bound carries information beyond a light cone or a largest-gap bound.

Several hypotheses matter when comparing a purportedly faster protocol. Nonlocal SWAPs change the geometry. Measurements and rapid classical feedforward change the circuit model. Restoring only individual work marginals changes the return requirement. Conversely, a fixed mixed catalyst need not preserve an arbitrary external purification. These are different tasks, rather than interchangeable definitions of the same resource.

## Scope of the literature check

The check examined the primary texts above, their stated ancillary models, the cited proof locations, and targeted searches for cyclic translation, initialized or borrowed workspace, QCA catalysis, and routing space–depth tradeoffs, including recent 2026 results. Among these sources, no theorem with the same finite $`n,k,m`$ optimization and return contracts was located. This bounded finding supports the comparison recorded here; it does not establish that no such theorem exists elsewhere.

The inspected arXiv versions were GNVW v2, Ranard–Walter–Witteveen v2, Yin–Lucas–Stephen v2, Stephen–Nandkishore–Zhang v2, Bapat et al. v1, Devulapalli et al. v2, Folkertsma et al. v1, and Farrelly v2. For Styliaris et al., the published *Quantum* PDF and the arXiv v3 bibliographic record were checked. Published versions are identified by DOI in the accompanying bibliography.
