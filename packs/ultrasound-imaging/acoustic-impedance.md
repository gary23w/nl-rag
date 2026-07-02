---
title: "Acoustic impedance"
source: https://en.wikipedia.org/wiki/Acoustic_impedance
domain: ultrasound-imaging
license: CC-BY-SA-4.0
tags: medical ultrasonography, ultrasound imaging, doppler ultrasound, acoustic impedance
fetched: 2026-07-02
---

# Acoustic impedance

**Acoustic impedance** and **specific acoustic impedance** are measures of the opposition that a system presents to the acoustic flow resulting from an acoustic pressure applied to the system. The SI unit of acoustic impedance is the pascal-second per cubic metre (symbol Pa·s/m3), or in the MKS system the rayl per square metre (Rayl/m2), while that of specific acoustic impedance is the pascal-second per metre (Pa·s/m), or in the MKS system the rayl (Rayl). There is a close analogy with electrical impedance, which measures the opposition that a system presents to the electric current resulting from a voltage applied to the system.

## Mathematical definitions

### Acoustic impedance

For a linear time-invariant system, the relationship between the acoustic pressure applied to the system and the resulting acoustic volume flow rate through a surface perpendicular to the direction of that pressure at its point of application is given by:

$p(t)=[R*Q](t),$

or equivalently by

$Q(t)=[G*p](t),$

where

- *p* is the acoustic pressure;
- *Q* is the acoustic volume flow rate;
- * is the convolution operator;
- *R* is the **acoustic resistance in the *time domain***;
- *G* = *R*−1 is the **acoustic conductance in the *time domain*** (*R*−1 is the convolution inverse of *R*).

**Acoustic impedance**, denoted *Z*, is the Laplace transform, or the Fourier transform, or the analytic representation of *time domain* acoustic resistance:

$Z(s){\stackrel {\mathrm {def} }{{}={}}}{\mathcal {L}}[R](s)={\frac {{\mathcal {L}}[p](s)}{{\mathcal {L}}[Q](s)}},$

$Z(\omega ){\stackrel {\mathrm {def} }{{}={}}}{\mathcal {F}}[R](\omega )={\frac {{\mathcal {F}}[p](\omega )}{{\mathcal {F}}[Q](\omega )}},$

$Z(t){\stackrel {\mathrm {def} }{{}={}}}R_{\mathrm {a} }(t)={\frac {1}{2}}\!\left[p_{\mathrm {a} }*\left(Q^{-1}\right)_{\mathrm {a} }\right]\!(t),$

where

- ${\mathcal {L}}$ is the Laplace transform operator;
- ${\mathcal {F}}$ is the Fourier transform operator;
- subscript "a" is the analytic representation operator;
- *Q*−1 is the convolution inverse of *Q*.

**Acoustic resistance**, denoted *R*, and **acoustic reactance**, denoted *X*, are the real part and imaginary part of acoustic impedance respectively:

$Z(s)=R(s)+iX(s),$

$Z(\omega )=R(\omega )+iX(\omega ),$

$Z(t)=R(t)+iX(t),$

where

- *i* is the imaginary unit;
- in *Z*(*s*), *R*(*s*) is *not* the Laplace transform of the time domain acoustic resistance *R*(*t*), *Z*(*s*) is;
- in *Z*(*ω*), *R*(*ω*) is *not* the Fourier transform of the time domain acoustic resistance *R*(*t*), *Z*(*ω*) is;
- in *Z*(*t*), *R*(*t*) is the time domain acoustic resistance and *X*(*t*) is the Hilbert transform of the time domain acoustic resistance *R*(*t*), according to the definition of the analytic representation.

**Inductive acoustic reactance**, denoted *X**L*, and **capacitive acoustic reactance**, denoted *X**C*, are the positive part and negative part of acoustic reactance respectively:

$X(s)=X_{L}(s)-X_{C}(s),$

$X(\omega )=X_{L}(\omega )-X_{C}(\omega ),$

$X(t)=X_{L}(t)-X_{C}(t).$

**Acoustic admittance**, denoted *Y*, is the Laplace transform, or the Fourier transform, or the analytic representation of *time domain* acoustic conductance:

$Y(s){\stackrel {\mathrm {def} }{{}={}}}{\mathcal {L}}[G](s)={\frac {1}{Z(s)}}={\frac {{\mathcal {L}}[Q](s)}{{\mathcal {L}}[p](s)}},$

$Y(\omega ){\stackrel {\mathrm {def} }{{}={}}}{\mathcal {F}}[G](\omega )={\frac {1}{Z(\omega )}}={\frac {{\mathcal {F}}[Q](\omega )}{{\mathcal {F}}[p](\omega )}},$

$Y(t){\stackrel {\mathrm {def} }{{}={}}}G_{\mathrm {a} }(t)=Z^{-1}(t)={\frac {1}{2}}\!\left[Q_{\mathrm {a} }*\left(p^{-1}\right)_{\mathrm {a} }\right]\!(t),$

where

- *Z*−1 is the convolution inverse of *Z*;
- *p*−1 is the convolution inverse of *p*.

**Acoustic conductance**, denoted *G*, and **acoustic susceptance**, denoted *B*, are the real part and imaginary part of acoustic admittance, respectively:

$Y(s)=G(s)+iB(s),$

$Y(\omega )=G(\omega )+iB(\omega ),$

$Y(t)=G(t)+iB(t),$

where

- in *Y*(*s*), *G*(*s*) is *not* the Laplace transform of the time domain acoustic conductance *G*(*t*), *Y*(*s*) is;
- in *Y*(*ω*), *G*(*ω*) is *not* the Fourier transform of the time domain acoustic conductance *G*(*t*), *Y*(*ω*) is;
- in *Y*(*t*), *G*(*t*) is the time domain acoustic conductance and *B*(*t*) is the Hilbert transform of the time domain acoustic conductance *G*(*t*), according to the definition of the analytic representation.

Acoustic resistance represents the energy transfer of an acoustic wave. The pressure and motion are in phase, so work is done on the medium ahead of the wave. Acoustic reactance represents the pressure that is out of phase with the motion and causes no average energy transfer. For example, a closed bulb connected to an organ pipe will have air moving into it and pressure, but they are out of phase, so no net energy is transmitted into it. While the pressure rises, air moves in, and while it falls, it moves out, but the average pressure when the air moves in is the same as that when it moves out, so the power flows back and forth but with no time-averaged energy transfer. A further electrical analogy is a capacitor connected across a power line: current flows through the capacitor but it is out of phase with the voltage, so no net power is transmitted into it.

### Specific acoustic impedance

For a linear time-invariant system, the relationship between the acoustic pressure applied to the system and the resulting particle velocity in the direction of that pressure at its point of application is given by

$p(t)=[r*v](t),$

or equivalently by:

$v(t)=[g*p](t),$

where

- *p* is the acoustic pressure;
- *v* is the particle velocity;
- *r* is the **specific acoustic resistance in the *time domain***;
- *g* = *r*−1 is the **specific acoustic conductance in the *time domain*** (*r*−1 is the convolution inverse of *r*).

**Specific acoustic impedance**, denoted *z* is the Laplace transform, or the Fourier transform, or the analytic representation of *time domain* specific acoustic resistance:

$z(s){\stackrel {\mathrm {def} }{{}={}}}{\mathcal {L}}[r](s)={\frac {{\mathcal {L}}[p](s)}{{\mathcal {L}}[v](s)}},$

$z(\omega ){\stackrel {\mathrm {def} }{{}={}}}{\mathcal {F}}[r](\omega )={\frac {{\mathcal {F}}[p](\omega )}{{\mathcal {F}}[v](\omega )}},$

$z(t){\stackrel {\mathrm {def} }{{}={}}}r_{\mathrm {a} }(t)={\frac {1}{2}}\!\left[p_{\mathrm {a} }*\left(v^{-1}\right)_{\mathrm {a} }\right]\!(t),$

where *v*−1 is the convolution inverse of *v*.

**Specific acoustic resistance**, denoted *r*, and **specific acoustic reactance**, denoted *x*, are the real part and imaginary part of specific acoustic impedance respectively:

$z(s)=r(s)+ix(s),$

$z(\omega )=r(\omega )+ix(\omega ),$

$z(t)=r(t)+ix(t),$

where

- in *z*(*s*), *r*(*s*) is *not* the Laplace transform of the time domain specific acoustic resistance *r*(*t*), *z*(*s*) is;
- in *z*(*ω*), *r*(*ω*) is *not* the Fourier transform of the time domain specific acoustic resistance *r*(*t*), *z*(*ω*) is;
- in *z*(*t*), *r*(*t*) is the time domain specific acoustic resistance and *x*(*t*) is the Hilbert transform of the time domain specific acoustic resistance *r*(*t*), according to the definition of the analytic representation.

**Specific inductive acoustic reactance**, denoted *x**L*, and **specific capacitive acoustic reactance**, denoted *x**C*, are the positive part and negative part of specific acoustic reactance respectively:

$x(s)=x_{L}(s)-x_{C}(s),$

$x(\omega )=x_{L}(\omega )-x_{C}(\omega ),$

$x(t)=x_{L}(t)-x_{C}(t).$

**Specific acoustic admittance**, denoted *y*, is the Laplace transform, or the Fourier transform, or the analytic representation of *time domain* specific acoustic conductance:

$y(s){\stackrel {\mathrm {def} }{{}={}}}{\mathcal {L}}[g](s)={\frac {1}{z(s)}}={\frac {{\mathcal {L}}[v](s)}{{\mathcal {L}}[p](s)}},$

$y(\omega ){\stackrel {\mathrm {def} }{{}={}}}{\mathcal {F}}[g](\omega )={\frac {1}{z(\omega )}}={\frac {{\mathcal {F}}[v](\omega )}{{\mathcal {F}}[p](\omega )}},$

$y(t){\stackrel {\mathrm {def} }{{}={}}}g_{\mathrm {a} }(t)=z^{-1}(t)={\frac {1}{2}}\!\left[v_{\mathrm {a} }*\left(p^{-1}\right)_{\mathrm {a} }\right]\!(t),$

where

- *z*−1 is the convolution inverse of *z*;
- *p*−1 is the convolution inverse of *p*.

**Specific acoustic conductance**, denoted *g*, and **specific acoustic susceptance**, denoted *b*, are the real part and imaginary part of specific acoustic admittance respectively:

$y(s)=g(s)+ib(s),$

$y(\omega )=g(\omega )+ib(\omega ),$

$y(t)=g(t)+ib(t),$

where

- in *y*(*s*), *g*(*s*) is *not* the Laplace transform of the time domain acoustic conductance *g*(*t*), *y*(*s*) is;
- in *y*(*ω*), *g*(*ω*) is *not* the Fourier transform of the time domain acoustic conductance *g*(*t*), *y*(*ω*) is;
- in *y*(*t*), *g*(*t*) is the time domain acoustic conductance and *b*(*t*) is the Hilbert transform of the time domain acoustic conductance *g*(*t*), according to the definition of the analytic representation.

Specific acoustic impedance *z* is an intensive property of a particular *medium* (e.g., the *z* of air or water can be specified); on the other hand, acoustic impedance *Z* is an extensive property of a particular *medium and geometry* (e.g., the *Z* of a particular duct filled with air can be specified).

### Acoustic ohm

The **acoustic ohm** is a unit of measurement of acoustic impedance. The SI unit of pressure is the pascal and of flow is cubic metres per second, so the acoustic ohm is equal to 1 Pa·s/m3.

The acoustic ohm can be applied to fluid flow outside the domain of acoustics. For such applications, a **hydraulic ohm** with an identical definition may be used. A hydraulic ohm measurement would be the ratio of hydraulic pressure to hydraulic volume flow.

### Relationship

For a *one-dimensional* wave passing through an aperture with area *A*, the acoustic volume flow rate *Q* is the volume of medium passing per second through the aperture; if the acoustic flow moves a distance d*x* = *v* d*t*, then the volume of medium passing through is d*V* = *A* d*x*, so:

$Q={\frac {\mathrm {d} V}{\mathrm {d} t}}=A{\frac {\mathrm {d} x}{\mathrm {d} t}}=Av.$

If the wave is one-dimensional, it yields

$Z(s)={\frac {{\mathcal {L}}[p](s)}{{\mathcal {L}}[Q](s)}}={\frac {{\mathcal {L}}[p](s)}{A{\mathcal {L}}[v](s)}}={\frac {z(s)}{A}},$

$Z(\omega )={\frac {{\mathcal {F}}[p](\omega )}{{\mathcal {F}}[Q](\omega )}}={\frac {{\mathcal {F}}[p](\omega )}{A{\mathcal {F}}[v](\omega )}}={\frac {z(\omega )}{A}},$

$Z(t)={\frac {1}{2}}\!\left[p_{\mathrm {a} }*\left(Q^{-1}\right)_{\mathrm {a} }\right]\!(t)={\frac {1}{2}}\!\left[p_{\mathrm {a} }*\left({\frac {v^{-1}}{A}}\right)_{\mathrm {a} }\right]\!(t)={\frac {z(t)}{A}}.$

## Characteristic acoustic impedance

### Characteristic specific acoustic impedance

The constitutive law of nondispersive linear acoustics in one dimension gives a relation between stress and strain:

$p=-\rho c^{2}{\frac {\partial \delta }{\partial x}},$

where

- *p* is the acoustic pressure in the medium;
- *ρ* is the volumetric mass density of the medium;
- *c* is the speed of the sound waves traveling in the medium;
- *δ* is the particle displacement;
- *x* is the space variable along the direction of propagation of the sound waves.

This equation is valid both for fluids and solids. In

- fluids, *ρc*2 = *K* (*K* stands for the bulk modulus);
- solids, *ρc*2 = *K* + 4/3 *G* (*G* stands for the shear modulus) for longitudinal waves and *ρc2* = *G* for transverse waves.

Newton's second law applied locally in the medium gives:

$\rho {\frac {\partial ^{2}\delta }{\partial t^{2}}}=-{\frac {\partial p}{\partial x}}.$

Combining this equation with the previous one yields the one-dimensional wave equation:

${\frac {\partial ^{2}\delta }{\partial t^{2}}}=c^{2}{\frac {\partial ^{2}\delta }{\partial x^{2}}}.$

The *plane waves*

$\delta (\mathbf {r} ,\,t)=\delta (x,\,t)$

that are solutions of this wave equation are composed of the sum of *two progressive plane waves* traveling along *x* with the same speed and *in opposite ways*:

$\delta (\mathbf {r} ,\,t)=f(x-ct)+g(x+ct)$

from which can be derived

$v(\mathbf {r} ,\,t)={\frac {\partial \delta }{\partial t}}(\mathbf {r} ,\,t)=-c{\big [}f'(x-ct)-g'(x+ct){\big ]},$

$p(\mathbf {r} ,\,t)=-\rho c^{2}{\frac {\partial \delta }{\partial x}}(\mathbf {r} ,\,t)=-\rho c^{2}{\big [}f'(x-ct)+g'(x+ct){\big ]}.$

For *progressive* plane waves:

${\begin{cases}p(\mathbf {r} ,\,t)=-\rho c^{2}\,f'(x-ct)\\v(\mathbf {r} ,\,t)=-c\,f'(x-ct)\end{cases}}$

or

${\begin{cases}p(\mathbf {r} ,\,t)=-\rho c^{2}\,g'(x+ct)\\v(\mathbf {r} ,\,t)=c\,g'(x+ct).\end{cases}}$

Finally, the specific acoustic impedance *z* is

$z(\mathbf {r} ,\,s)={\frac {{\mathcal {L}}[p](\mathbf {r} ,\,s)}{{\mathcal {L}}[v](\mathbf {r} ,\,s)}}=\pm \rho c,$

$z(\mathbf {r} ,\,\omega )={\frac {{\mathcal {F}}[p](\mathbf {r} ,\,\omega )}{{\mathcal {F}}[v](\mathbf {r} ,\,\omega )}}=\pm \rho c,$

$z(\mathbf {r} ,\,t)={\frac {1}{2}}\!\left[p_{\mathrm {a} }*\left(v^{-1}\right)_{\mathrm {a} }\right]\!(\mathbf {r} ,\,t)=\pm \rho c.$

The absolute value of this specific acoustic impedance is often called **characteristic specific acoustic impedance** and denoted *z*0:

$z_{0}=\rho c.$

The equations also show that

${\frac {p(\mathbf {r} ,\,t)}{v(\mathbf {r} ,\,t)}}=\pm \rho c=\pm z_{0}.$

### Effect of temperature

Temperature acts on speed of sound and mass density and thus on specific acoustic impedance.

| Celsius tempe­rature *θ* [°C] | Speed of sound *c* [m/s] | Density of air *ρ* [kg/m3] | Characteristic specific acoustic impedance *z*0 [Pa⋅s/m] |
|---|---|---|---|
| 35 | 351.88 | 1.1455 | 403.2 |
| 30 | 349.02 | 1.1644 | 406.5 |
| 25 | 346.13 | 1.1839 | 409.4 |
| 20 | 343.21 | 1.2041 | 413.3 |
| 15 | 340.27 | 1.2250 | 416.9 |
| 10 | 337.31 | 1.2466 | 420.5 |
| 5 | 334.32 | 1.2691 | 424.3 |
| 0 | 331.30 | 1.2923 | 428.0 |
| −5 | 328.25 | 1.3164 | 432.1 |
| −10 | 325.18 | 1.3414 | 436.1 |
| −15 | 322.07 | 1.3674 | 440.3 |
| −20 | 318.94 | 1.3943 | 444.6 |
| −25 | 315.77 | 1.4224 | 449.1 |

### Characteristic acoustic impedance

For a *one dimensional* wave passing through an aperture with area *A*, *Z* = *z*/*A*, so if the wave is a progressive plane wave, then:

$Z(\mathbf {r} ,\,s)=\pm {\frac {\rho c}{A}},$

$Z(\mathbf {r} ,\,\omega )=\pm {\frac {\rho c}{A}},$

$Z(\mathbf {r} ,\,t)=\pm {\frac {\rho c}{A}}.$

The absolute value of this acoustic impedance is often called **characteristic acoustic impedance** and denoted *Z*0:

$Z_{0}={\frac {\rho c}{A}}.$

and the characteristic specific acoustic impedance is

${\frac {p(\mathbf {r} ,\,t)}{Q(\mathbf {r} ,\,t)}}=\pm {\frac {\rho c}{A}}=\pm Z_{0}.$

If the aperture with area *A* is the start of a pipe and a plane wave is sent into the pipe, the wave passing through the aperture is a progressive plane wave in the absence of reflections, and the usually reflections from the other end of the pipe, whether open or closed, are the sum of waves travelling from one end to the other. (It is possible to have no reflections when the pipe is very long, because of the long time taken for the reflected waves to return, and their attenuation through losses at the pipe wall.) Such reflections and resultant standing waves are very important in the design and operation of musical wind instruments.
