---
title: "Denavit–Hartenberg parameters"
source: https://en.wikipedia.org/wiki/Denavit%E2%80%93Hartenberg_parameters
domain: inverse-kinematics-games
license: CC-BY-SA-4.0
tags: inverse kinematics, ik solver, forward kinematics, jacobian ik
fetched: 2026-07-02
---

# Denavit–Hartenberg parameters

In mechatronics engineering, the **Denavit–Hartenberg parameters** (also called **DH parameters**) are the four parameters associated with the DH convention for attaching reference frames to the links of a spatial kinematic chain, or robot manipulator.

Jacques Denavit and Richard Hartenberg introduced this convention in 1955 in order to standardize the coordinate frames for spatial linkages.

Richard Paul demonstrated its value for the kinematic analysis of robotic systems in 1981. While many conventions for attaching reference frames have been developed, the Denavit–Hartenberg convention remains a popular approach.

## Denavit–Hartenberg convention

A commonly used convention for selecting frames of reference in robotics applications is the **Denavit and Hartenberg (D–H) convention** which was introduced by Jacques Denavit and Richard S. Hartenberg. In this convention, coordinate frames are attached to the joints between two links such that one transformation is associated with the joint [*Z* ], and the second is associated with the link [*X* ]. The coordinate transformations along a serial robot consisting of n links form the kinematics equations of the robot:

$[T]=[Z_{1}][X_{1}][Z_{2}][X_{2}]\ldots [X_{n-1}][Z_{n}][X_{n}]\!$

where [*T* ] is the transformation that characterizes the location and orientation of the end-link.

To determine the coordinate transformations [*Z* ] and [*X* ], the joints connecting the links are modeled as either hinged or sliding joints, each of which has a unique line S in space that forms the joint axis and define the relative movement of the two links. A typical serial robot is characterized by a sequence of six lines *Si* (*i* = 1, 2, ..., 6), one for each joint in the robot. For each sequence of lines Si and *S**i*+1, there is a common normal line *A**i*,*i*+1. The system of six joint axes Si and five common normal lines *A**i*,*i*+1 form the kinematic skeleton of the typical six degree-of-freedom serial robot. Denavit and Hartenberg introduced the convention that z-coordinate axes are assigned to the joint axes Si and x-coordinate axes are assigned to the common normals *A**i*,*i*+1.

This convention allows the definition of the movement of links around a common joint axis Si by the screw displacement:

$[Z_{i}]={\begin{bmatrix}\cos \theta _{i}&-\sin \theta _{i}&0&0\\\sin \theta _{i}&\cos \theta _{i}&0&0\\0&0&1&d_{i}\\0&0&0&1\end{bmatrix}}$

where θi is the rotation around and di is the sliding motion along the z-axis. Each of these parameters could be a constant depending on the structure of the robot. Under this convention the dimensions of each link in the serial chain are defined by the screw displacement around the common normal *A**i*,*i*+1 from the joint *S**i* to *S**i*+1, which is given by

$[X_{i}]={\begin{bmatrix}1&0&0&r_{i,i+1}\\0&\cos \alpha _{i,i+1}&-\sin \alpha _{i,i+1}&0\\0&\sin \alpha _{i,i+1}&\cos \alpha _{i,i+1}&0\\0&0&0&1\end{bmatrix}},$

where *α**i*,*i*+1 and *r**i*,*i*+1 define the physical dimensions of the link in terms of the angle measured around and distance measured along the X axis.

In summary, the reference frames are laid out as follows:

1. The z-axis is in the direction of the joint axis.
2. The x-axis is parallel to the common normal: $x_{n}=z_{n}\times z_{n-1}$ (or away from *z**n*–1) If there is no unique common normal (parallel z axes), then d (below) is a free parameter. The direction of xn is from *z**n*–1 to zn, as shown in the video below.
3. the y-axis follows from the x- and z-axes by choosing it to be a right-handed coordinate system.

### Four parameters

The following four transformation parameters are known as D–H parameters:

- d: offset along previous z to the common normal
- θ: angle about previous z from old x to new x
- r: length of the common normal (aka a, but if using this notation, do not confuse with α). Assuming a revolute joint, this is the radius about previous z.
- α: angle about common normal, from old z axis to new z axis

There is some choice in frame layout as to whether the previous x axis or the next x points along the common normal. The latter system allows branching chains more efficiently, as multiple frames can all point away from their common ancestor, but in the alternative layout the ancestor can only point toward one successor. Thus the commonly used notation places each down-chain x axis collinear with the common normal, yielding the transformation calculations shown below.

We can note constraints on the relationships between the axes:

- the xn axis is perpendicular to both the *z**n*–1 and zn axes
- the xn axis intersects both *z**n*–1 and zn axes
- the origin of joint n is at the intersection of xn and zn
- yn completes a right-handed reference frame based on xn and zn

## Denavit–Hartenberg matrix

It is common to separate a screw displacement into product of a pure translation along a line and a pure rotation about the line, so that

$[Z_{i}]=\operatorname {Trans} _{Z_{i}}(d_{i})\operatorname {Rot} _{Z_{i}}(\theta _{i}),$

and

$[X_{i}]=\operatorname {Trans} _{X_{i}}(r_{i,i+1})\operatorname {Rot} _{X_{i}}(\alpha _{i,i+1}).$

Using this notation, each link can be described by a coordinate transformation from the concurrent coordinate system to the previous coordinate system.

${}^{n-1}T_{n}=[Z_{n-1}]\cdot [X_{n}]$

Note that this is the product of two screw displacements. The matrices associated with these operations are:

$\operatorname {Trans} _{z_{n-1}}(d_{n})=\left[{\begin{array}{ccc|c}1&0&0&0\\0&1&0&0\\0&0&1&d_{n}\\\hline 0&0&0&1\end{array}}\right]$

$\operatorname {Rot} _{z_{n-1}}(\theta _{n})=\left[{\begin{array}{ccc|c}\cos \theta _{n}&-\sin \theta _{n}&0&0\\\sin \theta _{n}&\cos \theta _{n}&0&0\\0&0&1&0\\\hline 0&0&0&1\end{array}}\right]$

$\operatorname {Trans} _{x_{n}}(r_{n})=\left[{\begin{array}{ccc|c}1&0&0&r_{n}\\0&1&0&0\\0&0&1&0\\\hline 0&0&0&1\end{array}}\right]$

$\operatorname {Rot} _{x_{n}}(\alpha _{n})=\left[{\begin{array}{ccc|c}1&0&0&0\\0&\cos \alpha _{n}&-\sin \alpha _{n}&0\\0&\sin \alpha _{n}&\cos \alpha _{n}&0\\\hline 0&0&0&1\end{array}}\right]$

This gives:

$\operatorname {} ^{n-1}T_{n}=\left[{\begin{array}{ccc|c}\cos \theta _{n}&-\sin \theta _{n}\cos \alpha _{n}&\sin \theta _{n}\sin \alpha _{n}&r_{n}\cos \theta _{n}\\\sin \theta _{n}&\cos \theta _{n}\cos \alpha _{n}&-\cos \theta _{n}\sin \alpha _{n}&r_{n}\sin \theta _{n}\\0&\sin \alpha _{n}&\cos \alpha _{n}&d_{n}\\\hline 0&0&0&1\end{array}}\right]=\left[{\begin{array}{ccc|c}&&&\\&R&&T\\&&&\\\hline 0&0&0&1\end{array}}\right]$

where *R* is the 3×3 submatrix describing rotation and *T* is the 3×1 submatrix describing translation.

In some books, the order of transformation for a pair of consecutive rotation and translation (such as $d_{n}$ and $\theta _{n}$ ) is reversed. This is possible (despite the fact that in general, matrix multiplication is not commutative) since translations and rotations are concerned with the same axes $z_{n-1}$ and $x_{n}$ , respectively. As matrix multiplication order for these pairs does not matter, the result is the same. For example: $\operatorname {Trans} _{z_{n-1}}(d_{n})\cdot \operatorname {Rot} _{z_{n-1}}(\theta _{n})=\operatorname {Rot} _{z_{n-1}}(\theta _{n})\cdot \operatorname {Trans} _{z_{n-1}}(d_{n})$ .

Therefore, we can write the transformation $\operatorname {} ^{n-1}T_{n}$ as follows: ${}^{n-1}T_{n}=\operatorname {Trans} _{z_{n-1}}(d_{n})\cdot \operatorname {Rot} _{z_{n-1}}(\theta _{n})\cdot \operatorname {Trans} _{x_{n}}(r_{n})\cdot \operatorname {Rot} _{x_{n}}(\alpha _{n})$ ${}^{n-1}T_{n}=\operatorname {Rot} _{z_{n-1}}(\theta _{n})\cdot \operatorname {Trans} _{z_{n-1}}(d_{n})\cdot \operatorname {Trans} _{x_{n}}(r_{n})\cdot \operatorname {Rot} _{x_{n}}(\alpha _{n})$

## Use of Denavit and Hartenberg matrices

The Denavit and Hartenberg notation gives a standard (distal) methodology to write the kinematic equations of a manipulator. This is especially useful for serial manipulators where a matrix is used to represent the pose (position and orientation) of one body with respect to another.

The position of body n with respect to $n-1$ may be represented by a position matrix indicated with the symbol T or M

$\operatorname {} ^{n-1}T_{n}=M_{n-1,n}$

This matrix is also used to transform a point from frame n to $n-1$

$M_{n-1,n}=\left[{\begin{array}{ccc|c}R_{xx}&R_{xy}&R_{xz}&T_{x}\\R_{yx}&R_{yy}&R_{yz}&T_{y}\\R_{zx}&R_{zy}&R_{zz}&T_{z}\\\hline 0&0&0&1\end{array}}\right]$

Where the upper left $3\times 3$ submatrix of M represents the relative orientation of the two bodies, and the upper right $3\times 1$ represents their relative position or more specifically the body position in frame *n* − 1 represented with element of frame *n*.

The position of body k with respect to body i can be obtained as the product of the matrices representing the pose of j with respect of i and that of k with respect of j

$M_{i,k}=M_{i,j}M_{j,k}$

An important property of Denavit and Hartenberg matrices is that the inverse is

$M^{-1}=\left[{\begin{array}{ccc|c}&&&\\&R^{T}&&-R^{T}T\\&&&\\\hline 0&0&0&1\end{array}}\right]$

where $R^{T}$ is both the transpose and the inverse of the orthogonal matrix R , i.e. $R_{ij}^{-1}=R_{ij}^{T}=R_{ji}$ .

## Kinematics

Further matrices can be defined to represent velocity and acceleration of bodies. The velocity of body i with respect to body j can be represented in frame k by the matrix

$W_{i,j(k)}=\left[{\begin{array}{ccc|c}0&-\omega _{z}&\omega _{y}&v_{x}\\\omega _{z}&0&-\omega _{x}&v_{y}\\-\omega _{y}&\omega _{x}&0&v_{z}\\\hline 0&0&0&0\end{array}}\right]$

where $\omega$ is the angular velocity of body j with respect to body i and all the components are expressed in frame k ; v is the velocity of one point of body j with respect to body i (the pole). The pole is the point of j passing through the origin of frame i .

The acceleration matrix can be defined as the sum of the time derivative of the velocity plus the velocity squared

$H_{i,j(k)}={\dot {W}}_{i,j(k)}+W_{i,j(k)}^{2}$

The velocity and the acceleration in frame i of a point of body j can be evaluated as

${\dot {P}}=W_{i,j}P$

${\ddot {P}}=H_{i,j}P$

It is also possible to prove that

${\dot {M}}_{i,j}=W_{i,j(i)}M_{i,j}$

${\ddot {M}}_{i,j}=H_{i,j(i)}M_{i,j}$

Velocity and acceleration matrices add up according to the following rules

$W_{i,k}=W_{i,j}+W_{j,k}$

$H_{i,k}=H_{i,j}+H_{j,k}+2W_{i,j}W_{j,k}$

in other words the absolute velocity is the sum of the parent velocity plus the relative velocity; for the acceleration the Coriolis' term is also present.

The components of velocity and acceleration matrices are expressed in an arbitrary frame k and transform from one frame to another by the following rule

$W_{(h)}=M_{h,k}W_{(k)}M_{k,h}$

$H_{(h)}=M_{h,k}H_{(k)}M_{k,h}$

## Dynamics

For the dynamics, three further matrices are necessary to describe the inertia J , the linear and angular momentum $\Gamma$ , and the forces and torques $\Phi$ applied to a body.

Inertia J :

$J=\left[{\begin{array}{ccc|c}I_{xx}&I_{xy}&I_{xz}&x_{g}m\\I_{yx}&I_{yy}&I_{yz}&y_{g}m\\I_{zx}&I_{zy}&I_{zz}&z_{g}m\\\hline x_{g}m&y_{g}m&z_{g}m&m\end{array}}\right]$

where m is the mass, $x_{g},\,y_{g},\,z_{g}$ represent the position of the center of mass, and the terms $I_{xx},\,I_{xy},\ldots$ represent inertia and are defined as

$I_{xx}=\iint x^{2}\,dm$

${\begin{aligned}I_{xy}&=\iint xy\,dm\\I_{xz}&=\cdots \\&\,\,\,\vdots \end{aligned}}$

Action matrix $\Phi$ , containing force f and torque t :

$\Phi =\left[{\begin{array}{ccc|c}0&-t_{z}&t_{y}&f_{x}\\t_{z}&0&-t_{x}&f_{y}\\-t_{y}&t_{x}&0&f_{z}\\\hline -f_{x}&-f_{y}&-f_{z}&0\end{array}}\right]$

Momentum matrix $\Gamma$ , containing linear $\rho$ and angular $\gamma$ momentum

$\Gamma =\left[{\begin{array}{ccc|c}0&-\gamma _{z}&\gamma _{y}&\rho _{x}\\\gamma _{z}&0&-\gamma _{x}&\rho _{y}\\-\gamma _{y}&\gamma _{x}&0&\rho _{z}\\\hline -\rho _{x}&-\rho _{y}&-\rho _{z}&0\end{array}}\right]$

All the matrices are represented with the vector components in a certain frame k . Transformation of the components from frame k to frame h follows the rule

${\begin{aligned}J_{(h)}&=M_{h,k}J_{(k)}M_{h,k}^{T}\\\Gamma _{(h)}&=M_{h,k}\Gamma _{(k)}M_{h,k}^{T}\\\Phi _{(h)}&=M_{h,k}\Phi _{(k)}M_{h,k}^{T}\end{aligned}}$

The matrices described allow the writing of the dynamic equations in a concise way.

Newton's law:

$\Phi =HJ-JH^{t}\,$

Momentum:

$\Gamma =WJ-JW^{t}\,$

The first of these equations express the Newton's law and is the equivalent of the vector equation $f=ma$ (force equal mass times acceleration) plus $t=J{\dot {\omega }}+\omega \times J\omega$ (angular acceleration in function of inertia and angular velocity); the second equation permits the evaluation of the linear and angular momentum when velocity and inertia are known.

## Modified DH parameters

Some books such as *Introduction to Robotics: Mechanics and Control (3rd Edition)* use modified (proximal) DH parameters. The difference between the classic (distal) DH parameters and the modified DH parameters are the locations of the coordinates system attachment to the links and the order of the performed transformations.

Compared with the classic DH parameters, the coordinates of frame $O_{i-1}$ is put on axis *i* − 1, not the axis *i* in classic DH convention. The coordinates of $O_{i}$ is put on the axis *i*, not the axis *i* + 1 in classic DH convention.

Another difference is that according to the modified convention, the transform matrix is given by the following order of operations:

${}^{n-1}T_{n}=\operatorname {Rot} _{x_{n-1}}(\alpha _{n-1})\cdot \operatorname {Trans} _{x_{n-1}}(a_{n-1})\cdot \operatorname {Rot} _{z_{n}}(\theta _{n})\cdot \operatorname {Trans} _{z_{n}}(d_{n})$

Thus, the matrix of the modified DH parameters becomes

$\operatorname {} ^{n-1}T_{n}=\left[{\begin{array}{ccc|c}\cos \theta _{n}&-\sin \theta _{n}&0&a_{n-1}\\\sin \theta _{n}\cos \alpha _{n-1}&\cos \theta _{n}\cos \alpha _{n-1}&-\sin \alpha _{n-1}&-d_{n}\sin \alpha _{n-1}\\\sin \theta _{n}\sin \alpha _{n-1}&\cos \theta _{n}\sin \alpha _{n-1}&\cos \alpha _{n-1}&d_{n}\cos \alpha _{n-1}\\\hline 0&0&0&1\end{array}}\right]$

Note that some books (e.g.:) use $a_{n}$ and $\alpha _{n}$ to indicate the length and twist of link *n* − 1 rather than link *n*. As a consequence, ${}^{n-1}T_{n}$ is formed only with parameters using the same subscript.

Surveys of DH conventions and its differences have been published.
