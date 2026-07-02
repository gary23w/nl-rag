---
title: "Indentation style"
source: https://en.wikipedia.org/wiki/Indentation_style
domain: editorconfig
license: CC-BY-SA-4.0
tags: editorconfig, editor coding style config, indentation style config, cross-editor formatting
fetched: 2026-07-02
---

# Indentation style

In computer programming, **indentation style** is a convention or style, governing the indentation of lines of source code. An indentation style generally specifies a consistent number of whitespace characters before each line of a block, so that the lines of code appear to be related, and dictates whether to use spaces or tabs as the indentation character.

## Overview

This article primarily addresses styles for free-form programming languages. As the name implies, such language code need not follow an indentation style. Indentation is a secondary notation that is often intended to lower cognitive load for a programmer to understand the structure of the code. Indentation can clarify the separation between the code executed based on control flow.

Structured languages, such as Python and occam, use indentation to determine the structure instead of using braces or keywords; this is termed the off-side rule. In such languages, indentation is meaningful to the language processor (such as compiler or interpreter). A programmer must conform to the language's indentation rules although may be free to choose indentation size.

This article focuses on curly-bracket languages (that delimit blocks with curly brackets, a.k.a. curly braces, a.k.a. braces) and in particular C-family languages, but a convention used for one language can be adapted to another language. For example, a language that uses `BEGIN` and `END` keywords instead of braces can be adapted by treating `BEGIN` the same as the open brace and so on.

Indentation style only applies to text-based languages. Visual programming languages generally do not use indentation in the same way.

## Research

Despite the ubiquitous use of indentation styles, little research has been conducted on its value. First experiments, conducted by Weissman in 1974, did not show any effect. In 2023, an experiment by Morzeck et al. showed a significant positive effect for nested `if` statements where non-indented code required on average 179% more time to read than indented code. A follow up-experiment by Hanenberg et al. confirmed a large effect (although in that experiment non-indented code just took 113% more time to read) and revealed that the differences in reading times can be explained by the code that can be skipped (for indented code). In another experiment on JSON objects non-indented code took even 544% more time to read.

## Brace placement styles

The table below illustrates how different brace placement styles interact with indentation in control structures. For consistency, indentation size for example code is 4 spaces even though this varies by coding convention.

| Example | Name |
|---|---|
| while (x == y) { foo(); bar(); } | Allman |
| while (x == y) { foo(); bar(); } | GNU |
| while (x == y) { foo(); bar(); } | Whitesmiths |
| while (x == y) { foo(); bar(); } | K&R |
| while (x == y) { foo(); bar(); } | Ratliff |
| while (x == y) { foo(); bar(); } | Horstmann |
| while (x == y) { foo(); bar(); } | Pico |
| while (x == y) { foo(); bar(); } | Lisp |
| #define W(c,b) {while(c){b}} W(x==y,f();b();) | APL |

## C/C++ styles

Attributes of C, C++ and other curly-brace programming language coding style include but are not limited to:

- Placement of braces relative to other code elements
- Use of tabs or spaces
- Wrapping single-statement blocks in braces. Advocates cite the advantage that resulting code is safer since inserting a statement cannot result in control flow that disagrees with indentation. A cited disadvantage is that the code is longer since one line is needed for the closing brace of a block (except for the `else if` construct and a `do{}while` block).

### K&R

The Kernighan & Ritchie (K&R) style is commonly used for C and C++ code and is the basis for many derivative styles. It is used in the original Unix kernel, Kernighan and Ritchie's book *The C Programming Language*, as well as Kernighan and Plauger's book *The Elements of Programming Style*.

Although *The C Programming Language* does not explicitly define this style, it follows it consistently. From the book:

> The position of braces is less important, although people hold passionate beliefs. We have chosen one of several popular styles. Pick a style that suits you, then use it consistently.

In this style, a function has its opening and closing braces on their own lines and with the same indentation as the declaration, while the statements in the body of the function are indented an additional level. A multi-statement block inside a function, however, has its opening brace on the same line as its control clause while the closing brace remains on its own line unless followed by a keyword such as `else` or `while`.

Example code:

```mw
int main(int argc, char *argv[])
{
    while (x == y) {
        do_something();
        do_something_else();
        if (some_error)
            fix_issue(); // single-statement block without braces
        else
            continue_as_usual();
    }
    final_thing();
}
```

#### Egyptian braces

The non-aligned braces of the multi-line blocks are nicknamed "Egyptian braces" (or "Egyptian brackets") for their resemblance to arms in some fanciful poses of ancient Egyptians.

#### Single statements

A single-statement block does not have braces, which is a cause of easy-to-miss bugs such as the goto fail bug.

### One True Brace

The *One True Brace Style* (abbreviated 1TBS or OTBS) is a variant of K&R style where braces are *not* omitted for a single-statement block.

```mw
bool is_negative(int x)
{
    if (x < 0) {
        return true;
    } else {
        return false;
    }
}
```

Although not required by languages such as C/C++, using braces for single-statement blocks ensures inserting a new statement does not result in control flow that disagrees with indenting, as seen for example in Apple's infamous goto fail bug.

Some sources disagree as to the meaning of One True Brace Style – it might have slight differences based on most prevalent style for given language, individual authors might declare vastly distinct style as OTBS according to their subjective preferences, while others note it as "hacker jargon" for K&R.

### Linux kernel

The Linux kernel source tree is styled in a variant of K&R. Linus Torvalds advises contributors to follow it. Attributes include:

- Uses tab characters for indentation (not spaces) and assumes tab stops every 8 spaces
- Brace layout matches K&R, with the braces of function definitions on their own lines and the opening brace of compound statements on the same line as the control clause, separated by a space
- Labels in a `switch` statement are aligned with the enclosing block (there is only one level of indents)
- Maximum line length is 100 characters although the pre-2020 limit of 80 characters is preferred.
- A single-statement body of a compound statement (such as if, while, and do-while) does not need to be surrounded by curly braces. If, however, one or more of the substatements in an `if-else` statement require braces, then both substatements should be wrapped in braces:

```mw
int power(int x, int y)
{
        int result;

        if (y < 0) {
                result = 0;
        } else {
                result = 1;
                while (y-- > 0)
                        result *= x;
        }
        return result;
}
```

### Java

A significant body of Java code uses a variant of the K&R style in which the opening brace is on the same line not only for the blocks inside a function, but also for class or method declarations. This style is widespread largely because Sun Microsystems's original style guides used this K&R variant, and as a result, most of the standard source code for the Java API is written in this style. It is also a popular indentation style for ActionScript and JavaScript, along with the Allman style.

### Stroustrup

Bjarne Stroustrup adapted the K&R style for C++ in his books, such as *Programming: Principles and Practice using C++* and *The C++ Programming Language*.

Unlike the variants above, Stroustrup does not use a "cuddled else". Thus, Stroustrup would write

```mw
if (x < 0) {
    puts("Negative");
    negative(x);
}
else {
    puts("Non-negative");
    nonnegative(x);
}
```

Stroustrup extends K&R style for classes, writing them as follows:

```mw
class DoubleVec {
public:
    // construct a DoubleVec
    DoubleVec(int s) :elem(new double[s]), sz(s) { }
    // element access: subscripting
    double& operator[](int i) { return elem[i]; }
    int size() { return sz; }
private:
    // pointer to the elements
    double* elem;
    // number of elements
    int sz;
};
```

Stroustrup does not indent the labels `public:` and `private:`. Also, in this style, while the opening brace of a function starts on a new line, the opening brace of a class is on the same line as the class name.

Stroustrup allows writing short functions all on one line. Stroustrup style is a named indentation style available in the editor Emacs. Stroustrup encourages a K&R-derived style layout with C++ as stated in his modern *C++ Core Guidelines*.

### BSD KNF

The Berkeley Software Distribution (BSD) operating systems uses a style that is sometimes termed "kernel normal form" (KNF). Although mostly intended for kernel code, it is also widely used in userland code. It is essentially a thoroughly documented variant of K&R style as used in the Bell Labs version 6 & 7 Unix source code.

The SunOS kernel and userland uses a similar indentation style. Like KNF, this also was based on AT&T style documents and is sometimes termed Bill Joy Normal Form. The SunOS guideline was published in 1996; ANSI C is discussed briefly. The correctness of the indentation of a list of source files can be verified by the *cstyle* program written by Bill Shannon.

In this style, the hard tabulator (ts in vi) is kept at eight columns, while a soft tabulator is often defined as a helper also (sw in vi), and set at four. The hard tabulators are used to indent code blocks, while a soft tabulator (four spaces) of additional indentation is used for all continuing lines that must be split over multiple lines.

Moreover, function calls do not use a space before the parenthesis, although C-language native statements such as `if`, `while`, `do`, `switch` and `return` do (in the case where `return` is used with parens). Functions that declare no local variables in their top-level block should also leave an empty line after their opening block brace.

Examples:

```mw
while (x == y) {
        something();
        something_else();
}
final_thing();
```

```mw
if (data != NULL && res > 0) {
        if (JS_DefineProperty(cx, o, "data",
            STRING_TO_JSVAL(JS_NewStringCopyN(cx, data, res)),
            NULL, NULL, JSPROP_ENUMERATE) != 0) {
                QUEUE_EXCEPTION("Internal error!");
                goto err;
        }
        PQfreemem(data);
} else {
        if (JS_DefineProperty(cx, o, "data", OBJECT_TO_JSVAL(NULL),
            NULL, NULL, JSPROP_ENUMERATE) != 0) {
                QUEUE_EXCEPTION("Internal error!");
                goto err;
        }
}
```

```mw
static JSBool
pgresult_constructor(JSContext *cx, JSObject *obj, uintN argc,
    jsval *argv, jsval *rval)
{

        QUEUE_EXCEPTION("PGresult class not user-instantiable");

        return (JS_FALSE);
}
```

### Allman

The Allman style is named after Eric Allman. It is also sometimes termed *BSD style* since Allman wrote many of the utilities for BSD Unix (although this should not be confused with the different "BSD KNF style"; see above).

This style puts the brace associated with a control statement on the next line, indented to the same level as the control statement. Statements within the braces are indented to the next level.

```mw
while (x == y)
{
    something();
    something_else();
}

final_thing();
```

This style is similar to the standard indentation used by the Pascal languages and Transact-SQL, where the braces are equivalent to the keywords `begin` and `end`.

```mw
(* Example Allman code indentation style in Pascal *)
procedure dosomething(x, y: Integer);
begin
    while x = y do
    begin
        something();
        something_else();
    end;
end;
```

Consequences of this style are that the indented code is clearly set apart from the containing statement by lines that are almost all whitespace and the closing brace lines up in the same column as the opening brace. Some people feel this makes it easy to find matching braces. The blocking style also delineates the block of code from the associated control statement. Commenting out or removing a control statement or block of code, or code refactoring, are all less likely to introduce syntax errors via dangling or missing braces. Also, it is consistent with brace placement for the outer-function block.

For example, the following is still correct syntactically:

```mw
// while (x == y)
{
    something();
    something_else();
}
```

As is this:

```mw
// for (int i=0; i < x; i++)
// while (x == y)
if (x == y)
{
    something();
    something_else();
}
```

Even like this, with conditional compilation:

```mw
    int c;
#ifdef HAS_GETCH
    while ((c = getch()) != EOF)
#else
    while ((c = getchar()) != EOF)
#endif
    {
        do_something(c);
    }
```

#### Variant: Allman-8

Allman-8 uses the 8-space indentation tabs and 80-column limit of the Linux Kernel variant of K&R. The style purportedly helps improve readability on projectors. Also, the indentation size and column restriction help create a visual cue for identifying excessive nesting of code blocks. These advantages combine to help provide newer developers and learners implicit guidance to manage code complexity.

### Whitesmiths

The Whitesmiths style, also sometimes termed Wishart style, was originally used in the documentation for the first commercial C compiler, the Whitesmiths Compiler. It was also popular in the early days of Windows, since it was used in three influential Windows programming books, *Programmer's Guide to Windows* by Durant, Carlson & Yao, *Programming Windows* by Petzold, and *Windows 3.0 Power Programming Techniques* by Norton & Yao.

Whitesmiths, along with Allman, were claimed to have been the most common bracing styles in 1991 by the Jargon File, with roughly equal popularity at the time.

This style puts the brace associated with a control statement on the next line, indented. Statements within the braces are indented to the same level as the braces.

Like Ratliff style, the closing brace is indented the same as statements within the braces.

```mw
while (x == y)
    {
    something();
    something_else();
    }

final_thing();
```

The advantages of this style are similar to those of the Allman style. Blocks are clearly set apart from control statements. The alignment of the braces with the block emphasizes that the full block is conceptually, and programmatically, one compound statement. Indenting the braces emphasizes that they are subordinate to the control statement. The ending brace no longer lines up with the statement, but instead with the opening brace.

An example:

```mw
if (data != NULL && res > 0)
    {
    if (!JS_DefineProperty(cx, o, "data", STRING_TO_JSVAL(JS_NewStringCopyN(cx, data, res)), NULL, NULL, JSPROP_ENUMERATE))
        {
        QUEUE_EXCEPTION("Internal error!");
        goto err;
        }
    PQfreemem(data);
    }
else if (!JS_DefineProperty(cx, o, "data", OBJECT_TO_JSVAL(NULL), NULL, NULL, JSPROP_ENUMERATE))
    {
    QUEUE_EXCEPTION("Internal error!");
    goto err;
    }
```

`else if` are treated as statement, much like the `#elif` preprocessor statement.

### GNU

Like the Allman and Whitesmiths styles, GNU style puts braces on a line by themselves, indented by two spaces, except when opening a function definition, where they are not indented. In either case, the contained code is indented by two spaces from the braces.

Popularised by Richard Stallman, the layout may be influenced by his background of writing Lisp code. In Lisp, the equivalent to a block (a progn) is a first-class data entity, and giving it its own indentation level helps to emphasize that, whereas in C, a block is only syntax. This style can also be found in some ALGOL and XPL programming language textbooks from the 1960s and 1970s.

Although not indentation per se, GNU coding style also includes a space after a function name – before the left parenthesis of an argument list.

```mw
static char *
concat (char *s1, char *s2)
{
  while (x == y)
    {
      something ();
      something_else ();
    }
  final_thing ();
}
```

This style combines the advantages of Allman and Whitesmiths, thereby removing the possible Whitesmiths disadvantage of braces not standing out from the block. One disadvantage is that the ending brace no longer lines up with the statement it conceptually belongs to. Another possible disadvantage is that it might waste space by using two visual levels of indents for one conceptual level, but in reality this is unlikely because, in systems with single-level indentation, each level is usually at least 4 spaces, same as 2 * 2 spaces in GNU style.

The GNU Coding Standards recommend this style, and nearly all maintainers of GNU project software use it.

The GNU Emacs text editor and the GNU systems' indent command will reformat code according to this style by default. Those who do not use GNU Emacs, or similarly extensible/customisable editors, may find that the automatic indentation settings of their editor are unhelpful for this style. However, many editors defaulting to KNF style cope well with the GNU style when the tab width is set to two spaces; likewise, GNU Emacs adapts well to KNF style by simply setting the tab width to eight spaces. In both cases, automatic reformatting destroys the original spacing, but automatic line indenting will work properly.

Steve McConnell, in his book Code Complete, advises against using this style: he marks a code sample which uses it with a "Coding Horror" icon, symbolizing especially dangerous code, and states that it impedes readability. The Linux kernel coding style documentation also recommends against this style, urging readers to burn a copy of the GNU coding standards as a "great symbolic gesture".

### Horstmann

The 1997 edition of *Computing Concepts with C++ Essentials* by Cay S. Horstmann adapts Allman by placing the first statement of a block on the same line as the opening brace. This style is also used in examples in Jensen and Wirth's *Pascal User Manual and Report*.

```mw
while (x == y)
{   something();
    something_else();
    //...
    if (x < 0)
    {   printf("Negative");
        negative(x);
    }
    else
    {   printf("Non-negative");
        nonnegative(x);
    }
}
final_thing();
```

This style combines the advantages of Allman by keeping the vertical alignment of the braces for readability, and identifying blocks easily, with the saving of a line of the K&R style. However, the 2003 edition now uses Allman style throughout.

### Pico

This is the style used most commonly in the language Pico by its designers. Pico lacks return statements, and uses semicolons as statement separators instead of terminators. It yields this syntax:

```
stuff(n):
{ x: 3 * n;
  y: do_stuff(x);
  y + x }
```

The advantages and disadvantages are similar to those of saving screen real estate with K&R style. An added advantage is that the starting and closing braces are consistent in application (both share space with a line of code), relative to K&R style, where one brace shares space with a line of code and one brace has a line alone.

### Ratliff

In the book *Programmers at Work*, C. Wayne Ratliff, the original programmer behind the popular dBase-II and -III fourth-generation programming languages, discussed a style that is like 1TBS but the closing brace lines up with the indentation of the nested block. He indicated that the style was originally documented in material from Digital Research Inc. This style has sometimes been termed *banner* style, possibly for the resemblance to a banner hanging from a pole. In this style, which is to Whitesmiths as K&R is to Allman, the closing control is indented the same as the last item in the list (and thus properly loses salience) The style can make visual scanning easier for some, since the *headers* of any block are the only thing exdented at that level (the theory being that the closing control of the prior block interferes with the visual flow of the next block header in the K&R and Allman styles). Kernighan and Plauger use this style in the Ratfor code in *Software Tools*.

```mw
 // In C
 for (i = 0; i < 10; i++) {
     if (i % 2 == 0) {
         do_something(i);
         }
     else {
         do_something_else(i);
         }
     }
```

## Derived C language styles

The following styles may be considered to be "derived" C styles, in the sense that they derive significant influence from the indentation styles of other, non-C languages. They might be applied to C code written as part of a project *mostly* written in one of these other languages, where maintaining a consistent *look and feel* to the project's core code overrides considerations of using more conventional C style.

### Lisp style

While GNU style is sometimes characterized as C code indented by a Lisp programmer, one might even go so far as to insert closing braces together in the last line of a block. This style makes indentation the only way to distinguish blocks of code, but has the advantage of containing no uninformative lines. This could easily be called the Lisp style because this style is very common in Lisp code. In Lisp, the grouping of identical braces at the end of expression trees is meant to signify that it is not the user's job to visually track nesting levels, only to understand the structure of the tree.

The traditional Lisp variant of this style prefers extremely narrow levels of indentation (typically two spaces) because Lisp code usually nests very deeply since Lisp features only expressions, with no distinct class of statements; function arguments are mostly indented to the same level to illustrate their shared status within the enclosing expression. This is also because, braces aside, Lisp is conventionally a very terse language, omitting even common forms of simple boilerplate code as uninformative, such as the `else` keyword in an `if : then | else` block, instead rendering it uniformly as `(if expr1 expr2 expr3)`.

```mw
// C
for (i = 0; i < 10; i++)
    {if (i % 2 == 0)
        {do_something(i);}
     else
        {do_something_else(i);
         do_third_thing(i);}}
```

```mw
;; Lisp
(dotimes (i 10)
  (if (= (rem i 2) 0)
      (do-something i)
    (progn
      (do-something-else i)
      (do-third-thing i))))
```

Note: `progn` is a procedure for evaluating multiple sub-expressions sequentially for effects, while discarding all but the final (nth) return value. If all return values are desired, the `values` procedure would be used.

### Haskell style

Haskell layout can make the placement of braces optional, although braces and semicolons are allowed in the language. The two segments below are equally acceptable to the compiler:

```mw
braceless = do
  text <- getContents
  let
    firstWord = head $ words text
    bigWord = map toUpper firstWord
  putStrLn bigWord

braceful = do
  { text <- getContents
  ; let
      { firstWord = head $ words text
      ; bigWord = map toUpper firstWord
      }
  ; putStrLn bigWord
  }
```

In Haskell, layout can replace braces. Usually the braces and semicolons are omitted for procedural `do` sections and the program text in general, but the style is commonly used for lists, records and other syntactic elements made up of some pair of parentheses or braces, which are separated with commas or semicolons. If code following the keywords `where`, `let`, or `of` omits braces and semicolons, then indentation is significant.

### APL style

For an example of how terse APL typically is, here is the implementation of the step function for Conway's Game of Life:

```mw
life←{⊃1⍵∨.∧3 4=+/+⌿¯1 0 1∘.⊖¯1 0 1⌽¨⊂⍵}
```

APL style C resembles the terse style of APL code, and is commonly used in their implementations. This style was pioneered by Arthur Whitney, and is heavily used in the implementation of K, Arthur's own project. The J programming language is implemented in this style as well. Notably, not all implementations of APL use this style of C, namely: GNU APL and Dyalog APL.

In addition to APL style C indentation, typically the names are shortened to either single or double characters: To reduce the amount of indentation, and expressions spanning multiple lines.

## Indentation size

Typically, programmers use the same width of whitespace to indent each block of code with commonly used widths varying from 1 to 4 spaces.

An experiment performed on PASCAL code in 1983, found that indentation size significantly affected comprehensibility. Indentation sizes between 2 and 4 characters proved optimal.

Although they both affect the general layout of code, indentation *size* is independent of the indentation *style* discussed here.

### Tab vs. space

Typically, a programmer uses a text editor that provides tab stops at fixed intervals (a number of spaces), to assist in maintaining whitespace according to a style. The interval is called the *tab width*. Sometimes the programmer stores the code with tab characters – one for each tab key press or they store a sequence of spaces equal in number to the tab width.

Storing tab characters in code can cause visual misalignment when viewed in different contexts, which counters the value of the indentation style.

Programmers lack consensus on storing tab characters. Proponents of storing tab characters cite ease of typing and smaller text files since a single tab character serves the purpose of multiple spaces. Opponents, such as Jamie Zawinski, state that using spaces instead increases cross-platform portability. Others, such as the writers of the WordPress coding standards, state the opposite: that hard tabs increase portability. A survey of the top 400,000 repositories on GitHub found that spaces are more common.

Many text editors, including Notepad++, TextEdit, Emacs, vi, and nano, can be configured to either store tab characters when entered via the tab key or to convert them to spaces (based on the configured tab width) so that tab characters are not added to the file when the tab key is pressed. Some editors can convert tab to space characters and vice versa.

Some text file pagers, such as less, can be configured for a tab width. Some tools such as expand/unexpand can convert on the fly via filters.

## Style automation

A tool can automate formatting code per an indentation style, for example the Unix `indent` command.

Emacs provides commands to modify indentation, including hitting `Tab` on a given line. `M-x indent-region` indents code.

Elastic tabstops is a tabulation style which requires support from the text editor, where entire blocks of text are kept automatically aligned when the length of one line in the block changes.

## Losing track of blocks

In more complicated code, the programmer may lose track of block boundaries while reading the code. This is often experienced in large sections of code containing many compound statements nested to many levels of indentation. As the programmer scrolls to the bottom of a huge set of nested statements, they may lose track of context – such as the control structure at the top of the block.

Long compound statements can be a code smell of over complexity which can be solved by refactoring.

Programmers who rely on counting the opening braces may have difficulty with indentation styles such as K&R, where the starting brace is not visually separated from its control statement. Programmers who rely more on indentations will gain more from styles that are vertically compact, such as K&R, because the blocks are shorter.

To avoid losing track of control statements such as `for`, a large indentation can be used, such as an 8-unit-wide hard tab, along with breaking up large functions into smaller and more readable functions. Linux is done this way, while using the K&R style.

Some text editors allow the programmer to jump between the two corresponding braces of a block. For example, vi jumps to the brace enclosing the same block as the one under the cursor when pressing the `%` key. Since the text cursor's `next` key (viz., the `n` key) retained directional positioning information (whether the `up` or `down` key was formerly pressed), the dot macro (the `.` key) could then be used to place the text cursor on the next brace, given a suitable coding style. Instead, inspecting the block boundaries using the `%` key can be used to enforce a coding standard.

Another way to maintain block awareness is to use comments after the closing brace. For example:

```mw
for (int i = 0; i < total; i++) {
    foo();
} //for (i)
```

```mw
if (x < 0) {
   bar();
} //if (x < 0)
```

A disadvantage is maintaining the same code in multiple locations – above and below the block.

Some editors provide support for maintaining block awareness. A folding editor can hide (fold) and reveal (unfold) blocks by indentation level. Some editors highlight matching braces when the cursor is positioned next to one.
