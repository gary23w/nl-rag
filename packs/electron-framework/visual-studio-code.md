---
title: "Visual Studio Code"
source: https://en.wikipedia.org/wiki/Visual_Studio_Code
domain: electron-framework
license: CC-BY-SA-4.0
tags: electron framework, chromium desktop app, node desktop runtime, web technology packaging
fetched: 2026-07-02
---

# Visual Studio Code

**Visual Studio Code** (commonly referred to as **VS Code**) is an integrated development environment developed by Microsoft for Windows, Linux, macOS and web browsers. Features include support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded version control with Git. Users can change the theme, keyboard shortcuts and preferences, as well as install extensions that add functionality, including to extend its capabilities to function as an IDE for other languages.

Visual Studio Code is proprietary software released under the "Microsoft Software License", but based on the MIT licensed program named "Visual Studio Code – Open Source" (also known as "Code – OSS"), also created by Microsoft and available through GitHub.

In the 2025 Stack Overflow Developer Survey, out of over 49,000 responses, 75.9% of respondents reported using Visual Studio Code, more than twice the percentage of respondents who reported using its nearest alternative, Visual Studio.

## History

Visual Studio Code was first announced on April 29, 2015, by Microsoft at the 2015 Build conference. A preview build was released shortly thereafter.

On November 18, 2015, the project "Visual Studio Code – Open Source" (also known as "Code – OSS"), on which Visual Studio Code is based, was released under the open-source MIT License and made available on GitHub.

Extension support was also announced. On April 14, 2016, Visual Studio Code graduated from the public preview stage and was released to the web.

## Features

### Code editor

Visual Studio Code includes a source-code editor that can be used with a variety of programming languages, including C, C#, C++, Fortran, Go, Java, JavaScript, Node.js, Python, Rust, and Julia. Visual Studio Code employs the same editor component (codenamed "Monaco") used in Azure DevOps (formerly called "Visual Studio Online" and "Visual Studio Team Services").

The downloadable version of Visual Studio Code is built on the Electron framework, which is used to develop Node.js web applications that run on the Blink layout engine. Visual Studio Code for the Web is a browser-based version of the editor that can be used to edit both local files and remote repositories (on GitHub and Microsoft Azure) without installing the full program. It is officially supported and hosted by Microsoft and can be accessed at vscode.dev.

Out of the box, Visual Studio Code includes basic support for most common programming languages. This basic support includes syntax highlighting, bracket matching, code folding, and configurable snippets. Visual Studio Code also ships with IntelliSense for JavaScript, TypeScript, JSON, CSS, and HTML, as well as debugging support for Node.js. Support for additional languages can be provided by freely available extensions on the VS Code Marketplace.

### Debugging

VS Code features a built-in debugger designed to enhance the development process. It provides native support for debugging Node.js applications, while additional debuggers for other programming languages can be installed via extensions. The debugger allows developers to attach to running processes and step through source code line-by-line during execution, offering a detailed view of program flow. It can also display disassembly for low-level analysis in C++. Furthermore, users can set breakpoints – either standard or conditional – to pause execution at specific points and examine the program's state, while also monitoring variable values in real-time as the code runs.

An interactive feature of VS Code's debugging toolkit is the Debug Console. This panel is integrated directly into the debugging session, enabling users to evaluate expressions, such as checking variable values or testing functions, and execute commands on the fly. This functionality provides developers with greater control and deeper insight into the program's behavior.

### File management and workspace

Instead of a project system, VS Code allows users to open one or more directories, which can then be saved in workspaces for future reuse. This allows it to operate as a language-agnostic code editor for any language. It supports many programming languages and a set of features that differ per language. Unwanted files and folders can be excluded from the project tree via settings.

### Command Palette

Many Visual Studio Code features are not exposed through menus or the user interface but can be accessed via the Command Palette. The Command Palette is able to execute virtually every feature the graphical interface supports, making it very keyboard-accessible.

### Integrated terminal

Visual Studio Code provides a fully featured *integrated terminal* that opens at the root of the current workspace, allowing users to run shell commands without leaving the editor environment. It can be toggled via **View → Terminal**, the Command Palette (`View: Toggle Integrated Terminal`), or the keyboard shortcut (`Ctrl+'`). Users may open multiple terminals in tabs or split panes, rename them, and kill sessions individually, directly within the editor UI.

This terminal hosts any shell installed on the system—Bash, Zsh, PowerShell, Fish, Git Bash, WSL, etc.—and detects available profiles automatically, making it simple to switch contexts via the dropdown menu or the `Terminal: Select Default Profile` command.

Beyond basic command execution, VS Code's shell integration also contains clickable file links, working directory awareness, and error-detection markers in the scrollbar. These enhancements simplify tracing errors and navigating code paths by allowing direct jumps to source files, preserving the current working directory context, and highlighting problems inline within the terminal's scroll bar.

### Extensibility and customization

Visual Studio Code can be extended via extensions. Users may install extensions from the VS Code Marketplace to add language support, editor, themes, debuggers, and additional utilities. A notable feature is the ability to create extensions that add support for new languages, themes, debuggers, time travel debuggers, perform static code analysis, and add code linters using the Language Server Protocol.

### Source control

Source control is a built-in feature of Visual Studio Code. It has a dedicated tab inside the menu bar where users can access version control settings and view changes made to the current project. To use the feature, Visual Studio Code must be linked to any supported version control system (Git, Apache Subversion, Perforce, etc.). This allows users to create repositories and to make push and pull requests directly from the Visual Studio Code program.

Visual Studio Code collects usage data and sends it to Microsoft to help improve the product. This telemetry feature can be disabled. The information contained in this telemetry data can be inspected by the public, since the product is open source.

### Remote development and web-based access

VS Code supports remote development through extensions such as Remote–SSH, Remote–Containers, and Remote–WSL. These tools enable users to connect to and develop within remote environments, including servers and containers.

Visual Studio Code for the Web (accessible at vscode.dev) allows users to edit files directly in a web browser without the need to install the desktop application. This version supports basic editing tasks and integration with remote repositories.

### Insiders

VS Code Insiders is a nightly build version of this code editor, providing users with the opportunity to experience new features, bug fixes, and improvements ahead of their official release. It is compiled every night based on the latest changes from the development team, allowing users to test and provide feedback before these updates are officially released in the stable version.

This version is completely independent of the standard version, meaning users can install and run both simultaneously without any interference between their settings, extensions, or themes. This design enables developers to explore and experiment with the latest features of the code editor without affecting their primary development environment.

## Reception

In the 2016 Stack Overflow Developer Survey, Visual Studio Code ranked 13th among the top popular development tools, with only 7% of the 47,000 respondents using it. Two years later, Visual Studio Code rose to the no. 1 spot, with 35% of the 75,000 respondents using it. Since then Visual Studio Code has retained the no. 1 spot, with the percentage of respondents reporting using it increasing to 50% in 2019, 74.5% in 2021, 74.48% in 2022, 73.71% in 2023, 73.6% in 2024, and 75.9% in 2025. The 2020 Developers Survey did not cover integrated development environments.

## Derivatives

| Name | Developed by | License | Notes |
|---|---|---|---|
| Antigravity | Google | Proprietary |   |
| Cursor | Anysphere | Proprietary |   |
| Trae | ByteDance | Proprietary |   |
| VSCodium | VSCodium contributors | MIT |   |
| Windsurf | Windsurf | Proprietary |   |
