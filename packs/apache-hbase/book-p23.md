---
title: "Apache HBase® Reference Guide (part 23/41)"
source: https://hbase.apache.org/book.html
domain: apache-hbase
license: CC-BY-SA-4.0
tags: apache hbase, bigtable clone, wide-column store, apache hadoop
fetched: 2026-07-02
part: 23/41
---

## 114. Loading Coprocessors

To make your coprocessor available to HBase, it must be *loaded*, either statically (through the HBase configuration) or dynamically (using HBase Shell or the Java API).

### 114.1. Static Loading

Follow these steps to statically load your coprocessor. Keep in mind that you must restart HBase to unload a coprocessor that has been loaded statically.

1. Define the Coprocessor in *hbase-site.xml*, with a <property> element with a <name> and a <value> sub-element. The <name> should be one of the following: `hbase.coprocessor.region.classes` for RegionObservers and Endpoints. `hbase.coprocessor.wal.classes` for WALObservers. `hbase.coprocessor.master.classes` for MasterObservers. <value> must contain the fully-qualified class name of your coprocessor’s implementation class. For example to load a Coprocessor (implemented in class SumEndPoint.java) you have to create following entry in RegionServer’s 'hbase-site.xml' file (generally located under 'conf' directory): `<property> <name>hbase.coprocessor.region.classes</name> <value>org.myname.hbase.coprocessor.endpoint.SumEndPoint</value> </property>` If multiple classes are specified for loading, the class names must be comma-separated. The framework attempts to load all the configured classes using the default class loader. Therefore, the jar file must reside on the server-side HBase classpath. Coprocessors which are loaded in this way will be active on all regions of all tables. These are also called system Coprocessor. The first listed Coprocessors will be assigned the priority `Coprocessor.Priority.SYSTEM`. Each subsequent coprocessor in the list will have its priority value incremented by one (which reduces its priority, because priorities have the natural sort order of Integers). These priority values can be manually overriden in hbase-site.xml. This can be useful if you want to guarantee that a coprocessor will execute after another. For example, in the following configuration `SumEndPoint` would be guaranteed to go last, except in the case of a tie with another coprocessor: `<property> <name>hbase.coprocessor.region.classes</name> <value>org.myname.hbase.coprocessor.endpoint.SumEndPoint|2147483647</value> </property>` When calling out to registered observers, the framework executes their callbacks methods in the sorted order of their priority. Ties are broken arbitrarily.
2. Put your code on HBase’s classpath. One easy way to do this is to drop the jar (containing you code and all the dependencies) into the `lib/` directory in the HBase installation.
3. Restart HBase.

### 114.2. Static Unloading

1. Delete the coprocessor’s <property> element, including sub-elements, from `hbase-site.xml`.
2. Restart HBase.
3. Optionally, remove the coprocessor’s JAR file from the classpath or HBase’s `lib/` directory.

### 114.3. Dynamic Loading

You can also load a coprocessor dynamically, without restarting HBase. This may seem preferable to static loading, but dynamically loaded coprocessors are loaded on a per-table basis, and are only available to the table for which they were loaded. For this reason, dynamically loaded tables are sometimes called **Table Coprocessor**.

In addition, dynamically loading a coprocessor acts as a schema change on the table, and the table must be taken offline to load the coprocessor.

There are three ways to dynamically load Coprocessor.

|   | Assumptions The below mentioned instructions makes the following assumptions: A JAR called `coprocessor.jar` contains the Coprocessor implementation along with all of its dependencies. The JAR is available in HDFS in some location like `hdfs://<namenode>:<port>/user/<hadoop-user>/coprocessor.jar`. |
|---|---|

#### 114.3.1. Using HBase Shell

1. Load the Coprocessor, using a command like the following: `hbase alter 'users', METHOD => 'table_att', 'Coprocessor'=>'hdfs://<namenode>:<port>/ user/<hadoop-user>/coprocessor.jar| org.myname.hbase.Coprocessor.RegionObserverExample|1073741823| arg1=1,arg2=2'` The Coprocessor framework will try to read the class information from the coprocessor table attribute value. The value contains four pieces of information which are separated by the pipe (`|`) character. File path: The jar file containing the Coprocessor implementation must be in a location where all region servers can read it. You could copy the file onto the local disk on each region server, but it is recommended to store it in HDFS. HBASE-14548 allows a directory containing the jars or some wildcards to be specified, such as: hdfs://<namenode>:<port>/user/<hadoop-user>/ or hdfs://<namenode>:<port>/user/<hadoop-user>/*.jar. Please note that if a directory is specified, all jar files(.jar) in the directory are added. It does not search for files in sub-directories. Do not use a wildcard if you would like to specify a directory. This enhancement applies to the usage via the JAVA API as well. Class name: The full class name of the Coprocessor. Priority: An integer. The framework will determine the execution sequence of all configured observers registered at the same hook using priorities. This field can be left blank. In that case the framework will assign a default priority value. Arguments (Optional): This field is passed to the Coprocessor implementation. This is optional.
2. Verify that the coprocessor loaded: `hbase(main):04:0> describe 'users'` The coprocessor should be listed in the `TABLE_ATTRIBUTES`.

#### 114.3.2. Using the Java API (all HBase versions)

The following Java code shows how to use the `setValue()` method of `HTableDescriptor` to load a coprocessor on the `users` table.

```
TableName tableName = TableName.valueOf("users");
String path = "hdfs://<namenode>:<port>/user/<hadoop-user>/coprocessor.jar";
Configuration conf = HBaseConfiguration.create();
Connection connection = ConnectionFactory.createConnection(conf);
Admin admin = connection.getAdmin();
HTableDescriptor hTableDescriptor = new HTableDescriptor(tableName);
HColumnDescriptor columnFamily1 = new HColumnDescriptor("personalDet");
columnFamily1.setMaxVersions(3);
hTableDescriptor.addFamily(columnFamily1);
HColumnDescriptor columnFamily2 = new HColumnDescriptor("salaryDet");
columnFamily2.setMaxVersions(3);
hTableDescriptor.addFamily(columnFamily2);
hTableDescriptor.setValue("COPROCESSOR$1", path + "|"
+ RegionObserverExample.class.getCanonicalName() + "|"
+ Coprocessor.PRIORITY_USER);
admin.modifyTable(tableName, hTableDescriptor);
```

#### 114.3.3. Using the Java API (HBase 0.96+ only)

In HBase 0.96 and newer, the `addCoprocessor()` method of `HTableDescriptor` provides an easier way to load a coprocessor dynamically.

```
TableName tableName = TableName.valueOf("users");
Path path = new Path("hdfs://<namenode>:<port>/user/<hadoop-user>/coprocessor.jar");
Configuration conf = HBaseConfiguration.create();
Connection connection = ConnectionFactory.createConnection(conf);
Admin admin = connection.getAdmin();
HTableDescriptor hTableDescriptor = new HTableDescriptor(tableName);
HColumnDescriptor columnFamily1 = new HColumnDescriptor("personalDet");
columnFamily1.setMaxVersions(3);
hTableDescriptor.addFamily(columnFamily1);
HColumnDescriptor columnFamily2 = new HColumnDescriptor("salaryDet");
columnFamily2.setMaxVersions(3);
hTableDescriptor.addFamily(columnFamily2);
hTableDescriptor.addCoprocessor(RegionObserverExample.class.getCanonicalName(), path,
Coprocessor.PRIORITY_USER, null);
admin.modifyTable(tableName, hTableDescriptor);
```

|   | There is no guarantee that the framework will load a given Coprocessor successfully. For example, the shell command neither guarantees a jar file exists at a particular location nor verifies whether the given class is actually contained in the jar file. |
|---|---|

### 114.4. Dynamic Unloading

#### 114.4.1. Using HBase Shell

1. Alter the table to remove the coprocessor with `table_att_unset`. `hbase> alter 'users', METHOD => 'table_att_unset', NAME => 'coprocessor$1'`
2. Alter the table to remove the coprocessor with `table_remove_coprocessor` introduced in HBASE-26524 by specifying an explicit classname `hbase> alter 'users', METHOD => 'table_remove_coprocessor', CLASSNAME => 'org.myname.hbase.Coprocessor.RegionObserverExample'`

#### 114.4.2. Using the Java API

Reload the table definition without setting the value of the coprocessor either by using `setValue()` or `addCoprocessor()` methods. This will remove any coprocessor attached to the table.

```
TableName tableName = TableName.valueOf("users");
String path = "hdfs://<namenode>:<port>/user/<hadoop-user>/coprocessor.jar";
Configuration conf = HBaseConfiguration.create();
Connection connection = ConnectionFactory.createConnection(conf);
Admin admin = connection.getAdmin();
HTableDescriptor hTableDescriptor = new HTableDescriptor(tableName);
HColumnDescriptor columnFamily1 = new HColumnDescriptor("personalDet");
columnFamily1.setMaxVersions(3);
hTableDescriptor.addFamily(columnFamily1);
HColumnDescriptor columnFamily2 = new HColumnDescriptor("salaryDet");
columnFamily2.setMaxVersions(3);
hTableDescriptor.addFamily(columnFamily2);
admin.modifyTable(tableName, hTableDescriptor);
```

In HBase 0.96 and newer, you can instead use the `removeCoprocessor()` method of the `HTableDescriptor` class.


## 115. Examples

HBase ships examples for Observer Coprocessor.

A more detailed example is given below.

These examples assume a table called `users`, which has two column families `personalDet` and `salaryDet`, containing personal and salary details. Below is the graphical representation of the `users` table.

|   | personalDet | salaryDet |   |   |   |   |
|---|---|---|---|---|---|---|
| **rowkey** | **name** | **lastname** | **dob** | **gross** | **net** | **allowances** |
| admin | Admin | Admin |   |   |   |   |
| cdickens | Charles | Dickens | 02/07/1812 | 10000 | 8000 | 2000 |
| jverne | Jules | Verne | 02/08/1828 | 12000 | 9000 | 3000 |

### 115.1. Observer Example

The following Observer coprocessor prevents the details of the user `admin` from being returned in a `Get` or `Scan` of the `users` table.

1. Write a class that implements the RegionCoprocessor, RegionObserver class.
2. Override the `preGetOp()` method (the `preGet()` method is deprecated) to check whether the client has queried for the rowkey with value `admin`. If so, return an empty result. Otherwise, process the request as normal.
3. Put your code and dependencies in a JAR file.
4. Place the JAR in HDFS where HBase can locate it.
5. Load the Coprocessor.
6. Write a simple program to test it.

Following are the implementation of the above steps:

```
public class RegionObserverExample implements RegionCoprocessor, RegionObserver {

    private static final byte[] ADMIN = Bytes.toBytes("admin");
    private static final byte[] COLUMN_FAMILY = Bytes.toBytes("details");
    private static final byte[] COLUMN = Bytes.toBytes("Admin_det");
    private static final byte[] VALUE = Bytes.toBytes("You can't see Admin details");

    @Override
    public Optional<RegionObserver> getRegionObserver() {
      return Optional.of(this);
    }

    @Override
    public void preGetOp(final ObserverContext<RegionCoprocessorEnvironment> e, final Get get, final List<Cell> results)
    throws IOException {

        if (Bytes.equals(get.getRow(),ADMIN)) {
            Cell c = CellUtil.createCell(get.getRow(),COLUMN_FAMILY, COLUMN,
            System.currentTimeMillis(), (byte)4, VALUE);
            results.add(c);
            e.bypass();
        }
    }
}
```

Overriding the `preGetOp()` will only work for `Get` operations. You also need to override the `preScannerOpen()` method to filter the `admin` row from scan results.

```
@Override
public RegionScanner preScannerOpen(final ObserverContext<RegionCoprocessorEnvironment> e, final Scan scan,
final RegionScanner s) throws IOException {

    Filter filter = new RowFilter(CompareOp.NOT_EQUAL, new BinaryComparator(ADMIN));
    scan.setFilter(filter);
    return s;
}
```

This method works but there is a *side effect*. If the client has used a filter in its scan, that filter will be replaced by this filter. Instead, you can explicitly remove any `admin` results from the scan:

```
@Override
public boolean postScannerNext(final ObserverContext<RegionCoprocessorEnvironment> e, final InternalScanner s,
final List<Result> results, final int limit, final boolean hasMore) throws IOException {
        Result result = null;
    Iterator<Result> iterator = results.iterator();
    while (iterator.hasNext()) {
    result = iterator.next();
        if (Bytes.equals(result.getRow(), ROWKEY)) {
            iterator.remove();
            break;
        }
    }
    return hasMore;
}
```

### 115.2. Endpoint Example

Still using the `users` table, this example implements a coprocessor to calculate the sum of all employee salaries, using an endpoint coprocessor.

1. Create a '.proto' file defining your service. `option java_package = "org.myname.hbase.coprocessor.autogenerated"; option java_outer_classname = "Sum"; option java_generic_services = true; option java_generate_equals_and_hash = true; option optimize_for = SPEED; message SumRequest { required string family = 1; required string column = 2; } message SumResponse { required int64 sum = 1 [default = 0]; } service SumService { rpc getSum(SumRequest) returns (SumResponse); }`
2. Execute the `protoc` command to generate the Java code from the above .proto' file. `$ mkdir src $ protoc --java_out=src ./sum.proto` This will generate a class call `Sum.java`.
3. Write a class that extends the generated service class, implement the `Coprocessor` and `CoprocessorService` classes, and override the service method. If you load a coprocessor from `hbase-site.xml` and then load the same coprocessor again using HBase Shell, it will be loaded a second time. The same class will exist twice, and the second instance will have a higher ID (and thus a lower priority). The effect is that the duplicate coprocessor is effectively ignored. `public class SumEndPoint extends Sum.SumService implements Coprocessor, CoprocessorService { private RegionCoprocessorEnvironment env; @Override public Service getService() { return this; } @Override public void start(CoprocessorEnvironment env) throws IOException { if (env instanceof RegionCoprocessorEnvironment) { this.env = (RegionCoprocessorEnvironment)env; } else { throw new CoprocessorException("Must be loaded on a table region!"); } } @Override public void stop(CoprocessorEnvironment env) throws IOException { } @Override public void getSum(RpcController controller, Sum.SumRequest request, RpcCallback<Sum.SumResponse> done) { Scan scan = new Scan(); scan.addFamily(Bytes.toBytes(request.getFamily())); scan.addColumn(Bytes.toBytes(request.getFamily()), Bytes.toBytes(request.getColumn())); Sum.SumResponse response = null; InternalScanner scanner = null; try { scanner = env.getRegion().getScanner(scan); List<Cell> results = new ArrayList<>(); boolean hasMore = false; long sum = 0L; do { hasMore = scanner.next(results); for (Cell cell : results) { sum = sum + Bytes.toLong(CellUtil.cloneValue(cell)); } results.clear(); } while (hasMore); response = Sum.SumResponse.newBuilder().setSum(sum).build(); } catch (IOException ioe) { ResponseConverter.setControllerException(controller, ioe); } finally { if (scanner != null) { try { scanner.close(); } catch (IOException ignored) {} } } done.run(response); } }` `Configuration conf = HBaseConfiguration.create(); Connection connection = ConnectionFactory.createConnection(conf); TableName tableName = TableName.valueOf("users"); Table table = connection.getTable(tableName); final Sum.SumRequest request = Sum.SumRequest.newBuilder().setFamily("salaryDet").setColumn("gross").build(); try { Map<byte[], Long> results = table.coprocessorService( Sum.SumService.class, null, null, new Batch.Call<Sum.SumService, Long>() { @Override public Long call(Sum.SumService aggregate) throws IOException { BlockingRpcCallback<Sum.SumResponse> rpcCallback = new BlockingRpcCallback<>(); aggregate.getSum(null, request, rpcCallback); Sum.SumResponse response = rpcCallback.get(); return response.hasSum() ? response.getSum() : 0L; } } ); for (Long sum : results.values()) { System.out.println("Sum = " + sum); } } catch (ServiceException e) { e.printStackTrace(); } catch (Throwable e) { e.printStackTrace(); }`
4. Load the Coprocessor.
5. Write a client code to call the Coprocessor.


## 116. Guidelines For Deploying A Coprocessor

**Bundling Coprocessors**

You can bundle all classes for a coprocessor into a single JAR on the RegionServer’s classpath, for easy deployment. Otherwise, place all dependencies on the RegionServer’s classpath so that they can be loaded during RegionServer start-up. The classpath for a RegionServer is set in the RegionServer’s `hbase-env.sh` file.

**Automating Deployment**

You can use a tool such as Puppet, Chef, or Ansible to ship the JAR for the coprocessor to the required location on your RegionServers' filesystems and restart each RegionServer, to automate coprocessor deployment. Details for such set-ups are out of scope of this document.

**Updating a Coprocessor**

Deploying a new version of a given coprocessor is not as simple as disabling it, replacing the JAR, and re-enabling the coprocessor. This is because you cannot reload a class in a JVM unless you delete all the current references to it. Since the current JVM has reference to the existing coprocessor, you must restart the JVM, by restarting the RegionServer, in order to replace it. This behavior is not expected to change.

**Coprocessor Logging**

The Coprocessor framework does not provide an API for logging beyond standard Java logging.

**Coprocessor Configuration**

If you do not want to load coprocessors from the HBase Shell, you can add their configuration properties to `hbase-site.xml`. In Using HBase Shell, two arguments are set: `arg1=1,arg2=2`. These could have been added to `hbase-site.xml` as follows:

```
<property>
  <name>arg1</name>
  <value>1</value>
</property>
<property>
  <name>arg2</name>
  <value>2</value>
</property>
```

Then you can read the configuration using code like the following:

```
Configuration conf = HBaseConfiguration.create();
Connection connection = ConnectionFactory.createConnection(conf);
TableName tableName = TableName.valueOf("users");
Table table = connection.getTable(tableName);

Get get = new Get(Bytes.toBytes("admin"));
Result result = table.get(get);
for (Cell c : result.rawCells()) {
    System.out.println(Bytes.toString(CellUtil.cloneRow(c))
        + "==> " + Bytes.toString(CellUtil.cloneFamily(c))
        + "{" + Bytes.toString(CellUtil.cloneQualifier(c))
        + ":" + Bytes.toLong(CellUtil.cloneValue(c)) + "}");
}
Scan scan = new Scan();
ResultScanner scanner = table.getScanner(scan);
for (Result res : scanner) {
    for (Cell c : res.rawCells()) {
        System.out.println(Bytes.toString(CellUtil.cloneRow(c))
        + " ==> " + Bytes.toString(CellUtil.cloneFamily(c))
        + " {" + Bytes.toString(CellUtil.cloneQualifier(c))
        + ":" + Bytes.toLong(CellUtil.cloneValue(c))
        + "}");
    }
}
```


## 117. Restricting Coprocessor Usage

Restricting arbitrary user coprocessors can be a big concern in multitenant environments. HBase provides a continuum of options for ensuring only expected coprocessors are running:

- `hbase.coprocessor.enabled`: Enables or disables all coprocessors. This will limit the functionality of HBase, as disabling all coprocessors will disable some security providers. An example coproccessor so affected is `org.apache.hadoop.hbase.security.access.AccessController`. `hbase.coprocessor.user.enabled`: Enables or disables loading coprocessors on tables (i.e. user coprocessors). One can statically load coprocessors, and optionally tune their priorities, via the following tunables in `hbase-site.xml`: `hbase.coprocessor.regionserver.classes`: A comma-separated list of coprocessors that are loaded by region servers `hbase.coprocessor.region.classes`: A comma-separated list of RegionObserver and Endpoint coprocessors `hbase.coprocessor.user.region.classes`: A comma-separated list of coprocessors that are loaded by all regions `hbase.coprocessor.master.classes`: A comma-separated list of coprocessors that are loaded by the master (MasterObserver coprocessors) `hbase.coprocessor.wal.classes`: A comma-separated list of WALObserver coprocessors to load `hbase.coprocessor.abortonerror`: Whether to abort the daemon which has loaded the coprocessor if the coprocessor should error other than `IOError`. If this is set to false and an access controller coprocessor should have a fatal error the coprocessor will be circumvented, as such in secure installations this is advised to be `true`; however, one may override this on a per-table basis for user coprocessors, to ensure they do not abort their running region server and are instead unloaded on error. `hbase.coprocessor.region.whitelist.paths`: A comma separated list available for those loading `org.apache.hadoop.hbase.security.access.CoprocessorWhitelistMasterObserver` whereby one can use the following options to white-list paths from which coprocessors may be loaded. Coprocessors on the classpath are implicitly white-listed `*` to wildcard all coprocessor paths An entire filesystem (e.g. `hdfs://my-cluster/`) A wildcard path to be evaluated by FilenameUtils.wildcardMatch Note: Path can specify scheme or not (e.g. `file:///usr/hbase/lib/coprocessors` or for all filesystems `/usr/hbase/lib/coprocessors`)

# Apache HBase Performance Tuning


## 118. Operating System

### 118.1. Memory

RAM, RAM, RAM. Don’t starve HBase.

### 118.2. 64-bit

Use a 64-bit platform (and 64-bit JVM).

### 118.3. Swapping

Watch out for swapping. Set `swappiness` to 0.

### 118.4. CPU

Make sure you have set up your Hadoop to use native, hardware checksumming. See hadoop.native.lib.


## 119. Network

Perhaps the most important factor in avoiding network issues degrading Hadoop and HBase performance is the switching hardware that is used, decisions made early in the scope of the project can cause major problems when you double or triple the size of your cluster (or more).

Important items to consider:

- Switching capacity of the device
- Number of systems connected
- Uplink capacity

### 119.1. Single Switch

The single most important factor in this configuration is that the switching capacity of the hardware is capable of handling the traffic which can be generated by all systems connected to the switch. Some lower priced commodity hardware can have a slower switching capacity than could be utilized by a full switch.

### 119.2. Multiple Switches

Multiple switches are a potential pitfall in the architecture. The most common configuration of lower priced hardware is a simple 1Gbps uplink from one switch to another. This often overlooked pinch point can easily become a bottleneck for cluster communication. Especially with MapReduce jobs that are both reading and writing a lot of data the communication across this uplink could be saturated.

Mitigation of this issue is fairly simple and can be accomplished in multiple ways:

- Use appropriate hardware for the scale of the cluster which you’re attempting to build.
- Use larger single switch configurations i.e. single 48 port as opposed to 2x 24 port
- Configure port trunking for uplinks to utilize multiple interfaces to increase cross switch bandwidth.

### 119.3. Multiple Racks

Multiple rack configurations carry the same potential issues as multiple switches, and can suffer performance degradation from two main areas:

- Poor switch capacity performance
- Insufficient uplink to another rack

If the switches in your rack have appropriate switching capacity to handle all the hosts at full speed, the next most likely issue will be caused by homing more of your cluster across racks. The easiest way to avoid issues when spanning multiple racks is to use port trunking to create a bonded uplink to other racks. The downside of this method however, is in the overhead of ports that could potentially be used. An example of this is, creating an 8Gbps port channel from rack A to rack B, using 8 of your 24 ports to communicate between racks gives you a poor ROI, using too few however can mean you’re not getting the most out of your cluster.

Using 10Gbe links between racks will greatly increase performance, and assuming your switches support a 10Gbe uplink or allow for an expansion card will allow you to save your ports for machines as opposed to uplinks.

### 119.4. Network Interfaces

Are all the network interfaces functioning correctly? Are you sure? See the Troubleshooting Case Study in Case Study #1 (Performance Issue On A Single Node).

### 119.5. Network Consistency and Partition Tolerance

The CAP Theorem states that a distributed system can maintain two out of the following three characteristics: - *C*onsistency — all nodes see the same data. - *A*vailability — every request receives a response about whether it succeeded or failed. - *P*artition tolerance — the system continues to operate even if some of its components become unavailable to the others.

HBase favors consistency and partition tolerance, where a decision has to be made. Coda Hale explains why partition tolerance is so important, in http://codahale.com/you-cant-sacrifice-partition-tolerance/.

Robert Yokota used an automated testing framework called Jepson to test HBase’s partition tolerance in the face of network partitions, using techniques modeled after Aphyr’s Call Me Maybe series. The results, available as a blog post and an addendum, show that HBase performs correctly.


## 120. Java

### 120.1. The Garbage Collector and Apache HBase

#### 120.1.1. Long GC pauses

In his presentation, Avoiding Full GCs with MemStore-Local Allocation Buffers, Todd Lipcon describes two cases of stop-the-world garbage collections common in HBase, especially during loading; CMS failure modes and old generation heap fragmentation brought.

To address the first, start the CMS earlier than default by adding `-XX:CMSInitiatingOccupancyFraction` and setting it down from defaults. Start at 60 or 70 percent (The lower you bring down the threshold, the more GCing is done, the more CPU used). To address the second fragmentation issue, Todd added an experimental facility, (MSLAB), that must be explicitly enabled in Apache HBase 0.90.x (It’s defaulted to be *on* in Apache 0.92.x HBase). Set `hbase.hregion.memstore.mslab.enabled` to true in your `Configuration`. See the cited slides for background and detail. The latest JVMs do better regards fragmentation so make sure you are running a recent release. Read down in the message, Identifying concurrent mode failures caused by fragmentation. Be aware that when enabled, each MemStore instance will occupy at least an MSLAB instance of memory. If you have thousands of regions or lots of regions each with many column families, this allocation of MSLAB may be responsible for a good portion of your heap allocation and in an extreme case cause you to OOME. Disable MSLAB in this case, or lower the amount of memory it uses or float less regions per server.

If you have a write-heavy workload, check out HBASE-8163 MemStoreChunkPool: An improvement for JAVA GC when using MSLAB. It describes configurations to lower the amount of young GC during write-heavy loadings. If you do not have HBASE-8163 installed, and you are trying to improve your young GC times, one trick to consider — courtesy of our Liang Xie — is to set the GC config `-XX:PretenureSizeThreshold` in *hbase-env.sh* to be just smaller than the size of `hbase.hregion.memstore.mslab.chunksize` so MSLAB allocations happen in the tenured space directly rather than first in the young gen. You’d do this because these MSLAB allocations are going to likely make it to the old gen anyways and rather than pay the price of a copies between s0 and s1 in eden space followed by the copy up from young to old gen after the MSLABs have achieved sufficient tenure, save a bit of YGC churn and allocate in the old gen directly.

Other sources of long GCs can be the JVM itself logging. See Eliminating Large JVM GC Pauses Caused by Background IO Traffic

For more information about GC logs, see JVM Garbage Collection Logs.

Consider also enabling the off-heap Block Cache. This has been shown to mitigate GC pause times. See Block Cache


## 121. HBase Configurations

See Recommended Configurations.

### 121.1. Improving the 99th Percentile

Try hedged_reads.

### 121.2. Managing Compactions

For larger systems, managing compactions and splits may be something you want to consider.

### 121.3. `hbase.regionserver.handler.count`

See [hbase.regionserver.handler.count].

### 121.4. `hfile.block.cache.size`

See [hfile.block.cache.size]. A memory setting for the RegionServer process.

### 121.5. Prefetch Option for Blockcache

HBASE-9857 adds a new option to prefetch HFile contents when opening the BlockCache, if a Column family or RegionServer property is set. This option is available for HBase 0.98.3 and later. The purpose is to warm the BlockCache as rapidly as possible after the cache is opened, using in-memory table data, and not counting the prefetching as cache misses. This is great for fast reads, but is not a good idea if the data to be preloaded will not fit into the BlockCache. It is useful for tuning the IO impact of prefetching versus the time before all data blocks are in cache.

To enable prefetching on a given column family, you can use HBase Shell or use the API.

Enable Prefetch Using HBase Shell

```
hbase> create 'MyTable', { NAME => 'myCF', PREFETCH_BLOCKS_ON_OPEN => 'true' }
```

Example 42. Enable Prefetch Using the API

```
HTableDescriptor tableDesc = new HTableDescriptor("myTable");
HColumnDescriptor cfDesc = new HColumnDescriptor("myCF");
cfDesc.setPrefetchBlocksOnOpen(true);
tableDesc.addFamily(cfDesc);
```

See the API documentation for CacheConfig.

To see prefetch in operation, enable TRACE level logging on `org.apache.hadoop.hbase.io.hfile.HFileReaderImpl` in hbase-2.0+ or on `org.apache.hadoop.hbase.io.hfile.HFileReaderV2` in earlier versions, hbase-1.x, of HBase.

### 121.6. `hbase.regionserver.global.memstore.size`

See [hbase.regionserver.global.memstore.size]. This memory setting is often adjusted for the RegionServer process depending on needs.

### 121.7. `hbase.regionserver.global.memstore.size.lower.limit`

See [hbase.regionserver.global.memstore.size.lower.limit]. This memory setting is often adjusted for the RegionServer process depending on needs.

### 121.8. `hbase.hstore.blockingStoreFiles`

See [hbase.hstore.blockingStoreFiles]. If there is blocking in the RegionServer logs, increasing this can help.

### 121.9. `hbase.hregion.memstore.block.multiplier`

See [hbase.hregion.memstore.block.multiplier]. If there is enough RAM, increasing this can help.

### 121.10. `hbase.regionserver.checksum.verify`

Have HBase write the checksum into the datablock and save having to do the checksum seek whenever you read.

See [hbase.regionserver.checksum.verify], [hbase.hstore.bytes.per.checksum] and [hbase.hstore.checksum.algorithm]. For more information see the release note on HBASE-5074 support checksums in HBase block cache.

### 121.11. Tuning `callQueue` Options

HBASE-11355 introduces several callQueue tuning mechanisms which can increase performance. See the JIRA for some benchmarking information.

To increase the number of callqueues, set `hbase.ipc.server.num.callqueue` to a value greater than `1`. To split the callqueue into separate read and write queues, set `hbase.ipc.server.callqueue.read.ratio` to a value between `0` and `1`. This factor weights the queues toward writes (if below .5) or reads (if above .5). Another way to say this is that the factor determines what percentage of the split queues are used for reads. The following examples illustrate some of the possibilities. Note that you always have at least one write queue, no matter what setting you use.

- The default value of `0` does not split the queue.
- A value of `.3` uses 30% of the queues for reading and 70% for writing. Given a value of `10` for `hbase.ipc.server.num.callqueue`, 3 queues would be used for reads and 7 for writes.
- A value of `.5` uses the same number of read queues and write queues. Given a value of `10` for `hbase.ipc.server.num.callqueue`, 5 queues would be used for reads and 5 for writes.
- A value of `.6` uses 60% of the queues for reading and 40% for writing. Given a value of `10` for `hbase.ipc.server.num.callqueue`, 6 queues would be used for reads and 4 for writes.
- A value of `1.0` uses one queue to process write requests, and all other queues process read requests. A value higher than `1.0` has the same effect as a value of `1.0`. Given a value of `10` for `hbase.ipc.server.num.callqueue`, 9 queues would be used for reads and 1 for writes.

You can also split the read queues so that separate queues are used for short reads (from Get operations) and long reads (from Scan operations), by setting the `hbase.ipc.server.callqueue.scan.ratio` option. This option is a factor between 0 and 1, which determine the ratio of read queues used for Gets and Scans. More queues are used for Gets if the value is below `.5` and more are used for scans if the value is above `.5`. No matter what setting you use, at least one read queue is used for Get operations.

- A value of `0` does not split the read queue.
- A value of `.3` uses 70% of the read queues for Gets and 30% for Scans. Given a value of `20` for `hbase.ipc.server.num.callqueue` and a value of `.5` for `hbase.ipc.server.callqueue.read.ratio`, 10 queues would be used for reads, out of those 10, 7 would be used for Gets and 3 for Scans.
- A value of `.5` uses half the read queues for Gets and half for Scans. Given a value of `20` for `hbase.ipc.server.num.callqueue` and a value of `.5` for `hbase.ipc.server.callqueue.read.ratio`, 10 queues would be used for reads, out of those 10, 5 would be used for Gets and 5 for Scans.
- A value of `.7` uses 30% of the read queues for Gets and 70% for Scans. Given a value of `20` for `hbase.ipc.server.num.callqueue` and a value of `.5` for `hbase.ipc.server.callqueue.read.ratio`, 10 queues would be used for reads, out of those 10, 3 would be used for Gets and 7 for Scans.
- A value of `1.0` uses all but one of the read queues for Scans. Given a value of `20` for `hbase.ipc.server.num.callqueue` and a value of`.5` for `hbase.ipc.server.callqueue.read.ratio`, 10 queues would be used for reads, out of those 10, 1 would be used for Gets and 9 for Scans.

You can use the new option `hbase.ipc.server.callqueue.handler.factor` to programmatically tune the number of queues:

- A value of `0` uses a single shared queue between all the handlers.
- A value of `1` uses a separate queue for each handler.
- A value between `0` and `1` tunes the number of queues against the number of handlers. For instance, a value of `.5` shares one queue between each two handlers. Having more queues, such as in a situation where you have one queue per handler, reduces contention when adding a task to a queue or selecting it from a queue. The trade-off is that if you have some queues with long-running tasks, a handler may end up waiting to execute from that queue rather than processing another queue which has waiting tasks.

For these values to take effect on a given RegionServer, the RegionServer must be restarted. These parameters are intended for testing purposes and should be used carefully.


## 122. ZooKeeper

See ZooKeeper for information on configuring ZooKeeper, and see the part about having a dedicated disk.


## 123. Schema Design

### 123.1. Number of Column Families

See On the number of column families.

### 123.2. Key and Attribute Lengths

See Try to minimize row and column sizes. See also However… for compression caveats.

### 123.3. Table RegionSize

The regionsize can be set on a per-table basis via `setMaxFileSize` on TableDescriptorBuilder in the event where certain tables require different regionsizes than the configured default regionsize.

See Determining region count and size for more information.

### 123.4. Bloom Filters

A Bloom filter, named for its creator, Burton Howard Bloom, is a data structure which is designed to predict whether a given element is a member of a set of data. A positive result from a Bloom filter is not always accurate, but a negative result is guaranteed to be accurate. Bloom filters are designed to be "accurate enough" for sets of data which are so large that conventional hashing mechanisms would be impractical. For more information about Bloom filters in general, refer to http://en.wikipedia.org/wiki/Bloom_filter.

In terms of HBase, Bloom filters provide a lightweight in-memory structure to reduce the number of disk reads for a given Get operation (Bloom filters do not work with Scans) to only the StoreFiles likely to contain the desired Row. The potential performance gain increases with the number of parallel reads.

The Bloom filters themselves are stored in the metadata of each HFile and never need to be updated. When an HFile is opened because a region is deployed to a RegionServer, the Bloom filter is loaded into memory.

HBase includes some tuning mechanisms for folding the Bloom filter to reduce the size and keep the false positive rate within a desired range.

Bloom filters were introduced in HBASE-1200. Since HBase 0.96, row-based Bloom filters are enabled by default. (HBASE-8450)

For more information on Bloom filters in relation to HBase, see Bloom Filters for more information, or the following Quora discussion: How are bloom filters used in HBase?.

#### 123.4.1. When To Use Bloom Filters

Since HBase 0.96, row-based Bloom filters are enabled by default. You may choose to disable them or to change some tables to use row+column Bloom filters, depending on the characteristics of your data and how it is loaded into HBase.

To determine whether Bloom filters could have a positive impact, check the value of `blockCacheHitRatio` in the RegionServer metrics. If Bloom filters are enabled, the value of `blockCacheHitRatio` should increase, because the Bloom filter is filtering out blocks that are definitely not needed.

You can choose to enable Bloom filters for a row or for a row+column combination. If you generally scan entire rows, the row+column combination will not provide any benefit. A row-based Bloom filter can operate on a row+column Get, but not the other way around. However, if you have a large number of column-level Puts, such that a row may be present in every StoreFile, a row-based filter will always return a positive result and provide no benefit. Unless you have one column per row, row+column Bloom filters require more space, in order to store more keys. Bloom filters work best when the size of each data entry is at least a few kilobytes in size.

Overhead will be reduced when your data is stored in a few larger StoreFiles, to avoid extra disk IO during low-level scans to find a specific row.

Bloom filters need to be rebuilt upon deletion, so may not be appropriate in environments with a large number of deletions.

#### 123.4.2. Enabling Bloom Filters

Bloom filters are enabled on a Column Family. You can do this by using the setBloomFilterType method of HColumnDescriptor or using the HBase API. Valid values are `NONE`, `ROW` (default), or `ROWCOL`. See When To Use Bloom Filters for more information on `ROW` versus `ROWCOL`. See also the API documentation for ColumnFamilyDescriptorBuilder.

The following example creates a table and enables a ROWCOL Bloom filter on the `colfam1` column family.

```
hbase> create 'mytable',{NAME => 'colfam1', BLOOMFILTER => 'ROWCOL'}
```

#### 123.4.3. Configuring Server-Wide Behavior of Bloom Filters

You can configure the following settings in the *hbase-site.xml*.

| Parameter | Default | Description |
|---|---|---|
| io.storefile.bloom.enabled | yes | Set to no to kill bloom filters server-wide if something goes wrong |
| io.storefile.bloom.error.rate | .01 | The average false positive rate for bloom filters. Folding is used to maintain the false positive rate. Expressed as a decimal representation of a percentage. |
| io.storefile.bloom.max.fold | 7 | The guaranteed maximum fold rate. Changing this setting should not be necessary and is not recommended. |
| io.storefile.bloom.max.keys | 128000000 | For default (single-block) Bloom filters, this specifies the maximum number of keys. |
| io.storefile.delete.family.bloom.enabled | true | Master switch to enable Delete Family Bloom filters and store them in the StoreFile. |
| io.storefile.bloom.block.size | 131072 | Target Bloom block size. Bloom filter blocks of approximately this size are interleaved with data blocks. |
| hfile.block.bloom.cacheonwrite | false | Enables cache-on-write for inline blocks of a compound Bloom filter. |

### 123.5. ColumnFamily BlockSize

The blocksize can be configured for each ColumnFamily in a table, and defaults to 64k. Larger cell values require larger blocksizes. There is an inverse relationship between blocksize and the resulting StoreFile indexes (i.e., if the blocksize is doubled then the resulting indexes should be roughly halved).

See ColumnFamilyDescriptorBuilder and Storefor more information.

### 123.6. In-Memory ColumnFamilies

ColumnFamilies can optionally be defined as in-memory. Data is still persisted to disk, just like any other ColumnFamily. In-memory blocks have the highest priority in the Block Cache, but it is not a guarantee that the entire table will be in memory.

See ColumnFamilyDescriptorBuilder for more information.

### 123.7. Compression

Production systems should use compression with their ColumnFamily definitions. See Compression and Data Block Encoding In HBase for more information.

#### 123.7.1. However…

Compression deflates data *on disk*. When it’s in-memory (e.g., in the MemStore) or on the wire (e.g., transferring between RegionServer and Client) it’s inflated. So while using ColumnFamily compression is a best practice, but it’s not going to completely eliminate the impact of over-sized Keys, over-sized ColumnFamily names, or over-sized Column names.

See Try to minimize row and column sizes on for schema design tips, and KeyValue for more information on HBase stores data internally.


## 124. HBase General Patterns

### 124.1. Constants

When people get started with HBase they have a tendency to write code that looks like this:

```
Get get = new Get(rowkey);
Result r = table.get(get);
byte[] b = r.getValue(Bytes.toBytes("cf"), Bytes.toBytes("attr"));  
```

But especially when inside loops (and MapReduce jobs), converting the columnFamily and column-names to byte-arrays repeatedly is surprisingly expensive. It’s better to use constants for the byte-arrays, like this:

```
public static final byte[] CF = "cf".getBytes();
public static final byte[] ATTR = "attr".getBytes();
...
Get get = new Get(rowkey);
Result r = table.get(get);
byte[] b = r.getValue(CF, ATTR);  
```
