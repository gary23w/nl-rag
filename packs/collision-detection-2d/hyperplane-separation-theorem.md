---
title: "Hyperplane separation theorem"
source: https://en.wikipedia.org/wiki/Hyperplane_separation_theorem
domain: collision-detection-2d
license: CC-BY-SA-4.0
tags: collision detection, collision response, bounding volume, separating axis theorem
fetched: 2026-07-02
---

# Hyperplane separation theorem

In geometry, the **hyperplane separation theorem** is a theorem about disjoint convex sets in *n*-dimensional Euclidean space. There are several rather similar versions. In one version of the theorem, if both these sets are closed and at least one of them is compact, then there is a hyperplane in between them and even two parallel hyperplanes in between them separated by a gap. In another version, if both disjoint convex sets are open, then there is a hyperplane in between them, but not necessarily any gap. An axis which is orthogonal to a separating hyperplane is a **separating axis**, because the orthogonal projections of the convex bodies onto the axis are disjoint.

The hyperplane separation theorem is due to Hermann Minkowski. The Hahn–Banach separation theorem generalizes the result to topological vector spaces.

A related result is the supporting hyperplane theorem.

In the context of support-vector machines, the *optimally separating hyperplane* or *maximum-margin hyperplane* is a hyperplane which separates two sets of points and maximizes its distance to both sets.

## Statements and proof

**Hyperplane separation theorem**—Let A and B be two disjoint nonempty convex subsets of $\mathbb {R} ^{n}$ . Then there exist a nonzero vector v and a real number c such that

$\langle x,v\rangle \geq c\,{\text{ and }}\langle y,v\rangle \leq c$

for all x in A and y in B ; i.e., the hyperplane $\langle \cdot ,v\rangle =c$ , v the normal vector, separates A and B .

If both sets are closed, and at least one of them is compact, then the separation can be strict, that is, $\langle x,v\rangle >c_{1}\,{\text{ and }}\langle y,v\rangle <c_{2}$ for some $c_{1}>c_{2}$

In all cases, assume $A,B$ to be disjoint, nonempty, and convex subsets of $\mathbb {R} ^{n}$ . The summary of the results are as follows:

| A | B | $\langle x,v\rangle$ | $\langle y,v\rangle$ |
|---|---|---|---|
|   |   | $\geq c$ | $\leq c$ |
| closed compact | closed | $>c_{1}$ | $<c_{2}$ with $c_{2}<c_{1}$ |
| closed | closed compact | $>c_{1}$ | $<c_{2}$ with $c_{2}<c_{1}$ |
| open |   | $>c$ | $\leq c$ |
| open | open | $>c$ | $<c$ |

The number of dimensions must be finite. In infinite-dimensional spaces there are examples of two closed, convex, disjoint sets which cannot be separated by a closed hyperplane (a hyperplane where a *continuous* linear functional equals some constant) even in the weak sense where the inequalities are not strict.

Here, the compactness in the hypothesis cannot be relaxed; see an example in the section Counterexamples and uniqueness. This version of the separation theorem does generalize to infinite-dimension; the generalization is more commonly known as the Hahn–Banach separation theorem.

The proof is based on the following lemma:

**Lemma**—Let A and B be two disjoint closed subsets of $\mathbb {R} ^{n}$ , and assume A is compact. Then there exist points $a_{0}\in A$ and $b_{0}\in B$ minimizing the distance $\|a-b\|$ over $a\in A$ and $b\in B$ .

Proof of lemma

Let $a\in A$ and $b\in B$ be any pair of points, and let $r_{1}=\|b-a\|$ . Since A is compact, it is contained in some ball centered on a ; let the radius of this ball be $r_{2}$ . Let $S=B\cap {\overline {B_{r_{1}+r_{2}}(a)}}$ be the intersection of B with a closed ball of radius $r_{1}+r_{2}$ around a . Then S is compact and nonempty because it contains b . Since the distance function is continuous, there exist points $a_{0}$ and $b_{0}$ whose distance $\|a_{0}-b_{0}\|$ is the minimum over all pairs of points in $A\times S$ . It remains to show that $a_{0}$ and $b_{0}$ in fact have the minimum distance over all pairs of points in $A\times B$ . Suppose for contradiction that there exist points $a'$ and $b'$ such that $\|a'-b'\|<\|a_{0}-b_{0}\|$ . Then in particular, $\|a'-b'\|<r_{1}$ , and by the triangle inequality, $\|a-b'\|\leq \|a'-b'\|+\|a-a'\|<r_{1}+r_{2}$ . Therefore $b'$ is contained in S , which contradicts the fact that $a_{0}$ and $b_{0}$ had minimum distance over $A\times S$ . $\square$

Proof of theorem

We first prove the second case. (See the diagram.)

WLOG, A is compact. By the lemma, there exist points $a_{0}\in A$ and $b_{0}\in B$ of minimum distance to each other. Since A and B are disjoint, we have $a_{0}\neq b_{0}$ . Now, construct two hyperplanes $L_{A},L_{B}$ perpendicular to line segment $[a_{0},b_{0}]$ , with $L_{A}$ across $a_{0}$ and $L_{B}$ across $b_{0}$ . We claim that neither A nor B enters the space between $L_{A},L_{B}$ , and thus the perpendicular hyperplanes to $(a_{0},b_{0})$ satisfy the requirement of the theorem.

Algebraically, the hyperplanes $L_{A},L_{B}$ are defined by the vector $v:=b_{0}-a_{0}$ , and two constants $c_{A}:=\langle v,a_{0}\rangle <c_{B}:=\langle v,b_{0}\rangle$ , such that $L_{A}=\{x:\langle v,x\rangle =c_{A}\},L_{B}=\{x:\langle v,x\rangle =c_{B}\}$ . Our claim is that $\forall a\in A,\langle v,a\rangle \leq c_{A}$ and $\forall b\in B,\langle v,b\rangle \geq c_{B}$ .

Suppose for contradiction that there is some point $a\in A$ such that $\langle v,a\rangle >c_{A}$ . Then since the gradient of the function $f(z)=\|z-b_{0}\|^{2}$ is given by $\nabla f(z)=2(z-b_{0})$ , it follows that the directional derivative $\nabla _{a-a_{0}}f(a_{0})$ has the same sign as $\langle a-a_{0},2(a_{0}-b_{0})\rangle =-2\langle a-a_{0},v\rangle$ , which is negative. So for sufficiently small $\epsilon >0$ , the point $a'=a_{0}+\epsilon (a-a_{0})$ satisfies $f(a')<f(a_{0})$ , which contradicts the choice of $a_{0}$ since $a'\in A$ by convexity. A similar argument shows $\forall b\in B,\langle v,b\rangle \geq c_{B}$ .

Now for the first case.

Approach both $A,B$ from the inside by $A_{1}\subseteq A_{2}\subseteq \cdots \subseteq A$ and $B_{1}\subseteq B_{2}\subseteq \cdots \subseteq B$ , such that each $A_{k},B_{k}$ is closed and compact, and the unions are the relative interiors $\mathrm {relint} (A),\mathrm {relint} (B)$ . (See relative interior page for details.)

Now by the second case, for each pair $A_{k},B_{k}$ there exists some unit vector $v_{k}$ and real number $c_{k}$ , such that $\langle v_{k},A_{k}\rangle <c_{k}<\langle v_{k},B_{k}\rangle$ .

Since the unit sphere is compact, we can take a convergent subsequence, so that $v_{k}\to v$ . Let $c_{A}:=\sup _{a\in A}\langle v,a\rangle ,c_{B}:=\inf _{b\in B}\langle v,b\rangle$ . We claim that $c_{A}\leq c_{B}$ , thus separating $A,B$ .

Assume not, then there exists some $a\in A,b\in B$ such that $\langle v,a\rangle >\langle v,b\rangle$ , then since $v_{k}\to v$ , for large enough k , we have $\langle v_{k},a\rangle >\langle v_{k},b\rangle$ , contradiction.

Since a separating hyperplane cannot intersect the interiors of open convex sets, we have a corollary:

**Separation theorem I**—Let A and B be two disjoint nonempty convex sets. If A is open, then there exist a nonzero vector v and real number c such that

$\langle x,v\rangle >c\,{\text{ and }}\langle y,v\rangle \leq c$

for all x in A and y in B . If both sets are open, then there exist a nonzero vector v and real number c such that

$\langle x,v\rangle >c\,{\text{ and }}\langle y,v\rangle <c$

for all x in A and y in B .

## Case with possible intersections

If the sets $A,B$ have possible intersections, but their relative interiors are disjoint, then the proof of the first case still applies with no change, thus yielding:

**Separation theorem II**—Let A and B be two nonempty convex subsets of $\mathbb {R} ^{n}$ with disjoint relative interiors. Then there exist a nonzero vector v and a real number c such that

$\langle x,v\rangle \geq c\,{\text{ and }}\langle y,v\rangle \leq c$

in particular, we have the supporting hyperplane theorem.

**Supporting hyperplane theorem**—if A is a convex set in $\mathbb {R} ^{n},$ and $a_{0}$ is a point on the boundary of A , then there exists a supporting hyperplane of A containing $a_{0}$ .

Proof

If the affine span of A is not all of $\mathbb {R} ^{n}$ , then extend the affine span to a supporting hyperplane. Else, $\mathrm {relint} (A)=\mathrm {int} (A)$ is disjoint from $\mathrm {relint} (\{a_{0}\})=\{a_{0}\}$ , so apply the above theorem.

## Converse of theorem

Note that the existence of a hyperplane that only "separates" two convex sets in the weak sense of both inequalities being non-strict obviously does not imply that the two sets are disjoint. Both sets could have points located on the hyperplane.

## Counterexamples and uniqueness

If one of *A* or *B* is not convex, then there are many possible counterexamples. For example, *A* and *B* could be concentric circles. A more subtle counterexample is one in which *A* and *B* are both closed but neither one is compact. For example, if *A* is a closed half plane and B is bounded by one arm of a hyperbola, then there is no strictly separating hyperplane:

$A=\{(x,y):x\leq 0\}$

$B=\{(x,y):x>0,y\geq 1/x\}.\$

(Although, by an instance of the second theorem, there is a hyperplane that separates their interiors.) Another type of counterexample has *A* compact and *B* open. For example, A can be a closed square and B can be an open square that touches *A*.

In the first version of the theorem, evidently the separating hyperplane is never unique. In the second version, it may or may not be unique. Technically a separating axis is never unique because it can be translated; in the second version of the theorem, a separating axis can be unique up to translation.

The horn angle provides a good counterexample to many hyperplane separations. For example, in $\mathbb {R} ^{2}$ , the unit disk is disjoint from the open interval $((1,0),(1,1))$ , but the only line separating them contains the entirety of $((1,0),(1,1))$ . This shows that if A is closed and B is *relatively* open, then there does not necessarily exist a separation that is strict for B . However, if A is a closed convex polyhedron then such a separation exists.

## More variants

Farkas' lemma and related results can be understood as hyperplane separation theorems when the convex bodies are defined by finitely many linear inequalities.

More results may be found.

## Use in collision detection

In collision detection, the hyperplane separation theorem is usually used in the following form:

**Separating axis theorem**—Two closed convex objects are disjoint if there exists a line ("separating axis") onto which the two objects' projections are disjoint.

Regardless of dimensionality, the separating axis is always a line. For example, in 3D, the space is separated by planes, but the separating axis is perpendicular to the separating plane.

The separating axis theorem can be applied for fast collision detection between polygon meshes. Each face's normal or other feature direction is used as a separating axis. Note that this yields possible separating axes, not separating lines/planes.

In 3D, using face normals alone will fail to separate some edge-on-edge non-colliding cases. Additional axes, consisting of the cross-products of pairs of edges, one taken from each object, are required.

For increased efficiency, parallel axes may be calculated as a single axis.
