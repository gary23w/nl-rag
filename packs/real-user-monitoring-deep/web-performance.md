---
title: "Web performance"
source: https://en.wikipedia.org/wiki/Web_performance
domain: real-user-monitoring-deep
license: CC-BY-SA-4.0
tags: real user monitoring, field performance telemetry, page load timing, core web vitals capture
fetched: 2026-07-02
---

# Web performance

**Web performance** refers to the speed in which web pages are downloaded and displayed on the user's web browser. **Web performance optimization (WPO)**, or **website optimization** is the field of knowledge about increasing web performance.

Faster website download speeds have been shown to increase visitor retention and loyalty and user satisfaction, especially for users with slow internet connections and those on mobile devices. Web performance also leads to less data travelling across the web, which in turn lowers a website's power consumption and environmental impact. Some aspects which can affect the speed of page load include browser/server cache, image optimization, and encryption (for example SSL), which can affect the time it takes for pages to render. The performance of the web page can be improved through techniques such as multi-layered cache, light weight design of presentation layer components and asynchronous communication with server side components.

## History

In the first decade or so of the web's existence, web performance improvement was focused mainly on optimizing website code and pushing hardware limitations. According to the 2002 book *Web Performance Tuning* by Patrick Killelea, some of the early techniques used were to use simple servlets or CGI, increase server memory, and look for packet loss and retransmission. Although these principles now comprise much of the optimized foundation of internet applications, they differ from current optimization theory in that there was much less of an attempt to improve the browser display speed.

Steve Souders coined the term "web performance optimization" in 2004. At that time Souders made several predictions regarding the impact that WPO as an "emerging industry" would bring to the web, such as websites being fast by default, consolidation, web standards for performance, environmental impacts of optimization, and speed as a differentiator.

One major point that Souders made in 2007 is that at least 80% of the time that it takes to download and view a website is controlled by the front-end structure. This lag time can be decreased through awareness of typical browser behavior, as well as of how HTTP works.

## Optimization techniques

Web performance optimization improves user experience (UX) when visiting a website and therefore is highly desired by web designers and web developers. They employ several techniques that streamline web optimization tasks to decrease web page load times. This process is known as front end optimization (FEO) or content optimization. FEO concentrates on reducing file sizes and "minimizing the number of requests needed for a given page to load."

In addition to the techniques listed below, the use of a content delivery network—a group of proxy servers spread across various locations around the globe—is an efficient delivery system that chooses a server for a specific user based on network proximity. Typically the server with the quickest response time is selected.

The following techniques are commonly used web optimization tasks and are widely used by web developers:

Web browsers open separate Transmission Control Protocol (TCP) connections for each Hypertext Transfer Protocol (HTTP) request submitted when downloading a web page. These requests total the number of page elements required for download. However, a browser is limited to opening only a certain number of simultaneous connections to a single host. To prevent bottlenecks, the number of individual page elements are reduced using resource consolidation whereby smaller files (such as images) are bundled together into one file. This reduces HTTP requests and the number of "round trips" required to load a web page.

Web pages are constructed from code files such JavaScript and Hypertext Markup Language (HTML). As web pages grow in complexity, so do their code files and subsequently their load times. File compression can reduce code files by about 40 percent, thereby improving site responsiveness.

Web Caching Optimization reduces server load, bandwidth usage and latency. CDNs use dedicated web caching software to store copies of documents passing through their system. Many website platforms, such as SiteGround, IONOS, Wix, and Hostinger, rely on global CDNs and caching technologies to deliver faster page loads across different geographical regions.

Subsequent requests from the cache may be fulfilled should certain conditions apply. Web caches are located on either the client side (forward position) or web-server side (reverse position) of a CDN. Web browsers are also able to store content for re-use through the HTTP cache or web cache. Requests web browsers make are typically routed to the HTTP cache to validate if a cached response may be used to fulfill a request. If such a match is made, the response is fulfilled from the cache. This can be helpful for reducing network latency and costs associated with data-transfer. The HTTP cache is configured using request and response headers.

Code minification distinguishes discrepancies between codes written by web developers and how network elements interpret code. Minification removes comments and extra spaces as well as crunch variable names in order to minimize code, decreasing files sizes by as much as 60%. In addition to caching and compression, lossy compression techniques (similar to those used with audio files) remove non-essential header information and lower original image quality on many high resolution images. These changes, such as pixel complexity or color gradations, are transparent to the end-user and do not noticeably affect perception of the image. Another technique is the replacement of raster graphics with resolution-independent vector graphics. Vector substitution is best suited for simple geometric images.

Lazy loading of images and video reduces initial page load time, initial page weight, and system resource usage, all of which have positive impacts on website performance. It is used to defer initialization of an object right until the point at which it is needed. The browser loads the images in a page or post when they are needed such as when the user scrolls down the page and not all images at once, which is the default behavior, and naturally, takes more time.

## HTTP/1.x and HTTP/2

Since web browsers use multiple TCP connections for parallel user requests, congestion and browser monopolization of network resources may occur. Because HTTP/1 requests come with associated overhead, web performance is impacted by limited bandwidth and increased usage.

Compared to HTTP/1, HTTP/2

- is binary instead of textual
- is fully multiplexed instead of ordered and blocked
- can therefore use one connection for parallelism
- uses header compression to reduce overhead
- allows servers to "push" responses proactively into client caches

Instead of a website's hosting server, CDNs are used in tandem with HTTP/2 in order to better serve the end-user with web resources such as images, JavaScript files and Cascading Style Sheet (CSS) files since a CDN's location is usually in closer proximity to the end-user.

## Metrics

In recent years, several metrics have been introduced that help developers measure various aspects of the performance of their websites. In 2019, Google introduced metrics such as Time to First Byte (TTFB), First Contentful Paint (FCP), First Paint (FP), First Input Delay (FID), Cumulative Layout Shift (CLS) and Largest Contentful Paint (LCP) allow for website owner to gain insights into issues that might hurt the performance of their websites making it seem sluggish or slow to the user. Other metrics including Request Count (number of requests required to load a page), DOMContentLoaded (time when HTML document is completely loaded and parsed excluding CSS style sheets, images, etc.), Above The Fold Time (content that is visible without scrolling), Round Trip Time, number of Render Blocking Resources (such as scripts, stylesheets), Onload Time, Connection Time, Total Page Size help provide an accurate picture of latencies and slowdowns occurring at the networking level which might slow down a site.

Modules to measure metrics such as TTFB, FCP, LCP, FP etc are provided with major frontend JavaScript libraries such as React, NuxtJS and Vue. Google publishes a library, the core-web-vitals library that allows for easy measurement of these metrics in frontend applications. In addition to this, Google also provides the Lighthouse, a Chrome dev-tools component and PageSpeed Insight a site that allows developers to measure and compare the performance of their website with Google's recommended minimums and maximums.

In addition to this, tools such as the Network Monitor by Mozilla Firefox help provide insight into network-level slowdowns that might occur during transmission of data.
