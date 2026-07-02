---
title: "Longest palindromic substring"
source: https://en.wikipedia.org/wiki/Longest_palindromic_substring
domain: manacher-palindrome
license: CC-BY-SA-4.0
tags: manacher algorithm, longest palindromic substring, palindrome radius, linear palindrome search
fetched: 2026-07-02
---

# Longest palindromic substring

In computer science, the **longest palindromic substring** or **longest symmetric factor** problem is the problem of finding a maximum-length contiguous substring of a given string that is also a palindrome. For example, the longest palindromic substring of "bananas" is "anana". The longest palindromic substring is not guaranteed to be unique; for example, in the string "abracadabra", there is no palindromic substring with length greater than three, but there are two palindromic substrings with length three, namely, "aca" and "ada". In some applications it may be necessary to return all maximal palindromic substrings (that is, all substrings that are themselves palindromes and cannot be extended to larger palindromic substrings) rather than returning only one substring or returning the maximum length of a palindromic substring.

Manacher (1975) invented an $O(n)$ -time algorithm for listing all the palindromes that appear at the start of a given string of length n . However, as observed e.g., by Apostolico, Breslauer & Galil (1995), the same algorithm can also be used to find all maximal palindromic substrings anywhere within the input string, again in $O(n)$ time. Therefore, it provides an $O(n)$ -time solution to the longest palindromic substring problem. Alternative $O(n)$ -time solutions were provided by Jeuring (1994), and by Gusfield (1997), who described a solution based on suffix trees. A faster algorithm can be achieved in the word RAM model of computation if the size $\sigma$ of the input alphabet is in $2^{o(\log n)}$ . In particular, this algorithm runs in $O(n\log \sigma /\log n)$ time using $O(n\log \sigma /\log n)$ space. Efficient parallel algorithms are also known for the problem.

The longest palindromic substring problem should not be confused with the different problem of finding the longest palindromic subsequence.

## Slower algorithm

This algorithm is slower than Manacher's algorithm, but is a good stepping stone for understanding Manacher's algorithm. It looks at each character as the center of a palindrome and loops to determine the largest palindrome with that center.

The loop at the center of the function only works for palindromes where the length is an odd number. The function works for even-length palindromes by modifying the input string. The character '|' is inserted between every character in the inputs string, and at both ends. So the input "book" becomes "|b|o|o|k|". The even-length palindrome "oo" in "book" becomes the odd-length palindrome "|o|o|".

```mw
// C pseudocode.
Longest_Palindrome_SLOW(string S, string R) {
    // R == S with a bogus character (eg. '|') inserted
    // between each character (including outer boundaries)

    // The radius of the longest palindrome centered on each place in R
    // note: length(R) = length(PalindromeRadii) = 2 × length(S) + 1

    array PalindromeRadii = [0,...,0]

    Center = 0

    while Center < length(R) {
        // Determine the longest palindrome starting
        // at Center-Radius and going to Center+Radius
        Radius = 0

        while Center-(Radius + 1) >= 0 and
              Center+(Radius + 1) < length(R) and
              R[Center-(Radius + 1)] = R[Center+(Radius + 1)] {
            Radius = Radius + 1
        }

        // Save the radius of the longest palindrome in the array

        PalindromeRadii[Center] = Radius

        Center = Center + 1
    }

    // One can show that longest_palindrome_in_S is max(PalindromeRadii).
    // if R[i] == '|', PalindromeRadii[i] is even, otherwise you could increase PalindromeRadii[i] by 1,
    // which is equivalent to inserting an extra '|' in each border.
    // Remember that a palindrome centered in an '|' in R corresponds to an even palindrome in S.
    // if R[i] != '|', PalindromeRadii[i] is odd (same argument), and corresponds to an odd palindrome.
    // In this case, the length of the palindrome
    // centered at that character is also x=PalindromeRadii[i], as we have (x-1)/2 characters on each side,
    // plus the extra middle one ((x-1)/2*2+1=x)
    longest_palindrome_in_S = max(PalindromeRadii)

    return longest_palindrome_in_S
}
```

The runtime of this algorithm is $O(n^{2})$ . The outer loop runs n times and the inner loop can run up to $n/2$ times.

## Manacher's algorithm

Below is the pseudocode for Manacher's algorithm. The algorithm is faster than the previous algorithm because it exploits when a palindrome happens inside another palindrome.

For example, consider the input string "abacaba". By the time it gets to the "c", Manacher's algorithm will have identified the length of every palindrome centered on the letters before the "c". At the "c", it runs a loop to identify the largest palindrome centered on the "c": "abacaba". With that knowledge, everything after the "c" looks like the reflection of everything before the "c". The "a" after the "c" has the same longest palindrome as the "a" before the "c". Similarly, the "b" after the "c" has a longest palindrome that is *at least* the length of the longest palindrome centered on the "b" before the "c". There are some special cases to consider, but that trick speeds up the computation dramatically.

```mw
// C pseudocode.
Longest_Palindrome(string S, string R) {
    // R == S with a bogus character (eg. '|') inserted
    // between each character (including outer boundaries)

    // The radius of the longest palindrome centered on each place in R
    // note: length(R) = length(PalindromeRadii) = 2 × length(S) + 1

    array PalindromeRadii = [0,...,0]

    Center = 0
    Radius = 0

    while Center < length(R) {
        // At the start of the loop, Radius is already set to a lower-bound
        // for the longest radius. In the first iteration, Radius is 0, but
        // it can be higher on later iterations.

        // Determine the longest palindrome starting at Center-Radius and
        // going to Center+Radius

        while Center-(Radius+1) >= 0 and
              Center+(Radius+1) < length(R) and
              R[Center-(Radius+1)] = R[Center+(Radius+1)] {
            Radius = Radius+1
        }

        // Save the radius of the longest palindrome in the array
        PalindromeRadii[Center] = Radius

        // Below, Center is incremented.
        // If any precomputed values can be reused, they are.
        // Also, Radius may be set to a value greater than 0

        OldCenter = Center
        OldRadius = Radius
        Center = Center+1

        // Radius' default value will be 0, if we reach the end of the
        // following loop.
        Radius = 0

        while Center <= OldCenter + OldRadius {

            // Because Center lies inside the old palindrome and every
            // character inside a palindrome has a "mirrored" character
            // reflected across its center, we can use the data that was
            // precomputed for the Center's mirrored point.

            MirroredCenter = OldCenter - (Center - OldCenter)
            MaxMirroredRadius = OldCenter + OldRadius - Center

            if PalindromeRadii[MirroredCenter] < MaxMirroredRadius {

                // The palindrome centered at MirroredCenter is entirely
                // contained in the palindrome centered at OldCenter. So,
                // MirroredCenter and Center have the same sized palindrome

                PalindromeRadii[Center] = PalindromeRadii[MirroredCenter]
                Center = Center+1
            } else if PalindromeRadii[MirroredCenter] > MaxMirroredRadius {

                // The palindrome at MirroredCenter extends beyond the
                // palindrome at OldCenter The palindrome at Center must
                // end at the edge of the OldCenter palindrome. Otherwise,
                // the palindrome at OldCenter would be bigger

                PalindromeRadii[Center] = MaxMirroredRadius
                Center = Center+1
            } else { // PalindromeRadii[MirroredCenter] = MaxMirroredRadius

                // Since the palindrome at MirroredCenter ends exactly at
                // the edge of the palindrome centered at OldCenter, the
                // palindrome at Center might be bigger. Set Radius to the
                // minimum size of the palindrome at Center so it doesn't
                // recheck unnecessarily

                Radius = MaxMirroredRadius
                break
            }
        }
    }

    // A palindrome's size is equal to its radius * 2. However, since our
    // variable Radius considers our bogus characters to the side of the
    // center, the size of its corresponding palindrome is actually 2 *
    // (Radius / 2), which means a palindrome's size is equal to its
    // corresponding Radius value in PalindromeRadii

    longest_palindrome_in_S = max(PalindromeRadii)
    return longest_palindrome_in_S
}
```

### Special cases

Manacher's algorithm is faster because it reuses precomputed data when a palindrome exists inside another palindrome. There are 3 cases of this. They are represented by the "if / else if / else" statement in the pseudocode.

The first case is when the palindrome at `MirroredCenter` lies completely inside the "Old" palindrome. In this situation, the palindrome at `Center` will have the same length as the one at `MirroredCenter`. For example, if the "Old" palindrome is "abcbpbcba", we can see that the palindrome centered on "c" after the "p" must have the same length as the palindrome centered on the "c" before the "p".

The second case is when the palindrome at `MirroredCenter` extends outside the "Old" palindrome. That is, it extends "to the left" (or, contains characters with a lower index than any inside the "Old" palindrome). Because the "Old" palindrome is the largest possible palindrome centered on `OldCenter`, we know the characters before and after it are different. Thus, the palindrome at `Center` will run exactly up to the border of the "Old" palindrome, because the next character will be different than the one inside the palindrome at `MirroredCenter`. For example, if the string was "ababc", the "Old" palindrome could be "bab" with the `Center` being the second "b" and the `MirroredCenter` being the first "b". Since the palindrome at the `MirroredCenter` is "aba" and extends beyond the boundaries of the "Old" palindrome, we know the longest palindrome at the second "b" can only extend up to the border of the "Old" palindrome. We know this because if the character after the "Old" palindrome had been an "a" instead of a "c", the "Old" palindrome would have been longer.

The third and last case is when the palindrome at `MirroredCenter` extends exactly up to the border of the "Old" palindrome. In this case, we don't know if the character after the "Old" palindrome might make the palindrome at `Center` longer than the one at `MirroredCenter`. But we do know that the palindrome at `Center` is *at least* as long as the one at `MirroredCenter`. In this case, `Radius` is initialized to the radius of the palindrome at `MirroredCenter` and the search starts from there. An example string would be "abcbpbcbp" where the "Old" palindrome is "bcbpbcb" and the `Center` is on the second "c". The `MirroredCenter` is the first "c" and it has a longest palindrome of "bcb". The longest palindrome at the `Center` on the second "c" has to be at least that long and, in this case, is longer.

### Runtime

The algorithm runs in linear time. This can be seen by noting that `Center` strictly increases after each outer loop and the sum `Center + Radius` is non-decreasing. Moreover, the number of operations in the first inner loop is linear in the increase of the sum `Center + Radius` while the number of operations in the second inner loop is linear in the increase of `Center`. Since `Center ≤ 2n+1` and `Radius ≤ n`, the total number of operations in the first and second inner loops is $O(n)$ and the total number of operations in the outer loop, other than those in the inner loops, is also $O(n)$ . The overall running time is therefore $O(n)$ .
