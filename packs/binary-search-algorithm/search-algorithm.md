---
title: "Search algorithm"
source: https://en.wikipedia.org/wiki/Search_algorithm
domain: binary-search-algorithm
license: CC-BY-SA-4.0
tags: binary search, sorted array, logarithmic search, search algorithm
fetched: 2026-07-02
---

# Search algorithm

In computer science, a **search algorithm** is an algorithm designed to solve a search problem. Search algorithms work to retrieve information stored within particular data structure, or calculated in the search space of a problem domain, with either discrete or continuous values.

Although search engines use search algorithms, they belong to the study of information retrieval, not algorithmics.

The appropriate search algorithm to use often depends on the data structure being searched, and may also include prior knowledge about the data. Search algorithms can be made faster or more efficient by specially constructed database structures, such as search trees, hash maps, and database indexes.

Search algorithms can be classified based on their mechanism of searching into three types of algorithms: linear, binary, and hashing. Linear search algorithms check every record for the one associated with a target key in a linear fashion. Binary, or half-interval, searches repeatedly target the center of the search structure and divide the search space in half. Comparison search algorithms improve on linear searching by successively eliminating records based on comparisons of the keys until the target record is found, and can be applied on data structures with a defined order. Digital search algorithms work based on the properties of digits in data structures by using numerical keys. Finally, hashing directly maps keys to records based on a hash function.

Algorithms are often evaluated by their computational complexity, or maximum theoretical run time. Binary search functions, for example, have a maximum complexity of *O*(log *n*), or logarithmic time. In simple terms, the maximum number of operations needed to find the search target is a logarithmic function of the size of the search space.

Specific applications of search algorithms include:

- Problems in combinatorial optimization, such as:
  - The vehicle routing problem, a form of shortest path problem
  - The knapsack problem: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
  - The nurse scheduling problem
- Problems in constraint satisfaction, such as:
  - The map coloring problem
  - Filling in a sudoku or crossword puzzle
- In game theory and especially combinatorial game theory, choosing the best move to make next (such as with the minmax algorithm)
- Finding a combination or password from the whole set of possibilities
- Factoring an integer (an important problem in cryptography)
- Search engine optimization (SEO) and content optimization for web crawlers
- Optimizing an industrial process, such as a chemical reaction, by changing the parameters of the process (like temperature, pressure, and pH)
- Retrieving a record from a database
- Finding the maximum or minimum value in a list or array
- Checking to see if a given value is present in a set of values

## Classes

Algorithms for searching virtual spaces are used in the constraint satisfaction problem, where the goal is to find a set of value assignments to certain variables that will satisfy specific mathematical equations and inequations / equalities. They are also used when the goal is to find a variable assignment that will maximize or minimize a certain function of those variables. Algorithms for these problems include the basic brute-force search (also called "naïve" or "uninformed" search), and a variety of heuristics that try to exploit partial knowledge about the structure of this space, such as linear relaxation, constraint generation, and constraint propagation.

An important subclass are the local search algorithms that view the elements of the search space as the vertices of a graph, with edges defined by a set of heuristics applicable to the case; and scan the space by moving from item to item along the edges, for example according to the steepest descent or best-first criterion, or in a stochastic search. This category includes a great variety of general metaheuristic methods, such as simulated annealing, tabu search, A-teams, and genetic programming, that combine arbitrary heuristics in specific ways. The opposite of local search would be global search methods. This method is applicable when the search space is not limited and all aspects of the given network are available to the entity running the search algorithm.

tree search algorithms are local graph search algorithms designed to work efficiently on directed acyclic graphs with a single root or starting node (trees). Tree search algorithms traverse the nodes of a tree in an particular order prescribed by an algorithm designed for a particular application. Examples of tree search algorithms include exhaustive methods such as depth-first search and breadth-first search, as well as heuristic-based search tree pruning algorithms such as backtracking, branch and bound and alpha-beta_pruning. Unlike metaheuristic algorithms, which may only prescribe a traversal order that is best in some probabilistic sense, many tree-search methods are guaranteed to find the exact optimal solution, if given enough time. In mathematics and logic, this is called a "completeness" guarantee.

Another important sub-class consists of algorithms for exploring the game tree of multiple-player games, such as chess or backgammon, whose nodes consist of all possible game situations that could result from the current situation. The goal in these problems is to find the move that provides the best chance of a win, taking into account all possible moves of the opponent(s). Similar problems occur when humans or machines have to make successive decisions whose outcomes are not entirely under one's control, such as in robot guidance or in marketing, financial, or military strategy planning. This kind of problem — combinatorial search — has been extensively studied in the context of artificial intelligence. Examples of algorithms for this class are the minimax algorithm, alpha–beta pruning, and the A* algorithm and its variants.

### For sub-structures of a given structure

An important and extensively studied subclass are the graph algorithms, in particular graph traversal algorithms, for finding specific sub-structures in a given graph — such as subgraphs, paths, circuits, and so on. Examples include Dijkstra's algorithm, Kruskal's algorithm, the nearest neighbour algorithm, and Prim's algorithm.

Another important subclass of this category are the string searching algorithms, that search for patterns within strings. Two famous examples are the Boyer–Moore and Knuth–Morris–Pratt algorithms, and several algorithms based on the suffix tree data structure.

In 1953, American statistician Jack Kiefer devised Fibonacci search which can be used to find the maximum of a unimodal function and has many other applications in computer science.

### For quantum computers

There are also search methods designed for quantum computers, like Grover's algorithm, that are theoretically faster than linear or brute-force search even without the help of data structures or heuristics. While the ideas and applications behind quantum computers are still entirely theoretical, studies have been conducted with algorithms like Grover's that accurately replicate the hypothetical physical versions of quantum computing systems.
