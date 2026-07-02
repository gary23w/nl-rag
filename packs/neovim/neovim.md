---
title: "Neovim"
source: https://en.wikipedia.org/wiki/Neovim
domain: neovim
license: CC-BY-SA-4.0
tags: neovim editor, text editor, modal editing, lua configuration
fetched: 2026-07-02
---

# Neovim

**Neovim** is a terminal text editor forked from Vim created to refactor and improve the maintainability of Vim's original code and improving the extensibility of Vim by adding support for Lua scripting. Some features of the fork include built-in Language Server Protocol (LSP) support, support for asynchronous I/O by using the C library libuv, a built in terminal emulator and support for Lua scripting by using LuaJIT language interpreter, allowing both plugin scripting and running scripts in headless / batch mode. Neovim also cleans up the outdated Vim codebase, making startup faster and allowing for asynchronous code execution. The project is open source and is licensed under the Apache 2.0 license. Its source code is available on GitHub.

## History

The Neovim project was started in 2014 by Thiago de Arruda as an effort to completely rework the outdated Vim source code as "Vim's rebirth of the 21st century" after a patch to Vim adding support for multi-threading was rejected. Neovim had a successful fundraising in March 2014, supporting at least one full-time developer.

Neovim is meant as a successor to Vim, not a replacement. As such, the project aims to build on top of Vim's features and source code while maintaining Vim's "character" and almost all of its features.

Over the years, various technical improvements were made to the source code, such as making the source code slimmer and more optimized, making features such as search faster and making Neovim extensible with the addition of support for Lua scripting.

Neovim has gained popularity in the development scene, and as of January 2026 Neovim gained almost 96 thousand stars on GitHub compared to Vim's almost 40 thousand. In 2025, Neovim was voted the most admired development environment in the Stack Overflow developer survey for the fifth consecutive year.

## Features and versions

With the 0.5 release of Neovim on 2 July 2021, it gained built-in support for the LSP, Tree-sitter, and more complete Lua support – including the support for more powerful configuration scripts written in Lua like NvChad and LazyVim instead of the outdated Vim script, scripts that extend Neovim's functionality by adding various features like text completion, syntax highlighting, mouse support and other features found in modern IDEs and text editors.

Support for versions of Vim script prior to Vim9script still exists, maintaining retrocompatibility with older configuration files made for Vim, but support for Vim9script will not be added due to the developers focusing on Lua improvements and because Vim script is considered hard to read and unintuitive.

Neovim is designed with a client-server architecture, allowing users to use core functionality through alternative interfaces. Although Neovim is conventionally utilized through a terminal emulator, several graphical user interfaces have been developed as frontends.

Since version 0.9 Neovim supports EditorConfig.

Version 0.11 of Neovim improved handling of text completion and made the configuration of LSP servers easier.

## Gallery

- (Neovim featuring configured statusbar and dark colorscheme.) Neovim featuring configured statusbar and dark colorscheme.
- (Tweaked v0.9.0-dev version.) Tweaked v0.9.0-dev version.
