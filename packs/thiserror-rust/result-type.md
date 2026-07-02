---
title: "Result type"
source: https://en.wikipedia.org/wiki/Result_type
domain: thiserror-rust
license: CC-BY-SA-4.0
tags: thiserror derive, rust custom errors, error enum rust, thiserror macro
fetched: 2026-07-02
---

# Result type

In functional programming, a **result type** is a monadic type holding a returned value or an error code. They provide an elegant way of handling errors, without resorting to exception handling; when a function that may fail returns a result type, the programmer is forced to consider success or failure paths, before getting access to the expected result; this eliminates the possibility of an erroneous programmer assumption.

## Examples

- In C++, it is defined by the standard library as `std::expected<T, E>`.
- In Elm, it is defined by the standard library as `type Result e v = Ok v | Err e`.
- In Haskell, by convention the `Either` type is used for this purpose, which is defined by the standard library as `data Either a b = Left a | Right b`, where `a` is the error type and `b` is the return type.
- In Java, it is not natively in the standard library, but is available from third party libraries. For example, result4j which includes an interface `Result<R, E>` similar to Rust `Result<T, E>`, and vavr includes an interface `Either<L, R>` similar to Haskell `Either a b`. Because Java and Kotlin are cross-compatible, Java can use the `Result` type from Kotlin.
- In Kotlin, it is defined by the standard library as `value class Result<out T>`.
- In OCaml, it is defined by the standard library as `type ('a, 'b) result = Ok of 'a | Error of 'b type`.
- In Python, it is not natively in the standard library, but is available from third party libraries such as returns and result.
- In Rust, it is defined by the standard library as `enum Result<T, E> { Ok(T), Err(E) }`.
- In Scala, the standard library also defines an `Either` type, however Scala also has more conventional exception handling.
- In Swift, it is defined by the standard library as `@frozen enum Result<Success, Failure> where Failure : Error`.
- In V, the result type is implemented natively using `!T` as the return type of a function. For example `fn my_function() !string { ... }`. Error Handling in V.

### C++

The `expected<T, E>` class uses `std::unexpected()` to return the type `E`, and can return `T` directly.

```mw
import std;

using std::expected;
using std::ifstream;
using std::string;
using std::stringstream;
using std::unexpected;
using std::filesystem::path;

enum class FileError {
    MISSING_FILE,
    NO_PERMISSION,
    // more errors here
};

expected<string, FileError> loadConfig(const path& p) noexcept {
    if (!std::filesystem::exists(p)) {
        return unexpected(FileError::MISSING_FILE);
    }
    ifstream config{p};
    stringstream buffer;
    if (!config.is_open()) {
        return unexpected(FileError::NO_PERMISSION);
    }
    buffer << config.rdbuf();
    config.close();
    return buffer.str();
}

int main(int argc, char* argv[]) {
    path p{"configs/my_config.txt"};
    if (const expected<String, FileError> s = loadConfig(p); s.has_value()) {
        std::println("Config contents: {}", s.value());
    } else {
        switch (s.error) {
            case FileError::MISSING_FILE:
                std::println("Error: path {} not valid or missing!", p);
                break;
            case FileError::NO_PERMISSION:
                std::println("Error: no permission to read file at path {}!", p);
                break;
            // additional cases...
            default:
                std::unreachable();
        }
    }
}
```

### Rust

Enums in Rust are tagged unions, which can be unpacked with strong type checking through pattern matching.

```mw
const CAT_FOUND: bool = true;

fn main() {
    let result: Result<(), String> = pet_cat();
    match result {
        Ok(_) => println!("Great, we could pet the cat!"),
        Err(error) => println!("Oh no, we couldn't pet the cat: {error}")
    }
}

fn pet_cat() -> Result<(), String> {
    if CAT_FOUND {
        Ok(())
    } else {
        Err(String::from("The cat is nowhere to be found!"))
    }
}
```

### Vlang

The `Error` type is an interface for `iError`.

```mw
const cat_found = true

fn main() {
    cat_name := get_pet_cat_name() or { 
        println("Oh no, we couldn't pet the cat!")
        exit(1)
    }

    println('Great, we could pet the cat ' + cat_name)
}

fn get_pet_cat_name() !string {
    if cat_found { return 'Max' } 
    else { return error('the cat is nowhere to be found') }
}
```
