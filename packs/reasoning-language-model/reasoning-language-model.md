---
title: "Reasoning model"
source: https://en.wikipedia.org/wiki/Reasoning_language_model
domain: reasoning-language-model
license: CC-BY-SA-4.0
tags: reasoning language model, chain of thought prompting, inference time compute, step by step reasoning
fetched: 2026-07-02
---

# Reasoning model

(Redirected from

Reasoning language model

)

A **reasoning model**, also known as a **reasoning language model** (**RLM**) or **large reasoning model** (**LRM**), is a type of large language model (LLM) that has been specifically trained to solve complex tasks requiring multiple steps of logical reasoning. These models demonstrate superior performance on logic, mathematics, and programming tasks compared to standard LLMs. They possess the ability to revisit and revise earlier reasoning steps and utilize additional computation during inference as a method to scale performance, complementing traditional scaling approaches based on training data size, model parameters, and training compute.

## Overview

Unlike traditional language models that generate responses immediately, reasoning models allocate additional compute, or thinking, time before producing an answer to solve multi-step problems. OpenAI introduced this terminology in September 2024 when it released the o1 series, describing the models as designed to "spend more time thinking" before responding. The company framed o1 as a reset in model naming that targets complex tasks in science, coding, and mathematics, and it contrasted o1's performance with GPT-4o on benchmarks such as AIME and Codeforces. Independent reporting the same week summarized the launch and highlighted OpenAI's claim that o1 automates chain-of-thought style reasoning to achieve large gains on difficult exams.

In operation, reasoning models generate internal chains of intermediate steps, then select and refine a final answer. OpenAI reported that o1's accuracy improves as the model is given more reinforcement learning during training and more test-time compute at inference. The company initially chose to hide raw chains and instead return a model-written summary, stating that it "decided not to show" the underlying thoughts so researchers could monitor them without exposing unaligned content to end users. Commercial deployments document separate "reasoning tokens" that meter hidden thinking and a control for "reasoning effort" that tunes how much compute the model uses. These features make the models slower than ordinary chat systems while enabling stronger performance on difficult problems.

## History

The research trajectory toward reasoning models combined advances in supervision, prompting, and search-style inference.

Early alignment work on reinforcement learning from human feedback showed that models can be fine-tuned to follow instructions with "human feedback" and preference-based rewards. In 2022, Google Research scientists Jason Wei and Denny Zhou showed that chain-of-thought prompting "significantly improves the ability" of large models on complex reasoning tasks.

${\text{Input}}\rightarrow \underbrace {{\text{Step}}_{1}\rightarrow {\text{Step}}_{2}\rightarrow \cdots \rightarrow {\text{Step}}_{n}} _{\text{Reasoning chain}}\rightarrow {\text{Answer}}$

A companion result demonstrated that the simple instruction "Let's think step by step" can elicit zero-shot reasoning. Follow-up work introduced self-consistency decoding, which "boosts the performance" of chain-of-thought by sampling diverse solution paths and choosing the consensus, and tool-augmented methods such as *ReAct*, a portmanteau of Reason and Act, that prompt models to "generate both reasoning traces" and actions. Research then generalized chain-of-thought into search over multiple candidate plans. The Tree-of-Thoughts framework from Princeton computer scientist Shunyu Yao proposes that models "perform deliberate decision making" by exploring and backtracking over a tree of intermediate thoughts.

OpenAI's reported breakthrough focused on supervising reasoning processes rather than only outcomes, with Lightman et al.'s "Let's Verify Step by Step" reporting that rewarding each correct step "significantly outperforms outcome supervision" on challenging math problems and improves interpretability by aligning the chain-of-thought with human judgment. OpenAI's o1 announcement ties these strands together with a large-scale reinforcement learning algorithm that trains the model to refine its own chain of thought, and it reports that accuracy rises with more training compute and more time spent thinking at inference.

Together, these developments define the core of reasoning models. They use supervision signals that evaluate the quality of intermediate steps, they exploit inference-time exploration such as consensus or tree search, and they expose controls for how much internal thinking compute to allocate. OpenAI's o1 family made this approach available at scale in September 2024 and popularized the label "reasoning model" for LLMs that deliberately think before they answer.

The development of reasoning models illustrates Richard S. Sutton's "bitter lesson" that scaling compute typically outperforms methods based on human-designed insights. This principle was demonstrated by researchers at the Generative AI Research Lab (GAIR), who initially attempted to replicate o1's capabilities using sophisticated methods including tree search and reinforcement learning in late 2024. Their findings, published in the "o1 Replication Journey" series, revealed that knowledge distillation, a comparatively straightforward technique that trains a smaller model to mimic o1's outputs, produced unexpectedly strong performance. This outcome illustrated how direct scaling approaches can, at times, outperform more complex engineering solutions.

### Drawbacks

Reasoning models require significantly more computational resources during inference compared to non-reasoning models. Research on the American Invitational Mathematics Examination (AIME) benchmark found that reasoning models were 10 to 74 times more expensive to operate than their non-reasoning counterparts. The extended inference time is attributed to the detailed, step-by-step reasoning outputs that these models generate, which are typically much longer than responses from standard large language models that provide direct answers without showing their reasoning process.

One researcher in early 2025 argued that these models may face potential additional denial-of-service concerns with "overthinking attacks."

### Releases

#### 2024

In September 2024, OpenAI released o1-preview, a large language model with enhanced reasoning capabilities. The full version, o1, was released in December 2024. OpenAI initially shared preliminary results on its successor model, o3, in December 2024, with the full o3 model becoming available in 2025.

Alibaba released reasoning versions of its Qwen large language models in November 2024. In December 2024, the company introduced QvQ-72B-Preview, an experimental visual reasoning model.

In December 2024, Google introduced Deep Research in Gemini, a feature designed to conduct multi-step research tasks.

On December 16, 2024, researchers demonstrated that by scaling test-time compute, a relatively small Llama 3B model could outperform a much larger Llama 70B model on challenging reasoning tasks. This experiment suggested that improved inference strategies can unlock reasoning capabilities even in smaller models.

#### 2025

In January 2025, DeepSeek released R1, a reasoning model that achieved performance comparable to OpenAI's o1 at significantly lower computational cost. The release demonstrated the effectiveness of Group Relative Policy Optimization (GRPO), a reinforcement learning technique used to train the model.

On January 25, 2025, DeepSeek enhanced R1 with web search capabilities, allowing the model to retrieve information from the internet while performing reasoning tasks.

Research during this period further validated the effectiveness of knowledge distillation for creating reasoning models. The s1-32B model achieved strong performance through budget forcing and scaling methods, reinforcing findings that simpler training approaches can be highly effective for reasoning capabilities.

On February 2, 2025, OpenAI released Deep Research, a feature powered by their o3 model that enables users to conduct comprehensive research tasks. The system generates detailed reports by automatically gathering and synthesizing information from multiple web sources.

OpenAI called GPT-4.5 its "last non-chain-of-thought model", and implemented with GPT-5 a router model that selects a model based on the difficulty of the task.

#### 2026

In January 2026, Moonshot AI released Kimi K2.5, an open-source 1 trillion parameter MoE model with 32 billion active parameters which was followed by release of Kimi K2.6 in April 2026 with both Kimi models use an “Agent Swarm” system that dynamically decomposes tasks into sub-agents for reasoning and execution, enabling more scalable multi-step problem solving than a single sequential reasoning chain, However both Kimi models despite being identical in parameters have differences in Agent Swarm with K2.5 utilizing a 100 sub-agent format while K2.6 utilized 300 sub-agent which enhanced the latter's ability for task coordination.

## Training

Reasoning models follow the familiar large-scale pretraining used for frontier language models, then diverge in the post-training and optimization. OpenAI reports that o1 is trained with a large-scale reinforcement learning algorithm that teaches the model to use and refine a chain of thought before answering. The company emphasizes two coupled levers, more reinforcement learning during training and more time spent thinking at inference, and it documents smooth gains as each increases. OpenAI also states that it decided not to show raw chains to end users and instead returns a model-written summary, a product choice tied to safety monitoring and competitive concerns.

A central ingredient is process supervision, which rewards intermediate steps rather than only the final answer. OpenAI's study introduced a process reward model trained on step-level labels and found that process supervision significantly outperforms outcome-only supervision on challenging math problems. The project also released the PRM800K step-level feedback dataset and argued that process-level rewards improve interpretability because humans can check each step. These results supplied a practical recipe for supervising chains of thought that was later scaled into production training.

This training differs in important ways from traditional frontier models that do not target reasoning. Standard systems are pretrained on internet-scale corpora with a next-token prediction objective, then aligned through instruction tuning and preference optimization. The canonical InstructGPT recipe first uses supervised fine-tuning on human demonstrations, then trains a reward model from pairwise preferences, and finally optimizes the policy with reinforcement learning, typically PPO with a KL penalty. Variants such as direct preference optimization remove the explicit RL step and optimize the model directly on preference data, but the supervision target is still the final outcome judged by raters rather than the quality of internal steps. Technical reports for GPT-4 summarize this conventional pipeline as next-token pretraining followed by RLHF-style post-training to shape behavior.

In contrast, reasoning models are optimized to produce, critique, and revise multi-step chains during training. OpenAI states that reinforcement learning is applied to the chain itself, which teaches the model to recognize mistakes, break problems into simpler steps, and switch strategies when the current approach fails. OpenAI also documents that it hides chains at inference and returns an answer that summarizes useful ideas from the internal trace. These design choices reflect the model's training objective and its intended monitoring.

Zelikman et al. introduced STaR (Self-Taught Reasoner), which explored bootstrapping rationales by iteratively generating and filtering chains, then fine-tuning on those traces, and they reported gains over outcome-only fine-tuning. One variant of this method supplied additional mechanisms for producing training signals that speak to intermediate reasoning, not only final answers.

DeepSeek reported R1 and R1-Zero systems trained with pure RL to elicit long chains, self-verification, and reflection, arguing that explicit chain-level rewards can induce general reasoning behaviors. These results indicate that post-training focused on chain quality has become a distinct regime separate from outcome-only alignment.

### Supervised fine-tuning

A large language model (LLM) can be fine-tuned on datasets of reasoning tasks paired with step-by-step solution traces. The fine-tuned model learns to produce its own reasoning chains for new problems.

Since human-written traces are expensive to collect, researchers use *rejection sampling fine-tuning* (RFT) to build datasets automatically. This method generates multiple reasoning traces for each prompt, then filters out traces with incorrect final answers using a verifier.

### Reinforcement learning

A pretrained language model can be further trained with reinforcement learning (RL). In RL, a generative language model acts as a policy, denoted $\pi$ . Within this formalism, a task prompt is called the environmental state x , and the model's response is an action y . The probability that the model responds y given x is written as $\pi (y|x)$ .

To further develop a reasoning language model using RL, the next step is to construct a reward model $r(x,y)$ to guide the process. Intuitively, the reward indicates how good a response is for a prompt. In a reasoning task, the reward is high if the response solves the task and low otherwise.

Building on this, a response y may be broken down into multiple steps, denoted $y_{1},y_{2},\dots ,y_{n}$ , where each $y_{n}$ represents a distinct step in the response process.

Most recent systems use policy-gradient methods such as Proximal Policy Optimization (PPO) for this reason, as PPO constrains each policy update with a clipped objective, stabilizing training for very large policies.

#### Outcome reward model

An outcome reward model, or outcome-supervised RM (ORM), gives the reward for a step $r(x,y_{1},\dots ,y_{i})$ based on the final answer: $r(x,y_{1},\dots ,y_{i})=r(x,y_{n})$ . Such models are often called "verifiers".

For tasks with answers that are easy to verify, such as math word problems, the outcome reward can be binary: 1 if the final answer is correct, 0 otherwise. If automatic verification is hard, humans can label answers as correct or not, and those labels can be used to finetune a base model that predicts the human label. For tasks like creative writing, where quality is not simply true or false, one can train a reward model on human ranked preference data, as in reinforcement learning from human feedback. A base model can also be fine-tuned to predict, from a partial thinking trace $x,y_{1},\dots ,y_{m}$ , whether the final answer will be correct, and this prediction can serve as a binary reward.

The ORM is usually trained with logistic regression, i.e. by minimizing cross-entropy loss.

Given a PRM, an ORM can be constructed by multiplying the total process reward during the reasoning trace, by taking the minimum, or by other ways of aggregating process rewards. DeepSeek used a simple ORM to train the R1 model.

#### Process reward model

A process reward model, or process-supervised RM (PRM), gives the reward for a step $r(x,y_{1},\dots ,y_{i})$ based only on the steps so far: $(x,y_{1},\dots ,y_{i})$ .

Given a partial thinking trace $x,y_{1},\dots ,y_{m}$ , a human can judge whether the steps so far are correct, without looking at the final answer. This yields a binary reward. Because human labels are costly, a base model can be fine-tuned to predict them. The PRM is usually trained with logistic regression on the human labels, i.e. by minimizing the cross-entropy loss between true and predicted labels.

As an example, a 2023 OpenAI paper collected 800K process labels for 75K thinking traces. A labeler saw a trace and marked each step as "positive" if it moved toward a solution, "neutral" if it was not wrong but did not help, and "negative" if it was a mistake. After the first "negative" label, the labeler stopped on that trace and moved to another. The authors argued that labeling up to the first error was enough to train a capable PRM, even though labeling later steps could give richer signals.

To avoid human labels, researchers have proposed methods to create PRM without human labels on the processes. Inspired by Monte Carlo tree search (MCTS), the Math-Shepherd method samples multiple continuations until the end, starting at each reasoning step $y_{i}$ , and set the reward at that step to be either ${\frac {\#{\text{(correct answers)}}}{\#{\text{(total answers)}}}}$ in the case of "soft estimation", or ${\begin{cases}1&{\text{if one of the answers is correct}}\\0&{\text{else}}\end{cases}}$ in the case of "hard estimation". This creates process rewards from an ORM, which is often easier or cheaper to construct. A PRM can then be trained on these labels. Some work has tried a fully MCTS approach.

One can also use an ORM to implicitly construct a PRM, similar to direct preference optimization.

#### Guided sampling

A trained ORM can be used to pick the best response. The policy generates several responses, and the ORM selects the best one. This implements a simple form of test-time compute scaling ("best-of-N").

A trained PRM can guide reasoning by a greedy tree search: the policy proposes several next steps, the PRM picks one, and the process repeats. This mirrors using an ORM to pick a whole response. Beam search performs better than greedy search.

*Lookahead search* is another tree search method. The policy proposes several next steps, then makes a short rollout for each. If a solution is found during rollout, the search stops early. Otherwise, the PRM scores each rollout, and the step with the highest score is chosen.

*Self-consistency* can be combined with an ORM. The model generates multiple answers, and the answers are clustered so that each cluster has the same final answer. The ORM scores each answer, scores in each cluster are summed, and the answer from the highest-scoring cluster is returned.

## Benchmarks

Reasoning models generally achieve higher scores than non-reasoning models on many benchmarks, particularly on tasks requiring multi-step reasoning.

For example, on the American Invitational Mathematics Examination (AIME), a challenging mathematics competition, non-reasoning models typically solved fewer than 30% of problems. In contrast, many early reasoning models achieved success rates between 50% and 80%. o3-mini-high, released in January 2025, achieved over 80% accuracy.

Some benchmarks exclude reasoning models due to their longer response times and higher inference costs, including benchmarks for online complex event detection in cyber-physical systems, general inference-time compute evaluation, Verilog engineering tasks, and network security assessments.

## Models

| Company | Model | Release Date |
|---|---|---|
| OpenAI (ChatGPT) | GPT-5 (o3.1) | August 2025 |
| GPT-OSS | August 2025 |   |
| o3 and o4-mini | April 2025 |   |
| o3-mini | January 2025 |   |
| o1 | December 2024 |   |
| o1-preview | September 2024 |   |
| Google Gemini | 3 Flash | December 2025 |
| 3 Pro | November 2025 |   |
| 2.5 Computer Use | October 2025 |   |
| 2.5 Flash | April 2025 |   |
| 2.5 Pro | March 2025 |   |
| 2.0 Flash Thinking | December 2024 |   |
| DeepSeek | V3.2-Exp | September 2025 |
| V3.1 | August 2025 |   |
| R1-0528 | May 2025 |   |
| V3-0324 | March 2025 |   |
| R1 and R1-Lite-Preview | January 2025 |   |
| Alibaba Group | QwQ-32B | March 2025 |
| QvQ-72B-Preview | December 2024 |   |
| QwQ-32B-Preview | November 2024 |   |
| Anthropic | Claude Opus 4.5 | November 2025 |
| Claude Haiku 4.5 | October 2025 |   |
| Claude Sonnet (since 3.7) | February 2025 |   |
| Mistral AI | Magistral Medium / Small | June 2025 |
| xAI | Grok 4 | July 2025 |
| Grok 3 | February 2025 |   |
| Hugging Face | OlympicCoder-7B & 32B | February 2025 |
| NVIDIA | Llama Nemotron | March 2025 |
| Tencent | Hunyuan T1 | March 2025 |
| Moonshot AI | Kimi K2 Thinking | November 2025 |
| Kimi K2.5 | January 2026 |   |
| Kimi K2.6 | April 2026 |   |
