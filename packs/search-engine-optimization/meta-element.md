---
title: "Meta element"
source: https://en.wikipedia.org/wiki/Meta_element
domain: search-engine-optimization
license: CC-BY-SA-4.0
tags: search engine optimization, meta description tag, canonical link relation, web crawler indexing
fetched: 2026-07-02
---

# Meta element

**Meta elements** are tags used in HTML and XHTML documents to provide structured metadata about a Web page. They are part of a web page's `head` section, the term meta indicating that they are a form of self-reference. Multiple Meta elements with different attributes can be used on the same page. Meta elements can be used to specify page description, keywords and any other metadata not provided through the other `head` elements and attributes.

The meta element has two uses: either to emulate the use of an HTTP response header field, or to embed additional metadata within the HTML document.

With HTML up to and including HTML 4.01 and XHTML, there were four valid attributes: `content`, `http-equiv`, `name` and `scheme`. Under HTML 5, `charset` has been added and `scheme` has been removed. `http-equiv` is used to emulate an HTTP header, and `name` to embed metadata. The value of the statement, in either case, is contained in the `content` attribute, which is the only required attribute unless `charset` is given. `charset` is used to indicate the character set of the document, and is available in HTML5.

Such elements must be placed as tags in the `head` section of an HTML or XHTML document.

## Examples of the `meta` element

`meta` elements can specify HTTP headers which should be sent before the actual content when the HTML page is served from the web server to the client. For example:

```mw
<meta charset="utf-8">
```

as an alternative to the response header `Content-Type:` to indicate the media type and, more commonly needed, the UTF-8 character encoding.

Meta tags can be used to describe the contents of the page:

```mw
<meta name="description" content="The Federal Aviation Administration is an operating mode of the U.S. Department of Transportation.">
```

In this example, the `meta` element describes the contents of a web page.

Meta elements provide information about the web page, which can be used by search engines to help categorize the page correctly.

They have been the focus of a field of marketing research known as search engine optimization (SEO), where different methods are used to provide a user's website with a higher ranking on search engines. Prior to the rise of content-analysis by search engines in the mid-1990s (most notably Google), search engines were reliant on metadata to correctly classify a Web page and webmasters quickly learned the commercial significance of having the right meta element. The search engine community is now divided as to the value of meta tags. Some claim they have no value, others that they are central, while many simply conclude there is no clear answer but, since they do no harm, they use them just in case. Google states they do support the meta tags "description", "robots", "google", "google-site-verification", "content-type", "refresh" and "google-bot".

Major search engine robots look at many factors when determining how to rank a page of which meta tags will only form a portion. Furthermore, most search engines change their ranking rules frequently. Google have stated they update their ranking rules every 48 hours. Under such circumstances, a definitive understanding of the role of meta tags in SEO is unlikely.

### The `keywords` attribute

The `keywords` attribute was popularized by search engines such as Infoseek and AltaVista in 1995, and its popularity quickly grew until it became one of the most commonly used `meta` elements.

No consensus exists whether or not the `keywords` attribute has any effect on ranking at any of the major search engines today. It is speculated that it does if the keywords used in the `meta` can also be found in the page copy itself. With respect to Google, thirty-seven leaders in search engine optimization concluded in April 2007 that the relevance of having keywords in the `meta`-attribute `keywords` is little to none and in September 2009 Matt Cutts of Google announced that they were no longer taking keywords into account whatsoever. However, both these articles suggest that Yahoo! still makes use of the keywords meta tag in some of its rankings. Yahoo! itself claims support for the keywords meta tag in conjunction with other factors for improving search rankings. In October 2009 Search Engine Round Table announced that "Yahoo Drops The Meta Keywords Tag Also" but later reported that the announcement made by Yahoo!'s Senior Director of Search was incorrect. In the corrected statement Yahoo! Senior Director of Search states that "…What changed with Yahoo's ranking algorithms is that while we still index the meta keyword tag, the ranking importance given to meta keyword tags receives the lowest ranking signal in our system … it will actually have less effect than introducing those same words in the body of the document, or any other section." In Sept 2012, Google announced that they will consider Keyword Meta tag for news publishers. Google said that this may help worthy content to get noticed. The syntax of the news meta keyword has subtle difference from custom keyword meta tag; it is denoted by "news_keywords", while the custom keyword meta tag is denoted by "keywords". Google News no longer takes into account keywords announced by news_keywords.

### The Title attribute

According to Moz, "Title tags are the second most important on-page factor for SEO, after content". They convey to the search engines what a given page is all about. It used to be standard SEO practice to include the primary and the secondary keywords in the title for better ranking. Google has gone through various iterations of showing short or longer amounts of content from within the title tags.

Regardless, the title tags still hold importance in three different ways.

- They are displayed as page title in search results (and influence user behavior with respect to clicking on particular results).
- Web browsers display them in naming open tabs; since the title is visible on hover, this is especially useful when too many tabs are open and only the favicon for each page (if available) is visible.
- As in search results, titles are visible when page links are posted on social media and this, too, conveys to the users what the link is about.

### The `robots` attribute

The `robots` attribute, supported by several major search engines, controls whether search engine spiders are allowed to index a page, or not, and whether they should follow links from a page, or not. The attribute can contain one or more comma-separate values. The `noindex` value prevents a page from being indexed, and `nofollow` prevents links from being crawled. Other values recognized by one or more search engines can influence how the engine indexes pages, and how those pages appear on the search results. These include `noarchive`, which instructs a search engine not to store an archived copy of the page, and `nosnippet`, which asks that the search engine not include a snippet from the page along with the page's listing in search results.

Meta tags are one of the best options for preventing search engines from indexing content of a website.

##### NOODP

The search engines Google, Yahoo! and MSN used in some cases the title and abstract of the DMOZ (aka Open Directory Project) listing of a website for the title and/or description (also called snippet or abstract) in the search engine results pages (SERP). To give webmasters the option to specify that the Open Directory Project content should not be used for listings of their website, Microsoft introduced in May 2006 the new "`NOODP`" value for the "`robots`" element of the meta tags. Google followed in July 2006 and Yahoo! in October 2006.

By 2017, Google reported stopping the use of DMOZ, following its closure, hence, NOODP directive is ignored since.

The syntax is the same for all search engines who support the tag.

```mw
<meta name="robots" content="noodp" >
```

Webmasters can decide if they want to disallow the use of their ODP listing on a per search engine basis

Google:

```mw
<meta name="googlebot" content="noodp" >
```

Yahoo!

```mw
<meta name="Slurp" content="noodp" >
```

MSN and Live Search (via bingbot, previously msnbot):

```mw
<meta name="bingbot" content="noodp" >
```

##### NOYDIR

Yahoo! puts content from their own Yahoo! directory next to the ODP listing. In 2007 they introduced a meta tag that lets web designers opt-out of this.

Adding the `NOYDIR` tag to a page will prevent Yahoo! from displaying Yahoo! Directory titles and abstracts.

```mw
<meta name="robots" content="noydir" >
<meta name="Slurp" content="noydir" >
```

### Effect on searching

Google does not use HTML keyword or meta tag elements for indexing. The Director of Research at Google, Monika Henzinger, was quoted (in 2002) as saying, "Currently we don't trust metadata because we are afraid of being manipulated." Other search engines developed techniques to penalize Web sites considered to be "cheating the system". For example, a Web site repeating the same meta keyword several times may have its ranking *decreased* by a search engine trying to eliminate this practice, though that is unlikely. It is more likely that a search engine will ignore the meta keyword element completely, and most do regardless of how many words are used in the element.

Google does, however, use meta tag elements for displaying site links. The title tags are used to create the link in search results:

```mw
<title>Site name - Page title - Keyword description</title>
```

The meta description often appears in Google search results to describe the link:

```mw
<meta name="description" content="A blurb to describe the content of the page appears here" >
```

Additionally, enterprise search startup Swiftype considers meta tags as a mechanism for signaling relevancy for their web site search engines, even introducing their own extension called Meta Tags 2.

## Redirects

Meta refresh elements can be used to instruct a Web browser to automatically refresh a Web page after a given time interval. It is also possible to specify an alternative URL and use this technique in order to redirect the user to a different location. Auto refreshing via a META element has been deprecated for more than ten years, and recognized as problematic before that.

The W3C suggests that user agents should allow users to disable it, otherwise META refresh should not be used by web pages. For Internet Explorer's security settings, under the miscellaneous category, meta refresh can be turned off by the user, thereby disabling its redirect ability. In Mozilla Firefox it can be disabled in the configuration file under the key name "accessibility.blockautorefresh".

Many web design tutorials also point out that client-side redirecting tends to interfere with the normal functioning of a Web browser's "back" button. After being redirected, clicking the back button will cause the user to go back to the redirect page, which redirects them again. Some modern browsers seem to overcome this problem however, including Safari, Mozilla Firefox and Opera.

Auto-redirects via markup (versus server-side redirects) are not in compliance with the W3C's – Web Content Accessibility Guidelines (WCAG) 1.0 (guideline 7.5).

## HTTP message headers

Meta elements of the form `<meta http-equiv="foo" content="bar">` can be used as alternatives to HTTP headers. For example, `<meta http-equiv="expires" content="Wed, 21 June 2006 14:25:27 GMT">` would tell the browser that the page "expires" on June 21, 2006 at 14:25:27 GMT and that it may safely cache the page until then. The HTML 4.01 specification optionally allows this tag to be parsed by HTTP servers and set as part of the HTTP response headers, but no web servers currently implement this behavior. Instead, the user agent emulates the behavior for some HTTP headers as if they had been sent in the response header itself.

## Alternative to `meta` elements

Some HTML elements and attributes already handle certain pieces of meta data and may be used by authors instead of META to specify those pieces: the TITLE element, the ADDRESS element, the INS and DEL elements, the title attribute, and the cite attribute.

An alternative to `meta` elements for enhanced subject access within a website is the use of a back-of-book-style index for the website. See the American Society of Indexers website for an example.

In 1994, ALIWEB, also used an index file to provide the type of information commonly found in meta keywords attributes.

In cases where the content attribute's value is a URL, many authors decide to use a link element with a proper value for its rel attribute as well.

For a comparison on when it is best to use HTTP-headers, meta-elements, or attributes in the case of language specification: see here.
