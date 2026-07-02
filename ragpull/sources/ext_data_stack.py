"""Big-data, data-engineering, and analytics platforms."""
from .common import CC_BY_SA, WIKI, wiki

DOMAINS = {
    "apache-spark": {
        "tags": ["apache spark", "spark rdd", "distributed data processing", "map reduce", "in memory computing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Spark", "MapReduce", "Resilient_distributed_dataset",
            "Distributed_computing", "In-memory_processing",
        )
        + ["https://spark.apache.org/docs/latest/"],
    },
    "apache-flink": {
        "tags": ["apache flink", "stream processing", "complex event processing", "stateful streaming", "event time"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Flink", "Stream_processing", "Complex_event_processing",
            "Event_stream_processing", "Data_stream",
        )
        + ["https://flink.apache.org/"],
    },
    "apache-beam": {
        "tags": ["apache beam", "dataflow programming", "unified batch streaming", "data pipeline", "windowing semantics"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Beam", "Dataflow_programming", "Pipeline_(computing)",
            "Batch_processing", "Stream_processing", "Distributed_computing",
        ),
    },
    "apache-airflow": {
        "tags": ["apache airflow", "workflow orchestration", "directed acyclic graph", "task scheduling", "pipeline automation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Airflow", "Directed_acyclic_graph", "Workflow_management_system",
            "Orchestration_(computing)", "Scheduling_(computing)",
        )
        + ["https://airflow.apache.org/docs/"],
    },
    "dagster": {
        "tags": ["dagster orchestrator", "data orchestration", "software defined assets", "pipeline scheduling", "data lineage"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Orchestration_(computing)", "Scheduling_(computing)", "Directed_acyclic_graph",
            "Data_lineage", "Pipeline_(computing)",
        )
        + ["https://docs.dagster.io/"],
    },
    "prefect": {
        "tags": ["prefect orchestration", "dataflow automation", "workflow engine", "task retries", "pipeline scheduling"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Workflow", "Data_transformation", "Scheduling_(computing)",
            "Orchestration_(computing)", "Directed_acyclic_graph",
        )
        + ["https://docs.prefect.io/"],
    },
    "dbt-transform": {
        "tags": ["data build tool", "sql transformation", "analytics engineering", "elt modeling", "materialized view"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Data_build_tool", "Data_transformation", "Materialized_view",
            "Data_warehouse", "Extract,_load,_transform",
        )
        + ["https://docs.getdbt.com/"],
    },
    "apache-hadoop": {
        "tags": ["apache hadoop", "hadoop distributed file system", "map reduce", "distributed storage", "yarn resource manager"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Hadoop", "MapReduce", "Clustered_file_system",
            "Fault_tolerance", "YARN", "Distributed_computing",
        )
        + ["https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html"],
    },
    "apache-hive": {
        "tags": ["apache hive", "hive query language", "sql on hadoop", "data warehouse system", "query language"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Hive", "HiveQL", "SQL",
            "Data_warehouse", "Query_language", "Apache_Hadoop",
        ),
    },
    "apache-hbase": {
        "tags": ["apache hbase", "wide column store", "google bigtable", "distributed key value", "nosql database"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_HBase", "Bigtable", "Log-structured_merge-tree",
            "Column_(data_store)", "NoSQL", "Distributed_database",
        ),
    },
    "databricks": {
        "tags": ["databricks platform", "data lakehouse", "unified analytics", "collaborative notebooks", "apache spark"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Databricks", "Data_lakehouse", "Apache_Spark",
            "Business_intelligence", "Data_engineering", "Machine_learning",
        ),
    },
    "delta-lake": {
        "tags": ["delta lake", "acid data lake", "snapshot isolation", "transaction log", "open table format"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Delta_Lake", "Data_lakehouse", "Snapshot_isolation",
            "ACID", "Data_lake",
        )
        + ["https://delta.io/"],
    },
    "apache-iceberg": {
        "tags": ["apache iceberg", "open table format", "schema evolution", "hidden partitioning", "data lakehouse"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Iceberg", "Schema_evolution", "Data_lakehouse",
            "Partition_(database)", "Snapshot_isolation",
        )
        + ["https://iceberg.apache.org/docs/latest/"],
    },
    "apache-hudi": {
        "tags": ["apache hudi", "incremental data lake", "upsert table format", "copy on write", "multiversion concurrency control"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Parquet", "Column-oriented_DBMS", "Multiversion_concurrency_control",
            "Data_lakehouse", "Change_data_capture",
        )
        + ["https://hudi.apache.org/docs/overview/"],
    },
    "apache-parquet": {
        "tags": ["apache parquet", "columnar storage format", "column oriented dbms", "predicate pushdown", "data compression"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Parquet", "Column-oriented_DBMS", "Database_index",
            "Data_serialization", "Data_compression", "Dictionary_coder",
        ),
    },
    "apache-avro": {
        "tags": ["apache avro", "row oriented serialization", "schema registry", "compact binary format", "remote procedure call"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Avro", "Data_serialization", "Serialization",
            "Schema_evolution", "Remote_procedure_call", "JSON",
        ),
    },
    "apache-orc": {
        "tags": ["apache orc", "optimized row columnar", "column oriented dbms", "stripe encoding", "run length encoding"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_ORC", "Column-oriented_DBMS", "Database_index",
            "Data_serialization", "Run-length_encoding", "Data_compression",
        ),
    },
    "apache-arrow": {
        "tags": ["apache arrow", "in memory columnar", "zero copy interchange", "vectorized execution", "single instruction multiple data"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Arrow", "Column-oriented_DBMS", "Serialization",
            "SIMD", "In-memory_processing",
        )
        + ["https://arrow.apache.org/docs/"],
    },
    "apache-nifi": {
        "tags": ["apache nifi", "data flow automation", "extract transform load", "flow based programming", "data provenance"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_NiFi", "Dataflow_programming", "Extract,_transform,_load",
            "Pipeline_(computing)", "Data_lineage", "Message_broker",
        ),
    },
    "apache-pulsar": {
        "tags": ["apache pulsar", "publish subscribe messaging", "multi tenant streaming", "message broker", "geo replication"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Publish%E2%80%93subscribe_pattern", "Message_broker", "Stream_processing",
            "Message-oriented_middleware", "Replication_(computing)",
        )
        + ["https://pulsar.apache.org/docs/"],
    },
    "apache-storm": {
        "tags": ["apache storm", "real time computation", "stream processing", "distributed topology", "fault tolerance"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Storm", "Stream_processing", "Real-time_computing",
            "Fault_tolerance", "Distributed_computing", "Data_stream",
        ),
    },
    "apache-samza": {
        "tags": ["apache samza", "stateful stream processing", "apache kafka integration", "distributed streaming", "event stream processing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Samza", "Stream_processing", "Kafka_Streams",
            "Event_stream_processing", "Apache_Kafka", "Fault_tolerance",
        ),
    },
    "rabbitmq": {
        "tags": ["rabbitmq broker", "advanced message queuing protocol", "message broker", "work queues", "enterprise messaging system"],
        "license": CC_BY_SA,
        "pages": wiki(
            "RabbitMQ", "Advanced_Message_Queuing_Protocol", "Message_broker",
            "Enterprise_messaging_system", "Publish%E2%80%93subscribe_pattern", "Message-oriented_middleware",
        ),
    },
    "nats-messaging": {
        "tags": ["nats messaging", "publish subscribe pattern", "message oriented middleware", "lightweight broker", "event driven architecture"],
        "license": CC_BY_SA,
        "pages": wiki(
            "NATS_Messaging", "Publish%E2%80%93subscribe_pattern", "Message-oriented_middleware",
            "Message_broker", "Event-driven_architecture", "Enterprise_messaging_system",
        ),
    },
    "zeromq": {
        "tags": ["zeromq library", "message oriented middleware", "asynchronous messaging", "socket patterns", "distributed messaging"],
        "license": CC_BY_SA,
        "pages": wiki(
            "ZeroMQ", "Message-oriented_middleware", "Message_broker",
            "Publish%E2%80%93subscribe_pattern", "Distributed_computing", "Remote_procedure_call",
        ),
    },
    "polars": {
        "tags": ["polars dataframe", "rust dataframe library", "lazy query engine", "vectorized execution", "lazy evaluation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Polars_(software)", "Pandas_(software)", "Apache_Arrow",
            "Lazy_evaluation", "Column-oriented_DBMS",
        )
        + ["https://docs.pola.rs/"],
    },
    "dask": {
        "tags": ["dask parallel", "parallel computing python", "distributed dataframe", "task scheduling", "out of core computing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Dask_(software)", "Parallel_computing", "Pandas_(software)",
            "Scheduling_(computing)", "Distributed_computing", "Directed_acyclic_graph",
        ),
    },
    "apache-superset": {
        "tags": ["apache superset", "data visualization", "business intelligence dashboards", "sql exploration", "reporting dashboards"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Superset", "Data_visualization", "Dashboard_(computing)",
            "Business_intelligence", "SQL",
        )
        + ["https://superset.apache.org/docs/intro"],
    },
    "metabase": {
        "tags": ["metabase analytics", "business intelligence tool", "self service dashboards", "data visualization", "ad hoc querying"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Business_intelligence", "Data_visualization", "Dashboard_(computing)",
            "Query_language", "Web_analytics",
        )
        + ["https://www.metabase.com/docs/latest/"],
    },
    "apache-druid": {
        "tags": ["apache druid", "real time analytics database", "online analytical processing", "time series olap", "columnar storage"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Druid", "Online_analytical_processing", "Column-oriented_DBMS",
            "Real-time_computing", "Time_series_database", "Data_stream",
        ),
    },
    "presto-db": {
        "tags": ["presto query engine", "distributed sql engine", "massively parallel processing", "interactive analytics", "query optimization"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Presto_(SQL_query_engine)", "Massively_parallel", "Query_optimization",
            "SQL", "Distributed_computing", "Data_virtualization",
        ),
    },
    "dremio": {
        "tags": ["dremio lakehouse", "data virtualization", "query acceleration", "self service analytics", "columnar cache"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Data_virtualization", "Query_optimization", "Data_lakehouse",
            "Apache_Arrow", "Massively_parallel",
        )
        + ["https://docs.dremio.com/"],
    },
    "great-expectations": {
        "tags": ["great expectations", "data validation framework", "data quality testing", "pipeline assertions", "unit testing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Data_validation", "Data_quality", "Extract,_transform,_load",
            "Unit_testing", "Anomaly_detection",
        )
        + ["https://greatexpectations.io/"],
    },
    "feature-store": {
        "tags": ["feature store", "feature engineering", "machine learning features", "online offline serving", "training serving skew"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Feature_store", "Feature_engineering", "Data_catalog",
            "Metadata", "Machine_learning", "Materialized_view",
        ),
    },
    "data-catalog": {
        "tags": ["data catalog", "metadata management", "data discovery", "data governance", "data dictionary"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Data_catalog", "Metadata", "Data_governance",
            "Data_quality", "Data_dictionary", "Data_lineage",
        ),
    },
    "data-mesh": {
        "tags": ["data mesh", "domain oriented ownership", "data as a product", "decentralized architecture", "domain driven design"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Data_mesh", "Data_governance", "Data_lakehouse",
            "Data_catalog", "Domain-driven_design", "Data_engineering",
        ),
    },
    "data-lakehouse": {
        "tags": ["data lakehouse", "open table format", "unified storage layer", "data warehouse convergence", "object storage"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Data_lakehouse", "Data_warehouse", "Delta_Lake",
            "Apache_Iceberg", "Data_lake", "Object_storage",
        ),
    },
    "change-data-capture": {
        "tags": ["change data capture", "database replication", "write ahead logging", "incremental sync", "database trigger"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Change_data_capture", "Replication_(computing)", "Write-ahead_logging",
            "Database_trigger", "Eventual_consistency", "Data_stream",
        ),
    },
    "debezium": {
        "tags": ["debezium connector", "change data capture", "database trigger streaming", "kafka connect", "write ahead logging"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Change_data_capture", "Write-ahead_logging", "Replication_(computing)",
            "Apache_Kafka", "Database_trigger",
        )
        + ["https://debezium.io/documentation/"],
    },
    "apache-zookeeper": {
        "tags": ["apache zookeeper", "distributed coordination service", "consensus algorithm", "configuration management", "leader election"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_ZooKeeper", "Consensus_(computer_science)", "Fault_tolerance",
            "Replication_(computing)", "Distributed_computing", "CAP_theorem",
        ),
    },
    "apache-kafka-streams": {
        "tags": ["kafka streams", "stream processing library", "stateful stream processing", "event driven microservices", "apache kafka"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kafka_Streams", "Stream_processing", "Event_stream_processing",
            "Apache_Kafka", "Event-driven_architecture",
        )
        + ["https://kafka.apache.org/documentation/streams/"],
    },
    "ksqldb": {
        "tags": ["ksqldb engine", "streaming sql", "continuous query", "materialized view streaming", "event stream processing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Continuous_query", "Stream_processing", "Materialized_view",
            "Data_stream_management_system", "Event_stream_processing",
        )
        + ["https://docs.ksqldb.io/en/latest/"],
    },
    "stream-processing-concepts": {
        "tags": ["stream processing", "event stream processing", "data stream management system", "windowing state", "complex event processing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Stream_processing", "Event_stream_processing", "Data_stream_management_system",
            "Complex_event_processing", "Data_stream", "Real-time_computing",
        ),
    },
    "batch-vs-streaming": {
        "tags": ["batch processing", "lambda architecture", "real time computing", "micro batching", "stream processing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Batch_processing", "Stream_processing", "Lambda_architecture",
            "Real-time_computing", "Data_processing", "Big_data",
        ),
    },
    "olap-cube": {
        "tags": ["olap cube", "online analytical processing", "multidimensional analysis", "aggregation rollup", "data warehouse"],
        "license": CC_BY_SA,
        "pages": wiki(
            "OLAP_cube", "Online_analytical_processing", "Data_warehouse",
            "Dimensional_modeling", "Star_schema", "Business_intelligence",
        ),
    },
    "star-schema-modeling": {
        "tags": ["star schema", "snowflake schema", "fact table", "dimensional modeling", "data warehouse"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Star_schema", "Snowflake_schema", "Fact_table",
            "Dimensional_modeling", "Data_warehouse", "Dimension_(data_warehouse)",
        ),
    },
    "slowly-changing-dimension": {
        "tags": ["slowly changing dimension", "dimension data warehouse", "historical tracking", "type two dimension", "dimensional modeling"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Slowly_changing_dimension", "Dimension_(data_warehouse)", "Dimensional_modeling",
            "Data_warehouse", "Star_schema", "Fact_table",
        ),
    },
    "data-vault-modeling": {
        "tags": ["data vault modeling", "hub link satellite", "agile data warehouse", "ensemble modeling", "database schema"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Data_vault_modeling", "Data_warehouse", "Dimensional_modeling",
            "Database_schema", "Relational_database", "Dimension_(data_warehouse)",
        ),
    },
    "columnar-format": {
        "tags": ["columnar storage", "column oriented dbms", "vectorized query", "compression encoding", "single instruction multiple data"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Column-oriented_DBMS", "Apache_Parquet", "Apache_ORC",
            "Database_index", "SIMD", "Data_compression",
        ),
    },
    "workflow-orchestration": {
        "tags": ["workflow orchestration", "directed acyclic graph", "task scheduling", "pipeline automation", "data orchestration"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Orchestration_(computing)", "Workflow_management_system", "Directed_acyclic_graph",
            "Scheduling_(computing)", "Pipeline_(computing)", "Fault_tolerance",
        ),
    },
}
