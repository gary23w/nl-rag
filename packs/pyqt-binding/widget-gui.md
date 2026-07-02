---
title: "Graphical widget"
source: https://en.wikipedia.org/wiki/Widget_(GUI)
domain: pyqt-binding
license: CC-BY-SA-4.0
tags: pyqt binding, python qt wrapper, sip generated binding, qt widgets python
fetched: 2026-07-02
---

# Graphical widget

(Redirected from

Widget (GUI)

)

In a graphical user interface (GUI), a **graphical widget** (also **graphical control element** or **control**) is an element of interaction, such as a button or a scroll bar. Controls are software components that a computer user interacts with through direct manipulation to read or edit information about an application. User interface libraries such as Windows Presentation Foundation, Qt, GTK, and Cocoa, contain a collection of controls and the logic to render these.

Each widget facilitates a specific type of user-computer interaction, and appears as a visible part of the application's GUI as defined by the theme and rendered by the rendering engine. The theme makes all widgets adhere to a unified aesthetic design and creates a sense of overall cohesion. Some widgets support interaction with the user, for example labels, buttons, and check boxes. Others act as containers that group the widgets added to them, for example windows, panels, and tabs.

Structuring a user interface with widget toolkits allows developers to reuse code for similar tasks, and provides users with a common language for interaction, maintaining consistency throughout the whole information system.

Graphical user interface builders facilitate the authoring of GUIs in a WYSIWYG manner employing a user interface markup language. They automatically generate all the source code for a widget from general descriptions provided by the developer, usually through direct manipulation.

## History

Around 1920, *widget* entered American English, as a generic term for any useful device, particularly a product manufactured for sale; a gadget.

In 1988, the term *widget* is attested in the context of Project Athena and the X Window System. In *An Overview of the X Toolkit* by Joel McCormack and Paul Asente, it says:

> The toolkit provides a library of user-interface components ("widgets") like text labels, scroll bars, command buttons, and menus; enables programmers to write new widgets; and provides the glue to assemble widgets into a complete user interface.

The same year, in the manual *X Toolkit Widgets - C Language X Interface* by Ralph R. Swick and Terry Weissman, it says:

> In the X Toolkit, a widget is the combination of an X window or sub window and its associated input and output semantics.

Finally, still in the same year, Ralph R. Swick and Mark S. Ackerman explain where the term *widget* came from:

> We chose this term since all other common terms were overloaded with inappropriate connotations. We offer the observation to the skeptical, however, that the principal realization of a widget is its associated X window and the common initial letter is not un-useful.

## Usage

Any widget displays an information arrangement changeable by the user, such as a window or a text box. The defining characteristic of a widget is to provide a single interaction point for the direct manipulation of a given kind of data. In other words, widgets are basic visual building blocks which, combined in an application, hold all the data processed by the application and the available interactions on this data.

GUI widgets are graphical elements used to build the human-machine-interface of a program. GUI widgets are implemented like software components. Widget toolkits and software frameworks, like e.g. GTK+ or Qt, contain them in software libraries so that programmers can use them to build GUIs for their programs.

A family of common reusable widgets has evolved for holding general information based on the Palo Alto Research Center Inc. research for the Xerox Alto User Interface. Various implementations of these generic widgets are often packaged together in widget toolkits, which programmers use to build graphical user interfaces (GUIs). Most operating systems include a set of ready-to-tailor widgets that a programmer can incorporate in an application, specifying how it is to behave. Each type of widget generally is defined as a class by object-oriented programming (OOP). Therefore, many widgets are derived from class inheritance.

In the context of an application, a widget may be *enabled* or *disabled* at a given point in time. An enabled widget has the capacity to respond to events, such as keystrokes or mouse actions. A widget that cannot respond to such events is considered disabled. The appearance of a widget typically differs depending on whether it is enabled or disabled; when disabled, a widget may be drawn in a lighter color ("**grayed out**") or be obscured visually in some way. See the adjacent image for an example.

The benefit of disabling unavailable controls rather than hiding them entirely is that users are shown that the control exists but is currently unavailable (with the implication that changing some other control may make it available), instead of possibly leaving the user uncertain about where to find the control at all. On pop-up dialogues, buttons might appear greyed out shortly after appearance to prevent accidental clicking or inadvertent double-tapping.

Widgets are sometimes qualified as *virtual* to distinguish them from their physical counterparts, e.g. *virtual* buttons that can be clicked with a pointer, vs. physical buttons that can be pressed with a finger (such as those on a computer mouse).

A related (but different) concept is the desktop widget, a small specialized GUI application that provides some visual information and/or easy access to frequently used functions such as clocks, calendars, news aggregators, calculators and desktop notes. These kinds of widgets are hosted by a widget engine.

## List of common generic widgets

### Selection and display of collections

- Button – control which can be clicked upon to perform an action. An equivalent to a push-button as found on mechanical or electronic instruments.
  - Radio button – control which can be clicked upon to select one option from a selection of options, similar to selecting a radio station from a group of buttons dedicated to radio tuning. Radio buttons always appear in pairs or larger groups, and only one option in the group can be selected at a time; selecting a new item from the group's buttons also de-selects the previously selected button.
  - Check box – control which can be clicked upon to enable or disable an option. Also called a tick box. The box indicates an "on" or "off" state via a check mark/tick ☑ or a cross ☒. Can be shown in an intermediate state (shaded or with a dash) to indicate that various objects in a multiple selection have different values for the property represented by the check box. Multiple check boxes in a group may be selected, in contrast with radio buttons.
  - Toggle switch - Functionally similar to a check box. Can be toggled on and off, but unlike check boxes, this typically has an immediate effect.
  - Toggle Button - Functionally similar to a check box, works as a switch, though appears as a button. Can be toggled on and off.
  - Split button – control combining a button (typically invoking some default action) and a drop-down list with related, secondary actions
  - Cycle button - a button that cycles its content through two or more values, thus enabling selection of one from a group of items.
- Slider – control with a handle that can be moved up and down (vertical slider) or right and left (horizontal slider) on a bar to select a value (or a range if two handles are present). The bar allows users to make adjustments to a value or process throughout a range of allowed values.
- List box – a graphical control element that allows the user to select one or more items from a list contained within a static, multiple line text box.
- Spinner – value input control which has small up and down buttons to step through a range of values
- Drop-down list – A list of items from which to select. The list normally only displays items when a special button or indicator is clicked.
- Menu – control with multiple actions which can be clicked upon to choose a selection to activate
  - Context menu – a type of menu whose contents depend on the *context* or state in effect when the menu is invoked
  - Pie menu – a circular context menu where selection depends on direction
- Menu bar – a graphical control element which contains drop down menus
- Toolbar – a graphical control element on which on-screen buttons, icons, menus, or other input or output elements are placed
  - Ribbon – a hybrid of menu and toolbar, displaying a large collection of commands in a visual layout through a tabbed interface.
- Combo box (text box with attached menu or List box) – A combination of a single-line text box and a drop-down list or list box, allowing the user to either type a value directly into the control or choose from the list of existing options.
- Icon – a quickly comprehensible symbol of a software tool, function, or a data file.
- Tree view – a graphical control element that presents a hierarchical view of information
- Grid view or datagrid – a spreadsheet-like tabular view of data that allows numbers or text to be entered in rows and columns.

### Navigation

- Link – Text with some kind of indicator (usually underlining and/or color) that indicates that clicking it will take one to another screen or page.
- Tab – a graphical control element that allows multiple documents or panels to be contained within a single window
- Scrollbar – a graphical control element by which continuous text, pictures, or any other content can be scrolled in a predetermined direction (up, down, left, or right)

### Text/value input

- Text box – (edit field) - a graphical control element intended to enable the user to input text

### Output

- Label – text used to describe another widget
- Tooltip – informational window which appears when the mouse hovers over another control
- Balloon help
- Status bar – a graphical control element which poses an information area typically found at the window's bottom
- Progress bar – a graphical control element used to visualize the progression of an extended computer operation, such as a download, file transfer, or installation
- Infobar – a graphical control element used by many programs to display non-critical information to a user

### Container

- Window – a graphical control element consisting of a visual area containing some of the graphical user interface elements of the program it belongs to
- Collapsible panel – a panel that can compactly store content which is hidden or revealed by clicking the tab of the widget.
  - Drawer: Side sheets or surfaces containing supplementary content that may be anchored to, pulled out from, or pushed away beyond the left or right edge of the screen.
- Accordion – a vertically stacked list of items, such as labels or thumbnails where each item can be "expanded" to reveal the associated content
- Modal window – a graphical control element subordinate to an application's main window which creates a mode where the main window can not be used.
- Dialog box – a small window that communicates information to the user and prompts for a response
- Palette window – also known as "Utility window" - a graphical control element which floats on top of all regular windows and offers ready access tools, commands or information for the current application
  - Inspector window – a type of dialog window that shows a list of the current attributes of a selected object and allows these parameters to be changed on the fly
- Frame – a type of box within which a collection of graphical control elements can be grouped as a way to show relationships visually
- Canvas – generic drawing element for representing graphical information
- Cover Flow – an animated, three-dimensional element to visually flipping through snapshots of documents, website bookmarks, album artwork, or photographs.
- Bubble Flow – an animated, two-dimensional element that allows users to browse and interact the entire tree view of a discussion thread.
- Carousel (computing) – a graphical widget used to display visual cards in a way that's quick for users to browse, both on websites and on mobile apps
