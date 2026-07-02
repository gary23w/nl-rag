---
title: "C Programming/Program flow control"
source: https://en.wikibooks.org/wiki/C_Programming/Program_flow_control
domain: c-book
license: CC-BY-SA-4.0 (Wikibooks C Programming)
tags: c pointers, c arrays, c memory management, c strings
fetched: 2026-07-02
---

# C Programming/Program flow control

<

C Programming

Very few programs follow exactly one control path and have each instruction stated explicitly. In order to program effectively, it is necessary to understand how one can alter the steps taken by a program due to user input or other conditions, how some steps can be executed many times with few lines of code, and how programs can appear to demonstrate a rudimentary grasp of logic. C constructs known as conditionals and loops grant this power.

From this point forward, it is necessary to understand what is usually meant by the word *block*. A block is a group of code statements that are associated and intended to be executed as a unit. In C, the beginning of a block of code is denoted with { (left curly), and the end of a block is denoted with }. It is not necessary to place a semicolon after the end of a block. Blocks can be empty, as in {}. Blocks can also be nested; i.e. there can be blocks of code within larger blocks.

## Conditionals

There is likely no meaningful program written in which a computer does not demonstrate basic decision-making skills. It can actually be argued that there is no meaningful human activity in which some sort of decision-making, instinctual or otherwise, does not take place. For example, when driving a car and approaching a traffic light, one does not think, "I will continue driving through the intersection." Rather, one thinks, "I will stop if the light is red, go if the light is green, and if yellow go only if I am traveling at a certain speed a certain distance from the intersection." These kinds of processes can be simulated in C using conditionals.

A conditional is a statement that instructs the computer to execute a certain block of code or alter certain data only if a specific condition has been met. The most common conditional is the If-Else statement, with conditional expressions and Switch-Case statements typically used as more shorthanded methods.

Before one can understand conditional statements, it is first necessary to understand how C expresses logical relations. C treats logic as being arithmetic. The value 0 (zero) represents false, and ***all other values*** represent true. If you chose some particular value to represent true and then compare values against it, sooner or later your code will fail when your assumed value (often 1) turns out to be incorrect. Code written by people uncomfortable with the C language can often be identified by the usage of #define to make a "TRUE" value.

Because logic is arithmetic in C, arithmetic operators and logical operators are one and the same. Nevertheless, there are a number of operators that are typically associated with logic:

### Relational and equivalence expressions

**a < b**

1 if

a

is less than

b

, 0 otherwise.

**a > b**

1 if

a

is greater than

b

, 0 otherwise.

**a <= b**

1 if

a

is less than or equal to

b

, 0 otherwise.

**a >= b**

1 if

a

is greater than or equal to

b

, 0 otherwise.

**a == b**

1 if

a

is equal to

b

, 0 otherwise.

**a != b**

1 if

a

is not equal to

b

, 0 otherwise

New programmers should take special note of the fact that the "equal to" operator is ==, not =. This is the cause of numerous coding mistakes and is often a difficult-to-find bug, as the expression `(a = b)` sets `a` equal to `b` and subsequently evaluates to `b`; but the expression `(a == b)`, which is usually intended, checks if `a` is equal to `b`. It needs to be pointed out that, if you confuse = with ==, your mistake will often not be brought to your attention by the compiler. A statement such as `if (c = 20) {}` is considered perfectly valid by the language, but will always assign 20 to `c` and evaluate as true. A simple technique to avoid this kind of bug (in many, not all cases) is to put the constant first. This will cause the compiler to issue an error, if == got misspelled with =.

Note that C does not have a dedicated boolean type as many other languages do. 0 means false and anything else true. So the following are equivalent:

```mw
 if (foo()) {
   // do something
 }
```

and

```mw
 if (foo() != 0) {
   // do something
 }
```

Often `#define TRUE 1` and `#define FALSE 0` are used to work around the lack of a boolean type. This is bad practice, since it makes assumptions that do not hold. It is a better idea to indicate what you are actually expecting as a result from a function call, as there are many different ways of indicating error conditions, depending on the situation.

```mw
 if (strstr("foo", bar) >= 0) {
   // bar contains "foo"
 }
```

Here, `strstr` returns the index where the substring foo is found and -1 if it was not found. Note: this would always fail with the `TRUE` definition mentioned in the previous paragraph. It would also not produce the expected results if we omitted the `>= 0`.

One other thing to note is that the relational expressions do not evaluate as they would in mathematical texts. That is, an expression `myMin < value < myMax` does not evaluate as you probably think it might. Mathematically, this would test whether or not *value* is between *myMin* and *myMax*. But in C, what happens is that *value* is first compared with *myMin*. This produces either a 0 or a 1. It is this value that is compared against myMax. Example:

```mw
 int value = 20;
 /* ... */
 if (0 < value < 10) { // don't do this! it always evaluates to "true"!
   /* do some stuff */
 }
```

Because *value* is greater than 0, the first comparison produces a value of 1. Now 1 is compared to be less than 10, which is true, so the statements in the if are executed. This probably is not what the programmer expected. The appropriate code would be:

```mw
 int value = 20;
 /* ... */
 if (0 < value && value < 10) {   // the && means "and"
   /* do some stuff */
 }
```

### Logical expressions

**a || b**

when EITHER

a

or

b

is true (or both), the result is 1, otherwise the result is 0.

**a && b**

when BOTH

a

and

b

are true, the result is 1, otherwise the result is 0.

**!a**

when

a

is true, the result is 0; when

a

is 0, the result is 1.

Here's an example of a larger logical expression. In the statement:

```mw
e = ((a && b) || (c > d));
```

e is set equal to 1 if a and b are non-zero, or if c is greater than d. In all other cases, e is set to 0.

C uses short circuit evaluation of logical expressions. That is to say, once it is able to determine the truth of a logical expression, it does no further evaluation. This is often useful as in the following:

```mw
int myArray[12];
...
if (i < 12 && myArray[i] > 3) { 
    ...
```

In the snippet of code, the comparison of i with 12 is done first. If it evaluates to 0 (false), **i** would be out of bounds as an index to **myArray**. In this case, the program never attempts to access **myArray[i]** since the truth of the expression is known to be false. Hence we need not worry here about trying to access an out-of-bounds array element if it is already known that i is greater than or equal to zero. A similar thing happens with expressions involving the or || operator.

```mw
while (doThis() || doThat())
    ...
```

doThat() is never called if doThis() returns a non-zero (true) value.

### The `if`–`else` statement

If-Else provides a way to instruct the computer to execute a block of code only if certain conditions have been met. The syntax of an If-Else construct is:

```mw
 if (/* condition goes here */) {
   /* if the condition is non-zero (true), this code will execute */
 } else {
   /* if the condition is 0 (false), this code will execute */
 }
```

The first block of code executes if the condition in parentheses directly after the *if* evaluates to non-zero (true); otherwise, the second block executes.

The *else* and following block of code are completely optional. If there is no need to execute code if a condition is not true, leave it out.

Also, keep in mind that an *if* can directly follow an *else* statement. While this can occasionally be useful, chaining more than two or three if-elses in this fashion is considered bad programming practice. We can get around this with the Switch-Case construct described later.

Two other general syntax notes need to be made that you will also see in other control constructs: First, note that there is no semicolon after *if* or *else*. There could be, but the block (code enclosed in { and }) takes the place of that. Second, if you only intend to execute one statement as a result of an *if* or *else*, curly braces are not needed. However, many programmers believe that inserting curly braces anyway in this case is good coding practice.

The following code sets a variable c equal to the greater of two variables a and b, or 0 if a and b are equal.

```mw
 if (a > b) {
   c = a;
 } else if (b > a) {
   c = b;
 } else {
   c = 0;
 }
```

Consider this question: why can't you just forget about *else* and write the code like:

```mw
 if (a > b) {
   c = a;
 }
 
 if (a < b) {
   c = b;
 }
 
 if (a == b) {
   c = 0;
 }
```

There are several answers to this. Most importantly, if your conditionals are not mutually exclusive, *two* cases could execute instead of only one. If the code was different and the value of a or b changes somehow (e.g.: you reset the lesser of a and b to 0 after the comparison) during one of the blocks? You could end up with multiple *if* statements being invoked, which is not your intent. Also, evaluating *if* conditionals takes processor time. If you use *else* to handle these situations, in the case above assuming (a > b) is non-zero (true), the program is spared the expense of evaluating additional *if* statements. The bottom line is that it is usually best to insert an *else* clause for all cases in which a conditional will not evaluate to non-zero (true).

#### The conditional expression

A conditional expression is a way to set values conditionally in a more shorthand fashion than If-Else. The syntax is:

```
(/* logical expression goes here */) ? (/* if non-zero (true) */) : (/* if 0 (false) */)
```

The logical expression is evaluated. If it is non-zero (true), the overall conditional expression evaluates to the expression placed between the ? and :, otherwise, it evaluates to the expression after the :. Therefore, the above example (changing its function slightly such that c is set to b when a and b are equal) becomes:

```
c = (a > b) ? a : b;
```

Conditional expressions can sometimes clarify the intent of the code. Nesting the conditional operator should usually be avoided. It's best to use conditional expressions only when the expressions for a and b are simple. Also, contrary to a common beginner belief, conditional expressions do not make for faster code. As tempting as it is to assume that fewer lines of code result in faster execution times, there is no such correlation.

### The `switch`–`case` statement

Say you write a program where the user inputs a number 1-5 (corresponding to student grades, A(represented as 1)-D(4) and F(5)), stores it in a variable **grade** and the program responds by printing to the screen the associated letter grade. If you implemented this using If-Else, your code would look something like this:

```mw
 if (grade == 1) {
   printf("A\n");
 } else if (grade == 2) {
   printf("B\n");
 } else if /* etc. etc. */
```

Having a long chain of if-else-if-else-if-else can be a pain, both for the programmer and anyone reading the code. Fortunately, there's a solution: the Switch-Case construct, of which the basic syntax is:

```mw
 switch (/* variable or other expression goes here */) {
 case /* potential value 1 */:
   /* code */
 case /* potential value 2 */:
   /* different code */
 /* insert additional cases as needed */
 default: 
   /* more code */
 }
```

The Switch-Case construct takes a variable, placed after *switch*, and compares it to the value following the *case* keyword. If the variable is equal to the value specified after *case*, the construct "activates", or begins executing the code after the case statement. Once the construct has "activated", there will be no further evaluation of *case*s.

Switch-Case is syntactically "weird" in that no braces are required for code associated with a *case*.

***Very important***: Typically, the last statement for each case is a break statement. This causes program execution to jump to the statement following the closing bracket of the switch statement, which is what one would normally want to happen. However if the break statement is omitted, program execution continues with the first line of the next case, if any. This is called a *fall-through*. When a programmer desires this action, a comment should be placed at the end of the block of statements indicating the desire to fall through. Otherwise another programmer maintaining the code could consider the omission of the 'break' to be an error, and inadvertently 'correct' the problem. Here's an example:

```mw
 switch (someVariable) {
 case 1:
   printf("This code handles case 1\n");
   break;
 case 2:
   printf("This prints when someVariable is 2, along with...\n");
   /* FALL THROUGH */
 case 3:
   printf("This prints when someVariable is either 2 or 3.\n" );
   break;
 }
```

If a *default* case is specified, the associated statements are executed if none of the other cases match. A *default* case is optional. Here's a switch statement that corresponds to the sequence of if - else if statements above.

Back to our example above. Here's what it would look like as Switch-Case:

```mw
 switch (grade) {
 case 1:
   printf("A\n");
   break;
 case 2:
   printf("B\n");
   break;
 case 3:
   printf("C\n");
   break;
 case 4:
   printf("D\n");
   break;
 default:
   printf("F\n");
   break;
 }
```

A set of statements to execute can be grouped with more than one value of the variable as in the following example. (the fall-through comment is not necessary here because the intended behavior is obvious)

```mw
 switch (something) {
 case 2:
 case 3:
 case 4:
   /* some statements to execute for 2, 3 or 4 */
   break;
 case 1:
 default:
   /* some statements to execute for 1 or other than 2,3,and 4 */
   break;
 }
```

## Loops

Often in computer programming, it is necessary to perform a certain action a certain number of times or until a certain condition is met. It is impractical and tedious to simply type a certain statement or group of statements a large number of times, not to mention that this approach is too inflexible and unintuitive to be counted on to stop when a certain event has happened. As a real-world analogy, someone asks a dishwasher at a restaurant what he did all night. He will respond, "I washed dishes all night long." He is not likely to respond, "I washed a dish, then washed a dish, then washed a dish, then...". The constructs that enable computers to perform certain repetitive tasks are called loops.

### `while` loops

A while loop is the most basic type of loop. It will run as long as the condition is non-zero (true). For example, if you try the following, the program will appear to lock up and you will have to manually close the program down. A situation where the conditions for exiting the loop will never become true is called an infinite loop.

```mw
 int a = 1;
 while (42) {
   a = a * 2;
 }
```

Here is another example of a while loop. It prints out all the powers of two less than 100.

```mw
 int a = 1;
 while (a < 100) {
   printf("a is %d \n", a);
   a = a * 2;
 }
```

The flow of all loops can also be controlled by **break** and **continue** statements. A break statement will immediately exit the enclosing loop. A continue statement will skip the remainder of the block and start at the controlling conditional statement again. For example:

```mw
 int a = 1;
 while (42) { // loops until the break statement in the loop is executed
   printf("a is %d ", a);
   a = a * 2;
   if (a > 100) {
     break;
   } else if (a == 64) {
     continue;  // Immediately restarts at while, skips next step
   }
   printf("a is not 64\n");
 }
```

In this example, the computer prints the value of a as usual, and prints a notice that a is not 64 (unless it was skipped by the continue statement).

Similar to If above, braces for the block of code associated with a While loop can be omitted if the code consists of only one statement, for example:

```mw
 int a = 1;
 while (a < 100)
   a = a * 2;
```

This will merely increase a until a is not less than 100.

When the computer reaches the end of the while loop, it always goes back to the while statement at the top of the loop, where it re-evaluates the controlling condition. If that condition is "true" at that instant -- even if it was temporarily 0 for a few statements inside the loop -- then the computer begins executing the statements inside the loop again; otherwise the computer exits the loop. The computer does not "continuously check" the controlling condition of a while loop during the execution of that loop. It only "peeks" at the controlling condition each time it reaches the `while` at the top of the loop.

It is very important to note, once the controlling condition of a While loop becomes 0 (false), the loop will not terminate until the block of code is finished and it is time to reevaluate the conditional. If you need to terminate a While loop immediately upon reaching a certain condition, consider using **break**.

A common idiom is to write:

```mw
 int i = 5;
 while (i--) {
   printf("java and c# can't do this\n");
 }
```

This executes the code in the while loop 5 times, with i having values that range from 4 down to 0 (inside the loop). Conveniently, these are the values needed to access every item of an array containing 5 elements.

### `for` loops

For loops generally look something like this:

```
for (initialization; test; increment) {
  /* code */
}
```

The *initialization* statement is executed exactly once - before the first evaluation of the *test* condition. Typically, it is used to assign an initial value to some variable, although this is not strictly necessary. The *initialization* statement can also be used to declare and initialize variables used in the loop.

The *test* expression is evaluated each time before the code in the *for* loop executes. If this expression evaluates as 0 (false) when it is checked (i.e. if the expression is not true), the loop is not (re)entered and execution continues normally at the code immediately following the FOR-loop. If the expression is non-zero (true), the code within the braces of the loop is executed.

After each iteration of the loop, the *increment* statement is executed. This often is used to increment the loop index for the loop, the variable initialized in the initialization expression and tested in the test expression. Following this statement execution, control returns to the top of the loop, where the *test* action occurs. If a *continue* statement is executed within the *for* loop, the increment statement would be the next one executed.

Each of these parts of the for statement is optional and may be omitted. Because of the free-form nature of the for statement, some fairly fancy things can be done with it. Often a for loop is used to loop through items in an array, processing each item at a time.

```mw
 int myArray[12];
 int ix;
 for (ix = 0; ix < 12; ix++) {
   myArray[ix] = 5 * ix + 3;
 }
```

The above for loop initializes each of the 12 elements of myArray. The loop index can start from any value. In the following case it starts from 1.

```mw
 for (ix = 1; ix <= 10; ix++) {
   printf("%d ", ix);
 }
```

which will print

```
1 2 3 4 5 6 7 8 9 10 
```

You will most often use loop indexes that start from 0, since arrays are indexed at zero, but you will sometimes use other values to initialize a loop index as well.

The *increment* action can do other things, such as *decrement*. So this kind of loop is common:

```mw
 for (i = 5; i > 0; i--) {
   printf("%d ", i);
 }
```

which yields

```
5 4 3 2 1 
```

Here's an example where the test condition is simply a variable. If the variable has a value of 0 or NULL, the loop exits, otherwise the statements in the body of the loop are executed.

```mw
 for (t = list_head; t; t = NextItem(t)) {
   /* body of loop */
 }
```

A WHILE loop can be used to do the same thing as a FOR loop, however a FOR loop is a more condensed way to perform a set number of repetitions since all of the necessary information is in a one line statement.

A FOR loop can also be given no conditions, for example:

```mw
 for (;;) {
   /* block of statements */
 }
```

This is called an infinite loop since it will loop forever unless there is a break statement within the statements of the for loop. The empty test condition effectively evaluates as true.

It is also common to use the comma operator in for loops to execute multiple statements.

```mw
 int i, j, n = 10;
 for (i = 0, j = 0; i <= n; i++, j += 2) {
   printf("i = %d , j = %d \n", i, j);
 }
```

Special care should be taken when designing or refactoring the conditional part, especially whether using < or <= , whether start and stop should be corrected by 1, and in case of prefix- and postfix-notations. ( On a 100 yards promenade with a tree every 10 yards there are 11 trees. )

```mw
 int i, n = 10;
 for (i = 0; i < n; i++)
   printf("%d ", i); // processed n times => 0 1 2 3 ... (n-1)
 printf("\n");
 for (i = 0; i <= n; i++)
   printf("%d ", i); // processed (n+1) times => 0 1 2 3 ... n 
 printf("\n");
 for (i = n; i--;)
   printf("%d ", i); // processed n times => (n-1) ...3 2 1 0 
 printf("\n");
 for (i = n; --i;)
   printf("%d ", i); // processed (n-1) times => (n-1) ...4 3 2 1 
 printf("\n");
```

### `do`–`while` loops

A DO-WHILE loop is a post-check while loop, which means that it checks the condition after each run. As a result, even if the condition is zero (false), it will run at least once. It follows the form of:

```mw
 do {
   /* do stuff */
 } while (condition);
```

Note the terminating semicolon. This is required for correct syntax. Since this is also a type of while loop, **break** and **continue** statements within the loop function accordingly. A **continue** statement causes a jump to the test of the condition and a *break* statement exits the loop.

It is worth noting that Do-While and While are functionally almost identical, with one important difference: Do-While loops are always guaranteed to execute at least once, but While loops will not execute at all if their condition is 0 (false) on the first evaluation.

## One last thing: `goto`

**goto** is a very simple and traditional control mechanism. It is a statement used to immediately and unconditionally jump to another line of code. To use goto, you must place a label at a point in your program. A label consists of a name followed by a colon (:) on a line by itself. Then, you can type "goto *label*;" at the desired point in your program. The code will then continue executing beginning with *label*. This looks like:

```mw
 MyLabel:
   /* some code */
   goto MyLabel;
```

The ability to transfer the flow of control enabled by gotos is so powerful that, in addition to the simple if, all other control constructs can be written using gotos instead. Here, we can let "S" and "T" be any arbitrary statements:

```mw
 if (''cond'') {
   S;
 } else {
   T;
 }
 /* ... */
```

The same statement could be accomplished using two gotos and two labels:

```mw
 if (''cond'') goto Label1;
   T;
   goto Label2;
 Label1:
   S;
 Label2:
   /* ... */
```

Here, the first goto is conditional on the value of "cond". The second goto is unconditional. We can perform the same translation on a loop:

```mw
 while (''cond1'') {
   S;
   if (''cond2'')
     break;
   T;
 }
 /* ... */
```

Which can be written as:

```mw
 Start:
   if (!''cond1'') goto End;
   S;
   if (''cond2'') goto End;
   T;
   goto Start;
 End:
   /* ... */
```

As these cases demonstrate, often the structure of what your program is doing can usually be expressed without using gotos. Undisciplined use of gotos can create unreadable, unmaintainable code when more idiomatic alternatives (such as if-elses, or for loops) can better express your structure. Theoretically, the goto construct does not ever *have* to be used, but there are cases when it can increase readability, avoid code duplication, or make control variables unnecessary. You should consider first mastering the idiomatic solutions, and use goto only when necessary. Keep in mind that many, if not most, C style guidelines *strictly forbid* use of **goto**, with the only common exceptions being the following examples.

One use of goto is to break out of a deeply nested loop. Since **break** will not work (it can only escape one loop), **goto** can be used to jump completely outside the loop. Breaking outside of deeply nested loops without the use of the goto is always possible, but often involves the creation and testing of extra variables that may make the resulting code far less readable than it would be with **goto**. The use of **goto** makes it easy to undo actions in an orderly fashion, typically to avoid failing to free memory that had been allocated.

Another accepted use is the creation of a state machine. This is a fairly advanced topic though, and not commonly needed.
