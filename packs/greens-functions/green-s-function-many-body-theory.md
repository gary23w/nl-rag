---
title: "Green's function (many-body theory)"
source: https://en.wikipedia.org/wiki/Green%27s_function_(many-body_theory)
domain: greens-functions
license: CC-BY-SA-4.0
tags: green's function, fundamental solution, method of images, propagator function
fetched: 2026-07-02
---

# Green's function (many-body theory)

In many-body theory, the term **Green's function** (or **Green function**) is sometimes used interchangeably with correlation function, but refers specifically to correlators of field operators or creation and annihilation operators.

The name comes from the Green's functions used to solve inhomogeneous differential equations, to which they are loosely related. (Specifically, only two-point "Green's functions" in the case of a non-interacting system are Green's functions in the mathematical sense; the linear operator that they invert is the Hamiltonian operator, which in the non-interacting case is quadratic in the fields.)

## Spatially uniform case

### Basic definitions

We consider a many-body theory with field operator (annihilation operator written in the position basis) $\psi (\mathbf {x} )$ .

The Heisenberg operators can be written in terms of Schrödinger operators as $\psi (\mathbf {x} ,t)=e^{iKt}\psi (\mathbf {x} )e^{-iKt}$ , and the creation operator is ${\bar {\psi }}(\mathbf {x} ,t)=[\psi (\mathbf {x} ,t)]^{\dagger }$ , where $K=H-\mu N$ is the grand-canonical Hamiltonian.

Similarly, for the imaginary-time operators, $\psi (\mathbf {x} ,\tau )=e^{K\tau }\psi (\mathbf {x} )e^{-K\tau }$ ${\bar {\psi }}(\mathbf {x} ,\tau )=e^{K\tau }\psi ^{\dagger }(\mathbf {x} )e^{-K\tau }.$ [Note that the imaginary-time creation operator ${\bar {\psi }}(\mathbf {x} ,\tau )$ is not the Hermitian conjugate of the annihilation operator $\psi (\mathbf {x} ,\tau )$ .]

In real time, the $2n$ -point Green function is defined by $G^{(n)}(1\ldots n\mid 1'\ldots n')=i^{n}\langle T\psi (1)\ldots \psi (n){\bar {\psi }}(n')\ldots {\bar {\psi }}(1')\rangle ,$ where we have used a condensed notation in which j signifies $(\mathbf {x} _{j},t_{j})$ and $j'$ signifies $(\mathbf {x} _{j}',t_{j}')$ . The operator T denotes time ordering, and indicates that the field operators that follow it are to be ordered so that their time arguments increase from right to left.

In imaginary time, the corresponding definition is ${\mathcal {G}}^{(n)}(1\ldots n\mid 1'\ldots n')=\langle T\psi (1)\ldots \psi (n){\bar {\psi }}(n')\ldots {\bar {\psi }}(1')\rangle ,$ where j signifies $\mathbf {x} _{j},\tau _{j}$ . (The imaginary-time variables $\tau _{j}$ are restricted to the range from 0 to the inverse temperature ${\textstyle \beta ={\frac {1}{k_{\text{B}}T}}}$ .)

**Note** regarding signs and normalization used in these definitions: The signs of the Green functions have been chosen so that Fourier transform of the two-point ( $n=1$ ) thermal Green function for a free particle is ${\mathcal {G}}(\mathbf {k} ,\omega _{n})={\frac {1}{-i\omega _{n}+\xi _{\mathbf {k} }}},$ and the retarded Green function is $G^{\mathrm {R} }(\mathbf {k} ,\omega )={\frac {1}{-(\omega +i\eta )+\xi _{\mathbf {k} }}},$ where $\omega _{n}={\frac {[2n+\theta (-\zeta )]\pi }{\beta }}$ is the Matsubara frequency.

Throughout, $\zeta$ is $+1$ for bosons and $-1$ for fermions and $[\ldots ,\ldots ]=[\ldots ,\ldots ]_{-\zeta }$ denotes either a commutator or anticommutator as appropriate.

(See below for details.)

### Two-point functions

The Green function with a single pair of arguments ( $n=1$ ) is referred to as the two-point function, or propagator. In the presence of both spatial and temporal translational symmetry, it depends only on the difference of its arguments. Taking the Fourier transform with respect to both space and time gives ${\mathcal {G}}(\mathbf {x} \tau \mid \mathbf {x} '\tau ')=\int _{\mathbf {k} }d\mathbf {k} {\frac {1}{\beta }}\sum _{\omega _{n}}{\mathcal {G}}(\mathbf {k} ,\omega _{n})e^{i\mathbf {k} \cdot (\mathbf {x} -\mathbf {x} ')-i\omega _{n}(\tau -\tau ')},$ where the sum is over the appropriate Matsubara frequencies (and the integral involves an implicit factor of $(L/2\pi )^{d}$ , as usual).

In real time, we will explicitly indicate the time-ordered function with a superscript T: $G^{\mathrm {T} }(\mathbf {x} t\mid \mathbf {x} 't')=\int _{\mathbf {k} }d\mathbf {k} \int {\frac {d\omega }{2\pi }}G^{\mathrm {T} }(\mathbf {k} ,\omega )e^{i\mathbf {k} \cdot (\mathbf {x} -\mathbf {x} ')-i\omega (t-t')}.$

The real-time two-point Green function can be written in terms of 'retarded' and 'advanced' Green functions, which will turn out to have simpler analyticity properties. The retarded and advanced Green functions are defined by $G^{\mathrm {R} }(\mathbf {x} t\mid \mathbf {x} 't')=-i\langle [\psi (\mathbf {x} ,t),{\bar {\psi }}(\mathbf {x} ',t')]_{\zeta }\rangle \Theta (t-t')$ and $G^{\mathrm {A} }(\mathbf {x} t\mid \mathbf {x} 't')=i\langle [\psi (\mathbf {x} ,t),{\bar {\psi }}(\mathbf {x} ',t')]_{\zeta }\rangle \Theta (t'-t),$ respectively.

They are related to the time-ordered Green function by $G^{\mathrm {T} }(\mathbf {k} ,\omega )=[1+\zeta n(\omega )]G^{\mathrm {R} }(\mathbf {k} ,\omega )-\zeta n(\omega )G^{\mathrm {A} }(\mathbf {k} ,\omega ),$ where $n(\omega )={\frac {1}{e^{\beta \omega }-\zeta }}$ is the Bose–Einstein or Fermi–Dirac distribution function.

#### Imaginary-time ordering and *β*-periodicity

The thermal Green functions are defined only when both imaginary-time arguments are within the range 0 to $\beta$ . The two-point Green function has the following properties. (The position or momentum arguments are suppressed in this section.)

Firstly, it depends only on the difference of the imaginary times: ${\mathcal {G}}(\tau ,\tau ')={\mathcal {G}}(\tau -\tau ').$ The argument $\tau -\tau '$ is allowed to run from $-\beta$ to $\beta$ .

Secondly, ${\mathcal {G}}(\tau )$ is (anti)periodic under shifts of $\beta$ . Because of the small domain within which the function is defined, this means just ${\mathcal {G}}(\tau -\beta )=\zeta {\mathcal {G}}(\tau ),$ for $0<\tau <\beta$ . Time ordering is crucial for this property, which can be proved straightforwardly, using the cyclicity of the trace operation.

These two properties allow for the Fourier transform representation and its inverse, ${\mathcal {G}}(\omega _{n})=\int _{0}^{\beta }d\tau \,{\mathcal {G}}(\tau )\,e^{i\omega _{n}\tau }.$

Finally, note that ${\mathcal {G}}(\tau )$ has a discontinuity at $\tau =0$ ; this is consistent with a long-distance behaviour of ${\mathcal {G}}(\omega _{n})\sim 1/|\omega _{n}|$ .

### Spectral representation

The propagators in real and imaginary time can both be related to the spectral density (or spectral weight), given by $\rho (\mathbf {k} ,\omega )={\frac {1}{\mathcal {Z}}}\sum _{\alpha ,\alpha '}2\pi \delta (E_{\alpha }-E_{\alpha '}-\omega )|\langle \alpha \mid \psi _{\mathbf {k} }^{\dagger }\mid \alpha '\rangle |^{2}\left(e^{-\beta E_{\alpha '}}-\zeta e^{-\beta E_{\alpha }}\right),$ where |*α*⟩ refers to a (many-body) eigenstate of the grand-canonical Hamiltonian *H* − *μN*, with eigenvalue *Eα*.

The imaginary-time propagator is then given by ${\mathcal {G}}(\mathbf {k} ,\omega _{n})=\int _{-\infty }^{\infty }{\frac {d\omega '}{2\pi }}{\frac {\rho (\mathbf {k} ,\omega ')}{-i\omega _{n}+\omega '}}~,$ and the retarded propagator by $G^{\mathrm {R} }(\mathbf {k} ,\omega )=\int _{-\infty }^{\infty }{\frac {d\omega '}{2\pi }}{\frac {\rho (\mathbf {k} ,\omega ')}{-(\omega +i\eta )+\omega '}},$ where the limit as $\eta \to 0^{+}$ is implied.

The advanced propagator is given by the same expression, but with $-i\eta$ in the denominator.

The time-ordered function can be found in terms of $G^{\mathrm {R} }$ and $G^{\mathrm {A} }$ . As claimed above, $G^{\mathrm {R} }(\omega )$ and $G^{\mathrm {A} }(\omega )$ have simple analyticity properties: the former (latter) has all its poles and discontinuities in the lower (upper) half-plane.

The thermal propagator ${\mathcal {G}}(\omega _{n})$ has all its poles and discontinuities on the imaginary $\omega _{n}$ axis.

The spectral density can be found very straightforwardly from $G^{\mathrm {R} }$ , using the Sokhatsky–Weierstrass theorem $\lim _{\eta \to 0^{+}}{\frac {1}{x\pm i\eta }}=P{\frac {1}{x}}\mp i\pi \delta (x),$ where P denotes the Cauchy principal part. This gives $\rho (\mathbf {k} ,\omega )=2\operatorname {Im} G^{\mathrm {R} }(\mathbf {k} ,\omega ).$

This furthermore implies that $G^{\mathrm {R} }(\mathbf {k} ,\omega )$ obeys the following relationship between its real and imaginary parts: $\operatorname {Re} G^{\mathrm {R} }(\mathbf {k} ,\omega )=-2P\int _{-\infty }^{\infty }{\frac {d\omega '}{2\pi }}{\frac {\operatorname {Im} G^{\mathrm {R} }(\mathbf {k} ,\omega ')}{\omega -\omega '}},$ where P denotes the principal value of the integral.

The spectral density obeys a sum rule, $\int _{-\infty }^{\infty }{\frac {d\omega }{2\pi }}\rho (\mathbf {k} ,\omega )=1,$ which gives $G^{\mathrm {R} }(\omega )\sim {\frac {1}{|\omega |}}$ as $|\omega |\to \infty$ .

#### Hilbert transform

The similarity of the spectral representations of the imaginary- and real-time Green functions allows us to define the function $G(\mathbf {k} ,z)=\int _{-\infty }^{\infty }{\frac {dx}{2\pi }}{\frac {\rho (\mathbf {k} ,x)}{-z+x}},$ which is related to ${\mathcal {G}}$ and $G^{\mathrm {R} }$ by ${\mathcal {G}}(\mathbf {k} ,\omega _{n})=G(\mathbf {k} ,i\omega _{n})$ and $G^{\mathrm {R} }(\mathbf {k} ,\omega )=G(\mathbf {k} ,\omega +i\eta ).$ A similar expression obviously holds for $G^{\mathrm {A} }$ .

The relation between $G(\mathbf {k} ,z)$ and $\rho (\mathbf {k} ,x)$ is referred to as a Hilbert transform.

#### Proof of spectral representation

We demonstrate the proof of the spectral representation of the propagator in the case of the thermal Green function, defined as ${\mathcal {G}}(\mathbf {x} ,\tau \mid \mathbf {x} ',\tau ')=\langle T\psi (\mathbf {x} ,\tau ){\bar {\psi }}(\mathbf {x} ',\tau ')\rangle .$

Due to translational symmetry, it is only necessary to consider ${\mathcal {G}}(\mathbf {x} ,\tau \mid \mathbf {0} ,0)$ for $\tau >0$ , given by ${\mathcal {G}}(\mathbf {x} ,\tau \mid \mathbf {0} ,0)={\frac {1}{\mathcal {Z}}}\sum _{\alpha '}e^{-\beta E_{\alpha '}}\langle \alpha '\mid \psi (\mathbf {x} ,\tau ){\bar {\psi }}(\mathbf {0} ,0)\mid \alpha '\rangle .$ Inserting a complete set of eigenstates gives ${\mathcal {G}}(\mathbf {x} ,\tau \mid \mathbf {0} ,0)={\frac {1}{\mathcal {Z}}}\sum _{\alpha ,\alpha '}e^{-\beta E_{\alpha '}}\langle \alpha '\mid \psi (\mathbf {x} ,\tau )\mid \alpha \rangle \langle \alpha \mid {\bar {\psi }}(\mathbf {0} ,0)\mid \alpha '\rangle .$

Since $|\alpha \rangle$ and $|\alpha '\rangle$ are eigenstates of $H-\mu N$ , the Heisenberg operators can be rewritten in terms of Schrödinger operators, giving ${\mathcal {G}}(\mathbf {x} ,\tau |\mathbf {0} ,0)={\frac {1}{\mathcal {Z}}}\sum _{\alpha ,\alpha '}e^{-\beta E_{\alpha '}}e^{\tau (E_{\alpha '}-E_{\alpha })}\langle \alpha '\mid \psi (\mathbf {x} )\mid \alpha \rangle \langle \alpha \mid \psi ^{\dagger }(\mathbf {0} )\mid \alpha '\rangle .$ Performing the Fourier transform then gives ${\mathcal {G}}(\mathbf {k} ,\omega _{n})={\frac {1}{\mathcal {Z}}}\sum _{\alpha ,\alpha '}e^{-\beta E_{\alpha '}}{\frac {1-\zeta e^{\beta (E_{\alpha '}-E_{\alpha })}}{-i\omega _{n}+E_{\alpha }-E_{\alpha '}}}\int _{\mathbf {k} '}d\mathbf {k} '\langle \alpha \mid \psi (\mathbf {k} )\mid \alpha '\rangle \langle \alpha '\mid \psi ^{\dagger }(\mathbf {k} ')\mid \alpha \rangle .$

Momentum conservation allows the final term to be written as (up to possible factors of the volume) $|\langle \alpha '\mid \psi ^{\dagger }(\mathbf {k} )\mid \alpha \rangle |^{2},$ which confirms the expressions for the Green functions in the spectral representation.

The sum rule can be proved by considering the expectation value of the commutator, $1={\frac {1}{\mathcal {Z}}}\sum _{\alpha }\langle \alpha \mid e^{-\beta (H-\mu N)}[\psi _{\mathbf {k} },\psi _{\mathbf {k} }^{\dagger }]_{-\zeta }\mid \alpha \rangle ,$ and then inserting a complete set of eigenstates into both terms of the commutator: $1={\frac {1}{\mathcal {Z}}}\sum _{\alpha ,\alpha '}e^{-\beta E_{\alpha }}\left(\langle \alpha \mid \psi _{\mathbf {k} }\mid \alpha '\rangle \langle \alpha '\mid \psi _{\mathbf {k} }^{\dagger }\mid \alpha \rangle -\zeta \langle \alpha \mid \psi _{\mathbf {k} }^{\dagger }\mid \alpha '\rangle \langle \alpha '\mid \psi _{\mathbf {k} }\mid \alpha \rangle \right).$

Swapping the labels in the first term then gives $1={\frac {1}{\mathcal {Z}}}\sum _{\alpha ,\alpha '}\left(e^{-\beta E_{\alpha '}}-\zeta e^{-\beta E_{\alpha }}\right)|\langle \alpha \mid \psi _{\mathbf {k} }^{\dagger }\mid \alpha '\rangle |^{2}~,$ which is exactly the result of the integration of ρ.

#### Non-interacting case

In the non-interacting case, $\psi _{\mathbf {k} }^{\dagger }\mid \alpha '\rangle$ is an eigenstate with (grand-canonical) energy $E_{\alpha '}+\xi _{\mathbf {k} }$ , where $\xi _{\mathbf {k} }=\epsilon _{\mathbf {k} }-\mu$ is the single-particle dispersion relation measured with respect to the chemical potential. The spectral density therefore becomes $\rho _{0}(\mathbf {k} ,\omega )={\frac {1}{\mathcal {Z}}}\,2\pi \delta (\xi _{\mathbf {k} }-\omega )\sum _{\alpha '}\langle \alpha '\mid \psi _{\mathbf {k} }\psi _{\mathbf {k} }^{\dagger }\mid \alpha '\rangle (1-\zeta e^{-\beta \xi _{\mathbf {k} }})e^{-\beta E_{\alpha '}}.$

From the commutation relations, $\langle \alpha '\mid \psi _{\mathbf {k} }\psi _{\mathbf {k} }^{\dagger }\mid \alpha '\rangle =\langle \alpha '\mid (1+\zeta \psi _{\mathbf {k} }^{\dagger }\psi _{\mathbf {k} })\mid \alpha '\rangle ,$ with possible factors of the volume again. The sum, which involves the thermal average of the number operator, then gives simply $[1+\zeta n(\xi _{\mathbf {k} })]{\mathcal {Z}}$ , leaving $\rho _{0}(\mathbf {k} ,\omega )=2\pi \delta (\xi _{\mathbf {k} }-\omega ).$

The imaginary-time propagator is thus ${\mathcal {G}}_{0}(\mathbf {k} ,\omega )={\frac {1}{-i\omega _{n}+\xi _{\mathbf {k} }}}$ and the retarded propagator is $G_{0}^{\mathrm {R} }(\mathbf {k} ,\omega )={\frac {1}{-(\omega +i\eta )+\xi _{\mathbf {k} }}}.$

#### Zero-temperature limit

As *β* → ∞, the spectral density becomes $\rho (\mathbf {k} ,\omega )=2\pi \sum _{\alpha }\left[\delta (E_{\alpha }-E_{0}-\omega )\left|\left\langle \alpha \mid \psi _{\mathbf {k} }^{\dagger }\mid 0\right\rangle \right|^{2}-\zeta \delta (E_{0}-E_{\alpha }-\omega )\left|\left\langle 0\mid \psi _{\mathbf {k} }^{\dagger }\mid \alpha \right\rangle \right|^{2}\right]$ where *α* = 0 corresponds to the ground state. Note that only the first (second) term contributes when ω is positive (negative).

## General case

### Basic definitions

We can use 'field operators' as above, or creation and annihilation operators associated with other single-particle states, perhaps eigenstates of the (noninteracting) kinetic energy. We then use $\psi (\mathbf {x} ,\tau )=\varphi _{\alpha }(\mathbf {x} )\psi _{\alpha }(\tau ),$ where $\psi _{\alpha }$ is the annihilation operator for the single-particle state $\alpha$ and $\varphi _{\alpha }(\mathbf {x} )$ is that state's wavefunction in the position basis. This gives ${\mathcal {G}}_{\alpha _{1}\ldots \alpha _{n}|\beta _{1}\ldots \beta _{n}}^{(n)}(\tau _{1}\ldots \tau _{n}|\tau _{1}'\ldots \tau _{n}')=\langle T\psi _{\alpha _{1}}(\tau _{1})\ldots \psi _{\alpha _{n}}(\tau _{n}){\bar {\psi }}_{\beta _{n}}(\tau _{n}')\ldots {\bar {\psi }}_{\beta _{1}}(\tau _{1}')\rangle$ with a similar expression for $G^{(n)}$ .

### Two-point functions

These depend only on the difference of their time arguments, so that ${\mathcal {G}}_{\alpha \beta }(\tau \mid \tau ')={\frac {1}{\beta }}\sum _{\omega _{n}}{\mathcal {G}}_{\alpha \beta }(\omega _{n})\,e^{-i\omega _{n}(\tau -\tau ')}$ and $G_{\alpha \beta }(t\mid t')=\int _{-\infty }^{\infty }{\frac {d\omega }{2\pi }}\,G_{\alpha \beta }(\omega )\,e^{-i\omega (t-t')}.$

We can again define retarded and advanced functions in the obvious way; these are related to the time-ordered function in the same way as above.

The same periodicity properties as described in above apply to ${\mathcal {G}}_{\alpha \beta }$ . Specifically, ${\mathcal {G}}_{\alpha \beta }(\tau \mid \tau ')={\mathcal {G}}_{\alpha \beta }(\tau -\tau ')$ and ${\mathcal {G}}_{\alpha \beta }(\tau )={\mathcal {G}}_{\alpha \beta }(\tau +\beta ),$ for $\tau <0$ .

### Spectral representation

In this case, $\rho _{\alpha \beta }(\omega )={\frac {1}{\mathcal {Z}}}\sum _{m,n}2\pi \delta (E_{n}-E_{m}-\omega )\;\langle m\mid \psi _{\alpha }\mid n\rangle \langle n\mid \psi _{\beta }^{\dagger }\mid m\rangle \left(e^{-\beta E_{m}}-\zeta e^{-\beta E_{n}}\right),$ where m and n are many-body states.

The expressions for the Green functions are modified in the obvious ways: ${\mathcal {G}}_{\alpha \beta }(\omega _{n})=\int _{-\infty }^{\infty }{\frac {d\omega '}{2\pi }}{\frac {\rho _{\alpha \beta }(\omega ')}{-i\omega _{n}+\omega '}}$ and $G_{\alpha \beta }^{\mathrm {R} }(\omega )=\int _{-\infty }^{\infty }{\frac {d\omega '}{2\pi }}{\frac {\rho _{\alpha \beta }(\omega ')}{-(\omega +i\eta )+\omega '}}.$

Their analyticity properties are identical to those of ${\mathcal {G}}(\mathbf {k} ,\omega _{n})$ and $G^{\mathrm {R} }(\mathbf {k} ,\omega )$ defined in the translationally invariant case. The proof follows exactly the same steps, except that the two matrix elements are no longer complex conjugates.

#### Noninteracting case

If the particular single-particle states that are chosen are 'single-particle energy eigenstates', i.e. $[H-\mu N,\psi _{\alpha }^{\dagger }]=\xi _{\alpha }\psi _{\alpha }^{\dagger },$ then for $|n\rangle$ an eigenstate: $(H-\mu N)\mid n\rangle =E_{n}\mid n\rangle ,$ so is $\psi _{\alpha }\mid n\rangle$ : $(H-\mu N)\psi _{\alpha }\mid n\rangle =(E_{n}-\xi _{\alpha })\psi _{\alpha }\mid n\rangle ,$ and so is $\psi _{\alpha }^{\dagger }\mid n\rangle$ : $(H-\mu N)\psi _{\alpha }^{\dagger }\mid n\rangle =(E_{n}+\xi _{\alpha })\psi _{\alpha }^{\dagger }\mid n\rangle .$

We therefore have $\langle m\mid \psi _{\alpha }\mid n\rangle \langle n\mid \psi _{\beta }^{\dagger }\mid m\rangle =\delta _{\xi _{\alpha },\xi _{\beta }}\delta _{E_{n},E_{m}+\xi _{\alpha }}\langle m\mid \psi _{\alpha }\mid n\rangle \langle n\mid \psi _{\beta }^{\dagger }\mid m\rangle .$

We then rewrite $\rho _{\alpha \beta }(\omega )={\frac {1}{\mathcal {Z}}}\sum _{m,n}2\pi \delta (\xi _{\alpha }-\omega )\delta _{\xi _{\alpha },\xi _{\beta }}\langle m\mid \psi _{\alpha }\mid n\rangle \langle n\mid \psi _{\beta }^{\dagger }\mid m\rangle e^{-\beta E_{m}}\left(1-\zeta e^{-\beta \xi _{\alpha }}\right),$ therefore $\rho _{\alpha \beta }(\omega )={\frac {1}{\mathcal {Z}}}\sum _{m}2\pi \delta (\xi _{\alpha }-\omega )\delta _{\xi _{\alpha },\xi _{\beta }}\langle m\mid \psi _{\alpha }\psi _{\beta }^{\dagger }e^{-\beta (H-\mu N)}\mid m\rangle \left(1-\zeta e^{-\beta \xi _{\alpha }}\right),$ use $\langle m\mid \psi _{\alpha }\psi _{\beta }^{\dagger }\mid m\rangle =\delta _{\alpha ,\beta }\langle m\mid \zeta \psi _{\alpha }^{\dagger }\psi _{\alpha }+1\mid m\rangle$ and the fact that the thermal average of the number operator gives the Bose–Einstein or Fermi–Dirac distribution function.

Finally, the spectral density simplifies to give $\rho _{\alpha \beta }=2\pi \delta (\xi _{\alpha }-\omega )\delta _{\alpha \beta },$ so that the thermal Green function is ${\mathcal {G}}_{\alpha \beta }(\omega _{n})={\frac {\delta _{\alpha \beta }}{-i\omega _{n}+\xi _{\beta }}}$ and the retarded Green function is $G_{\alpha \beta }(\omega )={\frac {\delta _{\alpha \beta }}{-(\omega +i\eta )+\xi _{\beta }}}.$ Note that the noninteracting Green function is diagonal, but this will not be true in the interacting case.
