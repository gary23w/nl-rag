---
title: "100 doors (part 4/10)"
source: https://rosettacode.org/wiki/100_doors
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 4/10
---

## Dart

**unoptimized**

```mw
main() {
    for (var k = 1, x = new List(101); k <= 100; k++) {
        for (int i = k; i <= 100; i += k)
            x[i] = !x[i];
        if (x[k]) print("$k open");
    }
}
```

Works with

:

Dart

version SDK 3.6.1

```
main() {
    var x = List.filled(101,false);
    for (var k = 1; k <= 100; k++) {
        for (int i = k; i <= 100; i += k)
            x[i] = !x[i];
        if (x[k]) print("$k open");
    }
}
```

**optimized version** (including generating squares without multiplication)

```mw
main() {
  for(int i=1,s=3;i<=100;i+=s,s+=2)
    print("door $i is open");
}
```

**comprehensible (not "code golf") version for a pedestrian language**

```mw
import 'dart:io';

final numDoors = 100;
final List<bool> doorClosed = List(numDoors);

String stateToString(String message) {
  var res = '';
  for (var i = 0; i < numDoors; i++) {
    res += (doorClosed[i] ? 'X' : '\u2610');
  }
  return res + " " + message;
}

main() {
  for (var i = 0; i < numDoors; i++) {
    doorClosed[i] = true;
  }
  stdout.writeln(stateToString("after initialization"));
  for (var step = 1; step <= numDoors; step++) {
    final start = step - 1;
    for (var i = start; i < numDoors; i += step) {
      doorClosed[i] = !doorClosed[i];
    }
    stdout.writeln(stateToString("after toggling with step = $step"));
  }
}
```

```
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX after initialization
☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐ after toggling with step = 1
☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X☐X after toggling with step = 2
☐XXX☐☐☐XXX☐☐☐XXX☐☐☐XXX☐☐☐XXX☐☐☐XXX☐☐☐XXX☐☐☐XXX☐☐☐XXX☐☐☐XXX☐☐☐XXX☐☐☐XXX☐☐☐XXX☐☐☐XXX☐☐☐XXX☐☐☐XXX☐☐☐XXX after toggling with step = 3
☐XX☐☐☐☐☐XX☐X☐XX☐☐☐☐☐XX☐X☐XX☐☐☐☐☐XX☐X☐XX☐☐☐☐☐XX☐X☐XX☐☐☐☐☐XX☐X☐XX☐☐☐☐☐XX☐X☐XX☐☐☐☐☐XX☐X☐XX☐☐☐☐☐XX☐X☐XX☐ after toggling with step = 4
☐XX☐X☐☐☐X☐☐X☐X☐☐☐☐☐XXX☐XXXX☐☐X☐☐XXXX☐XXX☐☐☐☐☐X☐X☐☐X☐☐☐X☐XX☐☐☐XX☐X☐☐☐X☐☐X☐X☐☐☐☐☐XXX☐XXXX☐☐X☐☐XXXX☐XXX after toggling with step = 5
☐XX☐XX☐☐X☐☐☐☐X☐☐☐X☐XXX☐☐XXX☐☐☐☐☐XXX☐☐XXX☐X☐☐☐X☐☐☐☐X☐☐XX☐XX☐X☐XX☐XX☐☐X☐☐☐☐X☐☐☐X☐XXX☐☐XXX☐☐☐☐☐XXX☐☐XXX after toggling with step = 6
☐XX☐XXX☐X☐☐☐☐☐☐☐☐X☐X☐X☐☐XXXX☐☐☐☐XX☐☐☐XXX☐☐☐☐☐X☐☐X☐X☐☐XXXXX☐X☐X☐☐XX☐☐XX☐☐☐X☐☐XX☐XXX☐XXXX☐☐☐X☐XXX☐☐☐XX after toggling with step = 7
☐XX☐XXXXX☐☐☐☐☐☐X☐X☐X☐X☐XXXXX☐☐☐XXX☐☐☐XX☐☐☐☐☐☐X☐XX☐X☐☐XX☐XX☐X☐X☐XXX☐☐XX☐X☐X☐☐XX☐☐XX☐XXXXX☐☐X☐XXXX☐☐XX after toggling with step = 8
☐XX☐XXXX☐☐☐☐☐☐☐X☐☐☐X☐X☐XXX☐X☐☐☐XXX☐X☐XX☐☐☐☐☐XX☐XX☐X☐☐☐X☐XX☐X☐XXXXX☐☐XX☐☐☐X☐☐XX☐☐☐X☐XXXXX☐XX☐XXXX☐☐☐X after toggling with step = 9
☐XX☐XXXX☐X☐☐☐☐☐X☐☐☐☐☐X☐XXX☐X☐X☐XXX☐X☐XXX☐☐☐☐XX☐XXXX☐☐☐X☐XX☐☐☐XXXXX☐☐X☐☐☐☐X☐☐XX☐X☐X☐XXXXX☐☐X☐XXXX☐☐☐☐ after toggling with step = 10
☐XX☐XXXX☐XX☐☐☐☐X☐☐☐☐☐☐☐XXX☐X☐X☐X☐X☐X☐XXX☐☐☐XXX☐XXXX☐☐☐☐☐XX☐☐☐XXXX☐☐☐X☐☐☐☐X☐☐☐X☐X☐X☐XXXX☐☐☐X☐XXXX☐☐X☐ after toggling with step = 11
☐XX☐XXXX☐XXX☐☐☐X☐☐☐☐☐☐☐☐XX☐X☐X☐X☐X☐☐☐XXX☐☐☐XXX☐☐XXX☐☐☐☐☐XX☐X☐XXXX☐☐☐X☐☐X☐X☐☐☐X☐X☐X☐☐XXX☐☐☐X☐XXX☐☐☐X☐ after toggling with step = 12
☐XX☐XXXX☐XXXX☐☐X☐☐☐☐☐☐☐☐X☐☐X☐X☐X☐X☐☐☐X☐X☐☐☐XXX☐☐XXXX☐☐☐☐XX☐X☐XXX☐☐☐☐X☐☐X☐X☐☐☐☐☐X☐X☐☐XXX☐☐☐☐☐XXX☐☐☐X☐ after toggling with step = 13
☐XX☐XXXX☐XXXXX☐X☐☐☐☐☐☐☐☐X☐☐☐☐X☐X☐X☐☐☐X☐X☐X☐XXX☐☐XXXX☐☐☐XXX☐X☐XXX☐☐☐☐XX☐X☐X☐☐☐☐☐X☐X☐XXXX☐☐☐☐☐XXX☐☐XX☐ after toggling with step = 14
☐XX☐XXXX☐XXXXXXX☐☐☐☐☐☐☐☐X☐☐☐☐☐☐X☐X☐☐☐X☐X☐X☐X☐X☐☐XXXX☐☐☐XXX☐☐☐XXX☐☐☐☐XX☐X☐XX☐☐☐☐X☐X☐XXXX☐☐X☐☐XXX☐☐XX☐ after toggling with step = 15
☐XX☐XXXX☐XXXXXX☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐X☐☐☐X☐X☐X☐X☐X☐XXXXX☐☐☐XXX☐☐☐XX☐☐☐☐☐XX☐X☐XX☐☐☐☐☐☐X☐XXXX☐☐X☐☐XXXX☐XX☐ after toggling with step = 16
☐XX☐XXXX☐XXXXXX☐X☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐X☐X☐X☐X☐X☐XXX☐X☐☐☐XXX☐☐☐XX☐☐☐☐XXX☐X☐XX☐☐☐☐☐☐X☐X☐XX☐☐X☐☐XXXX☐XX☐ after toggling with step = 17
☐XX☐XXXX☐XXXXXX☐XX☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐X☐X☐X☐X☐X☐X☐XXX☐X☐X☐XXX☐☐☐XX☐☐☐☐XXX☐☐☐XX☐☐☐☐☐☐X☐X☐XX☐☐☐☐☐XXXX☐XX☐ after toggling with step = 18
☐XX☐XXXX☐XXXXXX☐XXX☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐X☐☐☐X☐X☐X☐X☐XXX☐X☐X☐X☐X☐☐☐XX☐☐☐☐XXX☐☐☐XXX☐☐☐☐☐X☐X☐XX☐☐☐☐☐XX☐X☐XX☐ after toggling with step = 19
☐XX☐XXXX☐XXXXXX☐XXXX☐☐☐☐X☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐X☐X☐X☐XXX☐X☐X☐X☐X☐X☐XX☐☐☐☐XXX☐☐☐XXX☐☐☐X☐X☐X☐XX☐☐☐☐☐XX☐X☐XXX after toggling with step = 20
☐XX☐XXXX☐XXXXXX☐XXXXX☐☐☐X☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐X☐X☐XXX☐X☐X☐X☐X☐X☐X☐☐☐☐☐XXX☐☐☐XXX☐☐☐X☐X☐☐☐XX☐☐☐☐☐XX☐X☐XXX after toggling with step = 21
☐XX☐XXXX☐XXXXXX☐XXXXXX☐☐X☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐X☐XXX☐X☐X☐X☐X☐X☐X☐☐☐X☐XXX☐☐☐XXX☐☐☐X☐X☐☐☐XXX☐☐☐☐XX☐X☐XXX after toggling with step = 22
☐XX☐XXXX☐XXXXXX☐XXXXXXX☐X☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐XXX☐X☐X☐X☐X☐X☐X☐☐☐X☐X☐X☐☐☐XXX☐☐☐X☐X☐☐☐XXX☐☐☐XXX☐X☐XXX after toggling with step = 23
☐XX☐XXXX☐XXXXXX☐XXXXXXXXX☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐XX☐X☐X☐X☐X☐X☐X☐☐☐X☐X☐X☐X☐XXX☐☐☐X☐X☐☐☐XXX☐☐☐XXX☐☐☐XXX after toggling with step = 24
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐X☐☐X☐X☐X☐X☐X☐X☐☐☐X☐X☐X☐X☐X☐X☐☐☐X☐X☐☐☐XXX☐☐☐XXX☐☐☐XX☐ after toggling with step = 25
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐X☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐X☐X☐X☐X☐X☐☐☐X☐X☐X☐X☐X☐X☐X☐X☐X☐☐☐XXX☐☐☐XXX☐☐☐XX☐ after toggling with step = 26
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XX☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐X☐X☐X☐X☐☐☐X☐X☐X☐X☐X☐X☐X☐XXX☐☐☐XXX☐☐☐XXX☐☐☐XX☐ after toggling with step = 27
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXX☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐X☐X☐X☐☐☐X☐X☐X☐X☐X☐X☐X☐XXX☐X☐XXX☐☐☐XXX☐☐☐XX☐ after toggling with step = 28
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXX☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐X☐X☐☐☐X☐X☐X☐X☐X☐X☐X☐XXX☐X☐X☐X☐☐☐XXX☐☐☐XX☐ after toggling with step = 29
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXX☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐X☐X☐X☐X☐X☐X☐X☐XXX☐X☐X☐X☐X☐XXX☐☐☐XX☐ after toggling with step = 30
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXX☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐X☐X☐X☐X☐X☐X☐XXX☐X☐X☐X☐X☐X☐X☐☐☐XX☐ after toggling with step = 31
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXX☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐X☐X☐X☐X☐X☐X☐X☐XXX☐X☐X☐X☐X☐X☐X☐X☐XX☐ after toggling with step = 32
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXX☐☐X☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐X☐X☐X☐X☐X☐X☐XXX☐X☐X☐X☐X☐X☐X☐X☐X☐☐ after toggling with step = 33
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXX☐X☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐X☐X☐X☐X☐X☐XXX☐X☐X☐X☐X☐X☐X☐X☐X☐☐ after toggling with step = 34
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXXX☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐X☐X☐X☐X☐XXX☐X☐X☐X☐X☐X☐X☐X☐X☐☐ after toggling with step = 35
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐X☐X☐X☐XXX☐X☐X☐X☐X☐X☐X☐X☐X☐☐ after toggling with step = 36
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐X☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐X☐X☐XXX☐X☐X☐X☐X☐X☐X☐X☐X☐☐ after toggling with step = 37
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XX☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐X☐XXX☐X☐X☐X☐X☐X☐X☐X☐X☐☐ after toggling with step = 38
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXX☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐XXX☐X☐X☐X☐X☐X☐X☐X☐X☐☐ after toggling with step = 39
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXX☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐XX☐X☐X☐X☐X☐X☐X☐X☐X☐☐ after toggling with step = 40
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXX☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐X☐X☐X☐X☐X☐X☐X☐X☐☐ after toggling with step = 41
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXX☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐X☐X☐X☐X☐X☐X☐X☐☐ after toggling with step = 42
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXX☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐X☐X☐X☐X☐X☐X☐☐ after toggling with step = 43
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXX☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐X☐X☐X☐X☐X☐☐ after toggling with step = 44
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXX☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐X☐X☐X☐X☐☐ after toggling with step = 45
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXX☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐X☐X☐X☐☐ after toggling with step = 46
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXX☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐X☐☐ after toggling with step = 47
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXXX☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐ after toggling with step = 48
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐ after toggling with step = 49
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐X☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 50
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XX☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 51
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXX☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 52
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXX☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 53
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXX☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 54
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXX☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 55
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXX☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 56
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXX☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 57
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXX☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 58
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXX☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 59
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXX☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 60
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXX☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 61
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXX☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 62
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXXX☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 63
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 64
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 65
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XX☐☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 66
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXX☐☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 67
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXX☐☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 68
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXX☐☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 69
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXX☐☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 70
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXX☐☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 71
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXX☐☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 72
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXX☐☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 73
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXX☐☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 74
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXX☐☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 75
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXX☐☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 76
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXX☐☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 77
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXX☐☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 78
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXX☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 79
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXXX☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 80
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 81
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐X☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 82
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐XX☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 83
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐XXX☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 84
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐XXXX☐☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 85
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐XXXXX☐☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 86
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐XXXXXX☐☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 87
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐XXXXXXX☐☐☐☐☐☐☐☐☐☐☐X after toggling with step = 88
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐XXXXXXXX☐☐☐☐☐☐☐☐☐☐X after toggling with step = 89
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐XXXXXXXXX☐☐☐☐☐☐☐☐☐X after toggling with step = 90
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐XXXXXXXXXX☐☐☐☐☐☐☐☐X after toggling with step = 91
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐XXXXXXXXXXX☐☐☐☐☐☐☐X after toggling with step = 92
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐XXXXXXXXXXXX☐☐☐☐☐☐X after toggling with step = 93
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐XXXXXXXXXXXXX☐☐☐☐☐X after toggling with step = 94
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐XXXXXXXXXXXXXX☐☐☐☐X after toggling with step = 95
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐XXXXXXXXXXXXXXX☐☐☐X after toggling with step = 96
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐☐X after toggling with step = 97
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXXX☐X after toggling with step = 98
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXXXXX after toggling with step = 99
☐XX☐XXXX☐XXXXXX☐XXXXXXXX☐XXXXXXXXXX☐XXXXXXXXXXXX☐XXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXX☐XXXXXXXXXXXXXXXXXX☐ after toggling with step = 100
```


## Dc

**Unoptimized**:

Works with

:

GNU dc

version 1.3.95

```mw

## NB: This code uses the dc command "r" via register "r".

##     You may comment out the unwanted version.
[SxSyLxLy]sr    # this should work with every "dc"
[r]sr           # GNU dc can exchange top 2 stack values by "r"

## Now use "lrx" instead of "r" ...

0k              # we work without decimal places
[q]sq           # useful e.g. as loop termination


## (x)(y)>R  ==  if (y)>(x) eval R

## isle         x y --> (x <= y)
[
    [1q]S. [ !<. 0 ]x s.L.
]sl

## l: isle

[
    100 llx
]sL

## L: isle100


## for  initcode condcode incrcode body

##       [1]      [2]      [3]      [4]
[
    [q]S. 4:. 3:. 2:. 1:.  1;.x [2;.x 0=. 4;.x 3;.x 0;.x]d0:.x Os.L.o
]sf

## f: for
##----------------------------------------------------------------------------


##      for( i=1 ; i<=100 ; ++i ) {

##          door[i] = 0;

##      }
#[init ...]P []ps-
[1si] [li lLx] [li1+si] [
    li 0:d
]lfx


##      for( s=1 ; s<=100 ; ++s ) {

##          for( i=s ; i<=100 ; i+=s ) {

##              door[i] = 1 - door[i]

##          }

##      }
[1ss] [ls lLx] [ls1+ss] [
    #[step ]P lsn [ ...]ps-
    [lssi] [li lLx] [lils+si] [
        1 li;d - li:d
    ]lfx
]lfx


##      long output:

##          for( i=1 ; i<=100 ; ++i ) {

##              print "door #", i, " is ", (door[i] ? "open" : "closed")), NL

##          }
[
    [1si] [li lLx] [li1+si] [
        [door #]P
        li n
        [ is ]P
            [closed]
            [open]
        li;d 0=r lrx s- n
        [.]ps-
    ]lfx
]


##      terse output:

##          for( i=1 ; i<=100 ; ++i ) {

##              if( door[i] ) {

##                  print i

##              }

##              print NL

##          }
[
    [1si] [li lLx] [li1+si] [
        [] [ [ ]n lin ]
        li;d 0=r lrx s- x
    ]lfx
    []ps-
]

lrx             # comment out for the long output version
s- x
#[stack rest...]P []ps- f
```

Output:

```
 1 4 9 16 25 36 49 64 81 100
```


## DCL

**Adapted from optimized Batch example**

```mw
$! doors.com
$! Excecute by running @doors at prompt.
$ square = 1
$ incr = 3
$ count2 = 0
$ d = 1
$ LOOP2:
$       count2 = count2 + 1
$       IF (d .NE. square)
$               THEN WRITE SYS$OUTPUT "door ''d' is closed"
$       ELSE WRITE SYS$OUTPUT "door ''d' is open"
$               square = incr + square
$               incr = incr + 2
$       ENDIF
$       d = d + 1
$       IF (count2 .LT. 100) THEN GOTO LOOP2
```


## Delphi

See

Pascal


## Draco

```mw
proc nonrec main() void:
    byte DOORS = 100;
    [DOORS+1] bool door_open;
    unsigned DOORS i, j;

    /* make sure all doors are closed */
    for i from 1 upto DOORS do door_open[i] := false od;

    /* pass through the doors */
    for i from 1 upto DOORS do
        for j from i by i upto DOORS do
            door_open[j] := not door_open[j]
        od
    od;

    /* show the open doors */
    for i from 1 upto DOORS do
        if door_open[i] then
            writeln("Door ", i, " is open.")
        fi
    od
corp
```

**Output:**

```
Door 1 is open.
Door 4 is open.
Door 9 is open.
Door 16 is open.
Door 25 is open.
Door 36 is open.
Door 49 is open.
Door 64 is open.
Door 81 is open.
Door 100 is open.
```


## DuckDB

Works with

:

DuckDB

version V1.1

This entry illustrates how a simulation can be performed using a recursive Common Table Expression (CTE). This is ostensibly expensive in terms of memory requirements but DuckDB is free to optimize.

```mw
# Show the state of n doors after n iterations
create or replace function doors(n) as (
  with recursive cte(ix,d) as (
    select 0 as ix, list_transform(range(0, n), x -> false) as d
    union all
    select ix+1,
           list_transform(d, (x,i) -> if (i % (ix + 1) = 0, NOT x, x))
    from cte
    where ix < n
  )
  select last(d order by ix)
  from cte
);

# For brevity, we just show the indices of the doors that are open after all
# have been visited:
select ix
from (select unnest(generate_series(1,100)) as ix, unnest(doors(100)) as d)
where d = true;
```

**Output:**

```
┌───────┐
│  ix   │
│ int64 │
├───────┤
│     1 │
│     4 │
│     9 │
│    16 │
│    25 │
│    36 │
│    49 │
│    64 │
│    81 │
│   100 │
└───────┘
```


## DUP

```mw
100[$][0^:1-]#                                                  {initialize doors}
%
[s;[$101<][$$;~\:s;+]#%]d:                                     {function d, switch door state function}
1s:[s;101<][d;!s;1+s:]#                                        {increment step width from 1 to 100, execute function d each time}
1[$101<][$$.' ,;['o,'p,'e,'n,10,]['c,'l,'o,'s,'e,'d,10,]?1+]#  {loop through doors, print door number and state}
```

Result:

```mw
1 open
2 closed
3 closed
4 open
5 closed
6 closed
7 closed
8 closed
9 open
10 closed
11 closed
12 closed
...
94 closed
95 closed
96 closed
97 closed
98 closed
99 closed
100 open
```

Compare this solution to the FALSE solution of this problem.


## DWScript

**Unoptimized**

```mw
var doors : array [1..100] of Boolean;
var i, j : Integer;

for i := 1 to 100 do
   for j := i to 100 do
      if (j mod i) = 0 then
         doors[j] := not doors[j];F

for i := 1 to 100 do
   if doors[i] then
      PrintLn('Door '+IntToStr(i)+' is open');
```


## Dyalect

Outputs only open doors to save up space:

```mw
var doors = Array.Empty(100, false)
 
for p in 0..99 {
    for d in 0..99 {
        if (d + 1) % (p + 1) == 0 {
            doors[d] = !doors[d];
        }
    }
}
 
for d in doors.Indices() when doors[d] {
    print("Door \(d+1): Open")
}
```

**Output:**

```
Door 1: Open
Door 4: Open
Door 9: Open
Door 16: Open
Door 25: Open
Door 36: Open
Door 49: Open
Door 64: Open
Door 81: Open
Door 100: Open
```


## Dylan

**Unoptimized**

```mw
define function doors ()
  let n = 100;
  let doors = make(<vector>, size: n, fill: #f);
  for (x from 0 below n)
    for (y from x below n by x + 1)
      doors[y] := ~doors[y]
    end
  end;
  format-out("open: ");
  for (x from 0 below n) 
    if (doors[x]) 
      format-out("%d ", x + 1)
    end
  end
end function;
```

**Result:**

open: 1 4 9 16 25 36 49 64 81 100


## Déjà Vu

```mw
local :open-doors [ rep 101 false ]

for i range 1 100:
	local :j i
	while <= j 100:
		set-to open-doors j not open-doors! j
		set :j + j i

!print\ "Open doors: "
for i range 1 100:
	if open-doors! i:
		!print\( to-str i " " )
```

**Output:**

```
Open doors: 1 4 9 16 25 36 49 64 81 100 
```


## E

**Graphical**

Works with

:

E-on-Java

This version animates the changes of the doors (as checkboxes).

```mw
#!/usr/bin/env rune

var toggles := []
var gets := []

# Set up GUI (and data model)
def frame := <swing:makeJFrame>("100 doors")
frame.getContentPane().setLayout(<awt:makeGridLayout>(10, 10))
for i in 1..100 {
  def component := <import:javax.swing.makeJCheckBox>(E.toString(i))
  toggles with= fn { component.setSelected(!component.isSelected()) }
  gets with= fn { component.isSelected() }
  frame.getContentPane().add(component)
}

# Set up termination condition
def done
frame.addWindowListener(def _ {
  to windowClosing(event) {
    bind done := true
  }
  match _ {}
})

# Open and close doors
def loop(step, i) {
  toggles[i] <- ()
  def next := i + step
  timer.whenPast(timer.now() + 10, fn {
    if (next >= 100) {
      if (step >= 100) {
        # Done.
      } else {
        loop <- (step + 1, step)
      }
    } else {
      loop <- (step, i + step)
    }    
  })
}
loop(1, 0)

frame.pack()
frame.show()
interp.waitAtTop(done)
```


## EasyLang

```mw
len d[] 100
for p = 1 to 100
   i = p
   while i <= 100
      d[i] = 1 - d[i]
      i += p
   .
.
for i = 1 to 100
   if d[i] = 1 : write i & " "
.
```

**Output:**

```
1 4 9 16 25 36 49 64 81 100 
```


## EchoLisp

The result is obviously the same in we run the process backwards. So, we check the state of each door during the 100-th step (opening/closing every door)

```mw
; initial state = closed = #f
(define doors (make-vector 101 #f))
; run pass 100 to 1
(for* 
   ((pass (in-range 100 0 -1)) 
   (door (in-range 0 101 pass))) 
    (when (and 
        (vector-set! doors door (not (vector-ref doors door))) 
        (= pass 1)) 
        (writeln door "is open"))) 

1     "is open"    
4     "is open"    
9     "is open"    
16     "is open"    
25     "is open"    
36     "is open"    
49     "is open"    
64     "is open"    
81     "is open"    
100     "is open"
```


## ECL

**optimized version**

```mw
Doors := RECORD
 UNSIGNED1 DoorNumber;
 STRING6   State;
END;

AllDoors := DATASET([{0,0}],Doors);

Doors  OpenThem(AllDoors L,INTEGER Cnt) := TRANSFORM
 SELF.DoorNumber := Cnt;
 SELF.State      := IF((CNT * 10) % (SQRT(CNT)*10)<>0,'Closed','Opened');
END;

OpenDoors := NORMALIZE(AllDoors,100,OpenThem(LEFT,COUNTER));
 
OpenDoors;
```

**unoptimized version - demonstrating LOOP**

```mw
Doors := RECORD
  UNSIGNED1 DoorNumber;
  STRING6   State;
END;

AllDoors := DATASET([{0,'0'}],Doors);

//first build the 100 doors

Doors  OpenThem(AllDoors L,INTEGER Cnt) := TRANSFORM
  SELF.DoorNumber := Cnt;
  SELF.State      := 'Closed';
END;

ClosedDoors := NORMALIZE(AllDoors,100,OpenThem(LEFT,COUNTER));

//now iterate through them and use door logic

loopBody(DATASET(Doors) ds, UNSIGNED4 c) :=
            PROJECT(ds,    //ds=original input
              TRANSFORM(Doors,
                      	SELF.State := CASE((COUNTER % c) * 100,
		                            0 => IF(LEFT.STATE = 'Opened','Closed','Opened')
					    ,LEFT.STATE);
			SELF.DoorNumber := COUNTER;     //PROJECT COUNTER
                    ));
   
g1 := LOOP(ClosedDoors,100,loopBody(ROWS(LEFT),COUNTER));
   
OUTPUT(g1);
```

**unoptimized version - using ITERATE** This is a bit more efficient than the LOOP version

```mw
DoorSet := DATASET(100,TRANSFORM({UNSIGNED1 DoorState},SELF.DoorState := 1));
SetDoors := SET(DoorSet,DoorState);

Doors := RECORD
  UNSIGNED1 Pass;
  SET OF UNSIGNED1 DoorSet;
END;

StartDoors := DATASET(100,TRANSFORM(Doors,SELF.Pass := COUNTER,SELF.DoorSet := SetDoors));

Doors XF(Doors L, Doors R) := TRANSFORM
  ds := DATASET(L.DoorSet,{UNSIGNED1 DoorState});
  NextDoorSet := PROJECT(ds,  
                         TRANSFORM({UNSIGNED1 DoorState},
                      	           SELF.DoorState := CASE((COUNTER % R.Pass) * 100,
                                                          0 => IF(LEFT.DoorState = 1,0,1),
                                                          LEFT.DoorState)));
  SELF.DoorSet := IF(L.Pass=0,R.DoorSet,SET(NextDoorSet,DoorState));									
  SELF.Pass := R.Pass										
END;										
 
Res := DATASET(ITERATE(StartDoors,XF(LEFT,RIGHT))[100].DoorSet,{UNSIGNED1 DoorState});
PROJECT(Res,TRANSFORM({STRING20 txt},SELF.Txt := 'Door ' + COUNTER + ' is ' + IF(LEFT.DoorState=1,'Open','Closed')));
```


## Ecstasy

```mw
module OneHundredDoors {
    void run() {
        Boolean[] doors = new Boolean[100];
        for (Int pass : 0 ..< 100) {
            for (Int door = pass; door < 100; door += 1+pass) {
                doors[door] = !doors[door];
            }
        }

        @Inject Console console;
        console.print($|open doors: {doors.mapIndexed((d, i) -> d ? i+1 : 0)
                       |                  .filter(i -> i > 0)}
                     );
    }
}
```

**Output:**

```
open doors: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
```


## EDSAC order code

Since there are only 100 doors, we'll keep things simple and use a whole EDSAC location for each door. A single bit would be enough, but that would make the code much longer.

The program works through the array of doors by modifying its own orders (instructions). This would be considered bad practice today, but was quite usual on the EDSAC.

```mw
[Hundred doors problem from Rosetta Code website]
[EDSAC program, Initial Orders 2]

[Library subroutine M3. Prints header and is then overwritten.
Here, the last character sets the teleprinter to figures.]
       PFGKIFAFRDLFUFOFE@A6FG@E8FEZPF
       @&*THE!OPEN!DOORS!ARE@&#
       ..PZ   [blank tape, needed to mark end of header text]

[Library subroutine P6. Prints strictly positive integer.
32 locations; working locations 1, 4, 5]
        T56K  [define load address for subroutine]
        GKA3FT25@H29@VFT4DA3@TFH30@S6@T1F
        V4DU4DAFG26@TFTFO5FA4DF4FS4F
        L4FT4DA1FS3@G9@EFSFO31@E20@J995FJF!F

        T88K   [define load address for main program]
        GK     [set @ (theta) for relative addresses]

[The 100 doors are at locations 200..299.
Doors are numbered 0..99 internally, and 1..100 for output.
The base address and the number of doors can be varied.
The value of a door is 0 if open, negative if closed.]

                   [Constants. Program also uses order 'P 1 F'
                    which is permanently at absolute address 2.]
    [0] P200F  [address of door #0]
    [1] P100F  [number of doors, as an address]
    [2] UF     [makes S order from T, since 'S' = 'T' + 'U']
    [3] MF     [makes A order from T, since 'A' = 'T' + 'M']
    [4] V2047D [all 1's for "closed" (any negative value will do)]
    [5] &F     [line feed]
    [6] @F     [carriage return]
    [7] K4096F [teleprinter null[

                   [Variables]
    [8] PF   [pass number; step when toggling doors]
    [9] PF   [door number, as address, 0-based]
   [10] PF   [order referring to door 0]

                   [Enter with acc = 0]
                   [Part 1 : close all the doors]
   [11] T8@  [pass := 0 (used in part 2)]
        T9@  [door number := 0]
        A16@ [load 'T F' order]
        A@   [add base address]
        T10@ [store T order for door #0]
   [16] TF   [clear acc; also serves as constant]
        A9@  [load door number]
        A10@ [make T order]
        T21@ [plant in code]
        A4@  [load value for "closed"]
   [21] TF   [store in current door]
        A9@  [load door number]
        A2F  [add 1]
        U9@  [update door number]
        S1@  [done all doors yet?]
        G16@ [if not, loop back]

                   [Part 2 : 100 passes, toggling the doors]
   [27] TF   [clear acc]
        A8@  [load pass number]
        A2F  [add 1]
        T8@  [save updated pass number]
        S2F  [make -1]
        U9@  [door number := -1]
        A8@  [add pass number to get first door toggled on this pass]
        S1@  [gone beyond end?]
        E50@ [if so, move on to part 3]
   [36] A1@  [restore acc after test]
        U9@  [store current door number]
        A10@ [make T order to load status]
        U44@ [plant T order for first door in pass]
        A2@  [convert to S order]
        T43@ [plant S order]
        A4@  [load value for "closed"]
   [43] SF   [subtract status; toggles status]
   [44] TF   [update status]
        A9@  [load door number just toggled]
        A8@  [add pass number to get next door in pass]
        S1@  [gone beyond end?]
        G36@ [no, loop to do next door]
        E27@ [yes, loop to do next pass]

                   [Part 3 : Print list of open doors.
                    Header has set teleprinter to figures.]
   [50] TF   [clear acc]
        T9@  [door nr := 0]
        A10@ [T order for door 0]
        A3@  [convert to A order]
        T10@
   [55] TF
        A9@  [load door number]
        A10@ [make A order to load value]
        T59@ [plant in next order]
   [59] AF   [acc := 0 if open, < 0 if closed]
        G69@ [skip if closed]
        A9@  [door number as address]
        A2F  [add 1 for 1-based output]
        RD   [shift 1 right, address --> integer]
        TF   [store integer at 0 for printing]
   [65] A65@ [for return from subroutine]
        G56F [call subroutine to print door number]
        O6@  [followed by CRLF]
        O5@
   [69] TF   [clear acc]
        A9@  [load door number]
        A2F  [add 1]
        U9@  [update door number]
        S1@  [done all doors yet?]
        G55@  [if not, loop back]
   [75] O7@  [output null to flush teleprinter buffer]
        ZF   [stop]
        E11Z [define relative start address]
        PF
```

**Output:**

```
THE OPEN DOORS ARE
    1
    4
    9
   16
   25
   36
   49
   64
   81
  100
```


## Eero

```mw
#import <Foundation/Foundation.h>

int main()
  square := 1, increment = 3

  for int door in 1 .. 100
    printf("door #%d", door)

    if door == square
      puts(" is open.")
      square += increment
      increment += 2
    else
      puts(" is closed.")

  return 0
```


## Egel

```mw
import "prelude.eg"

using System
using List

data open, closed

def toggle =
    [ open N -> closed N | closed N -> open N ]

def doors =
    [ N -> map [ N -> closed N ] (fromto 1 N) ]

def toggleK =
    [ K nil              -> nil
    | K (cons (D N) DD)  -> 
         let DOOR = if (N%K) == 0 then toggle (D N) else D N in
             cons DOOR (toggleK K DD) ]

def toggleEvery =
    [ nil DOORS -> DOORS
    | (cons K KK) DOORS -> toggleEvery KK (toggleK K DOORS) ]

def run =
    [ N -> toggleEvery (fromto 1 N) (doors N) ]

def main = run 100
```


## EGL

```mw
program OneHundredDoors

   function main()

      doors boolean[] = new boolean[100];
      n int = 100;

      for (i int from 1 to n)
         for (j int from i to n by i)
            doors[j] = !doors[j];
         end
      end
             
      for (i int from 1 to n)
         if (doors[i])
            SysLib.writeStdout( "Door " + i + " is open" );
         end
      end
 
   end

end
```


## Eiffel

This is my first RosettaCode submission, as well as a foray into Eiffel for myself. I've tried to adhere to the description of the problem statement, as well as showcase a few Eiffelisms shown in the documentation.

The replacement code below took the original code and has made improvements in some ways, such as:

1. Removal of "magic" many magic numbers and strings.
2. Refactor of various code blocks to routines (commands and queries with good CQS).
3. Utilization/Demonstration of full, secret, and selective feature exporting.
4. Utilization/Demonstration of constants as expanded type constants and once-functions.
5. Utilization/Demonstration of static-references (e.g. {APPLICATION}.min_door_count).
6. Utilization/Demonstration of "like" keyword type anchoring (e.g. a_index_address: like {DOOR}.address).
7. Utilization/Demonstration of semi-strict logical implication (e.g. consistency: is_open implies not Is_closed).
8. Utilization/Demonstration of contracts, including require, ensure, and class invariant.
9. Utilization/Demonstration of agent and `do_all' call on ITERABLE type.
10. Utilization/Demonstration of various forms of across including "loop" and "all".

... as well as other Eiffel-ism's and some coding standards/best-practices.

**file: application.e**

```mw
note
	description: "100 Doors problem"
	date: "08-JUL-2015"
	revision: "1.1"

class
	APPLICATION

create
	make

feature {NONE} -- Initialization

	make
			-- Main application routine.
		do
			initialize_closed_doors
			toggle_doors
			output_door_states
		end

feature -- Access

	doors: ARRAYED_LIST [DOOR]
			-- A set of doors (self-initialized to capacity of `max_door_count').
		attribute
			create Result.make (max_door_count)
		end

feature -- Basic Operations

	initialize_closed_doors
			-- Initialize all `doors'.
		do
			across min_door_count |..| max_door_count as ic_address_list loop
				doors.extend (create {DOOR}.make_closed (ic_address_list.item))
			end
		ensure
			has_all_closed_doors: across doors as ic_doors_list all not ic_doors_list.item.is_open end
		end

	toggle_doors
			-- Toggle all `doors'.
		do
			across min_door_count |..| max_door_count as ic_addresses_list loop
				across doors as ic_doors_list loop
					if is_door_to_toggle (ic_doors_list.item.address, ic_addresses_list.item) then
						ic_doors_list.item.toggle_door
					end
				end
			end
		end

	output_door_states
			-- Output the state of all `doors'.
		do
			doors.do_all (agent door_state_out)
		end

feature -- Status Report

	is_door_to_toggle (a_door_address, a_index_address: like {DOOR}.address): BOOLEAN
			-- Is the door at `a_door_address' needing to be toggled, when compared to `a_index_address'?
		do
			Result := a_door_address \\ a_index_address = 0
		ensure
			only_modulus_zero: Result = (a_door_address \\ a_index_address = 0)
		end

feature -- Outputs

	door_state_out (a_door: DOOR)
			-- Output the state of `a_door'.
		do
			print ("Door " + a_door.address.out + " is ")
			if a_door.is_open then
				print ("open.")
			else
				print ("closed.")
			end
			io.new_line
		end

feature {DOOR} -- Constants

	min_door_count: INTEGER = 1
			-- Minimum number of doors.

	max_door_count: INTEGER = 100
			-- Maximum number of doors.

end
```

**file: door.e**

```mw
note
	description: "A door with an address and an open or closed state."
	date: "08-JUL-2015"
	revision: "1.1"

class
	DOOR

create
	make_closed,
	make

feature {NONE} -- initialization

	make_closed (a_address: INTEGER)
			-- Initialize Current {DOOR} at `a_address' and state of `Is_closed'.
		require
			positive: a_address >= {APPLICATION}.min_door_count and a_address >= Min_door_count
		do
			make (a_address, Is_closed)
		ensure
			closed: is_open = Is_closed
		end

	make (a_address: INTEGER; a_status: BOOLEAN)
			-- Initialize Current {DOOR} with `a_address' and `a_status', denoting position and `is_open' or `Is_closed'.
		require
			positive: a_address >= {APPLICATION}.min_door_count and a_address >= Min_door_count
		do
			address := a_address
			is_open := a_status
		ensure
			address_set: address = a_address
			status_set: is_open = a_status
		end

feature -- access

	address: INTEGER
			-- `address' of Current {DOOR}.

	is_open: BOOLEAN assign set_open
			-- `is_open' (or not) status of Current {DOOR}.

feature -- Setters

	set_open (a_status: BOOLEAN)
			-- Set `status' with `a_status'
		do
			is_open := a_status
		ensure
			open_updated: is_open = a_status
		end

feature {APPLICATION} -- Basic Operations

	toggle_door
			-- Toggle Current {DOOR} from `is_open' to not `is_open'.
		do
			is_open := not is_open
		ensure
			toggled: is_open /= old is_open
		end

feature {NONE} -- Implementation: Constants

	Is_closed: BOOLEAN = False
			-- State of being not `is_open'.

	Min_door_count: INTEGER = 1
			-- Minimum door count.

invariant
	one_or_more: address >= 1
	consistency: is_open implies not Is_closed

end
```


## Ela

**Standard Approach**

```mw
open generic

type Door = Open | Closed
  deriving Show

gate [] _ = []
gate (x::xs) (y::ys) 
  | x == y = Open :: gate xs ys
  | else = Closed :: gate xs ys

run n = gate [1..n] [& k*k \\ k <- [1..]]
```

**Alternate Approach**

```mw
open list
run n = takeWhile (<n) [& k*k \\ k <- [1..]]
```


## Elena

ELENA 6.x :

```mw
import system'routines;
import extensions;

public Program()
{ 
    var Doors := Array.allocate(100).populate::(n=>false);
    for(int i := 0; i < 100; i++)
    {
        for(int j := i; j < 100; j := j + i + 1)
        {
            Doors[j] := Doors[j].Inverted
        }
    };
 
    for(int i := 0; i < 100; i++)
    {
        Console.printLine("Door #",i + 1," :",Doors[i].iif("Open","Closed"))
    };
 
    Console.readChar()
}
```


## Elixir

```mw
defmodule HundredDoors do
  def doors(n \\ 100) do
    List.duplicate(false, n)
  end
  
  def toggle(doors, n) do
    List.update_at(doors, n, &(!&1))
  end
  
  def toggle_every(doors, n) do
    Enum.reduce( Enum.take_every((n-1)..99, n), doors, fn(n, acc) -> toggle(acc, n) end )
  end
end

# unoptimized
final_state = Enum.reduce(1..100, HundredDoors.doors, fn(n, acc) -> HundredDoors.toggle_every(acc, n) end)

open_doors = Enum.with_index(final_state)
             |> Enum.filter_map(fn {door,_} -> door end, fn {_,index} -> index+1 end)

IO.puts "All doors are closed except these: #{inspect open_doors}"

# optimized 
final_state = Enum.reduce(1..10, HundredDoors.doors, fn(n, acc) -> HundredDoors.toggle(acc, n*n-1) end)

open_doors = Enum.with_index(final_state)
             |> Enum.filter_map(fn {door,_} -> door end, fn {_,index} -> index+1 end)

IO.puts "All doors are closed except these: #{inspect open_doors}"
```

**Output:**

```
All doors are closed except these: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```


## Elm

```mw
-- Unoptimized
import List exposing (indexedMap, foldl, repeat, range)
import Html exposing (text)
import Debug exposing (toString)

type Door = Open | Closed

toggle d = if d == Open then Closed else Open

toggleEvery : Int -> List Door -> List Door
toggleEvery k doors = indexedMap 
  (\i door -> if modBy k (i+1) == 0 then toggle door else door)
  doors

n = 100

main = 
  text (toString (foldl toggleEvery (repeat n Closed) (range 1 n)))
```
