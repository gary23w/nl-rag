---
title: "Brachistochrone curve"
source: https://en.wikipedia.org/wiki/Brachistochrone_curve
domain: calculus-of-variations
license: CC-BY-SA-4.0
tags: calculus of variations, euler-lagrange equation, principle of least action, isoperimetric inequality
fetched: 2026-07-02
---

# Brachistochrone curve

In physics and mathematics, a **brachistochrone curve** (from Ancient Greek βράχιστος χρόνος*(brákhistos khrónos)* 'shortest time'), or curve of fastest descent, is the one lying on the plane between a point *A* and a lower point *B*, where *B* is not directly below *A*, on which a bead from rest slides frictionlessly under the influence of a uniform gravitational field to a given end point in the shortest time. The problem was posed by Johann Bernoulli in 1696 and famously solved in one night by Isaac Newton in 1697, though Bernoulli and several others had already found solutions of their own months earlier.

The brachistochrone curve is the same shape as the tautochrone curve; both are cycloids. But the portion of the cycloid used for each varies. Specifically, the brachistochrone can use up to a complete rotation of the cycloid (at the limit when A and B are at the same level), but always starts at a cusp, while the tautochrone can use only up to the first half rotation and always ends at the horizontal. The problem can be solved using tools from the calculus of variations and optimal control.

The curve is independent of both the mass of the test body and the local strength of gravity. Only a parameter is chosen so that the curve fits the starting point *A* and the ending point *B*. If the body is given an initial velocity at *A*, or if friction is taken into account, then the curve that minimizes time differs from the tautochrone curve.

## History

### Galileo's problem

In 1638, Galileo Galilei tried to solve a similar problem for the path of the fastest descent from a point to a wall in his *Two New Sciences*. He draws the conclusion that the arc of a circle is faster than any number of its chords,

> From the preceding it is possible to infer that the quickest path of all [lationem omnium velocissimam], from one point to another, is not the shortest path, namely, a straight line, but the arc of a circle.
> 
> . . .
> 
> Consequently the nearer the inscribed polygon approaches a circle the shorter the time required for descent from A to C. What has been proven for the quadrant holds true also for smaller arcs; the reasoning is the same.

Just after Theorem 6 of *Two New Sciences*, Galileo warns of possible fallacies and the need for a "higher science". In this dialogue, he reviews his own work. Galileo studied the cycloid and gave it its name, but the connection between it and his problem had to wait for advances in mathematics.

Galileo's conjecture is that "The shortest time of all [for a movable body] will be that of its fall along the arc ADB [of a quarter circle] and similar properties are to be understood as holding for all lesser arcs taken upward from the lowest limit B."

In Fig.1, from the "Dialogue Concerning the Two Chief World Systems", Galileo claims that the body sliding along the circular arc of a quarter circle, from A to B will reach B in less time than if it took any other path from A to B. Similarly, in Fig. 2, from any point D on the arc AB, he claims that the time along the lesser arc DB will be less than for any other path from D to B. In fact, the quickest path from A to B or from D to B, the brachistochrone, is a cycloidal arc, which is shown in Fig. 3 for the path from A to B, and Fig.4 for the path from D to B, superposed on the respective circular arc.

### Introduction of the problem

Johann Bernoulli posed the problem of the brachistochrone to the readers of *Acta Eruditorum* in June, 1696. He said:

> I, Johann Bernoulli, address the most brilliant mathematicians in the world. Nothing is more attractive to intelligent people than an honest, challenging problem, whose possible solution will bestow fame and remain as a lasting monument. Following the example set by Pascal, Fermat, etc., I hope to gain the gratitude of the whole scientific community by placing before the finest mathematicians of our time a problem which will test their methods and the strength of their intellect. If someone communicates to me the solution of the proposed problem, I shall publicly declare him worthy of praise

Bernoulli wrote the problem statement as:

> Given two points A and B in a vertical plane, what is the curve traced out by a point acted on only by gravity, which starts at A and reaches B in the shortest time.

Johann and his brother Jakob Bernoulli derived the same solution, but Johann's derivation was incorrect, and he tried to pass off Jakob's solution as his own. Johann published the solution in the journal in May 1697, and noted that the solution is the same curve as Huygens' tautochrone curve. After deriving the differential equation for the curve by the method given below, he went on to show that it does yield a cycloid, but his proof is marred by his use of a single constant instead of the three constants, *vm*, *2g* and *D*, below.

Bernoulli allowed six months for solutions but none were received during that period. At Leibniz's request, the time was publicly extended for a year and a half. At 4 p.m. on 29 January 1697, when he arrived home from the Royal Mint, Isaac Newton found the challenge in a letter from Johann Bernoulli. Newton stayed up all night to solve it and mailed the solution anonymously by the next post. Upon reading the solution, Bernoulli immediately recognized its author, exclaiming that he "recognizes a lion from his claw mark". This gives some idea of the extent of Newton's exceptionally broad knowledge, intellect, and ability, since it took Bernoulli himself two weeks to solve it, and many of Europe's greatest mathematicians took months to solve it. Newton also wrote, "I do not love to be dunned and teased by foreigners about mathematical things", and had already solved Newton's minimal resistance problem, which is considered the first of its kind in the calculus of variations. Bernoulli had employed the principle of least time in deriving his solution, but not the calculus of variations‍— Newton had employed both, and wound up pioneering the field as a result of his work on the two problems.

In the end, five mathematicians responded with solutions: Newton, Jakob Bernoulli, Gottfried Leibniz, Ehrenfried Walther von Tschirnhaus, and Guillaume de l'Hôpital. Four of the solutions (excluding L'Hôpital's) were published in the same edition of the journal as Bernoulli's. In his paper, Jakob Bernoulli gave a proof of the condition for least time similar to that below before showing that its solution is a cycloid. According to Newtonian scholar Tom Whiteside, in an attempt to outdo his brother, Jakob Bernoulli created a harder version of the brachistochrone problem. In solving it, he developed new methods that Leonhard Euler refined into what Euler called (in 1766) the *calculus of variations*. Joseph-Louis Lagrange did further work that resulted in modern infinitesimal calculus.

## Johann Bernoulli's solution

### Introduction

In a letter to L'Hôpital, (21/12/1696), Bernoulli wrote that in considering the problem of the curve of quickest descent, he first noticed a curious affinity or connection with another no less remarkable problem, leading to an "indirect method" of solution, and that shortly afterward he discovered a "direct method".

### Direct method

In a letter to Henri Basnage, held at the University of Basel Public Library, dated 30 March 1697, Bernoulli wrote that he had found two methods (always called "direct" and "indirect") to show that the Brachistochrone was the "common cycloid", also called the "roulette". On Leibniz's advice, he included only the indirect method in the *Acta Eruditorum Lipsidae* of May 1697. He wrote that this was partly because he believed it was sufficient to convince anyone who doubted the conclusion and partly because it also resolved two famous problems in optics that "the late Mr. Huygens" had raised in his treatise on light. In the same letter he criticised Newton for concealing his method.

In addition to his indirect method, he published the five other replies to the problem he had received.

Bernoulli's direct method is historically important as a proof that the brachistochrone is the cycloid. The method is to determine the curvature of the curve at each point. All the other proofs, including Newton's (which was not revealed at the time), are based on finding the gradient at each point.

In 1718, Bernoulli explained how he solved the brachistochrone problem by his direct method. He said he had not published it in 1697 for reasons that no longer applied in 1718. This paper was largely ignored until 1904, when the method's depth was first appreciated by Constantin Carathéodory, who said it shows that the cycloid is the only possible curve of quickest descent. According to him, the other solutions implied that the time of descent is stationary for the cycloid, but not necessarily the minimum possible.

#### Analytic solution

(Brachistochrone Bernoulli Direct Method)

A body is regarded as sliding along any small circular arc Ce between the radii KC and Ke, with centre K fixed. The first stage of the proof involves finding the particular circular arc, Mm, which the body traverses in the minimum time.

The line KNC intersects AL at N, and line Kne intersects it at n, and they make a small angle CKe at K. Let NK = a, and define a variable point, C on KN extended. Of all the possible circular arcs Ce, it is required to find the arc Mm, which requires the minimum time to slide between the 2 radii, KM and Km. To find Mm Bernoulli argues as follows.

Let MN = x. He defines m so that MD = mx, and n so that Mm = nx + na and notes that x is the only variable and that m is finite and n is infinitely small. The small time to travel along arc Mm is ${\frac {Mm}{MD^{\frac {1}{2}}}}={\frac {n(x+a)}{(mx)^{\frac {1}{2}}}}$ , which has to be a minimum (‘un plus petit’). He does not explain that because Mm is so small the speed along it can be assumed to be the speed at M, which is as the square root of MD, the vertical distance of M below the horizontal line AL. Plus MD=mx via Pythagoras theorem.

It follows that, when differentiated this must give

${\frac {(x-a)dx}{2x^{\frac {3}{2}}}}=0$

so that x = a.

This condition defines the curve that the body slides along in the shortest time possible. For each point, M on the curve, the radius of curvature, MK is cut in 2 equal parts by its axis AL. This property, which Bernoulli says had been known for a long time, is unique to the cycloid.

Finally, he considers the more general case where the speed is an arbitrary function X(x), so the time to be minimised is ${\frac {(x+a)}{X}}$ . The minimum condition then becomes $X={\frac {(x+a)dX}{dx}}$ which he writes as : $X=(x+a)\Delta x$ and which gives MN (=x) as a function of NK (= a). From this the equation of the curve could be obtained from the integral calculus, though he does not demonstrate this.

#### Synthetic solution

He then proceeds with what he called his Synthetic Solution, which was a classical, geometrical proof, that there is only a single curve that a body can slide down in the minimum time, and that curve is the cycloid.

"The reason for the synthetic demonstration, in the manner of the ancients, is to convince Mr. de la Hire. He has little time for our new analysis, describing it as false (He claims he has found 3 ways to prove that the curve is a cubic parabola)" – Letter from Johan Bernoulli to Pierre Varignon dated 27 Jul 1697.

Assume AMmB is the part of the cycloid joining A to B, which the body slides down in the minimum time. Let ICcJ be part of a different curve joining A to B, which can be closer to AL than AMmB. If the arc Mm subtends the angle MKm at its centre of curvature, K, let the arc on IJ that subtends the same angle be Cc. The circular arc through C with centre K is Ce. Point D on AL is vertically above M. Join K to D and point H is where CG intersects KD, extended if necessary.

Let $\tau$ and t be the times the body takes to fall along Mm and Ce respectively.

$\tau \propto {\frac {Mm}{MD^{\frac {1}{2}}}}$

,

$t\propto {\frac {Ce}{CG^{\frac {1}{2}}}}$

,

Extend CG to point F where, $CF={\frac {CH^{2}}{MD}}$ and since ${\frac {Mm}{Ce}}={\frac {MD}{CH}}$ , it follows that

${\frac {\tau }{t}}={\frac {Mm}{Ce}}.\left({\frac {CG}{MD}}\right)^{\frac {1}{2}}=\left({\frac {CG}{CF}}\right)^{\frac {1}{2}}$

Since MN = NK, for the cycloid:

$GH={\frac {MD.HD}{DK}}={\frac {MD.CM}{MK}}$

,

$CH={\frac {MD.CK}{MK}}={\frac {MD.(MK+CM)}{MK}}$

, and

$CG=CH+GH={\frac {MD.(MK+2CM)}{MK}}$

If Ce is closer to K than Mm then

$CH={\frac {MD.(MK-CM)}{MK}}$

and

$CG=CH-GH={\frac {MD.(MK-2CM)}{MK}}$

In either case,

$CF={\frac {CH^{2}}{MD}}>CG$

, and it follows that

$\tau <t$

If the arc, Cc subtended by the angle infinitesimal angle MKm on IJ is not circular, it must be greater than Ce, since Cec becomes a right-triangle in the limit as angle MKm approaches zero.

Note, Bernoulli proves that CF > CG by a similar but different argument.

From this he concludes that a body traverses the cycloid AMB in less time than any other curve ACB.

### Indirect method

According to Fermat’s principle, the path a beam of light takes between two points (which obeys Snell's law of refraction) is the one that takes the least time. In 1697, Bernoulli used this principle to derive the brachistochrone curve by considering the trajectory of a beam of light in a medium where the speed of light increases following a constant vertical acceleration (that of gravity *g*).

By the conservation of energy, the instantaneous speed of a body *v* after falling a height *y* in a uniform gravitational field is given by:

$v={\sqrt {2gy}}$

,

The speed of motion of the body along an arbitrary curve does not depend on the horizontal displacement.

Bernoulli noted that Snell's law of refraction gives a constant of the motion for a beam of light in a medium of variable density:

${\frac {\sin {\theta }}{v}}={\frac {1}{v}}{\frac {dx}{ds}}={\frac {1}{v_{m}}}$

,

where *vm* is the constant and *$\theta$* represents the angle of the trajectory with respect to the vertical.

The equations above lead to two conclusions:

1. At the onset, the angle must be zero when the particle speed is zero. Hence, the brachistochrone curve is tangent to the vertical at the origin.
2. The speed reaches a maximum value when the trajectory becomes horizontal and the angle θ = 90°.

Assuming for simplicity that the particle (or the beam) with coordinates (x,y) departs from the point (0,0) and reaches maximum speed after falling a vertical distance *D*:

$v_{m}={\sqrt {2gD}}$

.

Rearranging terms in the law of refraction and squaring gives:

$v_{m}^{2}dx^{2}=v^{2}ds^{2}=v^{2}(dx^{2}+dy^{2})$

which can be solved for *dx* in terms of *dy*:

$dx={\frac {v\,dy}{\sqrt {v_{m}^{2}-v^{2}}}}$

.

Substituting from the expressions for *v* and *vm* above gives:

$dx={\sqrt {\frac {y}{D-y}}}\,dy\,,$

which is the differential equation of an inverted cycloid generated by a circle of diameter *D=2r*, whose parametric equation is:

${\begin{aligned}x&=r(\varphi -\sin \varphi )\\y&=r(1-\cos \varphi ).\end{aligned}}$

where φ is a real parameter, corresponding to the angle through which the rolling circle has rotated. For given φ, the circle's centre lies at (*x*, *y*) = (*rφ*, *r*).

In the brachistochrone problem, the motion of the body is given by the time evolution of the parameter:

$\varphi (t)=\omega t\,,\quad \omega ={\sqrt {\frac {g}{r}}}$

where *t* is the time since the release of the body from the point (0,0).

## Jakob Bernoulli's solution

Johann's brother Jakob showed how 2nd differentials can be used to obtain the condition for least time. A modernized version of the proof is as follows. If we make a negligible deviation from the path of least time, then, for the differential triangle formed by the displacement along the path and the horizontal and vertical displacements,

$ds^{2}=dx^{2}+dy^{2}$

.

On differentiation with *dy* fixed we get,

$2ds\ d^{2}s=2dx\ d^{2}x$

.

And finally rearranging terms gives,

${\frac {dx}{ds}}d^{2}x=d^{2}s=v\ d^{2}t$

where the last part is the displacement for given change in time for 2nd differentials. Now consider the changes along the two neighboring paths in the figure below for which the horizontal separation between paths along the central line is *d2x* (the same for both the upper and lower differential triangles). Along the old and new paths, the parts that differ are,

$d^{2}t_{1}={\frac {1}{v_{1}}}{\frac {dx_{1}}{ds_{1}}}d^{2}x$

$d^{2}t_{2}={\frac {1}{v_{2}}}{\frac {dx_{2}}{ds_{2}}}d^{2}x$

For the path of least times these times are equal so for their difference we get,

$d^{2}t_{2}-d^{2}t_{1}=0={\bigg (}{\frac {1}{v_{2}}}{\frac {dx_{2}}{ds_{2}}}-{\frac {1}{v_{1}}}{\frac {dx_{1}}{ds_{1}}}{\bigg )}d^{2}x$

And the condition for least time is,

${\frac {1}{v_{2}}}{\frac {dx_{2}}{ds_{2}}}={\frac {1}{v_{1}}}{\frac {dx_{1}}{ds_{1}}}$

which agrees with Johann's assumption based on the law of refraction.

## Newton's solution

### Introduction

In June 1696, Johann Bernoulli had used the pages of the *Acta Eruditorum Lipsidae* to pose a challenge to the international mathematical community: to find the form of the curve joining two fixed points so that a mass will slide down along it, under the influence of gravity alone, in the minimum amount of time. The solution was originally to be submitted within six months. At Leibniz's suggestion, Bernoulli extended the challenge until Easter 1697, by means of a printed text called "Programma", published in Groningen, in the Netherlands.

The *Programma* is dated 1 January 1697, in the Gregorian Calendar. This was 22 December 1696 in the Julian Calendar, in use in Britain. According to Newton's niece Catherine Conduitt, Newton learned of the challenge at 4 pm on 29 January and had solved it by 4 am the next morning. His solution, communicated to the Royal Society, is dated 30 January. This solution, later published anonymously in the *Philosophical Transactions*, is correct but does not indicate the method by which Newton arrived at it. Bernoulli, writing to Henri Basnage in March 1697, indicated that even though its author, "by an excess of modesty", had not revealed his name, it could be recognised even from the scant details supplied as Newton's work, "as the lion by its claw" (in Latin, *ex ungue Leonem*).

D. T. Whiteside notes that the letter in French has *ex ungue Leonem* preceded by the French word *comme*. The much quoted version *tanquam ex ungue Leonem* is due to David Brewster's 1855 book on Newton's life and work. Bernoulli's intention was, Whiteside argues, simply to indicate he could tell the anonymous solution was Newton's, just as it was possible to tell that an animal was a lion given its claw; it was not meant to suggest that Bernoulli considered Newton the lion among mathematicians, as it has since come to be interpreted.

John Wallis, who was 80 years old at the time, learned of the problem in September 1696 from Bernoulli's youngest brother, Hieronymus, and spent three months attempting a solution before passing it in December to David Gregory, who also failed to solve it. After Newton submitted his solution, Gregory asked him for the details and took notes on their conversation. These can be found in the University of Edinburgh Library, manuscript A $78^{1}$ , dated 7 March 1697. Either Gregory did not understand Newton's argument, or Newton's explanation was very brief. But it is possible, with a high degree of confidence, to construct Newton's proof from Gregory's notes, by analogy with his method to determine the solid of minimum resistance (Principia, Book 2, Proposition 34, Scholium 2). A detailed description of his solution of this latter problem is included in the draft of a 1694 letter to Gregory. In addition to the minimum time curve problem, Newton solved a second problem at the same time. Both solutions appeared anonymously in *Philosophical Transactions of the Royal Society* for January 1697.

### The Brachistochrone problem

(Bernoulli Challenge to Newton 1)

Fig. 1, shows Gregory’s diagram (except the additional line IF is absent from it, and Z, the start point has been added). The curve ZVA is a cycloid and CHV is its generating circle. Since it appears that the body is moving upward from e to E, it must be assumed that a small body is released from Z and slides along the curve to A, without friction, under the action of gravity.

Consider a small arc eE, which the body is ascending. Assume that it traverses the straight line eL to point L, horizontally displaced from E by a small distance, o, instead of the arc eE. Note, that eL is not the tangent at e, and that o is negative when L is between B and E. Draw the line through E parallel to CH, cutting eL at n. From a property of the cycloid, En is the normal to the tangent at E, and similarly the tangent at E is parallel to VH.

Since the displacement EL is small, it differs little in direction from the tangent at E so that the angle EnL is close to a right-angle. In the limit as the arc eE approaches zero, eL becomes parallel to VH, provided o is small compared to eE making the triangles EnL and CHV similar.

Also en approaches the length of chord eE, and the increase in length, $eL-eE=nL={\frac {o.CH}{CV}}$ , ignoring terms in $o^{2}$ and higher, which represent the error due to the approximation that eL and VH are parallel.

The speed along eE or eL can be taken as that at E, proportional to ${\sqrt {CB}}$ , which is as CH, since $CH={\sqrt {CB.CV}}$

This appears to be all that Gregory’s note contains.

Let t be the additional time to reach L,

$t\propto {\frac {nL}{\sqrt {CB}}}={\frac {o.CH}{CV.{\sqrt {CB}}}}={\frac {o}{\sqrt {CV}}}$

Therefore, the increase in time to traverse a small arc displaced at one endpoint depends only on the displacement at the endpoint and is independent of the position of the arc. By Newton’s method, this is just the condition required for the curve to be traversed in the minimum time possible. Therefore, he concludes that the minimum curve must be the cycloid.

He argues as follows.

Assuming now that Fig. 1 is the minimum curve not yet determined, with vertical axis CV, and the circle CHV removed, and Fig. 2 shows part of the curve between the infinitesimal arc eE and a further infinitesimal arc Ff a finite distance along the curve. The extra time, t, to traverse eL (rather than eE) is nL divided by the speed at E (proportional to ${\sqrt {CB}}$ ), ignoring terms in $o^{2}$ and higher:

$t\propto {\frac {o.DE}{eE.{\sqrt {CB}}}}$ ,

At L the particle continues along a path LM, parallel to the original EF, to some arbitrary point M. As it has the same speed at L as at E, the time to traverse LM is the same as it would have been along the original curve EF. At M it returns to the original path at point f. By the same reasoning, the reduction in time, T, to reach f from M rather than from F is

$T\propto {\frac {o.FG}{Ff.{\sqrt {CI}}}}$

The difference (t – T) is the extra time it takes along the path eLMf compared to the original eEFf :

$(t-T)\propto \left({\frac {DE}{eE{\sqrt {CB}}}}-{\frac {FG}{Ff{\sqrt {CI}}}}\right).o$ plus terms in $o^{2}$ and higher (1)

Because eEFf is the minimum curve, (t – T) is must be greater than zero, whether o is positive or negative. It follows that the coefficient of o in (1) must be zero:

${\frac {DE}{eE{\sqrt {CB}}}}={\frac {FG}{Ff{\sqrt {CI}}}}$ (2) in the limit as eE and fF approach zero. Note since eEFf is the minimum curve it has to be assumed that the coefficient of $o^{2}$ is greater than zero.

Clearly there has to be 2 equal and opposite displacements, or the body would not return to the endpoint, A, of the curve.

If e is fixed, and if f is considered a variable point higher up the curve, then for all such points, f, ${\frac {FG}{Ff{\sqrt {CI}}}}$ is constant (equal to ${\frac {DE}{eE{\sqrt {CB}}}}$ ). By keeping f fixed and making e variable it is clear that ${\frac {DE}{eE{\sqrt {CB}}}}$ is also constant.

But, since points, e and f are arbitrary, equation (2) can be true only if ${\frac {DE}{eE{\sqrt {CB}}}}={\text{constant}}$ , everywhere, and this condition characterises the curve that is sought. This is the same technique he uses to find the form of the Solid of Least Resistance.

For the cycloid, ${\frac {DE}{eE}}={\frac {BH}{VH}}={\frac {CH}{CV}}$ , so that ${\frac {DE}{eE{\sqrt {CB}}}}={\frac {CH}{CV.{\sqrt {CB}}}}$ , which was shown above to be constant, and the Brachistochrone is the cycloid.

Newton gives no indication of how he discovered that the cycloid satisfied this last relation. It may have been by trial and error, or he may have recognised immediately that it implied the curve was the cycloid.
