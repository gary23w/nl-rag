---
title: "Box–Behnken design"
source: https://en.wikipedia.org/wiki/Box–Behnken_design
domain: response-surface-methodology
license: CC-BY-SA-4.0
tags: response surface methodology, central composite design, Box Behnken, optimal design
fetched: 2026-07-02
---

# Box–Behnken design

In statistics, **Box–Behnken designs** are experimental designs for response surface methodology, devised by George E. P. Box and Donald Behnken in 1960, to achieve the following goals:

- Each factor, or independent variable, is placed at one of three equally spaced values, usually coded as −1, 0, +1. (At least three levels are needed for the following goal.)
- The design should be sufficient to fit a quadratic model, that is, one containing squared terms, products of two factors, linear terms and an intercept.
- The ratio of the number of experimental points to the number of coefficients in the quadratic model should be reasonable (in fact, their designs kept in the range of 1.5 to 2.6).
- The estimation variance should more or less depend only on the distance from the centre (this is achieved exactly for the designs with 4 and 7 factors), and should not vary too much inside the smallest (hyper)cube containing the experimental points. (See "rotatability" in "Comparisons of response surface designs".)

Box-Behnken design is still considered to be more proficient and more powerful than other designs such as the three-level full factorial design, central composite design (CCD) and Doehlert design, despite its poor coverage of the corner of nonlinear design space.

The design with 7 factors was found first while looking for a design having the desired property concerning estimation variance, and then similar designs were found for other numbers of factors.

Each design can be thought of as a combination of a two-level (full or fractional) factorial design with an incomplete block design. In each block, a certain number of factors are put through all combinations for the factorial design, while the other factors are kept at the central values. For instance, the Box–Behnken design for 3 factors involves three blocks, in each of which 2 factors are varied through the 4 possible combinations of high and low. It is necessary to include centre points as well (in which all factors are at their central values).

In this table, *m* represents the number of factors which are varied in each of the blocks.

| factors | m | no. of blocks | factorial pts. per block | total with 1 centre point | typical total with extra centre points | no. of coefficients in quadratic model |
|---|---|---|---|---|---|---|
| 3 | 2 | 3 | 4 | 13 | 15, 17 | 10 |
| 4 | 2 | 6 | 4 | 25 | 27, 29 | 15 |
| 5 | 2 | 10 | 4 | 41 | 46 | 21 |
| 6 | 3 | 6 | 8 | 49 | 54 | 28 |
| 7 | 3 | 7 | 8 | 57 | 62 | 36 |
| 8 | 4 | 14 | 8 | 113 | 120 | 45 |
| 9 | 3 | 12 | 8 | 97 | 105 | 55 |
| 10 | 4 | 10 | 16 | 161 | 170 | 66 |
| 11 | 5 | 11 | 16 | 177 | 188 | 78 |
| 12 | 4 | 12 | 16 | 193 | 204 | 91 |
| 16 | 4 | 24 | 16 | 385 | 396 | 153 |

The design for 8 factors was not in the original paper. Taking the 9 factor design, deleting one column and any resulting duplicate rows produces an 81 run design for 8 factors, while giving up some "rotatability" (see above). Designs for other numbers of factors have also been invented (at least up to 21). A design for 16 factors exists having only 256 factorial points. Using Plackett–Burmans to construct a 16 factor design (see below) requires only 221 points.

Most of these designs can be split into groups (blocks), for each of which the model will have a different constant term, in such a way that the block constants will be uncorrelated with the other coefficients.

## Extended uses

These designs can be augmented with positive and negative "axial points", as in central composite designs, but, in this case, to estimate univariate cubic and quartic effects, with length α = min(2, (int(1.5 + *K*/4))1/2), for *K* factors, roughly to approximate original design points' distances from the centre.

Plackett–Burman designs can be used, replacing the fractional factorial and incomplete block designs, to construct smaller or larger Box–Behnkens, in which case, axial points of length *α* = ((*K* + 1)/2)1/2 better approximate original design points' distances from the centre. Since each column of the basic design has 50% 0s and 25% each +1s and −1s, multiplying each column, *j*, by *σ*(*X**j*)·21/2 and adding *μ*(*X**j*) prior to experimentation, under a general linear model hypothesis, produces a "sample" of output Y with correct first and second moments of *Y*.
