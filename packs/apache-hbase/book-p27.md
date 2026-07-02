---
title: "Apache HBase® Reference Guide (part 27/41)"
source: https://hbase.apache.org/book.html
domain: apache-hbase
license: CC-BY-SA-4.0
tags: apache hbase, bigtable clone, wide-column store, apache hadoop
fetched: 2026-07-02
part: 27/41
---

## 159. HBase Tools and Utilities

HBase provides several tools for administration, analysis, and debugging of your cluster. The entry-point to most of these tools is the *bin/hbase* command, though some tools are available in the *dev-support/* directory.

To see usage instructions for *bin/hbase* command, run it with no arguments, or with the `-h` argument. These are the usage instructions for HBase 0.98.x. Some commands, such as `version`, `pe`, `ltt`, `clean`, are not available in previous versions.

```
$ bin/hbase
Usage: hbase [<options>] <command> [<args>]
Options:
  --config DIR     Configuration direction to use. Default: ./conf
  --hosts HOSTS    Override the list in 'regionservers' file
  --auth-as-server Authenticate to ZooKeeper using servers configuration

Commands:
Some commands take arguments. Pass no args or -h for usage.
  shell           Run the HBase shell
  hbck            Run the HBase 'fsck' tool. Defaults read-only hbck1.
                  Pass '-j /path/to/HBCK2.jar' to run hbase-2.x HBCK2.
  snapshot        Tool for managing snapshots
  wal             Write-ahead-log analyzer
  hfile           Store file analyzer
  zkcli           Run the ZooKeeper shell
  master          Run an HBase HMaster node
  regionserver    Run an HBase HRegionServer node
  zookeeper       Run a ZooKeeper server
  rest            Run an HBase REST server
  thrift          Run the HBase Thrift server
  thrift2         Run the HBase Thrift2 server
  clean           Run the HBase clean up script
  jshell          Run a jshell with HBase on the classpath
  classpath       Dump hbase CLASSPATH
  mapredcp        Dump CLASSPATH entries required by mapreduce
  pe              Run PerformanceEvaluation
  ltt             Run LoadTestTool
  canary          Run the Canary tool
  version         Print the version
  backup          Backup tables for recovery
  restore         Restore tables from existing backup image
  regionsplitter  Run RegionSplitter tool
  rowcounter      Run RowCounter tool
  cellcounter     Run CellCounter tool
  CLASSNAME       Run the class named CLASSNAME
```

Some of the tools and utilities below are Java classes which are passed directly to the *bin/hbase* command, as referred to in the last line of the usage instructions. Others, such as `hbase shell` (The Apache HBase Shell), `hbase upgrade` (Upgrading), and `hbase thrift` (Thrift API and Filter Language), are documented elsewhere in this guide.

### 159.1. Canary

The Canary tool can help users "canary-test" the HBase cluster status. The default "region mode" fetches a row from every column-family of every regions. In "regionserver mode", the Canary tool will fetch a row from a random region on each of the cluster’s RegionServers. In "zookeeper mode", the Canary will read the root znode on each member of the zookeeper ensemble.

To see usage, pass the `-help` parameter (if you pass no parameters, the Canary tool starts executing in the default region "mode" fetching a row from every region in the cluster).

```
2018-10-16 13:11:27,037 INFO  [main] tool.Canary: Execution thread count=16
Usage: canary [OPTIONS] [<TABLE1> [<TABLE2]...] | [<REGIONSERVER1> [<REGIONSERVER2]..]
Where [OPTIONS] are:
 -h,-help        show this help and exit.
 -regionserver   set 'regionserver mode'; gets row from random region on server
 -allRegions     get from ALL regions when 'regionserver mode', not just random one.
 -zookeeper      set 'zookeeper mode'; grab zookeeper.znode.parent on each ensemble member
 -daemon         continuous check at defined intervals.
 -interval <N>   interval between checks in seconds
 -e              consider table/regionserver argument as regular expression
 -f <B>          exit on first error; default=true
 -failureAsError treat read/write failure as error
 -t <N>          timeout for canary-test run; default=600000ms
 -writeSniffing  enable write sniffing
 -writeTable     the table used for write sniffing; default=hbase:canary
 -writeTableTimeout <N>  timeout for writeTable; default=600000ms
 -readTableTimeouts <tableName>=<read timeout>,<tableName>=<read timeout>,...
                comma-separated list of table read timeouts (no spaces);
                logs 'ERROR' if takes longer. default=600000ms
 -permittedZookeeperFailures <N>  Ignore first N failures attempting to
                connect to individual zookeeper nodes in ensemble

 -D<configProperty>=<value> to assign or override configuration params
 -Dhbase.canary.read.raw.enabled=<true/false> Set to enable/disable raw scan; default=false

Canary runs in one of three modes: region (default), regionserver, or zookeeper.
To sniff/probe all regions, pass no arguments.
To sniff/probe all regions of a table, pass tablename.
To sniff/probe regionservers, pass -regionserver, etc.
See http:
```

|   | The `Sink` class is instantiated using the `hbase.canary.sink.class` configuration property. |
|---|---|

This tool will return non zero error codes to user for collaborating with other monitoring tools, such as Nagios. The error code definitions are:

```
private static final int USAGE_EXIT_CODE = 1;
private static final int INIT_ERROR_EXIT_CODE = 2;
private static final int TIMEOUT_ERROR_EXIT_CODE = 3;
private static final int ERROR_EXIT_CODE = 4;
private static final int FAILURE_EXIT_CODE = 5;
```

Here are some examples based on the following given case: given two Table objects called test-01 and test-02 each with two column family cf1 and cf2 respectively, deployed on 3 RegionServers. See the following table.

| RegionServer | test-01 | test-02 |
|---|---|---|
| rs1 | r1 | r2 |
| rs2 | r2 |   |
| rs3 | r2 | r1 |

Following are some example outputs based on the previous given case.

#### 159.1.1. Canary test for every column family (store) of every region of every table

```
$ ${HBASE_HOME}/bin/hbase canary

3/12/09 03:26:32 INFO tool.Canary: read from region test-01,,1386230156732.0e3c7d77ffb6361ea1b996ac1042ca9a. column family cf1 in 2ms
13/12/09 03:26:32 INFO tool.Canary: read from region test-01,,1386230156732.0e3c7d77ffb6361ea1b996ac1042ca9a. column family cf2 in 2ms
13/12/09 03:26:32 INFO tool.Canary: read from region test-01,0004883,1386230156732.87b55e03dfeade00f441125159f8ca87. column family cf1 in 4ms
13/12/09 03:26:32 INFO tool.Canary: read from region test-01,0004883,1386230156732.87b55e03dfeade00f441125159f8ca87. column family cf2 in 1ms
...
13/12/09 03:26:32 INFO tool.Canary: read from region test-02,,1386559511167.aa2951a86289281beee480f107bb36ee. column family cf1 in 5ms
13/12/09 03:26:32 INFO tool.Canary: read from region test-02,,1386559511167.aa2951a86289281beee480f107bb36ee. column family cf2 in 3ms
13/12/09 03:26:32 INFO tool.Canary: read from region test-02,0004883,1386559511167.cbda32d5e2e276520712d84eaaa29d84. column family cf1 in 31ms
13/12/09 03:26:32 INFO tool.Canary: read from region test-02,0004883,1386559511167.cbda32d5e2e276520712d84eaaa29d84. column family cf2 in 8ms
```

So you can see, table test-01 has two regions and two column families, so the Canary tool in the default "region mode" will pick 4 small piece of data from 4 (2 region * 2 store) different stores. This is a default behavior.

#### 159.1.2. Canary test for every column family (store) of every region of a specific table(s)

You can also test one or more specific tables by passing table names.

```
$ ${HBASE_HOME}/bin/hbase canary test-01 test-02
```

#### 159.1.3. Canary test with RegionServer granularity

In "regionserver mode", the Canary tool will pick one small piece of data from each RegionServer (You can also pass one or more RegionServer names as arguments to the canary-test when in "regionserver mode").

```
$ ${HBASE_HOME}/bin/hbase canary -regionserver

13/12/09 06:05:17 INFO tool.Canary: Read from table:test-01 on region server:rs2 in 72ms
13/12/09 06:05:17 INFO tool.Canary: Read from table:test-02 on region server:rs3 in 34ms
13/12/09 06:05:17 INFO tool.Canary: Read from table:test-01 on region server:rs1 in 56ms
```

#### 159.1.4. Canary test with regular expression pattern

You can pass regexes for table names when in "region mode" or for servernames when in "regionserver mode". The below will test both table test-01 and test-02.

```
$ ${HBASE_HOME}/bin/hbase canary -e test-0[1-2]
```

#### 159.1.5. Run canary test as a "daemon"

Run repeatedly with an interval defined via the option `-interval` (default value is 60 seconds). This daemon will stop itself and return non-zero error code if any error occur. To have the daemon keep running across errors, pass the -f flag with its value set to false (see usage above).

```
$ ${HBASE_HOME}/bin/hbase canary -daemon
```

To run repeatedly with 5 second intervals and not stop on errors, do the following.

```
$ ${HBASE_HOME}/bin/hbase canary -daemon -interval 5 -f false
```

#### 159.1.6. Force timeout if canary test stuck

In some cases the request is stuck and no response is sent back to the client. This can happen with dead RegionServers which the master has not yet noticed. Because of this we provide a timeout option to kill the canary test and return a non-zero error code. The below sets the timeout value to 60 seconds (the default value is 600 seconds).

```
$ ${HBASE_HOME}/bin/hbase canary -t 60000
```

#### 159.1.7. Enable write sniffing in canary

By default, the canary tool only checks read operations. To enable the write sniffing, you can run the canary with the `-writeSniffing` option set. When write sniffing is enabled, the canary tool will create an hbase table and make sure the regions of the table are distributed to all region servers. In each sniffing period, the canary will try to put data to these regions to check the write availability of each region server.

```
$ ${HBASE_HOME}/bin/hbase canary -writeSniffing
```

The default write table is `hbase:canary` and can be specified with the option `-writeTable`.

```
$ ${HBASE_HOME}/bin/hbase canary -writeSniffing -writeTable ns:canary
```

The default value size of each put is 10 bytes. You can set it via the config key: `hbase.canary.write.value.size`.

#### 159.1.8. Treat read / write failure as error

By default, the canary tool only logs read failures — due to e.g. RetriesExhaustedException, etc. — and will return the 'normal' exit code. To treat read/write failure as errors, you can run canary with the `-treatFailureAsError` option. When enabled, read/write failures will result in an error exit code.

```
$ ${HBASE_HOME}/bin/hbase canary -treatFailureAsError
```

#### 159.1.9. Running Canary in a Kerberos-enabled Cluster

To run the Canary in a Kerberos-enabled cluster, configure the following two properties in *hbase-site.xml*:

- `hbase.client.keytab.file`
- `hbase.client.kerberos.principal`

Kerberos credentials are refreshed every 30 seconds when Canary runs in daemon mode.

To configure the DNS interface for the client, configure the following optional properties in *hbase-site.xml*.

- `hbase.client.dns.interface`
- `hbase.client.dns.nameserver`

Example 44. Canary in a Kerberos-Enabled Cluster

This example shows each of the properties with valid values.

```
<property>
  <name>hbase.client.kerberos.principal</name>
  <value>hbase/_HOST@YOUR-REALM.COM</value>
</property>
<property>
  <name>hbase.client.keytab.file</name>
  <value>/etc/hbase/conf/keytab.krb5</value>
</property>

<property>
  <name>hbase.client.dns.interface</name>
  <value>default</value>
</property>
<property>
  <name>hbase.client.dns.nameserver</name>
  <value>default</value>
</property>
```

### 159.2. RegionSplitter

```
usage: bin/hbase regionsplitter <TABLE> <SPLITALGORITHM>
SPLITALGORITHM is the java class name of a class implementing
                      SplitAlgorithm, or one of the special strings
                      HexStringSplit or DecimalStringSplit or
                      UniformSplit, which are built-in split algorithms.
                      HexStringSplit treats keys as hexadecimal ASCII, and
                      DecimalStringSplit treats keys as decimal ASCII, and
                      UniformSplit treats keys as arbitrary bytes.
 -c <region count>        Create a new table with a pre-split number of
                          regions
 -D <property=value>      Override HBase Configuration Settings
 -f <family:family:...>   Column Families to create with new table.
                          Required with -c
    --firstrow <arg>      First Row in Table for Split Algorithm
 -h                       Print this usage help
    --lastrow <arg>       Last Row in Table for Split Algorithm
 -o <count>               Max outstanding splits that have unfinished
                          major compactions
 -r                       Perform a rolling split of an existing region
    --risky               Skip verification steps to complete
                          quickly. STRONGLY DISCOURAGED for production
                          systems.
```

For additional detail, see Manual Region Splitting.

### 159.3. Health Checker

You can configure HBase to run a script periodically and if it fails N times (configurable), have the server exit. See *HBASE-7351 Periodic health check script* for configurations and detail.

### 159.4. Driver

Several frequently-accessed utilities are provided as `Driver` classes, and executed by the *bin/hbase* command. These utilities represent MapReduce jobs which run on your cluster. They are run in the following way, replacing *UtilityName* with the utility you want to run. This command assumes you have set the environment variable `HBASE_HOME` to the directory where HBase is unpacked on your server.

```
${HBASE_HOME}/bin/hbase org.apache.hadoop.hbase.mapreduce.UtilityName
```

The following utilities are available:

**`LoadIncrementalHFiles`**

Complete a bulk data load.

**`CopyTable`**

Export a table from the local cluster to a peer cluster.

**`Export`**

Write table data to HDFS.

**`Import`**

Import data written by a previous `Export` operation.

**`ImportTsv`**

Import data in TSV format.

**`RowCounter`**

Count rows in an HBase table.

**`CellCounter`**

Count cells in an HBase table.

**`replication.VerifyReplication`**

Compare the data from tables in two different clusters. WARNING: It doesn’t work for incrementColumnValues’d cells since the timestamp is changed. Note that this command is in a different package than the others.

Each command except `RowCounter` and `CellCounter` accept a single `--help` argument to print usage instructions.

### 159.5. HBase `hbck`

The `hbck` tool that shipped with hbase-1.x has been made read-only in hbase-2.x. It is not able to repair hbase-2.x clusters as hbase internals have changed. Nor should its assessments in read-only mode be trusted as it does not understand hbase-2.x operation.

A new tool, HBase `HBCK2`, described in the next section, replaces `hbck`.

### 159.6. HBase `HBCK2`

`HBCK2` is the successor to HBase `hbck`, the hbase-1.x fix tool (A.K.A `hbck1`). Use it in place of `hbck1` making repairs against hbase-2.x installs.

`HBCK2` does not ship as part of hbase. It can be found as a subproject of the companion hbase-operator-tools repository at Apache HBase HBCK2 Tool. `HBCK2` was moved out of hbase so it could evolve at a cadence apart from that of hbase core.

See the [https://github.com/apache/hbase-operator-tools/tree/master/hbase-hbck2](HBCK2) Home Page for how `HBCK2` differs from `hbck1`, and for how to build and use it.

Once built, you can run `HBCK2` as follows:

```
$ hbase hbck -j /path/to/HBCK2.jar
```

This will generate `HBCK2` usage describing commands and options.

### 159.7. HFile Tool

See HFile Tool.

### 159.8. WAL Tools

For bulk replaying WAL files or *recovered.edits* files, see WALPlayer. For reading/verifying individual files, read on.

#### 159.8.1. WALPrettyPrinter

The `WALPrettyPrinter` is a tool with configurable options to print the contents of a WAL or a *recovered.edits* file. You can invoke it via the HBase cli with the 'wal' command.

```
 $ ./bin/hbase wal hdfs:
```

|   | WAL Printing in older versions of HBase Prior to version 2.0, the `WALPrettyPrinter` was called the `HLogPrettyPrinter`, after an internal name for HBase’s write ahead log. In those versions, you can print the contents of a WAL using the same configuration as above, but with the 'hlog' command. `$ ./bin/hbase hlog hdfs:` |
|---|---|

### 159.9. Compression Tool

See compression.test.

### 159.10. CopyTable

CopyTable is a utility that can copy part or of all of a table, either to the same cluster or another cluster. The target table must first exist. The usage is as follows:

```
$ ./bin/hbase org.apache.hadoop.hbase.mapreduce.CopyTable --help
/bin/hbase org.apache.hadoop.hbase.mapreduce.CopyTable --help
Usage: CopyTable [general options] [--starttime=X] [--endtime=Y] [--new.name=NEW] [--peer.adr=ADR] <tablename>

Options:
 rs.class     hbase.regionserver.class of the peer cluster,
              specify if different from current cluster
 rs.impl      hbase.regionserver.impl of the peer cluster,
 startrow     the start row
 stoprow      the stop row
 starttime    beginning of the time range (unixtime in millis)
              without endtime means from starttime to forever
 endtime      end of the time range.  Ignored if no starttime specified.
 versions     number of cell versions to copy
 new.name     new table's name
 peer.uri     The URI of the peer cluster
 peer.adr     Address of the peer cluster given in the format
              hbase.zookeeer.quorum:hbase.zookeeper.client.port:zookeeper.znode.parent
              Do not take effect if peer.uri is specified
              Deprecated, please use peer.uri instead
 families     comma-separated list of families to copy
              To copy from cf1 to cf2, give sourceCfName:destCfName.
              To keep the same name, just give "cfName"
 all.cells    also copy delete markers and deleted cells

Args:
 tablename    Name of the table to copy

Examples:
 To copy 'TestTable' to a cluster that uses replication for a 1 hour window:
 $ bin/hbase org.apache.hadoop.hbase.mapreduce.CopyTable --starttime=1265875194289 --endtime=1265878794289 --peer.adr=server1,server2,server3:2181:/hbase --families=myOldCf:myNewCf,cf2,cf3 TestTable

For performance consider the following general options:
  It is recommended that you set the following to >=100. A higher value uses more memory but
  decreases the round trip time to the server and may increase performance.
    -Dhbase.client.scanner.caching=100
  The following should always be set to false, to prevent writing data twice, which may produce
  inaccurate results.
    -Dmapred.map.tasks.speculative.execution=false
```

Starting from 3.0.0, we introduce a `peer.uri` option so the `peer.adr` option is deprecated. Please use connection URI for specifying HBase clusters. For all previous versions, you should still use the `peer.adr` option.

|   | Scanner Caching Caching for the input Scan is configured via `hbase.client.scanner.caching` in the job configuration. |
|---|---|

|   | Versions By default, CopyTable utility only copies the latest version of row cells unless `--versions=n` is explicitly specified in the command. |
|---|---|

|   | Data Load CopyTable does not perform a diff, it copies all Cells in between the specified startrow/stoprow starttime/endtime range. This means that already existing cells with same values will still be copied. |
|---|---|

See Jonathan Hsieh’s Online HBase Backups with CopyTable blog post for more on `CopyTable`.

### 159.11. HashTable/SyncTable

HashTable/SyncTable is a two steps tool for synchronizing table data, where each of the steps are implemented as MapReduce jobs. Similarly to CopyTable, it can be used for partial or entire table data syncing, under same or remote cluster. However, it performs the sync in a more efficient way than CopyTable. Instead of copying all cells in specified row key/time period range, HashTable (the first step) creates hashed indexes for batch of cells on source table and output those as results. On the next stage, SyncTable scans the source table and now calculates hash indexes for table cells, compares these hashes with the outputs of HashTable, then it just scans (and compares) cells for diverging hashes, only updating mismatching cells. This results in less network traffic/data transfers, which can be impacting when syncing large tables on remote clusters.

#### 159.11.1. Step 1, HashTable

First, run HashTable on the source table cluster (this is the table whose state will be copied to its counterpart).

Usage:

```
$ ./bin/hbase org.apache.hadoop.hbase.mapreduce.HashTable --help
Usage: HashTable [options] <tablename> <outputpath>

Options:
 batchsize         the target amount of bytes to hash in each batch
                   rows are added to the batch until this size is reached
                   (defaults to 8000 bytes)
 numhashfiles      the number of hash files to create
                   if set to fewer than number of regions then
                   the job will create this number of reducers
                   (defaults to 1/100 of regions -- at least 1)
 startrow          the start row
 stoprow           the stop row
 starttime         beginning of the time range (unixtime in millis)
                   without endtime means from starttime to forever
 endtime           end of the time range.  Ignored if no starttime specified.
 scanbatch         scanner batch size to support intra row scans
 versions          number of cell versions to include
 families          comma-separated list of families to include
 ignoreTimestamps  if true, ignores cell timestamps

Args:
 tablename     Name of the table to hash
 outputpath    Filesystem path to put the output data

Examples:
 To hash 'TestTable' in 32kB batches for a 1 hour window into 50 files:
 $ bin/hbase org.apache.hadoop.hbase.mapreduce.HashTable --batchsize=32000 --numhashfiles=50 --starttime=1265875194289 --endtime=1265878794289 --families=cf2,cf3 TestTable /hashes/testTable
```

The **batchsize** property defines how much cell data for a given region will be hashed together in a single hash value. Sizing this properly has a direct impact on the sync efficiency, as it may lead to less scans executed by mapper tasks of SyncTable (the next step in the process). The rule of thumb is that, the smaller the number of cells out of sync (lower probability of finding a diff), larger batch size values can be determined.

#### 159.11.2. Step 2, SyncTable

Once HashTable has completed on source cluster, SyncTable can be ran on target cluster. Just like replication and other synchronization jobs, it requires that all RegionServers/DataNodes on source cluster be accessible by NodeManagers on the target cluster (where SyncTable job tasks will be running).

Usage:

```
$ ./bin/hbase org.apache.hadoop.hbase.mapreduce.SyncTable --help
Usage: SyncTable [options] <sourcehashdir> <sourcetable> <targettable>

Options:
 sourceuri        Cluster connection uri of the source table
                  (defaults to cluster in classpath's config)
 sourcezkcluster  ZK cluster key of the source table
                  (defaults to cluster in classpath's config)
                  Do not take effect if sourceuri is specifie
                  Deprecated, please use sourceuri instead
 targeturi        Cluster connection uri of the target table
                  (defaults to cluster in classpath's config)
 targetzkcluster  ZK cluster key of the target table
                  (defaults to cluster in classpath's config)
                  Do not take effect if targeturi is specified
                  Deprecated, please use targeturi instead
 dryrun           if true, output counters but no writes
                  (defaults to false)
 doDeletes        if false, does not perform deletes
                  (defaults to true)
 doPuts           if false, does not perform puts
                  (defaults to true)
 ignoreTimestamps if true, ignores cells timestamps while comparing
                  cell values. Any missing cell on target then gets
                  added with current time as timestamp
                  (defaults to false)

Args:
 sourcehashdir    path to HashTable output dir for source table
                  (see org.apache.hadoop.hbase.mapreduce.HashTable)
 sourcetable      Name of the source table to sync from
 targettable      Name of the target table to sync to

Examples:
 For a dry run SyncTable of tableA from a remote source cluster
 to a local target cluster:
 $ bin/hbase org.apache.hadoop.hbase.mapreduce.SyncTable --dryrun=true --sourcezkcluster=zk1.example.com,zk2.example.com,zk3.example.com:2181:/hbase hdfs:
```

Starting from 3.0.0, we introduce `sourceuri` and `targeturi` options so `sourcezkcluster` and `targetzkcluster` are deprecated. Please use connection URI for specifying HBase clusters. For all previous versions, you should still use `sourcezkcluster` and `targetzkcluster`.

Cell comparison takes ROW/FAMILY/QUALIFIER/TIMESTAMP/VALUE into account for equality. When syncing at the target, missing cells will be added with original timestamp value from source. That may cause unexpected results after SyncTable completes, for example, if missing cells on target have a delete marker with a timestamp T2 (say, a bulk delete performed by mistake), but source cells timestamps have an older value T1, then those cells would still be unavailable at target because of the newer delete marker timestamp. Since cell timestamps might not be relevant to all use cases, *ignoreTimestamps* option adds the flexibility to avoid using cells timestamp in the comparison. When using *ignoreTimestamps* set to true, this option must be specified for both HashTable and SyncTable steps.

The **dryrun** option is useful when a read only, diff report is wanted, as it will produce only COUNTERS indicating the differences, but will not perform any actual changes. It can be used as an alternative to VerifyReplication tool.

By default, SyncTable will cause target table to become an exact copy of source table (at least, for the specified startrow/stoprow or/and starttime/endtime).

Setting doDeletes to false modifies default behaviour to not delete target cells that are missing on source. Similarly, setting doPuts to false modifies default behaviour to not add missing cells on target. Setting both doDeletes and doPuts to false would give same effect as setting dryrun to true.

|   | Additional info on doDeletes/doPuts "doDeletes/doPuts" were only added by HBASE-20305, so these may not be available on all released versions. For major 1.x versions, minimum minor release including it is **1.4.10**. For major 2.x versions, minimum minor release including it is **2.1.5**. |
|---|---|

|   | Additional info on ignoreTimestamps "ignoreTimestamps" was only added by HBASE-24302, so it may not be available on all released versions. For major 1.x versions, minimum minor release including it is **1.4.14**. For major 2.x versions, minimum minor release including it is **2.2.5**. |
|---|---|

|   | Set doDeletes to false on Two-Way Replication scenarios On Two-Way Replication or other scenarios where both source and target clusters can have data ingested, it’s advisable to always set doDeletes option to false, as any additional cell inserted on SyncTable target cluster and not yet replicated to source would be deleted, and potentially lost permanently. |
|---|---|

|   | Set sourcezkcluster to the actual source cluster ZK quorum Although not required, if sourcezkcluster is not set, SyncTable will connect to local HBase cluster for both source and target, which does not give any meaningful result. |
|---|---|

|   | Remote Clusters on different Kerberos Realms Often, remote clusters may be deployed on different Kerberos Realms. HBASE-20586 added SyncTable support for cross realm authentication, allowing a SyncTable process running on target cluster to connect to source cluster and read both HashTable output files and the given HBase table when performing the required comparisons. |
|---|---|

### 159.12. Export

Export is a utility that will dump the contents of table to HDFS in a sequence file. The Export can be run via a Coprocessor Endpoint or MapReduce. Invoke via:

**mapreduce-based Export**

```
$ bin/hbase org.apache.hadoop.hbase.mapreduce.Export <tablename> <outputdir> [<versions> [<starttime> [<endtime>]]]
```

**endpoint-based Export**

|   | Make sure the Export coprocessor is enabled by adding `org.apache.hadoop.hbase.coprocessor.Export` to `hbase.coprocessor.region.classes`. |
|---|---|

```
$ bin/hbase org.apache.hadoop.hbase.coprocessor.Export <tablename> <outputdir> [<versions> [<starttime> [<endtime>]]]
```

The outputdir is a HDFS directory that does not exist prior to the export. When done, the exported files will be owned by the user invoking the export command.

**The Comparison of Endpoint-based Export And Mapreduce-based Export**

|   | Endpoint-based Export | Mapreduce-based Export |
|---|---|---|
| HBase version requirement | 2.0+ | 0.2.1+ |
| Maven dependency | hbase-endpoint | hbase-mapreduce (2.0+), hbase-server(prior to 2.0) |
| Requirement before dump | mount the endpoint.Export on the target table | deploy the MapReduce framework |
| Read latency | low, directly read the data from region | normal, traditional RPC scan |
| Read Scalability | depend on number of regions | depend on number of mappers (see TableInputFormatBase#getSplits) |
| Timeout | operation timeout. configured by hbase.client.operation.timeout | scan timeout. configured by hbase.client.scanner.timeout.period |
| Permission requirement | READ, EXECUTE | READ |
| Fault tolerance | no | depend on MapReduce |
