---
title: "Lean Programming Language"
source: https://lean-lang.org/
domain: lean-prover
license: CC-BY-SA-4.0
tags: lean prover, lean theorem prover, lean4, mathlib lean
fetched: 2026-07-02
---

# Lean Programming Language

Lean is an open-source programming language and proof assistant that enables correct, maintainable, and formally verified code

Install

Learn

Powerful automation

Mathematics

example

(

x

:

Nat

)

:

0

<

match

x

with

|

0

=>

1

|

n

+

1

=>

x

+

n

:=

by

grind

example

(

x

y

:

Int

)

:

27

≤

11

*

x

+

13

*

y

→

11

*

x

+

13

*

y

≤

45

→

-

10

≤

7

*

x

-

9

*

y

→

7

*

x

-

9

*

y

>

4

:=

by

grind

def

IsPrime

(

n

:

Nat

)

:=

1

<

n

∧

∀

k

,

1

<

k

→

k

<

n

→

¬

k

∣

n

theorem

exists_prime_factor

:

∀

n

,

1

<

n

→

∃

k

,

IsPrime

k

∧

k

∣

n

:=

by

intro

n

h1

by_cases

hprime

:

IsPrime

n

·

grind

[

Nat.dvd_refl

]

·

obtain

⟨

k

,

_

⟩

:

∃

k

,

1

<

k

∧

k

<

n

∧

k

∣

n

:=

by

simp_all

[

IsPrime

]

obtain

⟨

p

,

_

,

_

⟩

:=

exists_prime_factor

k

(

by

grind

)

grind

[

Nat.dvd_trans

]

def

factorial

:

Nat

→

Nat

|

0

=>

1

|

n

+

1

=>

(

n

+

1

)

*

factorial

n

notation

:

10000

n

"!"

=>

factorial

n

theorem

factorial_pos

:

∀

n

,

0

<

n

!

:=

by

intro

n

;

induction

n

<;>

grind

[

factorial

]

theorem

dvd_factorial

:

∀

n

,

∀

k

≤

n

,

0

<

k

→

k

∣

n

!

:=

by

intro

n

;

induction

n

<;>

grind

[

Nat.dvd_mul_right

,

Nat.dvd_mul_left_of_dvd

,

factorial

]

theorem

InfinitudeOfPrimes

:

∀

n

,

∃

p

>

n

,

IsPrime

p

:=

by

intro

n

have

:

1

<

n

!

+

1

:=

by

grind

[

factorial_pos

]

obtain

⟨

p

,

hp

,

_

⟩

:=

exists_prime_factor

(

n

!

+

1

)

this

suffices

¬

p

≤

n

by

grind

intro

(

_

:

p

≤

n

)

have

:

1

<

p

:=

hp

.

1

have

:

p

∣

n

!

:=

dvd_factorial

n

p

‹

p

≤

n

›

(

by

grind

)

have

:=

Nat.dvd_sub

‹

p

∣

n

!

+

1

›

‹

p

∣

n

!

›

grind

[

Nat.add_sub_cancel_left

,

Nat.dvd_one

]

### Trustworthy

Lean's minimal trusted kernel guarantees absolute correctness in mathematical proof, software and hardware verification.

### Powerful

From elementary concepts to cutting-edge research, Lean's expressive language and extensive built-in tools let users focus on the big picture rather than routine details.

### Extensible

Lean's metaprogramming capabilities enable users to extend the language with domain-specific notations and new proof automation techniques.

# Get Started with Lean

Lean lets you write precise, verifiable code and formal proofs. Whether you are new or experienced, now is a great time to start.

Install

Learn

FEATURED PROJECTS

# Lean in Action

Showcasing Real-World Applications

VERIFICATION

## ArkLib

ArkLib, a project supported by the Ethereum Foundation, anchors a growing ecosystem of Lean libraries for formally verifying succinct non-interactive arguments of knowledge (SNARKs). It mechanizes the subtle, probabilistic security proofs these cryptographic systems depend on, giving zk engineers and cryptography researchers machine-checked specifications and executable references. This brings high assurance to proof systems where a single soundness bug can be catastrophic.

Read More

VERIFICATION

## Veil

Veil is an open-source multi-modal verification framework for distributed protocols, embedded in Lean. In contrast to standalone verifiers, Veil uses Lean as a platform, combining symbolic and concrete model checking, SMT-based automated proofs, and interactive theorem proving in a single cohesive tool with foundational guarantees and rich in-editor feedback. It shows Lean is not just a proof assistant, but a platform for industrial-strength verifiers with great user experience.

Read More

VERIFICATION

## Cedar

AWS uses Lean and verification-guided development to formally verify Cedar, the AWS authorization policy language. The approach involves creating executable models in Lean, proving security properties, and validating them against production code through differential testing. This achieves high assurance with minimal runtime overhead, demonstrating Lean's viability for verifying critical software.

Read More

VERIFICATION

## Aeneas

Aeneas takes a novel approach to Rust verification. Unlike other verification approaches that must reason about memory directly, Aeneas leverages Rust's rich type system to eliminate memory reasoning entirely for many Rust programs.

Read More

MATHEMATICS

## Mathlib

Mathlib is Lean's comprehensive mathematical library containing over a million lines of formalized mathematics spanning algebra, analysis, topology, probability, and computer science. This community-driven resource enables mathematicians to tackle frontier research problems and engineers to build verified systems by providing a rigorously verified foundation of mathematical knowledge that eliminates duplication of effort.

Read More

MATHEMATICS

## Fermat's Last Theorem

The Fermat's Last Theorem project is formalizing one of mathematics' most complex proofs in Lean, demonstrating the proof assistant's capacity to handle frontier research mathematics. This ambitious work is creating formalized definitions for advanced number-theoretic objects, enabling mathematicians to build machine-verified proofs of cutting-edge results while establishing Lean as a powerful platform for mathematical collaboration.

Read More

PROGRESS

# Growth and Impact

Tracking Lean's reach across math, research, and industry

JUNE, 2026

Quanta Books publishes The Proof in the Code, "the definitive account of the birth and rise of Lean"; Fortune magazine announces Axiom's EconLib, formalizing economic theory in Lean

MAY, 2026

Google DeepMind announces AlphaProof Nexus and autonomous proofs of 9 Erdős problems; SAIR convenes the Science x AI Summit in Palo Alto, foregrounding Lean and AI-assisted proof discovery; NASA holds its Formal Methods Symposium with keynotes on Lean, CSLib and Aristotle; TorchLean is released, bridging PyTorch and Lean

APRIL, 2026

OpenAI releases ChatGPT 5.5, used internally by OpenAI to discover a new Lean-verified proof relating to off-diagonal Ramsey numbers; The Economist profiles Lean-powered AI math startups; Software Verification in Lean takes place in Paris; The Signal Shot challenge is announced; The SAIR Mathematics Distillation Challenge Stage 2 announced

READ MORE →

"

> Lean enables large-scale collaboration by allowing mathematicians to break down complex proofs into smaller, verifiable components. This formalization process ensures the correctness of proofs and facilitates contributions from a broader community. With Lean, we are beginning to see how AI can accelerate the formalization of mathematics, opening up new possibilities for research.

## Terence Tao

Mathematician, UCLA

"

> Lean has become a key enabler in scaling automated reasoning at Amazon. Its capacity to verify complex systems involving advanced mathematical concepts has transformed how we tackle problems once thought too complex or impractical. Lean is an indispensable tool in modern, large-scale software engineering, helping ensure soundness, correctness, and verified AI across our systems.

## Byron Cook

VP and Distinguished Scientist, AWS

"

> At Google DeepMind, we used Lean to build AlphaProof, a new reinforcement-learning based system for formal math reasoning. Lean’s extensibility and verification capabilities were key in enabling the development of AlphaProof.

## Pushmeet Kohli

VP, Science and Strategic Initiatives, Google DeepMind

"

> Mathematical Superintelligence (MSI) with Lean will play a critical role in any industry where safety is paramount, including aerospace, automotive, and medical technology. In addition, we look forward to providing early access to our technology to students and researchers to accelerate advancement in mathematics, science, and engineering.

## Tudor Achim

Co-Founder and CEO, Harmonic

"

> Lean is the core verification technology behind Cedar, the open-source authorization language that powers cloud services like Amazon Verified Permissions and AWS Verified Access. Our team rigorously formalizes and verifies core components of Cedar using Lean’s proof assistant, and we leverage Lean’s lightning-fast runtime to continuously test our production Rust code against the Lean formalization. Lean’s efficiency, extensive libraries, and vibrant community enable us to develop and maintain Cedar at scale, while ensuring the key correctness and security properties that our users depend on.

## Emina Torlak

Senior Principal Applied Scientist, AWS

SUPPORTERS

# Sponsors and Partners

Lean FRO gratefully acknowledges support from **Alex Gerko**, Founder and CEO of XTX Markets, as well as from the following organizations.
