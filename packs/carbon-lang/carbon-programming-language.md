---
title: "Carbon (programming language)"
source: https://en.wikipedia.org/wiki/Carbon_(programming_language)
domain: carbon-lang
license: CC-BY-SA-4.0
tags: carbon language, carbon lang, carbon cpp successor
fetched: 2026-07-02
---

# Carbon (programming language)

**Carbon** is an experimental programming language designed for interoperability with C++. The project is open-source and was started at Google. Google's engineer Chandler Carruth first introduced Carbon at the CppNorth conference in Toronto in July 2022. He stated that Carbon was created to be a C++ successor. The language is expected to have an experimental MVP version 0.1 in late 2026 at the earliest and a production-ready version 1.0 after 2028.

The language intends to fix several perceived shortcomings of C++ but otherwise provides a similar feature set. The main goals of the language are readability and "bi-directional interoperability" (which allows the user to include C++ code in the Carbon file), as opposed to using a new language like Rust, that, whilst being influenced by C++, is not two-way compatible with C++ programs. Changes to the language will be decided by the Carbon leads. It aims to build on top of the C++ ecosystem the way in an analogous role to TypeScript to JavaScript, or Kotlin to Java.

Carbon's documents, design, implementation, and related tools are hosted on GitHub under the Apache-2.0 license with LLVM Exceptions.

## Example

The following shows how a program might be written in Carbon and C++:

| Carbon | C++ |
|---|---|
| package Geometry; import Math; class Circle { var radius: f32; } fn PrintTotalArea(circles: [Circle]) { var area: f32 = 0; for (circ: Circle in circles) { area += Math.Pi * circ.radius * circ.radius; } Print("Total area: {0}", area); } fn Run() -> i32 { // A dynamically sized array, like `std::vector`. var circles: array [Circle] = ({.radius = 1.0}, {.radius = 2.0}); // Implicitly constructs a slice from the array. PrintTotalArea(circles); return 0; } | import std; using std::span; using std::vector; struct Circle { float radius; }; void printTotalArea(span<Circle> circles) { float area = 0.0f; for (const Circle& circ : circles) { area += std::numbers::pi * circ.radius * circ.radius; } std::println("Total area: {}", area); } int main(int argc, char* argv[]) { vector<Circle> circles{{.radius = 1.0f}, {.radius = 2.0f}}; // Implicitly converts `vector` to `span`. printTotalArea(circles); return 0; } |
