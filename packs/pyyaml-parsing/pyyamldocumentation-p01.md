---
title: "PyYAML Documentation (part 1/2)"
source: https://pyyaml.org/wiki/PyYAMLDocumentation
domain: pyyaml-parsing
license: CC-BY-SA-4.0
tags: python pyyaml, pyyaml parsing, yaml config python
fetched: 2026-07-02
part: 1/2
---

# PyYAML Documentation

PyYAML is a YAML parser and emitter for Python.


## Installation

Simple install:

```
pip install pyyaml
```

To install from source, download the source package *PyYAML-5.1.tar.gz* and unpack it. Go to the directory *PyYAML-5.1* and run:

```
$ python setup.py install
```

If you want to use LibYAML bindings, which are much faster than the pure Python version, you need to download and install LibYAML. Then you may build and install the bindings by executing

```
$ python setup.py --with-libyaml install
```

In order to use LibYAML based parser and emitter, use the classes `CParser` and `CEmitter`. For instance,

```
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# ...

data = load(stream, Loader=Loader)

# ...

output = dump(data, Dumper=Dumper)
```

Note that there are some subtle (but not really significant) differences between pure Python and LibYAML based parsers and emitters.


## Frequently Asked Questions

### Dictionaries without nested collections are not dumped correctly

*Why does*

```
import yaml
document = """
  a: 1
  b:
    c: 3
    d: 4
"""
print yaml.dump(yaml.load(document))
```

*give*

```
a: 1
b: {c: 3, d: 4}
```

*(see #18, #24)?*

It’s a correct output despite the fact that the style of the nested mapping is different.

By default, PyYAML chooses the style of a collection depending on whether it has nested collections. If a collection has nested collections, it will be assigned the block style. Otherwise it will have the flow style.

If you want collections to be always serialized in the block style, set the parameter `default_flow_style` of `dump()` to `False`. For instance,

```
>>> print yaml.dump(yaml.load(document), default_flow_style=False)
a: 1
b:
  c: 3
  d: 4
```


## Python 3 support

Starting from the *3.08* release, PyYAML and LibYAML bindings provide a complete support for Python 3. This is a short outline of differences in PyYAML API between Python 2 and Python 3 versions.

*In Python 2:*

- `str` objects are converted into `!!str`, `!!python/str` or `!binary` nodes depending on whether the object is an ASCII, UTF-8 or binary string.
- `unicode` objects are converted into `!!python/unicode` or `!!str` nodes depending on whether the object is an ASCII string or not.
- `yaml.dump(data)` produces the document as a UTF-8 encoded `str` object.
- `yaml.dump(data, encoding=('utf-8'|'utf-16-be'|'utf-16-le'))` produces a `str` object in the specified encoding.
- `yaml.dump(data, encoding=None)` produces a `unicode` object.

*In Python 3:*

- `str` objects are converted to `!!str` nodes.
- `bytes` objects are converted to `!!binary` nodes.
- For compatibility reasons, `!!python/str` and `!python/unicode` tags are still supported and the corresponding nodes are converted to `str` objects.
- `yaml.dump(data)` produces the document as a `str` object.
- `yaml.dump(data, encoding=('utf-8'|'utf-16-be'|'utf-16-le'))` produces a `bytes` object in the specified encoding.


## Tutorial

Start with importing the `yaml` package.

```
>>> import yaml
```

### Loading YAML

**Warning: It is not safe to call `yaml.load` with any data received from an untrusted source! `yaml.load` is as powerful as `pickle.load` and so may call any Python function.** Check the `yaml.safe_load` function though.

The function `yaml.load` converts a YAML document to a Python object.

```
>>> yaml.load("""
... - Hesperiidae
... - Papilionidae
... - Apatelodidae
... - Epiplemidae
... """)

['Hesperiidae', 'Papilionidae', 'Apatelodidae', 'Epiplemidae']
```

`yaml.load` accepts a byte string, a Unicode string, an open binary file object, or an open text file object. A byte string or a file must be encoded with *utf-8*, *utf-16-be* or *utf-16-le* encoding. `yaml.load` detects the encoding by checking the *BOM* (byte order mark) sequence at the beginning of the string/file. If no *BOM* is present, the *utf-8* encoding is assumed.

`yaml.load` returns a Python object.

```
>>> yaml.load(u"""
... hello: Привет!
... """)    # In Python 3, do not use the 'u' prefix

{'hello': u'\u041f\u0440\u0438\u0432\u0435\u0442!'}

>>> stream = file('document.yaml', 'r')    # 'document.yaml' contains a single YAML document.
>>> yaml.load(stream)
[...]    # A Python object corresponding to the document.
```

If a string or a file contains several documents, you may load them all with the `yaml.load_all` function.

```
>>> documents = """
... ---
... name: The Set of Gauntlets 'Pauraegen'
... description: >
...     A set of handgear with sparks that crackle
...     across its knuckleguards.
... ---
... name: The Set of Gauntlets 'Paurnen'
... description: >
...   A set of gauntlets that gives off a foul,
...   acrid odour yet remains untarnished.
... ---
... name: The Set of Gauntlets 'Paurnimmen'
... description: >
...   A set of handgear, freezing with unnatural cold.
... """

>>> for data in yaml.load_all(documents):
...     print data

{'description': 'A set of handgear with sparks that crackle across its knuckleguards.\n',
'name': "The Set of Gauntlets 'Pauraegen'"}
{'description': 'A set of gauntlets that gives off a foul, acrid odour yet remains untarnished.\n',
'name': "The Set of Gauntlets 'Paurnen'"}
{'description': 'A set of handgear, freezing with unnatural cold.\n',
'name': "The Set of Gauntlets 'Paurnimmen'"}
```

PyYAML allows you to construct a Python object of any type.

```
>>> yaml.load("""
... none: [~, null]
... bool: [true, false, on, off]
... int: 42
... float: 3.14159
... list: [LITE, RES_ACID, SUS_DEXT]
... dict: {hp: 13, sp: 5}
... """)

{'none': [None, None], 'int': 42, 'float': 3.1415899999999999,
'list': ['LITE', 'RES_ACID', 'SUS_DEXT'], 'dict': {'hp': 13, 'sp': 5},
'bool': [True, False, True, False]}
```

Even instances of Python classes can be constructed using the `!!python/object` tag.

```
>>> class Hero:
...     def __init__(self, name, hp, sp):
...         self.name = name
...         self.hp = hp
...         self.sp = sp
...     def __repr__(self):
...         return "%s(name=%r, hp=%r, sp=%r)" % (
...             self.__class__.__name__, self.name, self.hp, self.sp)

>>> yaml.load("""
... !!python/object:__main__.Hero
... name: Welthyr Syxgon
... hp: 1200
... sp: 0
... """)

Hero(name='Welthyr Syxgon', hp=1200, sp=0)
```

Note that the ability to construct an arbitrary Python object may be dangerous if you receive a YAML document from an untrusted source such as the Internet. The function `yaml.safe_load` limits this ability to simple Python objects like integers or lists.

A python object can be marked as safe and thus be recognized by `yaml.safe_load`. To do this, derive it from `yaml.YAMLObject` (as explained in section *Constructors, representers, resolvers*) and explicitly set its class property `yaml_loader` to `yaml.SafeLoader`.

### Dumping YAML

The `yaml.dump` function accepts a Python object and produces a YAML document.

```
>>> print yaml.dump({'name': 'Silenthand Olleander', 'race': 'Human',
... 'traits': ['ONE_HAND', 'ONE_EYE']})

name: Silenthand Olleander
race: Human
traits: [ONE_HAND, ONE_EYE]
```

`yaml.dump` accepts the second optional argument, which must be an open text or binary file. In this case, `yaml.dump` will write the produced YAML document into the file. Otherwise, `yaml.dump` returns the produced document.

```
>>> stream = file('document.yaml', 'w')
>>> yaml.dump(data, stream)    # Write a YAML representation of data to 'document.yaml'.
>>> print yaml.dump(data)      # Output the document to the screen.
```

If you need to dump several YAML documents to a single stream, use the function `yaml.dump_all`. `yaml.dump_all` accepts a list or a generator producing

Python objects to be serialized into a YAML document. The second optional argument is an open file.

```
>>> print yaml.dump([1,2,3], explicit_start=True)
--- [1, 2, 3]

>>> print yaml.dump_all([1,2,3], explicit_start=True)
--- 1
--- 2
--- 3
```

You may even dump instances of Python classes.

```
>>> class Hero:
...     def __init__(self, name, hp, sp):
...         self.name = name
...         self.hp = hp
...         self.sp = sp
...     def __repr__(self):
...         return "%s(name=%r, hp=%r, sp=%r)" % (
...             self.__class__.__name__, self.name, self.hp, self.sp)

>>> print yaml.dump(Hero("Galain Ysseleg", hp=-3, sp=2))

!!python/object:__main__.Hero {hp: -3, name: Galain Ysseleg, sp: 2}
```

`yaml.dump` supports a number of keyword arguments that specify formatting details for the emitter. For instance, you may set the preferred intendation and width, use the canonical YAML format or force preferred style for scalars and collections.

```
>>> print yaml.dump(range(50))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
  23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
  43, 44, 45, 46, 47, 48, 49]

>>> print yaml.dump(range(50), width=50, indent=4)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
    16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
    28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
    40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

>>> print yaml.dump(range(5), canonical=True)
---
!!seq [
  !!int "0",
  !!int "1",
  !!int "2",
  !!int "3",
  !!int "4",
]

>>> print yaml.dump(range(5), default_flow_style=False)
- 0
- 1
- 2
- 3
- 4

>>> print yaml.dump(range(5), default_flow_style=True, default_style='"')
[!!int "0", !!int "1", !!int "2", !!int "3", !!int "4"]
```

### Constructors, representers, resolvers

You may define your own application-specific tags. The easiest way to do it is to define a subclass of `yaml.YAMLObject`:

```
>>> class Monster(yaml.YAMLObject):
...     yaml_tag = u'!Monster'
...     def __init__(self, name, hp, ac, attacks):
...         self.name = name
...         self.hp = hp
...         self.ac = ac
...         self.attacks = attacks
...     def __repr__(self):
...         return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
...             self.__class__.__name__, self.name, self.hp, self.ac, self.attacks)
```

The above definition is enough to automatically load and dump `Monster` objects:

```
>>> yaml.load("""
... --- !Monster
... name: Cave spider
... hp: [2,6]    # 2d6
... ac: 16
... attacks: [BITE, HURT]
... """)

Monster(name='Cave spider', hp=[2, 6], ac=16, attacks=['BITE', 'HURT'])

>>> print yaml.dump(Monster(
...     name='Cave lizard', hp=[3,6], ac=16, attacks=['BITE','HURT']))

!Monster
ac: 16
attacks: [BITE, HURT]
hp: [3, 6]
name: Cave lizard
```

`yaml.YAMLObject` uses metaclass magic to register a constructor, which transforms a YAML node to a class instance, and a representer, which serializes a class instance to a YAML node.

If you don’t want to use metaclasses, you may register your constructors and representers using the functions `yaml.add_constructor` and `yaml.add_representer`. For instance, you may want to add a constructor and a representer for the following `Dice` class:

```
>>> class Dice(tuple):
...     def __new__(cls, a, b):
...         return tuple.__new__(cls, [a, b])
...     def __repr__(self):
...         return "Dice(%s,%s)" % self

>>> print Dice(3,6)
Dice(3,6)
```

The default representation for `Dice` objects is not pretty:

```
>>> print yaml.dump(Dice(3,6))

!!python/object/new:__main__.Dice
- !!python/tuple [3, 6]
```

Suppose you want a `Dice` object to represented as `AdB` in YAML:

```
>>> print yaml.dump(Dice(3,6))

3d6
```

First we define a representer that converts a dice object to a scalar node with the tag `!dice`, then we register it.

```
>>> def dice_representer(dumper, data):
...     return dumper.represent_scalar(u'!dice', u'%sd%s' % data)

>>> yaml.add_representer(Dice, dice_representer)
```

Now you may dump an instance of the `Dice` object:

```
>>> print yaml.dump({'gold': Dice(10,6)})
{gold: !dice '10d6'}
```

Let us add the code to construct a Dice object:

```
>>> def dice_constructor(loader, node):
...     value = loader.construct_scalar(node)
...     a, b = map(int, value.split('d'))
...     return Dice(a, b)

>>> yaml.add_constructor(u'!dice', dice_constructor)
```

Then you may load a `Dice` object as well:

```
>>> print yaml.load("""
... initial hit points: !dice 8d4
... """)

{'initial hit points': Dice(8,4)}
```

You might not want to specify the tag `!dice` everywhere. There is a way to teach PyYAML that any untagged plain scalar which looks like XdY has the implicit tag `!dice`. Use `add_implicit_resolver`:

```
>>> import re
>>> pattern = re.compile(r'^\d+d\d+$')
>>> yaml.add_implicit_resolver(u'!dice', pattern)
```

Now you don’t have to specify the tag to define a `Dice` object:

```
>>> print yaml.dump({'treasure': Dice(10,20)})

{treasure: 10d20}

>>> print yaml.load("""
... damage: 5d10
... """)

{'damage': Dice(5,10)}
```


## YAML syntax

A good introduction to the YAML syntax is Chapter 2 of the YAML specification.

You may also check the YAML cookbook. Note that it is focused on a Ruby implementation and uses the old YAML 1.0 syntax.

Here we present most common YAML constructs together with the corresponding Python objects.

### Documents

YAML stream is a collection of zero or more documents. An empty stream contains no documents. Documents are separated with `---`. Documents may optionally end with `...`. A single document may or may not be marked with `---`.

Example of an implicit document:

```
- Multimedia
- Internet
- Education
```

Example of an explicit document:

```
---
- Afterstep
- CTWM
- Oroborus
...
```

Example of several documents in the same stream:

```
---
- Ada
- APL
- ASP

- Assembly
- Awk
---
- Basic
---
- C
- C#    # Note that comments are denoted with ' #' (space then #).
- C++
- Cold Fusion
```

### Block sequences

In the block context, sequence entries are denoted by `-` (dash then space):

```
# YAML
- The Dagger 'Narthanc'
- The Dagger 'Nimthanc'
- The Dagger 'Dethanc'
```

```
# Python
["The Dagger 'Narthanc'", "The Dagger 'Nimthanc'", "The Dagger 'Dethanc'"]
```

Block sequences can be nested:

```
# YAML
-
  - HTML
  - LaTeX
  - SGML
  - VRML
  - XML
  - YAML
-
  - BSD
  - GNU Hurd
  - Linux
```

```
# Python
[['HTML', 'LaTeX', 'SGML', 'VRML', 'XML', 'YAML'], ['BSD', 'GNU Hurd', 'Linux']]
```

It’s not necessary to start a nested sequence with a new line:

```
# YAML
- 1.1
- - 2.1
  - 2.2
- - - 3.1
    - 3.2
    - 3.3
```

```
# Python
[1.1, [2.1, 2.2], [[3.1, 3.2, 3.3]]]
```

A block sequence may be nested to a block mapping. Note that in this case it is not necessary to indent the sequence.

```
# YAML
left hand:
- Ring of Teleportation
- Ring of Speed

right hand:
- Ring of Resist Fire
- Ring of Resist Cold
- Ring of Resist Poison
```

```
# Python
{'right hand': ['Ring of Resist Fire', 'Ring of Resist Cold', 'Ring of Resist Poison'],
'left hand': ['Ring of Teleportation', 'Ring of Speed']}
```

### Block mappings

In the block context, keys and values of mappings are separated by `:` (colon then space):

```
# YAML
base armor class: 0
base damage: [4,4]
plus to-hit: 12
plus to-dam: 16
plus to-ac: 0
```

```
# Python
{'plus to-hit': 12, 'base damage': [4, 4], 'base armor class': 0, 'plus to-ac': 0, 'plus to-dam': 16}
```

Complex keys are denoted with `?` (question mark then space):

```
# YAML
? !!python/tuple [0,0]
: The Hero
? !!python/tuple [0,1]
: Treasure
? !!python/tuple [1,0]
: Treasure
? !!python/tuple [1,1]
: The Dragon
```

```
# Python
{(0, 1): 'Treasure', (1, 0): 'Treasure', (0, 0): 'The Hero', (1, 1): 'The Dragon'}
```

Block mapping can be nested:

```
# YAML
hero:
  hp: 34
  sp: 8
  level: 4
orc:
  hp: 12
  sp: 0
  level: 2
```

```
# Python
{'hero': {'hp': 34, 'sp': 8, 'level': 4}, 'orc': {'hp': 12, 'sp': 0, 'level': 2}}
```

A block mapping may be nested in a block sequence:

```
# YAML
- name: PyYAML
  status: 4
  license: MIT
  language: Python
- name: PySyck
  status: 5
  license: BSD
  language: Python
```

```
# Python
[{'status': 4, 'language': 'Python', 'name': 'PyYAML', 'license': 'MIT'},
{'status': 5, 'license': 'BSD', 'name': 'PySyck', 'language': 'Python'}]
```

### Flow collections

The syntax of flow collections in YAML is very close to the syntax of list and dictionary constructors in Python:

```
# YAML
{ str: [15, 17], con: [16, 16], dex: [17, 18], wis: [16, 16], int: [10, 13], chr: [5, 8] }
```

```
# Python
{'dex': [17, 18], 'int': [10, 13], 'chr': [5, 8], 'wis': [16, 16], 'str': [15, 17], 'con': [16, 16]}
```

### Scalars

There are 5 styles of scalars in YAML: plain, single-quoted, double-quoted, literal, and folded:

```
# YAML
plain: Scroll of Remove Curse
single-quoted: 'EASY_KNOW'
double-quoted: "?"
literal: |    # Borrowed from http://www.kersbergen.com/flump/religion.html
  by hjw              ___
     __              /.-.\
    /  )_____________\\  Y
   /_ /=== == === === =\ _\_
  ( /)=== == === === == Y   \
   `-------------------(  o  )
                        \___/
folded: >
  It removes all ordinary curses from all equipped items.
  Heavy or permanent curses are unaffected.
```

```
# Python
{'plain': 'Scroll of Remove Curse',
'literal':
    'by hjw              ___\n'
    '   __              /.-.\\\n'
    '  /  )_____________\\\\  Y\n'
    ' /_ /=== == === === =\\ _\\_\n'
    '( /)=== == === === == Y   \\\n'
    ' `-------------------(  o  )\n'
    '                      \\___/\n',
'single-quoted': 'EASY_KNOW',
'double-quoted': '?',
'folded': 'It removes all ordinary curses from all equipped items. Heavy or permanent curses are unaffected.\n'}
```

Each style has its own quirks. A plain scalar does not use indicators to denote its start and end, therefore it’s the most restricted style. Its natural applications are names of attributes and parameters.

Using single-quoted scalars, you may express any value that does not contain special characters. No escaping occurs for single quoted scalars except that a pair of adjacent quotes `''` is replaced with a lone single quote `'`.

Double-quoted is the most powerful style and the only style that can express any scalar value. Double-quoted scalars allow *escaping*. Using escaping sequences `\x*` and `\u***`, you may express any ASCII or Unicode character.

There are two kind of block scalar styles: *literal* and *folded*. The literal style is the most suitable style for large block of text such as source code. The folded style is similar to the literal style, but two adjacent non-empty lines are joined to a single line separated by a space character.

### Aliases

*Note that PyYAML does not yet support recursive objects.*

Using YAML you may represent objects of arbitrary graph-like structures. If you want to refer to the same object from different parts of a document, you need to use anchors and aliases.

Anchors are denoted by the `&` indicator while aliases are denoted by ``. For instance, the document

```
left hand: &A
  name: The Bastard Sword of Eowyn
  weight: 30
right hand: *A
```

expresses the idea of a hero holding a heavy sword in both hands.

PyYAML now fully supports recursive objects. For instance, the document

```
&A [ *A ]
```

will produce a list object containing a reference to itself.

### Tags

Tags are used to denote the type of a YAML node. Standard YAML tags are defined at http://yaml.org/type/index.html.

Tags may be implicit:

```
boolean: true
integer: 3
float: 3.14
```

```
{'boolean': True, 'integer': 3, 'float': 3.14}
```

or explicit:

```
boolean: !!bool "true"
integer: !!int "3"
float: !!float "3.14"
```

```
{'boolean': True, 'integer': 3, 'float': 3.14}
```

Plain scalars without explicitly defined tags are subject to implicit tag resolution. The scalar value is checked against a set of regular expressions and if one of them matches, the corresponding tag is assigned to the scalar. PyYAML allows an application to add custom implicit tag resolvers.


## YAML tags and Python types

The following table describes how nodes with different tags are converted to Python objects.

| *YAML tag* | *Python type* |
|---|---|
| *Standard YAML tags* |   |
| `!!null` | `None` |
| `!!bool` | `bool` |
| `!!int` | `int` or `long` (`int` in Python 3) |
| `!!float` | `float` |
| `!!binary` | `str` (`bytes` in Python 3) |
| `!!timestamp` | `datetime.datetime` |
| `!!omap`, `!!pairs` | `list` of pairs |
| `!!set` | `set` |
| `!!str` | `str` or `unicode` (`str` in Python 3) |
| `!!seq` | `list` |
| `!!map` | `dict` |
| *Python-specific tags* |   |
| `!!python/none` | `None` |
| `!!python/bool` | `bool` |
| `!!python/bytes` | (`bytes` in Python 3) |
| `!!python/str` | `str` (`str` in Python 3) |
| `!!python/unicode` | `unicode` (`str` in Python 3) |
| `!!python/int` | `int` |
| `!!python/long` | `long` (`int` in Python 3) |
| `!!python/float` | `float` |
| `!!python/complex` | `complex` |
| `!!python/list` | `list` |
| `!!python/tuple` | `tuple` |
| `!!python/dict` | `dict` |
| *Complex Python tags* |   |
| `!!python/name:module.name` | `module.name` |
| `!!python/module:package.module` | `package.module` |
| `!!python/object:module.cls` | `module.cls` instance |
| `!!python/object/new:module.cls` | `module.cls` instance |
| `!!python/object/apply:module.f` | value of `f(...)` |

### String conversion (Python 2 only)

There are four tags that are converted to `str` and `unicode` values: `!!str`, `!!binary`, `!!python/str`, and `!!python/unicode`.

`!!str`-tagged scalars are converted to `str` objects if its value is *ASCII*. Otherwise it is converted to `unicode`. `!!binary`-tagged scalars are converted to `str` objects with its value decoded using the *base64* encoding. `!!python/str` scalars are converted to `str` objects encoded with *utf-8* encoding. `!!python/unicode` scalars are converted to `unicode` objects.

Conversely, a `str` object is converted to 1. a `!!str` scalar if its value is *ASCII*. 2. a `!!python/str` scalar if its value is a correct *utf-8* sequence. 3. a `!!binary` scalar otherwise.

A `unicode` object is converted to 1. a `!!python/unicode` scalar if its value is *ASCII*. 2. a `!!str` scalar otherwise.

### String conversion (Python 3 only)

In Python 3, `str` objects are converted to `!!str` scalars and `bytes` objects to `!!binary` scalars. For compatibility reasons, tags `!!python/str` and `!!python/unicode` are still supported and converted to `str` objects.

### Names and modules

In order to represent static Python objects like functions or classes, you need to use a complex `!!python/name` tag. For instance, the function `yaml.dump` can be represented as

```
!!python/name:yaml.dump
```

Similarly, modules are represented using the tag `!python/module`:

```
!!python/module:yaml
```

### Objects

Any pickleable object can be serialized using the `!!python/object` tag:

```
!!python/object:module.Class { attribute: value, ... }
```

In order to support the pickle protocol, two additional forms of the `!!python/object` tag are provided:

```
!!python/object/new:module.Class
args: [argument, ...]
kwds: {key: value, ...}
state: ...
listitems: [item, ...]
dictitems: [key: value, ...]

!!python/object/apply:module.function
args: [argument, ...]
kwds: {key: value, ...}
state: ...
listitems: [item, ...]
dictitems: [key: value, ...]
```

If only the `args` field is non-empty, the above records can be shortened:

```
!!python/object/new:module.Class [argument, ...]

!!python/object/apply:module.function [argument, ...]
```
