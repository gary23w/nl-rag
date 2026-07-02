---
title: "Linux kernel (part 1/2)"
source: https://en.wikipedia.org/wiki/Linux_kernel
domain: landlock-lsm
license: CC-BY-SA-4.0
tags: landlock unprivileged sandbox, filesystem access restriction, self restricting process sandbox, linux security module ruleset
fetched: 2026-07-02
part: 1/2
---

# Linux kernel

The **Linux kernel** is a free and open-source Unix-like kernel that is used in many computer systems worldwide. The kernel was created by Linus Torvalds in 1991 and was soon adopted as the kernel for the GNU operating system (OS), which was created to be a free replacement for Unix. Since the late 1990s, it has been included in many operating system distributions, many of which are called Linux. One such Linux kernel operating system is Android, which is used in many mobile and embedded devices.

Most of the kernel code is written in C as supported by the GNU Compiler Collection (GCC), which has extensions beyond standard C. The code also contains assembly code for architecture-specific logic such as optimizing memory use and task execution. The kernel has a modular design such that modules can be integrated as software components – including dynamically loaded. The kernel is monolithic in an architectural sense since the entire OS kernel runs in kernel space.

Linux is provided under the GNU General Public License version 2, although it contains files under other compatible licenses.


## History

In 1991, Linus Torvalds was a computer science student enrolled at the University of Helsinki. During his time there, he began to develop an operating system as a side-project inspired by UNIX, for a personal computer. He started with a task switcher in Intel 80386 assembly language and a terminal driver. On 25 August 1991, Torvalds posted the following to *comp.os.minix*, a newsgroup on Usenet:

> I'm doing a (free) operating system (just a hobby, won't be big and professional like gnu) for 386(486) AT clones. This has been brewing since April, and is starting to get ready. I'd like any feedback on things people like/dislike in minix, as my OS resembles it somewhat (same physical layout of the file-system (due to practical reasons) among other things). I've currently ported bash(1.08) and gcc(1.40), and things seem to work. This implies that I'll get something practical within a few months [...] Yes - it's free of any minix code, and it has a multi-threaded fs. It is NOT protable [*sic*] (uses 386 task switching etc), and it probably never will support anything other than AT-harddisks, as that's all I have :-(.

On 17 September 1991, Torvalds prepared version 0.01 of Linux and put on the "ftp.funet.fi" – FTP server of the Finnish University and Research Network (FUNET). It was not even executable since its code still needed Minix to compile and test it.

On 5 October 1991, Torvalds announced the first "official" version of Linux, version 0.02.

> [As] I mentioned a month ago, I'm working on a free version of a Minix-lookalike for AT-386 computers. It has finally reached the stage where it's even usable (though may not be depending on what you want), and I am willing to put out the sources for wider distribution. It is just version 0.02...but I've successfully run bash, gcc, gnu-make, gnu-sed, compress, etc. under it.

At the time, the GNU Project had completed many components for its free UNIX replacement, GNU, but its kernel, the GNU Hurd, was incomplete. The project adopted the Linux kernel for its OS.

Torvalds labeled the kernel with major version 0 to indicate that it was not yet intended for general use. Version 0.11, released in December 1991, was the first version to be self-hosted; compiled on a computer running the Linux kernel.

When Torvalds released version 0.12 in January 1992, he adopted the GNU General Public License version 2 (GPLv2) over his previous self-drafted license, which had not permitted commercial redistribution. GPL took effect as of 1 February 1992. In contrast to Unix, all Linux source files are freely available, including device drivers.

The initial success of Linux was driven by programmers and testers across the world. Because Linux implemented Unix-like system call semantics and exposed the standard POSIX APIs through an implementation of the C standard library, Linux could run software and applications that had been originally developed for Unix.

On 19 January 1992, the first post to the new newsgroup *alt.os.linux* was submitted. On 31 March 1992, the newsgroup was renamed *comp.os.linux*.

The fact that Linux is a monolithic kernel rather than a microkernel was the topic of a debate between Andrew S. Tanenbaum, the creator of MINIX, and Torvalds. The Tanenbaum–Torvalds debate started in 1992 on the Usenet group *comp.os.minix* as a general discussion about kernel architectures.

Version 0.96 released in May 1992 was the first capable of running the X Window System. In March 1994, Linux 1.0.0 was released with 176,250 lines of code. As indicated by the version number, it was the first version considered suitable for a production environment. In June 1996, after release 1.3, Torvalds decided that Linux had evolved enough to warrant a new major number, and so labeled the next release as version 2.0.0. Significant features of 2.0 included symmetric multiprocessing (SMP), support for more processors types and support for selecting specific hardware targets and for enabling architecture-specific features and optimizations. The *make *config* family of commands of *kbuild* enable and configure options for building ad hoc kernel executables (vmlinux) and loadable modules.

Version 2.2, released on 20 January 1999, improved locking granularity and SMP management, added m68k, PowerPC, Sparc64, Alpha, and other 64-bit platforms support. Furthermore, it added new file systems including Microsoft's NTFS read-only capability. In 1999, IBM published its patches to the Linux 2.2.13 code for the support of the S/390 architecture.

Version 2.4.0, released on 4 January 2001, contained support for ISA Plug and Play, USB, and PC Cards. Linux 2.4 added support for the Pentium 4 and Itanium (the latter introduced the ia64 ISA that was jointly developed by Intel and Hewlett-Packard to supersede the older PA-RISC), and for the newer 64-bit MIPS processor. Development for 2.4.*x* changed a bit in that more features were made available throughout the series, including support for Bluetooth, Logical Volume Manager (LVM) version 1, RAID support, InterMezzo and ext3 file systems.

Version 2.6.0 was released on 17 December 2003. The development for 2.6.*x* changed further towards including new features throughout the series. Among the changes that have been made in the 2.6 series are: integration of μClinux into the mainline kernel sources, PAE support, support for several new lines of CPUs, integration of Advanced Linux Sound Architecture (ALSA) into the mainline kernel sources, support for up to 232 users (up from 216), support for up to 229 process IDs (64-bit only, 32-bit architectures still limited to 215), substantially increased the number of device types and the number of devices of each type, improved 64-bit support, support for file systems that support file sizes of up to 16 terabytes, in-kernel preemption, support for the Native POSIX Thread Library (NPTL), User-mode Linux integration into the mainline kernel sources, SELinux integration into the mainline kernel sources, InfiniBand support, and considerably more.

Starting with 2.6.x releases, the kernel supported a large number of file systems. Some were designed for Linux, like ext3, ext4, FUSE, and Btrfs. Others were native to other operating systems like JFS, XFS, Minix, Xenix, Irix, Solaris, System V, Windows, and MS-DOS.

Though development had not used a version control system thus far, in 2002, Linux developers adopted BitKeeper, which was made freely available to them even though it was not free software. In 2005, because of efforts to reverse-engineer it, the company that owned the software revoked its support of the Linux community. In response, Torvalds and others wrote Git. The new system was written within weeks, and in two months the first official kernel made using it was released.

In 2005 the *stable team* was formed as a response to the lack of a kernel tree where people could work on bug fixes, and it would keep updating *stable* versions. In February 2008 the *linux-next* tree was created to serve as a place where patches aimed to be merged during the next development cycle gathered. Several subsystem maintainers also adopted the suffix *-next* for trees containing code that they mean to submit for inclusion in the next release cycle. As of January 2014, the in-development version of Linux is held in an unstable branch named *linux-next*.

The 20th anniversary of Linux was celebrated by Torvalds in July 2011 with the release of version 3.0.0. As 2.6 had been the version number for 8 years, a new *uname26* personality that reports 3.x as 2.6.40+x had to be added to the kernel so that old programs would work.

Version 3.0 was released on 22 July 2011. On 30 May 2011, Torvalds announced that the big change was "NOTHING. Absolutely nothing." and asked, "...let's make sure we really make the next release not just an all new shiny number, but a good kernel too." After the expected 6–7 weeks of the development process, it would be released near the 20th anniversary of Linux.

On 11 December 2012, Torvalds decided to reduce kernel complexity by removing support for i386 processors—specifically by not having to emulate the atomic CMPXCHG instruction introduced with the i486 to allow reliable mutexes—making the 3.7 kernel series the last one still supporting the original processor. The same series unified support for the ARM processor.

The numbering change from 2.6.39 to 3.0, and from 3.19 to 4.0, involved no meaningful technical differentiation; the major version number was increased simply to avoid large minor numbers. Stable 3.x.y kernels were released until 3.19 in February 2015. Version 3.11, released on 2 September 2013, added many new features such as the new O_TMPFILE flag for `open(2)` to reduce temporary file vulnerabilities, experimental AMD Radeon dynamic power management, low-latency network polling, and zswap (compressed swap cache).

In April 2015, Torvalds released kernel version 4.0. By February 2015, Linux had received contributions from nearly 12,000 programmers from more than 1,200 companies, including some of the world's largest software and hardware vendors. Version 4.1 of Linux, released in June 2015, contains over 19.5 million lines of code contributed by almost 14,000 programmers.

Linus Torvalds announced that kernel version 4.22 would instead be numbered 5.0 in March 2019, stating that "'5.0' doesn't mean anything more than that the 4.x numbers started getting big enough that I ran out of fingers and toes." It featured many major additions such as support for the AMD Radeon FreeSync and NVIDIA Xavier display, fixes for F2FS, EXT4 and XFS, restored support for swap files on the Btrfs file system and continued work on the Intel Icelake Gen11 graphics and on the NXP i.MX8 SoCs. This release was noticeably larger than the rest, Torvalds mentioning that "The overall changes for all of the 5.0 release are much bigger."

A total of 1,991 developers, of whom 334 were first-time collaborators, added more than 553,000 lines of code to version 5.8, breaking the record previously held by version 4.9.


## Popularity

According to the Stack Overflow's annual Developer Survey of 2019, more than 53% of all respondents have developed software for Linux and about 27% for Android, although only about 25% develop with Linux-based operating systems.

Most websites run on Linux-based operating systems, and all of the world's 500 most powerful supercomputers run on Linux.

Linux distributions bundle the kernel with system software (e.g., the GNU C Library, systemd, and other Unix utilities and daemons) and a wide selection of application software, but their usage share in desktops is low in comparison to other operating systems.

Android, which runs on a modified Linux kernel, accounts for the majority of mobile device operating systems, and is increasingly being used in embedded devices, making it a significant driver of Linux adoption.


## Value

The cost to redevelop version 2.6.0 of the Linux kernel in a traditional proprietary development setting has been estimated to be US$612 million (€467M, £394M) in 2004 prices using the COCOMO person-month estimation model. In 2006, a study funded by the European Union put the redevelopment cost of kernel version 2.6.8 higher, at €882M ($1.14bn, £744M).

This topic was revisited in October 2008 by Amanda McPherson, Brian Proffitt, and Ron Hale-Evans. Using David A. Wheeler's methodology, they estimated redevelopment of the 2.6.25 kernel now costs $1.3bn (part of a total $10.8bn to redevelop Fedora 9). Again, Garcia-Garcia and Alonso de Magdaleno from University of Oviedo (Spain) estimate that the value annually added to kernel was about €100M between 2005 and 2007 and €225M in 2008, it would cost also more than €1bn (about $1.4bn as of February 2010) to develop in the European Union.

As of 7 March 2011, using then-current LOC (lines of code) of a 2.6.x Linux kernel and wage numbers with David A. Wheeler's calculations it would cost approximately $3bn (about €2.2bn) to redevelop the Linux kernel as it keeps getting bigger. An updated calculation as of 26 September 2018, using then-current 20,088,609 LOC (lines of code) for the 4.14.14 Linux kernel and the current US national average programmer salary of $75,506 show that it would cost approximately $14,725,449,000 (£11,191,341,000) to rewrite the existing code.


## Distribution

Most who use Linux do so via a Linux distribution. Some distributions ship the vanilla or stable kernel. Several vendors (such as Red Hat and Debian) maintain a customized source tree. These are usually updated at a slower pace than the vanilla branch, and they usually include all fixes from the relevant stable branch, but at the same time they can also add support for drivers or features that had not been released in the vanilla version the distribution vendor started basing its branch from.


## Developers

### Community

Graph of the sizes of Linux Kernel versions in millions of lines of code.

View

source data

.

The community of Linux kernel developers comprises about 5000–6000 members. According to the "2017 State of Linux Kernel Development", a study issued by the Linux Foundation, covering the commits for the releases 4.8 to 4.13, about 1500 developers were contributing from about 200–250 companies on average. The top 30 developers contributed a little more than 16% of the code. For companies, the top contributors are Intel (13.1%) and Red Hat (7.2%), Linaro (5.6%), IBM (4.1%), the second and fifth places are held by the 'none' (8.2%) and 'unknown' (4.1%) categories.

> "Instead of a roadmap, there are technical guidelines. Instead of a central resource allocation, there are persons and companies who all have a stake in the further development of the Linux kernel, quite independently from one another: People like Linus Torvalds and I don’t plan the kernel evolution. We don’t sit there and think up the roadmap for the next two years, then assign resources to the various new features. That's because we don’t have any resources. The resources are all owned by the various corporations who use and contribute to Linux, as well as by the various independent contributors out there. It's those people who own the resources who decide..."

— Andrew Morton, 2005

Intel

None

Red Hat

Linaro

Unknown

IBM

Consultants

Samsung

SUSE

Google

nearly 500 other

companies

Corporate affiliation of contributions to the Linux kernel, 4.8–4.13

### Conflict

Notable conflicts among Linux kernel developers:

- In July 2007, Con Kolivas announced that he would cease developing for the Linux kernel.
- In July 2009, Alan Cox quit his role as the TTY layer maintainer after disagreement with Torvalds.
- In December 2010, there was a discussion between Linux SCSI maintainer James Bottomley and SCST maintainer Vladislav Bolkhovitin about which SCSI target stack should be included in the Linux kernel. This made some Linux users upset.
- In June 2012, Torvalds made it very clear that he did not agree with NVIDIA releasing its drivers as closed.
- In April 2014, Torvalds banned Kay Sievers from submitting patches to the Linux kernel for failing to deal with bugs that caused systemd to negatively interact with the kernel.
- In October 2014, Lennart Poettering accused Torvalds of tolerating the rough discussion style on Linux kernel related mailing lists and of being a bad role model.
- In March 2015, Christoph Hellwig filed a lawsuit against VMware for infringement of the copyright on the Linux kernel. Linus Torvalds made it clear that he did not agree with this and similar initiatives by calling lawyers a festering disease.
- In April 2021, a team from the University of Minnesota was found to be submitting "bad faith" patches to the kernel as part of its research. This resulted in the immediate reversion of all patches ever submitted by a member of the university. In addition, a warning was issued by a senior maintainer that any future patch from the university would be rejected on sight.
- In February 2025, Hector Martin resigned as maintainer of the Asahi Linux project (that added support for Apple silicon systems to Linux) and related kernel subsystems over disagreements about the use of the Rust programming language in the kernel.
- In June 2025, the Bcachefs filesystem was creating tension with Torvalds and in September 2025 it was removed from the Linux kernel starting with version 6.18.

Prominent Linux kernel developers have been aware of the importance of avoiding conflicts between developers. For a long time there was no code of conduct for kernel developers due to opposition by Torvalds. A Linux Kernel *Code of Conflict* was introduced on 8 March 2015. It was replaced on 16 September 2018 by a new *Code of Conduct* based on the Contributor Covenant. This coincided with a public apology by Torvalds and a brief break from kernel development. On 30 November 2018, complying with the *Code of Conduct*, Jarkko Sakkinen of Intel sent out patches replacing instances of "fuck" appearing in source code comments with suitable versions focused on the word 'hug'.

Developers who feel treated unfairly can report this to the Linux Foundation Technical Advisory Board. In July 2013, the maintainer of the USB 3.0 driver Sage Sharp asked Torvalds to address the abusive commentary in the kernel development community. In 2014, Sharp backed out of Linux kernel development, saying that "The focus on technical excellence, in combination with overloaded maintainers, and people with different cultural and social norms, means that Linux kernel maintainers are often blunt, rude, or brutal to get their job done". At the linux.conf.au (LCA) conference in 2018, developers expressed the view that the culture of the community has gotten much better in the past few years. Daniel Vetter, the maintainer of the Intel drm/i915 graphics kernel driver, commented that the "rather violent language and discussion" in the kernel community has decreased or disappeared.

Laurent Pinchart asked developers for feedback on their experiences with the kernel community at the 2017 Embedded Linux Conference Europe. The issues brought up were discussed a few days later at the Maintainers Summit. Concerns over the lack of consistency in how maintainers responded to patches submitted by developers were echoed by Shuah Khan, the maintainer of the kernel self-test framework. Torvalds contended that there would never be consistency in the handling of patches because different kernel subsystems have, over time, adopted different development processes. Therefore, it was agreed upon that each kernel subsystem maintainer would document the rules for patch acceptance.


## Development

> Linux is evolution, not intelligent design!

— Linus Torvalds, 2005

### Codebase

The kernel source code, a.k.a. source tree, is managed in the Git version control system – also created by Torvalds.

As of 2021, the 5.11 release of the Linux kernel had around 30.34 million lines of code. Roughly 14% of the code is part of the "core," including architecture-specific code, kernel code, and memory management code, while 60% is drivers.

### Contributions

Contributions are submitted as patches, in the form of text messages on the Linux kernel mailing list (LKML) (and often also on other mailing lists dedicated to particular subsystems). The patches must conform to a set of rules and to a formal language that, among other things, describes which lines of code are to be deleted and what others are to be added to the specified files. These patches can be automatically processed so that system administrators can apply them in order to make just some changes to the code or to incrementally upgrade to the next version. Linux is distributed also in GNU zip (gzip) and bzip2 formats.

A developer who wants to change the Linux kernel writes and tests a code change. Depending on how significant the change is and how many subsystems it modifies, the change will either be submitted as a single patch or in multiple patches of source code. In case of a single subsystem that is maintained by a single maintainer, these patches are sent as e-mails to the maintainer of the subsystem with the appropriate mailing list in Cc. The maintainer and the readers of the mailing list will review the patches and provide feedback. Once the review process has finished the subsystem maintainer accepts the patches in the relevant Git kernel tree. If the changes to the Linux kernel are bug fixes that are considered important enough, a pull request for the patches will be sent to Torvalds within a few days. Otherwise, a pull request will be sent to Torvalds during the next merge window. The merge window usually lasts two weeks and starts immediately after the release of the previous kernel version. The Git kernel source tree names all developers who have contributed to the Linux kernel in the *Credits* directory and all subsystem maintainers are listed in *Maintainers*.

As with many large open-source software projects, developers are required to adhere to the Contributor Covenant, a code of conduct intended to address harassment of minority contributors. Additionally, to prevent offense the use of inclusive terminology within the source code is mandated.

### Programming language

Linux is written in a special C programming language supported by GCC, a compiler that extends the C standard in many ways, for example using inline sections of code written in the assembly language (in GCC's "AT&T-style" syntax) of the target architecture.

In September 2021, the GCC version requirement for compiling and building the Linux kernel increased from GCC 4.9 to 5.1, allowing the potential for the kernel to be moved from using C code based on the C89 standard to using code written with the C11 standard, with the migration to the standard taking place in March 2022, with the release of Linux 5.18.

Initial support for the Rust programming language was added in Linux 6.1, which was released in December 2022, with later kernel versions, such as Linux 6.2 and Linux 6.3, further improving the support.

### Coding style

Since 2002, code must adhere to the 21 rules of the *Linux Kernel Coding Style.*

### Versioning

As for most software, the kernel is versioned as a series of dot-separated numbers.

For early versions, the version consisted of three or four dot-separated numbers called *major release*, *minor release* and *revision.* At that time, odd-numbered minor releases were for development and testing, while even numbered minor releases for production. The optional fourth digit indicated a patch level. Development releases were indicated with a release candidate suffix (*-rc*).

The current versioning conventions are different. The odd/even number implying dev/prod has been dropped, and a major version is indicated by the first two numbers together. While the time-frame is open for the development of the next major, the -rcN suffix is used to identify the n'th release candidate for the next version. For example, the release of the version 4.16 was preceded by seven 4.16-rcN (from -rc1 to -rc7). Once a stable version is released, its maintenance is passed to the *stable team*. Updates to a stable release are identified by a three-number scheme (e.g., 4.16.1, 4.16.2, ...).

### Toolchain

The kernel is usually built with the GNU toolchain. The GNU C compiler, GNU cc, part of the GNU Compiler Collection (GCC), is the default compiler for mainline Linux. Sequencing is handled by GNU make. The GNU Assembler (often called GAS or GNU as) outputs the object files from the GCC generated assembly code. Finally, the GNU Linker (GNU ld) produces a statically linked executable kernel file called vmlinux. Both as and ld are part of GNU Binary Utilities (binutils).

GNU cc was for a long time the only compiler capable of correctly building Linux. In 2004, Intel claimed to have modified the kernel so that its C compiler was also capable of compiling it. There was another such reported success in 2009, with a modified 2.6.22 version. Support for the Intel compiler has been dropped in 2023.

Since 2010, effort has been underway to build Linux with Clang, an alternative compiler for the C language; as of 12 April 2014, the official kernel could almost be compiled by Clang. The project dedicated to this effort is named *LLVMLinux* after the LLVM compiler infrastructure upon which Clang is built. LLVMLinux does not aim to fork either Linux or the LLVM, therefore it is a meta-project composed of patches that are eventually submitted to the upstream projects. By enabling Linux to be compiled by Clang, developers may benefit from shorter compilation times.

In 2017, developers completed upstreaming patches to support building the Linux kernel with Clang in the 4.15 release, having backported support for X86-64 and AArch64 to the 4.4, 4.9, and 4.14 branches of the stable kernel tree. Google's Pixel 2 shipped with the first Clang built Linux kernel, though patches for Pixel (1st generation) did exist. 2018 saw ChromeOS move to building kernels with Clang by default, while Android made Clang and LLVM's linker LLD required for kernel builds in 2019. Google moved its production kernel used throughout its datacenters to being built with Clang in 2020. The *ClangBuiltLinux* group coordinates fixes to both Linux and LLVM to ensure compatibility, both composed of members from *LLVMLinux* and having upstreamed patches from *LLVMLinux*.

### Debugging

As with any software, problems with the Linux kernel can be difficult to troubleshoot. Common challenges relate to userspace vs. kernel space access, misuse of synchronization primitives, and incorrect hardware management.

An oops is a non-fatal error in the kernel. After such an error, operations continue with suspect reliability.

A panic (generated by panic()) is a fatal error. After such an error, the kernel prints a message and halts the computer.

The kernel provides for *debugging by printing* via printk(), which stores messages in a circular buffer (overwriting older entries with newer). The syslog(2) system call provides for reading and clearing the message buffer and for setting the maximum *log level* of the messages to be sent to the console. Kernel messages are also exported to userland through the */dev/kmsg* interface.

The *ftrace* mechanism allow for debugging by tracing. It is used for monitoring and debugging Linux at runtime and it can analyze user space latencies due to kernel misbehavior. Furthermore, *ftrace* allows users to trace Linux at boot-time.

*kprobes* and *kretprobes* can break into kernel execution (like debuggers in userspace) and collect information non-disruptively. *kprobes* can be inserted into code at (almost) any address, while kretprobes work at function return. *uprobes* have similar purposes but they also have some differences in usage and implementation.

With KGDB Linux can be debugged in much the same way as userspace programs. KGDB requires an additional machine that runs GDB and that is connected to the target to be debugged using a serial cable or Ethernet.

### Change process

The Linux kernel project integrates new code on a rolling basis. Standard operating procedure is that software checked into the project must work and compile without error.

Each kernel subsystem is assigned a maintainer who is responsible for reviewing patches against the kernel code standards and keeping a queue of patches that can be submitted to Torvalds within a merge window that is usually several weeks.

Patches are merged by Torvalds into the source code of the prior stable Linux kernel release, creating the release candidate (-rc) for the next stable release. Once the merge window is closed, only fixes to the new code in the development release are accepted. The -rc development release of the kernel goes through regression testing and once it is considered stable by Torvalds and the subsystem maintainers, a new version is released and the development process starts over again.

### Mainline Linux

The Git tree that contains the Linux kernel source code is referred to as **mainline Linux**. Every stable kernel release originates from the mainline tree, and is frequently published on kernel.org. Mainline Linux has only solid support for a small subset of the many devices that run Linux. Non-mainline support is provided by independent projects, such as Yocto or Linaro, but in many cases the kernel from the device vendor is needed. Using a vendor kernel likely requires a board support package.

Maintaining a kernel tree outside of mainline Linux has proven to be difficult.

*Mainlining* refers to the effort of adding support for a device to the mainline kernel, while there was formerly only support in a fork or no support at all. This usually includes adding drivers or device tree files. When this is finished, the feature or security fix is considered *mainlined*.

### Linux-like kernel

The maintainer of the stable branch, Greg Kroah-Hartman, has applied the term *Linux-like* to downstream kernel forks by vendors that add millions of lines of code to the mainline kernel. In 2019, Google stated that it wanted to use the mainline Linux kernel in Android so the number of kernel forks would be reduced. The term Linux-like has also been applied to the Embeddable Linux Kernel Subset, which does not include the full mainline Linux kernel but a small modified subset of the code.

### Linux forks

There are certain communities that develop kernels based on the official Linux. Some interesting bits of code from these forks that include Linux-libre, Compute Node Linux, INK, L4Linux, RTLinux, and User-Mode Linux (UML) have been merged into the mainline. Some operating systems developed for mobile phones initially used heavily modified versions of Linux, including Google Android, Firefox OS, HP webOS, Nokia Maemo and Jolla Sailfish OS. In 2010, the Linux community criticised Google for effectively starting its own kernel tree:

> This means that any drivers written for Android hardware platforms, can not get merged into the main kernel tree because they have dependencies on code that only lives in Google's kernel tree, causing it to fail to build in the kernel.org tree. Because of this, Google has now prevented a large chunk of hardware drivers and platform code from ever getting merged into the main kernel tree. Effectively creating a kernel branch that a number of different vendors are now relying on.

— Greg Kroah-Hartman, 2010

Today Android uses a customized Linux where major changes are implemented in device drivers, but some changes to the core kernel code is required. Android developers also submit patches to the official Linux that finally can boot the Android operating system. For example, a Nexus 7 can boot and run the mainline Linux.

At a 2001 presentation at the Computer History Museum, Torvalds had this to say in response to a question about distributions of Linux using precisely the same kernel sources or not:

> They're not... well they are, and they're not. There is no single kernel. Every single distribution has their own changes. That's been going on since pretty much day one. I don't know if you may remember Yggdrasil was known for having quite extreme changes to the kernel and even today all of the major vendors have their own tweaks because they have some portion of the market they're interested in and quite frankly that's how it should be. Because if everybody expects one person, me, to be able to track everything that's not the point of GPL. That's not the point of having an open system. So actually the fact that a distribution decides that something is so important to them that they will add patches for even when it's not in the standard kernel, that's a really good sign for me. So that's for example how something like ReiserFS got added. And the reason why ReiserFS is the first journaling filesystem that was integrated in the standard kernel was not because I love Hans Reiser. It was because SUSE actually started shipping with ReiserFS as their standard kernel, which told me "ok." This is actually in production use. Normal People are doing this. They must know something I don't know. So in a very real sense what a lot of distribution houses do, they are part of this "let's make our own branch" and "let's make our changes to this." And because of the GPL, I can take the best portions of them.

— Linus Torvalds, 2001

### Long-term support

The latest version and older versions are maintained separately. Most of the latest kernel releases were supervised by Torvalds.

The Linux kernel developer community maintains a stable kernel by applying fixes for software bugs that have been discovered during the development of the subsequent stable kernel. Therefore, www.kernel.org always lists two stable kernels. The next stable Linux kernel is released about 8 to 12 weeks later.

Some releases are designated for long-term support as *longterm* with bug fix releases for two or more years.

### Size

Some projects have attempted to reduce the size of the Linux kernel. One of them is TinyLinux. In 2014, Josh Triplett started the -tiny source tree for a reduced size version.
