---
title: "Randomized response"
source: https://en.wikipedia.org/wiki/Randomized_response
domain: differential-privacy-applied
license: CC-BY-SA-4.0
tags: differential privacy, local differential privacy, privacy budget epsilon, randomized response, statistical disclosure control
fetched: 2026-07-02
---

# Randomized response

**Randomised response** is a research method used in structured survey interview. It was first proposed by S. L. Warner in 1965 and later modified by B. G. Greenberg and coauthors in 1969. It allows respondents to respond to sensitive issues (such as criminal behavior or sexuality) while maintaining confidentiality. Chance decides, unknown to the interviewer, whether the question is to be answered truthfully, or "yes", regardless of the truth.

For example, social scientists have used it to ask people whether they use drugs, whether they have illegally installed telephones, or whether they have evaded paying taxes. Before abortions were legal, social scientists used the method to ask women whether they had had abortions.

The concept is somewhat similar to plausible deniability. Plausible deniability allows the subject to credibly say that they did not make a statement, while the randomized response technique allows the subject to credibly say that they had not been truthful when making a statement.

## Example

### With a coin

A person is asked if they had sex with a prostitute this month. Before they answer, they flip a coin. They are then instructed to answer "yes" if the coin comes up tails, and truthfully, if it comes up heads. Only they know whether their answer reflects the toss of the coin or their true experience. It is very important to assume that people who get heads will answer truthfully, otherwise the surveyor is not able to speculate.

Half the people—or half the questionnaire population—get tails and the other half get heads when they flip the coin. Therefore, half of those people will answer "yes" regardless of whether they have done it. The other half will answer truthfully according to their experience. So whatever proportion of the group said "no", the true number who did not have sex with a prostitute is double that, based on the assumption that the two halves are probably close to the same as it is a large randomized sampling. For example, if 20% of the population surveyed said "no", then the true fraction that did not have sex with a prostitute is 40%.

### With cards

The same question can be asked with three cards which are unmarked on one side, and bear a question on the other side. The cards are randomly mixed, and laid in front of the subject. The subject takes one card, turns it over, and answers the question on it truthfully with either "yes" or "no".

- One card asks: "Did you have sex with a prostitute this month?"
- Another card asks: "Is there a triangle on this card?" (There is no triangle.)
- The last card asks: "Is there a triangle on this card?" (There is a triangle.)

The researcher does not know which question has been asked.

Under the assumption that the "yes" and "no" answers to the control questions cancel each other out, the number of subjects who have had sex with a prostitute is triple that of all "yes" answers in excess of the "no" answers.

## Original version

Warner's original version (1965) is slightly different: The sensitive question is worded in two dichotomous alternatives, and chance decides, unknown to the interviewer, which one is to be answered honestly. The interviewer gets a "yes" or "no" without knowing to which of the two questions. For mathematical reasons chance cannot be "fair" (⁠1/2⁠ and ⁠1/2⁠). Let p be the probability to answer the sensitive question and $EP$ the true proportion of those interviewed bearing the embarrassing property, then the proportion of "yes"-answers $YA$ is composed as follows:

- $YA=p\times EP+(1-p)(1-EP)$

Transformed to yield EP:

- $EP={\frac {YA+p-1}{2p-1}}$

### Example

- Alternative 1: "I have consumed marijuana."
- Alternative 2: "I have never consumed marijuana."

The interviewed are asked to secretly throw a die and answer the first question only if they throw a 6, otherwise the second question ( $p={\tfrac {1}{6}}$ ). The "yes"-answers are now composed of consumers who have thrown a 6 and non-consumers who have thrown a different number. Let the result be 75 "yes"-answers out of 100 interviewed ( $YA={\tfrac {3}{4}}$ ). Inserted into the formula you get

- $EP=({\tfrac {3}{4}}+{\tfrac {1}{6}}-1)/(2\times {\tfrac {1}{6}}-1)={\tfrac {1}{8}}$

If all interviewed have answered honestly then their true proportion of consumers is 1/8 (= 12.5%).
