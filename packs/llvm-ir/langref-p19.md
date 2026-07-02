---
title: "LLVM Language Reference Manual (part 19/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-ir
license: CC-BY-SA-4.0
tags: llvm ir, llvm intermediate representation, static single assignment, three-address code
fetched: 2026-07-02
part: 19/20
---

# LLVM Language Reference Manual

The first argument and the return value are floating-point or vector of floating-point values of the same type. The second argument is an integer with the same number of elements.

The third and fourth arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function multiplies the first argument by 2 raised to the second argument’s power. If the first argument is NaN or infinite, the same value is returned. If the result underflows a zero with the same sign is returned. If the result overflows, the result is an infinity with the same sign.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.sin(<type> <op1>,
                                   metadata <rounding mode>,
                                   metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.sin`’ intrinsic returns the sine of the first argument.

##### Arguments:

The first argument and the return type are floating-point numbers of the same type.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the sine of the specified argument, returning the same values as the libm `sin` functions would, and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.cos(<type> <op1>,
                                   metadata <rounding mode>,
                                   metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.cos`’ intrinsic returns the cosine of the first argument.

##### Arguments:

The first argument and the return type are floating-point numbers of the same type.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the cosine of the specified argument, returning the same values as the libm `cos` functions would, and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.tan(<type> <op1>,
                                   metadata <rounding mode>,
                                   metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.tan`’ intrinsic returns the tangent of the first argument.

##### Arguments:

The first argument and the return type are floating-point numbers of the same type.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the tangent of the specified argument, returning the same values as the libm `tan` functions would, and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.asin(<type> <op1>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.asin`’ intrinsic returns the arcsine of the first operand.

##### Arguments:

The first argument and the return type are floating-point numbers of the same type.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the arcsine of the specified operand, returning the same values as the libm `asin` functions would, and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.acos(<type> <op1>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.acos`’ intrinsic returns the arccosine of the first operand.

##### Arguments:

The first argument and the return type are floating-point numbers of the same type.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the arccosine of the specified operand, returning the same values as the libm `acos` functions would, and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.atan(<type> <op1>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.atan`’ intrinsic returns the arctangent of the first operand.

##### Arguments:

The first argument and the return type are floating-point numbers of the same type.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the arctangent of the specified operand, returning the same values as the libm `atan` functions would, and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.atan2(<type> <op1>,
                                     <type> <op2>,
                                     metadata <rounding mode>,
                                     metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.atan2`’ intrinsic returns the arctangent of `<op1>` divided by `<op2>` accounting for the quadrant.

##### Arguments:

The first two arguments and the return value are floating-point numbers of the same type.

The third and fourth arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the quadrant-specific arctangent using the specified operands, returning the same values as the libm `atan2` functions would, and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.sinh(<type> <op1>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.sinh`’ intrinsic returns the hyperbolic sine of the first operand.

##### Arguments:

The first argument and the return type are floating-point numbers of the same type.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the hyperbolic sine of the specified operand, returning the same values as the libm `sinh` functions would, and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.cosh(<type> <op1>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.cosh`’ intrinsic returns the hyperbolic cosine of the first operand.

##### Arguments:

The first argument and the return type are floating-point numbers of the same type.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the hyperbolic cosine of the specified operand, returning the same values as the libm `cosh` functions would, and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.tanh(<type> <op1>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.tanh`’ intrinsic returns the hyperbolic tangent of the first operand.

##### Arguments:

The first argument and the return type are floating-point numbers of the same type.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the hyperbolic tangent of the specified operand, returning the same values as the libm `tanh` functions would, and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.exp(<type> <op1>,
                                   metadata <rounding mode>,
                                   metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.exp`’ intrinsic computes the base-e exponential of the specified value.

##### Arguments:

The first argument and the return value are floating-point numbers of the same type.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the same values as the libm `exp` functions would, and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.exp2(<type> <op1>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.exp2`’ intrinsic computes the base-2 exponential of the specified value.

##### Arguments:

The first argument and the return value are floating-point numbers of the same type.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the same values as the libm `exp2` functions would, and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.log(<type> <op1>,
                                   metadata <rounding mode>,
                                   metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.log`’ intrinsic computes the base-e logarithm of the specified value.

##### Arguments:

The first argument and the return value are floating-point numbers of the same type.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the same values as the libm `log` functions would, and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.log10(<type> <op1>,
                                     metadata <rounding mode>,
                                     metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.log10`’ intrinsic computes the base-10 logarithm of the specified value.

##### Arguments:

The first argument and the return value are floating-point numbers of the same type.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the same values as the libm `log10` functions would, and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.log2(<type> <op1>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.log2`’ intrinsic computes the base-2 logarithm of the specified value.

##### Arguments:

The first argument and the return value are floating-point numbers of the same type.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the same values as the libm `log2` functions would, and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.rint(<type> <op1>,
                                    metadata <rounding mode>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.rint`’ intrinsic returns the first argument rounded to the nearest integer. It may raise an inexact floating-point exception if the argument is not an integer.

##### Arguments:

The first argument and the return value are floating-point numbers of the same type.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the same values as the libm `rint` functions would, and handles error conditions in the same way. The rounding mode is described, not determined, by the rounding mode argument. The actual rounding mode is determined by the runtime floating-point environment. The rounding mode argument is only intended as information to the compiler.

##### Syntax:

```
declare <inttype>
@llvm.experimental.constrained.lrint(<fptype> <op1>,
                                     metadata <rounding mode>,
                                     metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.lrint`’ intrinsic returns the first argument rounded to the nearest integer. An inexact floating-point exception will be raised if the argument is not an integer. If the rounded value is too large to fit into the result type, an invalid exception is raised, and the return value is a non-deterministic value (equivalent to *freeze poison*).

##### Arguments:

The first argument is a floating-point number. The return value is an integer type. Not all types are supported on all targets. The supported types are the same as the `llvm.lrint` intrinsic and the `lrint` libm functions.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the same values as the libm `lrint` functions would, and handles error conditions in the same way.

The rounding mode is described, not determined, by the rounding mode argument. The actual rounding mode is determined by the runtime floating-point environment. The rounding mode argument is only intended as information to the compiler.

If the runtime floating-point environment is using the default rounding mode then the results will be the same as the `llvm.lrint` intrinsic.

##### Syntax:

```
declare <inttype>
@llvm.experimental.constrained.llrint(<fptype> <op1>,
                                      metadata <rounding mode>,
                                      metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.llrint`’ intrinsic returns the first argument rounded to the nearest integer. An inexact floating-point exception will be raised if the argument is not an integer. If the rounded value is too large to fit into the result type, an invalid exception is raised, and the return value is a non-deterministic value (equivalent to *freeze poison*).

##### Arguments:

The first argument is a floating-point number. The return value is an integer type. Not all types are supported on all targets. The supported types are the same as the `llvm.llrint` intrinsic and the `llrint` libm functions.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the same values as the libm `llrint` functions would, and handles error conditions in the same way.

The rounding mode is described, not determined, by the rounding mode argument. The actual rounding mode is determined by the runtime floating-point environment. The rounding mode argument is only intended as information to the compiler.

If the runtime floating-point environment is using the default rounding mode then the results will be the same as the `llvm.llrint` intrinsic.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.nearbyint(<type> <op1>,
                                         metadata <rounding mode>,
                                         metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.nearbyint`’ intrinsic returns the first argument rounded to the nearest integer. It will not raise an inexact floating-point exception if the argument is not an integer.

##### Arguments:

The first argument and the return value are floating-point numbers of the same type.

The second and third arguments specify the rounding mode and exception behavior as described above.

##### Semantics:

This function returns the same values as the libm `nearbyint` functions would, and handles error conditions in the same way. The rounding mode is described, not determined, by the rounding mode argument. The actual rounding mode is determined by the runtime floating-point environment. The rounding mode argument is only intended as information to the compiler.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.maxnum(<type> <op1>, <type> <op2>
                                      metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.maxnum`’ intrinsic returns the maximum of the two arguments.

##### Arguments:

The first two arguments and the return value are floating-point numbers of the same type.

The third argument specifies the exception behavior as described above.

##### Semantics:

This function follows the IEEE 754-2008 semantics for maxNum.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.minnum(<type> <op1>, <type> <op2>
                                      metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.minnum`’ intrinsic returns the minimum of the two arguments.

##### Arguments:

The first two arguments and the return value are floating-point numbers of the same type.

The third argument specifies the exception behavior as described above.

##### Semantics:

This function follows the IEEE 754-2008 semantics for minNum.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.maximum(<type> <op1>, <type> <op2>
                                       metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.maximum`’ intrinsic returns the maximum of the two arguments, propagating NaNs and treating -0.0 as less than +0.0.

##### Arguments:

The first two arguments and the return value are floating-point numbers of the same type.

The third argument specifies the exception behavior as described above.

##### Semantics:

This function follows semantics specified in the draft of IEEE 754-2019.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.minimum(<type> <op1>, <type> <op2>
                                       metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.minimum`’ intrinsic returns the minimum of the two arguments, propagating NaNs and treating -0.0 as less than +0.0.

##### Arguments:

The first two arguments and the return value are floating-point numbers of the same type.

The third argument specifies the exception behavior as described above.

##### Semantics:

This function follows semantics specified in the draft of IEEE 754-2019.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.ceil(<type> <op1>,
                                    metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.ceil`’ intrinsic returns the ceiling of the first argument.

##### Arguments:

The first argument and the return value are floating-point numbers of the same type.

The second argument specifies the exception behavior as described above.

##### Semantics:

This function returns the same values as the libm `ceil` functions would and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.floor(<type> <op1>,
                                     metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.floor`’ intrinsic returns the floor of the first argument.

##### Arguments:

The first argument and the return value are floating-point numbers of the same type.

The second argument specifies the exception behavior as described above.

##### Semantics:

This function returns the same values as the libm `floor` functions would and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.round(<type> <op1>,
                                     metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.round`’ intrinsic returns the first argument rounded to the nearest integer.

##### Arguments:

The first argument and the return value are floating-point numbers of the same type.

The second argument specifies the exception behavior as described above.

##### Semantics:

This function returns the same values as the libm `round` functions would and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.roundeven(<type> <op1>,
                                         metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.roundeven`’ intrinsic returns the first argument rounded to the nearest integer in floating-point format, rounding halfway cases to even (that is, to the nearest value that is an even integer), regardless of the current rounding direction.

##### Arguments:

The first argument and the return value are floating-point numbers of the same type.

The second argument specifies the exception behavior as described above.

##### Semantics:

This function implements IEEE 754 operation `roundToIntegralTiesToEven`. It also behaves in the same way as C standard function `roundeven` and can signal the invalid operation exception for a SNAN argument.

##### Syntax:

```
declare <inttype>
@llvm.experimental.constrained.lround(<fptype> <op1>,
                                      metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.lround`’ intrinsic returns the first argument rounded to the nearest integer with ties away from zero. It will raise an inexact floating-point exception if the argument is not an integer. If the rounded value is too large to fit into the result type, an invalid exception is raised, and the return value is a non-deterministic value (equivalent to *freeze poison*).

##### Arguments:

The first argument is a floating-point number. The return value is an integer type. Not all types are supported on all targets. The supported types are the same as the `llvm.lround` intrinsic and the `lround` libm functions.

The second argument specifies the exception behavior as described above.

##### Semantics:

This function returns the same values as the libm `lround` functions would and handles error conditions in the same way.

##### Syntax:

```
declare <inttype>
@llvm.experimental.constrained.llround(<fptype> <op1>,
                                       metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.llround`’ intrinsic returns the first argument rounded to the nearest integer with ties away from zero. It will raise an inexact floating-point exception if the argument is not an integer. If the rounded value is too large to fit into the result type, an invalid exception is raised, and the return value is a non-deterministic value (equivalent to *freeze poison*).

##### Arguments:

The first argument is a floating-point number. The return value is an integer type. Not all types are supported on all targets. The supported types are the same as the `llvm.llround` intrinsic and the `llround` libm functions.

The second argument specifies the exception behavior as described above.

##### Semantics:

This function returns the same values as the libm `llround` functions would and handles error conditions in the same way.

##### Syntax:

```
declare <type>
@llvm.experimental.constrained.trunc(<type> <op1>,
                                     metadata <exception behavior>)
```

##### Overview:

The ‘`llvm.experimental.constrained.trunc`’ intrinsic returns the first argument rounded to the nearest integer not larger in magnitude than the argument.

##### Arguments:

The first argument and the return value are floating-point numbers of the same type.

The second argument specifies the exception behavior as described above.

##### Semantics:

This function returns the same values as the libm `trunc` functions would and handles error conditions in the same way.

##### Syntax:

```
declare void @llvm.experimental.noalias.scope.decl(metadata !id.scope.list)
```

##### Overview:

The `llvm.experimental.noalias.scope.decl` intrinsic identifies where a noalias scope is declared. When the intrinsic is duplicated, a decision must also be made about the scope: depending on the reason of the duplication, the scope might need to be duplicated as well.

##### Arguments:

The `!id.scope.list` argument is metadata that is a list of `noalias` metadata references. The format is identical to that required for `noalias` metadata. This list must have exactly one element.

##### Semantics:

The `llvm.experimental.noalias.scope.decl` intrinsic identifies where a noalias scope is declared. When the intrinsic is duplicated, a decision must also be made about the scope: depending on the reason of the duplication, the scope might need to be duplicated as well.

For example, when the intrinsic is used inside a loop body, and that loop is unrolled, the associated noalias scope must also be duplicated. Otherwise, the noalias property it signifies would spill across loop iterations, whereas it was only valid within a single iteration.

```llvm
; This example shows two possible positions for noalias.decl and how they impact the semantics:
; If it is outside the loop (Version 1), then %a and %b are noalias across *all* iterations.
; If it is inside the loop (Version 2), then %a and %b are noalias only within *one* iteration.
declare void @decl_in_loop(ptr %a.base, ptr %b.base) {
entry:
  ; call void @llvm.experimental.noalias.scope.decl(metadata !2) ; Version 1: noalias decl outside loop
  br label %loop

loop:
  %a = phi ptr [ %a.base, %entry ], [ %a.inc, %loop ]
  %b = phi ptr [ %b.base, %entry ], [ %b.inc, %loop ]
  ; call void @llvm.experimental.noalias.scope.decl(metadata !2) ; Version 2: noalias decl inside loop
  %val = load i8, ptr %a, !alias.scope !2
  store i8 %val, ptr %b, !noalias !2
  %a.inc = getelementptr inbounds i8, ptr %a, i64 1
  %b.inc = getelementptr inbounds i8, ptr %b, i64 1
  %cond = call i1 @cond()
  br i1 %cond, label %loop, label %exit

exit:
  ret void
}

!0 = !{!0} ; domain
!1 = !{!1, !0} ; scope
!2 = !{!1} ; scope list
```

Multiple calls to *@llvm.experimental.noalias.scope.decl* for the same scope are possible, but one should never dominate another. Violations are pointed out by the verifier as they indicate a problem in either a transformation pass or the input.

These functions read or write floating point environment, such as rounding mode or state of floating point exceptions. Altering the floating point environment requires special care. See Floating Point Environment.

##### Syntax:

```
declare i32 @llvm.get.rounding()
```

##### Overview:

The ‘`llvm.get.rounding`’ intrinsic reads the current rounding mode.

##### Semantics:

The ‘`llvm.get.rounding`’ intrinsic returns the current rounding mode. Encoding of the returned values is same as the result of `FLT_ROUNDS`, specified by C standard:

```
0  - toward zero
1  - to nearest, ties to even
2  - toward positive infinity
3  - toward negative infinity
4  - to nearest, ties away from zero
```

Other values may be used to represent additional rounding modes, supported by a target. These values are target-specific.

##### Syntax:

```
declare void @llvm.set.rounding(i32 <val>)
```

##### Overview:

The ‘`llvm.set.rounding`’ intrinsic sets current rounding mode.

##### Arguments:

The argument is the required rounding mode. Encoding of rounding mode is the same as used by ‘`llvm.get.rounding`’.

##### Semantics:

The ‘`llvm.set.rounding`’ intrinsic sets the current rounding mode. It is similar to C library function ‘fesetround’, however this intrinsic does not return any value and uses platform-independent representation of IEEE rounding modes.

##### Syntax:

```
declare <integer_type> @llvm.get.fpenv()
```

##### Overview:

The ‘`llvm.get.fpenv`’ intrinsic returns bits of the current floating-point environment. The return value type is platform-specific.

##### Semantics:

The ‘`llvm.get.fpenv`’ intrinsic reads the current floating-point environment and returns it as an integer value.

##### Syntax:

```
declare void @llvm.set.fpenv(<integer_type> <val>)
```

##### Overview:

The ‘`llvm.set.fpenv`’ intrinsic sets the current floating-point environment.

##### Arguments:

The argument is an integer representing the new floating-point environment. The integer type is platform-specific.

##### Semantics:

The ‘`llvm.set.fpenv`’ intrinsic sets the current floating-point environment to the state specified by the argument. The state may be previously obtained by a call to ‘`llvm.get.fpenv`’ or synthesized in a platform-dependent way.

##### Syntax:

```
declare void @llvm.reset.fpenv()
```

##### Overview:

The ‘`llvm.reset.fpenv`’ intrinsic sets the default floating-point environment.

##### Semantics:

The ‘`llvm.reset.fpenv`’ intrinsic sets the current floating-point environment to default state. It is similar to the call ‘fesetenv(FE_DFL_ENV)’, except it does not return any value.

##### Syntax:

The ‘`llvm.get.fpmode`’ intrinsic returns bits of the current floating-point control modes. The return value type is platform-specific.

```
declare <integer_type> @llvm.get.fpmode()
```

##### Overview:

The ‘`llvm.get.fpmode`’ intrinsic reads the current dynamic floating-point control modes and returns it as an integer value.

##### Arguments:

None.

##### Semantics:

The ‘`llvm.get.fpmode`’ intrinsic reads the current dynamic floating-point control modes, such as rounding direction, precision, treatment of denormals and so on. It is similar to the C library function ‘fegetmode’, however this function does not store the set of control modes into memory but returns it as an integer value. Interpretation of the bits in this value is target-dependent.

##### Syntax:

The ‘`llvm.set.fpmode`’ intrinsic sets the current floating-point control modes.

```
declare void @llvm.set.fpmode(<integer_type> <val>)
```

##### Overview:

The ‘`llvm.set.fpmode`’ intrinsic sets the current dynamic floating-point control modes.

##### Arguments:

The argument is a set of floating-point control modes, represented as an integer value in a target-dependent way.

##### Semantics:

The ‘`llvm.set.fpmode`’ intrinsic sets the current dynamic floating-point control modes to the state specified by the argument, which must be obtained by a call to ‘`llvm.get.fpmode`’ or constructed in a target-specific way. It is similar to the C library function ‘fesetmode’, however this function does not read the set of control modes from memory but gets it as integer value.

##### Syntax:

```
declare void @llvm.reset.fpmode()
```

##### Overview:

The ‘`llvm.reset.fpmode`’ intrinsic sets the default dynamic floating-point control modes.

##### Arguments:

None.

##### Semantics:

The ‘`llvm.reset.fpmode`’ intrinsic sets the current dynamic floating-point environment to default state. It is similar to the C library function call ‘fesetmode(FE_DFL_MODE)’, however this function does not return any value.

These functions get properties of floating-point values.

##### Syntax:

```
declare i1 @llvm.is.fpclass(<fptype> <op>, i32 <test>)
declare <N x i1> @llvm.is.fpclass(<vector-fptype> <op>, i32 <test>)
```

##### Overview:

The ‘`llvm.is.fpclass`’ intrinsic returns a boolean value or vector of boolean values depending on whether the first argument satisfies the test specified by the second argument.

If the first argument is a floating-point scalar, then the result type is a boolean (i1).

If the first argument is a floating-point vector, then the result type is a vector of boolean with the same number of elements as the first argument.

##### Arguments:

The first argument to the ‘`llvm.is.fpclass`’ intrinsic must be floating-point or vector of floating-point values.

The second argument specifies, which tests to perform. It must be a compile-time integer constant, each bit in which specifies floating-point class:

| Bit # | floating-point class |
|---|---|
| 0 | Signaling NaN |
| 1 | Quiet NaN |
| 2 | Negative infinity |
| 3 | Negative normal |
| 4 | Negative subnormal |
| 5 | Negative zero |
| 6 | Positive zero |
| 7 | Positive subnormal |
| 8 | Positive normal |
| 9 | Positive infinity |

##### Semantics:

The function checks if `op` belongs to any of the floating-point classes specified by `test`. If `op` is a vector, then the check is made element by element. Each check yields an i1 result, which is `true`, if the element value satisfies the specified test. The argument `test` is a bit mask where each bit specifies floating-point class to test. For example, the value 0x108 makes test for normal value, - bits 3 and 8 in it are set, which means that the function returns `true` if `op` is a positive or negative normal value. The function never raises floating-point exceptions. The function does not canonicalize its input value and does not depend on the floating-point environment. If the floating-point environment has a zeroing treatment of subnormal input values (such as indicated by the denormal_fpenv attribute), a subnormal value will be observed (will not be implicitly treated as zero).

This class of intrinsics is designed to be generic and has no specific purpose.

##### Syntax:

```
declare void @llvm.var.annotation(ptr <val>, ptr <str>, ptr <str>, i32  <int>)
```

##### Overview:

The ‘`llvm.var.annotation`’ intrinsic.

##### Arguments:

The first argument is a pointer to a value, the second is a pointer to a global string, the third is a pointer to a global string which is the source file name, and the last argument is the line number.

##### Semantics:

This intrinsic allows annotation of local variables with arbitrary strings. This can be useful for special purpose optimizations that want to look for these annotations. These have no other defined use; they are ignored by code generation and optimization.

##### Syntax:

This is an overloaded intrinsic. You can use ‘`llvm.ptr.annotation`’ on a pointer to an integer of any width. *NOTE* you must specify an address space for the pointer. The identifier for the default address space is the integer ‘`0`’.

```
declare ptr @llvm.ptr.annotation.p0(ptr <val>, ptr <str>, ptr <str>, i32 <int>)
declare ptr @llvm.ptr.annotation.p1(ptr addrspace(1) <val>, ptr <str>, ptr <str>, i32 <int>)
```

##### Overview:

The ‘`llvm.ptr.annotation`’ intrinsic.

##### Arguments:

The first argument is a pointer to an integer value of arbitrary bitwidth (result of some expression), the second is a pointer to a global string, the third is a pointer to a global string which is the source file name, and the last argument is the line number. It returns the value of the first argument.

##### Semantics:

This intrinsic allows annotation of a pointer to an integer with arbitrary strings. This can be useful for special purpose optimizations that want to look for these annotations. These have no other defined use; transformations preserve annotations on a best-effort basis but are allowed to replace the intrinsic with its first argument without breaking semantics and the intrinsic is completely dropped during instruction selection.

##### Syntax:

This is an overloaded intrinsic. You can use ‘`llvm.annotation`’ on any integer bit width.

```
declare i8 @llvm.annotation.i8(i8 <val>, ptr <str>, ptr <str>, i32  <int>)
declare i16 @llvm.annotation.i16(i16 <val>, ptr <str>, ptr <str>, i32  <int>)
declare i32 @llvm.annotation.i32(i32 <val>, ptr <str>, ptr <str>, i32  <int>)
declare i64 @llvm.annotation.i64(i64 <val>, ptr <str>, ptr <str>, i32  <int>)
declare i256 @llvm.annotation.i256(i256 <val>, ptr <str>, ptr <str>, i32  <int>)
```

##### Overview:

The ‘`llvm.annotation`’ intrinsic.

##### Arguments:

The first argument is an integer value (result of some expression), the second is a pointer to a global string, the third is a pointer to a global string which is the source file name, and the last argument is the line number. It returns the value of the first argument.

##### Semantics:

This intrinsic allows annotations to be put on arbitrary expressions with arbitrary strings. This can be useful for special purpose optimizations that want to look for these annotations. These have no other defined use; transformations preserve annotations on a best-effort basis but are allowed to replace the intrinsic with its first argument without breaking semantics and the intrinsic is completely dropped during instruction selection.

##### Syntax:

This annotation emits a label at its program point and an associated `S_ANNOTATION` codeview record with some additional string metadata. This is used to implement MSVC’s `__annotation` intrinsic. It is marked `noduplicate`, so calls to this intrinsic prevent inlining and should be considered expensive.

```
declare void @llvm.codeview.annotation(metadata)
```

##### Arguments:

The argument should be an MDTuple containing any number of MDStrings.

##### Syntax:

```
declare void @llvm.trap() cold noreturn nounwind
```

##### Overview:

The ‘`llvm.trap`’ intrinsic.

##### Arguments:

None.

##### Semantics:

This intrinsic is lowered to the target-dependent trap instruction. If the target does not have a trap instruction, this intrinsic will be lowered to a call of the `abort()` function.

##### Syntax:

```
declare void @llvm.debugtrap() nounwind
```

##### Overview:

The ‘`llvm.debugtrap`’ intrinsic.

##### Arguments:

None.

##### Semantics:

This intrinsic is lowered to code which is intended to cause an execution trap with the intention of requesting the attention of a debugger.

##### Syntax:

```
declare void @llvm.ubsantrap(i8 immarg) cold noreturn nounwind
```

##### Overview:

The ‘`llvm.ubsantrap`’ intrinsic.

##### Arguments:

An integer describing the kind of failure detected.

##### Semantics:

This intrinsic is lowered to code which is intended to cause an execution trap, embedding the argument into encoding of that trap somehow to discriminate crashes if possible.

Equivalent to `@llvm.trap` for targets that do not support this behavior.

##### Syntax:

```
declare void @llvm.stackprotector(ptr <guard>, ptr <slot>)
```

##### Overview:

The `llvm.stackprotector` intrinsic takes the `guard` and stores it onto the stack at `slot`. The stack slot is adjusted to ensure that it is placed on the stack before local variables.

##### Arguments:

The `llvm.stackprotector` intrinsic requires two pointer arguments. The first argument is the value loaded from the stack guard `@__stack_chk_guard`. The second variable is an `alloca` that has enough space to hold the value of the guard.

##### Semantics:

This intrinsic causes the prologue/epilogue inserter to force the position of the `AllocaInst` stack slot to be before local variables on the stack. This is to ensure that if a local variable on the stack is overwritten, it will destroy the value of the guard. When the function exits, the guard on the stack is checked against the original guard by `llvm.stackprotectorcheck`. If they are different, then `llvm.stackprotectorcheck` causes the program to abort by calling the `__stack_chk_fail()` function.

##### Syntax:

```
declare ptr @llvm.stackguard()
```

##### Overview:

The `llvm.stackguard` intrinsic returns the system stack guard value.

It should not be generated by frontends, since it is only for internal usage. The reason why we create this intrinsic is that we still support IR form Stack Protector in FastISel.

##### Arguments:

None.

##### Semantics:

On some platforms, the value returned by this intrinsic remains unchanged between loads in the same thread. On other platforms, it returns the same global variable value, if any, e.g., `@__stack_chk_guard`.

Currently some platforms have IR-level customized stack guard loading (e.g. X86 Linux) that is not handled by `llvm.stackguard()`, while they should be in the future.

##### Syntax:

```
declare i32 @llvm.objectsize.i32(ptr <object>, i1 <min>, i1 <nullunknown>, i1 <dynamic>)
declare i64 @llvm.objectsize.i64(ptr <object>, i1 <min>, i1 <nullunknown>, i1 <dynamic>)
```

##### Overview:

The `llvm.objectsize` intrinsic is designed to provide information to the optimizer to determine whether a) an operation (like memcpy) will overflow a buffer that corresponds to an object, or b) that a runtime check for overflow isn’t necessary. An object in this context means an allocation of a specific class, structure, array, or other object.

##### Arguments:

The `llvm.objectsize` intrinsic takes four arguments. The first argument is a pointer to or into the `object`.

The second argument determines whether `llvm.objectsize` returns the minimum (if true) or maximum (if false) object size. The minimum size may be any size smaller than or equal to the actual object size (including 0 if unknown). The maximum size may be any size greater than or equal to the actual object size (including -1 if unknown).

The third argument controls how `llvm.objectsize` acts when `null` in address space 0 is used as its pointer argument. If it’s `false`, `llvm.objectsize` reports 0 bytes available when given `null`. Otherwise, if the `null` is in a non-zero address space or if `true` is given for the third argument of `llvm.objectsize`, we assume its size is unknown. The fourth argument to `llvm.objectsize` determines if the value should be evaluated at runtime.

The second, third, and fourth arguments only accept constants.

##### Semantics:

The `llvm.objectsize` intrinsic is lowered to a value representing the size of the object concerned. If the size cannot be determined, `llvm.objectsize` returns `i32/i64 -1 or 0` (depending on the `min` argument).

##### Syntax:

This is an overloaded intrinsic. You can use `llvm.expect` on any integer bit width.

```
declare i1 @llvm.expect.i1(i1 <val>, i1 <expected_val>)
declare i32 @llvm.expect.i32(i32 <val>, i32 <expected_val>)
declare i64 @llvm.expect.i64(i64 <val>, i64 <expected_val>)
```

##### Overview:

The `llvm.expect` intrinsic provides information about expected (the most probable) value of `val`, which can be used by optimizers.

##### Arguments:

The `llvm.expect` intrinsic takes two arguments. The first argument is a value. The second argument is an expected value.

##### Semantics:

This intrinsic is lowered to the `val`.

##### Syntax:

This intrinsic is similar to `llvm.expect`. This is an overloaded intrinsic. You can use `llvm.expect.with.probability` on any integer bit width.

```
declare i1 @llvm.expect.with.probability.i1(i1 <val>, i1 <expected_val>, double <prob>)
declare i32 @llvm.expect.with.probability.i32(i32 <val>, i32 <expected_val>, double <prob>)
declare i64 @llvm.expect.with.probability.i64(i64 <val>, i64 <expected_val>, double <prob>)
```

##### Overview:

The `llvm.expect.with.probability` intrinsic provides information about expected value of `val` with probability(or confidence) `prob`, which can be used by optimizers.

##### Arguments:

The `llvm.expect.with.probability` intrinsic takes three arguments. The first argument is a value. The second argument is an expected value. The third argument is a probability.

##### Semantics:

This intrinsic is lowered to the `val`.

##### Syntax:

```
declare void @llvm.assume(i1 %cond)
```

##### Overview:

The `llvm.assume` allows the optimizer to assume that the provided condition is true. This information can then be used in simplifying other parts of the code.

More complex assumptions can be encoded as assume operand bundles.

##### Arguments:

The argument of the call is the condition which the optimizer may assume is always true.

##### Semantics:

The intrinsic allows the optimizer to assume that the provided condition is always true whenever the control flow reaches the intrinsic call. No code is generated for this intrinsic, and instructions that contribute only to the provided condition are not used for code generation. If the condition is violated during execution, the behavior is undefined.

Note that the optimizer might limit the transformations performed on values used by the `llvm.assume` intrinsic in order to preserve the instructions only used to form the intrinsic’s input argument. This might prove undesirable if the extra information provided by the `llvm.assume` intrinsic does not cause sufficient overall improvement in code quality. For this reason, `llvm.assume` should not be used to document basic mathematical invariants that the optimizer can otherwise deduce or facts that are of little use to the optimizer.

##### Syntax:

```
declare type @llvm.ssa.copy(type returned %operand) memory(none)
```

##### Arguments:

The first argument is an operand which is used as the returned value.

##### Overview:

The `llvm.ssa.copy` intrinsic can be used to attach information to operations by copying them and giving them new names. For example, the PredicateInfo utility uses it to build Extended SSA form, and attach various forms of information to operands that dominate specific uses. It is not meant for general use, only for building temporary renaming forms that require value splits at certain points.

##### Syntax:

```
declare i1 @llvm.type.test(ptr %ptr, metadata %type) nounwind memory(none)
```

##### Arguments:

The first argument is a pointer to be tested. The second argument is a metadata object representing a type identifier.

##### Overview:

The `llvm.type.test` intrinsic tests whether the given pointer is associated with the given type identifier.

##### Syntax:

```
declare {ptr, i1} @llvm.type.checked.load(ptr %ptr, i32 %offset, metadata %type) nounwind memory(argmem: read)
```

##### Arguments:

The first argument is a pointer from which to load a function pointer. The second argument is the byte offset from which to load the function pointer. The third argument is a metadata object representing a type identifier.

##### Overview:

The `llvm.type.checked.load` intrinsic safely loads a function pointer from a virtual table pointer using type metadata. This intrinsic is used to implement control flow integrity in conjunction with virtual call optimization. The virtual call optimization pass will optimize away `llvm.type.checked.load` intrinsics associated with devirtualized calls, thereby removing the type check in cases where it is not needed to enforce the control flow integrity constraint.

If the given pointer is associated with a type metadata identifier, this function returns true as the second element of its return value. (Note that the function may also return true if the given pointer is not associated with a type metadata identifier.) If the function’s return value’s second element is true, the following rules apply to the first element:

- If the given pointer is associated with the given type metadata identifier, it is the function pointer loaded from the given byte offset from the given pointer.
- If the given pointer is not associated with the given type metadata identifier, it is one of the following (the choice of which is unspecified):
  1. The function pointer that would have been loaded from an arbitrarily chosen (through an unspecified mechanism) pointer associated with the type metadata.
  2. If the function has a non-void return type, a pointer to a function that returns an unspecified value without causing side effects.

If the function’s return value’s second element is false, the value of the first element is undefined.

##### Syntax:
