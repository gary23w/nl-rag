---
title: "Indexing (part 1/3)"
source: https://qdrant.tech/documentation/concepts/indexing/
domain: qdrant
license: CC-BY-SA-4.0
tags: qdrant, vector database, vector similarity search, approximate nearest neighbor
fetched: 2026-07-02
part: 1/3
---

# Indexing

A key feature of Qdrant is the effective combination of vector and traditional indexes. It is essential to have this because for vector search to work effectively with filters, having a vector index only is not enough. In simpler terms, a vector index speeds up vector search, and payload indexes speed up filtering.

The indexes in the segments exist independently, but the parameters of the indexes themselves are configured for the whole collection.

Not all segments automatically have indexes. Their necessity is determined by the optimizer settings and depends, as a rule, on the number of stored points.


## Payload Index

Payload index in Qdrant is similar to the index in conventional document-oriented databases. This index is built for a specific field and type, and is used for quick point requests by the corresponding filtering condition. The index is also used to accurately estimate the filter cardinality, which helps the query planning choose a search strategy.

Creating an index requires additional computational resources and memory, so choosing fields to be indexed is essential. Qdrant does not make this choice but grants it to the user.

The following field types support payload indexing:

- `keyword` - for keyword payload, affects Match filtering conditions.
- `integer` - for integer payload, affects Match and Range filtering conditions.
- `float` - for float payload, affects Range filtering conditions.
- `bool` - for bool payload, affects Match filtering conditions (available as of v1.4.0).
- `geo` - for geo payload, affects Geo Bounding Box and Geo Radius filtering conditions.
- `datetime` - for datetime payload, affects Range filtering conditions (available as of v1.8.0).
- `text` - a special kind of index, available for keyword / string payloads, affects Full Text search filtering conditions. Read more about text index configuration
- `uuid` - a special type of index, similar to `keyword`, but optimized for UUID values. Affects Match filtering conditions. (available as of v1.11.0)

Payload indexes occupy additional memory and disk space, so it is recommended to only apply payload indexes for those fields that are used in filtering conditions. If you need to filter by many fields and the memory limits do not allow for indexing all of them, it is recommended to choose the field that limits the search result the most. As a rule, the more different values a payload value has, the more efficiently the index will be used.

### Create a Payload Index

To create a payload index for a field:

```http
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": "keyword"
}
```

```python
client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.PayloadSchemaType.KEYWORD,
)
```

```typescript
client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: "keyword",
});
```

```rust
use qdrant_client::qdrant::{CreateFieldIndexCollectionBuilder, FieldType};

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "name_of_the_field_to_index",
            FieldType::Keyword,
        )
        .wait(true),
    )
    .await?;
```

```java
import io.qdrant.client.grpc.Collections.PayloadSchemaType;

client.createPayloadIndexAsync(
    "{collection_name}",
    "name_of_the_field_to_index",
    PayloadSchemaType.Keyword,
    null,
    true,
    null,
    null);
```

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.CreatePayloadIndexAsync(
    collectionName: "{collection_name}",
    fieldName: "name_of_the_field_to_index"
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

client.CreateFieldIndex(context.Background(), &qdrant.CreateFieldIndexCollection{
    CollectionName: "{collection_name}",
    FieldName:      "name_of_the_field_to_index",
    FieldType:      qdrant.FieldType_FieldTypeKeyword.Enum(),
})
```

You can use dot notation to specify a nested field for indexing. Similar to specifying nested filters.

**Payload indexes should be created before ingesting data.** Qdrant’s filterable HNSW index only benefits from additional filter-aware edges when it is generated after the payload indexes have been created. If you create a payload index after data has already been ingested, you need to rebuild the HNSW index to take advantage of the new payload indexes.

### Block Queries That Filter on Unindexed Fields

Queries that filter on unindexed fields are not only slower; they can also unnecessarily consume cluster resources, negatively impacting the latency of other search queries. To prevent that, Qdrant provides an option to block queries that filter on unindexed fields. This gives you:

- Fail-fast behavior: Queries that would degrade performance are rejected at the API boundary, surfacing misconfigured indexes as errors rather than latency spikes.
- Performance guarantees: Every query that succeeds is backed by an index, preventing accidental filters on unindexed fields from reaching production.
- Operational visibility: Without strict mode, a missing index might go unnoticed for a long time because queries still return results, albeit slowly.

To block queries that filter on unindexed fields, enable strict mode and set `unindexed_filtering_retrieve` to `false`. Qdrant will then return an error if a search query attempts to filter on an unindexed field. On Qdrant Cloud, these settings are applied to all collections by default.

For more information, refer to Disable Retrieving via Non Indexed Payload.

### Parameterized Index

*Available as of v1.8.0*

We’ve added a parameterized variant to the `integer` index, which allows you to fine-tune indexing and search performance.

Both the regular and parameterized `integer` indexes use the following flags:

- `lookup`: enables support for direct lookup using Match filters.
- `range`: enables support for Range filters.

The regular `integer` index assumes both `lookup` and `range` are `true`. In contrast, to configure a parameterized index, you would set only one of these filters to `true`:

| `lookup` | `range` | Result |
|---|---|---|
| `true` | `true` | Regular integer index |
| `true` | `false` | Parameterized integer index |
| `false` | `true` | Parameterized integer index |
| `false` | `false` | No integer index |

Setting `lookup` or `range` to `false` may help to tune and reduce memory usage in large collections. We encourage you to try out if setting either to `false` improves memory usage. If you don’t see an improvement or if you’re not sure what kind of payload filters you’re using, use the regular `integer` index.

Note: If you set `"range": false` and still use a range filter, it may lead to significant performance issues. The same is true for the lookup parameter and its respective filters.

For example, the following code sets up a parameterized integer index which supports only range filters:

```http
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": {
        "type": "integer",
        "lookup": false,
        "range": true
    }
}
```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.IntegerIndexParams(
        type=models.IntegerIndexType.INTEGER,
        lookup=False,
        range=True,
    ),
)
```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: {
    type: "integer",
    lookup: false,
    range: true,
  },
});
```

```rust
use qdrant_client::Qdrant;
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder, FieldType, IntegerIndexParamsBuilder,
};

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "name_of_the_field_to_index",
            FieldType::Integer,
        )
        .field_index_params(IntegerIndexParamsBuilder::new(false, true).build()),
    )
    .await?;
```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.IntegerIndexParams;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "name_of_the_field_to_index",
        PayloadSchemaType.Integer,
        PayloadIndexParams.newBuilder()
            .setIntegerIndexParams(
                IntegerIndexParams.newBuilder().setLookup(false).setRange(true).build())
            .build(),
        null,
        null,
        null)
    .get();
```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreatePayloadIndexAsync(
    collectionName: "{collection_name}",
    fieldName: "name_of_the_field_to_index",
    schemaType: PayloadSchemaType.Integer,
    indexParams: new PayloadIndexParams
    {
	    IntegerIndexParams = new()
	    {
		    Lookup = false,
		    Range = true
	    }
    }
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

client.CreateFieldIndex(context.Background(), &qdrant.CreateFieldIndexCollection{
	CollectionName: "{collection_name}",
	FieldName:      "name_of_the_field_to_index",
	FieldType:      qdrant.FieldType_FieldTypeInteger.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsInt(
		&qdrant.IntegerIndexParams{
			Lookup: qdrant.PtrOf(false),
			Range:  qdrant.PtrOf(true),
		}),
})
```

### On-Disk Payload Index

*Available as of v1.11.0*

By default all payload-related structures are stored in memory. In this way, the vector index can quickly access payload values during search. As latency in this case is critical, it is recommended to keep hot payload indexes in memory.

There are, however, cases when payload indexes are too large or rarely used. In those cases, it is possible to store payload indexes on disk.

To configure on-disk payload index, you can use the following index parameters:

```http
PUT /collections/{collection_name}/index
{
    "field_name": "payload_field_name",
    "field_schema": {
        "type": "keyword",
        "on_disk": true
    }
}
```

```python
client.create_payload_index(
    collection_name="{collection_name}",
    field_name="payload_field_name",
    field_schema=models.KeywordIndexParams(
        type=models.KeywordIndexType.KEYWORD,
        on_disk=True,
    ),
)
```

```typescript
client.createPayloadIndex("{collection_name}", {
  field_name: "payload_field_name",
  field_schema: {
    type: "keyword",
    on_disk: true
  },
});
```

```rust
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder,
    KeywordIndexParamsBuilder,
    FieldType
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.create_field_index(
    CreateFieldIndexCollectionBuilder::new(
        "{collection_name}",
        "payload_field_name",
        FieldType::Keyword,
    )
    .field_index_params(
        KeywordIndexParamsBuilder::default()
            .on_disk(true),
    ),
).await?;
```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.KeywordIndexParams;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "payload_field_name",
        PayloadSchemaType.Keyword,
        PayloadIndexParams.newBuilder()
            .setKeywordIndexParams(
                KeywordIndexParams.newBuilder()
                    .setOnDisk(true)
                    .build())
            .build(),
        null,
        null,
        null)
    .get();
```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreatePayloadIndexAsync(
 collectionName: "{collection_name}",
 fieldName: "payload_field_name",
 schemaType: PayloadSchemaType.Keyword,
 indexParams: new PayloadIndexParams
 {
  KeywordIndexParams = new KeywordIndexParams
  {
   OnDisk   = true
  }
 }
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

client.CreateFieldIndex(context.Background(), &qdrant.CreateFieldIndexCollection{
	CollectionName: "{collection_name}",
	FieldName:      "name_of_the_field_to_index",
	FieldType:      qdrant.FieldType_FieldTypeKeyword.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsKeyword(
		&qdrant.KeywordIndexParams{
			OnDisk: qdrant.PtrOf(true),
		}),
})
```

Payload index on-disk is supported for the following types:

- `keyword`
- `integer`
- `float`
- `datetime`
- `uuid`
- `text`
- `geo`

The list will be extended in future versions.

### Tenant Index

*Available as of v1.11.0*

Many vector search use-cases require multitenancy. In a multi-tenant scenario the collection is expected to contain multiple subsets of data, where each subset belongs to a different tenant.

Qdrant supports efficient multi-tenant search by enabling special configuration vector index, which disables global search and only builds sub-indexes for each tenant.

However, knowing that the collection contains multiple tenants unlocks more opportunities for optimization. To optimize storage in Qdrant further, you can enable tenant indexing for payload fields.

This option will tell Qdrant which fields are used for tenant identification and will allow Qdrant to structure storage for faster search of tenant-specific data. One example of such optimization is localizing tenant-specific data closer on disk, which will reduce the number of disk reads during search.

To enable tenant index for a field, you can use the following index parameters:

```http
PUT /collections/{collection_name}/index
{
    "field_name": "payload_field_name",
    "field_schema": {
        "type": "keyword",
        "is_tenant": true
    }
}
```

```python
client.create_payload_index(
    collection_name="{collection_name}",
    field_name="payload_field_name",
    field_schema=models.KeywordIndexParams(
        type=models.KeywordIndexType.KEYWORD,
        is_tenant=True,
    ),
)
```

```typescript
client.createPayloadIndex("{collection_name}", {
  field_name: "payload_field_name",
  field_schema: {
    type: "keyword",
    is_tenant: true
  },
});
```

```rust
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder,
    KeywordIndexParamsBuilder,
    FieldType
};

use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.create_field_index(
    CreateFieldIndexCollectionBuilder::new(
        "{collection_name}",
        "payload_field_name",
        FieldType::Keyword,
    )
    .field_index_params(
        KeywordIndexParamsBuilder::default()
            .is_tenant(true),
    ),
).await?;
```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.KeywordIndexParams;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "payload_field_name",
        PayloadSchemaType.Keyword,
        PayloadIndexParams.newBuilder()
            .setKeywordIndexParams(
                KeywordIndexParams.newBuilder()
                    .setIsTenant(true)
                    .build())
            .build(),
        null,
        null,
        null)
    .get();
```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreatePayloadIndexAsync(
 collectionName: "{collection_name}",
 fieldName: "payload_field_name",
 schemaType: PayloadSchemaType.Keyword,
 indexParams: new PayloadIndexParams
 {
  KeywordIndexParams = new KeywordIndexParams
  {
   IsTenant = true
  }
 }
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

client.CreateFieldIndex(context.Background(), &qdrant.CreateFieldIndexCollection{
	CollectionName: "{collection_name}",
	FieldName:      "name_of_the_field_to_index",
	FieldType:      qdrant.FieldType_FieldTypeKeyword.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsKeyword(
		&qdrant.KeywordIndexParams{
			IsTenant: qdrant.PtrOf(true),
		}),
})
```

Tenant optimization is supported for the following datatypes:

- `keyword`
- `uuid`

### Principal Index

*Available as of v1.11.0*

Similar to the tenant index, the principal index is used to optimize storage for faster search, assuming that the search request is primarily filtered by the principal field.

A good example of a use case for the principal index is time-related data, where each point is associated with a timestamp. In this case, the principal index can be used to optimize storage for faster search with time-based filters.

```http
PUT /collections/{collection_name}/index
{
    "field_name": "timestamp",
    "field_schema": {
        "type": "integer",
        "is_principal": true
    }
}
```

```python
client.create_payload_index(
    collection_name="{collection_name}",
    field_name="timestamp",
    field_schema=models.IntegerIndexParams(
        type=models.IntegerIndexType.INTEGER,
        is_principal=True,
    ),
)
```

```typescript
client.createPayloadIndex("{collection_name}", {
  field_name: "timestamp",
  field_schema: {
    type: "integer",
    is_principal: true
  },
});
```

```rust
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder,
    IntegerIndexParamsBuilder,
    FieldType
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.create_field_index(
    CreateFieldIndexCollectionBuilder::new(
        "{collection_name}",
        "timestamp",
        FieldType::Integer,
    )
    .field_index_params(
        IntegerIndexParamsBuilder::default()
            .is_principal(true),
    ),
).await?;
```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.IntegerIndexParams;
import io.qdrant.client.grpc.Collections.KeywordIndexParams;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "timestamp",
        PayloadSchemaType.Integer,
        PayloadIndexParams.newBuilder()
            .setIntegerIndexParams(
                IntegerIndexParams.newBuilder()
                    .setIsPrincipal(true)
                    .build())
            .build(),
        null,
        null,
        null)
    .get();
```

```csharp
using Qdrant.Client;
using Qdrant.Client.Grpc;

var client = new QdrantClient("localhost", 6334);

await client.CreatePayloadIndexAsync(
 collectionName: "{collection_name}",
 fieldName: "timestamp",
 schemaType: PayloadSchemaType.Integer,
 indexParams: new PayloadIndexParams
 {
  IntegerIndexParams = new IntegerIndexParams
  {
   IsPrincipal = true
  }
 }
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

client.CreateFieldIndex(context.Background(), &qdrant.CreateFieldIndexCollection{
	CollectionName: "{collection_name}",
	FieldName:      "name_of_the_field_to_index",
	FieldType:      qdrant.FieldType_FieldTypeInteger.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsInt(
		&qdrant.IntegerIndexParams{
			IsPrincipal: qdrant.PtrOf(true),
		}),
})
```

Principal optimization is supported for following types:

- `integer`
- `float`
- `datetime`
