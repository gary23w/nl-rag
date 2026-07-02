---
title: "Cypher (query language)"
source: https://en.wikipedia.org/wiki/Cypher_(query_language)
domain: neo4j
license: CC-BY-SA-4.0
tags: neo4j, cypher query language, property graph, graph database
fetched: 2026-07-02
---

# Cypher (query language)

**Cypher** is a declarative graph query language that allows for expressive and efficient data querying in a property graph.

Cypher was largely an invention of Andrés Taylor while working for Neo4j, Inc. (formerly Neo Technology) in 2011. Cypher was originally intended to be used with the graph database Neo4j, but was opened up through the openCypher project in October 2015.

The language was designed with the power and capability of SQL (standard query language for the relational database model) in mind, but Cypher was based on the components and needs of a database built upon the concepts of graph theory. In a graph model, data is structured as nodes (vertices in math and network science) and relationships (edges in math and network science) to focus on how entities in the data are connected and related to one another.

## Graph model

Cypher is based on the Property Graph Model, which organizes data into nodes and edges (called “relationships” in Cypher). In addition to those standard graph elements of nodes and relationships, the property graph model adds labels and properties for describing finer categories and attributes of the data.

Nodes are the entities in the graph. They can hold any number of attributes (key-value pairs) called properties. Nodes can be tagged with zero or more labels (like tags or categories), representing their different roles in a domain. Relationships provide directed, named, semantically-relevant connections between two node entities. A relationship always has a direction, a start node, an end node, and exactly one relationship type. Like nodes, relationships can also have properties.

Labels can group similar nodes together by assigning zero or more node labels. Labels are kind of like tags and allow you to specify certain types of entities to look for or create. Properties are key-value pairs with a binding of a string key and some value from the Cypher type system. Cypher queries are assembled with patterns of nodes and relationships with any specified filtering on labels and properties to create, read, update, delete data found in the specified pattern.

### Data type system

The Cypher's data type system includes many of the common data types used in other programming and query languages. Supported data types include scalar value types such as boolean, string, number, integer, and floating-point numbers. It also supports temporal types like `datetime`, `localdatetime`, date, time, localtime, and duration. Container data types for maps and lists are available, along with graph types for node, relationship, path, and a void type.

## Syntax

The Cypher query language depicts patterns of nodes and relationships and filters those patterns based on labels and properties. Cypher’s syntax is based on ASCII art, which is text-based visual art for computers. This makes the language very visual and easy to read because it both visually and structurally represents the data specified in the query. For instance, nodes are represented with parentheses around the attributes and information regarding the entity. Relationships are depicted with an arrow (either directed or undirected) with the relationship type in brackets.

```mw
//node
(variable:Label {propertyKey: 'propertyValue'})

//relationship
-[variable:RELATIONSHIP_TYPE]->

//Cypher pattern
(node1:LabelA)-[rel1:RELATIONSHIP_TYPE]->(node2:LabelB)
```

### Keywords

Similar to other query languages, Cypher contains a variety of keywords for specifying patterns, filtering patterns, and returning results. Among those most common are: MATCH, WHERE, and RETURN. These operate slightly differently than the SELECT and WHERE in SQL; however, they have similar purposes.

MATCH is used before describing the search pattern for finding nodes, relationships, or combinations of nodes and relationships together. WHERE in Cypher is used to add additional constraints to patterns and filter out any unwanted patterns. Cypher’s RETURN formats and organizes how the results should be outputted. Just as with other query languages, you can return the results with specific properties, lists, ordering, and more.

Using the keywords with the pattern syntax shown above, the example query below will search for the pattern of the node (Actor label and property called name with value of 'Nicole Kidman') connected by a relationship (ACTED_IN type and outgoing direction away from the first node) to another node (Movie label). The WHERE clause then filters to only keep patterns where the Movie node in the match clause has a year property that is less than the value of the parameter passed in. In the return, the query specifies to output the movie nodes that fit the pattern and filtering from the match and where clauses.

```mw
MATCH (nicole:Actor {name: 'Nicole Kidman'})-[:ACTED_IN]->(movie:Movie)
WHERE movie.year < $yearParameter
RETURN movie
```

Cypher also contains keywords to specify clauses for writing, updating, and deleting data. CREATE and DELETE are used to create and delete nodes and relationships. SET and REMOVE are used to set values to properties and add/delete labels on nodes. MERGE is used to create nodes uniquely without duplicates. Nodes can only be deleted when they have no other relationships still existing. For example:

```mw
MATCH (startContent:Content)-[relationship:IS_RELATED_TO]->(endContent:Content)
WHERE endContent.source = 'user'
OPTIONAL MATCH (endContent)-[r]-()
DELETE relationship, endContent
```

## Standardization

With the openCypher project, an effort began to standardize Cypher as the query language for graph processing. As part of this process there have been five face-to-face openCypher Implementers Meetings (oCIMs). The first meeting took place in February 2017 at SAP's headquarters in Walldorf in Germany, coincident with a meeting of the Linked Data Benchmark Council. The most recent OCIM took place in Berlin, coincident with the W3C Workshop on Web Standards for Graph Data Management, in March 2019.

At that meeting, there was a consensus to work towards Cypher becoming a significant input into a wider project for an international standardized Graph Query Language called GQL. In September 2019, a proposal for a GQL standard project was approved by a vote of national standards bodies which are members of ISO/IEC Joint Technical Committee 1 (responsible for information technology standards). The GQL project proposal states the following:

> Using graph as a fundamental representation for data modeling is an emerging approach in data management. In this approach, the data set is modeled as a graph, representing each data entity as a vertex (also called a node) of the graph and each relationship between two entities as an edge between corresponding vertices. The graph data model has been drawing attention for its unique advantages. Firstly, the graph model can be a natural fit for data sets that have hierarchical, complex, or even arbitrary structures. Such structures can be easily encoded into the graph model as edges. This can be more convenient than the relational model, which requires the normalization of the data set into a set of tables with fixed row types. Secondly, the graph model enables efficient execution of expensive queries or data analytic functions that need to observe multi-hop relationships among data entities, such as reachability queries, shortest or cheapest path queries, or centrality analysis. There are two graph models in current use: the Resource Description Framework (RDF) model and the Property Graph model. The RDF model has been standardized by W3C in a number of specifications. The Property Graph model, on the other hand, has a multitude of implementations in graph databases, graph algorithms, and graph processing facilities. However, a common, standardized query language for property graphs (like SQL for relational database systems) is missing. GQL is proposed to fill this void.

As of 2024, the GQL Standard has been published as the standard graph query language under ISO/IEC 39075:2024. The first open-source implementation of a subset of the language is already available. Aside from the implementation, one can also find a formalization and read the syntax of the specific subset of GQL.
