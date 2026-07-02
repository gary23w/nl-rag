---
title: "The GNU Awk User’s Guide (part 25/38)"
source: https://www.gnu.org/software/gawk/manual/gawk.html
domain: awk-lang
license: CC-BY-SA-4.0
tags: awk language, gnu awk, gawk, awk script
fetched: 2026-07-02
part: 25/38
---

## 16 Arithmetic and Arbitrary-Precision Arithmetic with `gawk`

This chapter introduces some basic concepts relating to how computers do arithmetic and defines some important terms. It then proceeds to describe floating-point arithmetic, which is what `awk` uses for all its computations, including a discussion of arbitrary-precision floating-point arithmetic, which is a feature available only in `gawk`. It continues on to present arbitrary-precision integers, and concludes with a description of some points where `gawk` and the POSIX standard are not quite in agreement.

> **NOTE:** Most users of `gawk` can safely skip this chapter. But if you want to do scientific calculations with `gawk`, this is the place to be.

### 16.1 A General Description of Computer Arithmetic

> Have you ever considered that the plural of “half” is “whole”?

—

Allan Sherman

Until now, we have worked with data as either numbers or strings. Ultimately, however, computers represent everything in terms of *binary digits*, or *bits*. A decimal digit can take on any of 10 values: zero through nine. A binary digit can take on any of two values, zero or one. Using binary, computers (and computer software) can represent and manipulate numerical and character data. In general, the more bits you can use to represent a particular thing, the greater the range of possible values it can take on.

Modern computers support at least two, and often more, ways to do arithmetic. Each kind of arithmetic uses a different representation (organization of the bits) for the numbers. The kinds of arithmetic that interest us are:

**Decimal arithmetic**

This is the kind of arithmetic you learned in elementary school, using paper and pencil (and/or a calculator). In theory, numbers can have an arbitrary number of digits on either side (or both sides) of the decimal point, and the results of a computation are always exact.

Some modern systems can do decimal arithmetic in hardware, but usually you need a special software library to provide access to these instructions. There are also libraries that do decimal arithmetic entirely in software.

Despite the fact that some users expect `gawk` to be performing decimal arithmetic,100 it does not do so.

**Integer arithmetic**

In school, integer values were referred to as “whole” numbers—that is, numbers without any fractional part, such as 1, 42, or −17. The advantage to integer numbers is that they represent values exactly. The disadvantage is that their range is limited.

In computers, integer values come in two flavors: *signed* and *unsigned*. Signed values may be negative or positive, whereas unsigned values are always greater than or equal to zero.

In computer systems, integer arithmetic is exact, but the possible range of values is limited. Integer arithmetic is generally faster than floating-point arithmetic.

**Floating-point arithmetic**

Floating-point numbers represent what were called in school “real” numbers (i.e., those that have a fractional part, such as 3.1415927). The advantage to floating-point numbers is that they can represent a much larger range of values than can integers. The disadvantage is that there are numbers that they cannot represent exactly.

Modern systems support floating-point arithmetic in hardware, with a limited range of values. There are software libraries that allow the use of arbitrary-precision floating-point calculations.

POSIX `awk` uses *double-precision* floating-point numbers, which can hold more digits than *single-precision* floating-point numbers. `gawk` has facilities for performing arbitrary-precision floating-point arithmetic, which we describe in more detail shortly.

Computers work with integer and floating-point values of different ranges. Integer values are usually either 32 or 64 bits in size. Single-precision floating-point values occupy 32 bits, whereas double-precision floating-point values occupy 64 bits. (Quadruple-precision floating point values also exist. They occupy 128 bits, but such numbers are not available in `awk`.) Floating-point values are always signed. The possible ranges of values are shown in Table 16.1 and Table 16.2.

| Representation | Minimum value | Maximum value |
|---|---|---|
| 32-bit signed integer | −2,147,483,648 | 2,147,483,647 |
| 32-bit unsigned integer | 0 | 4,294,967,295 |
| 64-bit signed integer | −9,223,372,036,854,775,808 | 9,223,372,036,854,775,807 |
| 64-bit unsigned integer | 0 | 18,446,744,073,709,551,615 |

**Table 16.1:**Value ranges for integer representations

| Representation | Minimum positive nonzero value | Minimum finite value | Maximum finite value |
|---|---|---|---|
| Single-precision floating-point | 1.175494*10-38 | -3.402823*1038 | 3.402823*1038 |
| Double-precision floating-point | 2.225074*10-308 | -1.797693*10308 | 1.797693*10308 |
| Quadruple-precision floating-point | 3.362103*10-4932 | -1.189731*104932 | 1.189731*104932 |

**Table 16.2:**Approximate value ranges for floating-point number representations

### 16.2 Other Stuff to Know

The rest of this chapter uses a number of terms. Here are some informal definitions that should help you work your way through the material here:

***Accuracy***

A floating-point calculation’s accuracy is how close it comes to the real (paper and pencil) value.

***Error***

The difference between what the result of a computation “should be” and what it actually is. It is best to minimize error as much as possible.

***Exponent***

The order of magnitude of a value; some number of bits in a floating-point value store the exponent.

***Inf***

A special value representing infinity. Operations involving another number and infinity produce infinity.

***NaN***

“Not a number.” A special value that results from attempting a calculation that has no answer as a real number. See Floating Point Values They Didn’t Talk About In School, for more information about infinity and not-a-number values.

***Normalized***

How the significand (see later in this list) is usually stored. The value is adjusted so that the first bit is one, and then that leading one is assumed instead of physically stored. This provides one extra bit of precision.

***Precision***

The number of bits used to represent a floating-point number. The more bits, the more digits you can represent. Binary and decimal precisions are related approximately, according to the formula:

```
prec = 3.322 * dps
```

Here, *prec* denotes the binary precision (measured in bits) and *dps* (short for decimal places) is the decimal digits.

***Rounding mode***

How numbers are rounded up or down when necessary. More details are provided later.

***Significand***

A floating-point value consists of the significand multiplied by 10 to the power of the exponent. For example, in `1.2345e67`, the significand is `1.2345`.

***Stability***

From the Wikipedia article on numerical stability: “Calculations that can be proven not to magnify approximation errors are called *numerically stable*.”

See the Wikipedia article on accuracy and precision for more information on some of those terms.

On modern systems, floating-point hardware uses the representation and operations defined by the IEEE 754 standard. Three of the standard IEEE 754 types are 32-bit single precision, 64-bit double precision, and 128-bit quadruple precision. The standard also specifies extended precision formats to allow greater precisions and larger exponent ranges. (`awk` uses only the 64-bit double-precision format.)

Table 16.3 lists the precision and exponent field values for the basic IEEE 754 binary formats.

| Name | Total bits | Precision | Minimum exponent | Maximum exponent |
|---|---|---|---|---|
| Single | 32 | 24 | −126 | +127 |
| Double | 64 | 53 | −1022 | +1023 |
| Quadruple | 128 | 113 | −16382 | +16383 |

**Table 16.3:**Basic IEEE format values

> **NOTE:** The precision numbers include the implied leading one that gives them one extra bit of significand.

### 16.3 Arbitrary-Precision Arithmetic Features in `gawk`

This section briefly describes arbitrary-precision arithmetic in `gawk`.

#### 16.3.1 Arbitrary Precision Arithmetic is On Parole!

As of version 5.2, arbitrary precision arithmetic in `gawk` is “on parole.” The primary `gawk` maintainer is no longer maintaining it. Fortunately, a volunteer from the development team has agreed to take it over.

This feature is on parole because its inclusion was a mistake. It has led to endless bug reports, misuse of the feature and public abuse of the maintainer, for no real increased value.

If the situation with support changes, the feature will be removed from `gawk`.

If you use this feature, you should consider finding a different toolset with which to accomplish your goals.101

#### 16.3.2 Arbitrary Precision Introduction

By default, `gawk` uses the double-precision floating-point values supplied by the hardware of the system it runs on. However, if it was compiled to do so, and the -M command-line option is supplied, `gawk` uses the GNU MPFR and GNU MP (GMP) libraries for arbitrary-precision arithmetic on numbers. You can see if MPFR support is available like so:

```
$ gawk --version
-| GNU Awk 5.3.1, API 4.0, PMA Avon 8-g1, (GNU MPFR 4.1.0, GNU MP 6.2.1)
-| Copyright (C) 1989, 1991-2024 Free Software Foundation.
...
```

(You may see different version numbers than what’s shown here. That’s OK; what’s important is to see that GNU MPFR and GNU MP are listed in the output.)

Additionally, there are a few elements available in the `PROCINFO` array to provide information about the MPFR and GMP libraries (see Built-in Variables That Convey Information).

The MPFR library provides precise control over precisions and rounding modes, and gives correctly rounded, reproducible, platform-independent results. With the -M command-line option, all floating-point arithmetic operators and numeric functions can yield results to any desired precision level supported by MPFR.

Two predefined variables, `PREC` and `ROUNDMODE`, provide control over the working precision and the rounding mode. The precision and the rounding mode are set globally for every operation to follow. See Setting the Precision and Setting the Rounding Mode for more information.

### 16.4 Floating-Point Arithmetic: Caveat Emptor!

> *Math class is tough!*

—

Teen Talk Barbie, July 1992

This section provides a high-level overview of the issues involved when doing lots of floating-point arithmetic.102 The discussion applies to both hardware and arbitrary-precision floating-point arithmetic.

> **CAUTION:** The material here is purposely general. If you need to do serious computer arithmetic, you should do some research first, and not rely just on what we tell you.

#### 16.4.1 Floating-Point Arithmetic Is Not Exact

Binary floating-point representations and arithmetic are inexact. Simple values like 0.1 cannot be precisely represented using binary floating-point numbers, and the limited precision of floating-point numbers means that slight changes in the order of operations or the precision of intermediate storage can change the result. To make matters worse, with arbitrary-precision floating-point arithmetic, you can set the precision before starting a computation, but then you cannot be sure of the number of significant decimal places in the final result.

#### 16.4.1.1 Many Numbers Cannot Be Represented Exactly

So, before you start to write any code, you should think about what you really want and what’s really happening. Consider the two numbers in the following example:

```
x = 0.875             # 1/2 + 1/4 + 1/8
y = 0.425
```

Unlike the number in `y`, the number stored in `x` is exactly representable in binary because it can be written as a finite sum of one or more fractions whose denominators are all powers of two. When `gawk` reads a floating-point number from program source, it automatically rounds that number to whatever precision your machine supports. If you try to print the numeric content of a variable using an output format string of `"%.17g"`, it may not produce the same number as you assigned to it:

```
$ gawk 'BEGIN { x = 0.875; y = 0.425
>               printf("%0.17g, %0.17g\n", x, y) }'
-| 0.875, 0.42499999999999999
```

Often the error is so small you do not even notice it, and if you do, you can always specify how much precision you would like in your output. Usually this is a format string like `"%.15g"`, which, when used in the previous example, produces an output identical to the input.

#### 16.4.1.2 Be Careful Comparing Values

Because the underlying representation can be a little bit off from the exact value, comparing floating-point values to see if they are exactly equal is generally a bad idea. Here is an example where it does not work like you would expect:

```
$ gawk 'BEGIN { print (0.1 + 12.2 == 12.3) }'
-| 0
```

The general wisdom when comparing floating-point values is to see if they are within some small range of each other (called a *delta*, or *tolerance*). You have to decide how small a delta is important to you. Code to do this looks something like the following:

```
delta = 0.00001                 # for example
difference = abs(a - b)         # subtract the two values
if (difference < delta)
    # all ok
else
    # not ok
```

(We assume that you have a simple absolute value function named `abs()` defined elsewhere in your program.) If you write a function to compare values with a delta, you should be sure to use ‘difference < abs(delta)’ in case someone passes in a negative delta value.

#### 16.4.1.3 Errors Accumulate

The loss of accuracy during a single computation with floating-point numbers usually isn’t enough to worry about. However, if you compute a value that is the result of a sequence of floating-point operations, the error can accumulate and greatly affect the computation itself. Here is an attempt to compute the value of *pi* using one of its many series representations:

```
BEGIN {
    x = 1.0 / sqrt(3.0)
    n = 6
    for (i = 1; i < 30; i++) {
        n = n * 2.0
        x = (sqrt(x * x + 1) - 1) / x
        printf("%.15f\n", n * x)
    }
}
```

When run, the early errors propagate through later computations, causing the loop to terminate prematurely after attempting to divide by zero:

```
$ gawk -f pi.awk
-| 3.215390309173475
-| 3.159659942097510
-| 3.146086215131467
-| 3.142714599645573
...
-| 3.224515243534819
-| 2.791117213058638
-| 0.000000000000000
error→ gawk: pi.awk:6: fatal: division by zero attempted
```

Here is an additional example where the inaccuracies in internal representations yield an unexpected result:

```
$ gawk 'BEGIN {
>   for (d = 1.1; d <= 1.5; d += 0.1)    # loop five times (?)
>       i++
>   print i
> }'
-| 4
```

#### 16.4.1.4 Floating Point Values They Didn’t Talk About In School

Both IEEE 754 floating-point hardware, and MPFR, support two kinds of values that you probably didn’t learn about in school. The first is *infinity*, a special value, that can be either negative or positive, and which is either smaller than any other value (negative infinity), or larger than any other value (positive infinity). When such values are generated, `gawk` prints them as either ‘-inf’ or ‘+inf’, respectively. It accepts those strings as data input and converts them to the proper floating-point values internally.

Infinity values of the same sign compare as equal to each other. Otherwise, operations (addition, subtraction, etc.) involving another number and infinity produce mathematically reasonable results.

The second kind of value is “not a number”, or NaN for short.103 This is a special value that results from attempting a calculation that has no answer as a real number. In such a case, programs can either receive a floating-point exception, or get NaN back as the result. The IEEE 754 standard recommends that systems return NaN. Some examples:

**`sqrt(-1)`**

This makes sense in the range of complex numbers, but not in the range of real numbers, so the result is NaN.

**`log(-8)`**

−8 is out of the domain of `log()`, so the result is NaN.

NaN values are strange. In particular, they cannot be compared with other floating point values; any such comparison, except for “is not equal to”, returns false. NaN values are so much unequal to other values that even comparing two identical NaN values with `!=` returns true!

NaN values can also be signed, although it depends upon the implementation as to which sign you get for any operation that returns a NaN. For example, on some systems, `sqrt(-1)` returns a negative NaN. On others, it returns a positive NaN.

When such values are generated, `gawk` prints them as either ‘-nan’ or ‘+nan’, respectively. Here too, `gawk` accepts those strings as data input and converts them to the proper floating-point values internally.

If you want to dive more deeply into this topic, you can find test programs in C, `awk` and Python in the directory awklib/eg/test-programs in the `gawk` distribution. These programs enable comparison among programming languages as to how they handle NaN and infinity values.

#### 16.4.2 Getting the Accuracy You Need

Can arbitrary-precision arithmetic give exact results? There are no easy answers. The standard rules of algebra often do not apply when using floating-point arithmetic. Among other things, the distributive and associative laws do not hold completely, and order of operation may be important for your computation. Rounding error, cumulative precision loss, and underflow are often troublesome.

When `gawk` tests the expressions ‘0.1 + 12.2’ and ‘12.3’ for equality using the machine double-precision arithmetic, it decides that they are not equal! (See Be Careful Comparing Values.) You can get the result you want by increasing the precision; 56 bits in this case does the job:

```
$ gawk -M -v PREC=56 'BEGIN { print (0.1 + 12.2 == 12.3) }'
-| 1
```

If adding more bits is good, perhaps adding even more bits of precision is better? Here is what happens if we use an even larger value of `PREC`:

```
$ gawk -M -v PREC=201 'BEGIN { print (0.1 + 12.2 == 12.3) }'
-| 0
```

This is not a bug in `gawk` or in the MPFR library. It is easy to forget that the finite number of bits used to store the value is often just an approximation after proper rounding. The test for equality succeeds if and only if *all* bits in the two operands are exactly the same. Because this is not necessarily true after floating-point computations with a particular precision and effective rounding mode, a straight test for equality may not work. Instead, compare the two numbers to see if they are within the desirable delta of each other.

In applications where 15 or fewer decimal places suffice, hardware double-precision arithmetic can be adequate, and is usually much faster. But you need to keep in mind that every floating-point operation can suffer a new rounding error with catastrophic consequences, as illustrated by our earlier attempt to compute the value of *pi*. Extra precision can greatly enhance the stability and the accuracy of your computation in such cases.

Additionally, you should understand that repeated addition is not necessarily equivalent to multiplication in floating-point arithmetic. In the example in Errors Accumulate:

```
$ gawk 'BEGIN {
>   for (d = 1.1; d <= 1.5; d += 0.1)    # loop five times (?)
>       i++
>   print i
> }'
-| 4
```

you may or may not succeed in getting the correct result by choosing an arbitrarily large value for `PREC`. Reformulation of the problem at hand is often the correct approach in such situations.

#### 16.4.3 Try a Few Extra Bits of Precision and Rounding

Instead of arbitrary-precision floating-point arithmetic, often all you need is an adjustment of your logic or a different order for the operations in your calculation. The stability and the accuracy of the computation of *pi* in the earlier example can be enhanced by using the following simple algebraic transformation:

```
(sqrt(x * x + 1) - 1) / x ≡ x / (sqrt(x * x + 1) + 1)
```

After making this change, the program converges to *pi* in under 30 iterations:

```
$ gawk -f pi2.awk
-| 3.215390309173473
-| 3.159659942097501
-| 3.146086215131436
-| 3.142714599645370
-| 3.141873049979825
...
-| 3.141592653589797
-| 3.141592653589797
```

#### 16.4.4 Setting the Precision

`gawk` uses a global working precision; it does not keep track of the precision or accuracy of individual numbers. Performing an arithmetic operation or calling a built-in function rounds the result to the current working precision. The default working precision is 53 bits, which you can modify using the predefined variable `PREC`. You can also set the value to one of the predefined case-insensitive strings shown in Table 16.4, to emulate an IEEE 754 binary format.

| `PREC` | IEEE 754 binary format |
|---|---|
| `"half"` | 16-bit half-precision |
| `"single"` | Basic 32-bit single precision |
| `"double"` | Basic 64-bit double precision |
| `"quad"` | Basic 128-bit quadruple precision |
| `"oct"` | 256-bit octuple precision |

**Table 16.4:**Predefined precision strings for `PREC`

The following example illustrates the effects of changing precision on arithmetic operations:

```
$ gawk -M -v PREC=100 'BEGIN { x = 1.0e-400; print x + 0
>   PREC = "double"; print x + 0 }'
-| 1e-400
-| 0
```

> **CAUTION:** Be wary of floating-point constants! When reading a floating-point constant from program source code, `gawk` uses the default precision (that of a C `double`), unless overridden by an assignment to the special variable `PREC` on the command line, to store it internally as an MPFR number. Changing the precision using `PREC` in the program text does *not* change the precision of a constant.
> 
> If you need to represent a floating-point constant at a higher precision than the default and cannot use a command-line assignment to `PREC`, you should either specify the constant as a string, or as a rational number, whenever possible. The following example illustrates the differences among various ways to print a floating-point constant:
> 
> ```
> $ gawk -M 'BEGIN { PREC = 113; printf("%0.25f\n", 0.1) }'
> -| 0.1000000000000000055511151
> $ gawk -M -v PREC=113 'BEGIN { printf("%0.25f\n", 0.1) }'
> -| 0.1000000000000000000000000
> $ gawk -M 'BEGIN { PREC = 113; printf("%0.25f\n", "0.1") }'
> -| 0.1000000000000000000000000
> $ gawk -M 'BEGIN { PREC = 113; printf("%0.25f\n", 1/10) }'
> -| 0.1000000000000000000000000
> ```

#### 16.4.5 Setting the Rounding Mode

The `ROUNDMODE` variable provides program-level control over the rounding mode. The correspondence between `ROUNDMODE` and the IEEE rounding modes is shown in Table 16.5.

| Rounding mode | IEEE name | `ROUNDMODE` |
|---|---|---|
| Round to nearest, ties to even | `roundTiesToEven` | `"N"` or `"n"` |
| Round toward positive infinity | `roundTowardPositive` | `"U"` or `"u"` |
| Round toward negative infinity | `roundTowardNegative` | `"D"` or `"d"` |
| Round toward zero | `roundTowardZero` | `"Z"` or `"z"` |
| Round away from zero |   | `"A"` or `"a"` |

**Table 16.5:**`gawk` rounding modes

`ROUNDMODE` has the default value `"N"`, which selects the IEEE 754 rounding mode `roundTiesToEven`. In Table 16.5, the value `"A"` selects rounding away from zero. This is only available if your version of the MPFR library supports it; otherwise, setting `ROUNDMODE` to `"A"` has no effect.

The default mode `roundTiesToEven` is the most preferred, but the least intuitive. This method does the obvious thing for most values, by rounding them up or down to the nearest digit. For example, rounding 1.132 to two digits yields 1.13, and rounding 1.157 yields 1.16.

However, when it comes to rounding a value that is exactly halfway between, things do not work the way you probably learned in school. In this case, the number is rounded to the nearest even digit. So rounding 0.125 to two digits rounds down to 0.12, but rounding 0.6875 to three digits rounds up to 0.688. You probably have already encountered this rounding mode when using `printf` to format floating-point numbers. For example:

```
BEGIN {
    x = -4.5
    for (i = 1; i < 10; i++) {
        x += 1.0
        printf("%4.1f => %2.0f\n", x, x)
    }
}
```

produces the following output when run on the author’s system:104

```
-3.5 => -4
-2.5 => -2
-1.5 => -2
-0.5 => 0
 0.5 => 0
 1.5 => 2
 2.5 => 2
 3.5 => 4
 4.5 => 4
```

The theory behind `roundTiesToEven` is that it more or less evenly distributes upward and downward rounds of exact halves, which might cause any accumulating round-off error to cancel itself out. This is the default rounding mode for IEEE 754 computing functions and operators.

| Rounding Modes and Conversion |
|---|
| It’s important to understand that, along with `CONVFMT` and `OFMT`, the rounding mode affects how numbers are converted to strings. For example, consider the following program: BEGIN { pi = 3.1416 OFMT = "%.f" # Print value as integer print pi # ROUNDMODE = "N" by default. ROUNDMODE = "U" # Now change ROUNDMODE print pi } Running this program produces this output: $ gawk -M -f roundmode.awk -\| 3 -\| 4 |

The other rounding modes are rarely used. Rounding toward positive infinity (`roundTowardPositive`) and toward negative infinity (`roundTowardNegative`) are often used to implement interval arithmetic, where you adjust the rounding mode to calculate upper and lower bounds for the range of output. The `roundTowardZero` mode can be used for converting floating-point numbers to integers. When rounding away from zero, the nearest number with magnitude greater than or equal to the value is selected.

Some numerical analysts will tell you that your choice of rounding style has tremendous impact on the final outcome, and advise you to wait until final output for any rounding. Instead, you can often avoid round-off error problems by setting the precision initially to some value sufficiently larger than the final desired precision, so that the accumulation of round-off error does not influence the outcome. If you suspect that results from your computation are sensitive to accumulation of round-off error, look for a significant difference in output when you change the rounding mode to be sure.

### 16.5 Arbitrary-Precision Integer Arithmetic with `gawk`

When given the -M option, `gawk` performs all integer arithmetic using GMP arbitrary-precision integers. Any number that looks like an integer in a source or data file is stored as an arbitrary-precision integer. The size of the integer is limited only by the available memory. For example, the following computes 5432, the result of which is beyond the limits of ordinary hardware double-precision floating-point values:

```
$ gawk -M 'BEGIN {
>   x = 5^4^3^2
>   print "number of digits =", length(x)
>   print substr(x, 1, 20), "...", substr(x, length(x) - 19, 20)
> }'
-| number of digits = 183231
-| 62060698786608744707 ... 92256259918212890625
```

If instead you were to compute the same value using arbitrary-precision floating-point values, the precision needed for correct output (using the formula ‘prec = 3.322 * dps’) would be 3.322 x 183231, or 608693.

The result from an arithmetic operation with an integer and a floating-point value is a floating-point value with a precision equal to the working precision. The following program calculates the eighth term in Sylvester’s sequence105 using a recurrence:

```
$ gawk -M 'BEGIN {
>   s = 2.0
>   for (i = 1; i <= 7; i++)
>       s = s * (s - 1) + 1
>   print s
> }'
-| 113423713055421845118910464
```

The output differs from the actual number, 113,423,713,055,421,844,361,000,443, because the default precision of 53 bits is not enough to represent the floating-point results exactly. You can either increase the precision (100 bits is enough in this case), or replace the floating-point constant ‘2.0’ with an integer, to perform all computations using integer arithmetic to get the correct output.

Sometimes `gawk` must implicitly convert an arbitrary-precision integer into an arbitrary-precision floating-point value. This is primarily because the MPFR library does not always provide the relevant interface to process arbitrary-precision integers or mixed-mode numbers as needed by an operation or function. In such a case, the precision is set to the minimum value necessary for exact conversion, and the working precision is not used for this purpose. If this is not what you need or want, you can employ a subterfuge and convert the integer to floating point first, like this:

```
gawk -M 'BEGIN { n = 13; print (n + 0.0) % 2.0 }'
```

You can avoid this issue altogether by specifying the number as a floating-point value to begin with:

```
gawk -M 'BEGIN { n = 13.0; print n % 2.0 }'
```

Note that for this particular example, it is likely best to just use the following:

```
gawk -M 'BEGIN { n = 13; print n % 2 }'
```

When dividing two arbitrary precision integers with either ‘/’ or ‘%’, the result is typically an arbitrary precision floating point value (unless the denominator evenly divides into the numerator).

### 16.6 How To Check If MPFR Is Available

Occasionally, you might like to be able to check if `gawk` was invoked with the -M option, enabling arbitrary-precision arithmetic. You can do so with the following function, contributed by Andrew Schorr:

```
# adequate_math_precision --- return true if we have enough bits

function adequate_math_precision(n)
{
    return (1 != (1+(1/(2^(n-1)))))
}
```

Here is code that invokes the function in order to check if arbitrary-precision arithmetic is available:

```
BEGIN {
    # How many bits of mantissa precision are required
    # for this program to function properly?
    fpbits = 123

    # We hope that we were invoked with MPFR enabled. If so, the
    # following statement should configure calculations to our desired
    # precision.
    PREC = fpbits

    if (! adequate_math_precision(fpbits)) {
        print("Error: insufficient computation precision available.\n" \
              "Try again with the -M argument?") > "/dev/stderr"
        # Note: you may need to set a flag here to bail out of END rules
        exit 1
    }
}
```

Please be aware that `exit` will jump to the `END` rules, if present (see The `exit` Statement).

### 16.7 Standards Versus Existing Practice

Historically, `awk` has converted any nonnumeric-looking string to the numeric value zero, when required. Furthermore, the original definition of the language and the original POSIX standards specified that `awk` only understands decimal numbers (base 10), and not octal (base 8) or hexadecimal numbers (base 16).

Changes in the language of the 2001 and 2004 POSIX standards can be interpreted to imply that `awk` should support additional features. These features are:

- Interpretation of floating-point data values specified in hexadecimal notation (e.g., `0xDEADBEEF`). (Note: data values, *not* source code constants.)
- Support for the special IEEE 754 floating-point values “not a number” (NaN), positive infinity (“inf”), and negative infinity (“−inf”). In particular, the format for these values is as specified by the ISO 1999 C standard, which ignores case and can allow implementation-dependent additional characters after the ‘nan’ and allow either ‘inf’ or ‘infinity’.

The first problem is that both of these are clear changes to historical practice:

- The `gawk` maintainer feels that supporting hexadecimal floating-point values, in particular, is ugly, and was never intended by the original designers to be part of the language.
- Allowing completely alphabetic strings to have valid numeric values is also a very severe departure from historical practice.

The second problem is that the `gawk` maintainer feels that this interpretation of the standard, which required a certain amount of “language lawyering” to arrive at in the first place, was not even intended by the standard developers. In other words, “We see how you got where you are, but we don’t think that that’s where you want to be.”

Recognizing these issues, but attempting to provide compatibility with the earlier versions of the standard, the 2008 POSIX standard added explicit wording to allow, but not require, that `awk` support hexadecimal floating-point values and special values for “not a number” and infinity.

Although the `gawk` maintainer continues to feel that providing those features is inadvisable, nevertheless, on systems that support IEEE floating point, it seems reasonable to provide *some* way to support NaN and infinity values. The solution implemented in `gawk` is as follows:

- With the --posix command-line option, `gawk` becomes “hands off.” String values are passed directly to the system library’s `strtod()` function, and if it successfully returns a numeric value, that is what’s used.106 By definition, the results are not portable across different systems. They are also a little surprising: $ echo nanny | gawk --posix '{ print $1 + 0 }' -| nan $ echo 0xDeadBeef | gawk --posix '{ print $1 + 0 }' -| 3735928559
- Without --posix, `gawk` interprets the four string values ‘+inf’, ‘-inf’, ‘+nan’, and ‘-nan’ specially, producing the corresponding special numeric values. The leading sign acts a signal to `gawk` (and the user) that the value is really numeric. Hexadecimal floating point is not supported (unless you also use --non-decimal-data, which is *not* recommended). For example: $ echo nanny | gawk '{ print $1 + 0 }' -| 0 $ echo +nan | gawk '{ print $1 + 0 }' -| +nan $ echo 0xDeadBeef | gawk '{ print $1 + 0 }' -| 0 `gawk` ignores case in the four special values. Thus, ‘+nan’ and ‘+NaN’ are the same.

Besides handling input, `gawk` also needs to print “correct” values on output when a value is either NaN or infinity. Starting with version 4.2.2, for such values `gawk` prints one of the four strings just described: ‘+inf’, ‘-inf’, ‘+nan’, or ‘-nan’. Similarly, in POSIX mode, `gawk` prints the result of the system’s C `printf()` function using the `%g` format string for the value, whatever that may be.

### 16.8 Summary

- Most computer arithmetic is done using either integers or floating-point values. Standard `awk` uses double-precision floating-point values.
- In the early 1990s Barbie mistakenly said, “Math class is tough!” Although math isn’t tough, floating-point arithmetic isn’t the same as pencil-and-paper math, and care must be taken:
  - Not all numbers can be represented exactly.
  - Comparing values should use a delta, instead of being done directly with ‘==’ and ‘!=’.
  - Errors accumulate.
  - Operations are not always truly associative or distributive.
- Increasing the accuracy can help, but it is not a panacea.
- Often, increasing the accuracy and then rounding to the desired number of digits produces reasonable results.
- Use -M (or --bignum) to enable MPFR arithmetic. Use `PREC` to set the precision in bits, and `ROUNDMODE` to set the IEEE 754 rounding mode.
- With -M, `gawk` performs arbitrary-precision integer arithmetic using the GMP library. This is faster and more space-efficient than using MPFR for the same calculations.
- There are several areas with respect to floating-point numbers where `gawk` disagrees with the POSIX standard. It pays to be aware of them.
- Overall, there is no need to be unduly suspicious about the results from floating-point arithmetic. The lesson to remember is that floating-point arithmetic is always more complex than arithmetic using pencil and paper. In order to take advantage of the power of floating-point arithmetic, you need to know its limitations and work within them. For most casual use of floating-point arithmetic, you will often get the expected result if you simply round the display of your final results to the correct number of significant decimal digits.
- As general advice, avoid presenting numerical data in a manner that implies better precision than is actually the case.
