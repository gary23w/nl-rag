---
title: "Doxygen"
source: https://en.wikipedia.org/wiki/Doxygen
domain: doxygen
license: CC-BY-SA-4.0
tags: doxygen docs, documentation generator, api documentation, source comments
fetched: 2026-07-02
---

# Doxygen

**Doxygen** (/ˈdɒksidʒən/ *DOK-see-jən*) is a documentation generator that works with many programming languages. It extracts information from specially-formatted source code comments and saves the information in one of various supported formats.

Doxygen supports static analysis of a codebase. It uses the parse tree parsed from the codebase to generate diagrams and charts of the code structure. It provides cross-referencing that a reader can use to refer back to the source code from the generated documentation.

Doxygen can be used in many programming contexts. It supports many languages including C, C++, C#, D, Fortran, IDL, Java, Objective-C, Perl, PHP, Python, and VHDL. It can run on many computers, including Unix-like, macOS, and Windows systems. It is free software, released under the terms of the GNU General Public License version 2 (GPLv2).

## History

The first version of Doxygen borrowed code from an early version of DOC++, developed by Roland Wunderling and Malte Zöckler at Zuse Institute Berlin. Later, the Doxygen code was rewritten by Dimitri van Heesch.

## Development

The Doxygen source code is hosted at GitHub, where the main developer, Dimitri van Heesch, contributes under the name "doxygen". Doxygen is written in C++, and consists of around 300,000 source lines of code. For lexical analysis, Lex (or its replacement Flex) is run via approximately 35,000 lines of lex script. The parsing tool Yacc (or its replacement Bison) is also used, but only for minor tasks. The bulk of parsing is done via native C++ code. The build system includes CMake and Python script.

## Design

Like other documentation generators such as Javadoc, Doxygen extracts information from both the comment and the symbolic (non-comment) code. A comment is associated with a programming symbol by immediately preceding it in the code. Markup in the comments allows for controlling inclusion and formatting of the resulting documentation.

Doxygen supports output in many formats including: HTML, CHM, RTF, PDF, LaTeX, PostScript and man page.

Doxygen can generate inheritance diagrams for C++ classes. For more advanced diagrams and graphs, Doxygen can use the "dot" tool from Graphviz.

## Example

All examples are given for languages with C-like comments where a multi-line comment starts with `/*` and a single line comment starts with `//`.

Doxygen ignores a comment unless it is marked specially. For a multi-line comment, the comment must start with `/**` or `/*!`. A markup tag is prefixed with a backslash (`\`) or an at-sign (`@`). The following is a relatively simple function comment block with markup in bold:

```
/**
 * Function description
 * @param p1 Parameter description
 * @param p2 Parameter description
 * @return Return description
 */
void foo(int p1, int p2) {}
```

A block can be formatted various ways. A common way is to left-align asterisks on each line which Doxygen does not include in the output. For example:

```
/**
 * Function description
 * @param p1 Parameter description
 * @param p2 Parameter description
 * @return Return description
 */
void foo(int p1, int p2) {}
```

Alternatively, a block can consist of a series of single-line comments. Doxygen accepts comments with an additional slash (`/`) or exclamation (`!`).

```
/// Function description
/// @param p1 Parameter description
/// @param p2 Parameter description
/// @return Return description
void foo(int p1, int p2) {}
```

To locate a documentation comment to the right of the code, an additional `<` marker is required. This allows for an alternative approach for documenting parameters as shown below.

```
/**
 * Function description
 */
void foo(int p1 /**<Parameter description*/, int p2 /**<Parameter description*/) {}
```

A mathematic formula can be specified via LaTeX commands. For example:

```mw
/**
 * An inline equation @f$ e^{\pi i}+1 = 0 @f$
 * A displayed equation: @f[ e^{\pi i}+1 = 0 @f]
 */
```

A more complete example in C++:

```mw
/**
 * @file Time.cpp
 * @module org.wikipedia.util.Time
 * @brief Time class
 * @author John Doe <jdoe@example.com>
 * @version 1.0
 * @copyright CC BY-SA or GFDL
 * @sa <a href="https://en.wikipedia.org/wiki/Wikipedia:Copyrights">Wikipedia:Copyrights - Wikipedia</a>
 */

export module org.wikipedia.util.Time;

import org.wikipedia.core;
import org.wikipedia.util.Date;

using org::wikipedia::core::ISerializable;

/**
 * @namespace org::wikipedia::util
 * @brief A namespace of utility classes
 */
export namespace org::wikipedia::util {

/**
 * @class Time
 * @brief Represents a moment of time
 * @author John Doe
 *
 * The class Time represents the amount of time elapsed
 * since the UNIX epoch.
 *
 * @extends Date
 * @implements ISerializiable
 */
class Time : public Date, public ISerializable {
private:
    int64_t millis; ///< Milliseconds since Jan 1, 1970
public:
    /**
     * Construct a new Time with a duration since 1 January 1970
     * @param millis A number of milliseconds
     */
    explicit Time(int64_t millis): 
        millis{millis} {}

    /**
     * Get a new instance with the current time
     * @return Instance
     */
    [[nodiscard]]
    static Time now() {
        // ...
    }

    /**
     * Get the number of milliseconds represented by a Time object
     * @return The int64_t representing the number of milliseconds
     */
    [[nodiscard]]
    int64_t getTime() const noexcept {
        return millis;
    }
};

}
```
