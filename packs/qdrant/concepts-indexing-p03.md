---
title: "Indexing (part 3/3)"
source: https://qdrant.tech/documentation/concepts/indexing/
domain: qdrant
license: CC-BY-SA-4.0
tags: qdrant, vector database, vector similarity search, approximate nearest neighbor
fetched: 2026-07-02
part: 3/3
---

## Sparse Vector Index

*Available as of v1.7.0*

Sparse vectors in Qdrant are indexed with a special data structure, which is optimized for vectors that have a high proportion of zeroes. In some ways, this indexing method is similar to the inverted index, which is used in text search engines.

- A sparse vector index in Qdrant is exact, meaning it does not use any approximation algorithms.
- All sparse vectors added to the collection are immediately indexed in the mutable version of a sparse index.

With Qdrant, you can benefit from a more compact and efficient immutable sparse index, which is constructed during the same optimization process as the dense vector index.

This approach is particularly useful for collections storing both dense and sparse vectors.

To configure a sparse vector index, create a collection with the following parameters:

`PUT /collections/{collection_name} { "sparse_vectors": { "text": { "index": { "on_disk": false } } } }``from qdrant_client import QdrantClient, models client = QdrantClient(url="http://localhost:6333") client.create_collection( collection_name="{collection_name}", vectors_config={}, sparse_vectors_config={ "text": models.SparseVectorParams( index=models.SparseIndexParams(on_disk=False), ) }, )``import { QdrantClient, Schemas } from "@qdrant/js-client-rest"; const client = new QdrantClient({ host: "localhost", port: 6333 }); client.createCollection("{collection_name}", { sparse_vectors: { "splade-model-name": { index: { on_disk: false } } } });``use qdrant_client::qdrant::{ CreateCollectionBuilder, SparseIndexConfigBuilder, SparseVectorParamsBuilder, SparseVectorsConfigBuilder, }; use qdrant_client::Qdrant; let client = Qdrant::from_url("http://localhost:6334").build()?; let mut sparse_vectors_config = SparseVectorsConfigBuilder::default(); sparse_vectors_config.add_named_vector_params( "splade-model-name", SparseVectorParamsBuilder::default() .index(SparseIndexConfigBuilder::default().on_disk(true)), ); client .create_collection( CreateCollectionBuilder::new("{collection_name}") .sparse_vectors_config(sparse_vectors_config), ) .await?;``import io.qdrant.client.QdrantClient; import io.qdrant.client.QdrantGrpcClient; import io.qdrant.client.grpc.Collections; QdrantClient client = new QdrantClient( QdrantGrpcClient.newBuilder("localhost", 6334, false).build()); client.createCollectionAsync( Collections.CreateCollection.newBuilder() .setCollectionName("{collection_name}") .setSparseVectorsConfig( Collections.SparseVectorConfig.newBuilder().putMap( "splade-model-name", Collections.SparseVectorParams.newBuilder() .setIndex( Collections.SparseIndexConfig .newBuilder() .setOnDisk(false) .build() ).build() ).build() ).build() ).get();``using Qdrant.Client; using Qdrant.Client.Grpc; var client = new QdrantClient("localhost", 6334); await client.CreateCollectionAsync( collectionName: "{collection_name}", sparseVectorsConfig: ("splade-model-name", new SparseVectorParams{ Index = new SparseIndexConfig { OnDisk = false, } }) );``import ( "context" "github.com/qdrant/go-client/qdrant" ) client, err := qdrant.NewClient(&qdrant.Config{ Host: "localhost", Port: 6334, }) client.CreateCollection(context.Background(), &qdrant.CreateCollection{ CollectionName: "{collection_name}", SparseVectorsConfig: qdrant.NewSparseVectorsConfig( map[string]*qdrant.SparseVectorParams{ "splade-model-name": { Index: &qdrant.SparseIndexConfig{ OnDisk: qdrant.PtrOf(false), }}, }), })``

The following parameters may affect performance:

- `on_disk: true` - The index is stored on disk, which lets you save memory. This may slow down search performance.
- `on_disk: false` - The index is still persisted on disk, but it is also loaded into memory for faster search.

Unlike a dense vector index, a sparse vector index does not require a predefined vector size. It automatically adjusts to the size of the vectors added to the collection.

**Note:** A sparse vector index only supports dot-product similarity searches. It does not support other distance metrics.

### IDF Modifier

*Available as of v1.10.0*

For many search algorithms, it is important to consider how often an item occurs in a collection. Intuitively speaking, the less frequently an item appears in a collection, the more important it is in a search.

This is also known as the Inverse Document Frequency (IDF). It is used in text search engines to rank search results based on the rarity of a word in a collection.

IDF depends on the currently stored documents and therefore can’t be pre-computed in the sparse vectors in streaming inference mode. In order to support IDF in the sparse vector index, Qdrant provides an option to modify the sparse vector query with the IDF statistics automatically.

The only requirement is to enable the IDF modifier in the collection configuration:

```http
PUT /collections/{collection_name}
{
    "sparse_vectors": {
        "text": {
            "modifier": "idf"
        }
    }
}
```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="{collection_name}",
    vectors_config={},
    sparse_vectors_config={
        "text": models.SparseVectorParams(
            modifier=models.Modifier.IDF,
        ),
    },
)
```

```typescript
import { QdrantClient, Schemas } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createCollection("{collection_name}", {
  sparse_vectors: {
    "text": {
      modifier: "idf"
    }
  }
});
```

```rust
use qdrant_client::qdrant::{
    CreateCollectionBuilder, Modifier, SparseVectorParamsBuilder, SparseVectorsConfigBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let mut sparse_vectors_config = SparseVectorsConfigBuilder::default();
sparse_vectors_config.add_named_vector_params(
    "text",
    SparseVectorParamsBuilder::default().modifier(Modifier::Idf),
);

client
    .create_collection(
        CreateCollectionBuilder::new("{collection_name}")
            .sparse_vectors_config(sparse_vectors_config),
    )
    .await?;
```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.CreateCollection;
import io.qdrant.client.grpc.Collections.Modifier;
import io.qdrant.client.grpc.Collections.SparseVectorConfig;
import io.qdrant.client.grpc.Collections.SparseVectorParams;

QdrantClient client =
  new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
  .createCollectionAsync(
    CreateCollection.newBuilder()
    .setCollectionName("{collection_name}")
    .setSparseVectorsConfig(
      SparseVectorConfig.newBuilder()
      .putMap("text", SparseVectorParams.newBuilder().setModifier(Modifier.Idf).build()))
    .build())
  .get();
```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreateCollectionAsync(
  collectionName: "{collection_name}",
  sparseVectorsConfig: ("text", new SparseVectorParams {
    Modifier = Modifier.Idf,
  })
);
```

```go
import (
	"context"

	"github.com/qdrant/go-client/qdrant"
)

client, err := qdrant.NewClient(&qdrant.Config{
	Host: "localhost",
	Port: 6334,
})

client.CreateCollection(context.Background(), &qdrant.CreateCollection{
	CollectionName: "{collection_name}",
	SparseVectorsConfig: qdrant.NewSparseVectorsConfig(
		map[string]*qdrant.SparseVectorParams{
			"text": {
				Modifier: qdrant.Modifier_Idf.Enum(),
			},
		}),
})
```

Qdrant uses the following formula to calculate the IDF modifier:

$$ \text{IDF}(q_i) = \ln \left(\frac{N - n(q_i) + 0.5}{n(q_i) + 0.5}+1\right) $$

Where:

- `N` is the total number of documents in the collection.
- `n` is the number of documents containing non-zero values for the given vector element.
