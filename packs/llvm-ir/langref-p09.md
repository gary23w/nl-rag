---
title: "LLVM Language Reference Manual (part 9/20)"
source: https://llvm.org/docs/LangRef.html
domain: llvm-ir
license: CC-BY-SA-4.0
tags: llvm ir, llvm intermediate representation, static single assignment, three-address code
fetched: 2026-07-02
part: 9/20
---

# LLVM Language Reference Manual

If the `samesign` keyword is present and the operands are not of the same sign then the result is a poison value.

##### Example:

```
<result> = icmp eq i32 4, 5          ; yields: result=false
<result> = icmp ne ptr %X, %X        ; yields: result=false
<result> = icmp ult i16  4, 5        ; yields: result=true
<result> = icmp sgt i16  4, 5        ; yields: result=false
<result> = icmp ule i16 -4, 5        ; yields: result=false
<result> = icmp sge i16  4, 5        ; yields: result=false
```

##### Syntax:

```
<result> = fcmp [fast-math flags]* <cond> <ty> <op1>, <op2>     ; yields i1 or <N x i1>:result
```

##### Overview:

The ‘`fcmp`’ instruction returns a boolean value or vector of boolean values based on comparison of its operands.

If the operands are floating-point scalars, then the result type is a boolean (i1).

If the operands are floating-point vectors, then the result type is a vector of boolean with the same number of elements as the operands being compared.

##### Arguments:

The ‘`fcmp`’ instruction takes three operands. The first operand is the condition code indicating the kind of comparison to perform. It is not a value, just a keyword. The possible condition codes are:

1. `false`: no comparison, always returns false
2. `oeq`: ordered and equal
3. `ogt`: ordered and greater than
4. `oge`: ordered and greater than or equal
5. `olt`: ordered and less than
6. `ole`: ordered and less than or equal
7. `one`: ordered and not equal
8. `ord`: ordered (no nans)
9. `ueq`: unordered or equal
10. `ugt`: unordered or greater than
11. `uge`: unordered or greater than or equal
12. `ult`: unordered or less than
13. `ule`: unordered or less than or equal
14. `une`: unordered or not equal
15. `uno`: unordered (either nans)
16. `true`: no comparison, always returns true

*Ordered* means that neither operand is a QNAN while *unordered* means that either operand may be a QNAN.

Each of `val1` and `val2` arguments must be either a floating-point type or a vector of floating-point type. They must have identical types.

##### Semantics:

The ‘`fcmp`’ instruction compares `op1` and `op2` according to the condition code given as `cond`. If the operands are vectors, then the vectors are compared element by element. Each comparison performed always yields an i1 result, as follows:

1. `false`: always yields `false`, regardless of operands.
2. `oeq`: yields `true` if both operands are not a QNAN and `op1` is equal to `op2`.
3. `ogt`: yields `true` if both operands are not a QNAN and `op1` is greater than `op2`.
4. `oge`: yields `true` if both operands are not a QNAN and `op1` is greater than or equal to `op2`.
5. `olt`: yields `true` if both operands are not a QNAN and `op1` is less than `op2`.
6. `ole`: yields `true` if both operands are not a QNAN and `op1` is less than or equal to `op2`.
7. `one`: yields `true` if both operands are not a QNAN and `op1` is not equal to `op2`.
8. `ord`: yields `true` if both operands are not a QNAN.
9. `ueq`: yields `true` if either operand is a QNAN or `op1` is equal to `op2`.
10. `ugt`: yields `true` if either operand is a QNAN or `op1` is greater than `op2`.
11. `uge`: yields `true` if either operand is a QNAN or `op1` is greater than or equal to `op2`.
12. `ult`: yields `true` if either operand is a QNAN or `op1` is less than `op2`.
13. `ule`: yields `true` if either operand is a QNAN or `op1` is less than or equal to `op2`.
14. `une`: yields `true` if either operand is a QNAN or `op1` is not equal to `op2`.
15. `uno`: yields `true` if either operand is a QNAN.
16. `true`: always yields `true`, regardless of operands.

The `fcmp` instruction can also optionally take any number of fast-math flags, which are optimization hints to enable otherwise unsafe floating-point optimizations.

Any set of fast-math flags are legal on an `fcmp` instruction, but the only flags that have any effect on its semantics are those that allow assumptions to be made about the values of input arguments; namely `nnan`, `ninf`, and `reassoc`. See Fast-Math Flags for more information.

##### Example:

```
<result> = fcmp oeq float 4.0, 5.0    ; yields: result=false
<result> = fcmp one float 4.0, 5.0    ; yields: result=true
<result> = fcmp olt float 4.0, 5.0    ; yields: result=true
<result> = fcmp ueq double 1.0, 2.0   ; yields: result=false
```

##### Syntax:

```
<result> = phi [fast-math-flags] <ty> [ <val0>, <label0>], ...
```

##### Overview:

The ‘`phi`’ instruction is used to implement the φ node in the SSA graph representing the function.

##### Arguments:

The type of the incoming values is specified with the first type field. After this, the ‘`phi`’ instruction takes a list of pairs as arguments, with one pair for each predecessor basic block of the current block. Only values of first class type may be used as the value arguments to the PHI node. Only labels may be used as the label arguments.

There must be no non-phi instructions between the start of a basic block and the PHI instructions: i.e., PHI instructions must be first in a basic block.

For the purposes of the SSA form, the use of each incoming value is deemed to occur on the edge from the corresponding predecessor block to the current block (but after any definition of an ‘`invoke`’ instruction’s return value on the same edge).

The optional `fast-math-flags` marker indicates that the phi has one or more fast-math-flags. These are optimization hints to enable otherwise unsafe floating-point optimizations. Fast-math-flags are only valid for phis that return supported floating-point types.

##### Semantics:

At runtime, the ‘`phi`’ instruction logically takes on the value specified by the pair corresponding to the predecessor basic block that executed just prior to the current block.

##### Example:

```llvm
Loop:       ; Infinite loop that counts from 0 on up...
  %indvar = phi i32 [ 0, %LoopHeader ], [ %nextindvar, %Loop ]
  %nextindvar = add i32 %indvar, 1
  br label %Loop
```

##### Syntax:

```
<result> = select [fast-math flags] selty <cond>, <ty> <val1>, <ty> <val2>             ; yields ty

selty is either i1 or {<N x i1>}
```

##### Overview:

The ‘`select`’ instruction is used to choose one value based on a condition, without IR-level branching.

##### Arguments:

The ‘`select`’ instruction requires an ‘i1’ value or a vector of ‘i1’ values indicating the condition, and two values of the same first class type.

1. The optional `fast-math flags` marker indicates that the select has one or more fast-math flags. These are optimization hints to enable otherwise unsafe floating-point optimizations. Fast-math flags are only valid for selects that return supported floating-point types. Note that the presence of value which would otherwise result in poison does not cause the result to be poison if the value is on the non-selected arm. If fast-math flags are present, they are only applied to the result, not both arms.

##### Semantics:

If the condition is an i1 and it evaluates to 1, the instruction returns the first value argument; otherwise, it returns the second value argument.

If the condition is a vector of i1, then the value arguments must be vectors of the same size, and the selection is done element by element.

If the condition is an i1 and the value arguments are vectors of the same size, then an entire vector is selected.

##### Example:

```llvm
%X = select i1 true, i8 17, i8 42                   ; yields i8:17
%Y = select nnan i1 true, float 0.0, float NaN      ; yields float:0.0
%Z = select nnan i1 false, float 0.0, float NaN     ; yields float:poison
```

##### Syntax:

```
<result> = freeze ty <val>    ; yields ty:result
```

##### Overview:

The ‘`freeze`’ instruction is used to stop propagation of undef and poison values.

##### Arguments:

The ‘`freeze`’ instruction takes a single argument.

##### Semantics:

If the argument is `undef` or `poison`, ‘`freeze`’ returns an arbitrary, but fixed, value of type ‘`ty`’. Otherwise, this instruction is a no-op and returns the input argument. All uses of a value returned by the same ‘`freeze`’ instruction are guaranteed to always observe the same value, while different ‘`freeze`’ instructions may yield different values.

While `undef` and `poison` pointers can be frozen, the result is a non-dereferenceable pointer. See the Pointer Aliasing Rules section for more information. Values of the byte type are frozen on a per-bit basis. If an aggregate value or vector is frozen, the operand is frozen element-wise. The padding of an aggregate isn’t considered, since it isn’t visible without storing it into memory and loading it with a different type.

##### Example:

```
%w = i32 undef
%x = freeze i32 %w
%y = add i32 %w, %w         ; undef
%z = add i32 %x, %x         ; even number because all uses of %x observe
                            ; the same value
%x2 = freeze i32 %w
%cmp = icmp eq i32 %x, %x2  ; can be true or false

; example with vectors
%v = <2 x i32> <i32 undef, i32 poison>
%a = extractelement <2 x i32> %v, i32 0    ; undef
%b = extractelement <2 x i32> %v, i32 1    ; poison
%add = add i32 %a, %a                      ; undef

%v.fr = freeze <2 x i32> %v                ; element-wise freeze
%d = extractelement <2 x i32> %v.fr, i32 0 ; not undef
%add.f = add i32 %d, %d                    ; even number

%l = load b32, ptr %p                      ; may be uninitialized
%f = freeze b32 %l                         ; freezes on a per-bit basis

; branching on frozen value
%poison = add nsw i1 %k, undef   ; poison
%c = freeze i1 %poison
br i1 %c, label %foo, label %bar ; non-deterministic branch to %foo or %bar
```

##### Syntax:

```
<result> = [tail | musttail | notail ] call [fast-math flags] [cconv] [ret attrs] [addrspace(<num>)]
           <ty>|<fnty> <fnptrval>(<function args>) [fn attrs] [ operand bundles ]
```

##### Overview:

The ‘`call`’ instruction represents a simple function call.

##### Arguments:

This instruction requires several arguments:

1. The optional `tail` and `musttail` markers indicate that the optimizers should perform tail call optimization. The `tail` marker is a hint that can be ignored. The `musttail` marker means that the call must be tail call optimized in order for the program to be correct. This is true even in the presence of attributes like “disable-tail-calls”. The `musttail` marker provides these guarantees: Both markers imply that the callee does not access allocas, va_args, or byval arguments from the caller. As an exception to that, an alloca or byval argument may be passed to the callee as a byval argument, which can be dereferenced inside the callee. For example: declare void @take_byval(ptr byval(i64)) declare void @take_ptr(ptr) ; Invalid (assuming @take_ptr dereferences the pointer), because %local ; may be de-allocated before the call to @take_ptr. define void @invalid_alloca() { entry: %local = alloca i64 tail call void @take_ptr(ptr %local) ret void } ; Valid, the byval attribute causes the memory allocated by %local to be ; copied into @take_byval's stack frame. define void @byval_alloca() { entry: %local = alloca i64 tail call void @take_byval(ptr byval(i64) %local) ret void } ; Invalid, because @use_global_va_list uses the variadic arguments from ; @invalid_va_list. %struct.va_list = type { ptr } @va_list = external global %struct.va_list define void @use_global_va_list() { entry: %arg = va_arg ptr @va_list, i64 ret void } define void @invalid_va_list(i32 %a, ...) { entry: call void @llvm.va_start.p0(ptr @va_list) tail call void @use_global_va_list() ret void } ; Valid, byval argument forwarded to tail call as another byval argument. define void @forward_byval(ptr byval(i64) %x) { entry: tail call void @take_byval(ptr byval(i64) %x) ret void } ; Invalid (assuming @take_ptr dereferences the pointer), byval argument ; passed to tail callee as non-byval ptr. define void @invalid_byval(ptr byval(i64) %x) { entry: tail call void @take_ptr(ptr %x) ret void } Calls marked `musttail` must obey the following additional rules: In addition, if the calling convention is not *swifttailcc* or *tailcc*: On the other hand, if the calling convention is *swifttailcc* or *tailcc*: Tail call optimization for calls marked `tail` is guaranteed to occur if the following conditions are met:
  - The call will not cause unbounded stack growth if it is part of a recursive cycle in the call graph.
  - Arguments with the inalloca or preallocated attribute are forwarded in place.
  - If the musttail call appears in a function with the `"thunk"` attribute and the caller and callee both have varargs, then any unprototyped arguments in register or memory are forwarded to the callee. Similarly, the return value of the callee is returned to the caller’s caller, even if a void return type is in use.
  - The call must immediately precede a ret instruction, or a pointer bitcast followed by a ret instruction.
  - The ret instruction must return the (possibly bitcasted) value produced by the call, undef, or void.
  - The calling conventions of the caller and callee must match.
  - The callee must be varargs iff the caller is varargs. Bitcasting a non-varargs function to the appropriate varargs type is legal so long as the non-varargs prefixes obey the other rules.
  - The return type must not undergo automatic conversion to an *sret* pointer.
  - All ABI-impacting function attributes, such as sret, byval, inreg, returned, and inalloca, must match.
  - The caller and callee prototypes must match. Pointer types of parameters or return types do not differ in address space.
  - Only these ABI-impacting attributes attributes are allowed: sret, byval, swiftself, and swiftasync.
  - Prototypes are not required to match.
  - Caller and callee both have the calling convention `fastcc` or `tailcc`.
  - The call is in tail position (ret immediately follows call and ret uses value of call or is void).
  - Option `-tailcallopt` is enabled, `llvm::GuaranteedTailCallOpt` is `true`, or the calling convention is `tailcc`.
  - Platform-specific constraints are met.
2. The optional `notail` marker indicates that the optimizers should not add `tail` or `musttail` markers to the call. It is used to prevent tail call optimization from being performed on the call.
3. The optional `fast-math flags` marker indicates that the call has one or more fast-math flags, which are optimization hints to enable otherwise unsafe floating-point optimizations. Fast-math flags are only valid for calls that return supported floating-point types.
4. The optional “cconv” marker indicates which calling convention the call should use. If none is specified, the call defaults to using C calling conventions. The calling convention of the call must match the calling convention of the target function, or else the behavior is undefined.
5. The optional Parameter Attributes list for return values. Only ‘`zeroext`’, ‘`signext`’, ‘`noext`’, and ‘`inreg`’ attributes are valid here.
6. The optional addrspace attribute can be used to indicate the address space of the called function. If it is not specified, the program address space from the datalayout string will be used.
7. ‘`ty`’: the type of the call instruction itself which is also the type of the return value. Functions that return no value are marked `void`. The signature is computed based on the return type and argument types.
8. ‘`fnty`’: shall be the signature of the function being called. The argument types must match the types implied by this signature. This is only required if the signature specifies a varargs type.
9. ‘`fnptrval`’: An LLVM value containing a pointer to a function to be called. In most cases, this is a direct function call, but indirect `call`’s are just as possible, calling an arbitrary pointer to function value.
10. ‘`function args`’: argument list whose types match the function signature argument types and parameter attributes. All arguments must be of first class type. If the function signature indicates the function accepts a variable number of arguments, the extra arguments can be specified.
11. The optional function attributes list.
12. The optional operand bundles list.

##### Semantics:

The ‘`call`’ instruction is used to cause control flow to transfer to a specified function, with its incoming arguments bound to the specified values. Upon a ‘`ret`’ instruction in the called function, control flow continues with the instruction after the function call, and the return value of the function is bound to the result argument.

If the callee refers to an intrinsic function, the signature of the call must match the signature of the callee. Otherwise, if the signature of the call does not match the signature of the called function, the behavior is target-specific. For a significant mismatch, this likely results in undefined behavior. LLVM interprocedural optimizations generally only optimize calls where the signature of the caller matches the signature of the callee.

Note that it is possible for the signatures to mismatch even if a call appears to be a “direct” call, like `call void @f()`.

##### Example:

```llvm
%retval = call i32 @test(i32 %argc)
call i32 (ptr, ...) @printf(ptr %msg, i32 12, i8 42)        ; yields i32
%X = tail call i32 @foo()                                    ; yields i32
%Y = tail call fastcc i32 @foo()  ; yields i32
call void %foo(i8 signext 97)

%struct.A = type { i32, i8 }
%r = call %struct.A @foo()                        ; yields { i32, i8 }
%gr = extractvalue %struct.A %r, 0                ; yields i32
%gr1 = extractvalue %struct.A %r, 1               ; yields i8
%Z = call void @foo() noreturn                    ; indicates that %foo never returns normally
%ZZ = call zeroext i32 @bar()                     ; Return value is %zero extended
```

llvm treats calls to some functions with names and arguments that match the standard C99 library as being the C99 library functions, and may perform optimizations or generate code for them under that assumption. This implies that undefined behavior in C standard library functions recognized by LLVM is also undefined behavior at the IR level.

##### Syntax:

```
<resultval> = va_arg <va_list*> <arglist>, <argty>
```

##### Overview:

The ‘`va_arg`’ instruction is used to access arguments passed through the “variable argument” area of a function call. It is used to implement the `va_arg` macro in C.

##### Arguments:

This instruction takes a `va_list*` value and the type of the argument. It returns a value of the specified argument type and increments the `va_list` to point to the next argument. The actual type of `va_list` is target specific.

##### Semantics:

The ‘`va_arg`’ instruction loads an argument of the specified type from the specified `va_list` and causes the `va_list` to point to the next argument. For more information, see the variable argument handling Intrinsic Functions.

It is legal for this instruction to be called in a function which does not take a variable number of arguments, for example, the `vfprintf` function.

`va_arg` is an LLVM instruction instead of an intrinsic function because it takes a type as an argument.

##### Example:

See the variable argument processing section.

Note that the code generator does not yet fully support va_arg on many targets. Also, it does not currently support va_arg with aggregate types on any target.

##### Syntax:

```
<resultval> = landingpad <resultty> <clause>+
<resultval> = landingpad <resultty> cleanup <clause>*

<clause> := catch <type> <value>
<clause> := filter <array constant type> <array constant>
```

##### Overview:

The ‘`landingpad`’ instruction is used by LLVM’s exception handling system to specify that a basic block is a landing pad — one where the exception lands, and corresponds to the code found in the `catch` portion of a `try`/`catch` sequence. It defines values supplied by the personality function upon re-entry to the function. The `resultval` has the type `resultty`.

##### Arguments:

The optional `cleanup` flag indicates that the landing pad block is a cleanup.

A `clause` begins with the clause type — `catch` or `filter` — and contains the global variable representing the “type” that may be caught or filtered respectively. Unlike the `catch` clause, the `filter` clause takes an array constant as its argument. Use “`[0 x ptr] undef`” for a filter which cannot throw. The ‘`landingpad`’ instruction must contain *at least* one `clause` or the `cleanup` flag.

##### Semantics:

The ‘`landingpad`’ instruction defines the values which are set by the personality function upon re-entry to the function, and therefore the “result type” of the `landingpad` instruction. As with calling conventions, how the personality function results are represented in LLVM IR is target specific.

The clauses are applied in order from top to bottom. If two `landingpad` instructions are merged together through inlining, the clauses from the calling function are appended to the list of clauses. When the call stack is being unwound due to an exception being thrown, the exception is compared against each `clause` in turn. If it doesn’t match any of the clauses, and the `cleanup` flag is not set, then unwinding continues further up the call stack.

The `landingpad` instruction has several restrictions:

- A landing pad block is a basic block which is the unwind destination of an ‘`invoke`’ instruction.
- A landing pad block must have a ‘`landingpad`’ instruction as its first non-PHI instruction.
- There can be only one ‘`landingpad`’ instruction within the landing pad block.
- A basic block that is not a landing pad block may not include a ‘`landingpad`’ instruction.

##### Example:

```llvm
;; A landing pad which can catch an integer.
%res = landingpad { ptr, i32 }
         catch ptr @_ZTIi
;; A landing pad that is a cleanup.
%res = landingpad { ptr, i32 }
         cleanup
;; A landing pad which can catch an integer and can only throw a double.
%res = landingpad { ptr, i32 }
         catch ptr @_ZTIi
         filter [1 x ptr] [ptr @_ZTId]
```

##### Syntax:

```
<resultval> = catchpad within <catchswitch> [<args>*]
```

##### Overview:

The ‘`catchpad`’ instruction is used by LLVM’s exception handling system to specify that a basic block begins a catch handler — one where a personality routine attempts to transfer control to catch an exception.

##### Arguments:

The `catchswitch` operand must always be a token produced by a catchswitch instruction in a predecessor block. This ensures that each `catchpad` has exactly one predecessor block, and it always terminates in a `catchswitch`.

The `args` correspond to whatever information the personality routine requires to determine if this is an appropriate handler for the exception. Each operand must be an alloca or a constant. Control will transfer to the `catchpad` if this is the first appropriate handler for the exception.

The `resultval` has the type token and is used to match the `catchpad` to corresponding catchrets and other nested EH pads.

##### Semantics:

When the call stack is being unwound due to an exception being thrown, the exception is compared against the `args`. If it doesn’t match, control will not reach the `catchpad` instruction. The representation of `args` is entirely target and personality function-specific.

Like the landingpad instruction, the `catchpad` instruction must be the first non-phi of its parent basic block.

The meaning of the tokens produced and consumed by `catchpad` and other “pad” instructions is described in the Windows exception handling documentation.

When a `catchpad` has been “entered” but not yet “exited” (as described in the EH documentation), it is undefined behavior to execute a call or invoke that does not carry an appropriate “funclet” bundle.

##### Example:

```
dispatch:
  %cs = catchswitch within none [label %handler0] unwind to caller
  ;; A catch block which can catch an integer.
handler0:
  %tok = catchpad within %cs [ptr @_ZTIi]
```

##### Syntax:

```
<resultval> = cleanuppad within <parent> [<args>*]
```

##### Overview:

The ‘`cleanuppad`’ instruction is used by LLVM’s exception handling system to specify that a basic block is a cleanup block — one where a personality routine attempts to transfer control to run cleanup actions. The `args` correspond to whatever additional information the personality function requires to execute the cleanup. The `resultval` has the type token and is used to match the `cleanuppad` to corresponding cleanuprets. The `parent` argument is the token of the funclet that contains the `cleanuppad` instruction. If the `cleanuppad` is not inside a funclet, this operand may be the token `none`.

##### Arguments:

The instruction takes a list of arbitrary values which are interpreted by the personality function.

##### Semantics:

When the call stack is being unwound due to an exception being thrown, the personality function transfers control to the `cleanuppad` with the aid of the personality-specific arguments. As with calling conventions, how the personality function results are represented in LLVM IR is target specific.

The `cleanuppad` instruction has several restrictions:

- A cleanup block is a basic block which is the unwind destination of an exceptional instruction.
- A cleanup block must have a ‘`cleanuppad`’ instruction as its first non-PHI instruction.
- There can be only one ‘`cleanuppad`’ instruction within the cleanup block.
- A basic block that is not a cleanup block may not include a ‘`cleanuppad`’ instruction.

When a `cleanuppad` has been “entered” but not yet “exited” (as described in the EH documentation), it is undefined behavior to execute a call or invoke that does not carry an appropriate “funclet” bundle.

##### Example:

```
%tok = cleanuppad within %cs []
```

Debug records appear interleaved with instructions, but are not instructions; they are used only to define debug information, and have no effect on generated code. They are distinguished from instructions by the use of a leading *#* and an extra level of indentation. As an example:

```llvm
%inst1 = op1 %a, %b
  #dbg_value(%inst1, !10, !DIExpression(), !11)
%inst2 = op2 %inst1, %c
```

These debug records replace the prior debug intrinsics. Debug records will be disabled if `--experimental-debuginfo-iterators=false` is passed to LLVM; it is an error for both records and intrinsics to appear in the same module. More information about debug records can be found in the LLVM Source Level Debugging document.

LLVM supports the notion of an “intrinsic function”. These functions have well known names and semantics and are required to follow certain restrictions. Overall, these intrinsics represent an extension mechanism for the LLVM language that does not require changing all of the transformations in LLVM when adding to the language (or the bitcode reader/writer, the parser, etc…).

Intrinsic function names must all start with an “`llvm.`” prefix. This prefix is reserved in LLVM for intrinsic names; thus, function names may not begin with this prefix. Intrinsic functions must always be external functions: you cannot define the body of intrinsic functions. Intrinsic functions may only be used in call or invoke instructions: it is illegal to take the address of an intrinsic function. Additionally, because intrinsic functions are part of the LLVM language, it is required if any are added that they be documented here.

Some intrinsic functions can be overloaded, i.e., the intrinsic represents a family of functions that perform the same operation but on different data types. Because LLVM can represent over 8 million different integer types, overloading is used commonly to allow an intrinsic function to operate on any integer type. One or more of the argument types or the result type can be overloaded to accept any integer type. Argument types may also be defined as exactly matching a previous argument’s type or the result type. This allows an intrinsic function which accepts multiple arguments, but needs all of them to be of the same type, to only be overloaded with respect to a single argument or the result.

Overloaded intrinsics will have the names of its overloaded argument types encoded into its function name, each preceded by a period. Only those types which are overloaded result in a name suffix. Arguments whose type is matched against another type do not. For example, the `llvm.ctpop` function can take an integer of any width and returns an integer of exactly the same integer width. This leads to a family of functions such as `i8 @llvm.ctpop.i8(i8 %val)` and `i29 @llvm.ctpop.i29(i29 %val)`. Only one type, the return type, is overloaded, and only one type suffix is required. Because the argument’s type is matched against the return type, it does not require its own name suffix.

Unnamed types are encoded as `s_s`. Overloaded intrinsics that depend on an unnamed type in one of its overloaded argument types get an additional `.<number>` suffix. This allows differentiating intrinsics with different unnamed types as arguments. (For example: `llvm.ssa.copy.p0s_s.2(%42*)`) The number is tracked in the LLVM module and it ensures unique names in the module. While linking together two modules, it is still possible to get a name clash. In that case one of the names will be changed by getting a new number.

For target developers who are defining intrinsics for back-end code generation, any intrinsic overloads based solely the distinction between integer or floating point types should not be relied upon for correct code generation. In such cases, the recommended approach for target maintainers when defining intrinsics is to create separate integer and FP intrinsics rather than rely on overloading. For example, if different codegen is required for `llvm.target.foo(<4 x i32>)` and `llvm.target.foo(<4 x float>)` then these should be split into different intrinsics.

To learn how to add an intrinsic function, please see the Extending LLVM Guide.

Variable argument support is defined in LLVM with the va_arg instruction and these three intrinsic functions. These functions are related to the similarly named macros defined in the `<stdarg.h>` header file.

All of these functions take as arguments pointers to a target-specific value type “`va_list`”. The LLVM assembly language reference manual does not define what this type is, so all transformations should be prepared to handle these functions regardless of the type used. The intrinsics are overloaded, and can be used for pointers to different address spaces.

The underlying argument list is destroyed when a function returns, so a `va_list` must not outlive the function that created it.

This example shows how the va_arg instruction and the variable argument handling intrinsic functions are used.

```llvm
; This struct is different for every platform. For most platforms,
; it is merely a ptr.
%struct.va_list = type { ptr }

; For Unix x86_64 platforms, va_list is the following struct:
; %struct.va_list = type { i32, i32, ptr, ptr }

define i32 @test(i32 %X, ...) {
  ; Initialize variable argument processing
  %ap = alloca %struct.va_list
  call void @llvm.va_start.p0(ptr %ap)

  ; Read a single integer argument
  %tmp = va_arg ptr %ap, i32

  ; Demonstrate usage of llvm.va_copy and llvm.va_end
  %aq = alloca ptr
  call void @llvm.va_copy.p0(ptr %aq, ptr %ap)
  call void @llvm.va_end.p0(ptr %aq)

  ; Stop processing of arguments.
  call void @llvm.va_end.p0(ptr %ap)
  ret i32 %tmp
}

declare void @llvm.va_start.p0(ptr)
declare void @llvm.va_copy.p0(ptr, ptr)
declare void @llvm.va_end.p0(ptr)
```

##### Syntax:

```
declare void @llvm.va_start.p0(ptr <arglist>)
declare void @llvm.va_start.p5(ptr addrspace(5) <arglist>)
```

##### Overview:

The ‘`llvm.va_start`’ intrinsic initializes `<arglist>` for subsequent use by `va_arg`.

##### Arguments:

The argument is a pointer to a `va_list` element to initialize.

##### Semantics:

The ‘`llvm.va_start`’ intrinsic works just like the `va_start` macro available in C. In a target-dependent way, it initializes the `va_list` element to which the argument points, so that the next call to `va_arg` will produce the first variable argument passed to the function. Unlike the C `va_start` macro, this intrinsic does not need to know the last argument of the function as the compiler can figure that out.

##### Syntax:

```
declare void @llvm.va_end.p0(ptr <arglist>)
declare void @llvm.va_end.p5(ptr addrspace(5) <arglist>)
```

##### Overview:

The ‘`llvm.va_end`’ intrinsic destroys `<arglist>`, which has been initialized previously with `llvm.va_start` or `llvm.va_copy`.

##### Arguments:

The argument is a pointer to a `va_list` to destroy.

##### Semantics:

The ‘`llvm.va_end`’ intrinsic works just like the `va_end` macro available in C. In a target-dependent way, it destroys the `va_list` element to which the argument points. Calls to `llvm.va_end` can be omitted when they are a no-op for the given target. `llvm.va_end` is a no-op for all currently supported targets.

When used, calls to `llvm.va_end` must be matched exactly with calls to llvm.va_start and llvm.va_copy.

##### Syntax:

```
declare void @llvm.va_copy.p0(ptr <destarglist>, ptr <srcarglist>)
declare void @llvm.va_copy.p5(ptr addrspace(5) <destarglist>, ptr addrspace(5) <srcarglist>)
```

##### Overview:

The ‘`llvm.va_copy`’ intrinsic copies the current argument position from the source argument list to the destination argument list.

##### Arguments:

The first argument is a pointer to a `va_list` element to initialize. The second argument is a pointer to a `va_list` element to copy from. The address spaces of the two arguments must match.

##### Semantics:

The ‘`llvm.va_copy`’ intrinsic works just like the `va_copy` macro available in C. In a target-dependent way, it copies the source `va_list` element into the destination `va_list` element. This intrinsic is necessary because the `llvm.va_start` intrinsic may be arbitrarily complex and require, for example, memory allocation.

On targets where `llvm.va_copy` is equivalent to `memcpy`, `memcpy` can be used instead to duplicate a `va_list`. `llvm.va_copy` is equivalent to `memcpy` on all currently supported targets.

LLVM’s support for Accurate Garbage Collection (GC) requires the frontend to generate code containing appropriate intrinsic calls and select an appropriate GC strategy which knows how to lower these intrinsics in a manner which is appropriate for the target collector.

These intrinsics allow identification of GC roots on the stack, as well as garbage collector implementations that require read and write barriers. Frontends for type-safe garbage collected languages should generate these intrinsics to make use of the LLVM garbage collectors. For more details, see Garbage Collection with LLVM.

LLVM provides an second experimental set of intrinsics for describing garbage collection safepoints in compiled code. These intrinsics are an alternative to the `llvm.gcroot` intrinsics, but are compatible with the ones for read and write barriers. The differences in approach are covered in the Garbage Collection with LLVM documentation. The intrinsics themselves are described in Garbage Collection Safepoints in LLVM.

##### Syntax:

```
declare void @llvm.gcroot(ptr %ptrloc, ptr %metadata)
```

##### Overview:

The ‘`llvm.gcroot`’ intrinsic declares the existence of a GC root to the code generator, and allows some metadata to be associated with it.

##### Arguments:

The first argument specifies the address of a stack object that contains the root pointer. The second pointer (which must be either a constant or a global value address) contains the meta-data to be associated with the root.

##### Semantics:

At runtime, a call to this intrinsic stores a null pointer into the “ptrloc” location. At compile-time, the code generator generates information to allow the runtime to find the pointer at GC safe points. The ‘`llvm.gcroot`’ intrinsic may only be used in a function which specifies a GC algorithm.

##### Syntax:

```
declare ptr @llvm.gcread(ptr %ObjPtr, ptr %Ptr)
```

##### Overview:

The ‘`llvm.gcread`’ intrinsic identifies reads of references from heap locations, allowing garbage collector implementations that require read barriers.

##### Arguments:

The second argument is the address to read from, which should be an address allocated from the garbage collector. The first object is a pointer to the start of the referenced object, if needed by the language runtime (otherwise null).

##### Semantics:

The ‘`llvm.gcread`’ intrinsic has the same semantics as a load instruction, but may be replaced with substantially more complex code by the garbage collector runtime, as needed. The ‘`llvm.gcread`’ intrinsic may only be used in a function which specifies a GC algorithm.

##### Syntax:

```
declare void @llvm.gcwrite(ptr %P1, ptr %Obj, ptr %P2)
```

##### Overview:

The ‘`llvm.gcwrite`’ intrinsic identifies writes of references to heap locations, allowing garbage collector implementations that require write barriers (such as generational or reference counting collectors).

##### Arguments:

The first argument is the reference to store, the second is the start of the object to store it to, and the third is the address of the field of Obj to store to. If the runtime does not require a pointer to the object, Obj may be null.

##### Semantics:

The ‘`llvm.gcwrite`’ intrinsic has the same semantics as a store instruction, but may be replaced with substantially more complex code by the garbage collector runtime, as needed. The ‘`llvm.gcwrite`’ intrinsic may only be used in a function which specifies a GC algorithm.

##### Syntax:

```
declare token
  @llvm.experimental.gc.statepoint(i64 <id>, i32 <num patch bytes>,
                 ptr elementtype(func_type) <target>,
                 i64 <#call args>, i64 <flags>,
                 ... (call parameters),
                 i64 0, i64 0)
```

##### Overview:

The statepoint intrinsic represents a call which is parse-able by the runtime.

##### Operands:

The ‘id’ operand is a constant integer that is reported as the ID field in the generated stackmap. LLVM does not interpret this parameter in any way and its meaning is up to the statepoint user to decide. Note that LLVM is free to duplicate code containing statepoint calls, and this may transform IR that had a unique ‘id’ per lexical call to statepoint to IR that does not.

If ‘num patch bytes’ is non-zero then the call instruction corresponding to the statepoint is not emitted and LLVM emits ‘num patch bytes’ bytes of nops in its place. LLVM will emit code to prepare the function arguments and retrieve the function return value in accordance to the calling convention; the former before the nop sequence and the latter after the nop sequence. It is expected that the user will patch over the ‘num patch bytes’ bytes of nops with a calling sequence specific to their runtime before executing the generated machine code. There are no guarantees with respect to the alignment of the nop sequence. Unlike Stack maps and patch points in LLVM statepoints do not have a concept of shadow bytes. Note that semantically the statepoint still represents a call or invoke to ‘target’, and the nop sequence after patching is expected to represent an operation equivalent to a call or invoke to ‘target’.

The ‘target’ operand is the function actually being called. The operand must have an elementtype attribute specifying the function type of the target. The target can be specified as either a symbolic LLVM function, or as an arbitrary Value of pointer type. Note that the function type must match the signature of the callee and the types of the ‘call parameters’ arguments.

The ‘#call args’ operand is the number of arguments to the actual call. It must exactly match the number of arguments passed in the ‘call parameters’ variable-length section.

The ‘flags’ operand is used to specify extra information about the statepoint. This is currently only used to mark certain statepoints as GC transitions. This operand is a 64-bit integer with the following layout, where bit 0 is the least significant bit:

> | Bit # | Usage |
> |---|---|
> | 0 | Set if the statepoint is a GC transition, cleared otherwise. |
> | 1-63 | Reserved for future use; must be cleared. |

The ‘call parameters’ arguments are simply the arguments which need to be passed to the call target. They will be lowered according to the specified calling convention and otherwise handled like a normal call instruction. The number of arguments must exactly match what is specified in ‘# call args’. The types must match the signature of ‘target’.

The ‘call parameter’ attributes must be followed by two ‘i64 0’ constants. These were originally the length prefixes for ‘gc transition parameter’ and ‘deopt parameter’ arguments, but the role of these parameter sets have been entirely replaced with the corresponding operand bundles. In a future revision, these now redundant arguments will be removed.

##### Semantics:

A statepoint is assumed to read and write all memory. As a result, memory operations can not be reordered past a statepoint. It is illegal to mark a statepoint as being either ‘readonly’ or ‘readnone’.

Note that legal IR can not perform any memory operation on a ‘gc pointer’ argument of the statepoint in a location statically reachable from the statepoint. Instead, the explicitly relocated value (from a `gc.relocate`) must be used.

##### Syntax:

```
declare type
  @llvm.experimental.gc.result(token %statepoint_token)
```

##### Overview:

`gc.result` extracts the result of the original call instruction which was replaced by the `gc.statepoint`. The `gc.result` intrinsic is actually a family of three intrinsics due to an implementation limitation. Other than the type of the return value, the semantics are the same.

##### Operands:

The first and only argument is the `gc.statepoint` which starts the safepoint sequence of which this `gc.result` is a part. Despite the typing of this as a generic token, *only* the value defined by a `gc.statepoint` is legal here.

##### Semantics:

The `gc.result` represents the return value of the call target of the `statepoint`. The type of the `gc.result` must exactly match the type of the target. If the call target returns void, there will be no `gc.result`.

A `gc.result` is modeled as a ‘readnone’ pure function. It has no side effects since it is just a projection of the return value of the previous call represented by the `gc.statepoint`.

##### Syntax:

```
declare <pointer type>
  @llvm.experimental.gc.relocate(token %statepoint_token,
                                 i32 %base_offset,
                                 i32 %pointer_offset)
```

##### Overview:

A `gc.relocate` returns the potentially relocated value of a pointer at the safepoint.

##### Operands:

The first argument is the `gc.statepoint` which starts the safepoint sequence of which this `gc.relocation` is a part. Despite the typing of this as a generic token, *only* the value defined by a `gc.statepoint` is legal here.

The second and third arguments are both indices into operands of the corresponding statepoint’s gc-live operand bundle.

The second argument is an index which specifies the allocation for the pointer being relocated. The associated value must be within the object with which the pointer being relocated is associated. The optimizer is free to change *which* interior derived pointer is reported, provided that it does not replace an actual base pointer with another interior derived pointer. Collectors are allowed to rely on the base pointer operand remaining an actual base pointer if so constructed.

The third argument is an index which specify the (potentially) derived pointer being relocated. It is legal for this index to be the same as the second argument if and only if a base pointer is being relocated.

##### Semantics:

The return value of `gc.relocate` is the potentially relocated value of the pointer specified by its arguments. It is unspecified how the value of the returned pointer relates to the argument to the `gc.statepoint` other than that a) it points to the same source language object with the same offset, and b) the ‘based-on’ relationship of the newly relocated pointers is a projection of the unrelocated pointers. In particular, the integer value of the pointer returned is unspecified.

A `gc.relocate` is modeled as a `readnone` pure function. It has no side effects since it is just a way to extract information about work done during the actual call modeled by the `gc.statepoint`.

##### Syntax:

```
declare <pointer type>
  @llvm.experimental.gc.get.pointer.base(
    <pointer type> readnone captures(none) %derived_ptr)
    nounwind willreturn memory(none)
```

##### Overview:

`gc.get.pointer.base` for a derived pointer returns its base pointer.

##### Operands:

The only argument is a pointer which is based on some object with an unknown offset from the base of said object.

##### Semantics:

This intrinsic is used in the abstract machine model for GC to represent the base pointer for an arbitrary derived pointer.

This intrinsic is inlined by the RewriteStatepointsForGC pass by replacing all uses of this callsite with the offset of a derived pointer from its base pointer value. The replacement is done as part of the lowering to the explicit statepoint model.

The return pointer type must be the same as the type of the parameter.

##### Syntax:

```
declare i64
  @llvm.experimental.gc.get.pointer.offset(
    <pointer type> readnone captures(none) %derived_ptr)
    nounwind willreturn memory(none)
```

##### Overview:

`gc.get.pointer.offset` for a derived pointer returns the offset from its base pointer.

##### Operands:

The only argument is a pointer which is based on some object with an unknown offset from the base of said object.

##### Semantics:

This intrinsic is used in the abstract machine model for GC to represent the offset of an arbitrary derived pointer from its base pointer.

This intrinsic is inlined by the RewriteStatepointsForGC pass by replacing all uses of this callsite with the offset of a derived pointer from its base pointer value. The replacement is done as part of the lowering to the explicit statepoint model.

Basically this call calculates difference between the derived pointer and its base pointer (see ‘llvm.experimental.gc.get.pointer.base’ Intrinsic) both ptrtoint casted. But this cast done outside the RewriteStatepointsForGC pass could result in the pointers lost for further lowering from the abstract model to the explicit physical one.

These intrinsics are provided by LLVM to expose special features that may only be implemented with code generator support.

##### Syntax:

```
declare ptr @llvm.returnaddress(i32 <level>)
```

##### Overview:

The ‘`llvm.returnaddress`’ intrinsic attempts to compute a target-specific value indicating the return address of the current function or one of its callers.

##### Arguments:

The argument to this intrinsic indicates which function to return the address for. Zero indicates the calling function, one indicates its caller, etc. The argument is **required** to be a constant integer value.

##### Semantics:
