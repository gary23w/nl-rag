---
title: "Types (part 3/3)"
source: https://docs.soliditylang.org/en/latest/types.html
domain: solidity-lang
license: GPL-3.0 (soliditylang.org)
tags: solidity, solidity contract, solidity types, contract inheritance
fetched: 2026-07-02
part: 3/3
---

## Conversions between Literals and Elementary Types

### Integer Types

Decimal and hexadecimal number literals can be implicitly converted to any integer type that is large enough to represent it without truncation:

open in Remix

```solidity
uint8 a = 12; // fine
uint32 b = 1234; // fine
uint16 c = 0x123456; // fails, since it would have to truncate to 0x3456
```

Note

Prior to version 0.8.0, any decimal or hexadecimal number literals could be explicitly converted to an integer type. From 0.8.0, such explicit conversions are as strict as implicit conversions, i.e., they are only allowed if the literal fits in the resulting range.

### Fixed-Size Byte Arrays

Decimal number literals cannot be implicitly converted to fixed-size byte arrays. Hexadecimal number literals can be, but only if the number of hex digits exactly fits the size of the bytes type. As an exception both decimal and hexadecimal literals which have a value of zero can be converted to any fixed-size bytes type:

open in Remix

```solidity
bytes2 a = 54321; // not allowed
bytes2 b = 0x12; // not allowed
bytes2 c = 0x123; // not allowed
bytes2 d = 0x1234; // fine
bytes2 e = 0x0012; // fine
bytes4 f = 0; // fine
bytes4 g = 0x0; // fine
```

String literals and hex string literals can be implicitly converted to fixed-size byte arrays, if their number of characters is less than or equal to the size of the bytes type:

open in Remix

```solidity
bytes2 a = hex"1234"; // fine
bytes2 b = "xy"; // fine
bytes2 c = hex"12"; // fine
bytes2 e = "x"; // fine
bytes2 f = "xyz"; // not allowed
```

### Addresses

As described in Address Literals, hex literals of the correct size that pass the checksum test are of `address` type. No other literals can be implicitly converted to the `address` type.

Explicit conversions to `address` are allowed only from `bytes20` and `uint160`.

An `address a` can be converted explicitly to `address payable` via `payable(a)`.

Note

Prior to version 0.8.0, it was possible to explicitly convert from any integer type (of any size, signed or unsigned) to `address` or `address payable`. Starting with 0.8.0 only conversion from `uint160` is allowed.
