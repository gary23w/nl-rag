---
title: "Dependency hell"
source: https://en.wikipedia.org/wiki/Dependency_hell
domain: dependency-pinning
license: CC-BY-SA-4.0
tags: dependency version pinning, lock file reproducibility, hash pinned dependency, deterministic dependency resolution
fetched: 2026-07-02
---

# Dependency hell

**Dependency hell** is a colloquial term for the frustration of some software users who have installed software packages which have dependencies on specific versions of other software packages.

The dependency issue arises when several packages have dependencies on the same *shared* packages or libraries, but they depend on different and incompatible versions of the shared packages. If the shared package or library can only be installed in a single version, the user may need to address the problem by obtaining newer or older versions of the dependent packages. This, in turn, may break other dependencies and push the problem to another set of packages.

## Problems

Dependency hell takes several forms:

### Many dependencies

An application depends on many

libraries

, requiring long downloads, large amounts of disk space, and being very portable (all libraries are already ported enabling the application itself to be ported easily). It can also be difficult to locate all the dependencies, which can be fixed by having a repository (see below). This is partly inevitable; an application built on a given

computing platform

(such as

Java

) requires that platform to be installed, but further applications do not require it. This is a particular problem if an application uses a small part of a big library (which can be solved by

code refactoring

), or a simple application relies on many libraries.

### Long chains of dependencies

If

app

depends on

liba

, which depends on

libb

, ..., which depends on

libz

. This is distinct from "many dependencies" if the dependencies must be resolved manually, e.g., on attempting to install

app

, the user is prompted to install

liba

first and on attempting to install

liba

, the user is then prompted to install

libb

, and so on. Sometimes, however, during this long chain of dependencies, conflicts arise where two different versions of the same package are required

(see

conflicting dependencies

below). These long chains of dependencies can be solved by having a

package manager

that resolves all dependencies automatically. Other than being a hassle (to resolve all the dependencies manually), manual resolution can mask dependency cycles or conflicts.

### Conflicting dependencies

Solving the dependencies for one software may break the compatibility of another in a similar fashion to

whack-a-mole

. If

app1

depends on

libfoo

1.2, and

app2

depends on

libfoo

2.0, and different versions of

libfoo

cannot be simultaneously installed, then

app1

and

app2

cannot simultaneously be used (or installed, if the installer checks dependencies). When possible, this is solved by allowing simultaneous installations of the different dependencies. Alternatively, the existing dependency, along with all software that depends on it, must be uninstalled in order to install the new dependency. A problem on Linux systems with installing packages from a different distributor is that the resulting long chain of dependencies may lead to a conflicting version of the

C standard library

(e.g., the

GNU C Library

), on which thousands of packages depend. If this happens, the user will be prompted to uninstall all of those packages.

### Circular dependencies

If application

A

depends upon and can't run without a specific version of application

B

, but application

B

in turn depends upon and can't run without a specific version of application

A

, then upgrading any application will break another. This scheme can be deeper in branching. Its impact can be quite heavy if it affects core systems or update software itself: a package manager (

A

), which requires specific run-time library (

B

) to function, may break itself (

A

) in the middle of the process when upgrading this library (

B

) to next version. Due to incorrect library (

B

) version, the package manager (

A

) is now broken, thus no rollback or downgrade of library (

B

) is possible. The usual solution is to download and deploy both applications, sometimes from within a temporary environment.

### Package manager dependencies

It is possible

for dependency hell to result from installing a prepared package via a package manager (e.g.,

APT

), but this is unlikely since major package managers have matured and official repositories are well maintained. This is the case with current releases of

Debian

and major derivatives such as

Ubuntu

. Dependency hell, however, can result from installing a package directly via a package installer (e.g.,

RPM Package Manager

(RPM) or

dpkg

).

### Diamond dependency

When a library

A

depends on libraries

B

and

C

, both

B

and

C

depend on library

D

, but

B

requires version

D.1

and

C

requires version

D.2

. The build fails because only one version of

D

can exist in the final executable.

Package managers like

yum

are prone to have conflicts between packages of their repositories, causing dependency hell in Linux distributions such as

CentOS

and

Red Hat Enterprise Linux

.

## Solutions

### Removing dependencies

Many software libraries are written in a generous way, in an attempt to fulfill most users' needs, but sometimes only a small portion of functions are required in the host code. By examining the source, the functionality can be rewritten in a much more compact way (with respect to the license). In general, this can significantly reduce the application code, reduce later maintenance costs, and improve the software writing skills of programmers.

### Version numbering

A very common solution to this problem is to have a standardized numbering system, wherein software uses a specific number for each version (aka

major version

), and also a subnumber for each revision (aka

minor version

), e.g.:

10

.1, or 5.

7

. The major version only changes when programs that used that version will no longer be compatible. The minor version might change with even a simple revision that does not prevent other software from working with it. In cases like this, software packages can then simply request a component that has a particular major version, and

any

minor version (greater than or equal to a particular minor version). As such, they will continue to work, and dependencies will be resolved successfully, even if the minor version changes. Semantic Versioning (aka "SemVer"

) is one example of an effort to generate a technical specification that employs specifically formatted numbers to create a software versioning scheme.

### Private per application versions

Windows File Protection

, introduced in

Windows 2000

, prevented applications from overwriting system

dynamic-link libraries

(DLLs). Developers were instead encouraged to use

Private DLLs,

which were duplicates of system DLLs stored in the program's folder. This requires custom dependencies to be packaged with a program, therefore preventing dependency hell.

PC-BSD, up to and including version 8.2, a predecessor of

TrueOS

(an

operating system

based on

FreeBSD

) places packages and dependencies into self-contained directories in

/Programs

, which avoids breakage if system libraries are upgraded or changed. It uses its own

push button installer

(PBI) for package management.

### Side-by-side installation of multiple versions

The version numbering solution can be improved upon by elevating the version numbering to an operating system supported feature. This allows an application to request a module/library by a unique name

and

version number constraints, effectively transferring the responsibility for brokering library/module versions from the applications to the operating system. A shared module can then be placed in a central repository without risk of breaking applications which are dependent on prior or later versions of the module. Each version gets its own entry, side by side with other versions of the same module.

This solution is used in

Microsoft Windows

operating systems since Windows Vista, where the

Global Assembly Cache

is an implementation of such a central registry with associated services and integrated with the installation system/package manager.

Gentoo Linux

solves this problem with a concept called slotting, which allows multiple versions of shared libraries to be installed.

### Smart package management

Some

package managers

can perform smart upgrades, in which interdependent software components are upgraded at the same time, thereby resolving the major number incompatibility issue too.

Many current

Linux

distributions have also implemented

repository

-based package management systems to try to solve the dependency problem. These systems are a layer on top of the

RPM Package Manager

(RPM),

dpkg

, or other packaging systems that are designed to automatically resolve dependencies by searching in one or more predefined

software repository

. Examples of these systems include Advanced Packaging Tool (

APT

),

Yum

,

Urpmi

,

ZYpp

,

Portage

,

Pacman

and others. Typically, the software repositories are

File Transfer Protocol

(FTP) sites or websites,

directories

on the local computer or shared across a

network

or, much less commonly, directories on removable media such as CDs or DVDs. This eliminates dependency hell for software packaged in those repositories, which are typically maintained by the Linux distribution provider and

mirrored

worldwide. Although these repositories are often huge, it is not possible to have every piece of software in them, so dependency hell can still occur. In all cases, dependency hell is still faced by the repository maintainers.

### Installer options

Because different pieces of software have different dependencies, it is possible to get into a

vicious circle

of dependency

requirements

, or an ever-expanding

tree

of requirements, as each new package demands several more be installed. Systems such as Debian's Advanced Packaging Tool (

APT

) can resolve this by presenting a user with a range of solutions, and allowing the user to accept or reject the solutions, as desired.

### Easy adaptability in programming

If application software is designed in such a way that its programmers are able to easily adapt the interface layer that deals with the OS, window manager or desktop environment to new or changing standards, then the programmers would only have to monitor notifications from the environment creators or component library designers and quickly adjust their software with updates for their users, all with minimal effort and a lack of costly and time-consuming redesign. This method would encourage programmers to pressure those upon whom they depend to maintain a reasonable notification process that is not onerous to anyone involved.

### Strict compatibility requirement in code development and maintenance

If the applications and libraries are developed and maintained with guaranteed downward compatibility in mind, any application or library can be replaced with a newer version at any time without breaking anything. While this does not alleviate the multitude of dependency, it does make the jobs of package managers or installers much easier.

### Software appliances

Another approach to avoiding dependency issues is to deploy applications as a

software appliance

. A software appliance encapsulates dependencies in a pre-integrated self-contained unit such that users no longer have to worry about resolving software dependencies. Instead the burden is shifted to developers of the software appliance.

Containers

and their images (such as those provided by

Docker

and Docker Hub) can be seen as an implementation of software appliances.

### Portable applications

An application (or version of an existing conventional application) that is completely self-contained and requires nothing to be already installed. It is coded to have all necessary components included, or is designed to keep all necessary files within its own directory, and will not create a dependency problem. These are often able to run independently of the system to which they are connected. Applications in

RISC OS

and the

ROX Desktop

for Linux use

application directories

, which work in much the same way: programs and their dependencies are self-contained in their own directories (folders).

This method of distribution has also proven useful when porting applications designed for

Unix-like

platforms to Windows, the most noticeable drawback being multiple installations of the same

shared libraries

. For example, Windows installers for

gedit

,

GIMP

, and

HexChat

all include identical copies of the

GTK

toolkit, which these programs use to render widgets. On the other hand, if different versions of GTK are required by each application, then this is the correct behavior and successfully avoids dependency hell.

## Platform-specific

On specific computing platforms, *dependency hell* often goes by a local specific name, generally the name of components.

- DLL hell – a form of dependency hell occurring on 16-bit Microsoft Windows.
- Extension conflict – a form of dependency hell occurring on the classic Mac OS.
- JAR hell – a form of dependency hell occurring in the Java Runtime Environment before build tools like Apache Maven solved this problem in 2004.
- RPM hell – a form of dependency hell occurring in the Red Hat distribution of Linux and other distributions that use RPM as a package manager.
