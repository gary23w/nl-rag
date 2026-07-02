---
title: "C Programming/String manipulation"
source: https://en.wikibooks.org/wiki/C_Programming/String_manipulation
domain: c-book
license: CC-BY-SA-4.0 (Wikibooks C Programming)
tags: c pointers, c arrays, c memory management, c strings
fetched: 2026-07-02
---

# C Programming/String manipulation

<

C Programming

A **string** in C is merely an array of characters. The length of a string is determined by a terminating null character: `'\0'`. So, a string with the contents, say, `"abc"` has four characters: `'a'`, `'b'`, `'c'`, and the terminating null (`'\0'`) character.

The terminating null character has the value zero.

## Syntax

In C, string constants (literals) are surrounded by double quotes ("), e.g. "Hello world!" and are compiled to an array of the specified char values with an additional null terminating character (0-valued) code to mark the end of the string. The type of a string constant is char [].

### backslash escapes

String literals may not directly in the source code contain embedded newlines or other control characters, or some other characters of special meaning in string.

To include such characters in a string, the backslash escapes may be used, like this:

| Escape | Meaning |
|---|---|
| \\ | Literal backslash |
| \" | Double quote |
| \' | Single quote |
| \n | Newline (line feed) |
| \r | Carriage return |
| \b | Backspace |
| \t | Horizontal tab |
| \f | Form feed |
| \a | Alert (bell) |
| \v | Vertical tab |
| \? | Question mark (used to escape trigraphs) |
| \*nnn* | Character with octal value *nnn* |
| \x*hh* | Character with hexadecimal value *hh* |

### Wide character strings

C supports wide character strings, defined as arrays of the type wchar_t, 16-bit (at least) values. They are written with an L before the string like this

wchar_t *p = L"Hello

world!";

This feature allows strings where more than 256 different possible characters are needed (although also variable length char strings can be used). They end with a zero-valued wchar_t. These strings are not supported by the <string.h> functions. Instead they have their own functions, declared in <wchar.h>.

### Character encodings

What character encoding the char and wchar_t represent is not specified by the C standard, except that the value 0x00 and 0x0000 specify the end of the string and not a character. It is the input and output code which are directly affected by the character encoding. Other code should not be too affected. The editor should also be able to handle the encoding if strings shall be able to be written in the source code.

There are three major types of encodings:

- One byte per character. Normally based on ASCII. There is a limit of 255 different characters plus the zero termination character.
- Variable length char strings, which allows many more than 255 different characters. Such strings are written as normal char-based arrays. These encodings are normally ASCII-based and examples are UTF-8 or Shift JIS.
- Wide character strings. They are arrays of wchar_t values. UTF-16 is the most common such encoding, and it is also variable-length, meaning that a character can be two wchar_t.

## The `<string.h>` standard header

Because programmers find raw strings cumbersome to deal with, they wrote the code in the `<string.h>` library. It represents not a concerted design effort but rather the accretion of contributions made by various authors over a span of years.

First, three types of functions exist in the string library:

- the `mem` functions manipulate sequences of arbitrary characters without regard to the null character;
- the `str` functions manipulate null-terminated sequences of characters;
- the `strn` functions manipulate sequences of non-null characters.

### The more commonly-used string functions

The nine most commonly used functions in the string library are:

- `strcat` - concatenate two strings
- `strchr` - string scanning operation
- `strcmp` - compare two strings
- `strcpy` - copy a string
- `strlen` - get string length
- `strncat` - concatenate one string with part of another
- `strncmp` - compare parts of two strings
- `strncpy` - copy part of a string
- `strrchr` - string scanning operation

Other functions, such as `strlwr` (convert to lower case), `strrev` (return the string reversed), and `strupr` (convert to upper case) may be popular; however, they are neither specified by the C Standard nor the Single Unix Standard. It is also unspecified whether these functions return copies of the original strings or convert the strings in place.

#### The `strcat` function

```mw
char *strcat(char * restrict s1, const char * restrict s2);
```

*Some people recommend using* `strncat()` *or* `strlcat()` *instead of strcat, in order to avoid buffer overflow.*

The `strcat()` function shall append a copy of the string pointed to by `s2` (including the terminating null byte) to the end of the string pointed to by `s1`. The initial byte of `s2` overwrites the null byte at the end of `s1`. If copying takes place between objects that overlap, the behavior is undefined. The function returns `s1`.

This function is used to attach one string to the end of another string. It is imperative that the first string (`s1`) have the space needed to store both strings.

Example:

```mw
#include <stdio.h>
#include <string.h>
...
static const char *colors[] = {"Red","Orange","Yellow","Green","Blue","Purple" };
static const char *widths[] = {"Thin","Medium","Thick","Bold" };
...
char penText[20];
...
int penColor = 3, penThickness = 2;
strcpy(penText, colors[penColor]);
strcat(penText, widths[penThickness]);
printf("My pen is %s\n", penText); /* prints 'My pen is GreenThick' */
```

Before calling `strcat()`, the destination must currently contain a null terminated string or the first character must have been initialized with the null character (e.g. `penText[0] = '\0';`).

The following is a public-domain implementation of `strcat`:

```mw
#include <string.h>
/* strcat */
char *(strcat)(char *restrict s1, const char *restrict s2)
{
    char *s = s1;
    /* Move s so that it points to the end of s1.  */
    while (*s != '\0')
        s++;
    /* Copy the contents of s2 into the space at the end of s1.  */
    strcpy(s, s2);
    return s1;
}
```

#### The `strchr` function

```mw
char *strchr(const char *s, int c);
```

The `strchr()` function shall locate the first occurrence of `c` (converted to a `char`) in the string pointed to by `s`. The terminating null byte is considered to be part of the string. The function returns the location of the found character, or a null pointer if the character was not found.

This function is used to find certain characters in strings.

At one point in history, this function was named `index`. The `strchr` name, however cryptic, fits the general pattern for naming.

The following is a public-domain implementation of `strchr`:

```mw
#include <string.h>
/* strchr */
char *(strchr)(const char *s, int c)
{
    char ch = c;
    /* Scan s for the character.  When this loop is finished,
       s will either point to the end of the string or the
       character we were looking for.  */
    while (*s != '\0' && *s != ch)
        s++;
    return (*s == ch) ? (char *) s : NULL;
}
```

#### The `strcmp` function

```mw
int strcmp(const char *s1, const char *s2);
```

A rudimentary form of string comparison is done with the strcmp() function. It takes two strings as arguments and returns a value less than zero if the first is lexographically less than the second, a value greater than zero if the first is lexographically greater than the second, or zero if the two strings are equal. The comparison is done by comparing the coded (ascii) value of the characters, character by character.

This simple type of string comparison is nowadays generally considered unacceptable when sorting lists of strings. More advanced algorithms exist that are capable of producing lists in dictionary sorted order. They can also fix problems such as strcmp() considering the string "Alpha2" greater than "Alpha12". (In the previous example, "Alpha2" compares greater than "Alpha12" because '2' comes after '1' in the character set.) What we're saying is, don't use this `strcmp()` alone for general string sorting in any commercial or professional code.

The `strcmp()` function shall compare the string pointed to by `s1` to the string pointed to by `s2`. The sign of a non-zero return value shall be determined by the sign of the difference between the values of the first pair of bytes (both interpreted as type `unsigned char`) that differ in the strings being compared. Upon completion, `strcmp()` shall return an integer greater than, equal to, or less than 0, if the string pointed to by `s1` is greater than, equal to, or less than the string pointed to by `s2`, respectively.

Since comparing pointers by themselves is not practically useful unless one is comparing pointers within the same array, this function lexically compares the strings that two pointers point to.

This function is useful in comparisons, e.g.

```mw
if (strcmp(s, "whatever") == 0)
    /* do something */;
```

The collating sequence used by `strcmp()` is equivalent to the machine's native character set. The only guarantee about the order is that the digits from '0' to '9' are in consecutive order.

The following is a public-domain implementation of `strcmp`:

```mw
#include <string.h>
/* strcmp */
int (strcmp)(const char *s1, const char *s2)
{
    unsigned char uc1, uc2;
    /* Move s1 and s2 to the first differing characters 
       in each string, or the ends of the strings if they
       are identical.  */
    while (*s1 != '\0' && *s1 == *s2) {
        s1++;
        s2++;
    }
    /* Compare the characters as unsigned char and
       return the difference.  */
    uc1 = (*(unsigned char *) s1);
    uc2 = (*(unsigned char *) s2);
    return ((uc1 < uc2) ? -1 : (uc1 > uc2));
}
```

#### The `strcpy` function

```mw
char *strcpy(char *restrict s1, const char *restrict s2);
```

*Some people recommend always using* `strncpy()` *instead of strcpy, to avoid buffer overflow.*

The `strcpy()` function shall copy the C string pointed to by `s2` (including the terminating null byte) into the array pointed to by `s1`. If copying takes place between objects that overlap, the behavior is undefined. The function returns `s1`. There is no value used to indicate an error: if the arguments to `strcpy()` are correct, and the destination buffer is large enough, the function will never fail.

Example:

```mw
#include <stdio.h>
#include <string.h>
/* ... */
static const char *penType="round";
/* ... */
char penText[20];
/* ... */
strcpy(penText, penType);
```

Important: You must ensure that the destination buffer (`s1`) is able to contain all the characters in the source array, including the terminating null byte. Otherwise, `strcpy()` will overwrite memory past the end of the buffer, causing a buffer overflow, which can cause the program to crash, or can be exploited by hackers to compromise the security of the computer.

The following is a public-domain implementation of `strcpy`:

```mw
#include <string.h>
/* strcpy */
char *(strcpy)(char *restrict s1, const char *restrict s2)
{
    char *dst = s1;
    const char *src = s2;
    /* Do the copying in a loop.  */
    while ((*dst++ = *src++) != '\0')
        ;               /* The body of this loop is left empty. */
    /* Return the destination string.  */
    return s1;
}
```

#### The `strlen` function

```mw
size_t strlen(const char *s);
```

The `strlen()` function shall compute the number of bytes in the string to which `s` points, not including the terminating null byte. It returns the number of bytes in the string. No value is used to indicate an error.

The following is a public-domain implementation of `strlen`:

```mw
#include <string.h>
/* strlen */
size_t (strlen)(const char *s)
{
    const char *p = s; /* pointer to character constant */
    /* Loop over the data in s.  */
    while (*p != '\0')
        p++;
    return (size_t)(p - s);
}
```

Note how the line

```mw
const char *p = s
```

declares and initializes a pointer `p` to an integer constant, i.e. `p` cannot change the value it points to.

#### The `strncat` function

```mw
char *strncat(char *restrict s1, const char *restrict s2, size_t n);
```

The `strncat()` function shall append not more than `n` bytes (a null byte and bytes that follow it are not appended) from the array pointed to by `s2` to the end of the string pointed to by `s1`. The initial byte of `s2` overwrites the null byte at the end of `s1`. A terminating null byte is always appended to the result. If copying takes place between objects that overlap, the behavior is undefined. The function returns `s1`.

The following is a public-domain implementation of `strncat`:

```mw
#include <string.h>
/* strncat */
char *(strncat)(char *restrict s1, const char *restrict s2, size_t n)
{
    char *s = s1;
    /* Loop over the data in s1.  */
    while (*s != '\0')
        s++;
    /* s now points to s1's trailing null character, now copy
       up to n bytes from s2 into s stopping if a null character
       is encountered in s2.
       It is not safe to use strncpy here since it copies EXACTLY n
       characters, NULL padding if necessary.  */
    while (n != 0 && (*s = *s2++) != '\0') {
        n--;
        s++;
    }
    if (*s != '\0')
        *s = '\0';
    return s1;
}
```

#### The `strncmp` function

```mw
int strncmp(const char *s1, const char *s2, size_t n);
```

The `strncmp()` function shall compare not more than `n` bytes (bytes that follow a null byte are not compared) from the array pointed to by `s1` to the array pointed to by `s2`. The sign of a non-zero return value is determined by the sign of the difference between the values of the first pair of bytes (both interpreted as type `unsigned char`) that differ in the strings being compared. See `strcmp` for an explanation of the return value.

This function is useful in comparisons, as the `strcmp` function is.

The following is a public-domain implementation of `strncmp`:

```mw
#include <string.h>
/* strncmp */
int (strncmp)(const char *s1, const char *s2, size_t n)
{
    unsigned char uc1, uc2;
    /* Nothing to compare?  Return zero.  */
    if (n == 0)
        return 0;
    /* Loop, comparing bytes.  */
    while (n-- > 0 && *s1 == *s2) {
        /* If we've run out of bytes or hit a null, return zero
           since we already know *s1 == *s2.  */
        if (n == 0 || *s1 == '\0')
            return 0;
        s1++;
        s2++;
    }
    uc1 = (*(unsigned char *) s1);
    uc2 = (*(unsigned char *) s2);
    return ((uc1 < uc2) ? -1 : (uc1 > uc2));
}
```

#### The `strncpy` function

```mw
char *strncpy(char *restrict s1, const char *restrict s2, size_t n);
```

The `strncpy()` function shall copy not more than `n` bytes (bytes that follow a null byte are not copied) from the array pointed to by `s2` to the array pointed to by `s1`. If copying takes place between objects that overlap, the behavior is undefined. If the array pointed to by `s2` is a string that is shorter than `n` bytes, null bytes shall be appended to the copy in the array pointed to by `s1`, until `n` bytes in all are written. The function shall return s1; no return value is reserved to indicate an error.

It is possible that the function will **not** return a null-terminated string, which happens if the `s2` string is longer than `n` bytes.

The following is a public-domain version of `strncpy`:

```mw
#include <string.h>
/* strncpy */
char *(strncpy)(char *restrict s1, const char *restrict s2, size_t n)
{
    char *dst = s1;
    const char *src = s2;
    /* Copy bytes, one at a time.  */
    while (n > 0) {
        n--;
        if ((*dst++ = *src++) == '\0') {
            /* If we get here, we found a null character at the end
               of s2, so use memset to put null bytes at the end of
               s1.  */
            memset(dst, '\0', n);
            break;
        }
    }
    return s1;
}
```

#### The `strrchr` function

```mw
char *strrchr(const char *s, int c);
```

The `strrchr` function is similar to the `strchr` function, except that `strrchr` returns a pointer to the **last** occurrence of `c` within `s` instead of the first.

The `strrchr()` function shall locate the last occurrence of `c` (converted to a `char`) in the string pointed to by `s`. The terminating null byte is considered to be part of the string. Its return value is similar to `strchr`'s return value.

At one point in history, this function was named `rindex`. The `strrchr` name, however cryptic, fits the general pattern for naming.

The following is a public-domain implementation of `strrchr`:

```mw
#include <string.h>
/* strrchr */
char *(strrchr)(const char *s, int c)
{
    const char *last = NULL;
    /* If the character we're looking for is the terminating null,
       we just need to look for that character as there's only one
       of them in the string.  */
    if (c == '\0')
        return strchr(s, c);
    /* Loop through, finding the last match before hitting NULL.  */
    while ((s = strchr(s, c)) != NULL) {
        last = s;
        s++;
    }
    return (char *) last;
}
```

### The less commonly-used string functions

The less-used functions are:

- `memchr` - Find a byte in memory
- `memcmp` - Compare bytes in memory
- `memcpy` - Copy bytes in memory
- `memmove` - Copy bytes in memory with overlapping areas
- `memset` - Set bytes in memory
- `strcoll` - Compare bytes according to a locale-specific collating sequence
- `strcspn` - Get the length of a complementary substring
- `strerror` - Get error message
- `strpbrk` - Scan a string for a byte
- `strspn` - Get the length of a substring
- `strstr` - Find a substring
- `strtok` - Split a string into tokens
- `strxfrm` - Transform string

#### Copying functions

##### The `memcpy` function

```mw
void *memcpy(void * restrict s1, const void * restrict s2, size_t n);
```

The `memcpy()` function shall copy `n` bytes from the object pointed to by `s2` into the object pointed to by `s1`. If copying takes place between objects that overlap, the behavior is undefined. The function returns `s1`.

Because the function does not have to worry about overlap, it can do the simplest copy it can.

The following is a public-domain implementation of `memcpy`:

```mw
#include <string.h>
/* memcpy */
void *(memcpy)(void * restrict s1, const void * restrict s2, size_t n)
{
    char *dst = s1;
    const char *src = s2;
    /* Loop and copy.  */
    while (n-- != 0)
        *dst++ = *src++;
    return s1;
}
```

##### The `memmove` function

```mw
void *memmove(void *s1, const void *s2, size_t n);
```

The `memmove()` function shall copy `n` bytes from the object pointed to by `s2` into the object pointed to by `s1`. Copying takes place as if the `n` bytes from the object pointed to by `s2` are first copied into a temporary array of `n` bytes that does not overlap the objects pointed to by `s1` and `s2`, and then the `n` bytes from the temporary array are copied into the object pointed to by `s1`. The function returns the value of `s1`.

The easy way to implement this without using a temporary array is to check for a condition that would prevent an ascending copy, and if found, do a descending copy.

The following is a public-domain, though not completely portable, implementation of `memmove`:

```mw
#include <string.h>
/* memmove */
void *(memmove)(void *s1, const void *s2, size_t n) 
{
   /* note: these don't have to point to unsigned chars */
   char *p1 = s1;
   const char *p2 = s2;
   /* test for overlap that prevents an ascending copy */
   if (p2 < p1 && p1 < p2 + n) {
       /* do a descending copy */
       p2 += n;
       p1 += n;
       while (n-- != 0) 
           *--p1 = *--p2;
   } else 
       while (n-- != 0) 
           *p1++ = *p2++;
   return s1; 
}
```

#### Comparison functions

##### The `memcmp` function

```mw
int memcmp(const void *s1, const void *s2, size_t n);
```

The `memcmp()` function shall compare the first `n` bytes (each interpreted as `unsigned char`) of the object pointed to by `s1` to the first `n` bytes of the object pointed to by `s2`. The sign of a non-zero return value shall be determined by the sign of the difference between the values of the first pair of bytes (both interpreted as type `unsigned char`) that differ in the objects being compared.

The following is a public-domain implementation of `memcmp`:

```mw
#include <string.h>
/* memcmp */
int (memcmp)(const void *s1, const void *s2, size_t n)
{
    const unsigned char *us1 = (const unsigned char *) s1;
    const unsigned char *us2 = (const unsigned char *) s2;
    while (n-- != 0) {
        if (*us1 != *us2)
            return (*us1 < *us2) ? -1 : +1;
        us1++;
        us2++;
    }
    return 0;
}
```

##### The `strcoll` and `strxfrm` functions

```mw
int strcoll(const char *s1, const char *s2);
```

```mw
size_t strxfrm(char *s1, const char *s2, size_t n);
```

The ANSI C Standard specifies two locale-specific comparison functions.

The `strcoll` function compares the string pointed to by `s1` to the string pointed to by `s2`, both interpreted as appropriate to the `LC_COLLATE` category of the current locale. The return value is similar to `strcmp`.

The `strxfrm` function transforms the string pointed to by `s2` and places the resulting string into the array pointed to by `s1`. The transformation is such that if the `strcmp` function is applied to the two transformed strings, it returns a value greater than, equal to, or less than zero, corresponding to the result of the `strcoll` function applied to the same two original strings. No more than `n` characters are placed into the resulting array pointed to by `s1`, including the terminating null character. If `n` is zero, `s1` is permitted to be a null pointer. If copying takes place between objects that overlap, the behavior is undefined. The function returns the length of the transformed string.

These functions are rarely used and nontrivial to code, so there is no code for this section.

##### The `memchr` function

```mw
void *memchr(const void *s, int c, size_t n);
```

The `memchr()` function shall locate the first occurrence of `c` (converted to an `unsigned char`) in the initial `n` bytes (each interpreted as `unsigned char`) of the object pointed to by `s`. If `c` is not found, `memchr` returns a null pointer.

The following is a public-domain implementation of `memchr`:

```mw
#include <string.h>
/* memchr */
void *(memchr)(const void *s, int c, size_t n)
{
    const unsigned char *src = s;
    unsigned char uc = c;
    while (n-- != 0) {
        if (*src == uc)
            return (void *) src;
        src++;
    }
    return NULL;
}
```

##### The `strcspn`, `strpbrk`, and `strspn` functions

```mw
size_t strcspn(const char *s1, const char *s2);
```

```mw
char *strpbrk(const char *s1, const char *s2);
```

```mw
size_t strspn(const char *s1, const char *s2);
```

The `strcspn` function computes the length of the maximum initial segment of the string pointed to by `s1` which consists entirely of characters **not** from the string pointed to by `s2`.

The `strpbrk` function locates the first occurrence in the string pointed to by `s1` of any character from the string pointed to by `s2`, returning a pointer to that character or a null pointer if not found.

The `strspn` function computes the length of the maximum initial segment of the string pointed to by `s1` which consists entirely of characters from the string pointed to by `s2`.

All of these functions are similar except in the test and the return value.

The following are public-domain implementations of `strcspn`, `strpbrk`, and `strspn`:

```mw
#include <string.h>
/* strcspn */
size_t (strcspn)(const char *s1, const char *s2)
{
    const char *sc1;
    for (sc1 = s1; *sc1 != '\0'; sc1++)
        if (strchr(s2, *sc1) != NULL)
            return (sc1 - s1);
    return sc1 - s1;            /* terminating nulls match */
}
```

```mw
#include <string.h>
/* strpbrk */
char *(strpbrk)(const char *s1, const char *s2)
{
    const char *sc1;
    for (sc1 = s1; *sc1 != '\0'; sc1++)
        if (strchr(s2, *sc1) != NULL)
            return (char *)sc1;
    return NULL;                /* terminating nulls match */
}
```

```mw
#include <string.h>
/* strspn */
size_t (strspn)(const char *s1, const char *s2)
{
    const char *sc1;
    for (sc1 = s1; *sc1 != '\0'; sc1++)
        if (strchr(s2, *sc1) == NULL)
            return (sc1 - s1);
    return sc1 - s1;            /* terminating nulls don't match */
}
```

##### The `strstr` function

```mw
char *strstr(const char *haystack, const char *needle);
```

The `strstr()` function shall locate the first occurrence in the string pointed to by `haystack` of the sequence of bytes (excluding the terminating null byte) in the string pointed to by `needle`. The function returns the pointer to the matching string in `haystack` or a null pointer if a match is not found. If `needle` is an empty string, the function returns `haystack`.

The following is a public-domain implementation of `strstr`:

```mw
#include <string.h>
/* strstr */
char *(strstr)(const char *haystack, const char *needle)
{
    size_t needlelen;
    /* Check for the null needle case.  */
    if (*needle == '\0')
        return (char *) haystack;
    needlelen = strlen(needle);
    for (; (haystack = strchr(haystack, *needle)) != NULL; haystack++)
        if (memcmp(haystack, needle, needlelen) == 0)
            return (char *) haystack;
    return NULL;
}
```

##### The `strtok` function

```mw
char *strtok(char *restrict s1, const char *restrict delimiters);
```

A sequence of calls to `strtok()` breaks the string pointed to by `s1` into a sequence of tokens, each of which is delimited by a byte from the string pointed to by `delimiters`. The first call in the sequence has `s1` as its first argument, and is followed by calls with a null pointer as their first argument. The separator string pointed to by `delimiters` may be different from call to call.

The first call in the sequence searches the string pointed to by `s1` for the first byte that is not contained in the current separator string pointed to by `delimiters`. If no such byte is found, then there are no tokens in the string pointed to by `s1` and `strtok()` shall return a null pointer. If such a byte is found, it is the start of the first token.

The `strtok()` function then searches from there for a byte (or multiple, consecutive bytes) that is contained in the current separator string. If no such byte is found, the current token extends to the end of the string pointed to by `s1`, and subsequent searches for a token shall return a null pointer. If such a byte is found, it is overwritten by a null byte, which terminates the current token. The `strtok()` function saves a pointer to the following byte, from which the next search for a token shall start.

Each subsequent call, with a null pointer as the value of the first argument, starts searching from the saved pointer and behaves as described above.

The `strtok()` function need not be reentrant. A function that is not required to be reentrant is not required to be thread-safe.

Because the `strtok()` function must save state between calls, and you could not have two tokenizers going at the same time, the Single Unix Standard defined a similar function, `strtok_r()`, that does not need to save state. Its prototype is this:

`char *strtok_r(char *s, const char *delimiters, char **lasts);`

The `strtok_r()` function considers the null-terminated string `s` as a sequence of zero or more text tokens separated by spans of one or more characters from the separator string `delimiters`. The argument lasts points to a user-provided pointer which points to stored information necessary for `strtok_r()` to continue scanning the same string.

In the first call to `strtok_r()`, `s` points to a null-terminated string, `delimiters` to a null-terminated string of separator characters, and the value pointed to by `lasts` is ignored. The `strtok_r()` function shall return a pointer to the first character of the first token, write a null character into `s` immediately following the returned token, and update the pointer to which `lasts` points.

In subsequent calls, `s` is a null pointer and `lasts` shall be unchanged from the previous call so that subsequent calls shall move through the string `s`, returning successive tokens until no tokens remain. The separator string `delimiters` may be different from call to call. When no token remains in `s`, a NULL pointer shall be returned.

The following public-domain code for `strtok` and `strtok_r` codes the former as a special case of the latter:

```mw
#include <string.h>
/* strtok_r */
char *(strtok_r)(char *s, const char *delimiters, char **lasts)
{
    char *sbegin, *send;
    sbegin = s ? s : *lasts;
    sbegin += strspn(sbegin, delimiters);
    if (*sbegin == '\0') {
        *lasts = "";
        return NULL;
    }
    send = sbegin + strcspn(sbegin, delimiters);
    if (*send != '\0')
        *send++ = '\0';
    *lasts = send;
    return sbegin;
}
/* strtok */
char *(strtok)(char *restrict s1, const char *restrict delimiters)
{
    static char *ssave = "";
    return strtok_r(s1, delimiters, &ssave);
}
```

#### Miscellaneous functions

These functions do not fit into one of the above categories.

##### The `memset` function

```mw
void *memset(void *s, int c, size_t n);
```

The `memset()` function converts `c` into `unsigned char`, then stores the character into the first `n` bytes of memory pointed to by `s`.

The following is a public-domain implementation of `memset`:

```mw
#include <string.h>
/* memset */
void *(memset)(void *s, int c, size_t n)
{
    unsigned char *us = s;
    unsigned char uc = c;
    while (n-- != 0)
        *us++ = uc;
    return s;
}
```

##### The `strerror` function

```mw
char *strerror(int errorcode);
```

This function returns a locale-specific error message corresponding to the parameter. Depending on the circumstances, this function could be trivial to implement, but this author will not do that as it varies.

The Single Unix System Version 3 has a variant, `strerror_r`, with this prototype:

`int strerror_r(int errcode, char *buf, size_t buflen);`

This function stores the message in `buf`, which has a length of size `buflen`.

## Examples

To determine the number of characters in a string, the `strlen()` function is used:

```mw
#include <stdio.h>
#include <string.h>
...
int length, length2;
char *turkey;
static char *flower= "begonia";
static char *gemstone="ruby ";

length = strlen(flower);
printf("Length = %d\n", length); // prints 'Length = 7'
length2 = strlen(gemstone);

turkey = malloc( length + length2 + 1);
if (turkey) {
    strcpy( turkey, gemstone);
    strcat( turkey, flower);
    printf( "%s\n", turkey); // prints 'ruby begonia'
    free( turkey );
}
```

Note that the amount of memory allocated for 'turkey' is one plus the sum of the lengths of the strings to be concatenated. This is for the terminating null character, which is not counted in the lengths of the strings.

### Exercises

1. The string functions use a lot of looping constructs. Is there some way to portably unravel the loops?
2. What functions are possibly missing from the library as it stands now?
