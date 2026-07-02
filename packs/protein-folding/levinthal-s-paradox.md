---
title: "Levinthal's paradox"
source: https://en.wikipedia.org/wiki/Levinthal%27s_paradox
domain: protein-folding
license: CC-BY-SA-4.0
tags: protein folding, protein structure prediction, levinthal paradox, anfinsen dogma
fetched: 2026-07-02
---

# Levinthal's paradox

**Levinthal's paradox** is a thought experiment in the field of computational protein structure prediction; protein folding is the process by which peptides reach a stable native configuration. In theory, a brute force search, testing all possible conformations, would take longer than the age of the universe to identify this minimum energy configuration (the native state). In reality, protein folding happens very quickly, even for complex structures, suggesting that the intermediate structures are steered to a stable state through an uneven energy landscape.

## History

In 1969, Cyrus Levinthal noted that, because of the many degrees of freedom in an unfolded polypeptide chain, the molecule has an astronomical number of possible conformations. An estimate of 10300 was made in one of his papers (often incorrectly cited as the 1968 paper). For example, a polypeptide of 100 residues will have 200 different phi and psi bond angles, two for each residue. If each torsion angle can be in one of three stable conformations, the protein may adopt a maximum of 3200 different conformations, without even considering interactions between residues or the conformations of side-chains. Therefore, if a protein were to reach its correctly folded configuration by sequentially sampling all possible conformations, it would need more time than the age of the universe to find its native conformation. This remains true even if conformations are sampled at rapid nanosecond or picosecond rates. The "paradox" is that most small proteins fold spontaneously on a millisecond or even microsecond time scale. Insights into this paradox have been advanced by computational approaches to protein structure prediction.

## Resolution and Explanations

Levinthal himself was aware that proteins fold spontaneously and on short timescales. He suggested that the paradox can be resolved if "protein folding is sped up and guided by the rapid formation of local interactions which then determine the further folding of the peptide; this suggests local amino acid sequences which form stable interactions and serve as nucleation points in the folding process". Indeed, the protein folding intermediates and the partially folded transition states were experimentally detected, which explains the fast protein folding.

### Protein Folding

Protein folding can be understood as a multidimensional optimization problem within a funnel-like energy landscape. Any particular configuration of amino acids has a corresponding stability, and the protein will spontaneously follow its energetic gradient toward higher stability states. This tendency directs the process of folding and dramatically shrinks the space of feasible structures the protein might adopt. The protein traverses this landscape of energetic states to its native state, found at the bottom of the funnel. This was shown by Christian Anfinsen in his famous experiments with ribonuclease A, demonstrating that an unfolded protein can refold to its native, functional structure, even in the absence of cellular machinery. This validated Anfinsen's thermodynamic hypothesis, also known as Anfinsen's dogma, which states that the native structure of a protein is the state in which it has a minimum of free energy.

In the process of folding it is possible for proteins to become trapped in intermediate states, a locally optimal state, but not a globally optimal state. This problem is addressed in part by chaperones, proteins which assist in the folding process, which help in bringing unfolded intermediates to their native state.

However, protein folding does not simply begin with a fully synthesized, unfolded peptide chain. In cellular systems, folding commonly begins while the protein is being produced in the ribosome. As each amino acid is added to the chain, residues can adopt secondary and tertiary structures, a process known as cotranslational folding.

According to Edward Trifonov and Igor Berezovsky, proteins fold by subunits (modules) of the size of 25–30 amino acids.

### Computational Protein Structure Prediction

The problem of protein folding is increasingly being answered by computational methods. Some computational approaches to protein structure prediction have sought to identify and simulate the mechanism of protein folding. The development of tools such as AlphaFold leverage machine learning and the known structures of homologous proteins to predict unknown structures with high accuracy. Levinthal's paradox was cited on the first page of the Scientific Background to the 2024 Nobel Prize in Chemistry (awarded to David Baker, Demis Hassabis, and John M. Jumper for computational protein design and protein structure prediction) by way of demonstrating the sheer scale of the problem given the astronomical number of permutations.
