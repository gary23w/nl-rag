"""More database engines and data-integration tooling."""

from .common import CC_BY_SA, wiki

DOMAINS = {
    "apache-ignite": {
        "tags": ["apache ignite", "in-memory data grid", "distributed cache", "ignite compute grid"],
        "license": CC_BY_SA,
        "pages": wiki("Apache_Ignite", "In-memory_database", "Distributed_cache", "Data_grid", "Distributed_computing") + [
            "https://ignite.apache.org/docs/latest/",
            "https://ignite.apache.org/docs/latest/data-modeling/data-partitioning",
            "https://ignite.apache.org/docs/latest/memory-architecture",
        ],
    },
    "hazelcast-imdg": {
        "tags": ["hazelcast platform", "in-memory data grid", "distributed computing", "hazelcast imdg"],
        "license": CC_BY_SA,
        "pages": wiki("Hazelcast", "Data_grid", "Distributed_cache", "Distributed_computing") + [
            "https://docs.hazelcast.com/hazelcast/latest/",
            "https://docs.hazelcast.com/hazelcast/latest/architecture/architecture",
            "https://docs.hazelcast.com/hazelcast/latest/data-structures/distributed-data-structures",
        ],
    },
    "aerospike-db": {
        "tags": ["aerospike database", "flash-optimized database", "key-value store", "real-time database"],
        "license": CC_BY_SA,
        "pages": wiki("Aerospike", "Key-value_database", "NoSQL", "Solid-state_drive") + [
            "https://aerospike.com/docs/",
            "https://aerospike.com/docs/database/learn/architecture/",
            "https://github.com/aerospike/aerospike-server/blob/master/README.md",
        ],
    },
    "memgraph": {
        "tags": ["memgraph database", "in-memory graph database", "cypher query language", "graph analytics"],
        "license": CC_BY_SA,
        "pages": wiki("Graph_database", "Cypher_(query_language)", "In-memory_database", "NoSQL") + [
            "https://memgraph.com/docs",
            "https://memgraph.com/docs/fundamentals/storage-memory-usage",
            "https://github.com/memgraph/memgraph/blob/master/README.md",
        ],
    },
    "janusgraph": {
        "tags": ["janusgraph", "distributed graph database", "apache tinkerpop", "gremlin query language"],
        "license": CC_BY_SA,
        "pages": wiki("Graph_database", "Apache_TinkerPop", "Gremlin_(query_language)", "Distributed_database") + [
            "https://docs.janusgraph.org/",
            "https://docs.janusgraph.org/getting-started/architecture/",
            "https://github.com/JanusGraph/janusgraph/blob/master/README.md",
        ],
    },
    "dgraph": {
        "tags": ["dgraph database", "distributed graph database", "dql query language", "graphql database"],
        "license": CC_BY_SA,
        "pages": wiki("Graph_database", "GraphQL", "Distributed_database", "NoSQL") + [
            "https://docs.dgraph.io/",
            "https://github.com/hypermodeinc/dgraph/blob/main/README.md",
            "https://docs.dgraph.io/dql",
        ],
    },
    "tigergraph": {
        "tags": ["tigergraph database", "parallel graph database", "gsql query language", "graph analytics"],
        "license": CC_BY_SA,
        "pages": wiki("Graph_database", "Graph_(abstract_data_type)", "Parallel_computing", "NoSQL") + [
            "https://docs.tigergraph.com/home/",
            "https://docs.tigergraph.com/gsql-ref/current/intro/",
            "https://www.tigergraph.com/",
        ],
    },
    "nebula-graph": {
        "tags": ["nebula graph", "distributed graph database", "ngql query language", "graph database"],
        "license": CC_BY_SA,
        "pages": wiki("Graph_database", "Distributed_database", "NoSQL", "Graph_(abstract_data_type)") + [
            "https://docs.nebula-graph.io/",
            "https://github.com/vesoft-inc/nebula/blob/master/README.md",
            "https://docs.nebula-graph.io/master/1.introduction/1.what-is-nebula-graph/",
        ],
    },
    "fauna-db": {
        "tags": ["fauna database", "distributed document database", "serializable transactions", "serverless database"],
        "license": CC_BY_SA,
        "pages": wiki("Distributed_database", "Document-oriented_database", "Serverless_computing", "NoSQL", "Google_Spanner", "Serializability") + [
            "https://github.com/fauna/fauna-js/blob/main/README.md",
        ],
    },
    "edgedb": {
        "tags": ["edgedb", "gel database", "graph-relational database", "edgeql query language"],
        "license": CC_BY_SA,
        "pages": wiki("Object%E2%80%93relational_mapping", "Relational_database", "PostgreSQL", "Database_schema") + [
            "https://docs.geldata.com/",
            "https://docs.geldata.com/reference/edgeql",
            "https://github.com/geldata/gel/blob/master/README.md",
        ],
    },
    "surrealdb": {
        "tags": ["surrealdb", "multi-model database", "surrealql query language", "document-graph database"],
        "license": CC_BY_SA,
        "pages": wiki("Multi-model_database", "Document-oriented_database", "Graph_database", "NoSQL") + [
            "https://surrealdb.com/docs/surrealdb",
            "https://surrealdb.com/docs/surrealql",
            "https://github.com/surrealdb/surrealdb/blob/main/README.md",
        ],
    },
    "datomic": {
        "tags": ["datomic database", "immutable database", "datalog query", "temporal database"],
        "license": CC_BY_SA,
        "pages": wiki("Datalog", "Immutable_object", "Temporal_database", "Database") + [
            "https://docs.datomic.com/datomic-overview.html",
            "https://docs.datomic.com/whatis/data-model.html",
            "https://www.datomic.com/",
        ],
    },
    "xtdb": {
        "tags": ["xtdb database", "bitemporal database", "datalog query", "immutable database"],
        "license": CC_BY_SA,
        "pages": wiki("Temporal_database", "Datalog", "Immutable_object", "Database") + [
            "https://docs.xtdb.com/",
            "https://github.com/xtdb/xtdb/blob/main/README.adoc",
            "https://docs.xtdb.com/intro/what-is-xtdb.html",
        ],
    },
    "eventstore-db": {
        "tags": ["eventstoredb", "event sourcing database", "event stream database", "cqrs pattern"],
        "license": CC_BY_SA,
        "pages": wiki("Event_store", "Domain-driven_design", "Database", "Message-oriented_middleware") + [
            "https://developers.eventstore.com/",
            "https://github.com/EventStore/EventStore/blob/master/README.md",
            "https://www.eventstore.com/eventstoredb",
        ],
    },
    "questdb": {
        "tags": ["questdb database", "time series database", "sql time series", "column-oriented dbms"],
        "license": CC_BY_SA,
        "pages": wiki("Time_series_database", "Column-oriented_DBMS", "SQL", "Database") + [
            "https://questdb.com/docs/",
            "https://questdb.com/docs/concept/storage-model/",
            "https://github.com/questdb/questdb/blob/master/README.md",
        ],
    },
    "victoriametrics": {
        "tags": ["victoriametrics", "time series database", "prometheus monitoring", "metrics database"],
        "license": CC_BY_SA,
        "pages": wiki("Time_series_database", "Prometheus_(software)", "Monitoring", "Database") + [
            "https://docs.victoriametrics.com/",
            "https://docs.victoriametrics.com/victoriametrics/keyconcepts/",
            "https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/README.md",
        ],
    },
    "m3db": {
        "tags": ["m3db", "distributed time series database", "m3 metrics platform", "prometheus monitoring"],
        "license": CC_BY_SA,
        "pages": wiki("Time_series_database", "Distributed_database", "Prometheus_(software)", "Metric_(mathematics)") + [
            "https://m3db.io/docs/",
            "https://github.com/m3db/m3/blob/master/README.md",
            "https://m3db.io/docs/overview/components/",
        ],
    },
    "apache-druid-deep": {
        "tags": ["apache druid", "real-time analytics database", "olap datastore", "columnar storage"],
        "license": CC_BY_SA,
        "pages": wiki("Apache_Druid", "Online_analytical_processing", "Column-oriented_DBMS", "Data_warehouse") + [
            "https://druid.apache.org/docs/latest/design/",
            "https://druid.apache.org/docs/latest/design/architecture/",
            "https://druid.apache.org/docs/latest/design/segments/",
        ],
    },
    "apache-pinot": {
        "tags": ["apache pinot", "real-time olap datastore", "low-latency analytics", "columnar storage"],
        "license": CC_BY_SA,
        "pages": wiki("Online_analytical_processing", "Column-oriented_DBMS", "Apache_Kafka", "Data_warehouse") + [
            "https://docs.pinot.apache.org/",
            "https://docs.pinot.apache.org/basics/concepts",
            "https://github.com/apache/pinot/blob/master/README.md",
        ],
    },
    "apache-kudu": {
        "tags": ["apache kudu", "columnar storage engine", "apache hadoop", "analytical storage"],
        "license": CC_BY_SA,
        "pages": wiki("Apache_Kudu", "Column-oriented_DBMS", "Apache_Hadoop", "Apache_Impala") + [
            "https://kudu.apache.org/docs/",
            "https://kudu.apache.org/docs/index.html",
            "https://kudu.apache.org/docs/schema_design.html",
        ],
    },
    "greenplum": {
        "tags": ["greenplum database", "massively parallel processing", "postgres data warehouse", "analytical database"],
        "license": CC_BY_SA,
        "pages": wiki("Greenplum", "Data_warehouse", "Massively_parallel_processing", "PostgreSQL") + [
            "https://docs.vmware.com/en/VMware-Greenplum/index.html",
            "https://github.com/greenplum-db/gpdb-archive/blob/main/README.md",
        ],
    },
    "monetdb": {
        "tags": ["monetdb database", "column-oriented dbms", "in-memory analytics", "columnar storage"],
        "license": CC_BY_SA,
        "pages": wiki("MonetDB", "Column-oriented_DBMS", "Online_analytical_processing", "In-memory_database") + [
            "https://www.monetdb.org/documentation/",
            "https://www.monetdb.org/blog/",
            "https://www.monetdb.org/documentation/user-guide/",
        ],
    },
    "firebird-db": {
        "tags": ["firebird database", "firebird sql", "relational database", "interbase fork"],
        "license": CC_BY_SA,
        "pages": wiki("Firebird_(database_server)", "Relational_database", "SQL", "InterBase") + [
            "https://firebirdsql.org/en/documentation/",
            "https://firebirdsql.org/en/features/",
            "https://firebirdsql.org/en/about-firebird/",
        ],
    },
    "hsqldb": {
        "tags": ["hsqldb database", "hypersql database", "java database", "embedded database"],
        "license": CC_BY_SA,
        "pages": wiki("HSQLDB", "Relational_database", "Java_(programming_language)", "Embedded_database") + [
            "https://hsqldb.org/doc/2.0/guide/index.html",
            "https://hsqldb.org/",
            "https://hsqldb.org/web/features200.html",
        ],
    },
    "h2-database": {
        "tags": ["h2 database", "h2 java database", "embedded database", "in-memory database"],
        "license": CC_BY_SA,
        "pages": wiki("H2_(database)", "Embedded_database", "Java_(programming_language)", "In-memory_database") + [
            "https://www.h2database.com/html/main.html",
            "https://www.h2database.com/html/features.html",
            "https://www.h2database.com/html/architecture.html",
        ],
    },
    "apache-derby": {
        "tags": ["apache derby", "java embedded database", "javadb", "relational database"],
        "license": CC_BY_SA,
        "pages": wiki("Apache_Derby", "Relational_database", "Java_(programming_language)", "Embedded_database") + [
            "https://db.apache.org/derby/manuals/index.html",
            "https://db.apache.org/derby/",
            "https://db.apache.org/derby/papers/DerbyTut/",
        ],
    },
    "apache-phoenix": {
        "tags": ["apache phoenix", "sql over hbase", "apache hbase", "relational layer"],
        "license": CC_BY_SA,
        "pages": wiki("Apache_Phoenix", "Apache_HBase", "SQL", "Apache_Hadoop") + [
            "https://phoenix.apache.org/",
            "https://phoenix.apache.org/faq.html",
            "https://phoenix.apache.org/Phoenix-in-15-minutes-or-less.html",
        ],
    },
    "apache-accumulo": {
        "tags": ["apache accumulo", "wide-column store", "cell-level security", "bigtable clone"],
        "license": CC_BY_SA,
        "pages": wiki("Apache_Accumulo", "Wide-column_store", "Bigtable", "Apache_Hadoop") + [
            "https://accumulo.apache.org/docs/2.x/",
            "https://accumulo.apache.org/docs/2.x/getting-started/design",
            "https://accumulo.apache.org/",
        ],
    },
    "foundationdb": {
        "tags": ["foundationdb", "distributed key-value store", "acid transactions", "ordered key-value store"],
        "license": CC_BY_SA,
        "pages": wiki("FoundationDB", "Key-value_database", "Distributed_database", "ACID") + [
            "https://apple.github.io/foundationdb/",
            "https://apple.github.io/foundationdb/architecture.html",
            "https://github.com/apple/foundationdb/blob/main/README.md",
        ],
    },
    "tarantool": {
        "tags": ["tarantool database", "in-memory database", "lua application server", "key-value store"],
        "license": CC_BY_SA,
        "pages": wiki("Tarantool", "In-memory_database", "Lua_(programming_language)", "NoSQL") + [
            "https://www.tarantool.io/en/doc/latest/",
            "https://github.com/tarantool/tarantool/blob/master/README.md",
            "https://www.tarantool.io/en/developers/",
        ],
    },
    "keydb": {
        "tags": ["keydb database", "multithreaded redis fork", "in-memory data store", "key-value cache"],
        "license": CC_BY_SA,
        "pages": wiki("Redis", "In-memory_database", "Key-value_database", "Multithreading_(computer_architecture)") + [
            "https://docs.keydb.dev/",
            "https://github.com/Snapchat/KeyDB/blob/main/README.md",
            "https://docs.keydb.dev/docs/download/",
        ],
    },
    "dragonfly-db": {
        "tags": ["dragonfly database", "in-memory data store", "redis alternative", "key-value cache"],
        "license": CC_BY_SA,
        "pages": wiki("Redis", "In-memory_database", "Key-value_database", "Cache_(computing)") + [
            "https://www.dragonflydb.io/docs",
            "https://github.com/dragonflydb/dragonfly/blob/main/README.md",
            "https://www.dragonflydb.io/docs/getting-started",
        ],
    },
    "garnet-cache": {
        "tags": ["garnet cache", "microsoft garnet", "remote cache store", "resp protocol"],
        "license": CC_BY_SA,
        "pages": wiki("Redis", "Cache_(computing)", "In-memory_database", "Microsoft_Research") + [
            "https://microsoft.github.io/garnet/docs",
            "https://github.com/microsoft/garnet/blob/main/README.md",
            "https://microsoft.github.io/garnet/docs/welcome/features",
        ],
    },
    "immudb": {
        "tags": ["immudb database", "immutable database", "cryptographic verification", "tamper-evident ledger"],
        "license": CC_BY_SA,
        "pages": wiki("Immutable_object", "Merkle_tree", "Database", "Tamperproofing") + [
            "https://docs.immudb.io/",
            "https://github.com/codenotary/immudb/blob/master/README.md",
            "https://docs.immudb.io/master/develop/reading.html",
        ],
    },
    "cratedb": {
        "tags": ["cratedb database", "distributed sql database", "lucene search database", "columnar storage"],
        "license": CC_BY_SA,
        "pages": wiki("SQL", "Distributed_database", "Apache_Lucene", "Column-oriented_DBMS") + [
            "https://cratedb.com/docs/crate/reference/en/latest/",
            "https://github.com/crate/crate/blob/master/README.rst",
            "https://cratedb.com/docs/guide/",
        ],
    },
    "singlestore": {
        "tags": ["singlestore database", "memsql database", "distributed sql", "htap database"],
        "license": CC_BY_SA,
        "pages": wiki("SingleStore", "Distributed_SQL", "In-memory_database", "Column-oriented_DBMS") + [
            "https://docs.singlestore.com/",
            "https://docs.singlestore.com/cloud/getting-started-with-singlestore-helios/",
            "https://docs.singlestore.com/db/latest/introduction/",
        ],
    },
    "materialize-db": {
        "tags": ["materialize database", "streaming sql database", "incremental view maintenance", "timely dataflow"],
        "license": CC_BY_SA,
        "pages": wiki("Materialized_view", "Stream_processing", "SQL", "Incremental_computing") + [
            "https://materialize.com/docs/",
            "https://github.com/MaterializeInc/materialize/blob/main/README.md",
            "https://materialize.com/docs/overview/what-is-materialize/",
        ],
    },
    "risingwave": {
        "tags": ["risingwave database", "streaming database", "streaming sql", "stream processing"],
        "license": CC_BY_SA,
        "pages": wiki("Stream_processing", "SQL", "Materialized_view", "Database") + [
            "https://docs.risingwave.com/",
            "https://github.com/risingwavelabs/risingwave/blob/main/README.md",
            "https://docs.risingwave.com/get-started/intro",
        ],
    },
    "ksqldb-streams": {
        "tags": ["ksqldb", "kafka streams", "streaming sql engine", "event stream processing"],
        "license": CC_BY_SA,
        "pages": wiki("Apache_Kafka", "Stream_processing", "SQL", "Event_stream_processing") + [
            "https://docs.ksqldb.io/en/latest/",
            "https://docs.ksqldb.io/en/latest/concepts/",
            "https://kafka.apache.org/documentation/streams/",
        ],
    },
    "apache-flink-sql": {
        "tags": ["apache flink", "flink sql", "stateful stream processing", "dataflow engine"],
        "license": CC_BY_SA,
        "pages": wiki("Apache_Flink", "Stream_processing", "SQL", "Dataflow_programming") + [
            "https://nightlies.apache.org/flink/flink-docs-stable/",
            "https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/table/sql/overview/",
            "https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/",
        ],
    },
    "airbyte-integration": {
        "tags": ["airbyte platform", "data integration platform", "elt pipeline", "data connectors"],
        "license": CC_BY_SA,
        "pages": wiki("Extract,_transform,_load", "Data_integration", "Data_pipeline", "Open-source_software") + [
            "https://docs.airbyte.com/",
            "https://docs.airbyte.com/understanding-airbyte/high-level-view",
            "https://github.com/airbytehq/airbyte/blob/master/README.md",
        ],
    },
    "fivetran-integration": {
        "tags": ["fivetran connector", "managed data pipeline", "automated elt", "data connectors"],
        "license": CC_BY_SA,
        "pages": wiki("Extract,_transform,_load", "Data_integration", "Data_pipeline", "Cloud_computing") + [
            "https://fivetran.com/docs/getting-started",
            "https://fivetran.com/docs/core-concepts",
            "https://fivetran.com/docs/connectors",
        ],
    },
    "singer-taps": {
        "tags": ["singer spec", "singer taps", "data extraction protocol", "etl connectors"],
        "license": CC_BY_SA,
        "pages": wiki("Extract,_transform,_load", "Data_integration", "JSON", "Pipeline_(software)") + [
            "https://www.singer.io/",
            "https://github.com/singer-io/getting-started/blob/master/README.md",
            "https://hub.meltano.com/singer/spec/",
        ],
    },
    "meltano": {
        "tags": ["meltano platform", "dataops platform", "elt orchestration", "singer taps"],
        "license": CC_BY_SA,
        "pages": wiki("Extract,_transform,_load", "DataOps", "Data_integration", "Open-source_software") + [
            "https://docs.meltano.com/",
            "https://docs.meltano.com/concepts/project",
            "https://github.com/meltano/meltano/blob/main/README.md",
        ],
    },
    "apache-hop": {
        "tags": ["apache hop", "hop orchestration platform", "data pipeline tool", "visual etl"],
        "license": CC_BY_SA,
        "pages": wiki("Extract,_transform,_load", "Data_integration", "Pentaho", "Data_pipeline") + [
            "https://hop.apache.org/manual/latest/",
            "https://hop.apache.org/",
            "https://hop.apache.org/manual/latest/getting-started/index.html",
        ],
    },
    "apache-camel": {
        "tags": ["apache camel", "enterprise integration patterns", "integration framework", "message routing"],
        "license": CC_BY_SA,
        "pages": wiki("Apache_Camel", "Enterprise_Integration_Patterns", "Message-oriented_middleware", "Enterprise_application_integration") + [
            "https://camel.apache.org/manual/",
            "https://camel.apache.org/manual/faq/what-is-camel.html",
            "https://camel.apache.org/components/next/eips/enterprise-integration-patterns.html",
        ],
    },
    "kestra-orchestration": {
        "tags": ["kestra orchestrator", "workflow orchestration", "data orchestration platform", "declarative workflows"],
        "license": CC_BY_SA,
        "pages": wiki("Orchestration_(computing)", "Workflow_engine", "Data_pipeline", "Directed_acyclic_graph") + [
            "https://kestra.io/docs",
            "https://github.com/kestra-io/kestra/blob/develop/README.md",
            "https://kestra.io/docs/getting-started/quickstart",
        ],
    },
    "mage-ai": {
        "tags": ["mage ai", "data pipeline tool", "data engineering platform", "notebook pipelines"],
        "license": CC_BY_SA,
        "pages": wiki("Data_pipeline", "Extract,_transform,_load", "Data_engineering", "Directed_acyclic_graph") + [
            "https://docs.mage.ai/introduction/overview",
            "https://github.com/mage-ai/mage-ai/blob/master/README.md",
            "https://docs.mage.ai/design/core-abstractions",
        ],
    },
    "flyte-workflows": {
        "tags": ["flyte platform", "workflow orchestration", "machine learning pipelines", "kubernetes workflows"],
        "license": CC_BY_SA,
        "pages": wiki("Workflow_engine", "Kubernetes", "Machine_learning", "Directed_acyclic_graph") + [
            "https://docs.flyte.org/en/latest/",
            "https://github.com/flyteorg/flyte/blob/master/README.md",
            "https://flyte.org/",
        ],
    },
    "metaflow": {
        "tags": ["metaflow framework", "data science workflows", "machine learning pipelines", "netflix metaflow"],
        "license": CC_BY_SA,
        "pages": wiki("Data_science", "Machine_learning", "Workflow_engine", "Netflix") + [
            "https://docs.metaflow.org/",
            "https://github.com/Netflix/metaflow/blob/master/README.md",
            "https://docs.metaflow.org/introduction/what-is-metaflow",
        ],
    },
    "kedro-pipelines": {
        "tags": ["kedro framework", "data science pipelines", "reproducible pipelines", "machine learning engineering"],
        "license": CC_BY_SA,
        "pages": wiki("Data_science", "Machine_learning", "Reproducibility", "Pipeline_(software)") + [
            "https://docs.kedro.org/en/stable/",
            "https://github.com/kedro-org/kedro/blob/main/README.md",
            "https://docs.kedro.org/en/stable/get_started/kedro_concepts.html",
        ],
    },
    "dbt-core-deep": {
        "tags": ["dbt core", "data build tool", "analytics engineering", "sql transformation"],
        "license": CC_BY_SA,
        "pages": wiki("Data_transformation", "Extract,_transform,_load", "SQL", "Data_warehouse") + [
            "https://docs.getdbt.com/docs/introduction",
            "https://docs.getdbt.com/docs/build/models",
            "https://github.com/dbt-labs/dbt-core/blob/main/README.md",
        ],
    },
    "great-expectations-deep": {
        "tags": ["great expectations", "data quality framework", "data validation tool", "data pipeline testing"],
        "license": CC_BY_SA,
        "pages": wiki("Data_validation", "Data_quality", "Software_testing", "Data_pipeline") + [
            "https://docs.greatexpectations.io/docs/home/",
            "https://github.com/great-expectations/great_expectations/blob/develop/README.md",
            "https://docs.greatexpectations.io/docs/core/introduction/",
        ],
    },
    "soda-data-quality": {
        "tags": ["soda core", "data quality testing", "data reliability", "soda checks language"],
        "license": CC_BY_SA,
        "pages": wiki("Data_quality", "Data_validation", "Data_governance", "Software_testing") + [
            "https://docs.soda.io/",
            "https://github.com/sodadata/soda-core/blob/main/README.md",
            "https://docs.soda.io/soda/quick-start-sip.html",
        ],
    },
}
