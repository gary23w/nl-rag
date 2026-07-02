---
title: "Perlin noise"
source: https://en.wikipedia.org/wiki/Perlin_noise
domain: cloud-rendering-volumetric
license: CC-BY-SA-4.0
tags: volumetric cloud rendering, cloud raymarching, atmospheric scattering cloud, volumetric lighting cloud
fetched: 2026-07-02
---

# Perlin noise

**Perlin noise** is a type of gradient noise developed by Ken Perlin in 1982. It has many uses, including but not limited to: procedurally generating terrain, applying pseudo-random changes to a variable, and assisting in the creation of image textures. It is most commonly implemented in two, three, or four dimensions, but can be defined for any number of dimensions.

## History

Ken Perlin developed Perlin noise in 1982 as a result of his problems with the "machine-like" look of computer-generated imagery (CGI) at the time. He formally described his findings in a SIGGRAPH paper in 1985 called "An Image Synthesizer". He developed it after working on Disney's computer animated sci-fi motion picture *Tron* (1982) for the animation company Mathematical Applications Group (MAGI). In 1997, Perlin was awarded an Academy Award for Technical Achievement for creating the algorithm, the citation for which read:

> To Ken Perlin for the development of Perlin Noise, a technique used to produce natural appearing textures on computer generated surfaces for motion picture visual effects. The development of Perlin Noise has allowed computer graphics artists to better represent the complexity of natural phenomena in visual effects for the motion picture industry.

Perlin did not apply for any patents on the algorithm, but in 2001 he was granted a patent for the use of 3D+ implementations of simplex noise for texture synthesis. Simplex noise has the same purpose of Perlin noise, but uses a simpler space-filling grid and produces less grid-shaped artifacts.

## Uses

Perlin noise is a procedural texture primitive, a type of gradient noise used by visual effects artists to increase the appearance of realism in computer graphics. The function has a pseudo-random appearance that causes all details created to stay the same size. This property allows it to be controllable; multiple scaled copies of Perlin noise can be inserted into mathematical expressions to create various procedural textures. Synthetic textures using Perlin noise are often used in CGI to make computer-generated visual elements appear more natural, by imitating the controlled random appearance of textures in nature.

It is also frequently used to generate textures when memory is limited, such as in demos. Its successors, such as fractal noise and simplex noise, have became popular in graphics processing units both for real-time graphics and for non-real-time procedural textures in computer graphics. It is also frequently used in video games to make procedurally generated terrain that looks natural.

## Algorithm detail

Perlin noise is most commonly implemented as a two-, three- or four-dimensional function, but can be defined for any number of dimensions. An implementation typically involves three steps: defining a grid of random gradient vectors, computing the dot product between the gradient vectors and their offsets, and interpolation between these values.

Define an n-dimensional grid where each grid intersection has associated with it a fixed random n-dimensional unit-length gradient vector, except in the one dimensional case where the gradients are random scalars between −1 and 1.

To work out the value of any candidate point, the unique grid cell in which the point lies is found. The 2*n* corners of that cell and their associated gradient vectors is identified. For each corner, an offset vector (a displacement vector from that corner to the candidate point) is calculated, and the dot product between its gradient vector and the offset vector is computed. This dot product will be zero if the candidate point is exactly at the grid corner.

For a point in a two-dimensional grid, this requires the computation of four offset vectors and dot products, while in three dimensions it requires eight offset vectors and eight dot products. In general, the algorithm has *O*(2*n*) complexity in n dimensions.

The final step is interpolation between the 2*n* dot products. Interpolation is performed using a function that has zero first derivative (and possibly also second derivative) at the 2*n* grid nodes. Therefore, at points close to the grid nodes, the output will approximate the dot product of the gradient vector of the node and the offset vector to the node. This means that the noise function will pass through 0 at every node, giving Perlin noise its characteristic look.

If *n* = 1, an example of a function that interpolates between value *a*0 at grid node 0 and value *a*1 at grid node 1 is

$f(x)=a_{0}+\operatorname {smoothstep} (x)\cdot (a_{1}-a_{0})\quad {\text{for }}0\leq x\leq 1$

where the smoothstep function was used.

Noise functions for use in computer graphics typically produce values in the range [–1.0, 1.0] and can be scaled accordingly.

## Gradient permutation

In Ken Perlin's original implementation he used a simple hashing scheme to determine what gradient vector is associated with each grid intersection. A pre-computed permutation table is used to turn a given grid coordinate into a random number. The original implementation worked on a 256-node grid and so included the following permutation table:

```mw
int permutation[] = { 151, 160, 137,  91,  90,  15, 131,  13, 201,  95,  96,  53, 194, 233,   7, 225,
                      140,  36, 103,  30,  69, 142,   8,  99,  37, 240,  21,  10,  23, 190,   6, 148,
                      247, 120, 234,  75,   0,  26, 197,  62,  94, 252, 219, 203, 117,  35,  11,  32,
                       57, 177,  33,  88, 237, 149,  56,  87, 174,  20, 125, 136, 171, 168,  68, 175,
                       74, 165,  71, 134, 139,  48,  27, 166,  77, 146, 158, 231,  83, 111, 229, 122,
                       60, 211, 133, 230, 220, 105,  92,  41,  55,  46, 245,  40, 244, 102, 143,  54,
                       65,  25,  63, 161,   1, 216,  80,  73, 209,  76, 132, 187, 208,  89,  18, 169,
                      200, 196, 135, 130, 116, 188, 159,  86, 164, 100, 109, 198, 173, 186,   3,  64,
                       52, 217, 226, 250, 124, 123,   5, 202,  38, 147, 118, 126, 255,  82,  85, 212,
                      207, 206,  59, 227,  47,  16,  58,  17, 182, 189,  28,  42, 223, 183, 170, 213,
                      119, 248, 152,   2,  44, 154, 163,  70, 221, 153, 101, 155, 167,  43, 172,   9,
                      129,  22,  39, 253,  19,  98, 108, 110,  79, 113, 224, 232, 178, 185, 112, 104,
                      218, 246,  97, 228, 251,  34, 242, 193, 238, 210, 144,  12, 191, 179, 162, 241,
                       81,  51, 145, 235, 249,  14, 239, 107,  49, 192, 214,  31, 181, 199, 106, 157,
                      184,  84, 204, 176, 115, 121,  50,  45, 127,   4, 150, 254, 138, 236, 205,  93,
                      222, 114,  67,  29,  24,  72, 243, 141, 128, 195,  78,  66, 215,  61, 156, 180 };
```

This specific permutation is not absolutely required, though it does require a randomized array of the integers 0 to 255. If creating a new permutation table, care should be taken to ensure uniform distribution of the values.

To get a gradient vector using the permutation table the coordinates of a grid point are looked up sequentially in the permutation table adding the value of each coordinate to the permutation of the previous coordinate. So for example the original implementation did this in 3D as follows:

```mw
// Values above 255 were handled by repeating the permutation table twice.
static final int p[] = new int[512];
static { for (int i=0; i < 256 ; i++) p[256+i] = p[i] = permutation[i]; }

int hash = p[p[p[X] + Y] + Z];
```

The algorithm then looks at the bottom 4 bits of the hash output to pick 1 of 12 gradient vectors for that grid point.

## Complexity

For each evaluation of the noise function, the dot product of the position and gradient vectors must be evaluated at each node of the containing grid cell. Perlin noise therefore scales with complexity *O*(2*n*) for n dimensions. Alternatives to Perlin noise producing similar results with improved complexity scaling include simplex noise and OpenSimplex noise.
