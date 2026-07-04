---
title: "Chirgwin–Coulson weights"
source: https://en.wikipedia.org/wiki/Chirgwin%E2%80%93Coulson_weights
domain: chirgwin-coulson-weights
license: CC-BY-SA-4.0
tags: chirgwin–coulson weights
fetched: 2026-07-04
---

# Chirgwin–Coulson weights

In modern valence bond (VB) theory calculations, **Chirgwin–Coulson weights** (also called Mulliken weights) are the relative weights of a set of possible VB structures of a molecule. Related methods of finding the relative weights of valence bond structures are the Löwdin and the inverse weights.

The weights are named after B. H. Chirgwin and Charles Coulson who developed it in 1950.

## Background

For a wave function $\Psi =\sum \limits _{i}C_{i}\Phi _{i}$ where $\Phi _{1},\Phi _{2},\dots ,\Phi _{n}$ are a linearly independent, orthogonal set of basis orbitals, the weight of a constituent orbital $\Psi _{i}$ would be $C_{i}^{2}$ since the overlap integral, $S_{ij}$ , between two wave functions $\Psi _{i},\Psi _{j}$ would be 1 for $i=j$ and 0 for $i\neq j$ . In valence bond theory, however, the generated structures are not necessarily orthogonal with each other, and oftentimes have substantial overlap between the two structures. As such, when considering non-orthogonal constituent orbitals (i.e. orbitals with non-zero overlap) the non-diagonal terms in the overlap matrix would be non-zero, and must be included in determining the weight of a constituent orbital. A method of computing the weight of a constituent orbital, $\Phi _{i}$ , proposed by Chirgwin and Coulson would be:

Chirgwin–Coulson formula

${\begin{aligned}W_{i}&=C_{i}\langle \Phi _{i}\vert \Psi \rangle =C_{i}\sum \limits _{j}C_{j}\langle \Psi _{i}\vert \Psi _{j}\rangle \\&=\sum \limits _{j}C_{i}C_{j}S_{ij}\end{aligned}}$

Application of the Chirgwin–Coulson formula to a molecular orbital yields the Mulliken population of the molecular orbital.

## Rigorous formulation

### Determination of VB Structures

#### Rumer's method

A method of creating a linearly independent, complete set of valence bond structures for a molecule was proposed by Yuri Rumer. For a system with n electrons and n orbitals, Rumer's method involves arranging the orbitals in a circle and connecting the orbitals together with lines that do not intersect one another. Covalent, or uncharged, structures can be created by connecting all of the orbitals with one another. Ionic, or charged, structures for a given atom can be determined by assigning a charge to a molecule, and then following Rumer's method. For the case of butadiene, the 20 possible Rumer structures are shown, where 1 and 2 are the covalent structures, 3-14 are the monoionic structures, and 15-20 are the diionic structures. The resulting VB structures can be represented by a linear combination of determinants $|a{\overline {b}}c{\overline {d}}|$ , where a letter without an over-line indicates an electron with $\alpha$ spin, while a letter with over-line indicates an electron with $\beta$ spin. The VB structure for 1, for example would be a linear combination of the determinants $|1{\overline {2}}3{\overline {4}}|$ , $|2{\overline {1}}3{\overline {4}}|$ , $|1{\overline {2}}4{\overline {3}}|$ , and $|2{\overline {1}}4{\overline {3}}|$ . For a monoanionic species, the VB structure for 11 would be a linear combination of $|1{\overline {2}}4{\overline {4}}|$ and $|2{\overline {1}}4{\overline {4}}|$ , namely:

$\phi _{11}={\frac {1}{\sqrt {2}}}(|1{\overline {2}}4{\overline {4}}|+|2{\overline {1}}4{\overline {4}}|)$

#### Matrix representation of VB structures

An arbitrary VB structure $|\varphi _{1}{\overline {\varphi _{2}}}\varphi _{3}{\overline {\varphi _{4}}}\dots |$ containing n electrons, represented by the electron indices $1,2,\dots ,n$ , and n orbitals, represented by $\varphi _{1},\varphi _{2},\dots ,\varphi _{n}$ , can be represented by the following Slater determinant:

$|\varphi _{1}{\overline {\varphi _{2}}}\varphi _{3}{\overline {\varphi _{4}}}\dots |={\frac {1}{\sqrt {n!}}}{\begin{vmatrix}\varphi _{1}(1)\alpha (1)&\varphi _{1}(2)\alpha (2)&\dots &\varphi _{1}(n)\alpha (n)\\\varphi _{2}(1)\beta (1)&\varphi _{2}(2)\beta (2)&\dots &\varphi _{2}(n)\beta (n)\\\vdots &\vdots &\ddots &\vdots \end{vmatrix}}$

Where $\alpha (k)$ and $\beta (k)$ represent an $\alpha$ or $\beta$ spin on the $k^{\text{th}}$ electron, respectively. For the case of a two electron system with orbitals a and b , the VB structure, $|a{\overline {b}}|$ , can be represented: $|a{\overline {b}}|={\frac {1}{\sqrt {2}}}{\begin{vmatrix}a(1)\alpha (1)&a(2)\alpha (2)\\b(1)\beta (1)&b(2)\beta (2)\end{vmatrix}}$

Evaluating the determinant yields:

$|a{\overline {b}}|={\frac {1}{\sqrt {2}}}(a(1)b(2)[\alpha (1)\beta (2)]-a(2)b(1)[\alpha (2)\beta (1)])$

### Definition of Chirgwin–Coulson weights

Given a wave function $\Psi =\sum \limits _{i}C_{i}\Phi _{i}$ where $\Phi _{1},\Phi _{2},\dots ,\Phi _{N}$ is a complete, linearly independent set of VB structures and $C_{k}$ is the coefficient of each structure, the Chirgwin-Coulson weight $W_{K}$ of a VB structure $\Phi _{K}$ can be computed in the following manner:

$W_{i}=\sum \limits _{j}C_{i}C_{j}\langle \Phi _{i}|\Phi _{j}\rangle =\sum \limits _{j}C_{i}C_{j}S_{ij}$

Where S is the overlap matrix satisfying $\langle \Phi _{i}|\Phi _{j}\rangle =S_{ij}$ .

Other methods of computing weights of VB structure include Löwdin weights, where $W_{i}^{\text{Lowdin}}=\sum \limits _{j,k}S_{ij}^{1/2}C_{j}S_{ik}^{1/2}C_{k}$ , and inverse weights, where $W_{i}^{\text{inverse}}={\frac {1}{N}}{\bigg (}{\frac {C_{i}^{2}}{(S^{-1})_{ii}}}{\bigg )}$ with N being a normalization factor defined by $N=\sum \limits _{i}{\frac {C_{i}^{2}}{(S^{-1})_{ii}}}$ . The use of Löwdin and inverse weights is appropriate when the Chirgwin–Coulson weights either exceed 1 or are negative.

### Half determinant decomposition of molecular orbitals

Given a set of molecular orbitals, $\Psi _{1},\Psi _{2},\dots ,\Psi _{m}$ , for a molecule, consider the determinant of a given orbital population, represented by $D_{\text{MO}}$ . The determinant can be written as the following Slater determinant:

$D_{\text{MO}}=|\Psi _{1}{\overline {\Psi }}_{1}\Psi _{2}{\overline {\Psi }}_{2}\dots |$

Computing the determinant explicitly by multiplying this expression can be a computationally difficult task, given that each molecular orbital is composed of a combination of atomic orbitals. On the other hand, because the determinant of a product of matrices is equal to the product of determinants, the determinant can be regrouped to half-determinants, one of which contains only electrons with $\alpha$ spin and the only with electrons of $\beta$ spin, that is: $D_{\text{MO}}=h_{\text{MO}}^{\alpha }h_{\text{MO}}^{\beta }$ where $h_{\text{MO}}^{\alpha }=|\phi _{1}\phi _{2}\dots |$ and $h_{\text{MO}}^{\beta }=|{\overline {\phi }}_{1}{\overline {\phi }}_{2}\dots |$ .

Note that any given molecular orbital $\Psi _{\text{MO}}$ can be written as a linear combination of atomic orbitals $\phi _{1},\phi _{2},\dots ,\phi _{n}$ , that is for each $\Psi _{i}$ , there exist $C_{ij}$ such that $\Psi _{i}=\sum \limits _{j}C_{ij}\phi _{j}$ . As such, the half determinant $h_{\text{MO}}^{\alpha }$ can be further decomposed into the half determinants for an ordering of atomic orbitals $h_{r}^{\alpha }=|\phi _{1},\phi _{2},\dots ,\phi _{n}|$ corresponding to a VB structure r . As such, the molecular orbital $\Psi _{i}$ can be represented as a combination of the half determinants of the atomic orbitals, $h_{\text{MO}}^{\alpha }=\sum \limits _{r}C_{r}^{\alpha }h_{r}^{\alpha }$ . The coefficient $C_{r}^{\alpha }$ can be determined by evaluating the following matrix:

$C_{r}^{\alpha }={\begin{vmatrix}C_{11}&C_{21}&\dots C_{n1}\\C_{12}&C_{22}&\dots C_{n2}\\\vdots &\vdots &\ddots \\C_{1n}&C_{2n}&\dots C_{nn}\\\end{vmatrix}}$

The same method can be used to evaluate the half determinant for the $\beta$ electrons, $h_{\text{MO}}^{\beta }$ . As such, the determinant $D_{\text{MO}}$ can be expressed as $D_{\text{MO}}=\sum \limits _{r,s}C_{r}^{\alpha }C_{r}^{\beta }h_{r}^{\alpha }h_{s}^{\beta }$ , where $r,s$ index across all possible VB structures.

## Sample computations for simple molecules

### Computations for the hydrogen molecule

The hydrogen molecule can be considered to be a linear combination of two ${\ce {H}}$ $1s$ orbitals, indicated as $\varphi _{1}$ and $\varphi _{2}$ . The possible VB structures for ${\ce {H_2}}$ are the two covalent structures, $|\varphi _{1}{\overline {\varphi _{2}}}|$ and $|\varphi _{2}{\overline {\varphi _{1}}}|$ indicated as 1 and 2 respectively, as well as the ionic structures $|\varphi _{1}{\overline {\varphi _{1}}}|$ and $|\varphi _{2}{\overline {\varphi _{2}}}|$ indicated as 3 and 4 respectively, shown below.

Because structures 1 and 2 both represent covalent bonding in the hydrogen molecule and exchanging the electrons of structure 1 yields structure 2, the two covalent structures can be combined into one wave function. As such, the Heitler-London model for bonding in ${\ce {H_2}}$ , $\Phi _{HL}$ , can be used in place of the VB structures $|\varphi _{1}{\overline {\varphi _{2}}}|$ and $|{\overline {\varphi _{1}}}\varphi _{2}|$ :

$\Phi _{HL}=|\varphi _{1}{\overline {\varphi _{2}}}|-|{\overline {\varphi _{1}}}\varphi _{2}|$

Where the negative sign arises from the antisymmetry of electron exchange. As such, the wave function for the ${\ce {H_2}}$ molecule, $\Psi _{{\text{H}}_{2}}$ , can be considered to be a linear combination of the Heitler-London structure and the two ionic valence bond structures.

$\Psi _{{\text{H}}_{2}}=C_{1}\Phi _{HL}+C_{2}|\varphi _{1}{\overline {\varphi _{1}}}|+C_{3}|\varphi _{2}{\overline {\varphi _{2}}}|$

The overlap matrix between the atomic orbitals between the three valence bond configurations $\Phi _{HL}$ , $|\varphi _{1}{\overline {\varphi _{1}}}|$ , and $|\varphi _{2}{\overline {\varphi _{2}}}|$ is given in the output for valence bond calculations. A sample output is given below:

$S={\begin{vmatrix}S_{11}\\S_{21}&S_{22}\\S_{31}&S_{32}&S_{33}\\\end{vmatrix}}={\begin{vmatrix}1\\0.77890423&1\\0.77890423&0.43543258&1\\\end{vmatrix}}$

Finding the eigenvectors of the matrix $H-ES=0$ , where H is the hamiltonian and E is energy due to orbital overlap, yields the VB-vector ${\vec {c}}$ , which satisfies:

$\Psi _{H}={\vec {c}}\{\Phi _{HL},|\varphi _{1}{\overline {\varphi _{1}}}|,|\varphi _{2}{\overline {\varphi _{2}}}|\}=C_{1}\Phi _{HL}+C_{2}|\varphi _{1}{\overline {\varphi _{1}}}|+C_{3}|\varphi _{2}{\overline {\varphi _{2}}}|$

Solving for the VB-vector ${\vec {c}}$ using density functional theory yields the coefficients $C_{1}=0.787469$ and $C_{2}=C_{3}=0.133870$ . Thus, the Coulson-Chrigwin weights can be computed:

$W_{1}=C_{1}^{2}S_{11}+C_{1}C_{2}S_{12}+C_{1}C_{3}S_{13}=0.784$

$W_{2}=W_{3}=0.108$

To check for consistency, the inverse weights can be computed by first determining the inverse of the overlap matrix:

$S^{-1}={\begin{vmatrix}6.46449\\-3.5078&3.13739\\-3.5078&1.36612&3.13739\\\end{vmatrix}}$

Next, the normalization constant N can be determined:

$N=\sum \limits _{K}{\frac {C_{K}^{2}}{(S^{-1})_{KK}}}=0.0185$

The final weights are: $W_{1}={\frac {1}{N}}{\bigg (}{\frac {C_{1}^{2}}{(S^{-1})_{11}}}{\bigg )}=0.803$ , and $W_{2}=W_{3}=0.098$ .

Informally, the computed weights indicate that the wave function for the ${\ce {H_2}}$ molecule has a minor contribution from an ionic species not predicted from a strictly MO model for bonding.

### Computations for ozone

Determining the relative weights of each resonance structure of ozone requires, first, the determination of the possible VB structures for ${\ce {O_3}}$ . Considering only the p orbitals of oxygen, and labeling the p orbital on the $i^{\text{th}}$ oxygen $\phi _{i}$ , ${\ce {O_3}}$ has 6 possible VB structures by Rumer's method. Assuming no atomic orbital overlap, the $k^{\text{th}}$ structure can be represented by the determinants $\Phi _{k}$ :

$\Phi _{1}={\frac {1}{\sqrt {2}}}(|\phi _{2}{\overline {\phi _{2}}}\phi _{1}{\overline {\phi _{3}}}|+|\phi _{2}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{1}}}|)$

$\Phi _{2}={\frac {1}{\sqrt {2}}}(|\phi _{1}{\overline {\phi _{1}}}\phi _{2}{\overline {\phi _{3}}}|+|\phi _{1}{\overline {\phi _{1}}}\phi _{3}{\overline {\phi _{2}}}|)$

$\Phi _{3}={\frac {1}{\sqrt {2}}}(|\phi _{1}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|+|\phi _{2}{\overline {\phi _{1}}}\phi _{3}{\overline {\phi _{3}}}|)$

$\Phi _{4}=|\phi _{1}{\overline {\phi _{1}}}\phi _{2}{\overline {\phi _{2}}}|$

$\Phi _{5}=|\phi _{2}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|$

$\Phi _{6}=|\phi _{1}{\overline {\phi _{1}}}\phi _{3}{\overline {\phi _{3}}}|$

${\ce {O_3}}$ has the following three molecular orbitals, one where all of the oxygen p orbitals are in phase, one where there is a node on the central oxygen, and one where all of the oxygen p orbitals are out of phase, shown below:

The wave functions for each of the molecular orbitals $\pi _{i}$ can be written as a linear combination of each of the oxygen p orbitals as follows:

${\begin{vmatrix}\pi _{1}\\\pi _{2}\\\pi _{3}\\\end{vmatrix}}={\begin{vmatrix}C_{11}&C_{12}&C_{13}\\C_{21}&C_{22}&C_{23}\\C_{31}&C_{32}&C_{33}\\\end{vmatrix}}{\begin{vmatrix}\phi _{1}\\\phi _{2}\\\phi _{3}\\\end{vmatrix}}={\begin{vmatrix}0.368&0.764&0.368\\0.710&0&-0.710\\0.614&-0.671&0.614\\\end{vmatrix}}{\begin{vmatrix}\phi _{1}\\\phi _{2}\\\phi _{3}\\\end{vmatrix}}$

Where $C_{ij}$ indicates the coefficient of $\phi _{j}$ in a molecular orbital $\pi _{i}$ . Consider, the VB contributions for the ground state of ${\ce {O_3}}$ , $|\pi _{1}{\overline {\pi _{1}}}\pi _{2}{\overline {\pi _{2}}}|$ . Using the methods of half determinants, the half determinants for the ground state are:

$|\phi _{1}\phi _{2}|_{g}={\begin{Vmatrix}C_{11}&C_{12}\\C_{21}&C_{22}\\\end{Vmatrix}}=-0.542$

$|\phi _{2}\phi _{3}|_{g}={\begin{Vmatrix}C_{12}&C_{13}\\C_{22}&C_{23}\\\end{Vmatrix}}=-0.542$

$|\phi _{1}\phi _{3}|_{g}={\begin{Vmatrix}C_{11}&C_{13}\\C_{21}&C_{23}\\\end{Vmatrix}}=-0.523$

By the method of half determinant expansion, the coefficient, $C_{i}$ , for a structure $|\phi _{i}{\overline {\phi _{j}}}\phi _{k}{\overline {\phi _{l}}}|$ is:

$|\phi _{i}{\overline {\phi _{j}}}\phi _{k}{\overline {\phi _{l}}}|=|\phi _{i}\phi _{k}||\phi _{j}\phi _{l}|$

Which implies that the ground state has the following coefficients:

${\begin{aligned}\Psi _{g}&=-0.416\Phi _{1}+0.400\Phi _{2}+0.400\Phi _{3}+0.294\Phi _{4}+0.294\Phi _{5}+0.274\Phi _{6}\\&=-0.294(|\phi _{2}{\overline {\phi _{2}}}\phi _{1}{\overline {\phi _{3}}}|+|\phi _{2}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{1}}}|)+0.283(|\phi _{1}{\overline {\phi _{1}}}\phi _{2}{\overline {\phi _{3}}}|+|\phi _{1}{\overline {\phi _{1}}}\phi _{3}{\overline {\phi _{2}}}|)+0.283(|\phi _{1}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|+|\phi _{2}{\overline {\phi _{1}}}\phi _{3}{\overline {\phi _{3}}}|)+\\&\quad \quad 0.294|\phi _{1}{\overline {\phi _{1}}}\phi _{2}{\overline {\phi _{2}}}|+0.294|\phi _{2}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|+0.274|\phi _{1}{\overline {\phi _{1}}}\phi _{3}{\overline {\phi _{3}}}|\end{aligned}}$

Given the following overlap matrix for the half determinants:

$S={\begin{vmatrix}\langle |\phi _{1}\phi _{2}|||\phi _{1}\phi _{2}|\rangle \\\langle |\phi _{1}\phi _{2}|||\phi _{1}\phi _{3}|\rangle &\langle |\phi _{1}\phi _{3}|||\phi _{1}\phi _{3}|\rangle \\\langle |\phi _{1}\phi _{2}|||\phi _{2}\phi _{3}|\rangle &\langle |\phi _{1}\phi _{3}|||\phi _{2}\phi _{3}|\rangle &\langle |\phi _{2}\phi _{3}|||\phi _{2}\phi _{3}|\rangle \end{vmatrix}}={\begin{vmatrix}0.98377\\0.12634&0.99993\\0.00810&0.12634&0.98377\end{vmatrix}}$

The overlap between two VB structures represented by the product of two VB determinants $\langle |\phi _{a}{\overline {\phi _{b}}}\phi _{c}{\overline {\phi _{d}}}|||\phi _{w}{\overline {\phi _{x}}}\phi _{y}{\overline {\phi _{z}}}|\rangle$ can be evaluated by finding the product of the overlap between the two half determinants, that is:

$\langle |\phi _{a}{\overline {\phi _{b}}}\phi _{c}{\overline {\phi _{d}}}|||\phi _{w}{\overline {\phi _{x}}}\phi _{y}{\overline {\phi _{z}}}|\rangle =(\langle |\phi _{a}\phi _{c}|||\phi _{w}\phi _{y}|\rangle )(\langle |\phi _{b}\phi _{d}|||\phi _{x}\phi _{z}|\rangle )$

For example, the overlap between the orbitals $|\phi _{1}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|$ and $|\phi _{1}{\overline {\phi _{2}}}\phi _{2}{\overline {\phi _{3}}}|$ would be:

$\langle |\phi _{1}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|||\phi _{1}{\overline {\phi _{2}}}\phi _{2}{\overline {\phi _{3}}}|\rangle =(\langle |\phi _{1}\phi _{3}|||\phi _{1}\phi _{2}|\rangle )(\langle |\phi _{2}\phi _{3}|||\phi _{2}\phi _{3}|\rangle )=(0.12634)(0.98377)=0.12429$

The weights of the standard Lewis structures for ${\ce {O_3}}$ would be $W(\Psi _{2})$ and $W(\Psi _{3})$ . The weights can be found by first computing the Chirgwin–Coulson weights for their constituent determinants:

${\begin{aligned}W(|\phi _{1}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|)&=\sum \limits _{k}0.283C_{k}\langle |\phi _{1}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|||\Phi _{k}|\rangle \\&=0.283[-0.294(\langle |\phi _{1}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|||\phi _{2}{\overline {\phi _{2}}}\phi _{1}{\overline {\phi _{3}}}|\rangle +\langle |\phi _{1}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|||\phi _{2}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{1}}}|\rangle )+0.283(\langle |\phi _{1}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|||\phi _{1}{\overline {\phi _{1}}}\phi _{2}{\overline {\phi _{3}}}|\rangle +\langle |\phi _{1}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|||\phi _{1}{\overline {\phi _{1}}}\phi _{3}{\overline {\phi _{2}}}|\rangle )\\&\quad \quad +0.283(\langle |\phi _{1}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|||\phi _{1}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|\rangle +\langle |\phi _{1}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|||\phi _{2}{\overline {\phi _{1}}}\phi _{3}{\overline {\phi _{3}}}|\rangle )+0.294\langle |\phi _{1}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|||\phi _{1}{\overline {\phi _{1}}}\phi _{2}{\overline {\phi _{2}}}|\rangle +0.294\langle |\phi _{1}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|||\phi _{2}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|\rangle \\&\quad \quad +0.274\langle |\phi _{1}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|||\phi _{1}{\overline {\phi _{1}}}\phi _{3}{\overline {\phi _{3}}}|\rangle ]\\&=0.111\end{aligned}}$

$W(|\phi _{2}{\overline {\phi _{1}}}\phi _{3}{\overline {\phi _{3}}}|)=W(|\phi _{1}{\overline {\phi _{1}}}\phi _{2}{\overline {\phi _{3}}}|)=W(|\phi _{1}{\overline {\phi _{1}}}\phi _{3}{\overline {\phi _{2}}}|)=0.111$

The weights for the standard lewis structures would be the sum of the weights of the constituent determinants. As such:

$W(\Psi _{2})=W(|\phi _{1}{\overline {\phi _{1}}}\phi _{2}{\overline {\phi _{3}}}|)+W(|\phi _{1}{\overline {\phi _{1}}}\phi _{3}{\overline {\phi _{2}}}|)=0.222$

$W(\Psi _{3})=W(|\phi _{1}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{3}}}|)+W(|\phi _{2}{\overline {\phi _{1}}}\phi _{3}{\overline {\phi _{3}}}|)=0.222$

This compares well with reported Chirgwin–Coulson weights of 0.226 for the standard Lewis structure of ozone in the ground state.

For the diradical state, $\Psi _{1}$ , the weight is:

$W(|\phi _{2}{\overline {\phi _{2}}}\phi _{1}{\overline {\phi _{3}}}|)=\sum \limits _{k}-0.294C_{k}|\phi _{2}{\overline {\phi _{2}}}\phi _{1}{\overline {\phi _{3}}}||\Phi _{k}|=0.106$

$W(|\phi _{2}{\overline {\phi _{2}}}\phi _{3}{\overline {\phi _{1}}}|)=0.106$

$W(\Psi _{1})=W(|\phi _{2}{\overline {\phi }}_{2}\phi _{1}{\overline {\phi }}_{3}|)+W(|\phi _{2}{\overline {\phi }}_{2}\phi _{1}{\overline {\phi }}_{3}|)=0.106+0.106=0.212$

This also compares favorably with reported Chirgwin–Coulson weights of 0.213 for the diradical state of ozone in the ground state.

## Applications to main group compounds

### Borazine

Borazine, (chemical formula ${\ce {B_3N_3H_6}}$ ) is a cyclic, planar compound that is isoelectronic with benzene. Given the lone pair in the nitrogen p orbital out of the plane and the empty p orbital of boron, the following resonance structure is possible:

However, VB calculations using a double-zeta D95 basis set indicate that the predominant resonance structures are the structure with all three lone pairs on the nitrogen (labeled 1 below) and the six resonance structures with one double bond between boron and nitrogen (labeled 2 below). The relative weights of the two structures are 0.17 and 0.08 respectively.

By contrast, the dominant resonance structures of benzene are the two Kekule structures, with weight 0.15, and 12 monozwitterionic structures with weight 0.03. The data, together, indicate that, despite the similarity in appearance and structure, the electrons on borazine are less delocalized than those on benzene.

### S2N2

Disulfur dinitride is a square planar compound that contains a 6 electron conjugated $\pi$ system. The primary diradical resonance structures (1 and 2) and a secondary zwitterionic structure (3) are shown below:

Valence bond calculations using the Dunning's D95 full double-zeta basis set indicate that the dominant resonance structure is the singlet diradical with a long nitrogen-nitrogen bond (structure 1), with Chirgwin–Coulson weight 0.47. This value is substantially higher than the weight for the singlet diradical centered on the sulfurs (structure 2), which has a Chirgwin–Coulson weight of 0.06. This result corresponds nicely with the general rules regarding Lewis structures, namely that formal charges ought to be minimized, and contrasts with earlier computational results indicating that 1 is the dominant structure.
