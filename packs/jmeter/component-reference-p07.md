---
title: "Apache JMeter (part 7/8)"
source: https://jmeter.apache.org/usermanual/component_reference.html
domain: jmeter
license: CC-BY-SA-4.0
tags: jmeter apache, load testing, performance testing, test plan
fetched: 2026-07-02
part: 7/8
---

## BeanShell PreProcessor

The BeanShell PreProcessor allows arbitrary code to be applied before taking a sample.

**For full details on using BeanShell, please see the BeanShell website.** Migration to JSR223 PreProcessor+Groovy is highly recommended for performance, support of new Java features and limited maintenance of the BeanShell library.

The test element supports the ThreadListener and TestListener methods. These should be defined in the initialisation file. See the file BeanShellListeners.bshrc for example definitions.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree. The name is stored in the script variable

Label

No

Reset bsh.Interpreter before each call

If this option is selected, then the interpreter will be recreated for each sample. This may be necessary for some long running scripts. For further information, see

Best Practices - BeanShell scripting

.

Yes

Parameters

Parameters to pass to the BeanShell script. The parameters are stored in the following variables:

- Parameters - string containing the parameters as a single variable
- bsh.args - String array containing parameters, split on white-space

No

Script file

A file containing the BeanShell script to run. The file name is stored in the script variable

FileName

No

Script

The BeanShell script. The return value is ignored.

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
- prev - (SampleResult) - gives access to the previous SampleResult (if any)
- sampler - (Sampler)- gives access to the current sampler

For details of all the methods available on each of the above variables, please check the Javadoc

If the property beanshell.preprocessor.init is defined, this is used to load an initialisation file, which can be used to define methods etc. for use in the BeanShell script.

^


## JSR223 PreProcessor

The JSR223 PreProcessor allows JSR223 script code to be applied before taking a sample.

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

- Parameters - string containing the parameters as a single variable
- args - String array containing parameters, split on white-space

No

Script file

A file containing the script to run, if a relative file path is used, then it will be relative to directory referenced by "

user.dir

" System property

No

Script compilation caching

Unique String across Test Plan that JMeter will use to cache result of Script compilation if language used supports

Compilable

interface (Groovy is one of these, java, beanshell and javascript are not)

See note in JSR223 Sampler Java System property if you're using Groovy without checking this option

No

Script

The script to run.

Yes (unless script file is provided)

The following JSR223 variables are set up for use by the script:

- log - (Logger) - can be used to write to the log file
- Label - the String Label
- FileName - the script file name (if any)
- Parameters - the parameters (as a String)
- args - the parameters as a String array (split on whitespace)
- ctx - (JMeterContext) - gives access to the context
- vars - (JMeterVariables) - gives read/write access to variables:
  ```
vars.get(key);
vars.put(key,val);
vars.putObject("OBJ1",new Object());
vars.getObject("OBJ2");
  ```
- props - (JMeterProperties - class java.util.Properties) - e.g. props.get("START.HMS"); props.put("PROP1","1234");
- sampler - (Sampler)- gives access to the current sampler
- OUT - System.out - e.g. OUT.println("message")

For details of all the methods available on each of the above variables, please check the Javadoc

^


## JDBC PreProcessor

The JDBC PreProcessor enables you to run some SQL statement just before a sample runs. This can be useful if your JDBC Sample requires some data to be in DataBase and you cannot compute this in a setup Thread group. For details, see JDBC Request.

See the following Test plan:

See also:

- Test Plan using JDBC Pre/Post Processor

In the linked test plan, "Create Price Cut-Off" JDBC PreProcessor calls a stored procedure to create a Price Cut-Off in Database, this one will be used by "Calculate Price cut off".

^


## RegEx User Parameters

Allows to specify dynamic values for HTTP parameters extracted from another HTTP Request using regular expressions. RegEx User Parameters are specific to individual threads.

This component allows you to specify reference name of a regular expression that extracts names and values of HTTP request parameters. Regular expression group numbers must be specified for parameter's name and also for parameter's value. Replacement will only occur for parameters in the Sampler that uses this RegEx User Parameters which name matches

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Regular Expression Reference Name

Name of a reference to a regular expression

Yes

Parameter names regexp group number

Group number of regular expression used to extract parameter names

Yes

Parameter values regex group number

Group number of regular expression used to extract parameter values

Yes

Regexp Example

¶

Suppose we have a request which returns a form with 3 input parameters and we want to extract the value of 2 of them to inject them in next request

1. Create Post Processor Regular Expression for first HTTP Request
  - refName - set name of a regular expression Expression (listParams)
  - regular expression - expression that will extract input names and input values attributes Ex: input name="([^"]+?)" value="([^"]+?)"
  - template - would be empty
  - match nr - -1 (in order to iterate through all the possible matches)
2. Create Pre Processor RegEx User Parameters for second HTTP Request
  - refName - set the same reference name of a regular expression, would be listParams in our example
  - parameter names group number - group number of regular expression for parameter names, would be 1 in our example
  - parameter values group number - group number of regular expression for parameter values, would be 2 in our example

See also the Regular Expression Extractor element, which is used to extract parameters names and values

^

See also:

- Test Plan showing how to use RegEx User Parameters


## Sample Timeout

This Pre-Processor schedules a timer task to interrupt a sample if it takes too long to complete. The timeout is ignored if it is zero or negative. For this to work, the sampler must implement Interruptible. The following samplers are known to do so: AJP, BeanShell, FTP, HTTP, Soap, AccessLog, MailReader, JMS Subscriber, TCPSampler, TestAction, JavaSampler

The test element is intended for use where individual timeouts such as Connection Timeout or Response Timeout are insufficient, or where the Sampler does not support timeouts. The timeout should be set sufficiently long so that it is not triggered in normal tests, but short enough that it interrupts samples that are stuck.

[By default, JMeter uses a Callable to interrupt the sampler. This executes in the same thread as the timer, so if the interrupt takes a long while, it may delay the processing of subsequent timeouts. This is not expected to be a problem, but if necessary the property InterruptTimer.useRunnable can be set to true to use a separate Runnable thread instead of the Callable.]

### Parameters

Attribute

Description

Required

Name

Descriptive name for this timer that is shown in the tree.

No

Sample Timeout

If the sample takes longer to complete, it will be interrupted.

Yes

^

^

# 18.8 Post-Processors

As the name suggests, Post-Processors are applied after samplers. Note that they are applied to **all** the samplers in the same scope, so to ensure that a post-processor is applied only to a particular sampler, add it as a child of the sampler.

Note: Unless documented otherwise, Post-Processors are not applied to sub-samples (child samples) - only to the parent sample. In the case of JSR223 and BeanShell post-processors, the script can retrieve sub-samples using the method

prev.getSubResults()

which returns an array of SampleResults. The array will be empty if there are none.

Post-Processors are run before Assertions, so they do not have access to any Assertion Results, nor will the sample status reflect the results of any Assertions. If you require access to Assertion Results, try using a Listener instead. Also note that the variable JMeterThread.last_sample_ok is set to "true" or "false" after all Assertions have been run.


## Regular Expression Extractor

Allows the user to extract values from a server response using a Perl-type regular expression. As a post-processor, this element will execute after each Sample request in its scope, applying the regular expression, extracting the requested values, generate the template string, and store the result into the given variable name.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Apply to:

This is for use with samplers that can generate sub-samples, e.g. HTTP Sampler with embedded resources, Mail Reader or samples generated by the Transaction Controller.

- Main sample only - only applies to the main sample
- Sub-samples only - only applies to the sub-samples
- Main sample and sub-samples - applies to both.
- JMeter Variable Name to use - extraction is to be applied to the contents of the named variable

Matching is applied to all qualifying samples in turn. For example if there is a main sample and 3 sub-samples, each of which contains a single match for the regex, (i.e. 4 matches in total). For match number =

3

, Sub-samples only, the extractor will match the 3

rd

sub-sample. For match number =

3

, Main sample and sub-samples, the extractor will match the 2

nd

sub-sample (1

st

match is main sample). For match number =

0

or negative, all qualifying samples will be processed. For match number >

0

, matching will stop as soon as enough matches have been found.

Yes

Field to check

The following fields can be checked:

- Body - the body of the response, e.g. the content of a web-page (excluding headers)
- Body (unescaped) - the body of the response, with all Html escape codes replaced. Note that Html escapes are processed without regard to context, so some incorrect substitutions may be made. Note that this option highly impacts performances, so use it only when absolutely necessary and be aware of its impacts
- Body as a Document - the extract text from various type of documents via Apache Tika (see View Results Tree Document view section). Note that the Body as a Document option can impact performances, so ensure it is OK for your test
- Request Headers - may not be present for non-HTTP samples
- Response Headers - may not be present for non-HTTP samples
- URL
- Response Code - e.g. 200
- Response Message - e.g. OK

Headers can be useful for HTTP samples; it may not be present for other sample types.

Yes

Name of created variable

The name of the JMeter variable in which to store the result. Also note that each group is stored as

[refname]_g#

, where

[refname]

is the string you entered as the reference name, and

#

is the group number, where group

0

is the entire match, group

1

is the match from the first set of parentheses, etc.

Yes

Regular Expression

The regular expression used to parse the response data. This must contain at least one set of parentheses "

()

" to capture a portion of the string, unless using the group

$0$

. Do not enclose the expression in

/ /

- unless of course you want to match these characters as well.

Yes

Template

The template used to create a string from the matches found. This is an arbitrary string with special elements to refer to groups within the regular expression. The syntax to refer to a group is: '

$1$

' to refer to group

1

, '

$2$

' to refer to group

2

, etc.

$0$

refers to whatever the entire expression matches.

Yes

Match No. (0 for Random)

Indicates which match to use. The regular expression may match multiple times.

- Use a value of zero to indicate JMeter should choose a match at random.
- A positive number N means to select the nth match.
- Negative numbers are used in conjunction with the ForEach Controller - see below.

Yes

Default Value

If the regular expression does not match, then the reference variable will be set to the default value. This is particularly useful for debugging tests. If no default is provided, then it is difficult to tell whether the regular expression did not match, or the RE element was not processed or maybe the wrong variable is being used.

However, if you have several test elements that set the same variable, you may wish to leave the variable unchanged if the expression does not match. In this case, remove the default value once debugging is complete.

No, but recommended

Use empty default value

If the checkbox is checked and

Default Value

is empty, then JMeter will set the variable to empty string instead of not setting it. Thus when you will for example use

${var}

(if

Reference Name

is var) in your Test Plan, if the extracted value is not found then

${var}

will be equal to empty string instead of containing

${var}

which may be useful if extracted value is optional.

No

If the match number is set to a non-negative number, and a match occurs, the variables are set as follows:

- refName - the value of the template
- refName_g*n*, where n=0,1,2 - the groups for the match
- refName_g - the number of groups in the Regex (excluding 0)

If no match occurs, then the refName variable is set to the default (unless this is absent). Also, the following variables are removed:

- refName_g0
- refName_g1
- refName_g

If the match number is set to a negative number, then all the possible matches in the sampler data are processed. The variables are set as follows:

- refName_matchNr - the number of matches found; could be 0
- refName_*n*, where n = 1, 2, 3 etc. - the strings as generated by the template
- refName_*n*_g*m*, where m=0, 1, 2 - the groups for match n
- refName - always set to the default value
- refName_g*n* - not set

Note that the refName variable is always set to the default value in this case, and the associated group variables are not set.

See also Response Assertion for some examples of how to specify modifiers, and for further information on JMeter regular expressions.

^


## CSS Selector Extractor (was: CSS/JQuery Extractor )

Allows the user to extract values from a server HTML response using a CSS Selector syntax. As a post-processor, this element will execute after each Sample request in its scope, applying the CSS/JQuery expression, extracting the requested nodes, extracting the node as text or attribute value and store the result into the given variable name.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Apply to:

This is for use with samplers that can generate sub-samples, e.g. HTTP Sampler with embedded resources, Mail Reader or samples generated by the Transaction Controller.

- Main sample only - only applies to the main sample
- Sub-samples only - only applies to the sub-samples
- Main sample and sub-samples - applies to both.
- JMeter Variable Name to use - extraction is to be applied to the contents of the named variable

Matching is applied to all qualifying samples in turn. For example if there is a main sample and 3 sub-samples, each of which contains a single match for the regex, (i.e. 4 matches in total). For match number =

3

, Sub-samples only, the extractor will match the 3

rd

sub-sample. For match number =

3

, Main sample and sub-samples, the extractor will match the 2

nd

sub-sample (1

st

match is main sample). For match number =

0

or negative, all qualifying samples will be processed. For match number >

0

, matching will stop as soon as enough matches have been found.

Yes

CSS Selector Implementation

2 Implementations for CSS/JQuery based syntax are supported:

- JSoup
- Jodd-Lagarto (CSSelly)

If selector is set to empty, default implementation(JSoup) will be used.

False

Name of created variable

The name of the JMeter variable in which to store the result.

Yes

CSS/JQuery expression

The CSS/JQuery selector used to select nodes from the response data. Selector, selectors combination and pseudo-selectors are supported, examples:

- E[foo] - an E element with a "foo" attribute
- ancestor child - child elements that descend from ancestor, e.g. .body p finds p elements anywhere under a block with class "body"
- :lt(n) - find elements whose sibling index (i.e. its position in the DOM tree relative to its parent) is less than n; e.g. td:lt(3)
- :contains(text) - find elements that contain the given text. The search is case-insensitive; e.g. p:contains(jsoup)
- …

For more details on syntax, see:

- JSoup
- Jodd-Lagarto (CSSelly)

Yes

Attribute

Name of attribute (as per HTML syntax) to extract from nodes that matched the selector. If empty, then the combined text of this element and all its children will be returned.

This is the equivalent

Element#attr(name)

function for JSoup if an attribute is set.

If empty this is the equivalent of

Element#text()

function for JSoup if not value is set for attribute.

false

Match No. (0 for Random)

Indicates which match to use. The CSS/JQuery selector may match multiple times.

- Use a value of zero to indicate JMeter should choose a match at random.
- A positive number N means to select the nth match.
- Negative numbers are used in conjunction with the ForEach Controller - see below.

Yes

Default Value

If the expression does not match, then the reference variable will be set to the default value. This is particularly useful for debugging tests. If no default is provided, then it is difficult to tell whether the expression did not match, or the CSS/JQuery element was not processed or maybe the wrong variable is being used.

However, if you have several test elements that set the same variable, you may wish to leave the variable unchanged if the expression does not match. In this case, remove the default value once debugging is complete.

No, but recommended

Use empty default value

If the checkbox is checked and

Default Value

is empty, then JMeter will set the variable to empty string instead of not setting it. Thus when you will for example use

${var}

(if

Reference Name

is var) in your Test Plan, if the extracted value is not found then

${var}

will be equal to empty string instead of containing

${var}

which may be useful if extracted value is optional.

No

If the match number is set to a non-negative number, and a match occurs, the variables are set as follows:

- refName - the value of the template

If no match occurs, then the refName variable is set to the default (unless this is absent).

If the match number is set to a negative number, then all the possible matches in the sampler data are processed. The variables are set as follows:

- refName_matchNr - the number of matches found; could be 0
- refName_n, where n = 1, 2, 3, etc. - the strings as generated by the template
- refName - always set to the default value

Note that the refName variable is always set to the default value in this case.

^


## XPath2 Extractor

This test element allows the user to extract value(s) from structured response - XML or (X)HTML - using XPath2 query language.

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
- JMeter Variable Name to use - extraction is to be applied to the contents of the named variable

XPath matching is applied to all qualifying samples in turn, and all the matching results will be returned.

Yes

Return entire XPath fragment instead of text content?

If selected, the fragment will be returned rather than the text content.

For example

//title

would return "

<title>Apache JMeter</title>

" rather than "

Apache JMeter

".

In this case,

//title/text()

would return "

Apache JMeter

".

Yes

Name of created variable

The name of the JMeter variable in which to store the result.

Yes

XPath Query

Element query in XPath 2.0 language. Can return more than one match.

Yes

Match No. (0 for Random)

If the XPath Path query leads to many results, you can choose which one(s) to extract as Variables:

- 0: means random (default value)
- -1 means extract all results, they will be named as *<variable name>*_N (where N goes from 1 to Number of results)
- X: means extract the Xth result. If this Xth is greater than number of matches, then nothing is returned. Default value will be used

No

Default Value

Default value returned when no match found. It is also returned if the node has no value and the fragment option is not selected.

yes

Namespaces aliases list

List of namespaces aliases you want to use to parse the document, one line per declaration. You must specify them as follow:

prefix=namespace

. This implementation makes it easier to use namespaces than with the old XPathExtractor version.

No

To allow for use in a ForEach Controller, it works exactly the same as the above XPath Extractor

XPath2 Extractor provides some interestings tools such as an improved syntax and much more functions than in its first version.

Here are some exemples:

**abs(/book/page[2])**

extracts 2

nd

absolute value of the page from a book

**avg(/librarie/book/page)**

extracts the average number of page from all the books in the libraries

**compare(/book[1]/page[2],/book[2]/page[2])**

return Integer value equal 0 to if the 2

nd

page of the first book is equal to the 2

nd

page of the 2

nd

book, else return -1.

To see more information about these functions, please check xPath2 functions

^


## XPath Extractor

This test element allows the user to extract value(s) from structured response - XML or (X)HTML - using XPath query language.

Since JMeter 5.0, you should use

XPath2 Extractor

as it provides better and easier namespace management, better performances and support for XPath 2.0

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
- JMeter Variable Name to use - extraction is to be applied to the contents of the named variable

XPath matching is applied to all qualifying samples in turn, and all the matching results will be returned.

Yes

Use Tidy (tolerant parser)

If checked use Tidy to parse HTML response into XHTML.

- "Use Tidy" should be checked on for HTML response. Such response is converted to valid XHTML (XML compatible HTML) using Tidy
- "Use Tidy" should be unchecked for both XHTML or XML response (for example RSS)

For HTML, CSS Selector Extractor is the correct and performing solution. Don't use XPath for HTML extractions.

Yes

Quiet

Sets the Tidy Quiet flag

If Tidy is selected

Report Errors

If a Tidy error occurs, then set the Assertion accordingly

If Tidy is selected

Show warnings

Sets the Tidy showWarnings option

If Tidy is selected

Use Namespaces

If checked, then the XML parser will use namespace resolution.(see note below on NAMESPACES) Note that currently only namespaces declared on the root element will be recognised. See below for user-definition of additional workspace names.

If Tidy is not selected

Validate XML

Check the document against its schema.

If Tidy is not selected

Ignore Whitespace

Ignore Element Whitespace.

If Tidy is not selected

Fetch External DTDs

If selected, external DTDs are fetched.

If Tidy is not selected

Return entire XPath fragment instead of text content?

If selected, the fragment will be returned rather than the text content.

For example

//title

would return "

<title>Apache JMeter</title>

" rather than "

Apache JMeter

".

In this case,

//title/text()

would return "

Apache JMeter

".

Yes

Name of created variable

The name of the JMeter variable in which to store the result.

Yes

XPath Query

Element query in XPath language. Can return more than one match.

Yes

Match No. (0 for Random)

If the XPath Path query leads to many results, you can choose which one(s) to extract as Variables:

- 0: means random
- -1 means extract all results (default value), they will be named as *<variable name>*_N (where N goes from 1 to Number of results)
- X: means extract the Xth result. If this Xth is greater than number of matches, then nothing is returned. Default value will be used

No

Default Value

Default value returned when no match found. It is also returned if the node has no value and the fragment option is not selected.

To allow for use in a ForEach Controller, the following variables are set on return:

- refName - set to first (or only) match; if no match, then set to default
- refName_matchNr - set to number of matches (may be 0)
- refName_n - n=1, 2, 3, etc. Set to the 1st, 2nd 3rd match etc.

Note: The next

refName_n

variable is set to

null

- e.g. if there are 2 matches, then

refName_3

is set to

null

, and if there are no matches, then

refName_1

is set to

null

.

XPath is query language targeted primarily for XSLT transformations. However it is useful as generic query language for structured data too. See XPath Reference or XPath specification for more information. Here are few examples:

**/html/head/title**

extracts title element from HTML response

**/book/page[2]**

extracts 2

nd

page from a book

**/book/page**

extracts all pages from a book

**//form[@name='countryForm']//select[@name='country']/option[text()='Czech Republic'])/@value**

extracts value attribute of option element that match text '

Czech Republic

' inside of select element with name attribute '

country

' inside of form with name attribute '

countryForm

'

When "

Use Tidy

" is checked on - resulting XML document may slightly differ from original HTML response:

- All elements and attribute names are converted to lowercase
- Tidy attempts to correct improperly nested elements. For example - original (incorrect) ul/font/li becomes correct ul/li/font

See

Tidy homepage

for more information.

NAMESPACES

As a work-round for namespace limitations of the Xalan XPath parser (implementation on which JMeter is based) you need to:

- provide a Properties file (if for example your file is named namespaces.properties) which contains mappings for the namespace prefixes:
  ```
prefix1=http\://foo.apache.org
prefix2=http\://toto.apache.org
…
  ```
- reference this file in user.properties file using the property:
  ```
xpath.namespace.config=namespaces.properties
  ```

```
//mynamespace:tagname
```

```
//*[local-name()='tagname' and namespace-uri()='uri-for-namespace']
```

uri-for-namespace

mynamespace

^


## JSON JMESPath Extractor

This test element allows the user to extract value(s) from JSON response using JMESPath query language.

In the XPATH Extractor we support to extract multiple xpaths at the same time, but in JMES Extractor only one JMES Expression can be entered at a time.

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
- JMeter Variable Name to use - extraction is to be applied to the contents of the named variable

Yes

Name of created variable

The name of the JMeter variable in which to store the result.

Yes

JMESPath expressions

Element query in JMESPath query language. Can return the matched result.

Yes

Match No. (0 for Random)

If the JMESPath query leads to many results, you can choose which one(s) to extract as Variables:

- 0: means random
- -1 means extract all results (default value), they will be named as *<variable name>*_N (where N goes from 1 to Number of results)
- X: means extract the Xth result. If this Xth is greater than number of matches, then nothing is returned. Default value will be used

No

Default Value

Default value returned when no match found. It is also returned if the node has no value and the fragment option is not selected.

JMESPath is a query language for JSON. It is described in an ABNF grammar with a complete specification. This ensures that the language syntax is precisely defined. See JMESPath Reference for more information. Here are also some examples JMESPath Example.

^


## Result Status Action Handler

This test element allows the user to stop the thread or the whole test if the relevant sampler failed.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Action to be taken after a Sampler error

Determines what happens if a sampler error occurs, either because the sample itself failed or an assertion failed. The possible choices are:

- Continue - ignore the error and continue with the test
- Start next thread loop - does not execute samplers following the sampler in error for the current iteration and restarts the loop on next iteration
- Stop Thread - current thread exits
- Stop Test - the entire test is stopped at the end of any current samples.
- Stop Test Now - the entire test is stopped abruptly. Any current samplers are interrupted if possible.

No

^


## BeanShell PostProcessor

The BeanShell PreProcessor allows arbitrary code to be applied after taking a sample.

BeanShell Post-Processor no longer ignores samples with zero-length result data

**For full details on using BeanShell, please see the BeanShell website.** Migration to JSR223 PostProcessor+Groovy is highly recommended for performance, support of new Java features and limited maintenance of the BeanShell library.

The test element supports the ThreadListener and TestListener methods. These should be defined in the initialisation file. See the file BeanShellListeners.bshrc for example definitions.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree. The name is stored in the script variable

Label

No

Reset bsh.Interpreter before each call

If this option is selected, then the interpreter will be recreated for each sample. This may be necessary for some long running scripts. For further information, see

Best Practices - BeanShell scripting

.

Yes

Parameters

Parameters to pass to the BeanShell script. The parameters are stored in the following variables:

- Parameters - string containing the parameters as a single variable
- bsh.args - String array containing parameters, split on white-space

No

Script file

A file containing the BeanShell script to run. The file name is stored in the script variable

FileName

No

Script

The BeanShell script. The return value is ignored.

Yes (unless script file is provided)

The following BeanShell variables are set up for use by the script:

- log - (Logger) - can be used to write to the log file
- ctx - (JMeterContext) - gives access to the context
- vars - (JMeterVariables) - gives read/write access to variables:
  ```
vars.get(key);
vars.put(key,val);
vars.putObject("OBJ1",new Object());
  ```
- props - (JMeterProperties - class java.util.Properties) - e.g. props.get("START.HMS"); props.put("PROP1","1234");
- prev - (SampleResult) - gives access to the previous SampleResult
- data - (byte [])- gives access to the current sample data

For details of all the methods available on each of the above variables, please check the Javadoc

If the property beanshell.postprocessor.init is defined, this is used to load an initialisation file, which can be used to define methods etc. for use in the BeanShell script.

^


## JSR223 PostProcessor

The JSR223 PostProcessor allows JSR223 script code to be applied after taking a sample.

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

- Parameters - string containing the parameters as a single variable
- args - String array containing parameters, split on white-space

No

Script file

A file containing the script to run, if a relative file path is used, then it will be relative to directory referenced by "

user.dir

" System property

No

Script compilation caching

Unique String across Test Plan that JMeter will use to cache result of Script compilation if language used supports

Compilable

interface (Groovy is one of these, java, beanshell and javascript are not)

See note in JSR223 Sampler Java System property if you're using Groovy without checking this option

No

Script

The script to run.

Yes (unless script file is provided)

Before invoking the script, some variables are set up. Note that these are JSR223 variables - i.e. they can be used directly in the script.

- log - (Logger) - can be used to write to the log file
- Label - the String Label
- FileName - the script file name (if any)
- Parameters - the parameters (as a String)
- args - the parameters as a String array (split on whitespace)
- ctx - (JMeterContext) - gives access to the context
- vars - (JMeterVariables) - gives read/write access to variables:
  ```
vars.get(key);
vars.put(key,val);
vars.putObject("OBJ1",new Object());
vars.getObject("OBJ2");
  ```
- props - (JMeterProperties - class java.util.Properties) - e.g. props.get("START.HMS"); props.put("PROP1","1234");
- prev - (SampleResult) - gives access to the previous SampleResult (if any)
- sampler - (Sampler)- gives access to the current sampler
- OUT - System.out - e.g. OUT.println("message")

For details of all the methods available on each of the above variables, please check the Javadoc

^


## JDBC PostProcessor

The JDBC PostProcessor enables you to run some SQL statement just after a sample has run. This can be useful if your JDBC Sample changes some data and you want to reset state to what it was before the JDBC sample run.

See also:

- Test Plan using JDBC Pre/Post Processor

In the linked test plan, "JDBC PostProcessor" JDBC PostProcessor calls a stored procedure to delete from Database the Price Cut-Off that was created by PreProcessor.

^


## JSON Extractor

The JSON PostProcessor enables you extract data from JSON responses using JSON-PATH syntax. This post processor is very similar to Regular expression extractor. It must be placed as a child of HTTP Sampler or any other sampler that has responses. It will allow you to extract in a very easy way text content, see JSON Path syntax.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

No

Apply to:

This is for use with samplers that can generate sub-samples, e.g. HTTP Sampler with embedded resources, Mail Reader or samples generated by the Transaction Controller.

**Main sample only**

only applies to the main sample

**Sub-samples only**

only applies to the sub-samples

**Main sample and sub-samples**

applies to both.

**JMeter Variable Name to use**

extraction is to be applied to the contents of the named variable

Yes

Names of created variables

Semicolon separated names of variables that will contain the results of JSON-PATH expressions (must match number of JSON-PATH expressions)

Yes

JSON Path Expressions

Semicolon separated JSON-PATH expressions (must match number of variables)

Yes

Default Values

Semicolon separated default values if JSON-PATH expressions do not return any result(must match number of variables)

No

Match Numbers

For each JSON Path Expression, if the JSON Path query leads to many results, you can choose which one(s) to extract as Variables:

- 0: means random (Default Value)
- -1 means extract all results, they will be named as *<variable name>*_N (where N goes from 1 to Number of results)
- X: means extract the *X*th result. If this *X*th is greater than number of matches, then nothing is returned. Default value will be used

The numbers have to be given as a Semicolon separated list. The number of elements in that list have to match the number of given JSON Path Expressions. If left empty, the value

0

will be used as default for every expression.

No

Compute concatenation var

If many results are found, plugin will concatenate them using ‘

,

’ separator and store it in a var named

<variable name>

_ALL

No

^


## Boundary Extractor

Allows the user to extract values from a server response using left and right boundaries. As a post-processor, this element will execute after each Sample request in its scope, testing the boundaries, extracting the requested values, generate the template string, and store the result into the given variable name.

### Parameters

Attribute

Description

Required

Name

Descriptive name for this element that is shown in the tree.

Apply to:

This is for use with samplers that can generate sub-samples, e.g. HTTP Sampler with embedded resources, Mail Reader or samples generated by the Transaction Controller.

- Main sample only - only applies to the main sample
- Sub-samples only - only applies to the sub-samples
- Main sample and sub-samples - applies to both.
- JMeter Variable Name to use - assertion is to be applied to the contents of the named variable

Matching is applied to all qualifying samples in turn. For example if there is a main sample and 3 sub-samples, each of which contains a single match test, (i.e. 4 matches in total). For match number =

3

, Sub-samples only, the extractor will match the 3

rd

sub-sample. For match number =

3

, Main sample and sub-samples, the extractor will match the 2

nd

sub-sample (1

st

match is main sample). For match number =

0

or negative, all qualifying samples will be processed. For match number >

0

, matching will stop as soon as enough matches have been found.

Yes

Field to check

The following fields can be checked:

- Body - the body of the response, e.g. the content of a web-page (excluding headers)
- Body (unescaped) - the body of the response, with all Html escape codes replaced. Note that Html escapes are processed without regard to context, so some incorrect substitutions may be made. Note that this option highly impacts performances, so use it only when absolutely necessary and be aware of its impacts
- Body as a Document - the extract text from various type of documents via Apache Tika (see View Results Tree Document view section). Note that the Body as a Document option can impact performances, so ensure it is OK for your test
- Request Headers - may not be present for non-HTTP samples
- Response Headers - may not be present for non-HTTP samples
- URL
- Response Code - e.g. 200
- Response Message - e.g. OK

Headers can be useful for HTTP samples; it may not be present for other sample types.

Yes

Name of created variable

The name of the JMeter variable in which to store the result. Also note that each group is stored as

[refname]_g#

, where

[refname]

is the string you entered as the reference name, and

#

is the group number, where group

0

is the entire match, group

1

is the match from the first set of parentheses, etc.

Yes

Left Boundary

Left boundary of value to find

No

Right Boundary

Right boundary of value to find

No

Match No. (0 for Random)

Indicates which match to use. The boundaries may match multiple times.

- Use a value of zero to indicate JMeter should choose a match at random.
- A positive number N means to select the nth match.
- Negative numbers are used in conjunction with the ForEach Controller - see below.

Yes

Default Value

If the boundaries do not match, then the reference variable will be set to the default value. This is particularly useful for debugging tests. If no default is provided, then it is difficult to tell whether the boundaries did not match, or maybe the wrong variable is being used.

However, if you have several test elements that set the same variable, you may wish to leave the variable unchanged if the expression does not match. In this case, remove the default value once debugging is complete.

No, but recommended

If the match number is set to a non-negative number, and a match occurs, the variables are set as follows:

- refName - the value of the extraction

If no match occurs, then the refName variable is set to the default (unless this is absent).

If the match number is set to a negative number, then all the possible matches in the sampler data are processed. The variables are set as follows:

- refName_matchNr - the number of matches found; could be 0
- refName_*n*, where n = 1, 2, 3 etc. - the strings as generated by the template
- refName_*n*_g*m*, where m=0, 1, 2 - the groups for match n
- refName - always set to the default value

Note that the refName variable is always set to the default value in this case, and the associated group variables are not set.

If both left and right boundary are null, the whole data selected in scope is returned

^

# 18.9 Miscellaneous Features


## Test Plan

The Test Plan is where the overall settings for a test are specified.

Static variables can be defined for values that are repeated throughout a test, such as server names. For example the variable SERVER could be defined as www.example.com, and the rest of the test plan could refer to it as ${SERVER}. This simplifies changing the name later.

If the same variable name is reused on one of more User Defined Variables Configuration elements, the value is set to the last definition in the test plan (reading from top to bottom). Such variables should be used for items that may change between test runs, but which remain the same during a test run.

Note that the Test Plan cannot refer to variables it defines. If you need to construct other variables from the Test Plan variables, use a User Defined Variables test element.

Selecting Functional Testing instructs JMeter to save the additional sample information - Response Data and Sampler Data - to all result files. This increases the resources needed to run a test, and may adversely impact JMeter performance. If more data is required for a particular sampler only, then add a Listener to it, and configure the fields as required. The option does not affect CSV result files, which cannot currently store such information.

Also, an option exists here to instruct JMeter to run the Thread Group serially rather than in parallel.

Run tearDown Thread Groups after shutdown of main threads: if selected, the tearDown groups (if any) will be run after graceful shutdown of the main threads. The tearDown threads won't be run if the test is forcibly stopped.

Test plan now provides an easy way to add classpath setting to a specific test plan. The feature is additive, meaning that you can add jar files or directories, but removing an entry requires restarting JMeter. Note that this cannot be used to add JMeter GUI plugins, because they are processed earlier. However it can be useful for utility jars such as JDBC drivers. The jars are only added to the search path for the JMeter loader, not for the system class loader.

JMeter properties also provides an entry for loading additional classpaths. In jmeter.properties, edit "user.classpath" or "plugin_dependency_paths" to include additional libraries. See JMeter's Classpath and Configuring JMeter for details.

^
