---
title: "Shor's algorithm"
source: https://en.wikipedia.org/wiki/Shor's_algorithm
domain: bqp-class
license: CC-BY-SA-4.0
tags: bounded error quantum polynomial, quantum turing machine, shor algorithm, grover algorithm
fetched: 2026-07-02
---

# Shor's algorithm

**Shor's algorithm** is a quantum algorithm for finding the prime factors of an integer. It was developed in 1994 by the American mathematician Peter Shor. It is one of the few known quantum algorithms with compelling potential applications and strong evidence of superpolynomial speedup compared to best known classical (non-quantum) algorithms. However, beating classical computers may require quantum computers with millions of qubits due to the overhead caused by quantum error correction.

Shor proposed multiple similar algorithms for solving the factoring problem, the discrete logarithm problem, and the period-finding problem. "Shor's algorithm" usually refers to the factoring algorithm, but may refer to any of the three algorithms. The discrete logarithm algorithm and the factoring algorithm are instances of the period-finding algorithm, and all three are instances of the hidden subgroup problem.

On a quantum computer, to factor an integer N , Shor's algorithm runs in polynomial time, meaning the time taken is polynomial in $\log N$ . It takes quantum gates of order $O\!\left((\log N)^{2}(\log \log N)(\log \log \log N)\right)$ using fast multiplication, or even $O\!\left((\log N)^{2}(\log \log N)\right)$ using the asymptotically fastest multiplication algorithm currently known due to Harvey and van der Hoeven, thus demonstrating that the integer factorization problem is in complexity class **BQP**. Shor's algorithm is asymptotically faster than the most scalable classical factoring algorithm, the general number field sieve, which works in sub-exponential time: $O\!\left(e^{1.9(\log N)^{1/3}(\log \log N)^{2/3}}\right)$ .

## Feasibility and implications

Assuming a quantum computer with a sufficient number of qubits could operate without succumbing to quantum noise and other quantum-decoherence phenomena, then Shor's algorithm could be used to break public-key cryptography schemes, such as

- The RSA scheme
- The finite-field Diffie–Hellman key exchange
- The elliptic-curve Diffie–Hellman key exchange

RSA can be broken if factoring large integers is computationally feasible. As far as is known, this is not possible using classical (non-quantum) computers; no classical algorithm is known that can factor integers in polynomial time. However, Shor's algorithm shows that factoring integers can be done with a polynomial complexity circuit on an ideal quantum computer. Thus, it might be feasible to defeat RSA by constructing a large enough quantum computer. This was a powerful motivator for the design and construction of quantum computers, and for the study of new quantum-computer algorithms. It has also facilitated research on new cryptosystems that are secure from quantum computers, collectively called post-quantum cryptography (PQC).

### Physical implementation

As of 2026, the high error rates of quantum computers and limited number of physical qubits available for quantum error correction, laboratory demonstrations of Shor's algorithm obtain correct results in only a fraction of attempts, and have only succeeded with small semiprimes.

In 2001, Shor's algorithm was demonstrated by a group at IBM, who factored $15$ into $3\times 5$ , using an NMR implementation of a quantum computer with seven qubits. After IBM's implementation, two independent groups implemented Shor's algorithm using photonic qubits, emphasizing that multi-qubit entanglement was observed when running Shor's algorithm circuits. In 2012, the factorization of $15$ was performed with solid-state qubits. Later, in 2012, the factorization of $21$ was achieved. In 2016, the factorization of $15$ was performed again using trapped-ion qubits. However, none of these demonstrations fulfill the requirements of Shor’s algorithm: they compile the circuit using prior knowledge of the solution, and some have even oversimplified the algorithm in a way that makes it equivalent to coin flipping.

## Algorithm

The problem that we are trying to solve is: *given an odd composite number N , find its integer factors*.

To achieve this, Shor's algorithm consists of two parts:

1. A classical reduction of the factoring problem to the problem of order-finding. This reduction is similar to that used for other factoring algorithms, such as the quadratic sieve.
2. A quantum algorithm to solve the order-finding problem.

### Classical reduction

A complete factoring algorithm is possible if we're able to efficiently factor arbitrary N into just two integers p and q greater than 1, since if either p or q are not prime, then the factoring algorithm can in turn be run on those until only primes remain.

A basic observation is that, using Euclid's algorithm, we can always compute the GCD between two integers efficiently. In particular, this means we can check efficiently whether N is even, in which case 2 is trivially a factor. Let us thus assume that N is odd for the remainder of this discussion. Afterwards, we can use efficient classical algorithms to check whether N is a prime power. For prime powers, efficient classical factorization algorithms exist, hence the rest of the quantum algorithm may assume that N is not a prime power.

If those easy cases do not produce a nontrivial factor of N , the algorithm proceeds to handle the remaining case. We pick a random integer $2\leq a<N{.}$ A possible nontrivial divisor of N can be found by computing $\gcd(a,N)$ , which can be done classically and efficiently using the Euclidean algorithm. If this produces a nontrivial factor (meaning $\gcd(a,N)\neq 1$ ), the algorithm is finished, and the other nontrivial factor is $N/\gcd(a,N)$ . If a nontrivial factor was not identified, then this means that N and the choice of a are coprime, so a is contained in the multiplicative group of integers modulo N , having a multiplicative inverse modulo N . Thus, a has a multiplicative order r modulo N , meaning

$a^{r}\equiv 1{\bmod {N}},$

and r is the smallest positive integer satisfying this congruence.

The quantum subroutine finds r . It can be seen from the congruence that N divides $a^{r}-1$ , written $N\mid a^{r}-1$ . This can be factored using difference of squares: $N\mid (a^{r/2}-1)(a^{r/2}+1).$ Since we have factored the expression in this way, the algorithm doesn't work for odd r (because $a^{r/2}$ must be an integer), meaning that the algorithm would have to restart with a new a . Hereafter we can therefore assume that r is even. It cannot be the case that $N\mid a^{r/2}-1$ , since this would imply $a^{r/2}\equiv 1{\bmod {N}}$ , which would contradictorily imply that $r/2$ would be the order of a , which was already r . At this point, it may or may not be the case that $N\mid a^{r/2}+1$ . If N does not divide $a^{r/2}+1$ , then this means that we are able to find a nontrivial factor of N . We compute $d=\gcd(N,a^{r/2}-1).$ If $d=1$ , then $N\mid a^{r/2}+1$ was true, and a nontrivial factor of N cannot be achieved from a , and the algorithm must restart with a new a . Otherwise, we have found a nontrivial factor of N , with the other being $N/d$ , and the algorithm is finished. For this step, it is also equivalent to compute $\gcd(N,a^{r/2}+1)$ ; it will produce a nontrivial factor if $\gcd(N,a^{r/2}-1)$ is nontrivial, and will not if it's trivial (where $N\mid a^{r/2}+1$ ).

The algorithm restated shortly follows: let N be odd, and not a prime power. We want to output two nontrivial factors of N .

1. Pick a random number $1<a<N$ .
2. Compute $K=\gcd(a,N)$ , the greatest common divisor of a and N .
3. If $K\neq 1$ , then K is a nontrivial factor of N , with the other factor being $N/K$ , and we are done.
4. Otherwise, use the quantum subroutine to find the order r of a .
5. If r is odd, then go back to step 1.
6. Compute $g=\gcd(N,a^{r/2}+1)$ . If g is nontrivial, the other factor is $N/g$ , and we're done. Otherwise, go back to step 1.

It has been shown that this will be likely to succeed after a few runs. In practice, a single call to the quantum order-finding subroutine is enough to completely factor N with very high probability of success if one uses a more advanced reduction.

### Quantum order-finding subroutine

The goal of the quantum subroutine of Shor's algorithm is, given coprime integers N and $1<a<N$ , to find the order r of a modulo N , the smallest positive integer r such that $a^{r}\equiv 1{\pmod {N}}$ . To achieve this, Shor's algorithm uses a quantum circuit involving two registers. The second register uses n qubits, where n is the smallest integer such that $N\leq 2^{n}$ , i.e., $n=\left\lceil {\log _{2}N}\right\rceil$ . The size of the first register determines how accurate of an approximation the circuit produces. It can be shown that using $2n$ qubits gives sufficient accuracy to find r . The exact quantum circuit depends on the parameters a and N , which define the problem. The following description of the algorithm uses bra–ket notation to denote quantum states, and $\otimes$ to denote the tensor product.

The algorithm consists of two main steps:

1. Use quantum phase estimation with unitary matrix U representing the operation of multiplying by a (modulo N ), and input state $|0\rangle ^{\otimes 2n}\otimes |1\rangle$ (where the second register is $|1\rangle$ made from n qubits). The eigenvalues of this U encode information about the period, and $|1\rangle$ can be seen to be writable as a sum of its eigenvectors. Thanks to these properties, the quantum phase estimation stage gives as output a random integer of the form ${\frac {j}{r}}2^{2n}$ for random $j=0,1,...,r-1$ .
2. Use the continued fractions algorithm to extract the period r from the measurement outcomes obtained in the previous stage. This is a procedure to post-process (with a classical computer) the measurement data obtained from measuring the output quantum states, and retrieve the period.

The connection with quantum phase estimation was not discussed in the original formulation of Shor's algorithm, but was later proposed by Alexei Kitaev.

#### Quantum phase estimation

In general the quantum phase estimation algorithm, for any unitary U and eigenstate $|\psi \rangle$ such that $U|\psi \rangle =e^{2\pi i\theta }|\psi \rangle$ , sends input states $|0\rangle |\psi \rangle$ to output states close to $|\phi \rangle |\psi \rangle$ , where $\phi$ is a superposition of integers close to $2^{2n}\theta$ . In other words, it sends each eigenstate $|\psi _{j}\rangle$ of U to a state containing information close to the associated eigenvalue. For the purposes of quantum order-finding, we employ this strategy using the unitary defined by the action $U|k\rangle ={\begin{cases}|ak{\pmod {N}}\rangle &0\leq k<N,\\|k\rangle &N\leq k<2^{n}.\end{cases}}$ The action of U on states $|k\rangle$ with $N\leq k<2^{n}$ is not crucial to the functioning of the algorithm, but needs to be included to ensure that the overall transformation is a well-defined quantum gate. Implementing the circuit for quantum phase estimation with U requires being able to efficiently implement the gates $U^{2^{j}}$ . This can be accomplished via modular exponentiation, which is the slowest part of the algorithm.

The gate thus defined satisfies $U^{r}=I$ , which immediately implies that its eigenvalues are the r -th roots of unity $\omega _{r}^{k}=e^{2\pi ik/r}$ . Furthermore, each eigenvalue $\omega _{r}^{j}$ has an eigenvector of the form ${\textstyle |\psi _{j}\rangle =r^{-1/2}\sum _{k=0}^{r-1}\omega _{r}^{-kj}|a^{k}\rangle }$ , and these eigenvectors are such that ${\begin{aligned}{\frac {1}{\sqrt {r}}}\sum _{j=0}^{r-1}|\psi _{j}\rangle &={\frac {1}{r}}\sum _{j=0}^{r-1}\sum _{k=0}^{r-1}\omega _{r}^{jk}|a^{k}\rangle \\&=|1\rangle +{\frac {1}{r}}\sum _{k=1}^{r-1}\left(\sum _{j=0}^{r-1}\omega _{r}^{jk}\right)|a^{k}\rangle =|1\rangle ,\end{aligned}}$ where the last identity follows from the geometric series formula, which implies ${\textstyle \sum _{j=0}^{r-1}\omega _{r}^{jk}=0}$ .

Using quantum phase estimation on an input state $|0\rangle ^{\otimes 2n}|\psi _{j}\rangle$ would then return the integer $2^{2n}j/r$ with high probability. More precisely, the quantum phase estimation circuit sends $|0\rangle ^{\otimes 2n}|\psi _{j}\rangle$ to $|\phi _{j}\rangle |\psi _{j}\rangle$ such that the resulting probability distribution $p_{k}\equiv |\langle k|\phi _{j}\rangle |^{2}$ is peaked around $k=2^{2n}j/r$ , with $p_{2^{2n}j/r}\geq 4/\pi ^{2}\approx 0.4053$ . This probability can be made arbitrarily close to 1 using extra qubits.

Applying the above reasoning to the input $|0\rangle ^{\otimes 2n}|1\rangle$ , quantum phase estimation thus results in the evolution $|0\rangle ^{\otimes 2n}|1\rangle ={\frac {1}{\sqrt {r}}}\sum _{j=0}^{r-1}|0\rangle ^{\otimes 2n}|\psi _{j}\rangle \to {\frac {1}{\sqrt {r}}}\sum _{j=0}^{r-1}|\phi _{j}\rangle |\psi _{j}\rangle .$ Measuring the first register, we now have a balanced probability $1/r$ to find each $|\phi _{j}\rangle$ , each one giving an integer approximation to $2^{2n}j/r$ , which can be divided by $2^{2n}$ to get a decimal approximation for $j/r$ .

#### Continued-fraction algorithm to retrieve the period

Then, we apply the continued-fraction algorithm to find integers b and c , where $b/c$ gives the best fraction approximation for the approximation measured from the circuit, for $b,c<N$ and coprime b and c . The number of qubits in the first register, $2n$ , which determines the accuracy of the approximation, guarantees that ${\frac {b}{c}}={\frac {j}{r}},$ given the best approximation from the superposition of $|\phi _{j}\rangle$ was measured (which can be made arbitrarily likely by using extra bits and truncating the output). However, while b and c are coprime, it may be the case that j and r are not coprime. Because of that, b and c may have lost some factors that were in j and r . This can be remedied by rerunning the quantum order-finding subroutine an arbitrary number of times, to produce a list of fraction approximations ${\frac {b_{1}}{c_{1}}},{\frac {b_{2}}{c_{2}}},\ldots ,{\frac {b_{s}}{c_{s}}},$ where s is the number of times the subroutine was run. Each $c_{k}$ will have different factors taken out of it because the circuit will (likely) have measured multiple different possible values of j . To recover the actual r value, we can take the least common multiple of each $c_{k}$ : $\operatorname {lcm} (c_{1},c_{2},\ldots ,c_{s}).$ The least common multiple will be the order r of the original integer a with high probability. In practice, a single run of the quantum order-finding subroutine is in general enough if more advanced post-processing is used.

#### Choosing the size of the first register

Phase estimation requires choosing the size of the first register to determine the accuracy of the algorithm, and for the quantum subroutine of Shor's algorithm, $2n$ qubits is sufficient to guarantee that the optimal bitstring measured from phase estimation (meaning the $|k\rangle$ where ${\textstyle k/2^{2n}}$ is the most accurate approximation of the phase from phase estimation) will allow the actual value of r to be recovered.

Each $|\phi _{j}\rangle$ before measurement in Shor's algorithm represents a superposition of integers approximating $2^{2n}j/r$ . Let $|k\rangle$ represent the most optimal integer in $|\phi _{j}\rangle$ . The following theorem guarantees that the continued fractions algorithm will recover $j/r$ from $k/2^{2{n}}$ :

**Theorem**—If j and r are n bit integers, and $\left\vert {\frac {j}{r}}-\phi \right\vert \leq {\frac {1}{2r^{2}}}$ then the continued fractions algorithm run on $\phi$ will recover both ${\textstyle {\frac {j}{\gcd(j,\;r)}}}$ and ${\textstyle {\frac {r}{\gcd(j,\;r)}}}$ .

As k is the optimal bitstring from phase estimation, $k/2^{2{n}}$ is accurate to $j/r$ by $2n$ bits. Thus, $\left\vert {\frac {j}{r}}-{\frac {k}{2^{2n}}}\right\vert \leq {\frac {1}{2^{2{n}+1}}}\leq {\frac {1}{2N^{2}}}\leq {\frac {1}{2r^{2}}}$ which implies that the continued fractions algorithm will recover j and r (or with their greatest common divisor taken out).

### The bottleneck

The runtime bottleneck of Shor's algorithm is quantum modular exponentiation, which is by far slower than the quantum Fourier transform and classical pre-/post-processing. There are several approaches to constructing and optimizing circuits for modular exponentiation. The simplest and (currently) most practical approach is to mimic conventional arithmetic circuits with reversible gates, starting with ripple-carry adders. Knowing the base and the modulus of exponentiation facilitates further optimizations. Reversible circuits typically use on the order of $n^{3}$ gates for n qubits. Alternative techniques asymptotically improve gate counts by using quantum Fourier transforms, but are not competitive with fewer than 600 qubits owing to high constants.

## Period finding and discrete logarithms

Shor's algorithms for the discrete log and the order finding problems are instances of an algorithm solving the period finding problem. All three are instances of the hidden subgroup problem.

### Shor's algorithm for discrete logarithms

Given a group G with order p and generator $g\in G$ , suppose we know that $x=g^{r}\in G$ , for some $r\in \mathbb {Z} _{p}$ , and we wish to compute r , which is the discrete logarithm: $r={\log _{g}}(x)$ . Consider the abelian group $\mathbb {Z} _{p}\times \mathbb {Z} _{p}$ , where each factor corresponds to modular addition of values. Now, consider the function

$f\colon \mathbb {Z} _{p}\times \mathbb {Z} _{p}\to G\;;\;f(a,b)=g^{a}x^{-b}.$

This gives us an abelian hidden subgroup problem, where f corresponds to a group homomorphism. The kernel corresponds to the multiples of $(r,1)$ . So, if we can find the kernel, we can find r . A quantum algorithm for solving this problem exists. This algorithm is, like the factor-finding algorithm, due to Peter Shor and both are implemented by creating a superposition through using Hadamard gates, followed by implementing f as a quantum transform, followed finally by a quantum Fourier transform. Due to this, the quantum algorithm for computing the discrete logarithm is also occasionally referred to as "Shor's Algorithm."

The order-finding problem can also be viewed as a hidden subgroup problem. To see this, consider the group of integers under addition, and for a given $a\in \mathbb {Z}$ such that: $a^{r}=1$ , the function

$f\colon \mathbb {Z} \to \mathbb {Z} \;;\;f(x)=a^{x},\;f(x+r)=f(x).$

For any finite abelian group G , a quantum algorithm exists for solving the hidden subgroup for G in polynomial time.
