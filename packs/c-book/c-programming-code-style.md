---
title: "C Programming/Code style"
source: https://en.wikibooks.org/wiki/C_Programming/Code_style
domain: c-book
license: CC-BY-SA-4.0 (Wikibooks C Programming)
tags: c pointers, c arrays, c memory management, c strings
fetched: 2026-07-02
---

# C Programming/Code style

<

C Programming

This is a basic introduction to good coding style in the C Programming Language. It is designed to provide information on how to effectively use indentation, comments, and other elements that will make your C code more readable. It is not a tutorial on actual C programming.

As a beginning programmer, the point of creating structure in the program code might not be clear, as the compiler doesn't care about the difference. However, as programs become complex, chances are that writing the program has become a joint effort. (Or others might want to see how it was accomplished. Or you may have to read it again years later.) Well-written code also helps you get an overview of what the code does.

In the following sections, we will attempt to explain good programming practices that will in turn make your programs clearer.

## Introduction

In C, programs are composed of statements. Statements are terminated with a semi-colon, and are collected in sections known as functions. By convention, a statement should be kept on its own line, as shown in the example below:

```mw
#include <stdio.h>
 
int main(void) {
	printf("Hello, World!\n");
	return 0;
}
```

The following block of code is essentially the same. While it contains exactly the same code, and will compile and execute with the same result, the removal of spacing causes an essential difference: it's harder to read.

```mw
#include <stdio.h>
int main(void) {printf("Hello, World!\n");return 0;}
```

The simple use of indents and line breaks can greatly improve code readability without impacting code performance. Readable code makes it much easier to see where functions and procedures end and which lines are part of which loops and procedures.

This lesson is going to focus on improving the coding style of an example piece of code which applies a formula and prints the result. Later, you'll see how to write code for such tasks in more detail. For now, focus on how the code looks, not what it does.

## Line breaks and indentation

The addition of white space inside your code is arguably the most important part of good code structure. Effective use of white space can create a visual scale of how your code flows, which can be very important when returning to your code when you want to maintain it.

### Line breaks

With minimal line breaks, code is barely human-readable, and may be hard to debug or understand:

```mw
#include <stdio.h>
int main(void) { int revenue = 80; int cost = 50; int roi; roi = (100 * (revenue - cost)) / cost; if (roi >= 0) { printf ("%d\n", roi); } return 0; }
```

Rather than putting everything on one line, it is much more readable to break up long lines so that each statement and declaration goes on its own line. After inserting line breaks, the code will look like this:

```mw
#include <stdio.h>
int main(void) {
int revenue = 80;
int cost = 50;
int roi;
roi = (100 * (revenue - cost)) / cost;
if (roi >= 0) {
printf ("%d\n", roi);
}
return 0;
}
```

### Blank lines

Blank lines should be used to offset the main components of your code. Always use them:

- After preprocessor directives.
- After new variables are declared.
- Use your own judgment for finding other places where components should be separated.

Based on these two rules, there should now be at least two line breaks added:

- After line 1, because line 1 has a preprocessor directive.
- After line 5, because line 5 contains a variable declaration.

This will make the code much more readable than it was before:

The following lines of code have line breaks between functions, but without indentation.

```mw
#include <stdio.h>

int main(void) {

int revenue = 80;
int cost = 50;
int roi;

roi = (100 * (revenue - cost)) / cost;

if (roi >= 0) {
printf ("%d\n", roi);
}

return 0;
}
```

But it's still not as readable as it can be.

### Indentation

Many text editors automatically indent appropriately when you hit the enter/return key.

Although adding simple line breaks between key blocks of code can make code easier to read, it provides no information about the block structure of the program. Using the tab key can be very helpful. Indentation visually separates paths of execution by moving their starting points to a new column. This simple practice will make it much easier to read and understand code. Indentation follows a fairly simple rule:

- All code inside a new block should be indented by one tab more than the code in the previous path.

Based on the code from the previous section, there are two blocks requiring indentation:

- Lines 4 to 16
- Line 13

```mw
#include <stdio.h>

int main(void) {

    int revenue = 80;
    int cost = 50;

    int roi;

    roi = (100 * (revenue - cost)) / cost;

    if (roi >= 0) {
        printf ("%d\n", roi);
    }

    return 0;
}
```

It is now fairly obvious as to which parts of the program fit inside which blocks. You can tell which parts of the program the coder has intended to be conditional, and which ones he or she has not. Although it might not be immediately noticeable, once many nested paths get added to the structure of the program, the use of indentation can be very important. Thus, indentation makes the structure of your program clear.

It is claimed that research has shown that an indentation size between 2 to 4 characters is easier to read than 8 character indents. However, an indent of 8 characters may still be in use for some systems.

This section is going to focus on the various uses of each form of commentary.

Single-line comments are most useful for simple 'side' notes that explain what certain parts of the code do. The best places to put these comments are next to variable declarations, and next to pieces of code that may need explanation. Comments should make clear the intention and ideas behind the corresponding code. What is immediately obvious from reading the code does not belong in a comment.

Based on our previous program, there are various good places to place comments:

- Line 5 and/or 6, to explain what 'int revenue' and 'int cost' represent,
- Line 8, to explain what the variable 'roi' is going to be used for,
- Line 10, to explain the idea of the calculation,
- Line 12, to explain the purpose of the 'if'.

This will make our program look something like:

```mw
#include <stdio.h>

int main(void) {

    int revenue = 80;               // as of 2016
    int cost = 50;

    int roi;                        // return on investment in percent

    roi = (100 * (revenue - cost)) / cost;  // formula from accounting book

    if (roi >= 0) {                 // we don't care about negative roi
        printf ("%d\n", roi);
    }

    return 0;
}
```

Multi-line comments are most useful for long explanations of code. They can be used as copyright/licensing notices, and they can also be used to explain the purpose of a block of code. This can be useful for two reasons: They make your functions easier to understand, and they make it easier to spot errors in code. If you know what a block is *supposed* to do, then it is much easier to find the piece of code that is responsible if an error occurs.

As an example, suppose we had a program that was designed to print "Hello, World! " a certain number of lines, a specified number of times. There would be many for loops in this program. For this example, we shall call the number of lines *i*, and the number of strings per line as *j*.

A good example of a multi-line comment that describes 'for' loop *i'*s purpose would be:

```mw
 /* For Loop (int i)
    Loops the following procedure i times (for number of lines).  Performs 'for' loop j on each loop,
    and prints a new line at end of each loop.
 */
```

This provides a good explanation of what *i'*s purpose is, whilst not going into detail of what *j* does. By going into detail over what the specific path does (and not ones inside it), it will be easier to troubleshoot the path.

Similarly, you should always include a multi-line comment before each function, to explain the role, preconditions and postconditions of each function. Always leave the technical details to the individual blocks inside your program - this makes it easier to troubleshoot.

A function descriptor should look something like:

```mw
 /* Function : int hworld (int i,int j)
    Input    : int i (Number of lines), int j (Number of instances per line)
    Output   : 0 (on success)
    Procedure: Prints "Hello, World!" j times, and a new line to standard output over i lines.
 */
```

This system allows for an at-a-glance explanation of what the function should do. You can then go into detail over how each aspect of the program is achieved later on in the program.

Applied to our original program, we can now include a much more descriptive and readable source code:

```mw
#include <stdio.h>

int main(void) {
    /*
     * Function: int main(void)
     * Input   : none
     * Output  : Returns 0 on success
     * Procedure: Prints 2016's return on investment in percent if it is not negative.
     */
    int revenue = 80;               // as of 2016
    int cost = 50;

    int roi;                        // return on investment in percent

    roi = (100 * (revenue - cost)) / cost;  // formula from accounting book

    if (roi >= 0) {                 // we don't care about negative roi
        printf ("%d\n", roi);
    }

    return 0;
}
```

This will allow any outside users of the program an easy way to comprehend what the code functions are and how they operate. It also inhibits uncertainty with other like-named functions.

Comments written in source files can be used for documenting source code automatically by using popular tools like Doxygen.
