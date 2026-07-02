---
title: "Maxwell–Boltzmann distribution"
source: https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_distribution
domain: statistical-mechanics
license: CC-BY-SA-4.0
tags: statistical mechanics, partition function, boltzmann distribution, canonical ensemble
fetched: 2026-07-02
---

# Maxwell–Boltzmann distribution

In physics (in particular in statistical mechanics), the **Maxwell–Boltzmann distribution**, or **Maxwell(ian) distribution**, is a particular probability distribution named after James Clerk Maxwell and Ludwig Boltzmann.

It was first defined and used for describing particle speeds in idealized gases, where the particles move freely inside a stationary container without interacting with one another, except for very brief collisions in which they exchange energy and momentum with each other or with their thermal environment. The term "particle" in this context refers to gaseous particles only (atoms or molecules), and the system of particles is assumed to have reached thermodynamic equilibrium. The energies of such particles follow what is known as Maxwell–Boltzmann statistics, and the statistical distribution of speeds is derived by equating particle energies with kinetic energy.

Mathematically, the Maxwell–Boltzmann distribution is the chi distribution with three degrees of freedom (the components of the velocity vector in Euclidean space), with a scale parameter measuring speeds in units proportional to the square root of $T/m$ (the ratio of temperature and particle mass).

The Maxwell–Boltzmann distribution is a result of the kinetic theory of gases, which provides a simplified explanation of many fundamental gaseous properties, including pressure and diffusion. The Maxwell–Boltzmann distribution applies fundamentally to particle velocities in three dimensions, but turns out to depend only on the speed (the magnitude of the velocity) of the particles. A particle speed probability distribution indicates which speeds are more likely: a randomly chosen particle will have a speed selected randomly from the distribution, and is more likely to be within one range of speeds than another. The kinetic theory of gases applies to the classical ideal gas, which is an idealization of real gases. In real gases, there are various effects (e.g., van der Waals interactions, vortical flow, relativistic speed limits, and quantum exchange interactions) that can make their speed distribution different from the Maxwell–Boltzmann form. However, rarefied gases at ordinary temperatures behave very nearly like an ideal gas and the Maxwell speed distribution is an excellent approximation for such gases. This is also true for ideal plasmas, which are ionized gases of sufficiently low density.

The distribution was first derived by Maxwell in 1860 on heuristic grounds. Boltzmann later, in the 1870s, carried out significant investigations into the physical origins of this distribution. The distribution can be derived on the ground that it maximizes the entropy of the system. A list of derivations are:

1. Maximum entropy probability distribution in the phase space, with the constraint of conservation of average energy $\langle H\rangle =E;$
2. Canonical ensemble.

## Distribution function

For a system containing a large number of identical non-interacting, non-relativistic classical particles in thermodynamic equilibrium, the fraction of the particles within an infinitesimal element of the three-dimensional velocity space *d* 3**v**, centered on a velocity vector $\mathbf {v}$ of magnitude v , is given by $f(\mathbf {v} )~d^{3}\mathbf {v} ={\biggl [}{\frac {m}{2\pi k_{\text{B}}T}}{\biggr ]}^{{3}/{2}}\,\exp \left(-{\frac {mv^{2}}{2k_{\text{B}}T}}\right)~d^{3}\mathbf {v} ,$ where:

- m is the particle mass;
- *k*B is the Boltzmann constant;
- T is thermodynamic temperature;
- $f(\mathbf {v} )$ is a probability distribution function, properly normalized so that ${\textstyle \int f(\mathbf {v} )\,d^{3}\mathbf {v} }$ over all velocities is unity.

One can write the element of velocity space as $d^{3}\mathbf {v} =dv_{x}\,dv_{y}\,dv_{z}$ , for velocities in a standard Cartesian coordinate system, or as $d^{3}\mathbf {v} =v^{2}\,dv\,d\Omega$ in a standard spherical coordinate system, where $d\Omega =\sin {\theta }~d\phi ~d\theta$ is an element of solid angle and ${\textstyle v^{2}=|\mathbf {v} |^{2}=v_{x}^{2}+v_{y}^{2}+v_{z}^{2}}$ .

Alternately, the distribution function can also be written in momentum space as $f(\mathbf {p} )\,d^{3}\mathbf {p} =\left[{\frac {1}{2\pi mk_{\text{B}}T}}\right]^{3/2}\exp \left(-{\frac {p^{2}}{2mk_{\text{B}}T}}\right)\,d^{3}\mathbf {p}$ where $\mathbf {p} =m\mathbf {v}$ is the momentum vector.

The Maxwellian distribution function for particles moving in only one direction, if this direction is x, is a normal distribution with a standard deviation of ${\textstyle {\sqrt {k_{\text{B}}T/m}}}$ : $f(v_{x})~dv_{x}={\sqrt {\frac {m}{2\pi k_{\text{B}}T}}}\,\exp \left(-{\frac {mv_{x}^{2}}{2k_{\text{B}}T}}\right)~dv_{x},$ which can be obtained by integrating the three-dimensional form given above over vy and vz.

Recognizing the symmetry of $f(v)$ , one can integrate over solid angle and write a probability distribution of speeds as the function

$f(v)={\biggl [}{\frac {m}{2\pi k_{\text{B}}T}}{\biggr ]}^{{3}/{2}}\,4\pi v^{2}\exp \left(-{\frac {mv^{2}}{2k_{\text{B}}T}}\right).$

This probability density function gives the probability, per unit speed, of finding the particle with a speed near v. This equation is simply the Maxwell–Boltzmann distribution (given in the infobox) with distribution parameter ${\textstyle a={\sqrt {k_{\text{B}}T/m}}\,.}$ The Maxwell–Boltzmann distribution is equivalent to the chi distribution with three degrees of freedom and scale parameter ${\textstyle a={\sqrt {k_{\text{B}}T/m}}\,.}$

The simplest ordinary differential equation satisfied by the distribution is: ${\begin{aligned}0&=k_{\text{B}}Tvf'(v)+f(v)\left(mv^{2}-2k_{\text{B}}T\right),\\[4pt]f(1)&={\sqrt {\frac {2}{\pi }}}\,{\biggl [}{\frac {m}{k_{\text{B}}T}}{\biggr ]}^{3/2}\exp \left(-{\frac {m}{2k_{\text{B}}T}}\right);\end{aligned}}$

or in unitless presentation: ${\begin{aligned}0&=a^{2}xf'(x)+\left(x^{2}-2a^{2}\right)f(x),\\[4pt]f(1)&={\frac {1}{a^{3}}}{\sqrt {\frac {2}{\pi }}}\exp \left(-{\frac {1}{2a^{2}}}\right).\end{aligned}}$ With the Darwin–Fowler method of mean values, the Maxwell–Boltzmann distribution is obtained as an exact result.

## Relaxation to the 2D Maxwell–Boltzmann distribution

For particles confined to move in a plane, the speed distribution is given by

$P(s<|\mathbf {v} |<s{+}ds)={\frac {ms}{k_{\text{B}}T}}\exp \left(-{\frac {ms^{2}}{2k_{\text{B}}T}}\right)ds$

This distribution is used for describing systems in equilibrium. However, most systems do not start out in their equilibrium state. The evolution of a system towards its equilibrium state is governed by the Boltzmann equation. The equation predicts that for short range interactions, the equilibrium velocity distribution will follow a Maxwell–Boltzmann distribution. To the right is a molecular dynamics (MD) simulation in which 900 hard sphere particles are constrained to move in a rectangle. They interact via perfectly elastic collisions. The system is initialized out of equilibrium, but the velocity distribution (in blue) quickly converges to the 2D Maxwell–Boltzmann distribution (in orange).

## Typical speeds

The mean speed $\langle v\rangle$ , most probable speed (mode) *v*p, and root-mean-square speed ${\textstyle {\sqrt {\langle v^{2}\rangle }}}$ can be obtained from properties of the Maxwell distribution.

This works well for nearly ideal, monatomic gases like helium, but also for molecular gases like diatomic oxygen. This is because despite the larger heat capacity (larger internal energy at the same temperature) due to their larger number of degrees of freedom, their translational kinetic energy (and thus their speed) is unchanged.

- The most probable speed, *v*p, is the speed most likely to be possessed by any molecule (of the same mass m) in the system and corresponds to the maximum value or the mode of *f*(*v*). To find it, we calculate the derivative ⁠ ${\tfrac {df}{dv}},$ ⁠ set it to zero and solve for v: ${\frac {df(v)}{dv}}=-8\pi {\biggl [}{\frac {m}{2\pi k_{\text{B}}T}}{\biggr ]}^{3/2}\,v\,\left[{\frac {mv^{2}}{2k_{\text{B}}T}}-1\right]\exp \left(-{\frac {mv^{2}}{2k_{\text{B}}T}}\right)=0$ with the solution: ${\frac {mv_{\text{p}}^{2}}{2k_{\text{B}}T}}=1;\quad v_{\text{p}}={\sqrt {\frac {2k_{\text{B}}T}{m}}}={\sqrt {\frac {2RT}{M}}}$ where: For diatomic nitrogen (N2, the primary component of air) at room temperature (300 K), this gives $v_{\text{p}}\approx {\sqrt {\frac {2\cdot 8.31\,\mathrm {J{\cdot }{mol}^{-1}K^{-1}} \ 300\,\mathrm {K} }{0.028\,\mathrm {{kg}{\cdot }{mol}^{-1}} }}}\approx 422\,\mathrm {m/s} .$
  - R is the gas constant;
  - M is molar mass of the substance, and thus may be calculated as a product of particle mass, m, and Avogadro constant, *N*A: $M=mN_{\mathrm {A} }.$
- The mean speed is the expected value of the speed distribution, setting ${\textstyle b={\frac {1}{2a^{2}}}={\frac {m}{2k_{\text{B}}T}}}$ : ${\begin{aligned}\langle v\rangle &=\int _{0}^{\infty }v\,f(v)\,dv\\[1ex]&=4\pi \left[{\frac {b}{\pi }}\right]^{3/2}\int _{0}^{\infty }v^{3}e^{-bv^{2}}dv=4\pi \left[{\frac {b}{\pi }}\right]^{3/2}{\frac {1}{2b^{2}}}\\[1.4ex]&={\sqrt {\frac {4}{\pi b}}}={\sqrt {\frac {8k_{\text{B}}T}{\pi m}}}={\sqrt {\frac {8RT}{\pi M}}}={\frac {2}{\sqrt {\pi }}}v_{\text{p}}\end{aligned}}$
- The mean square speed $\langle v^{2}\rangle$ is the second-order raw moment of the speed distribution. The "root mean square speed" $v_{\text{rms}}$ is the square root of the mean square speed, corresponding to the speed of a particle with average kinetic energy, setting ${\textstyle b={\frac {1}{2a^{2}}}={\frac {m}{2k_{\text{B}}T}}}$ : ${\begin{aligned}v_{\text{rms}}&={\sqrt {\langle v^{2}\rangle }}=\left[\int _{0}^{\infty }v^{2}\,f(v)\,dv\right]^{1/2}\\[1ex]&=\left[4\pi \left({\frac {b}{\pi }}\right)^{3/2}\int _{0}^{\infty }v^{4}e^{-bv^{2}}dv\right]^{1/2}\\[1ex]&=\left[4\pi \left({\frac {b}{\pi }}\right)^{3/2}{\frac {3}{8}}\left({\frac {\pi }{b^{5}}}\right)^{1/2}\right]^{1/2}={\sqrt {\frac {3}{2b}}}\\[1ex]&={\sqrt {\frac {3k_{\text{B}}T}{m}}}={\sqrt {\frac {3RT}{M}}}={\sqrt {\frac {3}{2}}}v_{\text{p}}\end{aligned}}$

In summary, the typical speeds are related as follows: $v_{\text{p}}\approx 88.6\%\ \langle v\rangle <\langle v\rangle <108.5\%\ \langle v\rangle \approx v_{\text{rms}}.$

The root mean square speed is directly related to the speed of sound c in the gas, by $c={\sqrt {\frac {\gamma }{3}}}\ v_{\mathrm {rms} }={\sqrt {\frac {f+2}{3f}}}\ v_{\mathrm {rms} }={\sqrt {\frac {f+2}{2f}}}\ v_{\text{p}},$ where ${\textstyle \gamma =1+{\frac {2}{f}}}$ is the adiabatic index, f is the number of degrees of freedom of the individual gas molecule. For the example above, diatomic nitrogen (approximating air) at 300 K, $f=5$ and $c={\sqrt {\frac {7}{15}}}v_{\mathrm {rms} }\approx 68\%\ v_{\mathrm {rms} }\approx 84\%\ v_{\text{p}}\approx 353\ \mathrm {m/s} ,$ the true value for air can be approximated by using the average molar weight of air (29 g/mol), yielding 347 m/s at 300 K (corrections for variable humidity are of the order of 0.1% to 0.6%).

The average relative velocity ${\begin{aligned}v_{\text{rel}}\equiv \langle |\mathbf {v} _{1}-\mathbf {v} _{2}|\rangle &=\int \!d^{3}\mathbf {v} _{1}\,d^{3}\mathbf {v} _{2}\left|\mathbf {v} _{1}-\mathbf {v} _{2}\right|f(\mathbf {v} _{1})f(\mathbf {v} _{2})\\[2pt]&={\frac {4}{\sqrt {\pi }}}{\sqrt {\frac {k_{\text{B}}T}{m}}}={\sqrt {2}}\langle v\rangle \end{aligned}}$ where the three-dimensional velocity distribution is $f(\mathbf {v} )\equiv \left[{\frac {2\pi k_{\text{B}}T}{m}}\right]^{-3/2}\exp \left(-{\frac {1}{2}}{\frac {m\mathbf {v} ^{2}}{k_{\text{B}}T}}\right).$

The integral can easily be done by changing to coordinates $\mathbf {u} =\mathbf {v} _{1}-\mathbf {v} _{2}$ and ${\textstyle \mathbf {U} ={\tfrac {1}{2}}(\mathbf {v} _{1}+\mathbf {v} _{2}).}$

## Limitations

The Maxwell–Boltzmann distribution assumes that the velocities of individual particles are much less than the speed of light, i.e. that $T\ll {\frac {mc^{2}}{k_{\text{B}}}}$ . For electrons, the temperature of electrons must be $T_{e}\ll 5.93\times 10^{9}~\mathrm {K}$ . For distribution of speeds of relativistic particles, see Maxwell–Jüttner distribution.

### Maxwell–Boltzmann statistics

The original derivation in 1860 by James Clerk Maxwell was an argument based on molecular collisions of the Kinetic theory of gases as well as certain symmetries in the speed distribution function; Maxwell also gave an early argument that these molecular collisions entail a tendency towards equilibrium. After Maxwell, Ludwig Boltzmann in 1872 also derived the distribution on mechanical grounds and argued that gases should over time tend toward this distribution, due to collisions (see H-theorem). He later (1877) derived the distribution again under the framework of statistical thermodynamics. The derivations in this section are along the lines of Boltzmann's 1877 derivation, starting with a result known as Maxwell–Boltzmann statistics (from statistical thermodynamics). Maxwell–Boltzmann statistics gives the average number of particles found in a given single-particle microstate. Under certain assumptions, the logarithm of the fraction of particles in a given microstate is linear in the ratio of the energy of that state to the temperature of the system: there are constants k and C such that, for all i , $-\log \left({\frac {N_{i}}{N}}\right)={\frac {1}{k}}\cdot {\frac {E_{i}}{T}}+C.$ The assumptions of this equation are that the particles do not interact, and that they are classical; this means that each particle's state can be considered independently from the other particles' states. Additionally, the particles are assumed to be in thermal equilibrium.

This relation can be written as an equation by introducing a normalizing factor:

| ${\frac {N_{i}}{N}}={\frac {\exp \left(-{\frac {E_{i}}{k_{\text{B}}T}}\right)}{\displaystyle \sum _{j}\exp \left(-{\tfrac {E_{j}}{k_{\text{B}}T}}\right)}}$ |   | 1 |
|---|---|---|

where:

- Ni is the expected number of particles in the single-particle microstate i,
- N is the total number of particles in the system,
- Ei is the energy of microstate i,
- the sum over index j takes into account all microstates,
- T is the equilibrium temperature of the system,
- *k*B is the Boltzmann constant.

The denominator in **equation 1** is a normalizing factor so that the ratios $N_{i}:N$ add up to unity — in other words it is a kind of partition function (for the single-particle system, not the usual partition function of the entire system).

Because velocity and speed are related to energy, Equation (**1**) can be used to derive relationships between temperature and the speeds of gas particles. All that is needed is to discover the density of microstates in energy, which is determined by dividing up momentum space into equal sized regions.

### Distribution for the momentum vector

The potential energy is taken to be zero, so that all energy is in the form of kinetic energy. The relationship between kinetic energy and momentum for massive non-relativistic particles is

| $E={\frac {p^{2}}{2m}}$ |   | 2 |
|---|---|---|

where *p*2 is the square of the momentum vector **p** = [*px*, *py*, *pz*]. We may therefore rewrite Equation (**1**) as:

| ${\frac {N_{i}}{N}}={\frac {1}{Z}}\exp \left(-{\frac {p_{i,x}^{2}+p_{i,y}^{2}+p_{i,z}^{2}}{2mk_{\text{B}}T}}\right)$ |   | 3 |
|---|---|---|

where:

- Z is the partition function, corresponding to the denominator in **equation 1**;
- m is the molecular mass of the gas;
- T is the thermodynamic temperature;
- *k*B is the Boltzmann constant.

This distribution of *Ni* : *N* is proportional to the probability density function *f***p** for finding a molecule with these values of momentum components, so:

| $f_{\mathbf {p} }(p_{x},p_{y},p_{z})\propto \exp \left(-{\frac {p_{x}^{2}+p_{y}^{2}+p_{z}^{2}}{2mk_{\text{B}}T}}\right)$ |   | 4 |
|---|---|---|

The normalizing constant can be determined by recognizing that the probability of a molecule having *some* momentum must be 1. Integrating the exponential in **equation 4** over all px, py, and pz yields a factor of $\iiint _{-\infty }^{+\infty }\exp \left(-{\frac {p_{x}^{2}+p_{y}^{2}+p_{z}^{2}}{2mk_{\text{B}}T}}\right)dp_{x}\,dp_{y}\,dp_{z}={\Bigl [}{\sqrt {\pi }}{\sqrt {2mk_{\text{B}}T}}{\Bigr ]}^{3}$

So that the normalized distribution function is:

$f_{\mathbf {p} }(p_{x},p_{y},p_{z})=\left[{\frac {1}{2\pi mk_{\text{B}}T}}\right]^{3/2}\exp \left(-{\frac {p_{x}^{2}+p_{y}^{2}+p_{z}^{2}}{2mk_{\text{B}}T}}\right)$    (6)

The distribution is seen to be the product of three independent normally distributed variables $p_{x}$ , $p_{y}$ , and $p_{z}$ , with variance $mk_{\text{B}}T$ . Additionally, it can be seen that the magnitude of momentum will be distributed as a Maxwell–Boltzmann distribution, with ${\textstyle a={\sqrt {mk_{\text{B}}T}}}$ . The Maxwell–Boltzmann distribution for the momentum (or equally for the velocities) can be obtained more fundamentally using the H-theorem at equilibrium within the Kinetic theory of gases framework.

### Distribution for the energy

The energy distribution is found imposing

| $f_{E}(E)\,dE=f_{p}(\mathbf {p} )\,d^{3}\mathbf {p} ,$ |   | 7 |
|---|---|---|

where $d^{3}\mathbf {p}$ is the infinitesimal phase-space volume of momenta corresponding to the energy interval dE. Making use of the spherical symmetry of the energy-momentum dispersion relation $E={\tfrac {|\mathbf {p} |^{2}}{2m}},$ this can be expressed in terms of dE as

| $d^{3}\mathbf {p} =4\pi \left\|\mathbf {p} \right\|^{2}\,d{\left\|\mathbf {p} \right\|}=4\pi m{\sqrt {2mE}}\ dE.$ |   | 8 |
|---|---|---|

Using then (**8**) in (**7**), and expressing everything in terms of the energy E, we get ${\begin{aligned}f_{E}(E)\,dE&=\left[{\frac {1}{2\pi mk_{\text{B}}T}}\right]^{3/2}\exp \left(-{\frac {E}{k_{\text{B}}T}}\right)4\pi m{\sqrt {2mE}}\ dE\\[1ex]&=2{\sqrt {\frac {E}{\pi }}}\,\left[{\frac {1}{k_{\text{B}}T}}\right]^{3/2}\exp \left(-{\frac {E}{k_{\text{B}}T}}\right)\,dE\end{aligned}}$ and finally

$f_{E}(E)=2{\sqrt {\frac {E}{\pi }}}\,\left[{\frac {1}{k_{\text{B}}T}}\right]^{3/2}\exp \left(-{\frac {E}{k_{\text{B}}T}}\right)$    (9)

Since the energy is proportional to the sum of the squares of the three normally distributed momentum components, this energy distribution can be written equivalently as a gamma distribution, using a shape parameter, $k_{\text{shape}}=3/2$ and a scale parameter, $\theta _{\text{scale}}=k_{\text{B}}T.$

Using the equipartition theorem, given that the energy is evenly distributed among all three degrees of freedom in equilibrium, we can also split $f_{E}(E)\,dE$ into a set of chi-squared distributions, where the energy per degree of freedom, ε is distributed as a chi-squared distribution with one degree of freedom, $f_{\varepsilon }(\varepsilon )\,d\varepsilon ={\sqrt {\frac {1}{\pi \varepsilon k_{\text{B}}T}}}~\exp \left(-{\frac {\varepsilon }{k_{\text{B}}T}}\right)\,d\varepsilon$

At equilibrium, this distribution will hold true for any number of degrees of freedom. For example, if the particles are rigid mass dipoles of fixed dipole moment, they will have three translational degrees of freedom and two additional rotational degrees of freedom. The energy in each degree of freedom will be described according to the above chi-squared distribution with one degree of freedom, and the total energy will be distributed according to a chi-squared distribution with five degrees of freedom. This has implications in the theory of the specific heat of a gas.

### Distribution for the velocity vector

Recognizing that the velocity probability density *f***v** is proportional to the momentum probability density function by

$f_{\mathbf {v} }d^{3}\mathbf {v} =f_{\mathbf {p} }\left({\frac {dp}{dv}}\right)^{3}d^{3}\mathbf {v}$

and using **p** = *m***v** we get

$f_{\mathbf {v} }(v_{x},v_{y},v_{z})={\biggl [}{\frac {m}{2\pi k_{\text{B}}T}}{\biggr ]}^{3/2}\exp \left(-{\frac {m\left(v_{x}^{2}+v_{y}^{2}+v_{z}^{2}\right)}{2k_{\text{B}}T}}\right)$

which is the Maxwell–Boltzmann velocity distribution. The probability of finding a particle with velocity in the infinitesimal element [*dvx*, *dvy*, *dvz*] about velocity **v** = [*vx*, *vy*, *vz*] is

$f_{\mathbf {v} }{\left(v_{x},v_{y},v_{z}\right)}\,dv_{x}\,dv_{y}\,dv_{z}.$

Like the momentum, this distribution is seen to be the product of three independent normally distributed variables $v_{x}$ , $v_{y}$ , and $v_{z}$ , but with variance ${\textstyle k_{\text{B}}T/m}$ . It can also be seen that the Maxwell–Boltzmann velocity distribution for the vector velocity [*vx*, *vy*, *vz*] is the product of the distributions for each of the three directions: $f_{\mathbf {v} }{\left(v_{x},v_{y},v_{z}\right)}=f_{v}(v_{x})f_{v}(v_{y})f_{v}(v_{z})$ where the distribution for a single direction is $f_{v}(v_{i})={\sqrt {\frac {m}{2\pi k_{\text{B}}T}}}\exp \left(-{\frac {mv_{i}^{2}}{2k_{\text{B}}T}}\right).$

Each component of the velocity vector has a normal distribution with mean $\mu _{v_{x}}=\mu _{v_{y}}=\mu _{v_{z}}=0$ and standard deviation ${\textstyle \sigma _{v_{x}}=\sigma _{v_{y}}=\sigma _{v_{z}}={\sqrt {k_{\text{B}}T/m}}}$ , so the vector has a 3-dimensional normal distribution, a particular kind of multivariate normal distribution, with mean $\mu _{\mathbf {v} }=\mathbf {0}$ and covariance ${\textstyle \Sigma _{\mathbf {v} }=\left({\frac {k_{\text{B}}T}{m}}\right)I}$ , where I is the 3 × 3 identity matrix.

A notable property of the distribution for the velocity vector is direction-independence, which means that velocity components are normally distributed in any selected direction, not only in three base directions x , y , and z .

### Distribution for the speed

The Maxwell–Boltzmann distribution for the speed follows immediately from the distribution of the velocity vector, above. Note that the speed is $v={\sqrt {v_{x}^{2}+v_{y}^{2}+v_{z}^{2}}}$ and the volume element in spherical coordinates $dv_{x}\,dv_{y}\,dv_{z}=v^{2}\sin \theta \,dv\,d\theta \,d\phi =v^{2}\,dv\,d\Omega$ where $\phi$ and $\theta$ are the spherical coordinate angles of the velocity vector. Integration of the probability density function of the velocity over the solid angles $d\Omega$ yields an additional factor of $4\pi$ . The speed distribution with substitution of the speed for the sum of the squares of the vector components:

$f(v)={\sqrt {\frac {2}{\pi }}}\,{\biggl [}{\frac {m}{k_{\text{B}}T}}{\biggr ]}^{3/2}v^{2}\exp \left(-{\frac {mv^{2}}{2k_{\text{B}}T}}\right).$

## In *n*-dimensional space

In n-dimensional space, Maxwell–Boltzmann distribution becomes: $f(\mathbf {v} )~d^{n}\mathbf {v} ={\biggl [}{\frac {m}{2\pi k_{\text{B}}T}}{\biggr ]}^{n/2}\exp \left(-{\frac {m|\mathbf {v} |^{2}}{2k_{\text{B}}T}}\right)~d^{n}\mathbf {v}$

Speed distribution becomes: $f(v)~dv=A\exp \left(-{\frac {mv^{2}}{2k_{\text{B}}T}}\right)v^{n-1}~dv$ where A is a normalizing constant.

The following integral result is useful: ${\begin{aligned}\int _{0}^{\infty }v^{a}\exp \left(-{\frac {mv^{2}}{2k_{\text{B}}T}}\right)dv&=\left[{\frac {2k_{\text{B}}T}{m}}\right]^{\frac {a+1}{2}}\int _{0}^{\infty }e^{-x}x^{a/2}\,dx^{1/2}\\[2pt]&=\left[{\frac {2k_{\text{B}}T}{m}}\right]^{\frac {a+1}{2}}\int _{0}^{\infty }e^{-x}x^{a/2}{\frac {x^{-1/2}}{2}}\,dx\\[2pt]&=\left[{\frac {2k_{\text{B}}T}{m}}\right]^{\frac {a+1}{2}}{\frac {\Gamma {\left({\frac {a+1}{2}}\right)}}{2}}\end{aligned}}$ where $\Gamma (z)$ is the Gamma function. This result can be used to calculate the moments of speed distribution function: $\langle v\rangle ={\frac {\displaystyle \int _{0}^{\infty }v\cdot v^{n-1}\exp \left(-{\tfrac {mv^{2}}{2k_{\text{B}}T}}\right)\,dv}{\displaystyle \int _{0}^{\infty }v^{n-1}\exp \left(-{\tfrac {mv^{2}}{2k_{\text{B}}T}}\right)\,dv}}={\sqrt {\frac {2k_{\text{B}}T}{m}}}~~{\frac {\Gamma {\left({\frac {n+1}{2}}\right)}}{\Gamma {\left({\frac {n}{2}}\right)}}}$ which is the mean speed itself ${\textstyle v_{\mathrm {avg} }=\langle v\rangle ={\sqrt {\frac {2k_{\text{B}}T}{m}}}\ {\frac {\Gamma \left({\frac {n+1}{2}}\right)}{\Gamma \left({\frac {n}{2}}\right)}}.}$

${\begin{aligned}\langle v^{2}\rangle &={\frac {\displaystyle \int _{0}^{\infty }v^{2}\cdot v^{n-1}\exp \left(-{\tfrac {mv^{2}}{2k_{\text{B}}T}}\right)\,dv}{\displaystyle \int _{0}^{\infty }v^{n-1}\exp \left(-{\tfrac {mv^{2}}{2k_{\text{B}}T}}\right)\,dv}}\\[1ex]&=\left[{\frac {2k_{\text{B}}T}{m}}\right]{\frac {\Gamma {\left({\frac {n+2}{2}}\right)}}{\Gamma {\left({\frac {n}{2}}\right)}}}\\[1.2ex]&=\left[{\frac {2k_{\text{B}}T}{m}}\right]{\frac {n}{2}}={\frac {nk_{\text{B}}T}{m}}\end{aligned}}$ which gives root-mean-square speed ${\textstyle v_{\text{rms}}={\sqrt {\langle v^{2}\rangle }}={\sqrt {\frac {nk_{\text{B}}T}{m}}}.}$

The derivative of speed distribution function: ${\frac {df(v)}{dv}}=A\exp \left(-{\frac {mv^{2}}{2k_{\text{B}}T}}\right){\biggl [}-{\frac {mv}{k_{\text{B}}T}}v^{n-1}+(n-1)v^{n-2}{\biggr ]}=0$

This yields the most probable speed (mode) ${\textstyle v_{\text{p}}={\sqrt {\left(n-1\right)k_{\text{B}}T/m}}.}$

## Extension to real gases

The derivations show that the validity of the Maxwell–Boltzmann velocity distribution is limited to ideal gases. A generalization of the formula to all gases (ideal and real alike) is known, its derivation starts from the fact that the properties of both ideal and real gases must be independent of the direction. The formula obtained contains $pV_{\text{m}}$ terms instead of $RT$ , where p is the pressure, $V_{\text{m}}$ is the molar volume of the gas sample:

$f(v)={\biggl [}{\frac {M}{2\pi pV_{\text{m}}}}{\biggr ]}^{{3}/{2}}\,4\pi v^{2}\exp \left(-{\frac {Mv^{2}}{2pV_{\text{m}}}}\right).$
