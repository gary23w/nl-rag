---
title: "typing (part 3/3)"
source: https://docs.python.org/3/library/typing.html
domain: python
license: PSF-2.0
tags: python, pytest, cpython, pip
fetched: 2026-07-02
part: 3/3
---

# typing

In code that needs to be compatible with Python 3.11 or older, generic Protocols can be written as follows:

```python3
T = TypeVar("T")

class GenProto(Protocol[T]):
    def meth(self) -> T:
        ...
```

Added in version 3.8.

**@typing.runtime_checkable**

Mark a protocol class as a runtime protocol.

Such a protocol can be used with `isinstance()` and `issubclass()`. This allows a simple-minded structural check, very similar to “one-trick ponies” in `collections.abc` such as `Iterable`. For example:

```python3
@runtime_checkable
class Closable(Protocol):
    def close(self): ...

assert isinstance(open('/some/file'), Closable)

@runtime_checkable
class Named(Protocol):
    name: str

import threading
assert isinstance(threading.Thread(name='Bob'), Named)
```

This decorator raises `TypeError` when applied to a non-protocol class.

Note

`runtime_checkable()` will check only the presence of the required methods or attributes, not their type signatures or types. For example, `ssl.SSLObject` is a class, therefore it passes an `issubclass()` check against Callable. However, the `ssl.SSLObject.__init__` method exists only to raise a `TypeError` with a more informative message, therefore making it impossible to call (instantiate) `ssl.SSLObject`.

Note

An `isinstance()` check against a runtime-checkable protocol can be surprisingly slow compared to an `isinstance()` check against a non-protocol class. Consider using alternative idioms such as `hasattr()` calls for structural checks in performance-sensitive code.

Added in version 3.8.

Changed in version 3.12: The internal implementation of `isinstance()` checks against runtime-checkable protocols now uses `inspect.getattr_static()` to look up attributes (previously, `hasattr()` was used). As a result, some objects which used to be considered instances of a runtime-checkable protocol may no longer be considered instances of that protocol on Python 3.12+, and vice versa. Most users are unlikely to be affected by this change.

Changed in version 3.12: The members of a runtime-checkable protocol are now considered “frozen” at runtime as soon as the class has been created. Monkey-patching attributes onto a runtime-checkable protocol will still work, but will have no impact on `isinstance()` checks comparing objects to the protocol. See What’s new in Python 3.12 for more details.

***class*typing.TypedDict(*dict*)**

Special construct to add type hints to a dictionary. At runtime “`TypedDict` instances” are simply `dicts`.

`TypedDict` declares a dictionary type that expects all of its instances to have a certain set of keys, where each key is associated with a value of a consistent type. This expectation is not checked at runtime but is only enforced by type checkers. Usage:

```python3
class Point2D(TypedDict):
    x: int
    y: int
    label: str

a: Point2D = {'x': 1, 'y': 2, 'label': 'good'}  # OK
b: Point2D = {'z': 3, 'label': 'bad'}           # Fails type check

assert Point2D(x=1, y=2, label='first') == dict(x=1, y=2, label='first')
```

An alternative way to create a `TypedDict` is by using function-call syntax. The second argument must be a literal `dict`:

```python3
Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': str})
```

This functional syntax allows defining keys which are not valid identifiers, for example because they are keywords or contain hyphens, or when key names must not be mangled like regular private names:

```python3
# raises SyntaxError
class Point2D(TypedDict):
    in: int  # 'in' is a keyword
    x-y: int  # name with hyphens

class Definition(TypedDict):
    __schema: str  # mangled to `_Definition__schema`

# OK, functional syntax
Point2D = TypedDict('Point2D', {'in': int, 'x-y': int})
Definition = TypedDict('Definition', {'__schema': str})  # not mangled
```

By default, all keys must be present in a `TypedDict`. It is possible to mark individual keys as non-required using `NotRequired`:

```python3
class Point2D(TypedDict):
    x: int
    y: int
    label: NotRequired[str]

# Alternative syntax
Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': NotRequired[str]})
```

This means that a `Point2D` `TypedDict` can have the `label` key omitted.

It is also possible to mark all keys as non-required by default by specifying a totality of `False`:

```python3
class Point2D(TypedDict, total=False):
    x: int
    y: int

# Alternative syntax
Point2D = TypedDict('Point2D', {'x': int, 'y': int}, total=False)
```

This means that a `Point2D` `TypedDict` can have any of the keys omitted. A type checker is only expected to support a literal `False` or `True` as the value of the `total` argument. `True` is the default, and makes all items defined in the class body required.

Individual keys of a `total=False` `TypedDict` can be marked as required using `Required`:

```python3
class Point2D(TypedDict, total=False):
    x: Required[int]
    y: Required[int]
    label: str

# Alternative syntax
Point2D = TypedDict('Point2D', {
    'x': Required[int],
    'y': Required[int],
    'label': str
}, total=False)
```

It is possible for a `TypedDict` type to inherit from one or more other `TypedDict` types using the class-based syntax. Usage:

```python3
class Point3D(Point2D):
    z: int
```

`Point3D` has three items: `x`, `y` and `z`. It is equivalent to this definition:

```python3
class Point3D(TypedDict):
    x: int
    y: int
    z: int
```

A `TypedDict` cannot inherit from a non-`TypedDict` class, except for `Generic`. For example:

```python3
class X(TypedDict):
    x: int

class Y(TypedDict):
    y: int

class Z(object): pass  # A non-TypedDict class

class XY(X, Y): pass  # OK

class XZ(X, Z): pass  # raises TypeError
```

A `TypedDict` can be generic:

```python3
class Group[T](TypedDict):
    key: T
    group: list[T]
```

To create a generic `TypedDict` that is compatible with Python 3.11 or lower, inherit from `Generic` explicitly:

```python
T = TypeVar("T")

class Group(TypedDict, Generic[T]):
    key: T
    group: list[T]
```

A `TypedDict` can be introspected via `annotationlib.get_annotations()` (see Annotations Best Practices for more information on annotations best practices) and the following attributes:

**__total__**

`Point2D.__total__` gives the value of the `total` argument. Example:

```pycon
>>> from typing import TypedDict
>>> class Point2D(TypedDict): pass
>>> Point2D.__total__
True
>>> class Point2D(TypedDict, total=False): pass
>>> Point2D.__total__
False
>>> class Point3D(Point2D): pass
>>> Point3D.__total__
True
```

This attribute reflects *only* the value of the `total` argument to the current `TypedDict` class, not whether the class is semantically total. For example, a `TypedDict` with `__total__` set to `True` may have keys marked with `NotRequired`, or it may inherit from another `TypedDict` with `total=False`. Therefore, it is generally better to use `__required_keys__` and `__optional_keys__` for introspection.

**__required_keys__**

Added in version 3.9.

**__optional_keys__**

`Point2D.__required_keys__` and `Point2D.__optional_keys__` return `frozenset` objects containing required and non-required keys, respectively.

Keys marked with `Required` will always appear in `__required_keys__` and keys marked with `NotRequired` will always appear in `__optional_keys__`.

For backwards compatibility with Python 3.10 and below, it is also possible to use inheritance to declare both required and non-required keys in the same `TypedDict`. This is done by declaring a `TypedDict` with one value for the `total` argument and then inheriting from it in another `TypedDict` with a different value for `total`:

```pycon
>>> class Point2D(TypedDict, total=False):
...     x: int
...     y: int
...
>>> class Point3D(Point2D):
...     z: int
...
>>> Point3D.__required_keys__ == frozenset({'z'})
True
>>> Point3D.__optional_keys__ == frozenset({'x', 'y'})
True
```

Added in version 3.9.

Note

If `from __future__ import annotations` is used or if annotations are given as strings, annotations are not evaluated when the `TypedDict` is defined. Therefore, the runtime introspection that `__required_keys__` and `__optional_keys__` rely on may not work properly, and the values of the attributes may be incorrect.

Support for `ReadOnly` is reflected in the following attributes:

**__readonly_keys__**

A `frozenset` containing the names of all read-only keys. Keys are read-only if they carry the `ReadOnly` qualifier.

Added in version 3.13.

**__mutable_keys__**

A `frozenset` containing the names of all mutable keys. Keys are mutable if they do not carry the `ReadOnly` qualifier.

Added in version 3.13.

See the TypedDict section in the typing documentation for more examples and detailed rules.

Added in version 3.8.

Changed in version 3.9: `TypedDict` is now a function rather than a class. It can still be used as a class base, as described above.

Changed in version 3.11: Added support for marking individual keys as `Required` or `NotRequired`. See **PEP 655**.

Changed in version 3.11: Added support for generic `TypedDict`s.

Changed in version 3.13: Removed support for the keyword-argument method of creating `TypedDict`s.

Changed in version 3.13: Support for the `ReadOnly` qualifier was added.

Deprecated since version 3.13, will be removed in version 3.15: When using the functional syntax to create a TypedDict class, failing to pass a value to the ‘fields’ parameter (`TD = TypedDict("TD")`) is deprecated. Passing `None` to the ‘fields’ parameter (`TD = TypedDict("TD", None)`) is also deprecated. Both will be disallowed in Python 3.15. To create a TypedDict class with 0 fields, use `class TD(TypedDict): pass` or `TD = TypedDict("TD", {})`.

### Protocols

The following protocols are provided by the `typing` module. All are decorated with `@runtime_checkable`.

***class*typing.SupportsAbs**

A protocol with one abstract method `__abs__` that is covariant in its return type.

***class*typing.SupportsBytes**

A protocol with one abstract method `__bytes__`.

***class*typing.SupportsComplex**

A protocol with one abstract method `__complex__`.

***class*typing.SupportsFloat**

A protocol with one abstract method `__float__`.

***class*typing.SupportsIndex**

A protocol with one abstract method `__index__`.

Added in version 3.8.

***class*typing.SupportsInt**

A protocol with one abstract method `__int__`.

***class*typing.SupportsRound**

A protocol with one abstract method `__round__` that is covariant in its return type.

### ABCs and Protocols for working with I/O

***class*typing.IO[*AnyStr*]**

***class*typing.TextIO**

***class*typing.BinaryIO**

Generic class `IO[AnyStr]` and its subclasses `TextIO(IO[str])` and `BinaryIO(IO[bytes])` represent the types of I/O streams such as returned by `open()`. Please note that these classes are not protocols, and their interface is fairly broad.

The protocols `io.Reader` and `io.Writer` offer a simpler alternative for argument types, when only the `read()` or `write()` methods are accessed, respectively:

```python3
def read_and_write(reader: Reader[str], writer: Writer[bytes]):
    data = reader.read()
    writer.write(data.encode())
```

Also consider using `collections.abc.Iterable` for iterating over the lines of an input stream:

```python3
def read_config(stream: Iterable[str]):
    for line in stream:
        ...
```

### Functions and decorators

**typing.cast(*typ*, *val*)**

Cast a value to a type.

This returns the value unchanged. To the type checker this signals that the return value has the designated type, but at runtime we intentionally don’t check anything (we want this to be as fast as possible).

**typing.assert_type(*val*, *typ*, */*)**

Ask a static type checker to confirm that *val* has an inferred type of *typ*.

At runtime this does nothing: it returns the first argument unchanged with no checks or side effects, no matter the actual type of the argument.

When a static type checker encounters a call to `assert_type()`, it emits an error if the value is not of the specified type:

```python3
def greet(name: str) -> None:
    assert_type(name, str)  # OK, inferred type of `name` is `str`
    assert_type(name, int)  # type checker error
```

This function is useful for ensuring the type checker’s understanding of a script is in line with the developer’s intentions:

```python3
def complex_function(arg: object):
    # Do some complex type-narrowing logic,
    # after which we hope the inferred type will be `int`
    ...
    # Test whether the type checker correctly understands our function
    assert_type(arg, int)
```

Added in version 3.11.

**typing.assert_never(*arg*, */*)**

Ask a static type checker to confirm that a line of code is unreachable.

Example:

```python3
def int_or_str(arg: int | str) -> None:
    match arg:
        case int():
            print("It's an int")
        case str():
            print("It's a str")
        case _ as unreachable:
            assert_never(unreachable)
```

Here, the annotations allow the type checker to infer that the last case can never execute, because `arg` is either an `int` or a `str`, and both options are covered by earlier cases.

If a type checker finds that a call to `assert_never()` is reachable, it will emit an error. For example, if the type annotation for `arg` was instead `int | str | float`, the type checker would emit an error pointing out that `unreachable` is of type `float`. For a call to `assert_never` to pass type checking, the inferred type of the argument passed in must be the bottom type, `Never`, and nothing else.

At runtime, this throws an exception when called.

See also

Unreachable Code and Exhaustiveness Checking has more information about exhaustiveness checking with static typing.

Added in version 3.11.

**typing.reveal_type(*obj*, */*)**

Ask a static type checker to reveal the inferred type of an expression.

When a static type checker encounters a call to this function, it emits a diagnostic with the inferred type of the argument. For example:

```python3
x: int = 1
reveal_type(x)  # Revealed type is "builtins.int"
```

This can be useful when you want to debug how your type checker handles a particular piece of code.

At runtime, this function prints the runtime type of its argument to `sys.stderr` and returns the argument unchanged (allowing the call to be used within an expression):

```python3
x = reveal_type(1)  # prints "Runtime type is int"
print(x)  # prints "1"
```

Note that the runtime type may be different from (more or less specific than) the type statically inferred by a type checker.

Most type checkers support `reveal_type()` anywhere, even if the name is not imported from `typing`. Importing the name from `typing`, however, allows your code to run without runtime errors and communicates intent more clearly.

Added in version 3.11.

**@typing.dataclass_transform(***, *eq_default=True*, *order_default=False*, *kw_only_default=False*, *frozen_default=False*, *field_specifiers=()*, ***kwargs*)**

Decorator to mark an object as providing `dataclass`-like behavior.

`dataclass_transform` may be used to decorate a class, metaclass, or a function that is itself a decorator. The presence of `@dataclass_transform()` tells a static type checker that the decorated object performs runtime “magic” that transforms a class in a similar way to `@dataclasses.dataclass`.

Example usage with a decorator function:

```python
@dataclass_transform()
def create_model[T](cls: type[T]) -> type[T]:
    ...
    return cls

@create_model
class CustomerModel:
    id: int
    name: str
```

On a base class:

```python3
@dataclass_transform()
class ModelBase: ...

class CustomerModel(ModelBase):
    id: int
    name: str
```

On a metaclass:

```python3
@dataclass_transform()
class ModelMeta(type): ...

class ModelBase(metaclass=ModelMeta): ...

class CustomerModel(ModelBase):
    id: int
    name: str
```

The `CustomerModel` classes defined above will be treated by type checkers similarly to classes created with `@dataclasses.dataclass`. For example, type checkers will assume these classes have `__init__` methods that accept `id` and `name`.

The decorated class, metaclass, or function may accept the following bool arguments which type checkers will assume have the same effect as they would have on the `@dataclasses.dataclass` decorator: `init`, `eq`, `order`, `unsafe_hash`, `frozen`, `match_args`, `kw_only`, and `slots`. It must be possible for the value of these arguments (`True` or `False`) to be statically evaluated.

The arguments to the `dataclass_transform` decorator can be used to customize the default behaviors of the decorated class, metaclass, or function:

**Parameters:**

- **eq_default** (*bool*) – Indicates whether the `eq` parameter is assumed to be `True` or `False` if it is omitted by the caller. Defaults to `True`.
- **order_default** (*bool*) – Indicates whether the `order` parameter is assumed to be `True` or `False` if it is omitted by the caller. Defaults to `False`.
- **kw_only_default** (*bool*) – Indicates whether the `kw_only` parameter is assumed to be `True` or `False` if it is omitted by the caller. Defaults to `False`.
- **frozen_default** (*bool*) – Indicates whether the `frozen` parameter is assumed to be `True` or `False` if it is omitted by the caller. Defaults to `False`. Added in version 3.12.
- **field_specifiers** (*tuple**[**Callable**[**...**,**Any**]**,**...**]*) – Specifies a static list of supported classes or functions that describe fields, similar to `dataclasses.field()`. Defaults to `()`.
- ****kwargs** (*Any*) – Arbitrary other keyword arguments are accepted in order to allow for possible future extensions.

Type checkers recognize the following optional parameters on field specifiers:

| Parameter name | Description |
|---|---|
| `init` | Indicates whether the field should be included in the synthesized `__init__` method. If unspecified, `init` defaults to `True`. |
| `default` | Provides the default value for the field. |
| `default_factory` | Provides a runtime callback that returns the default value for the field. If neither `default` nor `default_factory` are specified, the field is assumed to have no default value and must be provided a value when the class is instantiated. |
| `factory` | An alias for the `default_factory` parameter on field specifiers. |
| `kw_only` | Indicates whether the field should be marked as keyword-only. If `True`, the field will be keyword-only. If `False`, it will not be keyword-only. If unspecified, the value of the `kw_only` parameter on the object decorated with `dataclass_transform` will be used, or if that is unspecified, the value of `kw_only_default` on `dataclass_transform` will be used. |
| `alias` | Provides an alternative name for the field. This alternative name is used in the synthesized `__init__` method. |

At runtime, this decorator records its arguments in the `__dataclass_transform__` attribute on the decorated object. It has no other runtime effect.

See **PEP 681** for more details.

Added in version 3.11.

**@typing.overload**

Decorator for creating overloaded functions and methods.

The `@overload` decorator allows describing functions and methods that support multiple different combinations of argument types. A series of `@overload`-decorated definitions must be followed by exactly one non-`@overload`-decorated definition (for the same function/method).

`@overload`-decorated definitions are for the benefit of the type checker only, since they will be overwritten by the non-`@overload`-decorated definition. The non-`@overload`-decorated definition, meanwhile, will be used at runtime but should be ignored by a type checker. At runtime, calling an `@overload`-decorated function directly will raise `NotImplementedError`.

An example of overload that gives a more precise type than can be expressed using a union or a type variable:

```python
@overload
def process(response: None) -> None:
    ...
@overload
def process(response: int) -> tuple[int, str]:
    ...
@overload
def process(response: bytes) -> str:
    ...
def process(response):
    ...  # actual implementation goes here
```

See **PEP 484** for more details and comparison with other typing semantics.

Changed in version 3.11: Overloaded functions can now be introspected at runtime using `get_overloads()`.

**typing.get_overloads(*func*)**

Return a sequence of `@overload`-decorated definitions for *func*.

*func* is the function object for the implementation of the overloaded function. For example, given the definition of `process` in the documentation for `@overload`, `get_overloads(process)` will return a sequence of three function objects for the three defined overloads. If called on a function with no overloads, `get_overloads()` returns an empty sequence.

`get_overloads()` can be used for introspecting an overloaded function at runtime.

Added in version 3.11.

**typing.clear_overloads()**

Clear all registered overloads in the internal registry.

This can be used to reclaim the memory used by the registry.

Added in version 3.11.

**@typing.final**

Decorator to indicate final methods and final classes.

Decorating a method with `@final` indicates to a type checker that the method cannot be overridden in a subclass. Decorating a class with `@final` indicates that it cannot be subclassed.

For example:

```python3
class Base:
    @final
    def done(self) -> None:
        ...
class Sub(Base):
    def done(self) -> None:  # Error reported by type checker
        ...

@final
class Leaf:
    ...
class Other(Leaf):  # Error reported by type checker
    ...
```

There is no runtime checking of these properties. See **PEP 591** for more details.

Added in version 3.8.

Changed in version 3.11: The decorator will now attempt to set a `__final__` attribute to `True` on the decorated object. Thus, a check like `if getattr(obj, "__final__", False)` can be used at runtime to determine whether an object `obj` has been marked as final. If the decorated object does not support setting attributes, the decorator returns the object unchanged without raising an exception.

**@typing.no_type_check**

Decorator to indicate that annotations are not type hints.

This works as a class or function decorator. With a class, it applies recursively to all methods and classes defined in that class (but not to methods defined in its superclasses or subclasses). Type checkers will ignore all annotations in a function or class with this decorator.

`@no_type_check` mutates the decorated object in place.

**@typing.no_type_check_decorator**

Decorator to give another decorator the `no_type_check()` effect.

This wraps the decorator with something that wraps the decorated function in `no_type_check()`.

Deprecated since version 3.13, will be removed in version 3.15: No type checker ever added support for `@no_type_check_decorator`. It is therefore deprecated, and will be removed in Python 3.15.

**@typing.override**

Decorator to indicate that a method in a subclass is intended to override a method or attribute in a superclass.

Type checkers should emit an error if a method decorated with `@override` does not, in fact, override anything. This helps prevent bugs that may occur when a base class is changed without an equivalent change to a child class.

For example:

```python
class Base:
    def log_status(self) -> None:
        ...

class Sub(Base):
    @override
    def log_status(self) -> None:  # Okay: overrides Base.log_status
        ...

    @override
    def done(self) -> None:  # Error reported by type checker
        ...
```

There is no runtime checking of this property.

The decorator will attempt to set an `__override__` attribute to `True` on the decorated object. Thus, a check like `if getattr(obj, "__override__", False)` can be used at runtime to determine whether an object `obj` has been marked as an override. If the decorated object does not support setting attributes, the decorator returns the object unchanged without raising an exception.

See **PEP 698** for more details.

Added in version 3.12.

**@typing.type_check_only**

Decorator to mark a class or function as unavailable at runtime.

This decorator is itself not available at runtime. It is mainly intended to mark classes that are defined in type stub files if an implementation returns an instance of a private class:

```python3
@type_check_only
class Response:  # private or not available at runtime
    code: int
    def get_header(self, name: str) -> str: ...

def fetch_response() -> Response: ...
```

Note that returning instances of private classes is not recommended. It is usually preferable to make such classes public.

### Introspection helpers

**typing.get_type_hints(*obj*, *globalns=None*, *localns=None*, *include_extras=False*, ***, *format=Format.VALUE*)**

Return a dictionary containing type hints for a function, method, module, class object, or other callable object.

This is often the same as `annotationlib.get_annotations()`, but this function makes the following changes to the annotations dictionary:

- Forward references encoded as string literals or `ForwardRef` objects are handled by evaluating them in *globalns*, *localns*, and (where applicable) *obj*’s type parameter namespace. If *globalns* or *localns* is not given, appropriate namespace dictionaries are inferred from *obj*.
- `None` is replaced with `types.NoneType`.
- If `@no_type_check` has been applied to *obj*, an empty dictionary is returned.
- If *obj* is a class `C`, the function returns a dictionary that merges annotations from `C`’s base classes with those on `C` directly. This is done by traversing `C.__mro__` and iteratively combining annotations of each base class. Annotations on classes appearing earlier in the method resolution order always take precedence over annotations on classes appearing later in the method resolution order.
- The function recursively replaces all occurrences of `Annotated[T, ...]`, `Required[T]`, `NotRequired[T]`, and `ReadOnly[T]` with `T`, unless *include_extras* is set to `True` (see `Annotated` for more information).

Caution

This function may execute arbitrary code contained in annotations. See Security implications of introspecting annotations for more information.

Note

If `Format.VALUE` is used and any forward references in the annotations of *obj* are not resolvable, a `NameError` exception is raised. For example, this can happen with names imported under `if TYPE_CHECKING`. More generally, any kind of exception can be raised if an annotation contains invalid Python code.

Note

Calling `get_type_hints()` on an instance is not supported. To retrieve annotations for an instance, call `get_type_hints()` on the instance’s class instead (for example, `get_type_hints(type(obj))`).

Changed in version 3.9: Added `include_extras` parameter as part of **PEP 593**. See the documentation on `Annotated` for more information.

Changed in version 3.11: Previously, `Optional[t]` was added for function and method annotations if a default value equal to `None` was set. Now the annotation is returned unchanged.

Changed in version 3.14: Added the `format` parameter. See the documentation on `annotationlib.get_annotations()` for more information.

Changed in version 3.14: Calling `get_type_hints()` on instances is no longer supported. Some instances were accepted in earlier versions as an undocumented implementation detail.

**typing.get_origin(*tp*)**

Get the unsubscripted version of a type: for a typing object of the form `X[Y, Z, ...]` return `X`.

If `X` is a typing-module alias for a builtin or `collections` class, it will be normalized to the original class. If `X` is an instance of `ParamSpecArgs` or `ParamSpecKwargs`, return the underlying `ParamSpec`. Return `None` for unsupported objects.

Examples:

```python
assert get_origin(str) is None
assert get_origin(Dict[str, int]) is dict
assert get_origin(Union[int, str]) is Union
assert get_origin(Annotated[str, "metadata"]) is Annotated
P = ParamSpec('P')
assert get_origin(P.args) is P
assert get_origin(P.kwargs) is P
```

Added in version 3.8.

**typing.get_args(*tp*)**

Get type arguments with all substitutions performed: for a typing object of the form `X[Y, Z, ...]` return `(Y, Z, ...)`.

If `X` is a union or `Literal` contained in another generic type, the order of `(Y, Z, ...)` may be different from the order of the original arguments `[Y, Z, ...]` due to type caching. Return `()` for unsupported objects.

Examples:

```python
assert get_args(int) == ()
assert get_args(Dict[int, str]) == (int, str)
assert get_args(Union[int, str]) == (int, str)
```

Added in version 3.8.

**typing.get_protocol_members(*tp*)**

Return the set of members defined in a `Protocol`.

```pycon
>>> from typing import Protocol, get_protocol_members
>>> class P(Protocol):
...     def a(self) -> str: ...
...     b: int
>>> get_protocol_members(P) == frozenset({'a', 'b'})
True
```

Raise `TypeError` for arguments that are not Protocols.

Added in version 3.13.

**typing.is_protocol(*tp*)**

Determine if a type is a `Protocol`.

For example:

```python
class P(Protocol):
    def a(self) -> str: ...
    b: int

assert is_protocol(P)
assert not is_protocol(int)
```

This function only returns true for `Protocol` classes, not for generic aliases of them:

```python
class GenericP[T](Protocol):
    def a(self) -> T: ...
    b: int

assert not is_protocol(GenericP[int])
```

Added in version 3.13.

**typing.is_typeddict(*tp*)**

Check if a type is a `TypedDict`.

For example:

```python
class Film(TypedDict):
    title: str
    year: int

assert is_typeddict(Film)
assert not is_typeddict(list | str)

# TypedDict is a factory for creating typed dicts,
# not a typed dict itself
assert not is_typeddict(TypedDict)
```

This function only returns true for `TypedDict` classes, not for generic aliases of them:

```python
class GenericFilm[T](TypedDict):
    title: str
    year: T

assert not is_typeddict(GenericFilm[int])
```

Added in version 3.10.

***class*typing.ForwardRef**

Class used for internal typing representation of string forward references.

For example, `List["SomeClass"]` is implicitly transformed into `List[ForwardRef("SomeClass")]`. `ForwardRef` should not be instantiated by a user, but may be used by introspection tools.

Note

**PEP 585** generic types such as `list["SomeClass"]` will not be implicitly transformed into `list[ForwardRef("SomeClass")]` and thus will not automatically resolve to `list[SomeClass]`.

Added in version 3.7.4.

Changed in version 3.14: This is now an alias for `annotationlib.ForwardRef`. Several undocumented behaviors of this class have been changed; for example, after a `ForwardRef` has been evaluated, the evaluated value is no longer cached.

**typing.evaluate_forward_ref(*forward_ref*, ***, *owner=None*, *globals=None*, *locals=None*, *type_params=None*, *format=annotationlib.Format.VALUE*)**

Evaluate an `annotationlib.ForwardRef` as a type hint.

This is similar to calling `annotationlib.ForwardRef.evaluate()`, but unlike that method, `evaluate_forward_ref()` also recursively evaluates forward references nested within the type hint.

See the documentation for `annotationlib.ForwardRef.evaluate()` for the meaning of the *owner*, *globals*, *locals*, *type_params*, and *format* parameters.

Caution

This function may execute arbitrary code contained in annotations. See Security implications of introspecting annotations for more information.

Added in version 3.14.

**typing.NoDefault**

A sentinel object used to indicate that a type parameter has no default value. For example:

```pycon
>>> T = TypeVar("T")
>>> T.__default__ is typing.NoDefault
True
>>> S = TypeVar("S", default=None)
>>> S.__default__ is None
True
```

Added in version 3.13.

### Constant

**typing.TYPE_CHECKING**

A special constant that is assumed to be `True` by static type checkers. It’s `False` at runtime.

A module which is expensive to import, and which only contain types used for typing annotations, can be safely imported inside an `if TYPE_CHECKING:` block. This prevents the module from actually being imported at runtime; annotations aren’t eagerly evaluated (see **PEP 649**) so using undefined symbols in annotations is harmless–as long as you don’t later examine them. Your static type analysis tool will set `TYPE_CHECKING` to `True` during static type analysis, which means the module will be imported and the types will be checked properly during such analysis.

Usage:

```python3
if TYPE_CHECKING:
    import expensive_mod

def fun(arg: expensive_mod.SomeType) -> None:
    local_var: expensive_mod.AnotherType = other_fun()
```

If you occasionally need to examine type annotations at runtime which may contain undefined symbols, use `annotationlib.get_annotations()` with a `format` parameter of `annotationlib.Format.STRING` or `annotationlib.Format.FORWARDREF` to safely retrieve the annotations without raising `NameError`.

Added in version 3.5.2.

### Deprecated aliases

This module defines several deprecated aliases to pre-existing standard library classes. These were originally included in the `typing` module in order to support parameterizing these generic classes using `[]`. However, the aliases became redundant in Python 3.9 when the corresponding pre-existing classes were enhanced to support `[]` (see **PEP 585**).

The redundant types are deprecated as of Python 3.9. However, while the aliases may be removed at some point, removal of these aliases is not currently planned. As such, no deprecation warnings are currently issued by the interpreter for these aliases.

If at some point it is decided to remove these deprecated aliases, a deprecation warning will be issued by the interpreter for at least two releases prior to removal. The aliases are guaranteed to remain in the `typing` module without deprecation warnings until at least Python 3.14.

Type checkers are encouraged to flag uses of the deprecated types if the program they are checking targets a minimum Python version of 3.9 or newer.

#### Aliases to built-in types

***class*typing.Dict(*dict, MutableMapping[KT, VT]*)**

Deprecated alias to `dict`.

Note that to annotate arguments, it is preferred to use an abstract collection type such as `Mapping` rather than to use `dict` or `typing.Dict`.

Deprecated since version 3.9: `builtins.dict` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.List(*list, MutableSequence[T]*)**

Deprecated alias to `list`.

Note that to annotate arguments, it is preferred to use an abstract collection type such as `Sequence` or `Iterable` rather than to use `list` or `typing.List`.

Deprecated since version 3.9: `builtins.list` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.Set(*set, MutableSet[T]*)**

Deprecated alias to `builtins.set`.

Note that to annotate arguments, it is preferred to use an abstract collection type such as `collections.abc.Set` rather than to use `set` or `typing.Set`.

Deprecated since version 3.9: `builtins.set` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.FrozenSet(*frozenset, AbstractSet[T_co]*)**

Deprecated alias to `builtins.frozenset`.

Deprecated since version 3.9: `builtins.frozenset` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

**typing.Tuple**

Deprecated alias for `tuple`.

`tuple` and `Tuple` are special-cased in the type system; see Annotating tuples for more details.

Deprecated since version 3.9: `builtins.tuple` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.Type(*Generic[CT_co]*)**

Deprecated alias to `type`.

See The type of class objects for details on using `type` or `typing.Type` in type annotations.

Added in version 3.5.2.

Deprecated since version 3.9: `builtins.type` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

#### Aliases to types in `collections`

***class*typing.DefaultDict(*collections.defaultdict, MutableMapping[KT, VT]*)**

Deprecated alias to `collections.defaultdict`.

Added in version 3.5.2.

Deprecated since version 3.9: `collections.defaultdict` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.OrderedDict(*collections.OrderedDict, MutableMapping[KT, VT]*)**

Deprecated alias to `collections.OrderedDict`.

Added in version 3.7.2.

Deprecated since version 3.9: `collections.OrderedDict` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.ChainMap(*collections.ChainMap, MutableMapping[KT, VT]*)**

Deprecated alias to `collections.ChainMap`.

Added in version 3.6.1.

Deprecated since version 3.9: `collections.ChainMap` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.Counter(*collections.Counter, Dict[T, int]*)**

Deprecated alias to `collections.Counter`.

Added in version 3.6.1.

Deprecated since version 3.9: `collections.Counter` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.Deque(*deque, MutableSequence[T]*)**

Deprecated alias to `collections.deque`.

Added in version 3.6.1.

Deprecated since version 3.9: `collections.deque` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

#### Aliases to other concrete types

***class*typing.Pattern**

***class*typing.Match**

Deprecated aliases corresponding to the return types from `re.compile()` and `re.match()`.

These types (and the corresponding functions) are generic over `AnyStr`. `Pattern` can be specialised as `Pattern[str]` or `Pattern[bytes]`; `Match` can be specialised as `Match[str]` or `Match[bytes]`.

Deprecated since version 3.9: Classes `Pattern` and `Match` from `re` now support `[]`. See **PEP 585** and Generic Alias Type.

***class*typing.Text**

Deprecated alias for `str`.

`Text` is provided to supply a forward compatible path for Python 2 code: in Python 2, `Text` is an alias for `unicode`.

Use `Text` to indicate that a value must contain a unicode string in a manner that is compatible with both Python 2 and Python 3:

```python3
def add_unicode_checkmark(text: Text) -> Text:
    return text + u' \u2713'
```

Added in version 3.5.2.

Deprecated since version 3.11: Python 2 is no longer supported, and most type checkers also no longer support type checking Python 2 code. Removal of the alias is not currently planned, but users are encouraged to use `str` instead of `Text`.

#### Aliases to container ABCs in `collections.abc`

***class*typing.AbstractSet(*Collection[T_co]*)**

Deprecated alias to `collections.abc.Set`.

Deprecated since version 3.9: `collections.abc.Set` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.ByteString(*Sequence[int]*)**

Deprecated alias to `collections.abc.ByteString`.

Use `isinstance(obj, collections.abc.Buffer)` to test if `obj` implements the buffer protocol at runtime. For use in type annotations, either use `Buffer` or a union that explicitly specifies the types your code supports (e.g., `bytes | bytearray | memoryview`).

`ByteString` was originally intended to be an abstract class that would serve as a supertype of both `bytes` and `bytearray`. However, since the ABC never had any methods, knowing that an object was an instance of `ByteString` never actually told you anything useful about the object. Other common buffer types such as `memoryview` were also never understood as subtypes of `ByteString` (either at runtime or by static type checkers).

See **PEP 688** for more details.

Deprecated since version 3.9, will be removed in version 3.17.

***class*typing.Collection(*Sized, Iterable[T_co], Container[T_co]*)**

Deprecated alias to `collections.abc.Collection`.

Added in version 3.6.

Deprecated since version 3.9: `collections.abc.Collection` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.Container(*Generic[T_co]*)**

Deprecated alias to `collections.abc.Container`.

Deprecated since version 3.9: `collections.abc.Container` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.ItemsView(*MappingView, AbstractSet[tuple[KT_co, VT_co]]*)**

Deprecated alias to `collections.abc.ItemsView`.

Deprecated since version 3.9: `collections.abc.ItemsView` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.KeysView(*MappingView, AbstractSet[KT_co]*)**

Deprecated alias to `collections.abc.KeysView`.

Deprecated since version 3.9: `collections.abc.KeysView` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.Mapping(*Collection[KT], Generic[KT, VT_co]*)**

Deprecated alias to `collections.abc.Mapping`.

Deprecated since version 3.9: `collections.abc.Mapping` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.MappingView(*Sized*)**

Deprecated alias to `collections.abc.MappingView`.

Deprecated since version 3.9: `collections.abc.MappingView` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.MutableMapping(*Mapping[KT, VT]*)**

Deprecated alias to `collections.abc.MutableMapping`.

Deprecated since version 3.9: `collections.abc.MutableMapping` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.MutableSequence(*Sequence[T]*)**

Deprecated alias to `collections.abc.MutableSequence`.

Deprecated since version 3.9: `collections.abc.MutableSequence` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.MutableSet(*AbstractSet[T]*)**

Deprecated alias to `collections.abc.MutableSet`.

Deprecated since version 3.9: `collections.abc.MutableSet` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.Sequence(*Reversible[T_co], Collection[T_co]*)**

Deprecated alias to `collections.abc.Sequence`.

Deprecated since version 3.9: `collections.abc.Sequence` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.ValuesView(*MappingView, Collection[_VT_co]*)**

Deprecated alias to `collections.abc.ValuesView`.

Deprecated since version 3.9: `collections.abc.ValuesView` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

#### Aliases to asynchronous ABCs in `collections.abc`

***class*typing.Coroutine(*Awaitable[ReturnType], Generic[YieldType, SendType, ReturnType]*)**

Deprecated alias to `collections.abc.Coroutine`.

See Annotating generators and coroutines for details on using `collections.abc.Coroutine` and `typing.Coroutine` in type annotations.

Added in version 3.5.3.

Deprecated since version 3.9: `collections.abc.Coroutine` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.AsyncGenerator(*AsyncIterator[YieldType], Generic[YieldType, SendType]*)**

Deprecated alias to `collections.abc.AsyncGenerator`.

See Annotating generators and coroutines for details on using `collections.abc.AsyncGenerator` and `typing.AsyncGenerator` in type annotations.

Added in version 3.6.1.

Deprecated since version 3.9: `collections.abc.AsyncGenerator` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

Changed in version 3.13: The `SendType` parameter now has a default.

***class*typing.AsyncIterable(*Generic[T_co]*)**

Deprecated alias to `collections.abc.AsyncIterable`.

Added in version 3.5.2.

Deprecated since version 3.9: `collections.abc.AsyncIterable` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.AsyncIterator(*AsyncIterable[T_co]*)**

Deprecated alias to `collections.abc.AsyncIterator`.

Added in version 3.5.2.

Deprecated since version 3.9: `collections.abc.AsyncIterator` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.Awaitable(*Generic[T_co]*)**

Deprecated alias to `collections.abc.Awaitable`.

Added in version 3.5.2.

Deprecated since version 3.9: `collections.abc.Awaitable` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

#### Aliases to other ABCs in `collections.abc`

***class*typing.Iterable(*Generic[T_co]*)**

Deprecated alias to `collections.abc.Iterable`.

Deprecated since version 3.9: `collections.abc.Iterable` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.Iterator(*Iterable[T_co]*)**

Deprecated alias to `collections.abc.Iterator`.

Deprecated since version 3.9: `collections.abc.Iterator` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

**typing.Callable**

Deprecated alias to `collections.abc.Callable`.

See Annotating callable objects for details on how to use `collections.abc.Callable` and `typing.Callable` in type annotations.

Deprecated since version 3.9: `collections.abc.Callable` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

Changed in version 3.10: `Callable` now supports `ParamSpec` and `Concatenate`. See **PEP 612** for more details.

***class*typing.Generator(*Iterator[YieldType], Generic[YieldType, SendType, ReturnType]*)**

Deprecated alias to `collections.abc.Generator`.

See Annotating generators and coroutines for details on using `collections.abc.Generator` and `typing.Generator` in type annotations.

Deprecated since version 3.9: `collections.abc.Generator` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

Changed in version 3.13: Default values for the send and return types were added.

***class*typing.Hashable**

Deprecated alias to `collections.abc.Hashable`.

Deprecated since version 3.12: Use `collections.abc.Hashable` directly instead.

***class*typing.Reversible(*Iterable[T_co]*)**

Deprecated alias to `collections.abc.Reversible`.

Deprecated since version 3.9: `collections.abc.Reversible` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

***class*typing.Sized**

Deprecated alias to `collections.abc.Sized`.

Deprecated since version 3.12: Use `collections.abc.Sized` directly instead.

#### Aliases to `contextlib` ABCs

***class*typing.ContextManager(*Generic[T_co, ExitT_co]*)**

Deprecated alias to `contextlib.AbstractContextManager`.

The first type parameter, `T_co`, represents the type returned by the `__enter__()` method. The optional second type parameter, `ExitT_co`, which defaults to `bool | None`, represents the type returned by the `__exit__()` method.

Added in version 3.5.4.

Deprecated since version 3.9: `contextlib.AbstractContextManager` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

Changed in version 3.13: Added the optional second type parameter, `ExitT_co`.

***class*typing.AsyncContextManager(*Generic[T_co, AExitT_co]*)**

Deprecated alias to `contextlib.AbstractAsyncContextManager`.

The first type parameter, `T_co`, represents the type returned by the `__aenter__()` method. The optional second type parameter, `AExitT_co`, which defaults to `bool | None`, represents the type returned by the `__aexit__()` method.

Added in version 3.6.2.

Deprecated since version 3.9: `contextlib.AbstractAsyncContextManager` now supports subscripting (`[]`). See **PEP 585** and Generic Alias Type.

Changed in version 3.13: Added the optional second type parameter, `AExitT_co`.

## Deprecation Timeline of Major Features

Certain features in `typing` are deprecated and may be removed in a future version of Python. The following table summarizes major deprecations for your convenience. This is subject to change, and not all deprecations are listed.

| Feature | Deprecated in | Projected removal | PEP/issue |
|---|---|---|---|
| `typing` versions of standard collections | 3.9 | Undecided (see Deprecated aliases for more information) | **PEP 585** |
| `typing.ByteString` | 3.9 | 3.17 | gh-91896 |
| `typing.Text` | 3.11 | Undecided | gh-92332 |
| `typing.Hashable` and `typing.Sized` | 3.12 | Undecided | gh-94309 |
| `typing.TypeAlias` | 3.12 | Undecided | **PEP 695** |
| `@typing.no_type_check_decorator` | 3.13 | 3.15 | gh-106309 |
| `typing.AnyStr` | 3.13 | 3.18 | gh-105578 |
