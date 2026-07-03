---
title: "Admittance parameters"
source: https://en.wikipedia.org/wiki/Admittance_parameters
domain: electrical-network
license: CC-BY-SA-4.0
tags: electrical network
fetched: 2026-07-03
---

# Admittance parameters

**Admittance parameters** or **Y-parameters** (the elements of an **admittance matrix** or **Y-matrix**) are properties used in many areas of electrical engineering, such as power, electronics, and telecommunications. These parameters are used to describe the electrical behavior of linear electrical networks. They are also used to describe the small-signal (linearized) response of non-linear networks. Y parameters are also known as short circuited admittance parameters. They are members of a family of similar parameters used in electronic engineering, other examples being: S-parameters, Z-parameters, H-parameters, T-parameters or ABCD-parameters.

## The Y-parameter matrix

A Y-parameter matrix describes the behaviour of any linear electrical network that can be regarded as a black box with a number of ports. A *port* in this context is a pair of electrical terminals carrying equal and opposite currents into and out of the network, and having a particular voltage between them. The Y-matrix gives no information about the behaviour of the network when the currents at any port are not balanced in this way (should this be possible), nor does it give any information about the voltage between terminals not belonging to the same port. Typically, it is intended that each external connection to the network is between the terminals of just one port, so that these limitations are appropriate.

For a generic multi-port network definition, it is assumed that each of the ports is allocated an integer n ranging from 1 to N, where N is the total number of ports. For port n, the associated Y-parameter definition is in terms of the port voltage and port current, Vn and In respectively.

For all ports the currents may be defined in terms of the Y-parameter matrix and the voltages by the following matrix equation:

$I=YV\,$

where Y is an *N* × *N* matrix the elements of which can be indexed using conventional matrix notation. In general the elements of the Y-parameter matrix are complex numbers and functions of frequency. For a one-port network, the Y-matrix reduces to a single element, being the ordinary admittance measured between the two terminals.

## Two-port networks

The Y-parameter matrix for the two-port network is probably the most common. In this case the relationship between the port voltages, port currents and the Y-parameter matrix is given by:

${\begin{pmatrix}I_{1}\\I_{2}\end{pmatrix}}={\begin{pmatrix}Y_{11}&Y_{12}\\Y_{21}&Y_{22}\end{pmatrix}}{\begin{pmatrix}V_{1}\\V_{2}\end{pmatrix}}$

.

where

${\begin{aligned}Y_{11}&={I_{1} \over V_{1}}{\bigg |}_{V_{2}=0}\qquad Y_{12}={I_{1} \over V_{2}}{\bigg |}_{V_{1}=0}\\[8pt]Y_{21}&={I_{2} \over V_{1}}{\bigg |}_{V_{2}=0}\qquad Y_{22}={I_{2} \over V_{2}}{\bigg |}_{V_{1}=0}\end{aligned}}$

For the general case of an n-port network,

$Y_{nm}={I_{n} \over V_{m}}{\bigg |}_{V_{k}=0{\text{ for }}k\neq m}$

### Admittance relations

The input admittance of a two-port network is given by:

$Y_{in}=Y_{11}-{\frac {Y_{12}Y_{21}}{Y_{22}+Y_{L}}}$

where YL is the admittance of the load connected to port two.

Similarly, the output admittance is given by:

$Y_{out}=Y_{22}-{\frac {Y_{12}Y_{21}}{Y_{11}+Y_{S}}}$

where YS is the admittance of the source connected to port one.

## Relation to S-parameters

The Y-parameters of a network are related to its S-parameters by

${\begin{aligned}Y&={\sqrt {y}}(I_{N}-S)(I_{N}+S)^{-1}{\sqrt {y}}\\&={\sqrt {y}}(I_{N}+S)^{-1}(I_{N}-S){\sqrt {y}}\\\end{aligned}}$

and

${\begin{aligned}S&=(I_{N}-{\sqrt {z}}Y{\sqrt {z}})(I_{N}+{\sqrt {z}}Y{\sqrt {z}})^{-1}\\&=(I_{N}+{\sqrt {z}}Y{\sqrt {z}})^{-1}(I_{N}-{\sqrt {z}}Y{\sqrt {z}})\\\end{aligned}}$

where IN is the identity matrix, ${\sqrt {y}}$ is a diagonal matrix having the square root of the characteristic admittance (the reciprocal of the characteristic impedance) at each port as its non-zero elements,

${\sqrt {y}}={\begin{pmatrix}{\sqrt {y_{01}}}&\\&{\sqrt {y_{02}}}\\&&\ddots \\&&&{\sqrt {y_{0N}}}\end{pmatrix}}$

and ${\sqrt {z}}=({\sqrt {y}})^{-1}$ is the corresponding diagonal matrix of square roots of characteristic impedances. In these expressions the matrices represented by the bracketed factors commute and so, as shown above, may be written in either order.

### Two port

In the special case of a two-port network, with the same and real characteristic admittance $y_{01}=y_{02}=Y_{0}$ at each port, the above expressions reduce to

${\begin{aligned}Y_{11}&={(1-S_{11})(1+S_{22})+S_{12}S_{21} \over \Delta _{S}}Y_{0}\\Y_{12}&={-2S_{12} \over \Delta _{S}}Y_{0}\\[4pt]Y_{21}&={-2S_{21} \over \Delta _{S}}Y_{0}\\[4pt]Y_{22}&={(1+S_{11})(1-S_{22})+S_{12}S_{21} \over \Delta _{S}}Y_{0}\end{aligned}}$

where

$\Delta _{S}=(1+S_{11})(1+S_{22})-S_{12}S_{21}.$

The above expressions will generally use complex numbers for $S_{ij}$ and $Y_{ij}$ . Note that the value of $\Delta$ can become 0 for specific values of $S_{ij}$ so the division by $\Delta$ in the calculations of $Y_{ij}$ may lead to a division by 0.

The two-port S-parameters may also be obtained from the equivalent two-port Y-parameters by means of the following expressions.

${\begin{aligned}S_{11}&={(1-Z_{0}Y_{11})(1+Z_{0}Y_{22})+Z_{0}^{2}Y_{12}Y_{21} \over \Delta }\\S_{12}&={-2Z_{0}Y_{12} \over \Delta }\\[4pt]S_{21}&={-2Z_{0}Y_{21} \over \Delta }\\[4pt]S_{22}&={(1+Z_{0}Y_{11})(1-Z_{0}Y_{22})+Z_{0}^{2}Y_{12}Y_{21} \over \Delta }\end{aligned}}$

where

$\Delta =(1+Z_{0}Y_{11})(1+Z_{0}Y_{22})-Z_{0}^{2}Y_{12}Y_{21}\,$

and $Z_{0}$ is the characteristic impedance at each port (assumed the same for the two ports).

## Relation to Z-parameters

Conversion from Z-parameters to Y-parameters is much simpler, as the Y-parameter matrix is just the inverse of the Z-parameter matrix. The following expressions show the applicable relations:

${\begin{aligned}Y_{11}&={Z_{22} \over |Z|}\\[4pt]Y_{12}&={-Z_{12} \over |Z|}\\[4pt]Y_{21}&={-Z_{21} \over |Z|}\\[4pt]Y_{22}&={Z_{11} \over |Z|}\end{aligned}}$

where

$|Z|=Z_{11}Z_{22}-Z_{12}Z_{21}\,$

In this case $|Z|$ is the determinant of the Z-parameter matrix.

Vice versa the Y-parameters can be used to determine the Z-parameters, essentially using the same expressions since

$Y=Z^{-1}\,$

and

$Z=Y^{-1}.$
