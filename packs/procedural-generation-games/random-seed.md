---
title: "Random seed"
source: https://en.wikipedia.org/wiki/Random_seed
domain: procedural-generation-games
license: CC-BY-SA-4.0
tags: procedural generation, procedural content generation, roguelike generation, seeded generation
fetched: 2026-07-02
---

# Random seed

A **random seed** (or **seed state**, or just **seed**) is a number (or vector) used to initialize a pseudorandom number generator.

A pseudorandom number generator's number sequence is completely determined by the seed: thus, if a pseudorandom number generator is later reinitialized with the same seed, it will produce the same sequence of numbers.

For a seed to be used in a pseudorandom number generator, it does not need to be random. Because of the nature of number generating algorithms, so long as the original seed is ignored, the rest of the values that the algorithm generates will follow probability distribution in a pseudorandom manner. However, a non-random seed will be cryptographically insecure, as it can allow an adversary to predict the pseudorandom numbers generated.

The choice of a good random seed is crucial in the field of computer security. When a secret encryption key is pseudorandomly generated, having the seed will allow one to obtain the key. High entropy is important for selecting good random seed data.

Random seeds need to be chosen carefully in order to ensure random number generation. If a seed is chosen that doesn't provide actual random results, the numbers given by the PRNG (pseudo random number generator) will not work properly in an application that needs them. Charting the output values of a PRNG with a scatter plot is a good way to find out if the seed is working. If the graph shows static, then the PRNG is giving random results, but if a pattern appears, the seed needs to be fixed.

If the same *random* seed is deliberately shared, it becomes a secret key, so two or more systems using matching pseudorandom number algorithms and matching seeds can generate matching sequences of non-repeating numbers which can be used to synchronize remote systems, such as GPS satellites and receivers.

Random seeds are often generated from the state of the computer system (such as the time), a cryptographically secure pseudorandom number generator or from a hardware random number generator.
