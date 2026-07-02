---
title: "Architecture"
source: https://docs.pinecone.io/reference/architecture/serverless-architecture
domain: pinecone
license: CC-BY-SA-4.0
tags: pinecone vector db, managed vector database, vector similarity search, locality-sensitive hashing
fetched: 2026-07-02
---

# Architecture

Get started

# Architecture

Learn how Pinecone’s architecture enables fast, relevant vector search at any scale.

## Overview

Pinecone runs as a managed service on AWS, GCP, and Azure cloud platforms. When you send a request to Pinecone, it goes through an

API gateway

that routes it to either a global

control plane

or a regional

data plane

. All your vector data is stored in highly efficient, distributed

object storage

.

### API gateway

Every request to Pinecone includes an

API key

that’s assigned to a specific

project

. The API gateway first validates your API key to make sure you have permission to access the project. Once validated, it routes your request to either the global control plane (for managing projects and indexes) or a regional data plane (for reading and writing data), depending on what you’re trying to do.

### Control plane

The global control plane manages your organizational resources like projects and indexes. It uses a dedicated database to keep track of all these objects. The control plane also handles billing, user management, and coordinates operations across different regions.

### Data plane

The data plane handles all requests to write and read records in

indexes

within a specific

cloud region

. Each index is divided into one or more logical

namespaces

, and all your data read and write requests target a specific namespace.

Pinecone separates write and read operations into different paths, with each scaling independently based on demand. This separation ensures that your queries never slow down your writes, and your writes never slow down your queries.

### Object storage

For each namespace in a serverless index, Pinecone organizes records into immutable files called slabs. These slabs are

optimized for fast querying

and stored in distributed object storage that provides virtually unlimited scalability and high availability.

## Write path

### Request log

When you send a write request (to add, update, or delete records), the

data plane

first logs the request details with a unique sequence number (LSN). This ensures all operations happen in the correct order and provides a way to track the state of the index.

Pinecone immediately returns a

200 OK

response, guaranteeing that your write is durable and won’t be lost. The system then processes your write in the background.

### Index builder

The index builder stores your write data in an in-memory structure called a memtable. This includes your vector data, any metadata you’ve attached, and the sequence number. If you’re updating or deleting a record, the system also tracks how to handle the old version during queries.

Periodically, the index builder moves data from the memtable to permanent storage. In

object storage

, your data is organized into immutable files called slabs. These slabs are optimized for query performance. Smaller slabs use fast indexing techniques that provide good performance with minimal resource requirements. As slabs grow, the system merges them into larger slabs that use more sophisticated methods that provide better performance at scale. This adaptive process both optimizes query performance for each slab and amortizes the cost of more expensive indexing through the lifetime of the namespace.

All read operations check the memtable first, so you can immediately search data that you’ve just written, even before it’s moved to permanent storage. For more details, see

Query executors

.

## Read path

### Query routers

When you send a search query, the

data plane

first validates your request and checks that it meets system limits like

rate and object limits

. The query router then identifies which slabs contain relevant data and routes your query to the appropriate executors. It also searches the memtable for any recent data that hasn’t been moved to permanent storage yet.

### Query executors

Each query executor searches through its assigned slabs and returns the most relevant candidates to the query router. If your query includes metadata filters, the executors exclude records that don’t match your criteria before finding the best matches.

Most of the time, the slabs are cached in memory or on local SSD, which provides very fast query performance. If a slab isn’t cached (which happens when it’s accessed for the first time or hasn’t been used recently), the executor fetches it from object storage and caches it for future queries.

The query router then combines results from all executors, removes duplicates, merges them with results from the memtable, and returns the final set of best matches to you.

⌘

I
