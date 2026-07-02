---
title: "What is Cypher?"
source: https://neo4j.com/docs/getting-started/cypher/
domain: neo4j
license: CC-BY-SA-4.0
tags: neo4j, cypher query language, property graph, graph database
fetched: 2026-07-02
---

# What is Cypher?

|   | This page covers the basics of Cypher®. For the complete documentation, refer to the Cypher Manual. |
|---|---|

Figure 1. A visual representation of a Cypher query

Cypher is Neo4j’s declarative and GQL conformant query language. Available as open source via The openCypher project, Cypher is similar to SQL, but optimized for graphs.

Intuitive and close to natural language, Cypher provides a visual way of matching patterns and relationships by having its own design based on ASCII-art type of syntax:

```cypher
(:nodes)-[:ARE_CONNECTED_TO]->(:otherNodes)
```

Round brackets are used to represent `(:Nodes)`, and square brackets `-[]→` to represent a relationship between the `(:Nodes)`. With this query syntax, you can perform create, read, update, or delete (CRUD) operations on your graph.

|   | To try querying with Cypher, get a free Aura instance, no installation required. Use the graduation cap icon on the top right section to access the interactive guides. The "Query fundamentals" gives you a hands-on introduction to Cypher. |
|---|---|

## How does Cypher work?

The graph is composed of nodes and relationships, which may also have assigned properties. With nodes and relationships, you can build a graph that can express both simple and complex patterns.

Pattern recognition is a key fundamental cognitive process. With Cypher, you can use pattern matching, which in turn makes the learning process more intuitive.

## Cypher syntax

Cypher’s constructs are close to natural language and the syntax is designed to visually look like a graph.

Figure 2. A graph example involving four nodes and three relationships.

If you want to represent the data in this graph in English, it would read as something like: *"Sally likes Graphs. Sally is friends with John. Sally works for Neo4j."*

Now, if you were to write this same information in Cypher, then it would look like this:

```cypher
(:Sally)-[:LIKES]->(:Graphs)
(:Sally)-[:IS_FRIENDS_WITH]->(:John)
(:Sally)-[:WORKS_FOR]->(:Neo4j)
```

With this query, you turn the information into nodes and relationships, which are the core elements of Cypher.

### Nodes

The main components in a graph are nodes and relationships. Nodes are often used to represent nouns or objects in your data model. In the previous example, `Sally`, `John`, `Graphs`, and `Neo4j` are the nodes:

Figure 3. A visual representation of nodes.

As mentioned previously, nodes are represented as round brackets `(node)` in Cypher. The parentheses are a representation of the circles that compose the nodes in the visualization.

#### Node labels

Nodes can be grouped together through a label, which works like a tag and allows you to specify certain types of entities in your queries. Labels help Cypher distinguish between nodes and optimize execution.

In the example, both `Sally` and `John` are persons, so they get a `Person` label, `Graphs` gets a `Technology` label, and `Neo4j` is a `Company`:

Figure 4. Nodes grouped by labels. Note that

Sally

,

John

,

Graphs

, and

Neo4j

are now

properties

instead.

In a relational database context, this would be the same as using SQL to refer to a particular row in a table. The same way you can use SQL to query a person’s information from a `Person` table, you can also use the `Person` label for that information in Cypher.

|   | If you do not specify a label for Cypher to filter out non-matching node categories, the query will check all of the nodes in the database. This can affect performance in very large graphs. |
|---|---|

#### Node variables

If part of your query matches nodes that you need to reference in a later part of your query (i.e. in a subclause), you can use **node variables**.

Variables can be single letters or words, and should be written in lower-case. For example, if you want to bind all nodes labeled `Person` to the variable `p`, you write `(p:Person)`. If you want to use a full word as a variable, `(person:Person)` works exactly the same.

Retrieve all Person nodes

```cypher
MATCH (p:Person)
RETURN p
```

### Relationships

In a graph database, both nodes and relationships are first-class citizens and they have equal value. In a relational database, relationships are only implied via foreign keys and join tables.

In Cypher, relationships are represented as square brackets with an optional arrow to indicate the direction (e.g. `(Node1)-[]→(Node2)`).

In the example, the arrows connecting the nodes represent the relationship between the nodes:

Figure 5. Graph featuring nodes and relationships.

#### Relationship directions

Relationships **always** have a direction which is indicated by an arrow.

They can go from left to right:

```cypher
(p:Person)-[:LIKES]->(t:Technology)
```

From right to left:

```cypher
(p:Person)<-[:LIKES]-(t:Technology)
```

Or be undirected (where the direction is **not** specified):

```cypher
MATCH (p:Person)-[:LIKES]-(t:Technology)
```

#### Undirected relationships

An undirected relationship does not mean that it doesn’t have a direction, but that it can be traversed in **either** direction. While you can’t **create** relationships without a direction, you can **query** them undirected (in the example, using the `MATCH` clause).

Since Cypher won’t return anything if you write a query with the wrong direction, you can use undirected relationships in queries when you don’t know the direction. This way, Cypher will retrieve **all** nodes connected by the specified relationship type, regardless of direction.

|   | Because undirected relationships in queries are traversed twice (once for each direction), the same pattern will be returned twice. This may impact the performance of the query. |
|---|---|

#### Relationship types

Relationship types categorize and add meaning to a relationship, similar to how labels group nodes together. It is considered best practice to use verbs or derivatives for the relationship type. The type describes how the nodes relate to each other. This way, Cypher is almost like natural language, where nodes are the subjects and objects (nouns), and the relationships (verbs) are the predicates that relate them.

In the previous example, the relationship types are:

- `[:LIKES]` - communicates that Sally (a node) *likes* graphs (another node).
- `[:IS_FRIENDS_WITH]` - communicates that Sally *is friends with* John.
- `[:WORKS_FOR]` - communicates that Sally *works for* Neo4j.

|   | Remember to always put a colon in front of a relationship type. If you write `(Person)-[LIKES]→(Technology)`, `[LIKES]` will represent a relationship **variable**, not a relationship **type**. In this case, since no relationship type is declared, Cypher’s `RETURN` clause will search for all types of relationships in order to retrieve a result to your query. |
|---|---|

#### Relationship variables

Variables can be used for relationships in the same way as for nodes. Once you specify a variable, you can use it later in the query to reference the relationship.

Take this example:

```cypher
MATCH (p:Person)-[r:LIKES]->(t:Technology)
RETURN p,r,t
```

This query specifies variables for both the node labels (`p` for `Person` and `t` for `Technology`) and the relationship type (`r` for `:LIKES`). In the return clause, you can then use the variables (i.e. `p`, `r`, and `t`) to return the bound entities.

This would be your result:

Figure 6. Result for the example query using node and relationship variables.

| p | r | t |
|---|---|---|
| `(:Person)` | `[:LIKES]` | `(:Technology)` |
| Rows: 1 |   |   |

### Properties

Properties are used to store additional information and can be added both to nodes and relationships and be of a variety of data types. For a full list of values and types, see Cypher manual → Values and types.

In the following example, `sally` and `john` are variables for `Person` nodes which contain a `name` property with the **property values** "Sally" and "John":

Figure 7. Graph example with node and relationship properties.

To add this info to the graph, you can use the following query:

```cypher
CREATE (sally:Person {name:'Sally'})-[r:IS_FRIENDS_WITH]->(john:Person {name:'John'})
RETURN sally, r, john
```

Properties are enclosed by curly brackets (`{}`), the key is followed by a colon, and the value is enclosed by single or double quotation marks.

In case you have already added Sally and John as node labels, but want to change them into node properties, you need to refactor your graph. Refactoring is a strategy in data modeling that you can learn more about in this tutorial.

### Patterns in Cypher

Graph pattern matching sits at the very core of Cypher. It is the mechanism used to navigate, describe, and extract data from a graph by applying a declarative pattern.

Consider this example:

```cypher
(sally:Person {name:'Sally'})-[l:LIKES]->(g:Technology {type: "Graphs"})
```

This bit of Cypher represents a pattern. It expresses that a `Person` node with *Sally* as its `name` property has a `LIKES` relationship to the `Technology` node with *Graphs* as its `type` property.

You can use this pattern in different queries to the database by adding a keyword to make it a **clause**.

For example, you can add this information to the database with the `CREATE` clause:

```cypher
CREATE (sally:Person {name: "Sally"})-[r:LIKES]->(t:Technology {type: "Graphs"})
```

And once this data is written to the database, you can retrieve it with this pattern:

```cypher
MATCH (sally:Person {name: "Sally"})-[r:LIKES]->(t:Technology {type: "Graphs"})
RETURN sally,r,t
```

#### Pattern variables

In the same way as nodes and relationships, you can also use variables for patterns. Considering the previous example, you can turn the whole pattern (`(Sally)-[:LIKES]→(Technology)`) into a variable (`p`):

```cypher
MATCH p = (sally:Person {name: "Sally"})-[r:LIKES]->(t:Technology {type: "Graphs"})
RETURN p
```

For more information, refer to Cypher manual → Patterns → Syntax and Semantics.

## Keep learning

If you want to learn more about writing Cypher queries, you can take the tutorial on how to Get started with Cypher. In the Cypher manual, you can find more information on:

- How to write basic queries and what clauses you can use to read data from the database.
- How patterns work and how you can use them to navigate, describe and extract data from a graph.
- What values and types, and functions are available in Cypher.

### From SQL to Cypher

In case you have a background in SQL and are new to graph databases, these are some resources for more information on the key differences and the transition to graphs:

- Key differences between Cypher and SQL
- Transition from relational to graph database
- Reference: Comparing Cypher with SQL
- How-to: Import from RDBMS into graph
- How-to: Import from a relational database into Neo4j
- How-to: Model data from relational to graph

### From NoSQL to Graphs

If you are familiar with NoSQL ("Not only SQL") system, you can also learn more on how to make the transition to a graph database.

### GraphAcademy

With the Cypher Fundamentals course, you can learn Cypher in 60 minutes and practice using a sandbox.

### Other resources

For more suggestions on how to expand your knowledge about Cypher, refer to Resources.

## Glossary

**label**

Marks a node as a member of a named and indexed subset. A node may be assigned zero or more labels.

**labels**

A label marks a node as a member of a named and indexed subset. A node may be assigned zero or more labels.

**node**

A node represents an entity or discrete object in your graph data model. Nodes can be connected by relationships, hold data in properties, and are classified by labels.

**nodes**

A node represents an entity or discrete object in your graph data model. Nodes can be connected by relationships, hold data in properties, and are classified by labels.

**relationship**

A relationship represents a connection between nodes in your graph data model. Relationships connect a source node to a target node, hold data in properties, and are classified by type.

**relationships**

A relationship represents a connection between nodes in your graph data model. Relationships connect a source node to a target node, hold data in properties, and are classified by type.

**property**

Properties are key-value pairs that are used for storing data on nodes and relationships.

**properties**

Properties are key-value pairs that are used for storing data on nodes and relationships.

**cluster**

A Neo4j DBMS that spans multiple servers working together to increase fault tolerance and/or read scalability. Databases on a cluster may be configured to replicate across servers in the cluster thus achieving read scalability or high availability.

**clusters**

A Neo4j DBMS that spans multiple servers working together to increase fault tolerance and/or read scalability. Databases on a cluster may be configured to replicate across servers in the cluster thus achieving read scalability or high availability.

**graph**

A logical representation of a set of nodes where some pairs are connected by relationships.

**graphs**

A logical representation of a set of nodes where some pairs are connected by relationships.

**schema**

The prescribed property existence and datatypes for nodes and relationships.

**schemas**

The prescribed property existence and datatypes for nodes and relationships.

**[[database schema]]database schema**

The prescribed property existence and datatypes for nodes and relationships.

**indexes**

Data structure that improves read performance of a database. Read more about supported categories of indexes.

**indexed**

Data structure that improves read performance of a database. Read more about supported categories of indexes.

**constraints**

Constraints are sets of data modeling rules that ensure the data is consistent and reliable. See what constraints are available in Cypher.

**data model**

A data model defines how information is organized in a database. A good data model will make querying and understanding your data easier. In Neo4j, the data models have a graph structure.

**data models**

A data model defines how information is organized in a database. A good data model will make querying and understanding your data easier. In Neo4j, the data models have a graph structure.
