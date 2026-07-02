---
title: "JavaScript library"
source: https://en.wikipedia.org/wiki/JavaScript_library
domain: storybook
license: CC-BY-SA-4.0 / MIT (storybook.js.org)
tags: storybook ui, component explorer, ui component stories, isolated component development
fetched: 2026-07-02
---

# JavaScript library

A **JavaScript library** is a library of pre-written JavaScript code that allows for easier development of JavaScript-based applications, especially for AJAX and other web-centric technologies. They can be included in a website by embedding it directly in the HTML via a script tag.

## Libraries

With the expanded demands for JavaScript, an easier means for programmers to develop such dynamic interfaces was needed. Thus, JavaScript libraries and JavaScript widget libraries were developed, allowing for developers to concentrate more upon more distinctive applications of Ajax. This has led to other companies and groups, such as Microsoft and Yahoo! developing their own JavaScript-based user interface libraries, which find their way into the web applications developed by these companies. Some JavaScript libraries allow for easier integration of JavaScript with other web development technologies, such as CSS, PHP, Ruby, and Java, while others provide utilities, often in the form of JavaScript functions, to make repetitive and complex tasks less taxing. Many libraries include code to detect differences between runtime environments and remove the need for applications to allow for such inconsistencies.

Almost all JavaScript libraries are released under either a permissive or copyleft license to ensure license-free distribution, usage, and modification.

## Frameworks

Some JavaScript libraries, such as Angular, are classified as frameworks since they exhibit full-stack capabilities and properties not found in general JavaScript libraries.

### Capabilities and Trade-offs in Modern Frameworks

JavaScript-based web application frameworks, such as React and Vue, provide extensive capabilities but come with associated trade-offs. These frameworks often extend or enhance features available through native web technologies, such as routing, component-based development, and state management. While native web standards, including Web Components, modern JavaScript APIs like Fetch and ES Modules, and browser capabilities like Shadow DOM, have advanced significantly, frameworks remain widely used for their ability to enhance developer productivity, offer structured patterns for large-scale applications, simplify handling edge cases, and provide tools for performance optimization.

Frameworks can introduce abstraction layers that may contribute to performance overhead, larger bundle sizes, and increased complexity. Modern frameworks, such as React 18 and Vue 3, address these challenges with features like concurrent rendering, tree-shaking, and selective hydration. While these advancements improve rendering efficiency and resource management, their benefits depend on the specific application and implementation context.

Lightweight frameworks, such as Svelte and Preact, take different architectural approaches, with Svelte eliminating the virtual DOM entirely in favor of compiling components to efficient JavaScript code, and Preact offering a minimal, compatible alternative to React. Framework choice depends on an application’s requirements, including the team’s expertise, performance goals, and development priorities.

A newer category of web frameworks, including enhance.dev, Astro, and Fresh, leverages native web standards while minimizing abstractions and development tooling. These solutions emphasize progressive enhancement, server-side rendering, and optimizing performance. Astro renders static HTML by default while hydrating only interactive parts. Fresh focuses on server-side rendering with zero runtime overhead. Enhance.dev prioritizes progressive enhancement patterns using Web Components. While these tools reduce reliance on client-side JavaScript by shifting logic to build-time or server-side execution, they still use JavaScript where necessary for interactivity. This approach makes them particularly suitable for performance-critical and content-focused applications.

## Packages

All npm packages are JavaScript libraries, but not all libraries are packages. Npm serves as a package manager for packages used in Node.js runtimes. However, some npm packages offer CDN support for use of the library in both Node.js runtimes as well as the browser.
