"""How to think: every programming paradigm to ever exist, and the problem-solving canon."""

from .common import CC_BY_SA, wiki

DOMAINS = {
    "paradigms": {
        "tags": ["programming paradigm", "object-oriented", "functional programming", "declarative", "imperative programming"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Programming_paradigm",
            "Object-oriented_programming",
            "Functional_programming",
            "Imperative_programming",
            "Declarative_programming",
            "Procedural_programming",
            "Logic_programming",
            "Event-driven_programming",
            "Reactive_programming",
            "Dataflow_programming",
            "Actor_model",
            "Metaprogramming",
            "Generic_programming",
            "Aspect-oriented_programming",
            "Literate_programming",
            "Structured_programming",
            "Concurrent_computing",
        ),
    },
    "problem-solving": {
        "tags": ["problem solving", "heuristic", "computational thinking", "backtracking", "divide and conquer", "constraint satisfaction"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Problem_solving",
            "How_to_Solve_It",
            "Heuristic",
            "Computational_thinking",
            "Divide-and-conquer_algorithm",
            "Backtracking",
            "Branch_and_bound",
            "Constraint_satisfaction_problem",
            "Boolean_satisfiability_problem",
            "A*_search_algorithm",
            "Minimax",
            "Alpha%E2%80%93beta_pruning",
            "Simulated_annealing",
            "Genetic_algorithm",
            "Hill_climbing",
            "Rubber_duck_debugging",
            "First_principle",
        ),
    },
}
