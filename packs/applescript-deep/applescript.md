---
title: "AppleScript"
source: https://en.wikipedia.org/wiki/AppleScript
domain: applescript-deep
license: CC-BY-SA-4.0
tags: applescript language, apple events, hypercard software, scripting language, classic mac
fetched: 2026-07-02
---

# AppleScript

**AppleScript** is a scripting language created by Apple Inc. that facilitates automated control of Mac applications. First introduced in System 7, it is currently included in macOS in a package of automation tools. The term *AppleScript* may refer to the scripting language, to a script written in the language, or to the macOS Open Scripting Architecture that underlies the language.

AppleScript is primarily a mechanism for driving Apple events – an inter-application communication (IAC) technology that exchanges data between and controls applications. Additionally, AppleScript supports basic calculations and text processing, and is extensible via scripting additions that add functions to the language.

AppleScript is tightly bound to the Mac environment, similar to how Windows Script Host is bound to the Windows environment. In other words, AppleScript is not a general purpose scripting language like Python. One way that AppleScript is bound to the unique aspects of its environment is that it relies on applications to publish *dictionaries* of addressable objects and operations.

As is typical of a command language, AppleScript is not designed to directly perform intensive processing. For example, a script cannot efficiently perform intensive math operations or complicated text processing. However, AppleScript can be used in combination with other tools and technologies which allows it to leverage more efficient programming contexts.

The language has aspects of structured, procedural, object-oriented and natural language programming, but does not strictly conform to any of these paradigms.

## History

In the late 1980s, Apple considered using HyperCard's HyperTalk scripting language as the standard language for end-user development across the company and within its classic Mac OS operating system, and for interprocess communication between Apple and non-Apple products. HyperTalk could be used by novices to program a HyperCard stack. Apple engineers recognized that a similar, but more object-oriented scripting language could be designed to be used with any application, and the AppleScript project was born as a spin-off of a research effort to modernize the Macintosh as a whole and finally became part of System 7.

AppleScript was released in October 1993 as part of System 7.1.1 (System 7 Pro, the first major upgrade to System 7). QuarkXPress (ver. 3.2) was one of the first major software applications that supported AppleScript. This, in turn, led to AppleScript being widely adopted within the publishing and prepress world, often tying together complex workflows. This was a key factor in retaining the Macintosh's dominant position in publishing and prepress, even after QuarkXpress and other publishing applications were ported to Microsoft Windows.

After some uncertainty about the future of AppleScript on Apple's next generation OS, the move to Mac OS X (around 2002) and its Cocoa frameworks greatly increased the usefulness and flexibility of AppleScript. Cocoa applications allow application developers to implement basic scriptability for their apps with minimal effort, broadening the number of applications that are directly scriptable. At the same time, the shift to the Unix underpinnings and AppleScript's ability to run Unix commands directly, with the `do shell script` command, allowed AppleScripts much greater control over the operating system itself. AppleScript Studio, released with Mac OS X 10.2 as part of Xcode, and later AppleScriptObjC framework, released in Mac OS X 10.6, allowed users to build Cocoa applications using AppleScript.

In a 2006 article, *Macworld* included AppleScript among its rankings of Apple's 30 most significant products to date, placing it at #17.

In a 2013 article for *Macworld*, veteran Mac software developer and commentator John Gruber concluded his reflection on "the unlikely persistence of AppleScript" by noting: "In theory, AppleScript could be much better; in practice, though, it's the best thing we have that works. It exemplifies the Mac's advantages over iOS for tinkerers and advanced users."

In October 2016, longtime AppleScript product manager and automation evangelist Sal Soghoian left Apple when his position was eliminated "for business reasons". Veterans in the Mac community such as John Gruber and Andy Ihnatko generally responded with concern, questioning Apple's commitment to the developer community and pro users. Apple senior vice president of software engineering Craig Federighi responded in an email saying that "We have every intent to continue our support for the great automation technologies in macOS!", though Jeff Gamet at *The Mac Observer* opined that it did little to assuage his doubt about the future of Apple automation in general and AppleScript in particular. For the time being, AppleScript remains one component of macOS automation technologies, along with Automator, Shortcuts, Services, and shell scripting.

## Intent

AppleScript was designed to be used as an accessible end-user scripting language, offering users an intelligent mechanism to control applications, and to access and modify data and documents. AppleScript uses Apple events, a set of standardized data formats that the Macintosh operating system uses to send information to applications, roughly analogous to sending XPath queries over XML-RPC in the world of web services. Apple events allow a script to work with multiple applications simultaneously, passing data between them so that complex tasks can be accomplished without human interaction. For example, an AppleScript to create a simple web gallery might do the following:

1. Open a photo in a photo-editing application (by sending that application an *Open File* Apple event).
2. Tell the photo-editing application to manipulate the image (e.g. reduce its resolution, add a border, add a photo credit)
3. Tell the photo-editing application to save the changed image in a file in some different folder (by sending that application a *Save* and/or *Close* Apple event).
4. Send the new file path (via another Apple event) to a text editor or web editor application.
5. Tell that editor application to write a link for the photo into an HTML file.
6. Repeat the above steps for an entire folder of images (hundreds or even thousands of photos).
7. Upload the HTML file and folder of revised photos to a website, by sending Apple events to a graphical FTP client, by using built-in AppleScript commands, or by sending Apple events to Unix FTP utilities.

For the user, hundreds or thousands of steps in multiple applications have been reduced to the single act of running the script, and the task is accomplished in much less time and with no possibility of random human error. A large complex script could be developed to run only once, while other scripts are used again and again.

An application's scriptable elements are visible in the application's Scripting Dictionary (distributed as part of the application), which can be viewed in any script editor. Elements are generally grouped into *suites,* according to loose functional relationships between them. There are two basic kinds of elements present in any suite: classes and commands.

- *Classes* are scriptable objects—for example, a text editing application will almost certainly have classes for windows, documents, and texts—and these classes will have properties that can be changed (window size, document background color, text font size, etc.), and may contain other classes (a window will contain one or more documents, a document will contain text, a text object will contain paragraphs and words and characters).
- *Commands*, by contrast, are instructions that can be given to scriptable objects. The general format for a block of AppleScript is to *tell* a scriptable object to run a command.

All scriptable applications share a few basic commands and objects, usually called the Standard Suite—commands to open, close or save a file, to print something, to quit, to set data to variables—as well as a basic *application* object that gives the scriptable properties of the application itself. Many applications have numerous suites capable of performing any task the application itself can perform. In exceptional cases, applications may support plugins which include their own scripting dictionaries.

AppleScript was designed with the ability to build scripts intuitively by recording user actions. Such AppleScript recordability has to be engineered into the app—the app must support Apple events and AppleScript recording; as Finder supports AppleScript recording, it can be useful for reference. When AppleScript Editor (Script Editor) is open and the Record button clicked, user actions for recordable apps are converted to their equivalent AppleScript commands and output to the Script Editor window. The resulting script can be saved and re-run to duplicate the original actions, or modified to be more generally useful.

### Natural language metaphor

Whereas Apple events are a way to send messages into applications, AppleScript is a particular language designed to send Apple events. In keeping with the objective of ease-of-use for beginners, the AppleScript language is designed on the natural language metaphor, just as the graphical user interface is designed on the desktop metaphor. A well-written AppleScript should be clear enough to be read and understood by anyone, and easily edited. The language is based largely on HyperCard's HyperTalk language, extended to refer not only to the HyperCard world of cards and stacks, but also theoretically to any document. To this end, the AppleScript team introduced the AppleEvent Object Model (AEOM), which specifies the objects any particular application "knows".

The heart of the AppleScript language is the use of terms that act as nouns and verbs that can be combined. For example, rather than a different verb to print a page, document or range of pages (such as printPage, printDocument, printRange), AppleScript uses a single "print" verb which can be combined with an object, such as a page, a document or a range of pages.

```mw
print page 1

print document 2

print pages 1 thru 5 of document 2
```

Generally, AEOM defines a number of objects—like "document" or "paragraph"—and corresponding actions—like "cut" and "close". The system also defines ways to refer to properties of objects, so one can refer to the "third paragraph of the document 'Good Day'", or the "color of the last word of the front window". AEOM uses an application *dictionary* to associate the Apple events with human-readable terms, allowing the translation back and forth between human-readable AppleScript and bytecode Apple events. To discover what elements of a program are scriptable, dictionaries for supported applications may be viewed. (In the Xcode and Script Editor applications, this is under *File → Open Dictionary*.)

To designate which application is meant to be the target of such a message, AppleScript uses a "tell" construct:

```mw
tell application "Microsoft Word"
  quit
end tell
```

Alternatively, the tell may be expressed in one line by using an infinitive:

```mw
tell application "Microsoft Word" to quit
```

For events in the "Core Suite" (activate, open, reopen, close, print, and quit), the application may be supplied as the direct object to transitive commands:

```mw
quit application "Microsoft Word"
```

The concept of an object hierarchy can be expressed using nested blocks:

```mw
tell application "QuarkXPress"
  tell document 1
    tell page 2
      tell text box 1
        set word 5 to "Apple"
      end tell
    end tell
  end tell
end tell
```

The concept of an object hierarchy can also be expressed using either nested prepositional phrases or a series of possessives:

```mw
pixel 7 of row 3 of TIFF image "my bitmap"
TIFF image "my bitmap"'s 3rd row's 7th pixel
```

which in another programming language might be expressed as sequential method calls, like in this pseudocode:

```mw
getTIFF("my bitmap").getRow(3).getPixel(7);
```

AppleScript includes syntax for ordinal counting, "the first paragraph", as well as cardinal, "paragraph one". Likewise, the numbers themselves can be referred to as text or numerically, "five", "fifth" and "5" are all supported; they are synonyms in AppleScript. Also, the word "the" can legally be used anywhere in the script in order to enhance readability: it has no effect on the functionality of the script.

## Examples

### Hello, world!

A "Hello, World!" program can be written as a single line. To show a modal window with "OK" and "Cancel" buttons:

```mw
display dialog "Hello, world!"
```

To show a modal window with an "OK" button and an alert icon:

```mw
display alert "Hello, world!"
```

To output audio using a synthesized voice:

```mw
say "Hello, world!"
```

### Failsafe calculator

```mw
tell application "Finder"
	-- Set variables
	set the1 to text returned of (display dialog "1st" default answer "Number here" buttons {"Continue"} default button 1)
	set the2 to text returned of (display dialog "2nd" default answer "Number here" buttons {"Continue"} default button 1)
	try
		set the1 to the1 as integer
		set the2 to the2 as integer
	on error
		display dialog "You may only input numbers into a calculator." with title "ERROR" buttons {"OK"} default button 1
		return
	end try
	
	-- Add?
	if the button returned of (display dialog "Add?" buttons {"No", "Yes"} default button 2) is "Yes" then
		set ans to (the1 + the2)
		display dialog ans with title "Answer" buttons {"OK"} default button 1
		say ans
	-- Subtract?	
	else if the button returned of (display dialog "Subtract?" buttons {"No", "Yes"} default button 2) is "Yes" then
		set ans to (the1 - the2)
		display dialog ans with title "Answer" buttons {"OK"} default button 1
		say ans
	-- Multiply?	
	else if the button returned of (display dialog "Multiply?" buttons {"No", "Yes"} default button 2) is "Yes" then
		set ans to (the1 * the2)
		display dialog ans with title "Answer" buttons {"OK"} default button 1
		say ans
	-- Divide?	
	else if the button returned of (display dialog "Divide?" buttons {"No", "Yes"} default button 2) is "Yes" then
		set ans to (the1 / the2)
		display dialog ans with title "Answer" buttons {"OK"} default button 1
		say ans
	else
		delay 1
		say "You haven't selected a function. The operation has cancelled."
	end if
	
end tell
```

### Drive login

This script controls the Finder application to login with username "John" and password "app123":

```mw
tell application "Finder"
	set passAns to "app123"
	set userAns to "John"
	if the text returned of (display dialog "Username" default answer "") is userAns then
		display dialog "Correct" buttons {"Continue"} default button 1
		if the text returned of (display dialog "Username : John" & return & "Password" default answer "" buttons {"Continue"} default button 1 with hidden answer) is passAns then
			display dialog "Access granted" buttons {"OK"} default button 1
		else
			display dialog "Incorrect password" buttons {"OK"} default button 1
		end if
	else
		display dialog "Incorrect username" buttons {"OK"} default button 1
	end if
end tell
```

## Development tools

### Script editors

The development tools below provide a programing environment for scripting with AppleScript – supporting composing, validating, compiling, running and debugging scripts. Some also provide for listing AppleScript dictionaries, saving scripts in a number of formats, syntax highlighting and inserting code snippets.

**AppleScript Editor**

An editor from Apple packaged with macOS, called

AppleScript Editor

in

Mac OS X Snow Leopard

(10.6) through

OS X Mavericks

(10.9) and

Script Editor

in all earlier and later versions of macOS. Scripts are written in document editing windows where they can be compiled and run, and these windows contain various panes in which logged information, execution results, and other information is available for debugging purposes. Access to scripting dictionaries and prewritten code snippets is available through the application menus. Since

OS X Yosemite

(10.10), Script Editor includes the ability to write in both AppleScript and

JavaScript

.

**Xcode**

A suite of tools from Apple for developing applications with features for editing scripts and creating standalone applications written in AppleScript.

**Script Debugger**

A commercial IDE from

Late Night Software

, Script Debugger is a relatively advanced AppleScript environment that allows the script writer to debug AppleScripts via single

stepping

,

breakpoints

, stepping in and out of functions/subroutines, variable tracking, etc. Script Debugger also contains an advanced dictionary browser that allows the user to see the dictionary in action in real world situations. That is, rather than just a listing of what the dictionary covers, one can open a document in

Pages

, for example, and see how the dictionary's terms apply to that document, making it easier to determine which parts of the dictionary to use. Script Debugger is not designed to create scripts with a GUI, other than basic alerts and dialogs, but is focused more on the coding and debugging of scripts.

**Smile and SmileLab**

A third-party freeware/commercial IDE for AppleScript, itself written entirely in AppleScript.

Smile is free, and primarily designed for AppleScript development. SmileLab is commercial software with extensive additions for numerical analysis, graphing, machine automation and web production. Smile and SmileLab use an assortment of different windows—AppleScript windows for running and saving full scripts, AppleScript terminals for testing code line-by-line, unicode windows for working with text and XML. Users can create complex interfaces—called dialogs—for situations where the built-in dialogs in AppleScript are insufficient.

**ASObjC Explorer 4**

A discontinued commercial IDE from Shane Stanley for AppleScript, especially for

AppleScriptObjC

.

The main feature is

Cocoa

-object/event logging, debugging and code-completion. Users can read Cocoa events and objects like other scriptable applications. This tool was originally built for

AppleScript Libraries

(available in

OS X Mavericks

). AppleScript Libraries aims for re-usable AppleScript components and supports built-in AppleScript dictionary (sdef). ASObjC Explorer 4 can be an external Xcode script editor, too.

**FaceSpan**

A discontinued commercial IDE from

Late Night Software

for creating AppleScript applications with graphic user interfaces.

### Script launchers

For development and ad hoc scenarios, a script can be run from a script editor, but to support automation a script must run without opening another application. There are a number of options for doing so:

**Applets**

AppleScripts can be saved from a script editor as applications (called

applets

, or

droplets

when they accept input via

drag and drop

).

Applets can be run from the

Dock

, from the toolbar of

Finder

windows, from

Spotlight

, from third-party

application launchers

, or from any other place where applications can be run.

**Folder actions**

Using AppleScript folder actions, scripts can be launched when specific changes occur in folders (such as adding or removing files).

Folder actions can be assigned by clicking on a folder and choosing

Folder Actions Setup...

from the contextual menu; the location of this command differs slightly in Mac OS X 10.6.x from earlier versions. This same action can be achieved with third-party utilities such as Hazel.

**Hotkey launchers**

Keyboard shortcuts

can be assigned to AppleScripts in the script menu using the

Keyboard & Mouse Settings

Preference Pane

in

System Preferences

. In addition, various third-party utilities are available—

Alfred

,

FastScripts,

Keyboard Maestro

,

QuicKeys,

Quicksilver

,

TextExpander

—which can run AppleScripts on demand using key combinations.

**Script menu**

This system-wide menu provides access to AppleScripts from the macOS menu bar, visible no matter what application is running.

(In addition, many Apple applications, some third-party applications, and some add-ons provide their own script menus. These may be activated in different ways, but all function in essentially the same manner.) Selecting a script in the script menu launches it. Since Mac OS X 10.6.x, the system-wide script menu can be enabled from the preferences of

Script Editor

; in prior versions of Mac OS X, it could be enabled from the AppleScript Utility application. When first enabled, the script menu displays a default library of fairly generic, functional AppleScripts, which can also be opened in Script Editor and used as examples for learning AppleScript. Scripts can be organized so that they only appear in the menu when particular applications are in the foreground.

**Unix command line and launchd**

AppleScripts can be run from the Unix command line, or from launchd for scheduled tasks,

by using the osascript command line tool.

The osascript tool can run compiled scripts (.scpt files) and plain text files (.applescript files—these are compiled by the tool at runtime). Script applications can be run using the Unix open command.

## Resources

### AppleScript Libraries

Re-usable AppleScript modules (available since OS X Mavericks), written in AppleScript or AppleScriptObjC and saved as script files or bundles in certain locations, that can be called from other scripts. When saved as a bundle, a library can include an AppleScript dictionary (sdef) file, thus functioning like a scripting addition but written in AppleScript or AppleScriptObjC.

### AppleScript Studio

A framework for attaching Cocoa interfaces to AppleScript applications, part of the Xcode package in Mac OS X 10.4 and 10.5, now deprecated in favor of AppleScriptObjC.

### AppleScriptObjC

A Cocoa development software framework, also called AppleScript/Objective-C or ASOC, part of the Xcode package since Mac OS X Snow Leopard. AppleScriptObjC allows AppleScripts to use Cocoa classes and methods directly. The following table shows the availability of AppleScriptObjC in various versions of macOS:

| OS version | In Xcode | In applets | In AppleScript Libraries | In Script Editor |
|---|---|---|---|---|
| 10.6 | (Yes) |   |   |   |
| 10.7 | (Yes) | (Yes) |   |   |
| 10.8 | (Yes) | (Yes) |   |   |
| 10.9 | (Yes) | (Yes) | (Yes) |   |
| 10.10 | (Yes) | (Yes) | (Yes) | (Yes) |

AppleScriptObjC can be used in all subsequent Mac OS X versions.

### Automator

A graphical, modular editing environment in which *workflows* are built up from *actions*. It is intended to duplicate many of the functions of AppleScript without the necessity for programming knowledge. Automator has an action specifically designed to contain and run AppleScripts, for tasks that are too complex for Automator's simplified framework.

### Scriptable core system applications

These background-only applications, packaged with macOS, are used to allow AppleScript to access features that would not normally be scriptable. As of Mac OS X 10.6.3 they include the scriptable applications for:

- VoiceOver (scriptable auditory and braille screen reader package)
- System Events (control of non-scriptable applications and access to certain system functions and basic file operations)
- Printer Setup Utility (scriptable utility for handling print jobs)
- Image Events (core image manipulation)
- HelpViewer (scriptable utility for showing help displays)
- Database Events (minimal SQLite3 database interface)
- AppleScript Utility (for scripting a few AppleScript related preferences)

### Scripting Additions (OSAX)

Plug-ins for AppleScript developed by Apple or third parties. They are designed to extend the built-in command set, expanding AppleScript's features and making it somewhat less dependent on functionality provided by applications. macOS includes a collection of scripting additions referred to as Standard Additions (*StandardAdditions.osax*) that adds a set of commands and classes that are not part of AppleScript's core features, including user interaction dialogs, reading and writing files, file system commands, date functions, and text and mathematical operations; without this OSAX, AppleScript would have no capacity to perform many basic actions not directly provided by an application.

## Language

### Typing

Variables are not strictly typed, and do not need to be declared. Variables can take any data type (including scripts and functions). For example:

```mw
-- create an integer variable called variable1
set variable1 to 1

-- create a text variable called variable2
set variable2 to "Hello" 

-- create a list variable called variable3
copy {17, "doubleday"} to variable3 

-- copy the list items of variable3 into separate variables variable4 and variable5
set {variable4, variable5} to variable3 

-- set a variable to an instance of a script
set variable6 to script myScript
```

### Scoping

A subroutines cannot be called directly from an application tell block. Use of `my` or `of me` is required.

```mw
tell application "Finder"
    set x to my myHandler()
    -- or
    set x to myHandler() of me
end tell

on myHandler()
    --commands
end myHandler
```

Using the same technique for scripting addition commands can reduce errors and improve performance.

```mw
tell application "Finder"
	set anyNumber to my (random number from 5 to 50)
end tell
```

### Types and objects

A script can define custom data types, or use one of the many built-in classes and objects which are provided by the language and tend to be recognized by scriptable applications. Notable built-in types and objects include:

**Basic objects**

- **application**: used mostly as a specifier for tell statements (`tell application "Finder" …`)
- **script**: script objects are containers for scripts; every AppleScript creates a script object when run, and script objects may be created within AppleScripts
- **class**: meta-object that specifies the type of other objects
- **reference**: object that encapsulates an unevaluated object specifier that may or may not point to a valid object; can be evaluated on-demand by accessing its `contents` property

**Standard data objects**

- **constant**: constant value; language-defined constants include `pi`, `tab` and `linefeed`
- **boolean**: Boolean (true/false) value; subclass of `constant`
- **number**: abstract superclass of `integer` and `real`; rarely used directly
- **integer**: integer; can be manipulated with built-in mathematical operators
- **real**: floating-point (real) number; can be manipulated with built-in mathematical operators
- **date**: date and time
- **text**: before AppleScript 2.0 (Mac OS X 10.4 and below) the `text` class was distinct from `string` and `Unicode text`, and the three behaved somewhat differently; in 2.0 (10.5) and later, they are all synonyms and all text is handled as UTF-16

**Containers**

- **list**: ordered list of objects; can contain any class, including other lists and classes defined by applications
- **record**: keyed list of objects; like a list, except structured as key–value pairs; runtime keyed access is unsupported; all keys must be compile-time constant identifiers

**File system**

- **alias**: reference to an existing file system object (file or folder); maintains link to file system object if moved or renamed
- **file**: reference to a file system object; can refer to an object that does not exist
- **POSIX file**: reference to a file system object, in plain text, using Unix (POSIX)-style slash (/) notation; not a true data type, as AppleScript automatically converts a POSIX file to an ordinary file

**Miscellaneous**

- **RGB color**: specifies an RGB triplet (in 16-bit high color format), for use in commands and objects that work with colors
- **unit types**: converts between standard units; for instance, a value can be defined as `square yards`, then converted to `square feet` by casting between unit types using the `as` operator

### Block

AppleScript supports compound statement code structure via either single or multiple line syntax. The multiple line syntax ends a code block with a phrase that like `end *keyword*` where *keyword* is the statement keyword at the start of the block. For example:

```mw
-- Simple form
tell application "Safari" to activate

-- Compound
tell application "MyApp"
     -- commands for app
end tell
```

### Script

A script object is full object – encapsulating methods and data and inheriting data and behavior from a parent script. Script objects can use the same 'tell' constructs that are used for application objects and can be loaded from and saved to files. Runtime performance can be enhanced in some cases by using script objects. A script object is defined as:

```mw
script scriptName
     -- commands and handlers specific to the script
end script
```

### Loop

The loop construct has multiple variations, all using the keyword **repeat**. The loop can be exited via **exit repeat**.

**Unconditional**

```mw
repeat
     -- commands to be repeated
end repeat
```

**Repeat a number of times**

```mw
repeat 10 times
     -- commands to be repeated
end repeat
```

**Conditional**

For **repeat while**, the block is executed as long as a condition evaluates to true. The **repeat until** loop is the same except that the block is executed as long as the condition evaluates to false.

```mw
set x to 5
repeat while x > 0
     set x to x - 1
end repeat

set x to 5
repeat until x ≤ 0
     set x to x - 1
end repeat
```

**With a variable**

A variable is initialized to a value and after each execution of the block, the variable is incremented by the step value; 1 if not specified.

```mw
-- repeat the block 2000 times, i gets all values from 1 to 2000
repeat with i from 1 to 2000
     -- commands to be repeated
end repeat

-- repeat the block 4 times, i gets values 100, 75, 50 and 25
repeat with i from 100 to 25 by -25
    -- commands to be repeated 
end repeat
```

**Enumerate**

A variable has the value of each list item as the loop progresses.

```mw
set total to 0
repeat with loopVariable in {1, 2, 3, 4, 5}
	set total to total + loopVariable
end repeat
```

### Handler

A **handler**, a variation of the block structure defines a subroutine.

**Function handler**

```mw
on myFunction(parameters...)
     -- subroutine commands 
end myFunction
```

**Folder actions block**

```mw
on adding folder items to thisFolder after receiving theseItems
     -- commands to apply to the folder or items 	
end adding folder items to
```

**Run handler**

```mw
on run
     -- commands
end run
```

Handlers can also be defined using "to" in place of "on" and can be written to accept labeled parameters, not enclosed in parens.

**Handler with labeled parameters**

```mw
on rock around the clock
	display dialog (clock as string)
end rock
-- called with:
rock around the current date
```

**Handler using "to" and labeled parameters**

```mw
to check for yourNumber from bottom thru top
	if bottom ≤ yourNumber and yourNumber ≤ top then
		display dialog "Congratulations! You scored."
	end if
end check
--called with:
check for 8 from 7 thru 10
```

There are four types of predefined handlers in AppleScript—run, open, idle, and quit—each of which is created in the same way as the run handler shown above.

**Run handler**

Defines the main code of the script, which is called when the script is run. Run handler blocks are optional, unless arguments are being passed to the script. If an explicit run handler block is omitted, then all code that is not contained inside handler blocks is executed as though it were in an implicit run handler.

**Open handler**

Defined using "on open theItems".

```mw
on open theItems
     repeat with thisItem in theItems
         tell application "Finder" to update thisItem
     end repeat 
end open
```

When a script containing an "open handler' is saved as an applet, the applet becomes a droplet. A droplet can be identified in the Finder by its icon, which includes an arrow, indicating items can be dropped onto the icon. The droplet's open handler is executed when files or folders are dropped onto droplet's icon. References to the items dropped on the droplet's icon are passed to the droplet's script as the parameter of the open handler. A droplet can also be launched the same way as an ordinary applet, executing its run handler.

**Idle handler**

A subroutine that is run periodically by the system when the application is idle.

```mw
on idle
     --code to execute when the script's execution has completed
  return 60 -- number of seconds to pause before executing idle handler again
end idle
```

An idle handler can be used in applets or droplets saved as stay-open applets, and is useful for scripts that watch for particular data or events. The length of the idle time is 30 seconds by default, but can be changed by including a 'return x' statement at the end of the subroutine, where x is the number of seconds the system should wait before running the handler again.

**Quit handler**

A handler that is run when the applet receives a Quit request. This can be used to save data or do other ending tasks before quitting.

```mw
on quit
     --commands to execute before the script quits
  continue quit -- required for the script to actually quit
end quit
```

A comment can be formatted various ways. A line comment begins with `--` or alternatively in later versions (AppleScript 2.0, first released in Mac OS X Leopard) with `#`. The latter permits an AppleScript script to run as an executable if it begins with a shebang line `#!/usr/bin/osascript`. For example:

```mw
--This is a line comment
# So is this! (in later versions)
```

A block comment (can be multiple lines) is delimited by `(*` and `*)`. For example:

```mw
(* This is a
multiple
line
comment *)
```

### User interaction

AppleScript has several user interface options, including dialogs, alerts, and list of choices. (The character, produced by typing ⌥ Option+return in the Script Editor, denotes continuation of a single statement across multiple lines.)

```mw
-- Dialog
set dialogReply to display dialog "Dialog Text"
	default answer "Text Answer"
	hidden answer false
	buttons {"Skip", "Okay", "Cancel"}
	default button "Okay"
	cancel button "Skip"
	with title "Dialog Window Title"
	with icon note
	giving up after 15
```

```mw
-- Choose from list
set chosenListItem to choose from list {"A", "B", "3"}
	with title "List Title"
	with prompt "Prompt Text"
	default items "B"
	OK button name "Looks Good!"
	cancel button name "Nope, try again"
	multiple selections allowed false
	with empty selection allowed
```

```mw
-- Alert
set resultAlertReply to display alert "Alert Text"
	as warning
	buttons {"Skip", "Okay", "Cancel"}
	default button 2
	cancel button 1
	giving up after 2
```

Each user interaction method can return the values of buttons clicked, items chosen or text entered for further processing. For example:

```mw
display alert "Hello, world!" buttons {"Rudely decline", "Happily accept"}
set theAnswer to button returned of the result
if theAnswer is "Happily accept" then
	beep 5
else
	say "Piffle!"
end if
```

## Open Scripting Architecture

Apple provides the **Open Scripting Architecture** (OSA) for other scripting languages and third-party scripting/automation products (such as QuicKeys and UserLand Frontier) to function on an equal status with AppleScript. AppleScript is implemented as a component of Component Manager, and the basic specs for interfacing such components to the OSA are public, allowing other developers to add their own scripting components to the system. Public client APIs for loading, saving and compiling scripts work the same for all such components, which means that applets and droplets can hold scripts in any of those scripting languages.

One feature of the OSA is scripting additions, or OSAX for *Open Scripting Architecture eXtension*, which were inspired by HyperCard's External Commands. Scripting additions are libraries that allow programmers to extend the function of AppleScript. Commands included as scripting additions are available system-wide, and are not dependent on an application (see also § AppleScript Libraries). The AppleScript Editor is also able to directly edit and run some of the OSA languages.

### JavaScript for Automation

Under OS X Yosemite and later versions of macOS, the **JavaScript for Automation** (**JXA**) component remains the only serious OSA language alternative to AppleScript, though the Macintosh versions of Perl, Python, Ruby, and Tcl all support native means of working with Apple events without being OSA components.

JXA also provides an Objective-C (and C language) foreign language interface. Being an environment based on WebKit's JavaScriptCore engine, the JavaScript feature set is in sync with the system Safari browser engine. JXA provides a JavaScript module system and it is also possible to use CommonJS modules via browserify.
