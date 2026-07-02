---
title: "Backfitting algorithm"
source: https://en.wikipedia.org/wiki/Backfitting_algorithm
domain: generalized-additive-models
license: CC-BY-SA-4.0
tags: generalized additive model, backfitting, smoothing spline, kernel smoother
fetched: 2026-07-02
---

# Backfitting algorithm

In statistics, the **backfitting algorithm** is a simple iterative procedure used to fit a generalized additive model. It was introduced in 1985 by Leo Breiman and Jerome Friedman along with generalized additive models. In most cases, the backfitting algorithm is equivalent to the Gauss–Seidel method, an algorithm used for solving a certain linear system of equations.

## Algorithm

Additive models are a class of non-parametric regression models of the form:

$Y_{i}=\alpha +\sum _{j=1}^{p}f_{j}(X_{ij})+\epsilon _{i}$

where each $X_{1},X_{2},\ldots ,X_{p}$ is a variable in our p -dimensional predictor X , and Y is our outcome variable. $\epsilon$ represents our inherent error, which is assumed to have mean zero. The $f_{j}$ represent unspecified smooth functions of a single $X_{j}$ . Given the flexibility in the $f_{j}$ , we typically do not have a unique solution: $\alpha$ is left unidentifiable as one can add any constants to any of the $f_{j}$ and subtract this value from $\alpha$ . It is common to rectify this by constraining

$\sum _{i=1}^{N}f_{j}(X_{ij})=0$

for all

j

leaving

$\alpha =1/N\sum _{i=1}^{N}y_{i}$

necessarily.

The backfitting algorithm is then:

```
   Initialize 
  
    
      
        
          
            
              α
              ^
            
          
        
        =
        1
        
          /
        
        N
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        
          y
          
            i
          
        
        ,
        
          
            
              
                f
                
                  j
                
              
              ^
            
          
        
        ≡
        0
      
    
    {\displaystyle {\hat {\alpha }}=1/N\sum _{i=1}^{N}y_{i},{\hat {f_{j}}}\equiv 0}
  
,
  
    
      
        ∀
        j
      
    
    {\displaystyle \forall j}
  

   Do until 
  
    
      
        
          
            
              
                f
                
                  j
                
              
              ^
            
          
        
      
    
    {\displaystyle {\hat {f_{j}}}}
  
 converge:
       For each predictor j:
           (a) 
  
    
      
        
          
            
              
                f
                
                  j
                
              
              ^
            
          
        
        ←
        
          Smooth
        
        [
        {
        
          y
          
            i
          
        
        −
        
          
            
              α
              ^
            
          
        
        −
        
          ∑
          
            k
            ≠
            j
          
        
        
          
            
              
                f
                
                  k
                
              
              ^
            
          
        
        (
        
          x
          
            i
            k
          
        
        )
        
          }
          
            1
          
          
            N
          
        
        ]
      
    
    {\displaystyle {\hat {f_{j}}}\leftarrow {\text{Smooth}}[\lbrace y_{i}-{\hat {\alpha }}-\sum _{k\neq j}{\hat {f_{k}}}(x_{ik})\rbrace _{1}^{N}]}
  
 (backfitting step)
           (b) 
  
    
      
        
          
            
              
                f
                
                  j
                
              
              ^
            
          
        
        ←
        
          
            
              
                f
                
                  j
                
              
              ^
            
          
        
        −
        1
        
          /
        
        N
        
          ∑
          
            i
            =
            1
          
          
            N
          
        
        
          
            
              
                f
                
                  j
                
              
              ^
            
          
        
        (
        
          x
          
            i
            j
          
        
        )
      
    
    {\displaystyle {\hat {f_{j}}}\leftarrow {\hat {f_{j}}}-1/N\sum _{i=1}^{N}{\hat {f_{j}}}(x_{ij})}
  
 (mean centering of estimated function)
```

where ${\text{Smooth}}$ is our smoothing operator. This is typically chosen to be a cubic spline smoother but can be any other appropriate fitting operation, such as:

- local polynomial regression
- kernel smoothing methods
- more complex operators, such as surface smoothers for second and higher-order interactions

In theory, step **(b)** in the algorithm is not needed as the function estimates are constrained to sum to zero. However, due to numerical issues this might become a problem in practice.

## Motivation

If we consider the problem of minimizing the expected squared error:

$\min _{\alpha ,f_{j}}\ \mathbb {E} [(Y-\alpha -\sum _{j=1}^{p}f_{j}(X_{j}))^{2}]$

There exists a unique solution by the theory of projections given by:

$f_{i}(X_{i})=\mathbb {E} [Y-\alpha -\sum _{j\neq i}^{p}f_{j}(X_{j})\mid X_{i}]$

for *i* = 1, 2, ..., *p*.

This gives the matrix interpretation:

${\begin{pmatrix}I&P_{1}&\cdots &P_{1}\\P_{2}&I&\cdots &P_{2}\\\vdots &&\ddots &\vdots \\P_{p}&\cdots &P_{p}&I\end{pmatrix}}{\begin{pmatrix}f_{1}(X_{1})\\f_{2}(X_{2})\\\vdots \\f_{p}(X_{p})\end{pmatrix}}={\begin{pmatrix}P_{1}Y\\P_{2}Y\\\vdots \\P_{p}Y\end{pmatrix}}$

where $P_{i}(\cdot )=\mathbb {E} (\cdot |X_{i})$ . In this context we can imagine a smoother matrix, $S_{i}$ , which approximates our $P_{i}$ and gives an estimate, $S_{i}Y$ , of $\mathbb {E} (Y|X)$

${\begin{pmatrix}I&S_{1}&\cdots &S_{1}\\S_{2}&I&\cdots &S_{2}\\\vdots &&\ddots &\vdots \\S_{p}&\cdots &S_{p}&I\end{pmatrix}}{\begin{pmatrix}f_{1}\\f_{2}\\\vdots \\f_{p}\end{pmatrix}}={\begin{pmatrix}S_{1}Y\\S_{2}Y\\\vdots \\S_{p}Y\end{pmatrix}}$

or in abbreviated form

${\hat {S}}f=QY\,$

An exact solution of this is infeasible to calculate for large *np*, so the iterative technique of backfitting is used. We take initial guesses $f_{j}^{(0)}$ and update each $f_{j}^{(\ell )}$ in turn to be the smoothed fit for the residuals of all the others:

${\hat {f_{j}}}^{(\ell )}\leftarrow {\text{Smooth}}[\lbrace y_{i}-{\hat {\alpha }}-\sum _{k\neq j}{\hat {f_{k}}}(x_{ik})\rbrace _{1}^{N}]$

Looking at the abbreviated form it is easy to see the backfitting algorithm as equivalent to the Gauss–Seidel method for linear smoothing operators *S*.

## Explicit derivation for two dimensions

Following, we can formulate the backfitting algorithm explicitly for the two dimensional case. We have:

$f_{1}=S_{1}(Y-f_{2}),f_{2}=S_{2}(Y-f_{1})$

If we denote ${\hat {f}}_{1}^{(i)}$ as the estimate of $f_{1}$ in the *i*th updating step, the backfitting steps are

${\hat {f}}_{1}^{(i)}=S_{1}[Y-{\hat {f}}_{2}^{(i-1)}],{\hat {f}}_{2}^{(i)}=S_{2}[Y-{\hat {f}}_{1}^{(i)}]$

By induction we get

${\hat {f}}_{1}^{(i)}=Y-\sum _{\alpha =0}^{i-1}(S_{1}S_{2})^{\alpha }(I-S_{1})Y-(S_{1}S_{2})^{i-1}S_{1}{\hat {f}}_{2}^{(0)}$

and

${\hat {f}}_{2}^{(i)}=S_{2}\sum _{\alpha =0}^{i-1}(S_{1}S_{2})^{\alpha }(I-S_{1})Y+S_{2}(S_{1}S_{2})^{i-1}S_{1}{\hat {f}}_{2}^{(0)}$

If we set ${\hat {f}}_{2}^{(0)}=0$ then we get

${\hat {f}}_{1}^{(i)}=Y-S_{2}^{-1}{\hat {f}}_{2}^{(i)}=[I-\sum _{\alpha =0}^{i-1}(S_{1}S_{2})^{\alpha }(I-S_{1})]Y$

${\hat {f}}_{2}^{(i)}=[S_{2}\sum _{\alpha =0}^{i-1}(S_{1}S_{2})^{\alpha }(I-S_{1})]Y$

Where we have solved for ${\hat {f}}_{1}^{(i)}$ by directly plugging out from $f_{2}=S_{2}(Y-f_{1})$ .

We have convergence if $\|S_{1}S_{2}\|<1$ . In this case, letting ${\hat {f}}_{1}^{(i)},{\hat {f}}_{2}^{(i)}{\xrightarrow {}}{\hat {f}}_{1}^{(\infty )},{\hat {f}}_{2}^{(\infty )}$ :

${\hat {f}}_{1}^{(\infty )}=Y-S_{2}^{-1}{\hat {f}}_{2}^{(\infty )}=Y-(I-S_{1}S_{2})^{-1}(I-S_{1})Y$

${\hat {f}}_{2}^{(\infty )}=S_{2}(I-S_{1}S_{2})^{-1}(I-S_{1})Y$

We can check this is a solution to the problem, i.e. that ${\hat {f}}_{1}^{(i)}$ and ${\hat {f}}_{2}^{(i)}$ converge to $f_{1}$ and $f_{2}$ correspondingly, by plugging these expressions into the original equations.

## Issues

The choice of when to stop the algorithm is arbitrary and it is hard to know a priori how long reaching a specific convergence threshold will take. Also, the final model depends on the order in which the predictor variables $X_{i}$ are fit.

As well, the solution found by the backfitting procedure is non-unique. If b is a vector such that ${\hat {S}}b=0$ from above, then if ${\hat {f}}$ is a solution then so is ${\hat {f}}+\alpha b$ is also a solution for any $\alpha \in \mathbb {R}$ . A modification of the backfitting algorithm involving projections onto the eigenspace of *S* can remedy this problem.

## Modified algorithm

We can modify the backfitting algorithm to make it easier to provide a unique solution. Let ${\mathcal {V}}_{1}(S_{i})$ be the space spanned by all the eigenvectors of *S*i that correspond to eigenvalue 1. Then any *b* satisfying ${\hat {S}}b=0$ has $b_{i}\in {\mathcal {V}}_{1}(S_{i})\forall i=1,\dots ,p$ and $\sum _{i=1}^{p}b_{i}=0.$ Now if we take A to be a matrix that projects orthogonally onto ${\mathcal {V}}_{1}(S_{1})+\dots +{\mathcal {V}}_{1}(S_{p})$ , we get the following modified backfitting algorithm:

```
   Initialize 
  
    
      
        
          
            
              α
              ^
            
          
        
        =
        1
        
          /
        
        N
        
          ∑
          
            1
          
          
            N
          
        
        
          y
          
            i
          
        
        ,
        
          
            
              
                f
                
                  j
                
              
              ^
            
          
        
        ≡
        0
      
    
    {\displaystyle {\hat {\alpha }}=1/N\sum _{1}^{N}y_{i},{\hat {f_{j}}}\equiv 0}
  
,
  
    
      
        ∀
        i
        ,
        j
      
    
    {\displaystyle \forall i,j}
  
, 
  
    
      
        
          
            
              
                f
                
                  +
                
              
              ^
            
          
        
        =
        α
        +
        
          
            
              
                f
                
                  1
                
              
              ^
            
          
        
        +
        ⋯
        +
        
          
            
              
                f
                
                  p
                
              
              ^
            
          
        
      
    
    {\displaystyle {\hat {f_{+}}}=\alpha +{\hat {f_{1}}}+\dots +{\hat {f_{p}}}}
  

   Do until 
  
    
      
        
          
            
              
                f
                
                  j
                
              
              ^
            
          
        
      
    
    {\displaystyle {\hat {f_{j}}}}
  
 converge:
       Regress 
  
    
      
        y
        −
        
          
            
              
                f
                
                  +
                
              
              ^
            
          
        
      
    
    {\displaystyle y-{\hat {f_{+}}}}
  
 onto the space 
  
    
      
        
          
            
              V
            
          
          
            1
          
        
        (
        
          S
          
            i
          
        
        )
        +
        ⋯
        +
        
          
            
              V
            
          
          
            1
          
        
        (
        
          S
          
            p
          
        
        )
      
    
    {\displaystyle {\mathcal {V}}_{1}(S_{i})+\dots +{\mathcal {V}}_{1}(S_{p})}
  
, setting 
  
    
      
        a
        =
        A
        (
        Y
        −
        
          
            
              
                f
                
                  +
                
              
              ^
            
          
        
        )
      
    
    {\displaystyle a=A(Y-{\hat {f_{+}}})}
  

       For each predictor j:
           Apply backfitting update to 
  
    
      
        (
        Y
        −
        a
        )
      
    
    {\displaystyle (Y-a)}
  
 using the smoothing operator 
  
    
      
        (
        I
        −
        
          A
          
            i
          
        
        )
        
          S
          
            i
          
        
      
    
    {\displaystyle (I-A_{i})S_{i}}
  
, yielding new estimates for 
  
    
      
        
          
            
              
                f
                
                  j
                
              
              ^
            
          
        
      
    
    {\displaystyle {\hat {f_{j}}}}
  
```
