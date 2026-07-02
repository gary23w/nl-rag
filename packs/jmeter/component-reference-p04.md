---
title: "Apache JMeter (part 4/8)"
source: https://jmeter.apache.org/usermanual/component_reference.html
domain: jmeter
license: CC-BY-SA-4.0
tags: jmeter apache, load testing, performance testing, test plan
fetched: 2026-07-02
part: 4/8
---

## View Results Tree

View Results Tree MUST NOT BE USED during load test as it consumes a lot of resources (memory and CPU). Use it only for either functional testing or during Test Plan debugging and Validation.

The View Results Tree shows a tree of all sample responses, allowing you to view the response for any sample. In addition to showing the response, you can see the time it took to get this response, and some response codes. Note that the Request panel only shows the headers added by JMeter. It does not show any headers (such as

Host

) that may be added by the HTTP protocol implementation.

There are several ways to view the response, selectable by a drop-down box at the bottom of the left hand panel.

| **Renderer** | **Description** |
|---|---|
| CSS/JQuery Tester | The *CSS/JQuery Tester* only works for text responses. It shows the plain text in the upper panel. The "Test" button allows the user to apply the CSS/JQuery to the upper panel and the results will be displayed in the lower panel. The CSS/JQuery expression engine can be JSoup or Jodd, syntax of these 2 implementation differs slightly. For example, the Selector a[class=sectionlink] with attribute href applied to the current JMeter functions page gives the following output: Match count: 74 Match[1]=#functions Match[2]=#what_can_do Match[3]=#where Match[4]=#how Match[5]=#function_helper Match[6]=#functions Match[7]=#__regexFunction Match[8]=#__regexFunction_parms Match[9]=#__counter … and so on … |
| Document | The *Document view* will show the extract text from various type of documents like Microsoft Office (Word, Excel, PowerPoint 97-2003, 2007-2010 (openxml), Apache OpenOffice (writer, calc, impress), HTML, gzip, jar/zip files (list of content), and some meta-data on "multimedia" files like mp3, mp4, flv, etc. The complete list of support format is available on Apache Tika format page. A requirement to the Document view is to download the Apache Tika binary package (tika-app-x.x.jar) and put this in JMETER_HOME/lib directory. If the document is larger than 10 MB, then it won't be displayed. To change this limit, set the JMeter property document.max_size (unit is byte) or set to 0 to remove the limit. |
| HTML | The *HTML view* attempts to render the response as HTML. The rendered HTML is likely to compare poorly to the view one would get in any web browser; however, it does provide a quick approximation that is helpful for initial result evaluation. Images, style-sheets, etc. aren't downloaded. |
| HTML (download resources) | If the *HTML (download resources) view* option is selected, the renderer may download images, style-sheets, etc. referenced by the HTML code. |
| HTML Source formatted | If the *HTML Source formatted view* option is selected, the renderer will display the HTML source code formatted and cleaned by Jsoup. |
| JSON | The *JSON view* will show the response in tree style (also handles JSON embedded in JavaScript). |
| JSON Path Tester | The *JSON Path Tester view* will let you test your JSON-PATH expressions and see the extracted data from a particular response. |
| JSON JMESPath Tester | The *JSON JMESPath Tester view* will let you test your JMESPath expressions and see the extracted data from a particular response. |
| Regexp Tester | The *Regexp Tester view* only works for text responses. It shows the plain text in the upper panel. The "Test" button allows the user to apply the Regular Expression to the upper panel and the results will be displayed in the lower panel. The regular expression engine is the same as that used in the Regular Expression Extractor. For example, the RE (JMeter\w*).* applied to the current JMeter home page gives the following output: Match count: 26 Match[1][0]=JMeter - Apache JMeter</title> Match[1][1]=JMeter Match[2][0]=JMeter" title="JMeter" border="0"/></a> Match[2][1]=JMeter Match[3][0]=JMeterCommitters">Contributors</a> Match[3][1]=JMeterCommitters … and so on … The first number in [] is the match number; the second number is the group. Group [0] is whatever matched the whole RE. Group [1] is whatever matched the 1st group, i.e. (JMeter\w*) in this case. See Figure 9b (below). |
| Text | The default *Text view* shows all of the text contained in the response. Note that this will only work if the response content-type is considered to be text. If the content-type begins with any of the following, it is considered as binary, otherwise it is considered to be text. image/ audio/ video/ |
| XML | The *XML view* will show response in tree style. Any DTD nodes or Prolog nodes will not show up in tree; however, response may contain those nodes. You can right-click on any node and expand or collapse all nodes below it. |
| XPath Tester | The *XPath Tester* only works for text responses. It shows the plain text in the upper panel. The "Test" button allows the user to apply the XPath query to the upper panel and the results will be displayed in the lower panel. |
| Boundary Extractor Tester | The *Boundary Extractor Tester* only works for text responses. It shows the plain text in the upper panel. The "Test" button allows the user to apply the Boundary Extractor query to the upper panel and the results will be displayed in the lower panel. |

Scroll automatically? option permit to have last node display in tree selection

Starting with version 3.2 the number of entries in the View is restricted to the value of the property

view.results.tree.max_results

which defaults to

500

entries. The old behaviour can be restored by setting the property to

0

. Beware, that this might consume a lot of memory.

With Search option, most of the views also allow the displayed data to be searched; the result of the search will be high-lighted in the display above. For example the Control panel screenshot below shows one result of searching for "Java". Note that the search operates on the visible text, so you may get different results when searching the Text and HTML views. Note: The regular expression uses the Java engine (not ORO engine like the Regular Expression Extractor or Regexp Tester view).

If there is no content-type provided, then the content will not be displayed in the any of the Response Data panels. You can use Save Responses to a file to save the data in this case. Note that the response data will still be available in the sample result, so can still be accessed using Post-Processors.

If the response data is larger than 200K, then it won't be displayed. To change this limit, set the JMeter property view.results.tree.max_size. You can also use save the entire response to a file using Save Responses to a file.

Additional renderers can be created. The class must implement the interface org.apache.jmeter.visualizers.ResultRenderer and/or extend the abstract class org.apache.jmeter.visualizers.SamplerResultTab, and the compiled code must be available to JMeter (e.g. by adding it to the lib/ext directory).

The Control Panel (above) shows an example of an HTML display. Figure 9 (below) shows an example of an XML display. Figure 9a (below) shows an example of a Regexp tester display. Figure 9b (below) shows an example of a Document display.

^


## Aggregate Report

The aggregate report creates a table row for each differently named request in your test. For each request, it totals the response information and provides request count, min, max, average, error rate, approximate throughput (request/second) and Kilobytes per second throughput. Once the test is done, the throughput is the actual through for the duration of the entire test.

The throughput is calculated from the point of view of the sampler target (e.g. the remote server in the case of HTTP samples). JMeter takes into account the total time over which the requests have been generated. If other samplers and timers are in the same thread, these will increase the total time, and therefore reduce the throughput value. So two identical samplers with different names will have half the throughput of two samplers with the same name. It is important to choose the sampler names correctly to get the best results from the Aggregate Report.

Calculation of the Median and 90 % Line (90th percentile) values requires additional memory. JMeter now combines samples with the same elapsed time, so far less memory is used. However, for samples that take more than a few seconds, the probability is that fewer samples will have identical times, in which case more memory will be needed. Note you can use this listener afterwards to reload a CSV or XML results file which is the recommended way to avoid performance impacts. See the Summary Report for a similar Listener that does not store individual samples and so needs constant memory.

Starting with JMeter 2.12, you can configure the 3 percentile values you want to compute, this can be done by setting properties:

- aggregate_rpt_pct1: defaults to 90th percentile
- aggregate_rpt_pct2: defaults to 95th percentile
- aggregate_rpt_pct3: defaults to 99th percentile

- Label - The label of the sample. If "Include group name in label?" is selected, then the name of the thread group is added as a prefix. This allows identical labels from different thread groups to be collated separately if required.
- # Samples - The number of samples with the same label
- Average - The average time of a set of results
- Median - The median is the time in the middle of a set of results. 50 % of the samples took no more than this time; the remainder took at least as long.
- 90% Line - 90 % of the samples took no more than this time. The remaining samples took at least as long as this. (90th percentile)
- 95% Line - 95 % of the samples took no more than this time. The remaining samples took at least as long as this. (95th percentile)
- 99% Line - 99 % of the samples took no more than this time. The remaining samples took at least as long as this. (99th percentile)
- Min - The shortest time for the samples with the same label
- Max - The longest time for the samples with the same label
- Error % - Percent of requests with errors
- Throughput - the Throughput is measured in requests per second/minute/hour. The time unit is chosen so that the displayed rate is at least 1.0. When the throughput is saved to a CSV file, it is expressed in requests/second, i.e. 30.0 requests/minute is saved as 0.5.
- Received KB/sec - The throughput measured in received Kilobytes per second
- Sent KB/sec - The throughput measured in sent Kilobytes per second

Times are in milliseconds.

The figure below shows an example of selecting the "Include group name" checkbox.

^


## View Results in Table

This visualizer creates a row for every sample result. Like the

View Results Tree

, this visualizer uses a lot of memory.

By default, it only displays the main (parent) samples; it does not display the sub-samples (child samples). JMeter has a "Child Samples?" check-box. If this is selected, then the sub-samples are displayed instead of the main samples.

^


## Simple Data Writer

This listener can record results to a file but not to the UI. It is meant to provide an efficient means of recording data by eliminating GUI overhead. When running in CLI mode, the

-l

flag can be used to create a data file. The fields to save are defined by JMeter properties. See the

jmeter.properties

file for details.

^


## Aggregate Graph

The aggregate graph is similar to the aggregate report. The primary difference is the aggregate graph provides an easy way to generate bar graphs and save the graph as a PNG file.

The figure below shows an example of settings to draw this graph.

Please note: All this parameters

aren't

saved in JMeter JMX script.

### Parameters

Attribute

Description

Required

Column settings

- Columns to display: Choose the column(s) to display in graph.
- Rectangles color: Click on right color rectangle open a popup dialog to choose a custom color for column.
- Foreground color Allow to change the value text color.
- Value font: Allow to define font settings for the text.
- Draw outlines bar? To draw or not the border line on bar chart
- Show number grouping? Show or not the number grouping in Y Axis labels.
- Value labels vertical? Change orientation for value label. (Default is horizontal)
- Column label selection: Filter by result label. A regular expression can be used, example: .*Transaction.* Before display the graph, click on Apply filter button to refresh internal data.

Yes

Title

Define the graph's title on the head of chart. Empty value is the default value: "

Aggregate Graph

". The button

Synchronize with name

define the title with the label of the listener. And define font settings for graph title

No

Graph size

Compute the graph size by the width and height depending of the current JMeter's window size. Use

Width

and

Height

fields to define a custom size. The unit is pixel.

No

X Axis settings

Define the max length of X Axis label (in pixel).

No

Y Axis settings

Define a custom maximum value for Y Axis.

No

Legend

Define the placement and font settings for chart legend

Yes

^


## Response Time Graph

The Response Time Graph draws a line chart showing the evolution of response time during the test, for each labelled request. If many samples exist for the same timestamp, the mean value is displayed.

The figure below shows an example of settings to draw this graph.

Please note: All this parameters are saved in JMeter

.jmx

file.

### Parameters

Attribute

Description

Required

Interval (ms)

The time in milliseconds for X axis interval. Samples are grouped according to this value. Before display the graph, click on

Apply interval

button to refresh internal data.

Yes

Sampler label selection

Filter by result label. A regular expression can be used, ex.

.*Transaction.*

. Before display the graph, click on

Apply filter

button to refresh internal data.

No

Title

Define the graph's title on the head of chart. Empty value is the default value: "

Response Time Graph

". The button

Synchronize with name

define the title with the label of the listener. And define font settings for graph title

No

Line settings

Define the width of the line. Define the type of each value point. Choose

none

to have a line without mark

Yes

Graph size

Compute the graph size by the width and height depending of the current JMeter's window size. Use

Width

and

Height

fields to define a custom size. The unit is pixel.

No

X Axis settings

Customize the date format of X axis label. The syntax is the Java

SimpleDateFormat API

.

No

Y Axis settings

Define a custom maximum value for Y Axis in milli-seconds. Define the increment for the scale (in ms) Show or not the number grouping in Y Axis labels.

No

Legend

Define the placement and font settings for chart legend

Yes

^


## Mailer Visualizer

The mailer visualizer can be set up to send email if a test run receives too many failed responses from the server.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

From

Email address to send messages from.

Yes

Addressee(s)

Email address to send messages to, comma-separated.

Yes

Success Subject

Email subject line for success messages.

No

Success Limit

Once this number of successful responses is exceeded

after previously reaching the failure limit

, a success email is sent. The mailer will thus only send out messages in a sequence of failed-succeeded-failed-succeeded, etc.

Yes

Failure Subject

Email subject line for fail messages.

No

Failure Limit

Once this number of failed responses is exceeded, a failure email is sent - i.e. set the count to

0

to send an e-mail on the first failure.

Yes

Host

IP address or host name of SMTP server (email redirector) server.

No

Port

Port of SMTP server (defaults to

25

).

No

Login

Login used to authenticate.

No

Password

Password used to authenticate.

No

Connection security

Type of encryption for SMTP authentication (SSL, TLS or none).

No

Test Mail

Press this button to send a test mail

No

Failures

A field that keeps a running total of number of failures so far received.

No

^


## BeanShell Listener

The BeanShell Listener allows the use of BeanShell for processing samples for saving etc.

**For full details on using BeanShell, please see the BeanShell website.** Migration to JSR223 Listener+Groovy is highly recommended for performance, support of new Java features and limited maintenance of the BeanShell library.

The test element supports the ThreadListener and TestListener methods. These should be defined in the initialisation file. See the file BeanShellListeners.bshrc for example definitions.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree. The name is stored in the script variable Label

Reset bsh.Interpreter before each call

If this option is selected, then the interpreter will be recreated for each sample. This may be necessary for some long running scripts. For further information, see

Best Practices - BeanShell scripting

.

Yes

Parameters

Parameters to pass to the BeanShell script. The parameters are stored in the following variables:

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

The BeanShell script to run. The return value is ignored.

Yes (unless script file is provided)

Before invoking the script, some variables are set up in the BeanShell interpreter:

- log - (Logger) - can be used to write to the log file
- ctx - (JMeterContext) - gives access to the context
- vars - (JMeterVariables) - gives read/write access to variables:
  ```
vars.get(key);
vars.put(key,val);
vars.putObject("OBJ1",new Object());
  ```
- props - (JMeterProperties - class java.util.Properties) - e.g. props.get("START.HMS"); props.put("PROP1","1234");
- sampleResult, prev - (SampleResult) - gives access to the previous SampleResult
- sampleEvent (SampleEvent) gives access to the current sample event

For details of all the methods available on each of the above variables, please check the Javadoc

If the property beanshell.listener.init is defined, this is used to load an initialisation file, which can be used to define methods etc. for use in the BeanShell script.

^


## Summary Report

The summary report creates a table row for each differently named request in your test. This is similar to the

Aggregate Report

, except that it uses less memory.

The throughput is calculated from the point of view of the sampler target (e.g. the remote server in the case of HTTP samples). JMeter takes into account the total time over which the requests have been generated. If other samplers and timers are in the same thread, these will increase the total time, and therefore reduce the throughput value. So two identical samplers with different names will have half the throughput of two samplers with the same name. It is important to choose the sampler labels correctly to get the best results from the Report.

- Label - The label of the sample. If "Include group name in label?" is selected, then the name of the thread group is added as a prefix. This allows identical labels from different thread groups to be collated separately if required.
- # Samples - The number of samples with the same label
- Average - The average elapsed time of a set of results
- Min - The lowest elapsed time for the samples with the same label
- Max - The longest elapsed time for the samples with the same label
- Std. Dev. - the Standard Deviation of the sample elapsed time
- Error % - Percent of requests with errors
- Throughput - the Throughput is measured in requests per second/minute/hour. The time unit is chosen so that the displayed rate is at least 1.0. When the throughput is saved to a CSV file, it is expressed in requests/second, i.e. 30.0 requests/minute is saved as 0.5.
- Received KB/sec - The throughput measured in Kilobytes per second
- Sent KB/sec - The throughput measured in Kilobytes per second
- Avg. Bytes - average size of the sample response in bytes.

Times are in milliseconds.

The figure below shows an example of selecting the "Include group name" checkbox.

^


## Save Responses to a file

This test element can be placed anywhere in the test plan. For each sample in its scope, it will create a file of the response Data. The primary use for this is in creating functional tests, but it can also be useful where the response is too large to be displayed in the View Results Tree Listener. The file name is created from the specified prefix, plus a number (unless this is disabled, see below). The file extension is created from the document type, if known. If not known, the file extension is set to 'unknown'. If numbering is disabled, and adding a suffix is disabled, then the file prefix is taken as the entire file name. This allows a fixed file name to be generated if required. The generated file name is stored in the sample response, and can be saved in the test log output file if required.

The current sample is saved first, followed by any sub-samples (child samples). If a variable name is provided, then the names of the files are saved in the order that the sub-samples appear. See below.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Filename Prefix (can include folders)

Prefix for the generated file names; this can include a directory name. Relative paths are resolved relative to the current working directory (which defaults to the

bin/

directory). JMeter also supports paths relative to the directory containing the current test plan (JMX file). If the path name begins with "

~/

" (or whatever is in the

jmeter.save.saveservice.base_prefix

JMeter property), then the path is assumed to be relative to the JMX file location.

If parent folders in prefix do not exists, JMeter will create them and stop test if it fails.

Please note that Filename Prefix must not contain Thread related data, so don't use any Variable (

${varName}

) or functions like

${__threadNum}

in this field

Yes

Variable Name containing saved file name

Name of a variable in which to save the generated file name (so it can be used later in the test plan). If there are sub-samples then a numeric suffix is added to the variable name. E.g. if the variable name is

FILENAME

, then the parent sample file name is saved in the variable

FILENAME

, and the filenames for the child samplers are saved in

FILENAME1

,

FILENAME2

etc.

No

Minimum Length of sequence number

If "

Don't add number to prefix

" is not checked, then numbers added to prefix will be padded by

0

so that prefix is has size of this value. Defaults to

0

.

No

Save Failed Responses only

If selected, then only failed responses are saved

Yes

Save Successful Responses only

If selected, then only successful responses are saved

Yes

Don't add number to prefix

If selected, then no number is added to the prefix. If you select this option, make sure that the prefix is unique or the file may be overwritten.

Yes

Don't add content type suffix

If selected, then no suffix is added. If you select this option, make sure that the prefix is unique or the file may be overwritten.

Yes

Add timestamp

If selected, then date will be included in file suffix following format

yyyyMMdd-HHmm_

Yes

Don't Save Transaction Controller SampleResult

If selected, then SamplerResult generated by Transaction Controller will be ignored

Yes

^


## JSR223 Listener

The JSR223 Listener allows JSR223 script code to be applied to sample results.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Language

The JSR223 language to be used

Yes

Parameters

Parameters to pass to the script. The parameters are stored in the following variables:

**Parameters**

string containing the parameters as a single variable

**args**

String array containing parameters, split on white-space

No

Script file

A file containing the script to run, if a relative file path is used, then it will be relative to directory referenced by "

user.dir

" System property

No

Script compilation caching

Unique String across Test Plan that JMeter will use to cache result of Script compilation if language used supports

Compilable

interface (Groovy is one of these, java, beanshell and javascript are not).

See note in JSR223 Sampler Java System property if you're using Groovy without checking this option

No

Script

The script to run.

Yes (unless script file is provided)

Before invoking the script, some variables are set up. Note that these are JSR223 variables - i.e. they can be used directly in the script.

**log**

(

Logger

) - can be used to write to the log file

**Label**

the String Label

**FileName**

the script file name (if any)

**Parameters**

the parameters (as a String)

**args**

the parameters as a String array (split on whitespace)

**ctx**

(

JMeterContext

) - gives access to the context

**vars**

(

JMeterVariables

) - gives read/write access to variables:

```
vars.get(key);
vars.put(key,val);
vars.putObject("OBJ1",new Object());
vars.getObject("OBJ2");
```

**props**

(JMeterProperties - class

java.util.Properties

) - e.g.

props.get("START.HMS");

props.put("PROP1","1234");

**sampleResult, prev**

(

SampleResult

) - gives access to the SampleResult

**sampleEvent**

(

SampleEvent

) - gives access to the SampleEvent

**sampler**

(

Sampler

)- gives access to the last sampler

**OUT**

System.out

- e.g.

OUT.println("message")

For details of all the methods available on each of the above variables, please check the Javadoc

^


## Generate Summary Results

This test element can be placed anywhere in the test plan. Generates a summary of the test run so far to the log file and/or standard output. Both running and differential totals are shown. Output is generated every

n

seconds (default 30 seconds) on the appropriate time boundary, so that multiple test runs on the same time will be synchronised.

Since a summary/differential line is written only if there are samples emitted, the interval for generation may not be respected if your test has no sample generated within the interval

See

jmeter.properties

file for the summariser configuration items:

```
# Define the following property to automatically start a summariser with that name
# (applies to CLI mode only)
#summariser.name=summary
#
# interval between summaries (in seconds) default 3 minutes
#summariser.interval=30
#
# Write messages to log file
#summariser.log=true
#
# Write messages to System.out
#summariser.out=true
```

This element is mainly intended for batch (CLI) runs. The output looks like the following:

```
label +     16 in 0:00:12 =    1.3/s Avg:  1608 Min:  1163 Max:  2009 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label +     82 in 0:00:30 =    2.7/s Avg:  1518 Min:  1003 Max:  2020 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label =     98 in 0:00:42 =    2.3/s Avg:  1533 Min:  1003 Max:  2020 Err:     0 (0.00%)
label +     85 in 0:00:30 =    2.8/s Avg:  1505 Min:  1008 Max:  2005 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label =    183 in 0:01:13 =    2.5/s Avg:  1520 Min:  1003 Max:  2020 Err:     0 (0.00%)
label +     79 in 0:00:30 =    2.7/s Avg:  1578 Min:  1089 Max:  2012 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label =    262 in 0:01:43 =    2.6/s Avg:  1538 Min:  1003 Max:  2020 Err:     0 (0.00%)
label +     80 in 0:00:30 =    2.7/s Avg:  1531 Min:  1013 Max:  2014 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label =    342 in 0:02:12 =    2.6/s Avg:  1536 Min:  1003 Max:  2020 Err:     0 (0.00%)
label +     83 in 0:00:31 =    2.7/s Avg:  1512 Min:  1003 Max:  1982 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label =    425 in 0:02:43 =    2.6/s Avg:  1531 Min:  1003 Max:  2020 Err:     0 (0.00%)
label +     83 in 0:00:29 =    2.8/s Avg:  1487 Min:  1023 Max:  2013 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label =    508 in 0:03:12 =    2.6/s Avg:  1524 Min:  1003 Max:  2020 Err:     0 (0.00%)
label +     78 in 0:00:30 =    2.6/s Avg:  1594 Min:  1013 Max:  2016 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label =    586 in 0:03:43 =    2.6/s Avg:  1533 Min:  1003 Max:  2020 Err:     0 (0.00%)
label +     80 in 0:00:30 =    2.7/s Avg:  1516 Min:  1013 Max:  2005 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label =    666 in 0:04:12 =    2.6/s Avg:  1531 Min:  1003 Max:  2020 Err:     0 (0.00%)
label +     86 in 0:00:30 =    2.9/s Avg:  1449 Min:  1004 Max:  2017 Err:     0 (0.00%) Active: 5 Started: 5 Finished: 0
label =    752 in 0:04:43 =    2.7/s Avg:  1522 Min:  1003 Max:  2020 Err:     0 (0.00%)
label +     65 in 0:00:24 =    2.7/s Avg:  1579 Min:  1007 Max:  2003 Err:     0 (0.00%) Active: 0 Started: 5 Finished: 5
label =    817 in 0:05:07 =    2.7/s Avg:  1526 Min:  1003 Max:  2020 Err:     0 (0.00%)
```

The "

label

" is the name of the element. The

"+"

means that the line is a delta line, i.e. shows the changes since the last output.

The

"="

means that the line is a total line, i.e. it shows the running total.

Entries in the JMeter log file also include time-stamps. The example "

817 in 0:05:07 = 2.7/s

" means that there were 817 samples recorded in 5 minutes and 7 seconds, and that works out at 2.7 samples per second.

The

Avg

(Average),

Min

(Minimum) and

Max

(Maximum) times are in milliseconds.

"

Err

" means number of errors (also shown as percentage).

The last two lines will appear at the end of a test. They will not be synchronised to the appropriate time boundary. Note that the initial and final deltas may be for less than the interval (in the example above this is 30 seconds). The first delta will generally be lower, as JMeter synchronizes to the interval boundary. The last delta will be lower, as the test will generally not finish on an exact interval boundary.

The label is used to group sample results together. So if you have multiple Thread Groups and want to summarize across them all, then use the same label - or add the summariser to the Test Plan (so all thread groups are in scope). Different summary groupings can be implemented by using suitable labels and adding the summarisers to appropriate parts of the test plan.

In CLI mode by default a Generate Summary Results listener named "

summariser

" is configured, if you have already added one to your Test Plan, ensure you name it differently otherwise results will be accumulated under this label (summary) leading to wrong results (sum of total samples + samples located under the Parent of Generate Summary Results listener).

This is not a bug but a design choice allowing to summarize across thread groups.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree. It appears as the "

label

" in the output. Details for all elements with the same label will be added together.

Yes

^


## Comparison Assertion Visualizer

The Comparison Assertion Visualizer shows the results of any

Compare Assertion

elements.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Yes

^


## Backend Listener

The backend listener is an Asynchronous listener that enables you to plug custom implementations of

BackendListenerClient

. By default, a Graphite implementation is provided.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Yes

Backend Listener implementation

Class of the

BackendListenerClient

implementation.

Yes

Async Queue size

Size of the queue that holds the SampleResults while they are processed asynchronously.

Yes

Parameters

Parameters of the

BackendListenerClient

implementation.

Yes

The following parameters apply to the GraphiteBackendListenerClient implementation:

### Parameters

Attribute

Description

Required

graphiteMetricsSender

org.apache.jmeter.visualizers.backend.graphite.TextGraphiteMetricsSender

or

org.apache.jmeter.visualizers.backend.graphite.PickleGraphiteMetricsSender

Yes

graphiteHost

Graphite or InfluxDB (with Graphite plugin enabled) server host

Yes

graphitePort

Graphite or InfluxDB (with Graphite plugin enabled) server port, defaults to

2003

. Note

PickleGraphiteMetricsSender

(port

2004

) can only talk to Graphite server.

Yes

rootMetricsPrefix

Prefix of metrics sent to backend. Defaults to "

jmeter

." Note that JMeter does not add a separator between the root prefix and the samplerName which is why the trailing dot is currently needed.

Yes

summaryOnly

Only send a summary with no detail. Defaults to

true

.

Yes

samplersList

Defines the names (labels) of sample results to be sent to the back end. If

useRegexpForSamplersList=false

this is a list of semi-colon separated names. If

useRegexpForSamplersList=true

this is a regular expression which will be matched against the names.

Yes

useRegexpForSamplersList

Consider samplersList as a regular expression to select the samplers for which you want to report metrics to backend. Defaults to

false

.

Yes

percentiles

The percentiles you want to send to the backend. A percentile may contain a fractional part, for example

12.5

. (The separator is always ".") List must be semicolon separated. Generally 3 or 4 values should be sufficient.

Yes

See also Real-time results for more details.

Since JMeter 3.2, an implementation that allows writing directly in InfluxDB with a custom schema. It is called InfluxdbBackendListenerClient. The following parameters apply to the InfluxdbBackendListenerClient implementation:

### Parameters

Attribute

Description

Required

influxdbMetricsSender

org.apache.jmeter.visualizers.backend.influxdb.HttpMetricsSender

Yes

influxdbUrl

Influx URL (example:

http://influxHost:8086/write?db=jmeter

)

Yes

influxdbToken

InfluxDB 2

authentication token

(example:

HE9yIdAPzWJDspH_tCc2UvdKZpX==

); since 5.2.

No

application

Name of tested application. This value is stored in the '

events

' measurement as a tag named '

application

'

Yes

measurement

Measurement as per

Influx Line Protocol Reference

. Defaults to "

jmeter

".

Yes

summaryOnly

Only send a summary with no detail. Defaults to

true

.

Yes

samplersRegex

Regular expression which will be matched against the names of samples and sent to the back end.

Yes

testTitle

Test name. Defaults to

Test name

. This value is stored in the '

events

' measurement as a field named '

text

'. JMeter generate automatically at the start and the end of the test an annotation with this value ending with ' started' and ' ended'

Yes

eventTags

Grafana allow to display tag for each annotation. You can fill them here. This value is stored in the '

events

' measurement as a tag named '

tags

'.

No

percentiles

The percentiles you want to send to the backend. A percentile may contain a fractional part, for example

12.5

(The separator is always "

.

"). List must be semicolon separated. Generally three or four values should be sufficient.

Yes

TAG_WhatEverYouWant

You can add as many custom tags as you want. For each of them, create a new line and prefix its name by "

TAG_

"

No

See also Real-time results and Influxdb annotations in Grafana for more details. There is also a subsection on configuring the listener for InfluxDB v2.

Since JMeter 5.4, an implementation that writes all sample results to InfluxDB. It is called InfluxDBRawBackendListenerClient. It is worth noting that this will use more resources than the InfluxdbBackendListenerClient, both by JMeter and InfluxDB due to the increase in data and individual writes. The following parameters apply to the InfluxDBRawBackendListenerClient implementation:

### Parameters

Attribute

Description

Required

influxdbMetricsSender

org.apache.jmeter.visualizers.backend.influxdb.HttpMetricsSender

Yes

influxdbUrl

Influx URL (e.g. http://influxHost:8086/write?db=jmeter or, for the cloud, https://eu-central-1-1.aws.cloud2.influxdata.com/api/v2/write?org=org-id&bucket=jmeter)

Yes

influxdbToken

InfluxDB 2

authentication token

(e.g. HE9yIdAPzWJDspH_tCc2UvdKZpX==)

No

measurement

Measurement as per

Influx Line Protocol Reference

. Defaults to "

jmeter

."

Yes

^

^

# 18.4 Configuration Elements

Configuration elements can be used to set up defaults and variables for later use by samplers. Note that these elements are processed at the start of the scope in which they are found, i.e. before any samplers in the same scope.


## CSV Data Set Config

CSV Data Set Config is used to read lines from a file, and split them into variables. It is easier to use than the __CSVRead() and __StringFromFile() functions. It is well suited to handling large numbers of variables, and is also useful for testing with "random" and unique values.

Generating unique random values at run-time is expensive in terms of CPU and memory, so just create the data in advance of the test. If necessary, the "random" data from the file can be used in conjunction with a run-time parameter to create different sets of values from each run - e.g. using concatenation - which is much cheaper than generating everything at run-time.

JMeter allows values to be quoted; this allows the value to contain a delimiter. If "allow quoted data" is enabled, a value may be enclosed in double-quotes. These are removed. To include double-quotes within a quoted field, use two double-quotes. For example:

```
1,"2,3","4""5" =>
1
2,3
4"5
```

JMeter supports CSV files which have a header line defining the column names. To enable this, leave the "Variable Names" field empty. The correct delimiter must be provided.

JMeter supports CSV files with quoted data that includes new-lines.

By default, the file is only opened once, and each thread will use a different line from the file. However the order in which lines are passed to threads depends on the order in which they execute, which may vary between iterations. Lines are read at the start of each test iteration. The file name and mode are resolved in the first iteration.

See the description of the Share mode below for additional options. If you want each thread to have its own set of values, then you will need to create a set of files, one for each thread. For example test1.csv, test2.csv, …, test*n*.csv. Use the filename test${__threadNum}.csv and set the "Sharing mode" to "Current thread".

CSV Dataset variables are defined at the start of each test iteration. As this is after configuration processing is completed, they cannot be used for some configuration items - such as JDBC Config - that process their contents at configuration time (see

Bug 40394

) However the variables do work in the HTTP Auth Manager, as the

username

etc. are processed at run-time.

As a special case, the string "\t" (without quotes) in the delimiter field is treated as a Tab.

When the end of file (EOF) is reached, and the recycle option is true, reading starts again with the first line of the file.

If the recycle option is false, and stopThread is false, then all the variables are set to <EOF> when the end of file is reached. This value can be changed by setting the JMeter property csvdataset.eofstring.

If the Recycle option is false, and Stop Thread is true, then reaching EOF will cause the thread to be stopped.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Filename

Name of the file to be read.

Relative file names are resolved with respect to the path of the active test plan.

For distributed testing, the CSV file must be stored on the server host system in the correct relative directory to where the JMeter server is started.

Absolute file names are also supported, but note that they are unlikely to work in remote mode, unless the remote server has the same directory structure. If the same physical file is referenced in two different ways - e.g.

csvdata.txt

and

./csvdata.txt

- then these are treated as different files. If the OS does not distinguish between upper and lower case,

csvData.TXT

would also be opened separately.

Yes

File Encoding

The encoding to be used to read the file, if not the platform default.

No

Variable Names

List of variable names. The names must be separated by the delimiter character. They can be quoted using double-quotes. JMeter supports CSV header lines: if the variable name field empty, then the first line of the file is read and interpreted as the list of column names.

No

Use first line as Variable Names

Ignore first line of CSV file, it will only be used if Variable Names is not empty, if Variable Names is empty the first line must contain the headers.

No

Delimiter

Delimiter to be used to split the records in the file. If there are fewer values on the line than there are variables the remaining variables are not updated - so they will retain their previous value (if any).

Yes

Allow quoted data?

Should the CSV file allow values to be quoted? If enabled, then values can be enclosed in

"

- double-quote - allowing values to contain a delimiter.

Yes

Recycle on EOF?

Should the file be re-read from the beginning on reaching

EOF

? (default is

true

)

Yes

Stop thread on EOF?

Should the thread be stopped on

EOF

, if Recycle is false? (default is

false

)

Yes

Sharing mode

- All threads - (the default) the file is shared between all the threads.
- Current thread group - each file is opened once for each thread group in which the element appears
- Current thread - each file is opened separately for each thread
- Identifier - all threads sharing the same identifier share the same file. So for example if you have 4 thread groups, you could use a common id for two or more of the groups to share the file between them. Or you could use the thread number to share the file between the same thread numbers in different thread groups.

Yes

^


## FTP Request Defaults

^


## DNS Cache Manager

The DNS Cache Manager element allows to test applications, which have several servers behind load balancers (CDN, etc.), when user receives content from different IP's. By default JMeter uses JVM DNS cache. That's why only one server from the cluster receives load. DNS Cache Manager resolves names for each thread separately each iteration and saves results of resolving to its internal DNS Cache, which is independent from both JVM and OS DNS caches.

A mapping for static hosts can be used to simulate something like /etc/hosts file. These entries will be preferred over the custom resolver. Use custom DNS resolver has to be enabled, if you want to use this mapping.

Usage of static host table

¶

Say, you have a test server, that you want to reach with a name, that is not (yet) set up in your DNS servers. For our example, this would be www.example.com for the server name, which you want to reach at the IP of the server a123.another.example.org.

You could change your workstation and add an entry to your /etc/hosts file - or the equivalent for your OS, or add an entry to the Static Host Table of the DNS Cache Manager.

You would type www.example.com into the first column (Host) and a123.another.example.org into the second column (Hostname or IP address). As the name of the second column implies, you could even use the IP address of your test server there.

The IP address for the test server will be looked up by using the custom DNS resolver. When none is given, the system DNS resolver will be used.

Now you can use www.example.com in your HTTPClient4 samplers and the requests will be made against a123.another.example.org with all headers set to www.example.com.

DNS Cache Manager is designed for using in the root of Thread Group or Test Plan. Do not place it as child element of particular HTTP Sampler

DNS Cache Manager works only with HTTP requests using HTTPClient4 implementation.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Clear cache each Iteration

If selected, DNS cache of every Thread is cleared each time new iteration is started.

No

Use system DNS resolver

System DNS resolver will be used. For correct work edit

$JAVA_HOME/jre/lib/security/java.security

and add

networkaddress.cache.ttl=0

N/A

Use custom DNS resolver

Custom DNS resolver (from dnsjava library) will be used.

N/A

Hostname or IP address

List of DNS servers to use. If empty, network configuration DNS will used.

No

Add Button

Add an entry to the DNS servers table.

N/A

Delete Button

Delete the currently selected table entry.

N/A

Host and Hostname or IP address

Mapping of hostnames to a static host entry which will be resolved using the custom DNS resolver.

No

Add static host Button

Add an entry to the static hosts table.

N/A

Delete static host Button

Delete the currently selected static host in the table.

N/A

^
