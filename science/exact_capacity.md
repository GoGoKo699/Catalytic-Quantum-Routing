# Exact capacity of returned workspace

A local circuit can translate an entire ring much faster when initialized registers carry an opposite flow. This page proves how much initialized capacity that flow requires. The catalyst may be mixed and entangled across the ring; its state is returned exactly. Borrowed registers are required to undergo the identity channel on every input, including inputs entangled with a reference.

The argument uses a pure/mixed domain wall, following the shift obstruction of [YLS2024](../references/RELATED_WORK.md#yls2024). The additional step bounds how much the initialized registers in a circuit's two boundary patches can change the entropy. Index theory gives the broader interpretation of the shift obstruction [GNVW2012](../references/RELATED_WORK.md#gnvw2012), while local index stability supports the separate [gap theorem](placement.md). The capacity proof below uses finite-dimensional entropy inequalities directly.

## Registers, depth and capacity

There are $`n\ge 2`$ sites, labeled by $`\mathbb Z_n`$. Site $`i`$ contains a data register $`S_i`$ of dimension $`d\ge 2`$, optional initialized registers grouped as $`A_i`$, and optional borrowed registers grouped as $`B_i`$. A missing register has dimension one. All dimensions are finite, with no uniform bound imposed on the borrowed dimensions.

A layer consists of gates on pairwise disjoint registers. Each gate acts on one site or two neighboring sites. In particular, two gates may share a site if their registers are disjoint. The constructions use two-register SWAP gates. The lower bounds use only this locality and the resulting propagation of support by at most one site per layer.

Let $`T`$ move the data initially at site $`i`$ to site $`i+1`$. The initialized state $`\sigma_A`$ is fixed independently of the arbitrary input on $`SB`$. Exact implementation and return mean

```math
W(\rho_{SBR}\otimes \sigma_A)W^\dagger
=
\bigl[(T^k\otimes I_{BR})\rho_{SBR}
(T^{-k}\otimes I_{BR})\bigr]\otimes \sigma_A
```

for every input and reference $`R`$. The circuit does not act on $`R`$. When $`\sigma_A`$ is mixed, its return concerns the full physical state on $`A`$; preserving an arbitrary external purification of $`A`$ is a stronger requirement. Borrowed registers have the identity-with-reference requirement.

All entropies and logarithms on this page are in bits. Define

```math
a(X)=\sum_{i\in X}\log_2\dim A_i,
\qquad
M=a(\mathbb Z_n).
```

Thus $`M=m`$ for $`m`$ initialized qubits, including multiple qubits at one site. Counting occupied sites alone would miss the capacity of a larger register.

For a nontrivial rotation by $`t`$ sites, it is enough to take

```math
k=\min\{t\bmod n,\;n-(t\bmod n)\},
\qquad 1\le k\le \lfloor n/2\rfloor,
```

and reflect the site labels if necessary. The identity rotation has depth zero.

## The exact capacity theorem

Set

```math
q=\lfloor n/4\rfloor,
\qquad
\ell=\lfloor n/2\rfloor,
\qquad
P_x(D)=\{x-D,\ldots,x+D-1\}\pmod n.
```

The cut labeled $`x`$ lies between sites $`x-1`$ and $`x`$.

**Theorem 1: local and total initialized capacity.** Suppose $`1\le k\le q`$ and an exact implementation has depth $`D\le q`$. Then, for every cut $`x`$,

**Equation (1).**

```math
k\log_2 d
\le
3\bigl[a(P_x(D))+a(P_{x+\ell}(D))\bigr].
```

Consequently,

**Equation (2).**

```math
12DM\ge nk\log_2 d.
```

No assumption of a product state, full rank, or absence of long-range entanglement is imposed on $`\sigma_A`$. The number and dimensions of the borrowed registers do not appear in these bounds.

For $`1\le k\le q`$, a convenient unconditional consequence is

**Equation (3).**

```math
D\ge
\max\left\{
k,\;
\min\left\{q+1,\frac{nk\log_2 d}{12M}\right\}
\right\},
```

where the quotient is interpreted as infinity when $`M=0`$. For $`k>q`$, the ordinary propagation bound $`D\ge k>n/4`$ already gives linear depth.

The two finite-size conditions in Theorem 1 are exact integer conditions. The proof below works at $`D=q`$; when two patches meet at an endpoint, their sets of sites are still disjoint.

## Cut factorization

This lemma is shared with the [approximate capacity proof](approximate_capacity.md).

**Lemma 2: two boundary patches.** Let two cuts divide the ring into

```math
L=\{x,\ldots,x+\ell-1\},
\qquad
L^c=\mathbb Z_n\setminus L.
```

If $`2D\le \min\{\ell,n-\ell\}`$, every depth-$`D`$ circuit has both factorizations

**Equation (4).**

```math
W=(W_L\otimes W_{L^c})V_xV_{x+\ell}
=
\widetilde V_x\widetilde V_{x+\ell}
(W_L\otimes W_{L^c}),
```

where each of $`V_c,\widetilde V_c`$ is supported on $`P_c(D)`$. The two boundary patches are disjoint. The same internal circuit $`W_L\otimes W_{L^c}`$ can be used in both expressions.

**Proof.** Write the circuit in time order as $`W=L_D\cdots L_1`$. In layer $`t`$, separate the gates crossing either cut from the remaining gates:

```math
L_t=G_tC_t,
\qquad
C_t=C_{x,t}C_{x+\ell,t}.
```

The factors in one layer commute because their registers are disjoint. Deleting the crossing gates gives

```math
W_0=G_D\cdots G_1=W_L\otimes W_{L^c}.
```

Let $`G_{<t}=G_{t-1}\cdots G_1`$, with $`G_{<1}=I`$. An exact telescoping identity gives

**Equation (5).**

```math
W_0^\dagger W
=
\prod_{t=D}^{1}
G_{<t}^\dagger C_tG_{<t},
```

where larger $`t`$ appears farther left. A crossing gate at cut $`c`$ initially acts only on sites $`c-1,c`$. Conjugating it through $`t-1`$ internal layers enlarges its support to at most

```math
\{c-t,\ldots,c+t-1\}
\subseteq P_c(D).
```

All dressed factors associated with opposite cuts therefore have disjoint support. Regrouping them proves the first factorization in (4). Apply the same construction to $`W^\dagger`$ and take adjoints to obtain the second factorization with the same $`W_0`$.

This proof allows many distinct registers at each site and arbitrary gates within a neighboring pair of sites. Only support propagation and disjointness within a layer are used. For $`D\le q`$, the required separation follows from $`2q\le\ell\le n-\ell`$. □

## Entropy capacity of an initialized patch

**Lemma 3: a patch can reduce entropy by at most three times its initialized capacity.** Partition a finite system into left and right parts. A unitary $`V`$ acts on a patch $`QK`$, where $`K`$ consists of the initialized registers in that patch. Let $`Z`$ contain everything outside it. Suppose the input is

```math
\omega_Q\otimes\rho_{KZ},
```

where $`\omega_Q`$ is either a pure product across $`Q_L|Q_R`$ or the completely mixed state on $`Q`$. The state $`\rho_{KZ}`$ is arbitrary. Then

**Equation (6).**

```math
S(L)_{\rm after}-S(L)_{\rm before}
\ge -3\log_2\dim K.
```

**Proof.** Put $`X=Q_LK_L`$. The outside marginal $`Z_L`$ is unchanged, so the change of $`S(L)`$ equals the change of $`S(X|Z_L)`$. Initially,

**Equation (7).**

```math
S(X|Z_L)_{\rm before}
=
S(Q_L)+S(K_L|Z_L)
\le S(Q_L)+\log_2\dim K_L.
```

The output $`X`$ is obtained from $`QK`$ by a channel. Data processing therefore gives

**Equation (8).**

```math
I(X:Z_L)_{\rm after}
\le I(QK:Z_L)_{\rm before}
=
I(K:Z_L)_{\rm before}
\le 2\log_2\dim K.
```

For a pure product $`\omega_Q`$, the initial $`S(Q_L)`$ is zero and the final $`S(X)`$ is nonnegative. Combining (7), (8), and $`S(X|Z_L)=S(X)-I(X:Z_L)`$ gives (6).

For completely mixed $`\omega_Q`$, entropy conservation on the entire patch and the dimension bound on its right part imply

**Equation (9).**

```math
\begin{aligned}
S(X)_{\rm after}
&\ge S(QK)_{\rm after}-S(Q_RK_R)_{\rm after}\\
&\ge \log_2\dim Q_L-\log_2\dim K_R.
\end{aligned}
```

Since $`S(Q_L)=\log_2\dim Q_L`$, the same combination yields

```math
\Delta S(L)
\ge
-\log_2\dim K_L
-\log_2\dim K_R
-2\log_2\dim K
=
-3\log_2\dim K.
```

The bound is independent of the dimension of $`Q`$ and of correlations between $`K`$ and the outside system. □

## Proof of the theorem

Fix $`x=0`$; translated choices will be used afterward. Take $`L=\{0,\ldots,\ell-1\}`$. Initialize the data witness as a site-product state that is pure on

```math
\{-q,\ldots,\ell-q-1\}\pmod n
```

and completely mixed on the complementary arc. Choose each borrowed register pure or completely mixed with the same spatial profile. This is a permissible input because borrowed work must be handled correctly for every state. The initialized catalyst remains in its prescribed state $`\sigma_A`$.

The data in $`P_0(D)`$ are all pure, and the data in $`P_\ell(D)`$ are all completely mixed. The same holds for borrowed registers in those patches. These statements hold for every $`D\le q`$, including all residues of $`n`$ modulo four.

There are initially $`q`$ completely mixed data qudits in $`L`$. A right shift by $`k\le q`$ reduces this number to $`q-k`$. Borrowed registers are returned by identity, and the initialized state is returned in product with the data and borrowed registers. Hence the desired transformation has

**Equation (10).**

```math
S(L)_{\rm out}-S(L)_{\rm in}
=
-k\log_2d.
```

Use the input-side factorization in Lemma 2. The internal factors $`W_L,W_{L^c}`$ preserve $`S(L)`$. Apply Lemma 3 first to $`V_0`$ and then to $`V_\ell`$. The second patch's uninitialized registers are still pure or completely mixed and independent of the rest, because the first patch is disjoint. Its initialized registers may have become correlated with outside registers, which Lemma 3 permits. Equation (10) then proves (1).

Translate the witness and the pair of cuts through all $`n`$ positions. Each site appears in exactly $`2D`$ patches of the form $`P_x(D)`$. The translated second cut contributes the same count. Summing (1) gives

```math
nk\log_2d
\le
3(2DM+2DM)
=
12DM.
```

This proves Theorem 1. □

## Why exact unitary action gives product return

One can equivalently assume that the reduced channel on $`SB`$ is exactly $`T^k\otimes I_B`$ and that the initialized output marginal is $`\sigma_A`$. Product return then follows; it is not an additional independence assumption on the output.

To see this, purify the fixed initialized state using an inaccessible register $`E`$. The circuit defines an isometry from $`SB`$ to $`SBAE`$. An isometric extension of a unitary channel has the form

```math
|\psi\rangle_{SB}
\longmapsto
(T^k\otimes I_B)|\psi\rangle_{SB}\otimes|\eta\rangle_{AE},
```

with the same environment vector for every input. For basis inputs, purity of the reduced output gives a product vector. Preservation of the off-diagonal matrix elements forces their environment vectors to coincide. Linearity then proves the displayed form. Tracing $`E`$ gives a fixed product state on $`A`$, and the return condition identifies it with $`\sigma_A`$. This argument also preserves every reference attached to $`SB`$.

## The optimal exact frontier for qubits

Let $`D_{\rm ex}^*(n,k,m)`$ be the minimum depth over the placement and fixed state of $`m`$ initialized qubits and over all admissible circuits. Borrowed registers may be supplied in arbitrary number. Define

```math
F(n,k,m)
=
\min\left\{
n,\;
k\max\left\{1,\frac{n}{m+1}\right\}
\right\}.
```

For every $`n\ge2`$, $`m\ge0`$, and $`1\le k\le\lfloor n/2\rfloor`$,

**Equation (11).**

```math
\frac{F(n,k,m)}{12}
\le
D_{\rm ex}^*(n,k,m)
\le
6F(n,k,m).
```

The explicit upper circuits and their sharper depth and SWAP counts are given in [Constructions](constructions.md#balanced-placement-and-the-frontier).

For completeness, the propagation lower bound $`D\ge k`$ follows by changing one data input whose destination is $`k`$ sites away. At smaller depth, its destination cannot depend on that input. Pre-existing correlations in the fixed initialized state do not permit signaling outside this circuit light cone.

If $`D\ge q+1`$, then $`D>n/4\ge F/4`$. Otherwise, $`D\le q`$ and the propagation bound implies $`k\le q`$, so Theorem 1 applies. For $`m=0`$ it rules out this second case. For $`1\le m<n`$, it gives $`D\ge nk/(12m)\ge F/12`$. For $`m\ge n`$, $`F=k`$ and propagation suffices. This proves the lower bound in (11), including $`n=2,3`$.

If the data and each initialized register instead have the same dimension $`d`$, the same result holds with $`m`$ counting initialized $`d`$-level registers: both sides of (2) acquire the same factor $`\log_2d`$. For unequal ancillary dimensions, Theorem 1 remains valid with the bit capacity $`M`$; the qubit frontier should not be reinterpreted as a count of unequal registers.

The minimum in (11) optimizes the initialized state. It does not assert that every particular mixed or entangled catalyst attains the upper bound. Product states already attain the scaling. The exact entropy proof does not itself establish the corresponding fixed-error bound for arbitrary correlated mixed catalysts; the [approximate theorem](approximate_capacity.md) states its product-pure scope explicitly.
