---
title: "Doxygen: Special Commands (part 1/3)"
source: https://www.doxygen.nl/manual/commands.html
domain: doxygen
license: CC-BY-SA-4.0
tags: doxygen docs, documentation generator, api documentation, source comments
fetched: 2026-07-02
part: 1/3
---

# Introduction

All commands in the documentation start with a backslash (**\**) or an at-sign (**@**). If you prefer you can replace all commands starting with a backslash below by their counterparts that start with an at-sign.

Some commands have one or more arguments. Each argument has a certain range:

- If <sharp> braces are used the argument is a single word.
- If (round) braces are used the argument extends until the end of the line on which the command was found.
- If {curly} braces are used the argument extends until the next paragraph. Paragraphs are delimited by a blank line or by a section indicator. Note that {curly} braces are also used for command options, here the braces are mandatory and just 'normal' characters. The starting curly brace has to directly follow the command, so without whitespace.

If in addition to the above argument specifiers [square] brackets are used the argument is optional, unless they are placed between quotes in that case they are a mandatory part of the command argument.

Here is an alphabetically sorted list of all commands with references to their documentation:

- \a
- \addindex
- \addtogroup
- \anchor
- \arg
- \attention
- \author
- \authors
- \b
- \brief
- \bug
- \c
- \callergraph
- \callgraph
- \category
- \cite
- \class
- \code
- \collaborationgraph
- \concept
- \cond
- \copybrief
- \copydetails
- \copydoc
- \copyright
- \date
- \def
- \defgroup
- \deprecated
- \details
- \diafile
- \dir
- \directorygraph
- \docbookinclude
- \docbookonly
- \dontinclude
- \dot
- \dotfile
- \doxyconfig
- \e
- \else
- \elseif
- \em
- \emoji
- \endcode
- \endcond
- \enddocbookonly
- \enddot
- \endhtmlonly
- \endif
- \endinternal
- \endlatexonly
- \endlink
- \endmanonly
- \endmermaid
- \endmsc
- \endparblock
- \endrtfonly
- \endsecreflist
- \endverbatim
- \enduml
- \endxmlonly
- \enum
- \example
- \exception
- \extends
- \f(
- \f)
- \f$
- \f[
- \f]
- \f{
- \f}
- \file
- \fileinfo
- \fn
- \groupgraph
- \headerfile
- \hidecallergraph
- \hidecallgraph
- \hidecollaborationgraph
- \hidedirectorygraph
- \hideenumvalues
- \hidegroupgraph
- \hideincludedbygraph
- \hideincludegraph
- \hideinheritancegraph
- \hideinlinesource
- \hiderefby
- \hiderefs
- \hideinitializer
- \htmlinclude
- \htmlonly
- \idlexcept
- \if
- \ifnot
- \image
- \implements
- \important
- \include
- \includedoc
- \includedbygraph
- \includegraph
- \includelineno
- \ingroup
- \inheritancegraph
- \internal
- \invariant
- \interface
- \latexinclude
- \latexonly
- \li
- \line
- \lineinfo
- \link
- \mainpage
- \maninclude
- \manonly
- \memberof
- \mermaid
- \mermaidfile
- \module
- \msc
- \mscfile
- \n
- \name
- \namespace
- \noop
- \nosubgrouping
- \note
- \overload
- \p
- \package
- \page
- \par
- \paragraph
- \param
- \parblock
- \post
- \pre
- \private
- \privatesection
- \property
- \protected
- \protectedsection
- \protocol
- \public
- \publicsection
- \pure
- \qualifier
- \raisewarning
- \ref
- \refitem
- \related
- \relates
- \relatedalso
- \relatesalso
- \remark
- \remarks
- \requirement
- \result
- \return
- \returns
- \retval
- \rtfinclude
- \rtfonly
- \sa
- \satisfies
- \secreflist
- \section
- \see
- \short
- \showdate
- \showenumvalues
- \showinitializer
- \showinlinesource
- \showrefby
- \showrefs
- \since
- \skip
- \skipline
- \snippet
- \snippetdoc
- \snippetlineno
- \static
- \startuml
- \struct
- \subpage
- \subparagraph
- \subsection
- \subsubparagraph
- \subsubsection
- \tableofcontents
- \test
- \throw
- \throws
- \todo
- \tparam
- \typedef
- \plantumlfile
- \union
- \until
- \var
- \verbatim
- \verbinclude
- \verifies
- \version
- \vhdlflow
- \warning
- \weakgroup
- \xmlinclude
- \xmlonly
- \xrefitem
- \$
- \@
- \\
- \&
- \~
- \<
- \=
- \>
- \#
- \%
- \"
- \.
- \?
- \!
- \::
- \|
- \--
- \---

The following subsections provide a list of all commands that are recognized by Doxygen. Unrecognized commands are treated as normal text.


## --- Structural indicators ---

# \addtogroup <name> [(title)]

Defines a group just like \defgroup, but in contrast to that command using the same <name> more than once will not result in a warning, but rather one group with a merged documentation and the first title found in any of the commands.

The title is optional, so this command can also be used to add a number of entities to an existing group using `@{` and `@}` like this:

```
  /*! \addtogroup mygrp
   *  Additional documentation for group 'mygrp'
   *  @{
   */

  /*!
   *  A function
   */
  void func1()
  {
  }

  /*! Another function */
  void func2()
  {
  }

  /*! @} */
```

**See also**

page

Grouping

, sections

\defgroup

,

\ingroup

, and

\weakgroup

.

# \callgraph

When this command is put in a comment block of a function or method and HAVE_DOT is set to `YES`, then Doxygen will generate a call graph for that function (provided the implementation of the function or method calls other documented functions). The call graph will be generated regardless of the value of CALL_GRAPH.

**Note**

The completeness (and correctness) of the call graph depends on the Doxygen code parser which is not perfect.

**See also**

section

\callergraph

, section

\hidecallgraph

, section

\hidecallergraph

and option

CALL_GRAPH

# \hidecallgraph

When this command is put in a comment block of a function or method and then Doxygen will not generate a call graph for that function. The call graph will not be generated regardless of the value of CALL_GRAPH.

**Note**

The completeness (and correctness) of the call graph depends on the Doxygen code parser which is not perfect.

**See also**

section

\callergraph

, section

\callgraph

, section

\hidecallergraph

and option

CALL_GRAPH

# \callergraph

When this command is put in a comment block of a function or method and HAVE_DOT is set to `YES`, then Doxygen will generate a caller graph for that function (provided the implementation of the function or method is called by other documented functions). The caller graph will be generated regardless of the value of CALLER_GRAPH.

**Note**

The completeness (and correctness) of the caller graph depends on the Doxygen code parser which is not perfect.

**See also**

section

\callgraph

, section

\hidecallgraph

, section

\hidecallergraph

and option

CALLER_GRAPH

# \hidecallergraph

When this command is put in a comment block of a function or method and then Doxygen will not generate a caller graph for that function. The caller graph will not be generated regardless of the value of CALLER_GRAPH.

**Note**

The completeness (and correctness) of the caller graph depends on the Doxygen code parser which is not perfect.

**See also**

section

\callergraph

, section

\callgraph

, section

\hidecallgraph

and option

CALLER_GRAPH

# \showrefby

When this command is put in a comment block of a function, method or variable, then Doxygen will generate an overview for that function, method, variable of the, documented, functions and methods that call / use it. The overview will be generated regardless of the value of REFERENCED_BY_RELATION.

**Note**

The completeness (and correctness) of the overview depends on the Doxygen code parser which is not perfect.

**See also**

section

\showrefs

, section

\hiderefby

, section

\hiderefs

and option

REFERENCED_BY_RELATION

# \hiderefby

When this command is put in a comment block of a function, method or variable then Doxygen will not generate an overview for that function, method or variable of the functions and methods that call / use it. The overview will not be generated regardless of the value of REFERENCED_BY_RELATION.

**Note**

The completeness (and correctness) of the overview depends on the Doxygen code parser which is not perfect.

**See also**

section

\showrefs

, section

\showrefby

, section

\hiderefs

and option

REFERENCED_BY_RELATION

# \showrefs

When this command is put in a comment block of a function or method, then Doxygen will generate an overview for that function or method of the functions and methods that call it. The overview will be generated regardless of the value of REFERENCES_RELATION.

**Note**

The completeness (and correctness) of the overview depends on the Doxygen code parser which is not perfect.

**See also**

section

\showrefby

, section

\hiderefby

, section

\hiderefs

and option

REFERENCES_RELATION

# \hiderefs

When this command is put in a comment block of a function or method and then Doxygen will not generate an overview for that function or method of the functions and methods that call it. The overview will not be generated regardless of the value of REFERENCES_RELATION.

**Note**

The completeness (and correctness) of the overview depends on the Doxygen code parser which is not perfect.

**See also**

section

\showrefs

, section

\showrefby

, section

\hiderefby

and option

REFERENCES_RELATION

# \showinlinesource

When this command is put in a comment block of a function, multi-line macro, enum or a list initialized variable then Doxygen will generate the inline source for that member. The inline source will be generated regardless of the value of INLINE_SOURCES.

**See also**

section

\hideinlinesource

, option

INLINE_SOURCES

# \hideinlinesource

When this command is put in a comment block of a function, multi-line macro, enum or a list initialized variable then Doxygen will not generate the inline source for that member. The inline source will not be generated regardless of the value of INLINE_SOURCES.

**See also**

section

\showinlinesource

, option

INLINE_SOURCES

# \includegraph

When this command is put in a comment block of a file then Doxygen will generate an include graph for that file. The include graph will be generated regardless of the value of INCLUDE_GRAPH.

**See also**

section

\hideincludegraph

, section

\includedbygraph

, section

\hideincludedbygraph

and option

INCLUDE_GRAPH

# \hideincludegraph

When this command is put in a comment block of a file then Doxygen will not generate an include graph for that file. The include graph will not be generated regardless of the value of INCLUDE_GRAPH.

**See also**

section

\includegraph

, section

\includedbygraph

, section

\hideincludedbygraph

and option

INCLUDE_GRAPH

# \includedbygraph

When this command is put in a comment block of an include file then Doxygen will generate an included by graph for that include file. The included by graph will be generated regardless of the value of INCLUDED_BY_GRAPH.

**See also**

section

\hideincludedbygraph

, section

\ncludegraph

, section

\hideincludegraph

and option

INCLUDED_BY_GRAPH

# \hideincludedbygraph

When this command is put in a comment block of an include file then Doxygen will not generate an included by graph for that include file. The included by graph will not be generated regardless of the value of INCLUDED_BY_GRAPH.

**See also**

section

\includedbygraph

, section

\ncludegraph

, section

\hideincludegraph

and option

INCLUDED_BY_GRAPH

# \directorygraph

When this command is put in a comment block of a directory (see section \dir) then Doxygen will generate a directory graph for that directory. The directory graph will be generated regardless of the value of DIRECTORY_GRAPH.

**See also**

section

\hidedirectorygraph

, option

DIRECTORY_GRAPH

# \hidedirectorygraph

When this command is put in a comment block of a directory (see section \dir) then Doxygen will not generate a directory graph for that directory. The directory graph will not be generated regardless of the value of DIRECTORY_GRAPH.

**See also**

section

\directorygraph

, option

DIRECTORY_GRAPH

# \collaborationgraph

When this command is put in a comment block of a class then Doxygen will generate a collaboration graph for that class. The collaboration graph will be generated regardless of the value of COLLABORATION_GRAPH.

**See also**

section

\hidecollaborationgraph

, option

COLLABORATION_GRAPH

# \hidecollaborationgraph

When this command is put in a comment block of a class then Doxygen will not generate a collaboration graph for that class. The collaboration graph will not be generated regardless of the value of COLLABORATION_GRAPH.

**See also**

section

\collaborationgraph

, option

COLLABORATION_GRAPH

# \inheritancegraph['{option}']

When this command is put in a comment block of a class then Doxygen will generate an inheritance graph for that class conforming the option. The inheritance graph will be generated, conforming the option, regardless of the value of CLASS_GRAPH. The possible values of option are the same values as can be used with CLASS_GRAPH. In case no option is specified the value YES is assumed.

**See also**

section

\hideinheritancegraph

, option

CLASS_GRAPH

# \hideinheritancegraph

When this command is put in a comment block of a class then Doxygen will not generate an inheritance graph for that class. The inheritance graph will not be generated regardless of the value of CLASS_GRAPH.

**See also**

section

\inheritancegraph

, option

CLASS_GRAPH

# \groupgraph

When this command is put in a comment block of a \defgroup command then Doxygen will generate a group dependency graph for that group. The group graph will be generated regardless of the value of GROUP_GRAPHS.

**See also**

section

\hidegroupgraph

, option

GROUP_GRAPHS

# \hidegroupgraph

When this command is put in a comment block of a \defgroup command then Doxygen will not generate a group dependency graph for that group. The group graph will not be generated regardless of the value of GROUP_GRAPHS.

**See also**

section

\groupgraph

, option

GROUP_GRAPHS

# \showenumvalues

When this command is put in a comment block of an enum then doxygen will show the specified enum values for that enum, regardless of the value of SHOW_ENUM_VALUES.

**See also**

section

\hideenumvalues

, option

SHOW_ENUM_VALUES

# \hideenumvalues

When this command is put in a comment block of an enum then doxygen will not show the specified enum values for that enum, regardless of the value of SHOW_ENUM_VALUES.

**See also**

section

\showenumvalues

, option

SHOW_ENUM_VALUES

# \qualifier <label> | "(text)"

With this command it is possible to add custom qualifier labels to members and classes. These labels will be shown in the output in the same way as the automatically generated labels such as "static", "inline", and "final".

For instance to indicate that a function is only meant for testing purposes one could add \qualifier test

# \category <name> [<header-file>] [<header-name>]

For Objective-C only: Indicates that a comment block contains documentation for a class category with name <name>. The arguments are equal to the \class command.

**See also**

section

\class

.

# \class <name> [<header-file>] [<header-name>]

Indicates that a comment block contains documentation for a class with name <name>. Optionally a header file and a header name can be specified. If the header-file is specified, a link to a verbatim copy of the header will be included in the HTML documentation. The <header-name> argument can be used to overwrite the name of the link that is used in the class documentation to something other than <header-file>. This can be useful if the include name is not located on the default include path (like <X11/X.h>). With the <header-name> argument you can also specify how the include statement should look like, by adding either quotes or sharp brackets around the name. Sharp brackets are used if just the name is given. Note that the last two arguments can also be specified using the \headerfile command.

**Example:**

class

Test

{

};

Click

here

for the corresponding HTML documentation that is generated by Doxygen.

# \concept <name>

Indicates that a comment block contains documentation for a C++20 concept with name <name>. See also the \headerfile command to specify the header a user should be included to use the concept.

# \def <name>

Indicates that a comment block contains documentation for a `#define` macro.

**Example:**

#define ABS(x) (((x)>0)?(x):-(x))

#define MAX(x,y) ((x)>(y)?(x):(y))

#define MIN(x,y) ((x)>(y)?(y):(x))

Click

here

for the corresponding HTML documentation that is generated by Doxygen.

# \defgroup <name> (group title)

Indicates that a comment block contains documentation for a topics of classes, modules, concepts, files or namespaces. This can be used to categorize symbols, and document those categories. You can also use groups as members of other groups, thus building a hierarchy of groups.

The <name> argument should be a single-word identifier.

**See also**

page

Grouping

, sections

\ingroup

,

\addtogroup

, and

\weakgroup

.

# \dir [<path fragment>]

Indicates that a comment block contains documentation for a directory. The "path fragment" argument should include the directory name and enough of the path to be unique with respect to the other directories in the project. The STRIP_FROM_PATH option determines what is stripped from the full path before it appears in the output.

# \enum <name>

Indicates that a comment block contains documentation for an enumeration, with name <name>. If the enum is a member of a class and the documentation block is located outside the class definition, the scope of the class should be specified as well. If a comment block is located directly in front of an enum declaration, the `\enum` comment may be omitted.

**Note:**

The type of an anonymous enum cannot be documented, but the values of an anonymous enum can.

**Example:**

class

Enum_Test

{

public

:

enum

TEnum { Val1, Val2 };

enum

AnotherEnum

{

V1,

V2

};

};

Click

here

for the corresponding HTML documentation that is generated by Doxygen.

# \example['{lineno}'] <file-name>

Indicates that a comment block contains documentation for a source code example. The name of the source file is <file-name>. The contents of this file will be included in the documentation, just after the documentation contained in the comment block. You can add option {lineno} to enable line numbers for the example if desired. All examples are placed in a list. The source code is scanned for documented members and classes. If any are found, the names are cross-referenced with the documentation. Source files or directories can be specified using the EXAMPLE_PATH tag of Doxygen's configuration file.

If <file-name> itself is not unique for the set of example files specified by the EXAMPLE_PATH tag, you can include part of the absolute path to disambiguate it.

If more than one source file is needed for the example, the \include command can be used.

**Example:**

class

Example_Test

{

public

:

void

example();

};

void

Example_Test::example() {}

Where the example file

example_test.cpp

looks as follows:

void

main()

{

Example_Test t;

t.example();

}

Click

here

for the corresponding HTML documentation that is generated by Doxygen.

**See also**

section

\include

.

# \endinternal

This command ends a documentation fragment that was started with a \internal command. The text between \internal and `\endinternal` will only be visible if INTERNAL_DOCS is set to `YES`.

# \extends <name>

This command can be used to manually indicate an inheritance relation, when the programming language does not support this concept natively (e.g. C).

The file `manual.c` in the example directory shows how to use this command (see also \memberof for the complete file).

Click here for the corresponding HTML documentation that is generated by Doxygen.

**See also**

section

\implements

and section

\memberof

# \file [<name>]

Indicates that a comment block contains documentation for a source or header file with name <name>. The file name may include (part of) the path if the file-name alone is not unique. If the file name is omitted (i.e. the line after `\file` is left blank) then the documentation block that contains the `\file` command will belong to the file it is located in.

**Important**

The documentation of global functions, variables, typedefs, and enums will only be included in the output if the file they are in is documented as well or if

EXTRACT_ALL

is set to

YES

.

**Example:**

extern

int

globalValue;

Click

here

for the corresponding HTML documentation that is generated by Doxygen.

**Note**

In the above example

JAVADOC_AUTOBRIEF

has been set to

YES

in the configuration file.

# \fileinfo['{'option'}']

Shows (part) of the file name in which this command is placed. The option can be name, extension, filename, directory or, full, with

- name the name of the file without extension
- extension the extension of the file
- filename the filename i.e. name plus extension
- directory the directory of the given file
- full the full path and filename of the given file.

In case no option is specified the filename is used unless FULL_PATH_NAMES is set to YES in which case full is used.

**Note**

the command \fileinfo cannot be used as argument to the

\file

command

**See also**

section

\lineinfo

# \lineinfo

Shows the line number inside the file at which this command is placed.

**See also**

section

\fileinfo

# \fn (function declaration)

Indicates that a comment block contains documentation for a function (either global or as a member of a class). This command is *only* needed if a comment block is *not* placed in front (or behind) the function declaration or definition.

If your comment block *is* in front of the function declaration or definition this command can (and to avoid redundancy should) be omitted.

A full function declaration including arguments should be specified after the `\fn` command on a *single* line, since the argument ends at the end of the line!

This command is equivalent to \var, \typedef, and \property.

**Warning**

Do not use this command if it is not absolutely needed, since it will lead to duplication of information and thus to errors.

**Example:**

class

Fn_Test

{

public

:

const

char

*member(

char

,

int

)

throw

(std::out_of_range);

};

const

char

*Fn_Test::member(

char

c,

int

n)

throw

(std::out_of_range) {}

Click

here

for the corresponding HTML documentation that is generated by Doxygen.

**See also**

sections

\var

,

\property

, and

\typedef

.

# \headerfile <header-file> [<header-name>]

Intended to be used for class, struct, or union documentation, where the documentation is in front of the definition. The arguments of this command are the same as the second and third argument of \class. The <header-file> name refers to the file that should be included by the application to obtain the definition of the class, struct, or union. The <header-name> argument can be used to overwrite the name of the link that is used in the class documentation to something other than <header-file>. This can be useful if the include name is not located on the default include path (like <X11/X.h>).

With the <header-name> argument you can also specify how the include statement should look like, by adding either double quotes or sharp brackets around the name. By default sharp brackets are used if just the name is given.

If a pair of double quotes is given for either the <header-file> or <header-name> argument, the current file (in which the command was found) will be used but with quotes. So for a comment block with a `\headerfile` command inside a file `test.h`, the following three commands are equivalent:

```
  \headerfile test.h "test.h"
  \headerfile test.h ""
  \headerfile "" 
```

To get sharp brackets you do not need to specify anything, but if you want to be explicit you could use any of the following:

```
  \headerfile test.h <test.h>
  \headerfile test.h <>
  \headerfile <> 
```

To globally reverse the default include representation to local includes you can set FORCE_LOCAL_INCLUDES to `YES`.

To disable the include information altogether set SHOW_HEADERFILE to `NO`.

# \hideinitializer

By default the value of a define and the initializer of a variable are displayed unless they are longer than 30 lines. By putting this command in a comment block of a define or variable, the initializer is always hidden. The maximum number of initialization lines can be changed by means of the configuration parameter MAX_INITIALIZER_LINES, the default value is 30.

**See also**

section

\showinitializer

.

# \idlexcept <name>

Indicates that a comment block contains documentation for a IDL exception with name <name>.

# \implements <name>

This command can be used to manually indicate an inheritance relation, when the programming language does not support this concept natively (e.g. C).

The file `manual.c` in the example directory shows how to use this command (see also \memberof for the complete file).

Click here for the corresponding HTML documentation that is generated by Doxygen.

**See also**

section

\extends

and section

\memberof

# \ingroup (<groupname> [<groupname>]*)

If the `\ingroup` command is placed in a comment block of a compound entity (like class, file or namespace), then it will be added to the group(s) identified by the <groupname>(s). In case of members (like variable, functions, typedefs and enums) the member will be added only to one group (to avoid ambiguous linking targets in case a member is not documented in the context of its class, namespace or file, but only visible as part of a group).

**See also**

page

Grouping

, sections

\defgroup

,

\addtogroup

, and

\weakgroup

# \interface <name> [<header-file>] [<header-name>]

Indicates that a comment block contains documentation for an interface with name <name>. The arguments are equal to the arguments of the \class command.

**See also**

section

\class

.

# \internal

This command starts a documentation fragment that is meant for internal use only. The fragment naturally ends at the end of the comment block. You can also force the internal section to end earlier by using the \endinternal command.

If the `\internal` command is put inside a section (see for example \section) all subsections after the command are considered to be internal as well. Only a new section at the same level will end the fragment that is considered internal.

You can use INTERNAL_DOCS in the configuration file to show (`YES`) or hide (`NO`) the internal documentation.

**See also**

section

\endinternal

.

# \mainpage [(title)]

If the `\mainpage` command is placed in a comment block the block is used to customize the index page (in HTML) or the first chapter (in ({\LaTeX})).

The title argument is optional and replaces the default title that Doxygen normally generates. If you do not want any title you can specify `notitle` as the argument of `\mainpage`.

Here is an example:

```
/*! \mainpage My Personal Index Page
 *
 * \section intro_sec Introduction
 *
 * This is the introduction.
 *
 * \section install_sec Installation
 *
 * \subsection step1 Step 1: Opening the box
 *
 * etc...
 */
```

You can refer to the main page using: `\ref index`.

**See also**

section

\section

, section

\subsection

, and section

\page

.

# \memberof <name>

This command makes a function a member of a class in a similar way as \relates does, only with this command the function is represented as a real member of the class. This can be useful when the programming language does not support the concept of member functions natively (e.g. C).

It is also possible to use this command together with \public, \protected or \private.

**Example:**

The file

manual.c

in the example directory shows how to use this command:

typedef

struct

Object Object;

typedef

struct

Vehicle Vehicle;

typedef

struct

Car Car;

typedef

struct

Truck Truck;

struct

Object

{

int

ref;

};

static

Object * objRef(Object *obj);

static

Object * objUnref(Object *obj);

struct

Vehicle

{

Object base;

};

void

vehicleStart(Vehicle *obj);

void

vehicleStop(Vehicle *obj);

struct

Car

{

Vehicle base;

};

struct

Truck

{

Vehicle base;

};

int

main(

void

)

{

Car c;

vehicleStart((Vehicle*) &c);

}

Click

here

for the corresponding HTML documentation that is generated by Doxygen.

**See also**

sections

\extends

,

\implements

,

\public

,

\protected

and

\private

.

# \module <name>

Indicates that a comment block contains documentation for a C++20 module with name <name>.

# \name [(header)]

This command turns a comment block into a header definition of a member group. The comment block should be followed by a @{ ... @} block containing the members of the group.

See section Member Groups for an example.

# \namespace <name>

Indicates that a comment block contains documentation for a namespace with name <name>.

# \nosubgrouping

This command can be put in the documentation of a class. It can be used in combination with member grouping to avoid that Doxygen puts a member group as a subgroup of a Public/Protected/Private/... section.

**See also**

sections

\publicsection

,

\protectedsection

and

\privatesection

.

# \overload [(function declaration)]

This command can be used to generate the following standard text for an overloaded member function:

> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.

If the documentation for the overloaded member function is not located in front of the function declaration or definition, the optional argument should be used to specify the correct declaration of the overloaded function. Of course when the \overload command is directly in front of the overloaded member function and the optional argument is used this should also be the correct declaration of the overloaded function.

Any other documentation that is inside the documentation block will by appended after the generated message.

**Note 1:**

You are responsible that there is indeed an earlier documented member that is overloaded by this one. To prevent that document reorders the documentation you should set

SORT_MEMBER_DOCS

to

NO

in this case.

**Note 2:**

Only one

\overload

command can be present in a comment block.

**Example:**

class

Overload_Test

{

public

:

void

drawRect(

int

,

int

,

int

,

int

);

void

drawRect(

const

Rect &r);

};

void

Overload_Test::drawRect(

int

x,

int

y,

int

w,

int

h) {}

void

Overload_Test::drawRect(

const

Rect &r) {}

Click

here

for the corresponding HTML documentation that is generated by Doxygen.

# \package <name>

Indicates that a comment block contains documentation for a Java package with name <name>.

# \page <name> (title)

Indicates that a comment block contains a piece of documentation that is not directly related to one specific class, file or member. The HTML generator creates a page containing the documentation. The ({\LaTeX}) generator starts a new section in the chapter 'Page documentation'.

**Example:**

Click

here

for the corresponding HTML documentation that is generated by Doxygen.

**Note:**

The <name> argument consists of a combination of letters and number digits. If you wish to use upper case letters (e.g.

MYPAGE1

), or mixed case letters (e.g.

MyPage1

) in the <name> argument, you should set

CASE_SENSE_NAMES

to

YES

. However, this is advisable only if your file system is case sensitive. Otherwise (and for better portability) you should use all lower case letters (e.g.

mypage1

) for <name> in all references to the page.

**See also**

section

\section

, section

\subsection

, and section

\ref

.

# \private

Indicates that the member documented by the comment block is private, i.e., should only be accessed by other members in the same class.

Note that Doxygen automatically detects the protection level of members in object-oriented languages. This command is intended for use only when the language does not support the concept of protection level natively (e.g. C, PHP 4).

For starting a section of private members, in a way similar to the "private:" class marker in C++, use \privatesection.

**See also**

sections

\memberof

,

\public

,

\protected

and

\privatesection

.

# \privatesection

Starting a section of private members, in a way similar to the "private:" class marker in C++. Indicates that the member documented by the comment block is private, i.e., should only be accessed by other members in the same class.

**See also**

sections

\memberof

,

\public

,

\protected

and

\private

.

# \property (qualified property name)

Indicates that a comment block contains documentation for a property (either global or as a member of a class). This command is equivalent to \fn, \typedef, and \var.

**See also**

sections

\fn

,

\typedef

, and

\var

.

# \protected

Indicates that the member documented by the comment block is protected, i.e., should only be accessed by other members in the same or derived classes.

Note that Doxygen automatically detects the protection level of members in object-oriented languages. This command is intended for use only when the language does not support the concept of protection level natively (e.g. C, PHP 4).

For starting a section of protected members, in a way similar to the "protected:" class marker in C++, use \protectedsection.

**See also**

sections

\memberof

,

\public

,

\private

and

\protectedsection

.

# \protectedsection

Starting a section of protected members, in a way similar to the "protected:" class marker in C++. Indicates that the member documented by the comment block is protected, i.e., should only be accessed by other members in the same or derived classes.

**See also**

sections

\memberof

,

\public

,

\private

and

\protected

.

# \protocol <name> [<header-file>] [<header-name>]

Indicates that a comment block contains documentation for a protocol in Objective-C with name <name>. The arguments are equal to the \class command.

**See also**

section

\class

.

# \public

Indicates that the member documented by the comment block is public, i.e., can be accessed by any other class or function.

Note that Doxygen automatically detects the protection level of members in object-oriented languages. This command is intended for use only when the language does not support the concept of protection level natively (e.g. C, PHP 4).

For starting a section of public members, in a way similar to the "public:" class marker in C++, use \publicsection.

**See also**

sections

\memberof

,

\protected

,

\private

and

\publicsection

.

# \publicsection

Starting a section of public members, in a way similar to the "public:" class marker in C++. Indicates that the member documented by the comment block is public, i.e., can be accessed by any other class or function.

**See also**

sections

\memberof

,

\protected

,

\private

and

\public

.

# \pure

Indicates that the member documented by the comment block is pure virtual, i.e., it is abstract and has no implementation associated with it.

This command is intended for use only when the language does not support the concept of pure virtual methods natively (e.g. C, PHP 4).

# \relates <name>

This command can be used in the documentation of a non-member function <name>. It puts the function inside the 'related function' section of the class documentation. This command is useful for documenting non-friend functions that are nevertheless strongly coupled to a certain class. It prevents the need of having to document a file, but only works for functions.

**Example:**

class

String

{

friend

int

strcmp(

const

String &,

const

String &);

};

int

strcmp(

const

String &s1,

const

String &s2)

{

}

void

stringDebug()

{

}

Click

here

for the corresponding HTML documentation that is generated by Doxygen.

# \related <name>

Equivalent to \relates

# \relatesalso <name>

This command can be used in the documentation of a non-member function <name>. It puts the function both inside the 'related function' section of the class documentation as well as leaving it at its normal file documentation location. This command is useful for documenting non-friend functions that are nevertheless strongly coupled to a certain class. It only works for functions.

# \relatedalso <name>

Equivalent to \relatesalso

# \requirement <id> [(title)]

Indicates that a comment block contains documentation for a requirement. In the output, all requirements are collected on a single page.

A requirement can be referred to by its <id> using the normal linking commands like \ref. There are two special commands to refer to a requirement.

- \satisfies can be placed in the comment for a function or class (or any other symbol) that contributes to the *implementation* of the requirement.
- \verifies can be placed at the function or class that *tests* the requirement.

Together the \satisfies and \verifies commands help to provide traceability information to show where in the code a requirement has been implemented and/or tested.

Requirements can be imported via tag files as well.

**See also**

sections

\satisfies

and

\verifies

# \showinitializer

By default the value of a define and the initializer of a variable are only displayed if they are less than 30 lines long. By putting this command in a comment block of a define or variable, the initializer is shown unconditionally. The maximum number of initialization lines can be changed by means of the configuration parameter MAX_INITIALIZER_LINES, the default value is 30.

**See also**

section

\hideinitializer

.

# \static

Indicates that the member documented by the comment block is static, i.e., it works on a class, instead of on an instance of the class.

This command is intended for use only when the language does not support the concept of static methods natively (e.g. C).

# \struct <name> [<header-file>] [<header-name>]

Indicates that a comment block contains documentation for a struct with name <name>. The arguments are equal to the arguments of the \class command.

**See also**

section

\class

.

# \typedef (typedef declaration)

Indicates that a comment block contains documentation for a typedef (either global or as a member of a class). This command is equivalent to \fn, \property, and \var.

**See also**

section

\fn

,

\property

, and

\var

.

# \union <name> [<header-file>] [<header-name>]

Indicates that a comment block contains documentation for a union with name <name>. The arguments are equal to the arguments of the \class command.

**See also**

section

\class

.

# \var (variable declaration)

Indicates that a comment block contains documentation for a variable or enum value (either global or as a member of a class). This command is equivalent to \fn, \property, and \typedef.

Note that for PHP one can also specify the type of the variable. The syntax is similar as for the phpDocumentor but the description has to start at the next line, i.e.

```
@var  datatype $varname
Description
```

**See also**

section

\fn

,

\property

, and

\typedef

.

# \vhdlflow [(title for the flow chart)]

This is a VHDL specific command, which can be put in the documentation of a process to produce a flow chart of the logic in the process. Optionally a title for the flow chart can be given.

**Note**

Currently the flow chart will only appear in the HTML output.

# \weakgroup <name> [(title)]

Can be used exactly like \addtogroup, but has a lower priority when it comes to resolving conflicting grouping definitions.

**See also**

page

Grouping

and section

\addtogroup

.
