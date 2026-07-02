---
title: "Fock matrix"
source: https://en.wikipedia.org/wiki/Fock_matrix
domain: hartree-fock
license: CC-BY-SA-4.0
tags: hartree-fock method, self-consistent field, slater determinant, roothaan equations
fetched: 2026-07-02
---

# Fock matrix

The Fock matrix is defined by the Fock operator. In its general form the Fock operator is written

${\hat {F}}(i)={\hat {h}}(i)+\sum _{j=1}^{N}[{\hat {J}}_{j}(i)-{\hat {K}}_{j}(i)]$

where ${\hat {J}}_{j}$ and ${\hat {K}}_{j}$ are the Coulomb and exchange operators, and *i* runs over the total *N* spin orbitals. In the closed-shell case, it can be simplified by considering only the spatial orbitals by noting that the ${\hat {J}}$ terms are duplicated and the exchange terms are null between different spins. For the restricted case which assumes closed-shell orbitals and single- determinantal wavefunctions, the Fock operator for the *i*-th electron is given by:

${\hat {F}}(i)={\hat {h}}(i)+\sum _{j=1}^{n/2}[2{\hat {J}}_{j}(i)-{\hat {K}}_{j}(i)]$

where:

${\hat {F}}(i)$

is the Fock operator for the

i

-th electron in the system,

${\hat {h}}(i)$

is the one-electron

Hamiltonian

for the

i

-th electron,

n

is the number of electrons and

${\frac {n}{2}}$

is the number of occupied orbitals in the closed-shell system,

${\hat {J}}_{j}(i)$

is the

Coulomb operator

, defining the repulsive force between the

j

-th and

i

-th electrons in the system,

${\hat {K}}_{j}(i)$

is the

exchange operator

, defining the quantum effect produced by exchanging two electrons.

The Coulomb operator is multiplied by two since there are two electrons in each occupied orbital. The exchange operator is not multiplied by two since it has a non-zero result only for electrons which have the same spin as the *i*-th electron.

For systems with unpaired electrons there are many choices of Fock matrices.
