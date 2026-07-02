---
title: "Pointer (computer programming) (part 1/2)"
source: https://en.wikipedia.org/wiki/Pointer_(computer_programming)
domain: address-space-layout-randomization
license: CC-BY-SA-4.0
tags: address space layout randomization, position independent code, memory layout randomization, exploit mitigation technique, memory safety defense
fetched: 2026-07-02
part: 1/2
---

# Pointer (computer programming)

> I do consider assignment statements and pointer variables to be among computer science's "most valuable treasures."

—

Donald Knuth

,

Structured Programming, with go to Statements

In computer science, a **pointer** is an object in many programming languages that stores a memory address. This can be that of another value located in computer memory, or in some cases, that of memory-mapped computer hardware. A pointer *references* a location in memory, and obtaining the value stored at that location is known as *dereferencing* the pointer. As an analogy, a page number in a book's index could be considered a pointer to the corresponding page; dereferencing such a pointer would be done by flipping to the page with the given page number and reading the text found on that page. The actual format and content of a pointer variable is dependent on the underlying computer architecture.

Using pointers significantly improves performance for repetitive operations, like traversing iterable data structures (e.g. strings, lookup tables, control tables, linked lists, and tree structures). In particular, it is often much cheaper in time and space to copy and dereference pointers than it is to copy and access the data to which the pointers point.

Pointers are also used to hold the addresses of entry points for called subroutines in procedural programming and for run-time linking to dynamic link libraries (DLLs). In object-oriented programming, pointers to functions are used for binding methods, often using virtual method tables.

A pointer is a simple, more concrete implementation of the more abstract *reference* data type. Several languages, especially low-level languages, support some type of pointer, although some have more restrictions on their use than others. While "pointer" has been used to refer to references in general, it more properly applies to data structures whose interface explicitly allows the pointer to be manipulated (arithmetically via *pointer arithmetic*) as a memory address, as opposed to a magic cookie or capability which does not allow such. Because pointers allow both protected and unprotected access to memory addresses, there are risks associated with using them, particularly in the latter case. Primitive pointers are often stored in a format similar to an integer; however, attempting to dereference or "look up" such a pointer whose value is not a valid memory address could cause a program to crash (or contain invalid data). To alleviate this potential problem, as a matter of type safety, pointers are considered a separate type parameterized by the type of data they point to, even if the underlying representation is an integer. Other measures may also be taken (such as validation and bounds checking), to verify that the pointer variable contains a value that is both a valid memory address and within the numerical range that the processor is capable of addressing.


## History

In 1955, Soviet Ukrainian computer scientist Kateryna Yushchenko created the Address programming language that made possible indirect addressing and addresses of the highest rank – analogous to pointers. This language was widely used on the Soviet computers. However, it was unknown outside the Soviet Union and usually Harold Lawson is credited with the invention, in 1964, of the pointer. In 2000, Lawson was presented the Computer Pioneer Award by the IEEE "[f]or inventing the pointer variable and introducing this concept into PL/I, thus providing for the first time, the capability to flexibly treat linked lists in a general-purpose high-level language". His seminal paper on the concepts appeared in the June 1967 issue of CACM entitled: PL/I List Processing. According to the Oxford English Dictionary, the **word** *pointer* first appeared in print as a *stack pointer* in a technical memorandum by the System Development Corporation.


## Formal description

In computer science, a pointer is a kind of reference.

A *data primitive* (or just *primitive*) is any datum that can be read from or written to computer memory using one memory access (for instance, both a *byte* and a *word* are primitives).

A *data aggregate* (or just *aggregate*) is a group of primitives that are logically contiguous in memory and that are viewed collectively as one datum (for instance, an aggregate could be 3 logically contiguous bytes, the values of which represent the 3 coordinates of a point in space). When an aggregate is entirely composed of the same type of primitive, the aggregate may be called an *array*; in a sense, a multi-byte *word* primitive is an array of bytes, and some programs use words in this way.

In the context of these definitions, a *byte* is the smallest primitive; each memory address specifies a different byte. The memory address of the initial byte of a datum is considered the memory address (or *base memory address*) of the entire datum.

A *memory pointer* (or just *pointer*) is a primitive, the value of which is intended to be used as a memory address; it is said that *a pointer points to a memory address*. It is also said that *a pointer points to a datum [in memory]* when the pointer's value is the datum's memory address.

More generally, a pointer is a kind of reference, and it is said that *a pointer references a datum stored somewhere in memory*; to obtain that datum is *to dereference the pointer*. The feature that separates pointers from other kinds of reference is that a pointer's value is meant to be interpreted as a memory address, which is a rather low-level concept.

References serve as a level of indirection: A pointer's value determines which memory address (that is, which datum) is to be used in a calculation. Because indirection is a fundamental aspect of algorithms, pointers are often expressed as a fundamental data type in programming languages; in statically (or strongly) typed programming languages, the type of a pointer determines the type of the datum to which the pointer points.


## Architectural roots

Pointers are a very thin abstraction on top of the addressing capabilities provided by most modern architectures. In the simplest scheme, an *address*, or a numeric index, is assigned to each unit of memory in the system, where the unit is typically either a byte or a word – depending on whether the architecture is byte-addressable or word-addressable – effectively transforming all of memory into a very large array. The system would then also provide an operation to retrieve the value stored in the memory unit at a given address (usually utilizing the machine's general-purpose registers).

In the usual case, a pointer is large enough to hold more addresses than there are units of memory in the system. This introduces the possibility that a program may attempt to access an address which corresponds to no unit of memory, either because not enough memory is installed (i.e. beyond the range of available memory) or the architecture does not support such addresses. The first case may, in certain platforms such as the Intel x86 architecture, be called a segmentation fault (segfault). The second case is possible in the current implementation of AMD64, where pointers are 64 bit long and addresses only extend to 48 bits. Pointers must conform to certain rules (canonical addresses), so if a non-canonical pointer is dereferenced, the processor raises a general protection fault.

On the other hand, some systems have more units of memory than there are addresses. In this case, a more complex scheme such as memory segmentation or paging is employed to use different parts of the memory at different times. The last incarnations of the x86 architecture support up to 36 bits of physical memory addresses, which were mapped to the 32-bit linear address space through the PAE paging mechanism. Thus, only 1/16 of the possible total memory may be accessed at a time. Another example in the same computer family was the 16-bit protected mode of the 80286 processor, which, though supporting only 16 MB of physical memory, could access up to 1 GB of virtual memory, but the combination of 16-bit address and segment registers made accessing more than 64 KB in one data structure cumbersome.

In order to provide a consistent interface, some architectures provide memory-mapped I/O, which allows some addresses to refer to units of memory while others refer to device registers of other devices in the computer. There are analogous concepts such as file offsets, array indices, and remote object references that serve some of the same purposes as addresses for other types of objects.


## Uses

Pointers are directly supported without restrictions in languages such as PL/I, C, C++, Pascal, FreeBASIC, and implicitly in most assembly languages. They are used mainly to construct references, which in turn are fundamental to construct nearly all data structures, and to pass data between different parts of a program.

In functional programming languages that rely heavily on lists, data references are managed abstractly by using primitive constructs like cons and the corresponding elements car and cdr, which can be thought of as specialised pointers to the first and second components of a cons-cell. This gives rise to some of the idiomatic "flavour" of functional programming. By structuring data in such cons-lists, these languages facilitate recursive means for building and processing data—for example, by recursively accessing the head and tail elements of lists of lists; e.g. "taking the car of the cdr of the cdr". By contrast, memory management based on pointer dereferencing in some approximation of an array of memory addresses facilitates treating variables as slots into which data can be assigned imperatively.

When dealing with arrays, the critical lookup operation typically involves a stage called *address calculation* which involves constructing a pointer to the desired data element in the array. In other data structures, such as linked lists, pointers are used as references to explicitly tie one piece of the structure to another.

Pointers are used to pass parameters by reference. This is useful if the programmer wants a function's modifications to a parameter to be visible to the function's caller. This is also useful for returning multiple values from a function.

Pointers can also be used to allocate and deallocate dynamic variables and arrays in memory. Since a variable will often become redundant after it has served its purpose, it is a waste of memory to keep it, and therefore it is good practice to deallocate it (using the original pointer reference) when it is no longer needed. Failure to do so may result in a *memory leak* (where available free memory gradually, or in severe cases rapidly, diminishes because of an accumulation of numerous redundant memory blocks).

### C pointers

In C, the basic syntax to define a pointer is:

```mw
int *ptr;
```

This declares a variable `ptr` that stores a pointer to an object of type `int`. Other types can be used in place of `int`; for example, `bool *ptr` would declare a pointer to an object of type `bool`.

After a pointer has been declared, it can be assigned an address. In C, the address of a variable can be retrieved with the `&` unary operator:

```mw
// Declare a variable for a pointer to int
int *ptr;
// Declare a variable for an int
int a = 5;
// Assign the address of a to the pointer variable
ptr = &a;
```

To dereference the pointer, yielding the object it points to, an asterisk (`*`) can be used:

```mw
printf("%d\n", *ptr);
// Prints: 5
```

There are two styles of declarations of a pointer-to-`int` named `ptr`:

- `int *ptr;`, which emphasises that the expression `*ptr` has type `int`.
- `int* ptr;`, which emphasises that `ptr` has type `int*`. This style is more prevalent in C++ than C.

Both `int *x, y;` and `int* x, y;` declare `x` to be a pointer to `int`, but declare `y` to be an `int`. This is because the `*` applies only to the variable immediately following it.

The asterisk can also be used on the left-hand side of an assignment to change the object `a` without having to be in the same scope.

```mw
*ptr = 8;
```

If `a` is accessed later, its new value will be 8.

Because the C language does not specify an implicit initialization for objects of automatic storage duration, pointer variables can sometimes point to unexpected locations, causing undefined behavior. To combat this, pointers are sometimes initialized with a null pointer value, represented in C by the `NULL` macro; in C23 and later, `nullptr` is also available as an alternative, which is of type `nullptr_t`.

```mw
int *ptr = NULL;
int *ptr = nullptr; // since C23
```

Dereferencing a null pointer produces undefined behavior, which can result in unpredictable bugs and results.

This example may be clearer if memory is examined directly. Assume that `a` is located at address 0x8130 in memory and `ptr` at 0x8134; also assume this is a 32-bit machine such that an int is 32-bits wide. The following is what would be in memory after the following code snippet is executed:

```mw
int a = 5;
int *ptr = NULL;
```

| Address | Contents |
|---|---|
| **0x8130** | 0x00000005 |
| **0x8134** | 0x00000000 |

(The null pointer shown here is 0x00000000.) By assigning the address of `a` to `ptr`:

```mw
ptr = &a;
```

yields the following memory values:

| Address | Contents |
|---|---|
| **0x8130** | 0x00000005 |
| **0x8134** | 0x00008130 |

Then by dereferencing `ptr` by coding:

```mw
*ptr = 8;
```

the computer will take the contents of `ptr` (which is 0x8130), 'locate' that address, and assign 8 to that location yielding the following memory:

| Address | Contents |
|---|---|
| **0x8130** | 0x00000008 |
| **0x8134** | 0x00008130 |

Clearly, accessing `a` will yield the value of 8 because the previous instruction modified the contents of `a` by way of the pointer `ptr`.

### Use in data structures

When setting up data structures like lists, queues and trees, it is necessary to have pointers to help manage how the structure is implemented and controlled. Typical examples of pointers are start pointers, end pointers, and stack pointers. These pointers can either be **absolute** (the actual physical address or a virtual address in virtual memory) or **relative** (an offset from an absolute start address ("base") that typically uses fewer bits than a full address, but will usually require one additional arithmetic operation to resolve).

Relative addresses are a form of manual memory segmentation, and share many of its advantages and disadvantages. A two-byte offset, containing a 16-bit, unsigned integer, can be used to provide relative addressing for up to 64 KiB (216 bytes) of a data structure. This can easily be extended to 128, 256 or 512 KiB if the address pointed to is forced to be aligned on a half-word, word or double-word boundary (but, requiring an additional "shift left" bitwise operation—by 1, 2 or 3 bits—in order to adjust the offset by a factor of 2, 4 or 8, before its addition to the base address). Generally, though, such schemes are a lot of trouble, and for convenience to the programmer absolute addresses (and underlying that, a *flat address space*) is preferred.

A one byte offset, such as the hexadecimal ASCII value of a character (e.g. X'29') can be used to point to an alternative integer value (or index) in an array (e.g., X'01'). In this way, characters can be very efficiently translated from 'raw data' to a usable sequential index and then to an absolute address without a lookup table.

#### C arrays

In C, array indexing is formally defined in terms of pointer arithmetic; that is, the language specification requires that `a[i]` be equivalent to `*(a + i)`, because, if `a` is the name of an array, in most contexts the expression `a` evaluates to a pointer to the first element of `a`, so the syntax for accessing arrays is identical for that which can be used to dereference pointers. For example, an array `a` can be declared and used in the following manner:

```mw
int a[5]; // Declares 5 contiguous integers
int *ptr = a; // Array names in expressions evaluate to pointers in most cases
ptr[0] = 1; // Pointers can be indexed with array syntax
*(a + 1) = 2; // Arrays can be indexed with pointer syntax
*(1 + a) = 2; // Pointer addition is commutative
2[a] = 4; // Subscript operator is commutative (perhaps unusual)
```

This allocates a block of five integers and names the block `a`; the expression `a` evaluates, in most contexts, as a pointer to the first element of the block. Another common use of pointers is to point to dynamically allocated memory from malloc which returns a consecutive block of memory of no less than the requested size that can be used as an array.

While, when used as an operand for most operators, an array evaluates as a pointer to the first element of the array, this is not the case for the `sizeof` operator. In this example, `sizeof(a)` will evaluate to `5 * sizeof(int)` (the size of the array), while `sizeof(ptr)` will evaluate to `sizeof(int *)`, the size of the pointer itself.

Default values of an array can be declared like:

```mw
int a[5] = {2, 4, 3, 1, 5};
```

If `a` is located in memory starting at address 0x1000 on a 32-bit little-endian machine then memory will contain the following (values are in hexadecimal, like the addresses):

|   | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 1000 | 2 | 0 | 0 | 0 |
| 1004 | 4 | 0 | 0 | 0 |
| 1008 | 3 | 0 | 0 | 0 |
| 100C | 1 | 0 | 0 | 0 |
| 1010 | 5 | 0 | 0 | 0 |

Represented here are five integers: 2, 4, 3, 1, and 5. These five integers occupy 32 bits (4 bytes) each with the least-significant byte stored first (this is a little-endian CPU architecture) and are stored consecutively starting at address 0x1000.

The syntax for C with pointers is:

- `a` means 0x1000;
- `a + 1` means 0x1004: the "+ 1" means to add the size of 1 `int`, which is 4 bytes;
- `*a` means to dereference the contents of `a`. Considering the contents as a memory address (0x1000), look up the value at that location (0x0002);
- `a[i]` means element number `i`, 0-based, of `a` which is translated into `*(a + i)`.

The last example is how to access the contents of `a`. Breaking it down:

- `a + i` is the memory location of the `i`th element of `a`, starting at `i = 0`;
- `*(a + i)` takes that memory address and dereferences it to access the value.

#### C linked list

Below is an example definition of a linked list in C.

```mw
struct LinkedList {
    void *data; // data of this link
    struct LinkedList *next; // next link; NULL if there is none
};
```

This pointer-recursive definition is essentially the same as the reference-recursive definition from the language Haskell:

```mw
data LinkedList a
    = Nil
    | Cons a (LinkedList a)
```

where `Nil` is the empty list, and `Cons a (LinkedList a)` is a cons cell of type `a` with another link also of type `a`.

The definition with references, however, is type-checked and does not use potentially confusing signal values. For this reason, data structures in C are usually dealt with via wrapper functions, which are carefully checked for correctness.

### Pass-by-address using pointers

Pointers can be used to pass variables by their address, allowing their value to be changed. For example, consider the following C code:

```mw
// a copy of the int n can be changed within the function without affecting the calling code
void passByValue(int n) {
    n = 12;
}

// a pointer m is passed instead. No copy of the value pointed to by m is created
void passByAddress(int *m) {
    *m = 14;
}

int main(void) {
    int x = 3;

    // pass a copy of x's value as the argument
    passByValue(x);
    // the value was changed inside the function, but x is still 3 from here on

    // pass x's address as the argument
    passByAddress(&x);
    // x was actually changed by the function and is now equal to 14 here

    return 0;
}
```

### Dynamic memory allocation

In some programs, the required amount of memory depends on what *the user* may enter. In such cases the programmer needs to allocate memory dynamically. This is done by allocating memory at the *heap* rather than on the *stack*, where variables usually are stored (although variables can also be stored in the CPU registers). Dynamic memory allocation can only be made through pointers, and names – like with common variables – cannot be given.

Pointers are used to store and manage the addresses of dynamically allocated blocks of memory. Such blocks are used to store data objects or arrays of objects. Most structured and object-oriented languages provide an area of memory, called the *heap* or *free store*, from which objects are dynamically allocated.

The example C code below illustrates how structure objects are dynamically allocated and referenced. The standard C library provides the function `malloc()` for allocating memory blocks from the heap. It takes the size of an object to allocate as a parameter and returns a pointer to a newly allocated block of memory suitable for storing the object, or it returns a null pointer if the allocation failed.

```mw
// Parts inventory item
typedef struct {
    int id; // Part number
    char *name; // Part name
    float cost; // Cost
} Item;

// Allocate and initialize a new Item object
Item *makeItem(const char *name) {
    Item *item;

    // Allocate a block of memory for a new Item object
    item = malloc(sizeof(*item));
    if (!item) {
        return NULL;
    }

    // Initialize the members of the new Item
    memset(item, 0, sizeof(*item));
    item->id = -1;
    item->name = NULL;
    item->cost = 0.0;

    // Save a copy of the name in the new Item 
    item->name = malloc(strlen(name) + 1);
    if (!item->name) {
        free(item);
        return NULL;
    }
    strcpy(item->name, name);

    // Return the newly created Item object
    return item;
}
```

The code below illustrates how memory objects are dynamically deallocated, i.e., returned to the heap or free store. The standard C library provides the function `free()` for deallocating a previously allocated memory block and returning it back to the heap.

```mw
// Deallocate an Item object
void destroyItem(Item *item) {
    // Check for a null object pointer
    if (!item) {
        return;
    }

    // Deallocate the name string saved within the Item
    if (item->name) {
        free(item->name);
        item->name = NULL;
    }

    // Deallocate the Item object itself
    free(item);
}
```

### Memory-mapped hardware

On some computing architectures, pointers can be used to directly manipulate memory or memory-mapped devices.

Assigning addresses to pointers is an invaluable tool when programming microcontrollers. Below is a simple example declaring a pointer of type int and initialising it to a hexadecimal address in this example the constant 0x7FFF:

```mw
int *hardware_address = (int *)0x7FFF;
```

In the mid-1980s, using the BIOS to access the video capabilities of PCs was slow. Applications that were display-intensive typically used to access CGA video memory directly by casting the hexadecimal constant 0xB8000 to a pointer to an array of 80 unsigned 16-bit int values. Each value consisted of an ASCII code in the low byte, and a colour in the high byte. Thus, to put the letter 'A' at row 5, column 2 in bright white on blue, one would write code like the following:

```mw
#define VID ((unsigned short (*)[80])0xB8000)

void foo(void) {
    VID[4][1] = 0x1F00 | 'A';
}
```

### Use in control tables

Control tables that are used to control program flow usually make extensive use of pointers. The pointers, usually embedded in a table entry, may, for instance, be used to hold the entry points to subroutines to be executed, based on certain conditions defined in the same table entry. The pointers can however be simply indexes to other separate, but associated, tables comprising an array of the actual addresses or the addresses themselves (depending upon the programming language constructs available). They can also be used to point to earlier table entries (as in loop processing) or forward to skip some table entries (as in a switch or "early" exit from a loop). For this latter purpose, the "pointer" may simply be the table entry number itself and can be transformed into an actual address by simple arithmetic.


## Typed pointers and casting

In many languages, pointers have the additional restriction that the object they point to has a specific type. For example, a pointer may be declared to point to an integer; the language will then attempt to prevent the programmer from pointing it to objects which are not integers, such as floating-point numbers, eliminating some errors.

For example, in the following C code:

```mw
int *money;
char *bags;
```

`money` would be an integer pointer and `bags` would be a char pointer.

The following would yield a compiler warning of "assignment from incompatible pointer type" under GCC:

```mw
bags = money;
```

because `money` and `bags` were declared with different types.

To suppress the compiler warning, it must be made explicit to make the assignment by typecasting it:

```mw
bags = (char *)money;
```

which says to cast the integer pointer of `money` to a char pointer and assign to `bags`.

A 2005 draft of the C standard requires that casting a pointer derived from one type to one of another type should maintain the alignment correctness for both types (6.3.2.3 Pointers, par. 7):

```mw
char *external_buffer = "abcdef";
int *internal_data;

internal_data = (int *)external_buffer;  
// UNDEFINED BEHAVIOUR if "the resulting pointer is not correctly aligned"
```

In languages that allow pointer arithmetic, arithmetic on pointers takes into account the size of the type. For example, adding an integer number to a pointer produces another pointer that points to an address that is higher by that number times the size of the type. This allows us to easily compute the address of elements of an array of a given type, as was shown in the C arrays example above. When a pointer of one type is cast to another type of a different size, the programmer should expect that pointer arithmetic will be calculated differently. In C, for example, if the `money` array starts at 0x2000 and `sizeof(int)` is 4 bytes whereas `sizeof(char)` is 1 byte, then `money + 1` will point to 0x2004, but `bags + 1` would point to 0x2001. Other risks of casting include loss of data when "wide" data is written to "narrow" locations (e.g. `bags[0] = 65537;`), unexpected results when bit-shifting values, and comparison problems, especially with signed vs unsigned values.

Although it is impossible in general to determine at compile-time which casts are safe, some languages store run-time type information which can be used to confirm that these dangerous casts are valid at runtime. Other languages merely accept a conservative approximation of safe casts, or none at all.

### Value of pointers

In C and C++, even if two pointers compare as equal that doesn't mean they are equivalent. In these languages *and* LLVM, the rule is interpreted to mean that "just because two pointers point to the same address, does not mean they are equal in the sense that they can be used interchangeably", the difference between the pointers referred to as their *provenance*. Casting to an integer type such as `uintptr_t` is implementation-defined and the comparison it provides does not provide any more insight as to whether the two pointers are interchangeable. In addition, further conversion to bytes and arithmetic will throw off optimizers trying to keep track the use of pointers, a problem still being elucidated in academic research.


## Making pointers safer

As a pointer allows a program to attempt to access an object that may not be defined, pointers can be the origin of a variety of programming errors. However, the usefulness of pointers is so great that it can be difficult to perform programming tasks without them. Consequently, many languages have created constructs designed to provide some of the useful features of pointers without some of their pitfalls, also sometimes referred to as *pointer hazards*. In this context, pointers that directly address memory (as used in this article) are referred to as **raw pointers** or **naked pointer**, by contrast with smart pointers or other variants.

One major problem with pointers is that as long as they can be directly manipulated as a number, they can be made to point to unused addresses or to data which is being used for other purposes. Many languages, including most functional programming languages and recent imperative programming languages like Java, replace pointers with a more opaque type of reference, typically referred to as simply a *reference*, which can only be used to refer to objects and not manipulated as numbers, preventing this type of error. Array indexing is handled as a special case.

A pointer which does not have any address assigned to it is called a wild pointer. Any attempt to use such uninitialized pointers can cause unexpected behavior, either because the initial value is not a valid address, or because using it may damage other parts of the program. The result is often a segmentation fault, storage violation or wild branch (if used as a function pointer or branch address).

In systems with explicit memory allocation, it is possible to create a dangling pointer by deallocating the memory region it points into. This type of pointer is dangerous and subtle because a deallocated memory region may contain the same data as it did before it was deallocated but may be then reallocated and overwritten by unrelated code, unknown to the earlier code. Languages with garbage collection prevent this type of error because deallocation is performed automatically when there are no more references in scope.

In languages that abstract away pointers and pointer arithmetic, such as Java, one can use iterators, which can be seen as a safer means of iterating over a segment of memory or a collection without using direct pointer access. Many languages, even those with pointers, such as C++, C# and Rust, have iterators for collections.

```mw
import java.util.Iterator;
import java.util.List;

List<String> fruits = List.of("Apple", "Banana", "Cherry", "Date");
Iterator<String> iterator = fruits.iterator();

// Use the iterator to traverse the list
while (iterator.hasNext()) {
    // Get the next element
    String fruit = iterator.next();
    System.out.println(fruit);
}
```

In C++ the iterator can overload `operator++`, similar to the traditional syntax of incrementing a pointer in C. A custom-defined iterator traditionally overloads three operators:

- `operator==`/`operator!=` (equality comparison)
- `operator++` (increment)
- `operator*` (dereference)

```mw
import std;

using std::vector;

// collections such as vector define an iterator type,
// with begin() and end() method
vector<int> v{1, 2, 3, 4, 5};
// 'it' is of type vector<int>::iterator
// iterate through the collection similar to pointer arithmetic
for (auto it = v.begin(); it != v.end(); ++it) {
    std::print("{}", *it);
}
```

Some languages, like C++, support smart pointers, which use a simple form of reference counting to help track allocation of dynamic memory in addition to acting as a reference. In the absence of reference cycles, where an object refers to itself indirectly through a sequence of smart pointers, these eliminate the possibility of dangling pointers and memory leaks. Delphi strings support reference counting natively.

The Rust programming language introduces a *borrow checker*, *pointer lifetimes*, and an optimisation based around option types for null pointers to eliminate pointer bugs, without resorting to garbage collection.


## Special kinds of pointers

### Kinds defined by value

#### Null pointer

A **null pointer** has a value reserved for indicating that the pointer does not refer to a valid object. Null pointers are routinely used to represent conditions such as the end of a list of unknown length or the failure to perform some action; this use of null pointers can be compared to nullable types and to the *Nothing* value in an option type.

#### Dangling pointer

A **dangling pointer** is a pointer that does not point to a valid object and consequently may make a program crash or behave oddly. In the Pascal or C programming languages, pointers that are not specifically initialized may point to unpredictable addresses in memory.

The following example code shows a dangling pointer:

```mw
int func(void) {
    char *p1 = malloc(sizeof(char)); // (undefined) value of some place on the heap
    char *p2; // dangling (uninitialized) pointer
    *p1 = 'a'; // This is OK, assuming malloc() has not returned NULL.
    *p2 = 'b'; // This invokes undefined behavior
}
```

Here, `p2` may point to anywhere in memory, so performing the assignment `*p2 = 'b';` can corrupt an unknown area of memory or trigger a segmentation fault.

#### Wild branch

Where a pointer is used as the address of the entry point to a program or start of a function which doesn't return anything and is also either uninitialized or corrupted, if a call or jump is nevertheless made to this address, a "wild branch" is said to have occurred. In other words, a wild branch is a function pointer that is wild (dangling).

The consequences are usually unpredictable and the error may present itself in several different ways depending upon whether or not the pointer is a "valid" address and whether or not there is (coincidentally) a valid instruction (opcode) at that address. The detection of a wild branch can present one of the most difficult and frustrating debugging exercises since much of the evidence may already have been destroyed beforehand or by execution of one or more inappropriate instructions at the branch location. If available, an instruction set simulator can usually not only detect a wild branch before it takes effect, but also provide a complete or partial trace of its history.

### Kinds defined by structure

#### Autorelative pointer

An **autorelative pointer** is a pointer whose value is interpreted as an offset from the address of the pointer itself; thus, if a data structure has an autorelative pointer member that points to some portion of the data structure itself, then the data structure may be relocated in memory without having to update the value of the auto relative pointer.

The cited patent also uses the term **self-relative pointer** to mean the same thing. However, the meaning of this term has been used in other ways:

- to mean an offset from the address of a structure rather than from the address of the pointer itself;
- to mean a pointer containing its own address, which can be useful for reconstructing in any arbitrary region of memory a collection of data structures that point to each other.

#### Based pointer

A **based pointer** is a pointer whose value is an offset from the value of another pointer. This can be used to store and load blocks of data, assigning the address of the beginning of the block to the base pointer.

### Kinds defined by use or datatype

#### Multiple indirection

In some languages, a pointer can reference another pointer, requiring multiple dereference operations to get to the original value. While each level of indirection may add a performance cost, it is sometimes necessary in order to provide correct behavior for complex data structures. For example, in C it is typical to define a linked list in terms of an element that contains a pointer to the next element of the list:

```mw
typedef struct LinkedList {
    int value;
    struct LinkedList *next;
} LinkedList;

LinkedList *head = NULL;
```

This implementation uses a pointer to the first element in the list as a surrogate for the entire list. If a new value is added to the beginning of the list, `head` has to be changed to point to the new element. Since C arguments are always passed by value, using double indirection allows the insertion to be implemented correctly, and has the desirable side-effect of eliminating special case code to deal with insertions at the front of the list:

```mw
// Given a sorted list at *head, insert the element item at the first
// location where all earlier elements have lesser or equal value.
void insert(LinkedList **head, LinkedList *item) {
    // p points to a pointer to an element
    LinkedList **p = head;
    while (*p && (*p)->value < item->value) {
        p = &(*p)->next;
    }
    item->next = *p;
    *p = item;
}

// Caller does this:
insert(&head, item);
```

In this case, if the value of `item` is less than that of `head`, the caller's `head` is properly updated to the address of the new item.

A basic example is in the argv argument to the main function in C (and C++), which is given in the prototype as `char **argv` (or `char *argv[]`)—this is because the variable `argv` itself is a pointer to an array of strings (an array of arrays), so `*argv` is a pointer to the 0th string (by convention the name of the program), and `**argv` is the 0th character of the 0th string.

#### Function pointer

In some languages, a pointer can reference executable code, i.e., it can point to a function, method, or procedure. A function pointer will store the address of a function to be invoked. While this facility can be used to call functions dynamically, it is often a favorite technique of virus and other malicious software writers.

```mw
// Function with two integer parameters returning an integer value
int sum(int n1, int n2) {   
    return n1 + n2;
}

int main(void) {
    int a = 3;
    int b = 5;
    // Function pointer to a function (int, int) -> int
    // and points to function sum
    int (*fp)(int, int) = &sum;
    int x = (*fp)(a, b); // Calls function sum with arguments a and b
    int y = sum(a, b); // Calls function sum with arguments a and b
}
```

In C++, one may use a lambda (anonymous function) in place of a function pointer.

```mw
import std;

using Callback = void(*)(int);

void process(int a, int b, Callback cb) {
    callback(a + b);
}

void printResult(int result) {
    std::println("Result: {}", result);
}

int main(int argc, char* argv[]) {
    // using the traditional function pointer:
    process(1, 2, printResult);
    // prints: "Result: 3"

    // using a lambda:
    process(3, 4, [](int result) -> void { std::println("Result: {}"); });
    // prints: "Result: 7"
}
```

#### Back pointer

In doubly linked lists or tree structures, a back pointer held on an element 'points back' to the item referring to the current element. These are useful for navigation and manipulation, at the expense of greater memory use.
