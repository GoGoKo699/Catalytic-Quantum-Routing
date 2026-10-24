# Learning catalytic quantum routing

The starting question is concrete: if every unknown quantum register moves one site around a ring, where does the displaced information go during a local implementation? A second flow can make the operation shallow, but its registers must be returned under the promised contract. This project counts how much initialized capacity that requires.

## One anchor and a bridge

The educational anchor is **Terry Farrelly, [*A review of Quantum Cellular Automata*](https://quantum-journal.org/papers/q-2020-11-30-368/), *Quantum* 4, 368 (2020)**, with [arXiv:1904.13318v2](https://arxiv.org/html/1904.13318v2) as the versioned reading source.

The [source-to-project bridge](farrelly_bridge.md) identifies the relevant sections, reconciles notation and index conventions, and supplies the channel-return, entropy, and rank ingredients needed here. Its eight-site circuit is a complete worked example. Reading the entire review is not a prerequisite for following the bridge.

Primary research citations remain necessary for the shift obstruction, domain-wall strategy, inverse-copy construction, catalytic invariance, and index stability. Their roles are recorded in the [related-work account](../references/RELATED_WORK.md). They support the scientific arguments without turning the learning route into a second textbook list.

## A common map of 30 understanding targets

The [milestone map](milestones.md) contains exactly **M01–M30**:

- **M01–M14: background and preliminaries.** Registers, channels, locality, flow, and return conditions combine with entropy and spectral tools to define the complete problem.
- **M15–M30: narrative and innovation.** A local counterflow step and a local cut obstruction grow into the matching global workspace-depth law, its resource interpretation, and its scope.

This 14/16 allocation reflects the project's two prerequisite families: circuit geometry and QCA flow on one side, channel contracts and information-theoretic capacity on the other. Each milestone states a central question, understanding target, dependencies, conceptual connection, and source pointers. The end of each phase synthesizes its earlier components.

The map is defined by the project for any reader. It is a route to conceptual understanding of the contribution, not a claim to cover every technical detail of the proofs.

## Choose a reading route

| Reader's question | Route |
|---|---|
| What is the physical mechanism? | [Worked bridge](farrelly_bridge.md), then [constructions](../science/constructions.md) |
| Which ideas must fit together? | [Milestones M01–M30](milestones.md), with the bridge alongside them |
| What is proved under which assumptions? | [Model and theorem](../science/model.md), then its linked proof pages |
| Why does workspace matter beyond distance? | [Interpretation and separation example](../science/interpretation.md) |
| How can I reproduce the finite checks? | [Verification commands and evidence](../verification/README.md) |

The files under [science/](../science/README.md) remain the authoritative account. In particular, exact arbitrary-catalyst return, approximate product-pure joint return, and the separate arbitrary-state gap theorem have different hypotheses throughout both reading routes.
