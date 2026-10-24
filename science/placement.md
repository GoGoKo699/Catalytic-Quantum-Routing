# Spatial placement of initialized work

Total initialized capacity and its locations impose different constraints. A large initialized register at one site does not remove a long interval with no initialized registers. Conversely, for product-pure work, a translation of $`k`$ sites requires sufficient capacity in every short window, even when there are no large empty gaps.

This section gives a dimension-independent gap bound for arbitrary fixed initialized states and a sharper local capacity condition for product-pure states. The gap bound does not require initialized work to return.

## Model and definitions

The ring has $`n\ge2`$ sites. At each site there is a $`d`$-level data register $`S_i`$, with $`d\ge2`$, an arbitrary finite-dimensional borrowed register $`B_i`$, and an initialized register $`A_i`$, possibly of dimension one. The initialized state $`\sigma_A`$ is fixed independently of the arbitrary input on $`SB`$. It may be mixed and entangled across its occupied sites.

A depth-$`D`$ circuit $`W`$ contains unitary gates within a site or between neighboring sites, with disjoint registers in each layer. After tracing out initialized work, its induced channel is

```math
\mathcal E(\rho_{SB})
=\operatorname{Tr}_A\!\left[
W(\rho_{SB}\otimes\sigma_A)W^\dagger
\right].
```

Let $`\mathcal T_k`$ denote translation of every data register by $`k`$ sites to the right and the identity channel on all borrowed registers. The gap theorem assumes

```math
\|\mathcal E-\mathcal T_k\|_\diamond\le\epsilon,
\qquad
\epsilon\le\frac1{192},
\qquad
1\le k\le\lfloor n/2\rfloor.
\tag{1}
```

This is a condition on the **complete data and borrowed channel**, including reference correlations. Returning each borrowed marginal separately is insufficient. There is no return requirement on $`A`$ in this theorem, and no product-state restriction on $`\sigma_A`$.

Write

```math
C=\{i\in\mathbb Z_n:\dim A_i>1\},\qquad a=|C|.
```

An initialized-work-free interval contains no sites of $`C`$. If $`a\ge1`$, order the occupied sites cyclically as $`b_1,\ldots,b_a`$, put $`b_{a+1}=b_1+n`$, and define their largest cyclic spacing by

```math
g(C)=\max_{1\le j\le a}(b_{j+1}-b_j).
```

There are $`g(C)-1`$ empty sites in the largest gap. For $`C=\varnothing`$, define $`g(C)=n`$.

## Gap theorem

**Theorem.** Under (1),

```math
D\ge k,
\qquad
D\ge\left\lceil\frac{g(C)}4\right\rceil.
\tag{2}
```

More locally, if $`4D<n`$, there cannot be an initialized-work-free interval of $`4D`$ consecutive sites.

The lower bound is independent of every initialized and borrowed local dimension. In particular, arbitrarily large borrowed registers and arbitrarily large initialized registers outside the empty interval do not change it.

### The index stability input

The GNVW index is an invariant of one-dimensional locality-preserving automorphisms. In its logarithmic convention, a finite-depth circuit has index zero and translation of a $`d`$-dimensional factor by $`k`$ sites has index of magnitude $`k\log d`$. Tensoring stationary factors and blocking physical sites do not change this conclusion; see [GNVW2012](../references/RELATED_WORK.md#gnvw2012) and [RWW2022](../references/RELATED_WORK.md#rww2022), Theorem 4.4.

The quantitative input is Proposition 4.10 of [RWW2022](../references/RELATED_WORK.md#rww2022): two nearest-neighbor quantum cellular automata on the same quasi-local algebra have equal index if their operator-map norm difference on a pair of adjacent blocked sites, with the block origin chosen as in that proposition, is at most $`1/192`$. The threshold does not depend on local dimensions. The proof below supplies this operator-map condition from a finite-ring channel promise; it does not assign an index directly to a finite-ring unitary.

### 1. Select a causal neighborhood without initialized work

The [constant-error light-cone lemma](approximate_capacity.md#a-light-cone-bound-at-constant-error) applies to (1), so $`D\ge k\ge1`$.

Suppose, for contradiction, that $`4D<n`$ and an empty interval of $`4D`$ sites exists. Label those sites by integer representatives

```math
I=[u,u+4D),
\qquad
X=[u+D,u+3D).
```

Thus $`X`$ contains two adjacent blocks of $`D`$ sites, and its radius-$`D`$ neighborhood is contained in $`I`$. Since $`4D<n`$, these representatives are injective on the ring. There is at least one site outside this causal neighborhood, providing an explicit seam for the infinite-chain lifting below.

For every operator $`O`$ supported on the full data and borrowed algebra of $`X`$, strict circuit locality gives

```math
W^\dagger(O\otimes I_A)W=K_{SB}\otimes I_A,
\tag{3}
```

where $`K_{SB}`$ is supported in $`I`$. No initialized register occurs in that support. Multiple disjoint-register gates at one physical site do not enlarge the propagation radius beyond one site per layer.

### 2. Remove the initialized-state expectation

The adjoint of the reduced channel is

```math
\mathcal E^\dagger(O)
=\operatorname{Tr}_A\!\left[
(I_{SB}\otimes\sigma_A)
W^\dagger(O\otimes I_A)W
\right].
```

Substituting (3) gives $`\mathcal E^\dagger(O)=K_{SB}`$ exactly. The initial state may have arbitrary correlations among its initialized sites: only its normalization is used, because the Heisenberg operator is identity on all of $`A`$.

Diamond norm dominates the induced trace norm. Duality between induced trace norm and induced operator norm consequently implies

```math
\|\mathcal E^\dagger-\mathcal T_k^\dagger\|_{\infty\to\infty}
\le\epsilon.
```

After restricting to the operator algebra on $`X`$ and embedding outputs with identity on initialized registers, this becomes

```math
\left\|
\left[
\operatorname{Ad}_{W^\dagger}
-\operatorname{Ad}_{T^{-k}\otimes I_B\otimes I_A}
\right](O)
\right\|_\infty
\le\epsilon\|O\|_\infty.
\tag{4}
```

Here $`\operatorname{Ad}_U(O)=UOU^\dagger`$. No square-root loss or dimension factor enters (4). This is why arbitrarily large borrowed registers are permitted.

### 3. Lift the actual circuit to an infinite chain

Choose a seam outside $`I`$, write the ring as one period of $`n`$ sites, and repeat both its local register dimensions and its actual gate schedule periodically on $`\mathbb Z`$. Gates across the ring seam lift to nearest-neighbor gates across successive periods. Every layer remains disjoint on registers. The resulting infinite-chain automorphism $`\alpha`$ is a depth-$`D`$ circuit automorphism of radius at most $`D`$.

The local dimensions of the infinite chain are uniformly bounded because they repeat a finite list, even though that bound may depend on the original finite instance. No uniform bound independent of the borrowed workspace is used by the index stability statement.

Define $`\beta`$ on this same infinite-chain algebra by shifting only the uniform $`d`$-dimensional data factor by $`k`$ sites and fixing every borrowed and initialized factor. Its radius is $`k\le D`$. The choice of Heisenberg orientation fixes the sign of its logarithmic index; its magnitude is $`k\log d>0`$.

The backward causal neighborhoods of operators on $`X`$ lie in the injective interval $`I`$. Their finite-ring and infinite-chain images therefore agree under the natural tensor-factor identification. This assertion uses the actual periodically lifted gates, rather than an independently chosen infinite-chain completion. The ideal shift images agree as well. Tensoring identity factors preserves operator norm, so (4) is precisely

```math
\| (\alpha-\beta)|_{\mathcal A_X}\|\le\epsilon.
\tag{5}
```

### 4. Block and compare indices

Block the infinite chain into intervals of $`D`$ physical sites, starting at the left endpoint of $`X`$. The region $`X`$ is now a pair of adjacent blocked sites; label them $`0,1`$. Both $`\alpha`$ and $`\beta`$ are nearest-neighbor QCAs on the same blocked algebra. Equation (5) and $`\epsilon\le1/192`$ meet Proposition 4.10 of [RWW2022](../references/RELATED_WORK.md#rww2022).

That proposition gives equal indices. But $`\alpha`$ has index zero because it is finite depth, whereas $`\beta`$ has nonzero index. This is the contradiction.

The condition $`4D<n`$ was needed only to make the chosen causal neighborhood injective and leave a seam. The proof claims no contradiction from a neighborhood that covers or overlaps itself around the entire ring.

### 5. Convert the local obstruction into a spacing bound

If $`C\ne\varnothing`$ and $`g(C)>4D`$, the largest empty gap contains $`g(C)-1\ge4D`$ sites. Also $`4D<g(C)\le n`$. The local contradiction applies, so $`g(C)\le4D`$.

If $`C=\varnothing`$ and $`D<n/4`$, any $`4D`$ consecutive sites give the same contradiction. Thus $`D\ge\lceil n/4\rceil`$. These two cases prove (2). $`\square`$

## Consequences for support density

For $`a\ge1`$ occupied sites, their cyclic spacings sum to $`n`$, hence

```math
g(C)\ge\left\lceil\frac na\right\rceil,
\qquad
D\ge\left\lceil\frac{g(C)}4\right\rceil
\ge\frac{n}{4a}.
```

The number $`a`$ counts occupied **sites**, not initialized qubits. Concentrating many initialized qubits at one site increases total capacity without reducing an empty gap. The gap law is therefore complementary to a bound in terms of total capacity.

For one-site translation and a chosen initialized qubit at each occupied site, the counterflow construction has depth at most $`g(C)+1`$; see [constructions](constructions.md). It returns every cyclically invariant initialized joint state, including identical product states. Therefore the largest gap gives the optimal depth scaling for a prescribed set of available anchor sites when their initialized state may be chosen. For general $`k`$, repeating the construction gives depth at most $`k(g(C)+1)`$, while an independent path construction has depth $`O(n)`$.

The existence of finite-depth opposite translations and state-invariant catalytic cancellation is established background; see [SNZ2025](../references/RELATED_WORK.md#snz2025). The matching mixed-state example restores the physical initialized state, including its correlations within $`A`$. It need not restore an external purification of that state. A product-pure choice has no such distinction. These constructions do not assert achievability for every prescribed mixed spectrum at the anchors.

## Local capacity for product-pure work

The [approximate capacity theorem](approximate_capacity.md#local-capacity-theorem) gives a more detailed placement condition for initialized qubits. Let $`m_i`$ be their number at site $`i`$, let $`q=\lfloor n/4\rfloor`$, and require product-pure initialization with full joint-return diamond error less than one. For $`1\le k\le q`$ and $`D\le q`$,

```math
\sum_{i\in[x-D,x)}m_i\ge k
\qquad\text{for every cut }x.
\tag{6}
```

This is a capacity condition in every window of $`D`$ consecutive sites, not merely a condition that every window contains one initialized site. Summation gives $`DM\ge nk`$.

One can express the same placement requirement by the largest distance needed to encounter $`k`$ initialized qubits when moving backward from a cut. Define

```math
R_k(\mathbf m)
=\max_{x\in\mathbb Z_n}
\min\left\{
r\in\{0,1,\ldots,n\}:
\sum_{i\in[x-r,x)}m_i\ge k
\right\},
```

with $`R_k=+\infty`$ if $`M<k`$. Then every circuit satisfying that theorem obeys

```math
D\ge\min\{q+1,R_k(\mathbf m)\},
\qquad D\ge k.
\tag{7}
```

For $`k=1`$ and at least one occupied site, $`R_1(\mathbf m)=g(C)`$. For larger $`k`$, nearby registers can contribute several qubits, but capacity concentrated far from a cut cannot satisfy (6) at small depth. No matching characterization for every fixed capacity profile is asserted by (7); it is the placement-sensitive necessary condition proved by the local spectral argument.

The gap theorem and the local capacity theorem should be used with their respective hypotheses. The former allows arbitrary initialized states, requires only a reduced-channel error at most $`1/192`$, and does not require return. The latter allows full joint-return error below one, requires product-pure initialized work, and detects the number of qubits needed in each short window.
