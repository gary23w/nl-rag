---
title: "Forward kinematics"
source: https://en.wikipedia.org/wiki/Forward_kinematics
domain: robotics
license: CC-BY-SA-4.0
tags: robotics, robot, ros, slam, kinematics, path planning, odometry
fetched: 2026-07-02
---

# Forward kinematics

In robot kinematics, **forward kinematics** refers to the use of the kinematic equations of a robot to compute the position of the end-effector from specified values for the joint parameters.

The kinematics equations of the robot are used in robotics, computer games, and animation. The reverse process, that computes the joint parameters that achieve a specified position of the end-effector, is known as inverse kinematics.

## Kinematics equations

The kinematics equations for the series chain of a robot are obtained using a rigid transformation [Z] to characterize the relative movement allowed at each joint and separate rigid transformation [X] to define the dimensions of each link. The result is a sequence of rigid transformations alternating joint and link transformations from the base of the chain to its end link, which is equated to the specified position for the end link,

$[T]=[Z_{1}][X_{1}][Z_{2}][X_{2}]\ldots [X_{n-1}][Z_{n}],\!$

where [T] is the transformation locating the end-link. These equations are called the kinematics equations of the serial chain.

## Link transformations

In 1955, Jacques Denavit and Richard Hartenberg introduced a convention for the definition of the joint matrices [Z] and link matrices [X] to standardize the coordinate frame for spatial linkages. This convention positions the joint frame so that it consists of a screw displacement along the Z-axis

$[Z_{i}]=\operatorname {Trans} _{Z_{i}}(d_{i})\operatorname {Rot} _{Z_{i}}(\theta _{i}),$

and it positions the link frame so it consists of a screw displacement along the X-axis,

$[X_{i}]=\operatorname {Trans} _{X_{i}}(a_{i,i+1})\operatorname {Rot} _{X_{i}}(\alpha _{i,i+1}).$

Using this notation, each transformation-link goes along a serial chain robot, and can be described by the coordinate transformation,

${}^{i-1}T_{i}=[Z_{i}][X_{i}]=\operatorname {Trans} _{Z_{i}}(d_{i})\operatorname {Rot} _{Z_{i}}(\theta _{i})\operatorname {Trans} _{X_{i}}(a_{i,i+1})\operatorname {Rot} _{X_{i}}(\alpha _{i,i+1}),$

where *θi*, *di*, *αi,i+1* and *ai,i+1* are known as the Denavit-Hartenberg parameters.

### Kinematics equations revisited

The kinematics equations of a serial chain of *n* links, with joint parameters *θi* are given by

$[T]={}^{0}T_{n}=\prod _{i=1}^{n}{}^{i-1}T_{i}(\theta _{i}),$

where ${}^{i-1}T_{i}(\theta _{i})$ is the transformation matrix from the frame of link i to link $i-1$ . In robotics, these are conventionally described by Denavit–Hartenberg parameters.

### Denavit-Hartenberg matrix

The matrices associated with these operations are:

$\operatorname {Trans} _{Z_{i}}(d_{i})={\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&d_{i}\\0&0&0&1\end{bmatrix}},\quad \operatorname {Rot} _{Z_{i}}(\theta _{i})={\begin{bmatrix}\cos \theta _{i}&-\sin \theta _{i}&0&0\\\sin \theta _{i}&\cos \theta _{i}&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}}.$

Similarly,

$\operatorname {Trans} _{X_{i}}(a_{i,i+1})={\begin{bmatrix}1&0&0&a_{i,i+1}\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}},\quad \operatorname {Rot} _{X_{i}}(\alpha _{i,i+1})={\begin{bmatrix}1&0&0&0\\0&\cos \alpha _{i,i+1}&-\sin \alpha _{i,i+1}&0\\0&\sin \alpha _{i,i+1}&\cos \alpha _{i,i+1}&0\\0&0&0&1\end{bmatrix}}.$

The use of the Denavit-Hartenberg convention yields the link transformation matrix, [*i-1Ti*] as

$\operatorname {} ^{i-1}T_{i}={\begin{bmatrix}\cos \theta _{i}&-\sin \theta _{i}\cos \alpha _{i,i+1}&\sin \theta _{i}\sin \alpha _{i,i+1}&a_{i,i+1}\cos \theta _{i}\\\sin \theta _{i}&\cos \theta _{i}\cos \alpha _{i,i+1}&-\cos \theta _{i}\sin \alpha _{i,i+1}&a_{i,i+1}\sin \theta _{i}\\0&\sin \alpha _{i,i+1}&\cos \alpha _{i,i+1}&d_{i}\\0&0&0&1\end{bmatrix}},$

known as the *Denavit-Hartenberg matrix.*

## Computer animation

The forward kinematic equations can be used as a method in 3D computer graphics for animating models.

The essential concept of forward kinematic animation is that the positions of particular parts of the model at a specified time are calculated from the position and orientation of the object, together with any information on the joints of an articulated model. So for example if the object to be animated is an arm with the shoulder remaining at a fixed location, the location of the tip of the thumb would be calculated from the angles of the shoulder, elbow, wrist, thumb and knuckle joints. Three of these joints (the shoulder, wrist and the base of the thumb) have more than one degree of freedom, all of which must be taken into account. If the model were an entire human figure, then the location of the shoulder would also have to be calculated from other properties of the model.

Forward kinematic animation can be distinguished from inverse kinematic animation by this means of calculation - in inverse kinematics the orientation of articulated parts is calculated from the desired position of certain points on the model. It is also distinguished from other animation systems by the fact that the motion of the model is defined directly by the animator - no account is taken of any physical laws that might be in effect on the model, such as gravity or collision with other models.
