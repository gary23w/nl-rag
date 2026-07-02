---
title: "Apache HBase® Reference Guide (part 37/41)"
source: https://hbase.apache.org/book.html
domain: apache-hbase
license: CC-BY-SA-4.0
tags: apache hbase, bigtable clone, wide-column store, apache hadoop
fetched: 2026-07-02
part: 37/41
---

## 208. SASL Authentication with ZooKeeper

Newer releases of Apache HBase (>= 0.92) will support connecting to a ZooKeeper Quorum that supports SASL authentication (which is available in ZooKeeper versions 3.4.0 or later).

This describes how to set up HBase to mutually authenticate with a ZooKeeper Quorum. ZooKeeper/HBase mutual authentication (HBASE-2418) is required as part of a complete secure HBase configuration (HBASE-3025). For simplicity of explication, this section ignores additional configuration required (Secure HDFS and Coprocessor configuration). It’s recommended to begin with an HBase-managed ZooKeeper configuration (as opposed to a standalone ZooKeeper quorum) for ease of learning.

### 208.1. Operating System Prerequisites

You need to have a working Kerberos KDC setup. For each `$HOST` that will run a ZooKeeper server, you should have a principle `zookeeper/$HOST`. For each such host, add a service key (using the `kadmin` or `kadmin.local` tool’s `ktadd` command) for `zookeeper/$HOST` and copy this file to `$HOST`, and make it readable only to the user that will run zookeeper on `$HOST`. Note the location of this file, which we will use below as *$PATH_TO_ZOOKEEPER_KEYTAB*.

Similarly, for each `$HOST` that will run an HBase server (master or regionserver), you should have a principle: `hbase/$HOST`. For each host, add a keytab file called *hbase.keytab* containing a service key for `hbase/$HOST`, copy this file to `$HOST`, and make it readable only to the user that will run an HBase service on `$HOST`. Note the location of this file, which we will use below as *$PATH_TO_HBASE_KEYTAB*.

Each user who will be an HBase client should also be given a Kerberos principal. This principal should usually have a password assigned to it (as opposed to, as with the HBase servers, a keytab file) which only this user knows. The client’s principal’s `maxrenewlife` should be set so that it can be renewed enough so that the user can complete their HBase client processes. For example, if a user runs a long-running HBase client process that takes at most 3 days, we might create this user’s principal within `kadmin` with: `addprinc -maxrenewlife 3days`. The ZooKeeper client and server libraries manage their own ticket refreshment by running threads that wake up periodically to do the refreshment.

On each host that will run an HBase client (e.g. `hbase shell`), add the following file to the HBase home directory’s *conf* directory:

```
Client {
  com.sun.security.auth.module.Krb5LoginModule required
  useKeyTab=false
  useTicketCache=true;
};
```

We’ll refer to this JAAS configuration file as *$CLIENT_CONF* below.

### 208.2. HBase-managed ZooKeeper Configuration

On each node that will run a zookeeper, a master, or a regionserver, create a JAAS configuration file in the conf directory of the node’s *HBASE_HOME* directory that looks like the following:

```
Server {
  com.sun.security.auth.module.Krb5LoginModule required
  useKeyTab=true
  keyTab="$PATH_TO_ZOOKEEPER_KEYTAB"
  storeKey=true
  useTicketCache=false
  principal="zookeeper/$HOST";
};
Client {
  com.sun.security.auth.module.Krb5LoginModule required
  useKeyTab=true
  useTicketCache=false
  keyTab="$PATH_TO_HBASE_KEYTAB"
  principal="hbase/$HOST";
};
```

where the *$PATH_TO_HBASE_KEYTAB* and *$PATH_TO_ZOOKEEPER_KEYTAB* files are what you created above, and `$HOST` is the hostname for that node.

The `Server` section will be used by the ZooKeeper quorum server, while the `Client` section will be used by the HBase master and regionservers. The path to this file should be substituted for the text *$HBASE_SERVER_CONF* in the *hbase-env.sh* listing below.

The path to this file should be substituted for the text *$CLIENT_CONF* in the *hbase-env.sh* listing below.

Modify your *hbase-env.sh* to include the following:

```
export HBASE_OPTS="-Djava.security.auth.login.config=$CLIENT_CONF"
export HBASE_MANAGES_ZK=true
export HBASE_ZOOKEEPER_OPTS="-Djava.security.auth.login.config=$HBASE_SERVER_CONF"
export HBASE_MASTER_OPTS="-Djava.security.auth.login.config=$HBASE_SERVER_CONF"
export HBASE_REGIONSERVER_OPTS="-Djava.security.auth.login.config=$HBASE_SERVER_CONF"
```

where *$HBASE_SERVER_CONF* and *$CLIENT_CONF* are the full paths to the JAAS configuration files created above.

Modify your *hbase-site.xml* on each node that will run zookeeper, master or regionserver to contain:

```
<configuration>
  <property>
    <name>hbase.zookeeper.quorum</name>
    <value>$ZK_NODES</value>
  </property>
  <property>
    <name>hbase.cluster.distributed</name>
    <value>true</value>
  </property>
  <property>
    <name>hbase.zookeeper.property.authProvider.1</name>
    <value>org.apache.zookeeper.server.auth.SASLAuthenticationProvider</value>
  </property>
  <property>
    <name>hbase.zookeeper.property.kerberos.removeHostFromPrincipal</name>
    <value>true</value>
  </property>
  <property>
    <name>hbase.zookeeper.property.kerberos.removeRealmFromPrincipal</name>
    <value>true</value>
  </property>
</configuration>
```

where `$ZK_NODES` is the comma-separated list of hostnames of the ZooKeeper Quorum hosts.

Start your hbase cluster by running one or more of the following set of commands on the appropriate hosts:

```
bin/hbase zookeeper start
bin/hbase master start
bin/hbase regionserver start
```

### 208.3. External ZooKeeper Configuration

Add a JAAS configuration file that looks like:

```
Client {
  com.sun.security.auth.module.Krb5LoginModule required
  useKeyTab=true
  useTicketCache=false
  keyTab="$PATH_TO_HBASE_KEYTAB"
  principal="hbase/$HOST";
};
```

where the *$PATH_TO_HBASE_KEYTAB* is the keytab created above for HBase services to run on this host, and `$HOST` is the hostname for that node. Put this in the HBase home’s configuration directory. We’ll refer to this file’s full pathname as *$HBASE_SERVER_CONF* below.

Modify your hbase-env.sh to include the following:

```
export HBASE_OPTS="-Djava.security.auth.login.config=$CLIENT_CONF"
export HBASE_MANAGES_ZK=false
export HBASE_MASTER_OPTS="-Djava.security.auth.login.config=$HBASE_SERVER_CONF"
export HBASE_REGIONSERVER_OPTS="-Djava.security.auth.login.config=$HBASE_SERVER_CONF"
```

Modify your *hbase-site.xml* on each node that will run a master or regionserver to contain:

```
<configuration>
  <property>
    <name>hbase.zookeeper.quorum</name>
    <value>$ZK_NODES</value>
  </property>
  <property>
    <name>hbase.cluster.distributed</name>
    <value>true</value>
  </property>
  <property>
    <name>hbase.zookeeper.property.authProvider.1</name>
    <value>org.apache.zookeeper.server.auth.SASLAuthenticationProvider</value>
  </property>
  <property>
    <name>hbase.zookeeper.property.kerberos.removeHostFromPrincipal</name>
    <value>true</value>
  </property>
  <property>
    <name>hbase.zookeeper.property.kerberos.removeRealmFromPrincipal</name>
    <value>true</value>
  </property>
</configuration>
```

where `$ZK_NODES` is the comma-separated list of hostnames of the ZooKeeper Quorum hosts.

Also on each of these hosts, create a JAAS configuration file containing:

```
Server {
  com.sun.security.auth.module.Krb5LoginModule required
  useKeyTab=true
  keyTab="$PATH_TO_ZOOKEEPER_KEYTAB"
  storeKey=true
  useTicketCache=false
  principal="zookeeper/$HOST";
};
```

where `$HOST` is the hostname of each Quorum host. We will refer to the full pathname of this file as *$ZK_SERVER_CONF* below.

Start your ZooKeepers on each ZooKeeper Quorum host with:

```
SERVER_JVMFLAGS="-Djava.security.auth.login.config=$ZK_SERVER_CONF" bin/zkServer start
```

Start your HBase cluster by running one or more of the following set of commands on the appropriate nodes:

```
bin/hbase master start
bin/hbase regionserver start
```

### 208.4. ZooKeeper Server Authentication Log Output

If the configuration above is successful, you should see something similar to the following in your ZooKeeper server logs:

```
11/12/05 22:43:39 INFO zookeeper.Login: successfully logged in.
11/12/05 22:43:39 INFO server.NIOServerCnxnFactory: binding to port 0.0.0.0/0.0.0.0:2181
11/12/05 22:43:39 INFO zookeeper.Login: TGT refresh thread started.
11/12/05 22:43:39 INFO zookeeper.Login: TGT valid starting at:        Mon Dec 05 22:43:39 UTC 2011
11/12/05 22:43:39 INFO zookeeper.Login: TGT expires:                  Tue Dec 06 22:43:39 UTC 2011
11/12/05 22:43:39 INFO zookeeper.Login: TGT refresh sleeping until: Tue Dec 06 18:36:42 UTC 2011
..
11/12/05 22:43:59 INFO auth.SaslServerCallbackHandler:
  Successfully authenticated client: authenticationID=hbase/ip-10-166-175-249.us-west-1.compute.internal@HADOOP.LOCALDOMAIN;
  authorizationID=hbase/ip-10-166-175-249.us-west-1.compute.internal@HADOOP.LOCALDOMAIN.
11/12/05 22:43:59 INFO auth.SaslServerCallbackHandler: Setting authorizedID: hbase
11/12/05 22:43:59 INFO server.ZooKeeperServer: adding SASL authorization for authorizationID: hbase
```

### 208.5. ZooKeeper Client Authentication Log Output

On the ZooKeeper client side (HBase master or regionserver), you should see something similar to the following:

```
11/12/05 22:43:59 INFO zookeeper.ZooKeeper: Initiating client connection, connectString=ip-10-166-175-249.us-west-1.compute.internal:2181 sessionTimeout=180000 watcher=master:60000
11/12/05 22:43:59 INFO zookeeper.ClientCnxn: Opening socket connection to server /10.166.175.249:2181
11/12/05 22:43:59 INFO zookeeper.RecoverableZooKeeper: The identifier of this process is 14851@ip-10-166-175-249
11/12/05 22:43:59 INFO zookeeper.Login: successfully logged in.
11/12/05 22:43:59 INFO client.ZooKeeperSaslClient: Client will use GSSAPI as SASL mechanism.
11/12/05 22:43:59 INFO zookeeper.Login: TGT refresh thread started.
11/12/05 22:43:59 INFO zookeeper.ClientCnxn: Socket connection established to ip-10-166-175-249.us-west-1.compute.internal/10.166.175.249:2181, initiating session
11/12/05 22:43:59 INFO zookeeper.Login: TGT valid starting at:        Mon Dec 05 22:43:59 UTC 2011
11/12/05 22:43:59 INFO zookeeper.Login: TGT expires:                  Tue Dec 06 22:43:59 UTC 2011
11/12/05 22:43:59 INFO zookeeper.Login: TGT refresh sleeping until: Tue Dec 06 18:30:37 UTC 2011
11/12/05 22:43:59 INFO zookeeper.ClientCnxn: Session establishment complete on server ip-10-166-175-249.us-west-1.compute.internal/10.166.175.249:2181, sessionid = 0x134106594320000, negotiated timeout = 180000
```

### 208.6. Configuration from Scratch

This has been tested on the current standard Amazon Linux AMI. First setup KDC and principals as described above. Next checkout code and run a sanity check.

```
git clone https:
cd hbase
mvn clean test -Dtest=TestZooKeeperACL
```

Then configure HBase as described above. Manually edit target/cached_classpath.txt (see below):

```
bin/hbase zookeeper &
bin/hbase master &
bin/hbase regionserver &
```

### 208.7. Future improvements

#### 208.7.1. Fix target/cached_classpath.txt

You must override the standard hadoop-core jar file from the `target/cached_classpath.txt` file with the version containing the HADOOP-7070 fix. You can use the following script to do this:

```
echo `find ~/.m2 -name "*hadoop-core*7070*SNAPSHOT.jar"` ':' `cat target/cached_classpath.txt` | sed 's/ //g' > target/tmp.txt
mv target/tmp.txt target/cached_classpath.txt
```

#### 208.7.2. Set JAAS configuration programmatically

This would avoid the need for a separate Hadoop jar that fixes HADOOP-7070.

#### 208.7.3. Elimination of `kerberos.removeHostFromPrincipal` and`kerberos.removeRealmFromPrincipal`


## 209. TLS connection to ZooKeeper

Apache ZooKeeper also supports SSL/TLS client connections to encrypt the data in transmission. This is particularly useful when the ZooKeeper ensemble is running on a host different from HBase and data has to be sent over the wire.

### 209.1. Java system properties

The ZooKeeper client supports the following Java system properties to set up TLS connection:

```
zookeeper.client.secure=true
zookeeper.clientCnxnSocket=org.apache.zookeeper.ClientCnxnSocketNetty
zookeeper.ssl.keyStore.location="/path/to/your/keystore"
zookeeper.ssl.keyStore.password="keystore_password"
zookeeper.ssl.trustStore.location="/path/to/your/truststore"
zookeeper.ssl.trustStore.password="truststore_password"
```

Setting up KeyStore is optional and only required if ZooKeeper server requests for client certificate.

Find more detailed information in the ZooKeeper SSL User Guide.

|   | These’re standard Java properties which should be set in the HBase command line and are effective in the entire Java process. All ZooKeeper clients running in the same process will pick them up including co-processors. |
|---|---|

|   | Since ZooKeeper version 3.8 the following two properties are useful to store the keystore and truststore passwords in protected text files rather than exposing them in the command line. |
|---|---|

```
zookeeper.ssl.keyStore.passwordPath=/path/to/secure/file
zookeeper.ssl.trustStore.passwordPath=/path/to/secure/file
```

### 209.2. HBase configuration

By adding HBASE-28038, ZooKeeper client TLS settings are also available in *hbase-site.xml* via `hbase.zookeeper.property` prefix. In contrast to Java system properties this could be more convenient under some circumstances.

```
<configuration>
  <property>
    <name>hbase.zookeeper.property.client.secure</name>
    <value>true</value>
  </property>
  <property>
    <name>hbase.zookeeper.property.clientCnxnSocket</name>
    <value>org.apache.zookeeper.ClientCnxnSocketNetty</value>
  </property>
  <property>
    <name>hbase.zookeeper.property.ssl.trustStore.location</name>
    <value>/path/to/your/truststore</value>
  </property>
...
</configuration>
```

|   | These settings are eventually transformed into Java system properties, it’s just a convenience feature. So, the same rules that mentioned in the previous point, applies to them as well. |
|---|---|

# Community


## 210. Decisions

Feature Branches

Feature Branches are easy to make. You do not have to be a committer to make one. Just request the name of your branch be added to JIRA up on the developer’s mailing list and a committer will add it for you. Thereafter you can file issues against your feature branch in Apache HBase JIRA. Your code you keep elsewhere — it should be public so it can be observed — and you can update dev mailing list on progress. When the feature is ready for commit, 3 +1s from committers will get your feature merged. See HBase, mail # dev - Thoughts about large feature dev branches

How to set fix version in JIRA on issue resolve

Here is how we agreed to set versions in JIRA when we resolve an issue. If master is going to be 3.0.0, branch-2 will be 2.4.0, and branch-1 will be 1.7.0 then:

- Commit only to master (i.e., backward-incompatible new feature): Mark with 3.0.0
- Commit only to master and branch-2 (i.e., backward-compatible new feature, applicable only to 2.x+): Mark with 3.0.0 and 2.4.0
- Commit to master, branch-2, and branch-1 (i.e., backward-compatible new feature, applicable everywhere): Mark with 3.0.0, 2.4.0, and 1.7.0
- Commit to master, branch-2, and branch-2.3, branch-1, branch-1.4 (i.e., bug fix applicable to all active release lines): Mark with 3.0.0, 2.4.0, 2.3.x, 1.7.0, and 1.4.x
- Commit a fix to the website: no version

Policy on when to set a RESOLVED JIRA as CLOSED

We agreed that for issues that list multiple releases in their *Fix Version/s* field, CLOSE the issue on the release of any of the versions listed; subsequent change to the issue must happen in a new JIRA.

Only transient state in ZooKeeper!

You should be able to kill the data in zookeeper and hbase should ride over it recreating the zk content as it goes. This is an old adage around these parts. We just made note of it now. We also are currently in violation of this basic tenet — replication at least keeps permanent state in zk — but we are working to undo this breaking of a golden rule.


## 211. Community Roles

### 211.1. Release Managers

Each maintained release branch has a release manager, who volunteers to coordinate new features and bug fixes are backported to that release. The release managers are committers. If you would like your feature or bug fix to be included in a given release, communicate with that release manager. If this list goes out of date or you can’t reach the listed person, reach out to someone else on the list.

| Release | Release Manager | Latest Release | EOL |
|---|---|---|---|
| 0.94 | Lars Hofhansl | 0.94.27 | April 2017 |
| 0.96 | Michael Stack | 0.96.2 | September 2014 |
| 0.98 | Andrew Purtell | 0.98.24 | April 2017 |
| 1.0 | Enis Soztutar | 1.0.3 | January 2016 |
| 1.1 | Nick Dimiduk | 1.1.13 | December 2017 |
| 1.2 | Sean Busbey | 1.2.12 | June 2019 |
| 1.3 | Mikhail Antonov | 1.3.6 | August 2020 |
| 1.4 | Andrew Purtell | 1.4.14 | October 2021 |
| 1.5 | Andrew Purtell | 1.5.0 | October 2019 |
| 1.6 | Andrew Purtell | 1.6.0 | February 2020 |
| 1.7 | Reid Chan | 1.7.2 | August 2022 |
| 2.0 | Michael Stack | 2.0.6 | September 2019 |
| 2.1 | Duo Zhang | 2.1.10 | May 2020 |
| 2.2 | Guanghao Zhang | 2.2.7 | April 2021 |
| 2.3 | Nick Dimiduk | 2.3.7 | October 2021 |
| 2.4 | Andrew Purtell | 2.4.18 | June 2024 |
| 2.5 | Andrew Purtell | Check the download page | **NOT YET** |
| 2.6 | Bryan Beaudreault | Check the download page | **NOT YET** |


## 212. Commit Message format

We agreed to the following Git commit message format:

```
HBASE-xxxxx <title>. (<contributor>)
```

If the person making the commit is the contributor, leave off the '(<contributor>)' element.

# hbtop


## 213. Overview

`hbtop` is a real-time monitoring tool for HBase like Unix’s top command. It can display summary information as well as metrics per Region/Namespace/Table/RegionServer. In this tool, you can see the metrics sorted by a selected field and filter the metrics to see only metrics you really want to see. Also, with the drill-down feature, you can find hot regions easily in a top-down manner.


## 214. Usage

You can run hbtop with the following command:

```
$ hbase hbtop
```

In this case, the values of `hbase.client.zookeeper.quorum` and `zookeeper.znode.parent` in `hbase-site.xml` in the classpath or the default values of them are used to connect.

Or, you can specify your own zookeeper quorum and znode parent as follows:

```
$ hbase hbtop -Dhbase.client.zookeeper.quorum=<zookeeper quorum> -Dzookeeper.znode.parent=<znode parent>
```

The top screen consists of a summary part and of a metrics part. In the summary part, you can see `HBase Version`, `Cluster ID`, `The number of region servers`, `Region count`, `Average Cluster Load` and `Aggregated Request/s`. In the metrics part, you can see metrics per Region/Namespace/Table/RegionServer depending on the selected mode. The top screen is refreshed in a certain period – 3 seconds by default.

### 214.1. Scrolling metric records

You can scroll the metric records in the metrics part.

### 214.2. Command line arguments

| Argument | Description |
|---|---|
| -d,--delay <arg> | The refresh delay (in seconds); default is 3 seconds |
| -h,--help | Print usage; for help while the tool is running press `h` key |
| -m,--mode <arg> | The mode; `n` (Namespace)\| `t` (Table)\| `r` (Region)\| `s` (RegionServer), default is `r` |
| -n,--numberOfIterations <arg> | The number of iterations |
| -O,--outputFieldNames | Print each of the available field names on a separate line, then quit |
| -f,--fields <arg> | Show only the given fields. Specify comma separated fields to show multiple fields |
| -s,--sortField <arg> | The initial sort field. You can prepend a `+' or `-' to the field name to also override the sort direction. A leading `+' will force sorting high to low, whereas a `-' will ensure a low to high ordering |
| -i,--filters <arg> | The initial filters. Specify comma separated filters to set multiple filters |
| -b,--batchMode | Starts hbtop in Batch mode, which could be useful for sending output from hbtop to other programs or to a file. In this mode, hbtop will not accept input and runs until the iterations limit you’ve set with the `-n' command-line option or until killed |

### 214.3. Modes

There are the following modes in hbtop:

| Mode | Description |
|---|---|
| Region | Showing metric records per region |
| Namespace | Showing metric records per namespace |
| Table | Showing metric records per table |
| RegionServer | Showing metric records per region server |
| User | Showing metric records per user |
| Client | Showing metric records per client |

#### 214.3.1. Region mode

In Region mode, the default sort field is `#REQ/S`.

The fields in this mode are as follows:

| Field | Description | Displayed by default |
|---|---|---|
| RNAME | Region Name | false |
| NAMESPACE | Namespace Name | true |
| TABLE | Table Name | true |
| SCODE | Start Code | false |
| REPID | Replica ID | false |
| REGION | Encoded Region Name | true |
| RS | Short Region Server Name | true |
| LRS | Long Region Server Name | false |
| #REQ/S | Request Count per second | true |
| #READ/S | Read Request Count per second | true |
| #FREAD/S | Filtered Read Request Count per second | true |
| #WRITE/S | Write Request Count per second | true |
| SF | StoreFile Size | true |
| USF | Uncompressed StoreFile Size | false |
| #SF | Number of StoreFiles | true |
| MEMSTORE | MemStore Size | true |
| LOCALITY | Block Locality | true |
| SKEY | Start Key | false |
| #COMPingCELL | Compacting Cell Count | false |
| #COMPedCELL | Compacted Cell Count | false |
| %COMP | Compaction Progress | false |
| LASTMCOMP | Last Major Compaction Time | false |

#### 214.3.2. Namespace mode

In Namespace mode, the default sort field is `#REQ/S`.

The fields in this mode are as follows:

| Field | Description | Displayed by default |
|---|---|---|
| NAMESPACE | Namespace Name | true |
| #REGION | Region Count | true |
| #REQ/S | Request Count per second | true |
| #READ/S | Read Request Count per second | true |
| #FREAD/S | Filtered Read Request Count per second | true |
| #WRITE/S | Write Request Count per second | true |
| SF | StoreFile Size | true |
| USF | Uncompressed StoreFile Size | false |
| #SF | Number of StoreFiles | true |
| MEMSTORE | MemStore Size | true |

#### 214.3.3. Table mode

In Table mode, the default sort field is `#REQ/S`.

The fields in this mode are as follows:

| Field | Description | Displayed by default |
|---|---|---|
| NAMESPACE | Namespace Name | true |
| TABLE | Table Name | true |
| #REGION | Region Count | true |
| #REQ/S | Request Count per second | true |
| #READ/S | Read Request Count per second | true |
| #FREAD/S | Filtered Read Request Count per second | true |
| #WRITE/S | Write Request Count per second | true |
| SF | StoreFile Size | true |
| USF | Uncompressed StoreFile Size | false |
| #SF | Number of StoreFiles | true |
| MEMSTORE | MemStore Size | true |

#### 214.3.4. RegionServer mode

In RegionServer mode, the default sort field is `#REQ/S`.

The fields in this mode are as follows:

| Field | Description | Displayed by default |
|---|---|---|
| RS | Short Region Server Name | true |
| LRS | Long Region Server Name | false |
| #REGION | Region Count | true |
| #REQ/S | Request Count per second | true |
| #READ/S | Read Request Count per second | true |
| #FREAD/S | Filtered Read Request Count per second | true |
| #WRITE/S | Write Request Count per second | true |
| SF | StoreFile Size | true |
| USF | Uncompressed StoreFile Size | false |
| #SF | Number of StoreFiles | true |
| MEMSTORE | MemStore Size | true |
| UHEAP | Used Heap Size | true |
| MHEAP | Max Heap Size | true |

#### 214.3.5. User mode

In User mode, the default sort field is `#REQ/S`.

The fields in this mode are as follows:

| Field | Description | Displayed by default |
|---|---|---|
| USER | user Name | true |
| #CLIENT | Client Count | true |
| #REQ/S | Request Count per second | true |
| #READ/S | Read Request Count per second | true |
| #WRITE/S | Write Request Count per second | true |
| #FREAD/S | Filtered Read Request Count per second | true |

#### 214.3.6. Client mode

In Client mode, the default sort field is `#REQ/S`.

The fields in this mode are as follows:

| Field | Description | Displayed by default |
|---|---|---|
| CLIENT | Client Hostname | true |
| #USER | User Count | true |
| #REQ/S | Request Count per second | true |
| #READ/S | Read Request Count per second | true |
| #WRITE/S | Write Request Count per second | true |
| #FREAD/S | Filtered Read Request Count per second | true |

### 214.4. Changing mode

You can change mode by pressing `m` key in the top screen.

### 214.5. Changing the refresh delay

You can change the refresh by pressing `d` key in the top screen.

### 214.6. Changing the displayed fields

You can move to the field screen by pressing `f` key in the top screen. In the fields screen, you can change the displayed fields by choosing a field and pressing `d` key or `space` key.

### 214.7. Changing the sort field

You can move to the fields screen by pressing `f` key in the top screen. In the field screen, you can change the sort field by choosing a field and pressing `s`. Also, you can change the sort order (ascending or descending) by pressing `R` key.

### 214.8. Changing the order of the fields

You can move to the fields screen by pressing `f` key in the top screen. In the field screen, you can change the order of the fields.

### 214.9. Filters

You can filter the metric records with the filter feature. We can add filters by pressing `o` key for ignoring case or `O` key for case sensitive.

The syntax is as follows:

```
<Field><Operator><Value>
```

For example, we can add filters like the following:

```
NAMESPACE==default
REQ/S>1000
```

The operators we can specify are as follows:

| Operator | Description |
|---|---|
| = | Partial match |
| == | Exact match |
| > | Greater than |
| >= | Greater than or equal to |
| < | Less than |
| ⇐ | Less than and equal to |

You can see the current filters by pressing `^o` key and clear them by pressing `=` key.

### 214.10. Drilling down

You can drill down the metric record by choosing a metric record that you want to drill down and pressing `i` key in the top screen. With this feature, you can find hot regions easily in a top-down manner.

### 214.11. Help screen

You can see the help screen by pressing `h` key in the top screen.


## 215. Others

### 215.1. How hbtop gets the metrics data

hbtop gets the metrics from ClusterMetrics which is returned as the result of a call to Admin#getClusterMetrics() on the current HMaster. To add metrics to hbtop, they will need to be exposed via ClusterMetrics.

# Tracing


## 216. Overview

HBase used to depend on the HTrace project for tracing. After the Apache HTrace project moved to the Attic/retired, we decided to move to OpenTelemetry in HBASE-22120.

The basic support for tracing has been done, where we added tracing for async client, rpc, region read/write/scan operation, and WAL. We use opentelemetry-api to implement the tracing support manually by code, as our code base is way too complicated to be instrumented through a java agent. But notice that you still need to attach the opentelemetry java agent to enable tracing. Please see the official site for OpenTelemetry and the documentation for opentelemetry-java-instrumentation for more details on how to properly configure opentelemetry instrumentation.


## 217. Usage

### 217.1. Enable Tracing

See this section in hbase-env.sh

```
# Uncomment to enable trace, you can change the options to use other exporters such as jaeger or
# zipkin. See https://github.com/open-telemetry/opentelemetry-java-instrumentation on how to
# configure exporters and other components through system properties.
# export HBASE_TRACE_OPTS="-Dotel.resource.attributes=service.name=HBase -Dotel.traces.exporter=logging otel.metrics.exporter=none"
```

Uncomment this line to enable tracing. The default config is to output the tracing data to log. Please see the documentation for opentelemetry-java-instrumentation for more details on how to export tracing data to other tracing system such as OTel collector, jaeger or zipkin, what does the *service.name* mean, and how to change the sampling rate, etc.

|   | The LoggingSpanExporter uses java.util.logging(jul) for logging tracing data, and the logger is initialized in opentelemetry java agent, which seems to be ahead of our jul to slf4j bridge initialization, so it will always log the tracing data to console. We highly suggest that you use other tracing systems to collect and view tracing data instead of logging. |
|---|---|

### 217.2. Performance Impact

According to the result in HBASE-25658, the performance impact is minimal. Of course the test cluster is not under heavy load, so if you find out that enabling tracing would impact the performance, try to lower the sampling rate. See documentation for configuring sampler for more details.

# Store File Tracking


## 218. Overview

This feature introduces an abstraction layer to track store files still used/needed by store engines, allowing for plugging different approaches of identifying store files required by the given store.

Historically, HBase internals have relied on creating hfiles on temporary directories first, renaming those files to the actual store directory at operation commit time. That’s a simple and convenient way to separate transient from already finalised files that are ready to serve client reads with data. This approach works well with strong consistent file systems, but with the popularity of less consistent file systems, mainly Object Store which can be used like file systems, dependency on atomic rename operations starts to introduce performance penalties. The Amazon S3 Object Store, in particular, has been the most affected deployment, due to its lack of atomic renames. The HBase community temporarily bypassed this problem by building a distributed locking layer called HBOSS, to guarantee atomicity of operations against S3.

With **Store File Tracking**, decision on where to originally create new hfiles and how to proceed upon commit is delegated to the specific Store File Tracking implementation. The implementation can be set at the HBase service leve in **hbase-site.xml** or at the Table or Column Family via the TableDescriptor configuration.

|   | When the store file tracking implementation is specified in **hbase_site.xml**, this configuration is also propagated into a tables configuration at table creation time. This is to avoid dangerous configuration mismatches between processes, which could potentially lead to data loss. |
|---|---|


## 219. Available Implementations

Store File Tracking initial version provides three builtin implementations:

- DEFAULT
- FILE
- MIGRATION

### 219.1. DEFAULT

As per the name, this is the Store File Tracking implementation used by default when no explicit configuration has been defined. The DEFAULT tracker implements the standard approach using temporary directories and renames. This is how all previous (implicit) implementation that HBase used to track store files.

### 219.2. FILE

A file tracker implementation that creates new files straight in the store directory, avoiding the need for rename operations. It keeps a list of committed hfiles in memory, backed by meta files, in each store directory. Whenever a new hfile is committed, the list of *tracked files* in the given store is updated and a new meta file is written with this list contents, discarding the previous meta file now containing an out dated list.

### 219.3. MIGRATION

A special implementation to be used when swapping between Store File Tracking implementations on pre-existing tables that already contain data, and therefore, files being tracked under an specific logic.


## 220. Usage

For fresh deployments that don’t yet contain any user data, **FILE** implementation can be just set as value for **hbase.store.file-tracker.impl** property in global **hbase-site.xml** configuration, prior to the first hbase start. Omitting this property sets the **DEFAULT** implementation.

For clusters with data that are upgraded to a version of HBase containing the store file tracking feature, the Store File Tracking implementation can only be changed with the **MIGRATION** implementation, so that the *new tracker* can safely build its list of tracked files based on the list of the *current tracker*.

|   | MIGRATION tracker should NOT be set at global configuration. To use it, follow below section about setting Store File Tacking at Table or Column Family configuration. |
|---|---|

### 220.1. Configuring for Table or Column Family

Setting Store File Tracking configuration globally may not always be possible or desired, for example, in the case of upgraded clusters with pre-existing user data. Store File Tracking can be set at Table or Column Family level configuration. For example, to specify **FILE** implementation in the table configuration at table creation time, the following should be applied:

```
create 'my-table', 'f1', 'f2', {CONFIGURATION => {'hbase.store.file-tracker.impl' => 'FILE'}}
```

To define **FILE** for an specific Column Family:

```
create 'my-table', {NAME=> '1', CONFIGURATION => {'hbase.store.file-tracker.impl' => 'FILE'}}
```

### 220.2. Switching trackers at Table or Column Family

A very common scenario is to set Store File Tracking on pre-existing HBase deployments that have been upgraded to a version that supports this feature. To apply the FILE tracker, tables effectively need to be migrated from the DEFAULT tracker to the FILE tracker. As explained previously, such process requires the usage of the special MIGRATION tracker implementation, which can only be specified at table or Column Family level.

For example, to switch *tracker* from **DEFAULT** to **FILE** in a table configuration:

```
alter 'my-table', CONFIGURATION => {'hbase.store.file-tracker.impl' => 'MIGRATION',
'hbase.store.file-tracker.migration.src.impl' => 'DEFAULT',
'hbase.store.file-tracker.migration.dst.impl' => 'FILE'}
```

To apply similar switch at column family level configuration:

```
alter 'my-table', {NAME => 'f1', CONFIGURATION => {'hbase.store.file-tracker.impl' => 'MIGRATION',
'hbase.store.file-tracker.migration.src.impl' => 'DEFAULT',
'hbase.store.file-tracker.migration.dst.impl' => 'FILE'}}
```

Once all table regions have been onlined again, don’t forget to disable MIGRATION, by now setting **hbase.store.file-tracker.migration.dst.impl** value as the **hbase.store.file-tracker.impl**. In the above example, that would be as follows:

```
alter 'my-table', CONFIGURATION => {'hbase.store.file-tracker.impl' => 'FILE'}
```

### 220.3. Specifying trackers during snapshot recovery

It’s also possible to specify a given store file tracking implementation when recovering a snapshot using the *CLONE_SFT* option of *clone_snasphot* command. This is useful when recovering old snapshots, taken prior to a change in the global configuration, or if the snapshot has been imported from a different cluster that had a different store file tracking setting. Because snapshots preserve table and colum family descriptors, a simple restore would reload the original configuration, requiring the additional steps described above to convert the table/column family to the desired tracker implementation. An example of how to use *clone_snapshot* to specify the **FILE** tracker implementation is shown below:

```
clone_snapshot 'snapshotName', 'namespace:tableName', {CLONE_SFT=>'FILE'}
```

|   | The option to specify the tracker during snapshot recovery is only available for the *clone_snapshot* command. The *restore_snapshot* command does not support this parameter. |
|---|---|

# Bulk Data Generator Tool

This is a random data generator tool for HBase tables leveraging Hbase bulk load. It can create pre-splited HBase table and the generated data is

uniformly distributed

to all the regions of the table.


## 221. Usage

```
usage: hbase org.apache.hadoop.hbase.util.bulkdatagenerator.BulkDataGeneratorTool <OPTIONS> [-D<property=value>]*
 -d,--delete-if-exist         If it's set, the table will be deleted if already exist.
 -h,--help                    Show help message for the tool
 -mc,--mapper-count <arg>     The number of mapper containers to be launched.
 -o,--table-options <arg>     Table options to be set while creating the table.
 -r,--rows-per-mapper <arg>   The number of rows to be generated PER mapper.
 -sc,--split-count <arg>      The number of regions/pre-splits to be created for the table.
 -t,--table <arg>             The table name for which data need to be generated.
```

```
Examples:

hbase org.apache.hadoop.hbase.util.bulkdatagenerator.BulkDataGeneratorTool -t TEST_TABLE -mc 10 -r 100 -sc 10

hbase org.apache.hadoop.hbase.util.bulkdatagenerator.BulkDataGeneratorTool -t TEST_TABLE -mc 10 -r 100 -sc 10 -d -o "BACKUP=false,NORMALIZATION_ENABLED=false"

hbase org.apache.hadoop.hbase.util.bulkdatagenerator.BulkDataGeneratorTool -t TEST_TABLE -mc 10 -r 100 -sc 10 -Dmapreduce.map.memory.mb=8192
```


## 222. Overview

#### 222.1. Table Schema

Tool generates a HBase table with single column family, i.e. **cf** and 9 columns i.e.

```
ORG_ID, TOOL_EVENT_ID, EVENT_ID, VEHICLE_ID, SPEED, LATITUDE, LONGITUDE, LOCATION, TIMESTAMP
```

with row key as

```
<TOOL_EVENT_ID>:<ORGANIZATION_ID>
```

#### 222.2. Table Creation

Tool creates a pre-splited HBase Table having "**split-count**" splits (i.e. **split-count** + 1 regions) with sequential 6 digit region boundary prefix. Example: If a table is generated with "**split-count**" as 10, it will have (10+1) regions with following start-end keys.

```
(-000001, 000001-000002, 000002-000003, ...., 000009-000010, 0000010-)
```

#### 222.3. Data Generation

Tool creates and run a MR job to generate the HFiles, which are bulk loaded to table regions via `org.apache.hadoop.hbase.tool.BulkLoadHFilesTool`. The number of mappers is defined in input as "**mapper-count**". Each mapper generates "**records-per-mapper**" rows.

`org.apache.hadoop.hbase.util.bulkdatageneratorBulkDataGeneratorRecordReader` ensures that each record generated by mapper is associated with index (added to the key) ranging from 1 to "**records-per-mapper**".

The TOOL_EVENT_ID column for each row has a 6 digit prefix as

```
(index) mod ("split-count" + 1)
```

Example, if 10 records are to be generated by each mapper and "**split-count**" is 4, the TOOL_EVENT_IDs for each record will have a prefix as

| Record Index | TOOL_EVENT_ID’s first six characters |
|---|---|
| 1 | 000001 |
| 2 | 000002 |
| 3 | 000003 |
| 4 | 000004 |
| 5 | 000000 |
| 6 | 000001 |
| 7 | 000002 |
| 8 | 000003 |
| 9 | 000004 |
| 10 | 000005 |

Since TOOL_EVENT_ID is first attribute of row key and table region boundaries are also having start-end keys as 6 digit sequential prefixes, this ensures that each mapper generates (nearly) same number of rows for each region, making the data uniformly distributed. TOOL_EVENT_ID suffix and other columns of the row are populated with random data.

Number of rows generated is

```
rows-per-mapper * mapper-count
```

Size of each rows is (approximately)

```
850 B
```

### 222.4. Experiments

These results are from a 11 node cluster having HBase and Hadoop service running within self-managed test environment

| Data Size | Time to Generate Data (mins) |
|---|---|
| 100 GB | 6 minutes |
| 340 GB | 13 minutes |
| 3.5 TB | 3 hours 10 minutes |

# Appendix
