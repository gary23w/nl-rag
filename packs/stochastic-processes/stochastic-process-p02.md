---
title: "Stochastic process (part 2/2)"
source: https://en.wikipedia.org/wiki/Stochastic_process
domain: stochastic-processes
license: CC-BY-SA-4.0
tags: stochastic process, wiener process, brownian motion, stochastic calculus
fetched: 2026-07-02
part: 2/2
---

## History

### Early probability theory

Probability theory has its origins in games of chance, which have a long history, with some games being played thousands of years ago, but very little analysis on them was done in terms of probability. The year 1654 is often considered the birth of probability theory when French mathematicians Pierre Fermat and Blaise Pascal had a written correspondence on probability, motivated by a gambling problem. But there was earlier mathematical work done on the probability of gambling games such as *Liber de Ludo Aleae* by Gerolamo Cardano, written in the 16th century but posthumously published later in 1663.

After Cardano, Jakob Bernoulli wrote Ars Conjectandi, which is considered a significant event in the history of probability theory. Bernoulli's book was published, also posthumously, in 1713 and inspired many mathematicians to study probability. But despite some renowned mathematicians contributing to probability theory, such as Pierre-Simon Laplace, Abraham de Moivre, Carl Gauss, Siméon Poisson and Pafnuty Chebyshev, most of the mathematical community did not consider probability theory to be part of mathematics until the 20th century.

### Statistical mechanics

In the physical sciences, scientists developed in the 19th century the discipline of statistical mechanics, where physical systems, such as containers filled with gases, are regarded or treated mathematically as collections of many moving particles. Although there were attempts to incorporate randomness into statistical physics by some scientists, such as Rudolf Clausius, most of the work had little or no randomness. This changed in 1859 when James Clerk Maxwell contributed significantly to the field, more specifically, to the kinetic theory of gases, by presenting work where he modelled the gas particles as moving in random directions at random velocities. The kinetic theory of gases and statistical physics continued to be developed in the second half of the 19th century, with work done chiefly by Clausius, Ludwig Boltzmann and Josiah Gibbs, which would later have an influence on Albert Einstein's mathematical model for Brownian movement.

### Measure theory and probability theory

At the International Congress of Mathematicians in Paris in 1900, David Hilbert presented a list of mathematical problems, where his sixth problem asked for a mathematical treatment of physics and probability involving axioms. Around the start of the 20th century, mathematicians developed measure theory, a branch of mathematics for studying integrals of mathematical functions, where two of the founders were French mathematicians, Henri Lebesgue and Émile Borel. In 1925, another French mathematician Paul Lévy published the first probability book that used ideas from measure theory.

In the 1920s, fundamental contributions to probability theory were made in the Soviet Union by mathematicians such as Sergei Bernstein, Aleksandr Khinchin, and Andrei Kolmogorov. Kolmogorov published in 1929 his first attempt at presenting a mathematical foundation, based on measure theory, for probability theory. In the early 1930s, Khinchin and Kolmogorov set up probability seminars, which were attended by researchers such as Eugene Slutsky and Nikolai Smirnov, and Khinchin gave the first mathematical definition of a stochastic process as a set of random variables indexed by the real line.

### Birth of modern probability theory

In 1933, Andrei Kolmogorov published in German, his book on the foundations of probability theory titled *Grundbegriffe der Wahrscheinlichkeitsrechnung*, where Kolmogorov used measure theory to develop an axiomatic framework for probability theory. The publication of this book is now widely considered to be the birth of modern probability theory, when the theories of probability and stochastic processes became parts of mathematics.

After the publication of Kolmogorov's book, further fundamental work on probability theory and stochastic processes was done by Khinchin and Kolmogorov as well as other mathematicians such as Joseph Doob, William Feller, Maurice Fréchet, Paul Lévy, Wolfgang Doeblin, and Harald Cramér. Decades later, Cramér referred to the 1930s as the "heroic period of mathematical probability theory". World War II greatly interrupted the development of probability theory, causing, for example, the migration of Feller from Sweden to the United States of America and the death of Doeblin, considered now a pioneer in stochastic processes.

### Stochastic processes after World War II

After World War II, the study of probability theory and stochastic processes gained more attention from mathematicians, with significant contributions made in many areas of probability and mathematics as well as the creation of new areas. Starting in the 1940s, Kiyosi Itô published papers developing the field of stochastic calculus, which involves stochastic integrals and stochastic differential equations based on the Wiener or Brownian motion process.

Also starting in the 1940s, connections were made between stochastic processes, particularly martingales, and the mathematical field of potential theory, with early ideas by Shizuo Kakutani and then later work by Joseph Doob. Further work, considered pioneering, was done by Gilbert Hunt in the 1950s, connecting Markov processes and potential theory, which had a significant effect on the theory of Lévy processes and led to more interest in studying Markov processes with methods developed by Itô.

In 1953, Doob published his book *Stochastic processes*, which had a strong influence on the theory of stochastic processes and stressed the importance of measure theory in probability. Doob also chiefly developed the theory of martingales, with later substantial contributions by Paul-André Meyer. Earlier work had been carried out by Sergei Bernstein, Paul Lévy and Jean Ville, the latter adopting the term martingale for the stochastic process. Methods from the theory of martingales became popular for solving various probability problems. Techniques and theory were developed to study Markov processes and then applied to martingales. Conversely, methods from the theory of martingales were established to treat Markov processes.

Other fields of probability were developed and used to study stochastic processes, with one main approach being the theory of large deviations. The theory has many applications in statistical physics, among other fields, and has core ideas going back to at least the 1930s. Later in the 1960s and 1970s, fundamental work was done by Alexander Wentzell in the Soviet Union and Monroe D. Donsker and Srinivasa Varadhan in the United States of America, which would later result in Varadhan winning the 2007 Abel Prize. In the 1990s and 2000s the theories of Schramm–Loewner evolution and rough paths were introduced and developed to study stochastic processes and other mathematical objects in probability theory, which respectively resulted in Fields Medals being awarded to Wendelin Werner in 2008 and to Martin Hairer in 2014.

The theory of stochastic processes still continues to be a focus of research, with yearly international conferences on the topic of stochastic processes.

### Discoveries of specific stochastic processes

Although Khinchin gave mathematical definitions of stochastic processes in the 1930s, specific stochastic processes had already been discovered in different settings, such as the Brownian motion process and the Poisson process. Some families of stochastic processes such as point processes or renewal processes have long and complex histories, stretching back centuries.

#### Bernoulli process

The Bernoulli process, which can serve as a mathematical model for flipping a biased coin, is possibly the first stochastic process to have been studied. The process is a sequence of independent Bernoulli trials, which are named after Jacob Bernoulli who used them to study games of chance, including probability problems proposed and studied earlier by Christiaan Huygens. Bernoulli's work, including the Bernoulli process, were published in his book *Ars Conjectandi* in 1713.

#### Random walks

In 1905, Karl Pearson coined the term *random walk* while posing a problem describing a random walk on the plane, which was motivated by an application in biology, but such problems involving random walks had already been studied in other fields. Certain gambling problems that were studied centuries earlier can be considered as problems involving random walks. For example, the problem known as the *Gambler's ruin* is based on a simple random walk, and is an example of a random walk with absorbing barriers. Pascal, Fermat and Huyens all gave numerical solutions to this problem without detailing their methods, and then more detailed solutions were presented by Jakob Bernoulli and Abraham de Moivre.

For random walks in n -dimensional integer lattices, George Pólya published, in 1919 and 1921, work where he studied the probability of a symmetric random walk returning to a previous position in the lattice. Pólya showed that a symmetric random walk, which has an equal probability to advance in any direction in the lattice, will return to a previous position in the lattice an infinite number of times with probability one in one and two dimensions, but with probability zero in three or higher dimensions.

#### Wiener process

The Wiener process or Brownian motion process has its origins in different fields including statistics, finance and physics. In 1880, Danish astronomer Thorvald Thiele wrote a paper on the method of least squares, where he used the process to study the errors of a model in time-series analysis. The work is now considered as an early discovery of the statistical method known as Kalman filtering, but the work was largely overlooked. It is thought that the ideas in Thiele's paper were too advanced to have been understood by the broader mathematical and statistical community at the time.

The French mathematician Louis Bachelier used a Wiener process in his 1900 thesis in order to model price changes on the Paris Bourse, a stock exchange, without knowing the work of Thiele. It has been speculated that Bachelier drew ideas from the random walk model of Jules Regnault, but Bachelier did not cite him, and Bachelier's thesis is now considered pioneering in the field of financial mathematics.

It is commonly thought that Bachelier's work gained little attention and was forgotten for decades until it was rediscovered in the 1950s by the Leonard Savage, and then become more popular after Bachelier's thesis was translated into English in 1964. But the work was never forgotten in the mathematical community, as Bachelier published a book in 1912 detailing his ideas, which was cited by mathematicians including Doob, Feller and Kolmogorov. The book continued to be cited, but then starting in the 1960s, the original thesis by Bachelier began to be cited more than his book when economists started citing Bachelier's work.

In 1905, Albert Einstein published a paper where he studied the physical observation of Brownian motion or movement to explain the seemingly random movements of particles in liquids by using ideas from the kinetic theory of gases. Einstein derived a differential equation, known as a diffusion equation, for describing the probability of finding a particle in a certain region of space. Shortly after Einstein's first paper on Brownian movement, Marian Smoluchowski published work where he cited Einstein, but wrote that he had independently derived the equivalent results by using a different method.

Einstein's work, as well as experimental results obtained by Jean Perrin, later inspired Norbert Wiener in the 1920s to use a type of measure theory, developed by Percy Daniell, and Fourier analysis to prove the existence of the Wiener process as a mathematical object.

#### Poisson process

The Poisson process is named after Siméon Poisson, due to its definition involving the Poisson distribution, but Poisson never studied the process. There are a number of claims for early uses or discoveries of the Poisson process. At the beginning of the 20th century, the Poisson process would arise independently in different situations. In Sweden 1903, Filip Lundberg published a thesis containing work, now considered fundamental and pioneering, where he proposed to model insurance claims with a homogeneous Poisson process.

Another discovery occurred in Denmark in 1909 when A.K. Erlang derived the Poisson distribution when developing a mathematical model for the number of incoming phone calls in a finite time interval. Erlang was not at the time aware of Poisson's earlier work and assumed that the number phone calls arriving in each interval of time were independent to each other. He then found the limiting case, which is effectively recasting the Poisson distribution as a limit of the binomial distribution.

In 1910, Ernest Rutherford and Hans Geiger published experimental results on counting alpha particles. Motivated by their work, Harry Bateman studied the counting problem and derived Poisson probabilities as a solution to a family of differential equations, resulting in the independent discovery of the Poisson process. After this time there were many studies and applications of the Poisson process, but its early history is complicated, which has been explained by the various applications of the process in numerous fields by biologists, ecologists, engineers and various physical scientists.

#### Markov processes

Markov processes and Markov chains are named after Andrey Markov who studied Markov chains in the early 20th century. Markov was interested in studying an extension of independent random sequences. In his first paper on Markov chains, published in 1906, Markov showed that under certain conditions the average outcomes of the Markov chain would converge to a fixed vector of values, so proving a weak law of large numbers without the independence assumption, which had been commonly regarded as a requirement for such mathematical laws to hold. Markov later used Markov chains to study the distribution of vowels in Eugene Onegin, written by Alexander Pushkin, and proved a central limit theorem for such chains.

In 1912, Poincaré studied Markov chains on finite groups with an aim to study card shuffling. Other early uses of Markov chains include a diffusion model, introduced by Paul and Tatyana Ehrenfest in 1907, and a branching process, introduced by Francis Galton and Henry William Watson in 1873, preceding the work of Markov. After the work of Galton and Watson, it was later revealed that their branching process had been independently discovered and studied around three decades earlier by Irénée-Jules Bienaymé. Starting in 1928, Maurice Fréchet became interested in Markov chains, eventually resulting in him publishing in 1938 a detailed study on Markov chains.

Andrei Kolmogorov developed in a 1931 paper a large part of the early theory of continuous-time Markov processes. Kolmogorov was partly inspired by Louis Bachelier's 1900 work on fluctuations in the stock market as well as Norbert Wiener's work on Einstein's model of Brownian movement. He introduced and studied a particular set of Markov processes known as diffusion processes, where he derived a set of differential equations describing the processes. Independent of Kolmogorov's work, Sydney Chapman derived in a 1928 paper an equation, now called the Chapman–Kolmogorov equation, in a less mathematically rigorous way than Kolmogorov, while studying Brownian movement. The differential equations are now called the Kolmogorov equations or the Kolmogorov–Chapman equations. Other mathematicians who contributed significantly to the foundations of Markov processes include William Feller, starting in the 1930s, and then later Eugene Dynkin, starting in the 1950s.

#### Lévy processes

Lévy processes such as the Wiener process and the Poisson process (on the real line) are named after Paul Lévy who started studying them in the 1930s, but they have connections to infinitely divisible distributions going back to the 1920s. In a 1932 paper, Kolmogorov derived a characteristic function for random variables associated with Lévy processes. This result was later derived under more general conditions by Lévy in 1934, and then Khinchin independently gave an alternative form for this characteristic function in 1937. In addition to Lévy, Khinchin and Kolomogrov, early fundamental contributions to the theory of Lévy processes were made by Bruno de Finetti and Kiyosi Itô.


## Mathematical construction

In mathematics, constructions of mathematical objects are needed, which is also the case for stochastic processes, to prove that they exist mathematically. There are two main approaches for constructing a stochastic process. One approach involves considering a measurable space of functions, defining a suitable measurable mapping from a probability space to this measurable space of functions, and then deriving the corresponding finite-dimensional distributions.

Another approach involves defining a collection of random variables to have specific finite-dimensional distributions, and then using Kolmogorov's existence theorem to prove a corresponding stochastic process exists. This theorem, which is an existence theorem for measures on infinite product spaces, says that if any finite-dimensional distributions satisfy two conditions, known as *consistency conditions*, then there exists a stochastic process with those finite-dimensional distributions.

### Construction issues

When constructing continuous-time stochastic processes certain mathematical difficulties arise, due to the uncountable index sets, which do not occur with discrete-time processes. One problem is that it is possible to have more than one stochastic process with the same finite-dimensional distributions. For example, both the left-continuous modification and the right-continuous modification of a Poisson process have the same finite-dimensional distributions. This means that the distribution of the stochastic process does not, necessarily, specify uniquely the properties of the sample functions of the stochastic process.

Another problem is that functionals of continuous-time process that rely upon an uncountable number of points of the index set may not be measurable, so the probabilities of certain events may not be well-defined. For example, the supremum of a stochastic process or random field is not necessarily a well-defined random variable. For a continuous-time stochastic process X , other characteristics that depend on an uncountable number of points of the index set T include:

- a sample function of a stochastic process X is a continuous function of $t\in T$ ;
- a sample function of a stochastic process X is a bounded function of $t\in T$ ; and
- a sample function of a stochastic process X is an increasing function of $t\in T$ .

where the symbol **∈** can be read "a member of the set", as in t a member of the set T .

To overcome the two difficulties described above, i.e., "more than one..." and "functionals of...", different assumptions and approaches are possible.

### Resolving construction issues

One approach for avoiding mathematical construction issues of stochastic processes, proposed by Joseph Doob, is to assume that the stochastic process is separable. Separability ensures that infinite-dimensional distributions determine the properties of sample functions by requiring that sample functions are essentially determined by their values on a dense countable set of points in the index set. Furthermore, if a stochastic process is separable, then functionals of an uncountable number of points of the index set are measurable and their probabilities can be studied.

Another approach is possible, originally developed by Anatoliy Skorokhod and Andrei Kolmogorov, for a continuous-time stochastic process with any metric space as its state space. For the construction of such a stochastic process, it is assumed that the sample functions of the stochastic process belong to some suitable function space, which is usually the Skorokhod space consisting of all right-continuous functions with left limits. This approach is now more used than the separability assumption, but such a stochastic process based on this approach will be automatically separable.

Although less used, the separability assumption is considered more general because every stochastic process has a separable version. It is also used when it is not possible to construct a stochastic process in a Skorokhod space. For example, separability is assumed when constructing and studying random fields, where the collection of random variables is now indexed by sets other than the real line such as n -dimensional Euclidean space.


## Application

### Applications in Finance

#### Black-Scholes Model

One of the most famous applications of stochastic processes in finance is the **Black-Scholes model** for option pricing. Developed by Fischer Black, Myron Scholes, and Robert Merton (whose contributions led to the 1997 Nobel Memorial Prize in Economic Sciences), this model uses **Geometric Brownian motion**, a specific type of stochastic process, to describe the dynamics of asset prices.

The model assumes that the price of a stock follows a continuous-time stochastic process driven by a stochastic differential equation (SDE): $dS_{t}=\mu S_{t}\,dt+\sigma S_{t}\,dW_{t}$ Where:

- ${\textstyle S_{t}}$ is the price of the underlying asset at time t.
- μ is the drift rate, representing the expected return of the asset.
- σ is the volatility of the asset's returns.
- ${\textstyle W_{t}}$ is a standard Wiener process (Brownian motion) introducing the random market shocks.

The key assumption of the Black-Scholes model is that the price of a financial asset, such as a stock, follows a **log-normal distribution**, with its continuous returns following a normal distribution. Because of these properties, the model provides a closed-form solution for pricing European-style options. The Black-Scholes formula has had a profound impact on financial markets, forming the basis for much of modern options trading. Although the model has limitations, such as the assumption of constant volatility and no transaction costs, it remains widely used due to its simplicity and practical relevance.

#### Stochastic Volatility Models

Another significant application of stochastic processes in finance is in **stochastic volatility models**, which aim to capture the time-varying nature of market volatility. The **Heston model** is a popular example, allowing for the volatility of asset prices to follow its own stochastic process rather than remaining strictly constant.

In the Heston model, the asset price and its variance are modeled as a system of coupled stochastic differential equations: $dS_{t}=\mu S_{t}\,dt+{\sqrt {v_{t}}}S_{t}\,dW_{t}^{S}$ $dv_{t}=\kappa (\theta -v_{t})\,dt+\xi {\sqrt {v_{t}}}\,dW_{t}^{v}$ Where:

- ${\textstyle v_{t}}$ is the instantaneous variance, which follows a mean-reverting Cox–Ingersoll–Ross process.
- θ is the long-run average variance, and κ is the rate at which ${\textstyle v_{t}}$ reverts to θ.
- ξ is the "volatility of volatility".
- ${\textstyle W_{t}^{S}}$ and ${\textstyle W_{t}^{v}}$ are two distinct Wiener processes that are mathematically correlated (with correlation coefficient ρ), which allows the model to capture leverage effects (e.g., volatility often increases when stock prices fall).

Unlike the Black-Scholes model, which assumes constant volatility and results in a flat volatility surface, stochastic volatility models provide a more flexible framework for modeling market dynamics. They successfully reproduce the "volatility smile" observed in real-world options pricing, making them particularly crucial during periods of high uncertainty or market stress.

### Applications in Biology

#### Population Dynamics

One of the primary applications of stochastic processes in biology is in **population dynamics**. In contrast to deterministic models, which assume that populations change in predictable ways, stochastic models account for the inherent randomness in births, deaths, and migration. The **birth-death process**, a simple stochastic model, describes how populations fluctuate over time due to random births and deaths. These models are particularly important when dealing with small populations, where random events can have large impacts, such as in the case of endangered species or small microbial populations.

Another example is the **branching process**, which models the growth of a population where each individual reproduces independently. The branching process is often used to describe population extinction or explosion, particularly in epidemiology, where it can model the spread of infectious diseases within a population.

### Applications in Computer Science

#### Randomized Algorithms

Stochastic processes play a critical role in computer science, particularly in the analysis and development of **randomized algorithms**. These algorithms utilize random inputs to simplify problem-solving or enhance performance in complex computational tasks. For instance, Markov chains are widely used in probabilistic algorithms for optimization and sampling tasks, such as those employed in search engines like Google's PageRank. These methods balance computational efficiency with accuracy, making them invaluable for handling large datasets. Randomized algorithms are also extensively applied in areas such as cryptography, large-scale simulations, and artificial intelligence, where uncertainty must be managed effectively.

#### Queuing Theory

Another significant application of stochastic processes in computer science is in **queuing theory**, which models the random arrival and service of tasks in a system. This is particularly relevant in network traffic analysis and server management. For instance, queuing models help predict delays, manage resource allocation, and optimize throughput in web servers and communication networks. The flexibility of stochastic models allows researchers to simulate and improve the performance of high-traffic environments. For example, queueing theory is crucial for designing efficient data centers and cloud computing infrastructures.
