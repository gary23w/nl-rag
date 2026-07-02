---
title: "Pinecone documentation"
source: https://docs.pinecone.io/guides/get-started/overview
domain: pinecone
license: CC-BY-SA-4.0
tags: pinecone vector db, managed vector database, vector similarity search, locality-sensitive hashing
fetched: 2026-07-02
---

# Pinecone documentation

Get started

# Pinecone documentation

Pinecone is the leading vector database for building accurate and performant AI applications at scale in production.

## Database quickstart

Set up a fully managed vector database for high-performance semantic search

## Assistant quickstart

Create an AI assistant that answers complex questions about your proprietary data

## Marketplace quickstart

Publish a no-code knowledge application from a vertical template (public preview)

## Workflows

- Integrated embedding
- Bring your own vectors

Use integrated embedding to upsert and search with text and have Pinecone generate vectors automatically.

1

Create an index

Create an index

that matches your retrieval needs: an

index with a document schema

for

full-text search

on FTS-enabled

string

fields (BM25 ranking, with

dense_vector

and

sparse_vector

fields available in the same schema); an

index with dense vectors

integrated with a

hosted embedding model

for

semantic search

; or an

index with sparse vectors

for

sparse-vector lexical search

with a custom encoder.

2

Prepare data

Prepare

your data for efficient ingestion, retrieval, and management in Pinecone.

3

Upsert text

Upsert

your source text and have Pinecone convert the text to vectors automatically. For full-text search,

upsert typed documents

and Pinecone indexes each field according to the schema.

Use namespaces to partition data

for faster queries and multitenant isolation between customers.

4

Search with text

Search

the index with a query text. Again, Pinecone uses the index’s integrated model to convert the text to a vector automatically.

5

Improve relevance

Filter by metadata

to limit the scope of your search,

rerank results

to increase search accuracy, or use

full-text search

for precise keyword and phrase matching alongside semantic ranking on the same index.

If you use an external embedding model to generate vectors, you can upsert and search with vectors directly.

1

Generate vectors

Use an external embedding model to convert data into dense or sparse vectors.

2

Create an index

Create an index

that matches the characteristics of your embedding model. Dense vectors enable

semantic search

; sparse vectors enable

sparse-vector lexical search

with a custom encoder; or an

index with a document schema

lets you store dense and sparse vectors alongside BM25-indexed

string

fields (declared with

full_text_search

) under one schema, with auto-indexed filterable metadata on every document.

3

Prepare data

Prepare

your data for efficient ingestion, retrieval, and management in Pinecone.

4

Ingest vectors

Load your vectors

and metadata into your index using Pinecone’s import or upsert feature.

Use namespaces to partition data

for faster queries and multitenant isolation between customers.

5

Search with a vector

Use an external embedding model to convert a query text to a vector and

search

the index with the vector.

6

Improve relevance

Filter by metadata

to limit the scope of your search,

rerank results

to increase search accuracy, or add an

index with a document schema

for

full-text search

(or

sparse-vector lexical search

with a custom encoder) to capture precise keyword matches.

## Start building

## IDEs & CLIs

Use Pinecone with agentic IDEs and CLIs like Claude Code, Gemini CLI, and Cursor.

## CLI

Command-line tool for managing Pinecone infrastructure and data.

## API Reference

Comprehensive details about the Pinecone APIs, SDKs, utilities, and architecture.

## Integrated Inference

Simplify vector search with integrated embedding and reranking.

## Examples

Hands-on notebooks and sample apps with common AI patterns and tools.

## Integrations

Pinecone’s growing number of third-party integrations.

## Troubleshooting

Resolve common Pinecone issues with our troubleshooting guide.

## Releases

News about features and changes in Pinecone and related tools.

⌘

I
