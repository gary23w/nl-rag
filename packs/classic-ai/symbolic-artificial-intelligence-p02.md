---
title: "Symbolic artificial intelligence (part 2/2)"
source: https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence
domain: classic-ai
license: CC-BY-SA-4.0
tags: artificial intelligence, expert system, knowledge representation, nlp, computer vision, symbolic ai
fetched: 2026-07-02
part: 2/2
---

## Controversies

Controversies arose from early on in symbolic AI, both within the field—e.g., between logicists (the pro-logic "neats") and non-logicists (the anti-logic "scruffies")—and between those who embraced AI but rejected symbolic approaches—primarily connectionists—and those outside the field. Critiques from outside of the field were primarily from philosophers, on intellectual grounds, but also from funding agencies, especially during the two AI winters.

### The Frame Problem: knowledge representation challenges for first-order logic

Limitations were discovered in using simple first-order logic to reason about dynamic domains. Problems were discovered both with regards to enumerating the preconditions for an action to succeed and in providing axioms for what did not change after an action was performed.

McCarthy and Hayes introduced the Frame Problem in 1969 in the paper, "Some Philosophical Problems from the Standpoint of Artificial Intelligence." A simple example occurs in "proving that one person could get into conversation with another", as an axiom asserting "if a person has a telephone he still has it after looking up a number in the telephone book" would be required for the deduction to succeed. Similar axioms would be required for other domain actions to specify what *did not* change.

A similar problem, called the Qualification Problem, occurs in trying to enumerate the *preconditions* for an action to succeed. An infinite number of pathological conditions can be imagined, e.g., a banana in a tailpipe could prevent a car from operating correctly.

McCarthy's approach to fix the frame problem was circumscription, a kind of non-monotonic logic where deductions could be made from actions that need only specify what would change while not having to explicitly specify everything that would not change. Other non-monotonic logics provided truth maintenance systems that revised beliefs leading to contradictions.

Other ways of handling more open-ended domains included probabilistic reasoning systems and machine learning to learn new concepts and rules. McCarthy's Advice Taker can be viewed as an inspiration here, as it could incorporate new knowledge provided by a human in the form of assertions or rules. For example, experimental symbolic machine learning systems explored the ability to take high-level natural language advice and to interpret it into domain-specific actionable rules.

Similar to the problems in handling dynamic domains, common-sense reasoning is also difficult to capture in formal reasoning. Examples of common-sense reasoning include implicit reasoning about how people think or general knowledge of day-to-day events, objects, and living creatures. This kind of knowledge is taken for granted and not viewed as noteworthy. Common-sense reasoning is an open area of research and challenging both for symbolic systems (e.g., Cyc has attempted to capture key parts of this knowledge over more than a decade) and neural systems (e.g., self-driving cars that do not know not to drive into cones or not to hit pedestrians walking a bicycle).

McCarthy viewed his Advice Taker as having common-sense, but his definition of common-sense was different than the one above. He defined a program as having common sense "*if it automatically deduces for itself a sufficiently wide class of immediate consequences of anything it is told and what it already knows*."

### Connectionist AI: philosophical challenges and sociological conflicts

Connectionist approaches include earlier work on neural networks, such as perceptrons; work in the mid to late 80s, such as Danny Hillis's Connection Machine and Yann LeCun's advances in convolutional neural networks; to today's more advanced approaches, such as Transformers, GANs, and other work in deep learning.

Three philosophical positions have been outlined among connectionists:

1. Implementationism—where connectionist architectures implement the capabilities for symbolic processing,
2. Radical connectionism—where symbolic processing is rejected totally, and connectionist architectures underlie intelligence and are fully sufficient to explain it,
3. Moderate connectionism—where symbolic processing and connectionist architectures are viewed as complementary and both are required for intelligence.

Olazaran, in his sociological history of the controversies within the neural network community, described the moderate connectionism view as essentially compatible with current research in neuro-symbolic hybrids:

> The third and last position I would like to examine here is what I call the moderate connectionist view, a more eclectic view of the current debate between connectionism and symbolic AI. One of the researchers who has elaborated this position most explicitly is Andy Clark, a philosopher from the School of Cognitive and Computing Sciences of the University of Sussex (Brighton, England). Clark defended hybrid (partly symbolic, partly connectionist) systems. He claimed that (at least) two kinds of theories are needed in order to study and model cognition. On the one hand, for some information-processing tasks (such as pattern recognition) connectionism has advantages over symbolic models. But on the other hand, for other cognitive processes (such as serial, deductive reasoning, and generative symbol manipulation processes) the symbolic paradigm offers adequate models, and not only "approximations" (contrary to what radical connectionists would claim).

Gary Marcus has claimed that the animus in the deep learning community against symbolic approaches now may be more sociological than philosophical:

> To think that we can simply abandon symbol-manipulation is to suspend disbelief.
> 
> And yet, for the most part, that's how most current AI proceeds. Hinton and many others have tried hard to banish symbols altogether. The deep learning hope—seemingly grounded not so much in science, but in a sort of historical grudge—is that intelligent behavior will emerge purely from the confluence of massive data and deep learning. Where classical computers and software solve tasks by defining sets of symbol-manipulating rules dedicated to particular jobs, such as editing a line in a word processor or performing a calculation in a spreadsheet, neural networks typically try to solve tasks by statistical approximation and learning from examples.

According to Marcus, Geoffrey Hinton and his colleagues have been vehemently "anti-symbolic":

> When deep learning reemerged in 2012, it was with a kind of take-no-prisoners attitude that has characterized most of the last decade. By 2015, his hostility toward all things symbols had fully crystallized. He gave a talk at an AI workshop at Stanford comparing symbols to aether, one of science's greatest mistakes.
> 
> ...
> 
> Since then, his anti-symbolic campaign has only increased in intensity. In 2016, Yann LeCun, Bengio, and Hinton wrote a manifesto for deep learning in one of science's most important journals, Nature. It closed with a direct attack on symbol manipulation, calling not for reconciliation but for outright replacement. Later, Hinton told a gathering of European Union leaders that investing any further money in symbol-manipulating approaches was "a huge mistake," likening it to investing in internal combustion engines in the era of electric cars.

Part of these disputes may be due to unclear terminology:

> Turing award winner Judea Pearl offers a critique of machine learning which, unfortunately, conflates the terms machine learning and deep learning. Similarly, when Geoffrey Hinton refers to symbolic AI, the connotation of the term tends to be that of expert systems dispossessed of any ability to learn. The use of the terminology is in need of clarification. Machine learning is not confined to association rule mining, c.f. the body of work on symbolic ML and relational learning (the differences to deep learning being the choice of representation, localist logical rather than distributed, and the non-use of gradient-based learning algorithms). Equally, symbolic AI is not just about production rules written by hand. A proper definition of AI concerns knowledge representation and reasoning, autonomous multi-agent systems, planning and argumentation, as well as learning.

It is worth noting that, from a theoretical perspective, the boundary of advantages between connectionist AI and symbolic AI may not be as clear-cut as it appears. For instance, Heng Zhang and his colleagues have proved that mainstream knowledge representation formalisms are recursively isomorphic, provided they are universal or have equivalent expressive power. This finding implies that there is no fundamental distinction between using symbolic or connectionist knowledge representation formalisms for the realization of artificial general intelligence (AGI). Moreover, the existence of recursive isomorphisms suggests that different technical approaches can draw insights from one another. From this perspective, it seems unnecessary to overemphasize the advantages of any single technical school; instead, mutual learning and integration may offer the most promising path toward the realization of AGI.

### Situated robotics: the world as a model

Another critique of symbolic AI is the embodied cognition approach:

> The embodied cognition approach claims that it makes no sense to consider the brain separately: cognition takes place within a body, which is embedded in an environment. We need to study the system as a whole; the brain's functioning exploits regularities in its environment, including the rest of its body. Under the embodied cognition approach, robotics, vision, and other sensors become central, not peripheral.

Rodney Brooks invented behavior-based robotics, one approach to embodied cognition. Nouvelle AI, another name for this approach, is viewed as an alternative to *both* symbolic AI and connectionist AI. His approach rejected representations, either symbolic or distributed, as not only unnecessary, but as detrimental. Instead, he created the subsumption architecture, a layered architecture for embodied agents. Each layer achieves a different purpose and must function in the real world. For example, the first robot he describes in *Intelligence Without Representation*, has three layers. The bottom layer interprets sonar sensors to avoid objects. The middle layer causes the robot to wander around when there are no obstacles. The top layer causes the robot to go to more distant places for further exploration. Each layer can temporarily inhibit or suppress a lower-level layer. He criticized AI researchers for defining AI problems for their systems, when: "There is no clean division between perception (abstraction) and reasoning in the real world." He called his robots "Creatures" and each layer was "composed of a fixed-topology network of simple finite state machines." In the Nouvelle AI approach, "First, it is vitally important to test the Creatures we build in the real world; i.e., in the same world that we humans inhabit. It is disastrous to fall into the temptation of testing them in a simplified world first, even with the best intentions of later transferring activity to an unsimplified world." His emphasis on real-world testing was in contrast to "Early work in AI concentrated on games, geometrical problems, symbolic algebra, theorem proving, and other formal systems" and the use of the blocks world in symbolic AI systems such as SHRDLU.

### Current views

Each approach—symbolic, connectionist, and behavior-based—has advantages, but has been criticized by the other approaches. Symbolic AI has been criticized as disembodied, liable to the qualification problem, and poor in handling the perceptual problems where deep learning excels. In turn, connectionist AI has been criticized as poorly suited for deliberative step-by-step problem solving, incorporating knowledge, and handling planning. Finally, Nouvelle AI excels in reactive and real-world robotics domains but has been criticized for difficulties in incorporating learning and knowledge.

Hybrid AIs incorporating one or more of these approaches are currently viewed as the path forward. Russell and Norvig conclude that:

> Overall, Dreyfus saw areas where AI did not have complete answers and said that Al is therefore impossible; we now see many of these same areas undergoing continued research and development leading to increased capability, not impossibility.
