---
title: "Alpha–beta transformation"
source: https://en.wikipedia.org/wiki/Clarke_transformation
domain: field-oriented-control
license: CC-BY-SA-4.0
tags: vector control motor, Clarke transformation, space vector modulation, field-oriented control
fetched: 2026-07-02
---

# Alpha–beta transformation

(Redirected from

Clarke transformation

)

In electrical engineering, the **alpha-beta** ( $\alpha \beta \gamma$ ) **transformation** (also known as the **Clarke transformation**) is a mathematical transformation employed to simplify the analysis of three-phase circuits. Conceptually it is similar to the dq0 transformation. One very useful application of the $\alpha \beta \gamma$ transformation is the generation of the reference signal used for space vector modulation control of three-phase inverters.

## History

In 1937 and 1938, Edith Clarke published papers with modified methods of calculations on unbalanced three-phase problems, that turned out to be particularly useful.

## Definition

The $\alpha \beta \gamma$ transform applied to three-phase currents, as used by Edith Clarke, is

${\begin{bmatrix}i_{\alpha }(t)\\i_{\beta }(t)\\i_{\gamma }(t)\end{bmatrix}}=i_{\alpha \beta \gamma }(t)=Ti_{abc}(t)={\frac {2}{3}}{\begin{bmatrix}1&-{\frac {1}{2}}&-{\frac {1}{2}}\\0&{\frac {\sqrt {3}}{2}}&-{\frac {\sqrt {3}}{2}}\\{\frac {1}{2}}&{\frac {1}{2}}&{\frac {1}{2}}\\\end{bmatrix}}{\begin{bmatrix}i_{a}(t)\\i_{b}(t)\\i_{c}(t)\end{bmatrix}}$

where $i_{abc}(t)$ is a generic three-phase current sequence and $i_{\alpha \beta \gamma }(t)$ is the corresponding current sequence given by the transformation T . The inverse transform is:

${\begin{bmatrix}i_{a}(t)\\i_{b}(t)\\i_{c}(t)\end{bmatrix}}=i_{abc}(t)=T^{-1}i_{\alpha \beta \gamma }(t)={\begin{bmatrix}1&0&1\\-{\frac {1}{2}}&{\frac {\sqrt {3}}{2}}&1\\-{\frac {1}{2}}&-{\frac {\sqrt {3}}{2}}&1\end{bmatrix}}{\begin{bmatrix}i_{\alpha }(t)\\i_{\beta }(t)\\i_{\gamma }(t)\end{bmatrix}}.$

The above Clarke's transformation preserves the amplitude of the electrical variables which it is applied to. Indeed, consider a three-phase symmetric, direct, current sequence

${\begin{aligned}i_{a}(t)=&{\sqrt {2}}I\cos \theta (t),\\i_{b}(t)=&{\sqrt {2}}I\cos \left(\theta (t)-{\frac {2}{3}}\pi \right),\\i_{c}(t)=&{\sqrt {2}}I\cos \left(\theta (t)+{\frac {2}{3}}\pi \right),\end{aligned}}$

where I is the RMS of $i_{a}(t)$ , $i_{b}(t)$ , $i_{c}(t)$ and $\theta (t)$ is the generic time-varying angle that can also be set to $\omega t$ without loss of generality. Then, by applying T to the current sequence, it results

${\begin{aligned}i_{\alpha }=&{\sqrt {2}}I\cos \theta (t),\\i_{\beta }=&{\sqrt {2}}I\sin \theta (t),\\i_{\gamma }=&0,\end{aligned}}$

where the last equation holds since we have considered balanced currents. As it is shown in the above, the amplitudes of the currents in the $\alpha \beta \gamma$ reference frame are the same of that in the natural reference frame.

### Power invariant transformation

The active and reactive powers computed in the Clarke's domain with the transformation shown above are not the same of those computed in the standard reference frame. This happens because T is not unitary. In order to preserve the active and reactive powers one has, instead, to consider

$i_{\alpha \beta \gamma }(t)=Ui_{abc}(t)={\sqrt {\frac {2}{3}}}{\begin{bmatrix}1&-{\frac {1}{2}}&-{\frac {1}{2}}\\0&{\frac {\sqrt {3}}{2}}&-{\frac {\sqrt {3}}{2}}\\{\frac {1}{\sqrt {2}}}&{\frac {1}{\sqrt {2}}}&{\frac {1}{\sqrt {2}}}\\\end{bmatrix}}{\begin{bmatrix}i_{a}(t)\\i_{b}(t)\\i_{c}(t)\end{bmatrix}},$

where U is a (real) unitary matrix and the inverse coincides with its transpose. In this case the amplitudes of the transformed currents are not the same of those in the standard reference frame, that is

${\begin{aligned}i_{\alpha }=&{\sqrt {3}}I\cos \theta (t),\\i_{\beta }=&{\sqrt {3}}I\sin \theta (t),\\i_{\gamma }=&0.\end{aligned}}$

Finally, the inverse transformation in this case is

$i_{abc}(t)={\sqrt {\frac {2}{3}}}{\begin{bmatrix}1&0&{\frac {1}{\sqrt {2}}}\\-{\frac {1}{2}}&{\frac {\sqrt {3}}{2}}&{\frac {1}{\sqrt {2}}}\\-{\frac {1}{2}}&-{\frac {\sqrt {3}}{2}}&{\frac {1}{\sqrt {2}}}\\\end{bmatrix}}{\begin{bmatrix}i_{\alpha }(t)\\i_{\beta }(t)\\i_{\gamma }(t)\end{bmatrix}}.$

### Simplified transformation

Since in a balanced system $i_{a}(t)+i_{b}(t)+i_{c}(t)=0$ and thus $i_{\gamma }(t)=0$ one can also consider the simplified transform

${\begin{aligned}i_{\alpha \beta }(t)&={\frac {2}{3}}{\begin{bmatrix}1&-{\frac {1}{2}}&-{\frac {1}{2}}\\0&{\frac {\sqrt {3}}{2}}&-{\frac {\sqrt {3}}{2}}\end{bmatrix}}{\begin{bmatrix}i_{a}(t)\\i_{b}(t)\\i_{c}(t)\end{bmatrix}}\\&={\begin{bmatrix}1&0\\{\frac {1}{\sqrt {3}}}&{\frac {2}{\sqrt {3}}}\end{bmatrix}}{\begin{bmatrix}i_{a}(t)\\i_{b}(t)\end{bmatrix}}\end{aligned}}$

which is simply the original Clarke's transformation with the 3rd equation excluded, and

$i_{abc}(t)={\frac {3}{2}}{\begin{bmatrix}{\frac {2}{3}}&0\\-{\frac {1}{3}}&{\frac {\sqrt {3}}{3}}\\-{\frac {1}{3}}&-{\frac {\sqrt {3}}{3}}\end{bmatrix}}{\begin{bmatrix}i_{\alpha }(t)\\i_{\beta }(t)\end{bmatrix}}$

which is the corresponding inverse transformation.

## Geometric Interpretation

The $\alpha \beta \gamma$ transformation can be thought of as the projection of the three phase quantities (voltages or currents) onto two stationary axes, the alpha axis and the beta axis. However, no information is lost if the system is balanced, as the equation $I_{a}+I_{b}+I_{c}=0$ is equivalent to the equation for $I_{\gamma }$ in the transform. If the system is not balanced, then the $I_{\gamma }$ term will contain the error component of the projection. Thus, a $I_{\gamma }$ of zero indicates that the system is balanced (and thus exists entirely in the alpha-beta coordinate space), and can be ignored for two coordinate calculations that operate under this assumption that the system is balanced. This is the elegance of the Clarke transform as it reduces a three component system into a two component system thanks to this assumption.

Another way to understand this is that the equation $I_{a}+I_{b}+I_{c}=0$ defines a plane in a euclidean three coordinate space. The alpha-beta coordinate space can be understood as the two coordinate space defined by this plane, i.e. the alpha-beta axes lie on the plane defined by $I_{a}+I_{b}+I_{c}=0$ .

This also means that in order the use the Clarke transform, one must ensure the system is balanced, otherwise subsequent two coordinate calculations will be erroneous. This is a practical consideration in applications where the three phase quantities are measured and can possibly have measurement error.

### *dq*0 transform

The $dq0$ transform is conceptually similar to the $\alpha \beta \gamma$ transform. Whereas the $\alpha \beta \gamma$ transform is the projection of the phase quantities onto a stationary two-axis reference frame, the $dq0$ transform can be thought of as the projection of the phase quantities onto a rotating two-axis reference frame.
