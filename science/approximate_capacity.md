# Capacity at nonzero implementation error

For product-pure initialized work, the space–depth obstruction survives a fixed error in the complete output channel. In the qubit model, every short interval through which the circuit must carry a translation of $`k`$ sites contains at least $`k`$ initialized qubits. Consequently, in the regime where two cut neighborhoods fit on the ring, depth $`D`$ and total initialized capacity $`M`$ obey $`DM\ge nk`$.

The proof tracks the rank of a deliberately chosen input state and the largest eigenvalue of the ideal state after removing two local cut unitaries. Arbitrary borrowed register dimensions cancel from the comparison. The pure/mixed domain-wall witness and the zero-workspace spectral obstruction originate in [YLS2024](../references/RELATED_WORK.md#yls2024), especially Lemma 2.5. The local initialized-capacity factor is the additional ingredient here.

## Channel and return condition

There are $`n\ge2`$ sites on a ring, indexed by $`\mathbb Z_n`$. Site $`i`$ contains a data qubit $`S_i`$, an arbitrary finite-dimensional borrowed register $`B_i`$, and $`m_i\in\mathbb Z_{\ge0}`$ initialized qubits $`A_i`$. Set

```math
S=\bigotimes_i S_i,\qquad
B=\bigotimes_i B_i,\qquad
A=\bigotimes_i A_i,\qquad
M=\sum_{i\in\mathbb Z_n}m_i.
```

Initialized work begins in a product of pure states over sites. Local basis choices write this state as $`\eta_A=|0\rangle\langle0|_A`$. The input on $`SB`$ is arbitrary and independent of $`A`$; it can be entangled with an external reference. Let $`W`$ be a depth-$`D`$ circuit of unitary gates within a site or between neighboring sites, with disjoint registers in each layer. The implemented and ideal channels, both with output $`SBA`$, are

```math
\begin{aligned}
\mathcal F(\rho_{SB})
  &=W(\rho_{SB}\otimes\eta_A)W^\dagger,\\
\mathcal G_k(\rho_{SB})
  &=(T^k\otimes I_B)\rho_{SB}(T^{-k}\otimes I_B)
       \otimes\eta_A.
\end{aligned}
```

Here $`T`$ translates data one site to the right. Assume the **full joint-return error** satisfies

```math
\|\mathcal F-\mathcal G_k\|_\diamond\le\epsilon<1.
\tag{1}
```

The diamond norm and trace norm are unhalved: perfectly distinguishable states have trace distance two. Condition (1) includes the state of the returned initialized work and all output correlations. It also protects borrowed work together with any reference system.

If the output initialized marginal is returned exactly to the pure state $`\eta_A`$ for every input, a diamond bound on the reduced $`SB`$ channel is enough: a pure marginal forces the entire output to factor with $`\eta_A`$. Approximate marginal return by itself is not the hypothesis of this theorem.

The corresponding exact theorem allows an arbitrary fixed, possibly mixed and spatially entangled initialized state; see [exact capacity](exact_capacity.md). In that model, return of a fixed mixed state means return of its complete physical state on $`A`$. It does not promise preservation of an arbitrary external purification of that state. Borrowed work has the stronger identity-channel promise. The product-pure setting in this section has no mixed-state purification ambiguity.

## A light-cone bound at constant error

**Lemma.** For $`1\le k\le\lfloor n/2\rfloor`$, condition (1) implies $`D\ge k`$. The same conclusion holds for any fixed initialized state, even without a return promise, whenever the reduced data/borrowed channel has diamond error less than one.

**Proof.** Suppose $`D<k`$. Choose an output data site $`j`$ and change only input data site $`j-k`$ between two orthogonal pure states. Fix every other input register. Since the graph distance between these sites is $`k`$, the backward light cone of $`S_j`$ excludes $`S_{j-k}`$. The implemented output marginal on $`S_j`$ is therefore the same state $`\omega`$ for both inputs. This remains true if the initialized registers are entangled among themselves: their state is fixed independently of the changed data input.

The two ideal output marginals on $`S_j`$ are orthogonal states $`\phi_0`$ and $`\phi_1`$. Contractivity under taking a marginal, followed by the triangle inequality, gives

```math
2=\|\phi_0-\phi_1\|_1
\le\|\phi_0-\omega\|_1+\|\omega-\phi_1\|_1
\le2\epsilon<2,
```

a contradiction. No assumption on the dimensions or the return of borrowed work is needed for this particular bound. $`\square`$

## Local capacity theorem

Write

```math
q=\lfloor n/4\rfloor,\qquad \ell=\lfloor n/2\rfloor.
```

Intervals below are half-open cyclic intervals of integer sites; for example, $`[x-D,x)`$ contains exactly $`D`$ sites.

**Theorem.** Let $`n\ge4`$, $`1\le k\le q`$, and $`1\le D\le q`$. Under condition (1), every cut $`x`$ obeys

```math
\sum_{i\in[x-D,x)}m_i\ge k.
\tag{2}
```

In particular,

```math
DM\ge nk.
\tag{3}
```

Equality $`D=q`$ is allowed, including when $`4D=n`$.

### Two cut neighborhoods

Fix a cut $`x`$ and put $`y=x+\ell`$. Let $`L=[x,y)`$ and let $`R`$ be its complement. The [cut-factorization lemma](exact_capacity.md#cut-factorization) gives

```math
W=V_xV_y(W_L\otimes W_R),
\tag{4}
```

where $`V_c`$ is supported in

```math
P_c=[c-D,c+D),\qquad c\in\{x,y\}.
```

These supports are disjoint because $`2D\le\ell`$ and $`2D\le n-\ell`$. At equality their half-open intervals meet without sharing a site. Equation (4) is the output-side factorization; the similarly named input-side cut unitaries are not being interchanged with it.

### A target profile and its input rank

Choose the target state on data and borrowed registers to be completely mixed at sites in

```math
J_x=[x-q,x+\ell-q)
```

and pure product at the remaining sites. Data and borrowed registers are independent of each other and of $`\eta_A`$. This is an allowed test state because the channel promise is uniform over every borrowed input.

Define the **input** data state by translating the target data profile by $`-k`$. The input borrowed state is the target borrowed state, since the target borrowed operation is identity. Denote this product input on $`SBA`$ by $`\rho_{\mathrm{in}}`$ and its ideal output by $`\rho_{\mathrm{tar}}`$.

There are $`\ell-q`$ mixed target data qubits in $`L`$ and $`\ell-q-k`$ mixed input data qubits in $`L`$. The shifted arc does not enter the other end of $`L`$ because $`k\le q`$. Both counts are valid for every $`n`$, without a divisibility assumption.

The input left marginal is a normalized projector of some rank $`r`$. The target left marginal is a normalized projector of rank

```math
r\,2^k.
\tag{5}
```

The factor $`r`$ includes the dimensions of all mixed borrowed registers in $`L`$. These dimensions need not be equal at different sites.

Only the **target** profile must be homogeneous in the cut neighborhoods. For $`D\le q`$, the patch $`P_x`$ lies entirely in $`J_x`$ and the patch $`P_y`$ lies entirely in its complement. The input domain walls may be closer to a cut; the proof uses only their contribution to the flat input spectrum.

### Remove the cut unitaries

Conjugate the actual and target outputs by $`V_x^\dagger V_y^\dagger`$, then take their left marginals. Write the resulting states as $`\widehat\rho_L`$ and $`\widehat\sigma_L`$, respectively. Equation (4) implies

```math
\widehat\rho_L=W_L\rho_{\mathrm{in},L}W_L^\dagger.
```

Thus $`\widehat\rho_L`$ is supported on a projector $`P`$ of rank $`r`$, and $`\mathrm{Tr}(P\widehat\rho_L)=1`$.

The target is a tensor product over sites. The two cut patches are disjoint, so their conjugated target states and all outside target factors remain independent. The pure patch $`P_y`$ starts in a pure product state on data, borrowed work, and initialized work. Its reduced left state after $`V_y^\dagger`$ has operator norm at most one.

On the mixed patch $`P_x`$, write $`Q=Q_LQ_R`$ for data plus borrowed registers and $`K=K_LK_R`$ for initialized registers. This patch begins in

```math
\frac{I_Q}{\dim Q}\otimes|0\rangle\langle0|_K,
```

whose operator norm is $`1/\dim Q`$. Unitary conjugation preserves this norm. For a positive operator $`H`$, the inequality $`H\le\|H\|_\infty I`$ implies $`\mathrm{Tr}_YH\le(\dim Y)\|H\|_\infty I`$. Applying it to the right part of the patch yields

```math
\left\|
\mathrm{Tr}_{Q_RK_R}
\left[
V_x^\dagger
\left(\frac{I_Q}{\dim Q}\otimes|0\rangle\langle0|_K\right)
V_x
\right]
\right\|_\infty
\le \frac{\dim K_R}{\dim Q_L}.
\tag{6}
```

Multiplying the operator norms of the independent factors, and using the target rank (5), gives

```math
\|\widehat\sigma_L\|_\infty
\le\frac{\dim K_R}{r\,2^k}.
\tag{7}
```

Here $`K_R`$ consists precisely of the initialized qubits at the $`D`$ sites $`[x-D,x)`$.

### A two-outcome distinguishing measurement

The target weight in the rank-$`r`$ subspace is bounded by

```math
\mathrm{Tr}(P\widehat\sigma_L)
\le r\|\widehat\sigma_L\|_\infty
\le\frac{\dim K_R}{2^k}.
```

The binary measurement $`\{P,I-P\}`$ therefore gives

```math
\begin{aligned}
\epsilon
&\ge\|\widehat\rho_L-\widehat\sigma_L\|_1\\
&\ge2\left[1-\frac{\dim K_R}{2^k}\right].
\end{aligned}
\tag{8}
```

The first inequality follows from (1), invariance under the same unitary conjugation, and contractivity under taking the left marginal. The lower bound remains valid when its right side is negative.

Let $`b_x=\sum_{i\in[x-D,x)}m_i`$, so $`\dim K_R=2^{b_x}`$. If $`b_x\le k-1`$, equation (8) implies $`\epsilon\ge1`$. Since $`b_x`$ is an integer and $`\epsilon<1`$, it follows that $`b_x\ge k`$. This proves (2).

Sum (2) over all $`n`$ cuts. Each initialized qubit belongs to exactly $`D`$ of the windows $`[x-D,x)`$, so the left side sums to $`DM`$. This proves (3). $`\square`$

## General local dimensions

For $`d`$-level data and arbitrary finite initialized dimensions $`a_i=\dim A_i`$, the same proof gives

```math
\prod_{i\in[x-D,x)}a_i
\ge(1-\epsilon/2)d^k.
\tag{9}
```

Writing $`M=\sum_i\log_2a_i`$ and summing logarithms gives

```math
DM\ge n\left[k\log_2d+\log_2(1-\epsilon/2)\right].
\tag{10}
```

No integer rounding of $`\log_2a_i`$ is assumed in (10). The stronger error-independent qubit bound (3) uses the specific dimensions $`a_i=2^{m_i}`$ and integer $`m_i`$.

## Consequences and scope

For qubits with $`1\le k\le q`$, the theorem can be stated without assuming short depth as

```math
D\ge\min\left\{q+1,\left\lceil\frac{nk}{M}\right\rceil\right\},
\tag{11}
```

where the second term is infinite when $`M=0`$. The independent light-cone bound $`D\ge k`$ applies for the full range $`1\le k\le\lfloor n/2\rfloor`$. When $`k>q`$ or $`n<4`$, that bound already gives the required linear-in-$`n`$ branch, up to an absolute constant.

The exact counterflow constructions use product-pure initialized work and achieve zero error, so they supply the upper bounds for this approximate model as well; see [constructions](constructions.md). Optimizing placement gives the same asymptotic space–depth frontier as in the exact model. Equation (2) also provides a placement-sensitive condition stronger than a bound on total capacity; see [placement](placement.md#local-capacity-for-product-pure-work).

The general fixed-error theorem here requires product-pure initialized work. A spatially entangled initialized state need not give a flat input left spectrum, and its target state need not factor between the two cut patches and their outside. Those properties are used in (5)–(7). Accordingly, (3) is not asserted here for an arbitrary mixed or entangled initialized state. The exact arbitrary-state capacity theorem and the dimension-independent small-error gap theorem have their separate hypotheses and proofs.
