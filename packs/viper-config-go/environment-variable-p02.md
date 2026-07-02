---
title: "Environment variable (part 2/2)"
source: https://en.wikipedia.org/wiki/Environment_variable
domain: viper-config-go
license: CC-BY-SA-4.0
tags: viper config, go configuration library, config file go, viper settings loader
fetched: 2026-07-02
part: 2/2
---

## Pseudo-environment variables

The command processors in DOS and Windows also support pseudo-environment variables. These are values that are fetched like environment variables, but are not truly stored in the environment but computed when requested.

### DOS

Besides true environment variables, which are statically stored in the environment until changed or deleted, a number of pseudo-environment variables exist for batch processing.

The so-called *replacement parameters* or *replaceable parameters* (Microsoft / IBM terminology) aka *replacement variables* (Digital Research / Novell / Caldera terminology) or *batch file parameters* (JP Software terminology) `%1`..`%9` and `%0` can be used to retrieve the calling parameters of a batchjob, see `SHIFT`. In batchjobs, they can be retrieved just like environment variables, but are not actually stored in the environment.

Some command-line processors (like DR-DOS `COMMAND.COM`, Multiuser DOS `MDOS.COM`/`TMP.EXE` (Terminal Message Process), JP Software 4DOS, 4OS2, Take Command (formerly 4NT) and Windows cmd.exe) support a type of pseudo-environment variables named *system information variables* (Novell / Caldera terminology) or *internal variables* (JP Software terminology), which can be used to retrieve various possibly dynamic, but read-only information about the running system in batch jobs. The returned values represent the status of the system in the moment these variables are queried; that is, reading them multiple times in a row may return different values even within the same command; querying them has no direct effect on the system. Since they are not stored in the environment, they are not listed by SET and do not exist for external programs to retrieve. If a true environment variable of the same name is defined, it takes precedence over the corresponding variable until the environment variable is deleted again. They are not case-sensitive. While almost all such variables are prefixed with an underscore ("`_`") by 4DOS etc. by convention (f.e. `%_SECOND%`), they are not under DR-DOS `COMMAND.COM` (f.e. `%OS_VERSION%`).

In addition, 4DOS, 4OS2, 4NT, and Take Command also support so called *variable functions*, including user-definable ones. They work just like *internal variables*, but can take optional parameters (f.e. `%@EVAL[]%`) and may even change the system status depending on their function.

*System information variables* supported by DR-DOS `COMMAND.COM`:

**`%AM_PM%`**

This pseudo-variable returns the ante- or post-midday status of the current time. The returned string depends on the locale-specific version of DR-DOS, f.e. "

am

" or "

pm

" in the English version. It resembles an identically named

identifier variable

in

Novell NetWare

login scripts.

**`%DAY%`**

This pseudo-variable returns the days of the current date in a 2-digit format with leading zeros, f.e. "

01

".."

31

". See also the similar pseudo-variable

%_DAY%

. It resembles an identically named

identifier variable

in

Novell NetWare

login scripts.

**`%DAY_OF_WEEK%`**

This pseudo-variable returns the day name of the week in a 3-character format. The returned string depends on the locale-specific version of DR-DOS, f.e. "

Sun

", "

Mon

", "

Tue

", "

Wed

", "

Thu

", "

Fri

", or "

Sat

" in the English version. It resembles an identically named

identifier variable

in

Novell NetWare

login scripts.

**`%ERRORLEVEL%`**

In

COMMAND.COM

of DR-DOS 7.02 and higher, this pseudo-variable returns the last error level returned by an external program or the

RETURN

command, f.e. "

0

".."

255

".

See also the identically named pseudo-variable

%ERRORLEVEL%

under Windows and the

IF ERRORLEVEL

conditional command.

**`%ERRORLVL%`**

In DR-DOS 7.02 and higher, this pseudo-variable returns the last error level in a 3-digit format with leading zeros, f.e. "

000

".."

255

".

Under

Multiuser DOS

, this is a true environment variable automatically updated by the shell to the return code of exiting programs.

See also the related pseudo-variable

%ERRORLEVEL%

under DR-DOS and the

IF ERRORLEVEL

command.

**`%GREETING_TIME%`**

This pseudo-variable returns the 3-level day greeting time. The returned string depends on the locale-specific version of DR-DOS, f.e. "

morning

", "

afternoon

", or "

evening

" in the English version. It resembles an identically named

identifier variable

in

Novell NetWare

login scripts.

**`%HOUR%`**

This pseudo-variable returns the hours of the current time in 12-hour format without leading zeros, f.e. "

1

".."

12

". It resembles an identically named

identifier variable

in

Novell NetWare

login scripts.

**`%HOUR24%`**

This pseudo-variable returns the hours of the current time in 24-hour format in a 2-digit format with leading zeros, f.e. "

00

".."

23

". It resembles an identically named

identifier variable

in

Novell NetWare

login scripts. See also the similar pseudo-variable

%_HOUR%

.

**`%MINUTE%`**

This pseudo-variable returns the minutes of the current time in a 2-digit format with leading zeros, f.e "

00

".."

59

". It resembles an identically named

identifier variable

in

Novell NetWare

login scripts. See also the similar pseudo-variable

%_MINUTE%

.

**`%MONTH%`**

This pseudo-variable returns the months of the current date in a 2-digit format with leading zeros, f.e. "

01

".."

12

". It resembles an identically named

identifier variable

in

Novell NetWare

login scripts. See also the similar pseudo-variable

%_MONTH%

.

**`%MONTH_NAME%`**

This pseudo-variable returns the month name of the current date. The returned string depends on the locale-specific version of DR-DOS, f.e. "

January

", "

February

", "

March

", "

April

", "

May

", "

June

", "

July

", "

August

", "

September

", "

October

", or "

December

" in the English version. It resembles an identically named

identifier variable

in

Novell NetWare

login scripts.

**`%NDAY_OF_WEEK%`**

This pseudo-variable returns the number of day of the current week, f.e. "

1

".."

7

" (with "

1

" for Sunday). It resembles an identically named

identifier variable

in

Novell NetWare

login scripts.

**`%OS_VERSION%`**

This pseudo-variable returns the version of the operating system depending on the current setting of the environment variable

%VER%

. If

%VER%

is not defined,

%OS_VERSION%

returns "

off

". It resembles an identically named

identifier variable

in

Novell NetWare

login scripts, which may return versions also for non-DR-DOS versions of DOS.

**`%SECOND%`**

This pseudo-variable returns the seconds of the current time in a 2-digit format with leading zeros, f.e. "

00

".."

59

". It resembles an identically named

identifier variable

in

Novell NetWare

login scripts. See also the similar pseudo-variable

%_SECOND%

.

**`%SHORT_YEAR%`**

This pseudo-variable returns the year of the current date in a 2-digit format with leading zeros, f.e. "

93

".."

99

", "

00

".."

92

". It resembles an identically named

identifier variable

in

Novell NetWare

login scripts.

**`%YEAR%` and `%_YEAR%`**

Supported since

Novell DOS 7

, the

%YEAR%

pseudo-variable returns the year of the current date in a 4-digit format, f.e. "

1980

".."

2099

". It resembles an identically named

identifier variable

in

Novell NetWare

login scripts. DR-DOS 7.02 and higher added

%_YEAR%

for compatibility with

4DOS

, returning the same value.

**`%/%`**

In

COMMAND.COM

of DR-DOS 7.02 and higher, this pseudo-variable returns the current

SwitChar

setting of the system, either "

/

" (DOS style) or "

-

" (Unix style).

See also the related

CONFIG.SYS

directive

SWITCHAR

and the environment variable

%SWITCHAR%

.

**`%_CODEPAGE%`**

This pseudo-variable returns the systems' current

code page

("

1

".."

65533

"), f.e. "

437

", "

850

", "

858

". This variable was originally introduced by

4DOS

,

but also became available with

COMMAND.COM

since DR-DOS 7.02. See also the

CHCP

command.

**`%_COLUMNS%`**

This pseudo-variable returns the current number of screen columns depending on the display mode, f.e. "

40

", "

80

", "

132

", etc. This variable was originally introduced by

4DOS

,

but also became available with

COMMAND.COM

since DR-DOS 7.02. See also a similar environment variable

%$WIDTH%

under DOS Plus.

**`%_COUNTRY%`**

This pseudo-variable returns the systems' current

country code

("

1

".."

65534

"), f.e. "

1

" for USA, "

44

" for UK, "

49

" for Germany, "

20049

" with

ISO 8601

, "

21049

" with ISO 8601 and

Euro

support.

This variable was originally introduced by

4DOS

,

but also became available with

COMMAND.COM

since DR-DOS 7.02. See also the

CONFIG.SYS

directive

COUNTRY

.

**`%_DAY%`**

This pseudo-variable returns the days of the current date without leading zeros, f.e. "

1

".."

31

". This variable was originally introduced by

4DOS

,

but also became available with

COMMAND.COM

since DR-DOS 7.02. See also the similar pseudo-variable

%DAY%

.

**`%_HOUR%`**

This pseudo-variable returns the hours of the current time in 24-hour format without leading zeros, f.e. "

0

".."

23

". This variable was originally introduced by

4DOS

,

but also became available with

COMMAND.COM

since DR-DOS 7.02. See also the similar pseudo-variable

%HOUR24%

.

**`%_MINUTE%`**

This pseudo-variable returns the minutes of the current time without leading zeros, f.e "

0

".."

59

". This variable was originally introduced by

4DOS

,

but also became available with

COMMAND.COM

since DR-DOS 7.02. See also the similar pseudo-variable

%MINUTE%

.

**`%_MONTH%`**

This pseudo-variable returns the months of the current date without leading zeros, f.e. "

1

".."

12

". This variable was originally introduced by

4DOS

,

but also became available with

COMMAND.COM

since DR-DOS 7.02. See also the similar pseudo-variable

%MONTH%

.

**`%_ROWS%`**

This pseudo-variable returns the current number of screen rows depending on the display mode, f.e. "

25

", "

43

", "

50

", etc. This variable was originally introduced by

4DOS

,

but also became available with

COMMAND.COM

since DR-DOS 7.02. See a similar environment variable

%$LENGTH%

under DOS Plus.

**`%_SECOND%`**

This pseudo-variable returns the seconds of the current time without leading zeros, f.e. "

0

".."

59

". This variable was originally introduced by

4DOS

,

but also became available with

COMMAND.COM

since DR-DOS 7.02. See also the similar pseudo-variable

%SECOND%

.

*System information variables* supported by DR-DOS `COMMAND.COM` with networking loaded:

**`%LOGIN_NAME%`**

This pseudo-variable returns the user name. This always worked with

NETX

, but it will also work with

Personal NetWare

's

ODI

/

VLM

if the current drive is a PNW-mapped drive (otherwise an empty string is returned). See also the similarly named environment variable

%LOGINNAME%

.

**`%P_STATION%`**

This pseudo-variable returns the physical station number in a format "

????????????

". The value depends on the

MAC address

of the network adapter, but can be overridden. It resembles an identically named

identifier variable

in

Novell NetWare

login scripts.

**`%STATION%`**

This pseudo-variable returns the logical station number starting with "

1

" for the first client. The numbers are assigned by the file server and remain static for as long as the

IPX

connection remains established. It resembles an identically named

identifier variable

in

Novell NetWare

login scripts.

**`%FULL_NAME%`**

This pseudo-variable returns the full name of the logged in user, if available. It resembles an identically named

identifier variable

in

Novell NetWare

login scripts. See also the related pseudo-variable

%LOGIN_NAME%

.

### Windows

*Dynamic environment variables* (also named *internal variables* or *system information variables* under DOS) are pseudo-environment variables supported by `CMD.EXE` when command-line extensions are enabled, and they expand to various discrete values whenever queried, that is, their values can change when queried multiple times even within the same command. While they can be used in batch jobs and at the prompt, they are not stored in the environment. Consequently, they are neither listed by `SET` nor do they exist for external programs to read. They are not case-sensitive.

Indirectly, they are also supported under Windows' `COMMAND.COM`, which has been modified to internally call `CMD.EXE` to execute the commands.

**`%CD%`**

This pseudo-variable expands to the current directory equivalent to the output of the command

CD

when called without arguments. While a long filename can be returned under

CMD.EXE

depending on the current directory, the fact that the current directory will always be in

8.3

format under

COMMAND.COM

will cause it to return a short filename under

COMMAND.COM

, even when

COMMAND

internally calls

CMD

.

**`%CMDCMDLINE%`**

This pseudo-variable expands to the original startup parameters of

CMD.EXE

, f.e. "

C:\Windows\system32\cmd.exe

". Under Windows'

COMMAND.COM

, this may return something like "

C:\Windows\system32\cmd.exe /c ...

" due to the fact that

COMMAND.COM

calls

CMD.EXE

internally.

**`%CMDEXTVERSION%`**

This pseudo-variable expands to the version of the command-line extensions of

CMD.EXE

, if enabled (e.g. "

1

" under

Windows NT

, "

2

" under

Windows 2000

and

Windows XP

).

**`%DATE%`**

This pseudo-variable expands to the current date. The date is displayed according to the current user's

date format

preferences.

**`%ERRORLEVEL%`**

This pseudo-variable expands to the last set error level, a value between "

0

" and "

255

" (without leading zeros).

External commands and some internal commands set error levels upon execution. See also the identically named pseudo-variable

%ERRORLEVEL%

under DR-DOS and the

IF ERRORLEVEL

command.

**`%HIGHESTNUMANODENUMBER%`**

This pseudo-variable returns the number of the highest

NUMA

node.

**`%RANDOM%`**

This pseudo-variable returns a random number between "

0

" and "

32767

".

**`%TIME%`**

This pseudo-variable returns the current time. The time is displayed according to the current user's time format preferences. If the

%TIME%

and

%DATE%

variables are both used, it is important to read them both in this particular order in rapid succession in order to avoid midnight-rollover problems.

### Other shells

Unix-like shells have similar dynamically generated variables, bash's `$RANDOM` being a well-known example. However, since these shells have a concept of local variables, they are described as special local variables instead.
