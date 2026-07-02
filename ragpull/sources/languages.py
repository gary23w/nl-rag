"""Every other language a swarm might be asked to write: JVM, .NET, functional, lisp family,
scripting, mobile, scientific, assembly, and the legacy canon. Names match nl-veil atlas entries."""

from .common import BSD, CC_BY_SA, GFDL, MIT, WIKI, wiki, wikibooks

ORACLE_TUT = "https://docs.oracle.com/javase/tutorial/"

DOMAINS = {
    # ------------------------------------------------------------------ jvm & .net
    "java": {
        "tags": ["java", "jdk", "javase", "jvm"],
        "license": "Oracle-BCL (tutorial excerpts) / " + CC_BY_SA,
        "pages": [
            ORACLE_TUT + "java/concepts/index.html",
            ORACLE_TUT + "java/nutsandbolts/datatypes.html",
            ORACLE_TUT + "java/nutsandbolts/flow.html",
            ORACLE_TUT + "java/javaOO/classes.html",
            ORACLE_TUT + "java/IandI/createinterface.html",
            ORACLE_TUT + "java/generics/types.html",
            ORACLE_TUT + "collections/interfaces/index.html",
            ORACLE_TUT + "essential/exceptions/definition.html",
            ORACLE_TUT + "essential/concurrency/threads.html",
            WIKI + "Java_(programming_language)",
            WIKI + "Java_virtual_machine",
        ],
    },
    "kotlin": {
        "tags": ["kotlin", "kotlinlang", "kotlin multiplatform"],
        "license": "Apache-2.0",
        "pages": [
            "https://kotlinlang.org/docs/basic-syntax.html",
            "https://kotlinlang.org/docs/classes.html",
            "https://kotlinlang.org/docs/null-safety.html",
            "https://kotlinlang.org/docs/collections-overview.html",
            "https://kotlinlang.org/docs/coroutines-overview.html",
            "https://kotlinlang.org/docs/functions.html",
        ],
    },
    "scala": {
        "tags": ["scala", "scala 3", "sbt"],
        "license": CC_BY_SA,
        "pages": [
            "https://docs.scala-lang.org/scala3/book/introduction.html",
            "https://docs.scala-lang.org/scala3/book/taste-intro.html",
            "https://docs.scala-lang.org/scala3/book/first-look-at-types.html",
            "https://docs.scala-lang.org/scala3/book/fun-anonymous-functions.html",
            "https://docs.scala-lang.org/tour/pattern-matching.html",
            WIKI + "Scala_(programming_language)",
        ],
    },
    "clojure": {
        "tags": ["clojure", "clojurescript", "leiningen"],
        "license": "EPL-1.0 (docs) / " + CC_BY_SA,
        "pages": [
            "https://clojure.org/about/rationale",
            "https://clojure.org/reference/reader",
            "https://clojure.org/reference/data_structures",
            "https://clojure.org/guides/learn/syntax",
            "https://clojure.org/guides/learn/functions",
            WIKI + "Clojure",
        ],
    },
    "csharp-dotnet": {
        "tags": ["csharp", "c#", "dotnet", ".net framework"],
        "license": CC_BY_SA + " (learn.microsoft CC-BY-4.0)",
        "pages": [
            "https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/overview",
            "https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/",
            "https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/program-structure/",
            "https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/",
            "https://learn.microsoft.com/en-us/dotnet/standard/linq/",
            WIKI + "C_Sharp_(programming_language)",
        ],
    },
    # ------------------------------------------------------------------ functional & lisp family
    "haskell": {
        "tags": ["haskell", "ghc", "hackage", "cabal"],
        "license": CC_BY_SA + " (Wikibooks)",
        "pages": wikibooks(
            "Haskell/Variables_and_functions",
            "Haskell/Type_basics",
            "Haskell/Lists_and_tuples",
            "Haskell/Pattern_matching",
            "Haskell/Higher-order_functions",
            "Haskell/Understanding_monads",
        ) + wiki("Haskell", "Monad_(functional_programming)"),
    },
    "ocaml": {
        "tags": ["ocaml", "opam", "dune build"],
        "license": CC_BY_SA,
        "pages": [
            "https://ocaml.org/docs/tour-of-ocaml",
            "https://ocaml.org/docs/values-and-functions",
            "https://ocaml.org/docs/basic-data-types",
            "https://ocaml.org/docs/lists",
            WIKI + "OCaml",
        ],
    },
    "elixir": {
        "tags": ["elixir", "hexdocs", "iex"],
        "license": "Apache-2.0",
        "pages": [
            "https://hexdocs.pm/elixir/introduction.html",
            "https://hexdocs.pm/elixir/basic-types.html",
            "https://hexdocs.pm/elixir/pattern-matching.html",
            "https://hexdocs.pm/elixir/modules-and-functions.html",
            "https://hexdocs.pm/elixir/processes.html",
            WIKI + "Elixir_(programming_language)",
        ],
    },
    "erlang": {
        "tags": ["erlang", "erlang otp", "gen_server", "beam vm"],
        "license": "Apache-2.0 / " + CC_BY_SA,
        "pages": [
            "https://www.erlang.org/doc/system/seq_prog.html",
            "https://www.erlang.org/doc/system/conc_prog.html",
            WIKI + "Erlang_(programming_language)",
            WIKI + "Actor_model",
        ],
    },
    "racket": {
        "tags": ["racket", "scheme language", "drracket"],
        "license": MIT + "/Apache-2.0 / " + CC_BY_SA,
        "pages": [
            "https://docs.racket-lang.org/guide/intro.html",
            WIKI + "Racket_(programming_language)",
            WIKI + "Scheme_(programming_language)",
        ],
    },
    "common-lisp": {
        "tags": ["common lisp", "hyperspec", "clos", "sbcl"],
        "license": CC_BY_SA,
        "pages": [
            "https://lispcookbook.github.io/cl-cookbook/getting-started.html",
            "https://lispcookbook.github.io/cl-cookbook/functions.html",
            "https://lispcookbook.github.io/cl-cookbook/data-structures.html",
            "https://lispcookbook.github.io/cl-cookbook/clos.html",
            WIKI + "Common_Lisp",
            WIKI + "Lisp_(programming_language)",
        ],
    },
    # ------------------------------------------------------------------ scripting & general purpose
    "perl-docs": {
        "tags": ["perl", "perldoc", "perl script", "perl module", "cpan"],
        "license": "GPL-1.0-or-later OR Artistic-1.0",
        "pages": [
            "https://perldoc.perl.org/perlintro",
            "https://perldoc.perl.org/perlsyn",
            "https://perldoc.perl.org/perldata",
            "https://perldoc.perl.org/perlre",
            "https://perldoc.perl.org/perlsub",
        ],
    },
    "lua": {
        "tags": ["lua", "lua scripting", "lua manual", "programming in lua"],
        "license": MIT + " / " + CC_BY_SA,
        "pages": [
            "https://www.lua.org/manual/5.4/manual.html",
            WIKI + "Lua_(programming_language)",
        ],
    },
    "php-manual": {
        "tags": ["php", "php manual", "php function", "php script"],
        "license": "PHP-3.01 (docs CC-BY-3.0)",
        "pages": [
            "https://www.php.net/manual/en/language.types.intro.php",
            "https://www.php.net/manual/en/language.variables.basics.php",
            "https://www.php.net/manual/en/functions.user-defined.php",
            "https://www.php.net/manual/en/functions.arguments.php",
            "https://www.php.net/manual/en/language.oop5.basic.php",
            "https://www.php.net/manual/en/language.exceptions.php",
        ],
    },
    "typescript-docs": {
        "tags": ["typescript", "tsconfig", "tsc", "typescript type annotations", "typescript type system"],
        "license": "Apache-2.0",
        "pages": [
            "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html",
            "https://www.typescriptlang.org/docs/handbook/2/narrowing.html",
            "https://www.typescriptlang.org/docs/handbook/2/functions.html",
            "https://www.typescriptlang.org/docs/handbook/2/objects.html",
            "https://www.typescriptlang.org/docs/handbook/2/classes.html",
            "https://www.typescriptlang.org/docs/handbook/2/generics.html",
        ],
    },
    # ------------------------------------------------------------------ mobile & scientific
    "swift-language": {
        "tags": ["swift language", "swiftui", "ios"],
        "license": "Apache-2.0 / " + CC_BY_SA,
        "pages": [
            "https://www.swift.org/getting-started/",
            WIKI + "Swift_(programming_language)",
        ],
    },
    "dart": {
        "tags": ["dart language", "dart sdk", "dartlang"],
        "license": "CC-BY-4.0",
        "pages": [
            "https://dart.dev/language",
            "https://dart.dev/language/variables",
            "https://dart.dev/language/functions",
            "https://dart.dev/language/error-handling",
            "https://dart.dev/language/async",
        ],
    },
    "r-language": {
        "tags": ["r language", "rstats", "cran", "statistical computing"],
        "license": GFDL,
        "pages": [
            "https://cran.r-project.org/doc/manuals/r-release/R-intro.html",
            WIKI + "R_(programming_language)",
        ],
    },
    "julia": {
        "tags": ["julia language", "julialang"],
        "license": MIT,
        "pages": [
            "https://docs.julialang.org/en/v1/manual/getting-started/",
            "https://docs.julialang.org/en/v1/manual/variables/",
            "https://docs.julialang.org/en/v1/manual/functions/",
            "https://docs.julialang.org/en/v1/manual/types/",
            "https://docs.julialang.org/en/v1/manual/arrays/",
        ],
    },
    # ------------------------------------------------------------------ assembly & the machine
    "x86-assembly": {
        "tags": ["x86 assembly", "assembly language", "x86", "x86-64", "amd64", "asm"],
        "license": CC_BY_SA,
        "pages": wiki(
            "X86",
            "X86_assembly_language",
            "X86_instruction_listings",
            "X86_calling_conventions",
            "Assembly_language",
        ) + wikibooks(
            "X86_Assembly/X86_Architecture",
            "X86_Assembly/GNU_assembly_syntax",
            "X86_Assembly/Control_Flow",
        ),
    },
    "arm-riscv": {
        "tags": ["arm architecture", "aarch64", "risc-v", "riscv", "cortex-m", "instruction set"],
        "license": CC_BY_SA,
        "pages": wiki(
            "ARM_architecture_family",
            "AArch64",
            "RISC-V",
            "Reduced_instruction_set_computer",
            "Instruction_set_architecture",
            "ARM_Cortex-M",
            "Endianness",
        ),
    },
    # ------------------------------------------------------------------ the legacy & paradigm canon
    "legacy-languages": {
        "tags": ["fortran", "cobol", "ada language", "pascal", "smalltalk", "prolog", "forth language", "apl"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Fortran",
            "COBOL",
            "Ada_(programming_language)",
            "Pascal_(programming_language)",
            "BASIC",
            "Smalltalk",
            "Prolog",
            "Forth_(programming_language)",
            "APL_(programming_language)",
            "ALGOL",
        ),
    },
    "webassembly-docs": {
        "tags": ["webassembly", "wasm", "wasm module", "linear memory"],
        "license": "CC-BY-SA-2.5 (MDN) / " + CC_BY_SA,
        "pages": [
            "https://developer.mozilla.org/en-US/docs/WebAssembly/Guides/Concepts",
            "https://developer.mozilla.org/en-US/docs/WebAssembly/Guides/Understanding_the_text_format",
            WIKI + "WebAssembly",
        ],
    },
}
