# Thirty milestones for catalytic quantum routing

This map follows the scientific problem from individual quantum registers to the complete workspace–depth frontier. It contains exactly **30 understanding targets**, independent of any reader's background or learning history. It maps the conceptual structure of the project; it does not claim exhaustive mastery of every technical lemma or neighboring subject.

The allocation is **14 background/preliminary milestones and 16 narrative/innovation milestones**. The background joins two prerequisite strands: local circuits and QCA information flow, and quantum-channel return conditions with entropy and spectral tools. The narrative begins with elementary routing operations and local proof ingredients, then combines them into the global resource statement, its interpretation, and its limits.

The single educational anchor is Terry Farrelly, [*A review of Quantum Cellular Automata*, Quantum **4**, 368 (2020), arXiv:1904.13318v2](https://arxiv.org/html/1904.13318v2). The [Farrelly bridge](farrelly_bridge.md) identifies the selected sections, translates conventions, and supplies the channel and capacity material needed here. Primary papers cited in the scientific account support attribution and proof dependencies; they are not additional educational anchors.

| Phase | Milestones | Integrating endpoint |
|---|---|---|
| Background and preliminaries | M01–M14 | Formulate the complete routing task and identify the tools needed to study it. |
| Narrative and innovation | M15–M30 | Explain the matched frontier, why capacity matters, and which conclusions depend on each return contract. |

Read [the learning route](README.md) for orientation, [the model](../science/model.md) for authoritative statements, and [verification](../verification/README.md) for the scope of the finite checks.

## Phase I: Background and preliminaries

<a id="m01"></a>
### M01. Registers and initialized capacity

**Phase:** Background and preliminaries.

**Central question:** What is being counted when a circuit receives quantum workspace?

**Understanding target:** Distinguish a physical site, a quantum register, its Hilbert-space dimension, and its capacity in qubits. Explain why several qubits at one site increase capacity without increasing the number of occupied sites.

**Dependencies and story role:** No earlier milestone. This establishes the local objects from which geometry and resource accounting are built.

**Conceptual connection:** The quantity $`M=\sum_i\log_2\dim A_i`$ measures initialized capacity; $`M=m`$ for $`m`$ initialized qubits.

**Source pointers:** Farrelly §2.1; [registers and circuit layers](../science/model.md#registers-geometry-and-circuit-layers).

<a id="m02"></a>
### M02. Joint states and external references

**Phase:** Background and preliminaries.

**Central question:** Why can correct local output states still fail to preserve quantum information?

**Understanding target:** Explain how registers can share correlations, why a marginal state omits those correlations, and how an untouched reference records information that a correct implementation must preserve.

**Dependencies and story role:** [M01](#m01). The description expands from an individual register to the joint input on data, borrowed work, and a reference.

**Conceptual connection:** The promise is uniform over $`\rho_{SBR}`$, including entangled inputs; checking only separate register marginals would define a weaker task.

**Source pointers:** [Translation and return contracts](../science/model.md#translation-and-the-two-return-contracts); [Farrelly bridge](farrelly_bridge.md), which supplies the reference-system background.

<a id="m03"></a>
### M03. Universal channels and unitary action

**Phase:** Background and preliminaries.

**Central question:** What does it mean to implement the desired operation on every quantum input?

**Understanding target:** Distinguish a unitary acting on a closed register collection from the channel obtained after fixing and discarding ancillary systems. Explain why successful routing must preserve superpositions as well as individual input labels.

**Dependencies and story role:** [M01](#m01), [M02](#m02). This turns state manipulation into an input-independent operational promise.

**Conceptual connection:** Exact reduced unitary action forces any ancillary output to decouple from the arbitrary input; a separate return condition identifies that ancillary state.

**Source pointers:** Farrelly §§2.2–2.3 for dynamics and local descriptions; [exact unitary action and product return](../science/exact_capacity.md#why-exact-unitary-action-gives-product-return).

<a id="m04"></a>
### M04. Gates, layers, and local geometry

**Phase:** Background and preliminaries.

**Central question:** Which operations can occur in one counted layer?

**Understanding target:** Identify legal on-site and nearest-neighbor gates, distinguish register disjointness from site disjointness, and explain why unrestricted connectivity or intermediate resets would change the model.

**Dependencies and story role:** [M01](#m01), [M03](#m03). The allowed local operations acquire a precise physical cost.

**Conceptual connection:** The construction uses two-register SWAPs; the lower bounds permit general local unitary gates. On-site operations still count toward depth.

**Source pointers:** Farrelly §3.1; [geometry and layers](../science/model.md#registers-geometry-and-circuit-layers); [legality of the counterflow layers](../science/constructions.md#why-every-layer-is-legal).

<a id="m05"></a>
### M05. Heisenberg light cones

**Phase:** Background and preliminaries.

**Central question:** How does local gate depth constrain which inputs can influence an output?

**Understanding target:** Follow an output observable backward through a circuit, explain the growth of its support by at most one site per layer, and connect absent dependence to an impossibility of transmitting a changed input.

**Dependencies and story role:** [M03](#m03), [M04](#m04). This joins local gates into a causal constraint on the full circuit.

**Conceptual connection:** Fixed entanglement among initialized registers does not permit signaling outside this light cone. Translation by distance $`k`$ therefore requires $`D\ge k`$ under the stated accuracy promise.

**Source pointers:** Farrelly §§2.2–2.3; [constant-error light-cone lemma](../science/approximate_capacity.md#a-light-cone-bound-at-constant-error).

<a id="m06"></a>
### M06. Cyclic translation as a quantum task

**Phase:** Background and preliminaries.

**Central question:** What moves in a translation, and what must stay unchanged?

**Understanding target:** Describe the permutation $`i\mapsto i+k`$ of complete data registers on a ring, including unknown and entangled data. Explain the shorter-direction convention $`1\le k\le\lfloor n/2\rfloor`$ and why the identity rotation is excluded.

**Dependencies and story role:** [M04](#m04), [M05](#m05). The general locality framework is specialized to the operation studied here.

**Conceptual connection:** Moving every register by a short distance is a local target map, but that fact alone does not provide a shallow circuit.

**Source pointers:** Farrelly §1.1; [translation and return contracts](../science/model.md#translation-and-the-two-return-contracts).

<a id="m07"></a>
### M07. QCAs and finite-depth circuits

**Phase:** Background and preliminaries.

**Central question:** Why can a locality-preserving evolution fail to be a finite-depth local circuit?

**Understanding target:** Distinguish a bound on the spatial spread of observables from a decomposition into finitely many local gate layers. Use translation as the central example, while separating infinite-chain structure from finite-ring circuit depth.

**Dependencies and story role:** [M05](#m05), [M06](#m06). This identifies the structural obstruction beyond an ordinary light cone.

**Conceptual connection:** The finite-ring gap proof later uses an infinite-chain lift; it does not assign the infinite-chain invariant directly to an arbitrary finite-ring unitary.

**Source pointers:** Farrelly §§1.1, 3.1, and 5.2; [index stability input](../science/placement.md#the-index-stability-input).

<a id="m08"></a>
### M08. Index as directed information flow

**Phase:** Background and preliminaries.

**Central question:** What distinguishes a shift from a circuit when both preserve locality?

**Understanding target:** Explain the role of the one-dimensional QCA index as a measure of directed flow. Recognize that the original multiplicative index and its logarithm encode the same distinction with different conventions.

**Dependencies and story role:** [M07](#m07). A global invariant organizes the local-versus-circuit distinction.

**Conceptual connection:** In the logarithmic convention, finite-depth circuits have index zero and a nontrivial data shift has nonzero index. Stationary borrowed factors do not cancel that flow.

**Source pointers:** Farrelly §§5.2.1–5.2.2; [index conventions and attribution](../references/RELATED_WORK.md#attribution-of-the-proof-ingredients); [placement proof input](../science/placement.md#the-index-stability-input).

<a id="m09"></a>
### M09. Cancellation by an inverse copy

**Phase:** Background and preliminaries.

**Central question:** How can a second set of registers remove the circuit obstruction to a shift?

**Understanding target:** Explain why pairing a shift with an opposite shift cancels the net flow and admits a local circuit. Distinguish this doubled operation from implementing the desired action on the data alone.

**Dependencies and story role:** [M04](#m04), [M07](#m07), [M08](#m08). The obstruction now suggests the physical mechanism used by the upper construction.

**Conceptual connection:** The ancillary registers undergo a nontrivial permutation. Their availability becomes useful only when that permutation is compatible with the required return.

**Source pointers:** Farrelly §5.1; [one-step counterflow](../science/constructions.md#one-step-with-arbitrary-anchors); [prior inverse-copy construction](../references/RELATED_WORK.md#gnvw2012).

<a id="m10"></a>
### M10. Specified-state invariance and borrowed identity

**Phase:** Background and preliminaries.

**Central question:** When can a nontrivial ancillary operation still return reusable work?

**Understanding target:** Distinguish returning one specified initialized state from preserving every unknown borrowed state and its reference correlations. Explain how invariance of a fixed state under an ancillary permutation can satisfy the former contract.

**Dependencies and story role:** [M02](#m02), [M03](#m03), [M09](#m09). The counterflow mechanism is connected to the operational resource definition.

**Conceptual connection:** Initialization does not imply purity. Identical mixed product states may be invariant under cycling, whereas arbitrary borrowed values generally are not.

**Source pointers:** [Initialized and borrowed work](../science/interpretation.md#initialized-and-borrowed-work); [translation and catalyst return](../science/constructions.md#translation-by-several-sites-and-catalyst-return).

<a id="m11"></a>
### M11. Entropy and conditional correlations

**Phase:** Background and preliminaries.

**Central question:** How can local dimension constrain an entropy change even when the surroundings are correlated?

**Understanding target:** Relate entropy to a state's spectrum, distinguish the entropy of a part from the entropy of the whole, and explain why conditional entropy and mutual information track the effect of correlations with an untouched region.

**Dependencies and story role:** [M01](#m01), [M02](#m02). This starts the quantitative proof strand needed to charge initialized capacity.

**Conceptual connection:** Entropy is bounded by logarithmic dimension, and correlations carried by a finite register are bounded by its dimension. The exact patch lemma uses these facts without charging arbitrary borrowed width.

**Source pointers:** [Entropy capacity of an initialized patch](../science/exact_capacity.md#entropy-capacity-of-an-initialized-patch); [Farrelly bridge](farrelly_bridge.md) for the locally supplied entropy tools.

<a id="m12"></a>
### M12. Flat spectra, rank, and projectors

**Phase:** Background and preliminaries.

**Central question:** Why is a deliberately pure/mixed input useful for proving a circuit lower bound?

**Understanding target:** Explain the rank and largest eigenvalue of a normalized projector, the multiplication of ranks for independent factors, and how a projector measurement detects weight outside a chosen subspace.

**Dependencies and story role:** [M02](#m02), [M11](#m11). The spectral description of a witness provides a second route to a capacity bound.

**Conceptual connection:** Products of pure and completely mixed registers have a flat nonzero spectrum. This special structure permits an error bound without a factor depending on arbitrary borrowed dimensions.

**Source pointers:** [Target profile and input rank](../science/approximate_capacity.md#a-target-profile-and-its-input-rank); [distinguishing measurement](../science/approximate_capacity.md#a-two-outcome-distinguishing-measurement).

<a id="m13"></a>
### M13. Joint-return diamond accuracy

**Phase:** Background and preliminaries.

**Central question:** Which errors must an approximate routing promise control?

**Understanding target:** Explain why the comparison includes the data, borrowed work, initialized output, and any input reference. Distinguish a bound on the whole output channel from approximate restoration of each work marginal.

**Dependencies and story role:** [M02](#m02), [M03](#m03), [M12](#m12). The spectral witness is connected to an operational accuracy requirement.

**Conceptual connection:** The repository uses an unhalved diamond norm, with maximum channel distance two. Its product-pure theorem uses $`\epsilon<1`$; the different gap theorem uses a reduced-channel threshold $`1/192`$.

**Source pointers:** [Approximation includes return](../science/model.md#approximation-includes-return-of-the-work); [channel and return condition](../science/approximate_capacity.md#channel-and-return-condition).

<a id="m14"></a>
### M14. The complete routing problem

**Phase:** Background and preliminaries.

**Central question:** What exactly is optimized, and under which common physical rules?

**Understanding target:** Assemble the data operation, nearest-neighbor depth, initialized capacity, placement freedom, arbitrary borrowed work, and return accuracy into one well-defined problem. Identify the separate exact and product-pure approximate models.

**Dependencies and story role:** [M06](#m06), [M08](#m08), [M10](#m10), [M11](#m11), [M12](#m12), [M13](#m13). This integrates both prerequisite strands before the project-specific arguments begin.

**Conceptual connection:** A resource statement must retain its quantifiers: the frontier optimizes placement and initialized state, while each implementation must handle every allowed data-and-borrowed input.

**Source pointers:** [Model and optimal depth](../science/model.md); [the attained frontier](../science/model.md#the-attained-frontier).

## Phase II: Narrative and innovation

<a id="m15"></a>
### M15. Routing through one sparse-anchor segment

**Phase:** Narrative and innovation.

**Central question:** How does one initialized anchor allow a neighboring segment to advance?

**Understanding target:** Follow the saved anchor data, the ancillary contents at the segment endpoint, and the sequence of adjacent SWAPs that moves each intervening data register one site right.

**Dependencies and story role:** [M04](#m04), [M06](#m06), [M09](#m09), [M14](#m14). The narrative starts with a concrete local component of the constructive mechanism.

**Conceptual connection:** Sparse anchors replace the dense inverse-copy layer with a sweep whose duration is set by the segment length.

**Source pointers:** [One step with arbitrary anchors](../science/constructions.md#one-step-with-arbitrary-anchors); [exact action of the schedule](../science/constructions.md#why-the-action-is-exact).

<a id="m16"></a>
### M16. The complete counterflow permutation

**Phase:** Narrative and innovation.

**Central question:** What happens when all sparse segments operate together?

**Understanding target:** Explain why disjoint segments can run in parallel, why the final simultaneous SWAPs are legal, and how the full circuit translates the data while cycling anchor contents oppositely.

**Dependencies and story role:** [M15](#m15). The local segment operation is joined into one complete register permutation.

**Conceptual connection:** For largest anchor spacing $`g`$ and $`a`$ active anchors, one step costs depth $`g+1`$ and $`n+a`$ SWAPs; repeating $`k`$ times multiplies both costs by $`k`$.

**Source pointers:** [Layer legality](../science/constructions.md#why-every-layer-is-legal); [exact action](../science/constructions.md#why-the-action-is-exact); [several-site translation](../science/constructions.md#translation-by-several-sites-and-catalyst-return).

<a id="m17"></a>
### M17. Mixed-state return and purification

**Phase:** Narrative and innovation.

**Central question:** Why does a returned maximally mixed catalyst still differ from borrowed work?

**Understanding target:** Explain how the opposite anchor permutation preserves an invariant physical state while potentially changing correlations with an inaccessible purifier. Understand why preserving a full-rank catalyst together with that purifier forces identity action on its entire support in an exact universal task.

**Dependencies and story role:** [M10](#m10), [M16](#m16). The construction's ancillary output is checked against the precise return contract.

**Conceptual connection:** The matched exact frontier permits fixed mixed catalysts, but its operational meaning does not extend to arbitrary purification-preserving work under the same name.

**Source pointers:** [Purification boundary](../science/interpretation.md#why-a-mixed-catalysts-purification-matters); [catalyst return](../science/constructions.md#translation-by-several-sites-and-catalyst-return).

<a id="m18"></a>
### M18. The ancilla-free block exchange

**Phase:** Narrative and innovation.

**Central question:** How can the shift always be implemented when initialized work is scarce?

**Understanding target:** Describe the rotation as a stable exchange of two contiguous blocks, preserving the order within each block. Explain how parallel adjacent crossings give depth $`n-1`$ and $`k(n-k)`$ SWAPs.

**Dependencies and story role:** [M04](#m04), [M06](#m06). This supplies the second construction needed to cap the depth independently of workspace.

**Conceptual connection:** The optimized upper bound chooses between sparse counterflow and block exchange. A resource frontier must include the regime where adding a few anchors offers no asymptotic improvement.

**Source pointers:** [Ancilla-free schedule](../science/constructions.md#an-ancilla-free-schedule).

<a id="m19"></a>
### M19. Isolating the two circuit boundaries

**Phase:** Narrative and innovation.

**Central question:** How can an arbitrary local circuit be reduced to two controlled cut neighborhoods?

**Understanding target:** Explain the circuit obtained by deleting gates across two cuts, and how conjugation gathers the deleted action into depth-sized patches. Distinguish the input-side and output-side factorizations and their generally different patch unitaries.

**Dependencies and story role:** [M04](#m04), [M05](#m05), [M14](#m14). This supplies the common local structure for the two capacity proofs.

**Conceptual connection:** The patches remain disjoint for $`D\le\lfloor n/4\rfloor`$, including equality. Internal left and right unitaries preserve the relevant half-ring spectra and entropy.

**Source pointers:** [Cut-factorization lemma](../science/exact_capacity.md#cut-factorization); [approximate proof orientation](../science/approximate_capacity.md#two-cut-neighborhoods).

<a id="m20"></a>
### M20. The exact domain-wall witness

**Phase:** Narrative and innovation.

**Central question:** Which permissible input reveals a directed shift as a required entropy decrease?

**Understanding target:** Explain the pure/mixed spatial profile, the homogeneous states near the two cuts, and the loss of exactly $`k`$ mixed data factors from one half under translation. Explain why borrowed registers can be assigned the same profile as part of a valid witness.

**Dependencies and story role:** [M06](#m06), [M10](#m10), [M11](#m11), [M19](#m19). A universal circuit promise is tested on a strategically chosen input.

**Conceptual connection:** Borrowed work returns by identity and the initialized state returns exactly, so their target entropy contributions cancel; the data translation supplies the required change.

**Source pointers:** [Exact theorem proof](../science/exact_capacity.md#proof-of-the-theorem); [domain-wall attribution](../references/RELATED_WORK.md#yls2024).

<a id="m21"></a>
### M21. Entropy capacity of one initialized patch

**Phase:** Narrative and innovation.

**Central question:** How much of the required entropy decrease can a cut patch produce?

**Understanding target:** Explain why initialized registers of total logarithmic dimension $`\log_2\dim K`$ can lower the relevant entropy by at most three times that amount in the witness. Track why correlations between $`K`$ and the surroundings are allowed.

**Dependencies and story role:** [M11](#m11), [M19](#m19), [M20](#m20). This is the local quantitative step behind the exact converse.

**Conceptual connection:** The initialized capacity is charged while the dimension of the pure or maximally mixed uninitialized part cancels. Arbitrary borrowed width therefore does not evade the bound.

**Source pointers:** [Entropy-capacity lemma](../science/exact_capacity.md#entropy-capacity-of-an-initialized-patch); [borrowed-width cancellation](../science/interpretation.md#why-arbitrary-borrowed-width-disappears-from-the-bounds).

<a id="m22"></a>
### M22. Preparing the approximate rank comparison

**Phase:** Narrative and innovation.

**Central question:** Why does the approximate proof choose its homogeneous target profile first?

**Understanding target:** Explain how inverse translation determines the data input, why borrowed inputs remain unchanged, and why the left input has flat rank $`r`$ while the target rank is $`r2^k`$. Identify where product-pure initialized work supplies factorization.

**Dependencies and story role:** [M12](#m12), [M13](#m13), [M19](#m19). The proof changes from exact entropy accounting to an error-sensitive spectral comparison.

**Conceptual connection:** Removing the output-side cut unitaries preserves the actual flat rank while allowing an upper bound on the target's largest eigenvalue. General correlated initialized states need not have these properties.

**Source pointers:** [Target profile and input rank](../science/approximate_capacity.md#a-target-profile-and-its-input-rank); [removing the cut unitaries](../science/approximate_capacity.md#remove-the-cut-unitaries).

<a id="m23"></a>
### M23. Detecting insufficient local initialized capacity

**Phase:** Narrative and innovation.

**Central question:** How does a rank-projector measurement turn the spectral comparison into a workspace requirement?

**Understanding target:** Explain why the actual output lies in a rank-$`r`$ subspace, while insufficient initialized dimension limits the ideal output's weight there. Relate the resulting distinguishing probability to the unhalved trace-norm error.

**Dependencies and story role:** [M13](#m13), [M22](#m22). This establishes the local obstruction that survives fixed implementation error.

**Conceptual connection:** At $`\epsilon<1`$, integer qubit capacity forces every relevant backward window of $`D`$ sites to contain at least $`k`$ initialized qubits. The conclusion uses joint return and product-pure work.

**Source pointers:** [Two-outcome measurement](../science/approximate_capacity.md#a-two-outcome-distinguishing-measurement); [local capacity theorem](../science/approximate_capacity.md#local-capacity-theorem).

<a id="m24"></a>
### M24. From local capacity to total throughput

**Phase:** Narrative and innovation.

**Central question:** How do many local restrictions produce a lower bound involving the whole ring?

**Understanding target:** Explain the sum over translated cuts and count how often each initialized register is charged. Derive the distinction between the exact two-patch estimate $`12Dm\ge nk`$ and the product-pure one-sided estimate $`Dm\ge nk`$ in their shallow regimes.

**Dependencies and story role:** [M21](#m21), [M23](#m23). The local proof components become global resource constraints.

**Conceptual connection:** The factor $`nk`$ records the simultaneous demand across all cuts. The initialized capacity is shared across those demands rather than independently available at every cut.

**Source pointers:** [Exact theorem and averaging](../science/exact_capacity.md#proof-of-the-theorem); [approximate local theorem](../science/approximate_capacity.md#local-capacity-theorem).

<a id="m25"></a>
### M25. An empty interval and the QCA obstruction

**Phase:** Narrative and innovation.

**Central question:** Why does a long interval without initialized work obstruct shallow routing even without catalyst return?

**Understanding target:** Explain how an initialized-work-free causal neighborhood removes the ancillary-state expectation, how the actual finite circuit is lifted periodically, and how blocking permits comparison with a shift through local index stability.

**Dependencies and story role:** [M05](#m05), [M08](#m08), [M13](#m13), [M19](#m19). The QCA background now supplies a separate spatial converse.

**Conceptual connection:** At reduced data-plus-borrowed diamond error at most $`1/192`$, the largest anchor spacing $`g(C)`$ implies $`D\ge\lceil g(C)/4\rceil`$. Arbitrary initialized correlations are allowed; return is unnecessary.

**Source pointers:** Farrelly §§5.2.1–5.2.2 for index orientation; [gap theorem and lift](../science/placement.md#gap-theorem); [imported stability theorem](../references/RELATED_WORK.md#rww2022).

<a id="m26"></a>
### M26. Capacity, coverage, and prescribed placement

**Phase:** Narrative and innovation.

**Central question:** Why does equal total workspace not imply equal routing depth for different layouts?

**Understanding target:** Distinguish total qubit capacity, the number of occupied sites, the largest empty spacing, and the capacity in every short window. Explain how concentrated work may satisfy a total budget while leaving a spatial bottleneck.

**Dependencies and story role:** [M16](#m16), [M23](#m23), [M24](#m24), [M25](#m25). The capacity and gap results are combined without mixing their assumptions.

**Conceptual connection:** The one-site shift has a matching largest-gap scale when the anchor states can be chosen. For general $`k`$, the local necessary condition does not establish a matching optimum for every irregular profile.

**Source pointers:** [Support density](../science/placement.md#consequences-for-support-density); [local capacity and fixed placement](../science/placement.md#local-capacity-for-product-pure-work); [amount and location of work](../science/interpretation.md#the-amount-and-location-of-work).

<a id="m27"></a>
### M27. The frontier for every ring size

**Phase:** Narrative and innovation.

**Central question:** How do the component results determine the optimized depth for all $`n,k,m`$?

**Understanding target:** Combine the shallow capacity bounds with $`D\ge k`$ and the branch $`D>\lfloor n/4\rfloor`$. Explain how balanced anchors and the path construction give the matching upper scale, including zero workspace, dense workspace, and small rings.

**Dependencies and story role:** [M05](#m05), [M16](#m16), [M18](#m18), [M24](#m24), [M26](#m26). The constructive and converse branches meet in the complete theorem.

**Conceptual connection:** The common scale is $`F(n,k,m)=\min\{n,k\max(1,n/(m+1))\}`$. The exact and approximate optima share this scaling while retaining different initialized-state hypotheses and lower constants.

**Source pointers:** [Finite frontier theorem and proof](../science/model.md#the-attained-frontier); [balanced construction](../science/constructions.md#balanced-placement-and-the-frontier).

<a id="m28"></a>
### M28. Resource regimes and the capacity separation

**Phase:** Narrative and innovation.

**Central question:** In which regime does initialized capacity reveal a constraint missed by distance and spacing?

**Understanding target:** Explain the linear-depth, intermediate-throughput, and propagation-limited regimes. Interpret $`n=L^2`$, $`k=m=L`$: travel distance and balanced anchor spacing are order $`L`$, yet optimal depth is order $`L^2`$.

**Dependencies and story role:** [M24](#m24), [M26](#m26), [M27](#m27). The theorem is translated into its physical and architectural significance.

**Conceptual connection:** Sublinear depth requires both $`k=o(n)`$ and $`m/k\to\infty`$. At fixed $`k`$, sublinear but growing workspace still leaves diverging depth until the workspace becomes linear in $`n`$.

**Source pointers:** [Three regimes](../science/interpretation.md#three-regimes); [separation example](../science/interpretation.md#a-regime-missed-by-distance-and-gap-alone).

<a id="m29"></a>
### M29. Attribution and the kinds of evidence

**Phase:** Narrative and innovation.

**Central question:** Which ingredients are inherited, which statement is developed here, and what do the checks establish?

**Understanding target:** Identify the prior shift obstruction, domain-wall witness, inverse-copy circuit, and invariant-state catalytic mechanism. Distinguish analytical proofs, exact checks of finitely many generated permutations, and a targeted literature comparison.

**Dependencies and story role:** [M09](#m09), [M20](#m20), [M25](#m25), [M27](#m27), [M28](#m28). The complete result is placed in its evidential and scholarly context.

**Conceptual connection:** The contribution is the matched variable-capacity statement with explicit contracts. Finite checks neither prove arbitrary-circuit lower bounds nor establish exhaustive originality.

**Source pointers:** [Related work and attribution](../references/RELATED_WORK.md); [finite verification and its limits](../verification/README.md).

<a id="m30"></a>
### M30. The complete scientific meaning

**Phase:** Narrative and innovation.

**Central question:** What does catalytic quantum routing establish as one coherent resource statement?

**Understanding target:** Explain how opposite flow supplies the construction, why local initialized capacity limits its rate, and how the matched frontier follows. State the exact arbitrary-catalyst and approximate product-pure conclusions with their proper return contracts, placement optimization, and scope.

**Dependencies and story role:** [M14](#m14), [M17](#m17), [M26](#m26), [M27](#m27), [M28](#m28), [M29](#m29). This synthesizes the two phases from local mechanisms to the global contribution.

**Conceptual connection:** The results permit arbitrary borrowed width while charging initialized work. They do not establish the general fixed-error capacity frontier for correlated mixed catalysts or solve routing with measurements, teleportation, or unrestricted connectivity.

**Source pointers:** [Authoritative theorem](../science/model.md#the-attained-frontier); [operational interpretation](../science/interpretation.md); [boundaries](../science/interpretation.md#boundaries-of-the-result); [scientific account](../science/README.md).
