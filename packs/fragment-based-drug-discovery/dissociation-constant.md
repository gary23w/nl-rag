---
title: "Dissociation constant"
source: https://en.wikipedia.org/wiki/Dissociation_constant
domain: fragment-based-drug-discovery
license: CC-BY-SA-4.0
tags: fragment library, weak binder, surface plasmon resonance, growing
fetched: 2026-07-02
---

# Dissociation constant

In chemistry, biochemistry, and pharmacology, a **dissociation constant** (*K*D) is a specific type of equilibrium constant that measures the propensity of a larger object to separate (dissociate) reversibly into smaller components, as when a complex falls apart into its component molecules, or when a salt splits up into its component ions. The dissociation constant is the inverse of the association constant. In the special case of salts, the dissociation constant can also be called an ionization constant. For a general reaction:

${\ce {A_{\mathit {x}}B_{\mathit {y}}<=>{\mathit {x}}A{}+{\mathit {y}}B}}$

in which a complex ${\ce {A}}_{x}{\ce {B}}_{y}$ breaks down into *x* A subunits and *y* B subunits, the dissociation constant is defined as

$K_{\mathrm {D} }={\frac {[{\ce {A}}]^{x}[{\ce {B}}]^{y}}{[{\ce {A}}_{x}{\ce {B}}_{y}]}}$

where [A], [B], and [A*x* B*y*] are the equilibrium concentrations of A, B, and the complex A*x* B*y*, respectively.

One reason for the popularity of the dissociation constant in biochemistry and pharmacology is that in the frequently encountered case where *x* = *y* = 1, *K*D has a simple physical interpretation: when [A] = *K*D, then [B] = [AB] or, equivalently, ${\tfrac {[{\ce {AB}}]}{{[{\ce {B}}]}+[{\ce {AB}}]}}={\tfrac {1}{2}}$ . That is, *K*D, which has the dimensions of concentration, equals the concentration of free A at which half of the total molecules of B are associated with A. This simple interpretation does not apply for higher values of *x* or *y*. It also presumes the absence of competing reactions, though the derivation can be extended to explicitly allow for and describe competitive binding. It is useful as a quick description of the binding of a substance, in the same way that EC50 and IC50 describe the biological activities of substances.

## Concentration of bound molecules

### Molecules with one binding site

Experimentally, the concentration of the molecule complex [AB] is obtained indirectly from the measurement of the concentration of a free molecules, either [A] or [B]. In principle, the total amounts of molecule [A]0 and [B]0 added to the reaction are known. They separate into free and bound components according to the mass conservation principle:

${\begin{aligned}{\ce {[A]_0}}&={\ce {{[A]}+ [AB]}}\\{\ce {[B]_0}}&={\ce {{[B]}+ [AB]}}\end{aligned}}$

To track the concentration of the complex [AB], one substitutes the concentration of the free molecules ([A] or [B]), of the respective conservation equations, by the definition of the dissociation constant,

$[{\ce {A}}]_{0}=K_{\mathrm {D} }{\frac {[{\ce {AB}}]}{[{\ce {B}}]}}+[{\ce {AB}}]$

This yields the concentration of the complex related to the concentration of either one of the free molecules

${\ce {[AB]}}={\frac {\ce {[A]_{0}[B]}}{K_{\mathrm {D} }+[{\ce {B}}]}}={\frac {\ce {[B]_{0}[A]}}{K_{\mathrm {D} }+[{\ce {A}}]}}$

### Macromolecules with identical independent binding sites

Many biological proteins and enzymes can possess more than one binding site. Usually, when a ligand L binds with a macromolecule M, it can influence binding kinetics of other ligands L binding to the macromolecule. A simplified mechanism can be formulated if the affinity of all binding sites can be considered independent of the number of ligands bound to the macromolecule. This is valid for macromolecules composed of more than one, mostly identical, subunits. It can be then assumed that each of these n subunits are identical, symmetric and that they possess only a single binding site. Then the concentration of bound ligands ${\ce {[L]_{bound}}}$ becomes

${\ce {[L]}}_{\text{bound}}={\frac {n{\ce {[M]}}_{0}{\ce {[L]}}}{K_{\mathrm {D} }+{\ce {[L]}}}}$

In this case, ${\ce {[L]}}_{\text{bound}}\neq {\ce {[LM]}}$ , but comprises all partially saturated forms of the macromolecule:

${\ce {[L]}}_{\text{bound}}={\ce {[LM]}}+{\ce {2[L_{2}M]}}+{\ce {3[L_{3}M]}}+\ldots +n{\ce {[L_{\mathit {n}}M]}}$

where the saturation occurs stepwise

${\begin{aligned}{\ce {{[L]}+[M]}}&{\ce {{}<=>{[LM]}}}&K'_{1}&={\frac {\ce {[L][M]}}{[LM]}}&{\ce {[LM]}}&={\frac {\ce {[L][M]}}{K'_{1}}}\\{\ce {{[L]}+[LM]}}&{\ce {{}<=>{[L2M]}}}&K'_{2}&={\frac {\ce {[L][LM]}}{[L_{2}M]}}&{\ce {[L_{2}M]}}&={\frac {\ce {[L]^{2}[M]}}{K'_{1}K'_{2}}}\\{\ce {{[L]}+[L2M]}}&{\ce {{}<=>{[L3M]}}}&K'_{3}&={\frac {\ce {[L][L_{2}M]}}{[L_{3}M]}}&{\ce {[L_{3}M]}}&={\frac {\ce {[L]^{3}[M]}}{K'_{1}K'_{2}K'_{3}}}\\&\vdots &&\vdots &&\vdots \\{\ce {{[L]}+[L_{\mathit {n-1}}M]}}&{\ce {{}<=>{[L_{\mathit {n}}M]}}}&K'_{n}&={\frac {\ce {[L][L_{n-1}M]}}{[L_{n}M]}}&{\ce {[L_{n}M]}}&={\frac {\ce {[L]^{n}[M]}}{K'_{1}K'_{2}K'_{3}\cdots K'_{n}}}\end{aligned}}$

For the derivation of the general binding equation a saturation function r is defined as the quotient from the portion of bound ligand to the total amount of the macromolecule:

$r={\frac {\ce {[L]_{bound}}}{\ce {[M]_{0}}}}={\frac {\ce {{[LM]}+{2[L_{2}M]}+{3[L_{3}M]}+...+{\mathit {n}}[L_{\mathit {n}}M]}}{\ce {{[M]}+{[LM]}+{[L_{2}M]}+{[L_{3}M]}+...+[L_{\mathit {n}}M]}}}={\frac {\sum _{i=1}^{n}\left({\frac {i[{\ce {L}}]^{i}}{\prod _{j=1}^{i}K_{j}'}}\right)}{1+\sum _{i=1}^{n}\left({\frac {[{\ce {L}}]^{i}}{\prod _{j=1}^{i}K_{j}'}}\right)}}$

*K′n* are so-called macroscopic or apparent dissociation constants and can result from multiple individual reactions. For example, if a macromolecule *M* has three binding sites, *K′*1 describes a ligand being bound to any of the three binding sites. In this example, *K′*2 describes two molecules being bound and *K′3* three molecules being bound to the macromolecule. The microscopic or individual dissociation constant describes the equilibrium of ligands binding to specific binding sites. Because we assume identical binding sites with no cooperativity, the microscopic dissociation constant must be equal for every binding site and can be abbreviated simply as *K*D. In our example, *K′*1 is the amalgamation of a ligand binding to either of the three possible binding sites (I, II and III), hence three microscopic dissociation constants and three distinct states of the ligand–macromolecule complex. For *K′*2 there are six different microscopic dissociation constants (I–II, I–III, II–I, II–III, III–I, III–II) but only three distinct states (it does not matter whether you bind pocket I first and then II or II first and then I). For *K′*3 there are three different dissociation constants — there are only three possibilities for which pocket is filled last (I, II or III) — and one state (I–II–III).

Even when the microscopic dissociation constant is the same for each individual binding event, the macroscopic outcome (*K′*1, *K′*2 and *K′*3) is not equal. This can be understood intuitively for our example of three possible binding sites. *K′*1 describes the reaction from one state (no ligand bound) to three states (one ligand bound to either of the three binding sides). The apparent *K′*1 would therefore be three times smaller than the individual *K*D. *K′*2 describes the reaction from three states (one ligand bound) to three states (two ligands bound); therefore, *K′*2 would be equal to *K*D. *K′*3 describes the reaction from three states (two ligands bound) to one state (three ligands bound); hence, the apparent dissociation constant *K′*3 is three times bigger than the microscopic dissociation constant *K*D. The general relationship between both types of dissociation constants for *n* binding sites is

$K_{i}'=K_{\mathrm {D} }{\frac {i}{n-i+1}}$

Hence, the ratio of bound ligand to macromolecules becomes

$r={\frac {\sum _{i=1}^{n}i\left(\prod _{j=1}^{i}{\frac {n-j+1}{j}}\right)\left({\frac {{\ce {[L]}}}{K_{\mathrm {D} }}}\right)^{i}}{1+\sum _{i=1}^{n}\left(\prod _{j=1}^{i}{\frac {n-j+1}{j}}\right)\left({\frac {[L]}{K_{\mathrm {D} }}}\right)^{i}}}={\frac {\sum _{i=1}^{n}i{\binom {n}{i}}\left({\frac {[L]}{K_{\mathrm {D} }}}\right)^{i}}{1+\sum _{i=1}^{n}{\binom {n}{i}}\left({\frac {{\ce {[L]}}}{K_{\mathrm {D} }}}\right)^{i}}}$

where ${\binom {n}{i}}={\frac {n!}{(n-i)!i!}}$ is the binomial coefficient. Then the first equation is proved by applying the binomial rule

$r={\frac {n\left({\frac {\ce {[L]}}{K_{\mathrm {D} }}}\right)\left(1+{\frac {\ce {[L]}}{K_{\mathrm {D} }}}\right)^{n-1}}{\left(1+{\frac {\ce {[L]}}{K_{\mathrm {D} }}}\right)^{n}}}={\frac {n\left({\frac {\ce {[L]}}{K_{\mathrm {D} }}}\right)}{\left(1+{\frac {\ce {[L]}}{K_{\mathrm {D} }}}\right)}}={\frac {n[{\ce {L}}]}{K_{\mathrm {D} }+[{\ce {L}}]}}={\frac {\ce {[L]_{bound}}}{\ce {[M]_{0}}}}$

## Protein–ligand binding

The dissociation constant is commonly used to describe the affinity between a ligand ${\ce {L}}$ (such as a drug) and a protein ${\ce {P}}$ ; i.e., how tightly a ligand binds to a particular protein. Ligand–protein affinities are influenced by non-covalent intermolecular interactions between the two molecules such as hydrogen bonding, electrostatic interactions, hydrophobic and van der Waals forces. Affinities can also be affected by high concentrations of other macromolecules, which causes macromolecular crowding.

The formation of a ligand–protein complex ${\ce {LP}}$ can be described by a two-state process

${\ce {L + P <=> LP}}$

the corresponding dissociation constant is defined

$K_{\mathrm {D} }={\frac {\left[{\ce {L}}\right]\left[{\ce {P}}\right]}{\left[{\ce {LP}}\right]}}$

where ${\ce {[P], [L]}}$ , and ${\ce {[LP]}}$ represent molar concentrations of the protein, ligand, and protein–ligand complex, respectively.

The dissociation constant has molar units (M) and corresponds to the ligand concentration ${\ce {[L]}}$ at which half of the proteins are occupied at equilibrium, i.e., the concentration of ligand at which the concentration of protein with ligand bound ${\ce {[LP]}}$ equals the concentration of protein with no ligand bound ${\ce {[P]}}$ . The smaller the dissociation constant, the more tightly bound the ligand is, or the higher the affinity between ligand and protein. For example, a ligand with a nanomolar (nM) dissociation constant binds more tightly to a particular protein than a ligand with a micromolar (μM) dissociation constant.

Sub-picomolar dissociation constants as a result of non-covalent binding interactions between two molecules are rare. Nevertheless, there are some important exceptions. Biotin and avidin bind with a dissociation constant of roughly 10−15 M = 1 fM = 0.000001 nM. Ribonuclease inhibitor proteins may also bind to ribonuclease with a similar 10−15 M affinity.

The dissociation constant for a particular ligand–protein interaction can change with solution conditions (e.g., temperature, pH and salt concentration). The effect of different solution conditions is to effectively modify the strength of any intermolecular interactions holding a particular ligand–protein complex together.

Drugs can produce harmful side effects through interactions with proteins for which they were not meant to or designed to interact. Therefore, much pharmaceutical research is aimed at designing drugs that bind to only their target proteins (negative design) with high affinity (typically 0.1–10 nM) or at improving the affinity between a particular drug and its *in vivo* protein target (positive design).

### Antibodies

In the specific case of antibodies (Ab) binding to antigen (Ag), usually the term **affinity constant** refers to the association constant.

${\ce {Ab + Ag <=> AbAg}}$

$K_{\mathrm {A} }={\frac {\left[{\ce {AbAg}}\right]}{\left[{\ce {Ab}}\right]\left[{\ce {Ag}}\right]}}={\frac {1}{K_{\mathrm {D} }}}$

This chemical equilibrium is also the ratio of the on-rate (*k*forward or *k*a) and off-rate (*k*back or *k*d) constants. Two antibodies can have the same affinity, but one may have both a high on- and off-rate constant, while the other may have both a low on- and off-rate constant.

$K_{A}={\frac {k_{\text{forward}}}{k_{\text{back}}}}={\frac {\mbox{on-rate}}{\mbox{off-rate}}}$

## Acid–base reactions

For the deprotonation of acids, *K* is known as *K*a, the acid dissociation constant. Strong acids, such as sulfuric or phosphoric acid, have large dissociation constants; weak acids, such as acetic acid, have small dissociation constants.

The symbol *K*a, used for the acid dissociation constant, can lead to confusion with the association constant, and it may be necessary to see the reaction or the equilibrium expression to know which is meant.

Acid dissociation constants are sometimes expressed by p*K*a, which is defined by

${\text{p}}K_{\text{a}}=-\log _{10}{K_{\mathrm {a} }}$

This $\mathrm {p} K$ notation is seen in other contexts as well; it is mainly used for covalent dissociations (i.e., reactions in which chemical bonds are made or broken) since such dissociation constants can vary greatly.

A molecule can have several acid dissociation constants. In this regard, that is depending on the number of the protons they can give up, we define *monoprotic*, *diprotic* and *triprotic* acids. The first (e.g., acetic acid or ammonium) have only one dissociable group, the second (e.g., carbonic acid, bicarbonate, glycine) have two dissociable groups and the third (e.g., phosphoric acid) have three dissociable groups. In the case of multiple p*K* values they are designated by indices: p*K*1, p*K*2, p*K*3 and so on. For amino acids, the p*K*1 constant refers to its carboxyl (–COOH) group, p*K*2 refers to its amino (–NH2) group and the p*K*3 is the p*K* value of its side chain.

${\begin{aligned}{\ce {H3B}}&{\ce {{}<=>{H+}+{H2B^{-}}}}&K_{1}&={\ce {[H+].[H2B^{-}] \over [H3B]}}&\mathrm {p} K_{1}&=-\log K_{1}\\{\ce {H2B^{-}}}&{\ce {{}<=>{H+}+{HB^{2-}}}}&K_{2}&={\ce {[H+].[HB^{2-}] \over [H2B^{-}]}}&\mathrm {p} K_{2}&=-\log K_{2}\\{\ce {HB^{-2}}}&{\ce {{}<=>{H+}+{B^{3-}}}}&K_{3}&={\ce {[H+].[B^{3-}] \over [HB^{2-}]}}&\mathrm {p} K_{3}&=-\log K_{3}\end{aligned}}$

## Dissociation constant of water

The dissociation constant of water is denoted *K*w:

$K_{\mathrm {w} }=[{\ce {H}}^{+}][{\ce {OH}}^{-}]$

The concentration of water, [H2O], is omitted by convention, which means that the value of *K*w differs from the value of *K*eq that would be computed using that concentration.

The value of *K*w varies with temperature, as shown in the table below. This variation must be taken into account when making precise measurements of quantities such as pH.

| Water temperature | *K*w | p*K*w |
|---|---|---|
| 000 °C | 00.112×10−14 | 14.95 |
| 025 °C | 01.023×10−14 | 13.99 |
| 050 °C | 05.495×10−14 | 13.26 |
| 075 °C | 19.950×10−14 | 12.70 |
| 100 °C | 56.230×10−14 | 12.25 |
