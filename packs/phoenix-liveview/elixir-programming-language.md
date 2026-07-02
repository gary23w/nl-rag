---
title: "Elixir (programming language)"
source: https://en.wikipedia.org/wiki/Elixir_(programming_language)
domain: phoenix-liveview
license: CC-BY-SA-4.0
tags: phoenix liveview elixir, server rendered interactivity, elixir web framework, liveview stateful process
fetched: 2026-07-02
---

# Elixir (programming language)

**Elixir** is a functional, concurrent, high-level general-purpose programming language that runs on the BEAM virtual machine, which is also used to implement the Erlang programming language. Elixir builds on top of Erlang and shares the same abstractions for building distributed, fault-tolerant applications. Elixir also provides tooling and an extensible design. The latter is supported by compile-time metaprogramming with macros and polymorphism via protocols.

The community organizes yearly events in the United States, Europe, and Japan, as well as minor local events and conferences.

## History

José Valim created the Elixir programming language as a research and development project at Plataformatec. His goals were to enable higher extensibility and productivity in the Erlang VM while maintaining compatibility with Erlang's ecosystem.

Elixir is aimed at large-scale sites and apps. It uses features of Ruby, Erlang, and Clojure to develop a high-concurrency and low-latency language. It was designed to handle large data volumes. Elixir is also used in telecommunications, e-commerce, and finance.

In 2021, the Numerical Elixir effort was announced with the goal of bringing machine learning, neural networks, GPU compilation, data processing, and computational notebooks to the Elixir ecosystem.

## Features

- Compiles to bytecode for the BEAM virtual machine of Erlang. Full interoperability with Erlang code, without runtime impact.
- Scalability and fault-tolerance, thanks to Erlang's lightweight concurrency mechanisms
- Built-in tooling for managing dependencies, code compilation, running tests, formatting code, remote debugging and more.
- An interactive REPL inside running programs, including Phoenix web servers, with code reloading and access to internal state
- Everything is an expression
- Pattern matching to promote assertive code
- Type hints for static analysis tools
- Immutable data, with an emphasis, like other functional languages, on recursion and higher-order functions instead of side-effect-based looping
- Shared nothing concurrent programming via message passing (actor model)
- Lazy and async collections with streams
- Railway-oriented programming via the `with` construct
- Hygienic metaprogramming by direct access to the abstract syntax tree (AST). Libraries often implement small domain-specific languages, such as for databases or testing.
- Code execution at compile time. The Elixir compiler also runs on the BEAM, so modules that are being compiled can immediately run code which has already been compiled.
- Polymorphism via a mechanism called protocols. Dynamic dispatch, as in Clojure, however, without multiple dispatch because Elixir protocols dispatch on a single type.
- Support for documentation via Python-like docstrings in the Markdown formatting language
- Unicode support and UTF-8 strings

## Examples

The following examples can be run in an `iex` shell or saved in a file and run from the command line by typing `elixir *<filename>*`.

Classic Hello world example:

```mw
iex> IO.puts("Hello World!")
Hello World!
```

Pipe operator:

```mw
iex> "Elixir" |> String.graphemes() |> Enum.frequencies()
%{"E" => 1, "i" => 2, "l" => 1, "r" => 1, "x" => 1}

iex> %{values: 1..5} |> Map.get(:values) |> Enum.map(& &1 * 2)
[2, 4, 6, 8, 10]

iex> %{values: 1..5} |> Map.get(:values) |> Enum.map(& &1 * 2) |> Enum.sum()
30
```

Pattern matching (a.k.a. destructuring):

```mw
iex> %{left: x} = %{left: 5, right: 8}
iex> x
5

iex> {:ok, [_ | rest]} = {:ok, [1, 2, 3]}
iex> rest
[2, 3]
```

Pattern matching with multiple clauses:

```mw
iex> case File.read("path/to/file") do
iex>   {:ok, contents} -> IO.puts("found file: #{contents}")
iex>   {:error, reason} -> IO.puts("missing file: #{reason}")
iex> end
```

List comprehension:

```mw
iex> for n <- 1..5, rem(n, 2) == 1, do: n*n
[1, 9, 25]
```

Asynchronously reading files with streams:

```mw
1..5
|> Task.async_stream(&File.read!("#{&1}.txt"))
|> Stream.filter(fn {:ok, contents} -> String.trim(contents) != "" end)
|> Enum.join("\n")
```

Multiple function bodies with guards:

```mw
def fib(n) when n in [0, 1], do: n
def fib(n), do: fib(n-2) + fib(n-1)
```

Relational databases with the Ecto library:

```mw
schema "weather" do
  field :city     # Defaults to type :string
  field :temp_lo, :integer
  field :temp_hi, :integer
  field :prcp,    :float, default: 0.0
end

Weather |> where(city: "Kraków") |> order_by(:temp_lo) |> limit(10) |> Repo.all
```

Sequentially spawning a thousand processes:

```mw
for num <- 1..1000, do: spawn fn -> IO.puts("#{num * 2}") end
```

Asynchronously performing a task:

```mw
task = Task.async fn -> perform_complex_action() end
other_time_consuming_action()
Task.await task
```
