---
title: "Born–Oppenheimer approximation"
source: https://en.wikipedia.org/wiki/Born%E2%80%93Oppenheimer_approximation
domain: quantum-chemistry-methods
license: CC-BY-SA-4.0
tags: quantum chemistry methods, born oppenheimer approximation, slater determinant, coupled cluster
fetched: 2026-07-02
---

# Born–Oppenheimer approximation

In quantum chemistry and molecular physics, the **Born–Oppenheimer** (**BO**) **approximation** is the assumption that the wave functions of atomic nuclei and electrons in a molecule can be treated separately, based on the fact that the nuclei are much heavier than the electrons. Due to the larger relative mass of a nucleus compared to an electron, the coordinates of the nuclei in a system are approximated as fixed, while the coordinates of the electrons are dynamic. The approach is named after Max Born and his 23-year-old graduate student J. Robert Oppenheimer, the latter of whom proposed it in 1927 during a period of intense ferment in the development of quantum mechanics.

The approximation is widely used in quantum chemistry to speed up the computation of molecular wavefunctions and other properties for large molecules. There are cases where the assumption of separable motion no longer holds, which make the approximation lose validity (it is said to "break down"), but even then the approximation is usually used as a starting point for more refined methods.

In molecular spectroscopy, using the BO approximation means considering molecular energy as a sum of independent terms, e.g.: $E_{\text{total}}=E_{\text{electronic}}+E_{\text{vibrational}}+E_{\text{rotational}}+E_{\text{nuclear spin}}.$ These terms are of different orders of magnitude and the nuclear spin energy is so small that it is often omitted. The electronic energies $E_{\text{electronic}}$ consist of kinetic energies, interelectronic repulsions, internuclear repulsions, and electron–nuclear attractions, which are the terms typically included when computing the electronic structure of molecules.

## Example

The benzene molecule consists of 12 nuclei and 42 electrons. The Schrödinger equation, which must be solved to obtain the energy levels and wavefunction of this molecule, is a partial differential eigenvalue equation in the three-dimensional coordinates of the nuclei and electrons, giving 3 × 12 = 36 nuclear plus 3 × 42 = 126 electronic, totalling 162 variables for the wave function. The computational complexity, i.e., the computational power required to solve an eigenvalue equation, increases faster than the square of the number of coordinates.

When applying the BO approximation, two smaller, consecutive steps can be used: For a given position of the nuclei, the *electronic* Schrödinger equation is solved, while treating the nuclei as stationary (not "coupled" with the dynamics of the electrons). This corresponding eigenvalue problem then consists only of the 126 electronic coordinates. This electronic computation is then repeated for other possible positions of the nuclei, i.e. deformations of the molecule. For benzene, this could be done using a grid of 36 possible nuclear position coordinates. The electronic energies on this grid are then connected to give a potential energy surface for the nuclei. This potential is then used for a second Schrödinger equation containing only the 36 coordinates of the nuclei.

So, taking the most optimistic estimate for the complexity, instead of a large equation requiring at least $162^{2}=26\,244$ hypothetical calculation steps, a series of smaller calculations requiring $126^{2}N=15\,876\,N$ (with *N* being the number of grid points for the potential) and a very small calculation requiring $36^{2}=1296$ steps can be performed. In practice, the scaling of the problem is larger than $n^{2}$ , and more approximations are applied in computational chemistry to further reduce the number of variables and dimensions.

The slope of the potential energy surface can be used to simulate molecular dynamics, using it to express the mean force on the nuclei caused by the electrons and thereby skipping the calculation of the nuclear Schrödinger equation.

## Detailed description

The BO approximation recognizes the large difference between the electron mass and the masses of atomic nuclei, and correspondingly the time scales of their motion. Given the same amount of momentum, the nuclei move much more slowly than the electrons. In mathematical terms, the BO approximation consists of expressing the wavefunction ( $\Psi _{\mathrm {total} }$ ) of a molecule as the product of an electronic wavefunction and a nuclear (vibrational, rotational) wavefunction. $\Psi _{\mathrm {total} }=\psi _{\mathrm {electronic} }\psi _{\mathrm {nuclear} }$ . This enables a separation of the Hamiltonian operator into electronic and nuclear terms, where cross-terms between electrons and nuclei are neglected, so that the two smaller and decoupled systems can be solved more efficiently.

In the first step, the nuclear kinetic energy is neglected, that is, the corresponding operator *T*n is subtracted from the total molecular Hamiltonian. In the remaining electronic Hamiltonian *H*e the nuclear positions are no longer variable, but are constant parameters (they enter the equation "parametrically"). The electron–nucleus interactions are *not* removed, i.e., the electrons still "feel" the Coulomb potential of the nuclei clamped at certain positions in space. (This first step of the BO approximation is therefore often referred to as the *clamped-nuclei* approximation.)

The electronic Schrödinger equation

$H_{\text{e}}(\mathbf {r} ,\mathbf {R} )\chi (\mathbf {r} ,\mathbf {R} )=E_{\text{e}}\chi (\mathbf {r} ,\mathbf {R} )$

where $\chi (\mathbf {r} ,\mathbf {R} )$ , the electronic wavefunction for given positions of nuclei (fixed **R**), is solved approximately. The quantity **r** stands for all electronic coordinates and **R** for all nuclear coordinates. The electronic energy eigenvalue *E*e depends on the chosen positions **R** of the nuclei. Varying these positions **R** in small steps and repeatedly solving the electronic Schrödinger equation, one obtains *E*e as a function of **R**. This is the potential energy surface (PES): $E_{e}(\mathbf {R} )$ . Because this procedure of recomputing the electronic wave functions as a function of an infinitesimally changing nuclear geometry is reminiscent of the conditions for the adiabatic theorem, this manner of obtaining a PES is often referred to as the *adiabatic approximation* and the PES itself is called an *adiabatic surface*.

In the second step of the BO approximation, the nuclear kinetic energy *T*n (containing partial derivatives with respect to the components of **R**) is reintroduced, and the Schrödinger equation for the nuclear motion

$[T_{\text{n}}+E_{\text{e}}(\mathbf {R} )]\phi (\mathbf {R} )=E\phi (\mathbf {R} )$

where $\phi (\mathbf {R} )$ is the nuclear wavefunction, is solved. This second step of the BO approximation involves separation of vibrational, translational, and rotational motions. This can be achieved by application of the Eckart conditions. The eigenvalue *E* is the total energy of the molecule, including contributions from electrons, nuclear vibrations, and overall rotation and translation of the molecule. In accord with the Hellmann–Feynman theorem, the nuclear potential is taken to be an average over electron configurations of the sum of the electron–nuclear and internuclear electric potentials.

## Derivation

It will be discussed how the BO approximation may be derived and under which conditions it is applicable. At the same time we will show how the BO approximation may be improved by including vibronic coupling. To that end the second step of the BO approximation is generalized to a set of coupled eigenvalue equations depending on nuclear coordinates only. Off-diagonal elements in these equations are shown to be nuclear kinetic energy terms.

It will be shown that the BO approximation can be trusted whenever the PESs, obtained from the solution of the electronic Schrödinger equation, are well separated:

$E_{0}(\mathbf {R} )\ll E_{1}(\mathbf {R} )\ll E_{2}(\mathbf {R} )\ll \cdots {\text{ for all }}\mathbf {R}$

.

We start from the *exact* non-relativistic, time-independent molecular Hamiltonian:

$H=H_{\text{e}}+T_{\text{n}}$

with

$H_{\text{e}}=-\sum _{i}{{\frac {1}{2}}\nabla _{i}^{2}}-\sum _{i,A}{\frac {Z_{A}}{r_{iA}}}+\sum _{i>j}{\frac {1}{r_{ij}}}+\sum _{B>A}{\frac {Z_{A}Z_{B}}{R_{AB}}}\quad {\text{and}}\quad T_{\text{n}}=-\sum _{A}{{\frac {1}{2M_{A}}}\nabla _{A}^{2}}.$

The position vectors $\mathbf {r} \equiv \{\mathbf {r} _{i}\}$ of the electrons and the position vectors $\mathbf {R} \equiv \{\mathbf {R} _{A}=(R_{Ax},R_{Ay},R_{Az})\}$ of the nuclei are with respect to a Cartesian inertial frame. Distances between particles are written as $r_{iA}\equiv |\mathbf {r} _{i}-\mathbf {R} _{A}|$ (distance between electron *i* and nucleus *A*) and similar definitions hold for $r_{ij}$ and $R_{AB}$ .

We assume that the molecule is in a homogeneous (no external force) and isotropic (no external torque) space. The only interactions are the two-body Coulomb interactions among the electrons and nuclei. The Hamiltonian is expressed in atomic units, so that we do not see the Planck constant, the dielectric constant of the vacuum, electronic charge, or electronic mass in this formula. The only constants explicitly entering the formula are *ZA* and *MA* – the atomic number and mass of nucleus *A*.

It is useful to introduce the total nuclear momentum and to rewrite the nuclear kinetic energy operator as follows:

$T_{\text{n}}=\sum _{A}\sum _{\alpha =x,y,z}{\frac {P_{A\alpha }P_{A\alpha }}{2M_{A}}}\quad {\text{with}}\quad P_{A\alpha }=-i{\frac {\partial }{\partial R_{A\alpha }}}.$

Suppose we have *K* electronic eigenfunctions $\chi _{k}(\mathbf {r$ of $H_{\text{e}}$ ; that is, we have solved

$H_{\text{e}}\chi _{k}(\mathbf {r$

The electronic wave functions $\chi _{k}$ will be taken to be real, which is possible when there are no magnetic or spin interactions. The *parametric dependence* of the functions $\chi _{k}$ on the nuclear coordinates is indicated by the symbol after the semicolon. This indicates that, although $\chi _{k}$ is a real-valued function of $\mathbf {r}$ , its functional form depends on $\mathbf {R}$ .

For example, in the molecular-orbital-linear-combination-of-atomic-orbitals (LCAO-MO) approximation, $\chi _{k}$ is a molecular orbital (MO) given as a linear expansion of atomic orbitals (AOs). An AO depends visibly on the coordinates of an electron, but the nuclear coordinates are not explicit in the MO. However, upon change of geometry, i.e., change of $\mathbf {R}$ , the LCAO coefficients obtain different values and we see corresponding changes in the functional form of the MO $\chi _{k}$ .

We will assume that the parametric dependence is continuous and differentiable, so that it is meaningful to consider

$P_{A\alpha }\chi _{k}(\mathbf {r$

which in general will not be zero.

The total wave function $\Psi (\mathbf {R} ,\mathbf {r} )$ is expanded in terms of $\chi _{k}(\mathbf {r$ :

$\Psi (\mathbf {R} ,\mathbf {r} )=\sum _{k=1}^{K}\chi _{k}(\mathbf {r$

with

$\langle \chi _{k'}(\mathbf {r$

and where the subscript $(\mathbf {r} )$ indicates that the integration, implied by the bra–ket notation, is over electronic coordinates only. By definition, the matrix with general element

${\big (}\mathbb {H} _{\text{e}}(\mathbf {R} ){\big )}_{k'k}\equiv \langle \chi _{k'}(\mathbf {r$

is diagonal. After multiplication by the real function $\chi _{k'}(\mathbf {r$ from the left and integration over the electronic coordinates $\mathbf {r}$ the total Schrödinger equation

$H\Psi (\mathbf {R} ,\mathbf {r} )=E\Psi (\mathbf {R} ,\mathbf {r} )$

is turned into a set of *K* coupled eigenvalue equations depending on nuclear coordinates only

$[\mathbb {H} _{\text{n}}(\mathbf {R} )+\mathbb {H} _{\text{e}}(\mathbf {R} )]{\boldsymbol {\phi }}(\mathbf {R} )=E{\boldsymbol {\phi }}(\mathbf {R} ).$

The column vector ${\boldsymbol {\phi }}(\mathbf {R} )$ has elements $\phi _{k}(\mathbf {R} ),\ k=1,\ldots ,K$ . The matrix $\mathbb {H} _{\text{e}}(\mathbf {R} )$ is diagonal, and the nuclear Hamilton matrix is non-diagonal; its off-diagonal (*vibronic coupling*) terms ${\big (}\mathbb {H} _{\text{n}}(\mathbf {R} ){\big )}_{k'k}$ are further discussed below. The vibronic coupling in this approach is through nuclear kinetic energy terms.

Solution of these coupled equations gives an approximation for energy and wavefunction that goes beyond the Born–Oppenheimer approximation. Unfortunately, the off-diagonal kinetic energy terms are usually difficult to handle. This is why often a diabatic transformation is applied, which retains part of the nuclear kinetic energy terms on the diagonal, removes the kinetic energy terms from the off-diagonal and creates coupling terms between the adiabatic PESs on the off-diagonal.

If we can neglect the off-diagonal elements the equations will uncouple and simplify drastically. In order to show when this neglect is justified, we suppress the coordinates in the notation and write, by applying the Leibniz rule for differentiation, the matrix elements of $T_{\text{n}}$ as

$T_{\text{n}}(\mathbf {R} )_{k'k}\equiv {\big (}\mathbb {H} _{\text{n}}(\mathbf {R} ){\big )}_{k'k}=\delta _{k'k}T_{\text{n}}+\sum _{A,\alpha }{\frac {1}{M_{A}}}\langle \chi _{k'}|P_{A\alpha }|\chi _{k}\rangle _{(\mathbf {r} )}P_{A\alpha }+\langle \chi _{k'}|T_{\text{n}}|\chi _{k}\rangle _{(\mathbf {r} )}.$

The diagonal ( $k'=k$ ) matrix elements $\langle \chi _{k}|P_{A\alpha }|\chi _{k}\rangle _{(\mathbf {r} )}$ of the operator $P_{A\alpha }$ vanish, because we assume time-reversal invariant, so $\chi _{k}$ can be chosen to be always real. The off-diagonal matrix elements satisfy

$\langle \chi _{k'}|P_{A\alpha }|\chi _{k}\rangle _{(\mathbf {r} )}={\frac {\langle \chi _{k'}|[P_{A\alpha },H_{\text{e}}]|\chi _{k}\rangle _{(\mathbf {r} )}}{E_{k}(\mathbf {R} )-E_{k'}(\mathbf {R} )}}.$

The matrix element in the numerator is

$\langle \chi _{k'}|[P_{A\alpha },H_{\mathrm {e} }]|\chi _{k}\rangle _{(\mathbf {r} )}=iZ_{A}\sum _{i}\left\langle \chi _{k'}\left|{\frac {(\mathbf {r} _{iA})_{\alpha }}{r_{iA}^{3}}}\right|\chi _{k}\right\rangle _{(\mathbf {r} )}\quad {\text{with}}\quad \mathbf {r} _{iA}\equiv \mathbf {r} _{i}-\mathbf {R} _{A}.$

The matrix element of the one-electron operator appearing on the right side is finite.

When the two surfaces come close, $E_{k}(\mathbf {R} )\approx E_{k'}(\mathbf {R} )$ , the nuclear momentum coupling term becomes large and is no longer negligible. This is the case where the BO approximation breaks down, and a coupled set of nuclear motion equations must be considered instead of the one equation appearing in the second step of the BO approximation.

Conversely, if all surfaces are well separated, all off-diagonal terms can be neglected, and hence the whole matrix of $P_{\alpha }^{A}$ is effectively zero. The third term on the right side of the expression for the matrix element of *T*n (the *Born–Oppenheimer diagonal correction*) can approximately be written as the matrix of $P_{\alpha }^{A}$ squared and, accordingly, is then negligible also. Only the first (diagonal) kinetic energy term in this equation survives in the case of well separated surfaces, and a diagonal, uncoupled, set of nuclear motion equations results:

$[T_{\text{n}}+E_{k}(\mathbf {R} )]\phi _{k}(\mathbf {R} )=E\phi _{k}(\mathbf {R} )\quad {\text{for}}\quad k=1,\ldots ,K,$

which are the normal second step of the BO equations discussed above.

We reiterate that when two or more potential energy surfaces approach each other, or even cross, the Born–Oppenheimer approximation breaks down, and one must fall back on the coupled equations. Usually one invokes then the diabatic approximation.

## Born–Oppenheimer approximation with correct symmetry

To include the correct symmetry within the Born–Oppenheimer (BO) approximation, a molecular system presented in terms of (mass-dependent) nuclear coordinates $\mathbf {q}$ and formed by the two lowest BO adiabatic potential energy surfaces (PES) $u_{1}(\mathbf {q} )$ and $u_{2}(\mathbf {q} )$ is considered. To ensure the validity of the BO approximation, the energy *E* of the system is assumed to be low enough so that $u_{2}(\mathbf {q} )$ becomes a closed PES in the region of interest, with the exception of sporadic infinitesimal sites surrounding degeneracy points formed by $u_{1}(\mathbf {q} )$ and $u_{2}(\mathbf {q} )$ (designated as (1, 2) degeneracy points).

The starting point is the nuclear adiabatic BO (matrix) equation written in the form

$-{\frac {\hbar ^{2}}{2m}}(\nabla +\tau )^{2}\Psi +(\mathbf {u} -E)\Psi =0,$

where $\Psi (\mathbf {q} )$ is a column vector containing the unknown nuclear wave functions $\psi _{k}(\mathbf {q} )$ , $\mathbf {u} (\mathbf {q} )$ is a diagonal matrix containing the corresponding adiabatic potential energy surfaces $u_{k}(\mathbf {q} )$ , *m* is the reduced mass of the nuclei, *E* is the total energy of the system, $\nabla$ is the gradient operator with respect to the nuclear coordinates $\mathbf {q}$ , and $\mathbf {\tau } (\mathbf {q} )$ is a matrix containing the vectorial non-adiabatic coupling terms (NACT):

$\mathbf {\tau } _{jk}=\langle \zeta _{j}|\nabla \zeta _{k}\rangle .$

Here $|\zeta _{n}\rangle$ are eigenfunctions of the electronic Hamiltonian assumed to form a complete Hilbert space in the given region in configuration space.

To study the scattering process taking place on the two lowest surfaces, one extracts from the above BO equation the two corresponding equations:

$-{\frac {\hbar ^{2}}{2m}}\nabla ^{2}\psi _{1}+({\tilde {u}}_{1}-E)\psi _{1}-{\frac {\hbar ^{2}}{2m}}[2\mathbf {\tau } _{12}\nabla +\nabla \mathbf {\tau } _{12}]\psi _{2}=0,$

$-{\frac {\hbar ^{2}}{2m}}\nabla ^{2}\psi _{2}+({\tilde {u}}_{2}-E)\psi _{2}+{\frac {\hbar ^{2}}{2m}}[2\mathbf {\tau } _{12}\nabla +\nabla \mathbf {\tau } _{12}]\psi _{1}=0,$

where ${\tilde {u}}_{k}(\mathbf {q} )=u_{k}(\mathbf {q} )+(\hbar ^{2}/2m)\tau _{12}^{2}$ (*k* = 1, 2), and $\mathbf {\tau } _{12}=\mathbf {\tau } _{12}(\mathbf {q} )$ is the (vectorial) NACT responsible for the coupling between $u_{1}(\mathbf {q} )$ and $u_{2}(\mathbf {q} )$ .

Next a new function is introduced:

$\chi =\psi _{1}+i\psi _{2},$

and the corresponding rearrangements are made:

1. Multiplying the second equation by *i* and combining it with the first equation yields the (complex) equation $-{\frac {\hbar ^{2}}{2m}}\nabla ^{2}\chi +({\tilde {u}}_{1}-E)\chi +i{\frac {\hbar ^{2}}{2m}}[2\mathbf {\tau } _{12}\nabla +\nabla \mathbf {\tau } _{12}]\chi +i(u_{1}-u_{2})\psi _{2}=0.$
2. The last term in this equation can be deleted for the following reasons: At those points where $u_{2}(\mathbf {q} )$ is classically closed, $\psi _{2}(\mathbf {q} )\sim 0$ by definition, and at those points where $u_{2}(\mathbf {q} )$ becomes classically allowed (which happens at the vicinity of the (1, 2) degeneracy points) this implies that: $u_{1}(\mathbf {q} )\sim u_{2}(\mathbf {q} )$ , or $u_{1}(\mathbf {q} )-u_{2}(\mathbf {q} )\sim 0$ . Consequently, the last term is, indeed, negligibly small at every point in the region of interest, and the equation simplifies to become $-{\frac {\hbar ^{2}}{2m}}\nabla ^{2}\chi +({\tilde {u}}_{1}-E)\chi +i{\frac {\hbar ^{2}}{2m}}[2\mathbf {\tau } _{12}\nabla +\nabla \mathbf {\tau } _{12}]\chi =0.$

In order for this equation to yield a solution with the correct symmetry, it is suggested to apply a perturbation approach based on an elastic potential $u_{0}(\mathbf {q} )$ , which coincides with $u_{1}(\mathbf {q} )$ at the asymptotic region.

The equation with an elastic potential can be solved, in a straightforward manner, by substitution. Thus, if $\chi _{0}$ is the solution of this equation, it is presented as

$\chi _{0}(\mathbf {q} |\Gamma )=\xi _{0}(\mathbf {q} )\exp \left[-i\int _{\Gamma }d\mathbf {q} '\cdot \mathbf {\tau } (\mathbf {q} '|\Gamma )\right],$

where $\Gamma$ is an arbitrary contour, and the exponential function contains the relevant symmetry as created while moving along $\Gamma$ .

The function $\xi _{0}(\mathbf {q} )$ can be shown to be a solution of the (unperturbed/elastic) equation

$-{\frac {\hbar ^{2}}{2m}}\nabla ^{2}\xi _{0}+(u_{0}-E)\xi _{0}=0.$

Having $\chi _{0}(\mathbf {q} |\Gamma )$ , the full solution of the above decoupled equation takes the form

$\chi (\mathbf {q} |\Gamma )=\chi _{0}(\mathbf {q} |\Gamma )+\eta (\mathbf {q} |\Gamma ),$

where $\eta (\mathbf {q} |\Gamma )$ satisfies the resulting inhomogeneous equation:

$-{\frac {\hbar ^{2}}{2m}}\nabla ^{2}\eta +({\tilde {u}}_{1}-E)\eta +i{\frac {\hbar ^{2}}{2m}}[2\mathbf {\tau } _{12}\nabla +\nabla \mathbf {\tau } _{12}]\eta =(u_{1}-u_{0})\chi _{0}.$

In this equation the inhomogeneity ensures the symmetry for the perturbed part of the solution along any contour and therefore for the solution in the required region in configuration space.

The relevance of the present approach was demonstrated while studying a two-arrangement-channel model (containing one inelastic channel and one reactive channel) for which the two adiabatic states were coupled by a Jahn–Teller conical intersection. A nice fit between the symmetry-preserved single-state treatment and the corresponding two-state treatment was obtained. This applies in particular to the reactive state-to-state probabilities (see Table III in Ref. 5a and Table III in Ref. 5b), for which the ordinary BO approximation led to erroneous results, whereas the symmetry-preserving BO approximation produced the accurate results, as they followed from solving the two coupled equations.
