---
title: "Karmarkar's algorithm"
source: https://en.wikipedia.org/wiki/Karmarkar's_algorithm
domain: karmarkar-interior-point
license: CC-BY-SA-4.0
tags: karmarkar algorithm, interior point method, projective scaling, polynomial linear programming
fetched: 2026-07-02
---

# Karmarkar's algorithm

**Karmarkar's algorithm** is an algorithm introduced by Narendra Karmarkar in 1984 for solving linear programming problems. It was the first reasonably efficient algorithm that solves these problems in polynomial time. The ellipsoid method is also polynomial time but proved to be inefficient in practice.

Denoting by n the number of variables, *m* the number of inequality constraints, and L the number of bits of input to the algorithm, Karmarkar's algorithm requires $O(m^{1.5}n^{2}L)$ operations on $O(L)$ -digit numbers, as compared to $O(n^{3}(n+m)L)$ such operations for the ellipsoid algorithm. In "square" problems, when *m* is in O(*n*), Karmarkar's algorithm requires $O(n^{3.5}L)$ operations on $O(L)$ -digit numbers, as compared to $O(n^{4}L)$ such operations for the ellipsoid algorithm. The runtime of Karmarkar's algorithm is thus $O(n^{3.5}L^{2}\cdot \log L\cdot \log \log L),$ using FFT-based multiplication (see Big O notation).

Karmarkar's algorithm falls within the class of interior-point methods: the current guess for the solution does not follow the boundary of the feasible set as in the simplex method, but moves through the interior of the feasible region, improving the approximation of the optimal solution by a definite fraction with every iteration and converging to an optimal solution with rational data.

## The algorithm

Consider a linear programming problem in matrix form:

| maximize *c*T*x* |   |
|---|---|
| subject to | *Ax* ≤ *b*. |

Karmarkar's algorithm determines the next feasible direction toward optimality and scales back by a factor 0 < γ ≤ 1. It is described in a number of sources. Karmarkar also has extended the method to solve problems with integer constraints and non-convex problems.

```
Algorithm Affine-Scaling
```

Since the actual algorithm is rather complicated, researchers looked for a more intuitive version of it, and in 1985 developed affine scaling, a version of Karmarkar's algorithm that uses affine transformations where Karmarkar used projective ones, only to realize four years later that they had rediscovered an algorithm published by Soviet mathematician I. I. Dikin in 1967. The affine-scaling method can be described succinctly as follows. While applicable to small scale problems, it is not a polynomial time algorithm.

```
Input:  A, b, c, 
  
    
      
        
          x
          
            0
          
        
      
    
    {\displaystyle x^{0}}
  
, stopping criterion, γ.
```

```
  
    
      
        k
        ←
        0
      
    
    {\displaystyle k\leftarrow 0}
  

do while stopping criterion not satisfied
    
  
    
      
        
          v
          
            k
          
        
        ←
        b
        −
        A
        
          x
          
            k
          
        
      
    
    {\displaystyle v^{k}\leftarrow b-Ax^{k}}
  

    
  
    
      
        
          D
          
            v
          
        
        ←
        diag
        ⁡
        (
        
          v
          
            1
          
          
            k
          
        
        ,
        …
        ,
        
          v
          
            m
          
          
            k
          
        
        )
      
    
    {\displaystyle D_{v}\leftarrow \operatorname {diag} (v_{1}^{k},\ldots ,v_{m}^{k})}
  

    
  
    
      
        
          h
          
            x
          
        
        ←
        (
        
          A
          
            T
          
        
        
          D
          
            v
          
          
            −
            2
          
        
        A
        
          )
          
            −
            1
          
        
        c
      
    
    {\displaystyle h_{x}\leftarrow (A^{T}D_{v}^{-2}A)^{-1}c}
  

    
  
    
      
        
          h
          
            v
          
        
        ←
        −
        A
        
          h
          
            x
          
        
      
    
    {\displaystyle h_{v}\leftarrow -Ah_{x}}
  

    if 
  
    
      
        
          h
          
            v
          
        
        ≥
        0
      
    
    {\displaystyle h_{v}\geq 0}
  
 then
        return unbounded
    end if
    
  
    
      
        α
        ←
        γ
        ⋅
        min
        {
        −
        
          v
          
            i
          
          
            k
          
        
        
          /
        
        (
        
          h
          
            v
          
        
        
          )
          
            i
          
        
        
        
        
          |
        
        
        
        (
        
          h
          
            v
          
        
        
          )
          
            i
          
        
        <
        0
        ,
        
        i
        =
        1
        ,
        …
        ,
        m
        }
      
    
    {\displaystyle \alpha \leftarrow \gamma \cdot \min\{-v_{i}^{k}/(h_{v})_{i}\,\,|\,\,(h_{v})_{i}<0,\,i=1,\ldots ,m\}}
  

    
  
    
      
        
          x
          
            k
            +
            1
          
        
        ←
        
          x
          
            k
          
        
        +
        α
        
          h
          
            x
          
        
      
    
    {\displaystyle x^{k+1}\leftarrow x^{k}+\alpha h_{x}}
  

    
  
    
      
        k
        ←
        k
        +
        1
      
    
    {\displaystyle k\leftarrow k+1}
  

end do
```

- "←" denotes assignment. For instance, "*largest* ← *item*" means that the value of *largest* changes to the value of *item*.
- "**return**" terminates the algorithm and outputs the following value.

## Example

Consider the linear program ${\begin{array}{lrclr}{\text{maximize}}&x_{1}+x_{2}\\{\text{subject to}}&2px_{1}+x_{2}&\leq &p^{2}+1,&p=0.0,0.1,0.2,\ldots ,0.9,1.0.\end{array}}$ That is, there are 2 variables $x_{1},x_{2}$ and 11 constraints associated with varying values of p . This figure shows each iteration of the algorithm as red circle points. The constraints are shown as blue lines.

## Patent controversy

At the time he invented the algorithm, Karmarkar was employed by IBM as a postdoctoral fellow in the IBM San Jose Research Laboratory in California. On August 11, 1983 he gave a seminar at Stanford University explaining the algorithm, with his affiliation still listed as IBM. By the fall of 1983 Karmarkar started to work at AT&T and submitted his paper to the 1984 ACM Symposium on Theory of Computing (STOC, held April 30 - May 2, 1984) stating AT&T Bell Laboratories as his affiliation. After applying the algorithm to optimizing AT&T's telephone network, they realized that his invention could be of practical importance. In April 1985, AT&T promptly applied for a patent on his algorithm.

The patent became more fuel for the ongoing controversy over the issue of software patents. This left many mathematicians uneasy, such as Ronald Rivest (himself one of the holders of the patent on the RSA algorithm), who expressed the opinion that research proceeded on the basis that algorithms should be free. Even before the patent was actually granted, it was argued that there might have been prior art that was applicable. Mathematicians who specialized in numerical analysis, including Philip Gill and others, claimed that Karmarkar's algorithm is equivalent to a projected Newton barrier method with a logarithmic barrier function, if the parameters are chosen suitably. Legal scholar Andrew Chin opines that Gill's argument was flawed, insofar as the method they describe does not constitute an "algorithm", since it requires choices of parameters that don't follow from the internal logic of the method, but rely on external guidance, essentially from Karmarkar's algorithm. Furthermore, Karmarkar's contributions are considered far from obvious in light of all prior work, including Fiacco-McCormick, Gill and others cited by Saltzman. The patent was granted in recognition of the essential originality of Karmarkar's work, as U.S. patent 4,744,028: "Methods and apparatus for efficient resource allocation" in May 1988.

AT&T designed a vector multi-processor computer system specifically to run Karmarkar's algorithm, calling the resulting combination of hardware and software KORBX, and marketed this system at a price of US$8.9 million. Its first customer was the Pentagon.

Opponents of software patents have further argued that the patents ruined the positive interaction cycles that previously characterized the relationship between researchers in linear programming and industry, and specifically it isolated Karmarkar himself from the network of mathematical researchers in his field.

The patent itself expired in April 2006, and the algorithm is presently in the public domain.

The United States Supreme Court has held that mathematics cannot be patented in *Gottschalk v. Benson*, In that case, the Court first addressed whether computer algorithms could be patented and it held that they could not because the patent system does not protect ideas and similar abstractions. In *Diamond v. Diehr*, the Supreme Court stated, "A mathematical formula as such is not accorded the protection of our patent laws, and this principle cannot be circumvented by attempting to limit the use of the formula to a particular technological environment. In *Mayo Collaborative Services v. Prometheus Labs., Inc.*, the Supreme Court explained further that "simply implementing a mathematical principle on a physical machine, namely a computer, [i]s not a patentable application of that principle."

## Applications

Karmarkar's algorithm was used by the US Army for logistic planning during the Gulf War.
