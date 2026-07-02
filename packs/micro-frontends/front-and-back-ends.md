---
title: "Front end and back end"
source: https://en.wikipedia.org/wiki/Front_and_back_ends
domain: micro-frontends
license: CC-BY-SA-4.0
tags: micro frontends, frontend composition, separation of concerns, iframe isolation boundary
fetched: 2026-07-02
---

# Front end and back end

(Redirected from

Front and back ends

)

In software development, **front end** refers to the presentation layer that users interact with, while **back end** refers to the data management and processing behind the scenes. "Full stack" refers to both together. In the client–server model, the client is usually considered the front end, handling most user-facing tasks, and the server is the back end, mainly managing data and logic.

## Introduction

In software architecture, there can be many layers between the hardware and end user. The *front end* is an abstraction, simplifying the underlying components by providing a user-friendly interface, while the *back end* handles data storage and business logic.

## Examples

**E-commerce Website**: The front end is the user interface (e.g., product pages, search bar), while the back end processes payments and updates inventory.

**Banking App**: The front end displays account balances, while the back end handles secure transactions and updates records.

**Social Media Platform**: The front end shows the news feed, while the back end stores posts and manages notifications.

In telecommunication, the front end can be considered a device or service, while the back end is the infrastructure that supports the provision of services.

A rule of thumb is that the front end, or client side, includes any components manipulated by the user. The back end, or server side, usually resides on the server, often far removed physically from the user.

## Software definitions

There are many different ways the terms 'front end' and 'back end' can be defined in the context of software. For example, in content management systems, the front end refers to views facing end users, and the back end refers to views facing administrative users. Similarly, within the field of speech synthesis, the front end refers to the part of the synthesis system that converts the input text into a symbolic phonetic representation, and the back end converts the symbolic phonetic representation into actual sounds. In programming language compilers, the front end translates computer source code into an intermediate representation, and the back end produces executable code from the intermediate representation. The back end usually optimizes to produce code that runs faster. The front end/back end distinction can also separate a parser that deals with source code from a compiler that generates and optimizes executable code. Some designs, such as GCC, offer multiple front end options (parsing different source languages) and multiple back end options (generating code for different target processors).

Some graphical user interface (GUI) applications act as a thin front end for underlying command-line interface (CLI) programs, to save users from having to learn the CLI terminology and commands.

### Web development as an example

Another way to understand the differences between the front end and back end is to consider the knowledge that each requires of a software developer. The example lists below focus on web development.

#### Front end

- Markup and web languages such as HTML, CSS, and JavaScript, as well as ancillary libraries commonly used in those languages, such as Sass or jQuery
- Asynchronous request handling and AJAX
- Single-page applications with frameworks like React, Angular or Vue.js
- Web performance (optimization of things like largest contentful paint, time to interactive, animation FPS, and memory usage)
- Responsive web design
- Cross-browser compatibility issues and workarounds
- End-to-end testing with a headless browser
- Build automation to transform and bundle JavaScript files, reduce image sizes, and handle other processes using tools such as Webpack and Gulp.js
- Search engine optimization
- Accessibility concerns
- Image editing tools such as GIMP or Photoshop
- User interface design and creation

#### Back end

- Scripting languages like PHP, Python, Ruby, Perl, and Node.js
- Compiled languages like C#, Java, and Go
- Data access layer
- Business logic
- Database administration
- Scalability
- High availability
- Security concerns, such as authentication and authorization
- Software architecture
- Data transformation
- Backup methods and software

#### Front end and back end

- Version control tools such as Git, Mercurial, and Subversion
- File transfer tools and protocols such as FTP and rsync

### API

The front end communicates with the back end through an API. In the case of web and mobile front ends, the API is often based on HTTP requests/responses. An API can also reduce the front-end processing load by using different back-end services for different front-end interfaces, such as in the "Back end For Front end" (BFF) pattern.

## Hardware definitions

In computer networking, *front end* can refer to hardware that connects devices to the network, provides security such as a DMZ, or converts data into a transportable format. *Back end* refers to hardware that handles and transports data within the network.

In processor design, *front-end design* can refer to the initial description of a circuit's behavior in a hardware description language such as Verilog, while *back-end design* can refer to the process of mapping that behavior to physical transistors on a die.
