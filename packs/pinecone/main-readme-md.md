---
title: "python-sdk/README.md at main · pinecone-io/python-sdk · GitHub"
source: https://github.com/pinecone-io/pinecone-python-client/blob/main/README.md
domain: pinecone
license: CC-BY-SA-4.0
tags: pinecone vector db, managed vector database, vector similarity search, locality-sensitive hashing
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

pinecone-io

/

python-sdk

Public

- Notifications You must be signed in to change notification settings
- Fork 130
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

182 lines (128 loc) · 4.09 KB

Outline

# Pinecone Python SDK

The Pinecone Python SDK provides a client for the Pinecone vector database. Use it to create and manage indexes, upsert and query vectors, and run inference operations from Python.

Requires Python 3.10+.

## Installation

```highlight
pip install pinecone
```

For development dependencies (testing, type checking, linting):

```highlight
pip install pinecone[dev]
```

## Quick start

```highlight
from pinecone import Pinecone, ServerlessSpec

# Initialize the client
pc = Pinecone(api_key="your-api-key")

# Create a serverless index
pc.indexes.create(
    name="movie-recommendations",
    dimension=1536,
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-east-1"),
)

# Connect to the index
index = pc.index("movie-recommendations")

# Upsert vectors
index.upsert(
    vectors=[
        ("movie-42", [0.012, -0.087, 0.153]),  # 1536-dim embedding
        ("movie-87", [0.045, 0.021, -0.064]),  # 1536-dim embedding
    ],
    namespace="movies-en",
    batch_size=100,  # split larger inputs into parallel batches automatically
)

# Query for similar vectors
results = index.query(
    vector=[0.012, -0.087, 0.153],  # 1536-dim embedding
    top_k=10,
    namespace="movies-en",
)

for match in results.matches:
    print(f"{match.id}: {match.score:.4f}")
```

## Async usage

The SDK provides an async client for use with `asyncio`:

```highlight
import asyncio
from pinecone import AsyncPinecone

async def main():
    async with AsyncPinecone(api_key="your-api-key") as pc:
        desc = await pc.indexes.describe("movie-recommendations")
        index = await pc.index(host=desc.host)
        async with index:
            results = await index.query(
                vector=[0.012, -0.087, 0.153],  # 1536-dim vector
                top_k=10,
                namespace="movies-en",
            )
            for match in results.matches:
                print(f"{match.id}: {match.score:.4f}")

asyncio.run(main())
```

## Configuration

### API key

Pass the API key directly or set the `PINECONE_API_KEY` environment variable:

```highlight
from pinecone import Pinecone

# Explicit API key
pc = Pinecone(api_key="your-api-key")

# From environment variable (PINECONE_API_KEY)
pc = Pinecone()
```

### Custom host

Connect to a specific control plane host:

```highlight
pc = Pinecone(api_key="your-api-key", host="https://api.pinecone.io")
```

### Timeout

Configure request timeouts in seconds:

```highlight
pc = Pinecone(api_key="your-api-key", timeout=30)
```

### Debug logging

Enable debug logging by setting the `PINECONE_DEBUG` environment variable:

```highlight
export PINECONE_DEBUG=1
```

## Development

### Setup

Clone the repository and install dependencies with uv:

```highlight
uv sync
```

### Tests

```highlight
uv run pytest tests/unit/ -x -v
```

#### Retry/throttle smoke tests (opt-in)

A suite of live-API smoke tests verifies that the retry stack and AIMD adaptive concurrency hold up against real Pinecone rate limits. These are **not** run in normal CI because they require real credentials, create a live serverless index, and take 1–3 minutes per run.

**Required environment variables:**

| Variable | Description |
|---|---|
| `PINECONE_API_KEY` | A valid Pinecone API key |
| `PINECONE_RETRY_SMOKE` | Set to `1` to enable the smoke tests |

**Running the smoke tests:**

```highlight
PINECONE_API_KEY=your-api-key PINECONE_RETRY_SMOKE=1 \
  uv run pytest tests/integration/test_retry_smoke.py -x -v -s
```

**Cost:** Each run creates three serverless indexes, upserts ~100K vectors per index, then deletes all indexes. Total cost is under $3 per run.

**When to run:** Before any release that touches retry logic, HTTP transport, the AIMD adaptive-concurrency limiter (`pinecone._internal.adaptive`), or the batch-upsert path. The unit tests mock HTTP responses; this test catches divergence between the synthetic model and real API behavior (e.g., 503 instead of 429).

### Type checking

```highlight
uv run mypy --strict pinecone/
```

### Linting and formatting

```highlight
uv run ruff check --fix
uv run ruff format
```

## License

Apache-2.0. See LICENSE for details.
