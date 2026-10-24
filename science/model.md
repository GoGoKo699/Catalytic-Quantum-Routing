# Model and optimal depth

Consider unknown quantum data arranged on a ring. Translating every register by a short distance looks local, but a circuit must also accommodate the information displaced along the entire ring. Initialized workspace can provide the opposite flow while being returned for reuse. The question is how much workspace, and how much spatial access to it, are needed.

The distinction between a specified ancillary state and an arbitrary borrowed state is part of the task. The underlying obstruction to a shallow shift and the dense opposite-shift construction are established results; [the source comparison](../references/RELATED_WORK.md) identifies those ingredients.

## Registers, geometry, and circuit layers

There are $`n\ge 2`$ sites labeled by $`\mathbb Z_n`$. Site $`i`$ carries:

- a data register $`S_i\simeq\mathbb C^d`$, with the same dimension $`d\ge2`$ at every site;
- initialized work $`A_i`$, which may have dimension one;
- arbitrary finite-dimensional borrowed work $`B_i`$, which may also be absent.

Write $`S=\bigotimes_i S_i`$, $`A=\bigotimes_i A_i`$, and $`B=\bigotimes_i B_i`$. The initialized capacity is

```math
M=\sum_{i=0}^{n-1}\log_2\dim A_i.
```

For qubit workspace, $`A_i`$ consists of $`m_i`$ qubits and $`M=m=\sum_i m_i`$. Several initialized qubits may occupy one site. The number of occupied sites and the total capacity are different quantities.

A depth-$`D`$ circuit is a product of $`D`$ layers of unitary gates. Every gate is supported within one site or two neighboring sites, and gates in a layer act on disjoint registers. There are no measurements, resets during the circuit, instantaneous distant gates, or classical feedforward. On-site gates count toward depth. No restriction to Clifford gates or SWAP gates is imposed on the lower bounds.

The lower-bound proofs also permit arbitrary gates on the full registers of one or two adjacent sites, provided each layer has propagation radius at most one. The upper constructions use only two-qubit SWAP gates. A stricter convention allowing only disjoint *sites* per layer changes the constructions by at most a constant coloring factor; the displayed finite constants refer to the disjoint-register convention.

The initialized state $`\sigma_A`$ is fixed independently of the input and can be chosen as part of the implementation. It can be spatially entangled or mixed unless a theorem explicitly requires a product-pure state. Supplying such states enlarges the class against which the converse is proved. The matching upper bound needs only an on-site product state, whose preparation adds at most constant depth.

## Translation and the two return contracts

Let $`T_k`$ move the contents of data site $`i`$ to site $`i+k`$ modulo $`n`$. Equivalently,

```math
T_k|s_0,s_1,\ldots,s_{n-1}\rangle
=|s_{-k},s_{1-k},\ldots,s_{n-1-k}\rangle .
```

Throughout the frontier theorem,

```math
1\le k\le \lfloor n/2\rfloor .
```

Opposite shifts have the same depth by reversing the ring's orientation. The identity cases $`k=0`$ and $`k=n`$ are excluded.

An exact implementation satisfies, for every state $`\rho_{SBR}`$ and arbitrary reference system $`R`$,

```math
\begin{aligned}
&(W_{SBA}\otimes I_R)(\rho_{SBR}\otimes\sigma_A)
(W_{SBA}^{\dagger}\otimes I_R)\\
&\qquad =
(T_k\otimes I_{BR})\rho_{SBR}
(T_k^\dagger\otimes I_{BR})\otimes\sigma_A .
\end{aligned}
\tag{1}
```

Thus the data operation is correct on every input, borrowed work is restored through the identity channel, and initialized work is returned uncorrelated with the data and borrowed work.

The contracts on $`A`$ and $`B`$ are deliberately different. A mixed initialized catalyst is restored as the complete *physical state* $`\sigma_A`$, including its correlations among sites. Equation (1) does not require the preservation of a purification of $`\sigma_A`$ held in an inaccessible external system. Borrowed work must preserve arbitrary reference correlations. The [interpretation](interpretation.md) explains why identifying these contracts would change the problem.

Requiring the reduced $`SB`$ channel to be exactly unitary and requiring the ancillary marginal to return is equivalent to (1). An extension of a unitary channel has a constant ancillary output, so the ancillary output decouples. The [exact converse](exact_capacity.md) states this step explicitly.

## Approximation includes return of the work

For product-pure initialized work, local basis choices let us write its state as $`|0\rangle\langle0|_A`$. Define channels with input $`SB`$ and output $`SBA`$:

```math
\begin{aligned}
\mathcal F_W(\rho)
&=W(\rho\otimes|0\rangle\langle0|_A)W^\dagger,\\
\mathcal G_k(\rho)
&=(T_k\otimes I_B)\rho(T_k^\dagger\otimes I_B)
\otimes|0\rangle\langle0|_A.
\end{aligned}
```

The approximate return condition is

```math
\|\mathcal F_W-\mathcal G_k\|_\diamond\le\epsilon.
\tag{2}
```

The diamond norm here has no factor $`1/2`$; its largest distance between channels is two. The constant-error theorem holds for every $`0\le\epsilon<1`$. It controls restoration and residual correlations as well as the data operation. If work is returned exactly pure, the output necessarily factors and a reduced-channel error bound suffices. Approximate marginal return by itself is not substituted for (2).

## The attained frontier

For qubit data and $`m`$ initialized qubits, define

```math
F(n,k,m)=
\min\!\left\{n,\,
k\max\!\left(1,\frac{n}{m+1}\right)\right\}.
\tag{3}
```

Let $`D_{\rm ex}^{*}(n,k,m)`$ be the minimum exact depth after optimizing the placement and fixed initial state of the initialized work and allowing arbitrary finite borrowed work. Let $`D_{\rm p}^{*}(n,k,m;\epsilon)`$ be the corresponding minimum with product-pure initialized work and the joint error condition (2).

**Theorem 1 (optimal depth with reusable workspace).** For every $`n\ge2`$, $`m\ge0`$, and $`1\le k\le\lfloor n/2\rfloor`$,

```math
\frac1{12}F(n,k,m)
\le D_{\rm ex}^{*}(n,k,m)
\le 6F(n,k,m).
\tag{4}
```

For every $`0\le\epsilon<1`$,

```math
\frac14F(n,k,m)
\le D_{\rm p}^{*}(n,k,m;\epsilon)
\le 6F(n,k,m).
\tag{5}
```

The constants are explicit safe bounds, not optimal finite-size constants. Both minima have the same asymptotic scaling. Entanglement and mixedness of the initialized catalyst, as well as arbitrarily large borrowed work, cannot improve the exact scaling.

### Proof from the capacity bounds

Set $`q=\lfloor n/4\rfloor`$. Strict circuit locality gives $`D\ge k`$ for an exact implementation. It also gives this bound under (2) when $`\epsilon<1`$: if $`D<k`$, two orthogonal inputs at one site produce the same reduced output at their target site, whereas the ideal outputs are orthogonal. The triangle inequality then requires $`\epsilon\ge1`$.

If $`D\ge q+1`$, then $`D>n/4\ge F/4`$. Otherwise $`D\le q`$, so $`k\le q`$ by the propagation bound. The [exact capacity theorem](exact_capacity.md) gives

```math
12Dm\ge nk,
\tag{6}
```

and the [product-pure finite-error theorem](approximate_capacity.md) gives

```math
Dm\ge nk.
\tag{7}
```

If $`m=0`$, either inequality excludes this shallow branch. If $`m>0`$, use $`F\le nk/m`$ when $`m<n`$; for $`m\ge n-1`$, the direct bound $`D\ge k=F`$ already suffices. These observations prove the lower bounds in (4) and (5), including the small rings with $`q=0`$.

The [constructions](constructions.md) give, with $`a=\min(m,n)`$,

```math
D\le
\begin{cases}
n-1,&m=0,\\[2mm]
\min\{n-1,\ k(\lceil n/a\rceil+1)\},&m\ge1.
\end{cases}
\tag{8}
```

They return the initialized work exactly. For $`1\le m<n`$, the elementary bounds $`\lceil n/m\rceil+1\le n/m+2`$ and $`m+1\le2m`$ give (8) $`\le6F`$. For $`m\ge n`$, the bound $`2k`$ suffices. This proves both upper bounds.

## Capacity and placement are separate

Equation (3) optimizes placement. A fixed clustered placement can have much larger depth. In the product-pure error model, every one-sided $`D`$-site interval must contain at least $`k`$ initialized qubits whenever $`D\le q`$ and $`k\le q`$. This local statement is stronger than its sum $`Dm\ge nk`$.

For a one-site shift, a different [placement theorem](placement.md) gives an obstruction proportional to the largest gap between initialized sites. It allows arbitrary correlated initialized states, does not require their return, and remains valid at a fixed diamond error. Its proof uses local stability of the QCA index.

The total-capacity theorem, the local pure-work capacity requirement, and the arbitrary-state gap theorem have different hypotheses. None is used outside its stated domain.

## Proof map

| Claim | Authoritative argument |
|---|---|
| Exact capacity against arbitrary mixed and entangled catalysts | [Circuit factorization and entropy capacity](exact_capacity.md) |
| Constant-error capacity for product-pure work | [Rank and spectrum obstruction](approximate_capacity.md) |
| Matching circuits and charged SWAP counts | [Routing constructions](constructions.md) |
| Fixed-placement obstruction with arbitrary initialized states | [Spatial placement and index](placement.md) |
| Operational meaning, examples, and boundary cases | [Interpretation](interpretation.md) |

The finite verification checks the explicit schedules and algebraic examples. The universal lower bounds are established by these analytical arguments and the cited index theorem.
