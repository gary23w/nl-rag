---
title: "An Introduction to R (part 6/6)"
source: https://cran.r-project.org/doc/manuals/r-release/R-intro.html
domain: r-language
license: GFDL-1.3
tags: r language, rstats, cran, statistical computing
fetched: 2026-07-02
part: 6/6
---

## Appendix A A sample session

The following session is intended to introduce to you some features of the R environment by using them. Many features of the system will be unfamiliar and puzzling at first, but this puzzlement will soon disappear.

Start R appropriately for your platform (see Invoking R).

The R program begins, with a banner.

(Within R code, the prompt on the left hand side will not be shown to avoid confusion.)

**`help.start()`**

Start the HTML interface to on-line help (using a web browser available at your machine). You should briefly explore the features of this facility with the mouse.

Iconify the help window and move on to the next part.

**`x <- rnorm(50)`**

**`y <- rnorm(x)`**

Generate two pseudo-random normal vectors of *x*- and *y*-coordinates.

**`plot(x, y)`**

Plot the points in the plane. A graphics window will appear automatically.

**`ls()`**

See which R objects are now in the R workspace.

**`rm(x, y)`**

Remove objects no longer needed. (Clean up).

**`x <- 1:20`**

Make *x = (1, 2, ..., 20)*.

**`w <- 1 + sqrt(x)/2`**

A ‘weight’ vector of standard deviations.

**`dummy <- data.frame(x=x, y= x + rnorm(x)*w)`**

**`dummy`**

Make a *data frame* of two columns, *x* and *y*, and look at it.

**`fm <- lm(y ~ x, data=dummy)`**

**`summary(fm)`**

Fit a simple linear regression and look at the analysis. With `y` to the left of the tilde, we are modelling *y* dependent on *x*.

**`fm1 <- lm(y ~ x, data=dummy, weight=1/w^2)`**

**`summary(fm1)`**

Since we know the standard deviations, we can do a weighted regression.

**`attach(dummy)`**

Make the columns in the data frame visible as variables.

**`lrf <- lowess(x, y)`**

Make a nonparametric local regression function.

**`plot(x, y)`**

Standard point plot.

**`lines(x, lrf$y)`**

Add in the local regression.

**`abline(0, 1, lty=3)`**

The true regression line: (intercept 0, slope 1).

**`abline(coef(fm))`**

Unweighted regression line.

**`abline(coef(fm1), col = "red")`**

Weighted regression line.

**`detach()`**

Remove data frame from the search path.

**`plot(fitted(fm), resid(fm),`**

**`xlab="Fitted values",`**

**`ylab="Residuals",`**

**`main="Residuals vs Fitted")`**

A standard regression diagnostic plot to check for heteroscedasticity. Can you see it?

**`qqnorm(resid(fm), main="Residuals Rankit Plot")`**

A normal scores plot to check for skewness, kurtosis and outliers. (Not very useful here.)

**`rm(fm, fm1, lrf, x, dummy)`**

Clean up again.

The next section will look at data from the classical experiment of Michelson to measure the speed of light. This dataset is available in the `morley` object, but we will read it to illustrate the `read.table` function.

**`filepath <- system.file("data", "morley.tab" , package="datasets")`**

**`filepath`**

Get the path to the data file.

**`file.show(filepath)`**

Optional. Look at the file.

**`mm <- read.table(filepath)`**

**`mm`**

Read in the Michelson data as a data frame, and look at it. There are five experiments (column `Expt`) and each has 20 runs (column `Run`) and `sl` is the recorded speed of light, suitably coded.

**`mm$Expt <- factor(mm$Expt)`**

**`mm$Run <- factor(mm$Run)`**

Change `Expt` and `Run` into factors.

**`attach(mm)`**

Make the data frame visible at position 2 (the default).

**`plot(Expt, Speed, main="Speed of Light Data", xlab="Experiment No.")`**

Compare the five experiments with simple boxplots.

**`fm <- aov(Speed ~ Run + Expt, data=mm)`**

**`summary(fm)`**

Analyze as a randomized block, with ‘runs’ and ‘experiments’ as factors.

**`fm0 <- update(fm, . ~ . - Run)`**

**`anova(fm0, fm)`**

Fit the sub-model omitting ‘runs’, and compare using a formal analysis of variance.

**`detach()`**

**`rm(fm, fm0)`**

Clean up before moving on.

We now look at some more graphical features: contour and image plots.

**`x <- seq(-pi, pi, len=50)`**

**`y <- x`**

*x* is a vector of 50 equally spaced values in the interval [-pi\, pi]. *y* is the same.

**`f <- outer(x, y, function(x, y) cos(y)/(1 + x^2))`**

*f* is a square matrix, with rows and columns indexed by *x* and *y* respectively, of values of the function cos(y)/(1 + x^2).

**`oldpar <- par(no.readonly = TRUE)`**

**`par(pty="s")`**

Save the plotting parameters and set the plotting region to “square”.

**`contour(x, y, f)`**

**`contour(x, y, f, nlevels=15, add=TRUE)`**

Make a contour map of *f*; add in more lines for more detail.

**`fa <- (f-t(f))/2`**

`fa` is the “asymmetric part” of *f*. (`t()` is transpose).

**`contour(x, y, fa, nlevels=15)`**

Make a contour plot, …

**`par(oldpar)`**

… and restore the old graphics parameters.

**`image(x, y, f)`**

**`image(x, y, fa)`**

Make some high density image plots, (of which you can get hardcopies if you wish), …

**`objects(); rm(x, y, f, fa)`**

… and clean up before moving on.

R can do complex arithmetic, also.

**`th <- seq(-pi, pi, len=100)`**

**`z <- exp(1i*th)`**

`1i` is used for the complex number *i*.

**`par(pty="s")`**

**`plot(z, type="l")`**

Plotting complex arguments means plot imaginary versus real parts. This should be a circle.

**`w <- rnorm(100) + rnorm(100)*1i`**

Suppose we want to sample points within the unit circle. One method would be to take complex numbers with standard normal real and imaginary parts …

**`w <- ifelse(Mod(w) > 1, 1/w, w)`**

… and to map any outside the circle onto their reciprocal.

**`plot(w, xlim=c(-1,1), ylim=c(-1,1), pch="+",xlab="x", ylab="y")`**

**`lines(z)`**

All points are inside the unit circle, but the distribution is not uniform.

**`w <- sqrt(runif(100))*exp(2*pi*runif(100)*1i)`**

**`plot(w, xlim=c(-1,1), ylim=c(-1,1), pch="+", xlab="x", ylab="y")`**

**`lines(z)`**

The second method uses the uniform distribution. The points should now look more evenly spaced over the disc.

**`rm(th, w, z)`**

Clean up again.

**`q()`**

Quit the R program. You will be asked if you want to save the R workspace, and for an exploratory session like this, you probably do not want to save it.


## Appendix B Invoking R

Users of R on Windows or macOS should read the OS-specific section first, but command-line use is also supported.

### B.1 Invoking R from the command line

When working at a command line on UNIX or Windows, the command ‘R’ can be used both for starting the main R program in the form

```
R [options] [<infile] [>outfile],
```

or, via the `R CMD` interface, as a wrapper to various R tools (e.g., for processing files in R documentation format or manipulating add-on packages) which are not intended to be called “directly”.

At the Windows command-line, `Rterm.exe` is preferred to `R`.

You need to ensure that either the environment variable `TMPDIR` is unset or it points to a valid place to create temporary files and directories.

Most options control what happens at the beginning and at the end of an R session. The startup mechanism is as follows (see also the on-line help for topic ‘Startup’ for more information, and the section below for some Windows-specific details).

- Unless --no-environ was given, R searches for user and site files to process for setting environment variables. The name of the site file is the one pointed to by the environment variable `R_ENVIRON`; if this is unset, *R_HOME*/etc/Renviron.site is used (if it exists). The user file is the one pointed to by the environment variable `R_ENVIRON_USER` if this is set; otherwise, files .Renviron in the current or in the user’s home directory (in that order) are searched for. These files should contain lines of the form ‘*name*=*value*’. (See `help("Startup")` for a precise description.) Variables you might want to set include `R_PAPERSIZE` (the default paper size), `R_PRINTCMD` (the default print command) and `R_LIBS` (specifies the list of R library trees searched for add-on packages).
- Then R searches for the site-wide startup profile unless the command line option --no-site-file was given. The name of this file is taken from the value of the `R_PROFILE` environment variable. If that variable is unset, the default *R_HOME*/etc/Rprofile.site is used if this exists.
- Then, unless --no-init-file was given, R searches for a user profile and sources it. The name of this file is taken from the environment variable `R_PROFILE_USER`; if unset, a file called .Rprofile in the current directory or in the user’s home directory (in that order) is searched for.
- It also loads a saved workspace from file .RData in the current directory if there is one (unless --no-restore or --no-restore-data was specified).
- Finally, if a function `.First()` exists, it is executed. This function (as well as `.Last()` which is executed at the end of the R session) can be defined in the appropriate startup profiles, or reside in .RData.

In addition, there are options for controlling the memory available to the R process (see the on-line help for topic ‘Memory’ for more information). Users will not normally need to use these unless they are trying to limit the amount of memory used by R.

R accepts the following command-line options.

**--help**

**-h**

Print short help message to standard output and exit successfully.

**--version**

Print version information to standard output and exit successfully.

**--encoding=*enc***

Specify the encoding to be assumed for input from the console or `stdin`. This needs to be an encoding known to `iconv`: see its help page. (`--encoding *enc*` is also accepted.) The input is re-encoded to the locale R is running in and needs to be representable in the latter’s encoding (so e.g. you cannot re-encode Greek text in a French locale unless that locale uses the UTF-8 encoding).

**RHOME**

Print the path to the R “home directory” to standard output and exit successfully. Apart from the front-end shell script and the man page, R installation puts everything (executables, packages, etc.) into this directory.

**--save**

**--no-save**

Control whether data sets should be saved or not at the end of the R session. If neither is given in an interactive session, the user is asked for the desired behavior when ending the session with q(); in non-interactive use one of these must be specified or implied by some other option (see below).

**--no-environ**

Do not read any user file to set environment variables.

**--no-site-file**

Do not read the site-wide profile at startup.

**--no-init-file**

Do not read the user’s profile at startup.

**--restore**

**--no-restore**

**--no-restore-data**

Control whether saved images (file .RData in the directory where R was started) should be restored at startup or not. The default is to restore. (--no-restore implies all the specific --no-restore-* options.)

**--no-restore-history**

Control whether the history file (normally file .Rhistory in the directory where R was started, but can be set by the environment variable `R_HISTFILE`) should be restored at startup or not. The default is to restore.

**--no-Rconsole**

(Windows only) Prevent loading the Rconsole file at startup.

**--vanilla**

Combine --no-save, --no-environ, --no-site-file, --no-init-file and --no-restore. Under Windows, this also includes --no-Rconsole.

**-f *file***

**--file=*file***

(not `Rgui.exe`) Take input from *file*: ‘-’ means `stdin`. Implies --no-save unless --save has been set. On a Unix-alike, shell metacharacters should be avoided in *file* (but spaces are allowed).

**-e *expression***

(not `Rgui.exe`) Use *expression* as an input line. One or more -e options can be used, but not together with -f or --file. Implies --no-save unless --save has been set. (There is a limit of 10,000 bytes on the total length of expressions used in this way. Expressions containing spaces or shell metacharacters will need to be quoted.)

**--no-readline**

(UNIX only) Turn off command-line editing via **readline**. This is useful when running R from within Emacs using the ESS (“Emacs Speaks Statistics”) package. See The command-line editor, for more information. Command-line editing is enabled for default interactive use (see --interactive). This option also affects tilde-expansion: see the help for `path.expand`.

**--min-vsize=*N***

**--min-nsize=*N***

For expert use only: set the initial trigger sizes for garbage collection of vector heap (in bytes) and *cons cells* (number) respectively. Suffix ‘M’ specifies megabytes or millions of cells respectively. The defaults are 6Mb and 350k respectively and can also be set by environment variables `R_NSIZE` and `R_VSIZE`.

**--max-ppsize=*N***

Specify the maximum size of the pointer protection stack as *N* locations. This defaults to 10000, but can be increased to allow large and complicated calculations to be done. Currently the maximum value accepted is 100000.

**--quiet**

**--silent**

**-q**

Do not print out the initial copyright and welcome messages. Additionally set `options("quiet")` or equivalently, `getOption("quiet")`, to `TRUE` which other R functions may use to be more quiet than usually.

**--no-echo**

**-s**

Make R run as quietly as possible. This option is intended to support programs which use R to compute results for them. It implies --quiet and --no-save.

**--interactive**

(UNIX only) Assert that R really is being run interactively even if input has been redirected: use if input is from a FIFO or pipe and fed from an interactive program. (The default is to deduce that R is being run interactively if and only if stdin is connected to a terminal or `pty`.) Using -e, -f or --file asserts non-interactive use even if --interactive is given.

Note that this does not turn on command-line editing.

**--ess**

(Windows only) Set `Rterm` up for use by `R-inferior-mode` in ESS, including asserting interactive use (without the command-line editor) and no buffering of stdout.

**--verbose**

Print more information about progress, and in particular set R’s option `verbose` to `TRUE`. R code uses this option to control the printing of diagnostic messages.

**--debugger=*name***

**-d *name***

(UNIX only) Run R through debugger *name*. For most debuggers (the exceptions are `valgrind` and recent versions of `gdb`), further command line options are disregarded, and should instead be given when starting the R executable from inside the debugger.

**--gui=*type***

**-g *type***

(UNIX only) Use *type* as graphical user interface (note that this also includes interactive graphics). Currently, possible values for *type* are ‘X11’ (the default) and, provided that ‘Tcl/Tk’ support is available, ‘Tk’. (For back-compatibility, ‘x11’ and ‘tk’ are accepted.)

**--arch=*name***

(UNIX only) Run the specified sub-architecture.

**--args**

This flag does nothing except cause the rest of the command line to be skipped: this can be useful to retrieve values from it with `commandArgs(TRUE)`.

Note that input and output can be redirected in the usual way (using ‘<’ and ‘>’), but the line length limit of 4095 bytes still applies. Warning and error messages are sent to the error channel (`stderr`).

The command `R CMD` allows the invocation of various tools which are useful in conjunction with R, but not intended to be called “directly”. The general form is

```
R CMD command args
```

where *command* is the name of the tool and *args* the arguments passed on to it.

Currently, the following tools are available.

**`BATCH`**

Run R in batch mode. Runs `R --restore --save` with possibly further options (see `?BATCH`).

**`COMPILE`**

(UNIX only) Compile C, C++, Fortran … files for use with R.

**`SHLIB`**

Build shared library for dynamic loading.

**`INSTALL`**

Install add-on packages.

**`REMOVE`**

Remove add-on packages.

**`build`**

Build (that is, package) add-on packages.

**`check`**

Check add-on packages.

**`LINK`**

(UNIX only) Front-end for creating executable programs.

**`Rprof`**

Post-process R profiling files.

**`Rdconv`**

**`Rd2txt`**

Convert Rd format to various other formats, including HTML, LaTeX, plain text, and extracting the examples. `Rd2txt` can be used as shorthand for `Rd2conv -t txt`.

**`Rd2pdf`**

Convert Rd format to PDF.

**`Stangle`**

Extract S/R code from Sweave or other vignette documentation

**`Sweave`**

Process Sweave or other vignette documentation

**`Rdiff`**

Diff R output ignoring headers etc

**`config`**

Obtain configuration information

**`javareconf`**

(Unix only) Update the Java configuration variables

**`rtags`**

(Unix only) Create Emacs-style tag files from C, R, and Rd files

**`open`**

(Windows only) Open a file via Windows’ file associations

**`texify`**

(Windows only) Process (La)TeX files with R’s style files

Use

```
R CMD command --help
```

to obtain usage information for each of the tools accessible via the `R CMD` interface.

In addition, you can use options --arch=, --no-environ, --no-init-file, --no-site-file and --vanilla between `R` and `CMD`: these affect any R processes run by the tools. (Here --vanilla is equivalent to --no-environ --no-site-file --no-init-file.) However, note that `R CMD` does not of itself use any R startup files (in particular, neither user nor site Renviron files), and all of the R processes run by these tools (except `BATCH`) use --no-restore. Most use --vanilla and so invoke no R startup files: the current exceptions are `INSTALL`, `REMOVE`, `Sweave` and `SHLIB` (which uses --no-site-file --no-init-file).

```
R CMD cmd args
```

for any other executable `*cmd*` on the path or given by an absolute filepath: this is useful to have the same environment as R or the specific commands run under, for example to run `ldd` or `pdflatex`. Under Windows *cmd* can be an executable or a batch file, or if it has extension `.sh` or `.pl` the appropriate interpreter (if available) is called to run it.

### B.2 Invoking R under Windows

There are two ways to run R under Windows. Within a terminal window (e.g. `cmd.exe` or a more capable shell), the methods described in the previous section may be used, invoking by `R.exe` or more directly by `Rterm.exe`. For interactive use, there is a console-based GUI (`Rgui.exe`).

The startup procedure under Windows is very similar to that under UNIX, but references to the ‘home directory’ need to be clarified, as this is not always defined on Windows. If the environment variable `R_USER` is defined, that gives the home directory. Next, if the environment variable `HOME` is defined, that gives the home directory. After those two user-controllable settings, R tries to find system defined home directories. It first tries to use the Windows "personal" directory (typically `My Documents` in recent versions of Windows). If that fails, and environment variables `HOMEDRIVE` and `HOMEPATH` are defined (and they normally are) these define the home directory. Failing all those, the home directory is taken to be the starting directory.

You need to ensure that either the environment variables `TMPDIR`, `TMP` and `TEMP` are either unset or one of them points to a valid place to create temporary files and directories.

Environment variables can be supplied as ‘*name*=*value*’ pairs on the command line.

If there is an argument ending .RData (in any case) it is interpreted as the path to the workspace to be restored: it implies --restore and sets the working directory to the parent of the named file. (This mechanism is used for drag-and-drop and file association with `RGui.exe`, but also works for `Rterm.exe`. If the named file does not exist it sets the working directory if the parent directory exists.)

The following additional command-line options are available when invoking `RGui.exe`.

**--mdi**

**--sdi**

**--no-mdi**

Control whether `Rgui` will operate as an MDI program (with multiple child windows within one main window) or an SDI application (with multiple top-level windows for the console, graphics and pager). The command-line setting overrides the setting in the user’s Rconsole file.

**--debug**

Enable the “Break to debugger” menu item in `Rgui`, and trigger a break to the debugger during command line processing.

Under Windows with `R CMD` you may also specify your own .bat, .exe, .sh or .pl file. It will be run under the appropriate interpreter (Perl for .pl) with several environment variables set appropriately, including `R_HOME`, `R_OSTYPE`, `PATH`, `BSTINPUTS` and `TEXINPUTS`. For example, if you already have latex.exe on your path, then

```
R CMD latex.exe mydoc
```

will run LaTeX on mydoc.tex, with the path to R’s share/texmf macros appended to `TEXINPUTS`. (With the MiKTeX build of LaTeX, using `R CMD texify mydoc` is often more convenient.)

### B.3 Invoking R under macOS

There are two ways to run R under macOS. Within a `Terminal.app` window by invoking `R`, the methods described in the first subsection apply. There is also console-based GUI (`R.app`) that by default is installed in the `Applications` folder on your system. It is a standard double-clickable macOS application.

The startup procedure under macOS is very similar to that under UNIX, but `R.app` does not make use of command-line arguments. The ‘home directory’ is the one inside the R.framework, but the startup and current working directory are set as the user’s home directory unless a different startup directory is given in the Preferences window accessible from within the GUI.

### B.4 Scripting with R

If you just want to run a file foo.R of R commands, the recommended way is to use `R CMD BATCH foo.R`. If you want to run this in the background or as a batch job use OS-specific facilities to do so: for example in most shells on Unix-alike OSes `R CMD BATCH foo.R &` runs a background job.

You can pass parameters to scripts via additional arguments on the command line: for example (where the exact quoting needed will depend on the shell in use)

```
R CMD BATCH "--args arg1 arg2" foo.R &
```

will pass arguments to a script which can be retrieved as a character vector by

```
args <- commandArgs(TRUE)
```

This is made simpler by the alternative front-end `Rscript`, which can be invoked by

```
Rscript foo.R arg1 arg2
```

and this can also be used to write executable script files like (at least on Unix-alikes, and in some Windows shells)

```
#! /path/to/Rscript
args <- commandArgs(TRUE)
...
q(status=<exit status code>)
```

If this is entered into a text file runfoo and this is made executable (by `chmod 755 runfoo`), it can be invoked for different arguments by

```
runfoo arg1 arg2
```

For further options see `help("Rscript")`. This writes R output to stdout and stderr, and this can be redirected in the usual way for the shell running the command.

If you do not wish to hardcode the path to `Rscript` but have it in your path (which is normally the case for an installed R except on Windows, but e.g. macOS users may need to add /usr/local/bin to their path), use

```
#! /usr/bin/env Rscript
...
```

At least in Bourne and bash shells, the `#!` mechanism does **not** allow extra arguments like `#! /usr/bin/env Rscript --vanilla`.

One thing to consider is what `stdin()` refers to. It is commonplace to write R scripts with segments like

```
chem <- scan(n=24)
2.90 3.10 3.40 3.40 3.70 3.70 2.80 2.50 2.40 2.40 2.70 2.20
5.28 3.37 3.03 3.03 28.95 3.77 3.40 2.20 3.50 3.60 3.70 3.70
```

and `stdin()` refers to the script file to allow such traditional usage. If you want to refer to the process’s stdin, use `"stdin"` as a `file` connection, e.g. `scan("stdin", ...)`.

Another way to write executable script files (suggested by François Pinard) is to use a *here document* like

```
#!/bin/sh
[environment variables can be set here]
R --no-echo [other options] <<EOF

   R program goes here...

EOF
```

but here `stdin()` refers to the program source and `"stdin"` will not be usable.

Short scripts can be passed to `Rscript` on the command-line *via* the -e flag. (Empty scripts are not accepted.)

Note that on a Unix-alike the input filename (such as foo.R) should not contain spaces nor shell metacharacters.


## Appendix C The command-line editor

### C.1 Preliminaries

When the GNU **readline** library is available at the time R is configured for compilation under UNIX, an inbuilt command line editor allowing recall, editing and re-submission of prior commands is used. Note that other versions of **readline** exist and may be used by the inbuilt command line editor: this is most common on macOS. You can find out which version (if any) is available by running `extSoftVersion()` in an R session.

It can be disabled (useful for usage with ESS 25) using the startup option --no-readline.

Windows versions of R have somewhat simpler command-line editing: see ‘Console’ under the ‘Help’ menu of the GUI, and the file README.Rterm for command-line editing under `Rterm.exe`.

When using R with GNU26 **readline** capabilities, the functions described below are available, as well as others (probably) documented in `man readline` or `info readline` on your system.

Many of these use either Control or Meta characters. Control characters, such as Control-m, are obtained by holding the CTRL down while you press the m key, and are written as C-m below. Meta characters, such as Meta-b, are typed by holding down META27 and pressing b, and written as M-b in the following. If your terminal does not have a META key enabled, you can still type Meta characters using two-character sequences starting with ESC. Thus, to enter M-b, you could type ESCb. The ESC character sequences are also allowed on terminals with real Meta keys. Note that case is significant for Meta characters.

Some but not all versions28 of **readline** will recognize resizing of the terminal window so this is best avoided.

### C.2 Editing actions

The R program keeps a history of the command lines you type, including the erroneous lines, and commands in your history may be recalled, changed if necessary, and re-submitted as new commands. In Emacs-style command-line editing any straight typing you do while in this editing phase causes the characters to be inserted in the command you are editing, displacing any characters to the right of the cursor. In *vi* mode character insertion mode is started by M-i or M-a, characters are typed and insertion mode is finished by typing a further ESC. (The default is Emacs-style, and only that is described here: for *vi* mode see the **readline** documentation.)

Pressing the RET command at any time causes the command to be re-submitted.

Other editing actions are summarized in the following table.

### C.3 Command-line editor summary

#### Command recall and vertical motion

**C-p**

Go to the previous command (backwards in the history).

**C-n**

Go to the next command (forwards in the history).

**C-r *text***

Find the last command with the *text* string in it. This can be cancelled by `C-g` (and on some versions of R by `C-c`).

On most terminals, you can also use the up and down arrow keys instead of C-p and C-n, respectively.

#### Horizontal motion of the cursor

**C-a**

Go to the beginning of the command.

**C-e**

Go to the end of the line.

**M-b**

Go back one word.

**M-f**

Go forward one word.

**C-b**

Go back one character.

**C-f**

Go forward one character.

On most terminals, you can also use the left and right arrow keys instead of C-b and C-f, respectively.

#### Editing and re-submission

***text***

Insert *text* at the cursor.

**C-f *text***

Append *text* after the cursor.

**DEL**

Delete the previous character (left of the cursor).

**C-d**

Delete the character under the cursor.

**M-d**

Delete the rest of the word under the cursor, and “save” it.

**C-k**

Delete from cursor to end of command, and “save” it.

**C-y**

Insert (yank) the last “saved” text here.

**C-t**

Transpose the character under the cursor with the next.

**M-l**

Change the rest of the word to lower case.

**M-c**

Change the rest of the word to upper case.

**RET**

Re-submit the command to R.

The final RET terminates the command line editing sequence.

The **readline** key bindings can be customized in the usual way *via* a ~/.inputrc file. These customizations can be conditioned on application `R`, that is by including a section like

```
$if R
  "\C-xd": "q('no')\n"
$endif
```
