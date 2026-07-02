---
title: "wxPython"
source: https://en.wikipedia.org/wiki/WxPython
domain: wxpython
license: CC-BY-SA-4.0
tags: wxpython binding, phoenix wrapper, native python widgets, wxwidgets python
fetched: 2026-07-02
---

# wxPython

**wxPython** is a wrapper for the cross-platform GUI API (often referred to as a "toolkit") wxWidgets (which is written in C++) for the Python programming language. It is one of the alternatives to Tkinter. It is implemented as a Python extension module (native code).

## History

In 1995, Robin Dunn needed a GUI application to be deployed on HP-UX systems but also run Windows 3.1 within short time frame. He needed a cross-platform solution. While evaluating free and commercial solutions, he ran across Python bindings on the wxWidgets toolkit webpage (known as wxWindows at the time). This was Dunn's introduction to Python. Together with Harri Pasanen and Edward Zimmerman he developed those initial bindings into wxPython 0.2.

In August 1998, version 0.3 of wxPython was released. It was built for wxWidgets 2.0 and ran on Win32, with a wxGTK version in the works.

The first versions of the wrapper were created by hand. However, the code became difficult to maintain and keep synchronized with wxWidgets releases. By 1997, versions were created with SWIG, greatly decreasing the amount of work to update the wrapper.

### Project Phoenix

In 2010, the Project Phoenix began; an effort to clean up the wxPython implementation and in the process make it compatible with Python 3. The project is a new implementation of wxPython, focused on improving speed, maintainability and extensibility. Like the previous version of wxPython, it wraps the wxWidgets C++ toolkit and provides access to the user interface portions of the wxWidgets API.

With the release of 4.0.0a1 wxPython in 2017, the Project Phoenix version became the official version. wxPython 4.x is the current version being developed as of June 2022.

## Use

wxPython enables Python to be used for cross-platform GUI applications requiring very little, if any, platform-specific code.

### Example

This is a simple "Hello world" module, depicting the creation of the two main objects in wxPython (the main window object and the application object), followed by passing the control to the event-driven system (by calling `MainLoop()`) which manages the user-interactive part of the program.

```mw
#!/usr/bin/env python3

import wx

app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, title="Hello World") # A Frame is a top-level window.
frame.Show(True)     # Show the frame.
app.MainLoop()
```

This is another example of the wxPython Close Button with wxPython GUI display show in Windows 10 operating system.

```mw
import wx

class WxButton(wx.Frame):

    def __init__(self, *args, **kw):
        super(WxButton, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        closeButton = wx.Button(pnl, label='Close Me', pos=(20, 20))

        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)

        self.SetSize((350, 250))
        self.SetTitle('Close Button')
        self.Centre()

    def OnClose(self, e):
        self.Close(True)

def main():
    app = wx.App()
    ex = WxButton(None)
    ex.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
```

## License

Being a wrapper, wxPython uses the same free software license used by wxWidgets (wxWindows License)—which is approved by Free Software Foundation and Open Source Initiative.

## Applications developed with wxPython

- Chandler, a personal information manager
- Dropbox, desktop client for the Dropbox cloud-based storage
- Editra, a multi-platform text editor
- Google Drive, desktop client for the Google cloud-based storage system
- GRASS GIS, a free, open source geographical information system
- Métamorphose, a batch renamer
- Phatch, a photo batch processor
- PlayOnLinux and PlayOnMac, Wine front-ends
- PsychoPy, experiment creation tool for neuroscience and psychology research
