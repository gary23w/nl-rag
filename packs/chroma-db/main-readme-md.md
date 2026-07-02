---
title: "chroma/README.md at main · chroma-core/chroma · GitHub"
source: https://github.com/chroma-core/chroma/blob/main/README.md
domain: chroma-db
license: CC-BY-SA-4.0
tags: chroma, chromadb, embedding database, vector database
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

chroma-core

/

chroma

Public

- Notifications You must be signed in to change notification settings
- Fork 2.4k
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

78 lines (60 loc) · 3.2 KB

Outline

(Chroma) (Chroma)

**Chroma - the open-source data infrastructure for AI**.

(Discord) | (License) | Docs | Homepage

```highlight
pip install chromadb # python client
# for javascript, npm install chromadb!
# for client-server mode, chroma run --path /chroma_db_path
```

## Chroma Cloud

Our hosted service, Chroma Cloud, powers serverless vector, hybrid, and full-text search. It's extremely fast, cost-effective, scalable and painless. Create a DB and try it out in under 30 seconds with $5 of free credits.

Get started with Chroma Cloud

## API

The core API is only 4 functions (run our 💡 Google Colab):

```highlight
import chromadb
# setup Chroma in-memory, for easy prototyping. Can add persistence easily!
client = chromadb.Client()

# Create collection. get_collection, get_or_create_collection, delete_collection also available!
collection = client.create_collection("all-my-documents")

# Add docs to the collection. Can also update and delete. Row-based API coming soon!
collection.add(
    documents=["This is document1", "This is document2"], # we handle tokenization, embedding, and indexing automatically. You can skip that and add your own embeddings as well
    metadatas=[{"source": "notion"}, {"source": "google-docs"}], # filter on these!
    ids=["doc1", "doc2"], # unique for each doc
)

# Query/search 2 most similar results. You can also .get by id
results = collection.query(
    query_texts=["This is a query document"],
    n_results=2,
    # where={"metadata_field": "is_equal_to_this"}, # optional filter
    # where_document={"$contains":"search_string"}  # optional filter
)
```

Learn about all features on our Docs

## Get involved

Chroma is a rapidly developing project. We welcome PR contributors and ideas for how to improve the project.

- Join the conversation on Discord - `#contributing` channel
- Review the 🛣️ Roadmap and contribute your ideas
- Grab an issue and open a PR - `Good first issue tag`
- Read our contributing guide

**Release Cadence** We currently release new tagged versions of the `pypi` and `npm` packages on Mondays. Hotfixes go out at any time during the week.

## License

Apache 2.0
