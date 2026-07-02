---
title: "What is graph data modeling?"
source: https://neo4j.com/docs/getting-started/data-modeling/
domain: neo4j
license: CC-BY-SA-4.0
tags: neo4j, cypher query language, property graph, graph database
fetched: 2026-07-02
---

# What is graph data modeling?

Data modeling is a practice that defines the logic of queries and the structure of the data in storage. A well-designed model is the key to leveraging the strengths of a graph database as it improves query performance, supports flexible queries, and optimizes storage.

In summary, the process of creating a data model includes the following:

1. Understand the domain and define specific use cases (questions) for the application.
2. Develop an initial graph data model by extracting entities and decide how they relate to each other.
3. Test the use cases against the initial data model.
4. Create the graph with test data using Cypher®.
5. Test the use cases, including performance against the graph.
6. Refactor the graph data model due to changes in the key use cases or for performance reasons.

For a full tutorial, refer to Create a data model.

## Keep learning

For a more hands-on approach to data modeling, try the following resources:

- GraphAcademy: Data Modeling Fundamentals: enroll to an interactive course.
- From relational to graph: learn how to adapt data from a relational to a graph data model.
- Data modeling tools: see a list of tools you can use to create your data model.
- Data modeling tips: check tips on how to improve your data modeling skills.
- Modeling designs: see examples of data modeling designs that can be used as strategy for your project.
- Neo4j GraphGists: find examples of graph data modeling shared by the Neo4j community.

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
