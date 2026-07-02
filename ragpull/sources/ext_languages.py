"""Additional programming languages, dialects, and shells."""

from .common import CC_BY_SA, wiki

DOMAINS = {
    "nim-lang": {
        "tags": ["nim language", "nim lang", "nimble", "nim compiler"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Nim_(programming_language)",
            "Systems_programming",
            "Metaprogramming",
        ) + [
            "https://nim-lang.org/docs/tut1.html",
            "https://nim-lang.org/docs/tut2.html",
            "https://nim-lang.org/docs/manual.html",
            "https://nim-lang.org/documentation.html",
        ],
    },
    "crystal-lang": {
        "tags": ["crystal language", "crystal lang", "crystal shards"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Crystal_(programming_language)",
            "Type_inference",
            "Compiled_language",
        ) + [
            "https://crystal-lang.org/reference/",
            "https://crystal-lang.org/reference/1.14/index.html",
            "https://crystal-lang.org/reference/1.14/syntax_and_semantics/index.html",
        ],
    },
    "vlang": {
        "tags": ["vlang", "v lang", "v language"],
        "license": CC_BY_SA,
        "pages": wiki(
            "V_(programming_language)",
            "Systems_programming",
            "Memory_safety",
            "Compiled_language",
        ),
    },
    "odin-lang": {
        "tags": ["odin language", "odin lang", "odin programming"],
        "license": "docs: BSD-3-Clause (odin-lang.org)",
        "pages": wiki(
            "Data-oriented_design",
            "Manual_memory_management",
            "Systems_programming",
            "Video_game_development",
        ) + [
            "https://odin-lang.org/",
            "https://odin-lang.org/docs/",
            "https://odin-lang.org/docs/overview/",
        ],
    },
    "d-language": {
        "tags": ["d language", "d lang", "dlang", "dmd compiler"],
        "license": CC_BY_SA,
        "pages": wiki(
            "D_(programming_language)",
            "Generic_programming",
            "Systems_programming",
        ) + [
            "https://dlang.org/spec/spec.html",
            "https://tour.dlang.org/",
        ],
    },
    "fsharp": {
        "tags": ["f sharp", "fsharp language", "dotnet fsharp", "fsharp lang"],
        "license": CC_BY_SA,
        "pages": wiki(
            "F_Sharp_(programming_language)",
            "Functional_programming",
            "Common_Language_Runtime",
            "Type_inference",
        ) + [
            "https://fsharp.org/",
            "https://learn.microsoft.com/en-us/dotnet/fsharp/",
            "https://learn.microsoft.com/en-us/dotnet/fsharp/language-reference/",
        ],
    },
    "groovy-lang": {
        "tags": ["apache groovy", "groovy language", "groovy lang", "gradle groovy"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Groovy",
            "Java_virtual_machine",
            "Scripting_language",
        ) + [
            "https://groovy-lang.org/documentation.html",
        ],
    },
    "objective-c": {
        "tags": ["objective-c", "objective c", "cocoa framework", "nsobject"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Objective-C",
            "Cocoa_(API)",
            "Clang",
            "LLVM",
        ) + [
            "https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html",
        ],
    },
    "tcl-lang": {
        "tags": ["tcl language", "tcl tk", "tcl script", "tcl interp"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Tcl",
            "Scripting_language",
            "Interpreter_(computing)",
        ) + [
            "https://www.tcl-lang.org/man/tcl8.6/tutorial/tcltutorial.html",
            "https://www.tcl-lang.org/doc/",
            "https://wiki.tcl-lang.org/",
        ],
    },
    "elm-lang": {
        "tags": ["elm language", "elm lang", "elm architecture"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Elm_(programming_language)",
            "Purely_functional_programming",
            "Single-page_application",
        ) + [
            "https://elm-lang.org/docs",
            "https://guide.elm-lang.org/",
        ],
    },
    "purescript": {
        "tags": ["purescript", "pure script language", "purescript lang"],
        "license": CC_BY_SA,
        "pages": wiki(
            "PureScript",
            "Purely_functional_programming",
            "Algebraic_data_type",
        ) + [
            "https://www.purescript.org/",
            "https://book.purescript.org/",
        ],
    },
    "nix-language": {
        "tags": ["nix language", "nix lang", "nixos", "nixpkgs", "nix expression"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Nix_(package_manager)",
            "Purely_functional_programming",
            "Lazy_evaluation",
        ) + [
            "https://nixos.org/manual/nix/stable/",
            "https://nixos.org/manual/nixpkgs/stable/",
        ],
    },
    "raku-lang": {
        "tags": ["raku language", "raku lang", "perl 6", "rakudo"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Raku_(programming_language)",
            "Metaprogramming",
            "Pattern_matching",
        ) + [
            "https://docs.raku.org/",
            "https://docs.raku.org/language",
        ],
    },
    "gleam-lang": {
        "tags": ["gleam language", "gleam lang", "gleam beam"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Gleam_(programming_language)",
            "BEAM_(Erlang_virtual_machine)",
            "Type_inference",
        ) + [
            "https://gleam.run/documentation/",
            "https://gleam.run/book/",
        ],
    },
    "vala-lang": {
        "tags": ["vala language", "vala lang", "gobject vala", "gnome vala"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Vala_(programming_language)",
            "GObject",
            "GTK",
        ) + [
            "https://wiki.gnome.org/Projects/Vala/Tutorial",
            "https://valadoc.org/",
            "https://valadoc.org/glib-2.0/index.htm",
        ],
    },
    "object-pascal": {
        "tags": ["object pascal", "delphi language", "free pascal", "lazarus ide"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Object_Pascal",
            "Delphi_(software)",
            "Pascal_(programming_language)",
            "Turbo_Pascal",
            "Free_Pascal",
            "Lazarus_(IDE)",
        ) + [
            "https://www.freepascal.org/docs.html",
            "https://wiki.freepascal.org/",
        ],
    },
    "visual-basic-net": {
        "tags": ["visual basic net", "vb net", "vb.net language", "dotnet visual basic"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Visual_Basic_.NET",
            ".NET_Framework",
            "Common_Language_Runtime",
        ) + [
            "https://learn.microsoft.com/en-us/dotnet/visual-basic/",
            "https://learn.microsoft.com/en-us/dotnet/visual-basic/programming-guide/",
        ],
    },
    "vba-macros": {
        "tags": ["visual basic for applications", "vba macros", "excel vba", "office vba"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Visual_Basic_for_Applications",
            "Macro_(computer_science)",
            "Microsoft_Excel",
        ) + [
            "https://learn.microsoft.com/en-us/office/vba/api/overview/",
        ],
    },
    "matlab-language": {
        "tags": ["matlab language", "matlab lang", "matlab script", "simulink"],
        "license": CC_BY_SA,
        "pages": wiki(
            "MATLAB",
            "Numerical_analysis",
            "Simulink",
            "Matrix_(mathematics)",
        ),
    },
    "octave-lang": {
        "tags": ["gnu octave", "octave language", "octave script"],
        "license": CC_BY_SA,
        "pages": wiki(
            "GNU_Octave",
            "Numerical_analysis",
            "Matrix_(mathematics)",
        ) + [
            "https://gnu.org/software/octave/doc/interpreter/",
        ],
    },
    "mips-assembly": {
        "tags": ["mips assembly", "mips architecture", "mips isa", "mips instruction set"],
        "license": CC_BY_SA,
        "pages": wiki(
            "MIPS_architecture",
            "Reduced_instruction_set_computer",
            "Instruction_set_architecture",
            "Processor_register",
            "Assembly_language",
        ),
    },
    "retro-6502-assembly": {
        "tags": ["6502 assembly", "mos 6502", "6502 opcode", "6502 processor"],
        "license": CC_BY_SA,
        "pages": wiki(
            "MOS_Technology_6502",
            "Assembly_language",
            "Commodore_64",
            "Nintendo_Entertainment_System",
            "8-bit_computing",
        ),
    },
    "retro-z80-assembly": {
        "tags": ["z80 assembly", "zilog z80", "z80 opcode", "intel 8080"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Zilog_Z80",
            "Intel_8080",
            "Assembly_language",
            "ZX_Spectrum",
            "8-bit_computing",
        ),
    },
    "powershell": {
        "tags": ["powershell", "power shell", "pwsh", "powershell cmdlet"],
        "license": CC_BY_SA,
        "pages": wiki(
            "PowerShell",
            "Command-line_interface",
            "Scripting_language",
        ) + [
            "https://learn.microsoft.com/en-us/powershell/scripting/overview",
            "https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/00-introduction",
        ],
    },
    "zsh-shell": {
        "tags": ["zsh shell", "z shell", "oh my zsh", "zshrc"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Z_shell",
            "Unix_shell",
            "Bourne_shell",
            "Tab_completion",
        ) + [
            "https://zsh.sourceforge.io/Doc/",
        ],
    },
    "fish-shell": {
        "tags": ["fish shell", "friendly interactive shell", "fishshell"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Friendly_interactive_shell",
            "Unix_shell",
            "Command-line_interface",
        ) + [
            "https://fishshell.com/docs/current/index.html",
        ],
    },
    "awk-lang": {
        "tags": ["awk language", "gnu awk", "gawk", "awk script"],
        "license": CC_BY_SA,
        "pages": wiki(
            "AWK",
            "Regular_expression",
            "Sed",
            "Text_editor",
        ) + [
            "https://www.gnu.org/software/gawk/manual/gawk.html",
        ],
    },
    "batch-cmd": {
        "tags": ["batch file", "windows batch", "cmd.exe", "bat script"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Batch_file",
            "Cmd.exe",
            "MS-DOS",
        ) + [
            "https://ss64.com/nt/",
        ],
    },
    "vimscript": {
        "tags": ["vimscript", "vim script", "vimrc", "vim editor"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Vim_(text_editor)",
            "Text_editor",
            "Scripting_language",
        ),
    },
    "emacs-lisp": {
        "tags": ["emacs lisp", "elisp", "gnu emacs", "emacs config"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Emacs_Lisp",
            "GNU_Emacs",
            "Lisp_(programming_language)",
        ) + [
            "https://www.gnu.org/software/emacs/manual/html_node/elisp/index.html",
            "https://www.gnu.org/software/emacs/manual/html_node/emacs/index.html",
        ],
    },
    "autohotkey": {
        "tags": ["autohotkey", "auto hotkey", "ahk script", "hotkey macro"],
        "license": CC_BY_SA,
        "pages": wiki(
            "AutoHotkey",
            "Keyboard_shortcut",
            "Automation",
            "Windows_API",
        ) + [
            "https://www.autohotkey.com/docs/v2/",
            "https://www.autohotkey.com/docs/v1/",
        ],
    },
    "standard-ml": {
        "tags": ["standard ml", "sml language", "sml/nj", "ml programming language"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Standard_ML",
            "ML_(programming_language)",
            "Functional_programming",
            "Type_inference",
        ),
    },
    "idris-lang": {
        "tags": ["idris language", "idris lang", "idris dependent types"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Idris_(programming_language)",
            "Dependent_type",
            "Purely_functional_programming",
        ) + [
            "https://www.idris-lang.org/",
            "https://docs.idris-lang.org/en/latest/",
            "https://www.idris-lang.org/pages/documentation.html",
        ],
    },
    "agda-lang": {
        "tags": ["agda language", "agda lang", "agda proof"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Agda_(programming_language)",
            "Dependent_type",
            "Intuitionistic_type_theory",
        ) + [
            "https://agda.readthedocs.io/en/latest/",
            "https://agda.readthedocs.io/en/v2.6.4/getting-started/index.html",
        ],
    },
    "coq-prover": {
        "tags": ["coq proof assistant", "coq prover", "gallina coq", "rocq prover"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Coq_(software)",
            "Proof_assistant",
            "Calculus_of_constructions",
            "Interactive_theorem_proving",
        ) + [
            "https://coq.inria.fr/doc/",
            "https://coq.inria.fr/refman/",
        ],
    },
    "lean-prover": {
        "tags": ["lean prover", "lean theorem prover", "lean4", "mathlib lean"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Lean_(proof_assistant)",
            "Interactive_theorem_proving",
            "Formal_verification",
        ) + [
            "https://lean-lang.org/",
            "https://leanprover.github.io/theorem_proving_in_lean4/",
        ],
    },
    "carbon-lang": {
        "tags": ["carbon language", "carbon lang", "carbon cpp successor"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Carbon_(programming_language)",
            "Systems_programming",
            "Compiled_language",
        ),
    },
    "mojo-lang": {
        "tags": ["mojo language", "mojo lang", "modular mojo"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Mojo_(programming_language)",
            "Systems_programming",
            "Just-in-time_compilation",
        ) + [
            "https://mojolang.org/",
            "https://docs.modular.com/mojo/manual/",
        ],
    },
    "ballerina-lang": {
        "tags": ["ballerina language", "ballerina lang", "ballerina integration"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Ballerina_(programming_language)",
            "Cloud_computing",
            "Concurrent_computing",
        ) + [
            "https://ballerina.io/learn/",
            "https://ballerina.io/learn/language-basics/",
        ],
    },
    "hack-lang": {
        "tags": ["hack language", "hacklang", "hhvm hack", "facebook hack"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Hack_(programming_language)",
            "HHVM",
            "PHP",
        ) + [
            "https://docs.hhvm.com/hack/",
            "https://docs.hhvm.com/hack/getting-started/getting-started",
        ],
    },
    "abap-lang": {
        "tags": ["abap language", "abap lang", "sap abap", "abap program"],
        "license": CC_BY_SA,
        "pages": wiki(
            "ABAP",
            "SAP_SE",
            "Enterprise_resource_planning",
        ),
    },
    "plsql": {
        "tags": ["pl/sql", "plsql language", "oracle plsql", "plsql block"],
        "license": CC_BY_SA,
        "pages": wiki(
            "PL/SQL",
            "Oracle_Database",
            "Stored_procedure",
            "SQL",
        ) + [
            "https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/index.html",
        ],
    },
    "transact-sql": {
        "tags": ["transact-sql", "t-sql", "tsql language", "sql server tsql"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Transact-SQL",
            "Microsoft_SQL_Server",
            "Stored_procedure",
        ) + [
            "https://learn.microsoft.com/en-us/sql/t-sql/language-reference",
        ],
    },
    "nushell": {
        "tags": ["nushell", "nu shell", "nushell pipeline"],
        "license": "docs: MIT (nushell.sh)",
        "pages": wiki(
            "Shell_(computing)",
            "Command-line_interface",
            "Pipeline_(Unix)",
        ) + [
            "https://www.nushell.sh/",
            "https://www.nushell.sh/book/",
            "https://www.nushell.sh/commands/",
        ],
    },
    "applescript": {
        "tags": ["applescript", "apple script", "osascript", "macos automation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "AppleScript",
            "Scripting_language",
            "Automation",
        ) + [
            "https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html",
        ],
    },
    "wolfram-language": {
        "tags": ["wolfram language", "mathematica language", "wolfram lang", "symbolic wolfram"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Wolfram_Language",
            "Wolfram_Mathematica",
            "Computer_algebra_system",
            "Symbolic_computation",
        ) + [
            "https://reference.wolfram.com/language/",
        ],
    },
    "prolog-lang": {
        "tags": ["prolog language", "prolog lang", "swi-prolog", "logic programming"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Prolog",
            "Logic_programming",
            "Unification_(computer_science)",
            "SWI-Prolog",
        ) + [
            "https://www.swi-prolog.org/pldoc/man?section=quickstart",
        ],
    },
    "scheme-lang": {
        "tags": ["scheme language", "scheme lang", "r7rs scheme", "scheme lisp"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Scheme_(programming_language)",
            "Lisp_(programming_language)",
            "Read%E2%80%93eval%E2%80%93print_loop",
        ) + [
            "https://www.scheme.org/",
            "https://docs.scheme.org/",
        ],
    },
    "forth-lang": {
        "tags": ["forth language", "forth lang", "gforth", "forth stack"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Forth_(programming_language)",
            "Stack-oriented_programming",
            "Reverse_Polish_notation",
        ) + [
            "https://forth-standard.org/",
            "https://gforth.org/manual/",
        ],
    },
    "smalltalk-lang": {
        "tags": ["smalltalk language", "smalltalk lang", "pharo smalltalk", "squeak smalltalk"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Smalltalk",
            "Smalltalk-80",
            "Squeak",
            "Pharo",
            "Object-oriented_programming",
        ) + [
            "https://www.gnu.org/software/smalltalk/manual/html_node/index.html",
        ],
    },
    "apl-array": {
        "tags": ["apl language", "apl array", "apl programming", "dyalog apl"],
        "license": CC_BY_SA,
        "pages": wiki(
            "APL_(programming_language)",
            "Array_programming",
            "J_(programming_language)",
            "K_(programming_language)",
        ),
    },
    "chapel-lang": {
        "tags": ["chapel language", "chapel lang", "chapel parallel", "cray chapel"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Chapel_(programming_language)",
            "Partitioned_global_address_space",
            "Parallel_computing",
            "High-performance_computing",
        ) + [
            "https://chapel-lang.org/docs/",
        ],
    },
    "futhark-lang": {
        "tags": ["futhark language", "futhark lang", "futhark gpu"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Futhark_(programming_language)",
            "Data_parallelism",
            "Purely_functional_programming",
        ) + [
            "https://futhark-lang.org/docs.html",
        ],
    },
}
