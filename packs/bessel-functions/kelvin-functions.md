---
title: "Kelvin functions"
source: https://en.wikipedia.org/wiki/Kelvin_functions
domain: bessel-functions
license: CC-BY-SA-4.0
tags: bessel function, spherical bessel function, modified bessel function, kelvin functions
fetched: 2026-07-02
---

# Kelvin functions

In applied mathematics, the **Kelvin functions** ber*ν*(*x*) and bei*ν*(*x*) are the real and imaginary parts, respectively, of

$J_{\nu }\left(xe^{\frac {3\pi i}{4}}\right),\,$

where *x* is real, and *Jν*(*z*), is the *ν*th order Bessel function of the first kind. Similarly, the functions kerν(*x*) and keiν(*x*) are the real and imaginary parts, respectively, of

$e^{-\nu \pi i/2}K_{\nu }\left(xe^{\frac {\pi i}{4}}\right),\,$

where *Kν*(*z*) is the *ν*th order modified Bessel function of the second kind.

These functions are named after William Thomson, 1st Baron Kelvin.

While the Kelvin functions are defined as the real and imaginary parts of Bessel functions with *x* taken to be real, the functions can be analytically continued for complex arguments *xe**iφ*, 0 ≤ *φ* < 2*π*. With the exception of ber*n*(*x*) and bei*n*(*x*) for integral *n*, the Kelvin functions have a branch point at *x* = 0.

Below, Γ(*z*) is the gamma function and *ψ*(*z*) is the digamma function.

## ber(*x*)

For integers *n*, ber*n*(*x*) has the series expansion

$\mathrm {ber} _{n}(x)=\left({\frac {x}{2}}\right)^{n}\sum _{k\geq 0}{\frac {\cos \left[\left({\frac {3n}{4}}+{\frac {k}{2}}\right)\pi \right]}{k!\Gamma (n+k+1)}}\left({\frac {x^{2}}{4}}\right)^{k},$

where Γ(*z*) is the gamma function. The special case ber0(*x*), commonly denoted as just ber(*x*), has the series expansion

$\mathrm {ber} (x)=1+\sum _{k\geq 1}{\frac {(-1)^{k}}{[(2k)!]^{2}}}\left({\frac {x}{2}}\right)^{4k}$

and asymptotic series

$\mathrm {ber} (x)\sim {\frac {e^{\frac {x}{\sqrt {2}}}}{\sqrt {2\pi x}}}\left(f_{1}(x)\cos \alpha +g_{1}(x)\sin \alpha \right)-{\frac {\mathrm {kei} (x)}{\pi }}$

,

where

$\alpha ={\frac {x}{\sqrt {2}}}-{\frac {\pi }{8}},$

$f_{1}(x)=1+\sum _{k\geq 1}{\frac {\cos(k\pi /4)}{k!(8x)^{k}}}\prod _{l=1}^{k}(2l-1)^{2}$

$g_{1}(x)=\sum _{k\geq 1}{\frac {\sin(k\pi /4)}{k!(8x)^{k}}}\prod _{l=1}^{k}(2l-1)^{2}.$

## bei(*x*)

For integers *n*, bei*n*(*x*) has the series expansion

$\mathrm {bei} _{n}(x)=\left({\frac {x}{2}}\right)^{n}\sum _{k\geq 0}{\frac {\sin \left[\left({\frac {3n}{4}}+{\frac {k}{2}}\right)\pi \right]}{k!\Gamma (n+k+1)}}\left({\frac {x^{2}}{4}}\right)^{k}.$

The special case bei0(*x*), commonly denoted as just bei(*x*), has the series expansion

$\mathrm {bei} (x)=\sum _{k\geq 0}{\frac {(-1)^{k}}{[(2k+1)!]^{2}}}\left({\frac {x}{2}}\right)^{4k+2}$

and asymptotic series

$\mathrm {bei} (x)\sim {\frac {e^{\frac {x}{\sqrt {2}}}}{\sqrt {2\pi x}}}[f_{1}(x)\sin \alpha -g_{1}(x)\cos \alpha ]-{\frac {\mathrm {ker} (x)}{\pi }},$

where α, $f_{1}(x)$ , and $g_{1}(x)$ are defined as for ber(*x*).

## ker(*x*)

For integers *n*, ker*n*(*x*) has the (complicated) series expansion

${\begin{aligned}&\mathrm {ker} _{n}(x)=-\ln \left({\frac {x}{2}}\right)\mathrm {ber} _{n}(x)+{\frac {\pi }{4}}\mathrm {bei} _{n}(x)\\&+{\frac {1}{2}}\left({\frac {x}{2}}\right)^{-n}\sum _{k=0}^{n-1}\cos \left[\left({\frac {3n}{4}}+{\frac {k}{2}}\right)\pi \right]{\frac {(n-k-1)!}{k!}}\left({\frac {x^{2}}{4}}\right)^{k}\\&+{\frac {1}{2}}\left({\frac {x}{2}}\right)^{n}\sum _{k\geq 0}\cos \left[\left({\frac {3n}{4}}+{\frac {k}{2}}\right)\pi \right]{\frac {\psi (k+1)+\psi (n+k+1)}{k!(n+k)!}}\left({\frac {x^{2}}{4}}\right)^{k}.\end{aligned}}$

The special case ker0(*x*), commonly denoted as just ker(*x*), has the series expansion

$\mathrm {ker} (x)=-\ln \left({\frac {x}{2}}\right)\mathrm {ber} (x)+{\frac {\pi }{4}}\mathrm {bei} (x)+\sum _{k\geq 0}(-1)^{k}{\frac {\psi (2k+1)}{[(2k)!]^{2}}}\left({\frac {x^{2}}{4}}\right)^{2k}$

and the asymptotic series

$\mathrm {ker} (x)\sim {\sqrt {\frac {\pi }{2x}}}e^{-{\frac {x}{\sqrt {2}}}}[f_{2}(x)\cos \beta +g_{2}(x)\sin \beta ],$

where

$\beta ={\frac {x}{\sqrt {2}}}+{\frac {\pi }{8}},$

$f_{2}(x)=1+\sum _{k\geq 1}(-1)^{k}{\frac {\cos(k\pi /4)}{k!(8x)^{k}}}\prod _{l=1}^{k}(2l-1)^{2}$

$g_{2}(x)=\sum _{k\geq 1}(-1)^{k}{\frac {\sin(k\pi /4)}{k!(8x)^{k}}}\prod _{l=1}^{k}(2l-1)^{2}.$

## kei(*x*)

For integer *n*, kei*n*(*x*) has the series expansion

${\begin{aligned}&\mathrm {kei} _{n}(x)=-\ln \left({\frac {x}{2}}\right)\mathrm {bei} _{n}(x)-{\frac {\pi }{4}}\mathrm {ber} _{n}(x)\\&-{\frac {1}{2}}\left({\frac {x}{2}}\right)^{-n}\sum _{k=0}^{n-1}\sin \left[\left({\frac {3n}{4}}+{\frac {k}{2}}\right)\pi \right]{\frac {(n-k-1)!}{k!}}\left({\frac {x^{2}}{4}}\right)^{k}\\&+{\frac {1}{2}}\left({\frac {x}{2}}\right)^{n}\sum _{k\geq 0}\sin \left[\left({\frac {3n}{4}}+{\frac {k}{2}}\right)\pi \right]{\frac {\psi (k+1)+\psi (n+k+1)}{k!(n+k)!}}\left({\frac {x^{2}}{4}}\right)^{k}.\end{aligned}}$

The special case kei0(*x*), commonly denoted as just kei(*x*), has the series expansion

$\mathrm {kei} (x)=-\ln \left({\frac {x}{2}}\right)\mathrm {bei} (x)-{\frac {\pi }{4}}\mathrm {ber} (x)+\sum _{k\geq 0}(-1)^{k}{\frac {\psi (2k+2)}{[(2k+1)!]^{2}}}\left({\frac {x^{2}}{4}}\right)^{2k+1}$

and the asymptotic series

$\mathrm {kei} (x)\sim -{\sqrt {\frac {\pi }{2x}}}e^{-{\frac {x}{\sqrt {2}}}}[f_{2}(x)\sin \beta +g_{2}(x)\cos \beta ],$

where *β*, *f*2(*x*), and *g*2(*x*) are defined as for ker(*x*).
