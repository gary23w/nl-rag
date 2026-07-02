---
title: "Field (computer science)"
source: https://en.wikipedia.org/wiki/Field_(computer_science)
domain: attrs-classes
license: CC-BY-SA-4.0
tags: python attrs, attrs classes library, boilerplate class python
fetched: 2026-07-02
---

# Field (computer science)

In data hierarchy, a **field** (**data field**) is a variable in a record. A record, also known as a data structure, allows logically related data to be identified by a single name. Identifying related data as a single group is central to the construction of understandable computer programs. The individual fields in a record may be accessed by name, just like any variable in a computer program.

Each field in a record has two components. One component is the field's datatype declaration. The other component is the field's identifier.

## Memory fields

Fields may be stored in random access memory (RAM). The following Pascal record definition has three field identifiers: firstName, lastName, and age. The two name fields have a datatype of an array of character. The age field has a datatype of integer.

```mw
type PersonRecord =
    record
        lastName : array [ 1 .. 20 ] of Char;
        firstName : array [ 1 .. 20 ] of Char;
        age : Integer
    end;
```

In Pascal, the identifier component precedes a colon, and the datatype component follows the colon. Once a record is defined, variables of the record can be allocated. Once the memory of the record is allocated, a field can be accessed like a variable by using the dot notation.

```mw
var alice : PersonRecord;
alice.firstName := 'Alice';
```

Over time, the term *field* has been replaced with the terms *data member* and *attribute*. The following Java class has three attributes: firstName, lastName, and age.

```mw
public class PersonRecord
{
	private String firstName;
	private String lastName;
	private int age;
}
```

## File fields

Fields may be stored in a random access file. A file may be written to or read from in an arbitrary order. To accomplish the arbitrary access, the operating system provides a method to quickly *seek* around the file. Once the disk head is positioned at the beginning of a record, each file field can be read into its corresponding memory field.

File fields are the main storage structure in the Indexed Sequential Access Method (ISAM). In relational database theory, the term *field* has been replaced with the terms *column* and *attribute*.
