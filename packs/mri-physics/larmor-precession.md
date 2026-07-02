---
title: "Larmor precession"
source: https://en.wikipedia.org/wiki/Larmor_precession
domain: mri-physics
license: CC-BY-SA-4.0
tags: magnetic resonance imaging, mri physics, spin relaxation, pulse sequence
fetched: 2026-07-02
---

# Larmor precession

In physics, **Larmor precession** (named after Joseph Larmor) is the precession of the magnetic moment of an object about an external magnetic field. The phenomenon is conceptually similar to the precession of a tilted classical gyroscope in an external torque-exerting gravitational field. Objects with a magnetic moment also have angular momentum and effective internal electric current proportional to their angular momentum; these include electrons, protons, other fermions, many atomic and nuclear systems, as well as classical macroscopic systems. The external magnetic field exerts a torque on the magnetic moment,

${\vec {\tau }}={\vec {\mu }}\times {\vec {B}}=\gamma {\vec {J}}\times {\vec {B}},$

where ${\vec {\tau }}$ is the torque, ${\vec {\mu }}$ is the magnetic dipole moment, ${\vec {J}}$ is the angular momentum vector, ${\vec {B}}$ is the external magnetic field, $\times$ symbolizes the cross product, and $\gamma$ is the gyromagnetic ratio, which gives the proportionality constant between the magnetic moment and the angular momentum. The angular momentum vector ${\vec {J}}$ precesses about the external field axis with an angular frequency known as the **Larmor frequency**,

$\omega =\vert \gamma B\vert$

,

where $\omega$ is the angular frequency, B is the magnitude of the applied magnetic field, and $\gamma$ is the gyromagnetic ratio for a particle of charge $-e$ , equal to $-{\frac {eg}{2m}}$ , where m is the mass of the precessing system, while g is the *g*-factor of the system. The *g*-factor is the unit-less proportionality factor relating the system's angular momentum to the intrinsic magnetic moment; in classical physics it is 1 for any rigid object in which the charge and mass density are identically distributed. The Larmor frequency is independent of the angle between ${\vec {J}}$ and ${\vec {B}}$ .

In nuclear physics the *g*-factor of a given system includes the effect of the nucleon spins, their orbital angular momenta, and their couplings. Generally, the *g*-factors are very difficult to calculate for such many-body systems, but they have been measured to high precision for most nuclei. The Larmor frequency is important in NMR spectroscopy. The gyromagnetic ratios, which give the Larmor frequencies at a given magnetic field strength, have been measured and tabulated.

Crucially, the Larmor frequency is independent of the polar angle between the applied magnetic field and the magnetic moment direction. This is what makes it a key concept in fields such as nuclear magnetic resonance (NMR) and electron paramagnetic resonance (EPR), since the precession rate does not depend on the spatial orientation of the spins.

## Including Thomas precession

The above equation is the one that is used in most applications. However, a full treatment must include the effects of Thomas precession, yielding the equation (in CGS units, which are used so that *E* has the same units as *B*):

$\omega _{s}={\frac {geB}{2mc}}+(1-\gamma ){\frac {eB}{mc\gamma }}={\frac {eB}{2mc}}\left(g-2+{\frac {2}{\gamma }}\right)$

where $\gamma$ is the relativistic Lorentz factor (not to be confused with the gyromagnetic ratio above). Notably, for the electron spin *g* is very close to 2 (2.002...), so if one sets *g* = 2, one arrives at

$\omega _{s(g=2)}={\frac {eB}{mc\gamma }}$

## Bargmann–Michel–Telegdi equation

The spin precession of an electron in an external electromagnetic field is described by the Bargmann–Michel–Telegdi (BMT) equation (named after Valentine Bargmann, Louis Michel and Valentine Telegdi)

${\frac {da^{\tau }}{ds}}={\frac {e}{m}}u^{\tau }u_{\sigma }F^{\sigma \lambda }a_{\lambda }+2\mu (F^{\tau \lambda }-u^{\tau }u_{\sigma }F^{\sigma \lambda })a_{\lambda },$

where $a^{\tau }$ , e , m , and $\mu$ are polarization four-vector, charge, mass, and magnetic moment, $u^{\tau }$ is four-velocity of electron (in a system of units in which $c=1$ ), $a^{\tau }a_{\tau }=-u^{\tau }u_{\tau }=-1$ , $u^{\tau }a_{\tau }=0$ , and $F^{\tau \sigma }$ is electromagnetic field-strength tensor. Using equations of motion,

$m{\frac {du^{\tau }}{ds}}=eF^{\tau \sigma }u_{\sigma },$

one can rewrite the first term on the right side of the BMT equation as $(-u^{\tau }w^{\lambda }+u^{\lambda }w^{\tau })a_{\lambda }$ , where $w^{\tau }=du^{\tau }/ds$ is four-acceleration. This term describes Fermi–Walker transport and leads to Thomas precession. The second term is associated with Larmor precession.

When electromagnetic fields are uniform in space or when gradient forces like $\nabla ({\boldsymbol {\mu }}\cdot {\boldsymbol {B}})$ can be neglected, the particle's translational motion is described by

${\frac {du^{\alpha }}{d\tau }}={\frac {e}{m}}F^{\alpha \beta }u_{\beta }\;.$

The BMT equation is then written as

${\frac {dS^{\alpha }}{d\tau }}={\frac {e}{m}}{\bigg [}{g \over 2}F^{\alpha \beta }S_{\beta }+\left({g \over 2}-1\right)u^{\alpha }\left(S_{\lambda }F^{\lambda \mu }u_{\mu }\right){\bigg ]}\;,$

The Beam-Optical version of the Thomas-BMT, from the *Quantum Theory of Charged-Particle Beam Optics*, applicable in accelerator optics.

## Applications

A 1935 paper published by Lev Landau and Evgeny Lifshitz predicted the existence of ferromagnetic resonance of the Larmor precession, which was independently verified in experiments by J. H. E. Griffiths (UK) and E. K. Zavoiskij (USSR) in 1946.

Larmor precession is important in nuclear magnetic resonance, magnetic resonance imaging, electron paramagnetic resonance, muon spin resonance, and neutron spin echo. It is also important for the alignment of cosmic dust grains, which is a cause of the polarization of starlight.

To calculate the spin of a particle in a magnetic field, one must in general also take into account Thomas precession if the particle is moving.

## Precession direction

The spin angular momentum of an electron precesses counter-clockwise about the direction of the magnetic field. An electron has a negative charge, so the direction of its magnetic moment is opposite to that of its spin.
