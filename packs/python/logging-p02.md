---
title: "logging (part 2/2)"
source: https://docs.python.org/3/library/logging.html
domain: python
license: PSF-2.0
tags: python, pytest, cpython, pip
fetched: 2026-07-02
part: 2/2
---

## Module-Level Functions

In addition to the classes described above, there are a number of module-level functions.

**logging.getLogger(*name=None*)**

Return a logger with the specified name or, if name is `None`, return the root logger of the hierarchy. If specified, the name is typically a dot-separated hierarchical name like *‘a’*, *‘a.b’* or *‘a.b.c.d’*. Choice of these names is entirely up to the developer who is using logging, though it is recommended that `__name__` be used unless you have a specific reason for not doing that, as mentioned in Logger Objects.

All calls to this function with a given name return the same logger instance. This means that logger instances never need to be passed between different parts of an application.

**logging.getLoggerClass()**

Return either the standard `Logger` class, or the last class passed to `setLoggerClass()`. This function may be called from within a new class definition, to ensure that installing a customized `Logger` class will not undo customizations already applied by other code. For example:

```python3
class MyLogger(logging.getLoggerClass()):
    # ... override behaviour here
```

**logging.getLogRecordFactory()**

Return a callable which is used to create a `LogRecord`.

Added in version 3.2: This function has been provided, along with `setLogRecordFactory()`, to allow developers more control over how the `LogRecord` representing a logging event is constructed.

See `setLogRecordFactory()` for more information about the how the factory is called.

**logging.debug(*msg*, **args*, ***kwargs*)**

This is a convenience function that calls `Logger.debug()`, on the root logger. The handling of the arguments is in every way identical to what is described in that method.

The only difference is that if the root logger has no handlers, then `basicConfig()` is called, prior to calling `debug` on the root logger.

For very short scripts or quick demonstrations of `logging` facilities, `debug` and the other module-level functions may be convenient. However, most programs will want to carefully and explicitly control the logging configuration, and should therefore prefer creating a module-level logger and calling `Logger.debug()` (or other level-specific methods) on it, as described at the beginning of this documentation.

**logging.info(*msg*, **args*, ***kwargs*)**

Logs a message with level `INFO` on the root logger. The arguments and behavior are otherwise the same as for `debug()`.

**logging.warning(*msg*, **args*, ***kwargs*)**

Logs a message with level `WARNING` on the root logger. The arguments and behavior are otherwise the same as for `debug()`.

Note

There is an obsolete function `warn` which is functionally identical to `warning`. As `warn` is deprecated, please do not use it - use `warning` instead.

**logging.error(*msg*, **args*, ***kwargs*)**

Logs a message with level `ERROR` on the root logger. The arguments and behavior are otherwise the same as for `debug()`.

**logging.critical(*msg*, **args*, ***kwargs*)**

Logs a message with level `CRITICAL` on the root logger. The arguments and behavior are otherwise the same as for `debug()`.

**logging.exception(*msg*, **args*, ***kwargs*)**

Logs a message with level `ERROR` on the root logger. The arguments and behavior are otherwise the same as for `debug()`. Exception info is added to the logging message. This function should only be called from an exception handler.

**logging.log(*level*, *msg*, **args*, ***kwargs*)**

Logs a message with level *level* on the root logger. The arguments and behavior are otherwise the same as for `debug()`.

**logging.disable(*level=CRITICAL*)**

Provides an overriding level *level* for all loggers which takes precedence over the logger’s own level. When the need arises to temporarily throttle logging output down across the whole application, this function can be useful. Its effect is to disable all logging calls of severity *level* and below, so that if you call it with a value of INFO, then all INFO and DEBUG events would be discarded, whereas those of severity WARNING and above would be processed according to the logger’s effective level. If `logging.disable(logging.NOTSET)` is called, it effectively removes this overriding level, so that logging output again depends on the effective levels of individual loggers.

Note that if you have defined any custom logging level higher than `CRITICAL` (this is not recommended), you won’t be able to rely on the default value for the *level* parameter, but will have to explicitly supply a suitable value.

Changed in version 3.7: The *level* parameter was defaulted to level `CRITICAL`. See bpo-28524 for more information about this change.

**logging.addLevelName(*level*, *levelName*)**

Associates level *level* with text *levelName* in an internal dictionary, which is used to map numeric levels to a textual representation, for example when a `Formatter` formats a message. This function can also be used to define your own levels. The only constraints are that all levels used must be registered using this function, levels should be positive integers and they should increase in increasing order of severity.

Note

If you are thinking of defining your own levels, please see the section on Custom Levels.

**logging.getLevelNamesMapping()**

Returns a mapping from level names to their corresponding logging levels. For example, the string “CRITICAL” maps to `CRITICAL`. The returned mapping is copied from an internal mapping on each call to this function.

Added in version 3.11.

**logging.getLevelName(*level*)**

Returns the textual or numeric representation of logging level *level*.

If *level* is one of the predefined levels `CRITICAL`, `ERROR`, `WARNING`, `INFO` or `DEBUG` then you get the corresponding string. If you have associated levels with names using `addLevelName()` then the name you have associated with *level* is returned. If a numeric value corresponding to one of the defined levels is passed in, the corresponding string representation is returned.

The *level* parameter also accepts a string representation of the level such as ‘INFO’. In such cases, this functions returns the corresponding numeric value of the level.

If no matching numeric or string value is passed in, the string ‘Level %s’ % level is returned.

Note

Levels are internally integers (as they need to be compared in the logging logic). This function is used to convert between an integer level and the level name displayed in the formatted log output by means of the `%(levelname)s` format specifier (see LogRecord attributes), and vice versa.

Changed in version 3.4: In Python versions earlier than 3.4, this function could also be passed a text level, and would return the corresponding numeric value of the level. This undocumented behaviour was considered a mistake, and was removed in Python 3.4, but reinstated in 3.4.2 due to retain backward compatibility.

**logging.getHandlerByName(*name*)**

Returns a handler with the specified *name*, or `None` if there is no handler with that name.

Added in version 3.12.

**logging.getHandlerNames()**

Returns an immutable set of all known handler names.

Added in version 3.12.

**logging.makeLogRecord(*attrdict*)**

Creates and returns a new `LogRecord` instance whose attributes are defined by *attrdict*. This function is useful for taking a pickled `LogRecord` attribute dictionary, sent over a socket, and reconstituting it as a `LogRecord` instance at the receiving end.

**logging.basicConfig(***kwargs*)**

Does basic configuration for the logging system by creating a `StreamHandler` with a default `Formatter` and adding it to the root logger. The functions `debug()`, `info()`, `warning()`, `error()` and `critical()` will call `basicConfig()` automatically if no handlers are defined for the root logger.

This function does nothing if the root logger already has handlers configured, unless the keyword argument *force* is set to `True`.

Note

This function should be called from the main thread before other threads are started. In versions of Python prior to 2.7.1 and 3.2, if this function is called from multiple threads, it is possible (in rare circumstances) that a handler will be added to the root logger more than once, leading to unexpected results such as messages being duplicated in the log.

The following keyword arguments are supported.

| Format | Description |
|---|---|
| *filename* | Specifies that a `FileHandler` be created, using the specified filename, rather than a `StreamHandler`. |
| *filemode* | If *filename* is specified, open the file in this mode. Defaults to `'a'`. |
| *format* | Use the specified format string for the handler. Defaults to attributes `levelname`, `name` and `message` separated by colons. |
| *datefmt* | Use the specified date/time format, as accepted by `time.strftime()`. |
| *style* | If *format* is specified, use this style for the format string. One of `'%'`, `'{'` or `'$'` for printf-style, `str.format()` or `string.Template` respectively. Defaults to `'%'`. |
| *level* | Set the root logger level to the specified level. |
| *stream* | Use the specified stream to initialize the `StreamHandler`. Note that this argument is incompatible with *filename* - if both are present, a `ValueError` is raised. |
| *handlers* | If specified, this should be an iterable of already created handlers to add to the root logger. Any handlers which don’t already have a formatter set will be assigned the default formatter created in this function. Note that this argument is incompatible with *filename* or *stream* - if both are present, a `ValueError` is raised. |
| *force* | If this keyword argument is specified as true, any existing handlers attached to the root logger are removed and closed, before carrying out the configuration as specified by the other arguments. |
| *encoding* | If this keyword argument is specified along with *filename*, its value is used when the `FileHandler` is created, and thus used when opening the output file. |
| *errors* | If this keyword argument is specified along with *filename*, its value is used when the `FileHandler` is created, and thus used when opening the output file. If not specified, the value ‘backslashreplace’ is used. Note that if `None` is specified, it will be passed as such to `open()`, which means that it will be treated the same as passing ‘errors’. |

Changed in version 3.2: The *style* argument was added.

Changed in version 3.3: The *handlers* argument was added. Additional checks were added to catch situations where incompatible arguments are specified (e.g. *handlers* together with *stream* or *filename*, or *stream* together with *filename*).

Changed in version 3.8: The *force* argument was added.

Changed in version 3.9: The *encoding* and *errors* arguments were added.

**logging.shutdown()**

Informs the logging system to perform an orderly shutdown by flushing and closing all handlers. This should be called at application exit and no further use of the logging system should be made after this call.

When the logging module is imported, it registers this function as an exit handler (see `atexit`), so normally there’s no need to do that manually.

**logging.setLoggerClass(*klass*)**

Tells the logging system to use the class *klass* when instantiating a logger. The class should define `__init__()` such that only a name argument is required, and the `__init__()` should call `Logger.__init__()`. This function is typically called before any loggers are instantiated by applications which need to use custom logger behavior. After this call, as at any other time, do not instantiate loggers directly using the subclass: continue to use the `logging.getLogger()` API to get your loggers.

**logging.setLogRecordFactory(*factory*)**

Set a callable which is used to create a `LogRecord`.

**Parameters:**

**factory** – The factory callable to be used to instantiate a log record.

Added in version 3.2: This function has been provided, along with `getLogRecordFactory()`, to allow developers more control over how the `LogRecord` representing a logging event is constructed.

The factory has the following signature:

`factory(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)`

> **name:**
> 
> The logger name.
> 
> **level:**
> 
> The logging level (numeric).
> 
> **fn:**
> 
> The full pathname of the file where the logging call was made.
> 
> **lno:**
> 
> The line number in the file where the logging call was made.
> 
> **msg:**
> 
> The logging message.
> 
> **args:**
> 
> The arguments for the logging message.
> 
> **exc_info:**
> 
> An exception tuple, or `None`.
> 
> **func:**
> 
> The name of the function or method which invoked the logging call.
> 
> **sinfo:**
> 
> A stack traceback such as is provided by `traceback.print_stack()`, showing the call hierarchy.
> 
> **kwargs:**
> 
> Additional keyword arguments.


## Module-Level Attributes

**logging.lastResort**

A “handler of last resort” is available through this attribute. This is a `StreamHandler` writing to `sys.stderr` with a level of `WARNING`, and is used to handle logging events in the absence of any logging configuration. The end result is to just print the message to `sys.stderr`. This replaces the earlier error message saying that “no handlers could be found for logger XYZ”. If you need the earlier behaviour for some reason, `lastResort` can be set to `None`.

Added in version 3.2.

**logging.raiseExceptions**

Used to see if exceptions during handling should be propagated.

Default: `True`.

If `raiseExceptions` is `False`, exceptions get silently ignored. This is what is mostly wanted for a logging system - most users will not care about errors in the logging system, they are more interested in application errors.


## Integration with the warnings module

The `captureWarnings()` function can be used to integrate `logging` with the `warnings` module.

**logging.captureWarnings(*capture*)**

This function is used to turn the capture of warnings by logging on and off.

If *capture* is `True`, warnings issued by the `warnings` module will be redirected to the logging system. Specifically, a warning will be formatted using `warnings.formatwarning()` and the resulting string logged to a logger named `'py.warnings'` with a severity of `WARNING`.

If *capture* is `False`, the redirection of warnings to the logging system will stop, and warnings will be redirected to their original destinations (i.e. those in effect before `captureWarnings(True)` was called).

See also

**Module `logging.config`**

Configuration API for the logging module.

**Module `logging.handlers`**

Useful handlers included with the logging module.

****PEP 282** - A Logging System**

The proposal which described this feature for inclusion in the Python standard library.

**Original Python logging package**

This is the original source for the `logging` package. The version of the package available from this site is suitable for use with Python 1.5.2, 2.1.x and 2.2.x, which do not include the `logging` package in the standard library.
