---
title: "Apache HBase® Reference Guide (part 1/41)"
source: https://hbase.apache.org/book.html
domain: apache-hbase
license: CC-BY-SA-4.0
tags: apache hbase, bigtable clone, wide-column store, apache hadoop
fetched: 2026-07-02
part: 1/41
---

## Preface

This is the official reference guide for the HBase version it ships with.

Herein you will find either the definitive documentation on an HBase topic as of its standing when the referenced HBase version shipped, or it will point to the location in Javadoc or JIRA where the pertinent information can be found.

About This Guide

This reference guide is a work in progress. The source for this guide can be found in the _src/main/asciidoc directory of the HBase source. This reference guide is marked up using AsciiDoc from which the finished guide is generated as part of the 'site' build target. Run

```
mvn site
```

to generate this documentation. Amendments and improvements to the documentation are welcomed. Click this link to file a new documentation bug against Apache HBase with some values pre-selected.

Contributing to the Documentation

For an overview of AsciiDoc and suggestions to get started contributing to the documentation, see the relevant section later in this documentation.

Heads-up if this is your first foray into the world of distributed computing…

If this is your first foray into the wonderful world of Distributed Computing, then you are in for some interesting times. First off, distributed systems are hard; making a distributed system hum requires a disparate skillset that spans systems (hardware and software) and networking.

Your cluster’s operation can hiccup because of any of a myriad set of reasons from bugs in HBase itself through misconfigurations — misconfiguration of HBase but also operating system misconfigurations — through to hardware problems whether it be a bug in your network card drivers or an underprovisioned RAM bus (to mention two recent examples of hardware issues that manifested as "HBase is slow"). You will also need to do a recalibration if up to this your computing has been bound to a single box. Here is one good starting point: Fallacies of Distributed Computing.

That said, you are welcome. It’s a fun place to be. Yours, the HBase Community.

Reporting Bugs

Please use JIRA to report non-security-related bugs.

To protect existing HBase installations from new vulnerabilities, please **do not** use JIRA to report security-related bugs. Instead, send your report to the mailing list private@hbase.apache.org, which allows anyone to send messages, but restricts who can read them. Someone on that list will contact you to follow up on your report.

Support and Testing Expectations

The phrases /supported/, /not supported/, /tested/, and /not tested/ occur several places throughout this guide. In the interest of clarity, here is a brief explanation of what is generally meant by these phrases, in the context of HBase.

|   | Commercial technical support for Apache HBase is provided by many Hadoop vendors. This is not the sense in which the term /support/ is used in the context of the Apache HBase project. The Apache HBase team assumes no responsibility for your HBase clusters, your configuration, or your data. |
|---|---|

**Supported**

In the context of Apache HBase, /supported/ means that HBase is designed to work in the way described, and deviation from the defined behavior or functionality should be reported as a bug.

**Not Supported**

In the context of Apache HBase, /not supported/ means that a use case or use pattern is not expected to work and should be considered an antipattern. If you think this designation should be reconsidered for a given feature or use pattern, file a JIRA or start a discussion on one of the mailing lists.

**Tested**

In the context of Apache HBase, /tested/ means that a feature is covered by unit or integration tests, and has been proven to work as expected.

**Not Tested**

In the context of Apache HBase, /not tested/ means that a feature or use pattern may or may not work in a given way, and may or may not corrupt your data or cause operational issues. It is an unknown, and there are no guarantees. If you can provide proof that a feature designated as /not tested/ does work in a given way, please submit the tests and/or the metrics so that other users can gain certainty about such features or use patterns.

# Getting Started


## 1. Introduction

Quickstart will get you up and running on a single-node, standalone instance of HBase.


## 2. Quick Start - Standalone HBase

This section describes the setup of a single-node standalone HBase. A *standalone* instance has all HBase daemons — the Master, RegionServers, and ZooKeeper — running in a single JVM persisting to the local filesystem. It is our most basic deploy profile. We will show you how to create a table in HBase using the `hbase shell` CLI, insert rows into the table, perform put and scan operations against the table, enable or disable the table, and start and stop HBase.

Apart from downloading HBase, this procedure should take less than 10 minutes.

### 2.1. JDK Version Requirements

HBase requires that a JDK be installed. See Java for information about supported JDK versions.

### 2.2. Get Started with HBase

Procedure: Download, Configure, and Start HBase in Standalone Mode

1. Choose a download site from this list of Apache Download Mirrors. Click on the suggested top link. This will take you to a mirror of *HBase Releases*. Click on the folder named *stable* and then download the binary file that ends in *.tar.gz* to your local filesystem. Do not download the file ending in *src.tar.gz* for now.
2. Extract the downloaded file, and change to the newly-created directory. `$ tar xzvf hbase-4.0.0-alpha-1-SNAPSHOT-bin.tar.gz $ cd hbase-4.0.0-alpha-1-SNAPSHOT/`
3. You must set the `JAVA_HOME` environment variable before starting HBase. To make this easier, HBase lets you set it within the *conf/hbase-env.sh* file. You must locate where Java is installed on your machine, and one way to find this is by using the *whereis java* command. Once you have the location, edit the *conf/hbase-env.sh* file and uncomment the line starting with *#export JAVA_HOME=*, and then set it to your Java installation path. Example extract from *hbase-env.sh* where *JAVA_HOME* is set # Set environment variables here. # The java implementation to use. export JAVA_HOME=/usr/jdk64/jdk1.8.0_112
4. The *bin/start-hbase.sh* script is provided as a convenient way to start HBase. Issue the command, and if all goes well, a message is logged to standard output showing that HBase started successfully. You can use the `jps` command to verify that you have one running process called `HMaster`. In standalone mode HBase runs all daemons within this single JVM, i.e. the HMaster, a single HRegionServer, and the ZooKeeper daemon. Go to *http://localhost:16010* to view the HBase Web UI.

Procedure: Use HBase For the First Time

1. Connect to HBase. Connect to your running instance of HBase using the `hbase shell` command, located in the *bin/* directory of your HBase install. In this example, some usage and version information that is printed when you start HBase Shell has been omitted. The HBase Shell prompt ends with a `>` character. `$ ./bin/hbase shell hbase(main):001:0>`
2. Display HBase Shell Help Text. Type `help` and press Enter, to display some basic usage information for HBase Shell, as well as several example commands. Notice that table names, rows, columns all must be enclosed in quote characters.
3. Create a table. Use the `create` command to create a new table. You must specify the table name and the ColumnFamily name. `hbase(main):001:0> create 'test', 'cf' 0 row(s) in 0.4170 seconds => Hbase::Table - test`
4. List Information About your Table Use the `list` command to confirm your table exists `hbase(main):002:0> list 'test' TABLE test 1 row(s) in 0.0180 seconds => ["test"]` Now use the `describe` command to see details, including configuration defaults `hbase(main):003:0> describe 'test' Table test is ENABLED test COLUMN FAMILIES DESCRIPTION {NAME => 'cf', VERSIONS => '1', EVICT_BLOCKS_ON_CLOSE => 'false', NEW_VERSION_BEHAVIOR => 'false', KEEP_DELETED_CELLS => 'FALSE', CACHE_DATA_ON_WRITE => 'false', DATA_BLOCK_ENCODING => 'NONE', TTL => 'FOREVER', MIN_VERSIONS => '0', REPLICATION_SCOPE => '0', BLOOMFILTER => 'ROW', CACHE_INDEX_ON_WRITE => 'f alse', IN_MEMORY => 'false', CACHE_BLOOMS_ON_WRITE => 'false', PREFETCH_BLOCKS_ON_OPEN => 'false', COMPRESSION => 'NONE', BLOCKCACHE => 'true', BLOCKSIZE => '65536'} 1 row(s) Took 0.9998 seconds`
5. Put data into your table. To put data into your table, use the `put` command. `hbase(main):003:0> put 'test', 'row1', 'cf:a', 'value1' 0 row(s) in 0.0850 seconds hbase(main):004:0> put 'test', 'row2', 'cf:b', 'value2' 0 row(s) in 0.0110 seconds hbase(main):005:0> put 'test', 'row3', 'cf:c', 'value3' 0 row(s) in 0.0100 seconds` Here, we insert three values, one at a time. The first insert is at `row1`, column `cf:a`, with a value of `value1`. Columns in HBase are comprised of a column family prefix, `cf` in this example, followed by a colon and then a column qualifier suffix, `a` in this case.
6. Scan the table for all data at once. One of the ways to get data from HBase is to scan. Use the `scan` command to scan the table for data. You can limit your scan, but for now, all data is fetched. `hbase(main):006:0> scan 'test' ROW COLUMN+CELL row1 column=cf:a, timestamp=1421762485768, value=value1 row2 column=cf:b, timestamp=1421762491785, value=value2 row3 column=cf:c, timestamp=1421762496210, value=value3 3 row(s) in 0.0230 seconds`
7. Get a single row of data. To get a single row of data at a time, use the `get` command. `hbase(main):007:0> get 'test', 'row1' COLUMN CELL cf:a timestamp=1421762485768, value=value1 1 row(s) in 0.0350 seconds`
8. Disable a table. If you want to delete a table or change its settings, as well as in some other situations, you need to disable the table first, using the `disable` command. You can re-enable it using the `enable` command. `hbase(main):008:0> disable 'test' 0 row(s) in 1.1820 seconds hbase(main):009:0> enable 'test' 0 row(s) in 0.1770 seconds` Disable the table again if you tested the `enable` command above: `hbase(main):010:0> disable 'test' 0 row(s) in 1.1820 seconds`
9. Drop the table. To drop (delete) a table, use the `drop` command. `hbase(main):011:0> drop 'test' 0 row(s) in 0.1370 seconds`
10. Exit the HBase Shell. To exit the HBase Shell and disconnect from your cluster, use the `quit` command. HBase is still running in the background.

Procedure: Stop HBase

1. In the same way that the *bin/start-hbase.sh* script is provided to conveniently start all HBase daemons, the *bin/stop-hbase.sh* script stops them. `$ ./bin/stop-hbase.sh stopping hbase.................... $`
2. After issuing the command, it can take several minutes for the processes to shut down. Use the `jps` to be sure that the HMaster and HRegionServer processes are shut down.

The above has shown you how to start and stop a standalone instance of HBase. In the next sections we give a quick overview of other modes of hbase deploy.

### 2.3. Pseudo-Distributed for Local Testing

After working your way through quickstart standalone mode, you can re-configure HBase to run in pseudo-distributed mode. Pseudo-distributed mode means that HBase still runs completely on a single host, but each HBase daemon (HMaster, HRegionServer, and ZooKeeper) runs as a separate process: in standalone mode all daemons ran in one jvm process/instance. By default, unless you configure the `hbase.rootdir` property as described in quickstart, your data is still stored in */tmp/*. In this walk-through, we store your data in HDFS instead, assuming you have HDFS available. You can skip the HDFS configuration to continue storing your data in the local filesystem.

|   | Hadoop Configuration This procedure assumes that you have configured Hadoop and HDFS on your local system and/or a remote system, and that they are running and available. It also assumes you are using Hadoop 2. The guide on Setting up a Single Node Cluster in the Hadoop documentation is a good starting point. |
|---|---|

1. Stop HBase if it is running. If you have just finished quickstart and HBase is still running, stop it. This procedure will create a totally new directory where HBase will store its data, so any databases you created before will be lost.
2. Configure HBase. Edit the *hbase-site.xml* configuration. First, add the following property which directs HBase to run in distributed mode, with one JVM instance per daemon. `<property> <name>hbase.cluster.distributed</name> <value>true</value> </property>` Next, add a configuration for `hbase.rootdir`, pointing to the address of your HDFS instance, using the `hdfs:////` URI syntax. In this example, HDFS is running on the localhost at port 8020. `<property> <name>hbase.rootdir</name> <value>hdfs://localhost:9000/hbase</value> </property>` You do not need to create the directory in HDFS. HBase will do this for you. If you create the directory, HBase will attempt to do a migration, which is not what you want. Finally, remove existing configuration for `hbase.tmp.dir` and `hbase.unsafe.stream.capability.enforce`,
3. Start HBase. Use the *bin/start-hbase.sh* command to start HBase. If your system is configured correctly, the `jps` command should show the HMaster and HRegionServer processes running.
4. Check the HBase directory in HDFS. If everything worked correctly, HBase created its directory in HDFS. In the configuration above, it is stored in */hbase/* on HDFS. You can use the `hadoop fs` command in Hadoop’s *bin/* directory to list this directory. `$ ./bin/hadoop fs -ls /hbase Found 7 items drwxr-xr-x - hbase users 0 2014-06-25 18:58 /hbase/.tmp drwxr-xr-x - hbase users 0 2014-06-25 21:49 /hbase/WALs drwxr-xr-x - hbase users 0 2014-06-25 18:48 /hbase/corrupt drwxr-xr-x - hbase users 0 2014-06-25 18:58 /hbase/data -rw-r--r-- 3 hbase users 42 2014-06-25 18:41 /hbase/hbase.id -rw-r--r-- 3 hbase users 7 2014-06-25 18:41 /hbase/hbase.version drwxr-xr-x - hbase users 0 2014-06-25 21:49 /hbase/oldWALs`
5. Create a table and populate it with data. You can use the HBase Shell to create a table, populate it with data, scan and get values from it, using the same procedure as in shell exercises.
6. Start and stop a backup HBase Master (HMaster) server. Running multiple HMaster instances on the same hardware does not make sense in a production environment, in the same way that running a pseudo-distributed cluster does not make sense for production. This step is offered for testing and learning purposes only. The HMaster server controls the HBase cluster. You can start up to 9 backup HMaster servers, which makes 10 total HMasters, counting the primary. To start a backup HMaster, use the `local-master-backup.sh`. For each backup master you want to start, add a parameter representing the port offset for that master. Each HMaster uses two ports (16000 and 16010 by default). The port offset is added to these ports, so using an offset of 2, the backup HMaster would use ports 16002 and 16012. The following command starts 3 backup servers using ports 16002/16012, 16003/16013, and 16005/16015. `$ ./bin/local-master-backup.sh start 2 3 5` To kill a backup master without killing the entire cluster, you need to find its process ID (PID). The PID is stored in a file with a name like */tmp/hbase-USER-X-master.pid*. The only contents of the file is the PID. You can use the `kill -9` command to kill that PID. The following command will kill the master with port offset 1, but leave the cluster running: `$ cat /tmp/hbase-testuser-1-master.pid |xargs kill -9`
7. Start and stop additional RegionServers The HRegionServer manages the data in its StoreFiles as directed by the HMaster. Generally, one HRegionServer runs per node in the cluster. Running multiple HRegionServers on the same system can be useful for testing in pseudo-distributed mode. The `local-regionservers.sh` command allows you to run multiple RegionServers. It works in a similar way to the `local-master-backup.sh` command, in that each parameter you provide represents the port offset for an instance. Each RegionServer requires two ports, and the default ports are 16020 and 16030. Since HBase version 1.1.0, HMaster doesn’t use region server ports, this leaves 10 ports (16020 to 16029 and 16030 to 16039) to be used for RegionServers. For supporting additional RegionServers, set environment variables HBASE_RS_BASE_PORT and HBASE_RS_INFO_BASE_PORT to appropriate values before running script `local-regionservers.sh`. e.g. With values 16200 and 16300 for base ports, 99 additional RegionServers can be supported, on a server. The following command starts four additional RegionServers, running on sequential ports starting at 16022/16032 (base ports 16020/16030 plus 2). `$ ./bin/local-regionservers.sh start 2 3 4 5` To stop a RegionServer manually, use the `local-regionservers.sh` command with the `stop` parameter and the offset of the server to stop. `$ ./bin/local-regionservers.sh stop 3`
8. Stop HBase. You can stop HBase the same way as in the quickstart procedure, using the *bin/stop-hbase.sh* command.

### 2.4. Fully Distributed for Production

In reality, you need a fully-distributed configuration to fully test HBase and to use it in real-world scenarios. In a distributed configuration, the cluster contains multiple nodes, each of which runs one or more HBase daemon. These include primary and backup Master instances, multiple ZooKeeper nodes, and multiple RegionServer nodes.

This advanced quickstart adds two more nodes to your cluster. The architecture will be as follows:

| Node Name | Master | ZooKeeper | RegionServer |
|---|---|---|---|
| node-a.example.com | yes | yes | no |
| node-b.example.com | backup | yes | yes |
| node-c.example.com | no | yes | yes |

This quickstart assumes that each node is a virtual machine and that they are all on the same network. It builds upon the previous quickstart, Pseudo-Distributed for Local Testing, assuming that the system you configured in that procedure is now `node-a`. Stop HBase on `node-a` before continuing.

|   | Be sure that all the nodes have full access to communicate, and that no firewall rules are in place which could prevent them from talking to each other. If you see any errors like `no route to host`, check your firewall. |
|---|---|

Procedure: Configure Passwordless SSH Access

`node-a` needs to be able to log into `node-b` and `node-c` (and to itself) in order to start the daemons. The easiest way to accomplish this is to use the same username on all hosts, and configure password-less SSH login from `node-a` to each of the others.

1. On `node-a`, generate a key pair. While logged in as the user who will run HBase, generate a SSH key pair, using the following command: `$ ssh-keygen -t rsa` If the command succeeds, the location of the key pair is printed to standard output. The default name of the public key is *id_rsa.pub*.
2. Create the directory that will hold the shared keys on the other nodes. On `node-b` and `node-c`, log in as the HBase user and create a *.ssh/* directory in the user’s home directory, if it does not already exist. If it already exists, be aware that it may already contain other keys.
3. Copy the public key to the other nodes. Securely copy the public key from `node-a` to each of the nodes, by using the `scp` or some other secure means. On each of the other nodes, create a new file called *.ssh/authorized_keys* *if it does not already exist*, and append the contents of the *id_rsa.pub* file to the end of it. Note that you also need to do this for `node-a` itself. `$ cat id_rsa.pub >> ~/.ssh/authorized_keys`
4. Test password-less login. If you performed the procedure correctly, you should not be prompted for a password when you SSH from `node-a` to either of the other nodes using the same username.
5. Since `node-b` will run a backup Master, repeat the procedure above, substituting `node-b` everywhere you see `node-a`. Be sure not to overwrite your existing *.ssh/authorized_keys* files, but concatenate the new key onto the existing file using the `>>` operator rather than the `>` operator.

Procedure: Prepare

node-a

`node-a` will run your primary master and ZooKeeper processes, but no RegionServers. Stop the RegionServer from starting on `node-a`.

1. Edit *conf/regionservers* and remove the line which contains `localhost`. Add lines with the hostnames or IP addresses for `node-b` and `node-c`. Even if you did want to run a RegionServer on `node-a`, you should refer to it by the hostname the other servers would use to communicate with it. In this case, that would be `node-a.example.com`. This enables you to distribute the configuration to each node of your cluster any hostname conflicts. Save the file.
2. Configure HBase to use `node-b` as a backup master. Create a new file in *conf/* called *backup-masters*, and add a new line to it with the hostname for `node-b`. In this demonstration, the hostname is `node-b.example.com`.
3. Configure ZooKeeper In reality, you should carefully consider your ZooKeeper configuration. You can find out more about configuring ZooKeeper in zookeeper section. This configuration will direct HBase to start and manage a ZooKeeper instance on each node of the cluster. On `node-a`, edit *conf/hbase-site.xml* and add the following properties. `<property> <name>hbase.zookeeper.quorum</name> <value>node-a.example.com,node-b.example.com,node-c.example.com</value> </property> <property> <name>hbase.zookeeper.property.dataDir</name> <value>/usr/local/zookeeper</value> </property>`
4. Everywhere in your configuration that you have referred to `node-a` as `localhost`, change the reference to point to the hostname that the other nodes will use to refer to `node-a`. In these examples, the hostname is `node-a.example.com`.

Procedure: Prepare

node-b

and

node-c

`node-b` will run a backup master server and a ZooKeeper instance.

1. Download and unpack HBase. Download and unpack HBase to `node-b`, just as you did for the standalone and pseudo-distributed quickstarts.
2. Copy the configuration files from `node-a` to `node-b`.and `node-c`. Each node of your cluster needs to have the same configuration information. Copy the contents of the *conf/* directory to the *conf/* directory on `node-b` and `node-c`.

Procedure: Start and Test Your Cluster

1. Be sure HBase is not running on any node. If you forgot to stop HBase from previous testing, you will have errors. Check to see whether HBase is running on any of your nodes by using the `jps` command. Look for the processes `HMaster`, `HRegionServer`, and `HQuorumPeer`. If they exist, kill them.
2. Start the cluster. On `node-a`, issue the `start-hbase.sh` command. Your output will be similar to that below. `$ bin/start-hbase.sh node-c.example.com: starting zookeeper, logging to /home/hbuser/hbase-0.98.3-hadoop2/bin/../logs/hbase-hbuser-zookeeper-node-c.example.com.out node-a.example.com: starting zookeeper, logging to /home/hbuser/hbase-0.98.3-hadoop2/bin/../logs/hbase-hbuser-zookeeper-node-a.example.com.out node-b.example.com: starting zookeeper, logging to /home/hbuser/hbase-0.98.3-hadoop2/bin/../logs/hbase-hbuser-zookeeper-node-b.example.com.out starting master, logging to /home/hbuser/hbase-0.98.3-hadoop2/bin/../logs/hbase-hbuser-master-node-a.example.com.out node-c.example.com: starting regionserver, logging to /home/hbuser/hbase-0.98.3-hadoop2/bin/../logs/hbase-hbuser-regionserver-node-c.example.com.out node-b.example.com: starting regionserver, logging to /home/hbuser/hbase-0.98.3-hadoop2/bin/../logs/hbase-hbuser-regionserver-node-b.example.com.out node-b.example.com: starting master, logging to /home/hbuser/hbase-0.98.3-hadoop2/bin/../logs/hbase-hbuser-master-nodeb.example.com.out` ZooKeeper starts first, followed by the master, then the RegionServers, and finally the backup masters.
3. Verify that the processes are running. On each node of the cluster, run the `jps` command and verify that the correct processes are running on each server. You may see additional Java processes running on your servers as well, if they are used for other purposes. `node-a` `jps` Output `$ jps 20355 Jps 20071 HQuorumPeer 20137 HMaster` `node-b` `jps` Output `$ jps 15930 HRegionServer 16194 Jps 15838 HQuorumPeer 16010 HMaster` `node-c` `jps` Output `$ jps 13901 Jps 13639 HQuorumPeer 13737 HRegionServer` ZooKeeper Process Name The `HQuorumPeer` process is a ZooKeeper instance which is controlled and started by HBase. If you use ZooKeeper this way, it is limited to one instance per cluster node and is appropriate for testing only. If ZooKeeper is run outside of HBase, the process is called `QuorumPeer`. For more about ZooKeeper configuration, including using an external ZooKeeper instance with HBase, see zookeeper section.
4. Browse to the Web UI. If everything is set up correctly, you should be able to connect to the UI for the Master `http://node-a.example.com:16010/` or the secondary master at `http://node-b.example.com:16010/` using a web browser. If you can connect via `localhost` but not from another host, check your firewall rules. You can see the web UI for each of the RegionServers at port 16030 of their IP addresses, or by clicking their links in the web UI for the Master.
5. Test what happens when nodes or services disappear. With a three-node cluster you have configured, things will not be very resilient. You can still test the behavior of the primary Master or a RegionServer by killing the associated processes and watching the logs.

### 2.5. Where to go next

The next chapter, configuration, gives more information about the different HBase run modes, system requirements for running HBase, and critical configuration areas for setting up a distributed HBase cluster.

# Apache HBase Configuration

This chapter expands upon the

Getting Started

chapter to further explain configuration of Apache HBase. Please read this chapter carefully, especially the

Basic Prerequisites

to ensure that your HBase testing and deployment goes smoothly. Familiarize yourself with

Support and Testing Expectations

as well.


## 3. Configuration Files

Apache HBase uses the same configuration system as Apache Hadoop. All configuration files are located in the *conf/* directory, which needs to be kept in sync for each node on your cluster.

HBase Configuration File Descriptions

***backup-masters***

Not present by default. A plain-text file which lists hosts on which the Master should start a backup Master process, one host per line.

***hadoop-metrics2-hbase.properties***

Used to connect HBase Hadoop’s Metrics2 framework. See the Hadoop Wiki entry for more information on Metrics2. Contains only commented-out examples by default.

***hbase-env.cmd* and *hbase-env.sh***

Script for Windows and Linux / Unix environments to set up the working environment for HBase, including the location of Java, Java options, and other environment variables. The file contains many commented-out examples to provide guidance.

***hbase-policy.xml***

The default policy configuration file used by RPC servers to make authorization decisions on client requests. Only used if HBase security is enabled.

***hbase-site.xml***

The main HBase configuration file. This file specifies configuration options which override HBase’s default configuration. You can view (but do not edit) the default configuration file at *hbase-common/src/main/resources/hbase-default.xml*. You can also view the entire effective configuration for your cluster (defaults and overrides) in the HBase Configuration tab of the HBase Web UI.

***log4j2.properties***

Configuration file for HBase logging via `log4j2`.

***regionservers***

A plain-text file containing a list of hosts which should run a RegionServer in your HBase cluster. By default, this file contains the single entry `localhost`. It should contain a list of hostnames or IP addresses, one per line, and should only contain `localhost` if each node in your cluster will run a RegionServer on its `localhost` interface.

|   | Checking XML Validity When you edit XML, it is a good idea to use an XML-aware editor to be sure that your syntax is correct and your XML is well-formed. You can also use the `xmllint` utility to check that your XML is well-formed. By default, `xmllint` re-flows and prints the XML to standard output. To check for well-formedness and only print output if errors exist, use the command `xmllint -noout filename.xml`. |
|---|---|

|   | Keep Configuration In Sync Across the Cluster When running in distributed mode, after you make an edit to an HBase configuration, make sure you copy the contents of the *conf/* directory to all nodes of the cluster. HBase will not do this for you. Use a configuration management tool for managing and copying the configuration files to your nodes. For most configurations, a restart is needed for servers to pick up changes. Dynamic configuration is an exception to this, to be described later below. |
|---|---|


## 4. Basic Prerequisites

This section lists required services and some required system configuration.

Java

HBase runs on the Java Virtual Machine, thus all HBase deployments require a JVM runtime.

The following table summarizes the recommendations of the HBase community with respect to running on various Java versions. The symbol indicates a base level of testing and willingness to help diagnose and address issues you might run into; these are the expected deployment combinations. An entry of means that there may be challenges with this combination, and you should look for more information before deciding to pursue this as your deployment strategy. The means this combination does not work; either an older Java version is considered deprecated by the HBase community, or this combination is known to not work. For combinations of newer JDK with older HBase releases, it’s likely there are known compatibility issues that cannot be addressed under our compatibility guarantees, making the combination impossible. In some cases, specific guidance on limitations (e.g. whether compiling / unit tests work, specific operational issues, etc) are also noted. Assume any combination not listed here is considered .

|   | Long-Term Support JDKs are Recommended HBase recommends downstream users rely only on JDK releases that are marked as Long-Term Supported (LTS), either from the OpenJDK project or vendors. At the time of this writing, the following JDK releases are NOT LTS releases and are NOT tested or advocated for use by the Apache HBase community: JDK9, JDK10, JDK12, JDK13, and JDK14. Community discussion around this decision is recorded on HBASE-20264. |
|---|---|

|   | HotSpot vs. OpenJ9 At this time, all testing performed by the Apache HBase project runs on the HotSpot variant of the JVM. When selecting your JDK distribution, please take this into consideration. |
|---|---|

| HBase Version | JDK 6 | JDK 7 | JDK 8 | JDK 11 | JDK 17 |
|---|---|---|---|---|---|
| HBase 2.6 |   |   |   |   |   |
| HBase 2.5 |   |   |   | * |   |
| HBase 2.4 |   |   |   |   |   |
| HBase 2.3 |   |   | * |   |   |
| HBase 2.0-2.2 |   |   |   |   |   |
| HBase 1.2+ |   |   |   |   |   |
| HBase 1.0-1.1 |   |   |   |   |   |
| HBase 0.98 |   |   |   |   |   |
| HBase 0.94 |   |   |   |   |   |

|   | A Note on JDK11/JDK17 * Preliminary support for JDK11 is introduced with HBase 2.3.0, and for JDK17 is introduced with HBase 2.5.x. We will compile and run test suites with JDK11/17 in pre commit checks and nightly checks. We will mark the support as as long as we have run some ITs with the JDK version and also there are users in the community use the JDK version in real production clusters. For JDK11/JDK17 support in HBase, please refer to HBASE-22972 and HBASE-26038 For JDK11/JDK17 support in Hadoop, which may also affect HBase, please refer to HADOOP-15338 and HADOOP-17177 |
|---|---|

|   | You must set `JAVA_HOME` on each node of your cluster. *hbase-env.sh* provides a handy mechanism to do this. |
|---|---|

Operating System Utilities

**ssh**

HBase uses the Secure Shell (ssh) command and utilities extensively to communicate between cluster nodes. Each server in the cluster must be running `ssh` so that the Hadoop and HBase daemons can be managed. You must be able to connect to all nodes via SSH, including the local node, from the Master as well as any backup Master, using a shared key rather than a password. You can see the basic methodology for such a set-up in Linux or Unix systems at "Procedure: Configure Passwordless SSH Access". If your cluster nodes use OS X, see the section, SSH: Setting up Remote Desktop and Enabling Self-Login on the Hadoop wiki.

**DNS**

HBase uses the local hostname to self-report its IP address.

**NTP**

The clocks on cluster nodes should be synchronized. A small amount of variation is acceptable, but larger amounts of skew can cause erratic and unexpected behavior. Time synchronization is one of the first things to check if you see unexplained problems in your cluster. It is recommended that you run a Network Time Protocol (NTP) service, or another time-synchronization mechanism on your cluster and that all nodes look to the same service for time synchronization. See the Basic NTP Configuration at *The Linux Documentation Project (TLDP)* to set up NTP.

**Limits on Number of Files and Processes (ulimit)**

Apache HBase is a database. It requires the ability to open a large number of files at once. Many Linux distributions limit the number of files a single user is allowed to open to `1024` (or `256` on older versions of OS X). You can check this limit on your servers by running the command `ulimit -n` when logged in as the user which runs HBase. See the Troubleshooting section for some of the problems you may experience if the limit is too low. You may also notice errors such as the following:

```
2010-04-06 03:04:37,542 INFO org.apache.hadoop.hdfs.DFSClient: Exception increateBlockOutputStream java.io.EOFException
2010-04-06 03:04:37,542 INFO org.apache.hadoop.hdfs.DFSClient: Abandoning block blk_-6935524980745310745_1391901
```

It is recommended to raise the ulimit to at least 10,000, but more likely 10,240, because the value is usually expressed in multiples of 1024. Each ColumnFamily has at least one StoreFile, and possibly more than six StoreFiles if the region is under load. The number of open files required depends upon the number of ColumnFamilies and the number of regions. The following is a rough formula for calculating the potential number of open files on a RegionServer.

Calculate the Potential Number of Open Files

```
(StoreFiles per ColumnFamily) x (regions per RegionServer)
```

For example, assuming that a schema had 3 ColumnFamilies per region with an average of 3 StoreFiles per ColumnFamily, and there are 100 regions per RegionServer, the JVM will open `3 * 3 * 100 = 900` file descriptors, not counting open JAR files, configuration files, and others. Opening a file does not take many resources, and the risk of allowing a user to open too many files is minimal.

Another related setting is the number of processes a user is allowed to run at once. In Linux and Unix, the number of processes is set using the `ulimit -u` command. This should not be confused with the `nproc` command, which controls the number of CPUs available to a given user. Under load, a `ulimit -u` that is too low can cause OutOfMemoryError exceptions.

Configuring the maximum number of file descriptors and processes for the user who is running the HBase process is an operating system configuration, rather than an HBase configuration. It is also important to be sure that the settings are changed for the user that actually runs HBase. To see which user started HBase, and that user’s ulimit configuration, look at the first line of the HBase log for that instance.

Example 1.

ulimit

Settings on Ubuntu

To configure ulimit settings on Ubuntu, edit */etc/security/limits.conf*, which is a space-delimited file with four columns. Refer to the man page for *limits.conf* for details about the format of this file. In the following example, the first line sets both soft and hard limits for the number of open files (nofile) to 32768 for the operating system user with the username hadoop. The second line sets the number of processes to 32000 for the same user.

```
hadoop  -       nofile  32768
hadoop  -       nproc   32000
```

The settings are only applied if the Pluggable Authentication Module (PAM) environment is directed to use them. To configure PAM to use these limits, be sure that the */etc/pam.d/common-session* file contains the following line:

```
session required  pam_limits.so
```

**Linux Shell**

All of the shell scripts that come with HBase rely on the GNU Bash shell.

**Windows**

Running production systems on Windows machines is not recommended.

### 4.1. Hadoop

The following table summarizes the versions of Hadoop supported with each version of HBase. Older versions not appearing in this table are considered unsupported and likely missing necessary features, while newer versions are untested but may be suitable.

Based on the version of HBase, you should select the most appropriate version of Hadoop. You can use Apache Hadoop, or a vendor’s distribution of Hadoop. No distinction is made here. See the Hadoop wiki for information about vendors of Hadoop.

|   | Hadoop 3.x is recommended. Comparing to Hadoop 1.x, Hadoop 2.x is faster and includes features, such as short-circuit reads (see Leveraging local data), which will help improve your HBase random read profile. Hadoop 2.x also includes important bug fixes that will improve your overall HBase experience. HBase does not support running with earlier versions of Hadoop. See the table below for requirements specific to different HBase versions. Today, Hadoop 3.x is recommended as the last Hadoop 2.x release 2.10.2 was released years ago, and there is no release for Hadoop 2.x for a very long time, although the Hadoop community does not officially EOL Hadoop 2.x yet. |
|---|---|

Use the following legend to interpret these tables:

- = Tested to be fully-functional
- = Known to not be fully-functional, or there are CVEs so we drop the support in newer minor releases
- = Not tested, may/may-not function

|   | HBase-2.5.x | HBase-2.6.x |
|---|---|---|
| Hadoop-2.10.[0-1] |   |   |
| Hadoop-2.10.2+ |   |   |
| Hadoop-3.1.0 |   |   |
| Hadoop-3.1.1+ |   |   |
| Hadoop-3.2.[0-2] |   |   |
| Hadoop-3.2.3+ |   |   |
| Hadoop-3.3.[0-1] |   |   |
| Hadoop-3.3.[2-4] |   |   |
| Hadoop-3.3.5+ |   |   |
| Hadoop-3.4.0+ | (2.5.11+) | (2.6.2+) |

|   | HBase-2.3.x | HBase-2.4.x |
|---|---|---|
| Hadoop-2.10.x |   |   |
| Hadoop-3.1.0 |   |   |
| Hadoop-3.1.1+ |   |   |
| Hadoop-3.2.x |   |   |
| Hadoop-3.3.x |   |   |

|   | HBase-2.0.x | HBase-2.1.x | HBase-2.2.x |
|---|---|---|---|
| Hadoop-2.6.1+ |   |   |   |
| Hadoop-2.7.[0-6] |   |   |   |
| Hadoop-2.7.7+ |   |   |   |
| Hadoop-2.8.[0-2] |   |   |   |
| Hadoop-2.8.[3-4] |   |   |   |
| Hadoop-2.8.5+ |   |   |   |
| Hadoop-2.9.[0-1] |   |   |   |
| Hadoop-2.9.2+ |   |   |   |
| Hadoop-3.0.[0-2] |   |   |   |
| Hadoop-3.0.3+ |   |   |   |
| Hadoop-3.1.0 |   |   |   |
| Hadoop-3.1.1+ |   |   |   |

|   | HBase-1.5.x | HBase-1.6.x | HBase-1.7.x |
|---|---|---|---|
| Hadoop-2.7.7+ |   |   |   |
| Hadoop-2.8.[0-4] |   |   |   |
| Hadoop-2.8.5+ |   |   |   |
| Hadoop-2.9.[0-1] |   |   |   |
| Hadoop-2.9.2+ |   |   |   |
| Hadoop-2.10.x |   |   |   |

|   | HBase-1.0.x (Hadoop 1.x is NOT supported) | HBase-1.1.x | HBase-1.2.x | HBase-1.3.x | HBase-1.4.x |
|---|---|---|---|---|---|
| Hadoop-2.4.x |   |   |   |   |   |
| Hadoop-2.5.x |   |   |   |   |   |
| Hadoop-2.6.0 |   |   |   |   |   |
| Hadoop-2.6.1+ |   |   |   |   |   |
| Hadoop-2.7.0 |   |   |   |   |   |
| Hadoop-2.7.1+ |   |   |   |   |   |

|   | HBase-0.92.x | HBase-0.94.x | HBase-0.96.x | HBase-0.98.x (Support for Hadoop 1.1+ is deprecated.) |
|---|---|---|---|---|
| Hadoop-0.20.205 |   |   |   |   |
| Hadoop-0.22.x |   |   |   |   |
| Hadoop-1.0.x |   |   |   |   |
| Hadoop-1.1.x |   |   |   |   |
| Hadoop-0.23.x |   |   |   |   |
| Hadoop-2.0.x-alpha |   |   |   |   |
| Hadoop-2.1.0-beta |   |   |   |   |
| Hadoop-2.2.0 |   |   |   |   |
| Hadoop-2.3.x |   |   |   |   |
| Hadoop-2.4.x |   |   |   |   |
| Hadoop-2.5.x |   |   |   |   |

|   | Hadoop 2.y.0 Releases Starting around the time of Hadoop version 2.7.0, the Hadoop PMC got into the habit of calling out new minor releases on their major version 2 release line as not stable / production ready. As such, HBase expressly advises downstream users to avoid running on top of these releases. Note that additionally the 2.8.1 release was given the same caveat by the Hadoop PMC. For reference, see the release announcements for Apache Hadoop 2.7.0, Apache Hadoop 2.8.0, Apache Hadoop 2.8.1, and Apache Hadoop 2.9.0. |
|---|---|

|   | Hadoop 3.1.0 Release The Hadoop PMC called out the 3.1.0 release as not stable / production ready. As such, HBase expressly advises downstream users to avoid running on top of this release. For reference, see the release announcement for Hadoop 3.1.0. |
|---|---|

|   | Replace the Hadoop Bundled With HBase! Because HBase depends on Hadoop, it bundles Hadoop jars under its *lib* directory. The bundled jars are ONLY for use in stand-alone mode. In distributed mode, it is *critical* that the version of Hadoop that is out on your cluster match what is under HBase. Replace the hadoop jars found in the HBase lib directory with the equivalent hadoop jars from the version you are running on your cluster to avoid version mismatch issues. Make sure you replace the jars under HBase across your whole cluster. Hadoop version mismatch issues have various manifestations. Check for mismatch if HBase appears hung. |
|---|---|

#### 4.1.1. Hadoop 3 Support for the HBase Binary Releases and Maven Artifacts

For HBase 2.5.1 and earlier, the official HBase binary releases and Maven artifacts were built with Hadoop 2.x.

Starting with HBase 2.5.2, HBase provides binary releases and Maven artifacts built with both Hadoop 2.x and Hadoop 3.x. The Hadoop 2 artifacts do not have any version suffix, the Hadoop 3 artifacts add the `-hadoop-3` suffix to the version. i.e. `hbase-2.5.2-bin.tar.gz.asc` is the Binary release built with Hadoop2, and `hbase-2.5.2-hadoop3-bin.tar.gz` is the release built with Hadoop 3.

#### 4.1.2. Hadoop 3 version policy

Each HBase release has a default Hadoop 3 version. This is used when the Hadoop 3 version is not specified during build, and for building the official binary releases and artifacts. Generally when a new minor version is released (i.e. 2.5.0) the default version is set to the latest supported Hadoop 3 version at the start of the release process.

Up to HBase 2.5.10 and 2.6.1 even if HBase added support for newer Hadoop 3 releases in a patch release, the default Hadoop 3 version (and the one used in the official binary releases) was not updated. This simplified upgrading, but meant that HBase releases often included old unfixed CVEs both from Hadoop and Hadoop’s dependencies, even when newer Hadoop releases with fixes were available.

Starting with HBase 2.5.11 and 2.6.2, the default Hadoop 3 version is always set to the latest supported Hadoop 3 version, and is also used for the `-hadoop3` binary releases and artifacts. This will drastically reduce the number of known CVEs shipped in the HBase binary releases, and make sure that all fixes and improvements in Hadoop are included.

#### 4.1.3. `dfs.datanode.max.transfer.threads`

An HDFS DataNode has an upper bound on the number of files that it will serve at any one time. Before doing any loading, make sure you have configured Hadoop’s *conf/hdfs-site.xml*, setting the `dfs.datanode.max.transfer.threads` value to at least the following:

```
<property>
  <name>dfs.datanode.max.transfer.threads</name>
  <value>4096</value>
</property>
```

Be sure to restart your HDFS after making the above configuration.

Not having this configuration in place makes for strange-looking failures. One manifestation is a complaint about missing blocks. For example:

```
10/12/08 20:10:31 INFO hdfs.DFSClient: Could not obtain block
          blk_XXXXXXXXXXXXXXXXXXXXXX_YYYYYYYY from any node: java.io.IOException: No live nodes
          contain current block. Will get new block locations from namenode and retry...
```

See also casestudies.max.transfer.threads and note that this property was previously known as `dfs.datanode.max.xcievers` (e.g. Hadoop HDFS: Deceived by Xciever).

### 4.2. ZooKeeper Requirements

An Apache ZooKeeper quorum is required. The exact version depends on your version of HBase, though the minimum ZooKeeper version is 3.4.x due to the `useMulti` feature made default in 1.0.0 (see HBASE-16598).
