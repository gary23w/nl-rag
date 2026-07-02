---
title: "Cahn–Ingold–Prelog priority rules"
source: https://en.wikipedia.org/wiki/Cahn%E2%80%93Ingold%E2%80%93Prelog_priority_rules
domain: stereochemistry
license: CC-BY-SA-4.0
tags: molecular stereochemistry, optical isomers, chiral molecules, conformational analysis
fetched: 2026-07-02
---

# Cahn–Ingold–Prelog priority rules

In organic chemistry, the **Cahn–Ingold–Prelog** (**CIP**) **sequence rules** (also the **CIP priority convention**; named after Robert Sidney Cahn, Christopher Kelk Ingold, and Vladimir Prelog) are a standard process to completely and unequivocally name a stereoisomer of a molecule. The purpose of the CIP system is to assign an *R* or *S* descriptor to each stereocenter and an *E* or *Z* descriptor to each double bond so that the configuration of the entire molecule can be specified uniquely by including the descriptors in its systematic name. A molecule may contain any number of stereocenters and any number of double bonds, and each usually gives rise to two possible isomers. A molecule with an integer n describing the number of stereocenters will usually have 2*n* stereoisomers, and 2*n*−1 diastereomers each having an associated pair of enantiomers. The CIP sequence rules contribute to the precise naming of every stereoisomer of every organic molecule with all atoms of ligancy of fewer than 4 (but including ligancy of 6 as well, this term referring to the "number of neighboring atoms" bonded to a center).

The key article setting out the CIP sequence rules was published in 1966, and was followed by further refinements, before it was incorporated into the rules of the International Union of Pure and Applied Chemistry (IUPAC), the official body that defines organic nomenclature, in 1974. The rules have since been revised, most recently in 2013, as part of the IUPAC book Nomenclature of Organic Chemistry. The IUPAC presentation of the rules constitute the official, formal standard for their use, and it notes that "the method has been developed to cover all compounds with ligancy up to 4... and... [extended to the case of] ligancy 6... [as well as] for all configurations and conformations of such compounds." Nevertheless, though the IUPAC documentation presents a thorough introduction, it includes the caution that "it is essential to study the original papers, especially the 1966 paper, before using the sequence rule for other than fairly simple cases."

A recent paper argues for changes to some of the rules (sequence rules 1b and 2) to address certain molecules for which the correct descriptors were unclear. However, a different problem remains: in rare cases, two different stereoisomers of the same molecule can have the same CIP descriptors, so the CIP system may not be able to unambiguously name a stereoisomer, and other systems may be preferable.

## Steps for naming

The steps for naming molecules using the CIP system are often presented as:

1. Identification of stereocenters and double bonds;
2. Assignment of priorities to the groups attached to each stereocenter or double-bonded atom; and
3. Assignment of *R*/*S* and *E*/*Z* descriptors.

### Assignment of priorities

*R*/*S* and *E*/*Z* descriptors are assigned by using a system for ranking priority of the groups attached to each stereocenter. This procedure, often known as *the sequence rules*, is the heart of the CIP system. The overview in this section omits some rules that are needed only in rare cases.

1. Compare the atomic number (*Z*) of the atoms directly attached to the stereocenter; the group having the atom of higher atomic number Z receives higher priority (i.e. number 1).
2. If there is a tie, the atoms at distance 2 from the stereocenter have to be considered: a list is made for each group of further atoms bonded to the one directly attached to the stereocenter. Each list is arranged in order of decreasing atomic number Z. Then the lists are compared atom by atom; at the earliest difference, the group containing the atom of higher atomic number Z receives higher priority.
3. If there is still a tie, each atom in each of the two lists is replaced with a sublist of the other atoms bonded to it (at distance 3 from the stereocenter), the sublists are arranged in decreasing order of atomic number Z, and the entire structure is again compared atom by atom. This process is repeated recursively, each time with atoms one bond farther from the stereocenter, until the tie is broken.

#### Isotopes

If two groups differ only in isotopes, then the larger atomic mass is used to set the priority.

#### Double and triple bonds

If an atom, A, is double-bonded to another atom, then atom A should be treated as though it is "connected to the same atom twice". An atom that is double-bonded has a higher priority than an atom that is single bonded. When dealing with double bonded priority groups, one is allowed to visit the same atom twice as one creates an arc.

When B is replaced with a list of attached atoms, A itself, but not its "phantom", is excluded in accordance with the general principle of not doubling back along a bond that has just been followed. A triple bond is handled the same way except that A and B are each connected to two phantom atoms of the other.

#### Geometrical isomers

If two substituents on an atom are geometric isomers of each other, the *Z*-isomer has higher priority than the *E*-isomer. A stereoisomer that contains two higher priority groups on the same face of the double bond (*cis*) is classified as "Z." The stereoisomer with two higher priority groups on opposite sides of a carbon-carbon double bond (*trans*) is classified as "E."

#### Cyclic molecules

To handle a molecule containing one or more cycles, one must first expand it into a tree (called a **hierarchical digraph**) by traversing bonds in all possible paths starting at the stereocenter. When the traversal encounters an atom through which the current path has already passed, a phantom atom is generated in order to keep the tree finite. A single atom of the original molecule may appear in many places (some as phantoms, some not) in the tree.

### Assigning descriptors

#### Stereocenters: *R*/*S*

A chiral sp3 hybridized isomer contains four different substituents. All four substituents are assigned priorities based on its atomic numbers. After the substituents of a stereocenter have been assigned their priorities, the molecule is oriented in space so that the group with the lowest priority is pointed away from the observer. If the substituents are numbered from 1 (highest priority) to 4 (lowest priority), then the sense of rotation of a curve passing through 1, 2 and 3 distinguishes the stereoisomers. In a configurational isomer, the lowest priority group (most times hydrogen) is positioned behind the plane or the hatched bond going away from the reader. The highest priority group will have an arc drawn connecting to the rest of the groups, finishing at the group of third priority. An arc drawn clockwise, has the *rectus* (*R*) assignment. An arc drawn counterclockwise, has the *sinister* (*S*) assignment. The names are derived from the Latin for 'right' and 'left', respectively. When naming an organic isomer, the abbreviation for either rectus or sinister assignment is placed in front of the name in parentheses. For example, 3-methyl-1-pentene with a rectus assignment is formatted as (*R*)-3-methyl-1-pentene.

A practical method of determining whether an enantiomer is *R* or *S* is by using the right-hand rule: one wraps the molecule with the fingers in the direction 1 → 2 → 3. If the thumb points in the direction of the fourth substituent, the enantiomer is *R*; otherwise, it is *S*.

It is possible in rare cases that two substituents on an atom differ only in their absolute configuration (*R* or *S*). If the relative priorities of these substituents need to be established, *R* takes priority over *S*. When this happens, the descriptor of the stereocenter is a lowercase letter (*r* or *s*) instead of the uppercase letter normally used.

#### Double bonds: *E*/*Z*

For double bonded molecules, Cahn–Ingold–Prelog priority rules (CIP rules) are followed to determine the priority of substituents of the double bond. If both of the high priority groups are on the same side of the double bond (*cis* configuration), then the stereoisomer is assigned the configuration *Z* (*zusammen,* German word meaning "together"). If the high priority groups are on opposite sides of the double bond (*trans* configuration), then the stereoisomer is assigned the configuration *E* (*entgegen*, German word meaning "opposed")

#### Coordination compounds

In some cases where stereogenic centers are formed, the configuration must be specified. Without the presence of a non-covalent interaction, a compound is achiral. Some professionals have proposed a new rule to account for this. This rule states that "non-covalent interactions have a fictitious number between 0 and 1" when assigning priority. Compounds in which this occurs are referred to as coordination compounds.

#### Spiro compounds

Some spiro compounds, for example the SDP ligands ((*R*)- and (*S*)-7,7'-bis(diphenylphosphaneyl)-2,2',3,3'-tetrahydro-1,1'-spirobi[indene]), represent chiral, C2-symmetrical molecules where the rings lie approximately at right angles to each other and each molecule cannot be superposed on its mirror image. The spiro carbon, C, is a stereogenic centre, and priority can be assigned a>a′>b>b′, in which one ring (both give the same answer) contains atoms a and b adjacent to the spiro carbon, and the other contains a′ and b′. The configuration at C may then be assigned as for any other stereocentre.

### Examples

The following are examples of application of the nomenclature.

| *R*/*S* assignments for several compounds |   |
|---|---|
|   | The hypothetical molecule bromochlorofluoroiodomethane shown in its (*R*)-configuration would be a very simple chiral compound. The priorities are assigned based on atomic number (*Z*): iodine (*Z* = 53) > bromine (*Z* = 35) > chlorine (*Z* = 17) > fluorine (*Z* = 9). Allowing fluorine (lowest priority, number 4) to point away from the viewer the rotation is clockwise hence the *R* assignment. |
|   | In the assignment of L-serine highest priority (i.e. number 1) is given to the nitrogen atom (*Z* = 7) in the amino group (NH2). Both the hydroxymethyl group (CH2OH) and the carboxylic acid group (COOH) have carbon atoms (*Z* = 6) but priority is given to the latter because the carbon atom in the COOH group is connected to a second oxygen (*Z* = 8) whereas in the CH2OH group carbon is connected to a hydrogen atom (*Z* = 1). Lowest priority (i.e. number 4) is given to the hydrogen atom and as this atom points away from the viewer, the counterclockwise decrease in priority over the three remaining substituents completes the assignment as *S*. |
|   | The stereocenter in (*S*)-carvone is connected to one hydrogen atom (not shown, priority 4) and three carbon atoms. The isopropenyl group has priority 1 (carbon atoms only), and for the two remaining carbon atoms, priority is decided with the carbon atoms two bonds removed from the stereocenter, one part of the keto group (O, O, C, priority number 2) and one part of an alkene (C, C, H, priority number 3). The resulting counterclockwise rotation results in *S*. |

## Describing multiple centers

If a compound has more than one chiral stereocenter, each center is denoted by either *R* or *S*. For example, ephedrine exists in (1*R*,2*S*) and (1*S*,2*R*) stereoisomers, which are distinct mirror-image forms of each other, making them enantiomers. This compound also exists as the two enantiomers written (1*R*,2*R*) and (1*S*,2*S*), which are named pseudoephedrine rather than ephedrine. All four of these isomers are named 2-methylamino-1-phenyl-1-propanol in systematic nomenclature. However, ephedrine and pseudoephedrine are diastereomers, or stereoisomers that are not enantiomers because they are not related as mirror-image copies. Pseudoephedrine and ephedrine are given different names because, as diastereomers, they have different chemical properties, even for racemic mixtures of each.

More generally, for any pair of enantiomers, all of the descriptors are opposite: (*R*,*R*) and (*S*,*S*) are enantiomers, as are (*R*,*S*) and (*S*,*R*). Diastereomers have at least one descriptor in common; for example (*R*,*S*) and (*R*,*R*) are diastereomers, as are (*S*,*R*) and (*S*,*S*). This holds true also for compounds having more than two stereocenters: if two stereoisomers have at least one descriptor in common, they are diastereomers. If all the descriptors are opposite, they are enantiomers.

A meso compound is an achiral molecule, despite having two or more stereogenic centers. A meso compound is superposable on its mirror image, therefore it reduces the number of stereoisomers predicted by the 2n rule. This occurs because the molecule obtains a plane of symmetry that causes the molecule to rotate around the central carbon–carbon bond. One example is meso-tartaric acid, in which (*R*,*S*) is the same as the (*S*,*R*) form. In meso compounds the *R* and *S* stereocenters occur in symmetrically positioned pairs.

## Relative configuration

The relative configuration of two stereoisomers may be denoted by the descriptors *R* and *S* with an asterisk (*). (*R**,*R**) means two centers having identical configurations, (*R*,*R*) or (*S*,*S*); (*R**,*S**) means two centers having opposite configurations, (*R*,*S*) or (*S*,*R*). To begin, the lowest-numbered (according to IUPAC systematic numbering) stereogenic center is given the *R** descriptor.

To designate two anomers the relative stereodescriptors alpha (α) and beta (β) are used. In the α anomer the *anomeric carbon atom* and the *reference atom* do have opposite configurations (*R*,*S*) or (*S*,*R*), whereas in the β anomer they are the same (*R*,*R*) or (*S*,*S*).

## Faces

Stereochemistry also plays a role assigning *faces* to trigonal molecules such as ketones. A nucleophile in a nucleophilic addition can approach the carbonyl group from two opposite sides or faces. When an achiral nucleophile attacks acetone, both faces are identical and there is only one reaction product. When the nucleophile attacks butanone, the faces are not identical (*enantiotopic*) and a racemic product results. When the nucleophile is a chiral molecule diastereoisomers are formed. When one face of a molecule is shielded by substituents or geometric constraints compared to the other face the faces are called diastereotopic. The same rules that determine the stereochemistry of a stereocenter (*R* or *S*) also apply when assigning the face of a molecular group. The faces are then called the ***Re*-face** and ***Si*-face**. In the example displayed on the right, the compound acetophenone is viewed from the *Re*-face. Hydride addition as in a reduction process from this side will form the (*S*)-enantiomer and attack from the opposite *Si*-face will give the (*R*)-enantiomer. However, adding a chemical group to the prochiral center from the *Re*-face will not always lead to an (*S*)-stereocenter, as the priority of the chemical group has to be taken into account. That is, the absolute stereochemistry of the product is determined on its own and not by considering which face it was attacked from. In the above-mentioned example, if chloride (*Z* = 17) were added to the prochiral center from the *Re*-face, this would result in an (*R*)-enantiomer.
