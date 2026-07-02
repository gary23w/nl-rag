"""Database engines and data-storage concepts."""

from .common import CC_BY_SA, wiki

DOMAINS = {
    "oracle-database": {
        "tags": ["oracle database", "oracle rdbms", "pl/sql", "oracle corporation"],
        "license": CC_BY_SA,
        "pages": wiki("Oracle_Database", "PL/SQL", "Oracle_Corporation", "Stored_procedure") + [
            "https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/introduction-to-oracle-database.html",
            "https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/tables-and-table-clusters.html",
            "https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/indexes-and-index-organized-tables.html",
        ],
    },
    "sql-server": {
        "tags": ["sql server", "microsoft sql server", "transact-sql", "t-sql"],
        "license": CC_BY_SA,
        "pages": wiki("Microsoft_SQL_Server", "Transact-SQL", "SQL_Server_Management_Studio", "Stored_procedure") + [
            "https://learn.microsoft.com/en-us/sql/relational-databases/database-engine-tutorials",
            "https://learn.microsoft.com/en-us/sql/t-sql/language-reference",
            "https://learn.microsoft.com/en-us/sql/relational-databases/indexes/indexes",
            "https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-log-architecture-and-management-guide",
        ],
    },
    "mariadb": {
        "tags": ["mariadb", "aria storage engine", "galera cluster", "innodb engine"],
        "license": CC_BY_SA,
        "pages": wiki("MariaDB", "Aria_(storage_engine)", "InnoDB") + [
            "https://mariadb.com/kb/en/documentation/",
            "https://mariadb.com/kb/en/innodb/",
            "https://mariadb.com/kb/en/storage-engines/",
            "https://mariadb.com/kb/en/galera-cluster/",
            "https://mariadb.com/kb/en/replication-overview/",
        ],
    },
    "cockroachdb": {
        "tags": ["cockroachdb", "distributed sql", "cockroach labs", "distributed database"],
        "license": CC_BY_SA,
        "pages": wiki("CockroachDB", "Distributed_SQL", "Distributed_database") + [
            "https://www.cockroachlabs.com/docs/stable/architecture/overview.html",
            "https://www.cockroachlabs.com/docs/stable/architecture/distribution-layer.html",
            "https://www.cockroachlabs.com/docs/stable/architecture/replication-layer.html",
            "https://www.cockroachlabs.com/docs/stable/architecture/storage-layer.html",
            "https://github.com/cockroachdb/cockroach/blob/master/README.md",
        ],
    },
    "cassandra-db": {
        "tags": ["cassandra", "wide-column store", "apache cassandra", "gossip protocol"],
        "license": CC_BY_SA,
        "pages": wiki("Apache_Cassandra", "Wide-column_store", "Gossip_protocol", "Merkle_tree") + [
            "https://cassandra.apache.org/doc/stable/cassandra/architecture/overview.html",
            "https://cassandra.apache.org/doc/stable/cassandra/architecture/dynamo.html",
            "https://cassandra.apache.org/doc/stable/cassandra/architecture/storage-engine.html",
            "https://github.com/apache/cassandra/blob/trunk/README.asc",
        ],
    },
    "dynamodb": {
        "tags": ["dynamodb", "amazon dynamodb", "dynamo storage system", "vector clock"],
        "license": CC_BY_SA,
        "pages": wiki("Amazon_DynamoDB", "Dynamo_(storage_system)", "Vector_clock", "Quorum_(distributed_computing)") + [
            "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html",
            "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.html",
            "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.Partitions.html",
        ],
    },
    "couchdb": {
        "tags": ["couchdb", "apache couchdb", "document-oriented database", "eventual consistency"],
        "license": CC_BY_SA,
        "pages": wiki("Apache_CouchDB", "Document-oriented_database", "Eventual_consistency") + [
            "https://docs.couchdb.org/en/stable/intro/overview.html",
            "https://docs.couchdb.org/en/stable/intro/consistency.html",
            "https://docs.couchdb.org/en/stable/replication/intro.html",
            "https://couchdb.apache.org/",
        ],
    },
    "couchbase": {
        "tags": ["couchbase", "couchbase server", "document-oriented database", "key-value store"],
        "license": CC_BY_SA,
        "pages": wiki("Couchbase_Server", "Document-oriented_database", "Key-value_database", "NoSQL") + [
            "https://docs.couchbase.com/home/index.html",
            "https://docs.couchbase.com/server/current/learn/architecture-overview.html",
        ],
    },
    "neo4j": {
        "tags": ["neo4j", "cypher query language", "property graph", "graph database"],
        "license": CC_BY_SA,
        "pages": wiki("Neo4j", "Cypher_(query_language)", "Graph_database") + [
            "https://neo4j.com/docs/getting-started/",
            "https://neo4j.com/docs/getting-started/cypher/",
            "https://neo4j.com/docs/getting-started/data-modeling/",
        ],
    },
    "arangodb": {
        "tags": ["arangodb", "multi-model database", "aql query", "graph database"],
        "license": CC_BY_SA,
        "pages": wiki("ArangoDB", "Multi-model_database", "Graph_database", "Document-oriented_database") + [
            "https://arangodb.com/documentation/",
            "https://www.arangodb.com/docs/stable/",
            "https://www.arangodb.com/docs/stable/data-modeling.html",
        ],
    },
    "influxdb": {
        "tags": ["influxdb", "time series database", "influxdata", "database engine"],
        "license": CC_BY_SA,
        "pages": wiki("InfluxDB", "Time_series_database", "Database_engine") + [
            "https://docs.influxdata.com/influxdb/v2/",
            "https://docs.influxdata.com/influxdb/v2/reference/key-concepts/",
            "https://docs.influxdata.com/influxdb/v2/reference/internals/storage-engine/",
        ],
    },
    "timescaledb": {
        "tags": ["timescaledb", "hypertable", "time series database", "postgres extension"],
        "license": CC_BY_SA,
        "pages": wiki("TimescaleDB", "Time_series_database", "PostgreSQL") + [
            "https://docs.timescale.com/",
            "https://docs.timescale.com/use-timescale/latest/hypertables/",
            "https://docs.timescale.com/use-timescale/latest/continuous-aggregates/about-continuous-aggregates/",
            "https://docs.timescale.com/use-timescale/latest/compression/about-compression/",
        ],
    },
    "clickhouse": {
        "tags": ["clickhouse", "columnar olap", "mergetree engine", "column-oriented dbms"],
        "license": CC_BY_SA,
        "pages": wiki("ClickHouse", "Column-oriented_DBMS", "Online_analytical_processing") + [
            "https://clickhouse.com/docs/en/intro",
            "https://clickhouse.com/docs/en/development/architecture",
            "https://clickhouse.com/docs/en/introduction/distinctive-features",
            "https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree",
        ],
    },
    "duckdb": {
        "tags": ["duckdb", "embedded analytics", "olap engine", "apache parquet"],
        "license": CC_BY_SA,
        "pages": wiki("DuckDB", "Column-oriented_DBMS", "Online_analytical_processing", "Apache_Parquet") + [
            "https://duckdb.org/why_duckdb",
            "https://duckdb.org/docs/stable/sql/introduction",
            "https://duckdb.org/docs/stable/sql/statements/select",
            "https://duckdb.org/docs/stable/data/parquet/overview",
        ],
    },
    "elasticsearch": {
        "tags": ["elasticsearch", "apache lucene", "full-text search engine", "inverted index"],
        "license": CC_BY_SA,
        "pages": wiki("Elasticsearch", "Apache_Lucene", "Full-text_search", "Inverted_index") + [
            "https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html",
            "https://www.elastic.co/guide/en/elasticsearch/reference/current/documents-indices.html",
        ],
    },
    "opensearch": {
        "tags": ["opensearch", "search engine", "log analytics", "apache lucene"],
        "license": CC_BY_SA,
        "pages": wiki("OpenSearch_(software)", "Elasticsearch", "Apache_Lucene") + [
            "https://opensearch.org/docs/latest/",
            "https://opensearch.org/docs/latest/about/",
            "https://opensearch.org/docs/latest/getting-started/intro/",
        ],
    },
    "apache-solr": {
        "tags": ["apache solr", "solr search", "apache lucene", "search engine indexing"],
        "license": CC_BY_SA,
        "pages": wiki("Apache_Solr", "Apache_Lucene", "Full-text_search", "Search_engine_indexing") + [
            "https://solr.apache.org/guide/solr/latest/getting-started/introduction.html",
            "https://solr.apache.org/guide/solr/latest/indexing-guide/indexing-with-update-handlers.html",
            "https://lucene.apache.org/core/documentation.html",
        ],
    },
    "etcd-store": {
        "tags": ["etcd", "distributed key-value store", "raft consensus", "apache zookeeper"],
        "license": CC_BY_SA,
        "pages": wiki("Etcd", "Key-value_database", "Raft_(algorithm)", "Apache_ZooKeeper") + [
            "https://etcd.io/docs/v3.5/learning/data_model/",
            "https://etcd.io/docs/v3.5/learning/why/",
            "https://etcd.io/docs/v3.5/learning/api/",
        ],
    },
    "rocksdb": {
        "tags": ["rocksdb", "embedded key-value store", "lsm storage", "log-structured merge-tree"],
        "license": CC_BY_SA,
        "pages": wiki("RocksDB", "Log-structured_merge-tree", "Key-value_database", "Embedded_database") + [
            "https://rocksdb.org/docs/getting-started.html",
            "https://github.com/facebook/rocksdb/blob/main/README.md",
        ],
    },
    "leveldb": {
        "tags": ["leveldb", "embedded key-value store", "log-structured merge-tree", "storage engine"],
        "license": CC_BY_SA,
        "pages": wiki("LevelDB", "Log-structured_merge-tree", "Key-value_database", "Storage_engine", "Embedded_database") + [
            "https://github.com/google/leveldb/blob/main/doc/index.md",
        ],
    },
    "lmdb": {
        "tags": ["lmdb", "lightning memory-mapped database", "memory-mapped file", "copy-on-write"],
        "license": CC_BY_SA,
        "pages": wiki("Lightning_Memory-Mapped_Database", "Key-value_database", "Memory-mapped_file", "Copy-on-write") + [
            "https://www.symas.com/lmdb",
            "https://github.com/LMDB/lmdb/blob/mdb.master/libraries/liblmdb/lmdb.h",
        ],
    },
    "scylladb": {
        "tags": ["scylladb", "wide-column store", "seastar framework", "apache cassandra"],
        "license": CC_BY_SA,
        "pages": wiki("ScyllaDB", "Apache_Cassandra", "Wide-column_store") + [
            "https://docs.scylladb.com/stable/",
            "https://docs.scylladb.com/stable/architecture/",
            "https://github.com/scylladb/scylladb/blob/master/README.md",
        ],
    },
    "rethinkdb": {
        "tags": ["rethinkdb", "reql query", "document-oriented database", "distributed database"],
        "license": CC_BY_SA,
        "pages": wiki("RethinkDB", "Document-oriented_database", "NoSQL", "Distributed_database") + [
            "https://rethinkdb.com/docs/",
            "https://rethinkdb.com/docs/architecture/",
            "https://rethinkdb.com/docs/data-modeling/",
        ],
    },
    "firebase-firestore": {
        "tags": ["firebase", "cloud firestore", "backend as a service", "document-oriented database"],
        "license": CC_BY_SA,
        "pages": wiki("Firebase", "Document-oriented_database", "Backend_as_a_service", "NoSQL") + [
            "https://firebase.google.com/docs/firestore",
            "https://firebase.google.com/docs/firestore/data-model",
        ],
    },
    "supabase": {
        "tags": ["supabase", "backend as a service", "postgres platform", "cloud database"],
        "license": CC_BY_SA,
        "pages": wiki("PostgreSQL", "Backend_as_a_service", "Cloud_database", "Relational_database") + [
            "https://supabase.com/docs",
            "https://supabase.com/docs/guides/database/overview",
            "https://supabase.com/docs/guides/api",
            "https://github.com/supabase/supabase/blob/master/README.md",
        ],
    },
    "snowflake": {
        "tags": ["snowflake data cloud", "cloud data warehouse", "micro-partition", "columnar storage"],
        "license": CC_BY_SA,
        "pages": wiki("Snowflake_Inc.", "Data_warehouse", "Column-oriented_DBMS", "Cloud_database") + [
            "https://docs.snowflake.com/en/user-guide-intro",
            "https://docs.snowflake.com/en/user-guide/intro-key-concepts",
            "https://docs.snowflake.com/en/user-guide/tables-micro-partitions",
        ],
    },
    "google-bigquery": {
        "tags": ["bigquery", "google bigquery", "cloud data warehouse", "massively parallel processing"],
        "license": CC_BY_SA,
        "pages": wiki("BigQuery", "Data_warehouse", "Online_analytical_processing", "Massively_parallel_processing") + [
            "https://cloud.google.com/bigquery/docs/introduction",
            "https://cloud.google.com/bigquery/docs/storage_overview",
            "https://cloud.google.com/bigquery/docs/query-overview",
        ],
    },
    "amazon-redshift": {
        "tags": ["amazon redshift", "cloud data warehouse", "columnar storage", "massively parallel processing"],
        "license": CC_BY_SA,
        "pages": wiki("Amazon_Redshift", "Data_warehouse", "Column-oriented_DBMS", "Massively_parallel_processing") + [
            "https://docs.aws.amazon.com/redshift/latest/dg/welcome.html",
            "https://docs.aws.amazon.com/redshift/latest/dg/c_high_level_system_architecture.html",
        ],
    },
    "trino-presto": {
        "tags": ["trino query engine", "presto sql", "distributed query engine", "query optimization"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Trino_(SQL_query_engine)",
            "Presto_(SQL_query_engine)",
            "Online_analytical_processing",
            "Query_optimization",
        ) + [
            "https://trino.io/docs/current/overview.html",
            "https://trino.io/docs/current/overview/concepts.html",
        ],
    },
    "apache-hbase": {
        "tags": ["apache hbase", "bigtable clone", "wide-column store", "apache hadoop"],
        "license": CC_BY_SA,
        "pages": wiki("Apache_HBase", "Bigtable", "Wide-column_store", "Apache_Hadoop", "Google_File_System") + [
            "https://hbase.apache.org/book.html",
        ],
    },
    "riak": {
        "tags": ["riak", "distributed key-value store", "eventual consistency", "consistent hashing"],
        "license": CC_BY_SA,
        "pages": wiki("Riak", "Key-value_database", "Eventual_consistency", "Consistent_hashing") + [
            "https://docs.riak.com/",
            "https://docs.riak.com/riak/kv/latest/learn/concepts/replication/index.html",
            "https://docs.riak.com/riak/kv/latest/learn/concepts/clusters/index.html",
        ],
    },
    "vitess": {
        "tags": ["vitess", "mysql sharding", "database clustering", "horizontal scaling"],
        "license": CC_BY_SA,
        "pages": wiki("MySQL", "Shard_(database_architecture)", "Relational_database") + [
            "https://vitess.io/docs/",
            "https://vitess.io/docs/22.0/overview/whatisvitess/",
            "https://vitess.io/docs/22.0/overview/architecture/",
            "https://github.com/vitessio/vitess/blob/main/README.md",
        ],
    },
    "tidb": {
        "tags": ["tidb", "distributed sql", "htap database", "distributed database"],
        "license": CC_BY_SA,
        "pages": wiki("TiDB", "Distributed_SQL", "Distributed_database") + [
            "https://docs.pingcap.com/tidb/stable/overview/",
            "https://docs.pingcap.com/tidb/stable/tidb-architecture/",
            "https://docs.pingcap.com/tidb/stable/tidb-storage/",
            "https://docs.pingcap.com/tidb/stable/tidb-computing/",
        ],
    },
    "yugabytedb": {
        "tags": ["yugabytedb", "distributed sql", "postgres compatible", "distributed database"],
        "license": CC_BY_SA,
        "pages": wiki("YugabyteDB", "Distributed_SQL", "PostgreSQL", "Distributed_database") + [
            "https://docs.yugabyte.com/",
            "https://docs.yugabyte.com/preview/architecture/",
        ],
    },
    "milvus": {
        "tags": ["milvus", "vector database", "similarity search engine", "vector quantization"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Milvus_(vector_database)",
            "Vector_database",
            "Nearest_neighbor_search",
            "Vector_quantization",
        ) + [
            "https://github.com/milvus-io/milvus/blob/master/README.md",
            "https://github.com/milvus-io/milvus-docs/blob/v2.4.x/site/en/about/overview.md",
        ],
    },
    "qdrant": {
        "tags": ["qdrant", "vector database", "vector similarity search", "approximate nearest neighbor"],
        "license": CC_BY_SA,
        "pages": wiki("Qdrant", "Vector_database", "Nearest_neighbor_search") + [
            "https://qdrant.tech/documentation/",
            "https://qdrant.tech/documentation/overview/",
            "https://qdrant.tech/documentation/concepts/indexing/",
            "https://qdrant.tech/documentation/concepts/search/",
        ],
    },
    "weaviate": {
        "tags": ["weaviate", "vector database", "vector search engine", "hierarchical navigable small world"],
        "license": CC_BY_SA,
        "pages": wiki("Vector_database", "Nearest_neighbor_search", "Hierarchical_navigable_small_world") + [
            "https://weaviate.io/developers/weaviate",
            "https://weaviate.io/developers/weaviate/concepts",
            "https://weaviate.io/developers/weaviate/concepts/vector-index",
            "https://github.com/weaviate/weaviate/blob/main/README.md",
        ],
    },
    "pinecone": {
        "tags": ["pinecone vector db", "managed vector database", "vector similarity search", "locality-sensitive hashing"],
        "license": CC_BY_SA,
        "pages": wiki("Vector_database", "Nearest_neighbor_search", "Locality-sensitive_hashing", "Vector_space_model") + [
            "https://docs.pinecone.io/guides/get-started/overview",
            "https://docs.pinecone.io/reference/architecture/serverless-architecture",
            "https://github.com/pinecone-io/pinecone-python-client/blob/main/README.md",
        ],
    },
    "pgvector": {
        "tags": ["pgvector", "postgres vector extension", "vector similarity search", "word embedding"],
        "license": CC_BY_SA,
        "pages": wiki("Vector_database", "PostgreSQL", "Nearest_neighbor_search", "Word_embedding", "Embedding") + [
            "https://github.com/pgvector/pgvector/blob/master/README.md",
        ],
    },
    "faiss": {
        "tags": ["faiss", "similarity search library", "approximate nearest neighbor", "product quantization"],
        "license": CC_BY_SA,
        "pages": wiki("FAISS", "Nearest_neighbor_search", "Curse_of_dimensionality", "K-d_tree") + [
            "https://faiss.ai/",
            "https://faiss.ai/index.html",
            "https://github.com/facebookresearch/faiss/wiki",
        ],
    },
    "chroma-db": {
        "tags": ["chroma", "chromadb", "embedding database", "vector database"],
        "license": CC_BY_SA,
        "pages": wiki("Vector_database", "Word_embedding", "Nearest_neighbor_search") + [
            "https://www.trychroma.com/",
            "https://docs.trychroma.com/docs/overview/introduction",
            "https://docs.trychroma.com/docs/overview/getting-started",
            "https://github.com/chroma-core/chroma/blob/main/README.md",
        ],
    },
    "redis-cache": {
        "tags": ["redis", "in-memory data store", "key-value cache", "in-memory database"],
        "license": CC_BY_SA,
        "pages": wiki("Redis", "Key-value_database", "In-memory_database") + [
            "https://redis.io/docs/latest/",
            "https://redis.io/docs/latest/develop/data-types/",
            "https://redis.io/docs/latest/develop/data-types/streams/",
            "https://redis.io/docs/latest/operate/oss_and_stack/management/scaling/",
        ],
    },
    "database-sharding": {
        "tags": ["database sharding", "horizontal partitioning", "consistent hashing", "distributed database"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Shard_(database_architecture)",
            "Sharding",
            "Consistent_hashing",
            "Partition_(database)",
            "Distributed_database",
            "Quorum_(distributed_computing)",
        ),
    },
    "database-replication": {
        "tags": ["database replication", "eventual consistency", "cap theorem", "quorum consensus"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Replication_(computing)",
            "Eventual_consistency",
            "CAP_theorem",
            "Two-phase_commit_protocol",
            "Consistency_model",
        ) + [
            "https://www.postgresql.org/docs/current/high-availability.html",
        ],
    },
    "database-partitioning": {
        "tags": ["database partitioning", "table partitioning", "data striping", "horizontal partitioning"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Partition_(database)",
            "Data_striping",
            "Shard_(database_architecture)",
            "Consistent_hashing",
            "Distributed_database",
        ) + [
            "https://www.postgresql.org/docs/current/ddl-partitioning.html",
        ],
    },
    "connection-pooling-db": {
        "tags": ["connection pool", "database connection pooling", "resource pooling", "online transaction processing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Connection_pool",
            "Database",
            "Online_transaction_processing",
            "Database_engine",
            "Database_transaction",
            "Relational_database_management_system",
        ),
    },
    "secondary-index": {
        "tags": ["database index", "secondary index", "inverted index", "bitmap index"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Database_index",
            "Inverted_index",
            "Bitmap_index",
            "Search_engine_indexing",
            "B-tree",
        ) + [
            "https://www.postgresql.org/docs/current/indexes-types.html",
        ],
    },
    "materialized-view": {
        "tags": ["materialized view", "query result cache", "view maintenance", "query optimization"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Materialized_view",
            "Query_optimization",
            "Query_plan",
            "Online_analytical_processing",
            "Database_index",
        ) + [
            "https://www.postgresql.org/docs/current/rules-materializedviews.html",
        ],
    },
    "columnar-storage": {
        "tags": ["column-oriented dbms", "columnar storage", "olap analytics", "apache parquet"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Column-oriented_DBMS",
            "Online_analytical_processing",
            "Data_warehouse",
            "Column_family",
            "Apache_Parquet",
            "Apache_ORC",
        ),
    },
    "lsm-tree": {
        "tags": ["log-structured merge-tree", "lsm tree", "write-ahead logging", "bloom filter"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Log-structured_merge-tree",
            "Write-ahead_logging",
            "Bloom_filter",
            "B%2B_tree",
            "Storage_engine",
            "Copy-on-write",
        ),
    },
    "graph-database": {
        "tags": ["graph database", "property graph", "cypher query language", "multi-model database"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Graph_database",
            "Neo4j",
            "Cypher_(query_language)",
            "Multi-model_database",
            "NoSQL",
            "Distributed_database",
        ),
    },
    "index-tree-structures": {
        "tags": ["b-tree", "database index tree", "r-tree spatial index", "skip list"],
        "license": CC_BY_SA,
        "pages": wiki(
            "B-tree",
            "R-tree",
            "Trie",
            "Skip_list",
            "Hash_table",
            "K-d_tree",
        ),
    },
    "vector-index-ann": {
        "tags": ["approximate nearest neighbor", "hierarchical navigable small world", "locality-sensitive hashing", "cosine similarity"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Nearest_neighbor_search",
            "Hierarchical_navigable_small_world",
            "Locality-sensitive_hashing",
            "Cosine_similarity",
            "Curse_of_dimensionality",
            "Ball_tree",
        ),
    },
}
