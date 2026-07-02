---
title: "Koch snowflake"
source: https://en.wikipedia.org/wiki/Koch_snowflake
domain: fractals
license: CC-BY-SA-4.0
tags: fractal geometry, mandelbrot set, julia set, fractal dimension
fetched: 2026-07-02
---

# Koch snowflake

Koch antisnowflake

First four iterations

Sixth iteration

The **Koch** **snowflake** (also known as the **Koch curve**, **Koch star**, or **Koch island** is a fractal curve and one of the earliest fractals to have been described. It is based on the Koch curve, which appeared in a 1904 paper titled "On a Continuous Curve Without Tangents, Constructible from Elementary Geometry" by the Swedish mathematician Helge von Koch.

The Koch snowflake can be built up iteratively, in a sequence of stages. The first stage is an equilateral triangle, and each successive stage is formed by adding outward bends to each side of the previous stage, making smaller equilateral triangles. The areas enclosed by the successive stages in the construction of the snowflake converge to ${\tfrac {8}{5}}$ times the area of the original triangle, while the perimeters of the successive stages increase without bound. Consequently, the snowflake encloses a finite area, but has an infinite perimeter.

The Koch snowflake has been constructed as an example of a continuous curve where drawing a tangent line to any point is impossible. Unlike the earlier Weierstrass function where the proof was purely analytical, the Koch snowflake was created to be possible to geometrically represent at the time, so that this property could also be seen through "naive intuition".

## Origin and history

In his 1904 article, von Koch applies this recursive construction to a line segment, obtaining the curve that forms ${\tfrac {1}{3}}$ of the boundary of the Koch snowflake. However, the complete snowflake does not appear in the original article published in 1904, nor in the extended 1906 memoir. The Koch snowflake as a closed curve may instead be due to the American mathematician Edward Kasner.

## Construction

The Koch snowflake can be constructed by starting with an equilateral triangle, then recursively altering each line segment as follows:

1. divide the line segment into three segments of equal length.
2. draw an equilateral triangle that has the middle segment from step 1 as its base and points outward.
3. remove the line segment that is the base of the triangle from step 2.

The first iteration of this process produces the outline of a hexagram.

The Koch snowflake is the limit approached as the above steps are followed indefinitely. The Koch curve originally described by Helge von Koch is constructed using only one of the three sides of the original triangle. In other words, three Koch curves make a Koch snowflake.

A Koch curve–based representation of a nominally flat surface can similarly be created by repeatedly segmenting each line in a sawtooth pattern of segments with a given angle.

## Properties

### Perimeter of the Koch snowflake

The arc length of the Koch snowflake is infinite. To show this, we note that each iteration of the construction is a polygonal approximation of the curve. Thus, it suffices to show that the perimeters of the iterates is unbounded.

The perimeter of the snowflake after n iterations, in terms of the side length s of the original triangle, is

$3s\cdot {\left({\frac {4}{3}}\right)}^{n}\,,$

which diverges to infinity.

### Area of the Koch snowflake

The total area of the snowflake after n iterations is, in terms of the original area A of the original triangle, is the geometric series

$A\left(1+{\frac {3}{4}}\sum _{k=1}^{n}\left({\frac {4}{9}}\right)^{k}\right)=A\,{\frac {1}{5}}\left(8-3\left({\frac {4}{9}}\right)^{n}\right)\,.$

Taking the limit as n approaches infinity, the area of the Koch snowflake is ${\tfrac {8}{5}}$ of the area of the original triangle. Expressed in terms of the side length s of the original triangle, this is: ${\frac {2s^{2}{\sqrt {3}}}{5}}.$

#### Solid of revolution

The volume of the solid of revolution of the Koch snowflake about an axis of symmetry of the initiating equilateral triangle of unit side is ${\frac {11{\sqrt {3}}}{135}}\pi .$

### Other properties

The Koch snowflake is self-replicating with six smaller copies surrounding one larger copy at the center. Hence, it is an irrep-7 irrep-tile (see Rep-tile for discussion).

The Hausdorff dimension of the Koch curve is $d={\tfrac {\ln 4}{\ln 3}}\approx 1.26186$ . This is greater than that of a line ( $=1$ ) but less than that of Peano's space-filling curve ( $=2$ ).

The Hausdorff measure of the Koch curve S satisfies $0.032<{\mathcal {H}}^{d}(S)<0.6$ , but its exact value is unknown. It is conjectured that $0.528<{\mathcal {H}}^{d}(S)<0.590$ .

It is impossible to draw a tangent line to any point of the curve.

## Representation as a de Rham curve

The Koch curve arises as a special case of a de Rham curve. The de Rham curves are mappings of Cantor space into the plane, usually arranged so as to form a continuous curve. Every point on a continuous de Rham curve corresponds to a real number in the unit interval. For the Koch curve, the tips of the snowflake correspond to the dyadic rationals: each tip can be uniquely labeled with a distinct dyadic rational.

## Tessellation of the plane

It is possible to tessellate the plane by copies of Koch snowflakes in two different sizes. However, such a tessellation is not possible using only snowflakes of one size. Since each Koch snowflake in the tessellation can be subdivided into seven smaller snowflakes of two different sizes, it is also possible to find tessellations that use more than two sizes at once. Koch snowflakes and Koch antisnowflakes of the same size may be used to tile the plane.

## Thue–Morse sequence and turtle graphics

A turtle graphic is the curve that is generated if an automaton is programmed with a sequence. If the Thue–Morse sequence members are used in order to select program states:

- If $t(n)=0$ , move ahead by one unit,
- If $t(n)=1$ , rotate counterclockwise by an angle of ${\tfrac {\pi }{3}}$ radians or 60 degrees,

the resulting curve converges to the Koch snowflake.

## Representation as Lindenmayer system

The Koch curve can be expressed by the following rewrite system (Lindenmayer system):

Alphabet

: F

Constants

: +, −

Axiom

: F

Production rules

: F → F+F--F+F

Here, *F* means "draw forward", *-* means "turn right 60°", and *+* means "turn left 60°".

To create the Koch snowflake, one would use F--F--F (an equilateral triangle) as the axiom.

## Variants of the Koch curve

Following von Koch's concept, several variants of the Koch curve were designed, considering right angles (quadratic), other angles (Cesàro), circles and polyhedra and their extensions to higher dimensions (Sphereflake and Kochcube, respectively)

| Variant (dimension, angle) | Illustration | Construction |
|---|---|---|
| ≤1D, 60-90° angle | Cesàro fractal (85°) | The Cesàro fractal is a variant of the Koch curve with an angle between 60° and 90°. First four iterations of a Cesàro antisnowflake (four 60° curves arranged in a 90° square) |
| ≈1.46D, 90° angle | Quadratic type 1 curve | First two iterations |
| 1.5D, 90° angle | Quadratic type 2 curve | Minkowski Sausage First two iterations. Its fractal dimension equals ${\tfrac {3}{2}}$ and is exactly half-way between dimension 1 and 2. It is therefore often chosen when studying the physical properties of non-integer fractal objects. |
| ≤2D, 90° angle | Third iteration | Minkowski Island Four quadratic type 2 curves arranged in a square |
| ≈1.37D, 90° angle | Quadratic flake | 4 quadratic type 1 curves arranged in a polygon: First two iterations. Known as the "Minkowski Sausage", its fractal dimension equals ${\tfrac {\ln 3}{\ln {\sqrt {5}}}}=1.36521$ . |
| ≤2D, 90° angle | Quadratic antiflake | Anti**cross-stitch curve**, the quadratic flake type 1, with the curves facing inwards instead of outwards (Vicsek fractal) |
| ≈1.49D, 90° angle | Quadratic Cross | Another variation. Its fractal dimension equals ${\frac {\ln 3.33}{\ln {\sqrt {5}}}}=1.49$ . |
| ≤2D, 90° angle | Quadratic island | Quadratic curve, iterations 0, 1, and 2; dimension of ${\tfrac {\ln 18}{\ln 6}}\approx 1.61$ |
| ≤2D, 60° angle | von Koch surface | First three iterations of a natural extension of the Koch curve in two dimensions. |
| ≤2D, 90° angle | First (blue block), second (plus green blocks), third (plus yellow blocks) and fourth (plus transparent blocks) iterations of the type 1 3D Koch quadratic fractal | Extension of the quadratic type 1 curve. The illustration at left shows the fractal after the second iteration Animation quadratic surface |
| ≤3D, any | Koch curve in 3D | A three-dimensional fractal constructed from Koch curves. The shape can be considered a three-dimensional extension of the curve in the same sense that the Sierpiński pyramid and Menger sponge can be considered extensions of the Sierpinski triangle and Sierpinski carpet. The version of the curve used for this shape uses 85° angles. |

Squares can be used to generate similar fractal curves. Starting with a unit square and adding to each side at each iteration a square with dimension one third of the squares in the previous iteration, it can be shown that both the length of the perimeter and the total area are determined by geometric progressions. The progression for the area converges to 2 while the progression for the perimeter diverges to infinity, so as in the case of the Koch snowflake, we have a finite area bounded by an infinite fractal curve. The resulting area fills a square with the same center as the original, but twice the area, and rotated by ${\tfrac {\pi }{4}}$ radians, the perimeter touching but never overlapping itself.

The total area covered at the n th iteration is: $A_{n}={\frac {1}{5}}+{\frac {4}{5}}\sum _{k=0}^{n}\left({\frac {5}{9}}\right)^{k}\quad {\mbox{giving}}\quad \lim _{n\rightarrow \infty }A_{n}=2\,,$

while the total length of the perimeter is: $P_{n}=4\left({\frac {5}{3}}\right)^{n}a\,,$ which approaches infinity as n increases.

### Functionalisation

In addition to the curve, the paper by Helge von Koch that has established the Koch curve shows a variation of the curve as an example of a continuous everywhere yet nowhere differentiable function that was possible to represent geometrically at the time. From the base straight line, represented as AB, the graph can be drawn by recursively applying the following on each line segment:

- Divide the line segment (*XY*) into three parts of equal length, divided by dots *C* and *E*.
- Draw a line *DM*, where *M* is the middle point of *CE*, and *DM* is perpendicular to the initial base of *AB*, having the length of ${\frac {CE{\sqrt {3}}}{2}}$ .
- Draw the lines *CD* and *DE* and erase the lines *CE* and *DM*.

Each point of *AB* can be shown to converge to a single height. If $y=\phi (x)$ is defined as the distance of that point to the initial base, then $\phi (x)$ as a function is continuous everywhere and differentiable nowhere.

## Applications

Because the Koch snowflake has a finite area but an infinitely long boundary, it serves as a model for designs that require maximized perimeter or surface length within limited space. In antenna engineering, incorporating a Koch-type fractal design increases the perimeter of the material that transmits or receives electromagnetic radiation, allowing the construction of compact antennas suited to confined or complex circuit layouts. In acoustic engineering, a Koch snowflake-inspired acoustic metasurface has been tested for broadband sound diffusion in automotive cabins. The Koch snowflake geometry has also been applied to enhance heat transfer performance in double-pipe heat exchangers.
