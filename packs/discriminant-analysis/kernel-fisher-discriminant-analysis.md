---
title: "Kernel Fisher discriminant analysis"
source: https://en.wikipedia.org/wiki/Kernel_Fisher_discriminant_analysis
domain: discriminant-analysis
license: CC-BY-SA-4.0
tags: linear discriminant analysis, discriminant function, linear classifier, multiclass classification
fetched: 2026-07-02
---

# Kernel Fisher discriminant analysis

In statistics, **kernel Fisher discriminant analysis (KFD)**, also known as **generalized discriminant analysis** and **kernel discriminant analysis**, is a kernelized version of linear discriminant analysis (LDA). It is named after Ronald Fisher.

## Linear discriminant analysis

Intuitively, the idea of LDA is to find a projection where class separation is maximized. Given two sets of labeled data, $\mathbf {C} _{1}$ and $\mathbf {C} _{2}$ , we can calculate the mean value of each class, $\mathbf {m} _{1}$ and $\mathbf {m} _{2}$ , as

$\mathbf {m} _{i}={\frac {1}{l_{i}}}\sum _{n=1}^{l_{i}}\mathbf {x} _{n}^{i},$

where $l_{i}$ is the number of examples of class $\mathbf {C} _{i}$ . The goal of linear discriminant analysis is to give a large separation of the class means while also keeping the in-class variance small. This is formulated as maximizing, with respect to $\mathbf {w}$ , the following ratio:

$J(\mathbf {w} )={\frac {\mathbf {w} ^{\text{T}}\mathbf {S} _{B}\mathbf {w} }{\mathbf {w} ^{\text{T}}\mathbf {S} _{W}\mathbf {w} }},$

where $\mathbf {S} _{B}$ is the between-class covariance matrix and $\mathbf {S} _{W}$ is the total within-class covariance matrix:

${\begin{aligned}\mathbf {S} _{B}&=(\mathbf {m} _{2}-\mathbf {m} _{1})(\mathbf {m} _{2}-\mathbf {m} _{1})^{\text{T}}\\\mathbf {S} _{W}&=\sum _{i=1,2}\sum _{n=1}^{l_{i}}(\mathbf {x} _{n}^{i}-\mathbf {m} _{i})(\mathbf {x} _{n}^{i}-\mathbf {m} _{i})^{\text{T}}.\end{aligned}}$

The maximum of the above ratio is attained at

$\mathbf {w} \propto \mathbf {S} _{W}^{-1}(\mathbf {m} _{2}-\mathbf {m} _{1}).$

as can be shown by the Lagrange multiplier method (sketch of proof):

Maximizing $J(\mathbf {w} )={\frac {\mathbf {w} ^{\text{T}}\mathbf {S} _{B}\mathbf {w} }{\mathbf {w} ^{\text{T}}\mathbf {S} _{W}\mathbf {w} }}$ is equivalent to maximizing

$\mathbf {w} ^{\text{T}}\mathbf {S} _{B}\mathbf {w}$

subject to

$\mathbf {w} ^{\text{T}}\mathbf {S} _{W}\mathbf {w} =1.$

This, in turn, is equivalent to maximizing $I(\mathbf {w} ,\lambda )=\mathbf {w} ^{\text{T}}\mathbf {S} _{B}\mathbf {w} -\lambda (\mathbf {w} ^{\text{T}}\mathbf {S} _{W}\mathbf {w} -1)$ , where $\lambda$ is the Lagrange multiplier.

At the maximum, the derivatives of $I(\mathbf {w} ,\lambda )$ with respect to $\mathbf {w}$ and $\lambda$ must be zero. Taking ${\frac {dI}{d\mathbf {w} }}=\mathbf {0}$ yields

$\mathbf {S} _{B}\mathbf {w} -\lambda \mathbf {S} _{W}\mathbf {w} =\mathbf {0} ,$

which is trivially satisfied by $\mathbf {w} =c\mathbf {S} _{W}^{-1}(\mathbf {m} _{2}-\mathbf {m} _{1})$ and $\lambda =(\mathbf {m} _{2}-\mathbf {m} _{1})^{\text{T}}\mathbf {S} _{W}^{-1}(\mathbf {m} _{2}-\mathbf {m} _{1}).$

## Extending LDA

To extend LDA to non-linear mappings, the data, given as the $\ell$ points $\mathbf {x} _{i},$ can be mapped to a new feature space, $F,$ via some function $\phi .$ In this new feature space, the function that needs to be maximized is

$J(\mathbf {w} )={\frac {\mathbf {w} ^{\text{T}}\mathbf {S} _{B}^{\phi }\mathbf {w} }{\mathbf {w} ^{\text{T}}\mathbf {S} _{W}^{\phi }\mathbf {w} }},$

where

${\begin{aligned}\mathbf {S} _{B}^{\phi }&=\left(\mathbf {m} _{2}^{\phi }-\mathbf {m} _{1}^{\phi }\right)\left(\mathbf {m} _{2}^{\phi }-\mathbf {m} _{1}^{\phi }\right)^{\text{T}}\\\mathbf {S} _{W}^{\phi }&=\sum _{i=1,2}\sum _{n=1}^{l_{i}}\left(\phi (\mathbf {x} _{n}^{i})-\mathbf {m} _{i}^{\phi }\right)\left(\phi (\mathbf {x} _{n}^{i})-\mathbf {m} _{i}^{\phi }\right)^{\text{T}},\end{aligned}}$

and

$\mathbf {m} _{i}^{\phi }={\frac {1}{l_{i}}}\sum _{j=1}^{l_{i}}\phi (\mathbf {x} _{j}^{i}).$

Further, note that $\mathbf {w} \in F$ . Explicitly computing the mappings $\phi (\mathbf {x} _{i})$ and then performing LDA can be computationally expensive, and in many cases intractable. For example, F may be infinite dimensional. Thus, rather than explicitly mapping the data to F , the data can be implicitly embedded by rewriting the algorithm in terms of dot products and using kernel functions in which the dot product in the new feature space is replaced by a kernel function, $k(\mathbf {x} ,\mathbf {y} )=\phi (\mathbf {x} )\cdot \phi (\mathbf {y} )$ .

LDA can be reformulated in terms of dot products by first noting that $\mathbf {w}$ will have an expansion of the form

$\mathbf {w} =\sum _{i=1}^{l}\alpha _{i}\phi (\mathbf {x} _{i}).$

Then note that

$\mathbf {w} ^{\text{T}}\mathbf {m} _{i}^{\phi }={\frac {1}{l_{i}}}\sum _{j=1}^{l}\sum _{k=1}^{l_{i}}\alpha _{j}k\left(\mathbf {x} _{j},\mathbf {x} _{k}^{i}\right)=\mathbf {\alpha } ^{\text{T}}\mathbf {M} _{i},$

where

$(\mathbf {M} _{i})_{j}={\frac {1}{l_{i}}}\sum _{k=1}^{l_{i}}k(\mathbf {x} _{j},\mathbf {x} _{k}^{i}).$

The numerator of $J(\mathbf {w} )$ can then be written as:

$\mathbf {w} ^{\text{T}}\mathbf {S} _{B}^{\phi }\mathbf {w} =\mathbf {w} ^{\text{T}}\left(\mathbf {m} _{2}^{\phi }-\mathbf {m} _{1}^{\phi }\right)\left(\mathbf {m} _{2}^{\phi }-\mathbf {m} _{1}^{\phi }\right)^{\text{T}}\mathbf {w} =\mathbf {\alpha } ^{\text{T}}\mathbf {M} \mathbf {\alpha } ,\qquad {\text{where}}\qquad \mathbf {M} =(\mathbf {M} _{2}-\mathbf {M} _{1})(\mathbf {M} _{2}-\mathbf {M} _{1})^{\text{T}}.$

Similarly, the denominator can be written as

$\mathbf {w} ^{\text{T}}\mathbf {S} _{W}^{\phi }\mathbf {w} =\mathbf {\alpha } ^{\text{T}}\mathbf {N} \mathbf {\alpha } ,\qquad {\text{where}}\qquad \mathbf {N} =\sum _{j=1,2}\mathbf {K} _{j}(\mathbf {I} -\mathbf {1} _{l_{j}})\mathbf {K} _{j}^{\text{T}},$

with the $n^{\text{th}},m^{\text{th}}$ component of $\mathbf {K} _{j}$ defined as $k(\mathbf {x} _{n},\mathbf {x} _{m}^{j}),\mathbf {I}$ is the identity matrix, and $\mathbf {1} _{l_{j}}$ the matrix with all entries equal to $1/l_{j}$ . This identity can be derived by starting out with the expression for $\mathbf {w} ^{\text{T}}\mathbf {S} _{W}^{\phi }\mathbf {w}$ and using the expansion of $\mathbf {w}$ and the definitions of $\mathbf {S} _{W}^{\phi }$ and $\mathbf {m} _{i}^{\phi }$

${\begin{aligned}\mathbf {w} ^{\text{T}}\mathbf {S} _{W}^{\phi }\mathbf {w} &=\left(\sum _{i=1}^{l}\alpha _{i}\phi ^{\text{T}}(\mathbf {x} _{i})\right)\left(\sum _{j=1,2}\sum _{n=1}^{l_{j}}\left(\phi (\mathbf {x} _{n}^{j})-\mathbf {m} _{j}^{\phi }\right)\left(\phi (\mathbf {x} _{n}^{j})-\mathbf {m} _{j}^{\phi }\right)^{\text{T}}\right)\left(\sum _{k=1}^{l}\alpha _{k}\phi (\mathbf {x} _{k})\right)\\&=\sum _{j=1,2}\sum _{i=1}^{l}\sum _{n=1}^{l_{j}}\sum _{k=1}^{l}\left(\alpha _{i}\phi ^{\text{T}}(\mathbf {x} _{i})\left(\phi (\mathbf {x} _{n}^{j})-\mathbf {m} _{j}^{\phi }\right)\left(\phi (\mathbf {x} _{n}^{j})-\mathbf {m} _{j}^{\phi }\right)^{\text{T}}\alpha _{k}\phi (\mathbf {x} _{k})\right)\\&=\sum _{j=1,2}\sum _{i=1}^{l}\sum _{n=1}^{l_{j}}\sum _{k=1}^{l}\left(\alpha _{i}k(\mathbf {x} _{i},\mathbf {x} _{n}^{j})-{\frac {1}{l_{j}}}\sum _{p=1}^{l_{j}}\alpha _{i}k(\mathbf {x} _{i},\mathbf {x} _{p}^{j})\right)\left(\alpha _{k}k(\mathbf {x} _{k},\mathbf {x} _{n}^{j})-{\frac {1}{l_{j}}}\sum _{q=1}^{l_{j}}\alpha _{k}k(\mathbf {x} _{k},\mathbf {x} _{q}^{j})\right)\\&=\sum _{j=1,2}\left(\sum _{i=1}^{l}\sum _{n=1}^{l_{j}}\sum _{k=1}^{l}\left(\alpha _{i}\alpha _{k}k(\mathbf {x} _{i},\mathbf {x} _{n}^{j})k(\mathbf {x} _{k},\mathbf {x} _{n}^{j})-{\frac {2\alpha _{i}\alpha _{k}}{l_{j}}}\sum _{p=1}^{l_{j}}k(\mathbf {x} _{i},\mathbf {x} _{n}^{j})k(\mathbf {x} _{k},\mathbf {x} _{p}^{j})+{\frac {\alpha _{i}\alpha _{k}}{l_{j}^{2}}}\sum _{p=1}^{l_{j}}\sum _{q=1}^{l_{j}}k(\mathbf {x} _{i},\mathbf {x} _{p}^{j})k(\mathbf {x} _{k},\mathbf {x} _{q}^{j})\right)\right)\\&=\sum _{j=1,2}\left(\sum _{i=1}^{l}\sum _{n=1}^{l_{j}}\sum _{k=1}^{l}\left(\alpha _{i}\alpha _{k}k(\mathbf {x} _{i},\mathbf {x} _{n}^{j})k(\mathbf {x} _{k},\mathbf {x} _{n}^{j})-{\frac {\alpha _{i}\alpha _{k}}{l_{j}}}\sum _{p=1}^{l_{j}}k(\mathbf {x} _{i},\mathbf {x} _{n}^{j})k(\mathbf {x} _{k},\mathbf {x} _{p}^{j})\right)\right)\\[6pt]&=\sum _{j=1,2}\mathbf {\alpha } ^{\text{T}}\mathbf {K} _{j}\mathbf {K} _{j}^{\text{T}}\mathbf {\alpha } -\mathbf {\alpha } ^{\text{T}}\mathbf {K} _{j}\mathbf {1} _{l_{j}}\mathbf {K} _{j}^{\text{T}}\mathbf {\alpha } \\[4pt]&=\mathbf {\alpha } ^{\text{T}}\mathbf {N} \mathbf {\alpha } .\end{aligned}}$

With these equations for the numerator and denominator of $J(\mathbf {w} )$ , the equation for J can be rewritten as

$J(\mathbf {\alpha } )={\frac {\mathbf {\alpha } ^{\text{T}}\mathbf {M} \mathbf {\alpha } }{\mathbf {\alpha } ^{\text{T}}\mathbf {N} \mathbf {\alpha } }}.$

Then, differentiating and setting equal to zero gives

$(\mathbf {\alpha } ^{\text{T}}\mathbf {M} \mathbf {\alpha } )\mathbf {N} \mathbf {\alpha } =(\mathbf {\alpha } ^{\text{T}}\mathbf {N} \mathbf {\alpha } )\mathbf {M} \mathbf {\alpha } .$

Since only the direction of $\mathbf {w}$ , and hence the direction of $\mathbf {\alpha } ,$ matters, the above can be solved for $\mathbf {\alpha }$ as

$\mathbf {\alpha } =\mathbf {N} ^{-1}(\mathbf {M} _{2}-\mathbf {M} _{1}).$

Note that in practice, $\mathbf {N}$ is usually singular and so a multiple of the identity is added to it

$\mathbf {N} _{\epsilon }=\mathbf {N} +\epsilon \mathbf {I} .$

Given the solution for $\mathbf {\alpha }$ , the projection of a new data point is given by

$y(\mathbf {x} )=(\mathbf {w} \cdot \phi (\mathbf {x} ))=\sum _{i=1}^{l}\alpha _{i}k(\mathbf {x} _{i},\mathbf {x} ).$

## Multi-class KFD

The extension to cases where there are more than two classes is relatively straightforward. Let c be the number of classes. Then multi-class KFD involves projecting the data into a $(c-1)$ -dimensional space using $(c-1)$ discriminant functions

$y_{i}=\mathbf {w} _{i}^{\text{T}}\phi (\mathbf {x} )\qquad i=1,\ldots ,c-1.$

This can be written in matrix notation

$\mathbf {y} =\mathbf {W} ^{\text{T}}\phi (\mathbf {x} ),$

where the $\mathbf {w} _{i}$ are the columns of $\mathbf {W}$ . Further, the between-class covariance matrix is now

$\mathbf {S} _{B}^{\phi }=\sum _{i=1}^{c}l_{i}(\mathbf {m} _{i}^{\phi }-\mathbf {m} ^{\phi })(\mathbf {m} _{i}^{\phi }-\mathbf {m} ^{\phi })^{\text{T}},$

where $\mathbf {m} ^{\phi }$ is the mean of all the data in the new feature space. The within-class covariance matrix is

$\mathbf {S} _{W}^{\phi }=\sum _{i=1}^{c}\sum _{n=1}^{l_{i}}(\phi (\mathbf {x} _{n}^{i})-\mathbf {m} _{i}^{\phi })(\phi (\mathbf {x} _{n}^{i})-\mathbf {m} _{i}^{\phi })^{\text{T}},$

The solution is now obtained by maximizing

$J(\mathbf {W} )={\frac {\left|\mathbf {W} ^{\text{T}}\mathbf {S} _{B}^{\phi }\mathbf {W} \right|}{\left|\mathbf {W} ^{\text{T}}\mathbf {S} _{W}^{\phi }\mathbf {W} \right|}}.$

The kernel trick can again be used and the goal of multi-class KFD becomes

$\mathbf {A} ^{*}={\underset {\mathbf {A} }{\operatorname {argmax} }}={\frac {\left|\mathbf {A} ^{\text{T}}\mathbf {M} \mathbf {A} \right|}{\left|\mathbf {A} ^{\text{T}}\mathbf {N} \mathbf {A} \right|}},$

where $A=[\mathbf {\alpha } _{1},\ldots ,\mathbf {\alpha } _{c-1}]$ and

${\begin{aligned}M&=\sum _{j=1}^{c}l_{j}(\mathbf {M} _{j}-\mathbf {M} _{*})(\mathbf {M} _{j}-\mathbf {M} _{*})^{\text{T}}\\N&=\sum _{j=1}^{c}\mathbf {K} _{j}(\mathbf {I} -\mathbf {1} _{l_{j}})\mathbf {K} _{j}^{\text{T}}.\end{aligned}}$

The $\mathbf {M} _{i}$ are defined as in the above section and $\mathbf {M} _{*}$ is defined as

$(\mathbf {M} _{*})_{j}={\frac {1}{l}}\sum _{k=1}^{l}k(\mathbf {x} _{j},\mathbf {x} _{k}).$

$\mathbf {A} ^{*}$ can then be computed by finding the $(c-1)$ leading eigenvectors of $\mathbf {N} ^{-1}\mathbf {M}$ . Furthermore, the projection of a new input, $\mathbf {x} _{t}$ , is given by

$\mathbf {y} (\mathbf {x} _{t})=\left(\mathbf {A} ^{*}\right)^{\text{T}}\mathbf {K} _{t},$

where the $i^{th}$ component of $\mathbf {K} _{t}$ is given by $k(\mathbf {x} _{i},\mathbf {x} _{t})$ .

## Classification using KFD

In both two-class and multi-class KFD, the class label of a new input can be assigned as

$f(\mathbf {x} )=arg\min _{j}D(\mathbf {y} (\mathbf {x} ),{\bar {\mathbf {y} }}_{j}),$

where ${\bar {\mathbf {y} }}_{j}$ is the projected mean for class j and $D(\cdot ,\cdot )$ is a distance function.

## Applications

Kernel discriminant analysis has been used in a variety of applications. These include:

- Face recognition and detection
- Hand-written digit recognition
- Palmprint recognition
- Classification of malignant and benign cluster microcalcifications
- Seed classification
- Search for the Higgs Boson at CERN
