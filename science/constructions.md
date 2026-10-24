# Constructions and resource counts

The upper bounds use only SWAP gates. Their action is a permutation of complete quantum registers, so the proofs apply to arbitrary superpositions and entanglement with references.

The opposite-flow construction for densely supplied work is a standard way to implement a shift together with its inverse [YLS2024](../references/RELATED_WORK.md#yls2024). Returning a state invariant under the auxiliary action is the catalytic mechanism discussed in [SNZ2025](../references/RELATED_WORK.md#snz2025). The construction here specifies the schedule for arbitrary anchor positions and counts its depth and gates.

## One step with arbitrary anchors

Choose $`a`$ distinct anchor sites,

```math
0\le b_0<b_1<\cdots<b_{a-1}<n,
\qquad 1\le a\le n.
```

Place one initialized register $`A_j`$, of the same dimension as a data register, at site $`b_j`$. Use cyclic indexing and the unwrapped endpoint $`b_a=b_0+n`$. Define

```math
g_j=b_{j+1}-b_j,
\qquad
g=\max_j g_j.
```

The data segments

```math
S_{b_j+1},S_{b_j+2},\ldots,S_{b_{j+1}}
```

partition the ring. Their lengths are $`g_j`$.

**Proposition 1: one-step counterflow.** There is a circuit of depth $`g+1`$, using exactly $`n+a`$ SWAP gates, whose complete action is

```math
W_{\rm cf}=T_S\otimes C_A^{-1}\otimes I_B.
\tag{1}
```

Here $`T_S`$ moves each data input one site to the right, and $`C_A`$ moves the input at anchor index $`j`$ to anchor index $`j+1`$. The borrowed registers $`B`$ are untouched.

The circuit has three parts:

1. In one layer, swap $`S_{b_j}`$ with $`A_j`$ at every anchor.
2. For rounds $`r=1,\ldots,g-1`$, and every segment with $`r<g_j`$, swap
   $`S_{b_{j+1}-r}`$ with $`S_{b_{j+1}-r+1}`$. Different segments operate in parallel.
3. In one layer, swap $`A_j`$ with $`S_{b_j+1}`$ for every anchor.

Indices in actual gates are reduced modulo $`n`$.

### Why every layer is legal

The first layer acts on disjoint data–ancilla pairs at the anchors. In each sweep round, there is at most one gate per segment, and the data segments are disjoint. In the last layer, all $`A_j`$ are distinct and all $`S_{b_j+1}`$ are distinct. A last-layer gate may share a physical site with another gate, but it uses different registers there, as allowed by the [layer convention](exact_capacity.md#registers-depth-and-capacity).

Every gate acts at one site or across a neighboring pair of sites. No long-range gate or classical feedback is used.

### Why the action is exact

After the first layer, the input data from anchor $`b_j`$ are held in $`A_j`$. The previous contents of $`A_{j+1}`$ occupy the right endpoint $`S_{b_{j+1}}`$ of segment $`j`$.

The sweep moves those ancillary contents to $`S_{b_j+1}`$. Along the way, every other data input in the segment moves one site to the right. The final layer places the saved data from $`b_j`$ into $`S_{b_j+1}`$, while $`A_j`$ receives the previous contents of $`A_{j+1}`$.

Thus every data input moves one physical site right and every ancillary input moves one anchor left. Tracking distinct register labels proves the full unitary identity (1), with no assumption on their input states.

There are $`a`$ initial gates, $`\sum_j(g_j-1)=n-a`$ sweep gates, and $`a`$ final gates. Therefore

```math
D_{\rm cf}=g+1,
\qquad
N_{\rm SWAP,cf}=n+a.
\tag{2}
```

These counts include the case $`a=1`$, where the auxiliary permutation is identity, and $`a=n`$, where there are no sweep rounds.

## Translation by several sites and catalyst return

Repeat the one-step circuit $`k`$ times. The complete action is

```math
W_{\rm cf}^{\,k}
=
T_S^k\otimes C_A^{-k}\otimes I_B,
```

with resources

```math
D_{\rm cf}^{(k)}=k(g+1),
\qquad
N_{\rm SWAP,cf}^{(k)}=k(n+a).
\tag{3}
```

For an initialized state $`\sigma_A`$ independent of the arbitrary data and borrowed input, the final state of the initialized work is $`C_A^{-k}\sigma_AC_A^k`$. Hence exact catalytic return holds whenever

```math
C_A^k\sigma_AC_A^{-k}=\sigma_A.
\tag{4}
```

In particular, $`\sigma_A=\tau^{\otimes a}`$ works for every $`k`$ and every single-register state $`\tau`$, including pure and maximally mixed states. An entangled state invariant under the same anchor permutation also works. Invariance under the $`k`$th power is sufficient for return after the entire circuit; invariance after every individual repetition is not required.

The output remains product with the initialized work for arbitrary data–reference inputs. For mixed initialized states, (4) preserves their complete physical state but can change correlations with an external purification. This is why the same registers cannot simply be relabeled as arbitrary borrowed workspace.

The optimized upper bound can choose the standard pure product $`|0\rangle^{\otimes a}`$. It therefore requires $`a`$ local initializations and no entangled-state preparation. Those initializations supply the resource counted by $`a`$; no intermediate measurement or reset is used. If local preparation depth is included in a larger accounting, one parallel preparation layer is added to the displayed online unitary depth.

## An ancilla-free schedule

A separate construction gives an upper bound independent of the amount of work.

**Proposition 2: stable block exchange.** For every $`1\le k\le n-1`$, the right rotation by $`k`$ sites can be implemented on the open path $`0,1,\ldots,n-1`$ in exactly $`n-1`$ nonempty SWAP layers, using exactly $`k(n-k)`$ SWAPs.

Write $`u=n-k`$ and $`v=k`$. Label the first block of inputs $`A_1,\ldots,A_u`$ and the second block $`B_1,\ldots,B_v`$. The desired output order is

```math
B_1,\ldots,B_v,A_1,\ldots,A_u.
```

For each pair $`1\le i\le u`$, $`1\le j\le v`$, schedule the crossing of $`A_i`$ and $`B_j`$ in round

```math
r=u-i+j
```

at the data edge

```math
(i+j-2,\;i+j-1).
\tag{5}
```

The rounds run from $`1`$ to $`n-1`$. Within a round, $`j=r-u+i`$, so the starting sites of successive scheduled edges differ by two. Their registers are disjoint.

Immediately before its scheduled crossing, $`A_i`$ has crossed the $`j-1`$ earlier $`B`$ inputs and is at site $`i+j-2`$. Similarly, $`B_j`$ has crossed the $`u-i`$ later $`A`$ inputs and is at site $`i+j-1`$. These earlier crossings all occur in earlier rounds. Induction therefore verifies every scheduled adjacent exchange.

Every $`A`$–$`B`$ pair crosses exactly once, while the order within each block is unchanged. This proves the rotation, the $`uv=k(n-k)`$ gate count, and the $`n-1`$ depth. The schedule works on a ring without using its wraparound edge. No initialized or borrowed register is touched.

For a requested left rotation, reflect all site labels. For an arbitrary rotation, choosing the shorter direction gives $`k\le\lfloor n/2\rfloor`$ for the frontier below.

## Balanced placement and the frontier

Given $`m\ge1`$ initialized qubits, use

```math
a=\min\{m,n\}
```

of them, one at each balanced anchor

```math
b_j=\left\lfloor\frac{jn}{a}\right\rfloor,
\qquad j=0,\ldots,a-1.
```

The gaps are either $`\lfloor n/a\rfloor`$ or $`\lceil n/a\rceil`$, so $`g=\lceil n/a\rceil`$. Extra initialized registers, if $`m>n`$, remain untouched. Choose the shallower of Propositions 1 and 2:

```math
D_{\rm upper}(n,k,m)
\le
\begin{cases}
n-1, & m=0,\\[2mm]
\min\left\{n-1,\;
k\left(\left\lceil\frac{n}{\min\{m,n\}}\right\rceil+1\right)\right\},
& m\ge1.
\end{cases}
\tag{6}
```

The two available gate counts are explicit:

| Schedule | Initialized registers used | Depth | SWAP count |
|---|---:|---:|---:|
| Stable block exchange | $`0`$ | $`n-1`$ | $`k(n-k)`$ |
| Balanced counterflow | $`a=\min\{m,n\}`$ | $`k(\lceil n/a\rceil+1)`$ | $`k(n+a)`$ |

Unused borrowed and initialized registers contribute identity wires. If the depths tie, the schedule with fewer SWAPs may be selected.

For

```math
F(n,k,m)=
\min\left\{
n,\;
k\max\left\{1,\frac{n}{m+1}\right\}
\right\},
```

equation (6) implies $`D_{\rm upper}\le6F`$. For $`m=0`$, the statement follows from $`F=n`$. For $`1\le m<n`$,

```math
\left\lceil\frac nm\right\rceil+1
\le \frac nm+2
\le 3\frac nm
\le 6\frac n{m+1},
```

and one can choose the path bound whenever the first branch of $`F`$ is smaller. For $`m\ge n`$, the counterflow depth is $`2k`$ and $`F=k`$.

Combining this with [Theorem 1](exact_capacity.md#the-exact-capacity-theorem) yields the exact optimal frontier. The same circuits meet every positive approximation budget because they return the chosen pure product work exactly.

### An architecture with ancillary side leaves

If a hardware graph connects $`A_j`$ only to $`S_{b_j}`$, the last-layer SWAP between $`A_j`$ and $`S_{b_j+1}`$ can be replaced by three SWAPs along

```math
A_j\;-\;S_{b_j}\;-\;S_{b_j+1}.
```

This exchanges the two endpoint registers and restores the middle register. Color the participating data edges with at most three colors and execute one color at a time. The resulting one-step depth is at most $`g+9`$, with $`n+3a`$ SWAPs. The scaling is unchanged. The sharper counts in (2), (3), and (6) refer to the stated neighboring-register model.

## What the finite verification establishes

[The routing program](../verification/routing.py) generates the schedules and checks every layer against the locality and register-disjointness rules. It tracks a distinct symbolic input label on every data and initialized register and compares the complete output permutation with (1) and its powers. This detects errors in ancillary return, wraparound indexing, unequal gaps, and the simultaneous final layer without relying on a particular input state.

The default command is

```bash
python verification/routing.py
```

It exhausts all nonempty anchor subsets for rings with $`2\le n\le9`$, checks all positive step counts smaller than $`n`$, checks every path rotation through $`n=64`$, and checks balanced placements and the displayed resource inequalities. The program prints the actual case counts.

These finite checks verify the implemented schedules on their stated finite domains. The proofs above establish the identities and resource bounds for arbitrary system size. They do not establish optimality for every fixed irregular anchor pattern: the arbitrary-anchor construction gives $`k(g+1)`$, while the [placement theorem](placement.md) supplies the corresponding necessary local capacity conditions.
