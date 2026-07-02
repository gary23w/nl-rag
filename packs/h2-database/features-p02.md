---
title: "Features (part 2/2)"
source: https://www.h2database.com/html/features.html
domain: h2-database
license: CC-BY-SA-4.0
tags: h2 database, h2 java database, embedded database, in-memory database
fetched: 2026-07-02
part: 2/2
---

## Read Only Databases in Zip or Jar File

To create a read-only database in a zip file, first create a regular persistent database, and then create a backup. The database must not have pending changes, that means you need to close all connections to the database first. To speed up opening the read-only database and running queries, the database should be closed using `SHUTDOWN DEFRAG`. If you are using a database named `test`, an easy way to create a zip file is using the `Backup` tool. You can start the tool from the command line, or from within the H2 Console (Tools - Backup). Please note that the database must be closed when the backup is created. Therefore, the SQL statement `BACKUP TO` can not be used.

When the zip file is created, you can open the database in the zip file using the following database URL:

```
jdbc:h2:zip:~/data.zip!/test
```

Databases in zip files are read-only. The performance for some queries will be slower than when using a regular database, because random access in zip files is not supported (only streaming). How much this affects the performance depends on the queries and the data. The database is not read in memory; therefore large databases are supported as well. The same indexes are used as when using a regular database.

If the database is larger than a few megabytes, performance is much better if the database file is split into multiple smaller files, because random access in compressed files is not possible. See also the sample application ReadOnlyDatabaseInZip.

### Opening a Corrupted Database

If a database cannot be opened because the boot info (the SQL script that is run at startup) is corrupted, then the database can be opened by specifying a database event listener. The exceptions are logged, but opening the database will continue.


## Generated Columns (Computed Columns) / Function Based Index

Each column is either a base column or a generated column. A generated column is a column whose value is calculated before storing and cannot be assigned directly. The formula is evaluated when the row is inserted, and re-evaluated every time the row is updated. One use case is to automatically update the last-modification time:

```
CREATE TABLE TEST(
    ID INT,
    NAME VARCHAR,
    LAST_MOD TIMESTAMP WITH TIME ZONE
        GENERATED ALWAYS AS CURRENT_TIMESTAMP
);
```

Function indexes are not directly supported by this database, but they can be emulated by using generated columns. For example, if an index on the upper-case version of a column is required, create a generated column with the upper-case version of the original column, and create an index for this column:

```
CREATE TABLE ADDRESS(
    ID INT PRIMARY KEY,
    NAME VARCHAR,
    UPPER_NAME VARCHAR GENERATED ALWAYS AS UPPER(NAME)
);
CREATE INDEX IDX_U_NAME ON ADDRESS(UPPER_NAME);
```

When inserting data, it is not required (and not allowed) to specify a value for the upper-case version of the column, because the value is generated. But you can use the column when querying the table:

```
INSERT INTO ADDRESS(ID, NAME) VALUES(1, 'Miller');
SELECT * FROM ADDRESS WHERE UPPER_NAME='MILLER';
```


## Multi-Dimensional Indexes

A tool is provided to execute efficient multi-dimension (spatial) range queries. This database does not support a specialized spatial index (R-Tree or similar). Instead, the B-Tree index is used. For each record, the multi-dimensional key is converted (mapped) to a single dimensional (scalar) value. This value specifies the location on a space-filling curve.

Currently, Z-order (also called N-order or Morton-order) is used; Hilbert curve could also be used, but the implementation is more complex. The algorithm to convert the multi-dimensional value is called bit-interleaving. The scalar value is indexed using a B-Tree index (usually using a generated column).

The method can result in a drastic performance improvement over just using an index on the first column. Depending on the data and number of dimensions, the improvement is usually higher than factor 5. The tool generates a SQL query from a specified multi-dimensional range. The method used is not database dependent, and the tool can easily be ported to other databases. For an example how to use the tool, please have a look at the sample code provided in `TestMultiDimension.java`.


## User-Defined Functions and Stored Procedures

In addition to the built-in functions, this database supports user-defined Java functions. In this database, Java functions can be used as stored procedures as well. A function must be declared (registered) before it can be used. A function can be defined using source code, or as a reference to a compiled class that is available in the classpath. By default, the function aliases are stored in the current schema.

### Referencing a Compiled Method

When referencing a method, the class must already be compiled and included in the classpath where the database is running. Only static Java methods are supported; both the class and the method must be public. Example Java class:

```
package acme;
import java.math.*;
public class Function {
    public static boolean isPrime(int value) {
        return new BigInteger(String.valueOf(value)).isProbablePrime(100);
    }
}
```

The Java function must be registered in the database by calling `CREATE ALIAS ... FOR`:

```
CREATE ALIAS IS_PRIME FOR "acme.Function.isPrime";
```

For a complete sample application, see `src/test/org/h2/samples/Function.java`.

### Declaring Functions as Source Code

When defining a function alias with source code, the database tries to compile the source code using the Java compiler (the class `javax.tool.ToolProvider.getSystemJavaCompiler()`) if it is in the classpath. If not, `javac` is run as a separate process. Only the source code is stored in the database; the class is compiled each time the database is re-opened. Source code can be passed as dollar quoted text (`$$source code$$`) to avoid escaping problems. If you use some third-party script processing tool, use standard single quotes instead and don't forget to repeat each single quotation mark twice within the source code. Example:

```
CREATE ALIAS NEXT_PRIME AS '
String nextPrime(String value) {
    return new BigInteger(value).nextProbablePrime().toString();
}
';
```

By default, the three packages `java.util, java.math, java.sql` are imported. The method name (`nextPrime` in the example above) is ignored. Method overloading is not supported when declaring functions as source code, that means only one method may be declared for an alias. If different import statements are required, they must be declared at the beginning and separated with the tag `@CODE`:

```
CREATE ALIAS IP_ADDRESS AS '
import java.net.*;
@CODE
String ipAddress(String host) throws Exception {
    return InetAddress.getByName(host).getHostAddress();
}
';
```

The following template is used to create a complete Java class:

```
package org.h2.dynamic;
< import statements before the tag @CODE; if not set:
import java.util.*;
import java.math.*;
import java.sql.*;
>
public class <aliasName> {
    public static <sourceCode>
}
```

### Method Overloading

Multiple methods may be bound to a SQL function if the class is already compiled and included in the classpath. Each Java method must have a different number of arguments. Method overloading is not supported when declaring functions as source code.

### Function Data Type Mapping

Functions that accept non-nullable parameters such as `int` will not be called if one of those parameters is `NULL`. Instead, the result of the function is `NULL`. If the function should be called if a parameter is `NULL`, you need to use `java.lang.Integer` instead.

SQL types are mapped to Java classes and vice-versa as in the JDBC API. For details, see Data Types. There are a few special cases: `java.lang.Object` is mapped to `OTHER` (a serialized object). Therefore, `java.lang.Object` can not be used to match all SQL types (matching all SQL types is not supported). The second special case is `Object[]`: arrays of any class are mapped to `ARRAY`. Objects of type `org.h2.value.Value` (the internal value class) are passed through without conversion.

### Functions That Require a Connection

If the first parameter of a Java function is a `java.sql.Connection`, then the connection to database is provided. This connection does not need to be closed before returning. When calling the method from within the SQL statement, this connection parameter does not need to be (can not be) specified.

### Functions Throwing an Exception

If a function throws an exception, then the current statement is rolled back and the exception is thrown to the application. SQLException are directly re-thrown to the calling application; all other exceptions are first converted to a SQLException.

### Functions Returning a Result Set

Functions may returns a result set. Such a function can be called with the `CALL` statement:

```
public static ResultSet query(Connection conn, String sql) throws SQLException {
    return conn.createStatement().executeQuery(sql);
}

CREATE ALIAS QUERY FOR "org.h2.samples.Function.query";
CALL QUERY('SELECT * FROM TEST');
```

### Using SimpleResultSet

A function can create a result set using the `SimpleResultSet` tool:

```
import org.h2.tools.SimpleResultSet;
...
public static ResultSet simpleResultSet() throws SQLException {
    SimpleResultSet rs = new SimpleResultSet();
    rs.addColumn("ID", Types.INTEGER, 10, 0);
    rs.addColumn("NAME", Types.VARCHAR, 255, 0);
    rs.addRow(0, "Hello");
    rs.addRow(1, "World");
    return rs;
}

CREATE ALIAS SIMPLE FOR "org.h2.samples.Function.simpleResultSet";
CALL SIMPLE();
```

### Using a Function as a Table

A function that returns a result set can be used like a table. However, in this case the function is called at least twice: first while parsing the statement to collect the column names (with parameters set to `null` where not known at compile time). And then, while executing the statement to get the data (maybe multiple times if this is a join). If the function is called just to get the column list, the URL of the connection passed to the function is `jdbc:columnlist:connection`. Otherwise, the URL of the connection is `jdbc:default:connection`.

```
public static ResultSet getMatrix(Connection conn, Integer size)
        throws SQLException {
    SimpleResultSet rs = new SimpleResultSet();
    rs.addColumn("X", Types.INTEGER, 10, 0);
    rs.addColumn("Y", Types.INTEGER, 10, 0);
    String url = conn.getMetaData().getURL();
    if (url.equals("jdbc:columnlist:connection")) {
        return rs;
    }
    for (int s = size.intValue(), x = 0; x < s; x++) {
        for (int y = 0; y < s; y++) {
            rs.addRow(x, y);
        }
    }
    return rs;
}

CREATE ALIAS MATRIX FOR "org.h2.samples.Function.getMatrix";
SELECT * FROM MATRIX(4) ORDER BY X, Y;
```


## Pluggable or User-Defined Tables

For situations where you need to expose other data-sources to the SQL engine as a table, there are "pluggable tables". For some examples, have a look at the code in `org.h2.test.db.TestTableEngines`.

In order to create your own TableEngine, you need to implement the `org.h2.api.TableEngine` interface e.g. something like this:

```
package acme;
public static class MyTableEngine implements org.h2.api.TableEngine {

    private static class MyTable extends org.h2.table.TableBase {
        .. rather a lot of code here...
    }

    public EndlessTable createTable(CreateTableData data) {
        return new EndlessTable(data);
    }
}
```

and then create the table from SQL like this:

```
CREATE TABLE TEST(ID INT, NAME VARCHAR)
    ENGINE "acme.MyTableEngine";
```

It is also possible to pass in parameters to the table engine, like so:

```
CREATE TABLE TEST(ID INT, NAME VARCHAR) ENGINE "acme.MyTableEngine" WITH "param1", "param2";
```

In which case the parameters are passed down in the tableEngineParams field of the CreateTableData object.

It is also possible to specify default table engine params on schema creation:

```
CREATE SCHEMA TEST_SCHEMA WITH "param1", "param2";
```

Params from the schema are used when CREATE TABLE issued on this schema does not have its own engine params specified.


## Triggers

This database supports Java triggers that are called before or after a row is updated, inserted or deleted. Triggers can be used for complex consistency checks, or to update related data in the database. It is also possible to use triggers to simulate materialized views. For a complete sample application, see `src/test/org/h2/samples/TriggerSample.java`. A Java trigger must implement the interface `org.h2.api.Trigger`. The trigger class must be available in the classpath of the database engine (when using the server mode, it must be in the classpath of the server).

```
import org.h2.api.Trigger;
...
public class TriggerSample implements Trigger {

    public void init(Connection conn, String schemaName, String triggerName,
            String tableName, boolean before, int type) {
        // initialize the trigger object is necessary
    }

    public void fire(Connection conn,
            Object[] oldRow, Object[] newRow)
            throws SQLException {
        // the trigger is fired
    }

    public void close() {
        // the database is closed
    }

    public void remove() {
        // the trigger was dropped
    }

}
```

The connection can be used to query or update data in other tables. The trigger then needs to be defined in the database:

```
CREATE TRIGGER INV_INS AFTER INSERT ON INVOICE
    FOR EACH ROW CALL "org.h2.samples.TriggerSample"
```

The trigger can be used to veto a change by throwing a `SQLException`.

As an alternative to implementing the `Trigger` interface, an application can extend the abstract class `org.h2.tools.TriggerAdapter`. This will allows to use the `ResultSet` interface within trigger implementations. In this case, only the `fire` method needs to be implemented:

```
import org.h2.tools.TriggerAdapter;
...
public class TriggerSample extends TriggerAdapter {

    public void fire(Connection conn, ResultSet oldRow, ResultSet newRow)
            throws SQLException {
        // the trigger is fired
    }

}
```


## Compacting a Database

Empty space in the database file re-used automatically. When closing the database, the database is automatically compacted for up to 200 milliseconds by default. To compact more, use the SQL statement SHUTDOWN COMPACT. However re-creating the database may further reduce the database size because this will re-build the indexes. Here is a sample function to do this:

```
public static void compact(String dir, String dbName,
        String user, String password) throws Exception {
    String url = "jdbc:h2:" + dir + "/" + dbName;
    String file = "data/test.sql";
    Script.execute(url, user, password, file);
    DeleteDbFiles.execute(dir, dbName, true);
    RunScript.execute(url, user, password, file, null, false);
}
```

See also the sample application `org.h2.samples.Compact`. The commands `SCRIPT / RUNSCRIPT` can be used as well to create a backup of a database and re-build the database from the script.


## Cache Settings

The database keeps most frequently used data in the main memory. The amount of memory used for caching can be changed using the setting `CACHE_SIZE`. This setting can be set in the database connection URL (`jdbc:h2:~/test;CACHE_SIZE=131072`), or it can be changed at runtime using `SET CACHE_SIZE size`. The size of the cache, as represented by `CACHE_SIZE` is measured in KB, with each KB being 1024 bytes. This setting has no effect for in-memory databases. For persistent databases, the setting is stored in the database and re-used when the database is opened the next time. However, when opening an existing database, the cache size is set to at most half the amount of memory available for the virtual machine (Runtime.getRuntime().maxMemory()), even if the cache size setting stored in the database is larger; however the setting stored in the database is kept. Setting the cache size in the database URL or explicitly using `SET CACHE_SIZE` overrides this value (even if larger than the physical memory). To get the current used maximum cache size, use the query `SELECT * FROM INFORMATION_SCHEMA.SETTINGS WHERE SETTING_NAME = 'info.CACHE_MAX_SIZE'`

An experimental scan-resistant cache algorithm "Two Queue" (2Q) is available. To enable it, append `;CACHE_TYPE=TQ` to the database URL. The cache might not actually improve performance. If you plan to use it, please run your own test cases first.

Also included is an experimental second level soft reference cache. Rows in this cache are only garbage collected on low memory. By default the second level cache is disabled. To enable it, use the prefix `SOFT_`. Example: `jdbc:h2:~/test;CACHE_TYPE=SOFT_LRU`. The cache might not actually improve performance. If you plan to use it, please run your own test cases first.

To get information about page reads and writes, and the current caching algorithm in use, call `SELECT * FROM INFORMATION_SCHEMA.SETTINGS`. The number of pages read / written is listed.


## External authentication (Experimental)

External authentication allows to optionally validate user credentials externally (JAAS,LDAP,custom classes). Is also possible to temporary assign roles to externally authenticated users. **This feature is experimental and subject to change**

Master user cannot be externally authenticated

To enable external authentication on a database execute statement `SET AUTHENTICATOR TRUE`. This setting in persisted on the database.

To connect on a database by using external credentials client must append `AUTHREALM=H2` to the database URL. `H2` is the identifier of the authentication realm (see later).

External authentication requires to send password to the server. For this reason is works only on local connection or remote over ssl

By default external authentication is performed through JAAS login interface (configuration name is `h2`). To configure JAAS add argument `-Djava.security.auth.login.config=jaas.conf` Here an example of JAAS login configuration file content:

```
h2 {
    com.sun.security.auth.module.LdapLoginModule REQUIRED \
    userProvider="ldap://127.0.0.1:10389" authIdentity="uid={USERNAME},ou=people,dc=example,dc=com" \
    debug=true useSSL=false ;
};
```

Is it possible to specify custom authentication settings by using JVM argument `-Dh2auth.configurationFile={urlOfH2Auth.xml}`. Here an example of h2auth.xml file content:

```
<h2Auth allowUserRegistration="false" createMissingRoles="true">

    <!-- realm: DUMMY authenticate users named DUMMY[0-9] with a static password -->
    <realm name="DUMMY"
    validatorClass="org.h2.security.auth.impl.FixedPasswordCredentialsValidator">
        <property name="userNamePattern" value="DUMMY[0-9]" />
        <property name="password" value="mock" />
    </realm>

    <!-- realm LDAPEXAMPLE:perform credentials validation on LDAP -->
    <realm name="LDAPEXAMPLE"
    validatorClass="org.h2.security.auth.impl.LdapCredentialsValidator">
        <property name="bindDnPattern" value="uid=%u,ou=people,dc=example,dc=com" />
        <property name="host" value="127.0.0.1" />
        <property name="port" value="10389" />
        <property name="secure" value="false" />
    </realm>

    <!-- realm JAAS: perform credentials validation by using JAAS api -->
    <realm name="JAAS"
    validatorClass="org.h2.security.auth.impl.JaasCredentialsValidator">
        <property name="appName" value="H2" />
    </realm>

    <!--Assign to each user role @{REALM} -->
    <userToRolesMapper class="org.h2.security.auth.impl.AssignRealmNameRole"/>

    <!--Assign to each user role REMOTEUSER -->
    <userToRolesMapper class="org.h2.security.auth.impl.StaticRolesMapper">
        <property name="roles" value="REMOTEUSER"/>
    </userToRolesMapper>
</h2Auth>
```

Custom credentials validators must implement the interface `org.h2.api.CredentialsValidator`

Custom criteria for role assignments must implement the interface `org.h2.api.UserToRoleMapper`
