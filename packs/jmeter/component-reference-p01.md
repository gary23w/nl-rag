---
title: "Apache JMeter (part 1/8)"
source: https://jmeter.apache.org/usermanual/component_reference.html
domain: jmeter
license: CC-BY-SA-4.0
tags: jmeter apache, load testing, performance testing, test plan
fetched: 2026-07-02
part: 1/8
---

# Apache JMeter

- < Prev
- Index
- Next >

- 18 Introduction
- 18.1 Samplers
  - FTP Request
  - HTTP Request
  - JDBC Request
  - Java Request
  - LDAP Request
  - LDAP Extended Request
  - Access Log Sampler
  - BeanShell Sampler
  - JSR223 Sampler
  - TCP Sampler
  - JMS Publisher
  - JMS Subscriber
  - JMS Point-to-Point
  - JUnit Request
  - Mail Reader Sampler
  - Flow Control Action (was: Test Action )
  - SMTP Sampler
  - OS Process Sampler
  - MongoDB Script (DEPRECATED)
  - Bolt Request
- 18.2 Logic Controllers
  - Simple Controller
  - Loop Controller
  - Once Only Controller
  - Interleave Controller
  - Random Controller
  - Random Order Controller
  - Throughput Controller
  - Runtime Controller
  - If Controller
  - While Controller
  - Switch Controller
  - ForEach Controller
  - Module Controller
  - Include Controller
  - Transaction Controller
  - Recording Controller
  - Critical Section Controller
- 18.3 Listeners
  - Sample Result Save Configuration
  - Graph Results
  - Assertion Results
  - View Results Tree
  - Aggregate Report
  - View Results in Table
  - Simple Data Writer
  - Aggregate Graph
  - Response Time Graph
  - Mailer Visualizer
  - BeanShell Listener
  - Summary Report
  - Save Responses to a file
  - JSR223 Listener
  - Generate Summary Results
  - Comparison Assertion Visualizer
  - Backend Listener
- 18.4 Configuration Elements
  - CSV Data Set Config
  - FTP Request Defaults
  - DNS Cache Manager
  - HTTP Authorization Manager
  - HTTP Cache Manager
  - HTTP Cookie Manager
  - HTTP Request Defaults
  - HTTP Header Manager
  - Java Request Defaults
  - JDBC Connection Configuration
  - Keystore Configuration
  - Login Config Element
  - LDAP Request Defaults
  - LDAP Extended Request Defaults
  - TCP Sampler Config
  - User Defined Variables
  - Random Variable
  - Counter
  - Simple Config Element
  - MongoDB Source Config (DEPRECATED)
  - Bolt Connection Configuration
- 18.5 Assertions
  - Response Assertion
  - Duration Assertion
  - Size Assertion
  - XML Assertion
  - BeanShell Assertion
  - MD5Hex Assertion
  - HTML Assertion
  - XPath Assertion
  - XPath2 Assertion
  - XML Schema Assertion
  - JSR223 Assertion
  - Compare Assertion
  - SMIME Assertion
  - JSON Assertion
  - JSON JMESPath Assertion
- 18.6 Timers
  - Constant Timer
  - Gaussian Random Timer
  - Uniform Random Timer
  - Constant Throughput Timer
  - Precise Throughput Timer
  - Synchronizing Timer
  - BeanShell Timer
  - JSR223 Timer
  - Poisson Random Timer
- 18.7 Pre Processors
  - HTML Link Parser
  - HTTP URL Re-writing Modifier
  - User Parameters
  - BeanShell PreProcessor
  - JSR223 PreProcessor
  - JDBC PreProcessor
  - RegEx User Parameters
  - Sample Timeout
- 18.8 Post-Processors
  - Regular Expression Extractor
  - CSS Selector Extractor (was: CSS/JQuery Extractor )
  - XPath2 Extractor
  - XPath Extractor
  - JSON JMESPath Extractor
  - Result Status Action Handler
  - BeanShell PostProcessor
  - JSR223 PostProcessor
  - JDBC PostProcessor
  - JSON Extractor
  - Boundary Extractor
- 18.9 Miscellaneous Features
  - Test Plan
  - Open Model Thread Group
  - Thread Group
  - WorkBench
  - SSL Manager
  - HTTP(S) Test Script Recorder (was: HTTP Proxy Server )
  - HTTP Mirror Server
  - Property Display
  - Debug Sampler
  - Debug PostProcessor
  - Test Fragment
  - setUp Thread Group
  - tearDown Thread Group

# 18 Introduction

Several test elements use JMeter properties to control their behaviour. These properties are normally resolved when the class is loaded. This generally occurs before the test plan starts, so it's not possible to change the settings by using the

__setProperty()

function.

# 18.1 Samplers

Samplers perform the actual work of JMeter. Each sampler (except Flow Control Action) generates one or more sample results. The sample results have various attributes (success/fail, elapsed time, data size etc.) and can be viewed in the various listeners.


## FTP Request

This controller lets you send an FTP "retrieve file" or "upload file" request to an FTP server. If you are going to send multiple requests to the same FTP server, consider using a

FTP Request Defaults

Configuration Element so you do not have to enter the same information for each FTP Request Generative Controller. When downloading a file, it can be stored on disk (Local File) or in the Response Data, or both.

Latency is set to the time it takes to login.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Server Name or IP

Domain name or IP address of the FTP server.

Yes

Port

Port to use. If this is

>0

, then this specific port is used, otherwise JMeter uses the default FTP port.

No

Remote File:

File to retrieve or name of destination file to upload.

Yes

Local File:

File to upload, or destination for downloads (defaults to remote file name).

Yes, if uploading (*)

Local File Contents:

Provides the contents for the upload, overrides the Local File property.

Yes, if uploading (*)

get(RETR) / put(STOR)

Whether to retrieve or upload a file.

Yes

Use Binary mode?

Check this to use Binary mode (default ASCII)

Yes

Save File in Response?

Whether to store contents of retrieved file in response data. If the mode is ASCII, then the contents will be visible in the

View Results Tree

.

Yes, if downloading

Username

FTP account username.

Usually

Password

FTP account password. N.B. This will be visible in the test plan.

Usually

See also:

- Assertions
- FTP Request Defaults
- Building an FTP Test Plan

^


## HTTP Request

This sampler lets you send an HTTP/HTTPS request to a web server. It also lets you control whether or not JMeter parses HTML files for images and other embedded resources and sends HTTP requests to retrieve them. The following types of embedded resource are retrieved:

- images
- applets
- stylesheets (CSS) and resources referenced from those files
- external scripts
- frames, iframes
- background images (body, table, TD, TR)
- background sound

The default parser is org.apache.jmeter.protocol.http.parser.LagartoBasedHtmlParser. This can be changed by using the property "htmlparser.className" - see jmeter.properties for details.

If you are going to send multiple requests to the same web server, consider using an HTTP Request Defaults Configuration Element so you do not have to enter the same information for each HTTP Request.

Or, instead of manually adding HTTP Requests, you may want to use JMeter's HTTP(S) Test Script Recorder to create them. This can save you time if you have a lot of HTTP requests or requests with many parameters.

**There are three different test elements used to define the samplers:**

**AJP/1.3 Sampler**

uses the Tomcat mod_jk protocol (allows testing of Tomcat in AJP mode without needing Apache httpd) The AJP Sampler does not support multiple file upload; only the first file will be used.

**HTTP Request**

this has an implementation drop-down box, which selects the HTTP protocol implementation to be used:

**Java**

uses the HTTP implementation provided by the JVM. This has some limitations in comparison with the HttpClient implementations - see below.

**HTTPClient4**

uses Apache HttpComponents HttpClient 4.x.

**Blank Value**

does not set implementation on HTTP Samplers, so relies on HTTP Request Defaults if present or on

jmeter.httpsampler

property defined in

jmeter.properties

**GraphQL HTTP Request**

this is a GUI variation of the

HTTP Request

to provide more convenient UI elements to view or edit GraphQL

Query

,

Variables

and

Operation Name

, while converting them into HTTP Arguments automatically under the hood using the same sampler. This hides or customizes the following UI elements as they are less convenient for or irrelevant to GraphQL over HTTP/HTTPS requests:

- **Method**: Only POST and GET methods are available conforming the GraphQL over HTTP specification. POST method is selected by default.
- **Parameters** and **Post Body** tabs: you may view or edit parameter content through Query, Variables and Operation Name UI elements instead.
- **File Upload** tab: irrelevant to GraphQL queries.
- **Embedded Resources from HTML Files** section in the Advanced tab: irrelevant in GraphQL JSON responses.

The Java HTTP implementation has some limitations:

- There is no control over how connections are re-used. When a connection is released by JMeter, it may or may not be re-used by the same thread.
- The API is best suited to single-threaded usage - various settings are defined via system properties, and therefore apply to all connections.
- No support of Kerberos authentication
- It does not support client based certificate testing with Keystore Config.
- Better control of Retry mechanism
- It does not support virtual hosts.
- It supports only the following methods: GET, POST, HEAD, OPTIONS, PUT, DELETE and TRACE
- Better control on DNS Caching with DNS Cache Manager

Note: the

FILE

protocol is intended for testing purposes only. It is handled by the same code regardless of which HTTP Sampler is used.

If the request requires server or proxy login authorization (i.e. where a browser would create a pop-up dialog box), you will also have to add an HTTP Authorization Manager Configuration Element. For normal logins (i.e. where the user enters login information in a form), you will need to work out what the form submit button does, and create an HTTP request with the appropriate method (usually POST) and the appropriate parameters from the form definition. If the page uses HTTP, you can use the JMeter Proxy to capture the login sequence.

A separate SSL context is used for each thread. If you want to use a single SSL context (not the standard behaviour of browsers), set the JMeter property:

```
https.sessioncontext.shared=true
```

By default, since version 5.0, the SSL context is retained during a Thread Group iteration and reset for each test iteration. If in your test plan the same user iterates multiple times, then you should set this to false.

```
httpclient.reset_state_on_thread_group_iteration=true
```

Note: this does not apply to the Java HTTP implementation.

JMeter defaults to the SSL protocol level TLS. If the server needs a different level, e.g.

SSLv3

, change the JMeter property, for example:

```
https.default.protocol=SSLv3
```

JMeter also allows one to enable additional protocols, by changing the property https.socket.protocols.

If the request uses cookies, then you will also need an HTTP Cookie Manager. You can add either of these elements to the Thread Group or the HTTP Request. If you have more than one HTTP Request that needs authorizations or cookies, then add the elements to the Thread Group. That way, all HTTP Request controllers will share the same Authorization Manager and Cookie Manager elements.

If the request uses a technique called "URL Rewriting" to maintain sessions, then see section 6.1 Handling User Sessions With URL Rewriting for additional configuration steps.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Server

Domain name or IP address of the web server, e.g.

www.example.com

. [Do not include the

http://

prefix.] Note: If the "

Host

" header is defined in a Header Manager, then this will be used as the virtual host name.

Server is required, unless:

- it is provided by HTTP Request Defaults
- or a full URL including scheme, host and port (scheme://host:port) is set in **Path** field

No

Port

Port the web server is listening to. Default:

80

No

Connect Timeout

Connection Timeout. Number of milliseconds to wait for a connection to open.

No

Response Timeout

Response Timeout. Number of milliseconds to wait for a response. Note that this applies to each wait for a response. If the server response is sent in several chunks, the overall elapsed time may be longer than the timeout.

A Duration Assertion can be used to detect responses that take too long to complete.

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

Implementation

Java

,

HttpClient4

. If not specified (and not defined by HTTP Request Defaults), the default depends on the value of the JMeter property

jmeter.httpsampler

, failing that, the HttpClient4 implementation is used.

No

Protocol

HTTP

,

HTTPS

or

FILE

. Default:

HTTP

No

Method

GET

,

POST

,

HEAD

,

TRACE

,

OPTIONS

,

PUT

,

DELETE

,

PATCH

(not supported for

JAVA

implementation). With

HttpClient4

, the following methods related to WebDav are also allowed:

COPY

,

LOCK

,

MKCOL

,

MOVE

,

PROPFIND

,

PROPPATCH

,

UNLOCK

,

REPORT

,

MKCALENDAR

,

SEARCH

.

More methods can be pre-defined for the HttpClient4 by using the JMeter property httpsampler.user_defined_methods.

Yes

Content Encoding

Content encoding to be used (for

POST

,

PUT

,

PATCH

and

FILE

). This is the character encoding to be used, and is not related to the Content-Encoding HTTP header.

No

Redirect Automatically

Sets the underlying http protocol handler to automatically follow redirects, so they are not seen by JMeter, and thus will not appear as samples. Should only be used for

GET

and

HEAD

requests. The HttpClient sampler will reject attempts to use it for

POST

or

PUT

.

Warning: see below for information on cookie and header handling.

No

Follow Redirects

This only has any effect if "

Redirect Automatically

" is not enabled. If set, the JMeter sampler will check if the response is a redirect and follow it if so. The initial redirect and further responses will appear as additional samples. The URL and data fields of the parent sample will be taken from the final (non-redirected) sample, but the parent byte count and elapsed time include all samples. The latency is taken from the initial response. Note that the HttpClient sampler may log the following message:

```
"Redirect requested but followRedirects is disabled"
```

This can be ignored.

JMeter will collapse paths of the form '

/../segment

' in both absolute and relative redirect URLs. For example

http://host/one/../two

will be collapsed into

http://host/two

. If necessary, this behaviour can be suppressed by setting the JMeter property

httpsampler.redirect.removeslashdotdot=false

No

Use KeepAlive

JMeter sets the Connection:

keep-alive

header. This does not work properly with the default HTTP implementation, as connection re-use is not under user-control. It does work with the Apache HttpComponents HttpClient implementations.

No

Use multipart/form-data for HTTP POST

Use a

multipart/form-data

or

application/x-www-form-urlencoded

post request

No

Browser-compatible headers

When using

multipart/form-data

, this suppresses the

Content-Type

and

Content-Transfer-Encoding

headers; only the

Content-Disposition

header is sent.

No

Path

The path to resource (for example,

/servlets/myServlet

). If the resource requires query string parameters, add them below in the "Send Parameters With the Request" section.

As a special case, if the path starts with "

http://

" or "

https://

" then this is used as the full URL.

In this case, the server, port and protocol fields are ignored; parameters are also ignored for

GET

and

DELETE

methods. Also please note that the path is not encoded - apart from replacing spaces with

%20

- so unsafe characters may need to be encoded to avoid errors such as

URISyntaxException

.

No

Send Parameters With the Request

The query string will be generated from the list of parameters you provide. Each parameter has a

name

and

value

, the options to encode the parameter, and an option to include or exclude an equals sign (some applications don't expect an equals sign when the value is the empty string). The query string will be generated in the correct fashion, depending on the choice of "Method" you made (i.e. if you chose

GET

or

DELETE

, the query string will be appended to the URL, if

POST

or

PUT

, then it will be sent separately). Also, if you are sending a file using a multipart form, the query string will be created using the multipart form specifications.

See below for some further information on parameter handling.

Additionally, you can specify whether each parameter should be URL encoded. If you are not sure what this means, it is probably best to select it. If your values contain characters such as the following then encoding is usually required.:

- ASCII Control Chars
- Non-ASCII characters
- Reserved characters:URLs use some characters for special use in defining their syntax. When these characters are not used in their special role inside a URL, they need to be encoded, example: '$', '&', '+', ',' , '/', ':', ';', '=', '?', '@'
- Unsafe characters: Some characters present the possibility of being misunderstood within URLs for various reasons. These characters should also always be encoded, example: ' ', '<', '>', '#', '%', …

No

File Path:

Name of the file to send. If left blank, JMeter does not send a file, if filled in, JMeter automatically sends the request as a multipart form request.

When MIME Type is empty, JMeter will try to guess the MIME type of the given file.

If it is a POST or PUT or PATCH request and there is a single file whose 'Parameter name' attribute (below) is omitted, then the file is sent as the entire body of the request, i.e. no wrappers are added. This allows arbitrary bodies to be sent. This functionality is present for POST requests, and also for PUT requests. **See below for some further information on parameter handling.**

No

Parameter name:

Value of the "

name

" web request parameter.

No

MIME Type

MIME type (for example,

text/plain

). If it is a

POST

or

PUT

or

PATCH

request and either the '

name

' attribute (below) are omitted or the request body is constructed from parameter values only, then the value of this field is used as the value of the

content-type

request header.

No

Retrieve All Embedded Resources from HTML Files

Tell JMeter to parse the HTML file and send HTTP/HTTPS requests for all images, Java applets, JavaScript files, CSSs, etc. referenced in the file. See below for more details.

No

Save response as MD5 hash?

If this is selected, then the response is not stored in the sample result. Instead, the 32 character MD5 hash of the data is calculated and stored instead. This is intended for testing large amounts of data.

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

Use concurrent pool

Use a pool of concurrent connections to get embedded resources.

No

Size

Pool size for concurrent connections used to get embedded resources.

No

Source address type

[Only for HTTP Request with HTTPClient implementation]

To distinguish the source address value, select the type of these:

- Select *IP/Hostname* to use a specific IP address or a (local) hostname
- Select *Device* to pick the first available address for that interface which this may be either IPv4 or IPv6
- Select *Device IPv4* to select the IPv4 address of the device name (like eth0, lo, em0, etc.)
- Select *Device IPv6* to select the IPv6 address of the device name (like eth0, lo, em0, etc.)

No

Source address field

[Only for HTTP Request with HTTPClient implementation]

This property is used to enable IP Spoofing. It overrides the default local IP address for this sample. The JMeter host must have multiple IP addresses (i.e. IP aliases, network interfaces, devices). The value can be a host name, IP address, or a network interface device such as "

eth0

" or "

lo

" or "

wlan0

".

If the property

httpclient.localaddress

is defined, that is used for all HttpClient requests.

No

The following parameters are available only for **GraphQL HTTP Request**:

### Parameters

Attribute

Description

Required

Query

GraphQL query (or mutation) statement.

Yes

Variables

GraphQL query (or mutation) variables in a valid JSON string.

Note

: If the input string is not a valid JSON string, this will be ignored with an ERROR log.

No

Operation Name

Optional GraphQL operation name when making a request for multi-operation documents.

No

When using Automatic Redirection, cookies are only sent for the initial URL. This can cause unexpected behaviour for web-sites that redirect to a local server. E.g. if

www.example.com

redirects to

www.example.co.uk

. In this case the server will probably return cookies for both URLs, but JMeter will only see the cookies for the last host, i.e.

www.example.co.uk

. If the next request in the test plan uses

www.example.com

, rather than

www.example.co.uk

, it will not get the correct cookies. Likewise, Headers are sent for the initial request, and won't be sent for the redirect. This is generally only a problem for manually created test plans, as a test plan created using a recorder would continue from the redirected URL.

**Parameter Handling:** For the POST and PUT method, if there is no file to send, and the name(s) of the parameter(s) are omitted, then the body is created by concatenating all the value(s) of the parameters. Note that the values are concatenated without adding any end-of-line characters. These can be added by using the __char() function in the value fields. This allows arbitrary bodies to be sent. The values are encoded if the encoding flag is set. See also the MIME Type above how you can control the content-type request header that is sent. For other methods, if the name of the parameter is missing, then the parameter is ignored. This allows the use of optional parameters defined by variables.

You have the option to switch to Body Data tab when a request has only unnamed parameters (or no parameters at all). This option is useful in the following cases (amongst others):

- GWT RPC HTTP Request
- JSON REST HTTP Request
- XML REST HTTP Request
- SOAP HTTP Request

Note that once you leave the Tree node, you cannot switch back to the parameter tab unless you clear the

Body Data

tab from its data.

In Body Data mode, each line will be sent with CRLF appended, apart from the last line. To send a CRLF after the last line of data, just ensure that there is an empty line following it. (This cannot be seen, except by noting whether the cursor can be placed on the subsequent line.)

**Method Handling:** The GET, DELETE, POST, PUT and PATCH request methods work similarly, except that as of 3.1, only POST method supports multipart requests or file upload. The PUT and PATCH method body must be provided as one of the following:

- define the body as a file with empty Parameter name field; in which case the MIME Type is used as the Content-Type
- define the body as parameter value(s) with no name
- use the Body Data tab

The GET, DELETE and POST methods have an additional way of passing parameters by using the Parameters tab. GET, DELETE, PUT and PATCH require a Content-Type. If not using a file, attach a Header Manager to the sampler and define the Content-Type there.

JMeter scan responses from embedded resources. It uses the property HTTPResponse.parsers, which is a list of parser ids, e.g. htmlParser, cssParser and wmlParser. For each id found, JMeter checks two further properties:

- id.types - a list of content types
- id.className - the parser to be used to extract the embedded resources

See jmeter.properties file for the details of the settings. If the HTTPResponse.parser property is not set, JMeter reverts to the previous behaviour, i.e. only text/html responses will be scanned

Emulating slow connections:

HttpClient4 and Java Sampler support emulation of slow connections; see the following entries in jmeter.properties: # Define characters per second > 0 to emulate slow connections #httpclient.socket.http.cps=0 #httpclient.socket.https.cps=0 However the Java sampler only supports slow HTTPS connections.

**Response size calculation** The Java implementation does not include transport overhead such as chunk headers in the response body size. The HttpClient4 implementation does include the overhead in the response body size, so the value may be greater than the number of bytes in the response content.

**Retry handling** By default retry has been set to 0 for both HttpClient4 and Java implementations, meaning no retry is attempted. For HttpClient4, the retry count can be overridden by setting the relevant JMeter property, for example: httpclient4.retrycount=3 With HC4 Implementation, retry will be done on Idempotent Http Methods by default. If you want to retry for all methods, then set property httpclient4.request_sent_retry_enabled=true Note that the Java implementation does not retry neither by default, you can change this by setting http.java.sampler.retries=3

**Note: Certificates does not conform to algorithm constraints** You may encounter the following error: java.security.cert.CertificateException: Certificates does not conform to algorithm constraints if you run a HTTPS request on a web site with a SSL certificate (itself or one of SSL certificates in its chain of trust) with a signature algorithm using MD2 (like md2WithRSAEncryption) or with a SSL certificate with a size lower than 1024 bits.

This error is related to increased security in Java 8.

To allow you to perform your HTTPS request, you can downgrade the security of your Java installation by editing the Java jdk.certpath.disabledAlgorithms property. Remove the MD2 value or the constraint on size, depending on your case.

This property is in this file:

```
JAVA_HOME/jre/lib/security/java.security
```

See Bug 56357 for details.

See also:

- Assertion
- Building a Web Test Plan
- Building an Advanced Web Test Plan
- HTTP Authorization Manager
- HTTP Cookie Manager
- HTTP Header Manager
- HTML Link Parser
- HTTP(S) Test Script Recorder
- HTTP Request Defaults
- HTTP Requests and Session ID's: URL Rewriting

^


## JDBC Request

This sampler lets you send a JDBC Request (an SQL query) to a database.

Before using this you need to set up a JDBC Connection Configuration Configuration element

If the Variable Names list is provided, then for each row returned by a Select statement, the variables are set up with the value of the corresponding column (if a variable name is provided), and the count of rows is also set up. For example, if the Select statement returns 2 rows of 3 columns, and the variable list is A,,C, then the following variables will be set up:

```
A_#=2 (number of rows)
A_1=column 1, row 1
A_2=column 1, row 2
C_#=2 (number of rows)
C_1=column 3, row 1
C_2=column 3, row 2
```

If the Select statement returns zero rows, then the A_# and C_# variables would be set to 0, and no other variables would be set.

Old variables are cleared if necessary - e.g. if the first select retrieves six rows and a second select returns only three rows, the additional variables for rows four, five and six will be removed.

The latency time is set from the time it took to acquire a connection.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Variable Name of Pool declared in JDBC Connection Configuration

Name of the JMeter variable that the connection pool is bound to. This must agree with the '

Variable Name

' field of a

JDBC Connection Configuration

.

Yes

Query Type

Set this according to the statement type:

- Select Statement
- Update Statement - use this for Inserts and Deletes as well
- Callable Statement
- Prepared Select Statement
- Prepared Update Statement - use this for Inserts and Deletes as well
- Commit
- Rollback
- Autocommit(false)
- Autocommit(true)
- Edit - this should be a variable reference that evaluates to one of the above

The types

Commit

,

Rollback

,

Autocommit(false)

and

Autocommit(true)

are special, as they are ignoring the given SQL statements and are changing the state of the connection, only.

Yes

SQL Query

SQL query.

Do not enter a trailing semi-colon.

There is generally no need to use

{

and

}

to enclose Callable statements; however they may be used if the database uses a non-standard syntax.

The JDBC driver automatically converts the statement if necessary when it is enclosed in

{}

.

For example:

- select * from t_customers where id=23
- CALL SYSCS_UTIL.SYSCS_EXPORT_TABLE (null, ?, ?, null, null, null)
  - Parameter values: tablename,filename
  - Parameter types: VARCHAR,VARCHAR

The second example assumes you are using Apache Derby.

Yes

Parameter values

Comma-separated list of parameter values. Use

]NULL[

to indicate a

NULL

parameter. (If required, the null string can be changed by defining the property "

jdbcsampler.nullmarker

".)

The list must be enclosed in double-quotes if any of the values contain a comma or double-quote, and any embedded double-quotes must be doubled-up, for example:

```
"Dbl-Quote: "" and Comma: ,"
```

There must be as many values as there are placeholders in the statement even if your parameters are

OUT

ones. Be sure to set a value even if the value will not be used (for example in a CallableStatement).

Yes, if a prepared or callable statement has parameters

Parameter types

Comma-separated list of SQL parameter types (e.g.

INTEGER

,

DATE

,

VARCHAR

,

DOUBLE

) or integer values of Constants. Those integer values can be used, when you use custom database types proposed by driver (For example

OracleTypes.CURSOR

could be represented by its integer value

-10

).

These are defined as fields in the class

java.sql.Types

, see for example:

Javadoc for java.sql.Types

.

Note: JMeter will use whatever types are defined by the runtime JVM, so if you are running on a different JVM, be sure to check the appropriate documentation

If the callable statement has

INOUT

or

OUT

parameters, then these must be indicated by prefixing the appropriate parameter types, e.g. instead of "

INTEGER

", use "

INOUT INTEGER

".

If not specified, "

IN

" is assumed, i.e. "

DATE

" is the same as "

IN DATE

".

If the type is not one of the fields found in

java.sql.Types

, JMeter also accepts the corresponding integer number, e.g. since

OracleTypes.CURSOR == -10

, you can use "

INOUT -10

".

There must be as many types as there are placeholders in the statement.

Yes, if a prepared or callable statement has parameters

Variable Names

Comma-separated list of variable names to hold values returned by Select statements, Prepared Select Statements or CallableStatement. Note that when used with CallableStatement, list of variables must be in the same sequence as the

OUT

parameters returned by the call. If there are less variable names than

OUT

parameters only as many results shall be stored in the thread-context variables as variable names were supplied. If more variable names than

OUT

parameters exist, the additional variables will be ignored

No

Result Variable Name

If specified, this will create an Object variable containing a list of row maps. Each map contains the column name as the key and the column data as the value. Usage:

```
columnValue = vars.getObject("resultObject").get(0).get("Column Name");
```

No

Query timeout(s)

Set a timeout in seconds for query, empty value means 0 which is infinite.

-1

means don't set any query timeout which might be needed for use case or when certain drivers don't support timeout. Defaults to 0.

No

Limit ResultSet

Limits the number of rows to iterate through the ResultSet. Empty value means

-1

, e.g. no limitation, which is also the default. This can help to reduce the amount of data to be fetched from the database via the JDBC driver, but affects all possible options of

Handle ResultSet

respectively – e.g. incomplete ResultSet and a record count ≤ the limit.

No

Handle ResultSet

Defines how ResultSet returned from callable statements be handled:

- Store As String (default) - All variables on Variable Names list are stored as strings, will not iterate through a ResultSet when present on the list. CLOBs will be converted to Strings. BLOBs will be converted to Strings as if they were an UTF-8 encoded byte-array. Both CLOBs and BLOBs will be cut off after jdbcsampler.max_retain_result_size bytes.
- Store As Object - Variables of ResultSet type on Variables Names list will be stored as Object and can be accessed in subsequent tests/scripts and iterated, will not iterate through the ResultSet. CLOBs will be handled as if Store As String was selected. BLOBs will be stored as a byte array. Both CLOBs and BLOBs will be cut off after jdbcsampler.max_retain_result_size bytes.
- Count Records - Variables of ResultSet types will be iterated through showing the count of records as result. Variables will be stored as Strings. For BLOBs the size of the object will be stored.

No

See also:

- Building a Database Test Plan
- JDBC Connection Configuration

Current Versions of JMeter use UTF-8 as the character encoding. Previously the platform default was used.

Ensure Variable Name is unique across Test Plan.

^


## Java Request

This sampler lets you control a java class that implements the org.apache.jmeter.protocol.java.sampler.JavaSamplerClient interface. By writing your own implementation of this interface, you can use JMeter to harness multiple threads, input parameter control, and data collection.

The pull-down menu provides the list of all such implementations found by JMeter in its classpath. The parameters can then be specified in the table below - as defined by your implementation. Two simple examples (JavaTest and SleepTest) are provided.

The JavaTest example sampler can be useful for checking test plans, because it allows one to set values in almost all the fields. These can then be used by Assertions, etc. The fields allow variables to be used, so the values of these can readily be seen.

If the method

teardownTest

is not overridden by a subclass of

AbstractJavaSamplerClient

, its

teardownTest

method will not be called. This reduces JMeter memory requirements. This will not have any impact on existing Test plans.

The Add/Delete buttons don't serve any purpose at present.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Classname

The specific implementation of the JavaSamplerClient interface to be sampled.

Yes

Send Parameters with Request

A list of arguments that will be passed to the sampled class. All arguments are sent as Strings. See below for specific settings.

No

The following parameters apply to the SleepTest and JavaTest implementations:

### Parameters

Attribute

Description

Required

Sleep_time

How long to sleep for (ms)

Yes

Sleep_mask

How much "randomness" to add:

The sleep time is calculated as follows:

```
totalSleepTime = SleepTime + (System.currentTimeMillis() % SleepMask)
```

Yes

The following parameters apply additionally to the JavaTest implementation:

### Parameters

Attribute

Description

Required

Label

The label to use. If provided, overrides

Name

No

ResponseCode

If provided, sets the SampleResult ResponseCode.

No

ResponseMessage

If provided, sets the SampleResult ResponseMessage.

No

Status

If provided, sets the SampleResult Status. If this equals "

OK

" (ignoring case) then the status is set to success, otherwise the sample is marked as failed.

No

SamplerData

If provided, sets the SampleResult SamplerData.

No

ResultData

If provided, sets the SampleResult ResultData.

No

^


## LDAP Request

This Sampler lets you send a different LDAP request(

Add

,

Modify

,

Delete

and

Search

) to an LDAP server.

If you are going to send multiple requests to the same LDAP server, consider using an LDAP Request Defaults Configuration Element so you do not have to enter the same information for each LDAP Request.

The same way the

Login Config Element

also using for Login and password.

There are two ways to create test cases for testing an LDAP Server.

1. Inbuilt Test cases.
2. User defined Test cases.

There are four test scenarios of testing LDAP. The tests are given below:

1. Add Test
  1. Inbuilt test: This will add a pre-defined entry in the LDAP Server and calculate the execution time. After execution of the test, the created entry will be deleted from the LDAP Server.
  2. User defined test: This will add the entry in the LDAP Server. User has to enter all the attributes in the table.The entries are collected from the table to add. The execution time is calculated. The created entry will not be deleted after the test.
2. Modify Test
  1. Inbuilt test: This will create a pre-defined entry first, then will modify the created entry in the LDAP Server.And calculate the execution time. After execution of the test, the created entry will be deleted from the LDAP Server.
  2. User defined test: This will modify the entry in the LDAP Server. User has to enter all the attributes in the table. The entries are collected from the table to modify. The execution time is calculated. The entry will not be deleted from the LDAP Server.
3. Search Test
  1. Inbuilt test: This will create the entry first, then will search if the attributes are available. It calculates the execution time of the search query. At the end of the execution,created entry will be deleted from the LDAP Server.
  2. User defined test: This will search the user defined entry(Search filter) in the Search base (again, defined by the user). The entries should be available in the LDAP Server. The execution time is calculated.
4. Delete Test
  1. Inbuilt test: This will create a pre-defined entry first, then it will be deleted from the LDAP Server. The execution time is calculated.
  2. User defined test: This will delete the user-defined entry in the LDAP Server. The entries should be available in the LDAP Server. The execution time is calculated.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Server Name or IP

Domain name or IP address of the LDAP server. JMeter assumes the LDAP server is listening on the default port (

389

).

Yes

Port

Port to connect to (default is

389

).

Yes

root DN

Base DN to use for LDAP operations

Yes

Username

LDAP server username.

Usually

Password

LDAP server password. (N.B. this is stored unencrypted in the test plan)

Usually

Entry DN

the name of the context to create or Modify; may not be empty.

You have to set the right attributes of the object yourself. So if you want to add

cn=apache,ou=test

you have to add in the table

name

and

value

to

cn

and

apache

.

Yes, if User Defined Test and Add Test or Modify Test is selected

Delete

the name of the context to Delete; may not be empty

Yes, if User Defined Test and Delete Test is selected

Search base

the name of the context or object to search

Yes, if User Defined Test and Search Test is selected

Search filter

the filter expression to use for the search; may not be null

Yes, if User Defined Test and Search Test is selected

add test

Use these

name

,

value

pairs for creation of the new object in the given context

Yes, if User Defined Test and add Test is selected

modify test

Use these

name

,

value

pairs for modification of the given context object

Yes, if User Defined Test and Modify Test is selected

See also:

- Building an LDAP Test Plan
- LDAP Request Defaults

^
