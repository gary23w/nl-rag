---
title: "Scala (programming language) (part 2/2)"
source: https://en.wikipedia.org/wiki/Scala_(programming_language)
domain: finatra-scala
license: CC-BY-SA-4.0
tags: finatra scala framework, twitter finagle services, scala services framework, finatra dependency injection
fetched: 2026-07-02
part: 2/2
---

## Comparison with other JVM languages

Scala is often compared with Groovy and Clojure, two other programming languages also using the JVM. Substantial differences between these languages exist in the type system, in the extent to which each language supports object-oriented and functional programming, and in the similarity of their syntax to that of Java.

Scala is statically typed, while both Groovy and Clojure are dynamically typed. This makes the type system more complex and difficult to understand but allows almost all type errors to be caught at compile-time and can result in significantly faster execution. By contrast, dynamic typing requires more testing to ensure program correctness, and thus is generally slower, to allow greater programming flexibility and simplicity. Regarding speed differences, current versions of Groovy and Clojure allow optional type annotations to help programs avoid the overhead of dynamic typing in cases where types are practically static. This overhead is further reduced when using recent versions of the JVM, which has been enhanced with an *invoke dynamic* instruction for methods that are defined with dynamically typed arguments. These advances reduce the speed gap between static and dynamic typing, although a statically typed language, like Scala, is still the preferred choice when execution efficiency is very important.

Regarding programming paradigms, Scala inherits the object-oriented model of Java and extends it in various ways. Groovy, while also strongly object-oriented, is more focused in reducing verbosity. In Clojure, object-oriented programming is deemphasised with functional programming being the main strength of the language. Scala also has many functional programming facilities, including features found in advanced functional languages like Haskell, and tries to be agnostic between the two paradigms, letting the developer choose between the two paradigms or, more frequently, some combination thereof.

Regarding syntax similarity with Java, Scala inherits much of Java's syntax, as is the case with Groovy. Clojure on the other hand follows the Lisp syntax, which is different in both appearance and philosophy.


## Adoption

### Language rankings

Back in 2013, when Scala was in version 2.10, the ThoughtWorks Technology Radar, which is an opinion based biannual report of a group of senior technologists, recommended Scala adoption in its languages and frameworks category.

In July 2014, this assessment was made more specific and now refers to a “Scala, the good parts”, which is described as “To successfully use Scala, you need to research the language and have a very strong opinion on which parts are right for you, creating your own definition of Scala, the good parts.”.

In the 2018 edition of the *State of Java* survey, which collected data from 5160 developers on various Java-related topics, Scala places third in terms of use of alternative languages on the JVM. Relative to the prior year's edition of the survey, Scala's use among alternative JVM languages fell from 28.4% to 21.5%, overtaken by Kotlin, which rose from 11.4% in 2017 to 28.8% in 2018. The Popularity of Programming Language Index, which tracks searches for language tutorials, ranked Scala 15th in April 2018 with a small downward trend, and 17th in Jan 2021. This makes Scala the 3rd most popular JVM-based language after Java and Kotlin, ranked 12th.

The RedMonk Programming Language Rankings, which establishes rankings based on the number of GitHub projects and questions asked on Stack Overflow, in January 2021 ranked Scala 14th. Here, Scala was placed inside a second-tier group of languages–ahead of Go, PowerShell, and Haskell, and behind Swift, Objective-C, TypeScript, and R.

The TIOBE index of programming language popularity employs internet search engine rankings and similar publication counting to determine language popularity. In September 2021, it showed Scala in 31st place. In this ranking, Scala was ahead of Haskell (38th) and Erlang, but below Go (14th), Swift (15th), and Perl (19th).

As of 2022, JVM-based languages such as Clojure, Groovy, and Scala are highly ranked, but still significantly less popular than the original Java language, which is usually ranked in the top three places.

### Companies

- In April 2009, Twitter announced that it had switched large portions of its backend from Ruby to Scala and intended to convert the rest.
- Tesla, Inc. uses Akka with Scala in the backend of the Tesla Virtual Power Plant. Thereby, the Actor model is used for representing and operating devices that together with other components make up an instance of the virtual power plant, and Reactive Streams are used for data collection and data processing.
- Apache Kafka is implemented in Scala with regards to most of its core and other critical parts. It is maintained and extended through the open source project and by the company Confluent.
- Gilt uses Scala and Play Framework.
- Foursquare uses Scala and Lift.
- Coursera uses Scala and Play Framework.
- Apple Inc. uses Scala in certain teams, along with Java and the Play framework.
- *The Guardian* newspaper's high-traffic website guardian.co.uk announced in April 2011 that it was switching from Java to Scala.
- *The New York Times* revealed in 2014 that its internal content management system *Blackbeard* is built using Scala, Akka, and Play.
- The *Huffington Post* newspaper started to employ Scala as part of its content delivery system *Athena* in 2013.
- Swiss bank UBS approved Scala for general production use.
- LinkedIn uses the Scalatra microframework to power its Signal API.
- Meetup uses Unfiltered toolkit for real-time APIs.
- Remember the Milk uses Unfiltered toolkit, Scala and Akka for public API and real-time updates.
- Verizon seeking to make "a next-generation framework" using Scala.
- Airbnb develops open-source machine-learning software "Aerosolve", written in Java and Scala.
- Zalando moved its technology stack from Java to Scala and Play.
- SoundCloud uses Scala for its back-end, employing technologies such as Finagle (micro services), Scalding and Spark (data processing).
- Databricks uses Scala for the Apache Spark Big Data platform.
- Morgan Stanley uses Scala extensively in their finance and asset-related projects.
- There are teams within Google and Alphabet Inc. that use Scala, mostly due to acquisitions such as Firebase and Nest.
- Walmart Canada uses Scala for their back-end platform.
- Duolingo uses Scala for their back-end module that generates lessons.
- HMRC uses Scala for many UK Government tax applications.
- M1 Finance uses Scala for their back-end platform.
- Lichess uses Scala for their open-source platform core applications.


## Criticism

In November 2011, Yammer moved away from Scala for reasons that included the learning curve for new team members and incompatibility from one version of the Scala compiler to the next. In March 2015, former VP of the Platform Engineering group at Twitter Raffi Krikorian, stated that he would not have chosen Scala in 2011 due to its learning curve. The same month, LinkedIn SVP Kevin Scott stated their decision to "minimize [their] dependence on Scala".
