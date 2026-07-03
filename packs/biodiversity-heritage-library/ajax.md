---
title: "Ajax (programming)"
source: https://en.wikipedia.org/wiki/AJAX
domain: biodiversity-heritage-library
license: CC-BY-SA-4.0
tags: biodiversity heritage library
fetched: 2026-07-03
---

# Ajax (programming)

(Redirected from

AJAX

)

**Asynchronous JavaScript and XML**, usually referred to as **Ajax** (or **AJAX**, /ˈeɪdʒæks/) is a set of web development techniques that uses various web technologies on the client-side to create asynchronous web applications. With Ajax, web applications can send and retrieve data from a server asynchronously (in the background) without interfering with the display and behaviour of the existing page. By decoupling the data interchange layer from the presentation layer, Ajax allows web pages and, by extension, web applications, to change content dynamically without the need to reload the entire page. In practice, modern implementations commonly utilize JSON instead of XML.

Ajax is not a technology, but rather a programming pattern. HTML and CSS can be used in combination to mark up and style information. The webpage can be modified by JavaScript to dynamically display (and allow the user to interact with) the new information. The built-in XMLHttpRequest object is used to execute Ajax on webpages, allowing websites to load content onto the screen without refreshing the page.

## History

In the early-to-mid 1990s, most websites were based on complete HTML pages. Each user action required a complete new page to be loaded from the server. This process was inefficient, as reflected by the user experience: all page content disappeared, then the new page appeared. Each time the browser reloaded a page because of a partial change, all the content had to be re-sent, even though only some of the information had changed. This placed additional load on the server and made bandwidth a limiting factor in performance.

The foundations of AJAX originate back in 1996 with the introduction of JavaScript 1. Developers quickly discovered that any HTML element which accepted a "src" attribute could be used to fetch remote data. By changing the src of a hidden frame, a developer could fetch remote data, process or display it without a page refresh. The remote data could be a string, JavaScript code, XML or a partial HTML page generated on the server. The same could be done with `<img>` and `<embed>` tags, but many developers were alarmed at the concept of an executable GIF and preferred to use the hidden `<iframe>`. This technique was used for both Netscape Navigator and Internet Explorer, the two main browsers at the time, until developers discovered the XMLHTTP server object (MSXML 1.0) was included in Internet Explorer 4. Browser detection was then used to either implement the hidden `<iframe>` in Netscape or use the XMLHTTP (MSXML 1.0) object in IE 4.

In 1996, the iframe tag was introduced by Internet Explorer; like the object element, it can load a part of the web page asynchronously. In 1998, the Microsoft Outlook Web Access team developed the concept behind the XMLHttpRequest scripting object. It appeared as XMLHTTP in the second version of the MSXML library, which shipped with Internet Explorer 5.0 in March 1999.

The functionality of the Windows XMLHTTP ActiveX control in IE 5 was later implemented by Mozilla Firefox, Safari, Opera, Google Chrome, and other browsers as the XMLHttpRequest JavaScript object. Microsoft adopted the native XMLHttpRequest model as of Internet Explorer 7. Support for the ActiveX version remained in Internet Explorer and on "Internet Explorer mode" in Microsoft Edge. The utility of these background HTTP requests and asynchronous Web technologies remained fairly obscure until it started appearing in large scale online applications such as Outlook Web Access (2000) and Oddpost (2002).

Google made a wide deployment of standards-compliant, cross browser Ajax with Gmail (2004) and Google Maps (2005). In October 2004 Kayak.com's public beta release was among the first large-scale e-commerce uses of what their developers at that time called "the xml http thing". This increased interest in Ajax among web program developers.

The term *AJAX* was publicly used on 18 February 2005 by Jesse James Garrett in an article titled *Ajax: A New Approach to Web Applications*, based on techniques used on Google pages.

On 5 April 2006, the World Wide Web Consortium (W3C) released the first draft specification for the XMLHttpRequest object in an attempt to create an official Web standard. The latest draft of the XMLHttpRequest object was published on 6 October 2016, and the XMLHttpRequest specification is now a living standard.

## Technologies

The term *Ajax* has come to represent a broad group of Web technologies that can be used to implement a Web application that communicates with a server in the background, without interfering with the current state of the page. In the article that coined the term Ajax, Jesse James Garrett explained that the following technologies are incorporated:

- HTML (or XHTML) and CSS for presentation
- The Document Object Model (DOM) for dynamic display of and interaction with data
- JSON or XML for the interchange of data, and XSLT for XML manipulation
- The XMLHttpRequest object for asynchronous communication
- JavaScript to bring these technologies together

Since then, however, there have been a number of developments in the technologies used in an Ajax application, and in the definition of the term Ajax itself. XML is no longer required for data interchange and, therefore, XSLT is no longer required for the manipulation of data. JavaScript Object Notation (JSON) is often used as an alternative format for data interchange, although other formats such as preformatted HTML or plain text can also be used. A variety of popular JavaScript libraries, including jQuery, include abstractions to assist in executing Ajax requests.

## Examples

### JavaScript example

An example of a simple Ajax request using the GET method, written in JavaScript.

get-ajax-data.js:

```mw
// This is the client-side script.

// Initialize the HTTP request.
let xhr = new XMLHttpRequest();
// define the request
xhr.open('GET', 'send-ajax-data.php');

// Track the state changes of the request.
xhr.onreadystatechange = function ()
{
	const DONE = 4; // readyState 4 means the request is done.
	const OK = 200; // status 200 is a successful return.
	if (xhr.readyState === DONE)
	{
		if (xhr.status === OK)
		{
			console.log(xhr.responseText); // 'This is the output.'
		}
		else
		{
			console.log('Error: ' + xhr.status); // An error occurred during the request.
		}
	}
};

// Send the request to send-ajax-data.php
xhr.send(null);
```

send-ajax-data.php:

```mw
<?php
// This is the server-side script.

// Set the content type.
header('Content-Type: text/plain');

// Send the data back.
echo "This is the output.";
?>
```

### Fetch example

Fetch is a native JavaScript API. According to Google Developers Documentation, "Fetch makes it easier to make web requests and handle responses than with the older XMLHttpRequest."

```mw
fetch('send-ajax-data.php')
    .then(data => console.log(data))
    .catch (error => console.log('Error:' + error));
```

#### ES7 async/await example

```mw
async function doAjax1()
{
    try 
    {
        const res = await fetch('send-ajax-data.php');
        const data = await res.text();
        console.log(data);
    } 
    catch (error)
    {
        console.log('Error:' + error);
    }
}

doAjax1();
```

Fetch relies on JavaScript promises.

The `fetch` specification differs from `Ajax` in the following significant ways:

- The Promise returned from `fetch()` **won't reject on HTTP error status** even if the response is an HTTP 404 or 500. Instead, as soon as the server responds with headers, the Promise will resolve normally (with the `ok` property of the response set to false if the response isn't in the range 200–299), and it will only reject on network failure or if anything prevented the request from completing.
- `fetch()` **won't send cross-origin cookies** unless you set the *credentials* init option. (Since April 2018. The spec changed the default credentials policy to `same-origin`. Firefox changed since 61.0b13.)

## Benefits

Ajax offers several benefits that can significantly enhance web application performance and user experience. By reducing server traffic and improving speed, Ajax plays a crucial role in modern web development. One key advantage of Ajax is its capacity to render web applications without requiring data retrieval, resulting in reduced server traffic. This optimization minimizes response times on both the server and client sides, eliminating the need for users to endure loading screens.

Furthermore, Ajax facilitates asynchronous processing by simplifying the utilization of XmlHttpRequest, which enables efficient handling of requests for asynchronous data retrieval. Additionally, the dynamic loading of content enhances the application's performance significantly.

Besides, Ajax enjoys broad support across all major web browsers, including Microsoft Internet Explorer versions 5 and above, Mozilla Firefox versions 1.0 and beyond, Opera versions 7.6 and above, and Apple Safari versions 1.2 and higher.
