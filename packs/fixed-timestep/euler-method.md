---
title: "Euler method"
source: https://en.wikipedia.org/wiki/Euler_method
domain: fixed-timestep
license: CC-BY-SA-4.0
tags: fixed timestep, fixed time step, deterministic simulation step, physics timestep
fetched: 2026-07-02
---

# Euler method

In mathematics and computational science, the **Euler method** (also called the **forward Euler method**) is a first-order numerical procedure for solving ordinary differential equations (ODEs) with a given initial value. It is the most basic explicit method for numerical integration of ordinary differential equations and is the simplest Runge–Kutta method. The Euler method is named after Leonhard Euler, who first proposed it in his book *Institutionum calculi integralis* (published 1768–1770).

The Euler method is a first-order method, which means that the local error (error per step) is proportional to the square of the step size, and the global error (error at a given time) is proportional to the step size. The Euler method often serves as the basis to construct more complex methods, e.g., predictor–corrector method.

## Geometrical description

### Purpose and why it works

Consider the problem of calculating the shape of an unknown curve which starts at a given point and satisfies a given differential equation. Here, a differential equation can be thought of as a formula by which the slope of the tangent line to the curve can be computed at any point on the curve, once the position of that point has been calculated.

The idea is that while the curve is initially unknown, its starting point, which we denote by $A_{0},$ is known (see Figure 1). Then, from the differential equation, the slope to the curve at $A_{0}$ can be computed, and so, the tangent line.

Take a small step along that tangent line up to a point $A_{1}.$ Along this small step, the slope does not change too much, so $A_{1}$ will be close to the curve. If we pretend that $A_{1}$ is still on the curve, the same reasoning as for the point $A_{0}$ above can be used. After several steps, a polygonal curve ( $A_{0},A_{1},A_{2},A_{3},\dots$ ) is computed. In general, this curve does not diverge too far from the original unknown curve, and the error between the two curves can be made small if the step size is small enough and the interval of computation is finite.

### First-order process

When given the values for $t_{0}$ and $y(t_{0})$ , and the derivative of y is a given function of t and y denoted as $y'(t)=f\left(t,y(t)\right)$ . Begin the process by setting $y_{0}=y(t_{0})$ . Next, choose a value h for the size of every step along t-axis, and set $t_{n}=t_{0}+nh$ (or equivalently $t_{n+1}=t_{n}+h$ ). Now, the Euler method is used to find $y_{n+1}$ from $y_{n}$ and $t_{n}$ :

$y_{n+1}=y_{n}+hf(t_{n},y_{n}).$

The value of $y_{n}$ is an approximation of the solution at time $t_{n}$ , i.e., $y_{n}\approx y(t_{n})$ . The Euler method is explicit, i.e. the solution $y_{n+1}$ is an explicit function of $y_{i}$ for $i\leq n$ .

### Higher-order process

While the Euler method integrates a first-order ODE, any ODE of order N can be represented as a system of first-order ODEs. When given the ODE of order N defined as

$y^{(N+1)}(t)=f\left(t,y(t),y'(t),\ldots ,y^{(N)}(t)\right),$

as well as h , $t_{0}$ , and $y_{0},y'_{0},\dots ,y_{0}^{(N)}$ , we implement the following formula until we reach the approximation of the solution to the ODE at the desired time:

${\vec {y}}_{i+1}={\begin{pmatrix}y_{i+1}\\y'_{i+1}\\\vdots \\y_{i+1}^{(N-1)}\\y_{i+1}^{(N)}\end{pmatrix}}={\begin{pmatrix}y_{i}+h\cdot y'_{i}\\y'_{i}+h\cdot y''_{i}\\\vdots \\y_{i}^{(N-1)}+h\cdot y_{i}^{(N)}\\y_{i}^{(N)}+h\cdot f\left(t_{i},y_{i},y'_{i},\ldots ,y_{i}^{(N)}\right)\end{pmatrix}}$

These first-order systems can be handled by Euler's method or, in fact, by any other scheme for first-order systems.

## First-order example

Given the initial value problem

$y'=y,\quad y(0)=1,$

we would like to use the Euler method to approximate $y(4)$ .

### Using step size equal to 1 (*h* = 1)

The Euler method is

$y_{n+1}=y_{n}+hf(t_{n},y_{n}).$

so first we must compute $f(t_{0},y_{0})$ . In this simple differential equation, the function f is defined by $f(t,y)=y$ . We have

$f(t_{0},y_{0})=f(0,1)=1.$

By doing the above step, we have found the slope of the line that is tangent to the solution curve at the point $(0,1)$ . Recall that the slope is defined as the change in y divided by the change in t , or ${\textstyle {\frac {\Delta y}{\Delta t}}}$ .

The next step is to multiply the above value by the step size h , which we take equal to one here:

$h\cdot f(y_{0})=1\cdot 1=1.$

Since the step size is the change in t , when we multiply the step size and the slope of the tangent, we get a change in y value. This value is then added to the initial y value to obtain the next value to be used for computations.

$y_{0}+hf(y_{0})=y_{1}=1+1\cdot 1=2.$

The above steps should be repeated to find $y_{2}$ , $y_{3}$ and $y_{4}$ .

${\begin{aligned}y_{2}&=y_{1}+hf(y_{1})=2+1\cdot 2=4,\\y_{3}&=y_{2}+hf(y_{2})=4+1\cdot 4=8,\\y_{4}&=y_{3}+hf(y_{3})=8+1\cdot 8=16.\end{aligned}}$

Due to the repetitive nature of this algorithm, it can be helpful to organize computations in a chart form, as seen below, to avoid making errors.

| n | $y_{n}$ | $t_{n}$ | $f(t_{n},y_{n})$ | h | $\Delta y$ | $y_{n+1}$ |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 1 | 1 | 2 |
| 1 | 2 | 1 | 2 | 1 | 2 | 4 |
| 2 | 4 | 2 | 4 | 1 | 4 | 8 |
| 3 | 8 | 3 | 8 | 1 | 8 | 16 |

The conclusion of this computation is that $y_{4}=16$ . The exact solution of the differential equation is $y(t)=e^{t}$ , so $y(4)=e^{4}\approx 54.598$ . Although the approximation of the Euler method was not very precise in this specific case, particularly due to a large value step size h , its behaviour is qualitatively correct as the figure shows.

### Using other step sizes

As suggested in the introduction, the Euler method is more accurate if the step size h is smaller. The table below shows the result with different step sizes. The top row corresponds to the example in the previous section, and the second row is illustrated in the figure.

| step size | result of Euler's method | error |
|---|---|---|
| 1 | 16.00 | 38.60 |
| 0.25 | 35.53 | 19.07 |
| 0.1 | 45.26 | 09.34 |
| 0.05 | 49.56 | 05.04 |
| 0.025 | 51.98 | 02.62 |
| 0.0125 | 53.26 | 01.34 |

The error recorded in the last column of the table is the difference between the exact solution at $t=4$ and the Euler approximation. In the bottom of the table, the step size is half the step size in the previous row, and the error is also approximately half the error in the previous row. This suggests that the error is roughly proportional to the step size, at least for fairly small values of the step size. This is true in general, also for other equations; see the section *Global truncation error* for more details.

Other methods, such as the midpoint method also illustrated in the figures, behave more favourably: the global error of the midpoint method is roughly proportional to the *square* of the step size. For this reason, the Euler method is said to be a first-order method, while the midpoint method is second order.

We can extrapolate from the above table that the step size needed to get an answer that is correct to three decimal places is approximately 0.00001, meaning that we need 400,000 steps. This large number of steps entails a high computational cost. For this reason, higher-order methods are employed such as Runge–Kutta methods or linear multistep methods, especially if a high accuracy is desired.

## Higher-order example

For this third-order example, assume that the following information is given:

${\begin{aligned}&y'''+4ty''-t^{2}y'-(\cos {t})y=\sin {t}\\&t_{0}=0\\&y_{0}=y(t_{0})=2\\&y'_{0}=y'(t_{0})=-1\\&y''_{0}=y''(t_{0})=3\\&h=0.5\end{aligned}}$

From this we can isolate *y*''' to get the equation:

$y'''=f{\left(t,y,y',y''\right)}=\sin {t}+\left(\cos {t}\right)y+t^{2}y'-4ty''$

Using that we can get the solution for ${\vec {y}}_{1}$ : ${\begin{aligned}{\vec {y}}_{1}&={\begin{pmatrix}y_{1}\\y_{1}'\\y_{1}''\end{pmatrix}}={\begin{pmatrix}y_{0}\\y'_{0}\\y''_{0}\end{pmatrix}}+h{\begin{pmatrix}y'_{0}\\y''_{0}\\f{\left(t_{0},y_{0},y'_{0},y''_{0}\right)}\end{pmatrix}}\\[1ex]&={\begin{pmatrix}2\\-1\\3\end{pmatrix}}+0.5\cdot {\begin{pmatrix}-1\\3\\\sin {0}+(\cos {0})\cdot 2+0^{2}\cdot (-1)-4\cdot 0\cdot 3\end{pmatrix}}\\[1ex]&={\begin{pmatrix}1.5\\0.5\\4\end{pmatrix}}\end{aligned}}$ And using the solution for ${\vec {y}}_{1}$ , we can get the solution for ${\vec {y}}_{2}$ : ${\begin{aligned}{\vec {y}}_{2}&={\begin{pmatrix}y_{2}\\y_{2}'\\y_{2}''\end{pmatrix}}={\begin{pmatrix}y_{1}\\y'_{1}\\y''_{1}\end{pmatrix}}+h{\begin{pmatrix}y'_{1}\\y''_{1}\\f{\left(t_{1},y_{1},y'_{1},y''_{1}\right)}\end{pmatrix}}\\[1ex]&={\begin{pmatrix}1.5\\0.5\\4\end{pmatrix}}+0.5\cdot {\begin{pmatrix}0.5\\4\\\sin {0.5}+(\cos {0.5})\cdot 1.5+0.5^{2}\cdot 0.5-4\cdot 0.5\cdot 4\end{pmatrix}}\\[1ex]&={\begin{pmatrix}1.75\\2.5\\0.9604...\end{pmatrix}}\end{aligned}}$ We can continue this process using the same formula as long as necessary to find whichever ${\vec {y}}_{i}$ desired.

## Derivation

The Euler method can be derived in a number of ways.

1. Firstly, there is the geometrical description above.
2. Another possibility is to consider the Taylor expansion of the function y around $t_{0}$ : $y(t_{0}+h)=y(t_{0})+hy'(t_{0})+{\tfrac {1}{2}}h^{2}y''(t_{0})+O\left(h^{3}\right).$ The differential equation states that $y'=f(t,y)$ . If this is substituted in the Taylor expansion and the quadratic and higher-order terms are ignored, the Euler method arises. The Taylor expansion is used below to analyze the error committed by the Euler method, and it can be extended to produce Runge–Kutta methods.
3. A closely related derivation is to substitute the forward finite difference formula for the derivative, $y'(t_{0})\approx {\frac {y(t_{0}+h)-y(t_{0})}{h}}$ in the differential equation $y'=f(t,y)$ . Again, this yields the Euler method. A similar computation leads to the midpoint method and the backward Euler method.
4. Finally, one can integrate the differential equation from $t_{0}$ to $t_{0}+h$ and apply the fundamental theorem of calculus to get: $y(t_{0}+h)-y(t_{0})=\int _{t_{0}}^{t_{0}+h}f\left(t,y(t)\right)\,\mathrm {d} t.$ Now approximate the integral by the left-hand rectangle method (with only one rectangle): $\int _{t_{0}}^{t_{0}+h}f\left(t,y(t)\right)\,\mathrm {d} t\approx hf\left(t_{0},y(t_{0})\right).$ Combining both equations, one finds again the Euler method.

This line of thought can be continued to arrive at various linear multistep methods.

## Local truncation error

The local truncation error of the Euler method is the error made in a single step. It is the difference between the numerical solution after one step, $y_{1}$ , and the exact solution at time $t_{1}=t_{0}+h$ . The numerical solution is given by

$y_{1}=y_{0}+hf(t_{0},y_{0}).$

For the exact solution, we use the Taylor expansion mentioned in the section *Derivation* above:

$y(t_{0}+h)=y(t_{0})+hy'(t_{0})+{\tfrac {1}{2}}h^{2}y''(t_{0})+{\mathcal {O}}{\left(h^{3}\right)}.$

The local truncation error (LTE) introduced by the Euler method is given by the difference between these equations:

$\mathrm {LTE} =y(t_{0}+h)-y_{1}={\tfrac {1}{2}}h^{2}y''(t_{0})+{\mathcal {O}}{\left(h^{3}\right)}.$

This result is valid if y has a bounded third derivative.

This shows that for small h , the local truncation error is approximately proportional to $h^{2}$ . This makes the Euler method less accurate than higher-order techniques such as Runge–Kutta methods and linear multistep methods, for which the local truncation error is proportional to a higher power of the step size.

A slightly different formulation for the local truncation error can be obtained by using the Lagrange form for the remainder term in Taylor's theorem. If y has a continuous second derivative, then there exists a $\xi \in [t_{0},t_{0}+h]$ such that

$\mathrm {LTE} =y(t_{0}+h)-y_{1}={\tfrac {1}{2}}h^{2}y''(\xi ).$

In the above expressions for the error, the second derivative of the unknown exact solution y can be replaced by an expression involving the right-hand side of the differential equation. Indeed, it follows from the equation $y'=f(t,y)$ that

$y''(t_{0})={\frac {\partial f}{\partial t}}\left(t_{0},y(t_{0})\right)+{\frac {\partial f}{\partial y}}\left(t_{0},y(t_{0})\right)\,f\left(t_{0},y(t_{0})\right).$

## Global truncation error

The global truncation error is the error at a fixed time $t_{i}$ , after however many steps the method needs to take to reach that time from the initial time. The global truncation error is the cumulative effect of the local truncation errors committed in each step. The number of steps is easily determined to be ${\textstyle {\frac {t_{i}-t_{0}}{h}}}$ , which is proportional to ${\textstyle {\frac {1}{h}}}$ , and the error committed in each step is proportional to $h^{2}$ (see the previous section). Thus, it is to be expected that the global truncation error will be proportional to h .

This intuitive reasoning can be made precise. If the solution y has a bounded second derivative and f is Lipschitz continuous in its second argument, then the global truncation error (denoted as $|y(t_{i})-y_{i}|$ ) is bounded by

$\left|y(t_{i})-y_{i}\right|\leq {\frac {hM}{2L}}\left(e^{L(t_{i}-t_{0})}-1\right)$

where M is an upper bound on the second derivative of y on the given interval and L is the Lipschitz constant of f . Or more simply, when $y'(t)=f(t,y)$ , the value ${\textstyle L={\text{max}}\left(|{\frac {d}{dy}}\left[f(t,y)\right]|\right)}$ (such that t is treated as a constant). In contrast, ${\textstyle M=\max \left(\left|{\frac {d^{2}}{dt^{2}}}\left[y(t)\right]\right|\right)}$ where function $y(t)$ is the exact solution which only contains the t variable.

The precise form of this bound is of little practical importance, as in most cases the bound vastly overestimates the actual error committed by the Euler method. What is important is that it shows that the global truncation error is (approximately) proportional to h . For this reason, the Euler method is said to be first order.

### Example

If we have the differential equation $y'=1+(t-y)^{2}$ , and the exact solution $y=t+{\frac {1}{t-1}}$ , and we want to find M and L for when $2\leq t\leq 3$ . ${\begin{aligned}L&=\max \left|{\frac {d}{dy}}f(t,y)\right|=\max _{2\leq t\leq 3}\left|{\frac {d}{dy}}\left[1+\left(t-y\right)^{2}\right]\right|\\[1ex]&=\max _{2\leq t\leq 3}\left|2\left(t-y\right)\right|=\max _{2\leq t\leq 3}\left|2\left(t-\left[t+{\frac {1}{t-1}}\right]\right)\right|\\[1ex]&=\max _{2\leq t\leq 3}\left|-{\frac {2}{t-1}}\right|=2\end{aligned}}$ ${\begin{aligned}M&=\max \left|{\frac {d^{2}}{dt^{2}}}\left[y(t)\right]\right|\\&=\max _{2\leq t\leq 3}\left|{\frac {d^{2}}{dt^{2}}}\left(t+{\frac {1}{1-t}}\right)\right|\\&=\max _{2\leq t\leq 3}\left|{\frac {2}{\left(-t+1\right)^{3}}}\right|=2\end{aligned}}$ Thus we can find the error bound at *t*=2.5 and *h*=0.5:

${\begin{aligned}{\text{error bound}}&={\frac {hM}{2L}}\left(e^{L(t_{i}-t_{0})}-1\right)\\[1ex]&={\frac {0.5\cdot 2}{2\cdot 2}}\left(e^{2(2.5-2)}-1\right)=0.42957\end{aligned}}$ Notice that *t*0 is equal to 2 because it is the lower bound for t in $2\leq t\leq 3$ .

## Numerical stability

The Euler method can also be numerically unstable, especially for stiff equations, meaning that the numerical solution grows very large for equations where the exact solution does not. This can be illustrated using the linear equation $y'=-2.3y,\qquad y(0)=1.$ The exact solution is $y(t)=e^{-2.3t}$ , which decays to zero as $t\to \infty$ . However, if the Euler method is applied to this equation with step size $h=1$ , then the numerical solution is qualitatively wrong: It oscillates and grows (see the figure). This is what it means to be unstable. If a smaller step size is used, for instance $h=0.7$ , then the numerical solution does decay to zero.

If the Euler method is applied to the linear equation $y'=ky$ , then the numerical solution is unstable if the product $hk$ is outside the region $\left\{z\in \mathbf {C} \,{\big |}\,|z+1|\leq 1\right\},$ illustrated on the right. This region is called the (linear) *stability region*. In the example, $k=-2.3$ , so if $h=1$ then $hk=-2.3$ which is outside the stability region, and thus the numerical solution is unstable.

This limitation — along with its slow convergence of error with h — means that the Euler method is not often used, except as a simple example of numerical integration. Frequently models of physical systems contain terms representing fast-decaying elements (i.e. with large negative exponential arguments). Even when these are not of interest in the overall solution, the instability they can induce means that an exceptionally small timestep would be required if the Euler method is used.

## Rounding errors

In step n of the Euler method, the rounding error is roughly of the magnitude $\varepsilon y_{n}$ where $\varepsilon$ is the machine epsilon. Assuming that the rounding errors are independent random variables, the expected total rounding error is proportional to ${\textstyle {\frac {\varepsilon }{\sqrt {h}}}}$ . Thus, for extremely small values of the step size the truncation error will be small but the effect of rounding error may be big. Most of the effect of rounding error can be easily avoided if compensated summation is used in the formula for the Euler method.

## Modifications and extensions

A simple modification of the Euler method which eliminates the stability problems noted above is the backward Euler method: $y_{n+1}=y_{n}+hf(t_{n+1},y_{n+1}).$ This differs from the (standard, or forward) Euler method in that the function f is evaluated at the end point of the step, instead of the starting point. The backward Euler method is an implicit method, meaning that the formula for the backward Euler method has $y_{n+1}$ on both sides, so when applying the backward Euler method we have to solve an equation. This makes the implementation more costly.

Other modifications of the Euler method that help with stability yield the exponential Euler method or the semi-implicit Euler method.

More complicated methods can achieve a higher order (and more accuracy). One possibility is to use more function evaluations. This is illustrated by the midpoint method which is already mentioned in this article: $y_{n+1}=y_{n}+hf\left(t_{n}+{\tfrac {1}{2}}h,y_{n}+{\tfrac {1}{2}}hf(t_{n},y_{n})\right).$ This leads to the family of Runge–Kutta methods.

The other possibility is to use more past values, as illustrated by the two-step Adams–Bashforth method: $y_{n+1}=y_{n}+{\tfrac {3}{2}}hf(t_{n},y_{n})-{\tfrac {1}{2}}hf(t_{n-1},y_{n-1}).$ This leads to the family of linear multistep methods. There are other modifications which uses techniques from compressive sensing to minimize memory usage

## In popular culture

In the film *Hidden Figures*, Katherine Johnson resorts to the Euler method in calculating the re-entry of astronaut John Glenn from Earth orbit.
