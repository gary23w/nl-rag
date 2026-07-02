---
title: "Multics"
source: https://en.wikipedia.org/wiki/Multics
domain: bcpl-b-language
license: CC-BY-SA-4.0
tags: bcpl language, b language, martin richards, bootstrapping compilers, systems programming
fetched: 2026-07-02
---

# Multics

**Multics** ("**Multiplexed Information and Computing Service**") is an influential early time-sharing operating system based on the concept of a single-level memory. It has been written that Multics "has influenced all modern operating systems since, from microcomputers to mainframes."

Initial planning and development for Multics started in 1964, in Cambridge, Massachusetts. Originally it was a cooperative project led by MIT (Project MAC with Fernando Corbató) along with General Electric and Bell Labs. It was developed on the GE 645 computer, which was specially designed for it; the first one was delivered to MIT in January 1967. GE offered their earlier GE 635 systems with the Dartmouth Time-Sharing System, which they called "Mark I" and intended to offer the 645 with Multics as a larger successor. Bell withdrew from the project in 1969 as it became clear it would not deliver a working system in the short term. Shortly thereafter, GE decided to exit the computer industry entirely and sold the division to Honeywell in 1970. Honeywell offered Multics commercially, but with limited success.

Multics has numerous features intended to ensure high availability so that it would support a computing utility similar to the telephone and electricity utilities. Modular hardware structure and software architecture are used to achieve this. The system can grow in size by simply adding more of the appropriate resource, be it computing power, main memory, or disk storage. Separate access control lists on every file provide flexible information sharing, but complete privacy when needed. Multics has a number of standard mechanisms to allow engineers to analyze the performance of the system, as well as a number of adaptive performance optimization mechanisms.

Due to its many novel and valuable ideas, Multics has had a significant influence on computer science despite its faults. Its most lasting effect on the computer industry was to inspire the creation of Unix, which carried forward many Multics features, but was able to run on less expensive hardware. Unix was developed at Bell to allow their Multics team to continue their research using smaller machines, first a PDP-7 and ultimately the PDP-11.

## Novel ideas

Multics implements a single-level store for data access, discarding the clear distinction between files (called *segments* in Multics) and *process memory*. The memory of a process consists solely of segments that were mapped into its address space. To read or write to them, the process simply uses normal central processing unit (CPU) instructions, and the operating system takes care of making sure that all the modifications were saved to disk. In POSIX terminology, it is as if every file were `mmap()`ed; however, in Multics there is no concept of *process memory*, separate from the memory used to hold mapped-in files, as Unix has. *All* memory in the system is part of *some* segment, which appears in the file system; this includes the temporary scratch memory of the process, its kernel stack, etc.

Segments are limited to 256 kilowords, just over 1 MB, because Multics hardware had 18-bit word addresses for the content of a segment. Larger files are "multisegment files" and are handled differently. The 256 kiloword limit was rarely encountered in practice, because at the time, one megabyte of memory was prohibitively expensive.

Another major new idea of Multics was dynamic linking, in which a running process can make external routines available by adding the segments containing them to its address space. This allows applications to always use the latest version of any external routine, since those routines are kept in other segments, which are dynamically linked only when a process first attempts to begin execution in them. Since different processes can use different search rules, different users can end up using different versions of external routines. Equally importantly, with the appropriate settings in the Multics security facilities, the code in the other segment can gain access to data structures maintained in a different process. Dynamic linking in Multics does not require special dynamic-link libraries (DLLs); a program can dynamically link to any executable segment to which it has access rights.

Thus, to interact with an application running in part as a daemon (in another process), a user's process simply performs a normal procedure-call instruction to a code segment to which it had dynamically linked (a code segment that implemented some operation associated with the daemon). The code in that segment can then modify data maintained and used in the daemon. When the action necessary to commence the request is completed, a simple procedure return instruction returns control of the user's process to the user's code.

Multics also supports extremely aggressive on-line reconfiguration: central processing units, memory banks, disk drives, etc. can be added and removed while the system continues operating. At the MIT system, where most early software development was done, it was common practice to split the multiprocessor system into two separate systems during off-hours by incrementally removing enough components to form a second working system, leaving the rest still running for the original logged-in users. System software development testing could be done on the second system, then the components of the second system were added back to the main user system, without ever having shut it down. Multics is one of the earliest multiprocessor systems.

Multics is the first major operating system to be designed as a secure system from the outset. Despite this, early versions of Multics were compromised repeatedly. This led to further work that made the system more secure, and prefigured modern security engineering techniques. Break-ins became very rare once the second-generation hardware base was adopted; it has hardware support for ring-oriented security, a multilevel refinement of the concept of master mode. A US Air Force tiger team project tested Multics security in 1973 under the codeword ZARF. On 28 May 1997, the American National Security Agency declassified this use of the codeword ZARF.

Multics is the first operating system to provide a hierarchical file system, and file names can be of almost arbitrary length and syntax. A given file or directory can have multiple names (typically a long and short form), and symbolic links between directories are also supported. Multics is the first to use the now-standard concept of per-process stacks in the kernel, with a separate stack for each security ring. It is also the first to have a command processor implemented as ordinary user code – an idea later used in the Unix shell. It is also one of the first written in a high-level language (Multics PL/I), after the Burroughs MCP system written in ESPOL, an expanded version of ALGOL.

The deployment of Multics into secure computing environments also spurred the development of innovative supporting applications. In 1975, Morrie Gasser of MITRE Corporation developed a pronounceable random word generator to address password requirements of installations such as the Air Force Data Services Center (AFDSC) processing classified information. To avoid guessable passwords, the AFDSC decided to assign passwords but concluded the manual assignment required too much administrative overhead. Thus, a random word generator was researched and then developed in PL/I. Instead of being based on phonemes or individual letters or clarities, the system employed phonemic segments (second order approximations of English) and other rules to enhance pronounceability and randomness, which was statistically modeled against other approaches. A descendant of this generator was added to Multics during Project Guardian.

## Project history

In 1964, Multics was developed initially for the GE-645 mainframe, a 36-bit system. GE's computer business, including Multics, was taken over by Honeywell in 1970; around 1973, Multics was supported on the Honeywell 6180 machines, which included security improvements including hardware support for protection rings.

Bell Labs pulled out of the project in 1969 when it became clear that it would not produce a working system in the near future; some of the people who had worked on it there went on to create the Unix system. Multics development continued at MIT and General Electric. At MIT in 1975, use of Multics was declining, and it did not recover by 1976 to prior levels. Finally by slashing prices, MIT managed to lure users back to Multics in 1978.

In 1974 Honeywell entered into a development contract with the Air Force (with MIT as a sub-contractor) to develop a security kernel for Multics. This would involve reducing the size of the Multics hardcore by moving specific components of the supervisor out of Ring 0. One of the initial steps after carrying out a security evaluation was the implementation of a multilevel security framework within Multics called AIM (Access Isolation Mechanism). This provided mandatory access control which could be enabled to supplement the already existing discretionary access control that Multics already possessed. The resulting Project Guardian ran until termination in 1976; whilst most of its changes were not added to Multics, some parts of the project such as the proposed Secure Front End Processor was productized by Honeywell as SCOMP (Secure Communications Processor). In 1985 the US Department of Defense awarded STOP 2.1 an A1 security classification. The SCOMP and its STOP operating system eventually evolved via XTS-200 and XTS-300 into current XTS-400 offering of secure operating systems.

Honeywell continued system development until 1985. About 80 multimillion-dollar sites were installed, at universities, industry, and government sites. The French university system had several installations in the early 1980s. After Honeywell stopped supporting Multics, users migrated to other systems, such as Unix. Honeywell later slowly sold its Information Systems division (including rights to Multics) into a joint venture with Bull, and with NEC also participated, in 1986.

In 1985, Multics was issued certification as a B2 level secure operating system using the Trusted Computer System Evaluation Criteria from the National Computer Security Center (NCSC), a division of the NSA; it was the first operating system evaluated to this level.

Multics was distributed from 1975 to 2000 by Groupe Bull in Europe, and by Bull HN Information Systems Inc. (the legal name of what formerly known as Honeywell Information Systems Inc. and Honeywell Bull Inc.) in the United States. In 2006, Bull SAS released the source code of Multics versions MR10.2, MR11.0, MR12.0, MR12.1, MR12.2, MR12.3, MR12.4 & MR12.5 under a free software license.

The last known Multics installation running natively on Honeywell hardware was shut down on October 30, 2000, at the Canadian Department of National Defence in Halifax, Nova Scotia, Canada.

### Current status

In 2006 Bull HN released the source code for MR12.5, the final 1992 Multics release, to MIT. Most of the system is now available as free software with the exception of some optional pieces such as TCP/IP.

In 2014, Multics was successfully run on current hardware using an emulator created by Multicians Harry Reed and Charles Anthony. The 1.0 release of the emulator is available as of 2017. MR12.6f accompanies the 1.0 release of the emulator, and adds a few new features, including command line recall and editing using the video system.

In August 2023, MR12.8 was released with various fixes and improvements.

## Commands

The following is a list of programs and commands for common computing tasks that are supported by the Multics command-line interface.

### File and directory access commands

- change_wdir (cwd) - change the working directory
- create_dir (cd) - create a directory
- copy (cp) - copy files
- list (ls) - list files and directories
- print (pr) - print the contents of a text file
- print_wdir (pwd) - print the working directory
- move (mv) - move a file or directory to a different directory
- rename (rn) - rename a file without moving it

### Text editors

- edm - a simple line editor
- emacs - Multics Emacs
- qedx - a faster version of qed
- teco

### Document formatters

- runoff (rf)

### Compilers, assemblers, and interpreters

- alm
- apl
- basic
- c
- cobol
- fortran (ft)
- pascal
- pl1

### Email

- mail (ml)
- read_mail (rdm)
- send_mail (sdm)

### On-line documentation

- help

### Scripting

- echo
- if

### Data processing

- gcos (gc) - simulator to run GCOS programs
- sort, merge - sorting and merging of text and binary files

### Login sessions

- logout
- who

### Active functions

The Multics shell language supports "active functions", which are similar to commands, but which return a string value. An active function is called by putting the active function name and the arguments to the active function in square brackets [ and ]. The string returned by the active function is substituted into the command in place of the call to the active function. For example, when the command echo [working_dir] is processed, the active function working_dir is run; it returns the full path of the working directory, which is substituted into the command, so that the echo command prints the working directory.

Some programs can act either as commands or as active functions; when run as a command, its result is printed, and when run as an active function, its result is returned as a string.

Some common active functions are:

- ceil - returns the smallest integer greater than or equal to the argument
- floor - returns the largest integer less than or equal to the argument
- home_dir (hd) - returns the home directory
- ltrim
- rtrim
- trunc - returns the integer part of the argument
- working_dir (wd) - returns the working directory

## Retrospective observations

Peter H. Salus, author of a book covering Unix's early years, stated one position: "With Multics they tried to have a much more versatile and flexible operating system, and it failed miserably". This position, however, is said to have been discredited in the computing community because many of Multics' technical innovations are used in modern commercial computing systems.

The permanently resident kernel of Multics, a system derided in its day as being too large and complex, was 135 KB of code. The first MIT GE-645 had 512 kilowords of memory (2 MiB), a truly enormous amount at the time, and the kernel used a moderate portion of Multics main memory.

The entire system, including the operating system and the complex PL/I compiler, user commands, and subroutine libraries, consists of about 1500 source modules. These average roughly 200 lines of source code each, and compile to a total of roughly 4.5 MiB of procedure code, which was fairly large by the standards of the day.

Multics compilers generally optimise more for code density than CPU performance, for example using small sub-routines called *operators* for short standard code sequences, which makes comparison of object code size with modern systems less useful. High code density is a good optimisation choice for Multics as a multi-user system with expensive main memory.

During its commercial product history, it was often commented internally that the Honeywell Information Systems (HIS) (later Honeywell-Bull) sales and marketing staff were more familiar with and comfortable making the business case for Honeywell's other computer line, the DPS 6 running GCOS 6. The DPS-6 and GCOS 6 was a well-regarded and reliable platform for inventory, accounting, word processing, and vertical market applications, such as banking, where it had a sizeable customer base. In contrast, the full potential of Multics’ flexibility for even mundane tasks was not easy to comprehend in that era and its features were generally outside the skill set of contemporary business analysts. The scope of this disconnect was concretized by an anecdote conveyed by Paul Stachour, CNO/CSC:

> When American Telephone and Telegraph was changing its name to just AT&T in 1983, a staffer from Honeywell’s legal department showed up and asked a Multician if he could arrange to have the name changed in all of their computerized documents. When asked when the process could be completed, the Multician replied, "It's done." The staffer repeated that he needed *hundreds perhaps thousands* of documents updated. The Multician explained that he had executed a global search and replace as the staffer was speaking, and the task was in fact completed.

## Influence on other projects

### Unix

The design and features of Multics influenced the Unix operating system, which was originally written by two Multics programmers, Ken Thompson and Dennis Ritchie. Influence of Multics on Unix is evident in many areas, including the hierarchical file system, redirection, the shell, and the naming of some commands. But the internal design philosophy is quite different, focusing on keeping the system small and simple, and so correcting some perceived deficiencies of Multics because of its high resource demands on the limited computer hardware of the time.

The name *Unix* (originally *Unics*) is itself a pun on *Multics*. The *U* in Unix is rumored to stand for *uniplexed* as opposed to the *multiplexed* of Multics, further underscoring the designers' rejections of Multics' complexity in favor of a more straightforward and workable approach for smaller computers. (Garfinkel and Abelson cite an alternative origin: Peter Neumann at Bell Labs, watching a demonstration of the prototype, suggested the pun name UNICS – pronounced "eunuchs" – as a "castrated Multics", although Dennis Ritchie is said to have denied this.)

Ken Thompson, in a transcribed 2007 interview with Peter Seibel refers to Multics as "overdesigned and overbuilt and over everything. It was close to unusable. They [Massachusetts Institute of Technology] still claim it's a monstrous success, but it just clearly wasn't". On the influence of Multics on Unix, Thompson stated that "the things that I liked enough (about Multics) to actually take were the hierarchical file system and the shell — a separate process that you can replace with some other process".

Dennis Ritchie wrote that the design of Unix was influenced by MIT's CTSS, which was the immediate ancestor of Multics.

### Other operating systems

The Prime Computer operating system, PRIMOS, was referred to as "Multics in a shoebox" by William Poduska, a founder of the company. Poduska later moved on to found Apollo Computer, whose AEGIS and later Domain/OS operating systems, sometimes called "Multics in a matchbox", extends the Multics design to a networked graphics workstation environment.

The Stratus VOS operating system of Stratus Computer (now Stratus Technologies) is very strongly influenced by Multics, and both its external user interface and internal structure bear many close resemblances to the older project. The high-reliability, availability, and security features of Multics are extended in Stratus VOS to support a new line of fault tolerant computer systems supporting secure, reliable transaction processing. Stratus VOS is the most directly related descendant of Multics still in active development and production usage today.

General Motors' Multiple Console Time Sharing System (MCTS) for the Control Data Corporation STAR-100 computer was based on Multics.

The protection architecture of Multics, restricting the ability of code at one level of the system to access resources at another, was adopted as the basis for the security features of ICL's VME operating system.

The Edinburgh Multiple Access System (EMAS) draws particularly on the one-level store concept used by Multics, providing access to files only by mapping them into memory. All memory space is associated with a segment.
