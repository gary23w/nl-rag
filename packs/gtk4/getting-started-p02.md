---
title: "Gtk – 4.0: Getting Started with GTK (part 2/2)"
source: https://docs.gtk.org/gtk4/getting_started.html
domain: gtk4
license: CC-BY-SA-4.0
tags: gtk4 toolkit, gtk widgets, gnome application, libadwaita styling
fetched: 2026-07-02
part: 2/2
---

## Building applications

An application consists of a number of files:

**The binary**

This gets installed in

/usr/bin

.

**A desktop file**

The desktop file provides important information about the application to the desktop shell, such as its name, icon, D-Bus name, commandline to launch it, etc. It is installed in

/usr/share/applications

.

**An icon**

The icon gets installed in

/usr/share/icons/hicolor/48x48/apps

, where it will be found regardless of the current theme.

**A settings schema**

If the application uses GSettings, it will install its schema in

/usr/share/glib-2.0/schemas

, so that tools like dconf-editor can find it.

**Other resources**

Other files, such as GtkBuilder ui files, are best loaded from resources stored in the application binary itself. This eliminates the need for most of the files that would traditionally be installed in an application-specific location in

/usr/share

.

GTK includes application support that is built on top of `GApplication`. In this tutorial we’ll build a simple application by starting from scratch, adding more and more pieces over time. Along the way, we’ll learn about `GtkApplication`, templates, resources, application menus, settings, `GtkHeaderBar`, `GtkStack`, `GtkSearchBar`, `GtkListBox`, and more.

The full, buildable sources for these examples can be found in the `examples` directory of the GTK source distribution, or online in the GTK source code repository. You can build each example separately by using make with the `Makefile.example` file. For more information, see the `README` included in the examples directory.

### A trivial application

When using `GtkApplication`, the `main()` function can be very simple. We just call `g_application_run()` and give it an instance of our application class.

```
#include <gtk/gtk.h>

#include "exampleapp.h"

int
main (int argc, char *argv[])
{
  return g_application_run (G_APPLICATION (example_app_new ()), argc, argv);
}
```

All the application logic is in the application class, which is a subclass of `GtkApplication`. Our example does not yet have any interesting functionality. All it does is open a window when it is activated without arguments, and open the files it is given, if it is started with arguments.

To handle these two cases, we override the `activate()` vfunc, which gets called when the application is launched without commandline arguments, and the `open()` virtual function, which gets called when the application is launched with commandline arguments.

To learn more about `GApplication` entry points, consult the GIO documentation.

```
#include <gtk/gtk.h>

#include "exampleapp.h"
#include "exampleappwin.h"

struct _ExampleApp
{
  GtkApplication parent;
};

G_DEFINE_TYPE(ExampleApp, example_app, GTK_TYPE_APPLICATION);

static void
example_app_init (ExampleApp *app)
{
}

static void
example_app_activate (GApplication *app)
{
  ExampleAppWindow *win;

  win = example_app_window_new (EXAMPLE_APP (app));
  gtk_window_present (GTK_WINDOW (win));
}

static void
example_app_open (GApplication  *app,
                  GFile        **files,
                  int            n_files,
                  const char    *hint)
{
  GList *windows;
  ExampleAppWindow *win;
  int i;

  windows = gtk_application_get_windows (GTK_APPLICATION (app));
  if (windows)
    win = EXAMPLE_APP_WINDOW (windows->data);
  else
    win = example_app_window_new (EXAMPLE_APP (app));

  for (i = 0; i < n_files; i++)
    example_app_window_open (win, files[i]);

  gtk_window_present (GTK_WINDOW (win));
}

static void
example_app_class_init (ExampleAppClass *class)
{
  G_APPLICATION_CLASS (class)->activate = example_app_activate;
  G_APPLICATION_CLASS (class)->open = example_app_open;
}

ExampleApp *
example_app_new (void)
{
  return g_object_new (EXAMPLE_APP_TYPE,
                       "application-id", "org.gtk.exampleapp",
                       "flags", G_APPLICATION_HANDLES_OPEN,
                       NULL);
}
```

Another important class that is part of the application support in GTK is `GtkApplicationWindow`. It is typically subclassed as well. Our subclass does not do anything yet, so we will just get an empty window.

```
#include <gtk/gtk.h>

#include "exampleapp.h"
#include "exampleappwin.h"

struct _ExampleAppWindow
{
  GtkApplicationWindow parent;
};

G_DEFINE_TYPE(ExampleAppWindow, example_app_window, GTK_TYPE_APPLICATION_WINDOW);

static void
example_app_window_init (ExampleAppWindow *app)
{
}

static void
example_app_window_class_init (ExampleAppWindowClass *class)
{
}

ExampleAppWindow *
example_app_window_new (ExampleApp *app)
{
  return g_object_new (EXAMPLE_APP_WINDOW_TYPE, "application", app, NULL);
}

void
example_app_window_open (ExampleAppWindow *win,
                         GFile            *file)
{
}
```

As part of the initial setup of our application, we also create an icon and a desktop file.

(An icon)

```
[Desktop Entry]
Type=Application
Name=Example
Icon=exampleapp
StartupNotify=true
Exec=@bindir@/exampleapp
```

Note that `bindir@` needs to be replaced with the actual path to the binary before this desktop file can be used.

Here is what we’ve achieved so far:

(An application)

This does not look very impressive yet, but our application is already presenting itself on the session bus, it has single-instance semantics, and it accepts files as commandline arguments.

### Populating the window

In this step, we use a `GtkBuilder` template to associate a `GtkBuilder` ui file with our application window class.

Our simple ui file gives the window a title, and puts a `GtkStack` widget as the main content.

```
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <template class="ExampleAppWindow" parent="GtkApplicationWindow">
    <property name="title" translatable="yes">Example Application</property>
    <property name="default-width">600</property>
    <property name="default-height">400</property>
    <child>
      <object class="GtkBox" id="content_box">
        <property name="orientation">vertical</property>
        <child>
          <object class="GtkStack" id="stack"/>
        </child>
      </object>
    </child>
  </template>
</interface>
```

To make use of this file in our application, we revisit our `GtkApplicationWindow` subclass, and call `gtk_widget_class_set_template_from_resource()` from the class init function to set the ui file as template for this class. We also add a call to `gtk_widget_init_template()` in the instance init function to instantiate the template for each instance of our class.

```
 ...

static void
example_app_window_init (ExampleAppWindow *win)
{
  gtk_widget_init_template (GTK_WIDGET (win));
}

static void
example_app_window_class_init (ExampleAppWindowClass *class)
{
  gtk_widget_class_set_template_from_resource (GTK_WIDGET_CLASS (class),
                                               "/org/gtk/exampleapp/window.ui");
}

 ...
```

(full source)

You may have noticed that we used the `_from_resource()` variant of the function that sets a template. Now we need to use GLib’s resource functionality to include the ui file in the binary. This is commonly done by listing all resources in a `.gresource.xml` file, such as this:

```
<?xml version="1.0" encoding="UTF-8"?>
<gresources>
  <gresource prefix="/org/gtk/exampleapp">
    <file preprocess="xml-stripblanks">window.ui</file>
  </gresource>
</gresources>
```

This file has to be converted into a C source file that will be compiled and linked into the application together with the other source files. To do so, we use the `glib-compile-resources` utility:

```
glib-compile-resources exampleapp.gresource.xml --target=resources.c --generate-source
```

The gnome module of the Meson build system provides the `gnome.compile_resources()` method for this task.

Our application now looks like this:

(The application)

### Opening files

In this step, we make our application show the content of all the files that it is given on the commandline.

**Note: Providing filenames (e.g. `./exampleapp examplewin.c examplewin.h`) at the command line is a requirement for example apps 3-9 to display as shown in the screenshots below.**

To this end, we add a member to the struct of our application window subclass and keep a reference to the `GtkStack` there. The first member of the struct should be the parent type from which the class is derived. Here, `ExampleAppWindow` is derived from `GtkApplicationWindow`. The `gtk_widget_class_bind_template_child()` function arranges things so that after instantiating the template, the `stack` member of the struct will point to the widget of the same name from the template.

```
...

struct _ExampleAppWindow
{
  GtkApplicationWindow parent;

  GtkWidget *stack;
};

G_DEFINE_TYPE (ExampleAppWindow, example_app_window, GTK_TYPE_APPLICATION_WINDOW)

...

static void
example_app_window_class_init (ExampleAppWindowClass *class)
{
  gtk_widget_class_set_template_from_resource (GTK_WIDGET_CLASS (class),
                                               "/org/gtk/exampleapp/window.ui");
  gtk_widget_class_bind_template_child (GTK_WIDGET_CLASS (class), ExampleAppWindow, stack);
}

...
```

(full source)

Now we revisit the `example_app_window_open()` function that is called for each commandline argument, and construct a GtkTextView that we then add as a page to the stack:

```
...

void
example_app_window_open (ExampleAppWindow *win,
                         GFile            *file)
{
  char *basename;
  GtkWidget *scrolled, *view;
  char *contents;
  gsize length;

  basename = g_file_get_basename (file);

  scrolled = gtk_scrolled_window_new ();
  gtk_widget_set_hexpand (scrolled, TRUE);
  gtk_widget_set_vexpand (scrolled, TRUE);
  view = gtk_text_view_new ();
  gtk_text_view_set_editable (GTK_TEXT_VIEW (view), FALSE);
  gtk_text_view_set_cursor_visible (GTK_TEXT_VIEW (view), FALSE);
  gtk_scrolled_window_set_child (GTK_SCROLLED_WINDOW (scrolled), view);
  gtk_stack_add_titled (GTK_STACK (win->stack), scrolled, basename, basename);

  if (g_file_load_contents (file, NULL, &contents, &length, NULL, NULL))
    {
      GtkTextBuffer *buffer;

      buffer = gtk_text_view_get_buffer (GTK_TEXT_VIEW (view));
      gtk_text_buffer_set_text (buffer, contents, length);
      g_free (contents);
    }

  g_free (basename);
}

...
```

(full source)

Lastly, we add a `GtkStackSwitcher` to the titlebar area in the UI file, and we tell it to display information about our stack.

The stack switcher gets all its information it needs to display tabs from the stack that it belongs to. Here, we are passing the label to show for each file as the last argument to the `gtk_stack_add_titled()` function.

Our application is beginning to take shape:

(Application window)

The menu is shown at the right side of the headerbar. It is meant to collect infrequently used actions that affect the whole application.

Just like the window template, we specify our menu in a ui file, and add it as a resource to our binary.

```
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <menu id="menu">
    <section>
      <item>
        <attribute name="label" translatable="yes">_Preferences</attribute>
        <attribute name="action">app.preferences</attribute>
      </item>
    </section>
    <section>
      <item>
        <attribute name="label" translatable="yes">_Quit</attribute>
        <attribute name="action">app.quit</attribute>
      </item>
    </section>
  </menu>
</interface>
```

To make the menu appear, we have to load the ui file and associate the resulting menu model with the menu button that we’ve added to the headerbar. Since menus work by activating GActions, we also have to add a suitable set of actions to our application.

Adding the actions is best done in the `startup()` vfunc, which is guaranteed to be called once for each primary application instance:

```
...

static void
preferences_activated (GSimpleAction *action,
                       GVariant      *parameter,
                       gpointer       app)
{
}

static void
quit_activated (GSimpleAction *action,
                GVariant      *parameter,
                gpointer       app)
{
  g_application_quit (G_APPLICATION (app));
}

static GActionEntry app_entries[] =
{
  { "preferences", preferences_activated, NULL, NULL, NULL },
  { "quit", quit_activated, NULL, NULL, NULL }
};

static void
example_app_startup (GApplication *app)
{
  GtkBuilder *builder;
  GMenuModel *app_menu;
  const char *quit_accels[2] = { "&lt;Ctrl&gt;Q", NULL };

  G_APPLICATION_CLASS (example_app_parent_class)->startup (app);

  g_action_map_add_action_entries (G_ACTION_MAP (app),
                                   app_entries, G_N_ELEMENTS (app_entries),
                                   app);
  gtk_application_set_accels_for_action (GTK_APPLICATION (app),
                                         "app.quit",
                                         quit_accels);
}

static void
example_app_class_init (ExampleAppClass *class)
{
  G_APPLICATION_CLASS (class)->startup = example_app_startup;
  ...
}

...
```

(full source)

Our preferences menu item does not do anything yet, but the Quit menu item is fully functional. Note that it can also be activated by the usual Ctrl-Q shortcut. The shortcut was added with `gtk_application_set_accels_for_action()`.

The application menu looks like this:

(Application window)

### A preference dialog

A typical application will have a some preferences that should be remembered from one run to the next. Even for our simple example application, we may want to change the font that is used for the content.

We are going to use `GSettings` to store our preferences. `GSettings` requires a schema that describes our settings:

```
<?xml version="1.0" encoding="UTF-8"?>
<schemalist>
  <schema path="/org/gtk/exampleapp/" id="org.gtk.exampleapp">
    <key name="font" type="s">
      <default>'Monospace 12'</default>
      <summary>Font</summary>
      <description>The font to be used for content.</description>
    </key>
    <key name="transition" type="s">
      <choices>
        <choice value='none'/>
        <choice value='crossfade'/>
        <choice value='slide-left-right'/>
      </choices>
      <default>'none'</default>
      <summary>Transition</summary>
      <description>The transition to use when switching tabs.</description>
    </key>
  </schema>
</schemalist>
```

Before we can make use of this schema in our application, we need to compile it into the binary form that GSettings expects. GIO provides macros to do this in Autotools-based projects, and the gnome module of the Meson build system provides the `gnome.compile_schemas()` method for this task.

Next, we need to connect our settings to the widgets that they are supposed to control. One convenient way to do this is to use `GSettings` bind functionality to bind settings keys to object properties, as we do here for the transition setting.

```
...

static void
example_app_window_init (ExampleAppWindow *win)
{
  gtk_widget_init_template (GTK_WIDGET (win));
  win->settings = g_settings_new ("org.gtk.exampleapp");

  g_settings_bind (win->settings, "transition",
                   win->stack, "transition-type",
                   G_SETTINGS_BIND_DEFAULT);
}

...
```

(full source)

The code to connect the font setting is a little more involved, since there is no simple object property that it corresponds to, so we are not going to go into that here.

At this point, the application will already react if you change one of the settings, e.g. using the `gsettings` command line tool. Of course, we expect the application to provide a preference dialog for these. So lets do that now. Our preference dialog will be a subclass of `GtkDialog`, and we’ll use the same techniques that we’ve already seen: templates, private structs, settings bindings.

Lets start with the template.

```
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <template class="ExampleAppPrefs" parent="GtkDialog">
    <property name="title" translatable="yes">Preferences</property>
    <property name="resizable">0</property>
    <property name="modal">1</property>
    <child internal-child="content_area">
      <object class="GtkBox" id="content_area">
        <child>
          <object class="GtkGrid" id="grid">
            <property name="margin-start">12</property>
            <property name="margin-end">12</property>
            <property name="margin-top">12</property>
            <property name="margin-bottom">12</property>
            <property name="row-spacing">12</property>
            <property name="column-spacing">12</property>
            <child>
              <object class="GtkLabel" id="fontlabel">
                <property name="label">_Font:</property>
                <property name="use-underline">1</property>
                <property name="mnemonic-widget">font</property>
                <property name="xalign">1</property>
                <layout>
                  <property name="column">0</property>
                  <property name="row">0</property>
                </layout>
              </object>
            </child>
            <child>
              <object class="GtkFontButton" id="font">
                <layout>
                  <property name="column">1</property>
                  <property name="row">0</property>
                </layout>
              </object>
            </child>
            <child>
              <object class="GtkLabel" id="transitionlabel">
                <property name="label">_Transition:</property>
                <property name="use-underline">1</property>
                <property name="mnemonic-widget">transition</property>
                <property name="xalign">1</property>
                <layout>
                  <property name="column">0</property>
                  <property name="row">1</property>
                </layout>
              </object>
            </child>
            <child>
              <object class="GtkComboBoxText" id="transition">
                <items>
                  <item translatable="yes" id="none">None</item>
                  <item translatable="yes" id="crossfade">Fade</item>
                  <item translatable="yes" id="slide-left-right">Slide</item>
                </items>
                <layout>
                  <property name="column">1</property>
                  <property name="row">1</property>
                </layout>
              </object>
            </child>
          </object>
        </child>
      </object>
    </child>
  </template>
</interface>
```

Next comes the dialog subclass.

```
#include <gtk/gtk.h>

#include "exampleapp.h"
#include "exampleappwin.h"
#include "exampleappprefs.h"

struct _ExampleAppPrefs
{
  GtkDialog parent;

  GSettings *settings;
  GtkWidget *font;
  GtkWidget *transition;
};

G_DEFINE_TYPE (ExampleAppPrefs, example_app_prefs, GTK_TYPE_DIALOG)

static void
example_app_prefs_init (ExampleAppPrefs *prefs)
{
  gtk_widget_init_template (GTK_WIDGET (prefs));
  prefs->settings = g_settings_new ("org.gtk.exampleapp");

  g_settings_bind (prefs->settings, "font",
                   prefs->font, "font",
                   G_SETTINGS_BIND_DEFAULT);
  g_settings_bind (prefs->settings, "transition",
                   prefs->transition, "active-id",
                   G_SETTINGS_BIND_DEFAULT);
}

static void
example_app_prefs_dispose (GObject *object)
{
  ExampleAppPrefs *prefs;

  prefs = EXAMPLE_APP_PREFS (object);

  g_clear_object (&prefs->settings);

  G_OBJECT_CLASS (example_app_prefs_parent_class)->dispose (object);
}

static void
example_app_prefs_class_init (ExampleAppPrefsClass *class)
{
  G_OBJECT_CLASS (class)->dispose = example_app_prefs_dispose;

  gtk_widget_class_set_template_from_resource (GTK_WIDGET_CLASS (class),
                                               "/org/gtk/exampleapp/prefs.ui");
  gtk_widget_class_bind_template_child (GTK_WIDGET_CLASS (class), ExampleAppPrefs, font);
  gtk_widget_class_bind_template_child (GTK_WIDGET_CLASS (class), ExampleAppPrefs, transition);
}

ExampleAppPrefs *
example_app_prefs_new (ExampleAppWindow *win)
{
  return g_object_new (EXAMPLE_APP_PREFS_TYPE, "transient-for", win, "use-header-bar", TRUE, NULL);
}
```

Now we revisit the `preferences_activated()` function in our application class, and make it open a new preference dialog.

```
...

static void
preferences_activated (GSimpleAction *action,
                       GVariant      *parameter,
                       gpointer       app)
{
  ExampleAppPrefs *prefs;
  GtkWindow *win;

  win = gtk_application_get_active_window (GTK_APPLICATION (app));
  prefs = example_app_prefs_new (EXAMPLE_APP_WINDOW (win));
  gtk_window_present (GTK_WINDOW (prefs));
}

...
```

(full source)

After all this work, our application can now show a preference dialog like this:

(Preference dialog)

We continue to flesh out the functionality of our application. For now, we add search. GTK supports this with `GtkSearchEntry` and `GtkSearchBar`. The search bar is a widget that can slide in from the top to present a search entry.

We add a toggle button to the header bar, which can be used to slide out the search bar below the header bar.

```
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <template class="ExampleAppWindow" parent="GtkApplicationWindow">
    <property name="title" translatable="yes">Example Application</property>
    <property name="default-width">600</property>
    <property name="default-height">400</property>
    <child type="titlebar">
      <object class="GtkHeaderBar" id="header">
        <child type="title">
          <object class="GtkStackSwitcher" id="tabs">
            <property name="stack">stack</property>
          </object>
        </child>
        <child type="end">
          <object class="GtkMenuButton" id="gears">
            <property name="direction">none</property>
          </object>
        </child>
        <child type="end">
          <object class="GtkToggleButton" id="search">
            <property name="sensitive">0</property>
            <property name="icon-name">edit-find-symbolic</property>
          </object>
        </child>
      </object>
    </child>
    <child>
      <object class="GtkBox" id="content_box">
        <property name="orientation">vertical</property>
        <child>
          <object class="GtkSearchBar" id="searchbar">
            <child>
              <object class="GtkSearchEntry" id="searchentry">
                <signal name="search-changed" handler="search_text_changed"/>
              </object>
            </child>
          </object>
        </child>
        <child>
          <object class="GtkStack" id="stack">
            <signal name="notify::visible-child" handler="visible_child_changed"/>
          </object>
        </child>
      </object>
    </child>
  </template>
</interface>
```

Implementing the search needs quite a few code changes that we are not going to completely go over here. The central piece of the search implementation is a signal handler that listens for text changes in the search entry.

```
...

static void
search_text_changed (GtkEntry         *entry,
                     ExampleAppWindow *win)
{
  const char *text;
  GtkWidget *tab;
  GtkWidget *view;
  GtkTextBuffer *buffer;
  GtkTextIter start, match_start, match_end;

  text = gtk_editable_get_text (GTK_EDITABLE (entry));

  if (text[0] == '\0')
    return;

  tab = gtk_stack_get_visible_child (GTK_STACK (win->stack));
  view = gtk_scrolled_window_get_child (GTK_SCROLLED_WINDOW (tab));
  buffer = gtk_text_view_get_buffer (GTK_TEXT_VIEW (view));

  /* Very simple-minded search implementation */
  gtk_text_buffer_get_start_iter (buffer, &start);
  if (gtk_text_iter_forward_search (&start, text, GTK_TEXT_SEARCH_CASE_INSENSITIVE,
                                    &match_start, &match_end, NULL))
    {
      gtk_text_buffer_select_range (buffer, &match_start, &match_end);
      gtk_text_view_scroll_to_iter (GTK_TEXT_VIEW (view), &match_start,
                                    0.0, FALSE, 0.0, 0.0);
    }
}

static void
example_app_window_init (ExampleAppWindow *win)
{

...

  gtk_widget_class_bind_template_callback (GTK_WIDGET_CLASS (class), search_text_changed);

...

}

...
```

(full source)

With the search bar, our application now looks like this:

(A search bar)

### Adding a side bar

As another piece of functionality, we are adding a sidebar, which demonstrates `GtkMenuButton`, `GtkRevealer` and `GtkListBox`.

```
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <template class="ExampleAppWindow" parent="GtkApplicationWindow">
    <property name="title" translatable="yes">Example Application</property>
    <property name="default-width">600</property>
    <property name="default-height">400</property>
    <child type="titlebar">
      <object class="GtkHeaderBar" id="header">
        <child type="title">
          <object class="GtkStackSwitcher" id="tabs">
            <property name="stack">stack</property>
          </object>
        </child>
        <child type="end">
          <object class="GtkToggleButton" id="search">
            <property name="sensitive">0</property>
            <property name="icon-name">edit-find-symbolic</property>
          </object>
        </child>
        <child type="end">
          <object class="GtkMenuButton" id="gears">
            <property name="direction">none</property>
          </object>
        </child>
      </object>
    </child>
    <child>
      <object class="GtkBox" id="content_box">
        <property name="orientation">vertical</property>
        <child>
          <object class="GtkSearchBar" id="searchbar">
            <child>
              <object class="GtkSearchEntry" id="searchentry">
                <signal name="search-changed" handler="search_text_changed"/>
              </object>
            </child>
          </object>
        </child>
        <child>
          <object class="GtkBox" id="hbox">
            <child>
              <object class="GtkRevealer" id="sidebar">
                <property name="transition-type">slide-right</property>
                <child>
                  <object class="GtkScrolledWindow" id="sidebar-sw">
                    <property name="hscrollbar-policy">never</property>
                    <child>
                      <object class="GtkListBox" id="words">
                        <property name="selection-mode">none</property>
                      </object>
                    </child>
                  </object>
                </child>
              </object>
            </child>
            <child>
              <object class="GtkStack" id="stack">
                <signal name="notify::visible-child" handler="visible_child_changed"/>
              </object>
            </child>
          </object>
        </child>
      </object>
    </child>
  </template>
</interface>
```

The code to populate the sidebar with buttons for the words found in each file is a little too involved to go into here. But we’ll look at the code to add a checkbutton for the new feature to the menu.

```
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <menu id="menu">
    <section>
      <item>
        <attribute name="label" translatable="yes">_Words</attribute>
        <attribute name="action">win.show-words</attribute>
      </item>
      <item>
        <attribute name="label" translatable="yes">_Preferences</attribute>
        <attribute name="action">app.preferences</attribute>
      </item>
    </section>
    <section>
      <item>
        <attribute name="label" translatable="yes">_Quit</attribute>
        <attribute name="action">app.quit</attribute>
      </item>
    </section>
  </menu>
</interface>
```

To connect the menuitem to the show-words setting, we use a `GAction` corresponding to the given `GSettings` key.

```
...

static void
example_app_window_init (ExampleAppWindow *win)
{

...

  builder = gtk_builder_new_from_resource ("/org/gtk/exampleapp/gears-menu.ui");
  menu = G_MENU_MODEL (gtk_builder_get_object (builder, "menu"));
  gtk_menu_button_set_menu_model (GTK_MENU_BUTTON (priv->gears), menu);
  g_object_unref (builder);

  action = g_settings_create_action (priv->settings, "show-words");
  g_action_map_add_action (G_ACTION_MAP (win), action);
  g_object_unref (action);
}

...
```

(full source)

What our application looks like now:

(A sidebar)

### Properties

Widgets and other objects have many useful properties.

Here we show some ways to use them in new and flexible ways, by wrapping them in actions with `GPropertyAction` or by binding them with `GBinding`.

To set this up, we add two labels to the header bar in our window template, named `lines_label` and `lines`, and bind them to struct members in the private struct, as we’ve seen a couple of times by now.

We add a new “Lines” menu item to the gears menu, which triggers the show-lines action:

```
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <menu id="menu">
    <section>
      <item>
        <attribute name="label" translatable="yes">_Words</attribute>
        <attribute name="action">win.show-words</attribute>
      </item>
      <item>
        <attribute name="label" translatable="yes">_Lines</attribute>
        <attribute name="action">win.show-lines</attribute>
      </item>
      <item>
        <attribute name="label" translatable="yes">_Preferences</attribute>
        <attribute name="action">app.preferences</attribute>
      </item>
    </section>
    <section>
      <item>
        <attribute name="label" translatable="yes">_Quit</attribute>
        <attribute name="action">app.quit</attribute>
      </item>
    </section>
  </menu>
</interface>
```

To make this menu item do something, we create a property action for the visible property of the `lines` label, and add it to the actions of the window. The effect of this is that the visibility of the label gets toggled every time the action is activated.

Since we want both labels to appear and disappear together, we bind the visible property of the `lines_label` widget to the same property of the `lines` widget.

```
...

static void
example_app_window_init (ExampleAppWindow *win)
{
  ...

  action = (GAction*) g_property_action_new ("show-lines", win->lines, "visible");
  g_action_map_add_action (G_ACTION_MAP (win), action);
  g_object_unref (action);

  g_object_bind_property (win->lines, "visible",
                          win->lines_label, "visible",
                          G_BINDING_DEFAULT);
}

...
```

(full source)

We also need a function that counts the lines of the currently active tab, and updates the `lines` label. See the full source if you are interested in the details.

This brings our example application to this appearance:

(Full application)
