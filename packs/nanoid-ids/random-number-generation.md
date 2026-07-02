---
title: "Random number generation"
source: https://en.wikipedia.org/wiki/Random_number_generation
domain: nanoid-ids
license: CC-BY-SA-4.0
tags: nanoid generator, compact unique id, url-safe identifier, collision resistant id
fetched: 2026-07-02
---

# Random number generation

**Random number generation** is a process by which, often by means of a **random number generator** (**RNG**), a sequence of numbers or symbols is generated that cannot be reasonably predicted better than by random chance. This means that the particular outcome sequence will contain some patterns detectable in hindsight but impossible to foresee. True random number generators can be *hardware random-number generators* (HRNGs), wherein each generation is a function of the current value of a physical environment's attribute that is constantly changing in a manner that is practically impossible to model. This would be in contrast to so-called *random number generations* done by *pseudorandom number generators* (PRNGs), which generate pseudorandom numbers that are in fact predetermined—these numbers can be reproduced simply by knowing the initial state of the PRNG and the method it uses to generate numbers. There is also a class of non-physical true random number generators (NPTRNG) that produce true random numbers without an access to a dedicated hardware source, by scavenging entropy that is present in the computer system. See the details in True vs. pseudo-random numbers.

Various applications of randomness have led to the development of different methods for generating random data. Some of these have existed since ancient times, including well-known examples like the rolling of dice, coin flipping, the shuffling of playing cards, the use of yarrow stalks (for divination) in the I Ching, as well as countless other techniques. Because of the mechanical nature of these techniques, generating large quantities of sufficiently random numbers (important in statistics) required much work and time. Thus, results would sometimes be collected and distributed as random number tables.

Several computational methods for pseudorandom number generation exist. All fall short of the goal of true randomness, although they may meet, with varying success, some of the statistical tests for randomness intended to measure how unpredictable their results are (that is, to what degree their patterns are discernible). This generally makes them unusable for applications such as cryptography. However, carefully designed *cryptographically secure pseudorandom number generators* (CSPRNGS) also exist, with special features specifically designed for use in cryptography.

## Practical applications and uses

Random number generators have applications in gambling, statistical sampling, computer simulation, cryptography, completely randomized design, and other areas where producing an unpredictable result is desirable. Generally, in applications having unpredictability as the paramount feature, such as in security applications, hardware generators are generally preferred over pseudorandom algorithms, where feasible.

Pseudorandom number generators are very useful in developing Monte Carlo-method simulations, as debugging is facilitated by the ability to run the same sequence of random numbers again by starting from the same *random seed*. They are also used in cryptography – so long as the *seed* is secret. The sender and receiver can generate the same set of numbers automatically to use as keys.

The generation of pseudorandom numbers is an important and common task in computer programming. While cryptography and certain numerical algorithms require a very high degree of *apparent* randomness, many other operations only need a modest amount of unpredictability. Some simple examples might be presenting a user with a "random quote of the day", or determining which way a computer-controlled adversary might move in a computer game. Weaker forms of *randomness* are used in hash algorithms and in creating amortized searching and sorting algorithms.

Some applications that appear at first sight to be suitable for randomization are in fact not quite so simple. For instance, a system that "randomly" selects music tracks for a background music system must only *appear* random, and may even have ways to control the selection of music: a truly random system would have no restriction on the same item appearing two or three times in succession.

## True vs. pseudo-random numbers

There are two principal methods used to generate random numbers. The first method measures some physical phenomenon that is expected to be random and then compensates for possible biases in the measurement process. Example sources include measuring atmospheric noise, thermal noise, and other external electromagnetic and quantum phenomena. For example, cosmic background radiation or radioactive decay as measured over short timescales represent sources of natural entropy (as a measure of unpredictability or surprise of the number generation process).

The speed at which entropy can be obtained from natural sources is dependent on the underlying physical phenomena being measured. Thus, sources of naturally occurring *true* entropy are said to be blocking – they are rate-limited until enough entropy is harvested to meet the demand. On some Unix-like systems, including most Linux distributions, the pseudo device file /dev/random will block until sufficient entropy is harvested from the environment. Due to this blocking behavior, large bulk reads from /dev/random, such as filling a hard disk drive with random bits, can often be slow on systems that use this type of entropy source.

The second method uses computational algorithms that can produce long sequences of apparently random results, which are in fact completely determined by a shorter initial value, known as a seed value or key. As a result, the entire seemingly random sequence can be reproduced if the seed value is known. This type of random number generator is often called a pseudorandom number generator. This type of generator typically does not rely on sources of naturally occurring entropy, though it may be periodically seeded by natural sources. This generator type is non-blocking, so they are not rate-limited by an external event, making large bulk reads a possibility.

Standard cryptographic designs take a hybrid approach, using randomness harvested from natural sources to seed a cryptographically secure pseudorandom number generators (CSPRNGs). Hardware random number generators generally produce only a limited number of random bits per second. In order to increase the available output data rate, they are often used to generate the "seed" for a faster PRNG. PRNG also helps with the noise source "anonymization" (whitening out the noise source identifying characteristics) and entropy extraction. With a proper PRNG algorithm selected (cryptographically secure pseudorandom number generator, CSPRNG), the combination can satisfy the requirements of Federal Information Processing Standards and Common Criteria standards.

## Generation methods

### Physical methods

The earliest methods for generating random numbers, such as dice, coin flipping and roulette wheels, are still used today, mainly in games and gambling, as they tend to be too slow for most applications in statistics and cryptography.

Many natural phenomena generate low-level, statistically random "noise" signals, including thermal and shot noise, jitter and metastability of electronic circuits, Brownian motion, and atmospheric noise. Researchers also used the photoelectric effect, involving a beam splitter, other quantum phenomena, and even nuclear decay (due to practical considerations the latter, as well as the atmospheric noise, is not viable except for fairly restricted applications or online distribution services). While "classical" (non-quantum) phenomena are not truly random, an unpredictable physical system is usually acceptable as a source of randomness, so the qualifiers "true" and "physical" are used interchangeably.

A hardware random number generator is expected to output near-perfect random numbers ("full entropy"). A physical process usually does not have this property, and a practical TRNG typically includes a few blocks:

- a *noise source* that implements the physical process producing the entropy. Usually this process is analog, so a *digitizer* is used to convert the output of the analog source into a binary representation;
- a *conditioner* (randomness extractor) that improves the quality of the random bits;
- *health tests*. TRNGs are mostly used in cryptographical algorithms that get completely broken if the random numbers have low entropy, so the testing functionality is usually included.

### Computational methods

For performance and security reasons, most random number generators use PRNGs in their construction (this architecture is actually mandated in the industrial standards like NIST SP 800-90A).

A pseudorandom number generator (PRNG), also known as a deterministic random bit generator (DRBG), is an algorithm for generating a sequence of numbers whose properties approximate the properties of sequences of random numbers. The PRNG-generated sequence is not truly random, because it is completely determined by an initial value, called the PRNG's *seed* (which may include truly random values). Although sequences that are closer to truly random can be generated using hardware random number generators, *pseudorandom number generators* are important in practice for their speed in number generation and their reproducibility.

PRNGs are central in applications such as simulations (e.g. for the Monte Carlo method), electronic games (e.g. for procedural generation), and cryptography. Cryptographic applications require the output not to be predictable from earlier outputs, and more elaborate algorithms, which do not inherit the linearity of simpler PRNGs, are needed.

Good statistical properties are a central requirement for the output of a PRNG. In general, careful mathematical analysis is required to have any confidence that a PRNG generates numbers that are sufficiently close to random to suit the intended use. John von Neumann cautioned about the misinterpretation of a PRNG as a truly random generator, joking that "Anyone who considers arithmetical methods of producing random digits is, of course, in a state of sin."

### By humans

Random number generation may also be performed by humans, in the form of collecting various inputs from end users and using them as a randomization source. However, most studies find that human subjects have some degree of non-randomness when attempting to produce a random sequence of e.g., digits or letters. They may alternate too much between choices when compared to a good random generator; thus, this approach is not widely used. However, for the very reason that humans perform poorly in this task, human random number generation can be used as a tool to gain insights into brain functions otherwise not accessible.

## Post-processing and statistical checks

Even given a source of plausible random numbers (perhaps from a quantum mechanically based hardware generator), obtaining numbers which are completely unbiased takes care. In addition, behavior of these generators often changes with temperature, power supply voltage, the age of the device, or other outside interference.

Generated random numbers are sometimes subjected to statistical tests before use to ensure that the underlying source is still working, and then post-processed to improve their statistical properties. An example would be the TRNG9803 hardware random number generator, which uses an entropy measurement as a hardware test, and then post-processes the random sequence with a shift register stream cipher. It is generally hard to use statistical tests to validate the generated random numbers. Wang and Nicol proposed a distance-based statistical testing technique that is used to identify the weaknesses of several random generators. Li and Wang proposed a method of testing random numbers based on laser chaotic entropy sources using Brownian motion properties.

Statistical tests are also used to give confidence that the post-processed final output from a random number generator is truly unbiased, with numerous randomness test suites being developed.

## Other considerations

### Reshaping the distribution

#### Uniform distributions

Most random number generators natively work with integers or individual bits, so an extra step is required to arrive at the *canonical* uniform distribution between 0 and 1. The implementation is not as trivial as dividing the integer by its maximum possible value. Specifically:

1. The integer used in the transformation must provide enough bits for the intended precision.
2. The nature of floating-point math itself means there exists more precision the closer the number is to zero. This extra precision is usually not used due to the sheer number of bits required. (One consequence is Box–Muller transform § Tails truncation.)
3. Rounding error in division may bias the result. At worst, a supposedly excluded bound may be drawn contrary to expectations based on real-number math.

The mainstream algorithm, used by OpenJDK, Rust, and NumPy, is described in a proposal for C++'s STL. It does not use the extra precision and suffers from bias only in the last bit due to rounding half to even. Other numeric concerns are warranted when shifting this *canonical* uniform distribution to a different range. A proposed method for the Swift programming language claims to use the full precision everywhere.

Uniformly distributed integers are commonly used in algorithms such as the Fisher–Yates shuffle. Again, a naive implementation may induce a modulo bias into the result, so more involved algorithms must be used. A method that nearly never performs division was described in 2018 by Daniel Lemire, with the current state-of-the-art being the arithmetic encoding-inspired 2021 "optimal algorithm" by Stephen Canon of Apple Inc.

Most 0 to 1 RNGs include 0 but exclude 1, while others include or exclude both.

#### Other distributions

Given a source of uniform random numbers, there are a couple of methods to create a new random source that corresponds to a probability density function. One method called the inversion method, involves integrating up to an area greater than or equal to the random number (which should be generated between 0 and 1 for proper distributions). A second method called the acceptance-rejection method, involves choosing an x and y value and testing whether the function of x is greater than the y value. If it is, the x value is accepted. Otherwise, the x value is rejected and the algorithm tries again.

As an example for rejection sampling, to generate a pair of statistically independent standard normally distributed random numbers (*x*, *y*), one may first generate the polar coordinates (*r*, *θ*), where *r*2~χ22 and *θ*~UNIFORM(0,2π) (see Box–Muller transform).

### Whitening

The outputs of multiple independent RNGs can be combined (for example, using a bit-wise XOR operation) to provide a combined RNG at least as good as the best RNG used. This is referred to as software whitening.

Computational and hardware random number generators are sometimes combined to reflect the benefits of both kinds. Computational random number generators can typically generate pseudorandom numbers much faster than physical generators, while physical generators can generate true randomness.

## Low-discrepancy sequences as an alternative

Some computations making use of a random number generator can be summarized as the computation of a total or average value, such as the computation of integrals by the Monte Carlo method. For such problems, it may be possible to find a more accurate solution by the use of so-called low-discrepancy sequences, also called quasirandom numbers. Such sequences have a definite pattern that fills in gaps evenly, qualitatively speaking; a truly random sequence may, and usually does, leave larger gaps.

## Activities and demonstrations

The following sites make available random number samples:

- The SOCR resource pages contain a number of hands-on interactive activities and demonstrations of random number generation using Java applets.
- The Quantum Optics Group at the ANU generates random numbers sourced from quantum vacuum. Samples of random numbers are available at their quantum random number generator research page.
- Random.org makes available random numbers that are sourced from the randomness of atmospheric noise.
- The Quantum Random Bit Generator Service at the Ruđer Bošković Institute harvests randomness from the quantum process of photonic emission in semiconductors. They supply a variety of ways of fetching the data, including libraries for several programming languages.
- The Group at the Taiyuan University of Technology generates random numbers sourced from a chaotic laser. Samples of random numbers are available at their physical random number generator service.

## Backdoors

Since much cryptography depends on a cryptographically secure random number generator for key and cryptographic nonce generation, if a random number generator can be made predictable, it can be used as backdoor by an attacker to break the encryption.

The NSA is reported to have inserted a backdoor into the NIST certified cryptographically secure pseudorandom number generator Dual EC DRBG. If for example an SSL connection is created using this random number generator, then according to Matthew Green it would allow NSA to determine the state of the random number generator, and thereby eventually be able to read all data sent over the SSL connection. Even though it was apparent that Dual_EC_DRBG was a very poor and possibly backdoored pseudorandom number generator long before the NSA backdoor was confirmed in 2013, it had seen significant usage in practice until 2013, for example by the prominent security company RSA Security. There have subsequently been accusations that RSA Security knowingly inserted a NSA backdoor into its products, possibly as part of the Bullrun program. RSA has denied knowingly inserting a backdoor into its products.

It has also been theorized that hardware RNGs could be secretly modified to have less entropy than stated, which would make encryption using the hardware RNG susceptible to attack. One such method that has been published works by modifying the dopant mask of the chip, which would be undetectable to optical reverse-engineering. For example, for random number generation in Linux, it is seen as unacceptable to use Intel's RDRAND hardware RNG without mixing in the RDRAND output with other sources of entropy to counteract any backdoors in the hardware RNG, especially after the revelation of the NSA Bullrun program.

In 2010, a U.S. lottery draw was rigged by the information security director of the Multi-State Lottery Association (MUSL), who surreptitiously installed backdoor malware on the MUSL's secure RNG computer during routine maintenance. During the hacks the man won a total amount of $16,500,000 over multiple years.
