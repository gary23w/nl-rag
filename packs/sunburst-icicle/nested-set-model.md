---
title: "Nested set model"
source: https://en.wikipedia.org/wiki/Nested_set_model
domain: sunburst-icicle
license: CC-BY-SA-4.0
tags: sunburst chart, icicle diagram, radial hierarchy, nested rings
fetched: 2026-07-02
---

# Nested set model

The **nested set model** is a technique for representing nested set collections (also known as trees or hierarchies) in relational databases.

It is based on Nested Intervals, that "are immune to hierarchy reorganization problem, and allow answering ancestor path hierarchical queries algorithmically — without accessing the stored hierarchy relation".

## Motivation

The standard relational algebra and relational calculus, and the SQL operations based on them, are unable to express directly all desirable operations on hierarchies. The nested set model is a solution to that problem.

An alternative solution is the expression of the hierarchy as a parent-child relation. Joe Celko called this the adjacency list model. If the hierarchy can have arbitrary depth, the adjacency list model does not allow the expression of operations such as comparing the contents of hierarchies of two elements, or determining whether an element is somewhere in the subhierarchy of another element. When the hierarchy is of fixed or bounded depth, the operations are possible, but expensive, due to the necessity of performing one relational join per level. This is often known as the bill of materials problem.

Hierarchies may be expressed easily by switching to a graph database. Alternatively, several resolutions exist for the relational model and are available as a workaround in some relational database management systems:

- support for a dedicated hierarchy data type, such as in SQL's hierarchical query facility;
- extending the relational language with hierarchy manipulations, such as in the nested relational algebra.
- extending the relational language with transitive closure, such as SQL's CONNECT statement; this allows a parent-child relation to be used, but execution remains expensive;
- the queries can be expressed in a language that supports iteration and is wrapped around the relational operations, such as PL/SQL, T-SQL or a general-purpose programming language

When these solutions are not available or not feasible, another approach must be taken.

## Technique

The nested set model is to number the nodes according to a tree traversal, which visits each node twice, assigning numbers in the order of visiting, and at both visits. This leaves two numbers for each node, which are stored as two attributes. Querying becomes inexpensive: hierarchy membership can be tested by comparing these numbers. Updating requires renumbering and is therefore expensive. Refinements that use rational numbers instead of integers can avoid renumbering, and so are faster to update, although much more complicated.

## Example

In a clothing store catalog, clothing may be categorized according to the hierarchy given on the left:

| Node | Left | Right |
|---|---|---|
| Clothing | 1 | 22 |
| Men's | 2 | 9 |
| Women's | 10 | 21 |
| Suits | 3 | 8 |
| Slacks | 4 | 5 |
| Jackets | 6 | 7 |
| Dresses | 11 | 16 |
| Skirts | 17 | 18 |
| Blouses | 19 | 20 |
| Evening Gowns | 12 | 13 |
| Sun Dresses | 14 | 15 |

The "Clothing" category, with the highest position in the hierarchy, encompasses all subordinating categories. It is therefore given left and right domain values of 1 and 22, the latter value being the double of the total number of nodes being represented. The next hierarchical level contains "Men's" and "Women's", both containing levels within themselves that must be accounted for. Each level's data node is assigned left and right domain values according to the number of sublevels contained within, as shown in the table data.

## Performance

Queries using nested sets can be expected to be faster than queries using a stored procedure to traverse an adjacency list, and so are the faster option for databases which lack native recursive query constructs, such as MySQL 5.x. However, recursive SQL queries can be expected to perform comparably for 'find immediate descendants' queries, and much faster for other depth search queries, and so are the faster option for databases which provide them, such as PostgreSQL, Oracle, and Microsoft SQL Server. MySQL used to lack recursive query constructs but added such features in version 8.

## Drawbacks

The use case for a dynamic endless database tree hierarchy is rare. The Nested Set model is appropriate where the tree element and one or two attributes are the only data, but is a poor choice when more complex relational data exists for the elements in the tree. Given an arbitrary starting depth for a category of 'Vehicles' and a child of 'Cars' with a child of 'Mercedes', a foreign key table relationship must be established unless the tree table is natively non-normalized. Attributes of a newly created tree item may not share all attributes with a parent, child or even a sibling. If a foreign key table is established for a table of 'Plants' attributes, no integrity is given to the child attribute data of 'Trees' and its child 'Oak'. Therefore, in each case of an item inserted into the tree, a foreign key table of the item's attributes must be created for all but the most trivial of use cases.

If the tree isn't expected to change often, a properly normalized hierarchy of attribute tables can be created in the initial design of a system, leading to simpler, more portable SQL statements; specifically ones that don't require an arbitrary number of runtime, programmatically created or deleted tables for changes to the tree. For more complex systems, hierarchy can be developed through relational models rather than an implicit numeric tree structure. Depth of an item is simply another attribute rather than the basis for an entire DB architecture. As stated in *SQL Antipatterns*:

> Nested Sets is a clever solution – maybe too clever. It also fails to support referential integrity. It’s best used when you need to query a tree more frequently than you need to modify the tree.

The model doesn't allow for multiple parent categories. For example, an 'Oak' could be a child of 'Tree-Type', but also 'Wood-Type'. An additional tagging or taxonomy has to be established to accommodate this, again leading to a design more complex than a straightforward fixed model.

Nested sets are very slow for inserts because it requires updating left and right domain values for all records in the table after the insert. This can cause a lot of database stress as many rows are rewritten and indexes rebuilt. However, if it is possible to store a forest of small trees in table instead of a single big tree, the overhead may be significantly reduced, since only one small tree must be updated.

The nested interval model does not suffer from this problem, but is more complex to implement, and is not as well known. It still suffers from the relational foreign-key table problem. The nested interval model stores the position of the nodes as rational numbers expressed as quotients (n/d).

## Variations

Using the nested set model as described above has some performance limitations during certain tree traversal operations. For example, trying to find the immediate child nodes given a parent node requires pruning the subtree to a specific level as in the following SQL code example:

```mw
SELECT Child.Node, Child.Left, Child.Right
FROM Tree as Parent, Tree as Child
WHERE
	Child.Left BETWEEN Parent.Left AND Parent.Right
	AND NOT EXISTS (    -- No Middle Node
		SELECT *
		FROM Tree as Mid
		WHERE Mid.Left BETWEEN Parent.Left AND Parent.Right
     			AND Child.Left BETWEEN Mid.Left AND Mid.Right
			AND Mid.Node NOT IN (Parent.Node, Child.Node)
	)
	AND Parent.Left = 1  -- Given Parent Node Left Index
```

Or, equivalently:

```mw
SELECT DISTINCT Child.Node, Child.Left, Child.Right
FROM Tree as Child, Tree as Parent 
WHERE Parent.Left < Child.Left AND Parent.Right > Child.Right  -- associate Child Nodes with ancestors
GROUP BY Child.Node, Child.Left, Child.Right
HAVING max(Parent.Left) = 1  -- Subset for those with the given Parent Node as the nearest ancestor
```

The query will be more complicated when searching for children more than one level deep. To overcome this limitation and simplify tree traversal an additional column is added to the model to maintain the depth of a node within a tree.

| Node | Left | Right | Depth |
|---|---|---|---|
| Clothing | 1 | 22 | 0 |
| Men's | 2 | 9 | 1 |
| Women's | 10 | 21 | 1 |
| Suits | 3 | 8 | 2 |
| Slacks | 4 | 5 | 3 |
| Jackets | 6 | 7 | 3 |
| Dresses | 11 | 16 | 2 |
| Skirts | 17 | 18 | 2 |
| Blouses | 19 | 20 | 2 |
| Evening Gowns | 12 | 13 | 3 |
| Sun Dresses | 14 | 15 | 3 |

In this model, finding the immediate children given a parent node can be accomplished with the following SQL code:

```mw
SELECT Child.Node, Child.Left, Child.Right
FROM Tree as Child, Tree as Parent
WHERE
	Child.Depth = Parent.Depth + 1
	AND Child.Left > Parent.Left
	AND Child.Right < Parent.Right
	AND Parent.Left = 1  -- Given Parent Node Left Index
```
