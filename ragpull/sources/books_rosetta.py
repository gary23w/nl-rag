"""Open-licensed book content (Wikibooks, CC-BY-SA) and Rosetta Code cross-language tasks
(GFDL-1.2). Book chapters fold conceptual depth into topic packs; Rosetta gives the same
problem solved in dozens of languages — paradigm literacy in one page."""

from .common import CC_BY_SA, GFDL12, wikibooks

ROSETTA = "https://rosettacode.org/wiki/"

DOMAINS = {
    "c-book": {
        "tags": ["c pointers", "c arrays", "c memory management", "c strings"],
        "license": CC_BY_SA + " (Wikibooks C Programming)",
        "pages": wikibooks(
            "C_Programming/Variables",
            "C_Programming/Pointers_and_arrays",
            "C_Programming/Memory_management",
            "C_Programming/String_manipulation",
            "C_Programming/Program_flow_control",
            "C_Programming/Standard_libraries",
            "C_Programming/Code_style",
            "C_Programming/Preprocessor_directives_and_macros",
            "C_Programming/Common_practices",
        ),
    },
    "os-book": {
        "tags": ["operating system design", "kernel design", "process management"],
        "license": CC_BY_SA + " (Wikibooks OS Design)",
        "pages": wikibooks(
            "Operating_System_Design/Kernel_Architecture",
            "Operating_System_Design/Initialization",
            "Operating_System_Design/Memory_Management",
            "Microprocessor_Design",
        ),
    },
    "embedded-book": {
        "tags": ["embedded programming", "interrupt service routine", "embedded c"],
        "license": CC_BY_SA + " (Wikibooks Embedded Systems)",
        "pages": wikibooks(
            "Embedded_Systems/Embedded_Systems_Introduction",
            "Embedded_Systems/Microprocessor_Introduction",
            "Embedded_Systems/Interrupts",
            "Embedded_Systems/Memory",
            "Embedded_Systems/Real-Time_Operating_Systems",
            "Embedded_Systems/Common_Protocols",
        ),
    },
    "rosetta-code": {
        "tags": ["rosetta code", "cross-language comparison", "polyglot example"],
        "license": GFDL12,
        "pages": [
            ROSETTA + "FizzBuzz",
            ROSETTA + "Fibonacci_sequence",
            ROSETTA + "100_doors",
            ROSETTA + "Towers_of_Hanoi",
            ROSETTA + "Binary_search",
            ROSETTA + "Sorting_algorithms/Quicksort",
            ROSETTA + "Sieve_of_Eratosthenes",
            ROSETTA + "Dining_philosophers",
            ROSETTA + "Ackermann_function",
            ROSETTA + "99_Bottles_of_Beer",
        ],
    },
}
