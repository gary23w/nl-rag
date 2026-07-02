---
title: "Barycentric coordinate system"
source: https://en.wikipedia.org/wiki/Barycentric_coordinate_system
domain: interpolation-methods
license: CC-BY-SA-4.0
tags: polynomial interpolation, lagrange polynomial, newton polynomial, runge phenomenon
fetched: 2026-07-02
---

# Barycentric coordinate system

In geometry, a **barycentric coordinate system** is a coordinate system in which the location of a point is specified by reference to a simplex (a triangle for points in a plane, a tetrahedron for points in three-dimensional space, etc.). The **barycentric coordinates** of a point can be interpreted as masses placed at the vertices of the simplex, such that the point is the center of mass (or *barycenter*) of these masses. These masses can be zero or negative; they are all positive if and only if the point is strictly inside the simplex.

Every point has barycentric coordinates, and their sum is never zero. Two tuples of barycentric coordinates specify the same point if and only if they are proportional; that is to say, if one tuple can be obtained by multiplying the elements of the other tuple by the same non-zero number. Therefore, barycentric coordinates are either considered to be defined up to multiplication by a nonzero constant, or normalized for summing to unity.

Barycentric coordinates were introduced by August Möbius in 1827. They are special homogeneous coordinates. Barycentric coordinates are strongly related with Cartesian coordinates and, more generally, to affine coordinates ().

Barycentric coordinates are particularly useful in triangle geometry for studying properties that do not depend on the angles of the triangle, such as Ceva's theorem, Routh's theorem, and Menelaus's theorem. In computer-aided design, they are useful for defining some kinds of Bézier surfaces.

## Definition

Let $A_{0},\ldots ,A_{n}$ be *n* + 1 points in a Euclidean space, a flat or an affine space $\mathbf {A}$ of dimension n that are affinely independent; this means that there is no affine subspace of dimension *n* − 1 that contains all the points, or, equivalently that the points define a simplex. Given any point $P\in \mathbf {A} ,$ there are scalars $a_{0},\ldots ,a_{n}$ that are not all zero, such that $(a_{0}+\cdots +a_{n}){\overset {}{\overrightarrow {OP}}}=a_{0}{\overset {}{\overrightarrow {OA_{0}}}}+\cdots +a_{n}{\overset {}{\overrightarrow {OA_{n}}}},$ for any point O. (As usual, the notation ${\overset {}{\overrightarrow {AB}}}$ represents the translation vector or free vector that maps the point A to the point B.)

The elements of a (*n* + 1) tuple $(a_{0}:\dotsc :a_{n})$ that satisfies this equation are called *barycentric coordinates* of P with respect to $A_{0},\ldots ,A_{n}.$ The use of colons in the notation of the tuple means that barycentric coordinates are a sort of homogeneous coordinates, that is, the point is not changed if all coordinates are multiplied by the same nonzero constant. Moreover, the barycentric coordinates are also not changed if the auxiliary point O, the origin, is changed.

The barycentric coordinates of a point are unique up to a scaling. That is, two tuples $(a_{0}:\dotsc :a_{n})$ and $(b_{0}:\dotsc :b_{n})$ are barycentric coordinates of the same point if and only if there is a nonzero scalar $\lambda$ such that $b_{i}=\lambda a_{i}$ for every i.

In some contexts, it is useful to constrain the barycentric coordinates of a point so that they are unique. This is usually achieved by imposing the condition $\sum a_{i}=1,$ or equivalently by dividing every $a_{i}$ by the sum of all $a_{i}.$ These specific barycentric coordinates are called **normalized** or **absolute barycentric coordinates**. Sometimes, they are also called affine coordinates, although this term refers commonly to a slightly different concept.

Sometimes, it is the normalized barycentric coordinates that are called *barycentric coordinates*. In this case the above defined coordinates are called *homogeneous barycentric coordinates*.

With above notation, the homogeneous barycentric coordinates of Ai are all zero, except the one of index i. When working over the real numbers (the above definition is also used for affine spaces over an arbitrary field), the points whose all normalized barycentric coordinates are nonnegative form the convex hull of $\{A_{0},\ldots ,A_{n}\},$ which is the simplex that has these points as its vertices.

With above notation, a tuple $(a_{1},\ldots ,a_{n})$ such that $\sum _{i=0}^{n}a_{i}=0$ does not define any point, but the vector $a_{0}{\overset {}{\overrightarrow {OA_{0}}}}+\cdots +a_{n}{\overset {}{\overrightarrow {OA_{n}}}}$ is independent from the origin O. As the direction of this vector is not changed if all $a_{i}$ are multiplied by the same scalar, the homogeneous tuple $(a_{0}:\dotsc :a_{n})$ defines a direction of lines, that is a point at infinity. See below for more details.

## Relationship with Cartesian or affine coordinates

Barycentric coordinates are strongly related to Cartesian coordinates and, more generally, affine coordinates. For a space of dimension n, these coordinate systems are defined relative to a point O, the origin, whose coordinates are zero, and n points $A_{1},\ldots ,A_{n},$ whose coordinates are zero except that of index i that equals one.

A point has coordinates $(x_{1},\ldots ,x_{n})$ for such a coordinate system if and only if its normalized barycentric coordinates are $(1-x_{1}-\cdots -x_{n},x_{1},\ldots ,x_{n})$ relatively to the points $O,A_{1},\ldots ,A_{n}.$

The main advantage of barycentric coordinate systems is to be symmetric with respect to the *n* + 1 defining points. They are therefore often useful for studying properties that are symmetric with respect to *n* + 1 points. On the other hand, distances and angles are difficult to express in general barycentric coordinate systems, and when they are involved, it is generally simpler to use a Cartesian coordinate system.

## Relationship with projective coordinates

Homogeneous barycentric coordinates are also strongly related with some projective coordinates. However this relationship is more subtle than in the case of affine coordinates, and, for being clearly understood, requires a coordinate-free definition of the projective completion of an affine space, and a definition of a projective frame.

The *projective completion* of an affine space of dimension n is a projective space of the same dimension that contains the affine space as the complement of a hyperplane. The projective completion is unique up to an isomorphism. The hyperplane is called the hyperplane at infinity, and its points are the points at infinity of the affine space.

Given a projective space of dimension n, a *projective frame* is an ordered set of *n* + 2 points that are not contained in the same hyperplane. A projective frame defines a projective coordinate system such that the coordinates of the (*n* + 2)th point of the frame are all equal, and, otherwise, all coordinates of the ith point are zero, except the ith one.

When constructing the projective completion from an affine coordinate system, one commonly defines it with respect to a projective frame consisting of the intersections with the hyperplane at infinity of the coordinate axes, the origin of the affine space, and the point that has all its affine coordinates equal to one. This implies that the points at infinity have their last coordinate equal to zero, and that the projective coordinates of a point of the affine space are obtained by completing its affine coordinates by one as (*n* + 1)th coordinate.

When one has *n* + 1 points in an affine space that define a barycentric coordinate system, this is another projective frame of the projective completion that is convenient to choose. This frame consists of these points and their centroid, that is the point that has all its barycentric coordinates equal. In this case, the homogeneous barycentric coordinates of a point in the affine space are the same as the projective coordinates of this point. A point is at infinity if and only if the sum of its coordinates is zero. This point is in the direction of the vector defined at the end of § Definition.

## Barycentric coordinates on triangles

In the context of a triangle, barycentric coordinates are also known as **area coordinates** or **areal coordinates**, because the coordinates of *P* with respect to triangle *ABC* are equivalent to the (signed) ratios of the areas of *PBC*, *PCA* and *PAB* to the area of the reference triangle *ABC*. Areal and trilinear coordinates are used for similar purposes in geometry.

Barycentric or areal coordinates are extremely useful in engineering applications involving triangular subdomains. These make analytic integrals often easier to evaluate, and Gaussian quadrature tables are often presented in terms of area coordinates.

Consider a triangle $ABC$ with vertices $A=(a_{1},a_{2})$ , $B=(b_{1},b_{2})$ , $C=(c_{1},c_{2})$ in the x,y-plane, $\mathbb {R} ^{2}$ . One may regard points in $\mathbb {R} ^{2}$ as vectors, so it makes sense to add or subtract them and multiply them by scalars.

Each triangle $ABC$ has a *signed area* or *sarea*, which is plus or minus its area:

```
 
  
    
      
        sarea
        ⁡
        (
        A
        B
        C
        )
        =
        ±
        area
        ⁡
        (
        A
        B
        C
        )
        .
      
    
    {\displaystyle \operatorname {sarea} (ABC)=\pm \operatorname {area} (ABC).}
  
```

The sign is plus if the path from A to B to C then back to A goes around the triangle in a counterclockwise direction. The sign is minus if the path goes around in a clockwise direction.

Let P be a point in the plane, and let $(\lambda _{1},\lambda _{2},\lambda _{3})$ be its *normalized barycentric coordinates* with respect to the triangle $ABC$ , so

```
 
  
    
      
        P
        =
        
          λ
          
            1
          
        
        A
        +
        
          λ
          
            2
          
        
        B
        +
        
          λ
          
            3
          
        
        C
      
    
    {\displaystyle P=\lambda _{1}A+\lambda _{2}B+\lambda _{3}C}
  
```

and

```
 
  
    
      
        1
        =
        
          λ
          
            1
          
        
        +
        
          λ
          
            2
          
        
        +
        
          λ
          
            3
          
        
        .
      
    
    {\displaystyle 1=\lambda _{1}+\lambda _{2}+\lambda _{3}.}
  
```

Normalized barycentric coordinates $(\lambda _{1},\lambda _{2},\lambda _{3})$ are also called *areal coordinates* because they represent ratios of signed areas of triangles:

```
 
  
    
      
        
          
            
              
                
                  λ
                  
                    1
                  
                
              
              
                
                =
                sarea
                ⁡
                (
                P
                B
                C
                )
                
                  /
                
                sarea
                ⁡
                (
                A
                B
                C
                )
              
            
            
              
                
                  λ
                  
                    2
                  
                
              
              
                
                =
                sarea
                ⁡
                (
                A
                P
                C
                )
                
                  /
                
                sarea
                ⁡
                (
                A
                B
                C
                )
              
            
            
              
                
                  λ
                  
                    3
                  
                
              
              
                
                =
                sarea
                ⁡
                (
                A
                B
                P
                )
                
                  /
                
                sarea
                ⁡
                (
                A
                B
                C
                )
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\lambda _{1}&=\operatorname {sarea} (PBC)/\operatorname {sarea} (ABC)\\\lambda _{2}&=\operatorname {sarea} (APC)/\operatorname {sarea} (ABC)\\\lambda _{3}&=\operatorname {sarea} (ABP)/\operatorname {sarea} (ABC).\end{aligned}}}
  
```

One may prove these ratio formulas based on the facts that a triangle is half of a parallelogram, and the area of a parallelogram is easy to compute using a determinant.

Specifically, let

```
   
  
    
      
        D
        =
        −
        A
        +
        B
        +
        C
        .
      
    
    {\displaystyle D=-A+B+C.}
  
```

$ABCD$ is a parallelogram because its pairs of opposite sides, represented by the pairs of displacement vectors $D-C=B-A$ , and $D-B=C-A$ , are parallel and congruent.

Triangle $ABC$ is half of the parallelogram $ABDC$ , so twice its signed area is equal to the signed area of the parallelogram, which is given by the $2\times 2$ determinant $\det(B-A,C-A)$ whose *columns* are the displacement vectors $B-A$ and $C-A$ :

```
   
  
    
      
        sarea
        ⁡
        (
        A
        B
        C
        D
        )
        =
        det
        
          
            (
            
              
                
                  
                    b
                    
                      1
                    
                  
                  −
                  
                    a
                    
                      1
                    
                  
                
                
                  
                    c
                    
                      1
                    
                  
                  −
                  
                    a
                    
                      1
                    
                  
                
              
              
                
                  
                    b
                    
                      2
                    
                  
                  −
                  
                    a
                    
                      2
                    
                  
                
                
                  
                    c
                    
                      2
                    
                  
                  −
                  
                    a
                    
                      2
                    
                  
                
              
            
            )
          
        
      
    
    {\displaystyle \operatorname {sarea} (ABCD)=\det {\begin{pmatrix}b_{1}-a_{1}&c_{1}-a_{1}\\b_{2}-a_{2}&c_{2}-a_{2}\end{pmatrix}}}
  
```

Expanding the determinant, using its *alternating* and *multilinear* properties, one obtains

```
   
  
    
      
        
          
            
              
                det
                (
                B
                −
                A
                ,
                C
                −
                A
                )
              
              
                
                =
                det
                (
                B
                ,
                C
                )
                −
                det
                (
                A
                ,
                C
                )
                −
                det
                (
                B
                ,
                A
                )
                +
                det
                (
                A
                ,
                A
                )
              
            
            
              
              
                
                =
                det
                (
                A
                ,
                B
                )
                +
                det
                (
                B
                ,
                C
                )
                +
                det
                (
                C
                ,
                A
                )
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\det(B-A,C-A)&=\det(B,C)-\det(A,C)-\det(B,A)+\det(A,A)\\&=\det(A,B)+\det(B,C)+\det(C,A)\end{aligned}}}
  
```

so

```
  
  
    
      
        2
        sarea
        ⁡
        (
        A
        B
        C
        )
        =
        det
        (
        A
        ,
        B
        )
        +
        det
        (
        B
        ,
        C
        )
        +
        det
        (
        C
        ,
        A
        )
        .
      
    
    {\displaystyle 2\operatorname {sarea} (ABC)=\det(A,B)+\det(B,C)+\det(C,A).}
  
```

Similarly,

```
  
  
    
      
        2
        sarea
        ⁡
        (
        P
        B
        C
        )
        =
        det
        (
        P
        ,
        B
        )
        +
        det
        (
        B
        ,
        C
        )
        +
        det
        (
        C
        ,
        P
        )
      
    
    {\displaystyle 2\operatorname {sarea} (PBC)=\det(P,B)+\det(B,C)+\det(C,P)}
  
,
```

To obtain the ratio of these signed areas, express P in the second formula in terms of its barycentric coordinates:

```
  
  
    
      
        
          
            
              
                2
                sarea
                ⁡
                (
                P
                B
                C
                )
              
              
                
                =
                det
                (
                
                  λ
                  
                    1
                  
                
                A
                +
                
                  λ
                  
                    2
                  
                
                B
                +
                
                  λ
                  
                    3
                  
                
                C
                ,
                B
                )
                +
                det
                (
                B
                ,
                C
                )
                +
                det
                (
                C
                ,
                
                  λ
                  
                    1
                  
                
                A
                +
                
                  λ
                  
                    2
                  
                
                B
                +
                
                  λ
                  
                    3
                  
                
                C
                )
              
            
            
              
              
                
                =
                
                  λ
                  
                    1
                  
                
                det
                (
                A
                ,
                B
                )
                +
                
                  λ
                  
                    3
                  
                
                det
                (
                C
                ,
                B
                )
                +
                det
                (
                B
                ,
                C
                )
                +
                
                  λ
                  
                    1
                  
                
                det
                (
                C
                ,
                A
                )
                +
                
                  λ
                  
                    2
                  
                
                det
                (
                C
                ,
                B
                )
              
            
            
              
              
                
                =
                
                  λ
                  
                    1
                  
                
                det
                (
                A
                ,
                B
                )
                +
                
                  λ
                  
                    1
                  
                
                det
                (
                C
                ,
                A
                )
                +
                (
                1
                −
                
                  λ
                  
                    2
                  
                
                −
                
                  λ
                  
                    3
                  
                
                )
                det
                (
                B
                ,
                C
                )
              
            
          
        
        .
      
    
    {\displaystyle {\begin{aligned}2\operatorname {sarea} (PBC)&=\det(\lambda _{1}A+\lambda _{2}B+\lambda _{3}C,B)+\det(B,C)+\det(C,\lambda _{1}A+\lambda _{2}B+\lambda _{3}C)\\&=\lambda _{1}\det(A,B)+\lambda _{3}\det(C,B)+\det(B,C)+\lambda _{1}\det(C,A)+\lambda _{2}\det(C,B)\\&=\lambda _{1}\det(A,B)+\lambda _{1}\det(C,A)+(1-\lambda _{2}-\lambda _{3})\det(B,C)\end{aligned}}.}
  
```

The barycentric coordinates are normalized so $1=\lambda _{1}+\lambda _{2}+\lambda _{3}$ , hence $\lambda _{1}=(1-\lambda _{2}-\lambda _{3})$ . Plug that into the previous line to obtain

```
  
  
    
      
        
          
            
              
                2
                sarea
                ⁡
                (
                P
                B
                C
                )
              
              
                
                =
                
                  λ
                  
                    1
                  
                
                (
                det
                (
                A
                ,
                B
                )
                +
                det
                (
                B
                ,
                C
                )
                +
                det
                (
                C
                ,
                A
                )
                )
              
            
            
              
              
                
                =
                (
                
                  λ
                  
                    1
                  
                
                )
                (
                2
                sarea
                ⁡
                (
                A
                B
                C
                )
                )
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}2\operatorname {sarea} (PBC)&=\lambda _{1}(\det(A,B)+\det(B,C)+\det(C,A))\\&=(\lambda _{1})(2\operatorname {sarea} (ABC)).\end{aligned}}}
  
```

Therefore

```
 
  
    
      
        
          λ
          
            1
          
        
        =
        sarea
        ⁡
        (
        P
        B
        C
        )
        
          /
        
        sarea
        ⁡
        (
        A
        B
        C
        )
      
    
    {\displaystyle \lambda _{1}=\operatorname {sarea} (PBC)/\operatorname {sarea} (ABC)}
  
.
```

Similar calculations prove the other two formulas

```
 
  
    
      
        
          λ
          
            2
          
        
        =
        sarea
        ⁡
        (
        A
        P
        C
        )
        
          /
        
        sarea
        ⁡
        (
        A
        B
        C
        )
      
    
    {\displaystyle \lambda _{2}=\operatorname {sarea} (APC)/\operatorname {sarea} (ABC)}
  

 
  
    
      
        
          λ
          
            3
          
        
        =
        sarea
        ⁡
        (
        A
        B
        P
        )
        
          /
        
        sarea
        ⁡
        (
        A
        B
        C
        )
      
    
    {\displaystyle \lambda _{3}=\operatorname {sarea} (ABP)/\operatorname {sarea} (ABC)}
  
.
```

Trilinear coordinates $(\gamma _{1},\gamma _{2},\gamma _{3})$ of P are signed distances from P to the lines BC, AC, and AB, respectively. The sign of $\gamma _{1}$ is positive if P and A lie on the same side of BC, negative otherwise. The signs of $\gamma _{2}$ and $\gamma _{3}$ are assigned similarly. Let

```
 
  
    
      
        a
        =
        length
        ⁡
        (
        B
        C
        )
      
    
    {\displaystyle a=\operatorname {length} (BC)}
  
, 
  
    
      
        b
        =
        length
        ⁡
        (
        C
        A
        )
      
    
    {\displaystyle b=\operatorname {length} (CA)}
  
, 
  
    
      
        c
        =
        length
        ⁡
        (
        A
        B
        )
      
    
    {\displaystyle c=\operatorname {length} (AB)}
  
.  
```

Then

```
 
  
    
      
        
          
            
              
                
                  γ
                  
                    1
                  
                
                a
              
              
                
                =
                ±
                2
                sarea
                ⁡
                (
                P
                B
                C
                )
              
            
            
              
                
                  γ
                  
                    2
                  
                
                b
              
              
                
                =
                ±
                2
                sarea
                ⁡
                (
                A
                P
                C
                )
              
            
            
              
                
                  γ
                  
                    3
                  
                
                c
              
              
                
                =
                ±
                2
                sarea
                ⁡
                (
                A
                B
                P
                )
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}\gamma _{1}a&=\pm 2\operatorname {sarea} (PBC)\\\gamma _{2}b&=\pm 2\operatorname {sarea} (APC)\\\gamma _{3}c&=\pm 2\operatorname {sarea} (ABP)\end{aligned}}}
  
```

where, as above, sarea stands for signed area. All three signs are plus if triangle ABC is positively oriented, minus otherwise. The relations between trilinear and barycentric coordinates are obtained by substituting these formulas into the above formulas that express barycentric coordinates as ratios of areas.

Switching back and forth between the barycentric coordinates and other coordinate systems makes some problems much easier to solve.

### Conversion between barycentric and Cartesian coordinates

#### Edge approach

Given a point $\mathbf {r}$ in a triangle's plane one can obtain the barycentric coordinates $\lambda _{1}$ , $\lambda _{2}$ and $\lambda _{3}$ from the Cartesian coordinates $(x,y)$ or vice versa.

We can write the Cartesian coordinates of the point $\mathbf {r}$ in terms of the Cartesian components of the triangle vertices $\mathbf {r} _{1}$ , $\mathbf {r} _{2}$ , $\mathbf {r} _{3}$ where $\mathbf {r} _{i}=(x_{i},y_{i})$ and in terms of the barycentric coordinates of $\mathbf {r}$ as

${\begin{aligned}x&=\lambda _{1}x_{1}+\lambda _{2}x_{2}+\lambda _{3}x_{3}\\[2pt]y&=\lambda _{1}y_{1}+\lambda _{2}y_{2}+\lambda _{3}y_{3}\end{aligned}}$

That is, the Cartesian coordinates of any point are a weighted average of the Cartesian coordinates of the triangle's vertices, with the weights being the point's barycentric coordinates summing to unity.

To find the reverse transformation, from Cartesian coordinates to barycentric coordinates, we first substitute $\lambda _{3}=1-\lambda _{1}-\lambda _{2}$ into the above to obtain

${\begin{aligned}x&=\lambda _{1}x_{1}+\lambda _{2}x_{2}+(1-\lambda _{1}-\lambda _{2})x_{3}\\[2pt]y&=\lambda _{1}y_{1}+\lambda _{2}y_{2}+(1-\lambda _{1}-\lambda _{2})y_{3}\end{aligned}}$

Rearranging, this is

${\begin{aligned}\lambda _{1}(x_{1}-x_{3})+\lambda _{2}(x_{2}-x_{3})+x_{3}-x&=0\\[2pt]\lambda _{1}(y_{1}-y_{3})+\lambda _{2}(y_{2}-\,y_{3})+y_{3}-\,y&=0\end{aligned}}$

This linear transformation may be written more succinctly as

$\mathbf {T} \cdot \lambda =\mathbf {r} -\mathbf {r} _{3}$

where $\lambda$ is the vector of the first two barycentric coordinates, $\mathbf {r}$ is the vector of Cartesian coordinates, and $\mathbf {T}$ is a matrix given by

$\mathbf {T} =\left({\begin{matrix}x_{1}-x_{3}&x_{2}-x_{3}\\y_{1}-y_{3}&y_{2}-y_{3}\end{matrix}}\right)$

Now the matrix $\mathbf {T}$ is invertible, since $\mathbf {r} _{1}-\mathbf {r} _{3}$ and $\mathbf {r} _{2}-\mathbf {r} _{3}$ are linearly independent (if this were not the case, then $\mathbf {r} _{1}$ , $\mathbf {r} _{2}$ , and $\mathbf {r} _{3}$ would be collinear and would not form a triangle). Thus, we can rearrange the above equation to get

$\left({\begin{matrix}\lambda _{1}\\\lambda _{2}\end{matrix}}\right)=\mathbf {T} ^{-1}(\mathbf {r} -\mathbf {r} _{3})$

Finding the barycentric coordinates has thus been reduced to finding the 2×2 inverse matrix of $\mathbf {T}$ , an easy problem.

Explicitly, the formulae for the barycentric coordinates of point $\mathbf {r}$ in terms of its Cartesian coordinates (*x, y*) and in terms of the Cartesian coordinates of the triangle's vertices are:

${\begin{aligned}\lambda _{1}=&\ {\frac {(y_{2}-y_{3})(x-x_{3})+(x_{3}-x_{2})(y-y_{3})}{\det(\mathbf {T} )}}\\[4pt]&={\frac {(y_{2}-y_{3})(x-x_{3})+(x_{3}-x_{2})(y-y_{3})}{(y_{2}-y_{3})(x_{1}-x_{3})+(x_{3}-x_{2})(y_{1}-y_{3})}}\\[4pt]&={\frac {(\mathbf {r} -\mathbf {r_{3}} )\times (\mathbf {r_{2}} -\mathbf {r_{3}} )}{(\mathbf {r_{1}} -\mathbf {r_{3}} )\times (\mathbf {r_{2}} -\mathbf {r_{3}} )}}\\[12pt]\lambda _{2}=&\ {\frac {(y_{3}-y_{1})(x-x_{3})+(x_{1}-x_{3})(y-y_{3})}{\det(\mathbf {T} )}}\\[4pt]&={\frac {(y_{3}-y_{1})(x-x_{3})+(x_{1}-x_{3})(y-y_{3})}{(y_{2}-y_{3})(x_{1}-x_{3})+(x_{3}-x_{2})(y_{1}-y_{3})}}\\[4pt]&={\frac {(\mathbf {r} -\mathbf {r_{3}} )\times (\mathbf {r_{3}} -\mathbf {r_{1}} )}{(\mathbf {r_{1}} -\mathbf {r_{3}} )\times (\mathbf {r_{2}} -\mathbf {r_{3}} )}}\\[12pt]\lambda _{3}=&\ 1-\lambda _{1}-\lambda _{2}\\[4pt]&=1-{\frac {(\mathbf {r} -\mathbf {r_{3}} )\times (\mathbf {r_{2}} -\mathbf {r_{1}} )}{(\mathbf {r_{1}} -\mathbf {r_{3}} )\times (\mathbf {r_{2}} -\mathbf {r_{3}} )}}\\[4pt]&={\frac {(\mathbf {r} -\mathbf {r_{1}} )\times (\mathbf {r_{1}} -\mathbf {r_{2}} )}{(\mathbf {r_{1}} -\mathbf {r_{3}} )\times (\mathbf {r_{2}} -\mathbf {r_{3}} )}}\end{aligned}}$ When understanding the last line of equation, note the identity $(\mathbf {r_{1}} -\mathbf {r_{3}} )\times (\mathbf {r_{2}} -\mathbf {r_{3}} )=(\mathbf {r_{3}} -\mathbf {r_{1}} )\times (\mathbf {r_{1}} -\mathbf {r_{2}} )$ .

#### Vertex approach

Another way to solve the conversion from Cartesian to barycentric coordinates is to write the relation in the matrix form $\mathbf {R} {\boldsymbol {\lambda }}=\mathbf {r}$ with $\mathbf {R} =\left(\,\mathbf {r} _{1}\,|\,\mathbf {r} _{2}\,|\,\mathbf {r} _{3}\right)$ and ${\boldsymbol {\lambda }}=\left(\lambda _{1},\lambda _{2},\lambda _{3}\right)^{\top },$ i.e. ${\begin{pmatrix}x_{1}&x_{2}&x_{3}\\y_{1}&y_{2}&y_{3}\end{pmatrix}}{\begin{pmatrix}\lambda _{1}\\\lambda _{2}\\\lambda _{3}\end{pmatrix}}={\begin{pmatrix}x\\y\end{pmatrix}}$ To get the unique normalized solution we need to add the condition $\lambda _{1}+\lambda _{2}+\lambda _{3}=1$ . The barycentric coordinates are thus the solution of the linear system $\left({\begin{matrix}1&1&1\\x_{1}&x_{2}&x_{3}\\y_{1}&y_{2}&y_{3}\end{matrix}}\right){\begin{pmatrix}\lambda _{1}\\\lambda _{2}\\\lambda _{3}\end{pmatrix}}=\left({\begin{matrix}1\\x\\y\end{matrix}}\right)$ which is ${\begin{pmatrix}\lambda _{1}\\\lambda _{2}\\\lambda _{3}\end{pmatrix}}={\frac {1}{2A}}{\begin{pmatrix}x_{2}y_{3}-x_{3}y_{2}&y_{2}-y_{3}&x_{3}-x_{2}\\x_{3}y_{1}-x_{1}y_{3}&y_{3}-y_{1}&x_{1}-x_{3}\\x_{1}y_{2}-x_{2}y_{1}&y_{1}-y_{2}&x_{2}-x_{1}\end{pmatrix}}{\begin{pmatrix}1\\x\\y\end{pmatrix}}$ where $2A=\det(1|R)=x_{1}(y_{2}-y_{3})+x_{2}(y_{3}-y_{1})+x_{3}(y_{1}-y_{2})$ is twice the signed area of the triangle. The area interpretation of the barycentric coordinates can be recovered by applying Cramer's rule to this linear system.

### Conversion between barycentric and trilinear coordinates

A point with trilinear coordinates *x* : *y* : *z* has barycentric coordinates *ax* : *by* : *cz* where *a*, *b*, *c* are the side lengths of the triangle. Conversely, a point with barycentrics $\lambda _{1}:\lambda _{2}:\lambda _{3}$ has trilinears $\lambda _{1}/a:\lambda _{2}/b:\lambda _{3}/c.$

### Equations in barycentric coordinates

The three sides *a, b, c* respectively have equations

$\lambda _{1}=0,\quad \lambda _{2}=0,\quad \lambda _{3}=0.$

The equation of a triangle's Euler line is

${\begin{vmatrix}\lambda _{1}&\lambda _{2}&\lambda _{3}\\1&1&1\\\tan A&\tan B&\tan C\end{vmatrix}}=0.$

Using the previously given conversion between barycentric and trilinear coordinates, the various other equations given in Trilinear coordinates#Formulas can be rewritten in terms of barycentric coordinates.

### Distance between points

The displacement vector of two normalized points $P=(p_{1},p_{2},p_{3})$ and $Q=(q_{1},q_{2},q_{3})$ is

${\overset {}{\overrightarrow {PQ}}}=(q_{1}-p_{1},q_{2}-p_{2},q_{3}-p_{3}).$

The distance d between P and Q, or the length of the displacement vector ${\overset {}{\overrightarrow {PQ}}}=(x,y,z),$ is

${\begin{aligned}d^{2}&=|PQ|^{2}\\[2pt]&=-a^{2}yz-b^{2}zx-c^{2}xy\\[4pt]&={\frac {1}{2}}\left[x^{2}(b^{2}+c^{2}-a^{2})+y^{2}(c^{2}+a^{2}-b^{2})+z^{2}(a^{2}+b^{2}-c^{2})\right].\end{aligned}}$

where *a, b, c* are the sidelengths of the triangle. The equivalence of the last two expressions follows from $x+y+z=0,$ which holds because ${\begin{aligned}x+y+z&=(p_{1}-q_{1})+(p_{2}-q_{2})+(p_{3}-q_{3})\\[2pt]&=(p_{1}+p_{2}+p_{3})-(q_{1}+q_{2}+q_{3})\\[2pt]&=1-1=0.\end{aligned}}$

The barycentric coordinates of a point can be calculated based on distances *d**i* to the three triangle vertices by solving the equation $\left({\begin{matrix}-c^{2}&c^{2}&b^{2}-a^{2}\\-b^{2}&c^{2}-a^{2}&b^{2}\\1&1&1\end{matrix}}\right){\boldsymbol {\lambda }}=\left({\begin{matrix}d_{A}^{2}-d_{B}^{2}\\d_{A}^{2}-d_{C}^{2}\\1\end{matrix}}\right).$

### Applications

#### Determining location with respect to a triangle

Although barycentric coordinates are most commonly used to handle points inside a triangle, they can also be used to describe a point outside the triangle. If the point is not inside the triangle, then we can still use the formulas above to compute the barycentric coordinates. However, since the point is outside the triangle, at least one of the coordinates will violate our original assumption that $\lambda _{1...3}\geq 0$ . In fact, given any point in cartesian coordinates, we can use this fact to determine where this point is with respect to a triangle.

If a point lies in the interior of the triangle, all of the Barycentric coordinates lie in the open interval $(0,1).$ If a point lies on an edge of the triangle but not at a vertex, one of the area coordinates $\lambda _{1...3}$ (the one associated with the opposite vertex) is zero, while the other two lie in the open interval $(0,1).$ If the point lies on a vertex, the coordinate associated with that vertex equals 1 and the others equal zero. Finally, if the point lies outside the triangle at least one coordinate is negative.

Summarizing,

Point

$\mathbf {r}$

lies inside the triangle

if and only if

$0<\lambda _{i}<1\;\forall \;i{\text{ in }}{1,2,3}$

.

$\mathbf {r}$ lies on the edge or corner of the triangle if $0\leq \lambda _{i}\leq 1\;\forall \;i{\text{ in }}{1,2,3}$ and $\lambda _{i}=0\;{\text{, for some i in }}{1,2,3}$ .

Otherwise,

$\mathbf {r}$

lies outside the triangle.

In particular, if a point lies on the far side of a line the barycentric coordinate of the point in the triangle that is not on the line will have a negative value.

#### Interpolation on a triangular unstructured grid

If $f(\mathbf {r} _{1}),f(\mathbf {r} _{2}),f(\mathbf {r} _{3})$ are known quantities, but the values of f inside the triangle defined by $\mathbf {r} _{1},\mathbf {r} _{2},\mathbf {r} _{3}$ is unknown, they can be approximated using linear interpolation. Barycentric coordinates provide a convenient way to compute this interpolation. If $\mathbf {r}$ is a point inside the triangle with barycentric coordinates $\lambda _{1}$ , $\lambda _{2}$ , $\lambda _{3}$ , then

$f(\mathbf {r} )\approx \lambda _{1}f(\mathbf {r} _{1})+\lambda _{2}f(\mathbf {r} _{2})+\lambda _{3}f(\mathbf {r} _{3})$

In general, given any unstructured grid or polygon mesh, this kind of technique can be used to approximate the value of f at all points, as long as the function's value is known at all vertices of the mesh. In this case, we have many triangles, each corresponding to a different part of the space. To interpolate a function f at a point $\mathbf {r}$ , first a triangle must be found that contains $\mathbf {r}$ . To do so, $\mathbf {r}$ is transformed into the barycentric coordinates of each triangle. If some triangle is found such that the coordinates satisfy $0\leq \lambda _{i}\leq 1\;\forall \;i{\text{ in }}1,2,3$ , then the point lies in that triangle or on its edge (explained in the previous section). Then the value of $f(\mathbf {r} )$ can be interpolated as described above.

These methods have many applications, such as the finite element method (FEM).

#### Integration over a triangle or tetrahedron

The integral of a function over the domain of the triangle can be annoying to compute in a cartesian coordinate system. One generally has to split the triangle up into two halves, and great messiness follows. Instead, it is often easier to make a change of variables to any two barycentric coordinates, e.g. $\lambda _{1},\lambda _{2}$ . Under this change of variables,

$\int _{T}f(\mathbf {r} )\ d\mathbf {r} =2A\int _{0}^{1}\int _{0}^{1-\lambda _{2}}f(\lambda _{1}\mathbf {r} _{1}+\lambda _{2}\mathbf {r} _{2}+(1-\lambda _{1}-\lambda _{2})\mathbf {r} _{3})\ d\lambda _{1}\ d\lambda _{2}$

where A is the area of the triangle. This result follows from the fact that a rectangle in barycentric coordinates corresponds to a quadrilateral in cartesian coordinates, and the ratio of the areas of the corresponding shapes in the corresponding coordinate systems is given by $2A$ . Similarly, for integration over a tetrahedron, instead of breaking up the integral into two or three separate pieces, one could switch to 3D tetrahedral coordinates under the change of variables

$\int _{T}f(\mathbf {r} )\ d\mathbf {r} =6V\int _{0}^{1}\int _{0}^{1-\lambda _{3}}\int _{0}^{1-\lambda _{2}-\lambda _{3}}f(\lambda _{1}\mathbf {r} _{1}+\lambda _{2}\mathbf {r} _{2}+\lambda _{3}\mathbf {r} _{3}+(1-\lambda _{1}-\lambda _{2}-\lambda _{3})\mathbf {r} _{4})\ d\lambda _{1}\ d\lambda _{2}\ d\lambda _{3}$ where V is the volume of the tetrahedron.

This approach can be generalized to higher dimensions, to integrate over any n-dimensional simplex.

### Examples of special points

In the homogeneous barycentric coordinate system defined with respect to a triangle $ABC$ , the following statements about special points of $ABC$ hold.

Normalizing coordinates at vertices, the three vertices A, B, and C have coordinates:

${\begin{array}{rccccc}A=&1&:&0&:&0\\B=&0&:&1&:&0\\C=&0&:&0&:&1\end{array}}$

The centroid would be at ${\tfrac {1}{3}}:{\tfrac {1}{3}}:{\tfrac {1}{3}}$ .

If a, b, c are the edge lengths $BC$ , $CA$ , $AB$ respectively, $\alpha$ , $\beta$ , $\gamma$ are the angle measures $\angle CAB$ , $\angle ABC$ , and $\angle BCA$ respectively, and s is the semiperimeter of $ABC$ , then the following statements about special points of $ABC$ hold in addition.

The circumcenter has coordinates

${\begin{array}{rccccc}&\sin 2\alpha &:&\sin 2\beta &:&\sin 2\gamma \\[2pt]=&1-\cot \beta \cot \gamma &:&1-\cot \gamma \cot \alpha &:&1-\cot \alpha \cot \beta \\[2pt]=&a^{2}(-a^{2}+b^{2}+c^{2})&:&b^{2}(a^{2}-b^{2}+c^{2})&:&c^{2}(a^{2}+b^{2}-c^{2})\end{array}}$

The orthocenter has coordinates

${\begin{array}{rccccc}&\tan \alpha &:&\tan \beta &:&\tan \gamma \\[2pt]=&a\cos \beta \cos \gamma &:&b\cos \gamma \cos \alpha &:&c\cos \alpha \cos \beta \\[2pt]=&(a^{2}+b^{2}-c^{2})(a^{2}-b^{2}+c^{2})&:&(-a^{2}+b^{2}+c^{2})(a^{2}+b^{2}-c^{2})&:&(a^{2}-b^{2}+c^{2})(-a^{2}+b^{2}+c^{2})\end{array}}$

The incenter has coordinates ${\displaystyle a:b:c=\sin \alpha$

The excenters have coordinates

${\begin{array}{rrcrcr}J_{A}=&-a&:&b&:&c\\J_{B}=&a&:&-b&:&c\\J_{C}=&a&:&b&:&-c\end{array}}$

The nine-point center has coordinates

${\begin{array}{rccccc}&a\cos(\beta -\gamma )&:&b\cos(\gamma -\alpha )&:&c\cos(\alpha -\beta )\\[4pt]=&1+\cot \beta \cot \gamma &:&1+\cot \gamma \cot \alpha &:&1+\cot \alpha \cot \beta \\[4pt]=&a^{2}(b^{2}+c^{2})-(b^{2}-c^{2})^{2}&:&b^{2}(c^{2}+a^{2})-(c^{2}-a^{2})^{2}&:&c^{2}(a^{2}+b^{2})-(a^{2}-b^{2})^{2}\end{array}}$

The Gergonne point has coordinates $(s-b)(s-c):(s-c)(s-a):(s-a)(s-b)$ .

The Nagel point has coordinates $s-a:s-b:s-c$ .

The symmedian point has coordinates $a^{2}:b^{2}:c^{2}$ .

## Barycentric coordinates on tetrahedra

Barycentric coordinates may be easily extended to three dimensions. The 3D simplex is a tetrahedron, a polyhedron having four triangular faces and four vertices. Once again, the four barycentric coordinates are defined so that the first vertex $\mathbf {r} _{1}$ maps to barycentric coordinates $\lambda =(1,0,0,0)$ , $\mathbf {r} _{2}\to (0,1,0,0)$ , etc.

This is again a linear transformation, and we may extend the above procedure for triangles to find the barycentric coordinates of a point $\mathbf {r}$ with respect to a tetrahedron:

$\left({\begin{matrix}\lambda _{1}\\\lambda _{2}\\\lambda _{3}\end{matrix}}\right)=\mathbf {T} ^{-1}(\mathbf {r} -\mathbf {r} _{4})$

where $\mathbf {T}$ is now a 3×3 matrix:

$\mathbf {T} =\left({\begin{matrix}x_{1}-x_{4}&x_{2}-x_{4}&x_{3}-x_{4}\\y_{1}-y_{4}&y_{2}-y_{4}&y_{3}-y_{4}\\z_{1}-z_{4}&z_{2}-z_{4}&z_{3}-z_{4}\end{matrix}}\right)$

and $\lambda _{4}=1-\lambda _{1}-\lambda _{2}-\lambda _{3}$ with the corresponding Cartesian coordinates: ${\begin{aligned}x&=\lambda _{1}x_{1}+\lambda _{2}x_{2}+\lambda _{3}x_{3}+(1-\lambda _{1}-\lambda _{2}-\lambda _{3})x_{4}\\y&=\lambda _{1}y_{1}+\,\lambda _{2}y_{2}+\lambda _{3}y_{3}+(1-\lambda _{1}-\lambda _{2}-\lambda _{3})y_{4}\\z&=\lambda _{1}z_{1}+\,\lambda _{2}z_{2}+\lambda _{3}z_{3}+(1-\lambda _{1}-\lambda _{2}-\lambda _{3})z_{4}\end{aligned}}$ Once again, the problem of finding the barycentric coordinates has been reduced to inverting a 3×3 matrix.

3D barycentric coordinates may be used to decide if a point lies inside a tetrahedral volume, and to interpolate a function within a tetrahedral mesh, in an analogous manner to the 2D procedure. Tetrahedral meshes are often used in finite element analysis because the use of barycentric coordinates can greatly simplify 3D interpolation.

## Generalized barycentric coordinates

Barycentric coordinates $(\lambda _{1},\lambda _{2},...,\lambda _{k})$ of a point $p\in \mathbb {R} ^{n}$ that are defined with respect to a finite set of *k* points $x_{1},x_{2},...,x_{k}\in \mathbb {R} ^{n}$ instead of a simplex are called **generalized barycentric coordinates**. For these, the equation

$(\lambda _{1}+\lambda _{2}+\cdots +\lambda _{k})p=\lambda _{1}x_{1}+\lambda _{2}x_{2}+\cdots +\lambda _{k}x_{k}$

is still required to hold. Usually one uses normalized coordinates, $\lambda _{1}+\lambda _{2}+\cdots +\lambda _{k}=1$ . As for the case of a simplex, the points with nonnegative normalized generalized coordinates ( $0\leq \lambda _{i}\leq 1$ ) form the convex hull of *x*1, ..., *x**n*. If there are more points than in a full simplex ( $k>n+1$ ) the generalized barycentric coordinates of a point are *not* unique, as the defining linear system (here for n=2) $\left({\begin{matrix}1&1&1&...\\x_{1}&x_{2}&x_{3}&...\\y_{1}&y_{2}&y_{3}&...\end{matrix}}\right){\begin{pmatrix}\lambda _{1}\\\lambda _{2}\\\lambda _{3}\\\vdots \end{pmatrix}}=\left({\begin{matrix}1\\x\\y\end{matrix}}\right)$ is underdetermined. The simplest example is a quadrilateral in the plane. Various kinds of additional restrictions can be used to define unique barycentric coordinates.

### Abstraction

More abstractly, generalized barycentric coordinates express a convex polytope with *n* vertices, regardless of dimension, as the *image* of the standard $(n-1)$ -simplex, which has *n* vertices – the map is onto: $\Delta ^{n-1}\twoheadrightarrow P.$ The map is one-to-one if and only if the polytope is a simplex, in which case the map is an isomorphism; this corresponds to a point not having *unique* generalized barycentric coordinates except when P is a simplex.

Dual to generalized barycentric coordinates are slack variables, which measure by how much margin a point satisfies the linear constraints, and gives an embedding $P\hookrightarrow (\mathbf {R} _{\geq 0})^{f}$ into the *f*-orthant, where *f* is the number of faces (dual to the vertices). This map is one-to-one (slack variables are uniquely determined) but not onto (not all combinations can be realized).

This use of the standard $(n-1)$ -simplex and *f*-orthant as standard objects that map to a polytope or that a polytope maps into should be contrasted with the use of the standard vector space $K^{n}$ as the standard object for vector spaces, and the standard affine hyperplane $\{(x_{0},\ldots ,x_{n})\mid \sum x_{i}=1\}\subset K^{n+1}$ as the standard object for affine spaces, where in each case choosing a linear basis or affine basis provides an *isomorphism,* allowing all vector spaces and affine spaces to be thought of in terms of these standard spaces, rather than an onto or one-to-one map (not every polytope is a simplex). Further, the *n*-orthant is the standard object that maps *to* cones.

### Applications

Generalized barycentric coordinates have applications in computer graphics and more specifically in geometric modelling. Often, a three-dimensional model can be approximated by a polyhedron such that the generalized barycentric coordinates with respect to that polyhedron have a geometric meaning. In this way, the processing of the model can be simplified by using these meaningful coordinates. Barycentric coordinates are also used in geophysics.
