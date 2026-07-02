"""AI beyond ML basics, data engineering, and caching — the data-heavy half of the stack."""

from .common import CC_BY_SA, wiki

DOMAINS = {
    "classic-ai": {
        "tags": ["artificial intelligence", "expert system", "knowledge representation", "nlp", "computer vision", "symbolic ai"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Artificial_intelligence",
            "Expert_system",
            "Knowledge_representation_and_reasoning",
            "Automated_planning_and_scheduling",
            "Natural_language_processing",
            "Computer_vision",
            "Speech_recognition",
            "Symbolic_artificial_intelligence",
            "Turing_test",
            "Ontology_(information_science)",
            "Semantic_network",
        ),
    },
    "data-engineering": {
        "tags": ["etl", "data warehouse", "data pipeline", "kafka", "stream processing", "message queue"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Extract,_transform,_load",
            "Data_warehouse",
            "Data_lake",
            "Apache_Kafka",
            "Message_queue",
            "Stream_processing",
            "Batch_processing",
            "Online_analytical_processing",
            "Online_transaction_processing",
            "Change_data_capture",
            "Star_schema",
        ),
    },
    "caching": {
        "tags": ["cache invalidation", "cdn", "consistent hashing", "cache eviction", "memcached"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cache_replacement_policies",
            "Content_delivery_network",
            "Consistent_hashing",
            "Memcached",
            "Cache_coherence",
            "Time_to_live",
            "Hash_function",
        ),
    },
}
