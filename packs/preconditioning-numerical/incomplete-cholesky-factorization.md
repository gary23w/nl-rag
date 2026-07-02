---
title: "Incomplete Cholesky factorization"
source: https://en.wikipedia.org/wiki/Incomplete_Cholesky_factorization
domain: preconditioning-numerical
license: CC-BY-SA-4.0
tags: preconditioner matrix, incomplete lu factorization, condition number, schur complement
fetched: 2026-07-02
---

# Incomplete Cholesky factorization

In numerical analysis, an **incomplete Cholesky factorization** of a symmetric positive definite matrix is a sparse approximation of the Cholesky factorization. An incomplete Cholesky factorization is often used as a preconditioner for algorithms like the conjugate gradient method.

The Cholesky factorization of a positive definite matrix *A* of order *N* is *A* = *LL** where *L* is a lower triangular matrix. An incomplete Cholesky factorization is given by a lower triangular matrix *K* that is sparser than *L*, but in some sense similar to *L*. The corresponding preconditioner is *KK**.

There are many ways of constructing incomplete Cholesky factorizations. This article reviews two of them.

## Motivation

Consider the following matrix as an example:

$\mathbf {A} ={\begin{bmatrix}5&-2&0&-2&-2\\-2&5&-2&0&0\\0&-2&5&-2&0\\-2&0&-2&5&-2\\-2&0&0&-2&5\\\end{bmatrix}}$

If we apply the full regular Cholesky decomposition, it yields:

$\mathbf {L} ={\begin{bmatrix}2.24&0&0&0&0\\-0.89&2.05&0&0&0\\0&-0.98&2.02&0&0\\-0.89&-0.39&-1.18&1.63&0\\-0.89&-0.39&-0.19&-1.95&0.45\\\end{bmatrix}}$

And, by definition:

$\mathbf {A} =\mathbf {L} \mathbf {L'}$

However, by applying Cholesky decomposition, we observe that some zero elements in the original matrix end up being non-zero elements in the decomposed matrix, like elements (4,2), (5,2) and (5,3) in this example. These elements are known as "fill-ins".

This is not an issue per se, but it is very problematic when working with sparse matrices, since the fill-ins generation is mostly unpredictable and reduces the matrix sparsity, impacting the efficiency of sparse matrix algorithms.

Therefore, given the importance of the Cholesky decomposition in matrix calculations, it is extremely relevant to repurpose the regular method, so as to eliminate the fill-ins generation. Incomplete Cholesky factorizations do exactly that. They yield some matrix $\mathbf {K}$ that is sparser than $\mathbf {L}$ and gives an approximation $\mathbf {A} \approx \mathbf {K} \mathbf {K'}$ .

## Incomplete Cholesky of level zero

*Incomplete Cholesky of level zero* or *IC(0)* runs the exact Cholesky decomposition algorithm, but skips updates to *K* to ensure that it has the same sparsity as *A.* To describe the algorithm mathematically, initialize *K* to the *N-*by-*N* zero matrix. For i from 1 to N , we set

$K_{ii}=\left({a_{ii}-\sum \limits _{k=1}^{i-1}{K_{ik}^{2}}}\right)^{1 \over 2}$ ,

and for j from $i+1$ to N , we apply the following update only if $a_{ji}$ is nonzero

$K_{ji}={1 \over {K_{ii}}}\left({a_{ji}-\sum \limits _{k=1}^{i-1}{K_{ik}K_{jk}}}\right)$ .

This gives a factor *K* that is as sparse as the lower triangle of *A,* and so storing both *A* and *K* takes at most twice the storage required to store *A* on its own. The IC(0) algorithm may exit with an error on some positive definite matrices. It is guaranteed to succeed if *A* is diagonally dominant, although there many positive definite matrices where IC(0) succeeds even without diagonal dominance.

### Octave or MATLAB implementation for dense array datastructures

Implementation of the incomplete Cholesky factorization in the GNU Octave language. The factorization is stored as a lower triangular matrix, with the elements in the upper triangle set to zero.

```mw
function a = ichol(a)
	n = size(a,1);

	for k = 1:n
		a(k,k) = sqrt(a(k,k));
		for i = (k+1):n
		    if (a(i,k) != 0)
		        a(i,k) = a(i,k)/a(k,k);            
		    endif
		endfor
		for j = (k+1):n
		    for i = j:n
		        if (a(i,j) != 0)
		            a(i,j) = a(i,j) - a(i,k)*a(j,k);  
		        endif
		    endfor
		endfor
	endfor

    for i = 1:n
        for j = i+1:n
            a(i,j) = 0;
        endfor
    endfor            
endfunction
```

### Worked example

Consider again the matrix displayed in the motivation section of this article. Since it is symmetric and the method only uses the lower triangular elements, we can represent it by:

$\mathbf {A_{tri}} ={\begin{bmatrix}5&0&0&0&0\\-2&5&0&0&0\\0&-2&5&0&0\\-2&0&-2&5&0\\-2&0&0&-2&5\end{bmatrix}}$

More specifically, in its sparse form as a coordinate list, sweeping rows first:

```mw
Value	5	-2	-2	-2	5	-2	5	-2	5	-2	5
Row		1	2	4	5	2	3	3	4	4	5	5
Col		1	1	1	1	2	2	3	3	4	4	5
```

Then, we take the square root of (1,1) and divide the other (i,1) elements by the result:

```mw
Value	2.24 -0.89 -0.89 -0.89	| 5 -2 5 -2 5 -2 5
Row		1	  2	   4	 5	    | 2 3  3 4  4 5  5
Col		1	  1	   1  	 1	    | 2 2  3 3  4 4  5
```

After that, for all the other elements with column greater than 1, calculate (i,j)=(i,j)-(i,1)*(j,1) if (i,1) and (j,1) exist. For example: (5,4) = (5,4)-(5,1)*(4,1) = -2 -(-0.89*-0.89) = -2.8.

```mw
Value	2.24 -0.89 -0.89 -0.89	| 4.2 -2 5 -2 4.2 -2.8 4.2
Row		1	  2	   4	 5	    | 2   3  3 4  4	  5    5
Col		1	  1	   1  	 1	    | 2   2  3 3  4	  4    5
                                  ↑           ↑   ↑    ↑
```

The elements (2,2), (4,4), (5,4) and (5,5) (marked with an arrow) have been recalculated, since they obey this rule. On the other hand, the elements (3,2), (3,3) and (4,3) won't be recalculated since the element (3,1) doesn't exist, even though the elements (2,1) and (4,1) exist. Now, repeat the process, but for (i,2). Take the square root of (2,2) and divide the other (i,2) elements by the result:

```mw
Value	2.24 -0.89 -0.89 -0.89	| 2.05 -0.98 | 5 -2 4.2 -2.8 4.2
Row		1	  2	   4	 5	    | 2    3     | 3  4 4   5    5
Col		1	  1	   1  	 1	    | 2    2     | 3  3 4   4    5
```

Again, for elements with column greater than 2, calculate (i,j)=(i,j)-(i,2)*(j,2) if (i,2) and (j,2) exist:

```mw
Value	2.24 -0.89 -0.89 -0.89	| 2.05 -0.98 | 4.05 -2 4.2 -2.8 4.2
Row		1	  2	   4	 5	    | 2    3     | 3    4  4   5    5
Col		1	  1	   1  	 1	    | 2    2     | 3    3  4   4    5
                                               ↑
```

Repeat for (i,3). Take the square root of (3,3) and divide the other (i,3):

```mw
Value	2.24 -0.89 -0.89 -0.89	2.05 -0.98 | 2.01 -0.99 | 4.2 -2.8 4.2
Row		1	  2	   4	 5	    2    3     | 3    4     | 4	  5    5
Col		1	  1	   1  	 1	    2    2     | 3    3     | 4	  4    5
```

For elements with column greater than 3, calculate (i,j)=(i,j)-(i,3)*(j,3) if (i,3) and (j,3) exist:

```mw
Value	2.24 -0.89 -0.89 -0.89	2.05 -0.98 | 2.01 -0.99 | 3.21 -2.8 4.2
Row		1	  2	   4	 5	    2    3     | 3    4     | 4	   5    5
Col		1	  1	   1  	 1	    2    2     | 3    3     | 4	   4    5
                                                          ↑
```

Repeat for (i,4). Take the square root of (4,4) and divide the other (i,4):

```mw
Value	2.24 -0.89 -0.89 -0.89	2.05 -0.98 2.01 -0.99 | 1.79 -1.56 | 4.2
Row		1	  2	   4	 5	    2    3     3    4     | 4	   5   | 5
Col		1	  1	   1  	 1	    2    2     3    3     | 4	   4   | 5
```

For elements with column greater than 4, calculate (i,j)=(i,j)-(i,4)*(j,4) if (i,4) and (j,4) exist:

```mw
Value	2.24 -0.89 -0.89 -0.89	2.05 -0.98 2.01 -0.99 | 1.79 -1.56 | 1.76
Row		1	  2	   4	 5	    2    3     3    4     | 4	   5   | 5
Col		1	  1	   1  	 1	    2    2     3    3     | 4	   4   | 5
                                                                     ↑
```

Finally take the square root of (5,5):

```mw
Value	2.24 -0.89 -0.89 -0.89	2.05 -0.98 2.01 -0.99 1.79 -1.56 | 1.33
Row		1	  2	   4	 5	    2    3     3    4     4	   5     | 5
Col		1	  1	   1  	 1	    2    2     3    3     4	   4     | 5
```

Expanding the matrix to its full form:

$\mathbf {K} ={\begin{bmatrix}2.24&0&0&0&0\\-0.89&2.05&0&0&0\\0&-0.98&2.01&0&0\\-0.89&0&-0.99&1.79&0\\-0.89&0&0&-1.56&1.33\end{bmatrix}}$

Note that in this case no fill-ins were generated compared to the original matrix. The elements (4,2), (5,2) and (5,3) are still zero.

However, if we perform the multiplication of *K* to its transpose:

$\mathbf {KK'} ={\begin{bmatrix}5&-2&0&-2&-2\\-2&5&-2&0.8&0.8\\0&-2&5&-2&0\\-2&0.8&-2&5&-2\\-2&0.8&0&-2&5\end{bmatrix}}$

We get a matrix slightly different from the original one, since the decomposition didn't take into account all the elements, in order to eliminate the fill-ins.

### MATLAB implementation with a sparse matrix datastructure

The sparse version for the incomplete Cholesky factorization (the same procedure presented above) implemented in MATLAB can be seen below. Naturally, MATLAB has its own means for dealing with sparse matrixes, but the code below was made explicit for pedagogic purposes. This algorithm is efficient, since it treats the matrix as a sequential 1D array, automatically avoiding the zero elements.

```mw
function A=Sp_ichol(A)
	n=size(A,1);
	ncols=A(n).col;
    c_end=0;
    for col=1:ncols
        is_next_col=0;
        c_start=c_end+1;
        for i=c_start:n
            if A(i).col==col % in the current column (col):
                if A(i).col==A(i).row 
                    A(i).val=sqrt(A(i).val); % take the square root of the current column's diagonal element
                    div=A(i).val;
                else
                    A(i).val=A(i).val/div; % divide the other current column's elements by the square root of the diagonal element
                end
            end
            if A(i).col>col % in the next columns (col+1 ... ncols):
                if is_next_col==0
                    c_end=i-1;
                    is_next_col=1;
                end
                v1=0;
                v2=0;
                for j=c_start:c_end
                    if A(j).col==col
                        if A(j).row==A(i).row % search for current column's (col) elements A(j) whose row index is the same as current element's A(i) row index
                            v1=A(j).val;
                        end
                        if A(j).row==A(i).col % search for current column's (col) elements A(j) whose row index is the same as current element's A(i) column index
                            v2=A(j).val;
                        end
                        if v1~=0 && v2~=0 % if these elements exist in the current column (col), recalculate the current element A(i):
                            A(i).val=A(i).val-v1*v2;
                            break;
                        end
                    end
                end
            end
        end
    end
end
```

## Diagonal-based incomplete Cholesky

*Diagonal-based incomplete Cholesky* (DIC) constructs a factor *K* that can be stored using only existing space for *A* and *N* additional numbers. Like IC(0), the DIC algorithm succeeds when diagonally dominant. Variants of the DIC algorithm can run to completion for slightly more general classes of matrices.

With DIC, we define $\mathbf {K} =(\mathbf {S} +\mathbf {D} )\mathbf {D} ^{-1/2}$ , where $\mathbf {S}$ is the strict lower triangle of $\mathbf {A}$ and $\mathbf {D}$ is the diagonal matrix produced by the following procedure:

Initialize a vector *d* to the diagonal of *A*. We iterate over i from 2 to *N.* At a given iteration *i,* we iterate over *j* from *i+1* to *N,* and downdate $d_{j}=d_{j}-a_{ji}^{2}/d_{i}$ . Note that this downdate can be skipped when $a_{ji}$ is zero.

### Python implementation with a sparse matrix datastructure

```mw
from scipy.sparse import csc_matrix
import numpy as np

def dic_diagonal(A: csc_matrix) -> np.ndarray:
    # Figure 3.3 of www.netlib.org/templates/templates.pdf shows how to
    # compute the diagonal of "inv(D)" for the diagonal-based incomplete 
    # LU preconditioner. This function adapts that method for symmetric
    # diagonally dominant matrices and constructs the diagonal of D
    # (rather than that of inv(D)).
    d = A.diagonal()
    inds = A.indices
    ptrs = A.indptr
    vals = A.data
    for i in range(d.size):
        if d[i] < 0:
            raise ValueError('DIC factorization failed!')
        j = inds[ptrs[i]:ptrs[i+1]]
        v = vals[ptrs[i]:ptrs[i+1]]
        selector = j > i
        j = j[selector]
        v = v[selector]
        d[j] -= v**2 / d[i]
    return d
```
