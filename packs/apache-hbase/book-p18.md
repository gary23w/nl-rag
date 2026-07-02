---
title: "Apache HBase® Reference Guide (part 18/41)"
source: https://hbase.apache.org/book.html
domain: apache-hbase
license: CC-BY-SA-4.0
tags: apache hbase, bigtable clone, wide-column store, apache hadoop
fetched: 2026-07-02
part: 18/41
---

## 75. Storing Medium-sized Objects (MOB)

Data comes in many sizes, and saving all of your data in HBase, including binary data such as images and documents, is ideal. While HBase can technically handle binary objects with cells that are larger than 100 KB in size, HBase’s normal read and write paths are optimized for values smaller than 100KB in size. When HBase deals with large numbers of objects over this threshold, referred to here as medium objects, or MOBs, performance is degraded due to write amplification caused by splits and compactions. When using MOBs, ideally your objects will be between 100KB and 10MB (see the FAQ). HBase 2 added special internal handling of MOBs to maintain performance, consistency, and low operational overhead. MOB support is provided by the work done in HBASE-11339. To take advantage of MOB, you need to use HFile version 3. Optionally, configure the MOB file reader’s cache settings for each RegionServer (see Configuring the MOB Cache), then configure specific columns to hold MOB data. Client code does not need to change to take advantage of HBase MOB support. The feature is transparent to the client.

### 75.1. Configuring Columns for MOB

You can configure columns to support MOB during table creation or alteration, either in HBase Shell or via the Java API. The two relevant properties are the boolean `IS_MOB` and the `MOB_THRESHOLD`, which is the number of bytes at which an object is considered to be a MOB. Only `IS_MOB` is required. If you do not specify the `MOB_THRESHOLD`, the default threshold value of 100 KB is used.

Configure a Column for MOB Using HBase Shell

```
hbase> create 't1', {NAME => 'f1', IS_MOB => true, MOB_THRESHOLD => 102400}
hbase> alter 't1', {NAME => 'f1', IS_MOB => true, MOB_THRESHOLD => 102400}
```

Example 25. Configure a Column for MOB Using the Java API

```
...
HColumnDescriptor hcd = new HColumnDescriptor(“f”);
hcd.setMobEnabled(true);
...
hcd.setMobThreshold(102400L);
...
```

### 75.2. Testing MOB

The utility `org.apache.hadoop.hbase.IntegrationTestIngestWithMOB` is provided to assist with testing the MOB feature. The utility is run as follows:

```
$ sudo -u hbase hbase org.apache.hadoop.hbase.IntegrationTestIngestWithMOB \
            -threshold 1024 \
            -minMobDataSize 512 \
            -maxMobDataSize 5120
```

- `**threshold**` is the threshold at which cells are considered to be MOBs. The default is 1 kB, expressed in bytes.
- `**minMobDataSize**` is the minimum value for the size of MOB data. The default is 512 B, expressed in bytes.
- `**maxMobDataSize**` is the maximum value for the size of MOB data. The default is 5 kB, expressed in bytes.

### 75.3. MOB architecture

This section is derived from information found in HBASE-11339, which covered the initial GA implementation of MOB in HBase and HBASE-22749, which improved things by parallelizing MOB maintenance across the RegionServers. For more information see the last version of the design doc created during the initial work, "HBASE-11339 MOB GA design.pdf", and the design doc for the distributed mob compaction feature, "HBASE-22749 MOB distributed compaction.pdf".

#### 75.3.1. Overview

The MOB feature reduces the overall IO load for configured column families by storing values that are larger than the configured threshold outside of the normal regions to avoid splits, merges, and most importantly normal compactions.

When a cell is first written to a region it is stored in the WAL and memstore regardless of value size. When memstores from a column family configured to use MOB are eventually flushed two hfiles are written simultaneously. Cells with a value smaller than the threshold size are written to a normal region hfile. Cells with a value larger than the threshold are written into a special MOB hfile and also have a MOB reference cell written into the normal region HFile. As the Region Server flushes a MOB enabled memstore and closes a given normal region HFile it appends metadata that lists each of the special MOB hfiles referenced by the cells within.

MOB reference cells have the same key as the cell they are based on. The value of the reference cell is made up of two pieces of metadata: the size of the actual value and the MOB hfile that contains the original cell. In addition to any tags originally written to HBase, the reference cell prepends two additional tags. The first is a marker tag that says the cell is a MOB reference. This can be used later to scan specifically just for reference cells. The second stores the namespace and table at the time the MOB hfile is written out. This tag is used to optimize how the MOB system finds the underlying value in MOB hfiles after a series of HBase snapshot operations (ref HBASE-12332). Note that tags are only available within HBase servers and by default are not sent over RPCs.

All MOB hfiles for a given table are managed within a logical region that does not directly serve requests. When these MOB hfiles are created from a flush or MOB compaction they are placed in a dedicated mob data area under the hbase root directory specific to the namespace, table, mob logical region, and column family. In general that means a path structured like:

```
%HBase Root Dir%/mobdir/data/%namespace%/%table%/%logical region%/%column family%/
```

With default configs, an example table named 'some_table' in the default namespace with a MOB enabled column family named 'foo' this HDFS directory would be

```
/hbase/mobdir/data/default/some_table/372c1b27e3dc0b56c3a031926e5efbe9/foo/
```

These MOB hfiles are maintained by special chores in the HBase Master and across the individual Region Servers. Specifically those chores take care of enforcing TTLs and compacting them. Note that this compaction is primarily a matter of controlling the total number of files in HDFS because our operational assumptions for MOB data is that it will seldom update or delete.

When a given MOB hfile is no longer needed as a result of our compaction process then a chore in the Master will take care of moving it to the archive just like any normal hfile. Because the table’s mob region is independent of all the normal regions it can coexist with them in the regular archive storage area:

```
/hbase/archive/data/default/some_table/372c1b27e3dc0b56c3a031926e5efbe9/foo/
```

The same hfile cleaning chores that take care of eventually deleting unneeded archived files from normal regions thus also will take care of these MOB hfiles. As such, if there is a snapshot of a MOB enabled table then the cleaning system will make sure those MOB files stick around in the archive area as long as they are needed by a snapshot or a clone of a snapshot.

#### 75.3.2. MOB compaction

Each time the memstore for a MOB enabled column family performs a flush HBase will write values over the MOB threshold into MOB specific hfiles. When normal region compaction occurs the Region Server rewrites the normal data files while maintaining references to these MOB files without rewriting them. Normal client lookups for MOB values transparently will receive the original values because the Region Server internals take care of using the reference data to then pull the value out of a specific MOB file. This indirection means that building up a large number of MOB hfiles doesn’t impact the overall time to retrieve any specific MOB cell. Thus, we need not perform compactions of the MOB hfiles nearly as often as normal hfiles. As a result, HBase saves IO by not rewriting MOB hfiles as a part of the periodic compactions a Region Server does on its own.

However, if deletes and updates of MOB cells are frequent then this indirection will begin to waste space. The only way to stop using the space of a particular MOB hfile is to ensure no cells still hold references to it. To do that we need to ensure we have written the current values into a new MOB hfile. If our backing filesystem has a limitation on the number of files that can be present, as HDFS does, then even if we do not have deletes or updates of MOB cells eventually there will be a sufficient number of MOB hfiles that we will need to coalesce them.

Periodically a chore in the master coordinates having the region servers perform a special major compaction that also handles rewriting new MOB files. Like all compactions the Region Server will create updated hfiles that hold both the cells that are smaller than the MOB threshold and cells that hold references to the newly rewritten MOB file. Because this rewriting has the advantage of looking across all active cells for the region our several small MOB files should end up as a single MOB file per region. The chore defaults to running weekly and can be configured by setting `hbase.mob.compaction.chore.period` to the desired period in seconds.

```
<property>
    <name>hbase.mob.compaction.chore.period</name>
    <value>2592000</value>
    <description>Example of changing the chore period from a week to a month.</description>
</property>
```

By default, the periodic MOB compaction coordination chore will attempt to keep every region busy doing compactions in parallel in order to maximize the amount of work done on the cluster. If you need to tune the amount of IO this compaction generates on the underlying filesystem, you can control how many concurrent region-level compaction requests are allowed by setting `hbase.mob.major.compaction.region.batch.size` to an integer number greater than zero. If you set the configuration to 0 then you will get the default behavior of attempting to do all regions in parallel.

```
<property>
    <name>hbase.mob.major.compaction.region.batch.size</name>
    <value>1</value>
    <description>Example of switching from "as parallel as possible" to "serially"</description>
</property>
```

#### 75.3.3. MOB file archiving

Eventually we will have MOB hfiles that are no longer needed. Either clients will overwrite the value or a MOB-rewriting compaction will store a reference to a newer larger MOB hfile. Because any given MOB cell could have originally been written either in the current region or in a parent region that existed at some prior point in time, individual Region Servers do not decide when it is time to archive MOB hfiles. Instead a periodic chore in the Master evaluates MOB hfiles for archiving.

A MOB HFile will be subject to archiving under any of the following conditions:

- Any MOB HFile older than the column family’s TTL
- Any MOB HFile older than a "too recent" threshold with no references to it from the regular hfiles for all regions in a column family

To determine if a MOB HFile meets the second criteria the chore extracts metadata from the regular HFiles for each MOB enabled column family for a given table. That metadata enumerates the complete set of MOB HFiles needed to satisfy the references stored in the normal HFile area.

The period of the cleaner chore can be configured by setting `hbase.master.mob.cleaner.period` to a positive integer number of seconds. It defaults to running daily. You should not need to tune it unless you have a very aggressive TTL or a very high rate of MOB updates with a correspondingly high rate of non-MOB compactions.

### 75.4. MOB Optimization Tasks

#### 75.4.1. Further limiting write amplification

If your MOB workload has few to no updates or deletes then you can opt-in to MOB compactions that optimize for limiting the amount of write amplification. It achieves this by setting a size threshold to ignore MOB files during the compaction process. When a given region goes through MOB compaction it will evaluate the size of the MOB file that currently holds the actual value and skip rewriting the value if that file is over threshold.

The bound of write amplification in this mode can be approximated as Write Amplification=logK(MS)Write Amplification=logK(MS) where **K** is the number of files in compaction selection, **M** is the configurable threshold for MOB files size, and **S** is the minmum size of memstore flushes that create MOB files in the first place. For example given 5 files picked up per compaction, a threshold of 1 GB, and a flush size of 10MB the write amplification will be log5(1GB10MB)=log5(100)=2.86log5(1GB10MB)=log5(100)=2.86.

If we are using an underlying filesystem with a limitation on the number of files, such as HDFS, and we know our expected data set size we can choose our maximum file size in order to approach this limit but stay within it in order to minimize write amplification. For example, if we expect to store a petabyte and we have a conservative limitation of a million files in our HDFS instance, then 1PB1M=1GB1PB1M=1GB gives us a target limitation of a gigabyte per MOB file.

To opt-in to this compaction mode you must set `hbase.mob.compaction.type` to `optimized`. The default MOB size threshold in this mode is set to 1GB. It can be changed by setting `hbase.mob.compactions.max.file.size` to a positive integer number of bytes.

```
<property>
    <name>hbase.mob.compaction.type</name>
    <value>optimized</value>
    <description>opt-in to write amplification optimized mob compaction.</description>
</property>
<property>
    <name>hbase.mob.compactions.max.file.size</name>
    <value>10737418240</value>
    <description>Example of tuning the max mob file size to 10GB</dscription>
</property>
```

Additionally, when operating in this mode the compaction process will seek to avoid writing MOB files that are over the max file threshold. As it is writing out a additional MOB values into a MOB hfile it will check to see if the additional data causes the hfile to be over the max file size. When the hfile of MOB values reaches limit, the MOB hfile is committed to the MOB storage area and a new one is created. The hfile with reference cells will track the complete set of MOB hfiles it needs in its metadata.

|   | Be mindful of total time to complete compaction of a region When using the write amplification optimized compaction mode you need to watch for the maximum time to compact a single region. If it nears an hour you should read through the troubleshooting section below Adjusting the MOB cleaner’s tolerance for new hfiles. Failure to make the adjustments discussed there could lead to dataloss. |
|---|---|

#### 75.4.2. Configuring the MOB Cache

Because there can be a large number of MOB files at any time, as compared to the number of HFiles, MOB files are not always kept open. The MOB file reader cache is a LRU cache which keeps the most recently used MOB files open. To configure the MOB file reader’s cache on each RegionServer, add the following properties to the RegionServer’s `hbase-site.xml`, customize the configuration to suit your environment, and restart or rolling restart the RegionServer.

Example 26. Example MOB Cache Configuration

```
<property>
    <name>hbase.mob.file.cache.size</name>
    <value>1000</value>
    <description>
      Number of opened file handlers to cache.
      A larger value will benefit reads by providing more file handlers per mob
      file cache and would reduce frequent file opening and closing.
      However, if this is set too high, this could lead to a "too many opened file handers"
      The default value is 1000.
    </description>
</property>
<property>
    <name>hbase.mob.cache.evict.period</name>
    <value>3600</value>
    <description>
      The amount of time in seconds after which an unused file is evicted from the
      MOB cache. The default value is 3600 seconds.
    </description>
</property>
<property>
    <name>hbase.mob.cache.evict.remain.ratio</name>
    <value>0.5f</value>
    <description>
      A multiplier (between 0.0 and 1.0), which determines how many files remain cached
      after the threshold of files that remains cached after a cache eviction occurs
      which is triggered by reaching the `hbase.mob.file.cache.size` threshold.
      The default value is 0.5f, which means that half the files (the least-recently-used
      ones) are evicted.
    </description>
</property>
```

#### 75.4.3. Manually Compacting MOB Files

To manually compact MOB files, rather than waiting for the periodic chore to trigger compaction, use the `major_compact` HBase shell commands. These commands require the first argument to be the table name, and take a column family as the second argument. If used with a column family that includes MOB data, then these operator requests will result in the MOB data being compacted.

```
hbase> major_compact 't1'
hbase> major_compact 't2', 'c1’
```

This same request can be made via the `Admin.majorCompact` Java API.

### 75.5. MOB Troubleshooting

#### 75.5.1. Adjusting the MOB cleaner’s tolerance for new hfiles

The MOB cleaner chore ignores all MOB hfiles that were created more recently than an hour prior to the start of the chore to ensure we don’t miss the reference metadata from the corresponding regular hfile. Without this safety check it would be possible for the cleaner chore to see a MOB hfile for an in progress flush or compaction and prematurely archive the MOB data. This default buffer should be sufficient for normal use.

You will need to adjust the tolerance if you use write amplification optimized MOB compaction and the combination of your underlying filesystem performance and data shape is such that it could take more than an hour to complete major compaction of a single region. For example, if your MOB data is distributed such that your largest region adds 80GB of MOB data between compactions that include rewriting MOB data and your HDFS cluster is only capable of writing 20MB/s for a single file then when performing the optimized compaction the Region Server will take about a minute to write the first 1GB MOB hfile and then another hour and seven minutes to write the remaining seventy-nine 1GB MOB hfiles before finally committing the new reference hfile at the end of the compaction. Given this example, you would need a larger tolerance window.

You will also need to adjust the tolerance if Region Server flush operations take longer than an hour for the two HDFS move operations needed to commit both the MOB hfile and the normal hfile that references it. Such a delay should not happen with a normally configured and healthy HDFS and HBase.

The cleaner’s window for "too recent" is controlled by setting `hbase.mob.min.age.archive` to a positive integer number of milliseconds.

```
<property>
    <name>hbase.mob.min.age.archive</name>
    <value>86400000</value>
    <description>Example of tuning the cleaner to only archive files older than a day.</dscription>
</property>
```

While working on troubleshooting failures in the MOB system you can retrieve some of the internal information through the HBase shell by specifying special attributes on a scan.

```
hbase(main):112:0> scan 'some_table', {STARTROW => '00012-example-row-key', LIMIT => 1,
hbase(main):113:1*     CACHE_BLOCKS => false, ATTRIBUTES => { 'hbase.mob.scan.raw' => '1',
hbase(main):114:2*     'hbase.mob.scan.ref.only' => '1' } }
```

The MOB internal information is stored as four bytes for the size of the underlying cell value and then a UTF8 string with the name of the MOB HFile that contains the underlying cell value. Note that by default the entirety of this serialized structure will be passed through the HBase shell’s binary string converter. That means the bytes that make up the value size will most likely be written as escaped non-printable byte values, e.g. '\x03', unless they happen to correspond to ASCII characters.

Let’s look at a specific example:

```
hbase(main):112:0> scan 'some_table', {STARTROW => '00012-example-row-key', LIMIT => 1,
hbase(main):113:1*     CACHE_BLOCKS => false, ATTRIBUTES => { 'hbase.mob.scan.raw' => '1',
hbase(main):114:2*     'hbase.mob.scan.ref.only' => '1' } }
ROW                        COLUMN+CELL
 00012-example-row-key     column=foo:bar, timestamp=1511179764, value=\x00\x02|\x94d41d8cd98f00b204
                           e9800998ecf8427e19700118ffd9c244fe69488bbc9f2c77d24a3e6a
1 row(s) in 0.0130 seconds
```

In this case the first four bytes are `\x00\x02|\x94` which corresponds to the bytes `[0x00, 0x02, 0x7C, 0x94]`. (Note that the third byte was printed as the ASCII character '|'.) Decoded as an integer this gives us an underlying value size of 162,964 bytes.

The remaining bytes give us an HFile name, 'd41d8cd98f00b204e9800998ecf8427e19700118ffd9c244fe69488bbc9f2c77d24a3e6a'. This HFile will most likely be stored in the designated MOB storage area for this specific table. However, the file could also be in the archive area if this table is from a restored snapshot. Furthermore, if the table is from a cloned snapshot of a different table then the file could be in either the active or archive area of that source table. As mentioned in the explanation of MOB reference cells above, the Region Server will use a server side tag to optimize looking at the mob and archive area of the correct original table when finding the MOB HFile. Since your scan is client side it can’t retrieve that tag and you’ll either need to already know the lineage of your table or you’ll need to search across all tables.

Assuming you are authenticated as a user with HBase superuser rights, you can search for it:

```
$> hdfs dfs -find /hbase -name \
    d41d8cd98f00b204e9800998ecf8427e19700118ffd9c244fe69488bbc9f2c77d24a3e6a
/hbase/mobdir/data/default/some_table/372c1b27e3dc0b56c3a031926e5efbe9/foo/d41d8cd98f00b204e9800998ecf8427e19700118ffd9c244fe69488bbc9f2c77d24a3e6a
```

#### 75.5.3. Moving a column family out of MOB

If you want to disable MOB on a column family you must ensure you instruct HBase to migrate the data out of the MOB system prior to turning the feature off. If you fail to do this HBase will return the internal MOB metadata to applications because it will not know that it needs to resolve the actual values.

The following procedure will safely migrate the underlying data without requiring a cluster outage. Clients will see a number of retries when configuration settings are applied and regions are reloaded.

Procedure: Stop MOB maintenance, change MOB threshold, rewrite data via compaction

1. Ensure the MOB compaction chore in the Master is off by setting `hbase.mob.compaction.chore.period` to `0`. Applying this configuration change will require a rolling restart of HBase Masters. That will require at least one fail-over of the active master, which may cause retries for clients doing HBase administrative operations.
2. Ensure no MOB compactions are issued for the table via the HBase shell for the duration of this migration.
3. Use the HBase shell to change the MOB size threshold for the column family you are migrating to a value that is larger than the largest cell present in the column family. E.g. given a table named 'some_table' and a column family named 'foo' we can pick one gigabyte as an arbitrary "bigger than what we store" value: `hbase(main):011:0> alter 'some_table', {NAME => 'foo', MOB_THRESHOLD => '1000000000'} Updating all regions with the new schema... 9/25 regions updated. 25/25 regions updated. Done. 0 row(s) in 3.4940 seconds` Note that if you are still ingesting data you must ensure this threshold is larger than any cell value you might write; MAX_INT would be a safe choice.
4. Perform a major compaction on the table. Specifically you are performing a "normal" compaction and not a MOB compaction. `hbase(main):012:0> major_compact 'some_table' 0 row(s) in 0.2600 seconds`
5. Monitor for the end of the major compaction. Since compaction is handled asynchronously you’ll need to use the shell to first see the compaction start and then see it end. HBase should first say that a "MAJOR" compaction is happening. `hbase(main):015:0> @hbase.admin(@formatter).instance_eval do hbase(main):016:1* p @admin.get_compaction_state('some_table').to_string hbase(main):017:2* end “MAJOR”` When the compaction has finished the result should print out "NONE". `hbase(main):015:0> @hbase.admin(@formatter).instance_eval do hbase(main):016:1* p @admin.get_compaction_state('some_table').to_string hbase(main):017:2* end “NONE”`
6. Run the *mobrefs* utility to ensure there are no MOB cells. Specifically, the tool will launch a Hadoop MapReduce job that will show a job counter of 0 input records when we’ve successfully rewritten all of the data. `$> HADOOP_CLASSPATH=/etc/hbase/conf:$(hbase mapredcp) yarn jar \ /some/path/to/hbase-shaded-mapreduce.jar mobrefs mobrefs-report-output some_table foo ... 19/12/10 11:38:47 INFO impl.YarnClientImpl: Submitted application application_1575695902338_0004 19/12/10 11:38:47 INFO mapreduce.Job: The url to track the job: https: 19/12/10 11:38:47 INFO mapreduce.Job: Running job: job_1575695902338_0004 19/12/10 11:38:57 INFO mapreduce.Job: Job job_1575695902338_0004 running in uber mode : false 19/12/10 11:38:57 INFO mapreduce.Job: map 0% reduce 0% 19/12/10 11:39:07 INFO mapreduce.Job: map 7% reduce 0% 19/12/10 11:39:17 INFO mapreduce.Job: map 13% reduce 0% 19/12/10 11:39:19 INFO mapreduce.Job: map 33% reduce 0% 19/12/10 11:39:21 INFO mapreduce.Job: map 40% reduce 0% 19/12/10 11:39:22 INFO mapreduce.Job: map 47% reduce 0% 19/12/10 11:39:23 INFO mapreduce.Job: map 60% reduce 0% 19/12/10 11:39:24 INFO mapreduce.Job: map 73% reduce 0% 19/12/10 11:39:27 INFO mapreduce.Job: map 100% reduce 0% 19/12/10 11:39:35 INFO mapreduce.Job: map 100% reduce 100% 19/12/10 11:39:35 INFO mapreduce.Job: Job job_1575695902338_0004 completed successfully 19/12/10 11:39:35 INFO mapreduce.Job: Counters: 54 ... Map-Reduce Framework Map input records=0 ... 19/12/09 22:41:28 INFO mapreduce.MobRefReporter: Finished creating report for 'some_table', family='foo'` If the data has not successfully been migrated out, this report will show both a non-zero number of input records and a count of mob cells. `$> HADOOP_CLASSPATH=/etc/hbase/conf:$(hbase mapredcp) yarn jar \ /some/path/to/hbase-shaded-mapreduce.jar mobrefs mobrefs-report-output some_table foo ... 19/12/10 11:44:18 INFO impl.YarnClientImpl: Submitted application application_1575695902338_0005 19/12/10 11:44:18 INFO mapreduce.Job: The url to track the job: https: 19/12/10 11:44:18 INFO mapreduce.Job: Running job: job_1575695902338_0005 19/12/10 11:44:26 INFO mapreduce.Job: Job job_1575695902338_0005 running in uber mode : false 19/12/10 11:44:26 INFO mapreduce.Job: map 0% reduce 0% 19/12/10 11:44:36 INFO mapreduce.Job: map 7% reduce 0% 19/12/10 11:44:45 INFO mapreduce.Job: map 13% reduce 0% 19/12/10 11:44:47 INFO mapreduce.Job: map 27% reduce 0% 19/12/10 11:44:48 INFO mapreduce.Job: map 33% reduce 0% 19/12/10 11:44:50 INFO mapreduce.Job: map 40% reduce 0% 19/12/10 11:44:51 INFO mapreduce.Job: map 53% reduce 0% 19/12/10 11:44:52 INFO mapreduce.Job: map 73% reduce 0% 19/12/10 11:44:54 INFO mapreduce.Job: map 100% reduce 0% 19/12/10 11:44:59 INFO mapreduce.Job: map 100% reduce 100% 19/12/10 11:45:00 INFO mapreduce.Job: Job job_1575695902338_0005 completed successfully 19/12/10 11:45:00 INFO mapreduce.Job: Counters: 54 ... Map-Reduce Framework Map input records=1 ... MOB NUM_CELLS=1 ... 19/12/10 11:45:00 INFO mapreduce.MobRefReporter: Finished creating report for 'some_table', family='foo'` If this happens you should verify that MOB compactions are disabled, verify that you have picked a sufficiently large MOB threshold, and redo the major compaction step.
7. When the *mobrefs* report shows that no more data is stored in the MOB system then you can safely alter the column family configuration so that the MOB feature is disabled. `hbase(main):017:0> alter 'some_table', {NAME => 'foo', IS_MOB => 'false'} Updating all regions with the new schema... 8/25 regions updated. 25/25 regions updated. Done. 0 row(s) in 2.9370 seconds`
8. After the column family no longer shows the MOB feature enabled, it is safe to start MOB maintenance chores again. You can allow the default to be used for `hbase.mob.compaction.chore.period` by removing it from your configuration files or restore it to whatever custom value you had prior to starting this process.
9. Once the MOB feature is disabled for the column family there will be no internal HBase process looking for data in the MOB storage area specific to this column family. There will still be data present there from prior to the compaction process that rewrote the values into HBase’s data area. You can check for this residual data directly in HDFS as an HBase superuser. `$ hdfs dfs -count /hbase/mobdir/data/default/some_table 4 54 9063269081 /hbase/mobdir/data/default/some_table` This data is spurious and may be reclaimed. You should sideline it, verify your application’s view of the table, and then delete it.

#### 75.5.4. Data values over than the MOB threshold show up stored in non-MOB hfiles

Bulk load and WAL split-to-HFile don’t consider MOB threshold and write data into normal hfile (under /hbase/data directory).

|   | This won’t cause any functional problem, during next compaction such data will be written out to the MOB hfiles. |
|---|---|

### 75.6. MOB Upgrade Considerations

Generally, data stored using the MOB feature should transparently continue to work correctly across HBase upgrades.

#### 75.6.1. Upgrading to a version with the "distributed MOB compaction" feature

Prior to the work in HBASE-22749, "Distributed MOB compactions", HBase had the Master coordinate all compaction maintenance of the MOB hfiles. Centralizing management of the MOB data allowed for space optimizations but safely coordinating that management with Region Servers resulted in edge cases that caused data loss (ref HBASE-22075).

Users of the MOB feature upgrading to a version of HBase that includes HBASE-22749 should be aware of the following changes:

- The MOB system no longer allows setting "MOB Compaction Policies"
- The MOB system no longer attempts to group MOB values by the date of the original cell’s timestamp according to said compaction policies, daily or otherwise
- The MOB system no longer needs to track individual cell deletes through the use of special files in the MOB storage area with the suffix `_del`. After upgrading you should sideline these files.
- Under default configuration the MOB system should take much less time to perform a compaction of MOB stored values. This is a direct consequence of the fact that HBase will place a much larger load on the underlying filesystem when doing compactions of MOB stored values; the additional load should be a multiple on the order of magnitude of number of region servers. I.e. for a cluster with three region servers and two masters the default configuration should have HBase put three times the load on HDFS during major compactions that rewrite MOB data when compared to Master handled MOB compaction; it should also be approximately three times as fast.
- When the MOB system detects that a table has hfiles with references to MOB data but the reference hfiles do not yet have the needed file level metadata (i.e. from use of the MOB feature prior to HBASE-22749) then it will refuse to archive *any* MOB hfiles from that table. The normal course of periodic compactions done by Region Servers will update existing hfiles with MOB references, but until a given table has been through the needed compactions operators should expect to see an increased amount of storage used by the MOB feature.
- Performing a compaction with type "MOB" no longer has special handling to compact specifically the MOB hfiles. Instead it will issue a warning and do a compaction of the table. For example using the HBase shell as follows will result in a warning in the Master logs followed by a major compaction of the 'example' table in its entirety or for the 'big' column respectively. `hbase> major_compact 'example', nil, 'MOB' hbase> major_compact 'example', 'big', 'MOB'` The same is true for directly using the Java API for `admin.majorCompact(TableName.valueOf("example"), CompactType.MOB)`.
- Similarly, manually performing a major compaction on a table or region will also handle compacting the MOB stored values for that table or region respectively.

The following configuration setting has been deprecated and replaced:

- `hbase.master.mob.ttl.cleaner.period` has been replaced with `hbase.master.mob.cleaner.period`

The following configuration settings are no longer used:

- `hbase.mob.compaction.mergeable.threshold`
- `hbase.mob.delfile.max.count`
- `hbase.mob.compaction.batch.size`
- `hbase.mob.compactor.class`
- `hbase.mob.compaction.threads.max`


## 76. Scan over snapshot

In HBase, a scan of a table costs server-side HBase resources reading, formating, and returning data back to the client. Luckily, HBase provides a TableSnapshotScanner and TableSnapshotInputFormat (introduced by HBASE-8369), which can scan HBase-written HFiles directly in the HDFS filesystem completely by-passing hbase. This access mode performs better than going via HBase and can be used with an offline HBase with in-place or exported snapshot HFiles.

To read HFiles directly, the user must have sufficient permissions to access snapshots or in-place hbase HFiles.

### 76.1. TableSnapshotScanner

TableSnapshotScanner provides a means for running a single client-side scan over snapshot files. When using TableSnapshotScanner, we must specify a temporary directory to copy the snapshot files into. The client user should have write permissions to this directory, and the dir should not be a subdirectory of the hbase.rootdir. The scanner deletes the contents of the directory once the scanner is closed.

Example 27. Use TableSnapshotScanner

```
Path restoreDir = new Path("XX"); 
Scan scan = new Scan();
try (TableSnapshotScanner scanner = new TableSnapshotScanner(conf, restoreDir, snapshotName, scan)) {
    Result result = scanner.next();
    while (result != null) {
        ...
        result = scanner.next();
    }
}
```

### 76.2. TableSnapshotInputFormat

TableSnapshotInputFormat provides a way to scan over snapshot HFiles in a MapReduce job.

Example 28. Use TableSnapshotInputFormat

```
Job job = new Job(conf);
Path restoreDir = new Path("XX"); 
Scan scan = new Scan();
TableMapReduceUtil.initTableSnapshotMapperJob(snapshotName, scan, MyTableMapper.class, MyMapKeyOutput.class, MyMapOutputValueWritable.class, job, true, restoreDir);
```

### 76.3. Permission to access snapshot and data files

Generally, only the HBase owner or the HDFS admin have the permission to access HFiles.

HBASE-18659 uses HDFS ACLs to make HBase granted user have permission to access snapshot files.

#### 76.3.1. HDFS ACLs

HDFS ACLs supports an "access ACL", which defines the rules to enforce during permission checks, and a "default ACL", which defines the ACL entries that new child files or sub-directories receive automatically during creation. Via HDFS ACLs, HBase syncs granted users with read permission to HFiles.

#### 76.3.2. Basic idea

The HBase files are organized in the following ways:

- {hbase-rootdir}/.tmp/data/{namespace}/{table}
- {hbase-rootdir}/data/{namespace}/{table}
- {hbase-rootdir}/archive/data/{namespace}/{table}
- {hbase-rootdir}/.hbase-snapshot/{snapshotName}

So the basic idea is to add or remove HDFS ACLs to files of the global/namespace/table directory when grant or revoke permission to global/namespace/table.

See the design doc in HBASE-18659 for more details.

#### 76.3.3. Configuration to use this feature

- Firstly, make sure that HDFS ACLs are enabled and umask is set to 027

```
dfs.namenode.acls.enabled = true
fs.permissions.umask-mode = 027
```

- Add master coprocessor, please make sure the SnapshotScannerHDFSAclController is configured after AccessController

```
hbase.coprocessor.master.classes = "org.apache.hadoop.hbase.security.access.AccessController
,org.apache.hadoop.hbase.security.access.SnapshotScannerHDFSAclController"
```

- Enable this feature

```
hbase.acl.sync.to.hdfs.enable=true
```

- Modify table scheme to enable this feature for a specified table, this config is false by default for every table, this means the HBase granted ACLs will not be synced to HDFS

```
alter 't1', CONFIGURATION => {'hbase.acl.sync.to.hdfs.enable' => 'true'}
```

#### 76.3.4. Limitation

There are some limitations for this feature:

If we enable this feature, some master operations such as grant, revoke, snapshot… (See the design doc for more details) will be slower as we need to sync HDFS ACLs to related hfiles.

HDFS has a config which limits the max ACL entries num for one directory or file:

```
dfs.namenode.acls.max.entries = 32(default value)
```

The 32 entries include four fixed users for each directory or file: owner, group, other, and mask. For a directory, the four users contain 8 ACL entries(access and default) and for a file, the four users contain 4 ACL entries(access). This means there are 24 ACL entries left for named users or groups.

Based on this limitation, we can only sync up to 12 HBase granted users' ACLs. This means, if a table enables this feature, then the total users with table, namespace of this table, global READ permission should not be greater than 12.

There are some cases that this coprocessor has not handled or could not handle, so the user HDFS ACLs are not synced normally. It will not make a reference link to another hfile of other tables.

# In-memory Compaction


## 77. Overview

In-memory Compaction (A.K.A Accordion) is a new feature in hbase-2.0.0. It was first introduced on the Apache HBase Blog at Accordion: HBase Breathes with In-Memory Compaction. Quoting the blog:

> Accordion reapplies the LSM principal [*Log-Structured-Merge Tree*, the design pattern upon which HBase is based] to MemStore, in order to eliminate redundancies and other overhead while the data is still in RAM. Doing so decreases the frequency of flushes to HDFS, thereby reducing the write amplification and the overall disk footprint. With less flushes, the write operations are stalled less frequently as the MemStore overflows, therefore the write performance is improved. Less data on disk also implies less pressure on the block cache, higher hit rates, and eventually better read response times. Finally, having less disk writes also means having less compaction happening in the background, i.e., less cycles are stolen from productive (read and write) work. All in all, the effect of in-memory compaction can be envisioned as a catalyst that enables the system move faster as a whole.

A developer view is available at Accordion: Developer View of In-Memory Compaction.

In-memory compaction works best when high data churn; overwrites or over-versions can be eliminated while the data is still in memory. If the writes are all uniques, it may drag write throughput (In-memory compaction costs CPU). We suggest you test and compare before deploying to production.

In this section we describe how to enable Accordion and the available configurations.


## 78. Enabling

To enable in-memory compactions, set the *IN_MEMORY_COMPACTION* attribute on per column family where you want the behavior. The *IN_MEMORY_COMPACTION* attribute can have one of four values.

- *NONE*: No in-memory compaction.
- *BASIC*: Basic policy enables flushing and keeps a pipeline of flushes until we trip the pipeline maximum threshold and then we flush to disk. No in-memory compaction but can help throughput as data is moved from the profligate, native ConcurrentSkipListMap data-type to more compact (and efficient) data types.
- *EAGER*: This is *BASIC* policy plus in-memory compaction of flushes (much like the on-disk compactions done to hfiles); on compaction we apply on-disk rules eliminating versions, duplicates, ttl’d cells, etc.
- *ADAPTIVE*: Adaptive compaction adapts to the workload. It applies either index compaction or data compaction based on the ratio of duplicate cells in the data. Experimental.

To enable *BASIC* on the *info* column family in the table *radish*, add the attribute to the *info* column family:

```
hbase(main):003:0> alter 'radish', {NAME => 'info', IN_MEMORY_COMPACTION => 'BASIC'}
Updating all regions with the new schema...
All regions updated.
Done.
Took 1.2413 seconds
hbase(main):004:0> describe 'radish'
Table radish is DISABLED
radish
COLUMN FAMILIES DESCRIPTION
{NAME => 'info', VERSIONS => '1', EVICT_BLOCKS_ON_CLOSE => 'false', NEW_VERSION_BEHAVIOR => 'false', KEEP_DELETED_CELLS => 'FALSE', CACHE_DATA_ON_WRITE => 'false', DATA_BLOCK_ENCODING => 'NONE', TTL => 'FOREVER', MIN_VERSIONS => '0', REPLICATION_SCOPE => '0', BLOOMFILTER => 'ROW', CACHE_INDEX_ON_WRITE => 'false', IN_MEMORY => 'false', CACHE_BLOOMS_ON_WRITE => 'false', PREFETCH_BLOCKS_ON_OPEN => 'false', COMPRESSION => 'NONE', BLOCKCACHE => 'true', BLOCKSIZE => '65536', METADATA => {
'IN_MEMORY_COMPACTION' => 'BASIC'}}
1 row(s)
Took 0.0239 seconds
```

Note how the IN_MEMORY_COMPACTION attribute shows as part of the *METADATA* map.

There is also a global configuration, *hbase.hregion.compacting.memstore.type* which you can set in your *hbase-site.xml* file. Use it to set the default on creation of a new table (On creation of a column family Store, we look first to the column family configuration looking for the *IN_MEMORY_COMPACTION* setting, and if none, we then consult the *hbase.hregion.compacting.memstore.type* value using its content; default is *NONE*).

By default, new hbase system tables will have *NONE* in-memory compaction set. To specify otherwise, on new table-creation, set *hbase.systemtables.compacting.memstore.type* to *BASIC* / *EAGER* / *ADAPTIVE* (Note, setting this value post-creation of system tables will not have a retroactive effect; you will have to alter your tables to set the in-memory attribute).

When an in-memory flush happens is calculated by dividing the configured region flush size (Set in the table descriptor or read from *hbase.hregion.memstore.flush.size*) by the number of column families and then multiplying by *hbase.memstore.inmemoryflush.threshold.factor*. Default is 0.014.

The number of flushes carried by the pipeline is monitored so as to fit within the bounds of memstore sizing but you can also set a maximum on the number of flushes total by setting *hbase.hregion.compacting.pipeline.segments.limit*. Default is 2.

When a column family Store is created, it says what memstore type is in effect. As of this writing there is the old-school *DefaultMemStore* which fills a *ConcurrentSkipListMap* and then flushes to disk or the new *CompactingMemStore* that is the implementation that provides this new in-memory compactions facility. Here is a log-line from a RegionServer that shows a column family Store named *family* configured to use a *CompactingMemStore*:

```
Note how the IN_MEMORY_COMPACTION attribute shows as part of the _METADATA_ map.
2018-03-30 11:02:24,466 INFO  [Time-limited test] regionserver.HStore(325): Store=family,  memstore type=CompactingMemStore, storagePolicy=HOT, verifyBulkLoads=false, parallelPutCountPrintThreshold=10
```

Enable TRACE-level logging on the CompactingMemStore class (*org.apache.hadoop.hbase.regionserver.CompactingMemStore*) to see detail on its operation.

# RegionServer Offheap Read/Write Path


## 79. Overview

To help reduce P99/P999 RPC latencies, HBase 2.x has made the read and write path use a pool of offheap buffers. Cells are allocated in offheap memory outside of the purview of the JVM garbage collector with attendent reduction in GC pressure. In the write path, the request packet received from client will be read in on a pre-allocated offheap buffer and retained offheap until those cells are successfully persisted to the WAL and Memstore. The memory data structure in Memstore does not directly store the cell memory, but references the cells encoded in the offheap buffers. Similarly for the read path. We’ll try to read the block cache first and if a cache misses, we’ll go to the HFile and read the respective block. The workflow from reading blocks to sending cells to client does its best to avoid on-heap memory allocations reducing the amount of work the GC has to do.

For redress for the single mention of onheap in the read-section of the diagram above see Read block from HDFS to offheap directly.
