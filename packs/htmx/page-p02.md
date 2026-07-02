---
title: "</> htmx ~ Documentation (part 2/2)"
source: https://htmx.org/docs/
domain: htmx
license: CC-BY-SA-4.0 / BSD (htmx.org)
tags: htmx, hypermedia driven, hx-get, ajax attributes
fetched: 2026-07-02
part: 2/2
---

## Events & Logging

Htmx has an extensive events mechanism, which doubles as the logging system.

If you want to register for a given htmx event you can use

```js
document.body.addEventListener('htmx:load', function(evt) {
    myJavascriptLib.init(evt.detail.elt);
});
```

or, if you would prefer, you can use the following htmx helper:

```javascript
htmx.on("htmx:load", function(evt) {
    myJavascriptLib.init(evt.detail.elt);
});
```

The `htmx:load` event is fired every time an element is loaded into the DOM by htmx, and is effectively the equivalent to the normal `load` event.

Some common uses for htmx events are:

### Initialize A 3rd Party Library With Events

Using the `htmx:load` event to initialize content is so common that htmx provides a helper function:

```javascript
htmx.onLoad(function(target) {
    myJavascriptLib.init(target);
});
```

This does the same thing as the first example, but is a little cleaner.

### Configure a Request With Events

You can handle the `htmx:configRequest` event in order to modify an AJAX request before it is issued:

```javascript
document.body.addEventListener('htmx:configRequest', function(evt) {
    evt.detail.parameters['auth_token'] = getAuthToken(); // add a new parameter into the request
    evt.detail.headers['Authentication-Token'] = getAuthToken(); // add a new header into the request
});
```

Here we add a parameter and header to the request before it is sent.

### Modifying Swapping Behavior With Events

You can handle the `htmx:beforeSwap` event in order to modify the swap behavior of htmx:

```javascript
document.body.addEventListener('htmx:beforeSwap', function(evt) {
    if(evt.detail.xhr.status === 404){
        // alert the user when a 404 occurs (maybe use a nicer mechanism than alert())
        alert("Error: Could Not Find Resource");
    } else if(evt.detail.xhr.status === 422){
        // allow 422 responses to swap as we are using this as a signal that
        // a form was submitted with bad data and want to rerender with the
        // errors
        //
        // set isError to false to avoid error logging in console
        evt.detail.shouldSwap = true;
        evt.detail.isError = false;
    } else if(evt.detail.xhr.status === 418){
        // if the response code 418 (I'm a teapot) is returned, retarget the
        // content of the response to the element with the id `teapot`
        evt.detail.shouldSwap = true;
        evt.detail.target = htmx.find("#teapot");
    }
});
```

Here we handle a few 400-level error response codes that would normally not do a swap in htmx.

### Event Naming

Note that all events are fired with two different names

- Camel Case
- Kebab Case

So, for example, you can listen for `htmx:afterSwap` or for `htmx:after-swap`. This facilitates interoperability with other libraries. Alpine.js, for example, requires kebab case.

### Logging

If you set a logger at `htmx.logger`, every event will be logged. This can be very useful for troubleshooting:

```javascript
htmx.logger = function(elt, event, data) {
    if(console) {
        console.log(event, elt, data);
    }
}
```


## Debugging

Declarative and event driven programming with htmx (or any other declarative language) can be a wonderful and highly productive activity, but one disadvantage when compared with imperative approaches is that it can be trickier to debug.

Figuring out why something *isn’t* happening, for example, can be difficult if you don’t know the tricks.

Well, here are the tricks:

The first debugging tool you can use is the `htmx.logAll()` method. This will log every event that htmx triggers and will allow you to see exactly what the library is doing.

```javascript
htmx.logAll();
```

Of course, that won’t tell you why htmx *isn’t* doing something. You might also not know *what* events a DOM element is firing to use as a trigger. To address this, you can use the `monitorEvents()` method available in the browser console:

```javascript
monitorEvents(htmx.find("#theElement"));
```

This will spit out all events that are occurring on the element with the id `theElement` to the console, and allow you to see exactly what is going on with it.

Note that this *only* works from the console, you cannot embed it in a script tag on your page.

Finally, push come shove, you might want to just debug `htmx.js` by loading up the unminimized version. It’s about 2500 lines of javascript, so not an insurmountable amount of code. You would most likely want to set a break point in the `issueAjaxRequest()` and `handleAjaxResponse()` methods to see what’s going on.

And always feel free to jump on the Discord if you need help.

### Creating Demos

Sometimes, in order to demonstrate a bug or clarify a usage, it is nice to be able to use a javascript snippet site like jsfiddle. To facilitate easy demo creation, htmx hosts a demo script site that will install:

- htmx
- hyperscript
- a request mocking library

Simply add the following script tag to your demo/fiddle/whatever:

```html
<script src="https://demo.htmx.org"></script>
```

This helper allows you to add mock responses by adding `template` tags with a `url` attribute to indicate which URL. The response for that url will be the innerHTML of the template, making it easy to construct mock responses. You can add a delay to the response with a `delay` attribute, which should be an integer indicating the number of milliseconds to delay

You may embed simple expressions in the template with the `${}` syntax.

Note that this should only be used for demos and is in no way guaranteed to work for long periods of time as it will always be grabbing the latest versions htmx and hyperscript!

#### Demo Example

Here is an example of the code in action:

```html
<!-- load demo environment -->
<script src="https://demo.htmx.org"></script>

<!-- post to /foo -->
<button hx-post="/foo" hx-target="#result">
    Count Up
</button>
<output id="result"></output>

<!-- respond to /foo with some dynamic content in a template tag -->
<script>
    globalInt = 0;
</script>
<template url="/foo" delay="500"> <!-- note the url and delay attributes -->
    ${globalInt++}
</template>
```


## Scripting

While htmx encourages a hypermedia approach to building web applications, it offers many options for client scripting. Scripting is included in the REST-ful description of web architecture, see: Code-On-Demand. As much as is feasible, we recommend a hypermedia-friendly approach to scripting in your web application:

- Respect HATEOAS
- Use events to communicate between components
- Use islands to isolate non-hypermedia components from the rest of your application
- Consider inline scripting

The primary integration point between htmx and scripting solutions is the events that htmx sends and can respond to. See the SortableJS example in the 3rd Party Javascript section for a good template for integrating a JavaScript library with htmx via events.

Scripting solutions that pair well with htmx include:

- VanillaJS - Simply using the built-in abilities of JavaScript to hook in event handlers to respond to the events htmx emits can work very well for scripting. This is an extremely lightweight and increasingly popular approach.
- AlpineJS - Alpine.js provides a rich set of tools for creating sophisticated front end scripts, including reactive programming support, while still remaining extremely lightweight. Alpine encourages the “inline scripting” approach that we feel pairs well with htmx.
- jQuery - Despite its age and reputation in some circles, jQuery pairs very well with htmx, particularly in older code-bases that already have a lot of jQuery in them.
- hyperscript - Hyperscript is an experimental front-end scripting language created by the same team that created htmx. It is designed to embed well in HTML and both respond to and create events, and pairs very well with htmx.

We have an entire chapter entitled “Client-Side Scripting” in our book that looks at how scripting can be integrated into your htmx-based application.

### The `hx-on*` Attributes

HTML allows the embedding of inline scripts via the `onevent` properties, such as `onClick`:

```html
<button onclick="alert('You clicked me!')">
    Click Me!
</button>
```

This feature allows scripting logic to be co-located with the HTML elements the logic applies to, giving good Locality of Behaviour (LoB). Unfortunately, HTML only allows `on*` attributes for a fixed number of specific DOM events (e.g. `onclick`) and doesn’t provide a generalized mechanism for responding to arbitrary events on elements.

In order to address this shortcoming, htmx offers `hx-on*` attributes. These attributes allow you to respond to any event in a manner that preserves the LoB of the standard `on*` properties.

If we wanted to respond to the `click` event using an `hx-on` attribute, we would write this:

```html
<button hx-on:click="alert('You clicked me!')">
    Click Me!
</button>
```

So, the string `hx-on`, followed by a colon (or a dash), then by the name of the event.

For a `click` event, of course, we would recommend sticking with the standard `onclick` attribute. However, consider an htmx-powered button that wishes to add a parameter to a request using the `htmx:config-request` event. This would not be possible using a standard `on*` property, but it can be done using the `hx-on:htmx:config-request` attribute:

```html
<button hx-post="/example"
        hx-on:htmx:config-request="event.detail.parameters.example = 'Hello Scripting!'">
    Post Me!
</button>
```

Here the `example` parameter is added to the `POST` request before it is issued, with the value ‘Hello Scripting!’.

Another usecase is to reset user input on successful requests using the `afterRequest` event, avoiding the need for something like an out of band swap.

The `hx-on*` attributes are a very simple mechanism for generalized embedded scripting. It is *not* a replacement for more fully developed front-end scripting solutions such as AlpineJS or hyperscript. It can, however, augment a VanillaJS-based approach to scripting in your htmx-powered application.

Note that HTML attributes are *case insensitive*. This means that, unfortunately, events that rely on capitalization/ camel casing, cannot be responded to. If you need to support camel case events we recommend using a more fully functional scripting solution such as AlpineJS or hyperscript. htmx dispatches all its events in both camelCase and in kebab-case for this very reason.

### 3rd Party Javascript

Htmx integrates fairly well with third party libraries. If the library fires events on the DOM, you can use those events to trigger requests from htmx.

A good example of this is the SortableJS demo:

```html
<form class="sortable" hx-post="/items" hx-trigger="end">
    <div class="htmx-indicator">Updating...</div>
    <div><input type='hidden' name='item' value='1'/>Item 1</div>
    <div><input type='hidden' name='item' value='2'/>Item 2</div>
    <div><input type='hidden' name='item' value='2'/>Item 3</div>
</form>
```

With Sortable, as with most javascript libraries, you need to initialize content at some point.

In jquery you might do this like so:

```javascript
$(document).ready(function() {
    var sortables = document.body.querySelectorAll(".sortable");
    for (var i = 0; i < sortables.length; i++) {
        var sortable = sortables[i];
        new Sortable(sortable, {
            animation: 150,
            ghostClass: 'blue-background-class'
        });
    }
});
```

In htmx, you would instead use the `htmx.onLoad` function, and you would select only from the newly loaded content, rather than the entire document:

```js
htmx.onLoad(function(content) {
    var sortables = content.querySelectorAll(".sortable");
    for (var i = 0; i < sortables.length; i++) {
        var sortable = sortables[i];
        new Sortable(sortable, {
            animation: 150,
            ghostClass: 'blue-background-class'
        });
    }
})
```

This will ensure that as new content is added to the DOM by htmx, sortable elements are properly initialized.

If javascript adds content to the DOM that has htmx attributes on it, you need to make sure that this content is initialized with the `htmx.process()` function.

For example, if you were to fetch some data and put it into a div using the `fetch` API, and that HTML had htmx attributes in it, you would need to add a call to `htmx.process()` like this:

```js
let myDiv = document.getElementById('my-div')
fetch('http://example.com/movies.json')
    .then(response => response.text())
    .then(data => { myDiv.innerHTML = data; htmx.process(myDiv); } );
```

Some 3rd party libraries create content from HTML template elements. For instance, Alpine JS uses the `x-if` attribute on templates to add content conditionally. Such templates are not initially part of the DOM and, if they contain htmx attributes, will need a call to `htmx.process()` after they are loaded. The following example uses Alpine’s `$watch` function to look for a change of value that would trigger conditional content:

```html
<div x-data="{show_new: false}"
    x-init="$watch('show_new', value => {
        if (show_new) {
            htmx.process(document.querySelector('#new_content'))
        }
    })">
    <button @click = "show_new = !show_new">Toggle New Content</button>
    <template x-if="show_new">
        <div id="new_content">
            <a hx-get="/server/newstuff" href="#">New Clickable</a>
        </div>
    </template>
</div>
```

#### Web Components

Please see the Web Components Examples page for examples on how to integrate htmx with web components.


## Caching

htmx works with standard HTTP caching mechanisms out of the box.

If your server adds the `Last-Modified` HTTP response header to the response for a given URL, the browser will automatically add the `If-Modified-Since` request HTTP header to the next requests to the same URL. Be mindful that if your server can render different content for the same URL depending on some other headers, you need to use the `Vary` response HTTP header. For example, if your server renders the full HTML when the `HX-Request` header is missing or `false`, and it renders a fragment of that HTML when `HX-Request: true`, you need to add `Vary: HX-Request`. That causes the cache to be keyed based on a composite of the response URL and the `HX-Request` request header — rather than being based just on the response URL. Always disable `htmx.config.historyRestoreAsHxRequest` so that these history full HTML requests are not cached with partial fragment responses.

If you are unable (or unwilling) to use the `Vary` header, you can alternatively set the configuration parameter `getCacheBusterParam` to `true`. If this configuration variable is set, htmx will include a cache-busting parameter in `GET` requests that it makes, which will prevent browsers from caching htmx-based and non-htmx based responses in the same cache slot.

htmx also works with `ETag` as expected. Be mindful that if your server can render different content for the same URL (for example, depending on the value of the `HX-Request` header), the server needs to generate a different `ETag` for each content.


## Security

htmx allows you to define logic directly in your DOM. This has a number of advantages, the largest being Locality of Behavior, which makes your system easier to understand and maintain.

A concern with this approach, however, is security: since htmx increases the expressiveness of HTML, if a malicious user is able to inject HTML into your application, they can leverage this expressiveness of htmx to malicious ends.

### Rule 1: Escape All User Content

The first rule of HTML-based web development has always been: *do not trust input from the user*. You should escape all 3rd party, untrusted content that is injected into your site. This is to prevent, among other issues, XSS attacks.

There is extensive documentation on XSS and how to prevent it on the excellent OWASP Website, including a Cross Site Scripting Prevention Cheat Sheet.

The good news is that this is a very old and well understood topic, and the vast majority of server-side templating languages support automatic escaping of content to prevent just such an issue.

That being said, there are times people choose to inject HTML more dangerously, often via some sort of `raw()` mechanism in their templating language. This can be done for good reasons, but if the content being injected is coming from a 3rd party then it *must* be scrubbed, including removing attributes starting with `hx-` and `data-hx`, as well as inline `<script>` tags, etc.

If you are injecting raw HTML and doing your own escaping, a best practice is to *whitelist* the attributes and tags you allow, rather than to blacklist the ones you disallow.

### htmx Security Tools

Of course, bugs happen and developers are not perfect, so it is good to have a layered approach to security for your web application, and htmx provides tools to help secure your application as well.

Let’s take a look at them.

#### `hx-disable`

The first tool htmx provides to help further secure your application is the `hx-disable` attribute. This attribute will prevent processing of all htmx attributes on a given element, and on all elements within it. So, for example, if you were including raw HTML content in a template (again, this is not recommended!) then you could place a div around the content with the `hx-disable` attribute on it:

```html
<div hx-disable>
    <%= raw(user_content) %>
</div>
```

And htmx will not process any htmx-related attributes or features found in that content. This attribute cannot be disabled by injecting further content: if an `hx-disable` attribute is found anywhere in the parent hierarchy of an element, it will not be processed by htmx.

#### `hx-history`

Another security consideration is htmx history cache. You may have pages that have sensitive data that you do not want stored in the users `localStorage` cache. You can omit a given page from the history cache by including the `hx-history` attribute anywhere on the page, and setting its value to `false`.

#### Configuration Options

htmx also provides configuration options related to security:

- `htmx.config.selfRequestsOnly` - if set to `true`, only requests to the same domain as the current document will be allowed
- `htmx.config.allowScriptTags` - htmx will process `<script>` tags found in new content it loads. If you wish to disable this behavior you can set this configuration variable to `false`
- `htmx.config.historyCacheSize` - can be set to `0` to avoid storing any HTML in the `localStorage` cache
- `htmx.config.allowEval` - can be set to `false` to disable all features of htmx that rely on eval:
  - event filters
  - `hx-on:` attributes
  - `hx-vals` with the `js:` prefix
  - `hx-headers` with the `js:` prefix

Note that all features removed by disabling `eval()` can be reimplemented using your own custom javascript and the htmx event model.

#### Events

If you want to allow requests to some domains beyond the current host, but not leave things totally open, you can use the `htmx:validateUrl` event. This event will have the request URL available in the `detail.url` slot, as well as a `sameHost` property.

You can inspect these values and, if the request is not valid, invoke `preventDefault()` on the event to prevent the request from being issued.

```javascript
document.body.addEventListener('htmx:validateUrl', function (evt) {
  // only allow requests to the current server as well as myserver.com
  if (!evt.detail.sameHost && evt.detail.url.hostname !== "myserver.com") {
    evt.preventDefault();
  }
});
```

### CSP Options

Browsers also provide tools for further securing your web application. The most powerful tool available is a Content Security Policy. Using a CSP you can tell the browser to, for example, not issue requests to non-origin hosts, to not evaluate inline script tags, etc.

Here is an example CSP in a `meta` tag:

```html
    <meta http-equiv="Content-Security-Policy" content="default-src 'self';">
```

This tells the browser “Only allow connections to the original (source) domain”. This would be redundant with the `htmx.config.selfRequestsOnly`, but a layered approach to security is warranted and, in fact, ideal, when dealing with application security.

A full discussion of CSPs is beyond the scope of this document, but the MDN Article provides a good jumping-off point for exploring this topic.

### CSRF Prevention

The assignment and checking of CSRF tokens are typically backend responsibilities, but `htmx` can support returning the CSRF token automatically with every request using the `hx-headers` attribute. The attribute needs to be added to the element issuing the request or one of its ancestor elements. This makes the `html` and `body` elements effective global vehicles for adding the CSRF token to the `HTTP` request header, as illustrated below.

Note: `hx-boost` does not update the `<html>` or `<body>` tags; if using this feature with `hx-boost`, make sure to include the CSRF token on an element that *will* get replaced. Many web frameworks support automatically inserting the CSRF token as a hidden input in HTML forms. This is encouraged whenever possible.

```html
<html lang="en" hx-headers='{"X-CSRF-TOKEN": "CSRF_TOKEN_INSERTED_HERE"}'>
    :
</html>
```

```html
    <body hx-headers='{"X-CSRF-TOKEN": "CSRF_TOKEN_INSERTED_HERE"}'>
        :
    </body>
```

The above elements are usually unique in an HTML document and should be easy to locate within templates.


## Configuring htmx

Htmx has some configuration options that can be accessed either programmatically or declaratively. They are listed below:

| Config Variable | Info |
|---|---|
| `htmx.config.historyEnabled` | defaults to `true`, really only useful for testing |
| `htmx.config.historyCacheSize` | defaults to 10 |
| `htmx.config.refreshOnHistoryMiss` | defaults to `false`, if set to `true` htmx will issue a full page refresh on history misses rather than use an AJAX request |
| `htmx.config.defaultSwapStyle` | defaults to `innerHTML` |
| `htmx.config.defaultSwapDelay` | defaults to 0 |
| `htmx.config.defaultSettleDelay` | defaults to 20 |
| `htmx.config.includeIndicatorStyles` | defaults to `true` (determines if the indicator styles are loaded) |
| `htmx.config.indicatorClass` | defaults to `htmx-indicator` |
| `htmx.config.requestClass` | defaults to `htmx-request` |
| `htmx.config.addedClass` | defaults to `htmx-added` |
| `htmx.config.settlingClass` | defaults to `htmx-settling` |
| `htmx.config.swappingClass` | defaults to `htmx-swapping` |
| `htmx.config.allowEval` | defaults to `true`, can be used to disable htmx’s use of eval for certain features (e.g. trigger filters) |
| `htmx.config.allowScriptTags` | defaults to `true`, determines if htmx will process script tags found in new content |
| `htmx.config.inlineScriptNonce` | defaults to `''`, meaning that no nonce will be added to inline scripts |
| `htmx.config.attributesToSettle` | defaults to `["class", "style", "width", "height"]`, the attributes to settle during the settling phase |
| `htmx.config.inlineStyleNonce` | defaults to `''`, meaning that no nonce will be added to inline styles |
| `htmx.config.useTemplateFragments` | defaults to `false`, HTML template tags for parsing content from the server (not IE11 compatible!) |
| `htmx.config.wsReconnectDelay` | defaults to `full-jitter` |
| `htmx.config.wsBinaryType` | defaults to `blob`, the type of binary data being received over the WebSocket connection |
| `htmx.config.disableSelector` | defaults to `[hx-disable], [data-hx-disable]`, htmx will not process elements with this attribute on it or a parent |
| `htmx.config.withCredentials` | defaults to `false`, allow cross-site Access-Control requests using credentials such as cookies, authorization headers or TLS client certificates |
| `htmx.config.timeout` | defaults to 0, the number of milliseconds a request can take before automatically being terminated |
| `htmx.config.scrollBehavior` | defaults to ‘instant’, the scroll behavior when using the show modifier with `hx-swap`. The allowed values are `instant` (scrolling should happen instantly in a single jump), `smooth` (scrolling should animate smoothly) and `auto` (scroll behavior is determined by the computed value of scroll-behavior). |
| `htmx.config.defaultFocusScroll` | if the focused element should be scrolled into view, defaults to false and can be overridden using the focus-scroll swap modifier. |
| `htmx.config.getCacheBusterParam` | defaults to false, if set to true htmx will append the target element to the `GET` request in the format `org.htmx.cache-buster=targetElementId` |
| `htmx.config.globalViewTransitions` | if set to `true`, htmx will use the View Transition API when swapping in new content. |
| `htmx.config.methodsThatUseUrlParams` | defaults to `["get", "delete"]`, htmx will format requests with these methods by encoding their parameters in the URL, not the request body |
| `htmx.config.selfRequestsOnly` | defaults to `true`, whether to only allow AJAX requests to the same domain as the current document |
| `htmx.config.ignoreTitle` | defaults to `false`, if set to `true` htmx will not update the title of the document when a `title` tag is found in new content |
| `htmx.config.disableInheritance` | disables attribute inheritance in htmx, which can then be overridden by the `hx-inherit` attribute |
| `htmx.config.scrollIntoViewOnBoost` | defaults to `true`, whether or not the target of a boosted element is scrolled into the viewport. If `hx-target` is omitted on a boosted element, the target defaults to `body`, causing the page to scroll to the top. |
| `htmx.config.triggerSpecsCache` | defaults to `null`, the cache to store evaluated trigger specifications into, improving parsing performance at the cost of more memory usage. You may define a simple object to use a never-clearing cache, or implement your own system using a proxy object |
| `htmx.config.responseHandling` | the default Response Handling behavior for response status codes can be configured here to either swap or error |
| `htmx.config.allowNestedOobSwaps` | defaults to `true`, whether to process OOB swaps on elements that are nested within the main response element. See Nested OOB Swaps. |
| `htmx.config.historyRestoreAsHxRequest` | defaults to `true`, Whether to treat history cache miss full page reload requests as a “HX-Request” by returning this response header. This should always be disabled when using HX-Request header to optionally return partial responses |

You can set them directly in javascript, or you can use a `meta` tag:

```html
<meta name="htmx-config" content='{"defaultSwapStyle":"outerHTML"}'>
```


## Conclusion

And that’s it!

Have fun with htmx! You can accomplish quite a bit without writing a lot of code!
