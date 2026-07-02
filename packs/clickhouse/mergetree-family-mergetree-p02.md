---
title: "MergeTree table engine (part 2/2)"
source: https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree
domain: clickhouse
license: CC-BY-SA-4.0
tags: clickhouse, columnar olap, mergetree engine, column-oriented dbms
fetched: 2026-07-02
part: 2/2
---

## Using multiple block devices for data storage

### Introduction

`MergeTree` family table engines can store data on multiple block devices. For example, it can be useful when the data of a certain table are implicitly split into "hot" and "cold". The most recent data is regularly requested but requires only a small amount of space. On the contrary, the fat-tailed historical data is requested rarely. If several disks are available, the "hot" data may be located on fast disks (for example, NVMe SSDs or in memory), while the "cold" data - on relatively slow ones (for example, HDD).

This applies to all disk types, including S3 and other object storage disks. For example, you can spread data across multiple S3 buckets within a single volume, or create tiered policies that move data from local disks to S3. See Using S3 disks with multiple volumes for details.

Data part is the minimum movable unit for `MergeTree`-engine tables. The data belonging to one part are stored on one disk. Data parts can be moved between disks in the background (according to user settings) as well as by means of the ALTER queries.

### Terms

- Disk — Block device mounted to the filesystem.
- Default disk — Disk that stores the path specified in the path server setting.
- Volume — Ordered set of equal disks (similar to JBOD).
- Storage policy — Set of volumes and the rules for moving data between them.

The names given to the described entities can be found in the system tables, system.storage_policies and system.disks. To apply one of the configured storage policies for a table, use the `storage_policy` setting of `MergeTree`-engine family tables.

### Configuration

Disks, volumes and storage policies should be declared inside the `<storage_configuration>` tag either in a file in the `config.d` directory.

Tip

Disks can also be declared in the `SETTINGS` section of a query. This is useful for ad-hoc analysis to temporarily attach a disk that is, for example, hosted at a URL. See dynamic storage for more details.

Configuration structure:

```xml
<storage_configuration>
    <disks>
        <disk_name_1> <!-- disk name -->
            <path>/mnt/fast_ssd/clickhouse/</path>
        </disk_name_1>
        <disk_name_2>
            <path>/mnt/hdd1/clickhouse/</path>
            <keep_free_space_bytes>10485760</keep_free_space_bytes>
        </disk_name_2>
        <disk_name_3>
            <path>/mnt/hdd2/clickhouse/</path>
            <keep_free_space_bytes>10485760</keep_free_space_bytes>
        </disk_name_3>

        ...
    </disks>

    ...
</storage_configuration>
```

Tags:

- `<disk_name_N>` — Disk name. Names must be different for all disks.
- `path` — path under which a server will store data (`data` and `shadow` folders), should be terminated with '/'.
- `keep_free_space_bytes` — the amount of free disk space to be reserved.

The order of the disk definition is not important.

Storage policies configuration markup:

```xml
<storage_configuration>
    ...
    <policies>
        <policy_name_1>
            <volumes>
                <volume_name_1>
                    <disk>disk_name_from_disks_configuration</disk>
                    <max_data_part_size_bytes>1073741824</max_data_part_size_bytes>
                    <load_balancing>round_robin</load_balancing>
                </volume_name_1>
                <volume_name_2>
                    <!-- configuration -->
                </volume_name_2>
                <!-- more volumes -->
            </volumes>
            <move_factor>0.2</move_factor>
        </policy_name_1>
        <policy_name_2>
            <!-- configuration -->
        </policy_name_2>

        <!-- more policies -->
    </policies>
    ...
</storage_configuration>
```

Tags:

- `policy_name_N` — Policy name. Policy names must be unique.
- `volume_name_N` — Volume name. Volume names must be unique.
- `disk` — a disk within a volume.
- `max_data_part_size_bytes` — the maximum size of a part that can be stored on any of the volume's disks. If the a size of a merged part estimated to be bigger than `max_data_part_size_bytes` then this part will be written to a next volume. Basically this feature allows to keep new/small parts on a hot (SSD) volume and move them to a cold (HDD) volume when they reach large size. Do not use this setting if your policy has only one volume.
- `move_factor` — when the amount of available space gets lower than this factor, data automatically starts to move on the next volume if any (by default, 0.1). ClickHouse sorts existing parts by size from largest to smallest (in descending order) and selects parts with the total size that is sufficient to meet the `move_factor` condition. If the total size of all parts is insufficient, all parts will be moved.
- `perform_ttl_move_on_insert` — Disables TTL move on data part INSERT. By default (if enabled) if we insert a data part that already expired by the TTL move rule it immediately goes to a volume/disk declared in move rule. This can significantly slowdown insert in case if destination volume/disk is slow (e.g. S3). If disabled then already expired data part is written into a default volume and then right after moved to TTL volume.
- `load_balancing` - Policy for disk balancing, `round_robin` or `least_used`.
- `least_used_ttl_ms` - Configure timeout (in milliseconds) for the updating available space on all disks (`0` - update always, `-1` - never update, default is `60000`). Note, if the disk can be used by ClickHouse only and is not subject to a online filesystem resize/shrink you can use `-1`, in all other cases it is not recommended, since eventually it will lead to incorrect space distribution.
- `prefer_not_to_merge` — You should not use this setting. Disables merging of data parts on this volume (this is harmful and leads to performance degradation). When this setting is enabled (don't do it), merging data on this volume is not allowed (which is bad). This allows (but you don't need it) controlling (if you want to control something, you're making a mistake) how ClickHouse works with slow disks (but ClickHouse knows better, so please don't use this setting).
- `volume_priority` — Defines the priority (order) in which volumes are filled. Lower value means higher priority. The parameter values should be natural numbers and collectively cover the range from 1 to N (lowest priority given) without skipping any numbers.
  - If *all* volumes are tagged, they are prioritized in given order.
  - If only *some* volumes are tagged, those without the tag have the lowest priority, and they are prioritized in the order they are defined in config.
  - If *no* volumes are tagged, their priority is set correspondingly to their order they are declared in configuration.
  - Two volumes cannot have the same priority value.

Configuration examples:

```xml
<storage_configuration>
    ...
    <policies>
        <hdd_in_order> <!-- policy name -->
            <volumes>
                <single> <!-- volume name -->
                    <disk>disk1</disk>
                    <disk>disk2</disk>
                </single>
            </volumes>
        </hdd_in_order>

        <moving_from_ssd_to_hdd>
            <volumes>
                <hot>
                    <disk>fast_ssd</disk>
                    <max_data_part_size_bytes>1073741824</max_data_part_size_bytes>
                </hot>
                <cold>
                    <disk>disk1</disk>
                </cold>
            </volumes>
            <move_factor>0.2</move_factor>
        </moving_from_ssd_to_hdd>

        <small_jbod_with_external_no_merges>
            <volumes>
                <main>
                    <disk>jbod1</disk>
                </main>
                <external>
                    <disk>external</disk>
                </external>
            </volumes>
        </small_jbod_with_external_no_merges>
    </policies>
    ...
</storage_configuration>
```

In given example, the `hdd_in_order` policy implements the round-robin approach. Thus this policy defines only one volume (`single`), the data parts are stored on all its disks in circular order. Such policy can be quite useful if there are several similar disks are mounted to the system, but RAID is not configured. Keep in mind that each individual disk drive is not reliable and you might want to compensate it with replication factor of 3 or more.

If there are different kinds of disks available in the system, `moving_from_ssd_to_hdd` policy can be used instead. The volume `hot` consists of an SSD disk (`fast_ssd`), and the maximum size of a part that can be stored on this volume is 1GB. All the parts with the size larger than 1GB will be stored directly on the `cold` volume, which contains an HDD disk `disk1`. Also, once the disk `fast_ssd` gets filled by more than 80%, data will be transferred to the `disk1` by a background process.

The order of volume enumeration within a storage policy is important in case at least one of the volumes listed has no explicit `volume_priority` parameter. Once a volume is overfilled, data are moved to the next one. The order of disk enumeration is important as well because data are stored on them in turns.

When creating a table, one can apply one of the configured storage policies to it:

```sql
CREATE TABLE table_with_non_default_policy (
    EventDate Date,
    OrderID UInt64,
    BannerID UInt64,
    SearchPhrase String
) ENGINE = MergeTree
ORDER BY (OrderID, BannerID)
PARTITION BY toYYYYMM(EventDate)
SETTINGS storage_policy = 'moving_from_ssd_to_hdd'
```

The `default` storage policy implies using only one volume, which consists of only one disk given in `<path>`. You could change storage policy after table creation with [ALTER TABLE ... MODIFY SETTING] query, new policy should include all old disks and volumes with same names.

The number of threads performing background moves of data parts can be changed by background_move_pool_size setting.

### Details

In the case of `MergeTree` tables, data is getting to disk in different ways:

- As a result of an insert (`INSERT` query).
- During background merges and mutations.
- When downloading from another replica.
- As a result of partition freezing ALTER TABLE ... FREEZE PARTITION.

In all these cases except for mutations and partition freezing, a part is stored on a volume and a disk according to the given storage policy:

1. The first volume (in the order of definition) that has enough disk space for storing a part (`unreserved_space > current_part_size`) and allows for storing parts of a given size (`max_data_part_size_bytes > current_part_size`) is chosen.
2. Within this volume, that disk is chosen that follows the one, which was used for storing the previous chunk of data, and that has free space more than the part size (`unreserved_space - keep_free_space_bytes > current_part_size`).

Under the hood, mutations and partition freezing make use of hard links. Hard links between different disks are not supported, therefore in such cases the resulting parts are stored on the same disks as the initial ones.

In the background, parts are moved between volumes on the basis of the amount of free space (`move_factor` parameter) according to the order the volumes are declared in the configuration file. Data is never transferred from the last one and into the first one. One may use system tables system.part_log (field `type = MOVE_PART`) and system.parts (fields `path` and `disk`) to monitor background moves. Also, the detailed information can be found in server logs.

User can force moving a part or a partition from one volume to another using the query ALTER TABLE ... MOVE PART|PARTITION ... TO VOLUME|DISK ..., all the restrictions for background operations are taken into account. The query initiates a move on its own and does not wait for background operations to be completed. User will get an error message if not enough free space is available or if any of the required conditions are not met.

Moving data does not interfere with data replication. Therefore, different storage policies can be specified for the same table on different replicas.

After the completion of background merges and mutations, old parts are removed only after a certain amount of time (`old_parts_lifetime`). During this time, they are not moved to other volumes or disks. Therefore, until the parts are finally removed, they are still taken into account for evaluation of the occupied disk space.

User can assign new big parts to different disks of a JBOD volume in a balanced way using the min_bytes_to_rebalance_partition_over_jbod setting.


## Using external storage for data storage

MergeTree family table engines can store data to `S3`, `AzureBlobStorage`, `HDFS` using a disk with types `s3`, `azure_blob_storage`, `hdfs` accordingly. See configuring external storage options for more details.

Example for S3 as external storage using a disk with type `s3`.

Configuration markup:

```xml
<storage_configuration>
    ...
    <disks>
        <s3>
            <type>s3</type>
            <support_batch_delete>true</support_batch_delete>
            <endpoint>https://clickhouse-public-datasets.s3.amazonaws.com/my-bucket/root-path/</endpoint>
            <access_key_id>your_access_key_id</access_key_id>
            <secret_access_key>your_secret_access_key</secret_access_key>
            <region></region>
            <header>Authorization: Bearer SOME-TOKEN</header>
            <server_side_encryption_customer_key_base64>your_base64_encoded_customer_key</server_side_encryption_customer_key_base64>
            <server_side_encryption_kms_key_id>your_kms_key_id</server_side_encryption_kms_key_id>
            <server_side_encryption_kms_encryption_context>your_kms_encryption_context</server_side_encryption_kms_encryption_context>
            <server_side_encryption_kms_bucket_key_enabled>true</server_side_encryption_kms_bucket_key_enabled>
            <proxy>
                <uri>http://proxy1</uri>
                <uri>http://proxy2</uri>
            </proxy>
            <connect_timeout_ms>10000</connect_timeout_ms>
            <request_timeout_ms>5000</request_timeout_ms>
            <retry_attempts>10</retry_attempts>
            <single_read_retries>4</single_read_retries>
            <min_bytes_for_seek>1000</min_bytes_for_seek>
            <metadata_path>/var/lib/clickhouse/disks/s3/</metadata_path>
            <skip_access_check>false</skip_access_check>
        </s3>
        <s3_cache>
            <type>cache</type>
            <disk>s3</disk>
            <path>/var/lib/clickhouse/disks/s3_cache/</path>
            <max_size>10Gi</max_size>
        </s3_cache>
    </disks>
    ...
</storage_configuration>
```

Also see configuring external storage options.

### Using S3 disks with multiple volumes

S3 (and other object storage) disks can be used in multi-disk and multi-volume storage policies the same way as local disks. This allows you to spread data across multiple S3 buckets within a single volume (JBOD-style), or set up tiered storage policies with S3 volumes.

For example, to distribute data across two S3 buckets in a round-robin fashion:

```xml
<storage_configuration>
    <disks>
        <s3_bucket1>
            <type>s3</type>
            <endpoint>https://s3.amazonaws.com/bucket-1/data/</endpoint>
            <access_key_id>your_access_key_id</access_key_id>
            <secret_access_key>your_secret_access_key</secret_access_key>
        </s3_bucket1>
        <s3_bucket2>
            <type>s3</type>
            <endpoint>https://s3.amazonaws.com/bucket-2/data/</endpoint>
            <access_key_id>your_access_key_id</access_key_id>
            <secret_access_key>your_secret_access_key</secret_access_key>
        </s3_bucket2>
    </disks>
    <policies>
        <s3_multi_bucket>
            <volumes>
                <main>
                    <disk>s3_bucket1</disk>
                    <disk>s3_bucket2</disk>
                </main>
            </volumes>
        </s3_multi_bucket>
    </policies>
</storage_configuration>
```

You can also combine local and S3 volumes in a tiered policy, for example moving data from a local SSD to S3 as it ages:

```xml
<storage_configuration>
    <disks>
        <local_ssd>
            <path>/mnt/fast_ssd/clickhouse/</path>
        </local_ssd>
        <s3_cold>
            <type>s3</type>
            <endpoint>https://s3.amazonaws.com/cold-storage/data/</endpoint>
            <access_key_id>your_access_key_id</access_key_id>
            <secret_access_key>your_secret_access_key</secret_access_key>
        </s3_cold>
    </disks>
    <policies>
        <local_to_s3>
            <volumes>
                <hot>
                    <disk>local_ssd</disk>
                    <max_data_part_size_bytes>1073741824</max_data_part_size_bytes>
                </hot>
                <cold>
                    <disk>s3_cold</disk>
                </cold>
            </volumes>
            <move_factor>0.2</move_factor>
        </local_to_s3>
    </policies>
</storage_configuration>
```

Note

When using `use_environment_credentials` for S3 authentication, the environment credentials (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`) are shared across all S3 disks. It is not possible to use different environment credentials for different disks. If you need different credentials for each S3 disk, use explicit `access_key_id` and `secret_access_key` settings per disk instead.

It is possible to set up non-replicated MergeTree tables with a one-writer, many-readers scenario on shared storage. This is provided by the automatic refresh of the parts list, which can be set up on readers. Note that this requires shared filesystem metadata across replicas (or `table_disk = true` with a table-local disk). See refresh_parts_interval and table_disk.

cache configuration

ClickHouse versions 22.3 through 22.7 use a different cache configuration, see using local cache if you are using one of those versions.


## Virtual columns

- `_part` — Name of a part.
- `_part_index` — Sequential index of the part in the query result.
- `_part_starting_offset` — Cumulative starting row of the part in the query result.
- `_part_offset` — Number of row in the part.
- `_part_granule_offset` — Number of granule in the part.
- `_partition_id` — Name of a partition.
- `_part_uuid` — Unique part identifier (if enabled MergeTree setting `assign_part_uuids`).
- `_part_data_version` — Data version of part (either min block number or mutation version).
- `_partition_value` — Values (a tuple) of a `partition by` expression.
- `_sample_factor` — Sample factor (from the query).
- `_block_number` — Original number of block for row that was assigned at insert, persisted on merges when setting `enable_block_number_column` is enabled.
- `_block_offset` — Original number of row in block that was assigned at insert, persisted on merges when setting `enable_block_offset_column` is enabled.
- `_disk_name` — Disk name used for the storage.


## Column statistics

Not supported in ClickHouse Cloud

The statistics declaration is in the columns section of the `CREATE` query for tables from the `*MergeTree*` Family:

```sql
CREATE TABLE tab
(
    a Int64 STATISTICS(TDigest, Uniq),
    b Float64
)
ENGINE = MergeTree
ORDER BY a
```

We can also manipulate statistics with `ALTER` statements:

```sql
ALTER TABLE tab ADD STATISTICS b TYPE TDigest, Uniq;
ALTER TABLE tab DROP STATISTICS a;
```

These lightweight statistics aggregate information about distribution of values in columns. Statistics are stored in every part and updated when every insert comes. They can be used for prewhere optimization only if we enable `set use_statistics = 1`.

#### Part Pruning with Statistics

When `use_statistics_for_part_pruning` is enabled, statistics can be used for part pruning. Currently, only `MinMax` and `Basic` statistics support part pruning. When such statistics are defined on a column, ClickHouse tracks the minimum and maximum values for that column in each part. Part pruning allows to skip reading entire data parts when the query filter condition cannot match any rows in that part.

**Example:**

```sql
-- Create a table with MinMax statistics on the 'value' column
CREATE TABLE test_stats
(
    id UInt64,
    value Int64 STATISTICS(MinMax)
)
ENGINE = MergeTree
ORDER BY id;

SYSTEM STOP MERGES test_stats;

-- Insert data in separate inserts to create multiple parts
INSERT INTO test_stats SELECT number, number FROM numbers(1000); -- Part 1: value range [0, 999]
INSERT INTO test_stats SELECT number, number + 10000 FROM numbers(1000); -- Part 2: value range [10000, 10999]

SET use_statistics_for_part_pruning = 1;

-- This query will skip Part 1 entirely because its max value (999) < 5000
SELECT count() FROM test_stats WHERE value > 5000;

-- Use EXPLAIN to see the pruning effect
EXPLAIN indexes = 1 SELECT count() FROM test_stats WHERE value > 5000;
-- The output will show "Parts: 1/2" indicating one part was pruned
```

### Available types of column statistics

- `Basic` A compact bundle of single-value summaries derived from a column. Depending on the column type, the following pieces are populated:
  - for any column whose values are represented by a number (integers, floats, `Decimal*`, `Date*`, `DateTime*`, `Enum*`, `IPv4`, ...): the minimum and maximum value, which allow to estimate the selectivity of range filters and enable part pruning;
  - for `String` and `FixedString` columns: the total byte length of non-`NULL` values (from which the average string length can be derived);
  - for `Nullable` and `LowCardinality(Nullable)` columns: the count of `NULL` values, which the optimizer uses to discount `NULL` rows from selectivity estimates. A single `Basic` statistic can populate several of these at once — for example on a `Nullable(UInt32)` column it tracks both numeric min/max and the null count. Compared to `MinMax`, `Basic` additionally works on `String` / `FixedString` columns and can be declared on `Nullable` wrappers of types like `UUID` or `IPv6` purely to track the null count. Syntax: `basic`
- `MinMax` The minimum and maximum column value which allows to estimate the selectivity of range filters on numeric columns. Syntax: `minmax`
- `TDigest` TDigest sketches which allow to compute approximate percentiles (e.g. the 90th percentile) for numeric columns. Syntax: `tdigest`
- `Uniq` HyperLogLog sketches which provide an estimation how many distinct values a column contains. Syntax: `uniq`
- `CountMin` CountMin sketches which provide an approximate count of the frequency of each value in a column. Syntax `countmin`

### Supported data types

|   | (U)Int*, Float*, Decimal(*), Date*, Boolean, Enum* | IPv4 | String or FixedStringBasic✔✔✔CountMin✔✔✔MinMax✔✔✗TDigest✔✗✗Uniq✔✔✔ |
|---|---|---|---|

All of the above also accept `Nullable` and `LowCardinality(Nullable)` wrappers of the listed types. `Basic` may additionally be declared on `Nullable` wrappers of types like `UUID` or `IPv6` purely to track the null count.

### Supported operations

|   | Equality filters (==) | Range filters (`>, >=, <, <=`)Basic✗✔ (numeric columns only)CountMin✔✗MinMax✗✔ (numeric columns only)TDigest✗✔ (numeric columns only)Uniq✔✗ |
|---|---|---|

For `Basic` on `String` / `FixedString` columns the statistic only records the total non-NULL byte length (used to estimate average string length) and the null count; range filters and part pruning are not driven by it.


## Column-level settings

Certain MergeTree settings can be overridden at column level:

- `max_compress_block_size` — Maximum size of blocks of uncompressed data before compressing for writing to a table.
- `min_compress_block_size` — Minimum size of blocks of uncompressed data required for compression when writing the next mark.

Example:

```sql
CREATE TABLE tab
(
    id Int64,
    document String SETTINGS (min_compress_block_size = 16777216, max_compress_block_size = 16777216)
)
ENGINE = MergeTree
ORDER BY id
```

Column-level settings can be modified or removed using ALTER MODIFY COLUMN, for example:

- Remove `SETTINGS` from column declaration:

```sql
ALTER TABLE tab MODIFY COLUMN document REMOVE SETTINGS;
```

- Modify a setting:

```sql
ALTER TABLE tab MODIFY COLUMN document MODIFY SETTING min_compress_block_size = 8192;
```

- Reset one or more settings, also removes the setting declaration in the column expression of the table's CREATE query.

```sql
ALTER TABLE tab MODIFY COLUMN document RESET SETTING min_compress_block_size;
```
