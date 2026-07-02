---
title: "Message loop in Microsoft Windows"
source: https://en.wikipedia.org/wiki/Message_loop_in_Microsoft_Windows
domain: windows-forms
license: CC-BY-SA-4.0
tags: windows forms, winforms controls, dotnet desktop gui, event handler wiring
fetched: 2026-07-02
---

# Message loop in Microsoft Windows

The **message loop** is an obligatory section of code in every program that uses a graphical user interface under Microsoft Windows. Windows programs that have a GUI are event-driven. Windows maintains an individual message queue for each thread that has created a window. Usually only the first thread creates windows. Windows places messages into that queue whenever mouse activity occurs on that thread's window, whenever keyboard activity occurs while that window has focus, and at other times. A process can also add messages to its own queue. To accept user input, and for other reasons, each thread with a window must continuously retrieve messages from its queue, and act on them. A programmer makes the process do that by writing a loop that calls GetMessage (which blocks for a message and retrieves it), and then calls DispatchMessage (which dispatches the message), and repeats indefinitely. This is the message loop. There usually is a message loop in the main program, which runs on the main thread, and additional message loop in each created modal dialog. Messages for *every* window of the process pass through its message queue, and are handled by its message loop. A message loop is one kind of event loop.

A basic message loop appears as follows:

```mw
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
    MSG msg;
    int bRet;

    while (1)
    {
        bRet = GetMessage(&msg, NULL, 0, 0);

        if (bRet == -1)  // If bRet is -1, GetMessage has failed.
        {
            // Handle or log the error; possibly exit.
            // ...
        }
        else if (bRet != 0)  // If bRet is not 0 or -1, the message must be processed.
        {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
        else  // If bRet is 0, the message loop should exit.
        {
            break;
        }
    }
    return msg.wParam;
}
```

It is conventional for the event loop to call `TranslateMessage` on each message which can translate virtual keystrokes into strings. Calling `TranslateMessage` is not technically required, but problems can result if it is not called. The message loop must call `DispatchMessage`.

The message loop does not directly act on the messages that it handles. It dispatches them by calling `DispatchMessage`, which transfers the message to the "window procedure" for the window that the message was addressed to. (The "window procedure" is a callback procedure, which got associated with the window class when it was registered.) (More than one window can use the same window procedure.)

Code can also send messages directly to a window procedure. These are called nonqueued messages.

A strict message loop is not the only option. Code elsewhere in the program can also accept and dispatch messages. `PeekMessage` is a non-blocking call that returns immediately, with a message if any are waiting, or no message if none is waiting. `WaitMessage` allows a thread to sleep until a message is in the queue.

Modern graphical interface frameworks, such as Windows Forms, Windows Presentation Foundation, MFC, Delphi, Qt, and others do not require applications to code a Windows message loop, because they automatically route events such as key presses and mouse clicks to their appropriate handlers as defined within the framework. However, each framework implements a message loop somewhere, and the message loop can usually be accessed or replaced when more direct control is required.
