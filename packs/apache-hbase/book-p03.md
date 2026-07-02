---
title: "Apache HBase® Reference Guide (part 3/41)"
source: https://hbase.apache.org/book.html
domain: apache-hbase
license: CC-BY-SA-4.0
tags: apache hbase, bigtable clone, wide-column store, apache hadoop
fetched: 2026-07-02
part: 3/41
---

## 7. Default Configuration

### 7.1. *hbase-site.xml* and *hbase-default.xml*

Just as in Hadoop where you add site-specific HDFS configuration to the *hdfs-site.xml* file, for HBase, site specific customizations go into the file *conf/hbase-site.xml*. For the list of configurable properties, see hbase default configurations below or view the raw *hbase-default.xml* source file in the HBase source code at *src/main/resources*.

Not all configuration options make it out to *hbase-default.xml*. Some configurations would only appear in source code; the only way to identify these changes are through code review.

Currently, changes here will require a cluster restart for HBase to notice the change.

### 7.2. HBase Default Configuration

The documentation below is generated using the default hbase configuration file, *hbase-default.xml*, as source.

**`hbase.tmp.dir`**

Description

Temporary directory on the local filesystem. Change this setting to point to a location more permanent than '/tmp', the usual resolve for java.io.tmpdir, as the '/tmp' directory is cleared on machine restart.

Default

`${java.io.tmpdir}/hbase-${user.name}`

**`hbase.rootdir`**

Description

The directory shared by region servers and into which HBase persists. The URL should be 'fully-qualified' to include the filesystem scheme. For example, to specify the HDFS directory '/hbase' where the HDFS instance’s namenode is running at namenode.example.org on port 9000, set this value to: hdfs://namenode.example.org:9000/hbase. By default, we write to whatever ${hbase.tmp.dir} is set too — usually /tmp — so change this configuration or else all data will be lost on machine restart.

Default

`${hbase.tmp.dir}/hbase`

**`hbase.cluster.distributed`**

Description

The mode the cluster will be in. Possible values are false for standalone mode and true for distributed mode. If false, startup will run all HBase and ZooKeeper daemons together in the one JVM.

Default

`false`

**`hbase.zookeeper.quorum`**

Description

Comma separated list of servers in the ZooKeeper ensemble (This config. should have been named hbase.zookeeper.ensemble). For example, "host1.mydomain.com,host2.mydomain.com,host3.mydomain.com". By default this is set to localhost for local and pseudo-distributed modes of operation. For a fully-distributed setup, this should be set to a full list of ZooKeeper ensemble servers. If HBASE_MANAGES_ZK is set in hbase-env.sh this is the list of servers which hbase will start/stop ZooKeeper on as part of cluster start/stop. Client-side, we will take this list of ensemble members and put it together with the hbase.zookeeper.property.clientPort config. and pass it into zookeeper constructor as the connectString parameter.

Default

`127.0.0.1`

**`zookeeper.recovery.retry.maxsleeptime`**

Description

Max sleep time before retry zookeeper operations in milliseconds, a max time is needed here so that sleep time won’t grow unboundedly

Default

`60000`

**`hbase.local.dir`**

Description

Directory on the local filesystem to be used as a local storage.

Default

`${hbase.tmp.dir}/local/`

**`hbase.master.port`**

Description

The port the HBase Master should bind to.

Default

`16000`

**`hbase.master.info.port`**

Description

The port for the HBase Master web UI. Set to -1 if you do not want a UI instance run.

Default

`16010`

**`hbase.master.info.bindAddress`**

Description

The bind address for the HBase Master web UI

Default

`0.0.0.0`

**`hbase.master.logcleaner.plugins`**

Description

A comma-separated list of BaseLogCleanerDelegate invoked by the LogsCleaner service. These WAL cleaners are called in order, so put the cleaner that prunes the most files in front. To implement your own BaseLogCleanerDelegate, just put it in HBase’s classpath and add the fully qualified class name here. Always add the above default log cleaners in the list.

Default

`org.apache.hadoop.hbase.master.cleaner.TimeToLiveLogCleaner,org.apache.hadoop.hbase.master.cleaner.TimeToLiveProcedureWALCleaner,org.apache.hadoop.hbase.master.cleaner.TimeToLiveMasterLocalStoreWALCleaner`

**`hbase.master.logcleaner.ttl`**

Description

How long a WAL remain in the archive ({hbase.rootdir}/oldWALs) directory, after which it will be cleaned by a Master thread. The value is in milliseconds.

Default

`600000`

**`hbase.master.hfilecleaner.plugins`**

Description

A comma-separated list of BaseHFileCleanerDelegate invoked by the HFileCleaner service. These HFiles cleaners are called in order, so put the cleaner that prunes the most files in front. To implement your own BaseHFileCleanerDelegate, just put it in HBase’s classpath and add the fully qualified class name here. Always add the above default hfile cleaners in the list as they will be overwritten in hbase-site.xml.

Default

`org.apache.hadoop.hbase.master.cleaner.TimeToLiveHFileCleaner,org.apache.hadoop.hbase.master.cleaner.TimeToLiveMasterLocalStoreHFileCleaner`

**`hbase.master.infoserver.redirect`**

Description

Whether or not the Master listens to the Master web UI port (hbase.master.info.port) and redirects requests to the web UI server shared by the Master and RegionServer. Config. makes sense when Master is serving Regions (not the default).

Default

`true`

**`hbase.master.fileSplitTimeout`**

Description

Splitting a region, how long to wait on the file-splitting step before aborting the attempt. Default: 600000. This setting used to be known as hbase.regionserver.fileSplitTimeout in hbase-1.x. Split is now run master-side hence the rename (If a 'hbase.master.fileSplitTimeout' setting found, will use it to prime the current 'hbase.master.fileSplitTimeout' Configuration.

Default

`600000`

**`hbase.regionserver.port`**

Description

The port the HBase RegionServer binds to.

Default

`16020`

**`hbase.regionserver.info.port`**

Description

The port for the HBase RegionServer web UI Set to -1 if you do not want the RegionServer UI to run.

Default

`16030`

**`hbase.regionserver.info.bindAddress`**

Description

The address for the HBase RegionServer web UI

Default

`0.0.0.0`

**`hbase.regionserver.info.port.auto`**

Description

Whether or not the Master or RegionServer UI should search for a port to bind to. Enables automatic port search if hbase.regionserver.info.port is already in use. Useful for testing, turned off by default.

Default

`false`

**`hbase.regionserver.handler.count`**

Description

Count of RPC Listener instances spun up on RegionServers. Same property is used by the Master for count of master handlers. Too many handlers can be counter-productive. Make it a multiple of CPU count. If mostly read-only, handlers count close to cpu count does well. Start with twice the CPU count and tune from there.

Default

`30`

**`hbase.ipc.server.callqueue.handler.factor`**

Description

Factor to determine the number of call queues. A value of 0 means a single queue shared between all the handlers. A value of 1 means that each handler has its own queue.

Default

`0.1`

**`hbase.ipc.server.callqueue.read.ratio`**

Description

Split the call queues into read and write queues. The specified interval (which should be between 0.0 and 1.0) will be multiplied by the number of call queues. A value of 0 indicate to not split the call queues, meaning that both read and write requests will be pushed to the same set of queues. A value lower than 0.5 means that there will be less read queues than write queues. A value of 0.5 means there will be the same number of read and write queues. A value greater than 0.5 means that there will be more read queues than write queues. A value of 1.0 means that all the queues except one are used to dispatch read requests. Example: Given the total number of call queues being 10 a read.ratio of 0 means that: the 10 queues will contain both read/write requests. a read.ratio of 0.3 means that: 3 queues will contain only read requests and 7 queues will contain only write requests. a read.ratio of 0.5 means that: 5 queues will contain only read requests and 5 queues will contain only write requests. a read.ratio of 0.8 means that: 8 queues will contain only read requests and 2 queues will contain only write requests. a read.ratio of 1 means that: 9 queues will contain only read requests and 1 queues will contain only write requests.

Default

`0`

**`hbase.ipc.server.callqueue.scan.ratio`**

Description

Given the number of read call queues, calculated from the total number of call queues multiplied by the callqueue.read.ratio, the scan.ratio property will split the read call queues into small-read and long-read queues. A value lower than 0.5 means that there will be less long-read queues than short-read queues. A value of 0.5 means that there will be the same number of short-read and long-read queues. A value greater than 0.5 means that there will be more long-read queues than short-read queues A value of 0 or 1 indicate to use the same set of queues for gets and scans. Example: Given the total number of read call queues being 8 a scan.ratio of 0 or 1 means that: 8 queues will contain both long and short read requests. a scan.ratio of 0.3 means that: 2 queues will contain only long-read requests and 6 queues will contain only short-read requests. a scan.ratio of 0.5 means that: 4 queues will contain only long-read requests and 4 queues will contain only short-read requests. a scan.ratio of 0.8 means that: 6 queues will contain only long-read requests and 2 queues will contain only short-read requests.

Default

`0`

**`hbase.regionserver.msginterval`**

Description

Interval between messages from the RegionServer to Master in milliseconds.

Default

`3000`

**`hbase.regionserver.logroll.period`**

Description

Period at which we will roll the commit log regardless of how many edits it has.

Default

`3600000`

**`hbase.regionserver.logroll.errors.tolerated`**

Description

The number of consecutive WAL close errors we will allow before triggering a server abort. A setting of 0 will cause the region server to abort if closing the current WAL writer fails during log rolling. Even a small value (2 or 3) will allow a region server to ride over transient HDFS errors.

Default

`2`

**`hbase.regionserver.free.heap.min.memory.size`**

Description

Defines the minimum amount of heap memory that must remain free for the RegionServer to start, specified in bytes or human-readable formats like '512m' for megabytes or '4g' for gigabytes. If not set, the default is 20% of the total heap size. To disable the check entirely, set this value to 0. If the combined memory usage of memstore and block cache exceeds (total heap - this value), the RegionServer will fail to start.

Default

none

**`hbase.regionserver.global.memstore.size`**

Description

Maximum size of all memstores in a region server before new updates are blocked and flushes are forced. Defaults to 40% of heap (0.4). Updates are blocked and flushes are forced until size of all memstores in a region server hits hbase.regionserver.global.memstore.size.lower.limit. The default value in this configuration has been intentionally left empty in order to honor the old hbase.regionserver.global.memstore.upperLimit property if present.

Default

none

**`hbase.regionserver.global.memstore.size.lower.limit`**

Description

Maximum size of all memstores in a region server before flushes are forced. Defaults to 95% of hbase.regionserver.global.memstore.size (0.95). A 100% value for this value causes the minimum possible flushing to occur when updates are blocked due to memstore limiting. The default value in this configuration has been intentionally left empty in order to honor the old hbase.regionserver.global.memstore.lowerLimit property if present.

Default

none

**`hbase.systemtables.compacting.memstore.type`**

Description

Determines the type of memstore to be used for system tables like META, namespace tables etc. By default NONE is the type and hence we use the default memstore for all the system tables. If we need to use compacting memstore for system tables then set this property to BASIC/EAGER

Default

`NONE`

**`hbase.regionserver.optionalcacheflushinterval`**

Description

Maximum amount of time an edit lives in memory before being automatically flushed. Default 1 hour. Set it to 0 to disable automatic flushing.

Default

`3600000`

**`hbase.regionserver.dns.interface`**

Description

The name of the Network Interface from which a region server should report its IP address.

Default

`default`

**`hbase.regionserver.dns.nameserver`**

Description

The host name or IP address of the name server (DNS) which a region server should use to determine the host name used by the master for communication and display purposes.

Default

`default`

**`hbase.regionserver.region.split.policy`**

Description

A split policy determines when a region should be split. The various other split policies that are available currently are BusyRegionSplitPolicy, ConstantSizeRegionSplitPolicy, DisabledRegionSplitPolicy, DelimitedKeyPrefixRegionSplitPolicy, KeyPrefixRegionSplitPolicy, and SteppingSplitPolicy. DisabledRegionSplitPolicy blocks manual region splitting.

Default

`org.apache.hadoop.hbase.regionserver.SteppingSplitPolicy`

**`hbase.regionserver.regionSplitLimit`**

Description

Limit for the number of regions after which no more region splitting should take place. This is not hard limit for the number of regions but acts as a guideline for the regionserver to stop splitting after a certain limit. Default is set to 1000.

Default

`1000`

**`zookeeper.session.timeout`**

Description

ZooKeeper session timeout in milliseconds. It is used in two different ways. First, this value is used in the ZK client that HBase uses to connect to the ensemble. It is also used by HBase when it starts a ZK server and it is passed as the 'maxSessionTimeout'. See https://zookeeper.apache.org/doc/current/zookeeperProgrammers.html#ch_zkSessions. For example, if an HBase region server connects to a ZK ensemble that’s also managed by HBase, then the session timeout will be the one specified by this configuration. But, a region server that connects to an ensemble managed with a different configuration will be subjected that ensemble’s maxSessionTimeout. So, even though HBase might propose using 90 seconds, the ensemble can have a max timeout lower than this and it will take precedence. The current default maxSessionTimeout that ZK ships with is 40 seconds, which is lower than HBase’s.

Default

`90000`

**`zookeeper.znode.parent`**

Description

Root ZNode for HBase in ZooKeeper. All of HBase’s ZooKeeper files that are configured with a relative path will go under this node. By default, all of HBase’s ZooKeeper file paths are configured with a relative path, so they will all go under this directory unless changed.

Default

`/hbase`

**`zookeeper.znode.acl.parent`**

Description

Root ZNode for access control lists.

Default

`acl`

**`hbase.zookeeper.dns.interface`**

Description

The name of the Network Interface from which a ZooKeeper server should report its IP address.

Default

`default`

**`hbase.zookeeper.dns.nameserver`**

Description

The host name or IP address of the name server (DNS) which a ZooKeeper server should use to determine the host name used by the master for communication and display purposes.

Default

`default`

**`hbase.zookeeper.peerport`**

Description

Port used by ZooKeeper peers to talk to each other. See https://zookeeper.apache.org/doc/r3.4.10/zookeeperStarted.html#sc_RunningReplicatedZooKeeper for more information.

Default

`2888`

**`hbase.zookeeper.leaderport`**

Description

Port used by ZooKeeper for leader election. See https://zookeeper.apache.org/doc/r3.4.10/zookeeperStarted.html#sc_RunningReplicatedZooKeeper for more information.

Default

`3888`

**`hbase.zookeeper.property.initLimit`**

Description

Property from ZooKeeper’s config zoo.cfg. The number of ticks that the initial synchronization phase can take.

Default

`10`

**`hbase.zookeeper.property.syncLimit`**

Description

Property from ZooKeeper’s config zoo.cfg. The number of ticks that can pass between sending a request and getting an acknowledgment.

Default

`5`

**`hbase.zookeeper.property.dataDir`**

Description

Property from ZooKeeper’s config zoo.cfg. The directory where the snapshot is stored.

Default

`${hbase.tmp.dir}/zookeeper`

**`hbase.zookeeper.property.clientPort`**

Description

Property from ZooKeeper’s config zoo.cfg. The port at which the clients will connect.

Default

`2181`

**`hbase.zookeeper.property.maxClientCnxns`**

Description

Property from ZooKeeper’s config zoo.cfg. Limit on number of concurrent connections (at the socket level) that a single client, identified by IP address, may make to a single member of the ZooKeeper ensemble. Set high to avoid zk connection issues running standalone and pseudo-distributed.

Default

`300`

**`hbase.client.write.buffer`**

Description

Default size of the BufferedMutator write buffer in bytes. A bigger buffer takes more memory — on both the client and server side since server instantiates the passed write buffer to process it — but a larger buffer size reduces the number of RPCs made. For an estimate of server-side memory-used, evaluate hbase.client.write.buffer * hbase.regionserver.handler.count

Default

`2097152`

**`hbase.client.pause`**

Description

General client pause value. Used mostly as value to wait before running a retry of a failed get, region lookup, etc. See hbase.client.retries.number for description of how we backoff from this initial pause amount and how this pause works w/ retries.

Default

`100`

**`hbase.client.pause.server.overloaded`**

Description

Pause time when encountering an exception indicating a server is overloaded, CallQueueTooBigException or CallDroppedException. Set this property to a higher value than hbase.client.pause if you observe frequent CallQueueTooBigException or CallDroppedException from the same RegionServer and the call queue there keeps filling up. This config used to be called hbase.client.pause.cqtbe, which has been deprecated as of 2.5.0.

Default

none

**`hbase.client.retries.number`**

Description

Maximum retries. Used as maximum for all retryable operations such as the getting of a cell’s value, starting a row update, etc. Retry interval is a rough function based on hbase.client.pause. At first we retry at this interval but then with backoff, we pretty quickly reach retrying every ten seconds. See HConstants#RETRY_BACKOFF for how the backup ramps up. Change this setting and hbase.client.pause to suit your workload.

Default

`15`

**`hbase.client.max.total.tasks`**

Description

The maximum number of concurrent mutation tasks a single HTable instance will send to the cluster.

Default

`100`

**`hbase.client.max.perserver.tasks`**

Description

The maximum number of concurrent mutation tasks a single HTable instance will send to a single region server.

Default

`2`

**`hbase.client.max.perregion.tasks`**

Description

The maximum number of concurrent mutation tasks the client will maintain to a single Region. That is, if there is already hbase.client.max.perregion.tasks writes in progress for this region, new puts won’t be sent to this region until some writes finishes.

Default

`1`

**`hbase.client.perserver.requests.threshold`**

Description

The max number of concurrent pending requests for one server in all client threads (process level). Exceeding requests will be thrown ServerTooBusyException immediately to prevent user’s threads being occupied and blocked by only one slow region server. If you use a fix number of threads to access HBase in a synchronous way, set this to a suitable value which is related to the number of threads will help you. See https://issues.apache.org/jira/browse/HBASE-16388 for details.

Default

`2147483647`

**`hbase.client.scanner.caching`**

Description

Number of rows that we try to fetch when calling next on a scanner if it is not served from (local, client) memory. This configuration works together with hbase.client.scanner.max.result.size to try and use the network efficiently. The default value is Integer.MAX_VALUE by default so that the network will fill the chunk size defined by hbase.client.scanner.max.result.size rather than be limited by a particular number of rows since the size of rows varies table to table. If you know ahead of time that you will not require more than a certain number of rows from a scan, this configuration should be set to that row limit via Scan#setCaching. Higher caching values will enable faster scanners but will eat up more memory and some calls of next may take longer and longer times when the cache is empty. Do not set this value such that the time between invocations is greater than the scanner timeout; i.e. hbase.client.scanner.timeout.period

Default

`2147483647`

**`hbase.client.keyvalue.maxsize`**

Description

Specifies the combined maximum allowed size of a KeyValue instance. This is to set an upper boundary for a single entry saved in a storage file. Since they cannot be split it helps avoiding that a region cannot be split any further because the data is too large. It seems wise to set this to a fraction of the maximum region size. Setting it to zero or less disables the check.

Default

`10485760`

**`hbase.server.keyvalue.maxsize`**

Description

Maximum allowed size of an individual cell, inclusive of value and all key components. A value of 0 or less disables the check. The default value is 10MB. This is a safety setting to protect the server from OOM situations.

Default

`10485760`

**`hbase.client.scanner.timeout.period`**

Description

Client scanner lease period in milliseconds.

Default

`60000`

**`hbase.client.localityCheck.threadPoolSize`**

Default

`2`

**`hbase.bulkload.retries.number`**

Description

Maximum retries. This is maximum number of iterations to atomic bulk loads are attempted in the face of splitting operations 0 means never give up.

Default

`10`

**`hbase.compaction.after.bulkload.enable`**

Description

Request Compaction after bulkload immediately. If bulkload is continuous, the triggered compactions may increase load, bring about performance side effect.

Default

`false`

**`hbase.master.balancer.maxRitPercent`**

Description

The max percent of regions in transition when balancing. The default value is 1.0. So there are no balancer throttling. If set this config to 0.01, It means that there are at most 1% regions in transition when balancing. Then the cluster’s availability is at least 99% when balancing.

Default

`1.0`

**`hbase.balancer.period`**

Description

Period at which the region balancer runs in the Master, in milliseconds.

Default

`300000`

**`hbase.master.oldwals.dir.updater.period`**

Description

Period at which the oldWALs directory size calculator/updater will run in the Master, in milliseconds.

Default

`300000`

**`hbase.regions.slop`**

Description

The load balancer can trigger for several reasons. This value controls one of those reasons. Run the balancer if any regionserver has a region count outside the range of average +/- (average * slop) regions. If the value of slop is negative, disable sloppiness checks. The balancer can still run for other reasons, but sloppiness will not be one of them. If the value of slop is 0, run the balancer if any server has a region count more than 1 from the average. If the value of slop is 100, run the balancer if any server has a region count greater than 101 times the average. The default value of this parameter is 0.2, which runs the balancer if any server has a region count less than 80% of the average, or greater than 120% of the average. Note that for the default StochasticLoadBalancer, this does not guarantee any balancing actions will be taken, but only that the balancer will attempt to run.

Default

`0.2`

**`hbase.normalizer.period`**

Description

Period at which the region normalizer runs in the Master, in milliseconds.

Default

`300000`

**`hbase.normalizer.split.enabled`**

Description

Whether to split a region as part of normalization.

Default

`true`

**`hbase.normalizer.merge.enabled`**

Description

Whether to merge a region as part of normalization.

Default

`true`

**`hbase.normalizer.merge.min.region.count`**

Description

The minimum number of regions in a table to consider it for merge normalization.

Default

`3`

**`hbase.normalizer.merge.min_region_age.days`**

Description

The minimum age for a region to be considered for a merge, in days.

Default

`3`

**`hbase.normalizer.merge.min_region_size.mb`**

Description

The minimum size for a region to be considered for a merge, in whole MBs.

Default

`1`

**`hbase.normalizer.merge.merge_request_max_number_of_regions`**

Description

The maximum number of region count in a merge request for merge normalization.

Default

`100`

**`hbase.table.normalization.enabled`**

Description

This config is used to set default behaviour of normalizer at table level. To override this at table level one can set NORMALIZATION_ENABLED at table descriptor level and that property will be honored

Default

`false`

**`hbase.server.thread.wakefrequency`**

Description

In master side, this config is the period used for FS related behaviors: checking if hdfs is out of safe mode, setting or checking hbase.version file, setting or checking hbase.id file. Using default value should be fine. In regionserver side, this config is used in several places: flushing check interval, compaction check interval, wal rolling check interval. Specially, admin can tune flushing and compaction check interval by hbase.regionserver.flush.check.period and hbase.regionserver.compaction.check.period. (in milliseconds)

Default

`10000`

**`hbase.regionserver.flush.check.period`**

Description

It determines the flushing check period of PeriodicFlusher in regionserver. If unset, it uses hbase.server.thread.wakefrequency as default value. (in milliseconds)

Default

`${hbase.server.thread.wakefrequency}`

**`hbase.regionserver.compaction.check.period`**

Description

It determines the compaction check period of CompactionChecker in regionserver. If unset, it uses hbase.server.thread.wakefrequency as default value. (in milliseconds)

Default

`${hbase.server.thread.wakefrequency}`

**`hbase.server.versionfile.writeattempts`**

Description

How many times to retry attempting to write a version file before just aborting. Each attempt is separated by the hbase.server.thread.wakefrequency milliseconds.

Default

`3`

**`hbase.hregion.memstore.flush.size`**

Description

Memstore will be flushed to disk if size of the memstore exceeds this number of bytes. Value is checked by a thread that runs every hbase.server.thread.wakefrequency.

Default

`134217728`

**`hbase.hregion.percolumnfamilyflush.size.lower.bound.min`**

Description

If FlushLargeStoresPolicy is used and there are multiple column families, then every time that we hit the total memstore limit, we find out all the column families whose memstores exceed a "lower bound" and only flush them while retaining the others in memory. The "lower bound" will be "hbase.hregion.memstore.flush.size / column_family_number" by default unless value of this property is larger than that. If none of the families have their memstore size more than lower bound, all the memstores will be flushed (just as usual).

Default

`16777216`

**`hbase.hregion.preclose.flush.size`**

Description

If the memstores in a region are this size or larger when we go to close, run a "pre-flush" to clear out memstores before we put up the region closed flag and take the region offline. On close, a flush is run under the close flag to empty memory. During this time the region is offline and we are not taking on any writes. If the memstore content is large, this flush could take a long time to complete. The preflush is meant to clean out the bulk of the memstore before putting up the close flag and taking the region offline so the flush that runs under the close flag has little to do.

Default

`5242880`

**`hbase.hregion.memstore.block.multiplier`**

Description

Block updates if memstore has hbase.hregion.memstore.block.multiplier times hbase.hregion.memstore.flush.size bytes. Useful preventing runaway memstore during spikes in update traffic. Without an upper-bound, memstore fills such that when it flushes the resultant flush files take a long time to compact or split, or worse, we OOME.

Default

`4`

**`hbase.hregion.memstore.mslab.enabled`**

Description

Enables the MemStore-Local Allocation Buffer, a feature which works to prevent heap fragmentation under heavy write loads. This can reduce the frequency of stop-the-world GC pauses on large heaps.

Default

`true`

**`hbase.hregion.memstore.mslab.chunksize`**

Description

The maximum byte size of a chunk in the MemStoreLAB. Unit: bytes

Default

`2097152`

**`hbase.regionserver.offheap.global.memstore.size`**

Description

The amount of off-heap memory all MemStores in a RegionServer may use. A value of 0 means that no off-heap memory will be used and all chunks in MSLAB will be HeapByteBuffer, otherwise the non-zero value means how many megabyte of off-heap memory will be used for chunks in MSLAB and all chunks in MSLAB will be DirectByteBuffer. Unit: megabytes.

Default

`0`

**`hbase.hregion.memstore.mslab.max.allocation`**

Description

The maximal size of one allocation in the MemStoreLAB, if the desired byte size exceed this threshold then it will be just allocated from JVM heap rather than MemStoreLAB.

Default

`262144`

**`hbase.hregion.max.filesize`**

Description

Maximum file size. If the sum of the sizes of a region’s HFiles has grown to exceed this value, the region is split in two. There are two choices of how this option works, the first is when any store’s size exceed the threshold then split, and the other is overall region’s size exceed the threshold then split, it can be configed by hbase.hregion.split.overallfiles.

Default

`10737418240`

**`hbase.hregion.split.overallfiles`**

Description

If we should sum overall region files size when check to split.

Default

`true`

**`hbase.hregion.majorcompaction`**

Description

Time between major compactions, expressed in milliseconds. Set to 0 to disable time-based automatic major compactions. User-requested and size-based major compactions will still run. This value is multiplied by hbase.hregion.majorcompaction.jitter to cause compaction to start at a somewhat-random time during a given window of time. The default value is 7 days, expressed in milliseconds. If major compactions are causing disruption in your environment, you can configure them to run at off-peak times for your deployment, or disable time-based major compactions by setting this parameter to 0, and run major compactions in a cron job or by another external mechanism.

Default

`604800000`

**`hbase.hregion.majorcompaction.jitter`**

Description

A multiplier applied to hbase.hregion.majorcompaction to cause compaction to occur a given amount of time either side of hbase.hregion.majorcompaction. The smaller the number, the closer the compactions will happen to the hbase.hregion.majorcompaction interval.

Default

`0.50`

**`hbase.hstore.compactionThreshold`**

Description

If more than or equal to this number of StoreFiles exist in any one Store (one StoreFile is written per flush of MemStore), a compaction is run to rewrite all StoreFiles into a single StoreFile. Larger values delay compaction, but when compaction does occur, it takes longer to complete.

Default

`3`

**`hbase.regionserver.compaction.enabled`**

Description

Enable/disable compactions on by setting true/false. We can further switch compactions dynamically with the compaction_switch shell command.

Default

`true`

**`hbase.hstore.flusher.count`**

Description

The number of flush threads. With fewer threads, the MemStore flushes will be queued. With more threads, the flushes will be executed in parallel, increasing the load on HDFS, and potentially causing more compactions.

Default

`2`

**`hbase.hstore.blockingStoreFiles`**

Description

If more than this number of StoreFiles exist in any one Store (one StoreFile is written per flush of MemStore), updates are blocked for this region until a compaction is completed, or until hbase.hstore.blockingWaitTime has been exceeded.

Default

`16`

**`hbase.hstore.blockingWaitTime`**

Description

The time for which a region will block updates after reaching the StoreFile limit defined by hbase.hstore.blockingStoreFiles. After this time has elapsed, the region will stop blocking updates even if a compaction has not been completed.

Default

`90000`

**`hbase.hstore.compaction.min`**

Description

The minimum number of StoreFiles which must be eligible for compaction before compaction can run. The goal of tuning hbase.hstore.compaction.min is to avoid ending up with too many tiny StoreFiles to compact. Setting this value to 2 would cause a minor compaction each time you have two StoreFiles in a Store, and this is probably not appropriate. If you set this value too high, all the other values will need to be adjusted accordingly. For most cases, the default value is appropriate (empty value here, results in 3 by code logic). In previous versions of HBase, the parameter hbase.hstore.compaction.min was named hbase.hstore.compactionThreshold.

Default

none

**`hbase.hstore.compaction.max`**

Description

The maximum number of StoreFiles which will be selected for a single minor compaction, regardless of the number of eligible StoreFiles. Effectively, the value of hbase.hstore.compaction.max controls the length of time it takes a single compaction to complete. Setting it larger means that more StoreFiles are included in a compaction. For most cases, the default value is appropriate.

Default

`10`

**`hbase.hstore.compaction.min.size`**

Description

A StoreFile (or a selection of StoreFiles, when using ExploringCompactionPolicy) smaller than this size will always be eligible for minor compaction. HFiles this size or larger are evaluated by hbase.hstore.compaction.ratio to determine if they are eligible. Because this limit represents the "automatic include" limit for all StoreFiles smaller than this value, this value may need to be reduced in write-heavy environments where many StoreFiles in the 1-2 MB range are being flushed, because every StoreFile will be targeted for compaction and the resulting StoreFiles may still be under the minimum size and require further compaction. If this parameter is lowered, the ratio check is triggered more quickly. This addressed some issues seen in earlier versions of HBase but changing this parameter is no longer necessary in most situations. Default: 128 MB expressed in bytes.

Default

`134217728`

**`hbase.hstore.compaction.max.size`**

Description

A StoreFile (or a selection of StoreFiles, when using ExploringCompactionPolicy) larger than this size will be excluded from compaction. The effect of raising hbase.hstore.compaction.max.size is fewer, larger StoreFiles that do not get compacted often. If you feel that compaction is happening too often without much benefit, you can try raising this value. Default: the value of LONG.MAX_VALUE, expressed in bytes.

Default

`9223372036854775807`

**`hbase.hstore.compaction.ratio`**

Description

For minor compaction, this ratio is used to determine whether a given StoreFile which is larger than hbase.hstore.compaction.min.size is eligible for compaction. Its effect is to limit compaction of large StoreFiles. The value of hbase.hstore.compaction.ratio is expressed as a floating-point decimal. A large ratio, such as 10, will produce a single giant StoreFile. Conversely, a low value, such as .25, will produce behavior similar to the BigTable compaction algorithm, producing four StoreFiles. A moderate value of between 1.0 and 1.4 is recommended. When tuning this value, you are balancing write costs with read costs. Raising the value (to something like 1.4) will have more write costs, because you will compact larger StoreFiles. However, during reads, HBase will need to seek through fewer StoreFiles to accomplish the read. Consider this approach if you cannot take advantage of Bloom filters. Otherwise, you can lower this value to something like 1.0 to reduce the background cost of writes, and use Bloom filters to control the number of StoreFiles touched during reads. For most cases, the default value is appropriate.

Default

`1.2F`

**`hbase.hstore.compaction.ratio.offpeak`**

Description

Allows you to set a different (by default, more aggressive) ratio for determining whether larger StoreFiles are included in compactions during off-peak hours. Works in the same way as hbase.hstore.compaction.ratio. Only applies if hbase.offpeak.start.hour and hbase.offpeak.end.hour are also enabled.

Default

`5.0F`

**`hbase.hstore.time.to.purge.deletes`**

Description

The amount of time to delay purging of delete markers with future timestamps. If unset, or set to 0, all delete markers, including those with future timestamps, are purged during the next major compaction. Otherwise, a delete marker is kept until the major compaction which occurs after the marker’s timestamp plus the value of this setting, in milliseconds.

Default

`0`

**`hbase.offpeak.start.hour`**

Description

The start of off-peak hours, expressed as an integer between 0 and 23, inclusive. Set to -1 to disable off-peak.

Default

`-1`

**`hbase.offpeak.end.hour`**

Description

The end of off-peak hours, expressed as an integer between 0 and 23, inclusive. Set to -1 to disable off-peak.

Default

`-1`

**`hbase.regionserver.thread.compaction.throttle`**

Description

There are two different thread pools for compactions, one for large compactions and the other for small compactions. This helps to keep compaction of lean tables (such as hbase:meta) fast. If a compaction is larger than this threshold, it goes into the large compaction pool. In most cases, the default value is appropriate. Default: 2 x hbase.hstore.compaction.max x hbase.hregion.memstore.flush.size (which defaults to 128MB). The value field assumes that the value of hbase.hregion.memstore.flush.size is unchanged from the default.

Default

`2684354560`

**`hbase.regionserver.majorcompaction.pagecache.drop`**

Description

Specifies whether to drop pages read/written into the system page cache by major compactions. Setting it to true helps prevent major compactions from polluting the page cache, which is almost always required, especially for clusters with low/moderate memory to storage ratio.

Default

`true`

**`hbase.regionserver.minorcompaction.pagecache.drop`**

Description

Specifies whether to drop pages read/written into the system page cache by minor compactions. Setting it to true helps prevent minor compactions from polluting the page cache, which is most beneficial on clusters with low memory to storage ratio or very write heavy clusters. You may want to set it to false under moderate to low write workload when bulk of the reads are on the most recently written data.

Default

`true`

**`hbase.hstore.compaction.kv.max`**

Description

The maximum number of KeyValues to read and then write in a batch when flushing or compacting. Set this lower if you have big KeyValues and problems with Out Of Memory Exceptions Set this higher if you have wide, small rows.

Default

`10`

**`hbase.storescanner.parallel.seek.enable`**

Description

Enables StoreFileScanner parallel-seeking in StoreScanner, a feature which can reduce response latency under special conditions.

Default

`false`

**`hbase.storescanner.parallel.seek.threads`**

Description

The default thread pool size if parallel-seeking feature enabled.

Default

`10`

**`hfile.block.cache.policy`**

Description

The eviction policy for the L1 block cache (LRU or TinyLFU).

Default

`LRU`

**`hfile.block.cache.size`**

Description

Percentage of maximum heap (-Xmx setting) to allocate to block cache used by a StoreFile. Default of 0.4 means allocate 40%. Set to 0 to disable but it’s not recommended; you need at least enough cache to hold the storefile indices.

Default

`0.4`

**`hfile.block.cache.memory.size`**

Description

Defines the maximum heap memory allocated for the HFile block cache, specified in bytes or human-readable formats like '10m' for megabytes or '10g' for gigabytes. This configuration allows setting an absolute memory size instead of a percentage of the maximum heap. Takes precedence over hfile.block.cache.size if both are specified.

Default

none

**`hfile.block.index.cacheonwrite`**

Description

This allows to put non-root multi-level index blocks into the block cache at the time the index is being written.

Default

`false`

**`hfile.index.block.max.size`**

Description

When the size of a leaf-level, intermediate-level, or root-level index block in a multi-level block index grows to this size, the block is written out and a new block is started.

Default

`131072`

**`hbase.bucketcache.ioengine`**

Description

Where to store the contents of the bucketcache. One of: offheap, file, files, mmap or pmem. If a file or files, set it to file(s):PATH_TO_FILE. mmap means the content will be in an mmaped file. Use mmap:PATH_TO_FILE. 'pmem' is bucket cache over a file on the persistent memory device. Use pmem:PATH_TO_FILE. See offheap.blockcache for more information.

Default

none

**`hbase.hstore.compaction.throughput.lower.bound`**

Description

The target lower bound on aggregate compaction throughput, in bytes/sec. Allows you to tune the minimum available compaction throughput when the PressureAwareCompactionThroughputController throughput controller is active. (It is active by default.)

Default

`52428800`

**`hbase.hstore.compaction.throughput.higher.bound`**

Description

The target upper bound on aggregate compaction throughput, in bytes/sec. Allows you to control aggregate compaction throughput demand when the PressureAwareCompactionThroughputController throughput controller is active. (It is active by default.) The maximum throughput will be tuned between the lower and upper bounds when compaction pressure is within the range [0.0, 1.0]. If compaction pressure is 1.0 or greater the higher bound will be ignored until pressure returns to the normal range.

Default

`104857600`

**`hbase.bucketcache.size`**

Description

It is the total capacity in megabytes of BucketCache. Default: 0.0

Default

none

**`hbase.bucketcache.bucket.sizes`**

Description

A comma-separated list of sizes for buckets for the bucketcache. Can be multiple sizes. List block sizes in order from smallest to largest. The sizes you use will depend on your data access patterns. Must be a multiple of 256 else you will run into 'java.io.IOException: Invalid HFile block magic' when you go to read from cache. If you specify no values here, then you pick up the default bucketsizes set in code (See BucketAllocator#DEFAULT_BUCKET_SIZES).

Default

none

**`hfile.format.version`**

Description

The HFile format version to use for new files. Version 3 adds support for tags in hfiles (See #hbase.tags). Also see the configuration 'hbase.replication.rpc.codec'.
