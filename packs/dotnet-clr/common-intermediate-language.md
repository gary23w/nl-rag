---
title: "Common Intermediate Language"
source: https://en.wikipedia.org/wiki/Common_Intermediate_Language
domain: dotnet-clr
license: CC-BY-SA-4.0
tags: common language runtime, dotnet framework, common intermediate language, managed code
fetched: 2026-07-02
---

# Common Intermediate Language

**Common Intermediate Language** (**CIL**), formerly called **Microsoft Intermediate Language** (**MSIL**) or **Intermediate Language** (**IL**), is the intermediate language binary instruction set defined within the Common Language Infrastructure (CLI) specification. CIL instructions are executed by a CIL-compatible runtime environment such as the Common Language Runtime. Languages which target the CLI compile to CIL. CIL is object-oriented, stack-based bytecode. Runtimes typically just-in-time compile CIL instructions into native code.

CIL was originally known as Microsoft Intermediate Language (MSIL) during the beta releases of the .NET languages. Due to standardization of C# and the CLI, the bytecode is now officially known as CIL. Windows Defender virus definitions continue to refer to binaries compiled with it as MSIL.

## General information

During compilation of CLI programming languages, the source code is translated into CIL code rather than into platform- or processor-specific object code. CIL is a CPU- and platform-independent instruction set that can be executed in any environment supporting the Common Language Infrastructure, such as the .NET runtime on Windows, or the cross-platform Mono runtime. In theory, this eliminates the need to distribute different executable files for different platforms and CPU types. CIL code is verified for safety during runtime, providing better security and reliability than natively compiled executable files.

The execution process looks like this:

1. Source code is converted to CIL bytecode and a CLI assembly is created.
2. Upon execution of a CIL assembly, its code is passed through the runtime's JIT compiler to generate native code. Ahead-of-time compilation may also be used, which eliminates this step, but at the cost of executable-file portability.
3. The computer's processor executes the native code.

## Instructions

CIL bytecode has instructions for the following groups of tasks:

- Load and store
- Arithmetic
- Type conversion
- Object creation and manipulation
- Operand stack management (push / pop)
- Control transfer (branching)
- Method invocation and return
- Throwing exceptions
- Monitor-based concurrency
- Data and function pointers manipulation needed for C++/CLI and unsafe C# code

## Computational model

The Common Intermediate Language is object-oriented and stack-based, which means that instruction parameters and results are kept on a single stack instead of in several registers or other memory locations, as in most programming languages.

Code that adds two numbers in x86 assembly language, where eax and edx specify two different general-purpose registers:

```mw
add eax, edx
```

Code in an intermediate language (IL), where 0 is eax and 1 is edx:

```mw
ldloc.0    // push local variable 0 onto stack
ldloc.1    // push local variable 1 onto stack
add        // pop and add the top two stack items then push the result onto the stack
stloc.0    // pop and store the top stack item to local variable 0
```

In the latter example, the values of the two registers, eax and edx, are first pushed on the stack. When the add-instruction is called the operands are "popped", or retrieved, and the result is "pushed", or stored, on the stack. The resulting value is then popped from the stack and stored in eax.

### Object-oriented concepts

CIL is designed to be object-oriented. One may create objects, call methods, and use other types of members, such as fields.

Every method needs (with some exceptions) to reside in a class. So does this static method:

```mw
.class public Foo {
    .method public static int32 Add(int32, int32) cil managed {
        .maxstack 2
        ldarg.0 // load the first argument;
        ldarg.1 // load the second argument;
        add     // add them;
        ret     // return the result;
    }
}
```

The method Add does not require any instance of Foo to be declared because it is declared as static, and it may then be used like this in C#:

```mw
int r = Foo.Add(2, 3);    // 5
```

In CIL it would look like this:

```mw
ldc.i4.2
ldc.i4.3
call int32 Foo::Add(int32, int32)
stloc.0
```

#### Instance classes

An instance class contains at least one constructor and some instance members. The following class has a set of methods representing actions of a Car-object.

```mw
.class public Car {
    .method public specialname rtspecialname instance void .ctor(int32, int32) cil managed {
        /* Constructor */
    }

    .method public void Move(int32) cil managed { /* Omitting implementation */ }
    .method public void TurnRight() cil managed { /* Omitting implementation */ }
    .method public void TurnLeft() cil managed { /* Omitting implementation */ }
    .method public void Brake() cil managed { /* Omitting implementation */ }
}
```

#### Creating objects

In C# class instances are created like this:

```mw
Car myCar = new Car(1, 4); 
Car yourCar = new Car(1, 3);
```

And those statements are roughly the same as these instructions in CIL:

```mw
ldc.i4.1
ldc.i4.4
newobj instance void Car::.ctor(int32, int32)
stloc.0    // myCar = new Car(1, 4);
ldc.i4.1
ldc.i4.3
newobj instance void Car::.ctor(int32, int32)
stloc.1    // yourCar = new Car(1, 3);
```

#### Invoking instance methods

Instance methods are invoked in C# as the one that follows:

```mw
myCar.Move(3);
```

As invoked in CIL:

```mw
ldloc.0    // Load the object "myCar" on the stack
ldc.i4.3
call instance void Car::Move(int32)
```

The Common Language Infrastructure (CLI) records information about compiled classes as metadata. Like the type library in the Component Object Model, this enables applications to support and discover the interfaces, classes, types, methods, and fields in the assembly. The process of reading such metadata is called "reflection".

Metadata can be data in the form of "attributes". Attributes can be customized by extending the `Attribute` class. This is a powerful feature. It allows the creator of the class the ability to adorn it with extra information that consumers of the class can use in various meaningful ways, depending on the application domain.

## Example

Below is a basic "Hello, World!" program written in CIL assembler. It will display the string "Hello, world!".

```mw
.assembly Hello {}
.assembly extern mscorlib {}
.method static void Main()
{
    .entrypoint
    .maxstack 1
    ldstr "Hello, world!"
    call void [mscorlib]System.Console::WriteLine(string)
    ret
}
```

The following code is more complex in number of opcodes.

*This code can also be compared with the corresponding code in the article about Java bytecode.*

```mw
static void Main(string[] args)
{
    for (int i = 2; i < 1000; i++)
    {
        for (int j = 2; j < i; j++)
        {
             if (i % j == 0)
                 goto outer;
        }
        Console.WriteLine(i);
        outer:;
    }
}
```

In CIL assembler syntax it looks like this:

```mw
.method private hidebysig static void Main(string[] args) cil managed
{
    .entrypoint
    .maxstack  2
    .locals init (int32 V_0,
                  int32 V_1)

              ldc.i4.2
              stloc.0
              br.s       IL_001f
    IL_0004:  ldc.i4.2
              stloc.1
              br.s       IL_0011
    IL_0008:  ldloc.0
              ldloc.1
              rem
              brfalse.s  IL_001b
              ldloc.1
              ldc.i4.1
              add
              stloc.1
    IL_0011:  ldloc.1
              ldloc.0
              blt.s      IL_0008
              ldloc.0
              call       void [mscorlib]System.Console::WriteLine(int32)
    IL_001b:  ldloc.0
              ldc.i4.1
              add
              stloc.0
    IL_001f:  ldloc.0
              ldc.i4     0x3e8
              blt.s      IL_0004
              ret
}
```

This is just a representation of how CIL looks near the virtual machine (VM) level. When compiled the methods are stored in tables and the instructions are stored as bytes inside the assembly, which is a Portable Executable (PE).

## Generation

A CIL assembly and instructions are generated by either a compiler or a utility called the *IL Assembler* (ILAsm) that is shipped with the execution environment.

Assembled CIL can also be disassembled into code again using the *IL Disassembler* (ILDASM). There are other tools such as .NET Reflector that can decompile CIL into a high-level language (e. g. C# or Visual Basic). This makes CIL a very easy target for reverse engineering. This trait is shared with Java bytecode. However, there are tools that can obfuscate the code, and do it so that the code cannot be easily readable but still be runnable.

## Execution

### Just-in-time compilation

Just-in-time compilation (JIT) involves turning the byte-code into code immediately executable by the CPU. The conversion is performed gradually during the program's execution. JIT compilation provides environment-specific optimization and assembly verification. To accomplish this, the JIT compiler examines the assembly metadata for any illegal accesses and handles violations appropriately.

### Ahead-of-time compilation

CLI-compatible execution environments also come with the option to do an Ahead-of-time compilation (AOT) of an assembly to make it execute faster by removing the JIT process at runtime.

In the .NET Framework there is a special tool called the Native Image Generator (NGEN) that performs the AOT. A different approach for AOT is CoreRT that allows the compilation of .Net Core code to a single executable with no dependency on a runtime. Mono also supports AOT compilation.

## Pointer instructions - C++/CLI

A notable difference from Java's bytecode is that CIL comes with `ldind`, `stind`, `ldloca`, and many call instructions which are enough for data/function pointers manipulation needed to compile C/C++ code into CIL.

```mw
class A {
   public: virtual void __stdcall meth() {}
};
void test_pointer_operations(int param) {
	int k = 0;
	int * ptr = &k;
	*ptr = 1;
	ptr = &param;
	*ptr = 2;
	A a;
	A * ptra = &a;
	ptra->meth();
}
```

The corresponding code in CIL can be rendered as this:

```mw
.method assembly static void modopt([mscorlib]System.Runtime.CompilerServices.CallConvCdecl) 
        test_pointer_operations(int32 param) cil managed
{
  .vtentry 1 : 1
  // Code size       44 (0x2c)
  .maxstack  2
  .locals ([0] int32* ptr,
           [1] valuetype A* V_1,
           [2] valuetype A* a,
           [3] int32 k)
// k = 0;
  IL_0000:  ldc.i4.0 
  IL_0001:  stloc.3
// ptr = &k;
  IL_0002:  ldloca.s   k // load local's address instruction
  IL_0004:  stloc.0
// *ptr = 1;
  IL_0005:  ldloc.0
  IL_0006:  ldc.i4.1
  IL_0007:  stind.i4 // indirection instruction
// ptr = &param
  IL_0008:  ldarga.s   param // load parameter's address instruction
  IL_000a:  stloc.0
// *ptr = 2
  IL_000b:  ldloc.0
  IL_000c:  ldc.i4.2
  IL_000d:  stind.i4
// a = new A;
  IL_000e:  ldloca.s   a
  IL_0010:  call       valuetype A* modopt([mscorlib]System.Runtime.CompilerServices.CallConvThiscall) 'A.{ctor}'(valuetype A* modopt([mscorlib]System.Runtime.CompilerServices.IsConst) modopt([mscorlib]System.Runtime.CompilerServices.IsConst))
  IL_0015:  pop
// ptra = &a;
  IL_0016:  ldloca.s   a
  IL_0018:  stloc.1
// ptra->meth();
  IL_0019:  ldloc.1
  IL_001a:  dup
  IL_001b:  ldind.i4 // reading the VMT for virtual call
  IL_001c:  ldind.i4
  IL_001d:  calli      unmanaged stdcall void modopt([mscorlib]System.Runtime.CompilerServices.CallConvStdcall)(native int)
  IL_0022:  ret
} // end of method 'Global Functions'::test_pointer_operations
```
