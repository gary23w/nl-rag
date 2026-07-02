---
title: "PySide"
source: https://en.wikipedia.org/wiki/PySide
domain: pyside-binding
license: CC-BY-SA-4.0
tags: pyside binding, qt for python, shiboken generator, official qt python
fetched: 2026-07-02
---

# PySide

**PySide** is a Python binding of the cross-platform GUI toolkit Qt developed by The Qt Company, as part of the **Qt for Python** project. It is one of the alternatives to the standard library package Tkinter. Like Qt, PySide is free software. PySide supports Linux/X11, macOS, and Microsoft Windows. The project can also be cross compiled to embedded systems like Raspberry Pi, and Android devices.

## History

By 2009, Nokia, the then owners of the Qt toolkit, wanted Python binding available under the LGPL license. Nokia failed to reach an agreement with Riverbank Computing, the developers of the PyQt Python binding. In August, Nokia released PySide. It provided similar functionality, but under the LGPL. 'Side' is Finnish for binding.

There have been three major versions of PySide:

- PySide supports Qt 4
- PySide2 supports Qt 5
- PySide6 supports Qt 6

PySide version 1 was released in August 2009 under the LGPL by Nokia, then the owner of the Qt toolkit, after it failed to reach an agreement with PyQt developers Riverbank Computing to change its licensing terms to include LGPL as an alternative license. It supported Qt 4 under the operating systems Linux/X11, Mac OS X, Microsoft Windows, Maemo and MeeGo, while the PySide community added support for Android.

PySide2 was started by Christian Tismer to port PySide from Qt 4 to Qt 5 in 2015. The project was then folded into the Qt Project. It was released in December 2018.

PySide6 was released in December 2020. It added support for Qt 6 and removed support for all Python versions older than 3.6.

The project started out using Boost. Python from the Boost C++ libraries for the bindings. It later created its own binding generator named Shiboken, to reduce the size of the binaries and the memory footprint.

## "Hello, world!" example

```mw
import sys
from PySide6 import QtCore, QtWidgets

# Create a Qt application
app = QtWidgets.QApplication(sys.argv)

# Create the main window
main_window = QtWidgets.QWidget()
main_window.resize(320, 240)
main_window.setWindowTitle('"Hello, world!" example')

# Create a label for text in the main window
label = QtWidgets.QLabel(main_window)
label.setText("Hello, world!")
label.setGeometry(QtCore.QRect(100, 100, 100, 100))

# Show the main window
main_window.show()

# Enter the main loop and exit when done
sys.exit(app.exec())
```
