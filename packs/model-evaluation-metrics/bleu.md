---
title: "BLEU"
source: https://en.wikipedia.org/wiki/BLEU
domain: model-evaluation-metrics
license: CC-BY-SA-4.0
tags: model evaluation metrics, precision and recall, confusion matrix, cross validation
fetched: 2026-07-02
---

# BLEU

**BLEU** (**bilingual evaluation understudy**) is an algorithm for evaluating the quality of text which has been machine-translated from one natural language to another. Quality is considered to be the correspondence between a machine's output and that of a human: "the closer a machine translation is to a professional human translation, the better it is" – this is the central idea behind BLEU. Invented at IBM in 2001, BLEU was one of the first metrics to claim a high correlation with human judgements of quality, and remains one of the most popular automated and inexpensive metrics.

Scores are calculated for individual translated segments—generally sentences—by comparing them with a set of good quality reference translations. Those scores are then averaged over the whole corpus to reach an estimate of the translation's overall quality. Intelligibility or grammatical correctness are not taken into account.

BLEU's output is always a number between 0 and 1. This value indicates how similar the candidate text is to the reference texts, with values closer to 1 representing more similar texts. Few human translations will attain a score of 1, since this would indicate that the candidate is identical to one of the reference translations. For this reason, it is not necessary to attain a score of 1. Because there are more opportunities to match, adding additional reference translations will increase the BLEU score.

## Mathematical definition

### Basic setup

A basic, first attempt at defining the BLEU score would take two arguments: a candidate string ${\hat {y}}$ and a list of reference strings $(y^{(1)},...,y^{(N)})$ . The idea is that $BLEU({\hat {y}};y^{(1)},...,y^{(N)})$ should be close to 1 when ${\hat {y}}$ is similar to $y^{(1)},...,y^{(N)}$ , and close to 0 if not.

As an analogy, the BLEU score is like a language teacher trying to score the quality of a student translation ${\hat {y}}$ by checking how closely it follows the reference answers $y^{(1)},...,y^{(N)}$ .

Since in natural language processing, one should evaluate a large set of candidate strings, one must generalize the BLEU score to the case where one has a list of M candidate strings (called a "corpus") $({\hat {y}}^{(1)},\cdots ,{\hat {y}}^{(M)})$ , and for each candidate string ${\hat {y}}^{(i)}$ , a list of reference candidate strings $S_{i}:=(y^{(i,1)},...,y^{(i,N_{i})})$ .

Given any string $y=y_{1}y_{2}\cdots y_{K}$ , and any integer $n\geq 1$ , we define the set of its n-grams to be $G_{n}(y)=\{y_{1}\cdots y_{n},y_{2}\cdots y_{n+1},\cdots ,y_{K-n+1}\cdots y_{K}\}$ Note that it is a set of unique elements, not a multiset allowing redundant elements, so that, for example, $G_{2}(abab)=\{ab,ba\}$ .

Given any two strings $s,y$ , define the substring count $C(s,y)$ to be the number of appearances of s as a substring of y . For example, $C(ab,abcbab)=2$ .

Now, fix a candidate corpus ${\hat {S}}:=({\hat {y}}^{(1)},\cdots ,{\hat {y}}^{(M)})$ , and reference candidate corpus $S=(S_{1},\cdots ,S_{M})$ , where each $S_{i}:=(y^{(i,1)},...,y^{(i,N_{i})})$ .

### Modified n-gram precision

Define the **modified n-gram precision** function to be $p_{n}({\hat {S}};S):={\frac {\sum _{i=1}^{M}\sum _{s\in G_{n}({\hat {y}}^{(i)})}\min(C(s,{\hat {y}}^{(i)}),\max _{y\in S_{i}}C(s,y))}{\sum _{i=1}^{M}\sum _{s\in G_{n}({\hat {y}}^{(i)})}C(s,{\hat {y}}^{(i)})}}$ The modified n-gram, which looks complicated, is merely a straightforward generalization of the prototypical case: one candidate sentence and one reference sentence. In this case, it is $p_{n}(\{{\hat {y}}\};\{y\})={\frac {\sum _{s\in G_{n}({\hat {y}})}\min(C(s,{\hat {y}}),C(s,y))}{\sum _{s\in G_{n}({\hat {y}})}C(s,{\hat {y}})}}$ To work up to this expression, we start with the most obvious n-gram count summation: $\sum _{s\in G_{n}({\hat {y}})}C(s,y)={\text{number of n-substrings in }}{\hat {y}}{\text{ that appear in }}y$ This quantity measures how many n-grams in the reference sentence are reproduced by the candidate sentence. Note that we count the *n-substrings*, not *n-grams*. For example, when ${\hat {y}}=aba,y=abababa,n=2$ , all the 2-substrings in ${\hat {y}}$ (ab and ba) appear in y 3 times each, so the count is 6, not 2.

In the above situation, however, the candidate string is too short. Instead of 3 appearances of $ab$ it contains only one, so we add a minimum function to correct for that: ${\sum _{s\in G_{n}({\hat {y}})}\min(C(s,{\hat {y}}),C(s,y))}$ This count summation cannot be used to compare between sentences, since it is not normalized. If both the reference and the candidate sentences are long, the count could be big, even if the candidate is of very poor quality. So we normalize it ${\frac {\sum _{s\in G_{n}({\hat {y}})}\min(C(s,{\hat {y}}),C(s,y))}{\sum _{s\in G_{n}({\hat {y}})}C(s,{\hat {y}})}}$ The normalization is such that it is always a number in $[0,1]$ , allowing meaningful comparisons between corpuses. It is zero if none of the n-substrings in candidate is in reference. It is one if every n-gram in the candidate appears in reference, for at least as many times as in candidate. In particular, if the candidate is a substring of the reference, then it is one.

### Brevity penalty

The modified n-gram precision unduly gives a high score for candidate strings that are "telegraphic", that is, containing all the n-grams of the reference strings, but for as few times as possible.

In order to punish candidate strings that are too short, define the **brevity penalty** to be $BP({\hat {S}};S):=e^{-(r/c-1)^{+}}$ where $(r/c-1)^{+}=\max(0,r/c-1)$ is the positive part of $r/c-1$ .

- When $r\leq c$ , the brevity penalty $BP=1$ , meaning that we don't punish long candidates, and only punish short candidates.
- When $r>c$ , the brevity penalty $BP=e^{1-r/c}$

c is the length of the candidate corpus, that is, $c:=\sum _{i=1}^{M}|{\hat {y}}^{(i)}|$ where $|y|$ is the length of y .

r is the **effective reference corpus length**, that is, $r:=\sum _{i=1}^{M}|y^{(i,j)}|$ where $y^{(i,j)}=\arg \min _{y\in S_{i}}||y|-|{\hat {y}}^{(i)}||$ , that is, the sentence from $S_{i}$ whose length is as close to $|{\hat {y}}^{(i)}|$ as possible.

### Final formula

There is not a single definition of BLEU, but a whole family of them, parametrized by the weighting vector $w:=(w_{1},w_{2},\cdots )$ . It is a probability distribution on $\{1,2,3,\cdots \}$ , that is, $\sum _{i=1}^{\infty }w_{i}=1$ , and $\forall i\in \{1,2,3,\cdots \},w_{i}\in [0,1]$ .

With a choice of w , the BLEU score is $BLEU_{w}({\hat {S}};S):=BP({\hat {S}};S)\cdot \exp \left(\sum _{n=1}^{\infty }w_{n}\ln p_{n}({\hat {S}};S)\right)$ In words, it is a weighted geometric mean of all the modified n-gram precisions, multiplied by the brevity penalty. We use the weighted geometric mean, rather than the weighted arithmetic mean, to strongly favor candidate corpuses that are simultaneously good according to multiple n-gram precisions.

The most typical choice, the one recommended in the original paper, is $w_{1}=\cdots =w_{4}={\frac {1}{4}}$ .

## Algorithm

This is illustrated in the following example from Papineni et al. (2002):

| Candidate | the | the | the | the | the | the | the |
|---|---|---|---|---|---|---|---|
| Reference 1 | the | cat | is | on | the | mat |   |
| Reference 2 | there | is | a | cat | on | the | mat |

Of the seven words in the candidate translation, all of them appear in the reference translations. Thus the candidate text is given a unigram precision of,

$P={\frac {m}{w_{t}}}={\frac {7}{7}}=1$

where $~m$ is number of words from the candidate that are found in the reference, and $~w_{t}$ is the total number of words in the candidate. This is a perfect score, despite the fact that the candidate translation above retains little of the content of either of the references.

The modification that BLEU makes is fairly straightforward. For each word in the candidate translation, the algorithm takes its maximum total count, $~m_{max}$ , in any of the reference translations. In the example above, the word "the" appears twice in reference 1, and once in reference 2. Thus $~m_{max}=2$ .

For the candidate translation, the count $m_{w}$ of each word is clipped to a maximum of $m_{max}$ for that word. In this case, "the" has $~m_{w}=7$ and $~m_{max}=2$ , thus $~m_{w}$ is clipped to 2. These clipped counts $~m_{w}$ are then summed over all distinct words in the candidate. This sum is then divided by the total number of unigrams in the candidate translation. In the above example, the modified unigram precision score would be:

$P={\frac {2}{7}}$

In practice, however, using individual words as the unit of comparison is not optimal. Instead, BLEU computes the same modified precision metric using n-grams. The length which has the "highest correlation with monolingual human judgements" was found to be four. The unigram scores are found to account for the adequacy of the translation, how much information is retained. The longer n-gram scores account for the fluency of the translation, or to what extent it reads like "good English".

| Model | Set of grams | Score |
|---|---|---|
| Unigram | "the", "the", "cat" | ${\frac {1+1+1}{3}}=1$ |
| Grouped Unigram | "the"*2, "cat"*1 | ${\frac {1+1}{2+1}}={\frac {2}{3}}$ |
| Bigram | "the the", "the cat" | ${\frac {0+1}{2}}={\frac {1}{2}}$ |

An example of a candidate translation for the same references as above might be:

the cat

In this example, the modified unigram precision would be,

$P={\frac {1}{2}}+{\frac {1}{2}}={\frac {2}{2}}$

as the word 'the' and the word 'cat' appear once each in the candidate, and the total number of words is two. The modified bigram precision would be $1/1$ as the bigram, "the cat" appears once in the candidate. It has been pointed out that precision is usually twinned with recall to overcome this problem , as the unigram recall of this example would be $3/6$ or $2/7$ . The problem being that as there are multiple reference translations, a bad translation could easily have an inflated recall, such as a translation which consisted of all the words in each of the references.

To produce a score for the whole corpus, the modified precision scores for the segments are combined using the geometric mean multiplied by a brevity penalty to prevent very short candidates from receiving too high a score. Let r be the total length of the reference corpus, and c the total length of the translation corpus. If $c\leq r$ , the brevity penalty applies, defined to be $e^{(1-r/c)}$ . (In the case of multiple reference sentences, r is taken to be the sum of the lengths of the sentences whose lengths are closest to the lengths of the candidate sentences. However, in the version of the metric used by NIST evaluations prior to 2009, the shortest reference sentence had been used instead.)

iBLEU is an interactive version of BLEU that allows a user to visually examine the BLEU scores obtained by the candidate translations. It also allows comparing two different systems in a visual and interactive manner which is useful for system development.

## Performance

BLEU has frequently been reported as correlating well with human judgement, and remains a benchmark for the assessment of any new evaluation metric. There are however a number of criticisms that have been voiced. It has been noted that, although in principle capable of evaluating translations of any language, BLEU cannot, in its present form, deal with languages lacking word boundaries. Designed to be used for several reference translation, in practice it's used with only the single one. BLEU is infamously dependent on the tokenization technique, and scores achieved with different ones are incomparable (which is often overlooked); in order to improve reproducibility and comparability, SacreBLEU variant was designed.

It has been argued that although BLEU has significant advantages, there is no guarantee that an increase in BLEU score is an indicator of improved translation quality.
