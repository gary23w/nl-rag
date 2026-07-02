---
title: "Apache JMeter (part 2/8)"
source: https://jmeter.apache.org/usermanual/component_reference.html
domain: jmeter
license: CC-BY-SA-4.0
tags: jmeter apache, load testing, performance testing, test plan
fetched: 2026-07-02
part: 2/8
---

## LDAP Extended Request

This Sampler can send all 8 different LDAP requests to an LDAP server. It is an extended version of the LDAP sampler, therefore it is harder to configure, but can be made much closer resembling a real LDAP session.

If you are going to send multiple requests to the same LDAP server, consider using an LDAP Extended Request Defaults Configuration Element so you do not have to enter the same information for each LDAP Request.

There are nine test operations defined. These operations are given below:

****Thread bind****

Any LDAP request is part of an LDAP session, so the first thing that should be done is starting a session to the LDAP server. For starting this session a thread bind is used, which is equal to the LDAP "bind" operation. The user is requested to give a username (Distinguished name) and password, which will be used to initiate a session. When no password, or the wrong password is specified, an anonymous session is started. Take care, omitting the password will not fail this test, a wrong password will. (N.B. this is stored unencrypted in the test plan)

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Servername

The name (or IP-address) of the LDAP server.

Yes

Port

The port number that the LDAP server is listening to. If this is omitted JMeter assumes the LDAP server is listening on the default port(389).

No

DN

The distinguished name of the base object that will be used for any subsequent operation. It can be used as a starting point for all operations. You cannot start any operation on a higher level than this DN!

No

Username

Full distinguished name of the user as which you want to bind.

No

Password

Password for the above user. If omitted it will result in an anonymous bind. If it is incorrect, the sampler will return an error and revert to an anonymous bind. (N.B. this is stored unencrypted in the test plan)

No

Connection timeout (in milliseconds)

Timeout for connection, if exceeded connection will be aborted

No

Use Secure LDAP Protocol

Use

ldaps://

scheme instead of

ldap://

No

Trust All Certificates

Trust all certificates, only used if

Use Secure LDAP Protocol

is checked

No

****Thread unbind****

This is simply the operation to end a session. It is equal to the LDAP "unbind" operation.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

****Single bind/unbind****

This is a combination of the LDAP "bind" and "unbind" operations. It can be used for an authentication request/password check for any user. It will open a new session, just to check the validity of the user/password combination, and end the session again.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Username

Full distinguished name of the user as which you want to bind.

Yes

Password

Password for the above user. If omitted it will result in an anonymous bind. If it is incorrect, the sampler will return an error. (N.B. this is stored unencrypted in the test plan)

No

****Rename entry****

This is the LDAP "moddn" operation. It can be used to rename an entry, but also for moving an entry or a complete subtree to a different place in the LDAP tree.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Old entry name

The current distinguished name of the object you want to rename or move, relative to the given DN in the thread bind operation.

Yes

New distinguished name

The new distinguished name of the object you want to rename or move, relative to the given DN in the thread bind operation.

Yes

****Add test****

This is the LDAP "add" operation. It can be used to add any kind of object to the LDAP server.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Entry DN

Distinguished name of the object you want to add, relative to the given DN in the thread bind operation.

Yes

Add test

A list of attributes and their values you want to use for the object. If you need to add a multiple value attribute, you need to add the same attribute with their respective values several times to the list.

Yes

****Delete test****

This is the LDAP "delete" operation, it can be used to delete an object from the LDAP tree

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Delete

Distinguished name of the object you want to delete, relative to the given DN in the thread bind operation.

Yes

****Search test****

This is the LDAP "search" operation, and will be used for defining searches.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Search base

Distinguished name of the subtree you want your search to look in, relative to the given DN in the thread bind operation.

No

Search Filter

searchfilter, must be specified in LDAP syntax.

Yes

Scope

Use

0

for baseobject-,

1

for onelevel- and

2

for a subtree search. (Default=

0

)

No

Size Limit

Specify the maximum number of results you want back from the server. (default=

0

, which means no limit.) When the sampler hits the maximum number of results, it will fail with errorcode

4

No

Time Limit

Specify the maximum amount of (cpu)time (in milliseconds) that the server can spend on your search. Take care, this does not say anything about the response time. (default is

0

, which means no limit)

No

Attributes

Specify the attributes you want to have returned, separated by a semicolon. An empty field will return all attributes

No

Return object

Whether the object will be returned (

true

) or not (

false

). Default=

false

No

Dereference aliases

If

true

, it will dereference aliases, if

false

, it will not follow them (default=

false

)

No

Parse the search results?

If

true

, the search results will be added to the response data. If

false

, a marker - whether results where found or not - will be added to the response data.

No

****Modification test****

This is the LDAP "modify" operation. It can be used to modify an object. It can be used to add, delete or replace values of an attribute.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Entry name

Distinguished name of the object you want to modify, relative to the given DN in the thread bind operation

Yes

Modification test

The attribute-value-opCode triples.

The

opCode

can be any valid LDAP operationCode (

add

,

delete

,

remove

or

replace

).

If you don't specify a value with a

delete

operation, all values of the given attribute will be deleted.

If you do specify a value in a

delete

operation, only the given value will be deleted.

If this value is non-existent, the sampler will fail the test.

Yes

****Compare****

This is the LDAP "compare" operation. It can be used to compare the value of a given attribute with some already known value. In reality this is mostly used to check whether a given person is a member of some group. In such a case you can compare the DN of the user as a given value, with the values in the attribute "member" of an object of the type groupOfNames. If the compare operation fails, this test fails with errorcode 49.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Entry DN

The current distinguished name of the object of which you want to compare an attribute, relative to the given DN in the thread bind operation.

Yes

Compare filter

In the form "

attribute=value

"

Yes

See also:

- Building an LDAP Test Plan
- LDAP Extended Request Defaults

^


## Access Log Sampler

AccessLogSampler was designed to read access logs and generate http requests. For those not familiar with the access log, it is the log the webserver maintains of every request it accepted. This means every image, CSS file, JavaScript file, html file, …

Tomcat uses the common format for access logs. This means any webserver that uses the common log format can use the AccessLogSampler. Server that use common log format include: Tomcat, Resin, Weblogic, and SunOne. Common log format looks like this:

```
127.0.0.1 - - [21/Oct/2003:05:37:21 -0500] "GET /index.jsp?%2Findex.jsp= HTTP/1.1" 200 8343
```

The current implementation of the parser only looks at the text within the quotes that contains one of the HTTP protocol methods (

GET

,

PUT

,

POST

,

DELETE

, …). Everything else is stripped out and ignored. For example, the response code is completely ignored by the parser.

For the future, it might be nice to filter out entries that do not have a response code of 200. Extending the sampler should be fairly simple. There are two interfaces you have to implement:

- org.apache.jmeter.protocol.http.util.accesslog.LogParser
- org.apache.jmeter.protocol.http.util.accesslog.Generator

The current implementation of AccessLogSampler uses the generator to create a new HTTPSampler. The servername, port and get images are set by AccessLogSampler. Next, the parser is called with integer 1, telling it to parse one entry. After that, HTTPSampler.sample() is called to make the request.

```
samp = (HTTPSampler) GENERATOR.generateRequest();
samp.setDomain(this.getDomain());
samp.setPort(this.getPort());
samp.setImageParser(this.isImageParser());
PARSER.parse(1);
res = samp.sample();
res.setSampleLabel(samp.toString());
```

The required methods in

LogParser

are:

- setGenerator(Generator)
- parse(int)

Classes implementing Generator interface should provide concrete implementation for all the methods. For an example of how to implement either interface, refer to StandardGenerator and TCLogParser.


## (Beta Code)

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Server

Domain name or IP address of the web server.

Yes

Protocol

Scheme

No (defaults to http

Port

Port the web server is listening to.

No (defaults to 80)

Log parser class

The log parser class is responsible for parsing the logs.

Yes (default provided)

Filter

The filter class is used to filter out certain lines.

No

Location of log file

The location of the access log file.

Yes

The TCLogParser processes the access log independently for each thread. The SharedTCLogParser and OrderPreservingLogParser share access to the file, i.e. each thread gets the next entry in the log.

The SessionFilter is intended to handle Cookies across threads. It does not filter out any entries, but modifies the cookie manager so that the cookies for a given IP are processed by a single thread at a time. If two threads try to process samples from the same client IP address, then one will be forced to wait until the other has completed.

The LogFilter is intended to allow access log entries to be filtered by filename and regex, as well as allowing for the replacement of file extensions. However, it is not currently possible to configure this via the GUI, so it cannot really be used.

^


## BeanShell Sampler

This sampler allows you to write a sampler using the BeanShell scripting language.

**For full details on using BeanShell, please see the BeanShell website.** Migration to JSR223 Sampler+Groovy is highly recommended for performance, support of new Java features and limited maintenance of the BeanShell library.

The test element supports the ThreadListener and TestListener interface methods. These must be defined in the initialisation file. See the file BeanShellListeners.bshrc for example definitions.

The BeanShell sampler also supports the Interruptible interface. The interrupt() method can be defined in the script or the init file.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree. The name is stored in the script variable Label

No

Reset bsh.Interpreter before each call

If this option is selected, then the interpreter will be recreated for each sample. This may be necessary for some long running scripts. For further information, see

Best Practices - BeanShell scripting

.

Yes

Parameters

Parameters to pass to the BeanShell script. This is intended for use with script files; for scripts defined in the GUI, you can use whatever variable and function references you need within the script itself. The parameters are stored in the following variables:

**Parameters**

string containing the parameters as a single variable

**bsh.args**

String array containing parameters, split on white-space

No

Script file

A file containing the BeanShell script to run. The file name is stored in the script variable

FileName

No

Script

The BeanShell script to run. The return value (if not

null

) is stored as the sampler result.

Yes (unless script file is provided)

N.B. Each Sampler instance has its own BeanShell interpreter, and Samplers are only called from a single thread

If the property "beanshell.sampler.init" is defined, it is passed to the Interpreter as the name of a sourced file. This can be used to define common methods and variables. There is a sample init file in the bin directory: BeanShellSampler.bshrc.

If a script file is supplied, that will be used, otherwise the script will be used.

JMeter processes function and variable references before passing the script field to the interpreter, so the references will only be resolved once. Variable and function references in script files will be passed verbatim to the interpreter, which is likely to cause a syntax error. In order to use runtime variables, please use the appropriate props methods, e.g.

props.get("START.HMS"); props.put("PROP1","1234");

BeanShell does not currently support Java 5 syntax such as generics and the enhanced for loop.

Before invoking the script, some variables are set up in the BeanShell interpreter:

The contents of the Parameters field is put into the variable "Parameters". The string is also split into separate tokens using a single space as the separator, and the resulting list is stored in the String array bsh.args.

The full list of BeanShell variables that is set up is as follows:

- log - the Logger
- Label - the Sampler label
- FileName - the file name, if any
- Parameters - text from the Parameters field
- bsh.args - the parameters, split as described above
- SampleResult - pointer to the current SampleResult
- ResponseCode defaults to 200
- ResponseMessage defaults to "OK"
- IsSuccess defaults to true
- ctx - JMeterContext
- vars - JMeterVariables - e.g.
  ```
vars.get("VAR1");
vars.put("VAR2","value");
vars.remove("VAR3");
vars.putObject("OBJ1",new Object());
  ```
- props - JMeterProperties (class java.util.Properties) - e.g.
  ```
props.get("START.HMS");
props.put("PROP1","1234");
  ```

When the script completes, control is returned to the Sampler, and it copies the contents of the following script variables into the corresponding variables in the SampleResult:

- ResponseCode - for example 200
- ResponseMessage - for example "OK"
- IsSuccess - true or false

The SampleResult ResponseData is set from the return value of the script. If the script returns null, it can set the response directly, by using the method SampleResult.setResponseData(data), where data is either a String or a byte array. The data type defaults to "text", but can be set to binary by using the method SampleResult.setDataType(SampleResult.BINARY).

The SampleResult variable gives the script full access to all the fields and methods in the SampleResult. For example, the script has access to the methods setStopThread(boolean) and setStopTest(boolean). Here is a simple (not very useful!) example script:

```
if (bsh.args[0].equalsIgnoreCase("StopThread")) {
    log.info("Stop Thread detected!");
    SampleResult.setStopThread(true);
}
return "Data from sample with Label "+Label;
//or
SampleResult.setResponseData("My data");
return null;
```

Another example: ensure that the property beanshell.sampler.init=BeanShellSampler.bshrc is defined in jmeter.properties. The following script will show the values of all the variables in the ResponseData field:

```
return getVariables();
```

For details on the methods available for the various classes (JMeterVariables, SampleResult etc.) please check the Javadoc or the source code. Beware however that misuse of any methods can cause subtle faults that may be difficult to find.

^


## JSR223 Sampler

The JSR223 Sampler allows JSR223 script code to be used to perform a sample or some computation required to create/update variables. If you don't want to generate a SampleResult when this sampler is run, call the following method: SampleResult.setIgnore(); This call will have the following impact: SampleResult will not be delivered to SampleListeners like View Results Tree, Summariser ... SampleResult will not be evaluated in Assertions nor PostProcessors SampleResult will be evaluated to computing last sample status (${JMeterThread.last_sample_ok}), and ThreadGroup "Action to be taken after a Sampler error" (since JMeter 5.4)

The JSR223 test elements have a feature (compilation) that can significantly increase performance. To benefit from this feature:

- Use Script files instead of inlining them. This will make JMeter compile them if this feature is available on ScriptEngine and cache them.
- Or Use Script Text and check Cache compiled script if available property. When using this feature, ensure your script code does not use JMeter variables or JMeter function calls directly in script code as caching would only cache first replacement. Instead use script parameters. To benefit from caching and compilation, the language engine used for scripting must implement JSR223 Compilable interface (Groovy is one of these, java, beanshell and javascript are not) When using Groovy as scripting language and not checking Cache compiled script if available (while caching is recommended), you should set this JVM Property -Dgroovy.use.classvalue=true due to a Groovy Memory leak as of version 2.4.6, see: GROOVY-7683 GROOVY-7591 JDK-8136353

Cache size is controlled by the following JMeter property (

jmeter.properties

):

```
jsr223.compiled_scripts_cache_size=100
```

Unlike the

BeanShell Sampler

, the interpreter is not saved between invocations.

JSR223 Test Elements using Script file or Script text + checked

Cache compiled script if available

are now compiled if ScriptEngine supports this feature, this enables great performance enhancements.

JMeter processes function and variable references before passing the script field to the interpreter, so the references will only be resolved once. Variable and function references in script files will be passed verbatim to the interpreter, which is likely to cause a syntax error. In order to use runtime variables, please use the appropriate props methods, e.g.

```
props.get("START.HMS");
props.put("PROP1","1234");
```

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

Scripting Language

Name of the JSR223 scripting language to be used.

There are other languages supported than those that appear in the drop-down list. Others may be available if the appropriate jar is installed in the JMeter lib directory.

Notice that some languages such as Velocity may use a different syntax for JSR223 variables, e.g.

```
$log.debug("Hello " + $vars.get("a"));
```

for Velocity.

Yes

Script File

Name of a file to be used as a JSR223 script, if a relative file path is used, then it will be relative to directory referenced by "

user.dir

" System property

No

Parameters

List of parameters to be passed to the script file or the script.

No

Cache compiled script if available

If checked (advised) and the language used supports

Compilable

interface (Groovy is one of these, java, beanshell and javascript are not), JMeter will compile the Script and cache it using its MD5 hash as unique cache key

No

Script

Script to be passed to JSR223 language

Yes (unless script file is provided)

If a script file is supplied, that will be used, otherwise the script will be used.

Before invoking the script, some variables are set up. Note that these are JSR223 variables - i.e. they can be used directly in the script.

- log - the Logger
- Label - the Sampler label
- FileName - the file name, if any
- Parameters - text from the Parameters field
- args - the parameters, split as described above
- SampleResult - pointer to the current SampleResult
- sampler - (Sampler) - pointer to current Sampler
- ctx - JMeterContext
- vars - JMeterVariables - e.g.
  ```
vars.get("VAR1");
vars.put("VAR2","value");
vars.remove("VAR3");
vars.putObject("OBJ1",new Object());
  ```
- props - JMeterProperties (class java.util.Properties) - e.g.
  ```
props.get("START.HMS");
props.put("PROP1","1234");
  ```
- OUT - System.out - e.g. OUT.println("message")

The SampleResult ResponseData is set from the return value of the script. If the script returns null, it can set the response directly, by using the method SampleResult.setResponseData(data), where data is either a String or a byte array. The data type defaults to "text", but can be set to binary by using the method SampleResult.setDataType(SampleResult.BINARY).

The SampleResult variable gives the script full access to all the fields and methods in the SampleResult. For example, the script has access to the methods setStopThread(boolean) and setStopTest(boolean).

Unlike the BeanShell Sampler, the JSR223 Sampler does not set the ResponseCode, ResponseMessage and sample status via script variables. Currently the only way to changes these is via the SampleResult methods:

- SampleResult.setSuccessful(true/false)
- SampleResult.setResponseCode("code")
- SampleResult.setResponseMessage("message")

^


## TCP Sampler

The TCP Sampler opens a TCP/IP connection to the specified server. It then sends the text, and waits for a response.

If "Re-use connection" is selected, connections are shared between Samplers in the same thread, provided that the exact same host name string and port are used. Different hosts/port combinations will use different connections, as will different threads. If both of "Re-use connection" and "Close connection" are selected, the socket will be closed after running the sampler. On the next sampler, another socket will be created. You may want to close a socket at the end of each thread loop.

If an error is detected - or "Re-use connection" is not selected - the socket is closed. Another socket will be reopened on the next sample.

The following properties can be used to control its operation:

**tcp.status.prefix**

text that precedes a status number

**tcp.status.suffix**

text that follows a status number

**tcp.status.properties**

name of property file to convert status codes to messages

**tcp.handler**

Name of TCP Handler class (default

TCPClientImpl

) - only used if not specified on the GUI

The class that handles the connection is defined by the GUI, failing that the property

tcp.handler

. If not found, the class is then searched for in the package

org.apache.jmeter.protocol.tcp.sampler

.

Users can provide their own implementation. The class must extend org.apache.jmeter.protocol.tcp.sampler.TCPClient.

The following implementations are currently provided.

- TCPClientImpl
- BinaryTCPClientImpl
- LengthPrefixedBinaryTCPClientImpl

The implementations behave as follows:

**TCPClientImpl**

This implementation is fairly basic. When reading the response, it reads until the end of line byte, if this is defined by setting the property

tcp.eolByte

, otherwise until the end of the input stream. You can control charset encoding by setting

tcp.charset

, which will default to Platform default encoding.

**BinaryTCPClientImpl**

This implementation converts the GUI input, which must be a hex-encoded string, into binary, and performs the reverse when reading the response. When reading the response, it reads until the end of message byte, if this is defined by setting the property

tcp.BinaryTCPClient.eomByte

, otherwise until the end of the input stream.

**LengthPrefixedBinaryTCPClientImpl**

This implementation extends BinaryTCPClientImpl by prefixing the binary message data with a binary length byte. The length prefix defaults to 2 bytes. This can be changed by setting the property

tcp.binarylength.prefix.length

.

****Timeout handling****

If the timeout is set, the read will be terminated when this expires. So if you are using an

eolByte

/

eomByte

, make sure the timeout is sufficiently long, otherwise the read will be terminated early.

****Response handling****

If

tcp.status.prefix

is defined, then the response message is searched for the text following that up to the suffix. If any such text is found, it is used to set the response code. The response message is then fetched from the properties file (if provided).

Usage of pre- and suffix

¶

For example, if the prefix = "

[

" and the suffix = "

]

", then the following response:

```
[J28] XI123,23,GBP,CR
```

would have the response code

J28

.

Response codes in the range "

400

"-"

499

" and "

500

"-"

599

" are currently regarded as failures; all others are successful. [This needs to be made configurable!]

The login name/password are not used by the supplied TCP implementations.

Sockets are disconnected at the end of a test run.

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

Yes

Port Number

Port to be used

Yes

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

to skip

eol

checking. You may set this in

jmeter.properties

file as well with

eolByte

property. If you set this in TCP Sampler Config and in

jmeter.properties

file at the same time, the setting value in the TCP Sampler Config will be used.

No

Connect Timeout

Connect Timeout (milliseconds,

0

disables).

No

Response Timeout

Response Timeout (milliseconds,

0

disables).

No

Set NoDelay

See

java.net.Socket.setTcpNoDelay()

. If selected, this will disable Nagle's algorithm, otherwise Nagle's algorithm will be used.

Yes

Text to Send

Text to be sent

Yes

Login User

User Name - not used by default implementation

No

Password

Password - not used by default implementation (N.B. this is stored unencrypted in the test plan)

No

^


## JMS Publisher

JMS Publisher will publish messages to a given destination (topic/queue). For those not familiar with JMS, it is the J2EE specification for messaging. There are numerous JMS servers on the market and several open source options.

JMeter does not include any JMS implementation jar; this must be downloaded from the JMS provider and put in the lib directory

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

use JNDI properties file

use

jndi.properties

. Note that the file must be on the classpath - e.g. by updating the

user.classpath

JMeter property. If this option is not selected, JMeter uses the "

JNDI Initial Context Factory

" and "

Provider URL

" fields to create the connection.

Yes

JNDI Initial Context Factory

Name of the context factory

No

Provider URL

The URL for the JMS provider

Yes, unless using jndi.properties

Destination

The message destination (topic or queue name)

Yes

Setup

The destination setup type. With

At startup

, the destination name is static (i.e. always same name during the test), with

Each sample

, the destination name is dynamic and is evaluate at each sample (i.e. the destination name may be a variable)

Yes

Authentication

Authentication requirement for the JMS provider

Yes

User

User Name

No

Password

Password (N.B. this is stored unencrypted in the test plan)

No

Expiration

The expiration time (in milliseconds) of the message before it becomes obsolete. If you do not specify an expiration time, the default value is

0

(never expires).

No

Priority

The priority level of the message. There are ten priority levels from

0

(lowest) to

9

(highest). If you do not specify a priority level, the default level is

4

.

No

Reconnect on error codes (regex)

Regular expression for JMSException error codes which force reconnection. If empty no reconnection will be done

No

Number of samples to aggregate

Number of samples to aggregate

Yes

Message source

Where to obtain the message:

**From File**

means the referenced file will be read and reused by all samples. If file name changes it is reloaded since JMeter 3.0

**Random File from folder specified below**

means a random file will be selected from folder specified below, this folder must contain either files with extension

.dat

for Bytes Messages, or files with extension

.txt

or

.obj

for Object or Text messages

**Text area**

The Message to use either for Text or Object message

Yes

Message type

Text, Map, Object message or Bytes Message

Yes

Content encoding

Specify the encoding for reading the message source file:

**RAW:**

No variable support from the file and load it with default system charset.

**DEFAULT:**

Load file with default system encoding, except for XML which relies on XML prolog. If the file contain variables, they will be processed.

**Standard charsets:**

The specified encoding (valid or not) is used for reading the file and processing variables

Yes

Use non-persistent delivery mode?

Whether to set

DeliveryMode.NON_PERSISTENT

(defaults to

false

)

No

JMS Properties

The JMS Properties are properties specific for the underlying messaging system. You can setup the name, the value and the class (type) of value. Default type is

String

. For example: for WebSphere 5.1 web services you will need to set the JMS Property targetService to test webservices through JMS.

No

For the MapMessage type, JMeter reads the source as lines of text. Each line must have 3 fields, delimited by commas. The fields are:

- Name of entry
- Object class name, e.g. "String" (assumes java.lang package if not specified)
- Object string value

valueOf(String)

```
name,String,Example
size,Integer,1234
```

The Object message is implemented and works as follow:

- Put the JAR that contains your object and its dependencies in jmeter_home/lib/ folder
- Serialize your object as XML using XStream
- Either put result in a file suffixed with .txt or .obj or put XML content directly in Text Area

Note that if message is in a file, replacement of properties will not occur while it will if you use Text Area.

The following table shows some values which may be useful when configuring JMS:

| Apache ActiveMQ | Value(s) | Comment |
|---|---|---|
| Context Factory | org.apache.activemq.jndi.ActiveMQInitialContextFactory | . |
| Provider URL | vm://localhost |   |
| Provider URL | vm:(broker:(vm://localhost)?persistent=false) | Disable persistence |
| Queue Reference | dynamicQueues/QUEUENAME | Dynamically define the QUEUENAME to JNDI |
| Topic Reference | dynamicTopics/TOPICNAME | Dynamically define the TOPICNAME to JNDI |

^


## JMS Subscriber

JMS Subscriber will subscribe to messages in a given destination (topic or queue). For those not familiar with JMS, it is the J2EE specification for messaging. There are numerous JMS servers on the market and several open source options.

JMeter does not include any JMS implementation jar; this must be downloaded from the JMS provider and put in the lib directory

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

use JNDI properties file

use

jndi.properties

. Note that the file must be on the classpath - e.g. by updating the

user.classpath

JMeter property. If this option is not selected, JMeter uses the "

JNDI Initial Context Factory

" and "

Provider URL

" fields to create the connection.

Yes

JNDI Initial Context Factory

Name of the context factory

No

Provider URL

The URL for the JMS provider

No

Destination

the message destination (topic or queue name)

Yes

Durable Subscription ID

The ID to use for a durable subscription. On first use the respective queue will automatically be generated by the JMS provider if it does not exist yet.

No

Client ID

The Client ID to use when you use a durable subscription. Be sure to add a variable like

${__threadNum}

when you have more than one Thread.

No

JMS Selector

Message Selector as defined by JMS specification to extract only messages that respect the Selector condition. Syntax uses subpart of SQL 92.

No

Setup

The destination setup type. With

At startup

, the destination name is static (i.e. always same name during the test), with

Each sample

, the destination name is dynamic and is evaluated at each sample (i.e. the destination name may be a variable)

Yes

Authentication

Authentication requirement for the JMS provider

Yes

User

User Name

No

Password

Password (N.B. this is stored unencrypted in the test plan)

No

Number of samples to aggregate

number of samples to aggregate

Yes

Save response

should the sampler store the response. If not, only the response length is returned.

Yes

Timeout

Specify the timeout to be applied, in milliseconds.

0

=none. This is the overall aggregate timeout, not per sample.

Yes

Client

Which client implementation to use. Both of them create connections which can read messages. However they use a different strategy, as described below:

**MessageConsumer.receive()**

calls

receive()

for every requested message. Retains the connection between samples, but does not fetch messages unless the sampler is active. This is best suited to Queue subscriptions.

**MessageListener.onMessage()**

establishes a Listener that stores all incoming messages on a queue. The listener remains active after the sampler completes. This is best suited to Topic subscriptions.

Yes

Stop between samples?

If selected, then JMeter calls

Connection.stop()

at the end of each sample (and calls

start()

before each sample). This may be useful in some cases where multiple samples/threads have connections to the same queue. If not selected, JMeter calls

Connection.start()

at the start of the thread, and does not call

stop()

until the end of the thread.

Yes

Separator

Separator used to separate messages when there is more than one (related to setting Number of samples to aggregate). Note that

\n

,

\r

,

\t

are accepted.

No

Reconnect on error codes (regex)

Regular expression for JMSException error codes which force reconnection. If empty no reconnection will be done

No

Pause between errors (ms)

Pause in milliseconds that Subscriber will make when an error occurs

No

^


## JMS Point-to-Point

This sampler sends and optionally receives JMS Messages through point-to-point connections (queues). It is different from pub/sub messages and is generally used for handling transactions.

request_only will typically be used to put load on a JMS System. request_reply will be used when you want to test response time of a JMS service that processes messages sent to the Request Queue as this mode will wait for the response on the Reply queue sent by this service. browse returns the current queue depth, i.e. the number of messages on the queue. read reads a message from the queue (if any). clear clears the queue, i.e. remove all messages from the queue.

JMeter use the properties java.naming.security.[principal|credentials] - if present - when creating the Queue Connection. If this behaviour is not desired, set the JMeter property JMSSampler.useSecurity.properties=false

JMeter does not include any JMS implementation jar; this must be downloaded from the JMS provider and put in the lib directory

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

QueueConnection Factory

The JNDI name of the queue connection factory to use for connecting to the messaging system.

Yes

JNDI Name Request queue

This is the JNDI name of the queue to which the messages are sent.

Yes

JNDI Name Reply queue

The JNDI name of the receiving queue. If a value is provided here and the communication style is

Request Response

this queue will be monitored for responses to the requests sent.

No

Number of samples to aggregate

Number of samples to aggregate. Only applicable for Communication style Read.

Yes

JMS Selector

Message Selector as defined by JMS specification to extract only messages that respect the Selector condition. Syntax uses subpart of SQL 92.

No

Communication style

The Communication style can be

Request Only

(also known as Fire and Forget),

Request Response

,

Read

,

Browse

,

Clear

:

**Request Only**

will only send messages and will not monitor replies. As such it can be used to put load on a system.

**Request Response**

will send messages and monitor the replies it receives. Behaviour depends on the value of the JNDI Name Reply Queue. If JNDI Name Reply Queue has a value, this queue is used to monitor the results. Matching of request and reply is done with the message id of the request and the correlation id of the reply. If the JNDI Name Reply Queue is empty, then temporary queues will be used for the communication between the requestor and the server. This is very different from the fixed reply queue. With temporary queues the sending thread will block until the reply message has been received. With

Request Response

mode, you need to have a Server that listens to messages sent to Request Queue and sends replies to queue referenced by

message.getJMSReplyTo()

.

**Read**

will read a message from an outgoing queue which has no listeners attached. This can be convenient for testing purposes. This method can be used if you need to handle queues without a binding file (in case the jmeter-jms-skip-jndi library is used), which only works with the JMS Point-to-Point sampler. In case binding files are used, one can also use the JMS Subscriber Sampler for reading from a queue.

**Browse**

will determine the current queue depth without removing messages from the queue, returning the number of messages on the queue.

**Clear**

will clear the queue, i.e. remove all messages from the queue.

Yes

Use alternate fields for message correlation

These check-boxes select the fields which will be used for matching the response message with the original request.

**Use Request Message Id**

if selected, the request JMSMessageID will be used, otherwise the request JMSCorrelationID will be used. In the latter case the correlation id must be specified in the request.

**Use Response Message Id**

if selected, the response JMSMessageID will be used, otherwise the response JMSCorrelationID will be used.

There are two frequently used JMS Correlation patterns:

**JMS Correlation ID Pattern**

i.e. match request and response on their correlation Ids => deselect both checkboxes, and provide a correlation id.

**JMS Message ID Pattern**

i.e. match request message id with response correlation id => select "Use Request Message Id" only.

In both cases the JMS application is responsible for populating the correlation ID as necessary.

if the same queue is used to send and receive messages, then the response message will be the same as the request message. In which case, either provide a correlation id and clear both checkboxes; or select both checkboxes to use the message Id for correlation. This can be useful for checking raw JMS throughput.

Yes

Timeout

The timeout in milliseconds for the reply-messages. If a reply has not been received within the specified time, the specific testcase fails and the specific reply message received after the timeout is discarded. Default value is

2000

ms.

0

means no timeout.

Yes

Expiration

The expiration time (in milliseconds) of the message before it becomes obsolete. If you do not specify an expiration time, the default value is

0

(never expires).

No

Priority

The priority level of the message. There are ten priority levels from

0

(lowest) to

9

(highest). If you do not specify a priority level, the default level is

4

.

No

Use non-persistent delivery mode?

Whether to set

DeliveryMode.NON_PERSISTENT

.

Yes

Content

The content of the message.

No

JMS Properties

The JMS Properties are properties specific for the underlying messaging system. You can setup the name, the value and the class (type) of value. Default type is

String

. For example: for WebSphere 5.1 web services you will need to set the JMS Property targetService to test webservices through JMS.

No

Initial Context Factory

The Initial Context Factory is the factory to be used to look up the JMS Resources.

No

JNDI properties

The JNDI Properties are the specific properties for the underlying JNDI implementation.

No

Provider URL

The URL for the JMS provider.

No

^


## JUnit Request

The current implementation supports standard JUnit convention and extensions. It also includes extensions like

oneTimeSetUp

and

oneTimeTearDown

. The sampler works like the

Java Request

with some differences.

- rather than use JMeter's test interface, it scans the jar files for classes extending JUnit's TestCase class. That includes any class or subclass.
- JUnit test jar files should be placed in jmeter/lib/junit instead of /lib directory. You can also use the "user.classpath" property to specify where to look for TestCase classes.
- JUnit sampler does not use name/value pairs for configuration like the Java Request. The sampler assumes setUp and tearDown will configure the test correctly.
- The sampler measures the elapsed time only for the test method and does not include setUp and tearDown.
- Each time the test method is called, JMeter will pass the result to the listeners.
- Support for oneTimeSetUp and oneTimeTearDown is done as a method. Since JMeter is multi-threaded, we cannot call oneTimeSetUp/oneTimeTearDown the same way Maven does it.
- The sampler reports unexpected exceptions as errors. There are some important differences between standard JUnit test runners and JMeter's implementation. Rather than make a new instance of the class for each test, JMeter creates 1 instance per sampler and reuses it. This can be changed with checkbox "Create a new instance per sample".

The current implementation of the sampler will try to create an instance using the string constructor first. If the test class does not declare a string constructor, the sampler will look for an empty constructor. Example below:

JUnit Constructors

¶

Empty Constructor:

```
public class myTestCase {
  public myTestCase() {}
}
```

String Constructor:

```
public class myTestCase {
  public myTestCase(String text) {
    super(text);
  }
}
```

By default, JMeter will provide some default values for the success/failure code and message. Users should define a set of unique success and failure codes and use them uniformly across all tests.

### General Guidelines

If you use

setUp

and

tearDown

, make sure the methods are declared public. If you do not, the test may not run properly.

Here are some general guidelines for writing JUnit tests so they work well with JMeter. Since JMeter runs multi-threaded, it is important to keep certain things in mind.

- Write the setUp and tearDown methods so they are thread safe. This generally means avoid using static members.
- Make the test methods discrete units of work and not long sequences of actions. By keeping the test method to a discrete operation, it makes it easier to combine test methods to create new test plans.
- Avoid making test methods depend on each other. Since JMeter allows arbitrary sequencing of test methods, the runtime behavior is different than the default JUnit behavior.
- If a test method is configurable, be careful about where the properties are stored. Reading the properties from the Jar file is recommended.
- Each sampler creates an instance of the test class, so write your test so the setup happens in oneTimeSetUp and oneTimeTearDown.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Search for JUnit4 annotations

Select this to search for JUnit4 tests (

@Test

annotations)

Yes

Package filter

Comma separated list of packages to show. Example,

org.apache.jmeter

,

junit.framework

.

Class name

Fully qualified name of the JUnit test class.

Yes

Constructor string

String pass to the string constructor. If a string is set, the sampler will use the string constructor instead of the empty constructor.

Test method

The method to test.

Yes

Success message

A descriptive message indicating what success means.

Success code

An unique code indicating the test was successful.

Failure message

A descriptive message indicating what failure means.

Failure code

An unique code indicating the test failed.

Error message

A description for errors.

Error code

Some code for errors. Does not need to be unique.

Do not call setUp and tearDown

Set the sampler not to call

setUp

and

tearDown

. By default,

setUp

and

tearDown

should be called. Not calling those methods could affect the test and make it inaccurate. This option should only be used with calling

oneTimeSetUp

and

oneTimeTearDown

. If the selected method is

oneTimeSetUp

or

oneTimeTearDown

, this option should be checked.

Yes

Append assertion errors

Whether or not to append assertion errors to the response message.

Yes

Append runtime exceptions

Whether or not to append runtime exceptions to the response message. Only applies if "

Append assertion errors

" is not selected.

Yes

Create a new Instance per sample

Whether or not to create a new JUnit instance for each sample. Defaults to false, meaning JUnit

TestCase

is created one and reused.

Yes

The following JUnit4 annotations are recognised:

**@Test**

used to find test methods and classes. The "

expected

" and "

timeout

" attributes are supported.

**@Before**

treated the same as

setUp()

in JUnit3

**@After**

treated the same as

tearDown()

in JUnit3

**@BeforeClass, @AfterClass**

treated as test methods so they can be run independently as required

Note that JMeter currently runs the test methods directly, rather than leaving it to JUnit. This is to allow the

setUp

/

tearDown

methods to be excluded from the sample time. As a consequence, the sampler time excludes the time taken to call

setUp

/

tearDown

methods and their annotation based alternatives.

^
