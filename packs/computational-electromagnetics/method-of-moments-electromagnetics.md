---
title: "Method of moments (electromagnetics)"
source: https://en.wikipedia.org/wiki/Method_of_moments_(electromagnetics)
domain: computational-electromagnetics
license: CC-BY-SA-4.0
tags: computational electromagnetics, method of moments, boundary element method, electromagnetic scattering
fetched: 2026-07-02
---

# Method of moments (electromagnetics)

The **method of moments** (**MoM**), also known as the **moment method** and **method of weighted residuals**, is a numerical method in computational electromagnetics. It is used in computer programs that simulate the interaction of electromagnetic fields such as radio waves with matter, for example antenna simulation programs like NEC that calculate the radiation pattern of an antenna. Generally being a frequency-domain method, it involves the projection of an integral equation into a system of linear equations by the application of appropriate boundary conditions. This is done by using discrete meshes as in finite difference and finite element methods, often for the surface. The solutions are represented with the linear combination of pre-defined basis functions; generally, the coefficients of these basis functions are the sought unknowns. Green's functions and Galerkin method play a central role in the method of moments.

For many applications, the method of moments is identical to the boundary element method. It is one of the most common methods in microwave and antenna engineering.

## History

Development of boundary element method and other similar methods for different engineering applications is associated with the advent of digital computing in the 1960s. Prior to this, variational methods were applied to engineering problems at microwave frequencies by the time of World War II. While Julian Schwinger and Nathan Marcuvitz have respectively compiled these works into lecture notes and textbooks, Victor Rumsey has formulated these methods into the "reaction concept" in 1954. The concept was later shown to be equivalent to the Galerkin method. In the late 1950s, an early version of the method of moments was introduced by Yuen Lo at a course on mathematical methods in electromagnetic theory at University of Illinois.

In the 1960s, early research work on the method was published by Kenneth Mei, Jean van Bladel and Jack Richmond. In the same decade, the systematic theory for the method of moments in electromagnetics was largely formalized by Roger Harrington. While the term "the method of moments" was coined earlier by Leonid Kantorovich and Gleb Akilov for analogous numerical applications, Harrington has adapted the term for the electromagnetic formulation. Harrington published the seminal textbook *Field Computation by Moment Methods* on the moment method in 1968. The development of the method and its indications in radar and antenna engineering attracted interest; MoM research was subsequently supported by the United States government. The method was further popularized by the introduction of generalized antenna modeling codes such as Numerical Electromagnetics Code, which was released into public domain by the United States government in the late 1980s. In the 1990s, introduction of fast multipole and multilevel fast multipole methods enabled efficient MoM solutions to problems with millions of unknowns.

Being one of the most common simulation techniques in RF and microwave engineering, the method of moments forms the basis of many commercial design software such as FEKO. Many non-commercial and public domain codes of different sophistications are also available. In addition to its use in electrical engineering, the method of moments has been applied to light scattering and plasmonic problems.

## Background

### Basic concepts

An inhomogeneous integral equation can be expressed as: $L(f)=g$ where *L* denotes a linear operator, *g* denotes the known forcing function and *f* denotes the unknown function. *f* can be approximated by a finite number of basis functions ( $f_{n}$ ): $f\approx \sum _{n}^{N}a_{n}f_{n}.$

By linearity, substitution of this expression into the equation yields: $\sum _{n}^{N}a_{n}L(f_{n})\approx g.$

We can also define a residual for this expression, which denotes the difference between the actual and the approximate solution: $R=\sum _{n}^{N}a_{n}L(f_{n})-g$

The aim of the method of moments is to minimize this residual, which can be done by using appropriate weighting or testing functions, hence the name method of weighted residuals. After the determination of a suitable inner product for the problem, the expression then becomes: $\sum _{n}^{N}a_{n}\langle w_{m},L(f_{n})\rangle \approx \langle w_{m},g\rangle$

Thus, the expression can be represented in the matrix form: $\left[\ell _{mn}\right]\left[\alpha _{m}\right]=[g_{n}]$

The resulting matrix is often referred to as the impedance matrix. The coefficients of the basis functions can be obtained through inverting the matrix. For large matrices with a large number of unknowns, iterative methods such as conjugate gradient method can be used for acceleration. The actual field distributions can be obtained from the coefficients and the associated integrals. The interactions between each basis function in MoM is ensured by Green's function of the system.

### Basis and testing functions

Different basis functions can be chosen to model the expected behavior of the unknown function in the domain; these functions can either be subsectional or global. Choice of Dirac delta function as basis function is known as point-matching or collocation. This corresponds to enforcing the boundary conditions on N discrete points and is often used to obtain approximate solutions when the inner product operation is cumbersome to perform. Other subsectional basis functions include pulse, piecewise triangular, piecewise sinusoidal and rooftop functions. Triangular patches, introduced by S. Rao, D. Wilton and A. Glisson in 1982, are known as RWG basis functions and are widely used in MoM. Characteristic basis functions were also introduced to accelerate computation and reduce the matrix equation.

The testing and basis functions are often chosen to be the same; this is known as the Galerkin method. Depending on the application and studied structure, the testing and basis functions should be chosen appropriately to ensure convergence and accuracy, as well as to prevent possible high order algebraic singularities.

## Integral equations

Depending on the application and sought variables, different integral or integro-differential equations are used in MoM. Radiation and scattering by thin wire structures, such as many types of antennas, can be modeled by specialized equations. For surface problems, common integral equation formulations include electric field integral equation (EFIE), magnetic field integral equation (MFIE) and mixed-potential integral equation (MPIE).

### Thin-wire equations

As many antenna structures can be approximated as wires, thin wire equations are of interest in MoM applications. Two commonly used thin-wire equations are Pocklington and Hallén integro-differential equations. Pocklington's equation precedes the computational techniques, having been introduced in 1897 by Henry Cabourn Pocklington. For a linear wire that is centered on the origin and aligned with the z-axis, the equation can be written as: $\int _{-l/2}^{l/2}I_{z}(z')\left[\left({\frac {d^{2}}{dz^{2}}}+\beta ^{2}\right)G(z,z')\right]\,dz'=-j\omega \varepsilon E_{z}^{\text{inc}}(p=a)$ where l and a denote the total length and thickness, respectively. $G(z,z')$ is the Green's function for free space. The equation can be generalized to different excitation schemes, including magnetic frills.

Hallén integral equation, published by E. Hallén in 1938, can be given as: $\left({\frac {d^{2}}{dz^{2}}}+\beta ^{2}\right)\int _{-l/2}^{l/2}I_{z}(z')G(z,z')\,dz'=-j\omega \varepsilon E_{z}^{\text{inc}}(p=a)$

This equation, despite being more well-behaved than the Pocklington's equation, is generally restricted to the delta-gap voltage excitations at the antenna feed point, which can be represented as an impressed electric field.

### Electric field integral equation (EFIE)

The general form of electric field integral equation (EFIE) can be written as: ${\hat {\mathbf {n} }}\times \mathbf {E} ^{\text{inc}}(\mathbf {r} )={\hat {\mathbf {n} }}\times \int _{S}\left[\eta jk\,\mathbf {J} (\mathbf {r} ')G(\mathbf {r} ,\mathbf {r} ')+{\frac {\eta }{jk}}\left\{{\boldsymbol {\nabla }}_{s}'\cdot \mathbf {J} (\mathbf {r} ')\right\}{\boldsymbol {\nabla }}'G(\mathbf {r} ,\mathbf {r} ')\right]\,dS'$ where $\mathbf {E} _{\text{inc}}$ is the incident or impressed electric field. $G(r,r')$ is the Green function for Helmholtz equation and $\eta$ represents the wave impedance. The boundary conditions are met at a defined PEC surface. EFIE is a Fredholm integral equation of the first kind.

### Magnetic field integral equation (MFIE)

Another commonly used integral equation in MoM is the magnetic field integral equation (MFIE), which can be written as: $-{\frac {1}{2}}\mathbf {J} (r)+{\hat {\mathbf {n} }}\times \oint _{S}\mathbf {J} (r')\times {\boldsymbol {\nabla }}'G(r,r')\,dS'={\hat {\mathbf {n} }}\times \mathbf {H} _{\text{inc}}(r)$

MFIE is often formulated to be a Fredholm integral equation of the second kind and is generally well-posed. Nevertheless, the formulation necessitates the use of closed surfaces, which limits its applications.

### Other formulations

Many different surface and volume integral formulations for MoM exist. In many cases, EFIEs are converted to mixed potential integral equations (MFIE) through the use of Lorenz gauge condition; this aims to reduce the orders of singularities through the use of magnetic vector and scalar electric potentials. In order to bypass the internal resonance problem in dielectric scattering calculations, combined-field integral equation (CFIE) and Poggio—Miller—Chang—Harrington—Wu—Tsai (PMCHWT) formulations are also used. Another approach, the volumetric integral equation, necessitates the discretization of the volume elements and is often computationally expensive.

MoM can also be integrated with physical optics theory and finite element method.

## Green's functions

Appropriate Green's function for the studied structure must be known to formulate MoM matrices: automatic incorporation of the radiation condition into the Green's function makes MoM particularly useful for radiation and scattering problems. Even though the Green function can be derived in closed form for very simple cases, more complex structures necessitate numerical derivation of these functions.

Full wave analysis of planarly-stratified structures in particular, such as microstrips or patch antennas, necessitate the derivation of Green's functions that are peculiar to these geometries. This can be achieved in two different methods. In the first method, known as spectral-domain approach, the inner products and convolution operation for MoM matrix entries are evaluated in the Fourier space with analytically-derived spectral-domain Green's functions through Parseval's theorem. The other approach is based on the use of spatial-domain Green's functions. This involves the inverse Hankel transform of the spectral-domain Green's function, which is defined on the Sommerfeld integration path. Nevertheless, this integral cannot be evaluated analytically, and its numerical evaluation is often computationally expensive due to the oscillatory kernels and slowly-converging nature of the integral. Common approaches for evaluating these integrals include tail extrapolation approaches such as weighted-averages method.

Other approaches include the approximation of the integral kernel. Following the extraction of quasi-static and surface pole components, these integrals can be approximated as closed-form complex exponentials through Prony's method or generalized pencil-of-function method; thus, the spatial Green's functions can be derived through the use of appropriate identities such as Sommerfeld identity. This method is known in the computational electromagnetics literature as the discrete complex image method (DCIM), since the Green's function is effectively approximated with a discrete number of image dipoles that are located within a complex distance from the origin. The associated Green's functions are referred as closed-form Green's functions. The method has also been extended for cylindrically-layered structures.

Rational-function fitting method, as well as its combinations with DCIM, can also be used to approximate closed-form Green's functions. Alternatively, the closed-form Green's function can be evaluated through method of steepest descent. For the periodic structures such as phased arrays and frequency selective surfaces, series acceleration methods such as Kummer's transformation and Ewald summation is often used to accelerate the computation of the periodic Green's function.
