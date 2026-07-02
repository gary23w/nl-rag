---
title: "Michaelis–Menten kinetics"
source: https://en.wikipedia.org/wiki/Michaelis%E2%80%93Menten_kinetics
domain: enzymology
license: CC-BY-SA-4.0
tags: enzyme kinetics, michaelis menten, enzyme catalysis, enzyme inhibitor
fetched: 2026-07-02
---

# Michaelis–Menten kinetics

In biochemistry, **Michaelis–Menten kinetics**, named after Leonor Michaelis and Maud Menten, is the simplest case of enzyme kinetics, applied to enzyme-catalysed reactions involving the transformation of one substrate into one product. In 1913, Michaelis and Menten expanded on Victor Henri's fundamental equation of enzyme kinetics, which was established in 1902. It takes the form of a differential equation describing the reaction rate v (rate of formation of product P, with concentration p ) as a function of a , the concentration of the substrate A (using the symbols recommended by the IUBMB). The formula below is given by the **Michaelis–Menten equation**:

$v={\frac {\mathrm {d} p}{\mathrm {d} t}}={\frac {Va}{K_{\mathrm {m} }+a}}$

.

V , which is often written as $V_{\max }$ , represents the limiting rate approached by the system at saturating substrate concentration for a given enzyme concentration. The **Michaelis constant** $K_{\mathrm {m} }$ has units of concentration, and for a given reaction is equal to the concentration of substrate at which the reaction rate is half of V . Biochemical reactions involving a single substrate are often assumed to follow Michaelis–Menten kinetics, without regard to the model's underlying assumptions. Only a small proportion of enzyme-catalysed reactions have just one substrate, but the equation still often applies if only one substrate concentration is varied.

## Michaelis–Menten plot

The plot of v against a has often been called a "Michaelis–Menten plot", even recently, but this terminology is historically misleading, as Michaelis and Menten did not use such a plot. Instead, they plotted v against $\log a$ , which has some advantages over the usual ways of plotting Michaelis–Menten data. If v is the dependent variable, then it does not distort any experimental errors in v . Michaelis and Menten did not attempt to estimate V directly from the limit approached at high $\log a$ , something difficult to do accurately with data obtained with modern techniques, and almost impossible with their data. Instead they took advantage of the fact that the curve is almost straight in the middle range and has a maximum slope of $0.576V$ i.e. $0.25\ln 10\cdot V$ . With an accurate value of V it was easy to determine $\log K_{\mathrm {m} }$ from the point on the curve corresponding to $0.5V$ .

This plot is virtually never used today for estimating V and $K_{\mathrm {m} }$ , but it remains valuable to compare the properties of several enzymes across a broad range of substrate concentrations - such as isoenzymes. For example, the four mammalian isoenzymes of hexokinase are half-saturated by glucose at concentrations ranging from about 0.02 mM for hexokinase A (brain hexokinase) to about 50 mM for hexokinase D ("glucokinase", liver hexokinase), spanning a 2500-fold range. A conventional (linear) plot would compromise on readability for the high-affinity isoenzyme graphs, but a semi-logarithmic plot allows to read off the kinetic parameters for all isoenzymes.

## Model

A decade before Michaelis and Menten, Victor Henri found that enzyme reactions could be explained by assuming a binding interaction between the enzyme and the substrate. His work was taken up by Michaelis and Menten, who investigated the kinetics of invertase, an enzyme that catalyzes the hydrolysis of sucrose into glucose and fructose. In 1913, they proposed a mathematical model of the reaction. It involves an enzyme E binding to a substrate A to form a complex EA that releases a product P regenerating the original form of the enzyme. This may be represented schematically as

${\ce {E{}+A<=>[{\mathit {k_{\mathrm {+1} }}}][{\mathit {k_{\mathrm {-1} }}}]EA->[k_{\ce {cat}}]E{}+P}}$

where $k_{\mathrm {+1} }$ (forward rate constant), $k_{\mathrm {-1} }$ (reverse rate constant), and $k_{\mathrm {cat} }$ (catalytic rate constant) denote the rate constants, the double arrows between A (substrate) and EA (enzyme-substrate complex) represent the fact that enzyme-substrate binding is a reversible process, and the single forward arrow represents the formation of P (product).

Under certain assumptions – such as the enzyme concentration being much less than the substrate concentration – the rate of product formation is given by

$v={\frac {\mathrm {d} p}{\mathrm {d} t}}={\frac {V_{\max }a}{K_{\mathrm {m} }+a}}={\frac {k_{\mathrm {cat} }e_{0}a}{K_{\mathrm {m} }+a}}$

in which $e_{0}$ is the initial enzyme concentration. The reaction order depends on the relative size of the two terms in the denominator. At low substrate concentration $a\ll K_{\mathrm {m} }$ , so that the rate $v={\frac {k_{\mathrm {cat} }e_{0}a}{K_{\mathrm {m} }}}$ varies linearly with substrate concentration a (first-order kinetics in a ). However at higher a , with $a\gg K_{\mathrm {m} }$ , the reaction approaches independence of a (zero-order kinetics in a ), asymptotically approaching the limiting rate $V_{\mathrm {max} }=k_{\mathrm {cat} }e_{0}$ . This rate, which is never attained, refers to the hypothetical case in which all enzyme molecules are bound to substrate. $k_{\mathrm {cat} }$ , known as the turnover number or catalytic constant, normally expressed in s –1, is the limiting number of substrate molecules converted to product per enzyme molecule per unit of time. Further addition of substrate would not increase the rate, and the enzyme is said to be saturated.

The Michaelis constant $K_{\mathrm {m} }$ is not affected by the concentration or purity of an enzyme. Its value depends both on the identity of the enzyme and that of the substrate, as well as conditions such as temperature and pH.

The model is used in a variety of biochemical situations other than enzyme-substrate interaction, including antigen–antibody binding, DNA–DNA hybridization, and protein–protein interaction. It can be used to characterize a generic biochemical reaction, in the same way that the Langmuir equation can be used to model generic adsorption of biomolecular species. When an empirical equation of this form is applied to microbial growth, it is sometimes called a Monod equation.

Michaelis–Menten kinetics have also been applied to a variety of topics outside of biochemical reactions, including alveolar clearance of dusts, the richness of species pools, clearance of blood alcohol, the photosynthesis-irradiance relationship, and bacterial phage infection.

The equation can also be used to describe the relationship between ion channel conductivity and ligand concentration, and also, for example, to limiting nutrients and phytoplankton growth in the global ocean.

### Specificity

The specificity constant $k_{\text{cat}}/K_{\mathrm {m} }$ (also known as the *catalytic efficiency*) is a measure of how efficiently an enzyme converts a substrate into product. Although it is the ratio of $k_{\text{cat}}$ and $K_{\mathrm {m} }$ it is a parameter in its own right, more fundamental than $K_{\mathrm {m} }$ . Diffusion limited enzymes, such as fumarase, work at the theoretical upper limit of 108 – 1010 M−1s−1, limited by diffusion of substrate into the active site.

If we symbolize the specificity constant for a particular substrate A as $k_{\mathrm {A} }=k_{\text{cat}}/K_{\mathrm {m} }$ the Michaelis–Menten equation can be written in terms of $k_{\mathrm {A} }$ and $K_{\mathrm {m} }$ as follows:

$v={\dfrac {k_{\mathrm {A} }e_{0}a}{1+{\dfrac {a}{K_{\mathrm {m} }}}}}$

At small values of the substrate concentration this approximates to a first-order dependence of the rate on the substrate concentration:

$v\approx k_{\mathrm {A} }e_{0}a{\text{ when }}a\rightarrow 0$

Conversely it approaches a zero-order dependence on a when the substrate concentration is high:

$v\rightarrow k_{\mathrm {cat} }e_{0}{\text{ when }}a\rightarrow \infty$

The capacity of an enzyme to distinguish between two competing substrates that both follow Michaelis–Menten kinetics depends only on the specificity constant, and not on either $k_{\text{cat}}$ or $K_{\mathrm {m} }$ alone. Putting $k_{\mathrm {A} }$ for substrate $\mathrm {A}$ and $k_{\mathrm {A'} }$ for a competing substrate $\mathrm {A'}$ , then the two rates when both are present simultaneously are as follows:

$v_{\mathrm {A} }={\frac {k_{\mathrm {A} }e_{0}a}{1+{\dfrac {a}{K_{\mathrm {m} }^{\mathrm {A} }}}+{\dfrac {a'}{K_{\mathrm {m} }^{\mathrm {A'} }}}}},\;\;\;v_{\mathrm {A'} }={\frac {k_{\mathrm {A'} }e_{0}a'}{1+{\dfrac {a}{K_{\mathrm {m} }^{\mathrm {A} }}}+{\dfrac {a'}{K_{\mathrm {m} }^{\mathrm {A'} }}}}}$

Although both denominators contain the Michaelis constants they are the same, and thus cancel when one equation is divided by the other:

${\frac {v_{\mathrm {A} }}{v_{\mathrm {A'} }}}={\frac {k_{\mathrm {A} }\cdot a}{k_{\mathrm {A'} }\cdot a'}}$

and so the ratio of rates depends only on the concentrations of the two substrates and their specificity constants.

### Nomenclature

As the equation originated with Henri, not with Michaelis and Menten, it is more accurate to call it the Henri–Michaelis–Menten equation, though it was Michaelis and Menten who realized that analysing reactions in terms of initial rates would be simpler, and as a result more productive, than analysing the time course of reaction, as Henri had attempted. Although Henri derived the equation he made no attempt to apply it. In addition, Michaelis and Menten understood the need for buffers to control the pH, but Henri did not.

## Applications

Parameter values vary widely between enzymes. Some examples are as follows:

| Enzyme | $K_{\mathrm {m} }$ (M) | $k_{\text{cat}}$ (s−1) | $k_{\text{cat}}/K_{\mathrm {m} }$ (M−1s−1) |
|---|---|---|---|
| Chymotrypsin | 1.5 × 10−2 | 0.14 | 9.3 |
| Pepsin | 3.0 × 10−4 | 0.50 | 1.7 × 103 |
| tRNA synthetase | 9.0 × 10−4 | 7.6 | 8.4 × 103 |
| Ribonuclease | 7.9 × 10−3 | 7.9 × 102 | 1.0 × 105 |
| Carbonic anhydrase | 2.6 × 10−2 | 4.0 × 105 | 1.5 × 107 |
| Fumarase | 5.0 × 10−6 | 8.0 × 102 | 1.6 × 108 |

## Derivation

### Equilibrium approximation

In their analysis, Michaelis and Menten (and also Henri) assumed that the substrate is in instantaneous chemical equilibrium with the complex, which implies

$k_{+1}ea=k_{-1}x$

in which *e* is the concentration of free enzyme (not the total concentration) and *x* is the concentration of enzyme-substrate complex EA.

Conservation of enzyme requires that

$e=e_{0}-x$

where $e_{0}$ is now the total enzyme concentration. After combining the two expressions some straightforward algebra leads to the following expression for the concentration of the enzyme-substrate complex:

$x={\frac {e_{0}a}{K_{\mathrm {diss} }+a}}$

where $K_{\mathrm {diss} }=k_{-1}/k_{+1}$ is the dissociation constant of the enzyme-substrate complex. Hence the rate equation is the Michaelis–Menten equation,

$v={\frac {k_{+2}e_{0}a}{K_{\mathrm {diss} }+a}}$

where $k_{+2}$ corresponds to the catalytic constant $k_{\mathrm {cat} }$ and the limiting rate is $V_{\mathrm {max} }=k_{+2}e_{0}=k_{\mathrm {cat} }e_{0}$ . Likewise with the assumption of equilibrium the Michaelis constant $K_{\mathrm {m} }=K_{\mathrm {diss} }$ .

### Irreversible first step

When studying urease at about the same time as Michaelis and Menten were studying invertase, Donald Van Slyke and G. E. Cullen made essentially the opposite assumption, treating the first step not as an equilibrium but as an irreversible second-order reaction with rate constant $k_{+1}$ . As their approach is never used today it is sufficient to give their final rate equation:

$v={\frac {k_{\mathrm {+2} }e_{0}a}{k_{+2}/k_{+1}+a}}$

and to note that it is functionally indistinguishable from the Henri–Michaelis–Menten equation. One cannot tell from inspection of the kinetic behaviour whether $K_{\mathrm {m} }$ is equal to $k_{+2}/k_{+1}$ or to $k_{-1}/k_{+1}$ or to something else.

### Steady-state approximation

G. E. Briggs and J. B. S. Haldane undertook an analysis that harmonized the approaches of Michaelis and Menten and of Van Slyke and Cullen, and is taken as the basic approach to enzyme kinetics today. They assumed that the concentration of the intermediate complex does not change on the time scale over which product formation is measured. This assumption means that $k_{+1}ea=k_{-1}x+k_{\mathrm {cat} }x=(k_{-1}+k_{\mathrm {cat} })x$ . The resulting rate equation is as follows:

$v={\frac {k_{\mathrm {cat} }e_{0}a}{K_{\mathrm {m} }+a}}$

where

$k_{\mathrm {cat} }=k_{+2}{\text{ and }}K_{\mathrm {m} }={\frac {k_{-1}+k_{\mathrm {cat} }}{k_{+1}}}$

This is the generalized definition of the Michaelis constant.

### Assumptions and limitations

All of the derivations given treat the initial binding step in terms of the law of mass action, which assumes free diffusion through the solution. However, in the environment of a living cell where there is a high concentration of proteins, the cytoplasm often behaves more like a viscous gel than a free-flowing liquid, limiting molecular movements by diffusion and altering reaction rates. Although this gel-like structure severely restricts large molecules like proteins, its effect on small molecules, like many of the metabolites that participate in central metabolism, is very much smaller. In practice, therefore, treating the movement of substrates in terms of diffusion is not likely to produce major errors. Nonetheless, Schnell and Turner consider it more appropriate to model the cytoplasm as a fractal, in order to capture its limited-mobility kinetics.

## Estimation of Michaelis–Menten parameters

### Graphical methods

Determining the parameters of the Michaelis–Menten equation typically involves running a series of enzyme assays at varying substrate concentrations a , and measuring the initial reaction rates v , i.e. the reaction rates are measured after a time period short enough for it to be assumed that the enzyme-substrate complex has formed, but that the substrate concentration remains almost constant, and so the equilibrium or quasi-steady-state approximation remain valid. By plotting reaction rate against concentration, and using nonlinear regression of the Michaelis–Menten equation with correct weighting based on known error distribution properties of the rates, the parameters may be obtained.

Before computing facilities to perform nonlinear regression became available, graphical methods involving linearisation of the equation were used. A number of these were proposed, including the Eadie–Hofstee plot of v against $v/a$ , the Hanes plot of $a/v$ against a , and the Lineweaver–Burk plot (also known as the double-reciprocal plot) of $1/v$ against $1/a$ . Of these, the Hanes plot is the most accurate when v is subject to errors with uniform standard deviation. From the point of view of visualizaing the data the Eadie–Hofstee plot has an important property: the entire possible range of v values from 0 to V occupies a finite range of ordinate scale, making it impossible to choose axes that conceal a poor experimental design.

However, while useful for visualization, all three linear plots distort the error structure of the data and provide less precise estimates of v and $K_{\mathrm {m} }$ than correctly weighted non-linear regression. Assuming an error $\varepsilon (v)$ on v , an inverse representation leads to an error of $\varepsilon (v)/v^{2}$ on $1/v$ (Propagation of uncertainty), implying that linear regression of the double-reciprocal plot should include weights of $v^{4}$ . This was well understood by Lineweaver and Burk, who had consulted the eminent statistician W. Edwards Deming before analysing their data. Unlike nearly all workers since, Burk made an experimental study of the error distribution, finding it consistent with a uniform standard error in v , before deciding on the appropriate weights. This aspect of the work of Lineweaver and Burk received virtually no attention at the time, and was subsequently forgotten.

The direct linear plot is a graphical method in which the observations are represented by straight lines in parameter space, with axes $K_{\mathrm {m} }$ and V : each line is drawn with an intercept of $-a$ on the $K_{\mathrm {m} }$ axis and v on the V axis. The point of intersection of the lines for different observations yields the values of $K_{\mathrm {m} }$ and V .

### Weighting

Many authors, for example Greco and Hakala, have claimed that non-linear regression is always superior to regression of the linear forms of the Michaelis–Menten equation. However, that is correct only if the appropriate weighting scheme is used, preferably on the basis of experimental investigation, something that is almost never done. As noted above, Burk carried out the appropriate investigation, and found that the error structure of his data was consistent with a uniform standard deviation in v . More recent studies found that a uniform coefficient of variation (standard deviation expressed as a percentage) was closer to the truth with the techniques in use in the 1970s. However, this truth may be more complicated than any dependence on v alone can represent.

**Uniform standard deviation of $1/v$**. If the rates are considered to have a uniform standard deviation the appropriate weight for every v value for non-linear regression is 1. If the double-reciprocal plot is used each value of $1/v$ should have a weight of $v^{4}$ , whereas if the Hanes plot is used each value of $a/v$ should have a weight of $v^{4}/a^{2}$ .

**Uniform coefficient variation of $1/v$**. If the rates are considered to have a uniform coefficient variation the appropriate weight for every v value for non-linear regression is $v^{2}$ . If the double-reciprocal plot is used each value of $1/v$ should have a weight of $v^{2}$ , whereas if the Hanes plot is used each value of $a/v$ should have a weight of $v^{2}/a^{2}$ .

Ideally the v in each of these cases should be the true value, but that is always unknown. However, after a preliminary estimation one can use the calculated values ${\hat {v}}$ for refining the estimation. In practice the error structure of enzyme kinetic data is very rarely investigated experimentally, therefore almost never known, but simply assumed. It is, however, possible to form an impression of the error structure from internal evidence in the data. This is tedious to do by hand, but can readily be done in the computer.

### Closed form equation

Santiago Schnell and Claudio Mendoza suggested a closed form solution for the time course kinetics analysis of the Michaelis–Menten kinetics based on the solution of the Lambert W function. Namely,

${\frac {a}{K_{\mathrm {m} }}}=W(F(t))$

where *W* is the Lambert W function and

$F(t)={\frac {a_{0}}{K_{\mathrm {m} }}}\exp \!\left({\frac {a_{0}}{K_{\mathrm {m} }}}-{\frac {Vt}{K_{\mathrm {m} }}}\right)$

The above equation, known nowadays as the Schnell-Mendoza equation, has been used to estimate V and $K_{\mathrm {m} }$ from time course data.

## Reactions with more than one substrate

Only a small minority of enzyme-catalysed reactions have just one substrate, and even if the number is increased by treating two-substrate reactions in which one substrate is water as one-substrate reactions the number is still small. One might accordingly suppose that the Michaelis–Menten equation, normally written with just one substrate, is of limited usefulness. This supposition is misleading, however. One of the common equations for a two-substrate reaction can be written as follows to express v in terms of two substrate concentrations a and b :

$v={\frac {Vab}{K_{\mathrm {iA} }K_{\mathrm {mB} }+K_{\mathrm {mB} }a+K_{\mathrm {mA} }b+ab}}$

the other symbols represent kinetic constants. Suppose now that a is varied with b held constant. Then it is convenient to reorganize the equation as follows:

$v={\frac {Vb\cdot a}{K_{\mathrm {iA} }K_{\mathrm {mB} }+K_{\mathrm {mA} }b+(K_{\mathrm {mB} }+b)a}}={\dfrac {{\dfrac {Vb}{K_{\mathrm {mB} }+b}}\cdot a}{{\dfrac {K_{\mathrm {iA} }K_{\mathrm {mB} }+K_{\mathrm {mA} }b}{K_{\mathrm {mB} }+b}}+a}}$

This has exactly the form of the Michaelis–Menten equation

$v={\frac {V^{\mathrm {app} }a}{K_{\mathrm {m} }^{\mathrm {app} }+a}}$

with apparent values $V^{\mathrm {app} }$ and $K_{\mathrm {m} }^{\mathrm {app} }$ defined as follows:

$V^{\mathrm {app} }={\dfrac {Vb}{K_{\mathrm {mB} }+b}}$

$K_{\mathrm {m} }^{\mathrm {app} }={\dfrac {K_{\mathrm {iA} }K_{\mathrm {mB} }+K_{\mathrm {mA} }b}{K_{\mathrm {mB} }+b}}$

## Linear inhibition

The linear (simple) types of inhibition can be classified in terms of the general equation for mixed inhibition at an inhibitor concentration i :

$v={\dfrac {Va}{K_{\mathrm {m} }\left(1+{\dfrac {i}{K_{\mathrm {ic} }}}\right)+a\left(1+{\dfrac {i}{K_{\mathrm {iu} }}}\right)}}$

in which $K_{\mathrm {ic} }$ is the competitive inhibition constant and $K_{\mathrm {iu} }$ is the uncompetitive inhibition constant. This equation includes the other types of inhibition as special cases:

- If $K_{\mathrm {iu} }\rightarrow \infty$ the second parenthesis in the denominator approaches 1 and the resulting behaviour is competitive inhibition.
- If $K_{\mathrm {ic} }\rightarrow \infty$ the first parenthesis in the denominator approaches 1 and the resulting behaviour is uncompetitive inhibition.
- If both $K_{\mathrm {ic} }$ and $K_{\mathrm {iu} }$ are finite the behaviour is mixed inhibition.
- If $K_{\mathrm {ic} }=K_{\mathrm {iu} }$ the resulting special case is pure non-competitive inhibition.

Pure non-competitive inhibition is very rare, being mainly confined to effects of protons and some metal ions. Cleland recognized this, and he redefined *noncompetitive* to mean *mixed*. Some authors have followed him in this respect, but not all, so when reading any publication one needs to check what definition the authors are using.

In all cases the kinetic equations have the form of the Michaelis–Menten equation with apparent constants, as can be seen by writing the equation above as follows:

$v={\dfrac {{\dfrac {V}{1+i/K_{\mathrm {iu} }}}\cdot a}{{\dfrac {K_{\mathrm {m} }(1+i/K_{\mathrm {ic} })}{1+i/K_{\mathrm {iu} }}}+a}}={\frac {V^{\mathrm {app} }a}{K_{\mathrm {m} }^{\mathrm {app} }+a}}$

with apparent values $V^{\mathrm {app} }$ and $K_{\mathrm {m} }^{\mathrm {app} }$ defined as follows:

$V^{\mathrm {app} }={\dfrac {V}{1+i/K_{\mathrm {iu} }}}$

$K_{\mathrm {m} }^{\mathrm {app} }={\dfrac {K_{\mathrm {m} }(1+i/K_{\mathrm {ic} })}{1+i/K_{\mathrm {iu} }}}$
