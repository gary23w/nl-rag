---
title: "Successive over-relaxation"
source: https://en.wikipedia.org/wiki/Successive_over-relaxation
domain: multigrid-methods
license: CC-BY-SA-4.0
tags: multigrid method, gauss-seidel method, successive over-relaxation, domain decomposition
fetched: 2026-07-02
---

# Successive over-relaxation

In numerical linear algebra, the method of **successive over-relaxation** (**SOR**) is a variant of the Gauss–Seidel method for solving a linear system of equations, resulting in faster convergence. A similar method can be used for any slowly converging iterative process.

It was devised simultaneously by David M. Young Jr. and by Stanley P. Frankel in 1950 for the purpose of automatically solving linear systems on digital computers. Over-relaxation methods had been used before the work of Young and Frankel. An example is the method of Lewis Fry Richardson, and the methods developed by R. V. Southwell. However, these methods were designed for computation by human calculators, requiring some expertise to ensure convergence to the solution which made them inapplicable for programming on digital computers. These aspects are discussed in the thesis of David M. Young Jr.

## Formulation

Given a square system of *n* linear equations with unknown **x**:

$A\mathbf {x} =\mathbf {b}$

where:

${\begin{aligned}&A={\begin{bmatrix}a_{11}&a_{12}&\cdots &a_{1n}\\a_{21}&a_{22}&\cdots &a_{2n}\\\vdots &\vdots &\ddots &\vdots \\a_{n1}&a_{n2}&\cdots &a_{nn}\end{bmatrix}},\\[1ex]&\mathbf {x} ={\begin{bmatrix}x_{1}\\x_{2}\\\vdots \\x_{n}\end{bmatrix}},\qquad \mathbf {b} ={\begin{bmatrix}b_{1}\\b_{2}\\\vdots \\b_{n}\end{bmatrix}}.\end{aligned}}$

Then *A* can be decomposed into a diagonal component *D*, and strictly lower and upper triangular components *L* and *U*:

$A=D+L+U,$ where $D={\begin{bmatrix}a_{11}&0&\cdots &0\\0&a_{22}&\cdots &0\\\vdots &\vdots &\ddots &\vdots \\0&0&\cdots &a_{nn}\end{bmatrix}},\quad L={\begin{bmatrix}0&0&\cdots &0\\a_{21}&0&\cdots &0\\\vdots &\vdots &\ddots &\vdots \\a_{n1}&a_{n2}&\cdots &0\end{bmatrix}},\quad U={\begin{bmatrix}0&a_{12}&\cdots &a_{1n}\\0&0&\cdots &a_{2n}\\\vdots &\vdots &\ddots &\vdots \\0&0&\cdots &0\end{bmatrix}}.$

The system of linear equations may be rewritten as:

$\left(D+\omega L\right)\mathbf {x} =\omega \mathbf {b} -\left[\omega U+\left(\omega -1\right)D\right]\mathbf {x}$

for a constant *ω* > 1, called the *relaxation factor*.

The method of successive over-relaxation is an iterative technique that solves the left hand side of this expression for **x**, using the previous value for **x** on the right hand side. Analytically, this may be written as:

${\begin{aligned}\mathbf {x} ^{(k+1)}&=\left(D+\omega L\right)^{-1}\left(\omega \mathbf {b} -\left[\omega U+\left(\omega -1\right)D\right]\mathbf {x} ^{(k)}\right)\\&=L_{\omega }\mathbf {x} ^{(k)}+\mathbf {c} ,\end{aligned}}$

where $\mathbf {x} ^{(k)}$ is the *k*th approximation or iteration of $\mathbf {x}$ and $\mathbf {x} ^{(k+1)}$ is the next or *k* + 1 iteration of $\mathbf {x}$ . However, by taking advantage of the triangular form of (*D*+*ωL*), the elements of **x**(*k*+1) can be computed sequentially using forward substitution:

$x_{i}^{(k+1)}=\left(1-\omega \right)x_{i}^{(k)}+{\frac {\omega }{a_{ii}}}\left(b_{i}-\sum _{j<i}a_{ij}x_{j}^{(k+1)}-\sum _{j>i}a_{ij}x_{j}^{(k)}\right),\quad i=1,2,\ldots ,n.$

This can again be written analytically in matrix-vector form without the need of inverting the matrix $(D+\omega L)$ :

$\mathbf {x} ^{(k+1)}=\left(1-\omega \right)\mathbf {x} ^{(k)}+\omega D^{-1}\left(\mathbf {b} -L\mathbf {x} ^{(k+1)}-U\mathbf {x} ^{(k)}\right).$

## Convergence

The choice of relaxation factor *ω* is not necessarily easy, and depends upon the properties of the coefficient matrix. In 1947, Ostrowski proved that if A is symmetric and positive-definite then $\rho (L_{\omega })<1$ for $0<\omega <2$ . Thus, convergence of the iteration process follows, but we are generally interested in faster convergence rather than just convergence.

### Convergence Rate

The convergence rate for the SOR method can be analytically derived. One needs to assume the following

- the relaxation parameter is appropriate: $\omega \in (0,2)$
- Jacobi's iteration matrix $C_{\text{Jac}}:=I-D^{-1}A$ has only real eigenvalues
- Jacobi's method is convergent: $\mu :=\rho (C_{\text{Jac}})<1$
- the matrix decomposition $A=D+L+U$ satisfies the property that $\det \left(\lambda D+zL+{\tfrac {1}{z}}U\right)=\det \left(\lambda D+L+U\right)$ for any $z\in \mathbb {C} \setminus \{0\}$ and $\lambda \in \mathbb {C}$ .

Then the convergence rate can be expressed as $\rho (C_{\omega })={\begin{cases}{\frac {1}{4}}\left[\omega \mu +{\sqrt {\omega ^{2}\mu ^{2}-4(\omega -1)}}\right]^{2}\,,&0<\omega \leq \omega _{\text{opt}}\\[1ex]\omega -1\,,&\omega _{\text{opt}}<\omega <2\end{cases}}$ where the optimal relaxation parameter is given by $\omega _{\text{opt}}:=1+\left({\frac {\mu }{1+{\sqrt {1-\mu ^{2}}}}}\right)^{2}=1+{\frac {\mu ^{2}}{4}}+O(\mu ^{3})\,.$ In particular, for $\omega =1$ (Gauss-Seidel) it holds that $\rho (C_{\omega })=\mu ^{2}=\rho (C_{\text{Jac}})^{2}$ . For the optimal $\omega$ we get $\rho (C_{\omega })={\frac {1-{\sqrt {1-\mu ^{2}}}}{1+{\sqrt {1-\mu ^{2}}}}}={\frac {\mu ^{2}}{4}}+O(\mu ^{3})$ , which shows SOR is roughly four times more efficient than Gauss–Seidel.

The last assumption is satisfied for tridiagonal matrices since $Z(\lambda D+L+U)Z^{-1}=\lambda D+zL+{\tfrac {1}{z}}U$ for diagonal Z with entries $Z_{ii}=z^{i-1}$ and $\det \left(\lambda D+L+U\right)=\det \left(Z\left(\lambda D+L+U\right)Z^{-1}\right)$ .

## Algorithm

Since elements can be overwritten as they are computed in this algorithm, only one storage vector is needed, and vector indexing is omitted. The algorithm goes as follows:

```
Inputs: A, b, ω
Output: 
  
    
      
        ϕ
      
    
    {\displaystyle \phi }
  

Choose an initial guess 
  
    
      
        ϕ
      
    
    {\displaystyle \phi }
  
 to the solution
repeat until convergence
    for i from 1 until n do
        set σ to 0
        for j from 1 until n do
            if j ≠ i then
                set σ to 
  
    
      
        σ
        +
        
          a
          
            i
            j
          
        
        
          ϕ
          
            j
          
        
      
    
    {\displaystyle \sigma +a_{ij}\phi _{j}}
  

            end if
        end (j-loop)
        set 
  
    
      
        
          ϕ
          
            i
          
        
      
    
    {\displaystyle \phi _{i}}
  
 to 
  
    
      
        (
        1
        −
        ω
        )
        
          ϕ
          
            i
          
        
        +
        ω
        
        (
        
          b
          
            i
          
        
        −
        σ
        )
        
          /
        
        
          a
          
            i
            i
          
        
      
    
    {\displaystyle (1-\omega )\phi _{i}+\omega \,(b_{i}-\sigma )/a_{ii}}
  

    end (i-loop)
    check if convergence is reached
end (repeat)
```

**Note**

$(1-\omega )\phi _{i}+{\frac {\omega }{a_{ii}}}(b_{i}-\sigma )$

can also be written

$\phi _{i}+\omega \left({\frac {b_{i}-\sigma }{a_{ii}}}-\phi _{i}\right)$

, thus saving one multiplication in each iteration of the outer

for

-loop.

## Example

We are presented the linear system

${\begin{aligned}4x_{1}-x_{2}-6x_{3}+0x_{4}&=2,\\-5x_{1}-4x_{2}+10x_{3}+8x_{4}&=21,\\0x_{1}+9x_{2}+4x_{3}-2x_{4}&=-12,\\1x_{1}+0x_{2}-7x_{3}+5x_{4}&=-6.\end{aligned}}$

To solve the equations, we choose a relaxation factor $\omega =0.5$ and an initial guess vector $\phi =(0,0,0,0)$ . According to the successive over-relaxation algorithm, the following table is obtained, representing an exemplary iteration with approximations, which ideally, but not necessarily, finds the exact solution, (3, −2, 2, 1), in 38 steps.

| Iteration | $x_{1}$ | $x_{2}$ | $x_{3}$ | $x_{4}$ |
|---|---|---|---|---|
| 01 | 0.25 | −2.78125 | 1.6289062 | 0.5152344 |
| 02 | 1.2490234 | −2.2448974 | 1.9687712 | 0.9108547 |
| 03 | 2.070478 | −1.6696789 | 1.5904881 | 0.76172125 |
| ... | ... | ... | ... | ... |
| 37 | 2.9999998 | −2.0 | 2.0 | 1.0 |
| 38 | 3.0 | −2.0 | 2.0 | 1.0 |

A simple implementation of the algorithm in Common Lisp is offered below.

```mw
;; Set the default floating-point format to "long-float" in order to
;; ensure correct operation on a wider range of numbers.
(setf *read-default-float-format* 'long-float)

(defparameter +MAXIMUM-NUMBER-OF-ITERATIONS+ 100
  "The number of iterations beyond which the algorithm should cease its
   operation, regardless of its current solution. A higher number of
   iterations might provide a more accurate result, but imposes higher
   performance requirements.")

(declaim (type (integer 0 *) +MAXIMUM-NUMBER-OF-ITERATIONS+))

(defun get-errors (computed-solution exact-solution)
  "For each component of the COMPUTED-SOLUTION vector, retrieves its
   error with respect to the expected EXACT-SOLUTION vector, returning a
   vector of error values.
   ---
   While both input vectors should be equal in size, this condition is
   not checked and the shortest of the twain determines the output
   vector's number of elements.
   ---
   The established formula is the following:
     Let resultVectorSize = min(computedSolution.length, exactSolution.length)
     Let resultVector     = new vector of resultVectorSize
     For i from 0 to (resultVectorSize - 1)
       resultVector[i] = exactSolution[i] - computedSolution[i]
     Return resultVector"
  (declare (type (vector number *) computed-solution))
  (declare (type (vector number *) exact-solution))
  (map '(vector number *) #'- exact-solution computed-solution))

(defun is-convergent (errors &key (error-tolerance 0.001))
  "Checks whether the convergence is reached with respect to the
   ERRORS vector which registers the discrepancy betwixt the computed
   and the exact solution vector.
   ---
   The convergence is fulfilled if and only if each absolute error
   component is less than or equal to the ERROR-TOLERANCE, that is:
   For all e in ERRORS, it holds: abs(e) <= errorTolerance."
  (declare (type (vector number *) errors))
  (declare (type number            error-tolerance))
  (flet ((error-is-acceptable (error)
          (declare (type number error))
          (<= (abs error) error-tolerance)))
    (every #'error-is-acceptable errors)))

(defun make-zero-vector (size)
  "Creates and returns a vector of the SIZE with all elements set to 0."
  (declare (type (integer 0 *) size))
  (make-array size :initial-element 0.0 :element-type 'number))

(defun successive-over-relaxation (A b omega
                                   &key (phi (make-zero-vector (length b)))
                                        (convergence-check
                                          #'(lambda (iteration phi)
                                              (declare (ignore phi))
                                              (>= iteration +MAXIMUM-NUMBER-OF-ITERATIONS+))))
  "Implements the successive over-relaxation (SOR) method, applied upon
   the linear equations defined by the matrix A and the right-hand side
   vector B, employing the relaxation factor OMEGA, returning the
   calculated solution vector.
   ---
   The first algorithm step, the choice of an initial guess PHI, is
   represented by the optional keyword parameter PHI, which defaults
   to a zero-vector of the same structure as B. If supplied, this
   vector will be destructively modified. In any case, the PHI vector
   constitutes the function's result value.
   ---
   The terminating condition is implemented by the CONVERGENCE-CHECK,
   an optional predicate
     lambda(iteration phi) => generalized-boolean
   which returns T, signifying the immediate termination, upon achieving
   convergence, or NIL, signaling continuant operation, otherwise. In
   its default configuration, the CONVERGENCE-CHECK simply abides the
   iteration's ascension to the ``+MAXIMUM-NUMBER-OF-ITERATIONS+'',
   ignoring the achieved accuracy of the vector PHI."
  (declare (type (array  number (* *)) A))
  (declare (type (vector number *)     b))
  (declare (type number                omega))
  (declare (type (vector number *)     phi))
  (declare (type (function ((integer 1 *)
                            (vector number *))
                           *)
                 convergence-check))
  (let ((n (array-dimension A 0)))
    (declare (type (integer 0 *) n))
    (loop for iteration from 1 by 1 do
      (loop for i from 0 below n by 1 do
        (let ((rho 0))
          (declare (type number rho))
          (loop for j from 0 below n by 1 do
            (when (/= j i)
              (let ((a[ij]  (aref A i j))
                    (phi[j] (aref phi j)))
                (incf rho (* a[ij] phi[j])))))
          (setf (aref phi i)
                (+ (* (- 1 omega)
                      (aref phi i))
                   (* (/ omega (aref A i i))
                      (- (aref b i) rho))))))
      (format T "~&~d. solution = ~a" iteration phi)
      ;; Check if convergence is reached.
      (when (funcall convergence-check iteration phi)
        (return))))
  (the (vector number *) phi))

;; Summon the function with the exemplary parameters.
(let ((A              (make-array (list 4 4)
                        :initial-contents
                        '((  4  -1  -6   0 )
                          ( -5  -4  10   8 )
                          (  0   9   4  -2 )
                          (  1   0  -7   5 ))))
      (b              (vector 2 21 -12 -6))
      (omega          0.5)
      (exact-solution (vector 3 -2 2 1)))
  (successive-over-relaxation
    A b omega
    :convergence-check
    #'(lambda (iteration phi)
        (declare (type (integer 0 *)     iteration))
        (declare (type (vector number *) phi))
        (let ((errors (get-errors phi exact-solution)))
          (declare (type (vector number *) errors))
          (format T "~&~d. errors   = ~a" iteration errors)
          (or (is-convergent errors :error-tolerance 0.0)
              (>= iteration +MAXIMUM-NUMBER-OF-ITERATIONS+))))))
```

A simple Python implementation of the pseudo-code provided above.

```mw
import numpy as np
from scipy import linalg

def sor_solver(A, b, omega, initial_guess, convergence_criteria):
    """
    This is an implementation of the pseudo-code provided in the Wikipedia article.
    Arguments:
        A: nxn numpy matrix.
        b: n dimensional numpy vector.
        omega: relaxation factor.
        initial_guess: An initial solution guess for the solver to start with.
        convergence_criteria: The maximum discrepancy acceptable to regard the current solution as fitting.
    Returns:
        phi: solution vector of dimension n.
    """
    step = 0
    phi = initial_guess[:]
    residual = linalg.norm(A @ phi - b)  # Initial residual
    while residual > convergence_criteria:
        for i in range(A.shape[0]):
            sigma = 0
            for j in range(A.shape[1]):
                if j != i:
                    sigma += A[i, j] * phi[j]
            phi[i] = (1 - omega) * phi[i] + (omega / A[i, i]) * (b[i] - sigma)
        residual = linalg.norm(A @ phi - b)
        step += 1
        print("Step {} Residual: {:10.6g}".format(step, residual))
    return phi

# An example case that mirrors the one in the Wikipedia article
residual_convergence = 1e-8
omega = 0.5  # Relaxation factor

A = np.array([[4, -1, -6, 0],
              [-5, -4, 10, 8],
              [0, 9, 4, -2],
              [1, 0, -7, 5]])

b = np.array([2, 21, -12, -6])

initial_guess = np.zeros(4)

phi = sor_solver(A, b, omega, initial_guess, residual_convergence)
print(phi)
```

## Symmetric successive over-relaxation

The version for symmetric matrices *A*, in which

$U=L^{T},\,$

is referred to as **Symmetric Successive Over-Relaxation**, or (**SSOR**), in which

$P=\left({\frac {D}{\omega }}+L\right){\frac {\omega }{2-\omega }}D^{-1}\left({\frac {D}{\omega }}+U\right),$

and the iterative method is

$\mathbf {x} ^{k+1}=\mathbf {x} ^{k}-\gamma ^{k}P^{-1}\left(A\mathbf {x} ^{k}-\mathbf {b} \right),\ k\geq 0.$

The SOR and SSOR methods are credited to David M. Young Jr.

## Other applications of the method

A similar technique can be used for any iterative method. If the original iteration had the form

$x_{n+1}=f(x_{n})$

then the modified version would use

$x_{n+1}^{\mathrm {SOR} }=(1-\omega )x_{n}^{\mathrm {SOR} }+\omega f(x_{n}^{\mathrm {SOR} }).$

However, the formulation presented above, used for solving systems of linear equations, is not a special case of this formulation if x is considered to be the complete vector. If this formulation is used instead, the equation for calculating the next vector will look like

$\mathbf {x} ^{(k+1)}=\left(1-\omega \right)\mathbf {x} ^{(k)}+\omega L_{*}^{-1}\left(\mathbf {b} -U\mathbf {x} ^{(k)}\right),$

where $L_{*}=L+D$ . Values of $\omega >1$ are used to speed up convergence of a slow-converging process, while values of $\omega <1$ are often used to help establish convergence of a diverging iterative process or speed up the convergence of an overshooting process.

There are various methods that adaptively set the relaxation parameter $\omega$ based on the observed behavior of the converging process. Usually they help to reach a super-linear convergence for some problems but fail for the others.
