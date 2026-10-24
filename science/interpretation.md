# What the workspace frontier means

The [optimal-depth theorem](model.md#the-attained-frontier) concerns a simple operation: move every unknown data qubit by the same distance around a ring. The operation has a short input-output light cone, but implementing it by local gates requires a return path for the displaced information. The initialized workspace provides that path.

## Three regimes

For $`1\le k\le n/2`$, the depth scale is

```math
F(n,k,m)=\min\!\left\{n,\,
k\max\!\left(1,\frac{n}{m+1}\right)\right\}.
```

| Initialized workspace | Optimal depth scale | Meaning |
|---|---:|---|
| $`m=O(k)`$ | $`\Theta(n)`$ | There is too little reusable capacity to obtain a sublinear-depth translation. |
| $`k\ll m\ll n`$ | $`\Theta(nk/m)`$ | Additional distributed workspace increases the rate at which the opposite flow can be carried. |
| $`m=\Omega(n)`$ | $`\Theta(k)`$ | The ordinary propagation-distance limit is attained up to constants. |

The first row includes $`m=0`$. For fixed $`k`$, a growing but sublinear number of well-distributed initialized qubits gives diverging but sublinear depth; constant depth is attained when $`m`$ becomes proportional to $`n`$. To obtain $`D=o(n)`$ for a growing shift distance, both $`k=o(n)`$ and $`m/k\to\infty`$ are necessary and sufficient at the level of these asymptotic scales.

The theorem concerns depth. The constructions also give explicit SWAP counts: the ancillary counterflow uses $`k(n+a)`$ SWAPs for $`a`$ active anchors, while the ancilla-free block exchange uses $`k(n-k)`$ SWAPs. These are charged implementation costs, not claims of gate-count optimality for every allowed quantum gate model.

## A regime missed by distance and gap alone

Take $`n=L^2`$ and $`k=m=L`$, and place the initialized qubits evenly around the ring. The data travels distance $`L`$, and the largest workspace spacing is also $`L`$. Propagation and the separate largest-gap obstruction each give only an $`\Omega(L)`$ lower bound.

The capacity law instead requires $`Dm=\Omega(nk)`$, unless the circuit is already linear in depth. Substituting $`k=m=L`$ forces

```math
D=\Theta(n).
```

The extra restriction is simultaneous throughput. Each cut must support a directed flow of $`k`$ unknown qubits, and all cuts share the finite initialized capacity. Taking the larger of a propagation bound and a covering-gap bound does not account for that demand.

This is an asymptotic separation, not a numerical prediction of the minimum depth for a particular small device. The [finite constants](model.md#the-attained-frontier) and [explicit schedules](constructions.md) give the corresponding finite statements.

## The amount and location of work

Total capacity does not specify a layout. For a one-site shift, placing many initialized qubits in a short arc leaves a long resource-free interval. The [placement theorem](placement.md) still forces depth proportional to that interval, even if each occupied site carries a very large ancillary Hilbert space.

For product-pure work at full diamond error below one, the local capacity theorem gives a more demanding condition for a $`k`$-site shift: every one-sided $`D`$-site interval must contain at least $`k`$ initialized qubits in the shallow regime. This distinguishes capacity from mere coverage. One ancillary qubit in every long interval is sufficient to remove an empty-gap witness, but it need not provide the throughput needed for a larger shift.

The optimized frontier chooses an appropriate layout. It does not assert that every placement of $`m`$ qubits attains it, or that the local necessary condition alone characterizes the optimal depth for every nonuniform placement.

## Initialized and borrowed work

In the counterflow construction, the global unitary is

```math
W=T_{1,S}\otimes T_{-1,A},
```

where the second translation cycles the selected ancillary anchors in the opposite direction. The ancillary unitary generally is not identity. It nevertheless returns every state invariant under that cyclic permutation.

For example,

```math
\sigma_A=\tau^{\otimes a}
```

is returned for any one-qubit density operator $`\tau`$, including a maximally mixed state. The construction does not consume purity. It uses the fact that the specified state is unchanged under a nontrivial operation.

An arbitrary borrowed register obeys a stronger requirement. Its state may encode unknown information or be entangled with an external reference, and the final operation on that register must be the identity channel. Cycling arbitrary borrowed values would violate this contract. The lower bounds therefore permit as much borrowed work as desired while charging only the initialized capacity.

### Why a mixed catalyst's purification matters

Preserving a fixed mixed state is weaker than preserving its purification. This can be seen directly without an entropy inequality.

Suppose $`\sigma_A=\sum_j\lambda_j|j\rangle\langle j|`$ is full rank and has a purification

```math
|\Sigma\rangle_{AE}
=\sum_j\sqrt{\lambda_j}|j\rangle_A|j\rangle_E,
\qquad \lambda_j>0.
```

If a unitary $`W_{SA}`$ must implement $`U_S`$ for every input and return the entire purification, then

```math
(W_{SA}\otimes I_E)
(|\psi\rangle_S\otimes|\Sigma\rangle_{AE})
=
U_S|\psi\rangle_S\otimes|\Sigma\rangle_{AE}
```

up to an irrelevant common phase. Comparing the coefficients of the orthogonal states $`|j\rangle_E`$ gives

```math
W_{SA}(|\psi\rangle_S|j\rangle_A)
=U_S|\psi\rangle_S|j\rangle_A
```

for every $`j`$ and $`|\psi\rangle`$. Hence $`W=U\otimes I_A`$. A full-rank catalyst returned together with its purification is therefore borrowed work for this exact universal task. The same argument applies with $`SB`$ in place of $`S`$.

The maximally mixed counterflow construction does not satisfy this stronger condition: it changes the labels correlated with $`E`$. Its claimed return is exactly the physical-state return in [equation (1)](model.md#translation-and-the-two-return-contracts). Pure initialized work has no nontrivial inaccessible purification, so this distinction does not weaken the product-pure construction.

## Why arbitrary borrowed width disappears from the bounds

The exact proof chooses a spatial profile in which all uninitialized registers near one cut are pure and those near the other cut are completely mixed. The dimension of the borrowed registers can be arbitrarily large. Their entropy is part of the witness, but they return unchanged and therefore contribute no net target entropy change.

The only term that can lower the entropy at the relevant crossing patches is bounded by the logarithmic dimension of the initialized registers there. For the approximate pure-work proof, the borrowed dimensions enter a flat rank $`r`$ on the initial half-ring and cancel against the same $`r`$ in the target spectral bound. Both mechanisms depend on the full borrowed return contract.

## Boundaries of the result

The exact capacity theorem permits arbitrary fixed mixed and spatially entangled initialized states. The constant-error capacity theorem proved here requires product-pure initialized states and joint-return accuracy. A general constant-error capacity theorem for correlated mixed catalysts is not inferred from the exact entropy proof: direct entropy continuity would introduce unwanted dependence on the size of the data or borrowed registers.

The separate constant-error gap theorem does allow arbitrary initialized states and does not require their return. Its conclusion concerns the absence of initialized resources in a long interval, rather than the full $`k`$-dependent capacity frontier.

Measurements, teleportation, long-range gates, and a requirement to route only a subset of the data define different tasks. In particular, the results do not settle the general ancilla-count tradeoff for teleportation-assisted routing discussed in [Devulapalli et al.](../references/RELATED_WORK.md#devulapalli2024). Nor do they contradict catalytic Clifford compression with unrestricted connectivity.

The explicit constructions require no QRAM, input-dependent classical description, or nonlocal state preparation. The lower bounds hold for arbitrary quantum input states, including inputs correlated with an untouched reference.
