# From quantum cellular automata to catalytic routing

Move every unknown quantum register one site around a ring. Each input has a nearby destination, yet all registers must move together without losing information. The central question is how initialized work, returned for reuse, changes the depth needed to perform this translation.

The selected educational anchor is **Terry Farrelly, [*A review of Quantum Cellular Automata*](https://quantum-journal.org/papers/q-2020-11-30-368/), Quantum 4, 368 (2020)**, DOI [10.22331/q-2020-11-30-368](https://doi.org/10.22331/q-2020-11-30-368). The section pointers below refer to [arXiv:1904.13318v2](https://arxiv.org/html/1904.13318v2), the version identified by the publisher.

This page connects that source to the project's finite-ring model. The [milestone map](milestones.md) records the common understanding targets; the [scientific account](../science/README.md) contains the complete statements and proofs.

## A focused route through the anchor

| Farrelly section | Read for | Project connection |
|---|---|---|
| 1.1 | Circuit and shift examples | A local target can require a deep implementation. |
| 2.1–2.3 | Site algebras and local dynamics | Translate between data motion and observable support. |
| 3.1 | Circuit partitions | Interpret layers and support propagation. |
| 5.1 | Paired forward and inverse dynamics | Understand the starting point for counterflow. |
| 5.2.1 | One-dimensional index | Identify the obstruction carried by a shift. |
| 5.2.2 | A local index formula | Understand why a bounded region can detect flow. |
| 6.1 | QCA and Hamiltonian locality | Keep the discrete gate model distinct from continuous-time evolution. |

The project-specific additions are the work-return contracts, sparse scheduling, and finite capacity bounds. Those results are developed below and in the linked proofs; they are not attributed to the review.

## 1. States move forward; observables look backward

Let $`S_i`$ be the data register at site $`i`$, with labels taken modulo $`n`$. A state $`\rho`$ describes the data, including its correlations. An observable $`O_j`$ is an operator measured at output site $`j`$. Under a unitary $`U`$, the two equivalent descriptions are

```math
\rho\longmapsto U\rho U^\dagger,
\qquad
O_j\longmapsto U^\dagger O_jU.
```

The first describes the output state. The second asks which input operator has the same measurement statistics. Their equivalence follows from

```math
\operatorname{Tr}(O_jU\rho U^\dagger)
=\operatorname{Tr}(U^\dagger O_jU\,\rho).
```

Here $`\operatorname{Tr}`$ denotes the trace, and $`U^\dagger`$ is the adjoint of $`U`$.

This repository defines $`T_k`$ to move the input at $`i`$ to output $`i+k`$. Therefore

```math
T_k^\dagger O_jT_k=O_{j-k}.
```

Data moving right and observables moving left describe the same operation. In the review's notation, the one-step observable shift $`s`$ corresponds to this $`k=1`$ convention. Keep that distinction when comparing signs of flow.

A layer of nearest-neighbor gates enlarges an observable's support by at most one site. After $`D`$ layers, an output can depend only on input sites at distance at most $`D`$. Thus translating unknown data by $`k`$ sites requires $`D\ge k`$ in the chosen range $`1\le k\le\lfloor n/2\rfloor`$. The [constant-error proof](../science/approximate_capacity.md#a-light-cone-bound-at-constant-error) obtains the same conclusion below diamond error one.

This propagation argument says how far information can travel. The rest of the project asks how much simultaneous directed transport the available work can accommodate.

## 2. Specify what must return

Three types of register have different roles:

| Register | Initial information | Required final behavior |
|---|---|---|
| Data $`S`$ | Arbitrary unknown state | Translate by $`T_k`$. |
| Initialized work $`A`$ | A fixed state $`\sigma_A`$ independent of the input | Restore that complete physical state and decouple it from the output data and borrowed work. |
| Borrowed work $`B`$ | Arbitrary unknown state, possibly correlated with a reference | Apply the identity channel, preserving all those correlations. |

The exact promise is a statement about every input $`\rho_{SBR}`$, where $`R`$ is an untouched reference:

```math
W(\rho_{SBR}\otimes\sigma_A)W^\dagger
=
\bigl[(T_k\otimes I_{BR})\rho_{SBR}
(T_k^\dagger\otimes I_{BR})\bigr]\otimes\sigma_A.
```

Identity operators on untouched systems are implicit on the left. A reference makes the promise sensitive to the preservation of quantum correlations, rather than just the appearance of each local output.

A mixed initialized state need not be returned together with an inaccessible purification. For example, permuting identical maximally mixed ancillary registers restores their physical state but can change which register is correlated with a purifying system. Arbitrary borrowed registers do not allow that change. The [model](../science/model.md#translation-and-the-two-return-contracts) fixes this boundary, and the [purification argument](../science/interpretation.md#why-a-mixed-catalysts-purification-matters) explains its consequences.

## 3. A complete sparse counterflow example

Take eight data qubits at sites $`0,\ldots,7`$. Put one initialized qubit $`A_0`$ at site $`0`$ and one $`A_1`$ at site $`4`$. A SWAP exchanges the complete quantum states of its two registers. It performs the corresponding wire permutation even when the inputs are entangled with other systems.

The following schedule moves the data one site right. Each row is one layer; its two SWAPs act on disjoint registers.

| Layer | First SWAP | Second SWAP |
|---|---|---|
| 1 | $`S_0\leftrightarrow A_0`$ | $`S_4\leftrightarrow A_1`$ |
| 2 | $`S_3\leftrightarrow S_4`$ | $`S_7\leftrightarrow S_0`$ |
| 3 | $`S_2\leftrightarrow S_3`$ | $`S_6\leftrightarrow S_7`$ |
| 4 | $`S_1\leftrightarrow S_2`$ | $`S_5\leftrightarrow S_6`$ |
| 5 | $`A_0\leftrightarrow S_1`$ | $`A_1\leftrightarrow S_5`$ |

The edge between sites $`7`$ and $`0`$ is local because the geometry is a ring. On-site SWAPs in the first layer also count toward depth.

To track the action, give the input wires distinct labels $`s_0,\ldots,s_7,a_0,a_1`$. These labels identify where information originated; they do not assume a classical product input. The final labels are

```math
\begin{aligned}
(S_0,S_1,\ldots,S_7)_{\rm out}
&=(s_7,s_0,s_1,s_2,s_3,s_4,s_5,s_6),\\
(A_0,A_1)_{\rm out}&=(a_1,a_0).
\end{aligned}
```

Thus the circuit has depth five and ten SWAPs. Its ancillary action is an exchange. It returns $`|00\rangle`$, and more generally returns $`\tau\otimes\tau`$ for any one-qubit density operator $`\tau`$. It would not restore two arbitrary different borrowed inputs.

The general [counterflow construction](../science/constructions.md#one-step-with-arbitrary-anchors) partitions the data into segments between initialized anchors. With largest anchor spacing $`g`$ and $`a`$ active anchors, one step uses depth $`g+1`$ and $`n+a`$ SWAPs:

```math
W_{\rm cf}=T_{1,S}\otimes C_A^{-1}\otimes I_B.
```

The permutation $`C_A`$ advances the ancillary anchor labels by one. Repeating the circuit $`k`$ times returns any state invariant under $`C_A^k`$. A product-pure choice supplies the matching upper bound without nonlocal preparation.

## 4. The index gives context; capacity requires a finite argument

The one-dimensional QCA index distinguishes a shift from a circuit on an infinite chain. In the multiplicative convention, a finite-depth circuit has index one; the observable shift above has index $`d`$ for $`d`$-level data. Its inverse has index $`1/d`$. The primary result is attributed to [Gross, Nesme, Vogts, and Werner](../references/RELATED_WORK.md#gnvw2012).

Taking the logarithm defines an additive convention,

```math
\nu(\alpha)=\log_2\operatorname{ind}(\alpha).
```

Products of indices become sums. A circuit then has $`\nu=0`$, and a $`k`$-step shift has $`\nu=k\log_2d`$ in this orientation. Replacing an automorphism by its inverse reverses that sign. The [placement proof](../science/placement.md#the-index-stability-input) only needs the distinction between zero and nonzero index.

For paired opposite shifts, the two factors cancel. The inverse-copy construction is established background, as is using an invariant ancillary state as a catalyst; see the [attribution](../references/RELATED_WORK.md#attribution-of-the-proof-ingredients). The capacity question asks what remains possible when only a limited amount of initialized work is available.

There is a geometric reason to handle the finite ring carefully. Every finite-ring unitary can be synthesized by a sufficiently deep circuit, so an infinite-chain index obstruction cannot simply be assigned to every finite-ring circuit. The capacity proofs work directly with finite-dimensional states. The separate gap proof lifts the actual circuit to an infinite chain only inside a causal neighborhood that does not wrap around the ring.

## 5. Entropy turns a returned state into a capacity bound

For a density operator with eigenvalues $`\lambda_j`$, the entropy in bits is

```math
S(\rho)=-\sum_j\lambda_j\log_2\lambda_j.
```

A pure state has entropy zero. A completely mixed state on a register of dimension $`r`$ has $`r`$ equal eigenvalues $`1/r`$ and entropy $`\log_2r`$. A unitary preserves the entropy of the entire system on which it acts, while the entropy of one part can change through exchange and correlation with the other part.

The [exact proof](../science/exact_capacity.md) exploits that difference. Choose a test input that is pure on one arc and completely mixed on its complement. Give borrowed registers the same spatial profile. The target data shift changes the entropy of a half-ring by exactly $`k\log_2d`$ in magnitude. Borrowed work returns unchanged, and the initialized state returns exactly, so neither contributes to that target entropy difference.

Only gates crossing the two boundaries can change the half-ring entropy. At depth $`D`$, the [cut factorization](../science/exact_capacity.md#cut-factorization) gathers their effect into two patches, each of width $`2D`$. For this witness, a patch containing initialized space of dimension $`K`$ can lower the relevant entropy by at most $`3\log_2K`$, even when that initialized space is correlated with distant initialized registers.

This local estimate is the step that charges capacity. It uses entropy inequalities and bounds on mutual information; the complete argument is in the [patch lemma](../science/exact_capacity.md#entropy-capacity-of-an-initialized-patch). It does not charge the dimension of borrowed work.

Define total initialized capacity by

```math
M=\sum_i\log_2\dim A_i.
```

For initialized qubits, $`M=m`$. Translate the test input and its two cuts through every position. Each initialized bit is counted $`4D`$ times across the two families of patches. When $`D,k\le\lfloor n/4\rfloor`$, summing the local estimates gives

```math
nk\log_2d\le12DM.
```

The pure/mixed witness originates in [Yin, Lucas, and Stephen](../references/RELATED_WORK.md#yls2024). The additional initialized-capacity accounting, including arbitrary borrowed dimensions and arbitrary fixed catalyst correlations, is the finite argument developed here.

## 6. A rank comparison preserves the obstruction at nonzero error

The approximate theorem assumes product-pure initialized work. It compares two channels with output $`SBA`$: the implemented output and the ideal translation with the initialized work returned. Their unhalved diamond distance $`\epsilon`$ controls the trace distance of every output, including inputs correlated with a reference. Perfectly distinguishable output states have trace distance two.

The local spectral argument below assumes $`1\le D,k\le\lfloor n/4\rfloor`$, so the two boundary patches are disjoint. Its window condition is asserted within that regime.

The [spectral proof](../science/approximate_capacity.md) chooses a pure/mixed **target** profile and shifts it backward to define the data input. After removing the two boundary unitaries, the actual left output has a flat spectrum on a subspace of rank $`r`$. The ideal left rank before that boundary correction is $`r\,2^k`$. Arbitrary mixed borrowed dimensions enter both sides through the same $`r`$.

Let $`b_x`$ be the number of initialized qubits in the backward $`D`$-site interval ending at cut $`x`$. The corrected ideal state's largest eigenvalue is at most

```math
\frac{2^{b_x}}{r\,2^k}.
```

A measurement projecting onto the actual rank-$`r`$ support accepts the actual state with probability one. It accepts the corrected ideal state with probability at most $`2^{b_x-k}`$. Therefore

```math
\epsilon\ge2\bigl(1-2^{b_x-k}\bigr).
```

If $`b_x\le k-1`$, this forces $`\epsilon\ge1`$. Consequently, for $`\epsilon<1`$ every such window contains at least $`k`$ initialized qubits. Each qubit lies in exactly $`D`$ translated windows, giving $`Dm\ge nk`$.

Flatness and factorization are essential here. This proof does not establish the same error bound for arbitrary mixed or entangled catalysts. The exact arbitrary-state theorem and the approximate product-pure theorem have different scopes.

## 7. Assemble the depth frontier and keep placement visible

The two capacity arguments apply when the circuit is shallow enough for the cut patches to fit. If that condition fails, $`D>\!n/4`$ already supplies a linear lower bound. Combining these alternatives with $`D\ge k`$ gives the lower side of the [uniform theorem](../science/model.md#the-attained-frontier).

Now specialize to qubit data and $`m`$ initialized qubits. For the upper side with $`m\ge1`$, distribute $`a=\min(m,n)`$ anchors evenly. Their largest spacing is $`\lceil n/a\rceil`$. Repeat counterflow $`k`$ times, or use the separate ancilla-free path rotation of depth $`n-1`$, whichever is shallower. The latter also covers $`m=0`$. The resulting scale is

```math
F(n,k,m)=
\min\!\left\{n,\;
k\max\!\left(1,\frac{n}{m+1}\right)\right\}.
```

The exact optimum lies between $`F/12`$ and $`6F`$. With product-pure work and joint diamond error below one, it lies between $`F/4`$ and $`6F`$. These constants are safe bounds, not sharp minimum depths.

When $`n=L^2`$ and $`k=m=L`$, propagation distance and balanced anchor spacing are both of order $`L`$. Nevertheless, the capacity bound forces depth of order $`L^2`$. Simultaneous transport, rather than travel distance alone, determines this regime.

Total capacity does not specify placement. The [gap theorem](../science/placement.md#gap-theorem) treats arbitrary initialized states without requiring their return. If a $`4D`$-site causal neighborhood contains no initialized register and $`4D<n`$, the circuit can be lifted locally to an infinite chain. A primary local-stability theorem of [Ranard, Walter, and Witteveen](../references/RELATED_WORK.md#rww2022) then contradicts the shift's nonzero index at reduced-channel diamond error at most $`1/192`$. This gives $`D\ge\lceil g/4\rceil`$ for largest anchor spacing $`g`$.

The optimized frontier, the arbitrary-state gap theorem, and the product-pure local capacity law address different resource questions. Their hypotheses remain visible in the [interpretation](../science/interpretation.md). The [verification programs](../verification/README.md) check explicit finite schedules and geometry; the analytical proofs establish the general claims.
