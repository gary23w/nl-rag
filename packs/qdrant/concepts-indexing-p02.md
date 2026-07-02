---
title: "Indexing (part 2/3)"
source: https://qdrant.tech/documentation/concepts/indexing/
domain: qdrant
license: CC-BY-SA-4.0
tags: qdrant, vector database, vector similarity search, approximate nearest neighbor
fetched: 2026-07-02
part: 2/3
---

## Full-Text Index

Qdrant supports full-text search for string payload. Full-text index allows you to filter points by the presence of a word or a phrase in the payload field.

Full-text index configuration is a bit more complex than other indexes, as you can specify the tokenization parameters. Tokenization is the process of splitting a string into tokens, which are then indexed in the inverted index.

See Full Text match for examples of querying with a full-text index.

To create a full-text index, you can use the following:

```http
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": {
        "type": "text",
        "tokenizer": "word",
        "min_token_len": 2,
        "max_token_len": 10,
        "lowercase": true
    }
}
```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.TextIndexParams(
        type=models.TextIndexType.TEXT,
        tokenizer=models.TokenizerType.WORD,
        min_token_len=2,
        max_token_len=10,
        lowercase=True,
    ),
)
```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: {
    type: "text",
    tokenizer: "word",
    min_token_len: 2,
    max_token_len: 10,
    lowercase: true,
  },
});
```

```rust
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder,
    TextIndexParamsBuilder,
    FieldType,
    TokenizerType,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let text_index_params = TextIndexParamsBuilder::new(TokenizerType::Word)
    .min_token_len(2)
    .max_token_len(10)
    .lowercase(true);

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "name_of_the_field_to_index",
            FieldType::Text,
        ).field_index_params(text_index_params.build()),
    )
    .await?;
```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;
import io.qdrant.client.grpc.Collections.TextIndexParams;
import io.qdrant.client.grpc.Collections.TokenizerType;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "name_of_the_field_to_index",
        PayloadSchemaType.Text,
        PayloadIndexParams.newBuilder()
            .setTextIndexParams(
                TextIndexParams.newBuilder()
                    .setTokenizer(TokenizerType.Word)
                    .setMinTokenLen(2)
                    .setMaxTokenLen(10)
                    .setLowercase(true)
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
	fieldName: "name_of_the_field_to_index",
	schemaType: PayloadSchemaType.Text,
	indexParams: new PayloadIndexParams
	{
		TextIndexParams = new TextIndexParams
		{
			Tokenizer = TokenizerType.Word,
			MinTokenLen = 2,
			MaxTokenLen = 10,
			Lowercase = true
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
	FieldType:      qdrant.FieldType_FieldTypeText.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsText(
		&qdrant.TextIndexParams{
			Tokenizer:   qdrant.TokenizerType_Whitespace,
			MinTokenLen: qdrant.PtrOf(uint64(2)),
			MaxTokenLen: qdrant.PtrOf(uint64(10)),
			Lowercase:   qdrant.PtrOf(true),
		}),
})
```

### Tokenizers

Tokenizers are algorithms used to split text into smaller units called tokens, which are then indexed and searched in a full-text index. In the context of Qdrant, tokenizers determine how string payloads are broken down for efficient searching and filtering. The choice of tokenizer affects how queries match the indexed text, supporting different languages, word boundaries, and search behaviours such as prefix or phrase matching.

Available tokenizers are:

- `word` (default) - splits the string into words, separated by spaces, punctuation marks, and special characters.
- `whitespace` - splits the string into words, separated by spaces.
- `prefix` - splits the string into words, separated by spaces, punctuation marks, and special characters, and then creates a prefix index for each word. For example: `hello` will be indexed as `h`, `he`, `hel`, `hell`, `hello`.
- `multilingual` - a special type of tokenizer based on multiple packages like charabia and vaporetto to deliver fast and accurate tokenization for a large variety of languages. It allows proper tokenization and lemmatization for multiple languages, including those with non-Latin alphabets and non-space delimiters. See the charabia documentation for a full list of supported languages and normalization options. Note: For the Japanese language, Qdrant relies on the `vaporetto` project, which has much less overhead compared to `charabia`, while maintaining comparable performance.

### Lowercasing

By default, full-text search in Qdrant is case-insensitive. For example, users can search for the lowercase term `tv` and find text fields containing the uppercase word `TV`. Case-insensitivity is achieved by converting both the words in the index and the query terms to lowercase.

Lowercasing is enabled by default. To use case-sensitive full-text search, configure a full-text index with `lowercase` set to `false`.

```http
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": {
        "type": "text",
        "tokenizer": "word",
        "lowercase": false
    }
}
```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.TextIndexParams(
        type=models.TextIndexType.TEXT,
        tokenizer=models.TokenizerType.WORD,
        lowercase=False,
    ),
)
```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: {
    type: "text",
    tokenizer: "word",
    lowercase: false,
  },
});
```

```rust
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder,
    TextIndexParamsBuilder,
    FieldType,
    TokenizerType,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let text_index_params = TextIndexParamsBuilder::new(TokenizerType::Word)
    .lowercase(false);

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "name_of_the_field_to_index",
            FieldType::Text,
        ).field_index_params(text_index_params.build()),
    )
    .await?;
```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;
import io.qdrant.client.grpc.Collections.TextIndexParams;
import io.qdrant.client.grpc.Collections.TokenizerType;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "name_of_the_field_to_index",
        PayloadSchemaType.Text,
        PayloadIndexParams.newBuilder()
            .setTextIndexParams(
                TextIndexParams.newBuilder()
                    .setTokenizer(TokenizerType.Word)
                    .setLowercase(true)
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
    fieldName: "name_of_the_field_to_index",
    schemaType: PayloadSchemaType.Text,
    indexParams: new PayloadIndexParams
    {
        TextIndexParams = new TextIndexParams
        {
            Tokenizer = TokenizerType.Word,
            Lowercase = true,
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
    FieldType:      qdrant.FieldType_FieldTypeText.Enum(),
    FieldIndexParams: qdrant.NewPayloadIndexParamsText(
        &qdrant.TextIndexParams{
            Tokenizer:   qdrant.TokenizerType_Word,
            Lowercase:   qdrant.PtrOf(true),
        }),
})
```

### ASCII Folding

*Available as of v1.16.0*

When enabled, ASCII folding converts Unicode characters into their corresponding ASCII equivalents, for example, by removing diacritics. For instance, the character `ã` is changed into `a`, `ç` becomes `c`, and `é` is converted to `e`.

Because ASCII folding is applied to both the words in the index and the query terms, it increases recall. For example, users can search for `cafe` and also find text fields containing the word `café`.

ASCII folding is not enabled by default. To enable it, configure a full-text index with `ascii_folding` set to `true`.

```http
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": {
        "type": "text",
        "tokenizer": "word",
        "ascii_folding": true
    }
}
```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.TextIndexParams(
        type=models.TextIndexType.TEXT,
        tokenizer=models.TokenizerType.WORD,
        ascii_folding=True,
    ),
)
```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: {
    type: "text",
    tokenizer: "word",
    ascii_folding: true,
  },
});
```

```rust
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder,
    TextIndexParamsBuilder,
    FieldType,
    TokenizerType,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let text_index_params = TextIndexParamsBuilder::new(TokenizerType::Word)
    .ascii_folding(true);

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "name_of_the_field_to_index",
            FieldType::Text,
        ).field_index_params(text_index_params.build()),
    )
    .await?;
```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;
import io.qdrant.client.grpc.Collections.TextIndexParams;
import io.qdrant.client.grpc.Collections.TokenizerType;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "name_of_the_field_to_index",
        PayloadSchemaType.Text,
        PayloadIndexParams.newBuilder()
            .setTextIndexParams(
                TextIndexParams.newBuilder()
                    .setTokenizer(TokenizerType.Word)
                    .setLowercase(true)
                    .setAsciiFolding(true)
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
    fieldName: "name_of_the_field_to_index",
    schemaType: PayloadSchemaType.Text,
    indexParams: new PayloadIndexParams
    {
        TextIndexParams = new TextIndexParams
        {
            Tokenizer = TokenizerType.Word,
            Lowercase = true,
			AsciiFolding = true,
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
	FieldType:      qdrant.FieldType_FieldTypeText.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsText(
		&qdrant.TextIndexParams{
			Tokenizer:    qdrant.TokenizerType_Word,
			Lowercase:    qdrant.PtrOf(true),
			AsciiFolding: qdrant.PtrOf(true),
		}),
})
```

### Stemmer

A **stemmer** is an algorithm used in text processing to reduce words to their root or base form, known as the “stem.” For example, the words “running”, “runner and “runs” can all be reduced to the stem “run.” When configuring a full-text index in Qdrant, you can specify a stemmer to be used for a particular language. This enables the index to recognize and match different inflections or derivations of a word.

Qdrant provides an implementation of Snowball stemmer, a widely used and performant variant for some of the most popular languages. For the list of supported languages, please visit the rust-stemmers repository.

For full-text indices, stemming is not enabled by default. To enable it, configure the `snowball` stemmer with the desired language:

```http
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": {
        "type": "text",
        "tokenizer": "word",
        "stemmer": {
            "type": "snowball",
            "language": "english"
        }
    }
}
```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.TextIndexParams(
        type=models.TextIndexType.TEXT,
        tokenizer=models.TokenizerType.WORD,
        stemmer=models.SnowballParams(
            type=models.Snowball.SNOWBALL,
            language=models.SnowballLanguage.ENGLISH
        )
    ),
)
```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: {
    type: "text",
    tokenizer: "word",
    stemmer: {
      type: "snowball",
      language: "english"
    }
  }
});
```

```rust
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder,
    TextIndexParamsBuilder,
    FieldType,
    TokenizerType,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let text_index_params = TextIndexParamsBuilder::new(TokenizerType::Word)
    .snowball_stemmer("english".to_string());

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "{field_name}",
            FieldType::Text,
        ).field_index_params(text_index_params.build()),
    )
    .await?;
```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;
import io.qdrant.client.grpc.Collections.SnowballParams;
import io.qdrant.client.grpc.Collections.StemmingAlgorithm;
import io.qdrant.client.grpc.Collections.TextIndexParams;
import io.qdrant.client.grpc.Collections.TokenizerType;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "name_of_the_field_to_index",
        PayloadSchemaType.Text,
        PayloadIndexParams.newBuilder()
            .setTextIndexParams(
                TextIndexParams.newBuilder()
                    .setTokenizer(TokenizerType.Word)
                    .setStemmer(
                        StemmingAlgorithm.newBuilder()
                            .setSnowball(
                                SnowballParams.newBuilder().setLanguage("english").build())
                            .build())
                    .build())
            .build(),
        true,
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
	schemaType: PayloadSchemaType.Text,
	indexParams: new PayloadIndexParams
	{
		TextIndexParams = new TextIndexParams
		{
			Tokenizer = TokenizerType.Word,
			Stemmer = new StemmingAlgorithm
			{
				Snowball = new SnowballParams
				{
					Language = "english"
				}
			}
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
	FieldType:      qdrant.FieldType_FieldTypeText.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsText(
		&qdrant.TextIndexParams{
			Tokenizer: qdrant.TokenizerType_Word,
			Stemmer: qdrant.NewStemmingAlgorithmSnowball(&qdrant.SnowballParams{
				Language: "english",
			}),
		}),
})
```

### Stopwords

Stopwords are common words (such as “the”, “is”, “at”, “which”, and “on”) that are often filtered out during text processing because they carry little meaningful information for search and retrieval tasks.

In Qdrant, you can specify a list of stopwords to be ignored during full-text indexing and search. This helps simplify search queries and improves relevance.

You can configure stopwords based on predefined languages, as well as extend existing stopword lists with custom words.

For full-text indices, stopword removal is not enabled by default. To enable it, configure the `stopwords` parameter with the desired languages and any custom stopwords:

```http
// Simple
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": {
        "type": "text",
        "tokenizer": "word",
        "stopwords": "english"
    }
}

// Explicit
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": {
        "type": "text",
        "tokenizer": "word",
        "stopwords": {
            "languages": [
                "english",
                "spanish"
            ],
            "custom": [
                "example"
            ]
        }
    }
}
```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

# Simple
client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.TextIndexParams(
        type=models.TextIndexType.TEXT,
        tokenizer=models.TokenizerType.WORD,
        stopwords=models.Language.ENGLISH,
    ),
)

# Explicit
client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.TextIndexParams(
        type=models.TextIndexType.TEXT,
        tokenizer=models.TokenizerType.WORD,
        stopwords=models.StopwordsSet(
            languages=[
                models.Language.ENGLISH,
                models.Language.SPANISH,
            ],
            custom=[
                "example"
            ]
        ),
    ),
)
```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

// Simple
client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: {
    type: "text",
    tokenizer: "word",
    stopwords: "english"
  },
});

// Explicit
client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: {
    type: "text",
    tokenizer: "word",
    stopwords: {
      languages: [
        "english",
        "spanish"
      ],
      custom: [
        "example"
      ]
    }
  },
});
```

```rust
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder,
    TextIndexParamsBuilder,
    FieldType,
    TokenizerType,
    StopwordsSet,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

// Simple
let text_index_params = TextIndexParamsBuilder::new(TokenizerType::Word)
    .stopwords_language("english".to_string());

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "name_of_the_field_to_index",
            FieldType::Text,
        ).field_index_params(text_index_params.build()),
    )
    .await?;

// Explicit
let text_index_params = TextIndexParamsBuilder::new(TokenizerType::Word)
    .stopwords(StopwordsSet {
        languages: vec![
            "english".to_string(),
            "spanish".to_string(),
        ],
        custom: vec!["example".to_string()],
    });

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "{field_name}",
            FieldType::Text,
        ).field_index_params(text_index_params.build()),
    )
    .await?;
```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;
import io.qdrant.client.grpc.Collections.StopwordsSet;
import io.qdrant.client.grpc.Collections.TextIndexParams;
import io.qdrant.client.grpc.Collections.TokenizerType;
import java.util.List;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "name_of_the_field_to_index",
        PayloadSchemaType.Text,
        PayloadIndexParams.newBuilder()
            .setTextIndexParams(
                TextIndexParams.newBuilder()
                    .setTokenizer(TokenizerType.Word)
                    .setStopwords(
                        StopwordsSet.newBuilder()
                            .addAllLanguages(List.of("english", "spanish"))
                            .addAllCustom(List.of("example"))
                            .build())
                    .build())
            .build(),
        true,
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
	schemaType: PayloadSchemaType.Text,
	indexParams: new PayloadIndexParams
	{
		TextIndexParams = new TextIndexParams
		{
			Tokenizer = TokenizerType.Word,
			Stopwords = new StopwordsSet
			{
				Languages = { "english", "spanish" },
				Custom = { "example" }
			}
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
	FieldType:      qdrant.FieldType_FieldTypeText.Enum(),
	FieldIndexParams: qdrant.NewPayloadIndexParamsText(
		&qdrant.TextIndexParams{
			Tokenizer: qdrant.TokenizerType_Word,
			Stopwords: &qdrant.StopwordsSet{
				Languages: []string{"english", "spanish"},
				Custom:    []string{"example"},
			},
		}),
})
```

Phrase search in Qdrant allows you to find documents or points where a specific sequence of words appears together, in the same order, within a text payload field. This is useful when you want to match exact phrases rather than individual words scattered throughout the text.

When using a full-text index with phrase search enabled, you can perform phrase search by enclosing the desired phrase in double quotes in your filter query. For example, searching for `"machine learning"` will only return results where the words “machine” and “learning” appear together as a phrase, not just anywhere in the text.

For efficient phrase search, Qdrant requires building an additional data structure, so it needs to be configured during the creation of the full-text index:

```http
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": {
        "type": "text",
        "tokenizer": "word",
        "lowercase": true,
        "phrase_matching": true
    }
}
```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.TextIndexParams(
        type=models.TextIndexType.TEXT,
        tokenizer=models.TokenizerType.WORD,
        lowercase=True,
        phrase_matching=True,
    ),
)
```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: {
    type: "text",
    tokenizer: "word",
    lowercase: true,
    phrase_matching: true,
  },
});
```

```rust
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder,
    TextIndexParamsBuilder,
    FieldType,
    TokenizerType,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

let text_index_params = TextIndexParamsBuilder::new(TokenizerType::Word)
    .phrase_matching(true)
    .lowercase(true);

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "name_of_the_field_to_index",
            FieldType::Text,
        ).field_index_params(text_index_params.build()),
    )
    .await?;
```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;
import io.qdrant.client.grpc.Collections.PayloadIndexParams;
import io.qdrant.client.grpc.Collections.PayloadSchemaType;
import io.qdrant.client.grpc.Collections.TextIndexParams;
import io.qdrant.client.grpc.Collections.TokenizerType;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client
    .createPayloadIndexAsync(
        "{collection_name}",
        "name_of_the_field_to_index",
        PayloadSchemaType.Text,
        PayloadIndexParams.newBuilder()
            .setTextIndexParams(
                TextIndexParams.newBuilder()
                    .setTokenizer(TokenizerType.Word)
                    .setLowercase(true)
                    .setPhraseMatching(true)
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
    fieldName: "name_of_the_field_to_index",
    schemaType: PayloadSchemaType.Text,
    indexParams: new PayloadIndexParams
    {
        TextIndexParams = new TextIndexParams
        {
            Tokenizer = TokenizerType.Word,
            Lowercase = true,
            PhraseMatching = true
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
    FieldType:      qdrant.FieldType_FieldTypeText.Enum(),
    FieldIndexParams: qdrant.NewPayloadIndexParamsText(
        &qdrant.TextIndexParams{
            Tokenizer:   qdrant.TokenizerType_Whitespace,
            Lowercase:   qdrant.PtrOf(true),
            PhraseMatching: qdrant.PtrOf(true),
        }),
})
```

See Phrase Match for examples of querying phrases with a full-text index.


## Vector Index

A vector index is a data structure built on vectors through a specific mathematical model. Through the vector index, we can efficiently query several vectors similar to the target vector.

Qdrant currently only uses HNSW as a dense vector index.

HNSW (Hierarchical Navigable Small World Graph) is a graph-based indexing algorithm. It builds a multi-layer navigation structure for an image according to certain rules. In this structure, the upper layers are more sparse and the distances between nodes are farther. The lower layers are denser and the distances between nodes are closer. The search starts from the uppermost layer, finds the node closest to the target in this layer, and then enters the next layer to begin another search. After multiple iterations, it can quickly approach the target position.

In order to improve performance, HNSW limits the maximum degree of nodes on each layer of the graph to `m`. In addition, you can use `ef_construct` (when building an index) or `ef` (when searching targets) to specify a search range.

The corresponding parameters could be configured in the configuration file:

```yaml
storage:
  # Default parameters of HNSW Index. Could be overridden for each collection or named vector individually
  hnsw_index:
    # Number of edges per node in the index graph.
    # Larger the value - more accurate the search, more space required.
    m: 16
    # Number of neighbours to consider during the index building.
    # Larger the value - more accurate the search, more time required to build index.
    ef_construct: 100
    # Minimal size threshold (in KiloBytes) below which full-scan is preferred over HNSW search.
    # This measures the total size of vectors being queried against.
    # When the maximum estimated amount of points that a condition satisfies is smaller than
    # `full_scan_threshold_kb`, the query planner will use full-scan search instead of HNSW index
    # traversal for better performance.
    # Note: 1Kb = 1 vector of size 256
    full_scan_threshold: 10000
```

And so in the process of creating a collection. The `ef` parameter is configured during the search and by default is equal to `ef_construct`.

HNSW is chosen for several reasons. First, HNSW is well-compatible with the modification that allows Qdrant to use filters during a search. Second, it is one of the most accurate and fastest algorithms, according to public benchmarks.

*Available as of v1.1.1*

The HNSW parameters can also be configured on a collection and named vector level by setting `hnsw_config` to fine-tune search performance.

### Filterable HNSW Index

Separately, a payload index and a vector index cannot completely address the challenges of filtered search.

In the case of high-selectivity (weak) filters, you can use the HNSW index as it is. In the case of low-selectivity (strict) filters, you can use the payload index and do a complete rescore. However, for cases in the middle, this approach does not work well. On one hand, we cannot apply a full scan on too many vectors. On the other hand, the HNSW graph starts to fall apart when using filters that are too strict.

(HNSW fail)

Qdrant solves this problem by extending the HNSW graph with additional edges based on indexed payload values. Extra edges allow you to efficiently search for nearby vectors using the HNSW index and apply filters as you search in the graph. You can find more information on this approach in our article.

*Available as of v1.16.0*

In some cases, the additional edges built for Qdrant’s filterable HNSW may not be sufficient. These extra edges are added for each payload index separately, but not for every possible combination of payload indices. As a result, a combination of two or more strict filters might still lead to disconnected graph components. The same can happen when there are a large number of soft-deleted points in the graph. In such cases, use the ACORN Search Algorithm. When using ACORN, during graph traversal, it explores not just direct neighbors (first hop), but also neighbors of neighbors (second hop) when direct neighbors are filtered out. This improves search accuracy at the cost of performance.

### Disable the Creation of Extra Edges for Payload Fields

*Available as of v1.17.0*

Not all payload indices may be intended for use with dense vector search. For example, when a collection contains both dense and sparse vectors, some payload fields may only be used to filter sparse vector searches. Since sparse vector search does not use the HNSW index, it is unnecessary to build extra edges in the HNSW graph for these fields. Creating extra edges adds indexing latency and increases the size of the HNSW graph, which consumes memory as well as disk space, so you may want to disable it for fields that do not require it.

You can disable the creation of extra edges for an indexed payload field by setting `enable_hnsw` to `false` when configuring a payload index:

```http
PUT /collections/{collection_name}/index
{
    "field_name": "name_of_the_field_to_index",
    "field_schema": {
        "type": "keyword",
        "enable_hnsw": false
    }
}
```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

client.create_payload_index(
    collection_name="{collection_name}",
    field_name="name_of_the_field_to_index",
    field_schema=models.TextIndexParams(
        type=models.TextIndexType.TEXT,
        tokenizer=models.TokenizerType.WORD,
        enable_hnsw=False,
    ),
)
```

```typescript
client.createPayloadIndex("{collection_name}", {
  field_name: "name_of_the_field_to_index",
  field_schema: {
    type: "keyword",
    enable_hnsw: false,
  },
});
```

```rust
use qdrant_client::qdrant::{
    CreateFieldIndexCollectionBuilder, FieldType, KeywordIndexParamsBuilder,
};
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .create_field_index(
        CreateFieldIndexCollectionBuilder::new(
            "{collection_name}",
            "name_of_the_field_to_index",
            FieldType::Keyword,
        )
        .field_index_params(KeywordIndexParamsBuilder::default().enable_hnsw(false)),
    )
    .await?;
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
        "name_of_the_field_to_index",
        PayloadSchemaType.Keyword,
        PayloadIndexParams.newBuilder()
            .setKeywordIndexParams(
                KeywordIndexParams.newBuilder()
                    .setEnableHnsw(false)
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
 fieldName: "name_of_the_field_to_index",
 schemaType: PayloadSchemaType.Keyword,
 indexParams: new PayloadIndexParams
 {
  KeywordIndexParams = new KeywordIndexParams
  {
   EnableHnsw = false
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
			EnableHnsw: qdrant.PtrOf(false),
		}),
})
```

### Rebuild the HNSW Index

There may be cases when you need to rebuild the HNSW index, for example, when you create a new payload index and want to take advantage of filter-aware edges in the HNSW graph. To rebuild an HNSW index, make a small change to its HNSW configuration, for example by bumping `ef_construct` by `1`. This forces the optimizer to re-index all segments.

First, retrieve the current value of `ef_construct`:

```bash
BASE_EF=$(curl -s http://localhost:6333/collections/{collection_name} | \
  jq '.result.config.hnsw_config.ef_construct')
```

```python
base_ef = client.get_collection(
    collection_name="{collection_name}"
).config.hnsw_config.ef_construct
```

```typescript
const collectionInfo = await client.getCollection("{collection_name}");
const baseEf = collectionInfo.config.hnsw_config.ef_construct;
```

```rust
let base_ef = client
  .collection_info("{collection_name}")              
  .await?                                                                                                                                                   
  .result                                            
  .and_then(|info| info.config)
  .and_then(|config| config.hnsw_config)                                                                                                                    
  .and_then(|hnsw| hnsw.ef_construct);
```

```java
CollectionInfo collectionInfo = client.getCollectionInfoAsync("{collection_name}").get();
long baseEf = collectionInfo.getConfig().getHnswConfig().getEfConstruct();
```

```csharp
var collectionInfo = await client.GetCollectionInfoAsync("{collection_name}");
var baseEf = collectionInfo.Config.HnswConfig.EfConstruct;
```

```go
collectionInfo, err := client.GetCollectionInfo(context.Background(), "{collection_name}")
if err != nil { panic(err) }
baseEf := *collectionInfo.Config.HnswConfig.EfConstruct
```

Next, update the collection with the value of `ef_construct` incremented by `1`:

```bash
curl -X PATCH http://localhost:6333/collections/{collection_name} \
  -H 'Content-Type: application/json' \
  --data-raw "{
    \"hnsw_config\": {
        \"ef_construct\": $((BASE_EF + 1))
    }
  }"
```

```python
client.update_collection(
    collection_name="{collection_name}",
    hnsw_config=models.HnswConfigDiff(ef_construct=base_ef + 1),
)
```

```typescript
await client.updateCollection("{collection_name}", {
  hnsw_config: {
    ef_construct: baseEf + 1,
  },
});
```

```rust
client
    .update_collection(
        UpdateCollectionBuilder::new("{collection_name}")
            .hnsw_config(HnswConfigDiffBuilder::default().ef_construct(base_ef.unwrap_or(100) + 1)),
    )
    .await?;
```

```java
client
    .updateCollectionAsync(
        UpdateCollection.newBuilder()
            .setCollectionName("{collection_name}")
            .setHnswConfig(
                HnswConfigDiff.newBuilder()
                    .setEfConstruct(baseEf + 1)
                    .build())
            .build())
    .get();
```

```csharp
await client.UpdateCollectionAsync(
	collectionName: "{collection_name}",
	hnswConfig: new HnswConfigDiff { EfConstruct = baseEf + 1 }
);
```

```go
client.UpdateCollection(context.Background(), &qdrant.UpdateCollection{
	CollectionName: "{collection_name}",
	HnswConfig: &qdrant.HnswConfigDiff{
		EfConstruct: qdrant.PtrOf(baseEf + 1),
	},
})
```

Don’t immediately revert the value of `ef_construct` to its original value. Keep it set to the new value.
