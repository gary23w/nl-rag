---
title: "Variable shadowing"
source: https://en.wikipedia.org/wiki/Variable_shadowing
domain: closure-conversion
license: CC-BY-SA-4.0
tags: closure conversion, lambda lifting, free variable capture, environment representation
fetched: 2026-07-02
---

# Variable shadowing

In computer programming, **variable shadowing** occurs when a variable declared within a certain scope (decision block, method, or inner class) has the same name as a variable declared in an outer scope. At the level of identifiers (names, rather than variables), this is known as name masking. This outer variable is said to be shadowed by the inner variable, while the inner identifier is said to *mask* the outer identifier. This can lead to confusion, as it may be unclear which variable subsequent uses of the shadowed variable name refer to, which depends on the name resolution rules of the language.

One of the first languages to introduce variable shadowing was ALGOL, which first introduced blocks to establish scopes. It was also permitted by many of the derivative programming languages including C, C++ and Java.

The C# language breaks this tradition, allowing variable shadowing between an inner and an outer class, and between a method and its containing class, but not between an if-block and its containing method, or between case statements in a switch block.

Some languages allow variable shadowing in more cases than others. For example Kotlin allows an inner variable in a function to shadow a passed argument and a variable in an inner block to shadow another in an outer block, while Java does not allow these (see the example below). Both languages allow a passed argument to a function/Method to shadow a Class Field.

Some languages disallow variable shadowing completely such as CoffeeScript and V (Vlang).

## Example

### Lua

The following Lua code provides an example of variable shadowing, in multiple blocks.

```mw
v = 1 -- a global variable

do
  local v = v + 1 -- a new local that shadows global v
  print(v) -- prints 2

  do
    local v = v * 2 -- another local that shadows outer local v
    print(v) -- prints 4
  end

  print(v) -- prints 2
end

print(v) -- prints 1
```

### Python

The following Python code provides another example of variable shadowing:

```mw
x = 0

def outer():
    x = 1

    def inner():
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

# prints
# inner: 2
# outer: 1
# global: 0
```

As there is no variable declaration but only variable assignment in Python, the keyword `nonlocal` introduced in Python 3 is used to avoid variable shadowing and assign to non-local variables:

```mw
x = 0

def outer():
    x = 1

    def inner():
        nonlocal x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

# prints
# inner: 2
# outer: 2
# global: 0
```

The keyword `global` is used to avoid variable shadowing and assign to global variables:

```mw
x = 0

def outer():
    x = 1

    def inner():
        global x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

# prints
# inner: 2
# outer: 1
# global: 2
```

### Rust

```mw
fn main() {
    let x = 0;
    
    {
        // Shadow
        let x = 1;
        println!("Inner x: {}", x); // prints 1
    }
    
    println!("Outer x: {}", x); // prints 0
    
    let x = "Rust";
    println!("Outer x: {}", x);  // prints 'Rust'
}

//# Inner x: 1
//# Outer x: 0
//# Outer x: Rust
```

### C++

```mw
#include <iostream>

int main()
{
  int x = 42;
  int sum = 0;

  for (int i = 0; i < 10; i++) {
    int x = i;
    std::cout << "x: " << x << '\n'; // prints values of i from 0 to 9
    sum += x;
  }

  std::cout << "sum: " << sum << '\n'; // prints 45
  std::cout << "x:   " << x   << '\n'; // prints 42

  return 0;
}
```

### Java

```mw
public class Shadow {
    private int myIntVar = 0;

    public void shadowTheVar() {
        // Since it has the same name as above object instance field, it shadows above 
        // field inside this method.
        int myIntVar = 5;

        // If we simply refer to 'myIntVar' the one of this method is found 
        // (shadowing a second one with the same name)
        System.out.println(myIntVar); // prints 5

        // If we want to refer to the shadowed myIntVar from this class we need to 
        // refer to it like this:
        System.out.println(this.myIntVar); // prints 0
    }

    public static void main(String[] args){
        new Shadow().shadowTheVar();
    }
}
```

However, the following code will *not* compile:

```mw
public class Shadow {
    public static void main(String[] args){
        int a = 1;

        for(int i = 0; i < 10; i++) {
            // This causes a compilation error since redefining a variable
            // inside a nested block in the same function is not allowed.
            int a = i;
            System.out.println(a);
        }
    }
}
```

### JavaScript

ECMAScript 6 introduction of `let` and `const` with block scoping allow variable shadowing.

```mw
function myFunc() {
    let my_var = 'test';
    if (true) {
        let my_var = 'new test';
        console.log(my_var); // new test
    }
    console.log(my_var); // test
}
myFunc();
```
