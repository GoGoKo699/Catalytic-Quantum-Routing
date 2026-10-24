# Scientific account

The project determines how reusable initialized workspace changes the circuit depth of cyclic quantum routing on a ring. It distinguishes total capacity, spatial placement, and the stronger requirement of returning arbitrary borrowed quantum information.

Start with [the model and optimal-depth theorem](model.md). The complete argument is organized by the resource each proof controls:

1. [Exact capacity](exact_capacity.md) factors a local circuit around two cuts and bounds how much entropy their initialized registers can remove. This gives a throughput constraint for arbitrary returned mixed or entangled catalysts.
2. [Approximate capacity](approximate_capacity.md) uses a rank-versus-spectrum witness. For product-pure work, a constant-error circuit needs at least $`k`$ initialized qubits in every relevant one-sided depth window.
3. [Constructions](constructions.md) implements counterflow on distributed ancillary anchors and gives an ancilla-free block-exchange schedule. These attain the optimized depth scale.
4. [Placement](placement.md) uses a local QCA index theorem to constrain empty workspace gaps, including arbitrary correlated initialized states and without requiring their return.
5. [Interpretation](interpretation.md) explains the attained regimes, a separation missed by simpler bounds, and the distinction between physical-state and reference-preserving return.

For attribution, consult [related work](../references/RELATED_WORK.md) and the [bibliography](../references/references.bib). For executable schedule checks and their limits, use [verification](../verification/README.md).

The exact and approximate claims share a depth scale but have different state and return assumptions. The common definitions and the main theorem live in [model.md](model.md); individual proofs are authoritative in their topic pages.
