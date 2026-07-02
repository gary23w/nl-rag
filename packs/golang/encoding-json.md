---
title: "json package"
source: https://pkg.go.dev/encoding/json
domain: golang
license: BSD-3-Clause
tags: golang, goroutine, go module, go stdlib
fetched: 2026-07-02
---

# json

package

standard library

Version:

go1.26.4

Opens a new window with list of versions in this module.

Latest

Latest

This package is not in the latest version of its module.

Go to latest

Published: Jun 2, 2026

License:

BSD-3-Clause

Opens a new window with license information.

Imports:

17

Opens a new window with list of imports.

Imported by:

1,523,261

Opens a new window with list of known importers.

## Documentation

### Overview

Package json implements encoding and decoding of JSON as defined in RFC 7159. The mapping between JSON and Go values is described in the documentation for the Marshal and Unmarshal functions.

See "JSON and Go" for an introduction to this package: https://golang.org/doc/articles/json_and_go.html

#### Security Considerations

The JSON standard (RFC 7159) is lax in its definition of a number of parser behaviors. As such, many JSON parsers behave differently in various scenarios. These differences in parsers mean that systems that use multiple independent JSON parser implementations may parse the same JSON object in differing ways.

Systems that rely on a JSON object being parsed consistently for security purposes should be careful to understand the behaviors of this parser, as well as how these behaviors may cause interoperability issues with other parser implementations.

Due to the Go Backwards Compatibility promise (https://go.dev/doc/go1compat) there are a number of behaviors this package exhibits that may cause interopability issues, but cannot be changed. In particular the following parsing behaviors may cause issues:

- If a JSON object contains duplicate keys, keys are processed in the order they are observed, meaning later values will replace or be merged into prior values, depending on the field type (in particular maps and structs will have values merged, while other types have values replaced).
- When parsing a JSON object into a Go struct, keys are considered in a case-insensitive fashion.
- When parsing a JSON object into a Go struct, unknown keys in the JSON object are ignored (unless a Decoder is used and Decoder.DisallowUnknownFields has been called).
- Invalid UTF-8 bytes in JSON strings are replaced by the Unicode replacement character.
- Large JSON number integers will lose precision when unmarshaled into floating-point types.

Example (CustomMarshalJSON)

¶

```
//go:build !goexperiment.jsonv2

package main

import (
	"encoding/json"
	"fmt"
	"log"
	"strings"
)

type Animal int

const (
	Unknown Animal = iota
	Gopher
	Zebra
)

func (a *Animal) UnmarshalJSON(b []byte) error {
	var s string
	if err := json.Unmarshal(b, &s); err != nil {
		return err
	}
	switch strings.ToLower(s) {
	default:
		*a = Unknown
	case "gopher":
		*a = Gopher
	case "zebra":
		*a = Zebra
	}

	return nil
}

func (a Animal) MarshalJSON() ([]byte, error) {
	var s string
	switch a {
	default:
		s = "unknown"
	case Gopher:
		s = "gopher"
	case Zebra:
		s = "zebra"
	}

	return json.Marshal(s)
}

func main() {
	blob := `["gopher","armadillo","zebra","unknown","gopher","bee","gopher","zebra"]`
	var zoo []Animal
	if err := json.Unmarshal([]byte(blob), &zoo); err != nil {
		log.Fatal(err)
	}

	census := make(map[Animal]int)
	for _, animal := range zoo {
		census[animal] += 1
	}

	fmt.Printf("Zoo Census:\n* Gophers: %d\n* Zebras:  %d\n* Unknown: %d\n",
		census[Gopher], census[Zebra], census[Unknown])

}
```

```
Output:
Zoo Census:
* Gophers: 3
* Zebras:  2
* Unknown: 3
```

Example (TextMarshalJSON)

¶

```
//go:build !goexperiment.jsonv2

package main

import (
	"encoding/json"
	"fmt"
	"log"
	"strings"
)

type Size int

const (
	Unrecognized Size = iota
	Small
	Large
)

func (s *Size) UnmarshalText(text []byte) error {
	switch strings.ToLower(string(text)) {
	default:
		*s = Unrecognized
	case "small":
		*s = Small
	case "large":
		*s = Large
	}
	return nil
}

func (s Size) MarshalText() ([]byte, error) {
	var name string
	switch s {
	default:
		name = "unrecognized"
	case Small:
		name = "small"
	case Large:
		name = "large"
	}
	return []byte(name), nil
}

func main() {
	blob := `["small","regular","large","unrecognized","small","normal","small","large"]`
	var inventory []Size
	if err := json.Unmarshal([]byte(blob), &inventory); err != nil {
		log.Fatal(err)
	}

	counts := make(map[Size]int)
	for _, size := range inventory {
		counts[size] += 1
	}

	fmt.Printf("Inventory Counts:\n* Small:        %d\n* Large:        %d\n* Unrecognized: %d\n",
		counts[Small], counts[Large], counts[Unrecognized])

}
```

```
Output:
Inventory Counts:
* Small:        3
* Large:        2
* Unrecognized: 3
```

### Index

- func Compact(dst *bytes.Buffer, src []byte) error
- func HTMLEscape(dst *bytes.Buffer, src []byte)
- func Indent(dst *bytes.Buffer, src []byte, prefix, indent string) error
- func Marshal(v any) ([]byte, error)
- func MarshalIndent(v any, prefix, indent string) ([]byte, error)
- func Unmarshal(data []byte, v any) error
- func Valid(data []byte) bool
- type Decoder
  - func NewDecoder(r io.Reader) *Decoder
  - func (dec *Decoder) Buffered() io.Reader
  - func (dec *Decoder) Decode(v any) error
  - func (dec *Decoder) DisallowUnknownFields()
  - func (dec *Decoder) InputOffset() int64
  - func (dec *Decoder) More() bool
  - func (dec *Decoder) Token() (Token, error)
  - func (dec *Decoder) UseNumber()
- type Delim
  - func (d Delim) String() string
- type Encoder
  - func NewEncoder(w io.Writer) *Encoder
  - func (enc *Encoder) Encode(v any) error
  - func (enc *Encoder) SetEscapeHTML(on bool)
  - func (enc *Encoder) SetIndent(prefix, indent string)
- type InvalidUTF8Errordeprecated
  - func (e *InvalidUTF8Error) Error() string
- type InvalidUnmarshalError
  - func (e *InvalidUnmarshalError) Error() string
- type Marshaler
- type MarshalerError
  - func (e *MarshalerError) Error() string
  - func (e *MarshalerError) Unwrap() error
- type Number
  - func (n Number) Float64() (float64, error)
  - func (n Number) Int64() (int64, error)
  - func (n Number) String() string
- type RawMessage
  - func (m RawMessage) MarshalJSON() ([]byte, error)
  - func (m *RawMessage) UnmarshalJSON(data []byte) error
- type SyntaxError
  - func (e *SyntaxError) Error() string
- type Token
- type UnmarshalFieldErrordeprecated
  - func (e *UnmarshalFieldError) Error() string
- type UnmarshalTypeError
  - func (e *UnmarshalTypeError) Error() string
- type Unmarshaler
- type UnsupportedTypeError
  - func (e *UnsupportedTypeError) Error() string
- type UnsupportedValueError
  - func (e *UnsupportedValueError) Error() string

### Examples

- Package (CustomMarshalJSON)
- Package (TextMarshalJSON)
- Decoder
- Decoder.Decode (Stream)
- Decoder.Token
- HTMLEscape
- Indent
- Marshal
- MarshalIndent
- RawMessage (Marshal)
- RawMessage (Unmarshal)
- Unmarshal
- Valid

### Constants

This section is empty.

### Variables

This section is empty.

### Functions

#### func Compact

```
func Compact(dst *bytes.Buffer, src []byte) error
```

Compact appends to dst the JSON-encoded src with insignificant space characters elided.

#### func HTMLEscape

```
func HTMLEscape(dst *bytes.Buffer, src []byte)
```

HTMLEscape appends to dst the JSON-encoded src with <, >, &, U+2028 and U+2029 characters inside string literals changed to \u003c, \u003e, \u0026, \u2028, \u2029 so that the JSON will be safe to embed inside HTML <script> tags. For historical reasons, web browsers don't honor standard HTML escaping within <script> tags, so an alternative JSON encoding must be used.

Example

¶

```
package main

import (
	"bytes"
	"encoding/json"
	"os"
)

func main() {
	var out bytes.Buffer
	json.HTMLEscape(&out, []byte(`{"Name":"<b>HTML content</b>"}`))
	out.WriteTo(os.Stdout)
}
```

```
Output:
{"Name":"\u003cb\u003eHTML content\u003c/b\u003e"}
```

#### func Indent

```
func Indent(dst *bytes.Buffer, src []byte, prefix, indent string) error
```

Indent appends to dst an indented form of the JSON-encoded src. Each element in a JSON object or array begins on a new, indented line beginning with prefix followed by one or more copies of indent according to the indentation nesting. The data appended to dst does not begin with the prefix nor any indentation, to make it easier to embed inside other formatted JSON data. Although leading space characters (space, tab, carriage return, newline) at the beginning of src are dropped, trailing space characters at the end of src are preserved and copied to dst. For example, if src has no trailing spaces, neither will dst; if src ends in a trailing newline, so will dst.

Example

¶

```
package main

import (
	"bytes"
	"encoding/json"
	"log"
	"os"
)

func main() {
	type Road struct {
		Name   string
		Number int
	}
	roads := []Road{
		{"Diamond Fork", 29},
		{"Sheep Creek", 51},
	}

	b, err := json.Marshal(roads)
	if err != nil {
		log.Fatal(err)
	}

	var out bytes.Buffer
	json.Indent(&out, b, "=", "\t")
	out.WriteTo(os.Stdout)
}
```

```
Output:
[
=	{
=		"Name": "Diamond Fork",
=		"Number": 29
=	},
=	{
=		"Name": "Sheep Creek",
=		"Number": 51
=	}
=]
```

#### func Marshal

```
func Marshal(v any) ([]byte, error)
```

Marshal returns the JSON encoding of v.

Marshal traverses the value v recursively. If an encountered value implements Marshaler and is not a nil pointer, Marshal calls Marshaler.MarshalJSON to produce JSON. If no Marshaler.MarshalJSON method is present but the value implements encoding.TextMarshaler instead, Marshal calls encoding.TextMarshaler.MarshalText and encodes the result as a JSON string. The nil pointer exception is not strictly necessary but mimics a similar, necessary exception in the behavior of Unmarshaler.UnmarshalJSON.

Otherwise, Marshal uses the following type-dependent default encodings:

Boolean values encode as JSON booleans.

Floating point, integer, and Number values encode as JSON numbers. NaN and +/-Inf values will return an UnsupportedValueError.

String values encode as JSON strings coerced to valid UTF-8, replacing invalid bytes with the Unicode replacement rune. So that the JSON will be safe to embed inside HTML <script> tags, the string is encoded using HTMLEscape, which replaces "<", ">", "&", U+2028, and U+2029 are escaped to "\u003c","\u003e", "\u0026", "\u2028", and "\u2029". This replacement can be disabled when using an Encoder, by calling Encoder.SetEscapeHTML(false).

Array and slice values encode as JSON arrays, except that []byte encodes as a base64-encoded string, and a nil slice encodes as the null JSON value.

Struct values encode as JSON objects. Each exported struct field becomes a member of the object, using the field name as the object key, unless the field is omitted for one of the reasons given below.

The encoding of each struct field can be customized by the format string stored under the "json" key in the struct field's tag. The format string gives the name of the field, possibly followed by a comma-separated list of options. The name may be empty in order to specify options without overriding the default field name.

The "omitempty" option specifies that the field should be omitted from the encoding if the field has an empty value, defined as false, 0, a nil pointer, a nil interface value, and any array, slice, map, or string of length zero.

As a special case, if the field tag is "-", the field is always omitted. Note that a field with name "-" can still be generated using the tag "-,".

Examples of struct field tags and their meanings:

```
// Field appears in JSON as key "myName".
Field int `json:"myName"`

// Field appears in JSON as key "myName" and
// the field is omitted from the object if its value is empty,
// as defined above.
Field int `json:"myName,omitempty"`

// Field appears in JSON as key "Field" (the default), but
// the field is skipped if empty.
// Note the leading comma.
Field int `json:",omitempty"`

// Field is ignored by this package.
Field int `json:"-"`

// Field appears in JSON as key "-".
Field int `json:"-,"`
```

The "omitzero" option specifies that the field should be omitted from the encoding if the field has a zero value, according to rules:

1) If the field type has an "IsZero() bool" method, that will be used to determine whether the value is zero.

2) Otherwise, the value is zero if it is the zero value for its type.

If both "omitempty" and "omitzero" are specified, the field will be omitted if the value is either empty or zero (or both).

The "string" option signals that a field is stored as JSON inside a JSON-encoded string. It applies only to fields of string, floating point, integer, or boolean types. This extra level of encoding is sometimes used when communicating with JavaScript programs:

```
Int64String int64 `json:",string"`
```

The key name will be used if it's a non-empty string consisting of only Unicode letters, digits, and ASCII punctuation except quotation marks, backslash, and comma.

Embedded struct fields are usually marshaled as if their inner exported fields were fields in the outer struct, subject to the usual Go visibility rules amended as described in the next paragraph. An anonymous struct field with a name given in its JSON tag is treated as having that name, rather than being anonymous. An anonymous struct field of interface type is treated the same as having that type as its name, rather than being anonymous.

The Go visibility rules for struct fields are amended for JSON when deciding which field to marshal or unmarshal. If there are multiple fields at the same level, and that level is the least nested (and would therefore be the nesting level selected by the usual Go rules), the following extra rules apply:

1) Of those fields, if any are JSON-tagged, only tagged fields are considered, even if there are multiple untagged fields that would otherwise conflict.

2) If there is exactly one field (tagged or not according to the first rule), that is selected.

3) Otherwise there are multiple fields, and all are ignored; no error occurs.

Handling of anonymous struct fields is new in Go 1.1. Prior to Go 1.1, anonymous struct fields were ignored. To force ignoring of an anonymous struct field in both current and earlier versions, give the field a JSON tag of "-".

Map values encode as JSON objects. The map's key type must either be a string, an integer type, or implement encoding.TextMarshaler. The map keys are sorted and used as JSON object keys by applying the following rules, subject to the UTF-8 coercion described for string values above:

- keys of any string type are used directly
- keys that implement encoding.TextMarshaler are marshaled
- integer keys are converted to strings

Pointer values encode as the value pointed to. A nil pointer encodes as the null JSON value.

Interface values encode as the value contained in the interface. A nil interface value encodes as the null JSON value.

Channel, complex, and function values cannot be encoded in JSON. Attempting to encode such a value causes Marshal to return an UnsupportedTypeError.

JSON cannot represent cyclic data structures and Marshal does not handle them. Passing cyclic structures to Marshal will result in an error.

Example

¶

```
package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func main() {
	type ColorGroup struct {
		ID     int
		Name   string
		Colors []string
	}
	group := ColorGroup{
		ID:     1,
		Name:   "Reds",
		Colors: []string{"Crimson", "Red", "Ruby", "Maroon"},
	}
	b, err := json.Marshal(group)
	if err != nil {
		fmt.Println("error:", err)
	}
	os.Stdout.Write(b)
}
```

```
Output:
{"ID":1,"Name":"Reds","Colors":["Crimson","Red","Ruby","Maroon"]}
```

#### func MarshalIndent

```
func MarshalIndent(v any, prefix, indent string) ([]byte, error)
```

MarshalIndent is like Marshal but applies Indent to format the output. Each JSON element in the output will begin on a new line beginning with prefix followed by one or more copies of indent according to the indentation nesting.

Example

¶

```
package main

import (
	"encoding/json"
	"fmt"
	"log"
)

func main() {
	data := map[string]int{
		"a": 1,
		"b": 2,
	}

	b, err := json.MarshalIndent(data, "<prefix>", "<indent>")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(string(b))
}
```

```
Output:
{
<prefix><indent>"a": 1,
<prefix><indent>"b": 2
<prefix>}
```

#### func Unmarshal

```
func Unmarshal(data []byte, v any) error
```

Unmarshal parses the JSON-encoded data and stores the result in the value pointed to by v. If v is nil or not a pointer, Unmarshal returns an InvalidUnmarshalError.

Unmarshal uses the inverse of the encodings that Marshal uses, allocating maps, slices, and pointers as necessary, with the following additional rules:

To unmarshal JSON into a pointer, Unmarshal first handles the case of the JSON being the JSON literal null. In that case, Unmarshal sets the pointer to nil. Otherwise, Unmarshal unmarshals the JSON into the value pointed at by the pointer. If the pointer is nil, Unmarshal allocates a new value for it to point to.

To unmarshal JSON into a value implementing Unmarshaler, Unmarshal calls that value's Unmarshaler.UnmarshalJSON method, including when the input is a JSON null. Otherwise, if the value implements encoding.TextUnmarshaler and the input is a JSON quoted string, Unmarshal calls encoding.TextUnmarshaler.UnmarshalText with the unquoted form of the string.

To unmarshal JSON into a struct, Unmarshal matches incoming object keys to the keys used by Marshal (either the struct field name or its tag), ignoring case. If multiple struct fields match an object key, an exact case match is preferred over a case-insensitive one.

Incoming object members are processed in the order observed. If an object includes duplicate keys, later duplicates will replace or be merged into prior values.

To unmarshal JSON into an interface value, Unmarshal stores one of these in the interface value:

- bool, for JSON booleans
- float64, for JSON numbers
- string, for JSON strings
- []any, for JSON arrays
- map[string]any, for JSON objects
- nil for JSON null

To unmarshal a JSON array into a slice, Unmarshal resets the slice length to zero and then appends each element to the slice. As a special case, to unmarshal an empty JSON array into a slice, Unmarshal replaces the slice with a new empty slice.

To unmarshal a JSON array into a Go array, Unmarshal decodes JSON array elements into corresponding Go array elements. If the Go array is smaller than the JSON array, the additional JSON array elements are discarded. If the JSON array is smaller than the Go array, the additional Go array elements are set to zero values.

To unmarshal a JSON object into a map, Unmarshal first establishes a map to use. If the map is nil, Unmarshal allocates a new map. Otherwise Unmarshal reuses the existing map, keeping existing entries. Unmarshal then stores key-value pairs from the JSON object into the map. The map's key type must either be any string type, an integer, or implement encoding.TextUnmarshaler.

If the JSON-encoded data contain a syntax error, Unmarshal returns a SyntaxError.

If a JSON value is not appropriate for a given target type, or if a JSON number overflows the target type, Unmarshal skips that field and completes the unmarshaling as best it can. If no more serious errors are encountered, Unmarshal returns an UnmarshalTypeError describing the earliest such error. In any case, it's not guaranteed that all the remaining fields following the problematic one will be unmarshaled into the target object.

The JSON null value unmarshals into an interface, map, pointer, or slice by setting that Go value to nil. Because null is often used in JSON to mean “not present,” unmarshaling a JSON null into any other Go type has no effect on the value and produces no error.

When unmarshaling quoted strings, invalid UTF-8 or invalid UTF-16 surrogate pairs are not treated as an error. Instead, they are replaced by the Unicode replacement character U+FFFD.

Example

¶

```
package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	var jsonBlob = []byte(`[
	{"Name": "Platypus", "Order": "Monotremata"},
	{"Name": "Quoll",    "Order": "Dasyuromorphia"}
]`)
	type Animal struct {
		Name  string
		Order string
	}
	var animals []Animal
	err := json.Unmarshal(jsonBlob, &animals)
	if err != nil {
		fmt.Println("error:", err)
	}
	fmt.Printf("%+v", animals)
}
```

```
Output:
[{Name:Platypus Order:Monotremata} {Name:Quoll Order:Dasyuromorphia}]
```

#### func Valid ¶ added in go1.9

```
func Valid(data []byte) bool
```

Valid reports whether data is a valid JSON encoding.

Example

¶

```
package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	goodJSON := `{"example": 1}`
	badJSON := `{"example":2:]}}`

	fmt.Println(json.Valid([]byte(goodJSON)), json.Valid([]byte(badJSON)))
}
```

```
Output:
true false
```

### Types

#### type Decoder

```
type Decoder struct {
	
}
```

A Decoder reads and decodes JSON values from an input stream.

Example

¶

This example uses a Decoder to decode a stream of distinct JSON values.

```
package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"strings"
)

func main() {
	const jsonStream = `
	{"Name": "Ed", "Text": "Knock knock."}
	{"Name": "Sam", "Text": "Who's there?"}
	{"Name": "Ed", "Text": "Go fmt."}
	{"Name": "Sam", "Text": "Go fmt who?"}
	{"Name": "Ed", "Text": "Go fmt yourself!"}
`
	type Message struct {
		Name, Text string
	}
	dec := json.NewDecoder(strings.NewReader(jsonStream))
	for {
		var m Message
		if err := dec.Decode(&m); err == io.EOF {
			break
		} else if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("%s: %s\n", m.Name, m.Text)
	}
}
```

```
Output:
Ed: Knock knock.
Sam: Who's there?
Ed: Go fmt.
Sam: Go fmt who?
Ed: Go fmt yourself!
```

#### func NewDecoder

```
func NewDecoder(r io.Reader) *Decoder
```

NewDecoder returns a new decoder that reads from r.

The decoder introduces its own buffering and may read data from r beyond the JSON values requested.

#### func (*Decoder) Buffered ¶ added in go1.1

```
func (dec *Decoder) Buffered() io.Reader
```

Buffered returns a reader of the data remaining in the Decoder's buffer. The reader is valid until the next call to Decoder.Decode.

#### func (*Decoder) Decode

```
func (dec *Decoder) Decode(v any) error
```

Decode reads the next JSON-encoded value from its input and stores it in the value pointed to by v.

See the documentation for Unmarshal for details about the conversion of JSON into a Go value.

Example (Stream)

¶

This example uses a Decoder to decode a streaming array of JSON objects.

```
package main

import (
	"encoding/json"
	"fmt"
	"log"
	"strings"
)

func main() {
	const jsonStream = `
	[
		{"Name": "Ed", "Text": "Knock knock."},
		{"Name": "Sam", "Text": "Who's there?"},
		{"Name": "Ed", "Text": "Go fmt."},
		{"Name": "Sam", "Text": "Go fmt who?"},
		{"Name": "Ed", "Text": "Go fmt yourself!"}
	]
`
	type Message struct {
		Name, Text string
	}
	dec := json.NewDecoder(strings.NewReader(jsonStream))

	// read open bracket
	t, err := dec.Token()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%T: %v\n", t, t)

	// while the array contains values
	for dec.More() {
		var m Message
		// decode an array value (Message)
		err := dec.Decode(&m)
		if err != nil {
			log.Fatal(err)
		}

		fmt.Printf("%v: %v\n", m.Name, m.Text)
	}

	// read closing bracket
	t, err = dec.Token()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%T: %v\n", t, t)

}
```

```
Output:
json.Delim: [
Ed: Knock knock.
Sam: Who's there?
Ed: Go fmt.
Sam: Go fmt who?
Ed: Go fmt yourself!
json.Delim: ]
```

#### func (*Decoder) DisallowUnknownFields ¶ added in go1.10

```
func (dec *Decoder) DisallowUnknownFields()
```

DisallowUnknownFields causes the Decoder to return an error when the destination is a struct and the input contains object keys which do not match any non-ignored, exported fields in the destination.

#### func (*Decoder) InputOffset ¶ added in go1.14

```
func (dec *Decoder) InputOffset() int64
```

InputOffset returns the input stream byte offset of the current decoder position. The offset gives the location of the end of the most recently returned token and the beginning of the next token.

#### func (*Decoder) More ¶ added in go1.5

```
func (dec *Decoder) More() bool
```

More reports whether there is another element in the current array or object being parsed.

#### func (*Decoder) Token ¶ added in go1.5

```
func (dec *Decoder) Token() (Token, error)
```

Token returns the next JSON token in the input stream. At the end of the input stream, Token returns nil, io.EOF.

Token guarantees that the delimiters [ ] { } it returns are properly nested and matched: if Token encounters an unexpected delimiter in the input, it will return an error.

The input stream consists of basic JSON values—bool, string, number, and null—along with delimiters [ ] { } of type Delim to mark the start and end of arrays and objects. Commas and colons are elided.

Example

¶

This example uses a Decoder to decode a stream of distinct JSON values.

```
package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"strings"
)

func main() {
	const jsonStream = `
	{"Message": "Hello", "Array": [1, 2, 3], "Null": null, "Number": 1.234}
`
	dec := json.NewDecoder(strings.NewReader(jsonStream))
	for {
		t, err := dec.Token()
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("%T: %v", t, t)
		if dec.More() {
			fmt.Printf(" (more)")
		}
		fmt.Printf("\n")
	}
}
```

```
Output:
json.Delim: { (more)
string: Message (more)
string: Hello (more)
string: Array (more)
json.Delim: [ (more)
float64: 1 (more)
float64: 2 (more)
float64: 3
json.Delim: ] (more)
string: Null (more)
<nil>: <nil> (more)
string: Number (more)
float64: 1.234
json.Delim: }
```

#### func (*Decoder) UseNumber ¶ added in go1.1

```
func (dec *Decoder) UseNumber()
```

UseNumber causes the Decoder to unmarshal a number into an interface value as a Number instead of as a float64.

#### type Delim ¶ added in go1.5

```
type Delim rune
```

A Delim is a JSON array or object delimiter, one of [ ] { or }.

#### func (Delim) String ¶ added in go1.5

```
func (d Delim) String() string
```

#### type Encoder

```
type Encoder struct {
	
}
```

An Encoder writes JSON values to an output stream.

#### func NewEncoder

```
func NewEncoder(w io.Writer) *Encoder
```

NewEncoder returns a new encoder that writes to w.

#### func (*Encoder) Encode

```
func (enc *Encoder) Encode(v any) error
```

Encode writes the JSON encoding of v to the stream, with insignificant space characters elided, followed by a newline character.

See the documentation for Marshal for details about the conversion of Go values to JSON.

#### func (*Encoder) SetEscapeHTML ¶ added in go1.7

```
func (enc *Encoder) SetEscapeHTML(on bool)
```

SetEscapeHTML specifies whether problematic HTML characters should be escaped inside JSON quoted strings. The default behavior is to escape &, <, and > to \u0026, \u003c, and \u003e to avoid certain safety problems that can arise when embedding JSON in HTML.

In non-HTML settings where the escaping interferes with the readability of the output, SetEscapeHTML(false) disables this behavior.

#### func (*Encoder) SetIndent ¶ added in go1.7

```
func (enc *Encoder) SetIndent(prefix, indent string)
```

SetIndent instructs the encoder to format each subsequent encoded value as if indented by the package-level function Indent(dst, src, prefix, indent). Calling SetIndent("", "") disables indentation.

#### type InvalidUTF8Error deprecated

```
type InvalidUTF8Error struct {
	S string 
}
```

Before Go 1.2, an InvalidUTF8Error was returned by Marshal when attempting to encode a string value with invalid UTF-8 sequences. As of Go 1.2, Marshal instead coerces the string to valid UTF-8 by replacing invalid bytes with the Unicode replacement rune U+FFFD.

Deprecated: No longer used; kept for compatibility.

#### func (*InvalidUTF8Error) Error

```
func (e *InvalidUTF8Error) Error() string
```

#### type InvalidUnmarshalError

```
type InvalidUnmarshalError struct {
	Type reflect.Type
}
```

An InvalidUnmarshalError describes an invalid argument passed to Unmarshal. (The argument to Unmarshal must be a non-nil pointer.)

#### func (*InvalidUnmarshalError) Error

```
func (e *InvalidUnmarshalError) Error() string
```

#### type Marshaler

```
type Marshaler interface {
	MarshalJSON() ([]byte, error)
}
```

Marshaler is the interface implemented by types that can marshal themselves into valid JSON.

#### type MarshalerError

```
type MarshalerError struct {
	Type reflect.Type
	Err  error
	
}
```

A MarshalerError represents an error from calling a Marshaler.MarshalJSON or encoding.TextMarshaler.MarshalText method.

#### func (*MarshalerError) Error

```
func (e *MarshalerError) Error() string
```

#### func (*MarshalerError) Unwrap ¶ added in go1.13

```
func (e *MarshalerError) Unwrap() error
```

Unwrap returns the underlying error.

#### type Number ¶ added in go1.1

```
type Number string
```

A Number represents a JSON number literal.

#### func (Number) Float64 ¶ added in go1.1

```
func (n Number) Float64() (float64, error)
```

Float64 returns the number as a float64.

#### func (Number) Int64 ¶ added in go1.1

```
func (n Number) Int64() (int64, error)
```

Int64 returns the number as an int64.

#### func (Number) String ¶ added in go1.1

```
func (n Number) String() string
```

String returns the literal text of the number.

#### type RawMessage

```
type RawMessage []byte
```

RawMessage is a raw encoded JSON value. It implements Marshaler and Unmarshaler and can be used to delay JSON decoding or precompute a JSON encoding.

Example (Marshal)

¶

This example uses RawMessage to use a precomputed JSON during marshal.

```
package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func main() {
	h := json.RawMessage(`{"precomputed": true}`)

	c := struct {
		Header *json.RawMessage `json:"header"`
		Body   string           `json:"body"`
	}{Header: &h, Body: "Hello Gophers!"}

	b, err := json.MarshalIndent(&c, "", "\t")
	if err != nil {
		fmt.Println("error:", err)
	}
	os.Stdout.Write(b)

}
```

```
Output:
{
	"header": {
		"precomputed": true
	},
	"body": "Hello Gophers!"
}
```

Example (Unmarshal)

¶

This example uses RawMessage to delay parsing part of a JSON message.

```
package main

import (
	"encoding/json"
	"fmt"
	"log"
)

func main() {
	type Color struct {
		Space string
		Point json.RawMessage // delay parsing until we know the color space
	}
	type RGB struct {
		R uint8
		G uint8
		B uint8
	}
	type YCbCr struct {
		Y  uint8
		Cb int8
		Cr int8
	}

	var j = []byte(`[
	{"Space": "YCbCr", "Point": {"Y": 255, "Cb": 0, "Cr": -10}},
	{"Space": "RGB",   "Point": {"R": 98, "G": 218, "B": 255}}
]`)
	var colors []Color
	err := json.Unmarshal(j, &colors)
	if err != nil {
		log.Fatalln("error:", err)
	}

	for _, c := range colors {
		var dst any
		switch c.Space {
		case "RGB":
			dst = new(RGB)
		case "YCbCr":
			dst = new(YCbCr)
		}
		err := json.Unmarshal(c.Point, dst)
		if err != nil {
			log.Fatalln("error:", err)
		}
		fmt.Println(c.Space, dst)
	}
}
```

```
Output:
YCbCr &{255 0 -10}
RGB &{98 218 255}
```

#### func (RawMessage) MarshalJSON

```
func (m RawMessage) MarshalJSON() ([]byte, error)
```

MarshalJSON returns m as the JSON encoding of m.

#### func (*RawMessage) UnmarshalJSON

```
func (m *RawMessage) UnmarshalJSON(data []byte) error
```

UnmarshalJSON sets *m to a copy of data.

#### type SyntaxError

```
type SyntaxError struct {
	Offset int64 
	
}
```

A SyntaxError is a description of a JSON syntax error. Unmarshal will return a SyntaxError if the JSON can't be parsed.

#### func (*SyntaxError) Error

```
func (e *SyntaxError) Error() string
```

#### type Token ¶ added in go1.5

```
type Token any
```

A Token holds a value of one of these types:

- Delim, for the four JSON delimiters [ ] { }
- bool, for JSON booleans
- float64, for JSON numbers
- Number, for JSON numbers
- string, for JSON string literals
- nil, for JSON null

#### type UnmarshalFieldError deprecated

```
type UnmarshalFieldError struct {
	Key   string
	Type  reflect.Type
	Field reflect.StructField
}
```

An UnmarshalFieldError describes a JSON object key that led to an unexported (and therefore unwritable) struct field.

Deprecated: No longer used; kept for compatibility.

#### func (*UnmarshalFieldError) Error

```
func (e *UnmarshalFieldError) Error() string
```

#### type UnmarshalTypeError

```
type UnmarshalTypeError struct {
	Value  string       
	Type   reflect.Type 
	Offset int64        
	Struct string       
	Field  string       
}
```

An UnmarshalTypeError describes a JSON value that was not appropriate for a value of a specific Go type.

#### func (*UnmarshalTypeError) Error

```
func (e *UnmarshalTypeError) Error() string
```

#### type Unmarshaler

```
type Unmarshaler interface {
	UnmarshalJSON([]byte) error
}
```

Unmarshaler is the interface implemented by types that can unmarshal a JSON description of themselves. The input can be assumed to be a valid encoding of a JSON value. UnmarshalJSON must copy the JSON data if it wishes to retain the data after returning.

#### type UnsupportedTypeError

```
type UnsupportedTypeError struct {
	Type reflect.Type
}
```

An UnsupportedTypeError is returned by Marshal when attempting to encode an unsupported value type.

#### func (*UnsupportedTypeError) Error

```
func (e *UnsupportedTypeError) Error() string
```

#### type UnsupportedValueError

```
type UnsupportedValueError struct {
	Value reflect.Value
	Str   string
}
```

An UnsupportedValueError is returned by Marshal when attempting to encode an unsupported value.

#### func (*UnsupportedValueError) Error

```
func (e *UnsupportedValueError) Error() string
```

## Source Files

View all Source files

- decode.go
- encode.go
- fold.go
- indent.go
- scanner.go
- stream.go
- tables.go
- tags.go

## Directories

| Path | Synopsis |
|---|---|
| jsontext Package jsontext implements syntactic processing of JSON as specified in RFC 4627, RFC 7159, RFC 7493, RFC 8259, and RFC 8785. | Package jsontext implements syntactic processing of JSON as specified in RFC 4627, RFC 7159, RFC 7493, RFC 8259, and RFC 8785. |
| v2 Package json implements semantic processing of JSON as specified in RFC 8259. | Package json implements semantic processing of JSON as specified in RFC 8259. |

Click to show internal directories.

Click to hide internal directories.
