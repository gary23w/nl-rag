---
title: "PyYAML Documentation (part 2/2)"
source: https://pyyaml.org/wiki/PyYAMLDocumentation
domain: pyyaml-parsing
license: CC-BY-SA-4.0
tags: python pyyaml, pyyaml parsing, yaml config python
fetched: 2026-07-02
part: 2/2
---

## Reference

*Warning: API stability is not guaranteed!*

### The yaml package

```
scan(stream, Loader=Loader)
```

`scan(stream)` scans the given `stream` and produces a sequence of tokens.

```
parse(stream, Loader=Loader)

emit(events, stream=None, Dumper=Dumper,
    canonical=None,
    indent=None,
    width=None,
    allow_unicode=None,
    line_break=None)
```

`parse(stream)` parses the given `stream` and produces a sequence of parsing events.

`emit(events, stream=None)` serializes the given sequence of parsing `events` and writes them to the `stream`. if `stream` is `None`, it returns the produced stream.

```
compose(stream, Loader=Loader)
compose_all(stream, Loader=Loader)

serialize(node, stream=None, Dumper=Dumper,
    encoding='utf-8', # encoding=None (Python 3)
    explicit_start=None,
    explicit_end=None,
    version=None,
    tags=None,
    canonical=None,
    indent=None,
    width=None,
    allow_unicode=None,
    line_break=None)
serialize_all(nodes, stream=None, Dumper=Dumper, ...)
```

`compose(stream)` parses the given `stream` and returns the root of the representation graph for the first document in the stream. If there are no documents in the stream, it returns `None`.

`compose_all(stream)` parses the given `stream` and returns a sequence of representation graphs corresponding to the documents in the stream.

`serialize(node, stream=None)` serializes the given representation graph into the `stream`. If `stream` is `None`, it returns the produced stream.

`serialize_all(node, stream=None)` serializes the given sequence of representation graphs into the given `stream`. If `stream` is `None`, it returns the produced stream.

```
load(stream, Loader=Loader)
load_all(stream, Loader=Loader)

safe_load(stream)
safe_load_all(stream)

dump(data, stream=None, Dumper=Dumper,
    default_style=None,
    default_flow_style=None,
    encoding='utf-8', # encoding=None (Python 3)
    explicit_start=None,
    explicit_end=None,
    version=None,
    tags=None,
    canonical=None,
    indent=None,
    width=None,
    allow_unicode=None,
    line_break=None)
dump_all(data, stream=None, Dumper=Dumper, ...)

safe_dump(data, stream=None, ...)
safe_dump_all(data, stream=None, ...)
```

`load(stream)` parses the given `stream` and returns a Python object constructed from for the first document in the stream. If there are no documents in the stream, it returns `None`.

`load_all(stream)` parses the given `stream` and returns a sequence of Python objects corresponding to the documents in the stream.

`safe_load(stream)` parses the given `stream` and returns a Python object constructed from for the first document in the stream. If there are no documents in the stream, it returns `None`. `safe_load` recognizes only standard YAML tags and cannot construct an arbitrary Python object.

A python object can be marked as safe and thus be recognized by `yaml.safe_load`. To do this, derive it from `yaml.YAMLObject` (as explained in section *Constructors, representers, resolvers*) and explicitly set its class property `yaml_loader` to `yaml.SafeLoader`.

`safe_load_all(stream)` parses the given `stream` and returns a sequence of Python objects corresponding to the documents in the stream. `safe_load_all` recognizes only standard YAML tags and cannot construct an arbitrary Python object.

`dump(data, stream=None)` serializes the given Python object into the `stream`. If `stream` is `None`, it returns the produced stream.

`dump_all(data, stream=None)` serializes the given sequence of Python objects into the given `stream`. If `stream` is `None`, it returns the produced stream. Each object is represented as a YAML document.

`safe_dump(data, stream=None)` serializes the given Python object into the `stream`. If `stream` is `None`, it returns the produced stream. `safe_dump` produces only standard YAML tags and cannot represent an arbitrary Python object.

`safe_dump_all(data, stream=None)` serializes the given sequence of Python objects into the given `stream`. If `stream` is `None`, it returns the produced stream. Each object is represented as a YAML document. `safe_dump_all` produces only standard YAML tags and cannot represent an arbitrary Python object.

```
def constructor(loader, node):
    # ...
    return data

def multi_constructor(loader, tag_suffix, node):
    # ...
    return data

add_constructor(tag, constructor, Loader=Loader)
add_multi_constructor(tag_prefix, multi_constructor, Loader=Loader)
```

`add_constructor(tag, constructor)` specifies a `constructor` for the given `tag`. A constructor is a function that converts a node of a YAML representation graph to a native Python object. A constructor accepts an instance of `Loader` and a node and returns a Python object.

`add_multi_constructor(tag_prefix, multi_constructor)` specifies a `multi_constructor` for the given `tag_prefix`. A multi-constructor is a function that converts a node of a YAML representation graph to a native Python object. A multi-constructor accepts an instance of `Loader`, the suffix of the node tag, and a node and returns a Python object.

```
def representer(dumper, data):
    # ...
    return node

def multi_representer(dumper, data):
    # ...
    return node

add_representer(data_type, representer, Dumper=Dumper)
add_multi_representer(base_data_type, multi_representer, Dumper=Dumper)
```

`add_representer(data_type, representer)` specifies a `representer` for Python objects of the given `data_type`. A representer is a function that converts a native Python object to a node of a YAML representation graph. A representer accepts an instance of `Dumper` and an object and returns a node.

`add_multi_representer(base_data_type, multi_representer)` specifies a `multi_representer` for Python objects of the given `base_data_type` or any of its subclasses. A multi-representer is a function that converts a native Python object to a node of a YAML representation graph. A multi-representer accepts an instance of `Dumper` and an object and returns a node.

```
add_implicit_resolver(tag, regexp, first, Loader=Loader, Dumper=Dumper)
add_path_resolver(tag, path, kind, Loader=Loader, Dumper=Dumper)
```

`add_implicit_resolver(tag, regexp, first)` adds an implicit tag resolver for plain scalars. If the scalar value is matched the given `regexp`, it is assigned the `tag`. `first` is a list of possible initial characters or `None`.

`add_path_resolver(tag, path, kind)` adds a path-based implicit tag resolver. A `path` is a list of keys that form a path to a node in the representation graph. Paths elements can be string values, integers, or `None`. The `kind` of a node can be `str`, `list`, `dict`, or `None`.

### Mark

```
Mark(name, index, line, column, buffer, pointer)
```

An instance of `Mark` points to a certain position in the input stream. `name` is the name of the stream, for instance it may be the filename if the input stream is a file. `line` and `column` is the line and column of the position (starting from 0). `buffer`, when it is not `None`, is a part of the input stream that contain the position and `pointer` refers to the position in the `buffer`.

### YAMLError

```
YAMLError()
```

If the YAML parser encounters an error condition, it raises an exception which is an instance of `YAMLError` or of its subclass. An application may catch this exception and warn a user.

```
try:
    config = yaml.load(file('config.yaml', 'r'))
except yaml.YAMLError, exc:
    print "Error in configuration file:", exc
```

An exception produced by the YAML processor may point to the problematic position.

```
>>> try:
...     yaml.load("unbalanced blackets: ][")
... except yaml.YAMLError, exc:
...     if hasattr(exc, 'problem_mark'):
...         mark = exc.problem_mark
...         print "Error position: (%s:%s)" % (mark.line+1, mark.column+1)

Error position: (1:22)
```

### Tokens

Tokens are produced by a YAML scanner. They are not really useful except for low-level YAML applications such as syntax highlighting.

The PyYAML scanner produces the following types of tokens:

```
StreamStartToken(encoding, start_mark, end_mark) # Start of the stream.
StreamEndToken(start_mark, end_mark) # End of the stream.
DirectiveToken(name, value, start_mark, end_mark) # YAML directive, either %YAML or %TAG.
DocumentStartToken(start_mark, end_mark) # '---'.
DocumentEndToken(start_mark, end_mark) # '...'.
BlockSequenceStartToken(start_mark, end_mark) # Start of a new block sequence.
BlockMappingStartToken(start_mark, end_mark) # Start of a new block mapping.
BlockEndToken(start_mark, end_mark) # End of a block collection.
FlowSequenceStartToken(start_mark, end_mark) # '['.
FlowMappingStartToken(start_mark, end_mark) # '{'.
FlowSequenceEndToken(start_mark, end_mark) # ']'.
FlowMappingEndToken(start_mark, end_mark) # '}'.
KeyToken(start_mark, end_mark) # Either '?' or start of a simple key.
ValueToken(start_mark, end_mark) # ':'.
BlockEntryToken(start_mark, end_mark) # '-'.
FlowEntryToken(start_mark, end_mark) # ','.
AliasToken(value, start_mark, end_mark) # '*value'.
AnchorToken(value, start_mark, end_mark) # '&value'.
TagToken(value, start_mark, end_mark) # '!value'.
ScalarToken(value, plain, style, start_mark, end_mark) # 'value'.
```

`start_mark` and `end_mark` denote the beginning and the end of a token.

Example:

```
>>> document = """
... ---
... block sequence:
... - BlockEntryToken
... block mapping:
...   ? KeyToken
...   : ValueToken
... flow sequence: [FlowEntryToken, FlowEntryToken]
... flow mapping: {KeyToken: ValueToken}
... anchors and tags:
... - &A !!int '5'
... - *A
... ...
... """

>>> for token in yaml.scan(document):
...     print token

StreamStartToken(encoding='utf-8')

DocumentStartToken()

BlockMappingStartToken()

KeyToken()
ScalarToken(plain=True, style=None, value=u'block sequence')

ValueToken()
BlockEntryToken()
ScalarToken(plain=True, style=None, value=u'BlockEntryToken')

KeyToken()
ScalarToken(plain=True, style=None, value=u'block mapping')

ValueToken()
BlockMappingStartToken()

KeyToken()
ScalarToken(plain=True, style=None, value=u'KeyToken')
ValueToken()
ScalarToken(plain=True, style=None, value=u'ValueToken')
BlockEndToken()

KeyToken()
ScalarToken(plain=True, style=None, value=u'flow sequence')

ValueToken()
FlowSequenceStartToken()
ScalarToken(plain=True, style=None, value=u'FlowEntryToken')
FlowEntryToken()
ScalarToken(plain=True, style=None, value=u'FlowEntryToken')
FlowSequenceEndToken()

KeyToken()
ScalarToken(plain=True, style=None, value=u'flow mapping')

ValueToken()
FlowMappingStartToken()
KeyToken()
ScalarToken(plain=True, style=None, value=u'KeyToken')
ValueToken()
ScalarToken(plain=True, style=None, value=u'ValueToken')
FlowMappingEndToken()

KeyToken()
ScalarToken(plain=True, style=None, value=u'anchors and tags')

ValueToken()
BlockEntryToken()
AnchorToken(value=u'A')
TagToken(value=(u'!!', u'int'))
ScalarToken(plain=False, style="'", value=u'5')

BlockEntryToken()
AliasToken(value=u'A')

BlockEndToken()

DocumentEndToken()

StreamEndToken()
```

### Events

Events are used by the low-level Parser and Emitter interfaces, which are similar to the SAX API. While the Parser parses a YAML stream and produces a sequence of events, the Emitter accepts a sequence of events and emits a YAML stream.

The following events are defined:

```
StreamStartEvent(encoding, start_mark, end_mark)
StreamEndEvent(start_mark, end_mark)
DocumentStartEvent(explicit, version, tags, start_mark, end_mark)
DocumentEndEvent(start_mark, end_mark)
SequenceStartEvent(anchor, tag, implicit, flow_style, start_mark, end_mark)
SequenceEndEvent(start_mark, end_mark)
MappingStartEvent(anchor, tag, implicit, flow_style, start_mark, end_mark)
MappingEndEvent(start_mark, end_mark)
AliasEvent(anchor, start_mark, end_mark)
ScalarEvent(anchor, tag, implicit, value, style, start_mark, end_mark)
```

The `flow_style` flag indicates if a collection is block or flow. The possible values are `None`, `True`, `False`. The `style` flag of a scalar event indicates the style of the scalar. Possible values are `None`, `_`, `'\_`, `'"'`, `'|'`, `'>'`. The `implicit` flag of a collection start event indicates if the tag may be omitted when the collection is emitted. The `implicit` flag of a scalar event is a pair of boolean values that indicate if the tag may be omitted when the scalar is emitted in a plain and non-plain style correspondingly.

Example:

```
>>> document = """
... scalar: &A !!int '5'
... alias: *A
... sequence: [1, 2, 3]
... mapping: [1: one, 2: two, 3: three]
... """

>>> for event in yaml.parse(document):
...     print event

StreamStartEvent()

DocumentStartEvent()

MappingStartEvent(anchor=None, tag=None, implicit=True)

ScalarEvent(anchor=None, tag=None, implicit=(True, False), value=u'scalar')
ScalarEvent(anchor=u'A', tag=u'tag:yaml.org,2002:int', implicit=(False, False), value=u'5')

ScalarEvent(anchor=None, tag=None, implicit=(True, False), value=u'alias')
AliasEvent(anchor=u'A')

ScalarEvent(anchor=None, tag=None, implicit=(True, False), value=u'sequence')
SequenceStartEvent(anchor=None, tag=None, implicit=True)
ScalarEvent(anchor=None, tag=None, implicit=(True, False), value=u'1')
ScalarEvent(anchor=None, tag=None, implicit=(True, False), value=u'2')
ScalarEvent(anchor=None, tag=None, implicit=(True, False), value=u'3')
SequenceEndEvent()

ScalarEvent(anchor=None, tag=None, implicit=(True, False), value=u'mapping')
MappingStartEvent(anchor=None, tag=None, implicit=True)
ScalarEvent(anchor=None, tag=None, implicit=(True, False), value=u'1')
ScalarEvent(anchor=None, tag=None, implicit=(True, False), value=u'one')
ScalarEvent(anchor=None, tag=None, implicit=(True, False), value=u'2')
ScalarEvent(anchor=None, tag=None, implicit=(True, False), value=u'two')
ScalarEvent(anchor=None, tag=None, implicit=(True, False), value=u'3')
ScalarEvent(anchor=None, tag=None, implicit=(True, False), value=u'three')
MappingEndEvent()

MappingEndEvent()

DocumentEndEvent()

StreamEndEvent()

>>> print yaml.emit([
...     yaml.StreamStartEvent(encoding='utf-8'),
...     yaml.DocumentStartEvent(explicit=True),
...     yaml.MappingStartEvent(anchor=None, tag=u'tag:yaml.org,2002:map', implicit=True, flow_style=False),
...     yaml.ScalarEvent(anchor=None, tag=u'tag:yaml.org,2002:str', implicit=(True, True), value=u'agile languages'),
...     yaml.SequenceStartEvent(anchor=None, tag=u'tag:yaml.org,2002:seq', implicit=True, flow_style=True),
...     yaml.ScalarEvent(anchor=None, tag=u'tag:yaml.org,2002:str', implicit=(True, True), value=u'Python'),
...     yaml.ScalarEvent(anchor=None, tag=u'tag:yaml.org,2002:str', implicit=(True, True), value=u'Perl'),
...     yaml.ScalarEvent(anchor=None, tag=u'tag:yaml.org,2002:str', implicit=(True, True), value=u'Ruby'),
...     yaml.SequenceEndEvent(),
...     yaml.MappingEndEvent(),
...     yaml.DocumentEndEvent(explicit=True),
...     yaml.StreamEndEvent(),
... ])

---
agile languages: [Python, Perl, Ruby]
...
```

### Nodes

Nodes are entities in the YAML informational model. There are three kinds of nodes: *scalar*, *sequence*, and *mapping*. In PyYAML, nodes are produced by Composer and can be serialized to a YAML stream by Serializer.

```
ScalarNode(tag, value, style, start_mark, end_mark)
SequenceNode(tag, value, flow_style, start_mark, end_mark)
MappingNode(tag, value, flow_style, start_mark, end_mark)
```

The `style` and `flow_style` flags have the same meaning as for events. The value of a scalar node must be a unicode string. The value of a sequence node is a list of nodes. The value of a mapping node is a list of pairs consisting of key and value nodes.

Example:

```
>>> print yaml.compose("""
... kinds:
... - scalar
... - sequence
... - mapping
... """)

MappingNode(tag=u'tag:yaml.org,2002:map', value=[
    (ScalarNode(tag=u'tag:yaml.org,2002:str', value=u'kinds'), SequenceNode(tag=u'tag:yaml.org,2002:seq', value=[
        ScalarNode(tag=u'tag:yaml.org,2002:str', value=u'scalar'),
        ScalarNode(tag=u'tag:yaml.org,2002:str', value=u'sequence'),
        ScalarNode(tag=u'tag:yaml.org,2002:str', value=u'mapping')]))])

>>> print yaml.serialize(yaml.SequenceNode(tag=u'tag:yaml.org,2002:seq', value=[
...     yaml.ScalarNode(tag=u'tag:yaml.org,2002:str', value=u'scalar'),
...     yaml.ScalarNode(tag=u'tag:yaml.org,2002:str', value=u'sequence'),
...     yaml.ScalarNode(tag=u'tag:yaml.org,2002:str', value=u'mapping')]))

- scalar
- sequence
- mapping
```

### Loader

```
Loader(stream)
SafeLoader(stream)
BaseLoader(stream)

# The following classes are available only if you build LibYAML bindings.
CLoader(stream)
CSafeLoader(stream)
CBaseLoader(stream)
```

`Loader(stream)` is the most common of the above classes and should be used in most cases. `stream` is an input YAML stream. It can be a string, a Unicode string, an open file, an open Unicode file.

`Loader` supports all predefined tags and may construct an arbitrary Python object. Therefore it is not safe to use `Loader` to load a document received from an untrusted source. By default, the functions `scan`, `parse`, `compose`, `construct`, and others use `Loader`.

`SafeLoader(stream)` supports only standard YAML tags and thus it does not construct class instances and probably safe to use with documents received from an untrusted source. The functions `safe_load` and `safe_load_all` use `SafeLoader` to parse a stream.

`BaseLoader(stream)` does not resolve or support any tags and construct only basic Python objects: lists, dictionaries and Unicode strings.

`CLoader`, `CSafeLoader`, `CBaseLoader` are versions of the above classes written in C using the LibYAML library.

```
Loader.check_token(*TokenClasses)
Loader.peek_token()
Loader.get_token()
```

`Loader.check_token(*TokenClasses)` returns `True` if the next token in the stream is an instance of one of the given `TokenClasses`. Otherwise it returns `False`.

`Loader.peek_token()` returns the next token in the stream, but does not remove it from the internal token queue. The function returns `None` at the end of the stream.

`Loader.get_token()` returns the next token in the stream and removes it from the internal token queue. The function returns `None` at the end of the stream.

```
Loader.check_event(*EventClasses)
Loader.peek_event()
Loader.get_event()
```

`Loader.check_event(*EventClasses)` returns `True` if the next event in the stream is an instance of one of the given `EventClasses`. Otherwise it returns `False`.

`Loader.peek_event()` returns the next event in the stream, but does not remove it from the internal event queue. The function returns `None` at the end of the stream.

`Loader.get_event()` returns the next event in the stream and removes it from the internal event queue. The function returns `None` at the end of the stream.

```
Loader.check_node()
Loader.get_node()
```

`Loader.check_node()` returns `True` is there are more documents available in the stream. Otherwise it returns `False`.

`Loader.get_node()` construct the representation graph of the next document in the stream and returns its root node.

```
Loader.check_data()
Loader.get_data()

Loader.add_constructor(tag, constructor) # Loader.add_constructor is a class method.
Loader.add_multi_constructor(tag_prefix, multi_constructor) # Loader.add_multi_constructor is a class method.

Loader.construct_scalar(node)
Loader.construct_sequence(node)
Loader.construct_mapping(node)
```

`Loader.check_data()` returns `True` is there are more documents available in the stream. Otherwise it returns `False`.

`Loader.get_data()` constructs and returns a Python object corresponding to the next document in the stream.

`Loader.add_constructor(tag, constructor)`: see `add_constructor`.

`Loader.add_multi_constructor(tag_prefix, multi_constructor)`: see `add_multi_constructor`.

`Loader.construct_scalar(node)` checks that the given `node` is a scalar and returns its value. This function is intended to be used in constructors.

`Loader.construct_sequence(node)` checks that the given `node` is a sequence and returns a list of Python objects corresponding to the node items. This function is intended to be used in constructors.

`Loader.construct_mapping(node)` checks that the given `node` is a mapping and returns a dictionary of Python objects corresponding to the node keys and values. This function is intended to be used in constructors.

```
Loader.add_implicit_resolver(tag, regexp, first) # Loader.add_implicit_resolver is a class method.
Loader.add_path_resolver(tag, path, kind) # Loader.add_path_resolver is a class method.
```

`Loader.add_implicit_resolver(tag, regexp, first)`: see `add_implicit_resolver`.

`Loader.add_path_resolver(tag, path, kind)`: see `add_path_resolver`.

### Dumper

```
Dumper(stream,
    default_style=None,
    default_flow_style=None,
    canonical=None,
    indent=None,
    width=None,
    allow_unicode=None,
    line_break=None,
    encoding=None,
    explicit_start=None,
    explicit_end=None,
    version=None,
    tags=None)
SafeDumper(stream, ...)
BaseDumper(stream, ...)

# The following classes are available only if you build LibYAML bindings.
CDumper(stream, ...)
CSafeDumper(stream, ...)
CBaseDumper(stream, ...)
```

`Dumper(stream)` is the most common of the above classes and should be used in most cases. `stream` is an output YAML stream. It can be an open file or an open Unicode file.

`Dumper` supports all predefined tags and may represent an arbitrary Python object. Therefore it may produce a document that cannot be loaded by other YAML processors. By default, the functions `emit`, `serialize`, `dump`, and others use `Dumper`.

`SafeDumper(stream)` produces only standard YAML tags and thus cannot represent class instances and probably more compatible with other YAML processors. The functions `safe_dump` and `safe_dump_all` use `SafeDumper` to produce a YAML document.

`BaseDumper(stream)` does not support any tags and is useful only for subclassing.

`CDumper`, `CSafeDumper`, `CBaseDumper` are versions of the above classes written in C using the LibYAML library.

```
Dumper.emit(event)
```

`Dumper.emit(event)` serializes the given `event` and writes it to the output stream.

```
Dumper.open()
Dumper.serialize(node)
Dumper.close()
```

`Dumper.open()` emits `StreamStartEvent`.

`Dumper.serialize(node)` serializes the given representation graph into the output stream.

`Dumper.close()` emits `StreamEndEvent`.

```
Dumper.represent(data)

Dumper.add_representer(data_type, representer) # Dumper.add_representer is a class method.
Dumper.add_multi_representer(base_data_type, multi_representer) # Dumper.add_multi_representer is a class method.

Dumper.represent_scalar(tag, value, style=None)
Dumper.represent_sequence(tag, value, flow_style=None)
Dumper.represent_mapping(tag, value, flow_style=None)
```

`Dumper.represent(data)` serializes the given Python object to the output YAML stream.

`Dumper.add_representer(data_type, representer)`: see `add_representer`.

`Dumper.add_multi_representer(base_data_type, multi_representer)`: see `add_multi_representer`.

`Dumper.represent_scalar(tag, value, style=None)` returns a scalar node with the given `tag`, `value`, and `style`. This function is intended to be used in representers.

`Dumper.represent_sequence(tag, sequence, flow_style=None)` return a sequence node with the given `tag` and subnodes generated from the items of the given `sequence`.

`Dumper.represent_mapping(tag, mapping, flow_style=None)` return a mapping node with the given `tag` and subnodes generated from the keys and values of the given `mapping`.

```
Dumper.add_implicit_resolver(tag, regexp, first) # Dumper.add_implicit_resolver is a class method.
Dumper.add_path_resolver(tag, path, kind) # Dumper.add_path_resolver is a class method.
```

`Dumper.add_implicit_resolver(tag, regexp, first)`: see `add_implicit_resolver`.

`Dumper.add_path_resolver(tag, path, kind)`: see `add_path_resolver`.

### YAMLObject

```
class MyYAMLObject(YAMLObject):
    yaml_loader = Loader
    yaml_dumper = Dumper

    yaml_tag = u'...'
    yaml_flow_style = ...

    @classmethod
    def from_yaml(cls, loader, node):
        # ...
        return data

    @classmethod
    def to_yaml(cls, dumper, data):
        # ...
        return node
```

Subclassing `YAMLObject` is an easy way to define tags, constructors, and representers for your classes. You only need to override the `yaml_tag` attribute. If you want to define your custom constructor and representer, redefine the `from_yaml` and `to_yaml` method correspondingly.


## Deviations from the specification

*need to update this section*

- rules for tabs in YAML are confusing. We are close, but not there yet. Perhaps both the spec and the parser should be fixed. Anyway, the best rule for tabs in YAML is to not use them at all.
- Byte order mark. The initial BOM is stripped, but BOMs inside the stream are considered as parts of the content. It can be fixed, but it’s not really important now.
- Empty plain scalars are not allowed if alias or tag is specified. This is done to prevent anomalities like *[ !tag, value]*, which can be interpreted both as *[ !<!tag,> value ]* and *[ !<!tag> "“,”value" ]*. The spec should be fixed.
- Indentation of flow collections. The spec requires them to be indented more than their block parent node. Unfortunately this rule renders many intuitively correct constructs invalid, for instance,
  ```
  block: {
  } # this is indentation violation according to the spec.
  ```
- ‘:’ is not allowed for plain scalars in the flow mode. *{1:2}* is interpreted as *{ 1 : 2 }*.
