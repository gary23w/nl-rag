---
title: "Apache JMeter (part 5/8)"
source: https://jmeter.apache.org/usermanual/component_reference.html
domain: jmeter
license: CC-BY-SA-4.0
tags: jmeter apache, load testing, performance testing, test plan
fetched: 2026-07-02
part: 5/8
---

## HTTP Authorization Manager

The Authorization Manager lets you specify one or more user logins for web pages that are restricted using server authentication. You see this type of authentication when you use your browser to access a restricted page, and your browser displays a login dialog box. JMeter transmits the login information when it encounters this type of page.

The Authorization headers may not be shown in the Tree View Listener "Request" tab. The Java implementation does pre-emptive authentication, but it does not return the Authorization header when JMeter fetches the headers. The HttpComponents (HC 4.5.X) implementation defaults to pre-emptive since 3.2 and the header will be shown. To disable this, set the values as below, in which case authentication will only be performed in response to a challenge.

In the file jmeter.properties set httpclient4.auth.preemptive=false

Note: the above settings only apply to the HttpClient sampler.

When looking for a match against a URL, JMeter checks each entry in turn, and stops when it finds the first match. Thus the most specific URLs should appear first in the list, followed by less specific ones. Duplicate URLs will be ignored. If you want to use different usernames/passwords for different threads, you can use variables. These can be set up using a

CSV Data Set Config

Element (for example).

If there is more than one Authorization Manager in the scope of a Sampler, there is currently no way to specify which one is to be used.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Clear auth on each iteration?

Used by Kerberos authentication. If checked, authentication will be done on each iteration of Main Thread Group loop even if it has already been done in a previous one. This is usually useful if each main thread group iteration represents behaviour of one Virtual User.

Yes

Base URL

A partial or complete URL that matches one or more HTTP Request URLs. As an example, say you specify a Base URL of "

http://localhost/restricted/

" with a

Username

of "

jmeter

" and a

Password

of "

jmeter

". If you send an HTTP request to the URL "

http://localhost/restricted/ant/myPage.html

", the Authorization Manager sends the login information for the user named, "

jmeter

".

Yes

Username

The username to authorize.

Yes

Password

The password for the user. (N.B. this is stored unencrypted in the test plan)

Yes

Domain

The domain to use for NTLM.

No

Realm

The realm to use for NTLM.

No

Mechanism

Type of authentication to perform. JMeter can perform different types of authentications based on used Http Samplers:

**Java**

BASIC

**HttpClient 4**

BASIC

,

DIGEST

and

Kerberos

No

The Realm only applies to the HttpClient sampler.

Kerberos Configuration:

To configure Kerberos you need to setup at least two JVM system properties:

- -Djava.security.krb5.conf=krb5.conf
- -Djava.security.auth.login.config=jaas.conf

You can also configure those two properties in the file bin/system.properties. Look at the two sample configuration files (krb5.conf and jaas.conf) located in the JMeter bin folder for references to more documentation, and tweak them to match your Kerberos configuration.

Delegation of credentials is disabled by default for SPNEGO. If you want to enable it, you can do so by setting the property kerberos.spnego.delegate_cred to true.

When generating a SPN for Kerberos SPNEGO authentication IE and Firefox will omit the port number from the URL. Chrome has an option (--enable-auth-negotiate-port) to include the port number if it differs from the standard ones (80 and 443). That behavior can be emulated by setting the following JMeter property as below.

In jmeter.properties or user.properties, set:

- kerberos.spnego.strip_port=false

Controls:

- Add Button - Add an entry to the authorization table.
- Delete Button - Delete the currently selected table entry.
- Load Button - Load a previously saved authorization table and add the entries to the existing authorization table entries.
- Save As Button - Save the current authorization table to a file.

When you save the Test Plan, JMeter automatically saves all of the authorization table entries - including any passwords, which are not encrypted.

Authorization Example

¶

Download this example. In this example, we created a Test Plan on a local server that sends three HTTP requests, two requiring a login and the other is open to everyone. See figure 10 to see the makeup of our Test Plan. On our server, we have a restricted directory named, "secret", which contains two files, "index.html" and "index2.html". We created a login id named, "kevin", which has a password of "spot". So, in our Authorization Manager, we created an entry for the restricted directory and a username and password (see figure 11). The two HTTP requests named "SecretPage1" and "SecretPage2" make requests to "/secret/index.html" and "/secret/index2.html". The other HTTP request, named "NoSecretPage" makes a request to "/index.html".

When we run the Test Plan, JMeter looks in the Authorization table for the URL it is requesting. If the Base URL matches the URL, then JMeter passes this information along with the request.

You can download the Test Plan, but since it is built as a test for our local server, you will not be able to run it. However, you can use it as a reference in constructing your own Test Plan.

^


## HTTP Cache Manager

The HTTP Cache Manager is used to add caching functionality to HTTP requests within its scope to simulate browser cache feature. Each Virtual User thread has its own Cache. By default, Cache Manager will store up to 5000 items in cache per Virtual User thread, using LRU algorithm. Use property "maxSize" to modify this value. Note that the more you increase this value the more HTTP Cache Manager will consume memory, so be sure to adapt the -Xmx JVM option accordingly.

If a sample is successful (i.e. has response code 2xx) then the Last-Modified and Etag (and Expired if relevant) values are saved for the URL. Before executing the next sample, the sampler checks to see if there is an entry in the cache, and if so, the If-Last-Modified and If-None-Match conditional headers are set for the request.

Additionally, if the "Use Cache-Control/Expires header" option is selected, then the Cache-Control/Expires value is checked against the current time. If the request is a GET request, and the timestamp is in the future, then the sampler returns immediately, without requesting the URL from the remote server. This is intended to emulate browser behaviour. Note that if Cache-Control header is "no-cache", the response will be stored in cache as pre-expired, so will generate a conditional GET request. If Cache-Control has any other value, the "max-age" expiry option is processed to compute entry lifetime, if missing then expire header will be used, if also missing entry will be cached as specified in RFC 2616 section 13.2.4 using Last-Modified time and response Date.

If the requested document has not changed since it was cached, then the response body will be empty. Likewise if the

Expires

date is in the future. This may cause problems for Assertions.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Clear cache each iteration

If selected, then the cache is cleared at the start of the thread.

Yes

Use Cache Control/Expires header when processing GET requests

See description above.

Yes

Max Number of elements in cache

See description above.

Yes

^

The Cookie Manager element has two functions: First, it stores and sends cookies just like a web browser. If you have an HTTP Request and the response contains a cookie, the Cookie Manager automatically stores that cookie and will use it for all future requests to that particular web site. Each JMeter thread has its own "cookie storage area". So, if you are testing a web site that uses a cookie for storing session information, each JMeter thread will have its own session. Note that such cookies do not appear on the Cookie Manager display, but they can be seen using the View Results Tree Listener.

JMeter checks that received cookies are valid for the URL. This means that cross-domain cookies are not stored. If you have bugged behaviour or want Cross-Domain cookies to be used, define the JMeter property "CookieManager.check.cookies=false".

Received Cookies can be stored as JMeter thread variables. To save cookies as variables, define the property "CookieManager.save.cookies=true". Also, cookies names are prefixed with "COOKIE_" before they are stored (this avoids accidental corruption of local variables) To revert to the original behaviour, define the property "CookieManager.name.prefix= " (one or more spaces). If enabled, the value of a cookie with the name TEST can be referred to as ${COOKIE_TEST}.

Second, you can manually add a cookie to the Cookie Manager. However, if you do this, the cookie will be shared by all JMeter threads.

Note that such Cookies are created with an Expiration time far in the future

Cookies with null values are ignored by default. This can be changed by setting the JMeter property: CookieManager.delete_null_cookies=false. Note that this also applies to manually defined cookies - any such cookies will be removed from the display when it is updated. Note also that the cookie name must be unique - if a second cookie is defined with the same name, it will replace the first.

If there is more than one Cookie Manager in the scope of a Sampler, there is currently no way to specify which one is to be used. Also, a cookie stored in one cookie manager is not available to any other manager, so use multiple Cookie Managers with care.

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Clear Cookies each Iteration

If selected, all server-defined cookies are cleared each time the main Thread Group loop is executed. Any cookie defined in the GUI are not cleared.

Yes

Cookie Policy

The cookie policy that will be used to manage the cookies. "

standard

" is the default since 3.0, and should work in most cases. See

Cookie specifications

and

CookieSpec implementations

[Note: "

ignoreCookies

" is equivalent to omitting the CookieManager.]

Yes

Implementation

HC4CookieHandler

(HttpClient 4.5.X API). Default is

HC4CookieHandler

since 3.0.

[Note: If you have a website to test with IPv6 address, choose

HC4CookieHandler

(IPv6 compliant)]

Yes

User-Defined Cookies

This gives you the opportunity to use hardcoded cookies that will be used by all threads during the test execution.

The "

domain

" is the hostname of the server (without

http://

); the port is currently ignored.

No (discouraged, unless you know what you're doing)

Add Button

Add an entry to the cookie table.

N/A

Delete Button

Delete the currently selected table entry.

N/A

Load Button

Load a previously saved cookie table and add the entries to the existing cookie table entries.

N/A

Save As Button

Save the current cookie table to a file (does not save any cookies extracted from HTTP Responses).

N/A

^


## HTTP Request Defaults

This element lets you set default values that your HTTP Request controllers use. For example, if you are creating a Test Plan with 25 HTTP Request controllers and all of the requests are being sent to the same server, you could add a single HTTP Request Defaults element with the "Server Name or IP" field filled in. Then, when you add the 25 HTTP Request controllers, leave the "Server Name or IP" field empty. The controllers will inherit this field value from the HTTP Request Defaults element.

All port values are treated equally; a sampler that does not specify a port will use the HTTP Request Defaults port, if one is provided.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Server

Domain name or IP address of the web server. E.g.

www.example.com

. [Do not include the

http://

prefix.

No

Port

Port the web server is listening to.

No

Connect Timeout

Connection Timeout. Number of milliseconds to wait for a connection to open.

No

Response Timeout

Response Timeout. Number of milliseconds to wait for a response.

No

Implementation

Java

,

HttpClient4

. If not specified the default depends on the value of the JMeter property

jmeter.httpsampler

, failing that, the

Java

implementation is used.

No

Protocol

HTTP

or

HTTPS

.

No

Content encoding

The encoding to be used for the request.

No

Path

The path to resource (for example,

/servlets/myServlet

). If the resource requires query string parameters, add them below in the "

Send Parameters With the Request

" section. Note that the path is the default for the full path, not a prefix to be applied to paths specified on the HTTP Request screens.

No

Send Parameters With the Request

The query string will be generated from the list of parameters you provide. Each parameter has a

name

and

value

. The query string will be generated in the correct fashion, depending on the choice of "

Method

" you made (i.e. if you chose

GET

, the query string will be appended to the URL, if

POST

, then it will be sent separately). Also, if you are sending a file using a multipart form, the query string will be created using the multipart form specifications.

No

Server (proxy)

Hostname or IP address of a proxy server to perform request. [Do not include the

http://

prefix.]

No

Port

Port the proxy server is listening to.

No, unless proxy hostname is specified

Username

(Optional) username for proxy server.

No

Password

(Optional) password for proxy server. (N.B. this is stored unencrypted in the test plan)

No

Retrieve All Embedded Resources from HTML Files

Tell JMeter to parse the HTML file and send HTTP/HTTPS requests for all images, Java applets, JavaScript files, CSSs, etc. referenced in the file.

No

Use concurrent pool

Use a pool of concurrent connections to get embedded resources.

No

Size

Pool size for concurrent connections used to get embedded resources.

No

URLs must match:

If present, this must be a regular expression that is used to match against any embedded URLs found. So if you only want to download embedded resources from

http://example.invalid/

, use the expression:

http://example\.invalid/.*

No

URLs must not match:

If present, this must be a regular expression that is used to filter out any embedded URLs found. So if you don't want to download PNG or SVG files from any source, use the expression:

.*\.(?i:svg|png)

No

Note: radio buttons only have two states - on or off. This makes it impossible to override settings consistently - does off mean off, or does it mean use the current default? JMeter uses the latter (otherwise defaults would not work at all). So if the button is off, then a later element can set it on, but if the button is on, a later element cannot set it off.

^


## HTTP Header Manager

The Header Manager lets you add or override HTTP request headers.

**JMeter now supports multiple Header Managers**. The header entries are merged to form the list for the sampler. If an entry to be merged matches an existing header name, it replaces the previous entry. This allows one to set up a default set of headers, and apply adjustments to particular samplers. Note that an empty value for a header does not remove an existing header, it justs replace its value.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Name (Header)

Name of the request header. Two common request headers you may want to experiment with are "

User-Agent

" and "

Referer

".

No (You should have at least one, however)

Value

Request header value.

No (You should have at least one, however)

Add Button

Add an entry to the header table.

N/A

Delete Button

Delete the currently selected table entry.

N/A

Load Button

Load a previously saved header table and add the entries to the existing header table entries.

N/A

Save As Button

Save the current header table to a file.

N/A

Header Manager example

¶

Download this example. In this example, we created a Test Plan that tells JMeter to override the default "User-Agent" request header and use a particular Internet Explorer agent string instead. (see figures 12 and 13).

^


## Java Request Defaults

The Java Request Defaults component lets you set default values for Java testing. See the Java Request.

^


## JDBC Connection Configuration

Creates a database connection (used by

JDBC Request

Sampler) from the supplied JDBC Connection settings. The connection may be optionally pooled between threads. Otherwise each thread gets its own connection. The connection configuration name is used by the JDBC Sampler to select the appropriate connection. The used pool is DBCP, see

BasicDataSource Configuration Parameters

### Parameters

Attribute

Description

Required

Name

Descriptive name for the connection configuration that is shown in the tree.

No

Variable Name for created pool

The name of the variable the connection is tied to. Multiple connections can be used, each tied to a different variable, allowing JDBC Samplers to select the appropriate connection.

Each name must be different. If there are two configuration elements using the same name, only one will be saved. JMeter logs a message if a duplicate name is detected.

Yes

Max Number of Connections

Maximum number of connections allowed in the pool. In most cases,

set this to zero (0)

. This means that each thread will get its own pool with a single connection in it, i.e. the connections are not shared between threads.

If you really want to use shared pooling (why?), then set the max count to the same as the number of threads to ensure threads don't wait on each other.

Yes

Max Wait (ms)

Pool throws an error if the timeout period is exceeded in the process of trying to retrieve a connection, see

BasicDataSource.html#getMaxWaitMillis

Yes

Time Between Eviction Runs (ms)

The number of milliseconds to sleep between runs of the idle object evictor thread. When non-positive, no idle object evictor thread will be run. (Defaults to "

60000

", 1 minute). See

BasicDataSource.html#getTimeBetweenEvictionRunsMillis

Yes

Auto Commit

Turn auto commit on or off for the connections.

Yes

Transaction isolation

Transaction isolation level

Yes

Pool Prepared Statements

Max number of Prepared Statements to pool per connection.

"-1

" disables the pooling and "

0

" means unlimited number of Prepared Statements to pool. (Defaults to "

-1

")

Yes

Preinit Pool

The connection pool can be initialized instantly. If set to

False

(default), the JDBC request samplers using this pool might measure higher response times for the first queries – as the connection establishment time for the whole pool is included.

No

Init SQL statements separated by new line

A Collection of SQL statements that will be used to initialize physical connections when they are first created. These statements are executed only once - when the configured connection factory creates the connection.

No

Test While Idle

Test idle connections of the pool, see

BasicDataSource.html#getTestWhileIdle

. Validation Query will be used to test it.

Yes

Soft Min Evictable Idle Time(ms)

Minimum amount of time a connection may sit idle in the pool before it is eligible for eviction by the idle object evictor, with the extra condition that at least

minIdle

connections remain in the pool. See

BasicDataSource.html#getSoftMinEvictableIdleTimeMillis

. Defaults to 5000 (5 seconds)

Yes

Validation Query

A simple query used to determine if the database is still responding. This defaults to the '

isValid()

' method of the jdbc driver, which is suitable for many databases. However some may require a different query; for example Oracle something like '

SELECT 1 FROM DUAL

' could be used.

The list of the validation queries can be configured with jdbc.config.check.query property and are by default:

**hsqldb**

select 1 from INFORMATION_SCHEMA.SYSTEM_USERS

**Oracle**

select 1 from dual

**DB2**

select 1 from sysibm.sysdummy1

**MySQL or MariaDB**

select 1

**Microsoft SQL Server (MS JDBC driver)**

select 1

**PostgreSQL**

select 1

**Ingres**

select 1

**Derby**

values 1

**H2**

select 1

**Firebird**

select 1 from rdb$database

**Exasol**

select 1

The list come from

stackoverflow entry on different database validation queries

and it can be incorrect

Note this validation query is used on pool creation to validate it even if "

Test While Idle

" suggests query would only be used on idle connections. This is DBCP behaviour.

No

Database URL

JDBC Connection string for the database.

Yes

JDBC Driver class

Fully qualified name of driver class. (Must be in JMeter's classpath - easiest to copy

.jar

file into JMeter's

/lib

directory).

The list of the preconfigured jdbc driver classes can be configured with jdbc.config.jdbc.driver.class property and are by default:

**hsqldb**

org.hsqldb.jdbc.JDBCDriver

**Oracle**

oracle.jdbc.OracleDriver

**DB2**

com.ibm.db2.jcc.DB2Driver

**MySQL**

com.mysql.jdbc.Driver

**Microsoft SQL Server (MS JDBC driver)**

com.microsoft.sqlserver.jdbc.SQLServerDriver or com.microsoft.jdbc.sqlserver.SQLServerDriver

**PostgreSQL**

org.postgresql.Driver

**Ingres**

com.ingres.jdbc.IngresDriver

**Derby**

org.apache.derby.jdbc.ClientDriver

**H2**

org.h2.Driver

**Firebird**

org.firebirdsql.jdbc.FBDriver

**Apache Derby**

org.apache.derby.jdbc.ClientDriver

**MariaDB**

org.mariadb.jdbc.Driver

**SQLite**

org.sqlite.JDBC

**Sybase AES**

net.sourceforge.jtds.jdbc.Driver

**Exasol**

com.exasol.jdbc.EXADriver

Yes

Username

Name of user to connect as.

No

Password

Password to connect with. (N.B. this is stored unencrypted in the test plan)

No

Connection Properties

Connection Properties to set when establishing connection (like

internal_logon=sysdba

for Oracle for example)

No

Different databases and JDBC drivers require different JDBC settings. The Database URL and JDBC Driver class are defined by the provider of the JDBC implementation.

Some possible settings are shown below. Please check the exact details in the JDBC driver documentation.

If JMeter reports No suitable driver, then this could mean either:

- The driver class was not found. In this case, there will be a log message such as DataSourceElement: Could not load driver: {classname} java.lang.ClassNotFoundException: {classname}
- The driver class was found, but the class does not support the connection string. This could be because of a syntax error in the connection string, or because the wrong classname was used.

If the database server is not running or is not accessible, then JMeter will report a java.net.ConnectException.

Some examples for databases and their parameters are given below.

**MySQL**

**Driver class**

com.mysql.jdbc.Driver

**Database URL**

jdbc:mysql://host[:port]/dbname

**PostgreSQL**

**Driver class**

org.postgresql.Driver

**Database URL**

jdbc:postgresql:{dbname}

**Oracle**

**Driver class**

oracle.jdbc.OracleDriver

**Database URL**

jdbc:oracle:thin:@//host:port/service

OR

jdbc:oracle:thin:@(description=(address=(host={mc-name})(protocol=tcp)(port={port-no}))(connect_data=(sid={sid})))

**Ingress (2006)**

**Driver class**

ingres.jdbc.IngresDriver

**Database URL**

jdbc:ingres://host:port/db[;attr=value]

**Microsoft SQL Server (MS JDBC driver)**

**Driver class**

com.microsoft.sqlserver.jdbc.SQLServerDriver

**Database URL**

jdbc:sqlserver://host:port;DatabaseName=dbname

**Apache Derby**

**Driver class**

org.apache.derby.jdbc.ClientDriver

**Database URL**

jdbc:derby://server[:port]/databaseName[;URLAttributes=value[;…]]

**MariaDB**

**Driver class**

org.mariadb.jdbc.Driver

**Database URL**

jdbc:mariadb://host[:port]/dbname[;URLAttributes=value[;…]]

**Exasol (see also JDBC driver documentation)**

**Driver class**

com.exasol.jdbc.EXADriver

**Database URL**

jdbc:exa:host[:port][;schema=SCHEMA_NAME][;prop_x=value_x]

The above may not be correct - please check the relevant JDBC driver documentation.

^


## Keystore Configuration

The Keystore Config Element lets you configure how Keystore will be loaded and which keys it will use. This component is typically used in HTTPS scenarios where you don't want to take into account keystore initialization into account in response time.

To use this element, you need to setup first a Java Key Store with the client certificates you want to test, to do that:

1. Create your certificates either with Java keytool utility or through your PKI
2. If created by PKI, import your keys in Java Key Store by converting them to a format acceptable by JKS
3. Then reference the keystore file through the two JVM properties (or add them in system.properties):
  - -Djavax.net.ssl.keyStore=path_to_keystore
  - -Djavax.net.ssl.keyStorePassword=password_of_keystore

To use PKCS11 as the source for the store, you need to set javax.net.ssl.keyStoreType to PKCS11 and javax.net.ssl.keyStore to NONE.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Preload

Whether or not to preload Keystore. Setting it to

true

is usually the best option.

Yes

Variable name holding certificate alias

Variable name that will contain the alias to use for authentication by client certificate. Variable value will be filled from CSV Data Set for example. In the screenshot, "

certificat_ssl

" will also be a variable in CSV Data Set. Defaults to

clientCertAliasVarName

False

Alias Start Index

The index of the first key to use in Keystore, 0-based.

Yes

Alias End Index

The index of the last key to use in Keystore, 0-based. When using "

Variable name holding certificate alias

" ensure it is large enough so that all keys are loaded at startup. Default to -1 which means load all.

Yes

To make JMeter use more than one certificate you need to ensure that:

- https.use.cached.ssl.context=false is set in jmeter.properties or user.properties
- You use HTTPClient 4 implementation for HTTP Request

^


## Login Config Element

The Login Config Element lets you add or override username and password settings in samplers that use username and password as part of their setup.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Username

The default username to use.

No

Password

The default password to use. (N.B. this is stored unencrypted in the test plan)

No

^


## LDAP Request Defaults

The LDAP Request Defaults component lets you set default values for LDAP testing. See the LDAP Request.

^


## LDAP Extended Request Defaults

The LDAP Extended Request Defaults component lets you set default values for extended LDAP testing. See the LDAP Extended Request.

^


## TCP Sampler Config

The TCP Sampler Config provides default data for the TCP Sampler

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

TCPClient classname

Name of the TCPClient class. Defaults to the property

tcp.handler

, failing that

TCPClientImpl

.

No

ServerName or IP

Name or IP of TCP server

Port Number

Port to be used

Re-use connection

If selected, the connection is kept open. Otherwise it is closed when the data has been read.

Yes

Close connection

If selected, the connection will be closed after running the sampler.

Yes

SO_LINGER

Enable/disable

SO_LINGER

with the specified linger time in seconds when a socket is created. If you set "

SO_LINGER

" value as

0

, you may prevent large numbers of sockets sitting around with a

TIME_WAIT

status.

No

End of line(EOL) byte value

Byte value for end of line, set this to a value outside the range

-128

to

+127

to skip EOL checking. You may set this in

jmeter.properties

file as well with the

tcp.eolByte

property. If you set this in TCP Sampler Config and in

jmeter.properties

file at the same time, the setting value in the TCP Sampler Config will be used.

No

Connect Timeout

Connect Timeout (milliseconds, 0 disables).

No

Response Timeout

Response Timeout (milliseconds, 0 disables).

No

Set Nodelay

Should the nodelay property be set?

Text to Send

Text to be sent

^


## User Defined Variables

The User Defined Variables element lets you define an **initial set of variables**, just as in the Test Plan. Note that all the UDV elements in a test plan - no matter where they are - are processed at the start. So you cannot reference variables which are defined as part of a test run, e.g. in a Post-Processor.

**UDVs should not be used with functions that generate different results each time they are called. Only the result of the first function call will be saved in the variable.** However, UDVs can be used with functions such as __P(), for example:

```
HOST      ${__P(host,localhost)}
```

which would define the variable "HOST" to have the value of the JMeter property "host", defaulting to "localhost" if not defined.

For defining variables during a test run, see User Parameters. UDVs are processed in the order they appear in the Plan, from top to bottom.

For simplicity, it is suggested that UDVs are placed only at the start of a Thread Group (or perhaps under the Test Plan itself).

Once the Test Plan and all UDVs have been processed, the resulting set of variables is copied to each thread to provide the initial set of variables.

If a runtime element such as a User Parameters Pre-Processor or Regular Expression Extractor defines a variable with the same name as one of the UDV variables, then this will replace the initial value, and all other test elements in the thread will see the updated value.

If you have more than one Thread Group, make sure you use different names for different values, as UDVs are shared between Thread Groups. Also, the variables are not available for use until after the element has been processed, so you cannot reference variables that are defined in the same element. You can reference variables defined in earlier UDVs or on the Test Plan.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

User Defined Variables

Variable name/value pairs. The string under the "

Name

" column is what you'll need to place inside the brackets in

${…}

constructs to use the variables later on. The whole

${…}

will then be replaced by the string in the "

Value

" column.

^


## Random Variable

The Random Variable Config Element is used to generate random numeric strings and store them in variable for use later. It's simpler than using User Defined Variables together with the __Random() function.

The output variable is constructed by using the random number generator, and then the resulting number is formatted using the format string. The number is calculated using the formula minimum+Random.nextInt(maximum-minimum+1). Random.nextInt() requires a positive integer. This means that maximum-minimum - i.e. the range - must be less than 2147483647, however the minimum and maximum values can be any long values so long as the range is OK.

As the random value is evaluated at the start of each iteration, it is probably not a good idea to use a variable other than a property as a value for the minimum or maximum. It would be zero on the first iteration.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Yes

Variable Name

The name of the variable in which to store the random string.

Yes

Format String

The

java.text.DecimalFormat

format string to be used. For example "

000

" which will generate numbers with at least 3 digits, or "

USER_000

" which will generate output of the form

USER_nnn

. If not specified, the default is to generate the number using

Long.toString()

No

Minimum Value

The minimum value (

long

) of the generated random number.

Yes

Maximum Value

The maximum value (

long

) of the generated random number.

Yes

Random Seed

The seed for the random number generator. If you use the same seed value with Per Thread set to

true

, you will get the same value for each Thread as per

Random

class. If no seed is set, Default constructor of Random will be used.

No

Per Thread(User)?

If

False

, the generator is shared between all threads in the thread group. If

True

, then each thread has its own random generator.

Yes

^


## Counter

Allows the user to create a counter that can be referenced anywhere in the Thread Group. The counter config lets the user configure a starting point, a maximum, and the increment. The counter will loop from the start to the max, and then start over with the start, continuing on like that until the test is ended.

The counter uses a long to store the value, so the range is from -2^63 to 2^63-1.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Starting value

The starting value for the counter. The counter will equal this value during the first iteration (defaults to 0).

No

Increment

How much to increment the counter by after each iteration (defaults to 0, meaning no increment).

Yes

Maximum value

If the counter exceeds the maximum, then it is reset to the

Starting value

. Default is

Long.MAX_VALUE

No

Format

Optional format, e.g.

000

will format as

001

,

002

, etc. This is passed to

DecimalFormat

, so any valid formats can be used. If there is a problem interpreting the format, then it is ignored. [The default format is generated using

Long.toString()

]

No

Exported Variable Name

This will be the variable name under which the counter value is available. If you name it

counterA

, you can then access it using

${counterA}

as explained in

user-defined values

(By default, it creates an empty string variable that can be accessed using

${}

but this is highly discouraged)

No

Track Counter Independently for each User

In other words, is this a global counter, or does each user get their own counter? If unchecked, the counter is global (i.e., user #1 will get value "

1

", and user #2 will get value "

2

" on the first iteration). If checked, each user has an independent counter.

No

Reset counter on each Thread Group Iteration

This option is only available when counter is tracked per User, if checked, counter will be reset to

Start

value on each Thread Group iteration. This can be useful when Counter is inside a Loop Controller.

No

^


## Simple Config Element

The Simple Config Element lets you add or override arbitrary values in samplers. You can choose the name of the value and the value itself. Although some adventurous users might find a use for this element, it's here primarily for developers as a basic GUI that they can use while developing new JMeter components.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Yes

Parameter Name

The name of each parameter. These values are internal to JMeter's workings and are not generally documented. Only those familiar with the code will know these values.

Yes

Parameter Value

The value to apply to that parameter.

Yes

^


## MongoDB Source Config (DEPRECATED)

Creates a MongoDB connection (used by

MongoDB Script

Sampler) from the supplied Connection settings. Each thread gets its own connection. The connection configuration name is used by the JDBC Sampler to select the appropriate connection.

You can then access com.mongodb.DB object in Beanshell or JSR223 Test Elements through the element MongoDBHolder using this code

```
import com.mongodb.DB;
import org.apache.jmeter.protocol.mongodb.config.MongoDBHolder;
DB db = MongoDBHolder.getDBFromSource("value of property MongoDB Source",
            "value of property Database Name");
…
    
```

### Parameters

Attribute

Description

Required

Name

Descriptive name for the connection configuration that is shown in the tree.

No

Server Address List

Mongo DB Servers

Yes

MongoDB Source

The name of the variable the connection is tied to.

Each name must be different. If there are two configuration elements using the same name, only one will be saved.

Yes

Keep Trying

If

true

, the driver will keep trying to connect to the same server in case that the socket cannot be established.

There is maximum amount of time to keep retrying, which is 15s by default.

This can be useful to avoid some exceptions being thrown when a server is down temporarily by blocking the operations.

It can also be useful to smooth the transition to a new primary node (so that a new primary node is elected within the retry time).

Note that when using this flag

- for a replica set, the driver will try to connect to the old primary node for that time, instead of failing over to the new one right away
- this does not prevent exception from being thrown in read/write operations on the socket, which must be handled by application.

Even if this flag is false, the driver already has mechanisms to automatically recreate broken connections and retry the read operations.

Default is

false

.

No

Maximum connections per host

No

Connection timeout

The connection timeout in milliseconds.

It is used solely when establishing a new connection

Socket.connect(java.net.SocketAddress, int)

Default is

0

and means no timeout.

No

Maximum retry time

The maximum amount of time in milliseconds to spend retrying to open connection to the same server.

Default is

0

, which means to use the default 15s if

autoConnectRetry

is on.

No

Maximum wait time

The maximum wait time in milliseconds that a thread may wait for a connection to become available.

Default is

120,000

.

No

Socket timeout

The socket timeout in milliseconds It is used for I/O socket read and write operations

Socket.setSoTimeout(int)

Default is

0

and means no timeout.

No

Socket keep alive

This flag controls the socket keep alive feature that keeps a connection alive through firewalls

Socket.setKeepAlive(boolean)

Default is

false

.

No

ThreadsAllowedToBlockForConnectionMultiplier

This multiplier, multiplied with the connectionsPerHost setting, gives the maximum number of threads that may be waiting for a connection to become available from the pool.

All further threads will get an exception right away.

For example if

connectionsPerHost

is

10

and

threadsAllowedToBlockForConnectionMultiplier

is

5

, then up to 50 threads can wait for a connection.

Default is

5

.

No

Write Concern: Safe

If

true

the driver will use a

WriteConcern

of

WriteConcern.SAFE

for all operations.

If

w

,

wtimeout

,

fsync

or

j

are specified, this setting is ignored.

Default is

false

.

No

Write Concern: Fsync

The

fsync

value of the global

WriteConcern

.

Default is

false

.

No

Write Concern: Wait for Journal

The

j

value of the global

WriteConcern

.

Default is

false

.

No

Write Concern: Wait for servers

The

w

value of the global

WriteConcern

.

Default is

0

.

No

Write Concern: Wait timeout

The

wtimeout

value of the global

WriteConcern

.

Default is

0

.

No

Write Concern: Continue on error

If batch inserts should continue after the first error

No

^

^


## Bolt Connection Configuration

Creates a Bolt connection pool (used by

Bolt Request

Sampler) from the supplied Connection settings.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Comments

Free text for additional details.

No

Bolt URI

The database URI.

Yes

Username

User account.

No

Password

User credentials.

No

Connection Pool Max Size

Max size of the Neo4j driver Bolt connection pool. Raise the value if running large number of concurrent threads, so that JMeter threads are not blocked waiting for a connection to be released to the pool.

Yes

^

^

# 18.5 Assertions

Assertions are used to perform additional checks on samplers, and are processed after **every sampler** in the same scope. To ensure that an Assertion is applied only to a particular sampler, add it as a child of the sampler.

Note: Unless documented otherwise, Assertions are not applied to sub-samples (child samples) - only to the parent sample. In the case of JSR223 and BeanShell Assertions, the script can retrieve sub-samples using the method

prev.getSubResults()

which returns an array of SampleResults. The array will be empty if there are none.

Assertions can be applied to either the main sample, the sub-samples or both. The default is to apply the assertion to the main sample only. If the Assertion supports this option, then there will be an entry on the GUI which looks like the following:

or the following

If a sub-sampler fails and the main sample is successful, then the main sample will be set to failed status and an Assertion Result will be added. If the JMeter variable option is used, it is assumed to relate to the main sample, and any failure will be applied to the main sample only.

The variable

JMeterThread.last_sample_ok

is updated to "

true

" or "

false

" after all assertions for a sampler have been run.


## Response Assertion

The response assertion control panel lets you add pattern strings to be compared against various fields of the request or response. The pattern strings are:

- Contains, Matches: Perl5-style regular expressions
- Equals, Substring: plain text, case-sensitive

A summary of the pattern matching characters can be found at ORO Perl5 regular expressions.

You can also choose whether the strings will be expected to **match** the entire response, or if the response is only expected to **contain** the pattern. You can attach multiple assertions to any controller for additional flexibility.

Note that the pattern string should not include the enclosing delimiters, i.e. use Price: \d+ not /Price: \d+/.

By default, the pattern is in multi-line mode, which means that the "." meta-character does not match newline. In multi-line mode, "^" and "$" match the start or end of any line anywhere within the string - not just the start and end of the entire string. Note that \s does match new-line. Case is also significant. To override these settings, one can use the *extended regular expression* syntax. For example:

**(?i)**

ignore case

**(?s)**

treat target as single line, i.e. "

.

" matches new-line

**(?is)**

both the above

These can be used anywhere within the expression and remain in effect until overridden. E.g.

**(?i)apple(?-i) Pie**

matches "

ApPLe Pie

", but not "

ApPLe pIe

"

**(?s)Apple.+?Pie**

matches

Apple

followed by

Pie

, which may be on a subsequent line.

**Apple(?s).+?Pie**

same as above, but it's probably clearer to use the

(?s)

at the start.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Apply to:

This is for use with samplers that can generate sub-samples, e.g. HTTP Sampler with embedded resources, Mail Reader or samples generated by the Transaction Controller.

- Main sample only - only applies to the main sample
- Sub-samples only - only applies to the sub-samples
- Main sample and sub-samples - applies to both.
- JMeter Variable Name to use - assertion is to be applied to the contents of the named variable

Yes

Field to Test

Instructs JMeter which field of the Request or Response to test.

- Text Response - the response text from the server, i.e. the body, excluding any HTTP headers.
- Request data - the request text sent to the server, i.e. the body, excluding any HTTP headers.
- Response Code - e.g. 200
- Response Message - e.g. OK
- Response Headers, including Set-Cookie headers (if any)
- Request Headers
- URL sampled
- Document (text) - the extract text from various type of documents via Apache Tika (see View Results Tree Document view section).

Yes

Ignore status

Instructs JMeter to set the status to success initially.

The overall success of the sample is determined by combining the result of the assertion with the existing Response status. When the Ignore Status checkbox is selected, the Response status is forced to successful before evaluating the Assertion.

HTTP Responses with statuses in the

4xx

and

5xx

ranges are normally regarded as unsuccessful. The "

Ignore status

" checkbox can be used to set the status successful before performing further checks.

Note that this will have the effect of clearing any previous assertion failures, so make sure that this is only set on the first assertion.

Yes

Pattern Matching Rules

Indicates how the text being tested is checked against the pattern.

- Contains - true if the text contains the regular expression pattern
- Matches - true if the whole text matches the regular expression pattern
- Equals - true if the whole text equals the pattern string (case-sensitive)
- Substring - true if the text contains the pattern string (case-sensitive)

Equals

and

Substring

patterns are plain strings, not regular expressions.

NOT

may also be selected to invert the result of the check.

OR

Apply each assertion in OR combination (if 1 pattern to test matches, Assertion will be ok) instead of AND (All patterns must match so that Assertion is OK).

Yes

Patterns to Test

A list of patterns to be tested. Each pattern is tested separately. If a pattern fails, then further patterns are not checked. There is no difference between setting up one Assertion with multiple patterns and setting up multiple Assertions with one pattern each (assuming the other options are the same).

However, when the

Ignore Status

checkbox is selected, this has the effect of cancelling any previous assertion failures - so make sure that the

Ignore Status

checkbox is only used on the first Assertion.

Yes

Custom failure message

Lets you define the failure message that will replace the generated one

No

The pattern is a Perl5-style regular expression, but without the enclosing brackets.

Assertion Examples

¶

^


## Duration Assertion

The Duration Assertion tests that each response was received within a given amount of time. Any response that takes longer than the given number of milliseconds (specified by the user) is marked as a failed response.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Duration in Milliseconds

The maximum number of milliseconds each response is allowed before being marked as failed.

Yes

^
