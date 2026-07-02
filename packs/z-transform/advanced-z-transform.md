---
title: "Advanced z-transform"
source: https://en.wikipedia.org/wiki/Advanced_Z-transform
domain: z-transform
license: CC-BY-SA-4.0
tags: z-transform, bilinear transform, region of convergence, digital filter
fetched: 2026-07-02
---

# Advanced z-transform

(Redirected from

Advanced Z-transform

)

In mathematics and signal processing, the **advanced z-transform** is an extension of the z-transform, to incorporate ideal delays that are not multiples of the sampling time. The advanced z-transform is widely applied, for example, to accurately model processing delays in digital control. It is also known as the **modified z-transform**.

It takes the form

$F(z,m)=\sum _{k=0}^{\infty }f(kT+m)z^{-k}$

where

- *T* is the sampling period
- *m* (the "delay parameter") is a fraction of the sampling period $[0,T].$

## Properties

If the delay parameter, *m*, is considered fixed then all the properties of the z-transform hold for the advanced z-transform.

### Linearity

${\mathcal {Z}}\left\{\sum _{k=1}^{n}c_{k}f_{k}(t)\right\}=\sum _{k=1}^{n}c_{k}F_{k}(z,m).$

### Time shift

${\mathcal {Z}}\left\{u(t-nT)f(t-nT)\right\}=z^{-n}F(z,m).$

### Damping

${\mathcal {Z}}\left\{f(t)e^{-a\,t}\right\}=e^{-a\,m}F(e^{a\,T}z,m).$

### Time multiplication

${\mathcal {Z}}\left\{t^{y}f(t)\right\}=\left(-Tz{\frac {d}{dz}}+m\right)^{y}F(z,m).$

### Final value theorem

$\lim _{k\to \infty }f(kT+m)=\lim _{z\to 1}(1-z^{-1})F(z,m).$

## Example

Consider the following example where $f(t)=\cos(\omega t)$ :

${\begin{aligned}F(z,m)&={\mathcal {Z}}\left\{\cos \left(\omega \left(kT+m\right)\right)\right\}\\&={\mathcal {Z}}\left\{\cos(\omega kT)\cos(\omega m)-\sin(\omega kT)\sin(\omega m)\right\}\\&=\cos(\omega m){\mathcal {Z}}\left\{\cos(\omega kT)\right\}-\sin(\omega m){\mathcal {Z}}\left\{\sin(\omega kT)\right\}\\&=\cos(\omega m){\frac {z\left(z-\cos(\omega T)\right)}{z^{2}-2z\cos(\omega T)+1}}-\sin(\omega m){\frac {z\sin(\omega T)}{z^{2}-2z\cos(\omega T)+1}}\\&={\frac {z^{2}\cos(\omega m)-z\cos(\omega (T-m))}{z^{2}-2z\cos(\omega T)+1}}.\end{aligned}}$

If $m=0$ then $F(z,m)$ reduces to the transform

$F(z,0)={\frac {z^{2}-z\cos(\omega T)}{z^{2}-2z\cos(\omega T)+1}},$

which is clearly just the *z*-transform of $f(t)$ .
