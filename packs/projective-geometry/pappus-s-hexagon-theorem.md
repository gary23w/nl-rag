---
title: "Pappus's hexagon theorem"
source: https://en.wikipedia.org/wiki/Pappus's_hexagon_theorem
domain: projective-geometry
license: CC-BY-SA-4.0
tags: projective geometry, projective plane, homogeneous coordinates, desargues theorem
fetched: 2026-07-02
---

# Pappus's hexagon theorem

In mathematics, **Pappus's hexagon theorem** (attributed to Pappus of Alexandria) states that if $A,B,C$ is one set of collinear points, and $a,b,c$ is another set of collinear points, then the intersection points $X,Y,Z$ of line pairs $Ab$ and $aB,Ac$ and $aC,Bc$ and $bC$ are collinear, lying on the *Pappus line*. These three points are the points of intersection of the "opposite" sides of the hexagon $AbCaBc$ .

It holds in a projective plane over any field, but fails for projective planes over any noncommutative division ring. Projective planes in which the "theorem" is valid are called **pappian planes**.

If one considers a pappian plane containing a hexagon as just described but with sides $Ab$ and $aB$ parallel and also sides $Bc$ and $bC$ parallel (so that the Pappus line u is the line at infinity), one gets the *affine version* of Pappus's theorem shown in the second diagram.

If the Pappus line u and the lines $g,h$ have a point in common, one gets the so-called **little** version of Pappus's theorem.

The dual of this incidence theorem states that given one set of concurrent lines $A,B,C$ , and another set of concurrent lines $a,b,c$ , then the lines $x,y,z$ defined by pairs of points resulting from pairs of intersections $A\cap b$ and $a\cap B,\;A\cap c$ and $a\cap C,\;B\cap c$ and $b\cap C$ are concurrent. (*Concurrent* means that the lines pass through one point.)

Pappus's theorem is a special case of Pascal's theorem for a conic—the limiting case when the conic degenerates into 2 straight lines. Pascal's theorem is in turn a special case of the Cayley–Bacharach theorem.

The Pappus configuration is the configuration of 9 lines and 9 points that occurs in Pappus's theorem, with each line meeting 3 of the points and each point meeting 3 lines. In general, the Pappus line does not pass through the point of intersection of $ABC$ and $abc$ . This configuration is self dual. Since, in particular, the lines $Bc,bC,XY$ have the properties of the lines $x,y,z$ of the dual theorem, and collinearity of $X,Y,Z$ is equivalent to concurrence of $Bc,bC,XY$ , the dual theorem is therefore just the same as the theorem itself. The Levi graph of the Pappus configuration is the Pappus graph, a bipartite distance-regular graph with 18 vertices and 27 edges.

## Proof: affine form

If the affine form of the statement can be proven, then the projective form of Pappus's theorem is proven, as the extension of a pappian plane to a projective plane is unique.

Because of the parallelity in an affine plane one has to distinct two cases: $g\not \parallel h$ and $g\parallel h$ . The key for a simple proof is the possibility for introducing a "suitable" coordinate system:

**Case 1:** The lines $g,h$ intersect at point $S=g\cap h$ . In this case coordinates are introduced, such that $\;S=(0,0),\;A=(0,1),\;c=(1,0)\;$ (see diagram). $B,C$ have the coordinates $\;B=(0,\gamma ),\;C=(0,\delta ),\;\gamma ,\delta \notin \{0,1\}$ .

From the parallelity of the lines $Bc,\;Cb$ one gets $b=({\tfrac {\delta }{\gamma }},0)$ and the parallelity of the lines $Ab,Ba$ yields $a=(\delta ,0)$ . Hence line $Ca$ has slope $-1$ and is parallel line $Ac$ .

**Case 2:** $g\parallel h\$ (little theorem). In this case the coordinates are chosen such that $\;c=(0,0),\;b=(1,0),\;A=(0,1),\;B=(\gamma ,1),\;\gamma \neq 0$ . From the parallelity of $Ab\parallel Ba$ and $cB\parallel bC$ one gets $\;C=(\gamma +1,1)\;$ and $\;a=(\gamma +1,0)\;$ , respectively, and at least the parallelity $\;Ac\parallel Ca\;$ .

## Proof with homogeneous coordinates

Choose homogeneous coordinates with

$C=(1,0,0),\;c=(0,1,0),\;X=(0,0,1),\;A=(1,1,1)$

.

On the lines $AC,Ac,AX$ , given by $x_{2}=x_{3},\;x_{1}=x_{3},\;x_{2}=x_{1}$ , take the points $B,Y,b$ to be

$B=(p,1,1),\;Y=(1,q,1),\;b=(1,1,r)$

for some $p,q,r$ . The three lines $XB,CY,cb$ are $x_{1}=x_{2}p,\;x_{2}=x_{3}q,\;x_{3}=x_{1}r$ , so they pass through the same point a if and only if $rqp=1$ . The condition for the three lines $Cb,cB$ and $XY$ with equations $x_{2}=x_{1}q,\;x_{1}=x_{3}p,\;x_{3}=x_{2}r$ to pass through the same point Z is $rpq=1$ . So this last set of three lines is concurrent if all the other eight sets are because multiplication is commutative, so $pq=qp$ . Equivalently, $X,Y,Z$ are collinear.

The proof above also shows that for Pappus's theorem to hold for a projective space over a division ring it is both sufficient and necessary that the division ring is a (commutative) field. German mathematician Gerhard Hessenberg proved that Pappus's theorem implies Desargues's theorem. In general, Pappus's theorem holds for some projective plane if and only if it is a projective plane over a commutative field. The projective planes in which Pappus's theorem does not hold are Desarguesian projective planes over noncommutative division rings, and non-Desarguesian planes.

The proof is invalid if $C,c,X$ happen to be collinear. In that case an alternative proof can be provided, for example, using a different projective reference.

## Dual theorem

Because of the principle of duality for projective planes the **dual theorem of Pappus** is true:

If 6 lines $A,b,C,a,B,c$ are chosen alternately from two pencils with centers $G,H$ , the lines

$X:=(A\cap b)(a\cap B),$

$Y:=(c\cap A)(C\cap a),$

$Z:=(b\cap C)(B\cap c)$

are concurrent, that means: they have a point U in common. The left diagram shows the projective version, the right one an affine version, where the points $G,H$ are points at infinity. If point U is on the line $GH$ than one gets the "dual little theorem" of Pappus' theorem.

- (dual theorem: projective form) dual theorem: projective form
- (dual theorem: affine form) dual theorem: affine form

If in the affine version of the dual "little theorem" point U is a point at infinity too, one gets Thomsen's theorem, a statement on 6 points on the sides of a triangle (see diagram). The Thomsen figure plays an essential role coordinatising an axiomatic defined projective plane. The proof of the closure of Thomsen's figure is covered by the proof for the "little theorem", given above. But there exists a simple direct proof, too:

Because the statement of Thomsen's theorem (the closure of the figure) uses only the terms *connect, intersect* and *parallel*, the statement is affinely invariant, and one can introduce coordinates such that $P=(0,0),\;Q=(1,0),\;R=(0,1)$ (see right diagram). The starting point of the sequence of chords is $(0,\lambda ).$ One easily verifies the coordinates of the points given in the diagram, which shows: the last point coincides with the first point.

- (Thomsen figure (points '"`UNIQ--postMath-00000051-QINU`"' of the triangle '"`UNIQ--postMath-00000052-QINU`"') as dual theorem of the little theorem of Pappus ('"`UNIQ--postMath-00000053-QINU`"' is at infinity, too !).) *Thomsen figure* (points $\color {red}1,2,3,4,5,6$ of the triangle $PQR$ ) as dual theorem of the little theorem of Pappus ( U is at infinity, too !).
- (Thomsen figure: proof) Thomsen figure: proof

## Other statements of the theorem

In addition to the above characterizations of Pappus's theorem and its dual, the following are equivalent statements:

- If the six vertices of a hexagon lie alternately on two lines, then the three points of intersection of pairs of opposite sides are collinear.
- Arranged in a matrix of nine points (as in the figure and description above) and thought of as evaluating a permanent, if the first two rows and the six "diagonal" triads are collinear, then the third row is collinear.

$\left|{\begin{matrix}A&B&C\\a&b&c\\X&Y&Z\end{matrix}}\right|$

That is, if

$\ ABC,abc,AbZ,BcX,CaY,XbC,YcA,ZaB\$

are lines, then Pappus's theorem states that

$XYZ$

must be a line. Also, note that the same matrix formulation applies to the dual form of the theorem when

$(A,B,C)$

etc.

are triples of concurrent lines.

- Given three distinct points on each of two distinct lines, pair each point on one of the lines with one from the other line, then the joins of points not paired will meet in (opposite) pairs at points along a line.
- If two triangles are perspective in at least two different ways, then they are perspective in three ways.
- If $\;AB,CD,\;$ and $EF$ are concurrent and $DE,FA,$ and $BC$ are concurrent, then $AD,BE,$ and $CF$ are concurrent.

## Origins

What we call Pappus's Theorem is found in chapters 202, 206, 207, 209, and 211, also numbered as Propositions 134, 138, 139, 141, and 143, of Book VII of Pappus's *Collection*. These are Lemmas VIII, XII, XIII, XV, and XVII in the part of Book VII consisting of lemmas to the first of the three books of Euclid's *Porisms.*

Lemma VIII is what is called above the affine version of Pappus's Theorem. Pappus proves it with areas. In the figure below, $\varDelta E\ ||\ B\varGamma \quad \&\quad EH\ ||\ BZ.$

We are going to show $\varDelta Z\ ||\ \varGamma H.$ To do this, we draw BE, ΔΓ, and ZH.

As triangles, $\triangle \varDelta BE=\triangle \varDelta \varGamma E.$ Adding △*ΔAE* to either side yields $\triangle ABE=\triangle \varDelta \varGamma A.$ Likewise, $\triangle BEZ=\triangle BHZ,$ and subtracting △*BAZ* yields $\triangle ABE=\triangle AHZ.$ From this and what we already know, $\triangle \varDelta \varGamma A=\triangle AHZ.$ Adding △*AΓH*, we obtain $\triangle \varDelta \varGamma H=\triangle Z\varGamma H,$ which gives us the parallelism that we want.

The other lemmas are proved in terms of what today is known as the cross ratio of four collinear points. Three earlier lemmas are used. The first of these, Lemma III, has the diagram below (which uses Pappus's lettering, with G for Γ, D for Δ, J for Θ, and L for Λ).

Here three concurrent straight lines, AB, AG, and AD, are crossed by two lines, JB and JE, which concur at J. Also KL is drawn parallel to AZ. Then ${\overline {KJ}}:{\overline {JL}}::\left({\overline {KJ}}:{\overline {AG}}\ \&\ {\overline {AG}}:{\overline {JL}}\right)::\left({\overline {JD}}:{\overline {GD}}\ \&\ {\overline {BG}}:{\overline {JB}}\right)$ These proportions might be written today as equations: ${\frac {\overline {KJ}}{\overline {JL}}}={\frac {\overline {KJ}}{\overline {AG}}}\times {\frac {\overline {AG}}{\overline {JL}}}={\frac {\overline {JD}}{\overline {GD}}}\times {\frac {\overline {BG}}{\overline {JB}}}.$ The last compound ratio (namely *JD* : *GD* & *BG* : *JB*) is what is known today as the cross ratio of the collinear points J, G, D, and B in that order; it is denoted today by (*J*, *G*; *D*, *B*). So we have shown that this is independent of the choice of the particular straight line JD that crosses the three straight lines that concur at A. In particular $(J,G;D,B)=(J,Z;H,E).$ It does not matter on which side of A the straight line JE falls. In particular, the situation may be as in the next diagram, which is the diagram for Lemma X.

Just as before, we have $(J,G;D,B)=(J,Z;H,E).$ Pappus does not explicitly prove this; but Lemma X is a converse, namely that if these two cross ratios are the same, and the straight lines BE and DH cross at A, then the points G, A, and Z must be collinear.

What we showed originally can be written as $(J,\infty ;K,L)=(J,G;D,B),$ with ∞ taking the place of the (nonexistent) intersection of JK and AG. Pappus shows this, in effect, in Lemma XI, whose diagram, however, has different lettering:

What Pappus shows is ${\overline {DE}}\cdot {\overline {ZH}}:{\overline {EZ}}\cdot {\overline {HD}}::{\overline {GB}}:{\overline {BE}},$ which we may write as $(D,Z;E,H)=(\infty ,B;E,G).$ The diagram for Lemma XII is:

The diagram for Lemma XIII is the same, but BA and DG, extended, meet at N. In any case, considering straight lines through G as cut by the three straight lines through A, (and accepting that equations of cross ratios remain valid after permutation of the entries,) we have by Lemma III or XI $(G,J;E,H)=(G,D;\infty Z).$ Considering straight lines through D as cut by the three straight lines through B, we have $(L,D;E,K)=(G,D;\infty Z).$ Thus $(E,H;J,G)=(E,K;D,L),$ so by Lemma X, the points H, M, and K are collinear. That is, the points of intersection of the pairs of opposite sides of the hexagon ADEGBZ are collinear.

Lemmas XV and XVII are that, if the point M is determined as the intersection of HK and BG, then the points A, M, and D are collinear. That is, the points of intersection of the pairs of opposite sides of the hexagon BEKHZG are collinear.
