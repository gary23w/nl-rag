---
title: "Watson's lemma"
source: https://en.wikipedia.org/wiki/Watson%27s_lemma
domain: asymptotic-analysis
license: CC-BY-SA-4.0
tags: asymptotic analysis, asymptotic expansion, steepest descent, borel summation
fetched: 2026-07-02
---

# Watson's lemma

In mathematics, **Watson's lemma**, proved by G. N. Watson (1918, p. 133), has significant application within the theory on the asymptotic behavior of integrals.

## Statement of the lemma

Let $0<T\leq \infty$ be fixed. Assume $\varphi (t)=t^{\lambda }\,g(t)$ , where $g(t)$ has an infinite number of derivatives in the neighborhood of $t=0$ , with $g(0)\neq 0$ , and $\lambda >-1$ .

Suppose, in addition, either that

$|\varphi (t)|<Ke^{bt}\ \forall t>0,$

where $K,b$ are independent of t , or that

$\int _{0}^{T}|\varphi (t)|\,\mathrm {d} t<\infty .$

Then, it is true that for all positive x that

$\left|\int _{0}^{T}e^{-xt}\varphi (t)\,\mathrm {d} t\right|<\infty$

and that the following asymptotic equivalence holds:

$\int _{0}^{T}e^{-xt}\varphi (t)\,\mathrm {d} t\sim \ \sum _{n=0}^{\infty }{\frac {g^{(n)}(0)\ \Gamma (\lambda +n+1)}{n!\ x^{\lambda +n+1}}},\ \ (x>0,\ x\rightarrow \infty ).$

See, for instance, Watson (1918) for the original proof or Miller (2006) for a more recent development.

## Proof

We will prove the version of Watson's lemma which assumes that $|\varphi (t)|$ has at most exponential growth as $t\to \infty$ . The basic idea behind the proof is that we will approximate $g(t)$ by finitely many terms of its Taylor series. Since the derivatives of g are only assumed to exist in a neighborhood of the origin, we will essentially proceed by removing the tail of the integral, applying Taylor's theorem with remainder in the remaining small interval, then adding the tail back on in the end. At each step we will carefully estimate how much we are throwing away or adding on. This proof is a modification of the one found in Miller (2006).

Let $0<T\leq \infty$ and suppose that $\varphi$ is a measurable function of the form $\varphi (t)=t^{\lambda }g(t)$ , where $\lambda >-1$ and g has an infinite number of continuous derivatives in the interval $[0,\delta ]$ for some $0<\delta <T$ , and that $|\varphi (t)|\leq Ke^{bt}$ for all $\delta \leq t\leq T$ , where the constants K and b are independent of t .

We can show that the integral is finite for x large enough by writing

$(1)\quad \int _{0}^{T}e^{-xt}\varphi (t)\,\mathrm {d} t=\int _{0}^{\delta }e^{-xt}\varphi (t)\,\mathrm {d} t+\int _{\delta }^{T}e^{-xt}\varphi (t)\,\mathrm {d} t$

and estimating each term.

For the first term we have

$\left|\int _{0}^{\delta }e^{-xt}\varphi (t)\,\mathrm {d} t\right|\leq \int _{0}^{\delta }e^{-xt}|\varphi (t)|\,\mathrm {d} t\leq \int _{0}^{\delta }|\varphi (t)|\,\mathrm {d} t$

for $x\geq 0$ , where the last integral is finite by the assumptions that g is continuous on the interval $[0,\delta ]$ and that $\lambda >-1$ . For the second term we use the assumption that $\varphi$ is exponentially bounded to see that, for $x>b$ ,

${\begin{aligned}\left|\int _{\delta }^{T}e^{-xt}\varphi (t)\,\mathrm {d} t\right|&\leq \int _{\delta }^{T}e^{-xt}|\varphi (t)|\,\mathrm {d} t\\&\leq K\int _{\delta }^{T}e^{(b-x)t}\,\mathrm {d} t\\&\leq K\int _{\delta }^{\infty }e^{(b-x)t}\,\mathrm {d} t\\&=K\,{\frac {e^{(b-x)\delta }}{x-b}}.\end{aligned}}$

The finiteness of the original integral then follows from applying the triangle inequality to $(1)$ .

We can deduce from the above calculation that

$(2)\quad \int _{0}^{T}e^{-xt}\varphi (t)\,\mathrm {d} t=\int _{0}^{\delta }e^{-xt}\varphi (t)\,\mathrm {d} t+O\left(x^{-1}e^{-\delta x}\right)$

as $x\to \infty$ .

By appealing to Taylor's theorem with remainder we know that, for each integer $N\geq 0$ ,

$g(t)=\sum _{n=0}^{N}{\frac {g^{(n)}(0)}{n!}}\,t^{n}+{\frac {g^{(N+1)}(t^{*})}{(N+1)!}}\,t^{N+1}$

for $0\leq t\leq \delta$ , where $0\leq t^{*}\leq t$ . Plugging this in to the first term in $(2)$ we get

${\begin{aligned}(3)\quad \int _{0}^{\delta }e^{-xt}\varphi (t)\,\mathrm {d} t&=\int _{0}^{\delta }e^{-xt}t^{\lambda }g(t)\,\mathrm {d} t\\&=\sum _{n=0}^{N}{\frac {g^{(n)}(0)}{n!}}\int _{0}^{\delta }t^{\lambda +n}e^{-xt}\,\mathrm {d} t+{\frac {1}{(N+1)!}}\int _{0}^{\delta }g^{(N+1)}(t^{*})\,t^{\lambda +N+1}e^{-xt}\,\mathrm {d} t.\end{aligned}}$

To bound the term involving the remainder we use the assumption that $g^{(N+1)}$ is continuous on the interval $[0,\delta ]$ , and in particular it is bounded there. As such we see that

${\begin{aligned}\left|\int _{0}^{\delta }g^{(N+1)}(t^{*})\,t^{\lambda +N+1}e^{-xt}\,\mathrm {d} t\right|&\leq \sup _{t\in [0,\delta ]}\left|g^{(N+1)}(t)\right|\int _{0}^{\delta }t^{\lambda +N+1}e^{-xt}\,\mathrm {d} t\\&<\sup _{t\in [0,\delta ]}\left|g^{(N+1)}(t)\right|\int _{0}^{\infty }t^{\lambda +N+1}e^{-xt}\,\mathrm {d} t\\&=\sup _{t\in [0,\delta ]}\left|g^{(N+1)}(t)\right|\,{\frac {\Gamma (\lambda +N+2)}{x^{\lambda +N+2}}}.\end{aligned}}$

Here we have used the fact that

$\int _{0}^{\infty }t^{a}e^{-xt}\,\mathrm {d} t={\frac {\Gamma (a+1)}{x^{a+1}}}$

if $x>0$ and $a>-1$ , where $\Gamma$ is the gamma function.

From the above calculation we see from $(3)$ that

$(4)\quad \int _{0}^{\delta }e^{-xt}\varphi (t)\,\mathrm {d} t=\sum _{n=0}^{N}{\frac {g^{(n)}(0)}{n!}}\int _{0}^{\delta }t^{\lambda +n}e^{-xt}\,\mathrm {d} t+O\left(x^{-\lambda -N-2}\right)$

as $x\to \infty$ .

We will now add the tails on to each integral in $(4)$ . For each n we have

${\begin{aligned}\int _{0}^{\delta }t^{\lambda +n}e^{-xt}\,\mathrm {d} t&=\int _{0}^{\infty }t^{\lambda +n}e^{-xt}\,\mathrm {d} t-\int _{\delta }^{\infty }t^{\lambda +n}e^{-xt}\,\mathrm {d} t\\[5pt]&={\frac {\Gamma (\lambda +n+1)}{x^{\lambda +n+1}}}-\int _{\delta }^{\infty }t^{\lambda +n}e^{-xt}\,\mathrm {d} t,\end{aligned}}$

and we will show that the remaining integrals are exponentially small. Indeed, if we make the change of variables $t=s+\delta$ we get

${\begin{aligned}\int _{\delta }^{\infty }t^{\lambda +n}e^{-xt}\,\mathrm {d} t&=\int _{0}^{\infty }(s+\delta )^{\lambda +n}e^{-x(s+\delta )}\,\mathrm {d} s\\[5pt]&=e^{-\delta x}\int _{0}^{\infty }(s+\delta )^{\lambda +n}e^{-xs}\,\mathrm {d} s\\[5pt]&\leq e^{-\delta x}\int _{0}^{\infty }(s+\delta )^{\lambda +n}e^{-s}\,\mathrm {d} s\end{aligned}}$

for $x\geq 1$ , so that

$\int _{0}^{\delta }t^{\lambda +n}e^{-xt}\,\mathrm {d} t={\frac {\Gamma (\lambda +n+1)}{x^{\lambda +n+1}}}+O\left(e^{-\delta x}\right){\text{ as }}x\to \infty .$

If we substitute this last result into $(4)$ we find that

${\begin{aligned}\int _{0}^{\delta }e^{-xt}\varphi (t)\,\mathrm {d} t&=\sum _{n=0}^{N}{\frac {g^{(n)}(0)\ \Gamma (\lambda +n+1)}{n!\ x^{\lambda +n+1}}}+O\left(e^{-\delta x}\right)+O\left(x^{-\lambda -N-2}\right)\\&=\sum _{n=0}^{N}{\frac {g^{(n)}(0)\ \Gamma (\lambda +n+1)}{n!\ x^{\lambda +n+1}}}+O\left(x^{-\lambda -N-2}\right)\end{aligned}}$

as $x\to \infty$ . Finally, substituting this into $(2)$ we conclude that

${\begin{aligned}\int _{0}^{T}e^{-xt}\varphi (t)\,\mathrm {d} t&=\sum _{n=0}^{N}{\frac {g^{(n)}(0)\ \Gamma (\lambda +n+1)}{n!\ x^{\lambda +n+1}}}+O\left(x^{-\lambda -N-2}\right)+O\left(x^{-1}e^{-\delta x}\right)\\&=\sum _{n=0}^{N}{\frac {g^{(n)}(0)\ \Gamma (\lambda +n+1)}{n!\ x^{\lambda +n+1}}}+O\left(x^{-\lambda -N-2}\right)\end{aligned}}$

as $x\to \infty$ .

Since this last expression is true for each integer $N\geq 0$ we have thus shown that

$\int _{0}^{T}e^{-xt}\varphi (t)\,\mathrm {d} t\sim \sum _{n=0}^{\infty }{\frac {g^{(n)}(0)\ \Gamma (\lambda +n+1)}{n!\ x^{\lambda +n+1}}}$

as $x\to \infty$ , where the infinite series is interpreted as an asymptotic expansion of the integral in question.

## Example

When $0<a<b$ , the confluent hypergeometric function of the first kind has the integral representation

${}_{1}F_{1}(a,b,x)={\frac {\Gamma (b)}{\Gamma (a)\Gamma (b-a)}}\int _{0}^{1}e^{xt}t^{a-1}(1-t)^{b-a-1}\,\mathrm {d} t,$

where $\Gamma$ is the gamma function. The change of variables $t=1-s$ puts this into the form

${}_{1}F_{1}(a,b,x)={\frac {\Gamma (b)}{\Gamma (a)\Gamma (b-a)}}\,e^{x}\int _{0}^{1}e^{-xs}(1-s)^{a-1}s^{b-a-1}\,ds,$

which is now amenable to the use of Watson's lemma. Taking $\lambda =b-a-1$ and $g(s)=(1-s)^{a-1}$ , Watson's lemma tells us that

$\int _{0}^{1}e^{-xs}(1-s)^{a-1}s^{b-a-1}\,ds\sim \Gamma (b-a)x^{a-b}\quad {\text{as }}x\to \infty {\text{ with }}x>0,$

which allows us to conclude that

${}_{1}F_{1}(a,b,x)\sim {\frac {\Gamma (b)}{\Gamma (a)}}\,x^{a-b}e^{x}\quad {\text{as }}x\to \infty {\text{ with }}x>0.$
