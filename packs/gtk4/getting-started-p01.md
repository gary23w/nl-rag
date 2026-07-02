---
title: "Gtk – 4.0: Getting Started with GTK (part 1/2)"
source: https://docs.gtk.org/gtk4/getting_started.html
domain: gtk4
license: CC-BY-SA-4.0
tags: gtk4 toolkit, gtk widgets, gnome application, libadwaita styling
fetched: 2026-07-02
part: 1/2
---

#### Getting Started with GTK [src]

GTK is a widget toolkit. Each user interface created by GTK consists of widgets. This is implemented in C using `GObject`, an object-oriented framework for C. Widgets are organized in a hierarchy. The window widget is the main container. The user interface is then built by adding buttons, drop-down menus, input fields, and other widgets to the window. If you are creating complex user interfaces it is recommended to use GtkBuilder and its GTK-specific markup description language, instead of assembling the interface manually.

GTK is event-driven. The toolkit listens for events such as a click on a button, and passes the event to your application.

This chapter contains some tutorial information to get you started with GTK programming. It assumes that you have GTK, its dependencies and a C compiler installed and ready to use. If you need to build GTK itself first, refer to the Compiling the GTK libraries section in this reference.


## Basics

To begin our introduction to GTK, we’ll start with a very simple application. This program will create an empty 200 × 200 pixel window.

(A window)

Create a new file with the following content named `example-0.c`.

```
#include <gtk/gtk.h>

static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  GtkWidget *window;

  window = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (window), "Window");
  gtk_window_set_default_size (GTK_WINDOW (window), 200, 200);
  gtk_window_present (GTK_WINDOW (window));
}

int
main (int    argc,
      char **argv)
{
  GtkApplication *app;
  int status;

  app = gtk_application_new ("org.gtk.example", G_APPLICATION_DEFAULT_FLAGS);
  g_signal_connect (app, "activate", G_CALLBACK (activate), NULL);
  status = g_application_run (G_APPLICATION (app), argc, argv);
  g_object_unref (app);

  return status;
}
```

You can compile the program above with GCC using:

```
gcc $( pkg-config --cflags gtk4 ) -o example-0 example-0.c $( pkg-config --libs gtk4 )
```

For more information on how to compile a GTK application, please refer to the Compiling GTK Applications section in this reference.

All GTK applications will, of course, include `gtk/gtk.h`, which declares functions, types and macros required by GTK applications.

Even if GTK installs multiple header files, only the top-level `gtk/gtk.h` header can be directly included by third-party code. The compiler will abort with an error if any other GTK header is directly included.

In a GTK application, the purpose of the `main()` function is to create a `GtkApplication` object and run it. In this example a `GtkApplication` pointer named `app` is declared and then initialized using `gtk_application_new()`.

When creating a `GtkApplication`, you need to pick an application identifier (a name) and pass it to `gtk_application_new()` as parameter. For this example `org.gtk.example` is used. For choosing an identifier for your application, see this guide. Lastly, `gtk_application_new()` takes `GApplicationFlags` as input for your application, if your application would have special needs.

Next the activate signal is connected to the `activate()` function above the `main()` function. The `activate` signal will be emitted when your application is launched with `g_application_run()` on the line below. The `g_application_run()` call also takes as arguments the command line arguments (the `argc` count and the `argv` string array). Your application can override the command line handling, e.g. to open files passed on the commandline.

Within `g_application_run()` the activate signal is sent and we then proceed into the `activate()` function of the application. This is where we construct our GTK window, so that a window is shown when the application is launched. The call to `gtk_application_window_new()` will create a new `GtkApplicationWindow` and store a pointer to it in the `window` variable. The window will have a frame, a title bar, and window controls depending on the platform.

A window title is set using `gtk_window_set_title()`. This function takes a `GtkWindow` pointer and a string as input. As our `window` pointer is a `GtkWidget` pointer, we need to cast it to `GtkWindow`; instead of casting `window` via a typical C cast like `(GtkWindow*)`, `window` can be cast using the macro `GTK_WINDOW()`. `GTK_WINDOW()` will check if the pointer is an instance of the `GtkWindow` class, before casting, and emit a warning if the check fails. More information about this convention can be found in the GObject documentation.

Finally the window size is set using `gtk_window_set_default_size()` and the window is then shown by GTK via `gtk_window_present()`.

When you close the window, by (for example) pressing the X button, the `g_application_run()` call returns with a number which is saved inside an integer variable named `status`. Afterwards, the `GtkApplication` object is freed from memory with `g_object_unref()`. Finally the status integer is returned and the application exits.

While the program is running, GTK is receiving *events*. These are typically input events caused by the user interacting with your program, but also things like messages from the window manager or other applications. GTK processes these and as a result, *signals* may be emitted on your widgets. Connecting handlers for these signals is how you normally make your program do something in response to user input.

The following example is slightly more complex, and tries to showcase some of the capabilities of GTK.


## Hello, World

In the long tradition of programming languages and libraries, this example is called *Hello, World*.

(Hello, world)

### Hello World in C

Create a new file with the following content named `example-1.c`.

```
#include <gtk/gtk.h>

static void
print_hello (GtkWidget *widget,
             gpointer   data)
{
  g_print ("Hello World\n");
}

static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  GtkWidget *window;
  GtkWidget *button;
  GtkWidget *box;

  window = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (window), "Window");
  gtk_window_set_default_size (GTK_WINDOW (window), 200, 200);

  box = gtk_box_new (GTK_ORIENTATION_VERTICAL, 0);
  gtk_widget_set_halign (box, GTK_ALIGN_CENTER);
  gtk_widget_set_valign (box, GTK_ALIGN_CENTER);

  gtk_window_set_child (GTK_WINDOW (window), box);

  button = gtk_button_new_with_label ("Hello World");

  g_signal_connect (button, "clicked", G_CALLBACK (print_hello), NULL);
  g_signal_connect_swapped (button, "clicked", G_CALLBACK (gtk_window_destroy), window);

  gtk_box_append (GTK_BOX (box), button);

  gtk_window_present (GTK_WINDOW (window));
}

int
main (int    argc,
      char **argv)
{
  GtkApplication *app;
  int status;

  app = gtk_application_new ("org.gtk.example", G_APPLICATION_DEFAULT_FLAGS);
  g_signal_connect (app, "activate", G_CALLBACK (activate), NULL);
  status = g_application_run (G_APPLICATION (app), argc, argv);
  g_object_unref (app);

  return status;
}
```

You can compile the program above with GCC using:

```
gcc $( pkg-config --cflags gtk4 ) -o example-1 example-1.c $( pkg-config --libs gtk4 )
```

As seen above, `example-1.c` builds further upon `example-0.c` by adding a button to our window, with the label “Hello World”. Two new `GtkWidget` pointers are declared to accomplish this, `button` and `box`. The box variable is created to store a `GtkBox`, which is one of GTK’s ways of controlling the size and layout of widgets.

The `GtkBox` widget is created with `gtk_box_new()`, which takes a `GtkOrientation` enumeration value as parameter. The buttons which this box will contain can either be laid out horizontally or vertically. This does not matter in this particular case, as we are dealing with only one button. After initializing box with the newly created `GtkBox`, the code adds the box widget to the window widget using `gtk_window_set_child()`.

Next the `button` variable is initialized in similar manner. `gtk_button_new_with_label()` is called which returns a `GtkButton` to be stored in `button`. Afterwards `button` is added to our `box`.

Using `g_signal_connect()`, the button is connected to a function in our app called `print_hello()`, so that when the button is clicked, GTK will call this function. As the `print_hello()` function does not use any data as input, `NULL` is passed to it. `print_hello()` calls `g_print()` with the string “Hello World” which will print Hello World in a terminal if the GTK application was started from one.

After connecting `print_hello()`, another signal is connected to the “clicked” state of the button using `g_signal_connect_swapped()`. This functions is similar to a `g_signal_connect()`, with the difference lying in how the callback function is treated; `g_signal_connect_swapped()` allows you to specify what the callback function should take as parameter by letting you pass it as data. In this case the function being called back is `gtk_window_destroy()` and the `window` pointer is passed to it. This has the effect that when the button is clicked, the whole GTK window is destroyed. In contrast if a normal `g_signal_connect()` were used to connect the “clicked” signal with `gtk_window_destroy()`, then the function would be called on `button` (which would not go well, since the function expects a `GtkWindow` as argument).

The rest of the code in `example-1.c` is identical to `example-0.c`. The next section will elaborate further on how to add several `GtkWidget`s to your GTK application.


## Packing

When creating an application, you’ll want to put more than one widget inside a window. When you do so, it becomes important to control how each widget is positioned and sized. This is where packing comes in.

GTK comes with a large variety of *layout containers* whose purpose it is to control the layout of the child widgets that are added to them, like:

- `GtkBox`
- `GtkGrid`
- `GtkRevealer`
- `GtkStack`
- `GtkOverlay`
- `GtkPaned`
- `GtkExpander`
- `GtkFixed`

The following example shows how the `GtkGrid` container lets you arrange several buttons:

(Grid packing)

### Packing buttons

Create a new file with the following content named `example-2.c`.

```
#include <gtk/gtk.h>

static void
print_hello (GtkWidget *widget,
             gpointer   data)
{
  g_print ("Hello World\n");
}

static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  GtkWidget *window;
  GtkWidget *grid;
  GtkWidget *button;

  /* create a new window, and set its title */
  window = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (window), "Window");

  /* Here we construct the container that is going pack our buttons */
  grid = gtk_grid_new ();

  /* Pack the container in the window */
  gtk_window_set_child (GTK_WINDOW (window), grid);

  button = gtk_button_new_with_label ("Button 1");
  g_signal_connect (button, "clicked", G_CALLBACK (print_hello), NULL);

  /* Place the first button in the grid cell (0, 0), and make it fill
   * just 1 cell horizontally and vertically (ie no spanning)
   */
  gtk_grid_attach (GTK_GRID (grid), button, 0, 0, 1, 1);

  button = gtk_button_new_with_label ("Button 2");
  g_signal_connect (button, "clicked", G_CALLBACK (print_hello), NULL);

  /* Place the second button in the grid cell (1, 0), and make it fill
   * just 1 cell horizontally and vertically (ie no spanning)
   */
  gtk_grid_attach (GTK_GRID (grid), button, 1, 0, 1, 1);

  button = gtk_button_new_with_label ("Quit");
  g_signal_connect_swapped (button, "clicked", G_CALLBACK (gtk_window_destroy), window);

  /* Place the Quit button in the grid cell (0, 1), and make it
   * span 2 columns.
   */
  gtk_grid_attach (GTK_GRID (grid), button, 0, 1, 2, 1);

  gtk_window_present (GTK_WINDOW (window));
}

int
main (int    argc,
      char **argv)
{
  GtkApplication *app;
  int status;

  app = gtk_application_new ("org.gtk.example", G_APPLICATION_DEFAULT_FLAGS);
  g_signal_connect (app, "activate", G_CALLBACK (activate), NULL);
  status = g_application_run (G_APPLICATION (app), argc, argv);
  g_object_unref (app);

  return status;
}
```

You can compile the program above with GCC using:

```
gcc $( pkg-config --cflags gtk4 ) -o example-2 example-2.c $( pkg-config --libs gtk4 )
```


## Custom Drawing

Many widgets, like buttons, do all their drawing themselves. You just tell them the label you want to see, and they figure out what font to use, draw the button outline and focus rectangle, etc. Sometimes, it is necessary to do some custom drawing. In that case, a `GtkDrawingArea` might be the right widget to use. It offers a canvas on which you can draw by setting its draw function.

The contents of a widget often need to be partially or fully redrawn, e.g. when another window is moved and uncovers part of the widget, or when the window containing it is resized. It is also possible to explicitly cause a widget to be redrawn, by calling `gtk_widget_queue_draw()`. GTK takes care of most of the details by providing a ready-to-use cairo context to the draw function.

The following example shows how to use a draw function with `GtkDrawingArea`. It is a bit more complicated than the previous examples, since it also demonstrates input event handling with event controllers.

(Drawing)

### Drawing in response to input

Create a new file with the following content named `example-3.c`.

```
#include <gtk/gtk.h>

/* Surface to store current scribbles */
static cairo_surface_t *surface = NULL;

static void
clear_surface (void)
{
  cairo_t *cr;

  cr = cairo_create (surface);

  cairo_set_source_rgb (cr, 1, 1, 1);
  cairo_paint (cr);

  cairo_destroy (cr);
}

/* Create a new surface of the appropriate size to store our scribbles */
static void
resize_cb (GtkWidget *widget,
           int        width,
           int        height,
           gpointer   data)
{
  if (surface)
    {
      cairo_surface_destroy (surface);
      surface = NULL;
    }

  if (gtk_native_get_surface (gtk_widget_get_native (widget)))
    {
      surface = cairo_image_surface_create (CAIRO_FORMAT_ARGB32,
                                            gtk_widget_get_width (widget),
                                            gtk_widget_get_height (widget));

      /* Initialize the surface to white */
      clear_surface ();
    }
}

/* Redraw the screen from the surface. Note that the draw
 * callback receives a ready-to-be-used cairo_t that is already
 * clipped to only draw the exposed areas of the widget
 */
static void
draw_cb (GtkDrawingArea *drawing_area,
         cairo_t        *cr,
         int             width,
         int             height,
         gpointer        data)
{
  cairo_set_source_surface (cr, surface, 0, 0);
  cairo_paint (cr);
}

/* Draw a rectangle on the surface at the given position */
static void
draw_brush (GtkWidget *widget,
            double     x,
            double     y)
{
  cairo_t *cr;

  /* Paint to the surface, where we store our state */
  cr = cairo_create (surface);

  cairo_rectangle (cr, x - 3, y - 3, 6, 6);
  cairo_fill (cr);

  cairo_destroy (cr);

  /* Now invalidate the drawing area. */
  gtk_widget_queue_draw (widget);
}

static double start_x;
static double start_y;

static void
drag_begin (GtkGestureDrag *gesture,
            double          x,
            double          y,
            GtkWidget      *area)
{
  start_x = x;
  start_y = y;

  draw_brush (area, x, y);
}

static void
drag_update (GtkGestureDrag *gesture,
             double          x,
             double          y,
             GtkWidget      *area)
{
  draw_brush (area, start_x + x, start_y + y);
}

static void
drag_end (GtkGestureDrag *gesture,
          double          x,
          double          y,
          GtkWidget      *area)
{
  draw_brush (area, start_x + x, start_y + y);
}

static void
pressed (GtkGestureClick *gesture,
         int              n_press,
         double           x,
         double           y,
         GtkWidget       *area)
{
  clear_surface ();
  gtk_widget_queue_draw (area);
}

static void
close_window (void)
{
  if (surface)
    cairo_surface_destroy (surface);
}

static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  GtkWidget *window;
  GtkWidget *frame;
  GtkWidget *drawing_area;
  GtkGesture *drag;
  GtkGesture *press;

  window = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (window), "Drawing Area");

  g_signal_connect (window, "destroy", G_CALLBACK (close_window), NULL);

  frame = gtk_frame_new (NULL);
  gtk_window_set_child (GTK_WINDOW (window), frame);

  drawing_area = gtk_drawing_area_new ();
  /* set a minimum size */
  gtk_widget_set_size_request (drawing_area, 100, 100);

  gtk_frame_set_child (GTK_FRAME (frame), drawing_area);

  gtk_drawing_area_set_draw_func (GTK_DRAWING_AREA (drawing_area), draw_cb, NULL, NULL);

  g_signal_connect_after (drawing_area, "resize", G_CALLBACK (resize_cb), NULL);

  drag = gtk_gesture_drag_new ();
  gtk_gesture_single_set_button (GTK_GESTURE_SINGLE (drag), GDK_BUTTON_PRIMARY);
  gtk_widget_add_controller (drawing_area, GTK_EVENT_CONTROLLER (drag));
  g_signal_connect (drag, "drag-begin", G_CALLBACK (drag_begin), drawing_area);
  g_signal_connect (drag, "drag-update", G_CALLBACK (drag_update), drawing_area);
  g_signal_connect (drag, "drag-end", G_CALLBACK (drag_end), drawing_area);

  press = gtk_gesture_click_new ();
  gtk_gesture_single_set_button (GTK_GESTURE_SINGLE (press), GDK_BUTTON_SECONDARY);
  gtk_widget_add_controller (drawing_area, GTK_EVENT_CONTROLLER (press));

  g_signal_connect (press, "pressed", G_CALLBACK (pressed), drawing_area);

  gtk_window_present (GTK_WINDOW (window));
}

int
main (int    argc,
      char **argv)
{
  GtkApplication *app;
  int status;

  app = gtk_application_new ("org.gtk.example", G_APPLICATION_DEFAULT_FLAGS);
  g_signal_connect (app, "activate", G_CALLBACK (activate), NULL);
  status = g_application_run (G_APPLICATION (app), argc, argv);
  g_object_unref (app);

  return status;
}
```

You can compile the program above with GCC using:

```
gcc $( pkg-config --cflags gtk4 ) -o example-3 example-3.c $( pkg-config --libs gtk4 )
```


## Building user interfaces

When constructing a more complicated user interface, with dozens or hundreds of widgets, doing all the setup work in C code is cumbersome, and making changes becomes next to impossible.

Thankfully, GTK supports the separation of user interface layout from your business logic, by using UI descriptions in an XML format that can be parsed by the `GtkBuilder` class.

### Packing buttons with GtkBuilder

Create a new file with the following content named `example-4.c`.

```
#include <gtk/gtk.h>
#include <glib/gstdio.h>

static void
print_hello (GtkWidget *widget,
             gpointer   data)
{
  g_print ("Hello World\n");
}

static void
quit_cb (GtkWindow *window)
{
  gtk_window_close (window);
}

static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  /* Construct a GtkBuilder instance and load our UI description */
  GtkBuilder *builder = gtk_builder_new ();
  gtk_builder_add_from_file (builder, "builder.ui", NULL);

  /* Connect signal handlers to the constructed widgets. */
  GObject *window = gtk_builder_get_object (builder, "window");
  gtk_window_set_application (GTK_WINDOW (window), app);

  GObject *button = gtk_builder_get_object (builder, "button1");
  g_signal_connect (button, "clicked", G_CALLBACK (print_hello), NULL);

  button = gtk_builder_get_object (builder, "button2");
  g_signal_connect (button, "clicked", G_CALLBACK (print_hello), NULL);

  button = gtk_builder_get_object (builder, "quit");
  g_signal_connect_swapped (button, "clicked", G_CALLBACK (quit_cb), window);

  gtk_widget_set_visible (GTK_WIDGET (window), TRUE);

  /* We do not need the builder any more */
  g_object_unref (builder);
}

int
main (int   argc,
      char *argv[])
{
#ifdef GTK_SRCDIR
  g_chdir (GTK_SRCDIR);
#endif

  GtkApplication *app = gtk_application_new ("org.gtk.example", G_APPLICATION_DEFAULT_FLAGS);
  g_signal_connect (app, "activate", G_CALLBACK (activate), NULL);

  int status = g_application_run (G_APPLICATION (app), argc, argv);
  g_object_unref (app);

  return status;
}
```

Create a new file with the following content named `builder.ui`.

```
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <object id="window" class="GtkWindow">
    <property name="title">Grid</property>
    <child>
      <object id="grid" class="GtkGrid">
        <child>
          <object id="button1" class="GtkButton">
            <property name="label">Button 1</property>
            <layout>
              <property name="column">0</property>
              <property name="row">0</property>
            </layout>
          </object>
        </child>
        <child>
          <object id="button2" class="GtkButton">
            <property name="label">Button 2</property>
            <layout>
              <property name="column">1</property>
              <property name="row">0</property>
            </layout>
          </object>
        </child>
        <child>
          <object id="quit" class="GtkButton">
            <property name="label">Quit</property>
            <layout>
              <property name="column">0</property>
              <property name="row">1</property>
              <property name="column-span">2</property>
            </layout>
          </object>
        </child>
      </object>
    </child>
  </object>
</interface>
```

You can compile the program above with GCC using:

```
gcc $( pkg-config --cflags gtk4 ) -o example-4 example-4.c $( pkg-config --libs gtk4 )
```

Note that `GtkBuilder` can also be used to construct objects that are not widgets, such as tree models, adjustments, etc. That is the reason the method we use here is called `gtk_builder_get_object()` and returns a `GObject` instead of a `GtkWidget`.

Normally, you would pass a full path to `gtk_builder_add_from_file()` to make the execution of your program independent of the current directory. A common location to install UI descriptions and similar data is `/usr/share/appname`.

It is also possible to embed the UI description in the source code as a string and use `gtk_builder_add_from_string()` to load it. But keeping the UI description in a separate file has several advantages:

- it is possible to make minor adjustments to the UI without recompiling your program
- it is easier to isolate the UI code from the business logic of your application
- it is easier to restructure your UI into separate classes using composite widget templates

Using GResource it is possible to combine the best of both worlds: you can keep the UI definition files separate inside your source code repository, and then ship them embedded into your application.
