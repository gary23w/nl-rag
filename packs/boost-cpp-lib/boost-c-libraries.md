---
title: "Boost (C++ libraries)"
source: https://en.wikipedia.org/wiki/Boost_(C%2B%2B_libraries)
domain: boost-cpp-lib
license: CC-BY-SA-4.0
tags: boost libraries, cpp peer-reviewed library, boost header only, boost smart pointers
fetched: 2026-07-02
---

# Boost (C++ libraries)

The **Boost C++ Libraries** (also known simply as **Boost**) are a set of libraries for the C++ programming language that provides support for tasks and structures such as linear algebra, pseudorandom number generation, multithreading, image processing, regular expressions, and unit testing. It currently contains 170 individual libraries.

All of the Boost libraries are licensed under the Boost Software License, designed to allow Boost to be used with both free and proprietary software projects. Boost is used complementary with the C++ Standard Library to supplement its features. Many of Boost's founders are on the C++ standards committee, and several Boost libraries have been accepted for incorporation into the C++ Technical Report 1, the C++11 standard (e.g. smart pointers, threads, regular expressions, random number generation, rational arithmetic (ratio), tuples) and the C++17 standard (e.g. file system API, any types, option types, variant types, and string views).

The Boost community emerged around 1998, when the first version of the standard was released. It has grown continuously since then and now plays a big role in the standardization of C++. Even though there is no formal relationship between the Boost community and the standardization committee, some of the developers are active in both groups.

## Design

The libraries are aimed at a wide range of C++ users and application domains. They range from general-purpose libraries like the smart pointer library, to operating system abstractions like *Boost FileSystem*, to libraries primarily aimed at other library developers and advanced C++ users, like the template metaprogramming (MPL) and domain-specific language (DSL) creation (Proto).

In order to ensure efficiency and flexibility, Boost makes extensive use of templates. Boost has been a source of extensive work and research into generic programming and metaprogramming in C++.

Most Boost libraries are header based, consisting of inline functions and templates, and as such do not need to be built in advance of their use. Some Boost libraries coexist as independent libraries. Some Boost libraries, such as `boost.regex`, are offered as modules, as the rest of the library begins to support modules.

## Associated people

Boost was founded in 1998 by three members of the C++ Standards Committee: Beman Dawes, David Abrahams, and Robert Klarer. The idea originated during a conversation between Klarer and Dawes at the March 1998 C++ Standards Committee meeting in Sophia Antipolis, France, with Abrahams joining shortly thereafter to establish the first Boost mailing list.*"History of Boost". *Boost Site Docs*. The C++ Alliance. Retrieved 26 January 2026.**Stroustrup, Bjarne; Sutter, Herb (1 December 2020). "Remembering Beman Dawes". *Standard C++*. Retrieved 26 January 2026.*

Beman Dawes (died December 2020) served on the C++ Standards Committee (WG21) from 1992 and chaired the Library Working Group for five years during the completion of C++98.*Stroustrup, Bjarne; Sutter, Herb (1 December 2020). "Remembering Beman Dawes". *Standard C++*. Retrieved 26 January 2026.* He was the original author of the Boost.Filesystem library, which later formed the basis for the std::filesystem library in C++17. Dawes was instrumental in establishing Boost's peer-review process and testing culture.*"History of Boost". *Boost Site Docs*. The C++ Alliance. Retrieved 26 January 2026.*

David Abrahams was a member of the C++ Standards Committee from 1996 to 2012 and is known for developing the theory of exception safety for C++, including the "Abrahams guarantees" framework.*"David Abrahams (computer programmer)". *Wikipedia*. Retrieved 26 January 2026.* He authored multiple Boost libraries including Boost.Python and co-authored the book *C++ Template Metaprogramming* (2004). In 2001, Abrahams founded Boost Consulting (later BoostPro Computing) to provide commercial support for Boost libraries.*"David Abrahams (computer programmer)". *Wikipedia*. Retrieved 26 January 2026.*

Robert Klarer, working at IBM, co-initiated the Boost concept with Dawes and contributed to early discussions on best practices for high-quality library development.*"History of Boost". *Boost Site Docs*. The C++ Alliance. Retrieved 26 January 2026.**Falco, Vinnie (8 May 2023). "The Future of Boost". *The C++ Alliance*. Retrieved 26 January 2026.* There are mailing lists devoted to Boost library use and library development, active as of 2023.

## License

Boost is licensed under its own free, open-source license, known as the Boost Software License. It is a permissive license in the style of the BSD license and the MIT license, but without requiring attribution for redistribution in binary form. The license has been OSI-approved since February 2008 and is considered a free software license, compatible with the GNU General Public License, by the Free Software Foundation.
