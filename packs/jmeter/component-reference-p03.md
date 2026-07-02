---
title: "Apache JMeter (part 3/8)"
source: https://jmeter.apache.org/usermanual/component_reference.html
domain: jmeter
license: CC-BY-SA-4.0
tags: jmeter apache, load testing, performance testing, test plan
fetched: 2026-07-02
part: 3/8
---

## Mail Reader Sampler

The Mail Reader Sampler can read (and optionally delete) mail messages using POP3(S) or IMAP(S) protocols.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Server Type

The protocol used by the provider: e.g.

pop3

,

pop3s

,

imap

,

imaps

. or another string representing the server protocol. For example

file

for use with the read-only mail file provider. The actual provider names for POP3 and IMAP are

pop3

and

imap

Yes

Server

Hostname or IP address of the server. See below for use with

file

protocol.

Yes

Port

Port to be used to connect to the server (optional)

No

Username

User login name

Password

User login password (N.B. this is stored unencrypted in the test plan)

Folder

The IMAP(S) folder to use. See below for use with

file

protocol.

Yes, if using IMAP(S)

Number of messages to retrieve

Set this to retrieve all or some messages

Yes

Fetch headers only

If selected, only the message headers will be retrieved.

Yes

Delete messages from the server

If set, messages will be deleted after retrieval

Yes

Store the message using MIME

Whether to store the message as MIME. If so, then the entire raw message is stored in the Response Data; the headers are not stored as they are available in the data. If not, the message headers are stored as Response Headers. A few headers are stored (

Date

,

To

,

From

,

Subject

) in the body.

Yes

Use no security features

Indicates that the connection to the server does not use any security protocol.

Use SSL

Indicates that the connection to the server must use the SSL protocol.

Use StartTLS

Indicates that the connection to the server should attempt to start the TLS protocol.

Enforce StartTLS

If the server does not start the TLS protocol the connection will be terminated.

Trust All Certificates

When selected it will accept all certificates independent of the CA.

Use local truststore

When selected it will only accept certificates that are locally trusted.

Local truststore

Path to file containing the trusted certificates. Relative paths are resolved against the current directory.

Failing that, against the directory containing the test script (JMX file).

You can pass mail related environment properties by adding to

user.properties

any of the properties described

here

.

Messages are stored as subsamples of the main sampler. Multipart message parts are stored as subsamples of the message.

**Special handling for "file" protocol:** The file JavaMail provider can be used to read raw messages from files. The server field is used to specify the path to the parent of the folder. Individual message files should be stored with the name n.msg, where n is the message number. Alternatively, the server field can be the name of a file which contains a single message. The current implementation is quite basic, and is mainly intended for debugging purposes.

^


## Flow Control Action (was: Test Action )

The Flow Control Action sampler is a sampler that is intended for use in a conditional controller. Rather than generate a sample, the test element either pauses or stops the selected target.

This sampler can also be useful in conjunction with the Transaction Controller, as it allows pauses to be included without needing to generate a sample. For variable delays, set the pause time to zero, and add a Timer as a child.

The "Stop" action stops the thread or test after completing any samples that are in progress. The "Stop Now" action stops the test without waiting for samples to complete; it will interrupt any active samples. If some threads fail to stop within the 5 second time-limit, a message will be displayed in GUI mode. You can try using the Stop command to see if this will stop the threads, but if not, you should exit JMeter. In CLI mode, JMeter will exit if some threads fail to stop within the 5 second time limit. The time to wait can be changed using the JMeter property jmeterengine.threadstop.wait. The time is given in milliseconds.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Target

Current Thread

/

All Threads

(ignored for

Pause

and

Go to next loop iteration

)

Yes

Action

Pause

/

Stop

/

Stop Now

/

Go to next loop iteration

Yes

Duration

How long to pause for (milliseconds)

Yes, if Pause is selected

^


## SMTP Sampler

The SMTP Sampler can send mail messages using SMTP/SMTPS protocol. It is possible to set security protocols for the connection (SSL and TLS), as well as user authentication. If a security protocol is used a verification on the server certificate will occur. Two alternatives to handle this verification are available:

**Trust all certificates**

This will ignore certificate chain verification

**Use a local truststore**

With this option the certificate chain will be validated against the local truststore file.

### Parameters

Attribute

Description

Required

Server

Hostname or IP address of the server. See below for use with

file

protocol.

Yes

Port

Port to be used to connect to the server. Defaults are: SMTP=25, SSL=465, StartTLS=587

No

Connection timeout

Connection timeout value in milliseconds (socket level). Default is infinite timeout.

No

Read timeout

Read timeout value in milliseconds (socket level). Default is infinite timeout.

No

Address From

The from address that will appear in the e-mail

Yes

Address To

The destination e-mail address (multiple values separated by "

;

")

Yes, unless CC or BCC is specified

Address To CC

Carbon copy destinations e-mail address (multiple values separated by "

;

")

No

Address To BCC

Blind carbon copy destinations e-mail address (multiple values separated by "

;

")

No

Address Reply-To

Alternate Reply-To address (multiple values separated by "

;

")

No

Use Auth

Indicates if the SMTP server requires user authentication

Username

User login name

Password

User login password (N.B. this is stored unencrypted in the test plan)

Use no security features

Indicates that the connection to the SMTP server does not use any security protocol.

Use SSL

Indicates that the connection to the SMTP server must use the SSL protocol.

Use StartTLS

Indicates that the connection to the SMTP server should attempt to start the TLS protocol.

Enforce StartTLS

If the server does not start the TLS protocol the connection will be terminated.

Trust All Certificates

When selected it will accept all certificates independent of the CA.

Use local truststore

When selected it will only accept certificates that are locally trusted.

Local truststore

Path to file containing the trusted certificates. Relative paths are resolved against the current directory.

Failing that, against the directory containing the test script (JMX file).

Override System SSL/TLS Protocols

Specify a custom SSL/TLS protocol as space separated list to use on handshake example

TLSv1 TLSv1.1 TLSv1.2

. Defaults to all supported protocols.

No

Subject

The e-mail message subject.

Suppress Subject Header

If selected, the "

Subject:

" header is omitted from the mail that is sent. This is different from sending an empty "

Subject:

" header, though some e-mail clients may display it identically.

Include timestamp in subject

Includes the

System.currentTimemillis()

in the subject line.

Add Header

Additional headers can be defined using this button.

No

Message

The message body.

Send plain body (i.e. not multipart/mixed)

If selected, then send the body as a plain message, i.e. not

multipart/mixed

, if possible. If the message body is empty and there is a single file, then send the file contents as the message body.

Note: If the message body is not empty, and there is at least one attached file, then the body is sent as

multipart/mixed

.

No

Attach files

Files to be attached to the message.

Send .eml

If set, the

.eml

file will be sent instead of the entries in the

Subject

,

Message

, and

Attach file(s)

fields

Calculate message size

Calculates the message size and stores it in the sample result.

Enable debug logging?

If set, then the "

mail.debug

" property is set to "

true

"

^


## OS Process Sampler

The OS Process Sampler is a sampler that can be used to execute commands on the local machine. It should allow execution of any command that can be run from the command line. Validation of the return code can be enabled, and the expected return code can be specified.

Note that OS shells generally provide command-line parsing. This varies between OSes, but generally the shell will split parameters on white-space. Some shells expand wild-card file names; some don't. The quoting mechanism also varies between OSes. The sampler deliberately does not do any parsing or quote handling. The command and its parameters must be provided in the form expected by the executable. This means that the sampler settings will not be portable between OSes.

Many OSes have some built-in commands which are not provided as separate executables. For example the Windows DIR command is part of the command interpreter (CMD.EXE). These built-ins cannot be run as independent programs, but have to be provided as arguments to the appropriate command interpreter.

For example, the Windows command-line: DIR C:\TEMP needs to be specified as follows:

**Command:**

CMD

**Param 1:**

/C

**Param 2:**

DIR

**Param 3:**

C:\TEMP

### Parameters

Attribute

Description

Required

Command

The program name to execute.

Yes

Working directory

Directory from which command will be executed, defaults to folder referenced by "

user.dir

" System property

No

Command Parameters

Parameters passed to the program name.

No

Environment Parameters

Key/Value pairs added to environment when running command.

No

Standard input (stdin)

Name of file from which input is to be taken (

STDIN

).

No

Standard output (stdout

Name of output file for standard output (

STDOUT

). If omitted, output is captured and returned as the response data.

No

Standard error (stderr)

Name of output file for standard error (

STDERR

). If omitted, output is captured and returned as the response data.

No

Check Return Code

If checked, sampler will compare return code with

Expected Return Code

.

No

Expected Return Code

Expected return code for System Call, required if "

Check Return Code

" is checked. Note 500 is used as an error indicator in JMeter so you should not use it.

No

Timeout

Timeout for command in milliseconds, defaults to

0

, which means

no

timeout. If the timeout expires before the command finishes, JMeter will attempt to kill the OS process.

No

^


## MongoDB Script (DEPRECATED)

This sampler lets you send a Request to a MongoDB.

Before using this you need to set up a MongoDB Source Config Configuration element

This Element currently uses

com.mongodb.DB#eval

which takes a global write lock causing a performance impact on the database, see

db.eval()

. So it is better to avoid using this element for load testing and use JSR223+Groovy scripting using

MongoDBHolder

instead. MongoDB Script is more suitable for functional testing or test setup (setup/teardown threads)

### Parameters

Attribute

Description

Required

Name

Descriptive name for this sampler that is shown in the tree.

No

MongoDB Source

Name of the JMeter variable that the MongoDB connection is bound to. This must agree with the '

MongoDB Source

' field of a MongoDB Source Config.

Yes

Database Name

Database Name, will be used in your script

Yes

Username

No

Password

No

Script

Mongo script as it would be used in MongoDB shell

Yes

See also:

- MongoDB Source Config

Ensure Variable Name is unique across Test Plan.

^

^


## Bolt Request

This sampler allows you to run Cypher queries through the Bolt protocol.

Before using this you need to set up a Bolt Connection Configuration

Every request uses a connection acquired from the pool and returns it to the pool when the sampler completes. The connection pool size defaults to 100 and is configurable.

The measured response time corresponds to the "full" query execution, including both the time to execute the cypher query AND the time to consume the results sent back by the database.

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

Cypher statement

The query to execute.

Yes

Params

The parameter values, JSON formatted.

No

Record Query Results

Whether to add or not query result data to the sampler response (default false). Note that activating this has a memory overhead, use it wisely.

No

Access Mode

Whether to access the database in WRITE or READ mode. Use WRITE for a standalone Neo4j instance. For a Neo4j cluster, select mode depending on whether the query writes to the database. That setting will allow correct routing to the cluster leader, followers or read replicas.

Yes

Database

The database to run the query against. Required for Neo4j 4.0+, unless querying the default database. Must be undefined for Neo4j 3.5.

No

Transaction timeout

Timeout for the transaction.

No

It is strongly advised to use query parameters, allowing the database to cache and reuse execution plans.

See also:

- Bolt Connection Configuration

^

^

# 18.2 Logic Controllers

Logic Controllers determine the order in which Samplers are processed.


## Simple Controller

The Simple Logic Controller lets you organize your Samplers and other Logic Controllers. Unlike other Logic Controllers, this controller provides no functionality beyond that of a storage device.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

Using the Simple Controller

¶

Download this example (see Figure 6). In this example, we created a Test Plan that sends two Ant HTTP requests and two Log4J HTTP requests. We grouped the Ant and Log4J requests by placing them inside Simple Logic Controllers. Remember, the Simple Logic Controller has no effect on how JMeter processes the controller(s) you add to it. So, in this example, JMeter sends the requests in the following order: Ant Home Page, Ant News Page, Log4J Home Page, Log4J History Page.

Note, the File Reporter is configured to store the results in a file named "simple-test.dat" in the current directory.

^


## Loop Controller

If you add Generative or Logic Controllers to a Loop Controller, JMeter will loop through them a certain number of times, in addition to the loop value you specified for the Thread Group. For example, if you add one HTTP Request to a Loop Controller with a loop count of two, and configure the Thread Group loop count to three, JMeter will send a total of 2 * 3 = 6 HTTP Requests. JMeter will expose the looping index as a variable named __jm__<Name of your element>__idx. So for example, if your Loop Controller is named LC, then you can access the looping index through ${__jm__LC__idx}. Index starts at 0

### Parameters

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

Loop Count

The number of times the subelements of this controller will be iterated each time through a test run.

The value -1 is equivalent to checking the Forever toggle.

**Special Case:** The Loop Controller embedded in the Thread Group element behaves slightly different. Unless set to forever, it stops the test after the given number of iterations have been done.

When using a function in this field, be aware it may be evaluated multiple times. Example using

__Random

will evaluate it to a different value for each child samplers of Loop Controller and result into unwanted behaviour.

Yes, unless "Forever" is checked

Looping Example

¶

Download this example (see Figure 4). In this example, we created a Test Plan that sends a particular HTTP Request only once and sends another HTTP Request five times.

We configured the Thread Group for a single thread and a loop count value of one. Instead of letting the Thread Group control the looping, we used a Loop Controller. You can see that we added one HTTP Request to the Thread Group and another HTTP Request to a Loop Controller. We configured the Loop Controller with a loop count value of five.

JMeter will send the requests in the following order: Home Page, News Page, News Page, News Page, News Page, and News Page.

Note, the File Reporter is configured to store the results in a file named "

loop-test.dat

" in the current directory.

^


## Once Only Controller

The Once Only Logic Controller tells JMeter to process the controller(s) inside it only once per Thread, and pass over any requests under it during further iterations through the test plan.

The Once Only Controller will now execute always during the first iteration of any looping parent controller. Thus, if the Once Only Controller is placed under a Loop Controller specified to loop 5 times, then the Once Only Controller will execute only on the first iteration through the Loop Controller (i.e. every 5 times).

Note this means the Once Only Controller will still behave as previously expected if put under a Thread Group (runs only once per test per Thread), but now the user has more flexibility in the use of the Once Only Controller.

For testing that requires a login, consider placing the login request in this controller since each thread only needs to login once to establish a session.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

Once Only Example

¶

Download this example (see Figure 5). In this example, we created a Test Plan that has two threads that send HTTP request. Each thread sends one request to the Home Page, followed by three requests to the Bug Page. Although we configured the Thread Group to iterate three times, each JMeter thread only sends one request to the Home Page because this request lives inside a Once Only Controller.

Each JMeter thread will send the requests in the following order: Home Page, Bug Page, Bug Page, Bug Page.

Note, the File Reporter is configured to store the results in a file named "loop-test.dat" in the current directory.

^


## Interleave Controller

If you add Generative or Logic Controllers to an Interleave Controller, JMeter will alternate among each of the other controllers for each loop iteration.

### Parameters

Attribute

Description

Required

name

Descriptive name for this controller that is shown in the tree.

No

ignore sub-controller blocks

If checked, the interleave controller will treat sub-controllers like single request elements and only allow one request per controller at a time.

No

Interleave across threads

If checked, the interleave controller will alternate among each of its children controllers for each loop iteration but across all threads, for example in a configuration with 4 threads and 3 child controllers, on first iteration thread 1 will run first child, thread 2 second child, thread 3 third child, thread 4 first child, on next iteration each thread will run the following child controller

No

Simple Interleave Example

¶

Download this example (see Figure 1). In this example, we configured the Thread Group to have two threads and a loop count of five, for a total of ten requests per thread. See the table below for the sequence JMeter sends the HTTP Requests.

| Loop Iteration | Each JMeter Thread Sends These HTTP Requests |
|---|---|
| 1 | News Page |
| 1 | Log Page |
| 2 | FAQ Page |
| 2 | Log Page |
| 3 | Gump Page |
| 3 | Log Page |
| 4 | Because there are no more requests in the controller, JMeter starts over and sends the first HTTP Request, which is the News Page. |
| 4 | Log Page |
| 5 | FAQ Page |
| 5 | Log Page |

Useful Interleave Example

¶

Download another example (see Figure 2). In this example, we configured the Thread Group to have a single thread and a loop count of eight. Notice that the Test Plan has an outer Interleave Controller with two Interleave Controllers inside of it.

The outer Interleave Controller alternates between the two inner ones. Then, each inner Interleave Controller alternates between each of the HTTP Requests. Each JMeter thread will send the requests in the following order: Home Page, Interleaved, Bug Page, Interleaved, CVS Page, Interleaved, and FAQ Page, Interleaved.

Note, the File Reporter is configured to store the results in a file named "interleave-test2.dat" in the current directory.

If the two interleave controllers under the main interleave controller were instead simple controllers, then the order would be: Home Page, CVS Page, Interleaved, Bug Page, FAQ Page, Interleaved.

However, if "ignore sub-controller blocks" was checked on the main interleave controller, then the order would be: Home Page, Interleaved, Bug Page, Interleaved, CVS Page, Interleaved, and FAQ Page, Interleaved.

^


## Random Controller

The Random Logic Controller acts similarly to the Interleave Controller, except that instead of going in order through its sub-controllers and samplers, it picks one at random at each pass.

Interactions between multiple controllers can yield complex behavior. This is particularly true of the Random Controller. Experiment before you assume what results any given interaction will give

### Parameters

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

ignore sub-controller blocks

If checked, the interleave controller will treat sub-controllers like single request elements and only allow one request per controller at a time.

No

^


## Random Order Controller

The Random Order Controller is much like a Simple Controller in that it will execute each child element at most once, but the order of execution of the nodes will be random.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

^


## Throughput Controller

The Throughput Controller allows the user to control how often it is executed. There are two modes: percent execution total executions Percent executions causes the controller to execute a certain percentage of the iterations through the test plan. Total executions causes the controller to stop executing after a certain number of executions have occurred. Like the Once Only Controller, this setting is reset when a parent Loop Controller restarts.

This controller is badly named, as it does not control throughput. Please refer to the

Constant Throughput Timer

for an element that can be used to adjust the throughput.

The Throughput Controller can yield very complex behavior when combined with other controllers - in particular with interleave or random controllers as parents (also very useful).

### Parameters

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

Execution Style

Whether the controller will run in percent executions or total executions mode.

Yes

Throughput

A number. For percent execution mode, a number from

0

-

100

that indicates the percentage of times the controller will execute. "

50

" means the controller will execute during half the iterations through the test plan. For total execution mode, the number indicates the total number of times the controller will execute.

Yes

Per User

If checked, per user will cause the controller to calculate whether it should execute on a per user (per thread) basis. If unchecked, then the calculation will be global for all users. For example, if using total execution mode, and uncheck "

per user

", then the number given for throughput will be the total number of executions made. If "

per user

" is checked, then the total number of executions would be the number of users times the number given for throughput.

No

^


## Runtime Controller

The Runtime Controller controls how long its children will run. Controller will run its children until configured Runtime(s) is exceeded.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree, and used to name the transaction.

Yes

Runtime (seconds)

Desired runtime in seconds. 0 means no run.

Yes

^


## If Controller

The If Controller allows the user to control whether the test elements below it (its children) are run or not.

By default, the condition is evaluated only once on initial entry, but you have the option to have it evaluated for every runnable element contained in the controller.

The best option (default one) is to check Interpret Condition as Variable Expression?, then in the condition field you have 2 options: Option 1: Use a variable that contains true or false If you want to test if last sample was successful, you can use ${JMeterThread.last_sample_ok} (If Controller using Variable) Option 2: Use a function (${__jexl3()} is advised) to evaluate an expression that must return true or false (If Controller using expression) For example, previously one could use the condition: ${__jexl3(${VAR} == 23)} and this would be evaluated as true/false, the result would then be passed to JavaScript which would then return true/false. If the Variable Expression option is selected, then the expression is evaluated and compared with "true", without needing to use JavaScript.

To test if a variable is undefined (or null) do the following, suppose var is named

myVar

, expression will be:

```
"${myVar}" == "\${myVar}"
```

Or use:

```
"${myVar}" != "\${myVar}"
```

to test if a variable is defined and is not null.

If you uncheck

Interpret Condition as Variable Expression?

,

If Controller

will internally use javascript to evaluate the condition which has a performance penalty that can be very big and make your test less scalable.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

Condition (default JavaScript)

By default the condition is interpreted as

JavaScript

code that returns "

true

" or "

false

", but this can be overridden (see below)

Yes

Interpret Condition as Variable Expression?

If this is selected, then the condition must be an expression that evaluates to "

true

" (case is ignored). For example,

${FOUND}

or

${__jexl3(${VAR} > 100)}

. Unlike the JavaScript case, the condition is only checked to see if it matches "

true

" (case is ignored).

Checking this and using

__jexl3

or

__groovy

function in Condition is advised for performances

Yes

Evaluate for all children

Should condition be evaluated for all children? If not checked, then the condition is only evaluated on entry.

Yes

Examples (JavaScript)

¶

- ${COUNT} < 10
- "${VAR}" == "abcd"

If there is an error interpreting the code, the condition is assumed to be

false

, and a message is logged in

jmeter.log

.

Note it is advised to avoid using JavaScript mode for performance.

When using

__groovy

take care to not use variable replacement in the string, otherwise if using a variable that changes the script cannot be cached. Instead get the variable using:

vars.get("myVar").

See the Groovy examples below.

Examples (Variable Expression)

¶

- ${__groovy(vars.get("myVar") != "Invalid" )} (Groovy check myVar is not equal to Invalid)
- ${__groovy(vars.get("myInt").toInteger() <=4 )} (Groovy check myInt is less then or equal to 4)
- ${__groovy(vars.get("myMissing") != null )} (Groovy check if the myMissing variable is not set)
- ${__jexl3(${COUNT} < 10)}
- ${RESULT}
- ${JMeterThread.last_sample_ok} (check if the last sample succeeded)

^


## While Controller

The While Controller runs its children until the condition is "false". JMeter will expose the looping index as a variable named __jm__<Name of your element>__idx. So for example, if your While Controller is named WC, then you can access the looping index through ${__jm__WC__idx}. Index starts at 0

Possible condition values:

- blank - exit loop when last sample in loop fails
- LAST - exit loop when last sample in loop fails. If the last sample just before the loop failed, don't enter loop.
- Otherwise - exit (or don't enter) the loop when the condition is equal to the string "false"

The condition can be any variable or function that eventually evaluates to the string "

false

". This allows the use of

__jexl3

,

__groovy

function, properties or variables as needed.

Note that the condition is evaluated twice, once before starting sampling children and once at end of children sampling, so putting non idempotent functions in Condition (like

__counter

) can introduce issues.

For example:

- ${VAR} - where VAR is set to false by some other test element
- ${__jexl3(${C}==10)}
- ${__jexl3("${VAR2}"=="abcd")}
- ${_P(property)} - where property is set to "false" somewhere else

### Parameters

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree, and used to name the transaction.

No

Condition

blank,

LAST

, or variable/function

No

^


## Switch Controller

The Switch Controller acts like the Interleave Controller in that it runs one of the subordinate elements on each iteration, but rather than run them in sequence, the controller runs the element defined by the switch value.

The switch value can also be a name.

If the switch value is out of range, it will run the zeroth element, which therefore acts as the default for the numeric case. It also runs the zeroth element if the value is the empty string.

If the value is non-numeric (and non-empty), then the Switch Controller looks for the element with the same name (case is significant). If none of the names match, then the element named "default" (case not significant) is selected. If there is no default, then no element is selected, and the controller will not run anything.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

Switch Value

The number (or name) of the subordinate element to be invoked. Elements are numbered from 0. Defaults to 0

No

^


## ForEach Controller

A ForEach controller loops through the values of a set of related variables. When you add samplers (or controllers) to a ForEach controller, every sample (or controller) is executed one or more times, where during every loop the variable has a new value. The input should consist of several variables, each extended with an underscore and a number. Each such variable must have a value. So for example when the input variable has the name inputVar, the following variables should have been defined:

- inputVar_1 = wendy
- inputVar_2 = charles
- inputVar_3 = peter
- inputVar_4 = john

Note: the "_" separator is now optional.

When the return variable is given as "returnVar", the collection of samplers and controllers under the ForEach controller will be executed 4 consecutive times, with the return variable having the respective above values, which can then be used in the samplers.

JMeter will expose the looping index as a variable named __jm__<Name of your element>__idx. So for example, if your Loop Controller is named FEC, then you can access the looping index through ${__jm__FEC__idx}. Index starts at 0

It is especially suited for running with the regular expression post-processor. This can "create" the necessary input variables out of the result data of a previous request. By omitting the "_" separator, the ForEach Controller can be used to loop through the groups by using the input variable refName_g, and can also loop through all the groups in all the matches by using an input variable of the form refName_${C}_g, where C is a counter variable.

The ForEach Controller does not run any samples if

inputVar_1

is

null

. This would be the case if the Regular Expression returned no matches.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

Input variable prefix

Prefix for the variable names to be used as input. Defaults to an empty string as prefix.

No

Start index for loop

Start index (exclusive) for loop over variables (first element is at start index + 1)

No

End index for loop

End index (inclusive) for loop over variables

No

Output variable

The name of the variable which can be used in the loop for replacement in the samplers. Defaults to an empty variable name, which is most probably not wanted.

No

Use Separator

If not checked, the "

_

" separator is omitted.

Yes

ForEach Example

¶

Download this example (see Figure 7). In this example, we created a Test Plan that sends a particular HTTP Request only once and sends another HTTP Request to every link that can be found on the page.

We configured the Thread Group for a single thread and a loop count value of one. You can see that we added one HTTP Request to the Thread Group and another HTTP Request to the ForEach Controller.

After the first HTTP request, a regular expression extractor is added, which extracts all the html links out of the return page and puts them in the inputVar variable

In the ForEach loop, a HTTP sampler is added which requests all the links that were extracted from the first returned HTML page.

ForEach Example

¶

Here is another example you can download. This has two Regular Expressions and ForEach Controllers. The first RE matches, but the second does not match, so no samples are run by the second ForEach Controller

The Thread Group has a single thread and a loop count of two.

Sample 1 uses the JavaTest Sampler to return the string "a b c d".

The Regex Extractor uses the expression (\w)\s which matches a letter followed by a space, and returns the letter (not the space). Any matches are prefixed with the string "inputVar".

The ForEach Controller extracts all variables with the prefix "inputVar_", and executes its sample, passing the value in the variable "returnVar". In this case it will set the variable to the values "a" "b" and "c" in turn.

The For 1 Sampler is another Java Sampler which uses the return variable "returnVar" as part of the sample Label and as the sampler Data.

Sample 2, Regex 2 and For 2 are almost identical, except that the Regex has been changed to "(\w)\sx", which clearly won't match. Thus the For 2 Sampler will not be run.

^


## Module Controller

The Module Controller provides a mechanism for substituting test plan fragments into the current test plan at run-time.

A test plan fragment consists of a Controller and all the test elements (samplers etc.) contained in it. The fragment can be located in any Thread Group. If the fragment is located in a Thread Group, then its Controller can be disabled to prevent the fragment being run except by the Module Controller. Or you can store the fragments in a dummy Thread Group, and disable the entire Thread Group.

There can be multiple fragments, each with a different series of samplers under them. The module controller can then be used to easily switch between these multiple test cases simply by choosing the appropriate controller in its drop down box. This provides convenience for running many alternate test plans quickly and easily.

A fragment name is made up of the Controller name and all its parent names. For example:

```
Test Plan / Protocol: JDBC / Control / Interleave Controller (Module1)
```

Any **fragments used by the Module Controller must have a unique name**, as the name is used to find the target controller when a test plan is reloaded. For this reason it is best to ensure that the Controller name is changed from the default - as shown in the example above - otherwise a duplicate may be accidentally created when new elements are added to the test plan.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

Module to Run

The module controller provides a list of all controllers loaded into the gui. Select the one you want to substitute in at runtime.

Yes

^


## Include Controller

The include controller is designed to use an external JMX file. To use it, create a Test Fragment underneath the Test Plan and add any desired samplers, controllers etc. below it. Then save the Test Plan. The file is now ready to be included as part of other Test Plans.

For convenience, a Thread Group can also be added in the external JMX file for debugging purposes. A Module Controller can be used to reference the Test Fragment. The Thread Group will be ignored during the include process.

If the test uses a Cookie Manager or User Defined Variables, these should be placed in the top-level test plan, not the included file, otherwise they are not guaranteed to work.

This element does not support variables/functions in the filename field.

However, if the property

includecontroller.prefix

is defined, the contents are used to prefix the pathname.

When using Include Controller and including the same JMX file, ensure you name the Include Controller differently to avoid facing known issue

Bug 50898

.

If the file cannot be found at the location given by prefix+Filename, then the controller attempts to open the Filename relative to the JMX launch directory.

### Parameters

Attribute

Description

Required

Filename

The file to include.

Yes

^


## Transaction Controller

The Transaction Controller generates an additional sample which measures the overall time taken to perform the nested test elements.

Note: when the check box "

Include duration of timer and pre-post processors in generated sample

" is checked, the time includes all processing within the controller scope, not just the samples.

There are two modes of operation:

- additional sample is added after the nested samples
- additional sample is added as a parent of the nested samples

The generated sample time includes all the times for the nested samplers excluding by default (since 2.11) timers and processing time of pre/post processors unless checkbox "Include duration of timer and pre-post processors in generated sample" is checked. Depending on the clock resolution, it may be slightly longer than the sum of the individual samplers plus timers. The clock might tick after the controller recorded the start time but before the first sample starts. Similarly at the end.

The generated sample is only regarded as successful if all its sub-samples are successful.

In parent mode, the individual samples can still be seen in the Tree View Listener, but no longer appear as separate entries in other Listeners. Also, the sub-samples do not appear in CSV log files, but they can be saved to XML files.

In parent mode, Assertions (etc.) can be added to the Transaction Controller. However by default they will be applied to both the individual samples and the overall transaction sample. To limit the scope of the Assertions, use a Simple Controller to contain the samples, and add the Assertions to the Simple Controller. Parent mode controllers do not currently properly support nested transaction controllers of either type.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree, and used to name the transaction.

Yes

Generate Parent Sample

If checked, then the sample is generated as a parent of the other samples, otherwise the sample is generated as an independent sample.

Yes

Include duration of timer and pre-post processors in generated sample

Whether to include timer, pre- and post-processing delays in the generated sample. Default is

false

Yes

^


## Recording Controller

The Recording Controller is a place holder indicating where the proxy server should record samples to. During test run, it has no effect, similar to the Simple Controller. But during recording using the HTTP(S) Test Script Recorder, all recorded samples will by default be saved under the Recording Controller.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this controller that is shown in the tree.

No

^


## Critical Section Controller

The Critical Section Controller ensures that its children elements (samplers/controllers, etc.) will be executed by only one thread as a named lock will be taken before executing children of controller.

The figure below shows an example of using Critical Section Controller, in the figure below 2 Critical Section Controllers ensure that:

- DS2-${__threadNum} is executed only by one thread at a time
- DS4-${__threadNum} is executed only by one thread at a time

### Parameters

Attribute

Description

Required

Lock Name

Lock that will be taken by controller, ensure you use different lock names for unrelated sections

Yes

Critical Section Controller takes locks only within one JVM, so if using Distributed testing ensure your use case does not rely on all threads of all JVMs blocking.

^

^

# 18.3 Listeners

Most of the listeners perform several roles in addition to "listening" to the test results. They also provide means to view, save, and read saved test results.

Note that Listeners are processed at the end of the scope in which they are found.

The saving and reading of test results is generic. The various listeners have a panel whereby one can specify the file to which the results will be written (or read from). By default, the results are stored as XML files, typically with a ".jtl" extension. Storing as CSV is the most efficient option, but is less detailed than XML (the other available option).

**Listeners do *not* process sample data in CLI mode, but the raw data will be saved if an output file has been configured.** In order to analyse the data generated by a CLI run, you need to load the file into the appropriate Listener.

To read existing results and display them, use the file panel Browse button to open the file.

If you want to clear any current data before loading a new file, use the menu item Run → Clear (Ctrl + Shift + E) or Run → Clear All (Ctrl + E) before loading the file.

Results can be read from XML or CSV format files. When reading from CSV results files, the header (if present) is used to determine which fields are present. **In order to interpret a header-less CSV file correctly, the appropriate properties must be set in jmeter.properties.** XML files written by JMeter have version 1.0 declared in header while actual file is serialized with 1.1 rules. (This is done for historical compatibility reasons; see Bug 59973 and Bug 58679) This causes strict XML parsers to fail. Consider using non-strict XML parsers to read JTL files.

The file name can contain function and/or variable references. However variable references do not work in client-server mode (functions work OK). This is because the file is created on the client, and the client does not run the test locally so does not set up variables.

**Listeners can use a lot of memory if there are a lot of samples.** Most of the listeners currently keep a copy of every sample in their scope, apart from:

- Simple Data Writer
- BeanShell/JSR223 Listener
- Mailer Visualizer
- Summary Report

The following Listeners no longer need to keep copies of every single sample. Instead, samples with the same elapsed time are aggregated. Less memory is now needed, especially if most samples only take a second or two at most.

- Aggregate Report
- Aggregate Graph

To minimise the amount of memory needed, use the Simple Data Writer, and use the CSV format.

JMeter variables can be saved to the output files. This can only be specified using a property. See the

Listener Sample Variables

for details

For full details on setting up the default items to be saved see the Listener Default Configuration documentation. For details of the contents of the output files, see the CSV log format or the XML log format.

The entries in

jmeter.properties

are used to define the defaults; these can be overridden for individual listeners by using the Configure button, as shown below. The settings in

jmeter.properties

also apply to the listener that is added by using the

-l

command-line flag.

The figure below shows an example of the result file configuration panel

### Parameters

Attribute

Description

Required

Filename

Name of the file containing sample results. The file name can be specified using either a relative or an absolute path name. Relative paths are resolved relative to the current working directory (which defaults to the

bin/

directory). JMeter also support paths relative to the directory containing the current test plan (JMX file). If the path name begins with "

~/

" (or whatever is in the

jmeter.save.saveservice.base_prefix

JMeter property), then the path is assumed to be relative to the JMX file location.

No

Browse …

File Browse Button

No

Errors

Select this to write/read only results with errors

No

Successes

Select this to write/read only results without errors. If neither

Errors

nor

Successes

is selected, then all results are processed.

No

Configure

Configure Button, see below

No


## Sample Result Save Configuration

Listeners can be configured to save different items to the result log files (JTL) by using the Config popup as shown below. The defaults are defined as described in the Listener Default Configuration documentation. Items with (CSV) after the name only apply to the CSV format; items with (XML) only apply to XML format. CSV format cannot currently be used to save any items that include line-breaks.

Note that cookies, method and the query string are saved as part of the "Sampler Data" option.

^


## Graph Results

Graph Results MUST NOT BE USED during load test as it consumes a lot of resources (memory and CPU). Use it only for either functional testing or during Test Plan debugging and Validation.

The Graph Results listener generates a simple graph that plots all sample times. Along the bottom of the graph, the current sample (black), the current average of all samples (blue), the current standard deviation (red), and the current throughput rate (green) are displayed in milliseconds.

The throughput number represents the actual number of requests/minute the server handled. This calculation includes any delays you added to your test and JMeter's own internal processing time. The advantage of doing the calculation like this is that this number represents something real - your server in fact handled that many requests per minute, and you can increase the number of threads and/or decrease the delays to discover your server's maximum throughput. Whereas if you made calculations that factored out delays and JMeter's processing, it would be unclear what you could conclude from that number.

The following table briefly describes the items on the graph. Further details on the precise meaning of the statistical terms can be found on the web - e.g. Wikipedia - or by consulting a book on statistics.

- Data - plot the actual data values
- Average - plot the Average
- Median - plot the Median (midway value)
- Deviation - plot the Standard Deviation (a measure of the variation)
- Throughput - plot the number of samples per unit of time

The individual figures at the bottom of the display are the current values. "Latest Sample" is the current elapsed sample time, shown on the graph as "Data".

The value displayed on the top left of graph is the max of 90th percentile of response time.

^


## Assertion Results

Assertion Results MUST NOT BE USED during load test as it consumes a lot of resources (memory and CPU). Use it only for either functional testing or during Test Plan debugging and Validation.

The Assertion Results visualizer shows the Label of each sample taken. It also reports failures of any Assertions that are part of the test plan.

See also:

- Response Assertion

^
