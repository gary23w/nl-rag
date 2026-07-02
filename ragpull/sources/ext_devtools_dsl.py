"""Config DSLs, policy languages, language-tooling protocols, and compiler infrastructure."""
from .common import CC_BY_SA, APACHE, MIT, BSD, WIKI, wiki

DOMAINS = {
    "hcl-config": {
        "tags": ["hcl config", "hashicorp configuration language",
                 "terraform config syntax", "infrastructure as code"],
        "license": CC_BY_SA,
        "pages": wiki(
            "HCL",
            "Terraform_(software)",
            "Configuration_file",
            "Infrastructure_as_code",
            "Declarative_programming",
            "Configuration_management",
        ),
    },
    "jsonnet": {
        "tags": ["jsonnet language", "data templating language",
                 "json config generation", "google jsonnet"],
        "license": APACHE,
        "pages": wiki(
            "JSON",
            "Domain-specific_language",
            "Template_processor",
            "Declarative_programming",
        ) + [
            "https://jsonnet.org/",
            "https://github.com/google/jsonnet",
        ],
    },
    "dhall-config": {
        "tags": ["dhall config", "dhall language",
                 "total functional configuration", "typed config language"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Total_functional_programming",
            "Domain-specific_language",
            "Configuration_file",
            "Declarative_programming",
            "Type_system",
        ) + [
            "https://dhall-lang.org/",
        ],
    },
    "cue-language": {
        "tags": ["cue language", "cue configuration language",
                 "data validation config", "cuelang schema"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Configuration_file",
            "Data_validation",
            "Domain-specific_language",
            "Declarative_programming",
            "Type_system",
        ) + [
            "https://cuelang.org/docs/",
        ],
    },
    "starlark": {
        "tags": ["starlark language", "bazel build language",
                 "python-like config dialect", "starlark scripting"],
        "license": APACHE,
        "pages": wiki(
            "Domain-specific_language",
            "Build_automation",
            "Bazel_(software)",
            "Declarative_programming",
        ) + [
            "https://github.com/bazelbuild/starlark",
            "https://github.com/bazelbuild/starlark/blob/master/spec.md",
        ],
    },
    "rego-opa-policy": {
        "tags": ["rego policy", "open policy agent", "policy as code",
                 "rego datalog rules"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Datalog",
            "Policy-based_management",
            "Attribute-based_access_control",
            "Authorization",
            "Access-control_list",
        ) + [
            "https://www.openpolicyagent.org/docs/latest/policy-language/",
        ],
    },
    "cedar-policy": {
        "tags": ["cedar policy language", "cedar authorization",
                 "policy as code", "access control policy"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Attribute-based_access_control",
            "Role-based_access_control",
            "Access-control_list",
            "Authorization",
        ) + [
            "https://www.cedarpolicy.com/",
            "https://docs.cedarpolicy.com/",
        ],
    },
    "handlebars-templating": {
        "tags": ["handlebars templating", "handlebars template engine",
                 "logic-less templates", "web template rendering"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Mustache_(template_system)",
            "Web_template_system",
            "Template_processor",
            "Comparison_of_web_template_engines",
            "JavaScript",
        ) + [
            "https://handlebarsjs.com/guide/",
        ],
    },
    "mustache-templating": {
        "tags": ["mustache templating", "mustache template system",
                 "logic-less templates", "web template rendering"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Mustache_(template_system)",
            "Web_template_system",
            "Template_processor",
            "Server-side_scripting",
            "HTML",
        ) + [
            "https://mustache.github.io/mustache.5.html",
        ],
    },
    "liquid-templating": {
        "tags": ["liquid templating", "liquid template language",
                 "shopify liquid", "web template rendering"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Web_template_system",
            "Template_processor",
            "Server-side_scripting",
            "Comparison_of_web_template_engines",
            "Markup_language",
        ) + [
            "https://shopify.github.io/liquid/",
        ],
    },
    "pug-templating": {
        "tags": ["pug templating", "pug template engine",
                 "jade template engine", "html template rendering"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Web_template_system",
            "Template_processor",
            "HTML",
            "Comparison_of_web_template_engines",
            "Node.js",
        ) + [
            "https://pugjs.org/api/getting-started.html",
        ],
    },
    "ejs-templating": {
        "tags": ["ejs templating", "embedded javascript templates",
                 "server-side templates", "web template rendering"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Web_template_system",
            "Server-side_scripting",
            "JavaScript",
            "Comparison_of_web_template_engines",
            "Template_processor",
        ) + [
            "https://ejs.co/",
        ],
    },
    "xslt-stylesheet": {
        "tags": ["xslt stylesheet", "xsl transformations",
                 "xml stylesheet language", "xpath expressions"],
        "license": CC_BY_SA,
        "pages": wiki(
            "XSLT",
            "XPath",
            "XSL",
            "Markup_language",
            "Template_processor",
            "XML",
        ),
    },
    "ansi-escape-codes": {
        "tags": ["ansi escape code", "terminal escape sequences",
                 "ansi color codes", "control character sequences"],
        "license": CC_BY_SA,
        "pages": wiki(
            "ANSI_escape_code",
            "ANSI.SYS",
            "Control_character",
            "Escape_sequence",
            "Terminal_emulator",
            "Character_encoding",
        ),
    },
    "language-server-protocol": {
        "tags": ["language server protocol", "lsp editor tooling",
                 "code intelligence protocol", "json-rpc editor"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Language_Server_Protocol",
            "JSON-RPC",
            "Integrated_development_environment",
            "Autocomplete",
            "Text_editor",
        ) + [
            "https://microsoft.github.io/language-server-protocol/",
        ],
    },
    "debug-adapter-protocol": {
        "tags": ["debug adapter protocol", "dap debugging",
                 "editor debugger integration", "breakpoint protocol"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Debugger",
            "Debugging",
            "Breakpoint",
            "Integrated_development_environment",
            "Stack_trace",
        ) + [
            "https://microsoft.github.io/debug-adapter-protocol/",
        ],
    },
    "tree-sitter-parsing": {
        "tags": ["tree-sitter parser", "incremental parsing",
                 "concrete syntax tree", "editor syntax parsing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Tree-sitter_(parser_generator)",
            "Abstract_syntax_tree",
            "Incremental_computing",
            "Compiler-compiler",
            "Parse_tree",
        ) + [
            "https://tree-sitter.github.io/tree-sitter/",
        ],
    },
    "antlr-parser": {
        "tags": ["antlr parser generator", "ll star parsing",
                 "grammar parser generator", "recursive descent parsing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "ANTLR",
            "LL_parser",
            "Recursive_descent_parser",
            "Formal_grammar",
            "Parsing",
        ) + [
            "https://www.antlr.org/",
        ],
    },
    "lex-yacc": {
        "tags": ["lex yacc", "lexical analyzer generator",
                 "yacc parser generator", "gnu bison"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Lex_(software)",
            "Yacc",
            "GNU_Bison",
            "Lexical_analysis",
            "Compiler-compiler",
            "Deterministic_finite_automaton",
        ),
    },
    "peg-parser": {
        "tags": ["parsing expression grammar", "peg parser",
                 "packrat parsing", "top-down parsing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Parsing_expression_grammar",
            "Packrat_parser",
            "Top-down_parsing_language",
            "Context-free_grammar",
            "Comparison_of_parser_generators",
            "Recursion_(computer_science)",
        ),
    },
    "llvm-infrastructure": {
        "tags": ["llvm infrastructure", "llvm compiler toolchain",
                 "optimizing compiler backend", "clang frontend"],
        "license": CC_BY_SA,
        "pages": wiki(
            "LLVM",
            "Optimizing_compiler",
            "Clang",
            "Register_allocation",
            "Compiler",
        ) + [
            "https://llvm.org/docs/LangRef.html",
        ],
    },
    "llvm-ir": {
        "tags": ["llvm ir", "llvm intermediate representation",
                 "static single assignment", "three-address code"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Intermediate_representation",
            "Static_single-assignment_form",
            "Three-address_code",
            "Control-flow_graph",
            "Optimizing_compiler",
        ) + [
            "https://llvm.org/docs/LangRef.html",
        ],
    },
    "mlir-dialects": {
        "tags": ["mlir dialects", "multi-level ir",
                 "compiler ir framework", "llvm mlir"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Intermediate_representation",
            "Compiler",
            "Optimizing_compiler",
            "LLVM",
            "Code_generation_(compiler)",
        ) + [
            "https://mlir.llvm.org/",
        ],
    },
    "gcc-internals": {
        "tags": ["gcc internals", "gnu compiler collection",
                 "compiler optimization passes", "cross compiler"],
        "license": CC_BY_SA,
        "pages": wiki(
            "GNU_Compiler_Collection",
            "Optimizing_compiler",
            "Cross_compiler",
            "Register_allocation",
            "Assembly_language",
        ) + [
            "https://gcc.gnu.org/onlinedocs/",
        ],
    },
    "wasm-toolchain": {
        "tags": ["webassembly toolchain", "wasm bytecode",
                 "wasm stack machine", "wasm binary format"],
        "license": CC_BY_SA,
        "pages": wiki(
            "WebAssembly",
            "Bytecode",
            "Stack_machine",
            "Just-in-time_compilation",
            "Instruction_set_architecture",
        ) + [
            "https://webassembly.org/",
        ],
    },
    "wasi-interface": {
        "tags": ["wasi interface", "webassembly system interface",
                 "wasm sandbox capabilities", "wasm host abi"],
        "license": CC_BY_SA,
        "pages": wiki(
            "WebAssembly",
            "Sandbox_(computer_security)",
            "Application_binary_interface",
            "Virtual_machine",
            "POSIX",
        ) + [
            "https://wasi.dev/",
        ],
    },
    "wasm-component-model": {
        "tags": ["wasm component model", "webassembly components",
                 "wasm interface types", "component composition wasm"],
        "license": CC_BY_SA,
        "pages": wiki(
            "WebAssembly",
            "Component-based_software_engineering",
            "Interface_(computing)",
            "Application_binary_interface",
            "Type_system",
        ) + [
            "https://component-model.bytecodealliance.org/",
        ],
    },
    "emscripten": {
        "tags": ["emscripten toolchain", "llvm to wasm",
                 "c++ to webassembly", "asm.js compilation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Emscripten",
            "WebAssembly",
            "Source-to-source_compiler",
            "LLVM",
            "Software_portability",
        ) + [
            "https://emscripten.org/docs/introducing_emscripten/about_emscripten.html",
        ],
    },
    "source-maps": {
        "tags": ["source maps", "javascript source mapping",
                 "minified code debugging", "transpiled code mapping"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Minification_(programming)",
            "JavaScript",
            "Debugging",
            "Source-to-source_compiler",
            "TypeScript",
        ) + [
            "https://esbuild.github.io/api/",
        ],
    },
    "ast-transformation": {
        "tags": ["ast transformation", "abstract syntax tree rewriting",
                 "program transformation", "syntax tree rewriting"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Abstract_syntax_tree",
            "Program_transformation",
            "Rewriting",
            "Source-to-source_compiler",
            "Semantic_analysis_(compilers)",
            "Parse_tree",
        ),
    },
    "babel-plugins": {
        "tags": ["babel plugins", "javascript transpiler",
                 "babel transcompiler", "ecmascript downleveling"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Babel_(transcompiler)",
            "Source-to-source_compiler",
            "Abstract_syntax_tree",
            "Plug-in_(computing)",
            "TypeScript",
        ) + [
            "https://babeljs.io/docs/",
        ],
    },
    "swc-compiler": {
        "tags": ["swc compiler", "rust javascript compiler",
                 "fast typescript transpiler", "swc bundler"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Source-to-source_compiler",
            "JavaScript",
            "Abstract_syntax_tree",
            "Compiler",
        ) + [
            "https://swc.rs/",
            "https://swc.rs/docs/getting-started",
        ],
    },
    "esbuild-internals": {
        "tags": ["esbuild bundler", "go javascript bundler",
                 "fast module bundler", "esbuild transform"],
        "license": CC_BY_SA,
        "pages": wiki(
            "JavaScript",
            "Source-to-source_compiler",
            "Minification_(programming)",
            "Compiler",
        ) + [
            "https://esbuild.github.io/",
            "https://esbuild.github.io/api/",
        ],
    },
    "monorepo-nx": {
        "tags": ["nx monorepo", "nx build system",
                 "monorepo task orchestration", "javascript monorepo tooling"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Monorepo",
            "Build_automation",
            "Version_control",
            "Software_repository",
            "Continuous_integration",
        ) + [
            "https://nx.dev/getting-started/intro",
        ],
    },
    "turborepo": {
        "tags": ["turborepo monorepo", "turbo build cache",
                 "monorepo task pipeline", "incremental build cache"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Monorepo",
            "Build_automation",
            "Incremental_computing",
            "Version_control",
            "Cache_(computing)",
        ) + [
            "https://turbo.build/repo/docs",
        ],
    },
    "lerna-monorepo": {
        "tags": ["lerna monorepo", "javascript package publishing",
                 "monorepo package manager", "multi-package repository"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Monorepo",
            "Package_manager",
            "Software_repository",
            "Version_control",
            "Node.js",
        ) + [
            "https://lerna.js.org/docs/introduction",
        ],
    },
    "pants-build": {
        "tags": ["pants build system", "pants monorepo build",
                 "fine-grained build graph", "polyglot build tool"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Build_automation",
            "Monorepo",
            "Software_build",
            "Incremental_computing",
            "Package_manager",
        ) + [
            "https://www.pantsbuild.org/",
        ],
    },
    "buck2-build": {
        "tags": ["buck2 build system", "buck build tool",
                 "hermetic build graph", "meta build system"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Buck_(software)",
            "Build_automation",
            "Software_build",
            "Monorepo",
        ) + [
            "https://buck2.build/",
            "https://buck2.build/docs/",
        ],
    },
    "git-hooks": {
        "tags": ["git hooks", "git commit hooks",
                 "version control hooks", "pre-commit hook scripts"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Git",
            "Hooking",
            "Continuous_integration",
            "Version_control",
            "Continuous_delivery",
        ) + [
            "https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks",
        ],
    },
    "pre-commit-framework": {
        "tags": ["pre-commit framework", "pre-commit hooks",
                 "git hook manager", "code linting hooks"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Git",
            "Hooking",
            "Continuous_integration",
            "Coding_conventions",
            "Text_editor",
        ) + [
            "https://pre-commit.com/",
        ],
    },
    "editorconfig": {
        "tags": ["editorconfig", "editor coding style config",
                 "indentation style config", "cross-editor formatting"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Coding_conventions",
            "Indentation_style",
            "Text_editor",
            "Configuration_file",
            "Whitespace_character",
        ) + [
            "https://editorconfig.org/",
        ],
    },
    "gitignore-patterns": {
        "tags": ["gitignore patterns", "git ignore rules",
                 "glob ignore patterns", "version control exclusion"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Glob_(programming)",
            "Pattern_matching",
            "Git",
            "Filename",
            "Directory_(computing)",
        ) + [
            "https://git-scm.com/docs/gitignore",
        ],
    },
    "dotfiles-management": {
        "tags": ["dotfiles management", "unix dotfiles",
                 "hidden config files", "shell config files"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Hidden_file_and_hidden_directory",
            "Home_directory",
            "Environment_variable",
            "Symbolic_link",
            "Unix_shell",
            "Configuration_file",
        ),
    },
    "shell-completion": {
        "tags": ["shell completion", "command-line completion",
                 "tab completion shells", "bash completion scripts"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Command-line_completion",
            "Autocomplete",
            "Shell_(computing)",
            "Tab_key",
            "Comparison_of_command_shells",
            "POSIX",
        ),
    },
    "terminfo-termcap": {
        "tags": ["terminfo database", "termcap capabilities",
                 "terminal capability database", "terminal control codes"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Terminfo",
            "Termcap",
            "Terminal_emulator",
            "Control_character",
            "Character_encoding",
            "Escape_sequence",
        ),
    },
    "readline-library": {
        "tags": ["gnu readline", "readline line editing",
                 "command-line editing library", "interactive line editor"],
        "license": CC_BY_SA,
        "pages": wiki(
            "GNU_Readline",
            "Line_editor",
            "Command-line_interface",
            "Shell_(computing)",
            "Command_history",
        ) + [
            "https://tiswww.case.edu/php/chet/readline/rltop.html",
        ],
    },
    "ncurses-tui": {
        "tags": ["ncurses library", "curses tui programming",
                 "text-based user interface", "terminal ui library"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Ncurses",
            "Curses_(programming_library)",
            "Text-based_user_interface",
            "Terminal_emulator",
            "Graphical_widget",
        ) + [
            "https://invisible-island.net/ncurses/",
        ],
    },
    "protocol-buffers-idl": {
        "tags": ["protocol buffers", "protobuf idl",
                 "interface description language", "binary serialization schema"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Protocol_Buffers",
            "Interface_description_language",
            "Serialization",
            "Remote_procedure_call",
        ) + [
            "https://protobuf.dev/",
            "https://developers.google.com/protocol-buffers/docs/overview",
        ],
    },
    "thrift-idl": {
        "tags": ["apache thrift", "thrift idl",
                 "cross-language rpc", "thrift interface definition"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Thrift",
            "Interface_description_language",
            "Remote_procedure_call",
            "Serialization",
            "Marshalling_(computer_science)",
        ) + [
            "https://thrift.apache.org/docs/",
        ],
    },
    "openapi-codegen": {
        "tags": ["openapi codegen", "openapi specification",
                 "api client generation", "swagger code generation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "OpenAPI_Specification",
            "Swagger_(software)",
            "Web_API",
            "Automatic_programming",
        ) + [
            "https://openapi-generator.tech/",
            "https://swagger.io/specification/",
        ],
    },
    "code-generation-templates": {
        "tags": ["code generation", "template metaprogramming",
                 "automatic programming", "compiler code generation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Automatic_programming",
            "Template_metaprogramming",
            "Code_generation_(compiler)",
            "Metaprogramming",
            "Macro_(computer_science)",
            "Preprocessor",
        ),
    },
}
