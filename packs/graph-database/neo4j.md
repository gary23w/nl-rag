---
title: "Neo4j"
source: https://en.wikipedia.org/wiki/Neo4j
domain: graph-database
license: CC-BY-SA-4.0
tags: graph database, property graph, cypher query language, multi-model database
fetched: 2026-07-02
---

# Neo4j

**Neo4j, Inc.** is a global graph intelligence company that provides technology for analyzing and managing connected data.

It is most known for creating the Neo4j Graph database, a graph database management system (GDBMS), which is implemented in Java and accessible from software written in other languages using the Cypher query language through a transactional HTTP endpoint, or through the binary "Bolt" protocol.

The company contributed to the development of the Graph Query Language (GQL), an ISO-standardized query language for property graphs, and is a founding member of the GraphQL Foundation, an open-source initiative under the Linux Foundation.

Graph database management systems, such as the Neo4j Graph Database, are used in artificial intelligence applications to represent and query relationships within connected data.

As of 2024, the company was valued at $2.2 billion with over 800 employees and 1,700 customers globally, with deployments across financial institutions, government, retailers, and technology companies. Neo4j has over 300 enterprise customers, including Adobe, Microsoft, Walmart, UBS, and Daimler Truck.

## History

Neo4j is developed by Neo4j, Inc., headquartered in San Mateo, California, United States, with locations in Sweden, Germany, the United Kingdom, France, Singapore, and Australia.

The company was founded in 2007 in Sweden as an open source project by Emil Eifrem, Johan Svensson, and Peter Neubauer, but the idea for the company dates back to a drawing Eifrem sketched on the back of his napkin during a flight in 2000.

Neo4j was developed as an alternative to traditional tabular databases for use cases in which data relationships are central to the structure and querying of information. It is used in applications such as AI systems, recommendation engines, fraud detection, supply chain, and pharmaceutical research, where traversing relationships between data points is a requirement.

The name combines "Neo," meaning "new," with "4j," a naming convention in the Java community meaning "for Java." The project was originally called “Project Neo,” and the name Neo4j was adopted when the company was formed. The company helped popularize the term “graph database,” thus creating a new market category.

In 2011, the company relocated to Silicon Valley, while its engineering hub remained in Sweden.

In 2016, the Neo4j graph database was used in the analysis of the Panama Papers, a data leak that exposed how wealthy individuals and organizations used offshore financial structures to manage and conceal assets.

In 2017, NASA acknowledged Neo4j’s contribution to Project Orion for its use in retrieving missing data from the Apollo program.

In 2018, the company launched its Graphs4Good program to support social impact and non-corporate use cases.

During the COVID-19 pandemic, Neo4j supported vaccine product development.

Neo4j surpassed $200 million in revenue in 2024, and in 2025, it was reported that 84 of the Fortune 100 and over half of the Fortune 500 use Neo4j’s software to build, orchestrate, and deploy graph databases, including in AI systems at Uber, Walmart, and Daimler Truck.

In 2025, Neo4j announced a $100 million investment in generative AI, including a startup program supporting 1,000 AI-focused companies worldwide; program members include Medium, Shutl (acquired by eBay), and SOUQ (acquired by Amazon). In 2026, the company announced its acquisition of GraphAware, an intelligence analysis software provider for government agencies, as part of its AI investment.

Neo4j participates in the AI Alliance and engages with Linux Foundation projects focused on open-source data and AI ecosystems.

## Funding

Neo4j raised $10.6 million in Series A Funding led by Fidelity Growth Partners Europe in 2011. In November 2012, the company raised $11 million in Series B Funding led by Sunstone Capital. In January 2015, Neo4j secured $20 million in Series C Funding led by Creandum and Dawn Capital.

In November 2016, Neo4j secured $36 million in Series D Funding led by Greenbridge Partners Ltd. In November 2018, Neo4j secured $80 million in Series E Funding led by One Peak Partners and Morgan Stanley Expansion Capital, with participation from other investors including Creandum, Eight Roads and Greenbridge Partners. In June 2021, Neo4j announced $325 million in Series F funding, led by Eurazeo and GV (Alphabet’s venture capital arm), which valued the company at over $2 billion making the company one of the best funded database companies.

In late 2024, the company began preparations for an initial public offering (IPO) on the Nasdaq stock exchange.

By early 2025, the company announced it had surpassed $200 million in Annual Recurring Revenue (ARR). In 2026, the company continues to maintain its position as the most widely deployed graph database, according to industry rankings, while remaining IPO-ready as market conditions for tech listings stabilize.

## Product launches and release history

Neo4j released version 1.0 of its graph database in 2010, version 2.0 in 2013, version 3.0 in 2016, version 3.5 in 2018, aimed at AI and machine learning, and version 4.0 in 2020 with unlimited scaling, partitioning, also known as ‘sharding,’ and role-based access. In 2022, version 5.0 of its graph database was released.

Neo4j launched Ops Manager, a tool to monitor and manage global deployments in a unified dashboard in 2022, and vector search to its graph database in 2023, expanding contextual search for generative AI and large language models.

In 2025, the company launched agentic AI enterprise offerings; Neo4j Aura Agent lets companies build, test, and deploy AI agents using their enterprise data, providing end-to-end automated orchestration and AIOps for graph-based knowledge retrieval. Neo4j also launched Aura Graph Analytics for cloud data warehouses and data lake platforms, including Oracle, Microsoft SQL and OneLake, Databricks, Snowflake, and Google BigQuery.

In September 2025, Neo4j introduced Infinigraph, a scalable graph database architecture designed for operational, analytical and AI workloads at over 100 terabytes and billions of nodes.

## Partnerships

In March 2024, Neo4j and Microsoft announced a collaboration to integrate graph database capabilities into Azure AI services, including Fabric and Azure OpenAI. The integration lets users build knowledge graphs, supporting AI use cases such as GraphRAG.

In June 2024, Neo4j integrated with Snowflake to enable graph analytics and machine learning directly within the Snowflake AI Data Cloud, allowing users access to 65 graph algorithms using SQL.

## Licensing and editions

Neo4j has multiple editions for both its self-managed and fully managed offerings.

As an ACID-compliant transactional database with native graph storage and processing, Neo4j graph database is available in three editions: Community Edition, Enterprise Edition, and Infinigraph Edition. Community Edition is free and open source software under the GNU General Public License version 3 (GPLv3).

The Enterprise and Infinigraph Editions are distributed under a closed-source commercial license and includes additional features related to scalability, performance, operability, and security.

The previous licensing of Enterprise Edition was dual-licensed: GPL v3 (with parts of the code under AGPLv3 with Commons Clause), allowing for clustering, hot backups, and monitoring.

Neo4j AuraDB is available in four tiers: Free, Professional, Business Critical, and Virtual Dedicated Cloud.

## Data structure

The data elements Neo4j stores in its graph database are nodes, edges which connect nodes to one another, and attributes of nodes and edges. Nodes and edges can be labelled. Labels can be used to narrow searches. As of version 2.0, indexing was added to Cypher with the introduction of schemas. Previously, indexes were supported separately from Cypher.

## Criticisms

Database researcher Andy Pavlo from Carnegie Mellon University has questioned graph databases' decision to abandon the longstanding relational model in favor of a custom model. Researchers from CWI benchmarked a modified version of DuckDB against Neo4j on graph-related workloads and found that, despite being an extension of a relational database running SQL, their implementation outperforms Neo4j in a few specific tasks.

Neo4j sued PureThink, for utilizing a power created under the terms of the GNU AGPL, to remove a restrictive Commons clause that Neo4j had added to the AGPL license. The United States District Court for the Northern District of California made a decision on 2024-07-22 to impose $597,000 in actual damages on PureThink, having previously decided that PureThink had violated the DMCA by removing the Commons Clause from Neo4j's AGPL license, and that it had violated trademark law by continuing to use the name Neo4j in selling to government agencies.
