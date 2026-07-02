---
title: "Quine–McCluskey algorithm"
source: https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm
domain: logic-synthesis
license: CC-BY-SA-4.0
tags: logic minimization, boolean function synthesis, karnaugh map, two-level logic
fetched: 2026-07-02
---

# Quine–McCluskey algorithm

The **Quine–McCluskey algorithm** (**QMC**), also known as the **method of prime implicants** or the **tabulation method**, is a method used for minimization of Boolean functions that was developed by Willard V. Quine in 1952 and extended by Edward J. McCluskey in 1956. As a general principle this approach had already been demonstrated by the logician Hugh McColl in 1878, was proved by Archie Blake in 1937, and was rediscovered by Edward W. Samson and Burton E. Mills in 1954 and by Raymond J. Nelson in 1955. Also in 1955, Paul W. Abrahams and John G. Nordahl as well as Albert A. Mullin and Wayne G. Kellner proposed a decimal variant of the method.

The Quine–McCluskey algorithm is functionally identical to Karnaugh mapping, but the tabular form makes it more efficient for use in computer algorithms, and it also gives a deterministic way to check that the minimal form of a Boolean F has been reached.

The Quine-McCluskey algorithm works as follows:

1. Finding all prime implicants of the function.
2. Use those prime implicants in a *prime implicant chart* to find the essential prime implicants of the function, as well as other prime implicants that are necessary to cover the function.

## Complexity

Although more practical than Karnaugh mapping when dealing with more than four variables, the Quine–McCluskey algorithm also has a limited range of use since the problem it solves is NP-complete. The running time of the Quine–McCluskey algorithm grows exponentially with the number of variables. For a function of *n* variables the number of prime implicants can be as large as $3^{n}/{\sqrt {n}}$ , e.g. for 32 variables there may be over 534 × 1012 prime implicants. Functions with a large number of variables have to be minimized with potentially non-optimal heuristic methods, of which the Espresso heuristic logic minimizer was the de facto standard in 1995. For one natural class of functions f , the precise complexity of finding all prime implicants is better-understood: Milan Mossé, Harry Sha, and Li-Yang Tan discovered a near-optimal algorithm for finding all prime implicants of a formula in conjunctive normal form.

Step two of the algorithm amounts to solving the set cover problem; NP-hard instances of this problem may occur in this algorithm step.

## Example

### Input

In this example, the input is a Boolean function in four variables, $f:\{0,1\}^{4}\to \{0,1\}$ which evaluates to 1 on the values $4,8,10,11,12$ and $15$ , evaluates to an unknown value on 9 and $14$ , and to 0 everywhere else (where these integers are interpreted in their binary form for input to f for succinctness of notation). The inputs that evaluate to 1 are called 'minterms'. We encode all of this information by writing

$f(A,B,C,D)=\sum m(4,8,10,11,12,15)+d(9,14).\,$

This expression says that the output function f will be 1 for the minterms $4,8,10,11,12$ and $15$ (denoted by the 'm' term) and that we don't care about the output for 9 and $14$ combinations (denoted by the 'd' term). The summation symbol $\sum$ denotes the logical sum (logical OR, or disjunction) of all the terms being summed over.

### Step 1: Finding the prime implicants

First, we write the function as a table (where 'x' stands for don't care):

|   | A | B | C | D | f |
|---|---|---|---|---|---|
| m0 | 0 | 0 | 0 | 0 | 0 |
| m1 | 0 | 0 | 0 | 1 | 0 |
| m2 | 0 | 0 | 1 | 0 | 0 |
| m3 | 0 | 0 | 1 | 1 | 0 |
| m4 | 0 | 1 | 0 | 0 | 1 |
| m5 | 0 | 1 | 0 | 1 | 0 |
| m6 | 0 | 1 | 1 | 0 | 0 |
| m7 | 0 | 1 | 1 | 1 | 0 |
| m8 | 1 | 0 | 0 | 0 | 1 |
| m9 | 1 | 0 | 0 | 1 | x |
| m10 | 1 | 0 | 1 | 0 | 1 |
| m11 | 1 | 0 | 1 | 1 | 1 |
| m12 | 1 | 1 | 0 | 0 | 1 |
| m13 | 1 | 1 | 0 | 1 | 0 |
| m14 | 1 | 1 | 1 | 0 | x |
| m15 | 1 | 1 | 1 | 1 | 1 |

One can easily form the canonical sum of products expression from this table, simply by summing the minterms (leaving out don't-care terms) where the function evaluates to one:

f

A,B,C,D

= A'BC'D' + AB'C'D' + AB'CD' + AB'CD + ABC'D' + ABCD.

which is not minimal. So to optimize, all minterms that evaluate to one are first placed in a minterm table. Don't-care terms are also added into this table (names in parentheses), so they can be combined with minterms:

| Number of 1s | Minterm | Binary Representation |
|---|---|---|
| 1 | m4 | 0100 |
| m8 | 1000 |   |
| 2 | (m9) | 1001 |
| m10 | 1010 |   |
| m12 | 1100 |   |
| 3 | m11 | 1011 |
| (m14) | 1110 |   |
| 4 | m15 | 1111 |

At this point, one can start combining minterms with other minterms in adjacent groups; as in, we compare minterms in nth group with (n+1)th group. So for the m4 minterm in with only one Number of 1s, we compare it to m9, m10, and m12 which have two Number of 1s.

If two terms differ by only a single digit, that digit is replaced with a dash indicating that the digit doesn't matter. For instance `1000` and `1001` can be combined to give `100-`, indicating that both minterms imply the first digit is `1` and the next two are `0`. Terms that can't be combined any more are marked with an asterisk (*).

| Number of 1s | Minterm | 0-Cube | Size 2 Implicants |   |
|---|---|---|---|---|
| 1 | m4 | 0100 | m(4,12) | -100 * |
| m8 | 1000 | m(8,9) | 100- |   |
| — | m(8,10) | 10-0 |   |   |
| — | m(8,12) | 1-00 |   |   |
| 2 | m9 | 1001 | m(9,11) | 10-1 |
| m10 | 1010 | m(10,11) | 101- |   |
| — | m(10,14) | 1-10 |   |   |
| m12 | 1100 | m(12,14) | 11-0 |   |
| 3 | m11 | 1011 | m(11,15) | 1-11 |
| m14 | 1110 | m(14,15) | 111- |   |
| 4 | m15 | 1111 | — |   |

When going from Size 2 to Size 4, treat `-` as a third bit value. Match up the `-`'s first. The terms represent products and to combine two product terms they must have the same variables. One of the variables should be complemented in one term and uncomplemented in the other. The remaining variables present should agree. So to match two terms the `-`'s must align and all but one of the other digits must be the same. For instance, `-110` and `-100` can be combined to give `-1-0`, as can `-110` and `-010` to give `--10`, but `-110` and `011-` cannot since the `-`'s do not align. `-110` corresponds to BCD' while `011-` corresponds to A'BC, and BCD' + A'BC is not equivalent to a product term.

| Number of 1s | Minterm | 0-Cube | Size 2 Implicants | Size 4 Implicants |   |
|---|---|---|---|---|---|
| 1 | m4 | 0100 | m(4,12) | -100 * | — |
| m8 | 1000 | m(8,9) | 100- | m(8,9,10,11) | 10-- * |
| — | m(8,10) | 10-0 | m(8,10,12,14) | 1--0 * |   |
| — | m(8,12) | 1-00 | — |   |   |
| 2 | m9 | 1001 | m(9,11) | 10-1 | — |
| m10 | 1010 | m(10,11) | 101- | m(10,11,14,15) | 1-1- * |
| — | m(10,14) | 1-10 | — |   |   |
| m12 | 1100 | m(12,14) | 11-0 | — |   |
| 3 | m11 | 1011 | m(11,15) | 1-11 | — |
| m14 | 1110 | m(14,15) | 111- | — |   |
| 4 | m15 | 1111 | — | — |   |

Note: In this example, none of the terms in the size 4 implicants table can be combined any further. In general, this process is continued in sizes that are powers of 2 (sizes 8, 16 etc.) until no more terms can be combined.

### Step 2: Prime implicant chart

None of the terms can be combined any further than this, so at this point we construct an essential prime implicant table. Along the side goes the prime implicants that have just been generated (these are the ones that have been marked with a "*" in the previous step), and along the top go the minterms specified earlier. The don't care terms are not placed on top—they are omitted from this section because they are not necessary inputs.

4

8

10

11

12

15

⇒

A

B

C

D

m(4,12)

#

⇒

—

1

0

0

m(8,9,10,11)

⇒

1

0

—

—

m(8,10,12,14)

⇒

1

—

—

0

m(10,11,14,15)

#

⇒

1

—

1

—

To find the essential prime implicants, we look for columns with only one "✓". If a column has only one "✓", this means that the minterm can only be covered by one prime implicant. This prime implicant is *essential*.

For example: in the first column, with minterm 4, there is only one "✓". This means that m(4,12) is essential (hence marked by #). Minterm 15 also has only one "✓", so m(10,11,14,15) is also essential. Now all columns with one "✓" are covered. The rows with minterm m(4,12) and m(10,11,14,15) can now be removed, together with all the columns they cover.

The second prime implicant can be 'covered' by the third and fourth, and the third prime implicant can be 'covered' by the second and first, and neither is thus essential. If a prime implicant is essential then, as would be expected, it is necessary to include it in the minimized Boolean equation. In some cases, the essential prime implicants do not cover all minterms, in which case additional procedures for chart reduction can be employed. The simplest "additional procedure" is trial and error, but a more systematic way is Petrick's method. In the current example, the essential prime implicants do not handle all of the minterms, so, in this case, the essential implicants can be combined with one of the two non-essential ones to yield one equation:

f

A,B,C,D

= BC'D' + AB' + AC

or

f

A,B,C,D

= BC'D' + AD' + AC

Both of those final equations are functionally equivalent to the original, verbose equation:

f

A,B,C,D

= A'BC'D' + AB'C'D' + AB'C'D + AB'CD' + AB'CD + ABC'D' + ABCD' + ABCD.

## Algorithm

### Step 1: Finding the prime implicants

The pseudocode below recursively computes the prime implicants given the list of minterms of a Boolean function. It does this by trying to merge all possible minterms and filtering out minterms that have been merged until no more merges of the minterms can be performed and hence, the prime implicants of the function have been found.

```
// Computes the prime implicants from a list of minterms. 
// each minterm is of the form "1001", "1010", etc and can be represented with a string. 
function getPrimeImplicants(list minterms) is 
    primeImplicants ← empty list
    merges ← new Boolean array of length equal to the number of minterms, each set to false
    numberOfmerges ← 0 
    mergedMinterm, minterm1, minterm2 ← empty strings 

    for i = 0 to length(minterms) do
        for c = i + 1 to length(minterms) do
            minterm1 ← minterms[i]
            minterm2 ← minterms[c]
            // Checking that two minterms can be merged
            if CheckDashesAlign(minterm1, minterm2) && CheckMintermDifference(minterm1, minterm2) then
                mergedMinterm ← MergeMinterms(minterm1, minterm2) 
                if primeImplicants Does Not Contain mergedMinterm then
                    primeImplicants.Add(mergedMinterm) 
                numberOfMerges ← numberOfMerges + 1
                merges[i] ← true
                merges[c] ← true

    // Filtering all minterms that have not been merged as they are prime implicants. Also removing duplicates
    for j = 0 to length(minterms) do
        if merges[j] == false && primeImplicants Does Not Contain minterms[j] then
            primeImplicants.Add(minterms[j]) 

    // if no merges have taken place then all of the prime implicants have been found so return, otherwise 
    // keep merging the minterms. 
    if numberOfmerges == 0 then
        return primeImplicants
    else 
        return getPrimeImplicants(primeImplicants)
```

In this example the `CheckDashesAlign` and `CheckMintermDifference` functions perform the necessary checks for determining whether two minterms can be merged. The function `MergeMinterms` merges the minterms and adds the dashes where necessary. The utility functions below assume that each minterm will be represented using strings.

```
function MergeMinterms(minterm1, minterm2) is
    mergedMinterm ← empty string
    for i = 0 to length(minterm1) do 
        //If the bits vary then replace it with a dash, otherwise the bit remains in the merged minterm.
        if minterm[i] != minterm2[i] then
            mergedMinterm ← mergedMinterm + '-'
        else
            mergedMinterm ← mergedMinterm + minterm1[i] 
    return mergedMinterm

function CheckDashesAlign(minterm1, minterm2) is
    for i = 0 to length(minterm1) do 
        // If one minterm has dashes and the other does not then the minterms cannot be merged. 
        if minterm1[i] != '-' && minterm2[i] == '-' then
            return false 
    return true

function CheckMintermDifference(minterm1, minterm2) is 
    // minterm1 and minterm2 are strings representing all of the currently found prime implicants and merged 
    // minterms. Examples include '01--' and '10-0'
    m1, m2 ← integer representation of minterm1 and minterm2 with the dashes removed, these are replaced with 0
    // ^ here is a bitwise XOR
    res ← m1 ^ m2
    return res != 0 && (res & res - 1) == 0
```

### Step 2: Prime implicant chart

The pseudocode below can be split into two sections:

1. Creating the prime implicant chart using the prime implicants
2. Reading the prime implicant chart to find the essential prime implicants.

#### Creating the prime implicant chart

The prime implicant chart can be represented by a dictionary where each key is a prime implicant and the corresponding value is an empty string that will store a binary string once this step is complete. Each bit in the binary string is used to represent the ticks within the prime implicant chart. The prime implicant chart can be created using the following steps:

1. Iterate through each key (prime implicant of the dictionary).
2. Replace each dash in the prime implicant with the `\d` character code. This creates a regular expression that can be checked against each of the minterms, looking for matches.
3. Iterate through each minterm, comparing the regular expression with the binary representation of the minterm, if there is a match append a `"1"` to the corresponding string in the dictionary. Otherwise append a `"0"`.
4. Repeat for all prime implicants to create the completed prime implicant chart.

When written in pseudocode, the algorithm described above is:

```
function CreatePrimeImplicantChart(list primeImplicants, list minterms) 
    primeImplicantChart ← new dictionary with key of type string and value of type string
    // Creating the empty chart with the prime implicants as the key and empty strings as the value. 
    for i = 0 to length(primeImplicants) do
        // Adding a new prime implicant to the chart. 
        primeImplicantChart.Add(primeImplicants[i], "")
    
    for i = 0 to length(primeImplicantChart.Keys) do
        primeImplicant ← primeImplicantChart.Keys[i]
        // Convert the "-" to "\d" which can be used to find the row of ticks above.
        regularExpression ← ConvertToRegularExpression(primeImplicant)
        for j = 0 to length(minterms) do
            // If there is a match between the regular expression and the minterm than append a 1 otherwise 0. 
            if regularExpression.matches(minterms[j]) then
                primeImplicantChart[primeImplicant] += "1"
            else 
                primeImplicantChart[primeImplicant] += "0"

    // The prime implicant chart is complete so return the completed chart. 
    return primeImplicantChart
```

The utility function, `ConvertToRegularExpression`, is used to convert the prime implicant into the regular expression to check for matches between the implicant and the minterms.

```
function ConvertToRegularExpression(string primeImplicant)
    regularExpression ← new string 
    for i = 0 to length(primeImplicant) do
        if primeImplicant[i] == "-" then
            // Add the literal character "\d". 
            regularExpression += @"\d"
        else
            regularExpression += primeImplicant[i]
    return regularExpression
```

#### Finding the essential prime implicants

Using the function, `CreatePrimeImplicantChart`, defined above, we can find the essential prime implicants by simply iterating column by column of the values in the dictionary, and where a single `"1"` is found then an essential prime implicant has been found. This process is described by the pseudocode below.

```
function getEssentialPrimeImplicants(Dictionary primeImplicantChart, list minterms)
    essentialPrimeImplicants ← new list 
    mintermCoverages ← list with all of the values in the dictionary 
    for i = 0 to length(ticks) do
        mintermCoverage ← ticks[i] 
        for j = 0 to length(mintermCoverage) do
            if mintermCoverage[j] == "1" then
                essentialPrimeImplicants.Add(primeImplicantChart.Keys[i])

    return essentialPrimeImplicants
```

Using the algorithm above it is now possible to find the minimised Boolean expression, by converting the essential prime implicants into the canonical form ie. `-100 -> BC'D'` and separating the implicants by logical OR. The pseudocode assumes that the essential prime implicants will cover the entire Boolean expression.
