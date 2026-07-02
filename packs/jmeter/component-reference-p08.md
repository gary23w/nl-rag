---
title: "Apache JMeter (part 8/8)"
source: https://jmeter.apache.org/usermanual/component_reference.html
domain: jmeter
license: CC-BY-SA-4.0
tags: jmeter apache, load testing, performance testing, test plan
fetched: 2026-07-02
part: 8/8
---

## Open Model Thread Group

This thread group is experimental, and it might change in the future releases. Please provide your feedback on what works and what could be improved.

Open Model Thread Group defines a pool of users that will execute a particular test case against the server. The users are generated according to the schedule.

The load profile consists of a sequence of constant, increasing or decreasing load. The basic configuration is rate(1/sec) random_arrivals(2 min) rate(3/sec) which means the load will increase linearly from one request per second to three requests per second during a period of two-minutes. If you omit rate at the end, then it will be set to the same value as that from the start. For example, rate(1/sec) random_arrivals(2 min) is exactly the same as rate(1/sec) random_arrivals(2 min) rate(1/sec). That is why rate(1/sec) random_arrivals(2 min) random_arrivals(3 min) rate(4/sec) is exactly the same as rate(1/sec) random_arrivals(2 min) rate(1/sec) random_arrivals(3 min) rate(4/sec), so the load is one request per second during the first two minutes, after which it increases linearly from one request per second to four requests per second during three minutes.

Here are examples for using the schedule: rate(10/sec) random_arrivals(1 min) rate(10/sec) constant load rate of ten requests per second during one minute rate(0) random_arrivals(1 min) rate(10/sec) linearly increase the load from zero requests per second to ten requests per second during one minute rate(0) random_arrivals(1 min) rate(10/sec) random_arrivals(1 min) rate(10/sec) random_arrivals(1 min) rate(0) linearly increase the load from zero requests per second to ten requests per second during one minute, then hold the load during one minute, then linearly decrease the load from ten requests per second to zero during one minute rate(10) random_arrivals(1 min) rate(10/sec) random_arrivals(1 min) rate(10/sec) random_arrivals(1 min) rate(0) linearly increase the load from zero requests per second to ten requests per second during one minute, then hold the load during one minute, then linearly decrease the load from ten requests per second to zero requests per second during one minute rate(10) random_arrivals(1 min) pause(2 sec) random_arrivals(1 min) run with constant load of ten requests per second during one minute, then make two second pause, then resume the load of ten requests per second for one minute

The following commands are available: rate(<number>/sec) configures target load rate. The following time units are supported: ms, sec, min, hour, day. You can omit time unit in case the rate is 0: rate(0) random_arrivals(<number> sec) configures random arrivals schedule with the given duration. The starting load rate is configured before random_arrivals, and the finish load rate is configured after random_arrivals. For example, 10 minute test from five requests per second at the beginning to fifteen request per second at the end could be configured as rate(5/sec) random_arrivals(10 min) rate(15/sec). The implicit rate at the beginning of the test is 0. If the finish rate is not provided (or if several random_arrivals steps go one after another), then the load is constant. For instance, rate(3/sec) random_arrivals(1 min) random_arrivals(2 min) rate(6/sec) configures constant rate of three requests per second for the first minute, and then the load increases from three requests per second to six requests per second during the next two minutes. The time units are the same as in rate. even_arrivals(<number> sec) configures even arrivals (TODO: not implemented yet). For instance, if the desired load is one request per second, then random_arrivals would lauch samples with exactly one second intervals. pause(<number> sec) configures a pause for the given duration. The rate is restored after the pause, so rate(2/sec) random_arrivals(5 sec) pause(5 sec) random_arrivals(5 sec) generates random arrivals with two requests per second rate, then a pause for five seconds (no new arrivals), then five more seconds with two requests per second rate. Note: pause duration is always honoured, even if all the scenarios are complete, and no new ones will be scheduled. For instance, if you use rate(1/sec) random_arrivals(1 min) pause(1 hour), the thread group would always last for sixty-one minutes no matter how much time do individual scenarios take. /* Comments */ can be used to clarify the schedule or temporary disable some steps. Comments cannot be nested. // line comments can be used to clarify the schedule or temporary disable some steps. Line comment lasts till the end of the line.

The thread groups terminates threads as soon as the schedule ends. In other words, the threads are interrupted after all arrivals and pause intervals. If you want to let the threads complete safely, consider adding pause(5 min) at the end of the schedule. That will add five minutes for the threads to continue.

There are no special functions for generating the load profile in a loop, however, the default JMeter templating functions can be helpful for generating the schedule.

For example, the following pattern would generate a sequence of 10 steps where each step lasts 10 seconds: 10/sec, 20/sec, 30/sec, ... ${__groovy((1..10).collect { "rate(" + it*10 + "/sec) random_arrivals(10 sec) pause(1 sec)" }.join(" "))} You can get variables from properties as follows: rate(${__P(beginRate,40)}) random_arrivals(${__P(testDuration, 10)} sec) rate(${__P(endRate,40)})

Currently, the load profile is evaluated at the beginning of the test only, so if you use dynamic functions, then only the first result will be used.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this thread group that is shown in the tree

No

Schedule

The expression that configures schedule. For example:

rate(5/sec) random_arrivals(1 min) pause(5 sec)

Yes

Random Seed (change from 0 to random)

Note: different thread groups should better have different seed values. Constant seed ensures thread group generates the same delays each test start. The value of "0" means the schedule is truly random (non-repeatable from one execution to another)..

No

^


## Thread Group

A Thread Group defines a pool of users that will execute a particular test case against your server. In the Thread Group GUI, you can control the number of users simulated (number of threads), the ramp up time (how long it takes to start all the threads), the number of times to perform the test, and optionally, a start and stop time for the test.

See also tearDown Thread Group and setUp Thread Group.

When using the scheduler, JMeter runs the thread group until either the number of loops is reached or the duration/end-time is reached - whichever occurs first. Note that the condition is only checked between samples; when the end condition is reached, that thread will stop. JMeter does not interrupt samplers which are waiting for a response, so the end time may be delayed arbitrarily.

Since JMeter 3.0, you can run a selection of Thread Group by selecting them and right clicking. A popup menu will appear: (Popup menu to start a selection of Thread Groups) Notice you have three options to run the selection of Thread Groups: Start Start the selected thread groups only Start no pauses Start the selected thread groups only but without running the timers Validate Start the selected thread groups only using validation mode. Per default this runs the Thread Group in validation mode (see below) **Validation Mode:** This mode enables rapid validation of a Thread Group by running it with one thread, one iteration, no timers and no Startup delay set to 0. Behaviour can be modified with some properties by setting in user.properties: testplan_validation.nb_threads_per_thread_group Number of threads to use to validate a Thread Group, by default 1 testplan_validation.ignore_timers Ignore timers when validating the thread group of plan, by default 1 testplan_validation.number_iterations Number of iterations to use to validate a Thread Group testplan_validation.tpc_force_100_pct Whether to force Throughput Controller in percentage mode to run as if percentage was 100 %. Defaults to false

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Action to be taken after a Sampler error

Determines what happens if a sampler error occurs, either because the sample itself failed or an assertion failed. The possible choices are:

- Continue - ignore the error and continue with the test
- Start Next Thread Loop - ignore the error, start next loop and continue with the test
- Stop Thread - current thread exits
- Stop Test - the entire test is stopped at the end of any current samples.
- Stop Test Now - the entire test is stopped abruptly. Any current samplers are interrupted if possible.

No

Number of Threads

Number of users to simulate.

Yes

Ramp-up Period

How long JMeter should take to get all the threads started. If there are 10 threads and a ramp-up time of 100 seconds, then each thread will begin 10 seconds after the previous thread started, for a total time of 100 seconds to get the test fully up to speed.

The first thread will always start directly, so if you configured

one

thread, the ramp-up time is effectively

zero

. For the same reason, the tenth thread in the above example will actually be started after 90 seconds and not 100 seconds.

Yes

Same user on each iteration

If selected, cookie and cache data from the first sampler response are used in subsequent requests (requires a global Cookie and Cache Manager respectively).

If not selected, cookie and cache data from the first sampler response are not used in subsequent requests.

If not selected, a new connection will be opened between iterations which will result in increased response times and consume more resources (memory and cpu).

Yes

Loop Count

Number of times to perform the test case. Alternatively, "

infinite

" can be selected causing the test to run until manually stopped or end of the thread lifetime is reached.

Yes, unless Infinite is selected

Same user on each iteration

If selected, cookie and cache data from the first sampler response are used in subsequent requests (requires a global Cookie and Cache Manager respectively).

If not selected, cookie and cache data from the first sampler response are not used in subsequent requests.

If not selected, a new connection will be opened between iterations which will result in increased response times and consume more resources (memory and cpu).

Yes

Delay Thread creation until needed

If selected, threads are created only when the appropriate proportion of the ramp-up time has elapsed. This is most appropriate for tests with a ramp-up time that is significantly longer than the time to execute a single thread. I.e. where earlier threads finish before later ones start.

If not selected, all threads are created when the test starts (they then pause for the appropriate proportion of the ramp-up time). This is the original default, and is appropriate for tests where threads are active throughout most of the test.

Yes

Specify Thread lifetime

If selected, confines Thread operation time to the given bounds

Yes

Duration (seconds)

If the scheduler checkbox is selected, one can choose a relative end time. JMeter will use this to calculate the End Time.

No

Startup delay (seconds)

If the scheduler checkbox is selected, one can choose a relative startup delay. JMeter will use this to calculate the Start Time.

No

^


## WorkBench

^


## SSL Manager

The SSL Manager is a way to select a client certificate so that you can test applications that use Public Key Infrastructure (PKI). It is only needed if you have not set up the appropriate System properties.

If you want to test client certificate authentication, see

Keystore Configuration

Choosing a Client Certificate

You may either use a Java Key Store (JKS) format key store, or a Public Key Certificate Standard #12 (PKCS12) file for your client certificates. There is a feature of the JSSE libraries that require you to have at least a six character password on your key (at least for the keytool utility that comes with your JDK).

To select the client certificate, choose Options → SSL Manager from the menu bar. You will be presented with a file finder that looks for PKCS12 files by default. Your PKCS12 file must have the extension '.p12' for SSL Manager to recognize it as a PKCS12 file. Any other file will be treated like an average JKS key store. If JSSE is correctly installed, you will be prompted for the password. The text box does not hide the characters you type at this point -- so make sure no one is looking over your shoulder. The current implementation assumes that the password for the keystore is also the password for the private key of the client you want to authenticate as.

Or you can set the appropriate System properties - see the system.properties file.

The next time you run your test, the SSL Manager will examine your key store to see if it has at least one key available to it. If there is only one key, SSL Manager will select it for you. If there is more than one key, it currently selects the first key. There is currently no way to select other entries in the keystore, so the desired key must be the first.

Things to Look Out For

You must have your Certificate Authority (CA) certificate installed properly if it is not signed by one of the five CA certificates that ships with your JDK. One method to install it is to import your CA certificate into a JKS file, and name the JKS file "jssecacerts". Place the file in your JRE's lib/security folder. This file will be read before the "cacerts" file in the same directory. Keep in mind that as long as the "jssecacerts" file exists, the certificates installed in "cacerts" will not be used. This may cause problems for you. If you don't mind importing your CA certificate into the "cacerts" file, then you can authenticate against all of the CA certificates installed.

^


## HTTP(S) Test Script Recorder (was: HTTP Proxy Server )

The HTTP(S) Test Script Recorder allows JMeter to intercept and record your actions while you browse your web application with your normal browser. JMeter will create test sample objects and store them directly into your test plan as you go (so you can view samples interactively while you make them). Ensure you read this wiki page to setup correctly JMeter.

To use the recorder, *add* the HTTP(S) Test Script Recorder element. Right-click on the Test Plan element to get the Add menu: (Add → Non-Test Elements → HTTP(S) Test Script Recorder ).

The recorder is implemented as an HTTP(S) proxy server. You need to set up your browser use the proxy for all HTTP and HTTPS requests. Do not use JMeter as the proxy for any other request types - FTP, etc. - as JMeter cannot handle them.

Ideally use private browsing mode when recording the session. This should ensure that the browser starts with no stored cookies, and prevents certain changes from being saved. For example, Firefox does not allow certificate overrides to be saved permanently.

#### HTTPS recording and certificates

HTTPS connections use certificates to authenticate the connection between the browser and the web server. When connecting via HTTPS, the server presents the certificate to the browser. To authenticate the certificate, the browser checks that the server certificate is signed by a Certificate Authority (CA) that is linked to one of its in-built root CAs. Browsers also check that the certificate is for the correct host or domain, and that it is valid and not expired. If any of the browser checks fail, it will prompt the user who can then decide whether to allow the connection to proceed.

JMeter needs to use its own certificate to enable it to intercept the HTTPS connection from the browser. Effectively JMeter has to pretend to be the target server.

JMeter will generate its own certificate(s). These are generated with a validity period defined by the property proxy.cert.validity, default 7 days, and random passwords. If JMeter detects that it is running under Java 8 or later, it will generate certificates for each target server as necessary (dynamic mode) unless the following property is defined: proxy.cert.dynamic_keys=false. When using dynamic mode, the certificate will be for the correct host name, and will be signed by a JMeter-generated CA certificate. By default, this CA certificate won't be trusted by the browser, however it can be installed as a trusted certificate. Once this is done, the generated server certificates will be accepted by the browser. This has the advantage that even embedded HTTPS resources can be intercepted, and there is no need to override the browser checks for each new server. Browsers don't prompt for embedded resources. So with earlier versions, embedded resources would only be downloaded for servers that were already 'known' to the browser

Unless a keystore is provided (and you define the property proxy.cert.alias), JMeter needs to use the keytool application to create the keystore entries. JMeter includes code to check that keytool is available by looking in various standard places. If JMeter is unable to find the keytool application, it will report an error. If necessary, the system property keytool.directory can be used to tell JMeter where to find keytool. This should be defined in the file system.properties.

The JMeter certificates are generated (if necessary) when the Start button is pressed. Certificate generation can take some while, during which time the GUI will be unresponsive. The cursor is changed to an hour-glass whilst this is happening. When certificate generation is complete, the GUI will display a pop-up dialogue containing the details of the certificate for the root CA. This certificate needs to be installed by the browser in order for it to accept the host certificates generated by JMeter; see below for details.

If necessary, you can force JMeter to regenerate the keystore (and the exported certificates - ApacheJMeterTemporaryRootCA[.usr|.crt]) by deleting the keystore file proxyserver.jks from the JMeter directory.

This certificate is not one of the certificates that browsers normally trust, and will not be for the correct host. As a consequence:

- The browser should display a dialogue asking if you want to accept the certificate or not. For example: You will need to accept the certificate in order to allow the JMeter Proxy to intercept the SSL traffic in order to record it. However, do not accept this certificate permanently; it should only be accepted temporarily. Browsers only prompt this dialogue for the certificate of the main URL, not for the resources loaded in the page, such as images, CSS or JavaScript files hosted on a secured external CDN. If you have such resources (gmail has for example), you'll have to first browse manually to these other domains in order to accept JMeter's certificate for them. Check in jmeter.log for secure domains that you need to register certificate for.
  ```
                                    1) The server's name "www.example.com" does not match the certificate's name
   "_ JMeter Root CA for recording (INSTALL ONLY IF IT S YOURS)". Somebody may be trying to eavesdrop on you.
2) The certificate for "_ JMeter Root CA for recording (INSTALL ONLY IF IT S YOURS)" is signed by the unknown Certificate Authority
   "_ JMeter Root CA for recording (INSTALL ONLY IF IT S YOURS)". It is not possible to verify that this is a valid certificate.

                                
  ```
- If the browser has already registered a validated certificate for this domain, the browser will detect JMeter as a security breach and will refuse to load the page. If so, you have to remove the trusted certificate from your browser's keystore.

Versions of JMeter from 2.10 onwards still support this method, and will continue to do so if you define the following property: proxy.cert.alias The following properties can be used to change the certificate that is used:

- proxy.cert.directory - the directory in which to find the certificate (default = JMeter bin/)
- proxy.cert.file - name of the keystore file (default "proxyserver.jks")
- proxy.cert.keystorepass - keystore password (default "password") [Ignored if using JMeter certificate]
- proxy.cert.keypassword - certificate key password (default "password") [Ignored if using JMeter certificate]
- proxy.cert.type - the certificate type (default "JKS") [Ignored if using JMeter certificate]
- proxy.cert.factory - the factory (default "SunX509") [Ignored if using JMeter certificate]
- proxy.cert.alias - the alias for the key to be used. If this is defined, JMeter does not attempt to generate its own certificate(s).
- proxy.ssl.protocol - the protocol to be used (default "SSLv3")

If your browser currently uses a proxy (e.g. a company intranet may route all external requests via a proxy), then you need to

tell JMeter to use that proxy

before starting JMeter, using the

command-line options

-H

and

-P

. This setting will also be needed when running the generated test plan.

#### Installing the JMeter CA certificate for HTTPS recording

As mentioned above, when run under Java 8, JMeter can generate certificates for each server. For this to work smoothly, the root CA signing certificate used by JMeter needs to be trusted by the browser. The first time that the recorder is started, it will generate the certificates if necessary. The root CA certificate is exported into a file with the name ApacheJMeterTemporaryRootCA in the current launch directory. When the certificates have been set up, JMeter will show a dialog with the current certificate details. At this point, the certificate can be imported into the browser, as per the instructions below.

Note that once the root CA certificate has been installed as a trusted CA, the browser will trust any certificates signed by it. Until such time as the certificate expires or the certificate is removed from the browser, it will not warn the user that the certificate is being relied upon. So anyone that can get hold of the keystore and password can use the certificate to generate certificates which will be accepted by any browsers that trust the JMeter root CA certificate. For this reason, the password for the keystore and private keys are randomly generated and a short validity period used. The passwords are stored in the local preferences area. Please ensure that only trusted users have access to the host with the keystore.

The popup that displays once you start the Recorder is an informational popup:

Just click ok and proceed further.

##### Installing the certificate in Firefox

Choose the following options:

- Tools / Options
- Advanced / Certificates
- View Certificates
- Authorities
- Import …
- Browse to the JMeter launch directory, and click on the file ApacheJMeterTemporaryRootCA.crt, press Open
- Click View and check that the certificate details agree with the ones displayed by the JMeter Test Script Recorder
- If OK, select "Trust this CA to identify web sites", and press OK
- Close dialogs by pressing OK as necessary

##### Installing the certificate in Chrome or Internet Explorer

Both Chrome and Internet Explorer use the same trust store for certificates.

- Browse to the JMeter launch directory, and click on the file ApacheJMeterTemporaryRootCA.crt, and open it
- Click on the "Details" tab and check that the certificate details agree with the ones displayed by the JMeter Test Script Recorder
- If OK, go back to the "General" tab, and click on "Install Certificate …" and follow the Wizard prompts

##### Installing the certificate in Opera

- Tools / Preferences / Advanced / Security
- Manage Certificates …
- Select "Intermediate" tab, click "Import …"
- Browse to the JMeter launch directory, and click on the file ApacheJMeterTemporaryRootCA.usr, and open it

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Port

The port that the HTTP(S) Test Script Recorder listens to.

8888

is the default, but you can change it.

Yes

HTTPS Domains

List of domain (or host) names for HTTPS. Use this to pre-generate certificates for all servers you wish to record.

For example,

*.example.com,*.subdomain.example.com

Note that wildcard domains only apply to one level, i.e.

abc.subdomain.example.com

matches

*.subdomain.example.com

but not

*.example.com

No

Target Controller

The controller where the proxy will store the generated samples. By default, it will look for a Recording Controller and store them there wherever it is.

Yes

Grouping

Whether to group samplers for requests from a single "click" (requests received without significant time separation), and how to represent that grouping in the recording:

- Do not group samplers - store all recorded samplers sequentially, without any grouping.
- Add separators between groups - add a controller named "--------------" to create a visual separation between the groups. Otherwise the samplers are all stored sequentially.
- Put each group in a new controller - create a new Simple Controller for each group, and store all samplers for that group in it.
- Store 1st sampler of each group only - only the first request in each group will be recorded. The "Follow Redirects" and "Retrieve All Embedded Resources …" flags will be turned on in those samplers.
- Put each group in a new transaction controller - create a new Transaction Controller for each group, and store all samplers for that group in it.

The property

proxy.pause

determines the minimum gap that JMeter needs between requests to treat them as separate "clicks". The default is

5000

(milliseconds) i.e. 5 seconds. If you are using grouping, please ensure that you leave the required gap between clicks.

Yes

Capture HTTP Headers

Should headers be added to the plan? If specified, a Header Manager will be added to each HTTP Sampler. The Proxy server always removes Cookie and Authorization headers from the generated Header Managers. By default it also removes

If-Modified-Since

and

If-None-Match

headers. These are used to determine if the browser cache items are up to date; when recording one normally wants to download all the content. To change which additional headers are removed, define the JMeter property

proxy.headers.remove

as a comma-separated list of headers.

Yes

Add Assertions

Add a blank assertion to each sampler?

Yes

Regex Matching

Use Regex Matching when replacing variables? If checked replacement will use word boundaries, i.e. it will only replace word matching values of variable, not part of a word. A word boundary follows Perl5 definition and is equivalent to

\b

. More information below in the paragraph about "

User Defined Variable replacement

".

Yes

Prefix/Transaction name

Add a prefix to sampler name during recording (Prefix mode). Or replace sampler name by user chosen name (Transaction name)

No

Naming scheme

Select the naming scheme for sampler names during recording. Default is

Transaction name

No

Naming format

If

Use format string

is selected as naming scheme, a freestyle format can be given. Placeholders for the transaction name, scheme, host, port, path and counter can be given by

#{name}

,

#{scheme}

,

#{host}

,

#{port}

,

#{path}

,

#{url}

and

#{counter}

. A simple format could be "

#{name}-#{counter}

", which would be equivalent to the numbered default naming scheme. For more complex formatting Java formatting for MessageFormat can be used, as in "

#{counter,number,000}: #{name}-#{path}

", which would print the counter filled with up to three zeroes. Note that scheme is called

protocol

in the sampler GUI and host is called

domain

. Default is an empty string.

No

Counter start value

Can be used to reset the counter to a given value. Note, that the next sample will first increment and then use the value. If the first sampler should start with

1

, reset the counter to

0

.

No

Create new transaction after request (ms)

Inactivity time between two requests needed to consider them in two separate groups.

No

Type

Which type of sampler to generate (the HTTPClient default or Java)

Yes

Redirect Automatically

Set Redirect Automatically in the generated samplers?

Yes

Follow Redirects

Set Follow Redirects in the generated samplers?

Note: see "Recording and redirects" section below for important information.

Yes

Use Keep-Alive

Set Use Keep-Alive in the generated samplers?

Yes

Retrieve all Embedded Resources

Set Retrieve all Embedded Resources in the generated samplers?

Yes

Content Type filter

Filter the requests based on the

content-type

- e.g. "

text/html [;charset=utf-8 ]

". The fields are regular expressions which are checked to see if they are contained in the

content-type

. [Does not have to match the entire field]. The include filter is checked first, then the exclude filter. Samples which are filtered out will not be stored.

Note: this filtering is applied to the content type of the response

No

Patterns to Include

Regular expressions that are matched against the full URL that is sampled. Allows filtering of requests that are recorded. All requests pass through, but only those that meet the requirements of the

Include

/

Exclude

fields are

recorded

. If both

Include

and

Exclude

are left empty, then everything is recorded (which can result in dozens of samples recorded for each page, as images, stylesheets, etc. are recorded).

If there is at least one entry in the

Include

field, then only requests that match one or more

Include

patterns are recorded

.

No

Patterns to Exclude

Regular expressions that are matched against the URL that is sampled.

Any requests that match one or more

Exclude

pattern are

not

recorded

.

No

Notify Child Listeners of filtered samplers

Notify Child Listeners of filtered samplers

Any response that match one or more

Exclude

pattern is

not

delivered to Child Listeners (View Results Tree)

.

No

Start Button

Start the proxy server. JMeter writes the following message to the console once the proxy server has started up and is ready to take requests: "

Proxy up and running!

".

N/A

Stop Button

Stop the proxy server.

N/A

Restart Button

Stops and restarts the proxy server. This is useful when you change/add/delete an include/exclude filter expression.

N/A

#### Recording and redirects

During recording, the browser will follow a redirect response and generate an additional request. The Proxy will record both the original request and the redirected request (subject to whatever exclusions are configured). The generated samples have "Follow Redirects" selected by default, because that is generally better. Redirects may depend on the original request, so repeating the originally recorded sample may not always work.

Now if JMeter is set to follow the redirect during replay, it will issue the original request, and then replay the redirect request that was recorded. To avoid this duplicate replay, JMeter tries to detect when a sample is the result of a previous redirect. If the current response is a redirect, JMeter will save the redirect URL. When the next request is received, it is compared with the saved redirect URL and if there is a match, JMeter will disable the generated sample. It also adds comments to the redirect chain. This assumes that all the requests in a redirect chain will follow each other without any intervening requests. To disable the redirect detection, set the property proxy.redirect.disabling=false

#### Includes and Excludes

The **include and exclude patterns** are treated as regular expressions (using Jakarta ORO). They will be matched against the host name, port (actual or implied), path and query (if any) of each browser request. If the URL you are browsing is "http://localhost/jmeter/index.html?username=xxxx", then the regular expression will be tested against the string: "localhost:80/jmeter/index.html?username=xxxx". Thus, if you want to include all .html files, your regular expression might look like: ".*\.html(\?.*)?" - or ".*\.html if you know that there is no query string or you only want html pages without query strings.

If there are any include patterns, then the URL **must match at least one** of the patterns , otherwise it will not be recorded. If there are any exclude patterns, then the URL **must not match any** of the patterns , otherwise it will not be recorded. Using a combination of includes and excludes, you should be able to record what you are interested in and skip what you are not.

N.B. the string that is matched by the regular expression must be the same as the

whole

host+path string.

Thus "

\.html

" will

not

match

localhost:80/index.html

#### Capturing binary POST data

JMeter is able to capture binary POST data. To configure which content-types are treated as binary, update the JMeter property proxy.binary.types. The default settings are as follows:

```
# These content-types will be handled by saving the request in a file:
proxy.binary.types=application/x-amf,application/x-java-serialized-object
# The files will be saved in this directory:
proxy.binary.directory=user.dir
# The files will be created with this file filesuffix:
proxy.binary.filesuffix=.binary
```

#### Adding timers

It is also possible to have the proxy add timers to the recorded script. To do this, create a timer directly within the HTTP(S) Test Script Recorder component. The proxy will place a copy of this timer into each sample it records, or into the first sample of each group if you're using grouping. This copy will then be scanned for occurrences of variable ${T} in its properties, and any such occurrences will be replaced by the time gap from the previous sampler recorded (in milliseconds).

When you are ready to begin, hit "start".

You will need to edit the proxy settings of your browser to point at the appropriate server and port, where the server is the machine JMeter is running on, and the port # is from the Proxy Control Panel shown above.

#### Where Do Samples Get Recorded?

JMeter places the recorded samples in the Target Controller you choose. If you choose the default option "Use Recording Controller", they will be stored in the first Recording Controller found in the test object tree (so be sure to add a Recording Controller before you start recording).

If the Proxy does not seem to record any samples, this could be because the browser is not actually using the proxy. To check if this is the case, try stopping the proxy. If the browser still downloads pages, then it was not sending requests via the proxy. Double-check the browser options. If you are trying to record from a server running on the same host, then check that the browser is not set to "Bypass proxy server for local addresses" (this example is from IE7, but there will be similar options for other browsers). If JMeter does not record browser URLs such as http://localhost/ or http://127.0.0.1/, try using the non-loopback hostname or IP address, e.g. http://myhost/ or http://192.168.0.2/.

#### Handling of HTTP Request Defaults

If the HTTP(S) Test Script Recorder finds enabled HTTP Request Defaults directly within the controller where samples are being stored, or directly within any of its parent controllers, the recorded samples will have empty fields for the default values you specified. You may further control this behaviour by placing an HTTP Request Defaults element directly within the HTTP(S) Test Script Recorder, whose non-blank values will override those in the other HTTP Request Defaults. See Best Practices with the HTTP(S) Test Script Recorder for more info.

#### User Defined Variable replacement

Similarly, if the HTTP(S) Test Script Recorder finds User Defined Variables (UDV) directly within the controller where samples are being stored, or directly within any of its parent controllers, the recorded samples will have any occurrences of the values of those variables replaced by the corresponding variable. Again, you can place User Defined Variables directly within the HTTP(S) Test Script Recorder to override the values to be replaced. See Best Practices with the Test Script Recorder for more info.

Please note that matching is case-sensitive.

Replacement by Variables: by default, the Proxy server looks for all occurrences of UDV values. If you define the variable WEB with the value www, for example, the string www will be replaced by ${WEB} wherever it is found. To avoid this happening everywhere, set the "Regex Matching" check-box. This tells the proxy server to treat values as Regexes (using the perl5 compatible regex matchers provided by ORO).

If "Regex Matching" is selected every variable will be compiled into a perl compatible regex enclosed in \b( and )\b. That way each match will start and end at a word boundary.

Note that the boundary characters are not part of the matching group, e.g.

n.*

to match

name

out of

You can call me 'name'

.

If you don't want your regex to be enclosed with those boundary matchers, you have to enclose your regex within parens, e.g ('.*?') to match 'name' out of You can call me 'name'.

The variables will be checked in random order. So ensure, that the potential matches don't overlap. Overlapping matchers would be

.*

(which matches anything) and

www

(which matches

www

only). Non-overlapping matchers would be

a+

(matches a sequence of

a

's) and

b+

(matches a sequence of

b

's).

If you want to match a whole string only, enclose it in (^ and $), e.g. (^thus$). The parens are necessary, since the normally added boundary characters will prevent ^ and $ to match.

If you want to match /images at the start of a string only, use the value (^/images). Jakarta ORO also supports zero-width look-ahead, so one can match /images/… but retain the trailing / in the output by using (^/images(?=/)).

Note that the current version of Jakarta ORO does not support look-behind - i.e.

(?<=…)

or

(?<!…)

.

Look out for overlapping matchers. For example the value .* as a regex in a variable named regex will partly match a previous replaced variable, which will result in something like ${{regex}, which is most probably not the desired result.

If there are any problems interpreting any variables as patterns, these are reported in jmeter.log, so be sure to check this if UDVs are not working as expected.

When you are done recording your test samples, stop the proxy server (hit the "stop" button). Remember to reset your browser's proxy settings. Now, you may want to sort and re-order the test script, add timers, listeners, a cookie manager, etc.

#### How can I record the server's responses too?

Just place a View Results Tree listener as a child of the HTTP(S) Test Script Recorder and the responses will be displayed. You can also add a Save Responses to a file Post-Processor which will save the responses to files.

#### Associating requests with responses

If you define the property proxy.number.requests=true JMeter will add a number to each sampler and each response. Note that there may be more responses than samplers if excludes or includes have been used. Responses that have been excluded will have labels enclosed in [ and ], for example [23 /favicon.ico]

#### Cookie Manager

If the server you are testing against uses cookies, remember to add an HTTP Cookie Manager to the test plan when you have finished recording it. During recording, the browser handles any cookies, but JMeter needs a Cookie Manager to do the cookie handling during a test run. The JMeter Proxy server passes on all cookies sent by the browser during recording, but does not save them to the test plan because they are likely to change between runs.

#### Authorization Manager

The HTTP(S) Test Script Recorder grabs "Authentication" header, tries to compute the Auth Policy. If Authorization Manager was added to target controller manually, HTTP(S) Test Script Recorder will find it and add authorization (matching ones will be removed). Otherwise Authorization Manager will be added to target controller with authorization object. You may have to fix automatically computed values after recording.

#### Uploading files

Some browsers (e.g. Firefox and Opera) don't include the full name of a file when uploading files. This can cause the JMeter proxy server to fail. One solution is to ensure that any files to be uploaded are in the JMeter working directory, either by copying the files there or by starting JMeter in the directory containing the files.

#### Recording HTTP Based Non Textual Protocols not natively available in JMeter

You may have to record an HTTP protocol that is not handled by default by JMeter (Custom Binary Protocol, Adobe Flex, Microsoft Silverlight, … ). Although JMeter does not provide a native proxy implementation to record these protocols, you have the ability to record these protocols by implementing a custom SamplerCreator. This Sampler Creator will translate the binary format into a HTTPSamplerBase subclass that can be added to the JMeter Test Case. For more details see "Extending JMeter".

^


## HTTP Mirror Server

The HTTP Mirror Server is a very simple HTTP server - it simply mirrors the data sent to it. This is useful for checking the content of HTTP requests.

It uses default port 8081.

### Parameters

Attribute

Description

Required

Port

Port on which Mirror server listens, defaults to

8081

.

Yes

Max Number of threads

If set to a value >

0

, number of threads serving requests will be limited to the configured number, if set to a value ≤

0

a new thread will be created to serve each incoming request. Defaults to

0

No

Max Queue size

Size of queue used for holding tasks before they are executed by Thread Pool, when Thread pool is exceeded, incoming requests will be held in this queue and discarded when this queue is full. This parameter is only used if Max Number of Threads is greater than

0

. Defaults to

25

No

Note that you can get more control over the responses by adding an HTTP Header Manager with the following name/value pairs:

### Parameters

Attribute

Description

Required

X-Sleep

Time to sleep in ms before sending response

No

X-SetCookie

Cookies to be set on response

No

X-ResponseStatus

Response status, see

HTTP Status responses

, example 200 OK, 500 Internal Server Error, ….

No

X-ResponseLength

Size of response, this trims the response to the requested size if that is less than the total size

No

X-SetHeaders

Pipe separated list of headers, example:

headerA: valueA|headerB: valueB

would set

headerA

to

valueA

and

headerB

to

valueB

.

No

You can also use the following query parameters:

### Parameters

Attribute

Description

Required

redirect

Generates a 302 (Temporary Redirect) with the provided location, e.g.

?redirect=/path

No

status

Overrides the default status return, e.g.

?status=404 Not Found

No

v

Verbose flag, writes some details to standard output, e.g. first line and redirect location if specified

No

^


## Property Display

The Property Display shows the values of System or JMeter properties. Values can be changed by entering new text in the Value column.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

^


## Debug Sampler

The Debug Sampler generates a sample containing the values of all JMeter variables and/or properties.

The values can be seen in the View Results Tree Listener Response Data pane.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

JMeter Properties

Include JMeter properties?

Yes

JMeter Variables

Include JMeter variables?

Yes

System Properties

Include System properties?

Yes

^


## Debug PostProcessor

The Debug PostProcessor creates a subSample with the details of the previous Sampler properties, JMeter variables, properties and/or System Properties.

The values can be seen in the View Results Tree Listener Response Data pane.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

JMeter Properties

Whether to show JMeter properties (default

false

).

Yes

JMeter Variables

Whether to show JMeter variables (default

false

).

Yes

Sampler Properties

Whether to show Sampler properties (default

true

).

Yes

System Properties

Whether to show System properties (default

false

).

Yes

^


## Test Fragment

The Test Fragment is used in conjunction with the Include Controller and Module Controller.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Yes

When using Test Fragment with

Module Controller

, ensure you disable the Test Fragment to avoid the execution of Test Fragment itself. This is done by default since JMeter 2.13.

^


## setUp Thread Group

A special type of ThreadGroup that can be utilized to perform Pre-Test Actions. The behavior of these threads is exactly like a normal Thread Group element. The difference is that these type of threads execute before the test proceeds to the executing of regular Thread Groups.

^


## tearDown Thread Group

A special type of ThreadGroup that can be utilized to perform Post-Test Actions. The behavior of these threads is exactly like a normal Thread Group element. The difference is that these type of threads execute after the test has finished executing its regular Thread Groups.

Note that by default it won't run if Test is gracefully shutdown, if you want to make it run in this case, ensure you check option "

Run tearDown Thread Groups after shutdown of main threads

" on Test Plan element. If Test Plan is stopped, tearDown will not run even if option is checked.

^

^

- < Prev
- Index
- Next >

Go to top
