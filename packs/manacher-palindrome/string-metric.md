---
title: "String metric"
source: https://en.wikipedia.org/wiki/String_metric
domain: manacher-palindrome
license: CC-BY-SA-4.0
tags: manacher algorithm, longest palindromic substring, palindrome radius, linear palindrome search
fetched: 2026-07-02
---

# String metric

In mathematics and computer science, a **string metric** (also known as a **string similarity metric** or **string distance function**) is a metric that measures distance ("inverse similarity") between two text strings for approximate string matching or comparison and in fuzzy string searching. A requirement for a string *metric* (e.g. in contrast to string matching) is fulfillment of the triangle inequality. For example, the strings "Sam" and "Samuel" can be considered to be close. A string metric provides a number indicating an algorithm-specific indication of distance.

The most widely known string metric is a rudimentary one called the Levenshtein distance (also known as edit distance). It operates between two input strings, returning a number equivalent to the number of substitutions and deletions needed in order to transform one input string into another. Simplistic string metrics such as Levenshtein distance have expanded to include phonetic, token, grammatical and character-based methods of statistical comparisons.

String metrics are used heavily in information integration and are currently used in areas including fraud detection, fingerprint analysis, plagiarism detection, ontology merging, DNA analysis, RNA analysis, image analysis, evidence-based machine learning, database data deduplication, data mining, incremental search, data integration, malware detection, and semantic knowledge integration.

## List of string metrics

- Levenshtein distance, or its generalization edit distance
- Damerau–Levenshtein distance
- Sørensen–Dice coefficient
- Block distance or L1 distance or City block distance
- Hamming distance
- Simple matching coefficient (SMC)
- Jaccard similarity or Jaccard coefficient or Tanimoto coefficient
- Tversky index
- Overlap coefficient
- Variational distance
- Hellinger distance or Bhattacharyya distance
- Information radius (Jensen–Shannon divergence)
- Skew divergence
- Confusion probability
- Tau metric, an approximation of the Kullback–Leibler divergence
- Fellegi and Sunters metric (SFS)
- Maximal matches
- Grammar-based distance
- TFIDF distance metric

There also exist functions which measure a dissimilarity between strings, but do not necessarily fulfill the triangle inequality, and as such are not *metrics* in the mathematical sense. An example of such function is the Jaro–Winkler distance.

## Selected string measures examples

| Name | Description | Example |
|---|---|---|
| Hamming distance | Only for strings of the same length. Number of changed characters. | "**karolin**" and "**kathrin**" is 3. |
| Levenshtein distance and Damerau–Levenshtein distance | Generalization of Hamming distance that allows for different length strings, and (with Damerau) for transpositions | **k**itt**e**n and **s**itt**i**n**g** have a distance of 3. **k**itten → **s**itten (substitution of "s" for "k") sitt**e**n → sitt**i**n (substitution of "i" for "e") sittin → sittin**g** (insertion of "g" at the end). |
| Jaro–Winkler distance |   | JaroWinklerDist("MARTHA","MARHTA") = $d_{j}={\frac {1}{3}}\left({\frac {m}{\|s_{1}\|}}+{\frac {m}{\|s_{2}\|}}+{\frac {m-t}{m}}\right)={\frac {1}{3}}\left({\frac {6}{6}}+{\frac {6}{6}}+{\frac {6-{\frac {2}{2}}}{6}}\right)=0.944$ m is the number of *matching characters*; t is half the number of *transpositions*(`"MARTHA"[3]!=H, "MARHTA"[3]!=T`). |
| Most frequent k characters |   | MostFreqKeySimilarity('research', 'seeking', 2) = 2 |
