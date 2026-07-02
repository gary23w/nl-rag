---
title: "Namespace"
source: https://en.wikipedia.org/wiki/Namespace
domain: resource-quotas-k8s
license: CC-BY-SA-4.0
tags: resource quota, namespace resource cap, limit range default, aggregate consumption limit
fetched: 2026-07-02
---

# Namespace

In computing, a **namespace** is a set of signs (*names*) that are used to identify and refer to objects of various kinds. A namespace ensures that all of a given set of objects have unique names so that they can be easily identified.

Namespaces are commonly structured as hierarchies to allow reuse of names in different contexts. As an analogy, consider a system of naming of people where each person has a given name, as well as a family name shared with their relatives. If the first names of family members are unique only within each family, then each person can be uniquely identified by the combination of first name and family name; there is only one Jane Doe, though there may be many Janes. Within the namespace of the Doe family, just "Jane" suffices to unambiguously designate this person, while within the "global" namespace of all people, the full name must be used.

Prominent examples for namespaces include file systems, which assign names to files. Some programming languages organize their variables and subroutines in namespaces. Computer networks and distributed systems assign names to resources, such as computers, printers, websites, and remote files. Operating systems can partition kernel resources by isolated namespaces to support OS-level virtualization containers.

Similarly, hierarchical file systems organize files in directories. Each directory is a separate namespace, so that the directories "letters" and "invoices" may both contain a file "to_jane".

In computer programming, namespaces are typically used to group symbols and identifiers around a given task and to avoid name collisions between multiple identifiers that share the same name.

In computer networking, the Domain Name System organizes websites (and other resources) into hierarchical namespaces.

## Name conflicts

Element names are defined by the developer. This often results in a conflict when trying to mix XML documents from different XML applications.

This XML carries HTML table information:

```mw
<table>
    <tr>
        <td>Good</td>
        <td>Bad</td>
    </tr>
</table>
```

This XML carries information about a table (i.e. a piece of furniture):

```mw
<table>
    <name>Mahogany Coffee Table</name>
    <width>30</width>
    <length>120</length>
</table>
```

If these XML fragments were added together, there would be a name conflict. Both contain a `<table>...</table>` element, but the elements have different content and meaning.

An XML parser will not know how to handle these differences.

### Solution via prefix

Name conflicts in XML can easily be avoided using a name prefix.

The following XML distinguishes between information about the HTML table and furniture by prefixing "h" and "f" at the beginning of the elements.

```mw
<h:table>
    <h:tr>
        <h:td>Good</h:td>
        <h:td>Bad</h:td>
    </h:tr>
</h:table>

<f:table>
    <f:name>Mahogany Coffee Table</f:name>
    <f:width>30</f:width>
    <f:length>120</f:length>
</f:table>
```

## Naming system

A name in a namespace consists of a namespace name and a local name. The namespace name is usually applied as a prefix to the local name.

In augmented Backus–Naur form:

```mw
name = <namespace name> separator <local name>
```

When local names are used by themselves, name resolution is used to decide which (if any) particular name is alluded to by some particular local name.

### Examples

| Context | Name | Namespace name | Local name |
|---|---|---|---|
| Domain name | www.example.com | example.com (domain name) | www (subdomain name) |
| Wikipedia | Talk:Mona Lisa | Talk | Mona Lisa |
| Path (UNIX) | /home/admin/Documents/readme.txt | /home/admin/Documents (directory) | readme.txt (file name) |
| Path (Windows) | C:\Users\Admin\Documents\readme.txt | C:\Users\Admin\Documents (directory) | readme.txt (file name) |
| C++ standard library namespace | `std::chrono::system_clock` | `std::chrono` (C++ namespace) | `system_clock` (class) |
| C++ namespace | `Poco::Net::HTTPClientSession` | `Poco::Net` (C++ namespace) | `HTTPClientSession` (class) |
| C# namespace | `System.Collections.Generic.Dictionary` | `System.Collections.Generic` (C# namespace) | `Dictionary` (class) |
| Java standard library package | `java.util.Date` | `java.util` (Java package) | `Date` (class) |
| Java package | `org.apache.commons.math3.special.Gamma` | `org.apache.commons.math3.special` (Java package) | `Gamma` (class) |
| UN/LOCODE | US NYC | US (country or territory) | NYC (locality) |
| XML | `xmlns:xhtml="http://www.w3.org/1999/xhtml"` `<xhtml:body>` | `xhtml` (previously declared XML namespace `xhtml="http://www.w3.org/1999/xhtml"`) | `body` (element) |
| Perl | `$DBI::errstr` | `$DBI` (Perl module) | `errstr` (variable) |
| Uniform Resource Name (URN) | urn:nbn:fi-fe19991055 | urn:nbn (National Bibliography Numbers) | fi-fe19991055 |
| Handle System | 10.1000/182 | 10 (handle naming authority) | 1000/182 (handle local name) |
| Digital object identifier | 10.1000/182 | 10.1000 (publisher) | 182 (publication) |
| MAC address | 01-23-45-67-89-ab | 01-23-45 (organizationally unique identifier) | 67-89-ab (NIC specific) |
| PCI ID | 1234 abcd | 1234 (vendor ID) | abcd (device ID) |
| USB VID/PID | 2341 003f | 2341 (vendor ID) | 003f (product ID) |
| SPARQL | `dbr:Sydney` | `dbr` (previously declared ontology, e.g. by specifying `@prefix dbr: <http://dbpedia.org/resource/>`) | `Sydney` |

### Delegation

Delegation of responsibilities between parties is important in real-world applications, such as the structure of the World Wide Web. Namespaces allow delegation of identifier assignment to multiple name issuing organisations whilst retaining global uniqueness. A central Registration authority registers the assigned namespace names allocated. Each namespace name is allocated to an organisation which is subsequently responsible for the assignment of names in their allocated namespace. This organisation may be a name issuing organisation that assign the names themselves, or another Registration authority which further delegates parts of their namespace to different organisations.

### Hierarchy

A naming scheme that allows subdelegation of namespaces to third parties is a **hierarchical namespace**.

A hierarchy is recursive if the syntax for the namespace names is the same for each subdelegation. An example of a recursive hierarchy is the Domain name system.

An example of a non-recursive hierarchy are Uniform Resource Name representing an Internet Assigned Numbers Authority (IANA) number.

| Registry | Registrar | Example Identifier | Namespace name | Namespace |
|---|---|---|---|---|
| Uniform Resource Name (URN) | Internet Assigned Numbers Authority | urn:isbn:978-3-16-148410-0 | urn | Formal URN namespace |
| Formal URN namespace | Internet Assigned Numbers Authority | urn:isbn:978-3-16-148410-0 | ISBN | International Standard Book Numbers as Uniform Resource Names |
| International Article Number (EAN) | GS1 | 978-3-16-148410-0 | 978 | Bookland |
| International Standard Book Number (ISBN) | International ISBN Agency | 3-16-148410-X | 3 | German-speaking countries |
| German publisher code | Agentur für Buchmarktstandards | 3-16-148410-X | 16 | Mohr Siebeck |

### Namespace versus scope

A namespace name may provide context (scope in computer science) to a name, and the terms are sometimes used interchangeably. However, the context of a name may also be provided by other factors, such as the location where it occurs or the syntax of the name.

|   | Without a namespace | With a namespace |
|---|---|---|
| *Local scope* | Vehicle registration plate | Filesystem Hierarchy Standard |
| *Global scope* | Universally unique identifier | Domain Name System |

## In programming languages

For many programming languages, namespace is a context for their identifiers. In an operating system, an example of namespace is a directory. Each name in a directory uniquely identifies one file or subdirectory.

As a rule, names in a namespace cannot have more than one meaning; that is, different meanings cannot share the same name in the same namespace. A namespace is also called a context, because the same name in different namespaces can have different meanings, each one appropriate for its namespace.

Following are other characteristics of namespaces:

- Names in the namespace can represent objects as well as concepts, be the namespace a natural or ethnic language, a constructed language, the technical terminology of a profession, a dialect, a sociolect, or an artificial language (e.g., a programming language).
- In the Java programming language, identifiers that appear in namespaces have a short (local) name and a unique long "qualified" name for use outside the namespace.
- Some compilers (for languages such as C++) combine namespaces and names for internal use in the compiler in a process called *name mangling*.

As well as its abstract language technical usage as described above, some languages have a specific keyword used for explicit namespace control, amongst other uses. Below is an example of a namespace in C++:

```mw
import std;

// This is how one brings a name into the current scope.  In this case, it's
// bringing them into global scope.
using std::println;

namespace box1 {
    constexpr int BOX_SIDE = 4;
}

namespace box2 {
    constexpr int BOX_SIDE = 12;
}

int main() {
    constexpr int BOX_SIDE = 42;
    println("{}", box1::BOX_SIDE);  // Outputs 4.
    println("{}", box2::BOX_SIDE);  // Outputs 12.
    println("{}", BOX_SIDE);  // Outputs 42.
}
```

### Computer-science considerations

A namespace in computer science (sometimes also called a **name scope**) is an abstract container or environment created to hold a logical grouping of unique identifiers or symbols (i.e. names). An identifier defined in a namespace is associated only with that namespace. The same identifier can be independently defined in multiple namespaces. That is, an identifier defined in one namespace may or may not have the same meaning as the same identifier defined in another namespace. Languages that support namespaces specify the rules that determine to which namespace an identifier (not its definition) belongs.

This concept can be illustrated with an analogy. Imagine that two companies, X and Y, each assign ID numbers to their employees. X should not have two employees with the same ID number, and likewise for Y; but it is not a problem for the same ID number to be used at both companies. For example, if Bill works for company X and Jane works for company Y, then it is not a problem for each of them to be employee #123. In this analogy, the ID number is the identifier, and the company serves as the namespace. It does not cause problems for the same identifier to identify a different person in each namespace.

In large computer programs or documents it is common to have hundreds or thousands of identifiers. Namespaces (or a similar technique, see Emulating namespaces) provide a mechanism for hiding local identifiers. They provide a means of grouping logically related identifiers into corresponding namespaces, thereby making the system more modular.

Data storage devices and many modern programming languages support namespaces. Storage devices use directories (or folders) as namespaces. This allows two files with the same name to be stored on the device so long as they are stored in different directories. In some programming languages (e.g. C++, Python), the identifiers naming namespaces are themselves associated with an enclosing namespace. Thus, in these languages namespaces can nest, forming a namespace tree. At the root of this tree is the unnamed **global namespace**.

#### Use in common languages

##### C

It is possible to use anonymous structs as namespaces in C since C99.

Math.h:

```mw
#pragma once

const struct {
    double PI;
    double (*sin)(double);
} Math;
```

Math.c:

```mw
#include <math.h>

static double _sin(double arg) {
    return sin(arg);
}

const struct {
    double PI;
    double (*sin)(double);
} Math = { M_PI, _sin };
```

Main.c:

```mw
#include <stdio.h>
#include "Math.h"

int main() {
    printf("sin(0) = %d\n", Math.sin(0));
    printf("pi is %f\n", Math.PI);
}
```

##### C++

In C++, a namespace is defined with a namespace block.

```mw
namespace abc {
    int bar;
}
```

Within this block, identifiers can be used exactly as they are declared. Outside of this block, the namespace specifier must be prefixed. For example, outside of `namespace abc`, `bar` must be written `abc::bar` to be accessed. C++ includes another construct that makes this verbosity unnecessary. By adding the line

```mw
using namespace abc;
```

to a piece of code, the prefix `abc::` is no longer needed.

Identifiers that are not explicitly declared within a namespace are considered to be in the global namespace.

```mw
int foo;
```

These identifiers can be used exactly as they are declared, or, since the global namespace is unnamed, the namespace specifier `::` can be prefixed. For example, `foo` can also be written `::foo`.

Namespace resolution in C++ is hierarchical. This means that within the hypothetical namespace `food::soup`, the identifier `Chicken` refers to `food::soup::Chicken`. If `food::soup::Chicken` doesn't exist, it then refers to `food::Chicken`. If neither `food::soup::Chicken` nor `food::Chicken` exist, `Chicken` refers to `::Chicken`, an identifier in the global namespace.

Namespaces in C++ are most often used to avoid naming collisions. Although namespaces are used extensively in recent C++ code, most older code does not use this facility because it did not exist in early versions of the language. For example, the entire C++ Standard Library is defined within `namespace std`, but before standardization many components were originally in the global namespace. The `using` statement can be used to import a symbol into the current scope.

The use of the `using` statements in headers for reasons other than backwards compatibility (e.g., convenience) is considered to be against good code practices, as those `using` statements propagate into all translation units that include the header. However, modules do not export `using` statements unless explicitly marked `export`, making `using` statements safer to use. For instance, one can import a module `wikipedia.project.util` with matching namespace `wikipedia::project::util` and then use `using` statements on symbols from that namespace to simplify verbose namespaces. Unlike other languages like Java or Rust, C++ modules, namespaces and source file structure do not necessarily match, though it is convention to match them for clarity (for example, module `abc.def.uvw.XYZ` matches namespaced class `abc::def::uvw::XYZ` and resides in file `abc/def/uvw/XYZ.cppm`).

`using` should be used to simplify verbose nested namespaces when modular translation units are used.

```mw
export module wikipedia.project.App;

import std;

import wikipedia.project.fs;
import wikipedia.project.util;

using wikipedia::project::fs::File;
using wikipedia::project::util::ConfigLoader;
using wikipedia::project::util::logging::Logger;
using wikipedia::project::util::logging::LoggerFactory;

export namespace wikipedia::project {

class App {
private:
    Logger logger;
    // private fields and methods
public:
    App():
        logger{LoggerFactory::getLogger("Main")} {
        ConfigLoader cl(File("config/config_file.txt"));
        logger.log("Application starting...");
        // rest of code
    }
};

}
```

C++11 introduces *inline namespaces*, which is such that its members are treated as if they are also members of the enclosing namespace. It is declared by writing `inline namespace`. It is akin to an implicit `using namespace` statement, meaning qualifying symbols in it is optional.

The inline property is transitive. If a namespace `a` contains an inline namespace `b`, which in turn contains another inline namespace `c`, then members of `c` can be accessed as if they were members of `a` or `b`.

A primary use case for inline namespaces is ABI compatibility and versioning. By placing different versions of an API within distinct inline namespaces (e.g., `v1`, `v2`), and then making the currently desired version inline, library developers can manage ABI compatibility. When a new version is released, the inline keyword can be moved to the new version's namespace, allowing users to automatically link against the new version while still enabling access to older versions through explicit qualification.

```mw
namespace mylib::utils {
    namespace v1 {
        [[deprecated("Use mylib::utils::v2::func() instead")]]
        void func() {
            // Old implementation
        }
    }

    // v2 is the currently active version
    inline namespace v2 {
        void func() {
            // New implementation
        }
    }
}

int main() {
    // Calls mylib::utils::v2::func() implicitly
    mylib::utils::func();

    // Calls mylib::utils::v2::func() explicitly
    mylib::utils::v2::func();

    // Calls mylib::utils::v1::func() explicitly
    mylib::utils::v1::func();

    return 0;
}
```

##### C

Namespaces are heavily used in C# language. All .NET framework classes are organized in namespaces, to be used more clearly and to avoid chaos. Also, custom namespaces are used extensively by programmers, to organize their work and to avoid naming collisions. When referencing a class, one may specify either its fully qualified name, meaning its namespace followed by the class name:

```mw
System.Console.WriteLine("Hello World!");
int i = System.Convert.ToInt32("123");
```

or add a `using` statement. This eliminates the need to mention the complete name of all classes in that namespace.

```mw
using System;

Console.WriteLine("Hello World!");
int i = Convert.ToInt32("123");
```

In the above examples, `System` is a namespace, and `Console` and `Convert` are classes defined within `System`.

(UML diagram with a Console and a Convert class.)

Unlike C++, `using` can only import all symbols in a namespace (much like `using namespace` from C++, `use *` in Rust, or `import *` in Java). It cannot be used to import individual symbols and classes like it is used in Java.

```mw
namespace Wikipedia.Project;

using System;
using System.IO;

using Microsoft.Extensions.Logging;

using Wikipedia.Project.Utility;

class App
{
    private static ILogger<Program> logger;

    public App()
    {
        ConfigLoader cl = new ConfigLoader(Path.Combine("config", "config_file.txt"));
        LoggerFactory loggerFactory = LoggerFactory.Create(builder => 
        {
            builder.AddConsole();
        });
        logger = loggerFactory.CreateLogger<Program>();
        logger.LogInformation("Application starting...");
        // rest of code
    }
}
```

Unlike C++, C# namespaces do not allow relative referencing of symbols. For example, the class `Foo.Bar.Baz.Qux` cannot be referred to as `Baz.Qux` even if referred to from within namespace `Foo.Bar`: either the namespace `Foo.Bar.Baz` must be imported to refer to class `Qux`, or `Foo.Bar.Baz.Qux` must be fully qualified.

##### Java

In Java, the idea of a namespace is embodied in Java packages. All code belongs to a package, although that package need not be explicitly named. Code from other packages is accessed by prefixing the package name before the appropriate identifier, for example `class String` in `package java.lang` can be referred to as `java.lang.String` (this is known as the fully qualified class name). Like C++, Java offers a construct that makes it unnecessary to type the package name (`import`). However, certain features (such as reflection) require the programmer to use the fully qualified name.

Unlike C++, namespaces in Java are not hierarchical as to the syntax of the language. However, packages are named in a hierarchical manner. For example, all packages beginning with `java` are a part of the Java platform—the package `java.lang` contains classes core to the language, and `java.lang.reflect` contains core classes specifically relating to reflection.

In Java (and Ada, C#, and others), namespaces/packages express semantic categories of code. For example, in C#, `namespace System` contains code provided by the system (the .NET framework). How specific these categories are and how deep the hierarchies go differ from language to language.

Function and class scopes can be viewed as implicit namespaces that are inextricably linked with visibility, accessibility, and object lifetime.

In Java, packages cannot be partially qualified like they can in C++. For instance, it is not possible to import the `java` namespace and then refer to `java.util.ArrayList` as `util.ArrayList`. Symbols must either be fully qualified or imported completely into scope. `import` statements are not transitive nor can they be deliberately marked `export` like in C++. All `import` statements must appear at the beginning of the file, and cannot be written at any other scope. This is in contrast to C++, where the `std` namespace can be imported by writing `using namespace std;`, and then `std::chrono::system_clock` can be referred to as `chrono::system_clock`.

```mw
package org.wikipedia.project;

import java.nio.file.Paths;
import java.util.logging.Level;
import java.util.logging.Logger;

import org.wikipdia.project.util.ConfigLoader;

public class App {
    private static final Logger logger = Logger.getLogger(Main.class.getName());

    public App() {
        ConfigLoader cl = new ConfigLoader(Paths.get("config/config_file.txt"));
        logger.log(Level.INFO, "Application starting...");
        // rest of code
    }
}
```

Because Java does not support independent functions outside of classes, static class methods and so-called "utility classes" (classes with private constructors and all methods and fields static) are the equivalent to C++-style namespaces. Some examples are `java.lang.Math`, which contains the constants like `Math.PI` and methods like `Math.sin()`.

`import` statements can be used to import all symbols in a package, called a glob import, which is similar to `using namespace` in C++. For instance, writing `import java.util.*;` imports all classes in the `java.util` package. This however, can cause symbol pollution within a file. Furthermore, using glob import statements on packages that have classes with the same name can cause ambiguity, and will fail to compile. However, `java.lang.*` is implicitly imported into all Java source files by default.

```mw
import java.sql.*; // Imports all classes in java.sql, including java.sql.Date
import java.util.*; // Imports all classes in java.util, including java.util.Date

Date d = new Date(); // Ambiguous Date reference resulting in compilation error

// Instead, the fully-qualified names must be used:
java.sql.Date sqlDate = new java.sql.Date(System.currentTimeMillis());
java.util.Date utilDate = new java.util.Date();
```

##### Kotlin

Kotlin packages are very similar to Java packages, but unlike Java where only class-like objects may reside directly in a package, any top-level symbol (such as a variable, class, type alias, etc.) may live directly inside a package.

```mw
package org.wikipedia.examples

import kotlin.math.PI

var myPi = PI

fun circleArea(radius: Double): Double {
    return myPi * radius * radius
}
```

##### PHP

Namespaces were introduced into PHP from version 5.3 onwards. Naming collision of classes, functions and variables can be avoided. In PHP, a namespace is defined with a namespace block.

```mw
# File phpstar/foobar.php

namespace phpstar;

class FooBar
{
    public function foo(): void
    {
        echo 'Hello world, from function foo';
    }

    public function bar(): void
    {
        echo 'Hello world, from function bar';
    }
}
```

We can reference a PHP namespace with the following different ways:

```mw
# File index.php

# Include the file
include "phpstar/foobar.php";

# Option 1: directly prefix the class name with the namespace
$obj_foobar = new \phpstar\FooBar();

# Option 2: import the namespace
use phpstar\FooBar;
$obj_foobar = new FooBar();

# Option 2a: import & alias the namespace
use phpstar\FooBar as FB;
$obj_foobar = new FB();

# Access the properties and methods with regular way
$obj_foobar->foo();
$obj_foobar->bar();
```

(UML diagram of the phpstar package with the class FooBar.)

##### Python

In Python, namespaces are defined by the individual modules, and since modules can be contained in hierarchical packages, then namespaces are hierarchical too. In general when a module is imported then the names defined in the module are defined via that module's namespace, and are accessed in from the calling modules by using the fully qualified name.

```mw
# assume mod_a defines two functions : func1() and func2() and one class : Class1
import mod_a

mod_a.func1()
mod_a.func2()
a: mod_a.Class1 = mod_a.Class1()
```

The `from ... import ...` statement can be used to insert the relevant names directly into the calling module's namespace, and those names can be accessed from the calling module without the qualified name:

```mw
# assume mod_a defines two functions : func1() and func2() and one class : Class1
from mod_a import func1

func1()
func2() # this will fail as an undefined name, as will the full name mod_a.func2()
a: Class1 = Class1() # this will fail as an undefined name, as will the full name mod_a.Class1()
```

Since this directly imports names (without qualification) it can overwrite existing names with no warnings.

A special form of the statement is `from ... import *` which imports all names defined in the named package directly in the calling module's namespace. Use of this form of import, although supported within the language, is generally discouraged as it pollutes the namespace of the calling module and will cause already defined names to be overwritten in the case of name clashes, though using `from import` in Python can simplify verbose namespaces, such as nested namespaces.

```mw
from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

if __name__ == "__main__":
    driver: Firefox = Firefox()
    element: WebElement = driver.find_element(By.ID, "myInputField")
    element.send_keys(f"Hello World{Keys.ENTER}")
    action: ActionChains = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
```

Python also supports `import x as y` as a way of providing an alias or alternative name for use by the calling module:

```mw
import numpy as np
from numpy.typing import NDArray, float32

a: NDArray[float32] = np.arange(1000)
```

##### Rust

In Rust, a namespace is called a "module" and declared using `mod`. Symbols inside the module are by default private, and cannot be accessed externally, unless declared with the `pub` keyword which exposes them. Modules can have sub-modules inside of them, allowing for nested namespaces.

Similar to the `using` keyword in C++, Rust has the `use` keyword to import symbols into the current scope.

```mw
mod my_module {
    pub trait Greet {
        fn greet(&self);
    }

    pub struct Person {
        pub name: String,
    }

    impl Greet for Person {
        fn greet(&self) {
            println!("Hello, {}!", self.name);
        }
    }
}

fn main() {
    use my_module::{Person, Greet};

    let person = Person { name: String::from("Alice") };
    person.greet();
}
```

Writing `mod util;` indicates to the compiler to find either a file named `util.rs` or `util/mod.rs`. `crate` in a `use` statement refers to the root of the current "crate" (project), while `super` can be used to refer to the parent module.

```mw
mod util;

use std::fs::File;

use crate::util::ConfigLoader;
use crate::util::logging::{Logger, LoggerFactory};

pub struct App {
    config_loader: ConfigLoader;
}

impl App {
    pub fn new() -> Self {
        config_loader = ConfigLoader::new(File::open("config/config_file.txt"));
        config_loader.load();
        let logger: Logger = LoggerFactory::get_logger("Main");
        logger.log("Application starting...");
        // rest of code
    }
}
```

The `use` keyword in Rust is more versatile than its counterpart `using` in C++. In addition to importing single symbols, symbol aliasing with `as` and glob imports, `use` can import multiple symbols on the same line using braces (which may be nested), import individual namespaces, and do all of the above in a single statement. This is an example of using all of the above:

```mw
use std::{
    alloc::Layout, // imports std::alloc::Layout
    fmt::*, // imports all symbols in std::fmt
    fs::{File, Metadata}, // imports std::fs::File and std::fs::Metadata
    io::{prelude::*, BufReader, BufWriter} // imports all symbols in std::io::prelude::*, std::io::BufReader, and std::io::BufWriter
    process, // imports the std::process namespace (for example std::process::Command can be referred to as process::Command)
    time::{self, Duration} // imports the std::time namespace and std::time::Duration
};

use std::fmt::Result as FmtResult; // renames std::fmt::Result to FmtResult
```

##### XML namespace

In XML, the XML namespace specification enables the names of elements and attributes in an XML document to be unique, similar to the role of namespaces in programming languages. Using XML namespaces, XML documents may contain element or attribute names from more than one XML vocabulary.

##### SAP Namespace

In SAP systems (especially ABAP environments), namespaces are used to prevent naming collisions between standard SAP-delivered objects and customer or partner developments.

A namespace identifier is delimited with “/” (for example `/MYNS/`) and is reserved via SAP’s namespace registration process. Once reserved, objects created under that namespace are uniquely identifiable and protected from unintended overwrite by SAP upgrades or imports.

In modern SAP landscapes (such as ABAP in the cloud and HDI containers), namespaces are also used to semantically group development artifacts or bundles.

### Emulating namespaces

In programming languages lacking language support for namespaces, namespaces can be emulated to some extent by using an identifier naming convention. For example, C libraries such as libpng often use a fixed prefix for all functions and variables that are part of their exposed interface. Libpng exposes identifiers such as:

```
png_create_write_struct
png_get_signature
png_read_row
png_set_invalid
```

This naming convention provides reasonable assurance that the identifiers are unique and can therefore be used in larger programs without naming collisions. Likewise, many packages originally written in Fortran (e.g., BLAS, LAPACK) reserve the first few letters of a function's name to indicate the group to which the function belongs.

This technique has several drawbacks:

- It doesn't scale well to nested namespaces; identifiers become excessively long since all uses of the identifiers must be fully namespace-qualified;
- Individuals or organizations may use inconsistent naming conventions, potentially introducing unwanted obfuscation;
- Compound or "query-based" operations on groups of identifiers, based on the namespaces in which they are declared, are rendered unwieldy or unfeasible;
- In languages with restricted identifier length, the use of prefixes limits the number of characters that can be used to identify what the function does; this is a particular problem for packages originally written in FORTRAN 77, which offered only 6 characters per identifier; for example, the name of the BLAS function `DGEMM` indicates that it operates on double-precision floating-point numbers (`D`) and general matrices (`GE`), with only the last two characters (`MM`) showing what it actually does: matrix–matrix multiplication.

It also has a few advantages:

- No special software tools are required to locate names in source-code files; a simple program like grep suffices;
- There are no namespace-related name conflicts;
- There is no need for name mangling, and thus no potential incompatibility problems.
