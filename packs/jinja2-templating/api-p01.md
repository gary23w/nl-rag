---
title: "API — Jinja Documentation (3.1.x) (part 1/2)"
source: https://jinja.palletsprojects.com/en/stable/api/
domain: jinja2-templating
license: CC-BY-SA-4.0
tags: python jinja2, jinja2 template engine, template rendering python
fetched: 2026-07-02
part: 1/2
---

# API

This document describes the API to Jinja and not the template language (for that, see Template Designer Documentation). It will be most useful as reference to those implementing the template interface to the application and not those who are creating Jinja templates.


## Basics

Jinja uses a central object called the template `Environment`. Instances of this class are used to store the configuration and global objects, and are used to load templates from the file system or other locations. Even if you are creating templates from strings by using the constructor of `Template` class, an environment is created automatically for you, albeit a shared one.

Most applications will create one `Environment` object on application initialization and use that to load templates. In some cases however, it’s useful to have multiple environments side by side, if different configurations are in use.

The simplest way to configure Jinja to load templates for your application is to use `PackageLoader`.

```python
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("yourapp"),
    autoescape=select_autoescape()
)
```

This will create a template environment with a loader that looks up templates in the `templates` folder inside the `yourapp` Python package (or next to the `yourapp.py` Python module). It also enables autoescaping for HTML files. This loader only requires that `yourapp` is importable, it figures out the absolute path to the folder for you.

Different loaders are available to load templates in other ways or from other locations. They’re listed in the Loaders section below. You can also write your own if you want to load templates from a source that’s more specialized to your project.

To load a template from this environment, call the `get_template()` method, which returns the loaded `Template`.

```python
template = env.get_template("mytemplate.html")
```

To render it with some variables, call the `render()` method.

```python
print(template.render(the="variables", go="here"))
```

Using a template loader rather than passing strings to `Template` or `Environment.from_string()` has multiple advantages. Besides being a lot easier to use it also enables template inheritance.

Notes on Autoescaping

In future versions of Jinja we might enable autoescaping by default for security reasons. As such you are encouraged to explicitly configure autoescaping now instead of relying on the default.


## High Level API

The high-level API is the API you will use in the application to load and render Jinja templates. The Low Level API on the other side is only useful if you want to dig deeper into Jinja or develop extensions.

***class*jinja2.Environment([*options*])**

The core component of Jinja is the `Environment`. It contains important shared variables like configuration, filters, tests, globals and others. Instances of this class may be modified if they are not shared and if no template was loaded so far. Modifications on environments after the first template was loaded will lead to surprising effects and undefined behavior.

Here are the possible initialization parameters:

> **`block_start_string`**
> 
> The string marking the beginning of a block. Defaults to `'{%'`.
> 
> **`block_end_string`**
> 
> The string marking the end of a block. Defaults to `'%}'`.
> 
> **`variable_start_string`**
> 
> The string marking the beginning of a print statement. Defaults to `'{{'`.
> 
> **`variable_end_string`**
> 
> The string marking the end of a print statement. Defaults to `'}}'`.
> 
> **`comment_start_string`**
> 
> The string marking the beginning of a comment. Defaults to `'{#'`.
> 
> **`comment_end_string`**
> 
> The string marking the end of a comment. Defaults to `'#}'`.
> 
> **`line_statement_prefix`**
> 
> If given and a string, this will be used as prefix for line based statements. See also Line Statements.
> 
> **`line_comment_prefix`**
> 
> If given and a string, this will be used as prefix for line based comments. See also Line Statements.
> 
> Changelog
> 
> Added in version 2.2.
> 
> **`trim_blocks`**
> 
> If this is set to `True` the first newline after a block is removed (block, not variable tag!). Defaults to `False`.
> 
> **`lstrip_blocks`**
> 
> If this is set to `True` leading spaces and tabs are stripped from the start of a line to a block. Defaults to `False`.
> 
> **`newline_sequence`**
> 
> The sequence that starts a newline. Must be one of `'\r'`, `'\n'` or `'\r\n'`. The default is `'\n'` which is a useful default for Linux and OS X systems as well as web applications.
> 
> **`keep_trailing_newline`**
> 
> Preserve the trailing newline when rendering templates. The default is `False`, which causes a single newline, if present, to be stripped from the end of the template.
> 
> Changelog
> 
> Added in version 2.7.
> 
> **`extensions`**
> 
> List of Jinja extensions to use. This can either be import paths as strings or extension classes. For more information have a look at the extensions documentation.
> 
> **`optimized`**
> 
> should the optimizer be enabled? Default is `True`.
> 
> **`undefined`**
> 
> `Undefined` or a subclass of it that is used to represent undefined values in the template.
> 
> **`finalize`**
> 
> A callable that can be used to process the result of a variable expression before it is output. For example one can convert `None` implicitly into an empty string here.
> 
> **`autoescape`**
> 
> If set to `True` the XML/HTML autoescaping feature is enabled by default. For more details about autoescaping see `Markup`. As of Jinja 2.4 this can also be a callable that is passed the template name and has to return `True` or `False` depending on autoescape should be enabled by default.
> 
> Changelog
> 
> Changed in version 2.4: `autoescape` can now be a function
> 
> **`loader`**
> 
> The template loader for this environment.
> 
> **`cache_size`**
> 
> The size of the cache. Per default this is `400` which means that if more than 400 templates are loaded the loader will clean out the least recently used template. If the cache size is set to `0` templates are recompiled all the time, if the cache size is `-1` the cache will not be cleaned.
> 
> Changelog
> 
> Changed in version 2.8: The cache size was increased to 400 from a low 50.
> 
> **`auto_reload`**
> 
> Some loaders load templates from locations where the template sources may change (ie: file system or database). If `auto_reload` is set to `True` (default) every time a template is requested the loader checks if the source changed and if yes, it will reload the template. For higher performance it’s possible to disable that.
> 
> **`bytecode_cache`**
> 
> If set to a bytecode cache object, this object will provide a cache for the internal Jinja bytecode so that templates don’t have to be parsed if they were not changed.
> 
> See Bytecode Cache for more information.
> 
> **`enable_async`**
> 
> If set to true this enables async template execution which allows using async functions and generators.

**Parameters:**

- **block_start_string** (*str*)
- **block_end_string** (*str*)
- **variable_start_string** (*str*)
- **variable_end_string** (*str*)
- **comment_start_string** (*str*)
- **comment_end_string** (*str*)
- **line_statement_prefix** (*str**|**None*)
- **line_comment_prefix** (*str**|**None*)
- **trim_blocks** (*bool*)
- **lstrip_blocks** (*bool*)
- **newline_sequence** (*te.Literal**[**'\n'**,**'\r\n'**,**'\r'**]*)
- **keep_trailing_newline** (*bool*)
- **extensions** (*Sequence**[**str**|**Type**[**Extension**]**]*)
- **optimized** (*bool*)
- **undefined** (*Type**[**Undefined**]*)
- **finalize** (*Callable**[**[**...**]**,**Any**]**|**None*)
- **autoescape** (*bool**|**Callable**[**[**str**|**None**]**,**bool**]*)
- **loader** (*BaseLoader**|**None*)
- **cache_size** (*int*)
- **auto_reload** (*bool*)
- **bytecode_cache** (*BytecodeCache**|**None*)
- **enable_async** (*bool*)

**shared**

If a template was created by using the `Template` constructor an environment is created automatically. These environments are created as shared environments which means that multiple templates may have the same anonymous environment. For all shared environments this attribute is `True`, else `False`.

**sandboxed**

If the environment is sandboxed this attribute is `True`. For the sandbox mode have a look at the documentation for the `SandboxedEnvironment`.

**filters**

A dict of filters for this environment. As long as no template was loaded it’s safe to add new filters or remove old. For custom filters see Custom Filters. For valid filter names have a look at Notes on Identifiers.

**tests**

A dict of test functions for this environment. As long as no template was loaded it’s safe to modify this dict. For custom tests see Custom Tests. For valid test names have a look at Notes on Identifiers.

**globals**

A dict of variables that are available in every template loaded by the environment. As long as no template was loaded it’s safe to modify this. For more details see The Global Namespace. For valid object names see Notes on Identifiers.

**policies**

A dictionary with Policies. These can be reconfigured to change the runtime behavior or certain template features. Usually these are security related.

**code_generator_class**

The class used for code generation. This should not be changed in most cases, unless you need to modify the Python code a template compiles to.

**context_class**

The context used for templates. This should not be changed in most cases, unless you need to modify internals of how template variables are handled. For details, see `Context`.

**overlay([*options*])**

Create a new overlay environment that shares all the data with the current environment except for cache and the overridden attributes. Extensions cannot be removed for an overlayed environment. An overlayed environment automatically gets all the extensions of the environment it is linked to plus optional extra extensions.

Creating overlays should happen after the initial environment was set up completely. Not all attributes are truly linked, some are just copied over so modifications on the original environment may not shine through.

Changed in version 3.1.5: `enable_async` is applied correctly.

Changed in version 3.1.2: Added the `newline_sequence`, `keep_trailing_newline`, and `enable_async` parameters to match `__init__`.

**Parameters:**

- **block_start_string** (*str*)
- **block_end_string** (*str*)
- **variable_start_string** (*str*)
- **variable_end_string** (*str*)
- **comment_start_string** (*str*)
- **comment_end_string** (*str*)
- **line_statement_prefix** (*str**|**None*)
- **line_comment_prefix** (*str**|**None*)
- **trim_blocks** (*bool*)
- **lstrip_blocks** (*bool*)
- **newline_sequence** (*te.Literal**[**'\n'**,**'\r\n'**,**'\r'**]*)
- **keep_trailing_newline** (*bool*)
- **extensions** (*Sequence**[**str**|**Type**[**Extension**]**]*)
- **optimized** (*bool*)
- **undefined** (*Type**[**Undefined**]*)
- **finalize** (*Callable**[**[**...**]**,**Any**]**|**None*)
- **autoescape** (*bool**|**Callable**[**[**str**|**None**]**,**bool**]*)
- **loader** (*BaseLoader**|**None*)
- **cache_size** (*int*)
- **auto_reload** (*bool*)
- **bytecode_cache** (*BytecodeCache**|**None*)
- **enable_async** (*bool*)

**Return type:**

te.Self

**undefined([*hint*, *obj*, *name*, *exc*])**

Creates a new `Undefined` object for `name`. This is useful for filters or functions that may return undefined objects for some operations. All parameters except of `hint` should be provided as keyword parameters for better readability. The `hint` is used as error message for the exception if provided, otherwise the error message will be generated from `obj` and `name` automatically. The exception provided as `exc` is raised if something with the generated undefined object is done that the undefined object does not allow. The default exception is `UndefinedError`. If a `hint` is provided the `name` may be omitted.

The most common way to create an undefined object is by providing a name only:

```
return environment.undefined(name='some_name')
```

This means that the name `some_name` is not defined. If the name was from an attribute of an object it makes sense to tell the undefined object the holder object to improve the error message:

```
if not hasattr(obj, 'attr'):
    return environment.undefined(obj=obj, name='attr')
```

For a more complex example you can provide a hint. For example the `first()` filter creates an undefined object that way:

```
return environment.undefined('no first item, sequence was empty')
```

If it the `name` or `obj` is known (for example because an attribute was accessed) it should be passed to the undefined object, even if a custom `hint` is provided. This gives undefined objects the possibility to enhance the error message.

**add_extension(*extension*)**

Adds an extension after the environment was created.

Changelog

Added in version 2.5.

**Parameters:**

**extension** (*str**|**Type**[**Extension**]*)

**Return type:**

None

**extend(***attributes*)**

Add the items to the instance of the environment if they do not exist yet. This is used by extensions to register callbacks and configuration values without breaking inheritance.

**Parameters:**

**attributes** (*Any*)

**Return type:**

None

**compile_expression(*source*, *undefined_to_none=True*)**

A handy helper method that returns a callable that accepts keyword arguments that appear as variables in the expression. If called it returns the result of the expression.

This is useful if applications want to use the same rules as Jinja in template “configuration files” or similar situations.

Example usage:

```
>>> env = Environment()
>>> expr = env.compile_expression('foo == 42')
>>> expr(foo=23)
False
>>> expr(foo=42)
True
```

Per default the return value is converted to `None` if the expression returns an undefined value. This can be changed by setting `undefined_to_none` to `False`.

```
>>> env.compile_expression('var')() is None
True
>>> env.compile_expression('var', undefined_to_none=False)()
Undefined
```

Changelog

Added in version 2.1.

**Parameters:**

- **source** (*str*)
- **undefined_to_none** (*bool*)

**Return type:**

*TemplateExpression*

**compile_templates(*target*, *extensions=None*, *filter_func=None*, *zip='deflated'*, *log_function=None*, *ignore_errors=True*)**

Finds all the templates the loader can find, compiles them and stores them in `target`. If `zip` is `None`, instead of in a zipfile, the templates will be stored in a directory. By default a deflate zip algorithm is used. To switch to the stored algorithm, `zip` can be set to `'stored'`.

`extensions` and `filter_func` are passed to `list_templates()`. Each template returned will be compiled to the target folder or zipfile.

By default template compilation errors are ignored. In case a log function is provided, errors are logged. If you want template syntax errors to abort the compilation you can set `ignore_errors` to `False` and you will get an exception on syntax errors.

Changelog

Added in version 2.4.

**Parameters:**

- **target** (*str**|**PathLike**[**str**]*)
- **extensions** (*Collection**[**str**]**|**None*)
- **filter_func** (*Callable**[**[**str**]**,**bool**]**|**None*)
- **zip** (*str**|**None*)
- **log_function** (*Callable**[**[**str**]**,**None**]**|**None*)
- **ignore_errors** (*bool*)

**Return type:**

None

**list_templates(*extensions=None*, *filter_func=None*)**

Returns a list of templates for this environment. This requires that the loader supports the loader’s `list_templates()` method.

If there are other files in the template folder besides the actual templates, the returned list can be filtered. There are two ways: either `extensions` is set to a list of file extensions for templates, or a `filter_func` can be provided which is a callable that is passed a template name and should return `True` if it should end up in the result list.

If the loader does not support that, a `TypeError` is raised.

Changelog

Added in version 2.4.

**Parameters:**

- **extensions** (*Collection**[**str**]**|**None*)
- **filter_func** (*Callable**[**[**str**]**,**bool**]**|**None*)

**Return type:**

*List*[str]

**join_path(*template*, *parent*)**

Join a template with the parent. By default all the lookups are relative to the loader root so this method returns the `template` parameter unchanged, but if the paths should be relative to the parent template, this function can be used to calculate the real template name.

Subclasses may override this method and implement template path joining here.

**Parameters:**

- **template** (*str*)
- **parent** (*str*)

**Return type:**

str

**get_template(*name*, *parent=None*, *globals=None*)**

Load a template by name with `loader` and return a `Template`. If the template does not exist a `TemplateNotFound` exception is raised.

**Parameters:**

- **name** (*str**|**Template*) – Name of the template to load. When loading templates from the filesystem, “/” is used as the path separator, even on Windows.
- **parent** (*str**|**None*) – The name of the parent template importing this template. `join_path()` can be used to implement name transformations with this.
- **globals** (*MutableMapping**[**str**,**Any**]**|**None*) – Extend the environment `globals` with these extra variables available for all renders of this template. If the template has already been loaded and cached, its globals are updated with any new items.

**Return type:**

*Template*

Changelog

Changed in version 3.0: If a template is loaded from cache, `globals` will update the template’s globals instead of ignoring the new values.

Changed in version 2.4: If `name` is a `Template` object it is returned unchanged.

**select_template(*names*, *parent=None*, *globals=None*)**

Like `get_template()`, but tries loading multiple names. If none of the names can be loaded a `TemplatesNotFound` exception is raised.

**Parameters:**

- **names** (*Iterable**[**str**|**Template**]*) – List of template names to try loading in order.
- **parent** (*str**|**None*) – The name of the parent template importing this template. `join_path()` can be used to implement name transformations with this.
- **globals** (*MutableMapping**[**str**,**Any**]**|**None*) – Extend the environment `globals` with these extra variables available for all renders of this template. If the template has already been loaded and cached, its globals are updated with any new items.

**Return type:**

*Template*

Changelog

Changed in version 3.0: If a template is loaded from cache, `globals` will update the template’s globals instead of ignoring the new values.

Changed in version 2.11: If `names` is `Undefined`, an `UndefinedError` is raised instead. If no templates were found and `names` contains `Undefined`, the message is more helpful.

Changed in version 2.4: If `names` contains a `Template` object it is returned unchanged.

Added in version 2.3.

**get_or_select_template(*template_name_or_list*, *parent=None*, *globals=None*)**

Use `select_template()` if an iterable of template names is given, or `get_template()` if one name is given.

Changelog

Added in version 2.3.

**Parameters:**

- **template_name_or_list** (*str**|**Template**|**List**[**str**|**Template**]*)
- **parent** (*str**|**None*)
- **globals** (*MutableMapping**[**str**,**Any**]**|**None*)

**Return type:**

*Template*

**from_string(*source*, *globals=None*, *template_class=None*)**

Load a template from a source string without using `loader`.

**Parameters:**

- **source** (*str**|**Template*) – Jinja source to compile into a template.
- **globals** (*MutableMapping**[**str**,**Any**]**|**None*) – Extend the environment `globals` with these extra variables available for all renders of this template. If the template has already been loaded and cached, its globals are updated with any new items.
- **template_class** (*Type**[**Template**]**|**None*) – Return an instance of this `Template` class.

**Return type:**

*Template*

***class*jinja2.Template(*source*, *block_start_string=BLOCK_START_STRING*, *block_end_string=BLOCK_END_STRING*, *variable_start_string=VARIABLE_START_STRING*, *variable_end_string=VARIABLE_END_STRING*, *comment_start_string=COMMENT_START_STRING*, *comment_end_string=COMMENT_END_STRING*, *line_statement_prefix=LINE_STATEMENT_PREFIX*, *line_comment_prefix=LINE_COMMENT_PREFIX*, *trim_blocks=TRIM_BLOCKS*, *lstrip_blocks=LSTRIP_BLOCKS*, *newline_sequence=NEWLINE_SEQUENCE*, *keep_trailing_newline=KEEP_TRAILING_NEWLINE*, *extensions=()*, *optimized=True*, *undefined=Undefined*, *finalize=None*, *autoescape=False*, *enable_async=False*)**

A compiled template that can be rendered.

Use the methods on `Environment` to create or load templates. The environment is used to configure how templates are compiled and behave.

It is also possible to create a template object directly. This is not usually recommended. The constructor takes most of the same arguments as `Environment`. All templates created with the same environment arguments share the same ephemeral `Environment` instance behind the scenes.

A template object should be considered immutable. Modifications on the object are not supported.

**Parameters:**

- **source** (*str**|**Template*)
- **block_start_string** (*str*)
- **block_end_string** (*str*)
- **variable_start_string** (*str*)
- **variable_end_string** (*str*)
- **comment_start_string** (*str*)
- **comment_end_string** (*str*)
- **line_statement_prefix** (*str**|**None*)
- **line_comment_prefix** (*str**|**None*)
- **trim_blocks** (*bool*)
- **lstrip_blocks** (*bool*)
- **newline_sequence** (*te.Literal**[**'\n'**,**'\r\n'**,**'\r'**]*)
- **keep_trailing_newline** (*bool*)
- **extensions** (*Sequence**[**str**|**Type**[**Extension**]**]*)
- **optimized** (*bool*)
- **undefined** (*Type**[**Undefined**]*)
- **finalize** (*Callable**[**[**...**]**,**Any**]**|**None*)
- **autoescape** (*bool**|**Callable**[**[**str**|**None**]**,**bool**]*)
- **enable_async** (*bool*)

**Return type:**

*Any*

**globals**

A dict of variables that are available every time the template is rendered, without needing to pass them during render. This should not be modified, as depending on how the template was loaded it may be shared with the environment and other templates.

Defaults to `Environment.globals` unless extra values are passed to `Environment.get_template()`.

Globals are only intended for data that is common to every render of the template. Specific data should be passed to `render()`.

See The Global Namespace.

**name**

The loading name of the template. If the template was loaded from a string this is `None`.

**filename**

The filename of the template on the file system if it was loaded from there. Otherwise this is `None`.

**render([*context*])**

This method accepts the same arguments as the `dict` constructor: A dict, a dict subclass or some keyword arguments. If no arguments are given the context will be empty. These two calls do the same:

```
template.render(knights='that say nih')
template.render({'knights': 'that say nih'})
```

This will return the rendered template as a string.

**Parameters:**

- **args** (*Any*)
- **kwargs** (*Any*)

**Return type:**

str

**generate([*context*])**

For very large templates it can be useful to not render the whole template at once but evaluate each statement after another and yield piece for piece. This method basically does exactly that and returns a generator that yields one item after another as strings.

It accepts the same arguments as `render()`.

**Parameters:**

- **args** (*Any*)
- **kwargs** (*Any*)

**Return type:**

*Iterator*[str]

**stream([*context*])**

Works exactly like `generate()` but returns a `TemplateStream`.

**Parameters:**

- **args** (*Any*)
- **kwargs** (*Any*)

**Return type:**

*TemplateStream*

***async*render_async([*context*])**

This works similar to `render()` but returns a coroutine that when awaited returns the entire rendered template string. This requires the async feature to be enabled.

Example usage:

```
await template.render_async(knights='that say nih; asynchronously')
```

**Parameters:**

- **args** (*Any*)
- **kwargs** (*Any*)

**Return type:**

str

***async*generate_async([*context*])**

An async version of `generate()`. Works very similarly but returns an async iterator instead.

**Parameters:**

- **args** (*Any*)
- **kwargs** (*Any*)

**Return type:**

*AsyncGenerator*[str, object]

**make_module(*vars=None*, *shared=False*, *locals=None*)**

This method works like the `module` attribute when called without arguments but it will evaluate the template on every call rather than caching it. It’s also possible to provide a dict which is then used as context. The arguments are the same as for the `new_context()` method.

**Parameters:**

- **vars** (*Dict**[**str**,**Any**]**|**None*)
- **shared** (*bool*)
- **locals** (*Mapping**[**str**,**Any**]**|**None*)

**Return type:**

*TemplateModule*

***property*module*: TemplateModule***

The template as module. This is used for imports in the template runtime but is also useful if one wants to access exported template variables from the Python layer:

```
>>> t = Template('{% macro foo() %}42{% endmacro %}23')
>>> str(t.module)
'23'
>>> t.module.foo() == u'42'
True
```

This attribute is not available if async mode is enabled.

***class*jinja2.environment.TemplateStream**

A template stream works pretty much like an ordinary python generator but it can buffer multiple items to reduce the number of total iterations. Per default the output is unbuffered which means that for every unbuffered instruction in the template one string is yielded.

If buffering is enabled with a buffer size of 5, five items are combined into a new string. This is mainly useful if you are streaming big templates to a client via WSGI which flushes after each iteration.

**Parameters:**

**gen** (*Iterator**[**str**]*)

**dump(*fp*, *encoding=None*, *errors='strict'*)**

Dump the complete stream into a file or file-like object. Per default strings are written, if you want to encode before writing specify an `encoding`.

Example usage:

```
Template('Hello {{ name }}!').stream(name='foo').dump('hello.html')
```

**Parameters:**

- **fp** (*str**|**IO**[**bytes**]*)
- **encoding** (*str**|**None*)
- **errors** (*str**|**None*)

**Return type:**

None

**disable_buffering()**

Disable the output buffering.

**Return type:**

None

**enable_buffering(*size=5*)**

Enable buffering. Buffer `size` items before yielding them.

**Parameters:**

**size** (*int*)

**Return type:**

None


## Autoescaping

Changelog

Changed in version 2.4.

Jinja now comes with autoescaping support. As of Jinja 2.9 the autoescape extension is removed and built-in. However autoescaping is not yet enabled by default though this will most likely change in the future. It’s recommended to configure a sensible default for autoescaping. This makes it possible to enable and disable autoescaping on a per-template basis (HTML versus text for instance).

**jinja2.select_autoescape(*enabled_extensions=('html', 'htm', 'xml')*, *disabled_extensions=()*, *default_for_string=True*, *default=False*)**

Intelligently sets the initial value of autoescaping based on the filename of the template. This is the recommended way to configure autoescaping if you do not want to write a custom function yourself.

If you want to enable it for all templates created from strings or for all templates with `.html` and `.xml` extensions:

```
from jinja2 import Environment, select_autoescape
env = Environment(autoescape=select_autoescape(
    enabled_extensions=('html', 'xml'),
    default_for_string=True,
))
```

Example configuration to turn it on at all times except if the template ends with `.txt`:

```
from jinja2 import Environment, select_autoescape
env = Environment(autoescape=select_autoescape(
    disabled_extensions=('txt',),
    default_for_string=True,
    default=True,
))
```

The `enabled_extensions` is an iterable of all the extensions that autoescaping should be enabled for. Likewise `disabled_extensions` is a list of all templates it should be disabled for. If a template is loaded from a string then the default from `default_for_string` is used. If nothing matches then the initial value of autoescaping is set to the value of `default`.

For security reasons this function operates case insensitive.

Changelog

Added in version 2.9.

**Parameters:**

- **enabled_extensions** (*Collection**[**str**]*)
- **disabled_extensions** (*Collection**[**str**]*)
- **default_for_string** (*bool*)
- **default** (*bool*)

**Return type:**

*Callable*[[str | None], bool]

Here a recommended setup that enables autoescaping for templates ending in `'.html'`, `'.htm'` and `'.xml'` and disabling it by default for all other extensions. You can use the `select_autoescape()` function for this:

```
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(autoescape=select_autoescape(['html', 'htm', 'xml']),
                  loader=PackageLoader('mypackage'))
```

The `select_autoescape()` function returns a function that works roughly like this:

```
def autoescape(template_name):
    if template_name is None:
        return False
    if template_name.endswith(('.html', '.htm', '.xml'))
```

When implementing a guessing autoescape function, make sure you also accept `None` as valid template name. This will be passed when generating templates from strings. You should always configure autoescaping as defaults in the future might change.

Inside the templates the behaviour can be temporarily changed by using the `autoescape` block (see Autoescape Overrides).


## Notes on Identifiers

Jinja uses Python naming rules. Valid identifiers can be any combination of characters accepted by Python.

Filters and tests are looked up in separate namespaces and have slightly modified identifier syntax. Filters and tests may contain dots to group filters and tests by topic. For example it’s perfectly valid to add a function into the filter dict and call it `to.str`. The regular expression for filter and test identifiers is `[a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)*`.


## Undefined Types

These classes can be used as undefined types. The `Environment` constructor takes an `undefined` parameter that can be one of those classes or a custom subclass of `Undefined`. Whenever the template engine is unable to look up a name or access an attribute one of those objects is created and returned. Some operations on undefined values are then allowed, others fail.

The closest to regular Python behavior is the `StrictUndefined` which disallows all operations beside testing if it’s an undefined object.

***class*jinja2.Undefined**

The default undefined type. This can be printed, iterated, and treated as a boolean. Any other operation will raise an `UndefinedError`.

```
>>> foo = Undefined(name='foo')
>>> str(foo)
''
>>> not foo
True
>>> foo + 42
Traceback (most recent call last):
  ...
jinja2.exceptions.UndefinedError: 'foo' is undefined
```

**Parameters:**

- **hint** (*str**|**None*)
- **obj** (*Any*)
- **name** (*str**|**None*)
- **exc** (*Type**[**TemplateRuntimeError**]*)

**_undefined_hint**

Either `None` or a string with the error message for the undefined object.

**_undefined_obj**

Either `None` or the owner object that caused the undefined object to be created (for example because an attribute does not exist).

**_undefined_name**

The name for the undefined variable / attribute or just `None` if no such information exists.

**_undefined_exception**

The exception that the undefined object wants to raise. This is usually one of `UndefinedError` or `SecurityError`.

**_fail_with_undefined_error(*\*args*, *\**kwargs*)**

When called with any arguments this method raises `_undefined_exception` with an error message generated from the undefined hints stored on the undefined object.

***class*jinja2.ChainableUndefined**

An undefined that is chainable, where both `__getattr__` and `__getitem__` return itself rather than raising an `UndefinedError`.

```
>>> foo = ChainableUndefined(name='foo')
>>> str(foo.bar['baz'])
''
>>> foo.bar['baz'] + 42
Traceback (most recent call last):
  ...
jinja2.exceptions.UndefinedError: 'foo' is undefined
```

Changelog

Added in version 2.11.0.

**Parameters:**

- **hint** (*str**|**None*)
- **obj** (*Any*)
- **name** (*str**|**None*)
- **exc** (*Type**[**TemplateRuntimeError**]*)

***class*jinja2.DebugUndefined**

An undefined that returns the debug info when printed.

```
>>> foo = DebugUndefined(name='foo')
>>> str(foo)
'{{ foo }}'
>>> not foo
True
>>> foo + 42
Traceback (most recent call last):
  ...
jinja2.exceptions.UndefinedError: 'foo' is undefined
```

**Parameters:**

- **hint** (*str**|**None*)
- **obj** (*Any*)
- **name** (*str**|**None*)
- **exc** (*Type**[**TemplateRuntimeError**]*)

***class*jinja2.StrictUndefined**

An undefined that barks on print and iteration as well as boolean tests and all kinds of comparisons. In other words: you can do nothing with it except checking if it’s defined using the `defined` test.

```
>>> foo = StrictUndefined(name='foo')
>>> str(foo)
Traceback (most recent call last):
  ...
jinja2.exceptions.UndefinedError: 'foo' is undefined
>>> not foo
Traceback (most recent call last):
  ...
jinja2.exceptions.UndefinedError: 'foo' is undefined
>>> foo + 42
Traceback (most recent call last):
  ...
jinja2.exceptions.UndefinedError: 'foo' is undefined
```

**Parameters:**

- **hint** (*str**|**None*)
- **obj** (*Any*)
- **name** (*str**|**None*)
- **exc** (*Type**[**TemplateRuntimeError**]*)

There is also a factory function that can decorate undefined objects to implement logging on failures:

**jinja2.make_logging_undefined(*logger=None*, *base=Undefined*)**

Given a logger object this returns a new undefined class that will log certain failures. It will log iterations and printing. If no logger is given a default logger is created.

Example:

```
logger = logging.getLogger(__name__)
LoggingUndefined = make_logging_undefined(
    logger=logger,
    base=Undefined
)
```

Changelog

Added in version 2.8.

**Parameters:**

- **logger** (*logging.Logger**|**None*) – the logger to use. If not provided, a default logger is created.
- **base** (*Type**[**Undefined**]*) – the base class to add logging functionality to. This defaults to `Undefined`.

**Return type:**

*Type*[*Undefined*]

Undefined objects are created by calling `undefined`.

Implementation

`Undefined` is implemented by overriding the special `__underscore__` methods. For example the default `Undefined` class implements `__str__` to returns an empty string, while `__int__` and others fail with an exception. To allow conversion to int by returning `0` you can implement your own subclass.

```python
class NullUndefined(Undefined):
    def __int__(self):
        return 0

    def __float__(self):
        return 0.0
```

To disallow a method, override it and raise `_undefined_exception`. Because this is very common there is the helper method `_fail_with_undefined_error()` that raises the error with the correct information. Here’s a class that works like the regular `Undefined` but fails on iteration:

```
class NonIterableUndefined(Undefined):
    def __iter__(self):
        self._fail_with_undefined_error()
```


## The Context

***class*jinja2.runtime.Context**

The template context holds the variables of a template. It stores the values passed to the template and also the names the template exports. Creating instances is neither supported nor useful as it’s created automatically at various stages of the template evaluation and should not be created by hand.

The context is immutable. Modifications on `parent` **must not** happen and modifications on `vars` are allowed from generated template code only. Template filters and global functions marked as `pass_context()` get the active context passed as first argument and are allowed to access the context read-only.

The template context supports read only dict operations (`get`, `keys`, `values`, `items`, `iterkeys`, `itervalues`, `iteritems`, `__getitem__`, `__contains__`). Additionally there is a `resolve()` method that doesn’t fail with a `KeyError` but returns an `Undefined` object for missing variables.

**Parameters:**

- **environment** (*Environment*)
- **parent** (*Dict**[**str**,**Any**]*)
- **name** (*str**|**None*)
- **blocks** (*Dict**[**str**,**Callable**[**[**Context**]**,**Iterator**[**str**]**]**]*)
- **globals** (*MutableMapping**[**str**,**Any**]**|**None*)

**parent**

A dict of read only, global variables the template looks up. These can either come from another `Context`, from the `Environment.globals` or `Template.globals` or points to a dict created by combining the globals with the variables passed to the render function. It must not be altered.

**vars**

The template local variables. This list contains environment and context functions from the `parent` scope as well as local modifications and exported variables from the template. The template will modify this dict during template evaluation but filters and context functions are not allowed to modify it.

**environment**

The environment that loaded the template.

**exported_vars**

This set contains all the names the template exports. The values for the names are in the `vars` dict. In order to get a copy of the exported variables as dict, `get_exported()` can be used.

**name**

The load name of the template owning this context.

**blocks**

A dict with the current mapping of blocks in the template. The keys in this dict are the names of the blocks, and the values a list of blocks registered. The last item in each list is the current active block (latest in the inheritance chain).

**eval_ctx**

The current Evaluation Context.

**call(*callable*, *\*args*, *\**kwargs*)**

Call the callable with the arguments and keyword arguments provided but inject the active context or environment as first argument if the callable has `pass_context()` or `pass_environment()`.

**Parameters:**

- **_Context__obj** (*Callable**[**[**...**]**,**Any**]*)
- **args** (*Any*)
- **kwargs** (*Any*)

**Return type:**

*Any* | *Undefined*

**get(*key*, *default=None*)**

Look up a variable by name, or return a default if the key is not found.

**Parameters:**

- **key** (*str*) – The variable name to look up.
- **default** (*Any*) – The value to return if the key is not found.

**Return type:**

*Any*

**resolve(*key*)**

Look up a variable by name, or return an `Undefined` object if the key is not found.

If you need to add custom behavior, override `resolve_or_missing()`, not this method. The various lookup functions use that method, not this one.

**Parameters:**

**key** (*str*) – The variable name to look up.

**Return type:**

*Any* | *Undefined*

**resolve_or_missing(*key*)**

Look up a variable by name, or return a `missing` sentinel if the key is not found.

Override this method to add custom lookup behavior. `resolve()`, `get()`, and `__getitem__()` use this method. Don’t call this method directly.

**Parameters:**

**key** (*str*) – The variable name to look up.

**Return type:**

*Any*

**get_exported()**

Get a new dict with the exported variables.

**Return type:**

*Dict*[str, *Any*]

**get_all()**

Return the complete context as dict including the exported variables. For optimizations reasons this might not return an actual copy so be careful with using it.

**Return type:**

*Dict*[str, *Any*]

The context is immutable, it prevents modifications, and if it is modified somehow despite that those changes may not show up. For performance, Jinja does not use the context as data storage for, only as a primary data source. Variables that the template does not define are looked up in the context, but variables the template does define are stored locally.

Instead of modifying the context directly, a function should return a value that can be assigned to a variable within the template itself.

```jinja
{% set comments = get_latest_comments() %}
```


## Loaders

Loaders are responsible for loading templates from a resource such as the file system. The environment will keep the compiled modules in memory like Python’s `sys.modules`. Unlike `sys.modules` however this cache is limited in size by default and templates are automatically reloaded. All loaders are subclasses of `BaseLoader`. If you want to create your own loader, subclass `BaseLoader` and override `get_source`.

***class*jinja2.BaseLoader**

Baseclass for all loaders. Subclass this and override `get_source` to implement a custom loading mechanism. The environment provides a `get_template` method that calls the loader’s `load` method to get the `Template` object.

A very basic example for a loader that looks up templates on the file system could look like this:

```
from jinja2 import BaseLoader, TemplateNotFound
from os.path import join, exists, getmtime

class MyLoader(BaseLoader):

    def __init__(self, path):
        self.path = path

    def get_source(self, environment, template):
        path = join(self.path, template)
        if not exists(path):
            raise TemplateNotFound(template)
        mtime = getmtime(path)
        with open(path) as f:
            source = f.read()
        return source, path, lambda: mtime == getmtime(path)
```

**get_source(*environment*, *template*)**

Get the template source, filename and reload helper for a template. It’s passed the environment and template name and has to return a tuple in the form `(source, filename, uptodate)` or raise a `TemplateNotFound` error if it can’t locate the template.

The source part of the returned tuple must be the source of the template as a string. The filename should be the name of the file on the filesystem if it was loaded from there, otherwise `None`. The filename is used by Python for the tracebacks if no loader extension is used.

The last item in the tuple is the `uptodate` function. If auto reloading is enabled it’s always called to check if the template changed. No arguments are passed so the function must store the old state somewhere (for example in a closure). If it returns `False` the template will be reloaded.

**Parameters:**

- **environment** (*Environment*)
- **template** (*str*)

**Return type:**

*Tuple*[str, str | None, *Callable*[[], bool] | None]

**load(*environment*, *name*, *globals=None*)**

Loads a template. This method looks up the template in the cache or loads one by calling `get_source()`. Subclasses should not override this method as loaders working on collections of other loaders (such as `PrefixLoader` or `ChoiceLoader`) will not call this method but `get_source` directly.

**Parameters:**

- **environment** (*Environment*)
- **name** (*str*)
- **globals** (*MutableMapping**[**str**,**Any**]**|**None*)

**Return type:**

Template

Here a list of the builtin loaders Jinja provides:

***class*jinja2.FileSystemLoader(*searchpath*, *encoding='utf-8'*, *followlinks=False*)**

Load templates from a directory in the file system.

The path can be relative or absolute. Relative paths are relative to the current working directory.

```python
loader = FileSystemLoader("templates")
```

A list of paths can be given. The directories will be searched in order, stopping at the first matching template.

```python
loader = FileSystemLoader(["/override/templates", "/default/templates"])
```

**Parameters:**

- **searchpath** (*str**|**os.PathLike**[**str**]**|**Sequence**[**str**|**os.PathLike**[**str**]**]*) – A path, or list of paths, to the directory that contains the templates.
- **encoding** (*str*) – Use this encoding to read the text from template files.
- **followlinks** (*bool*) – Follow symbolic links in the path.

Changelog

Changed in version 2.8: Added the `followlinks` parameter.

***class*jinja2.PackageLoader(*package_name*, *package_path='templates'*, *encoding='utf-8'*)**

Load templates from a directory in a Python package.

**Parameters:**

- **package_name** (*str*) – Import name of the package that contains the template directory.
- **package_path** (*str*) – Directory within the imported package that contains the templates.
- **encoding** (*str*) – Encoding of template files.

The following example looks up templates in the `pages` directory within the `project.ui` package.

```python
loader = PackageLoader("project.ui", "pages")
```

Only packages installed as directories (standard pip behavior) or zip/egg files (less common) are supported. The Python API for introspecting data in packages is too limited to support other installation methods the way this loader requires.

There is limited support for **PEP 420** namespace packages. The template directory is assumed to only be in one namespace contributor. Zip files contributing to a namespace are not supported.

Changelog

Changed in version 3.0: No longer uses `setuptools` as a dependency.

Changed in version 3.0: Limited PEP 420 namespace package support.

***class*jinja2.DictLoader(*mapping*)**

Loads a template from a Python dict mapping template names to template source. This loader is useful for unittesting:

```
>>> loader = DictLoader({'index.html': 'source here'})
```

Because auto reloading is rarely useful this is disabled by default.

**Parameters:**

**mapping** (*Mapping**[**str**,**str**]*)

***class*jinja2.FunctionLoader(*load_func*)**

A loader that is passed a function which does the loading. The function receives the name of the template and has to return either a string with the template source, a tuple in the form `(source, filename, uptodatefunc)` or `None` if the template does not exist.

```
>>> def load_template(name):
...     if name == 'index.html':
...         return '...'
...
>>> loader = FunctionLoader(load_template)
```

The `uptodatefunc` is a function that is called if autoreload is enabled and has to return `True` if the template is still up to date. For more details have a look at `BaseLoader.get_source()` which has the same return value.

**Parameters:**

**load_func** (*Callable**[**[**str**]**,**str**|**Tuple**[**str**,**str**|**None**,**Callable**[**[**]**,**bool**]**|**None**]**|**None**]*)

***class*jinja2.PrefixLoader(*mapping*, *delimiter='/'*)**

A loader that is passed a dict of loaders where each loader is bound to a prefix. The prefix is delimited from the template by a slash per default, which can be changed by setting the `delimiter` argument to something else:

```
loader = PrefixLoader({
    'app1':     PackageLoader('mypackage.app1'),
    'app2':     PackageLoader('mypackage.app2')
})
```

By loading `'app1/index.html'` the file from the app1 package is loaded, by loading `'app2/index.html'` the file from the second.

**Parameters:**

- **mapping** (*Mapping**[**str**,**BaseLoader**]*)
- **delimiter** (*str*)

***class*jinja2.ChoiceLoader(*loaders*)**

This loader works like the `PrefixLoader` just that no prefix is specified. If a template could not be found by one loader the next one is tried.

```
>>> loader = ChoiceLoader([
...     FileSystemLoader('/path/to/user/templates'),
...     FileSystemLoader('/path/to/system/templates')
... ])
```

This is useful if you want to allow users to override builtin templates from a different location.

**Parameters:**

**loaders** (*Sequence**[**BaseLoader**]*)

***class*jinja2.ModuleLoader(*path*)**

This loader loads templates from precompiled templates.

Example usage:

```
>>> loader = ModuleLoader('/path/to/compiled/templates')
```

Templates can be precompiled with `Environment.compile_templates()`.

**Parameters:**

**path** (*str**|**os.PathLike**[**str**]**|**Sequence**[**str**|**os.PathLike**[**str**]**]*)
