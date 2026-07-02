---
title: "Pointer (computer programming) (part 2/2)"
source: https://en.wikipedia.org/wiki/Pointer_(computer_programming)
domain: separation-logic
license: CC-BY-SA-4.0
tags: separation logic, separating conjunction, heap assertion, frame rule
fetched: 2026-07-02
part: 2/2
---

## Support in various programming languages

### Ada

Ada is a strongly typed language where all pointers are typed and only safe type conversions are permitted. All pointers are by default initialized to `null`, and any attempt to access data through a `null` pointer causes an exception to be raised. Pointers in Ada are called *access types*. Ada 83 did not permit arithmetic on access types (although many compiler vendors provided for it as a non-standard feature), but Ada 95 supports “safe” arithmetic on access types via the package `System.Storage_Elements`.

### BASIC

Several old versions of BASIC for the Windows platform had support for `STRPTR()` to return the address of a string, and for `VARPTR()` to return the address of a variable. Visual Basic 5 also had support for `OBJPTR()` to return the address of an object interface, and for an ADDRESSOF operator to return the address of a function. The types of all of these are integers, but their values are equivalent to those held by pointer types.

Newer dialects of BASIC, such as FreeBASIC or BlitzMax, have exhaustive pointer implementations, however. In FreeBASIC, arithmetic on ANY pointers (equivalent to C's `void *`) are treated as though the ANY pointer was a byte width. ANY pointers cannot be dereferenced, as in C. Also, casting between ANY and any other type's pointers will not generate any warnings.

```mw
dim as integer f = 257
dim as any ptr g = @f
dim as integer ptr i = g
assert(*i = 257)
assert( (g + 4) = (@f + 1) )
```

### C

In C pointers are variables that store addresses and can be *null*. Each pointer has a type it points to, but one can freely cast between pointer types. However, it is not possible to cast between a function pointer and an object pointer. A special pointer type called the "void pointer" allows pointing to any (non-function) object, but is limited by the fact that it cannot be dereferenced directly. The address itself can often be directly manipulated by casting a pointer to and from an integral type of sufficient size, though the results are undefined; while earlier C standards did not have an integral type that was guaranteed to be large enough, C99 specifies the `uintptr_t` type defined in `<stdint.h>`, but an implementation need not provide it.

**Pointer arithmetic**, that is, the ability to modify a pointer's target address with arithmetic operations (as well as magnitude comparisons), is restricted by the language standard to remain within the bounds of a single array object or just after it, and will otherwise invoke undefined behavior. Adding or subtracting from a pointer moves it by a multiple of the size of its datatype. For example, adding 1 to a pointer to 4-byte integer values will increment the pointer's pointed-to byte-address by 4. This has the effect of incrementing the pointer to point at the next element in a contiguous array of integers—which is often the intended result. Pointer arithmetic cannot be performed on `void` pointers because the void type has no size, and thus the pointed address cannot be added to, although gcc and other compilers will perform byte arithmetic on `void *` as a non-standard extension, treating it as if it were `char *`.

Pointer arithmetic provides the programmer with a single way of dealing with different types: adding and subtracting the number of elements required instead of the actual offset in bytes. In particular, the C standard explicitly declares that the syntax `a[n]`, which is the n-th element of the array `a`, is equivalent to `*(a + n)`, which is the content of the element pointed by `a + n`. This implies that, for example, `a[3]` and `3[a]` both access the fourth element of the array `a`.

While powerful, pointer arithmetic can be a source of computer bugs. It tends to confuse novice programmers, forcing them into different contexts: an expression can be an ordinary arithmetic one or a pointer arithmetic one, and sometimes it is easy to mistake one for the other. In response to this, many modern high-level computer languages do not permit direct access to memory using addresses.

The **`void` pointer**, or **`void *`**, is supported in ANSI C as a generic pointer type. A pointer to `void` can store the address of any object (not function), and, is implicitly converted to any other object pointer type on assignment, but it must be explicitly cast if dereferenced. Before ANSI C, K&R used `char *` for the "type-agnostic pointer" purpose.

```mw
int x = 4;
void *p1 = &x;
int *p2 = p1; // void * implicitly converted to int *
int a = *p2;
int b = *(int *)p1; // when dereferencing inline, there is no implicit conversion
```

### C++

C++ fully supports C pointers and C typecasting. It also supports a new group of typecasting operators to help catch some unintended dangerous casts at compile-time. C++ also supports another form of reference, quite different from a pointer, called simply a *reference* or *reference type*.

Since C++11, the C++ standard library also provides smart pointers, which can be used in some situations as a safer alternative to primitive C pointers.

- `std::unique_ptr` (represents unique ownership of a resource, cannot be copied but can be moved)
- `std::shared_ptr` (represents shared ownership of a resource, resource is only deleted once the last shared pointer is destroyed or reset)
- `std::weak_ptr` (represents no ownership, can point to a shared pointer's resources without incrementing the reference count)
- `std::hazard_pointer` (single-writer multi-reader pointer that may be owned by at most one thread at any point of time)

`std::unique_ptr` replaces the previous smart pointer std::auto_ptr, which was deprecated in C++11 and removed in C++17.

In contrast to C, C++ does not allow the implicit conversion of `void*` to other pointer types, even in assignments. This was a design decision to avoid careless and even unintended casts, though most compilers only output warnings, not errors, when encountering other casts.

```mw
int x = 4;
void* p1 = &x;
int* p2 = p1; // this fails: there is no implicit conversion from void*
int* p3 = reinterpret_cast<int*>(p1); // C++ cast
```

In C++, there is no `void&` (reference to void) to complement `void*` (pointer to void), because references behave like aliases to the variables they point to, and there can never be a variable whose type is `void`.

#### Pointer-to-member

In C++ pointers to non-static members of a class can be defined. If a class `MyClass` has a member `T a` then `&MyClass::a` is a pointer to the member `a` of type `T MyClass::*`. This member can be an object or a function. They can be used on the right-hand side of operators `.*` and `->*` to access the corresponding member.

```mw
struct Integer {
    int value;
    
    [[nodiscard]]
    int get() const noexcept {
        return value;
    }
};

Integer s1; // default-constructed, s1.value = 0
Integer* ps = &s1;

int Integer::* ptr = &Integer::value; // pointer to Integer::value
int (Integer::* fp)() const = &Integer::get; // pointer to Integer::get

s1.*ptr = 1;
std::println("{}", (s1.*fp)()); // prints 1
ps->*ptr = 2;
std::println("{}", (ps->*fp)()); // prints 2
```

The following are declarations involving pointers-to-member:

```mw
class X {
    // ...
};

class Y {
    // ...
};

char X::* a; // pointer-to-member to char
char X::* b[5]; // array of pointers-to-member to char 
char* X::* c; // pointer-to-member to pointer to char(s)
char X::** d; // pointer to pointer-to-member to char 
char (*e)[5]; // pointer-to-member to array(s) of chars 
char X::* f(); // function which returns a pointer-to-member to char
char Y::* X::* g; // pointer-to-member to pointer-to-member to pointer to char(s)
char X::* X::* h; // pointer-to-member to pointer-to-member to pointer to char(s)
char (X::* i())[5]; // function which returns pointer-to-member to an array of chars
char (X::* j)() // pointer-to-member-function which returns a char
char (X::* k[5])(); // an array of pointers-to-member-functions which return a char
```

The `()` and `[]` have a higher priority than `*`.

### C

In the C# programming language, pointers are supported by either marking blocks of code that include pointers with the `unsafe` keyword, or through the `System.Runtime.CompilerServices` namespace for pointer access. The syntax is essentially the same as in C++, and the address pointed can be either managed or unmanaged memory. However, pointers to managed memory (any pointer to a managed object) must be declared using the `fixed` keyword, which prevents the garbage collector from moving the pointed object as part of memory management while the pointer is in scope, thus keeping the pointer address valid.

However, an exception to this is from using the `IntPtr` structure, which is a memory managed equivalent to `int*`, and does not require the `unsafe` keyword nor the `CompilerServices` assembly. This type is often returned when using methods from the `System.Runtime.InteropServices`, for example:

```mw
using System;
using System.Runtime.InteropServices;

// Get 16 bytes of memory from the process's unmanaged memory
IntPtr pointer = Marshal.AllocHGlobal(16);

// Do something with the allocated memory

// Free the allocated memory
Marshal.FreeHGlobal(pointer);
```

The .NET framework includes many classes and methods in the `System` and `System.Runtime.InteropServices` namespaces (such as the `Marshal` class) which convert .NET types (for example, `System.String`) to and from many unmanaged types and pointers (for example, `LPWSTR` or `void*`) to allow communication with unmanaged code. Most such methods have the same security permission requirements as unmanaged code, since they can affect arbitrary places in memory.

C# allows stack-allocated arrays in safe code using `System.Span`.

```mw
namespace Wikipedia.Examples;

using System;

public class Example
{
    static void Main(string[] args)
    {
        int num = 1024;
        unsafe 
        {
            // convert an int into bytes by creating a byte pointer
            byte* p = (byte*)&number;
            Console.Write("The 4 bytes of the integer are: ");
            for (int i = 0; i < sizeof(int); ++i)
            {
                Console.Write(" {0:X2}", *p);
                ++p;
            }
            Console.WriteLine();
        }

        // Stack-allocated arrays can be done either through pointers or Span<T>
        unsafe
        {
            int* numbers = stackalloc int[5];
        }
        Span<int> numbers = stackalloc int[5];
    }
}
```

C#, like C and C++, also has a `void*` (void pointer) type, but it is highly unrecommended.

Unlike C and C++, right-aligned asterisks are not accepted by the compiler. For example:

```mw
int* a, b;
int *a, *b; // illegal in C#
```

In C and C++, this would declare `a` as `int*` and `b` as `int`, but in C# this declares both variables as `int*`.

### COBOL

The COBOL programming language supports pointers to variables. Primitive or group (record) data objects declared within the `LINKAGE SECTION` of a program are inherently pointer-based, where the only memory allocated within the program is space for the address of the data item (typically a single memory word). In program source code, these data items are used just like any other `WORKING-STORAGE` variable, but their contents are implicitly accessed indirectly through their `LINKAGE` pointers.

Memory space for each pointed-to data object is typically allocated dynamically using external `CALL` statements or via embedded extended language constructs such as `EXEC CICS` or `EXEC SQL` statements.

Extended versions of COBOL also provide pointer variables declared with `USAGE` `IS` `POINTER` clauses. The values of such pointer variables are established and modified using `SET` and `SET` `ADDRESS` statements.

Some extended versions of COBOL also provide `PROCEDURE-POINTER` variables, which are capable of storing the addresses of executable code.

### PL/I

The PL/I language provides full support for pointers to all data types (including pointers to structures), recursion, multitasking, string handling, and extensive built-in functions. PL/I was quite a leap forward compared to the programming languages of its time. PL/I pointers are untyped, and therefore no casting is required for pointer dereferencing or assignment. The declaration syntax for a pointer is `DECLARE xxx POINTER;`, which declares a pointer named "xxx". Pointers are used with `BASED` variables. A based variable can be declared with a default locator (`DECLARE xxx BASED(ppp);` or without (`DECLARE xxx BASED;`), where xxx is a based variable, which may be an element variable, a structure, or an array, and ppp is the default pointer). Such a variable can be address without an explicit pointer reference (`xxx=1;`, or may be addressed with an explicit reference to the default locator (ppp), or to any other pointer (`qqq->xxx=1;`).

Pointer arithmetic is not explicitly part of the PL/I standard, but the `UNSPEC` builtin function and pseudo-variable allow pointer arithmetic and many compilers allow expressions of the form `ptr = ptr±expression`. IBM PL/I also has the builtin function `PTRADD` to perform the arithmetic. Pointer arithmetic is always performed in bytes.

IBM *Enterprise* PL/I compilers have a new form of typed pointer called a `HANDLE`.

### D

The D programming language is a derivative of C and C++ which fully supports C pointers and C typecasting. It supports pointer arithmetic, and also has pointer slices. A pointer in D can decay to `void*` implicitly.

In D, it is possible to use `ref` for a reference, which automatically dereferences, disallows pointer arithmetic, and does not allow escaping a function (i.e. through `return`).

A pointer slice can be seen as a pointer with a length.

```mw
import std.stdio;

void main() {
    int[] arr = [10, 20, 30, 40, 50];
    int* ptr = &arr[0];
    int[] slice = ptr[0 .. 3]; // Slice the array from index 0 to 3 (exclusive)
    writeln("Slice: ", slice); // Output: Slice: [10, 20, 30]
}
```

### Eiffel

The Eiffel object-oriented language employs value and reference semantics without pointer arithmetic. Nevertheless, pointer classes are provided. They offer pointer arithmetic, typecasting, explicit memory management, interfacing with non-Eiffel software, and other features.

### Fortran

Fortran-90 introduced a strongly typed pointer capability. Fortran pointers contain more than just a simple memory address. They also encapsulate the lower and upper bounds of array dimensions, strides (for example, to support arbitrary array sections), and other metadata. An *association operator*, `=>` is used to associate a `POINTER` to a variable which has a `TARGET` attribute. The Fortran-90 `ALLOCATE` statement may also be used to associate a pointer to a block of memory. For example, the following code might be used to define and create a linked list structure:

```mw
type real_list_t
  real :: sample_data(100)
  type (real_list_t), pointer :: next => null ()
end type

type (real_list_t), target :: my_real_list
type (real_list_t), pointer :: real_list_temp

real_list_temp => my_real_list
do
  read (1,iostat=ioerr) real_list_temp%sample_data
  if (ioerr /= 0) exit
  allocate (real_list_temp%next)
  real_list_temp => real_list_temp%next
end do
```

Fortran-2003 adds support for procedure pointers. Also, as part of the *C Interoperability* feature, Fortran-2003 supports intrinsic functions for converting C-style pointers into Fortran pointers and back.

### Go

Go has pointers, declared similar to C/C++ pointers but with the asterisk first. For example, a pointer to `T` is written `*T`. Unlike C, Go has garbage collection, and disallows pointer arithmetic. Reference types, like in C++, do not exist. Some built-in types, like maps and channels, are boxed (i.e. internally they are pointers to mutable structures), and are initialized using the `make` function. In an approach to unified syntax between pointers and non-pointers, the arrow (`->`) operator has been dropped: the dot operator on a pointer refers to the field or method of the dereferenced object. This, however, only works with one level of indirection.

### Java

There is no explicit representation of pointers in Java. Instead, more complex data structures like objects and arrays are implemented using references. The language does not provide any explicit pointer manipulation operators. It is still possible for code to attempt to dereference a null reference (null pointer), however, which throws a java.lang.NullPointerException. The space occupied by unreferenced memory objects is recovered automatically by garbage collection at run-time.

Java provides the classes `java.lang.ref.WeakReference` and `java.lang.ref.PhantomReference`, which respectively implement weak references and phantom references.

### Modula-2

Pointers are implemented very much as in Pascal, as are `VAR` parameters in procedure calls. Modula-2 is even more strongly typed than Pascal, with fewer ways to escape the type system. Some of the variants of Modula-2 (such as Modula-3) include garbage collection.

### Oberon

Much as with Modula-2, pointers are available. There are still fewer ways to evade the type system and so Oberon and its variants are still safer with respect to pointers than Modula-2 or its variants. As with Modula-3, garbage collection is a part of the language specification.

### Pascal

Unlike many languages that feature pointers, standard ISO Pascal only allows pointers to reference dynamically created variables that are anonymous and does not allow them to reference standard static or local variables. It does not have pointer arithmetic. Pointers also must have an associated type and a pointer to one type is not compatible with a pointer to another type (e.g. a pointer to a char is not compatible with a pointer to an integer). This helps eliminate the type security issues inherent with other pointer implementations, particularly those used for PL/I or C. It also removes some risks caused by dangling pointers, but the ability to dynamically let go of referenced space by using the `dispose` standard procedure (which has the same effect as the `free` library function found in C) means that the risk of dangling pointers has not been eliminated.

However, in some commercial and open source Pascal (or derivatives) compiler implementations —like Free Pascal, Turbo Pascal or the Object Pascal in Embarcadero Delphi— a pointer is allowed to reference standard static or local variables and can be cast from one pointer type to another. Moreover, pointer arithmetic is unrestricted: adding or subtracting from a pointer moves it by that number of bytes in either direction, but using the `Inc` or `Dec` standard procedures with it moves the pointer by the size of the data type it is *declared* to point to. An untyped pointer is also provided under the name `Pointer`, which is compatible with other pointer types.

#### Pascal pointers

Pointers are declared by use of the dereference operator `^`. When it is used in the definition of a variable, the pointer is a reference to a type, which is either intrinsic (defined by the language compiler) or explicitly declared, either in another unit, in the current unit or the main program.

A pointer declaration looks like this (Pascal is not case sensitive, so types and variables can use upper or lower case):

```mw
Type
   months = (jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec);
   calptr = ^Calendar_Type;
   Calendar_Type = record
       Prev,Next: CalPtr;
       Month: Months;
       day: byte;
       year: integer;
       event: string;
   end;

var
   That: ^integer;
   NextCalendar,
   calendar: ^calptr;

begin
    new(calendar)
    calendar^.prev := nil;
    calendar^.next := nil;
    Calendar^.Month := Sep;
    Calendar^.Day := 11;
    Calendar^.Year := 2001;

    new(that);
    That^ := 1;

    New(nextCalendar);
    nextCalendar^.prev := Calendar;
    nextCalendar^.Next := NIL;
    New(Calendar);
...
    Dispose(that);
    Dispose(calendar);
    Dispose(nextCalendar);
  
end;
```

Line 2 shows the creation of a new type *months* and creates named constants of the months of the year. Line 3 defines a pointer to a record type. Lines 4-10 define that record. Lines 12-15 define the pointer variables; line 13 defines a pointer to a scalar and lines 14-15 create a linked list. Line 18 allocates memory through the *new* function, and stores the address of that memory to the variable *calendar*. Lines 19-23 initialize a linked list. Line 26 shows assignment to the memory pointed to by the pointer *that*. Lines 28 to 31 show the creation of a new link in the linked list. Lines 33-35 release the memory allocated to those pointers.

### Perl

The Perl programming language supports pointers, although rarely used, in the form of the pack and unpack functions. These are intended only for simple interactions with compiled OS libraries. In all other cases, Perl uses references, which are typed and do not allow any form of pointer arithmetic. They are used to construct complex data structures.

### Rust

Rust uses references, which are similar to pointers but guaranteed to point to a valid value. Working with raw pointers is less common, generally for low-level systems programming. Raw pointers can only be dereferenced inside an `unsafe` block. Operations with raw pointers are found in `std::ptr`.

In Rust, there is no null pointer constant. It is instead given by `std::ptr::null()`.

Rust also has several types of smart pointers:

- `std::boxed::Box`: equivalent to C++'s `std::unique_ptr`
- `std::rc::Rc`: equivalent to a reference-counted single-threaded shared pointer
- `std::sync::Arc`: equivalent to an atomically reference-counted thread safe shared pointer
- `std::rc::Weak`: equivalent to C++'s `std::weak_ptr`

A pointer to `T` is written as `*const T` or `*mut T` in Rust. The following demonstrates raw pointers in Rust:

```mw
fn main() {
    let mut num: i32 = 42;

    let r1 = &num as *const i32;
    let r2 = &mut num as *mut i32;

    unsafe {
        println!("r1 points to: {}", *r1);
        println!("r2 points to: {}", *r2);

        *r2 = 100;
        println!("num is now: {}", num);
    }
}
```
