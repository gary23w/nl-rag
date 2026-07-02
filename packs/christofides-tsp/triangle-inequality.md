---
title: "Triangle inequality"
source: https://en.wikipedia.org/wiki/Triangle_inequality
domain: christofides-tsp
license: CC-BY-SA-4.0
tags: christofides algorithm, traveling salesman approximation, metric tsp, approximation ratio
fetched: 2026-07-02
---

# Triangle inequality

In mathematics, the **triangle inequality** states that for any triangle, the sum of the lengths of any two sides must be greater than or equal to the length of the remaining side. This statement permits the inclusion of degenerate triangles, but some authors, especially those writing about elementary geometry, will exclude this possibility, thus leaving out the possibility of equality. If a, b, and c are the lengths of the sides of a triangle then the triangle inequality states that

$c\leq a+b,$

with equality only in the degenerate case of a triangle with zero area.

In Euclidean geometry and some other geometries, the triangle inequality is a theorem about vectors and vector lengths (norms):

$\|\mathbf {u} +\mathbf {v} \|\leq \|\mathbf {u} \|+\|\mathbf {v} \|,$

where the length of the third side has been replaced by the length of the vector sum **u** + **v**. When **u** and **v** are real numbers, they can be viewed as vectors in $\mathbb {R} ^{1}$ , and the triangle inequality expresses a relationship between absolute values.

In Euclidean geometry, for right triangles the triangle inequality is a consequence of the Pythagorean theorem, and for general triangles, a consequence of the law of cosines, although it may be proved without these theorems. The inequality can be viewed intuitively in either $\mathbb {R} ^{2}$ or $\mathbb {R} ^{3}$ . The figure at the right shows three examples beginning with clear inequality (top) and approaching equality (bottom). In the Euclidean case, equality occurs only if the triangle has a 180° angle and two 0° angles, making the three vertices collinear, as shown in the bottom example. Thus, in Euclidean geometry, the shortest distance between two points is a straight line.

In spherical geometry, the shortest distance between two points is an arc of a great circle, but the triangle inequality holds provided the restriction is made that the distance between two points on a sphere is the length of a minor spherical line segment (that is, one with central angle in [0, *π*]) with those endpoints.

The triangle inequality is a *defining property* of norms and measures of distance. This property must be established as a theorem for any function proposed for such purposes for each particular space: for example, spaces such as the real numbers, Euclidean spaces, the Lp spaces (*p* ≥ 1), and inner product spaces.

## Euclidean geometry

The triangle inequality theorem is stated in Euclid's Elements, Book I, Proposition 20:

*[…] in the triangle ABC the sum of any two sides is greater than the remaining one, that is, the sum of BA and AC is greater than BC, the sum of AB and BC is greater than AC, and the sum of BC and CA is greater than AB.*

Euclid proved the triangle inequality for distances in plane geometry using the construction in the figure. Beginning with triangle ABC, an isosceles triangle is constructed with one side taken as BC and the other equal leg BD along the extension of side AB. It then is argued that angle β has larger measure than angle α, so side AD is longer than side AC. However:

${\overline {AD}}={\overline {AB}}+{\overline {BD}}={\overline {AB}}+{\overline {BC}},$

so the sum of the lengths of sides AB and BC is larger than the length of AC. This proof appears in Euclid's Elements, Book I, Proposition 20.

### Mathematical expression of the constraint on the sides of a triangle

For a proper triangle, the triangle inequality, as stated in words, literally translates into three inequalities (given that a proper triangle has side lengths *a*, *b*, *c* that are all positive and excludes the degenerate case of zero area):

$a+b>c,\quad b+c>a,\quad c+a>b.$

A more succinct form of this inequality system can be shown to be

$|a-b|<c<a+b.$

Another way to state it is

$\max(a,b,c)<a+b+c-\max(a,b,c)$

implying

$2\max(a,b,c)<a+b+c$

and thus that the longest side length is less than the semiperimeter.

A mathematically equivalent formulation is that the area of a triangle with sides *a*, *b*, *c* must be a real number greater than zero. Heron's formula for the area is

${\begin{aligned}4\cdot {\text{area}}&={\sqrt {(a+b+c)(-a+b+c)(a-b+c)(a+b-c)}}\\&={\sqrt {-a^{4}-b^{4}-c^{4}+2a^{2}b^{2}+2a^{2}c^{2}+2b^{2}c^{2}}}.\end{aligned}}$

In terms of either area expression, the triangle inequality imposed on all sides is equivalent to the condition that the expression under the square root sign be real and greater than zero (so the area expression is real and greater than zero).

The triangle inequality provides two more interesting constraints for triangles whose sides are *a*, *b*, *c*, where *a* ≥ *b* ≥ *c* and $\phi$ is the golden ratio, as

$1<{\frac {a+c}{b}}<3$

$1\leq \min \left({\frac {a}{b}},{\frac {b}{c}}\right)<\phi .$

### Right triangle

In the case of right triangles, the triangle inequality specializes to the statement that the hypotenuse is greater than either of the two sides and less than their sum.

The second part of this theorem is already established above for any side of any triangle. The first part is established using the lower figure. In the figure, consider the right triangle ADC. An isosceles triangle ABC is constructed with equal sides *AB* = *AC*. From the triangle postulate, the angles in the right triangle ADC satisfy:

$\alpha +\gamma =\pi /2\ .$

Likewise, in the isosceles triangle ABC, the angles satisfy:

$2\beta +\gamma =\pi \ .$

Therefore,

$\alpha =\pi /2-\gamma ,\ \mathrm {while} \ \beta =\pi /2-\gamma /2\ ,$

and so, in particular,

$\alpha <\beta \ .$

That means side AD, which is opposite to angle α, is shorter than side AB, which is opposite to the larger angle β. But *AB* = *AC*. Hence:

${\overline {AC}}>{\overline {AD}}\ .$

A similar construction shows *AC* > *DC*, establishing the theorem.

An alternative proof (also based upon the triangle postulate) proceeds by considering three positions for point B: (i) as depicted (which is to be proved), or (ii) B coincident with D (which would mean the isosceles triangle had two right angles as base angles plus the vertex angle γ, which would violate the triangle postulate), or lastly, (iii) B interior to the right triangle between points A and D (in which case angle ABC is an exterior angle of a right triangle BDC and therefore larger than *π*/2, meaning the other base angle of the isosceles triangle also is greater than *π*/2 and their sum exceeds π in violation of the triangle postulate).

This theorem establishing inequalities is sharpened by Pythagoras' theorem to the equality that the square of the length of the hypotenuse equals the sum of the squares of the other two sides.

### Examples of use

Consider a triangle whose sides are in an arithmetic progression and let the sides be *a*, *a* + *d*, *a* + 2*d*. Then the triangle inequality requires that

${\begin{array}{rcccl}0&<&a&<&2a+3d,\\0&<&a+d&<&2a+2d,\\0&<&a+2d&<&2a+d.\end{array}}$

To satisfy all these inequalities requires

$a>0{\text{ and }}-{\frac {a}{3}}<d<a.$

When d is chosen such that *d* = *a*/3, it generates a right triangle that is always similar to the Pythagorean triple with sides 3, 4, 5.

Now consider a triangle whose sides are in a geometric progression and let the sides be *a*, *ar*, *ar*2. Then the triangle inequality requires that

${\begin{array}{rcccl}0&<&a&<&ar+ar^{2},\\0&<&ar&<&a+ar^{2},\\0&<&\!ar^{2}&<&a+ar.\end{array}}$

The first inequality requires *a* > 0; consequently it can be divided through and eliminated. With *a* > 0, the middle inequality only requires *r* > 0. This now leaves the first and third inequalities needing to satisfy

${\begin{aligned}r^{2}+r-1&{}>0\\r^{2}-r-1&{}<0.\end{aligned}}$

The first of these quadratic inequalities requires r to range in the region beyond the value of the positive root of the quadratic equation *r*2 + *r* − 1 = 0, i.e. *r* > *φ* − 1 where φ is the golden ratio. The second quadratic inequality requires r to range between 0 and the positive root of the quadratic equation *r*2 − *r* − 1 = 0, i.e. 0 < *r* < *φ*. The combined requirements result in r being confined to the range

$\varphi -1<r<\varphi \,{\text{ and }}a>0.$

When r the common ratio is chosen such that *r* = √*φ* it generates a right triangle that is always similar to the Kepler triangle.

### Generalization to any polygon

The triangle inequality can be extended by mathematical induction to arbitrary polygonal paths, showing that the total length of such a path is no less than the length of the straight line between its endpoints. Consequently, the length of any polygon side is always less than the sum of the other polygon side lengths.

#### Example of the generalized polygon inequality for a quadrilateral

Consider a quadrilateral whose sides are in a geometric progression and let the sides be *a*, *ar*, *ar*2, *ar*3. Then the generalized polygon inequality requires that

${\begin{array}{rcccl}0&<&a&<&ar+ar^{2}+ar^{3}\\0&<&ar&<&a+ar^{2}+ar^{3}\\0&<&ar^{2}&<&a+ar+ar^{3}\\0&<&ar^{3}&<&a+ar+ar^{2}.\end{array}}$

These inequalities for *a* > 0 reduce to the following

$r^{3}+r^{2}+r-1>0$

$r^{3}-r^{2}-r-1<0.$

The left-hand side polynomials of these two inequalities have roots that are the tribonacci constant and its reciprocal. Consequently, r is limited to the range 1/*t* < *r* < *t* where t is the tribonacci constant.

#### Relationship with shortest paths

This generalization can be used to prove that the shortest curve between two points in Euclidean geometry is a straight line.

No polygonal path between two points is shorter than the line between them. This implies that no curve can have an arc length less than the distance between its endpoints. By definition, the arc length of a curve is the least upper bound of the lengths of all polygonal approximations of the curve. The result for polygonal paths shows that the straight line between the endpoints is the shortest of all the polygonal approximations. Because the arc length of the curve is greater than or equal to the length of every polygonal approximation, the curve itself cannot be shorter than the straight line path.

### Converse

The converse of the triangle inequality theorem is also true: if three real numbers are such that each is less than the sum of the others, then there exists a triangle with these numbers as its side lengths and with positive area; and if one number equals the sum of the other two, there exists a degenerate triangle (that is, with zero area) with these numbers as its side lengths.

In either case, if the side lengths are a, b, c we can attempt to place a triangle in the Euclidean plane as shown in the diagram. We need to prove that there exists a real number h consistent with the values a, b, and c, in which case this triangle exists.

By the Pythagorean theorem we have *b*2 = *h*2 + *d*2 and *a*2 = *h*2 + (*c* − *d*)2 according to the figure at the right. Subtracting these yields *a*2 − *b*2 = *c*2 − 2*cd*. This equation allows us to express d in terms of the sides of the triangle:

$d={\frac {-a^{2}+b^{2}+c^{2}}{2c}}.$

For the height of the triangle we have that *h*2 = *b*2 − *d*2. By replacing d with the formula given above, we have

$h^{2}=b^{2}-\left({\frac {-a^{2}+b^{2}+c^{2}}{2c}}\right)^{2}.$

For a real number h to satisfy this, *h*2 must be non-negative:

${\begin{aligned}0&\leq b^{2}-\left({\frac {-a^{2}+b^{2}+c^{2}}{2c}}\right)^{2}\\[4pt]0&\leq \left(b-{\frac {-a^{2}+b^{2}+c^{2}}{2c}}\right)\left(b+{\frac {-a^{2}+b^{2}+c^{2}}{2c}}\right)\\[4pt]0&\leq \left(a^{2}-(b-c)^{2})((b+c)^{2}-a^{2}\right)\\[6pt]0&\leq (a+b-c)(a-b+c)(b+c+a)(b+c-a)\\[6pt]0&\leq (a+b-c)(a+c-b)(b+c-a)\end{aligned}}$

which holds if the triangle inequality is satisfied for all sides. Therefore, there does exist a real number h consistent with the sides $a,b,c$ , and the triangle exists. If each triangle inequality holds strictly, $h>0$ and the triangle is non-degenerate (has positive area); but if one of the inequalities holds with equality, so $h=0$ , the triangle is degenerate.

### Generalization to higher dimensions

The area of a triangular face of a tetrahedron is less than or equal to the sum of the areas of the other three triangular faces. More generally, in Euclidean space the hypervolume of an (*n* − 1)-facet of an n-simplex is less than or equal to the sum of the hypervolumes of the other n facets.

Much as the triangle inequality generalizes to a polygon inequality, the inequality for a simplex of any dimension generalizes to a polytope of any dimension: the hypervolume of any facet of a polytope is less than or equal to the sum of the hypervolumes of the remaining facets.

In some cases the tetrahedral inequality is stronger than several applications of the triangle inequality. For example, the triangle inequality appears to allow the possibility of four points A, B, C, and Z in Euclidean space such that distances

AB

=

BC

=

CA

= 26

and

AZ

=

BZ

=

CZ

= 14

.

However, points with such distances cannot exist: the area of the 26–26–26 equilateral triangle *ABC* is ${\textstyle 169{\sqrt {3}}}$ , which is larger than three times ${\textstyle 39{\sqrt {3}}}$ , the area of a 26–14–14 isosceles triangle (all by Heron's formula), and so the arrangement is forbidden by the tetrahedral inequality.

## Normed vector space

In a normed vector space V, one of the defining properties of the norm is the triangle inequality:

$\|\mathbf {u} +\mathbf {v} \|\leq \|\mathbf {u} \|+\|\mathbf {v} \|\quad \forall \,\mathbf {u} ,\mathbf {v} \in V$

That is, the norm of the sum of two vectors is at most as large as the sum of the norms of the two vectors. This is also referred to as subadditivity. For any proposed function to behave as a norm, it must satisfy this requirement.

If the normed space is Euclidean, or, more generally, strictly convex, then $\|\mathbf {u} +\mathbf {v} \|=\|\mathbf {u} \|+\|\mathbf {v} \|$ if and only if the triangle formed by **u**, **v**, and **u** + **v** is degenerate; that is, **u** and **v** are on the same ray, i.e., **u** = 0 or **v** = 0 or **u** = *α* **v** for some *α* > 0.

This property characterizes strictly convex normed spaces such as the ℓp spaces with 1 < *p* < ∞. However, there are normed spaces in which this is not true. For instance, consider the plane with the *ℓ*1 norm (the Manhattan distance) and denote **u** = (1, 0) and **v** = (0, 1). Then the triangle formed by **u**, **v**, and **u** + **v**, is non-degenerate but

$\|\mathbf {u} +\mathbf {v} \|=\|(1,1)\|=|1|+|1|=2=\|\mathbf {u} \|+\|\mathbf {v} \|.$

### Example norms

The *absolute value* is a norm for the real line; as required, the absolute value satisfies the triangle inequality for any real numbers u and v.

- If u and v have the same sign or either of them is zero, then $|u+v|=|u|+|v|.$
- If u and v have opposite signs, then without loss of generality assume $|u|>|v|.$ Then $|u+v|=|u|-|v|<|u|+|v|.$

Combining these cases:

$|u+v|\leq |u|+|v|.$

The triangle inequality is useful in mathematical analysis for determining the best upper estimate on the size of the sum of two numbers, in terms of the sizes of the individual numbers. There is also a lower estimate, which can be found using the *reverse triangle inequality* which states that for any real numbers u and v, $|u-v|\geq {\bigl |}|u|-|v|{\bigr |}.$

The *taxicab norm* or 1-norm is one generalization absolute value to higher dimensions. To find the norm of a vector $v=(v_{1},v_{2},\ldots v_{n}),$ just add the absolute value of each component separately, $\|v\|_{1}=|v_{1}|+|v_{2}|+\dotsb +|v_{n}|.$

The *Euclidean norm* or 2-norm defines the length of translation vectors in an n-dimensional Euclidean space in terms of a Cartesian coordinate system. For a vector $v=(v_{1},v_{2},\ldots v_{n}),$ its length is defined using the n-dimensional Pythagorean theorem: $\|v\|_{2}={\sqrt {|v_{1}|^{2}+|v_{2}|^{2}+\dotsb +|v_{n}|^{2}}}.$

The *inner product* is norm in any inner product space, a generalization of Euclidean vector spaces including infinite-dimensional examples. The triangle inequality follows from the Cauchy–Schwarz inequality as follows: Given vectors u and v, and denoting the inner product as $\langle u,v\rangle$ :

${\begin{aligned}\|u+v\|^{2}&=\langle u+v,u+v\rangle \\&=\|u\|^{2}+\langle u,v\rangle +\langle v,u\rangle +\|v\|^{2}\\&\leq \|u\|^{2}+2|\langle u,v\rangle |+\|v\|^{2}\\&\leq \|u\|^{2}+2\|u\|\|v\|+\|v\|^{2}\quad {\text{(by Cauchy–Schwarz inequality)}}\\&=\left(\|u\|+\|v\|\right)^{2}\end{aligned}}$

The Cauchy–Schwarz inequality turns into an equality if and only if u and v are linearly dependent. The inequality $\langle u,v\rangle +\langle v,u\rangle \leq 2\left|\left\langle u,v\right\rangle \right|$ turns into an equality for linearly dependent u and v if and only if one of the vectors u or v is a *nonnegative* scalar of the other. Taking the square root of the final result gives the triangle inequality.

The p-norm is a generalization of taxicab and Euclidean norms, using an arbitrary positive integer exponent, $\|v\|_{p}={\bigl (}|v_{1}|^{p}+|v_{2}|^{p}+\dotsb +|v_{n}|^{p}{\bigr )}^{1/p},$ where the vi are the components of vector v.

Except for the case *p* = 2, the p-norm is *not* an inner product norm, because it does not satisfy the parallelogram law. The triangle inequality for general values of p is called Minkowski's inequality. It takes the form: $\|u+v\|_{p}\leq \|u\|_{p}+\|v\|_{p}\ .$

## Metric space

In a metric space M with metric d, the triangle inequality is a requirement upon distance: $d(A,\ C)\leq d(A,\ B)+d(B,\ C)\ ,$

for all points A, B, and C in M. That is, the distance from A to C is at most as large as the sum of the distance from A to B and the distance from B to C.

The triangle inequality is responsible for most of the interesting structure on a metric space, namely, convergence. This is because the remaining requirements for a metric are rather simplistic in comparison. For example, the fact that any convergent sequence in a metric space is a Cauchy sequence is a direct consequence of the triangle inequality, because if we choose any xn and xm such that $d(x_{n},x)<{\frac {\varepsilon }{2}},\quad d(x_{m},x)<{\frac {\varepsilon }{2}},$ where *ε* > 0 is given and arbitrary (as in the definition of a limit in a metric space), then by the triangle inequality,

$d(x_{n},x_{m})\leq d(x_{n},x)+d(x_{m},x)<{\frac {\varepsilon }{2}}+{\frac {\varepsilon }{2}}=\varepsilon ,$

so that the sequence {*xn*} is a Cauchy sequence, by definition.

This version of the triangle inequality reduces to the one stated above in case of normed vector spaces where a metric is induced via $d(u,v):=\|u-v\|,$ with *u* − *v* being the vector pointing from point v to u.

## Reverse triangle inequality

The **reverse triangle inequality** is an equivalent alternative formulation of the triangle inequality that gives lower bounds instead of upper bounds. For plane geometry, the statement is:

Any side of a triangle is greater than or equal to the difference between the other two sides

.

In the case of a normed vector space, the statement is: ${\big |}\|u\|-\|v\|{\big |}\leq \|u-v\|,$ or, for metric spaces: $|d(A,C)-d(B,C)|\leq d(A,B).$ This implies that the norm $\|\cdot \|$ as well as the distance-from-z function *d*(*z*, ·) are Lipschitz continuous with Lipschitz constant 1, and therefore are in particular uniformly continuous.

The proof of the reverse triangle inequality from the usual one uses ${\begin{aligned}\|v-u\|&=\|{-}1(u-v)\|\\[2pt]&=|{-}1|\cdot \|u-v\|\\[2pt]&=\|u-v\|\end{aligned}}$ to find: ${\begin{aligned}\|u\|=\|(u-v)+v\|&\leq \|u-v\|+\|v\|\\[4pt]\Rightarrow \quad \|u\|-\|v\|&\leq \|u-v\|,\\[10pt]\|v\|=\|(v-u)+u\|&\leq \|v-u\|+\|u\|\\[4pt]\Rightarrow \quad \|u\|-\|v\|&\geq -\|u-v\|,\end{aligned}}$

Combining these two statements gives: ${\begin{aligned}&-\|u-v\|\leq \|u\|-\|v\|\leq \|u-v\|\\[4pt]&\Rightarrow \quad {\big |}\|u\|-\|v\|{\big |}\leq \|u-v\|.\end{aligned}}$

In the converse, the proof of the triangle inequality from the reverse triangle inequality works in two cases:

- If $\|u+v\|-\|u\|\geq 0,$ then by the reverse triangle inequality, ${\begin{aligned}&\|u+v\|-\|u\|={\big |}\|u+v\|-\|u\|{\big |}\leq \|(u+v)-u\|=\|v\|\\[4pt]&\Rightarrow \quad \|u+v\|\leq \|u\|+\|v\|\end{aligned}}$
- And if $\|u+v\|-\|u\|<0,$ then trivially $\|u\|+\|v\|\geq \|u\|>\|u+v\|$ by the nonnegativity of the norm.

Thus, in both cases, we find that $\|u\|+\|v\|\geq \|u+v\|.$

For metric spaces, the proof of the reverse triangle inequality is found similarly by: ${\begin{aligned}d(A,B)+d(B,C)&\geq d(A,C)\\[4pt]\Rightarrow \quad d(A,B)&\geq d(A,C)-d(B,C)\\[10pt]d(C,A)+d(A,B)&\geq d(C,B)\\[4pt]\Rightarrow \quad d(A,B)&\geq d(B,C)-d(A,C)\end{aligned}}$ Putting these equations together we find: $d(A,B)\geq |d(A,C)-d(B,C)|$

And in the converse, beginning from the reverse triangle inequality, we can again use two cases:

- If $d(A,C)-d(B,C)\geq 0$ , then ${\begin{aligned}&d(A,B)\geq |d(A,C)-d(B,C)|=d(A,C)-d(B,C)\\[4pt]&\Rightarrow \quad d(A,B)+d(B,C)\geq d(A,C)\end{aligned}}$
- And if $d(A,C)-d(B,C)<0,$ then $d(A,B)+d(B,C)\geq d(B,C)>d(A,C)$ again by the nonnegativity of the metric.

Thus, in both cases, we find that $d(A,B)+d(B,C)\geq d(A,C).$

## Triangle inequality for cosine similarity

By applying the cosine function to the triangle inequality and reverse triangle inequality for arc lengths and employing the angle addition and subtraction formulas for cosines, it follows immediately that

$\operatorname {sim} (u,w)\geq \operatorname {sim} (u,v)\cdot \operatorname {sim} (v,w)-{\sqrt {\left(1-\operatorname {sim} (u,v)^{2}\right)\cdot \left(1-\operatorname {sim} (v,w)^{2}\right)}}$

and

$\operatorname {sim} (u,w)\leq \operatorname {sim} (u,v)\cdot \operatorname {sim} (v,w)+{\sqrt {\left(1-\operatorname {sim} (u,v)^{2}\right)\cdot \left(1-\operatorname {sim} (v,w)^{2}\right)}}\,.$

With these formulas, one needs to compute a square root for each triple of vectors {*u*, *v*, *w*} that is examined rather than arccos(sim(*u*,*v*)) for each pair of vectors {*u*, *v*} examined, and could be a performance improvement when the number of triples examined is less than the number of pairs examined.

## Reversal in Minkowski space

The Minkowski space metric $\eta _{\mu \nu }$ is not positive-definite, which means that $\|u\|^{2}=\eta _{\mu \nu }u^{\mu }u^{\nu }$ can have either sign or vanish, even if the vector u is non-zero. Moreover, if u and v are both timelike vectors lying in the future light cone, the triangle inequality is reversed:

$\|u+v\|\geq \|u\|+\|v\|.$

A physical example of this inequality is the twin paradox in special relativity. The same reversed form of the inequality holds if both vectors lie in the past light cone, and if one or both are null vectors. The result holds in $n+1$ dimensions for any $n\geq 1$ . If the plane defined by u and v is space-like (and therefore a Euclidean subspace) then the usual triangle inequality holds.
