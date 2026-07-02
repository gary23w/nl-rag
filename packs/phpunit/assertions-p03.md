---
title: "1. Assertions (part 3/3)"
source: https://docs.phpunit.de/en/11.5/assertions.html
domain: phpunit
license: CC-BY-SA-4.0
tags: phpunit php, php testing, unit testing, test assertions
fetched: 2026-07-02
part: 3/3
---

## Strings

### `assertStringStartsWith()`

`assertStringStartsWith(string $prefix, string $string[, string $message])`

Reports an error identified by `$message` if the `$string` does not start with `$prefix`.

`assertStringStartsNotWith()` is the inverse of this assertion and takes the same arguments.

Example 1.59

Usage of assertStringStartsWith()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class StringStartsWithTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertStringStartsWith('prefix', 'foo');
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/StringStartsWithTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) StringStartsWithTest::testFailure
Failed asserting that 'foo' starts with "prefix".

/path/to/tests/StringStartsWithTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertStringEndsWith()`

`assertStringEndsWith(string $suffix, string $string[, string $message])`

Reports an error identified by `$message` if the `$string` does not end with `$suffix`.

`assertStringEndsNotWith()` is the inverse of this assertion and takes the same arguments.

Example 1.60

Usage of assertStringEndsWith()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class StringEndsWithTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertStringEndsWith('suffix', 'foo');
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/StringEndsWithTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) StringEndsWithTest::testFailure
Failed asserting that 'foo' ends with "suffix".

/path/to/tests/StringEndsWithTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertStringContainsString()`

`assertStringContainsString(string $needle, string $haystack[, string $message])`

Reports an error identified by `$message` if `$needle` is not a substring of `$haystack`.

`assertStringNotContainsString()` is the inverse of this assertion and takes the same arguments.

`assertStringContainsStringIgnoringLineEndings()` takes the same arguments and can be used if line endings should be ignored.

Example 1.61

Usage of assertStringContainsString()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class StringContainsStringTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertStringContainsString('foo', 'bar');
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/StringContainsStringTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) StringContainsStringTest::testFailure
Failed asserting that 'bar' [ASCII](length: 3) contains "foo" [ASCII](length: 3).

/path/to/tests/StringContainsStringTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertStringContainsStringIgnoringCase()`

`assertStringContainsStringIgnoringCase(string $needle, string $haystack[, string $message])`

Reports an error identified by `$message` if `$needle` is not a substring of `$haystack`.

Differences in casing are ignored when `$needle` is searched for in `$haystack`. This also works for Unicode characters with diacritics (accents, umlauts, circumflex, etc.) as long as both strings have the same Normalization Form.

`assertStringNotContainsStringIgnoringCase()` is the inverse of this assertion and takes the same arguments.

Example 1.62

Usage of assertStringContainsStringIgnoringCase()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class StringContainsStringIgnoringCaseTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertStringContainsStringIgnoringCase('foo', 'bar');
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/StringContainsStringIgnoringCaseTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) StringContainsStringIgnoringCaseTest::testFailure
Failed asserting that 'bar' [Encoding ignored](length: 3) contains "foo" [Encoding ignored](length: 3).

/path/to/tests/StringContainsStringIgnoringCaseTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertStringEqualsStringIgnoringLineEndings()`

`assertStringEqualsStringIgnoringLineEndings(string $expected, string $actual[, string $message])`

Reports an error identified by `$message` if the two strings `$expected` and `$actual` are not equal while ignoring line endings.

### `assertMatchesRegularExpression()`

`assertMatchesRegularExpression(string $pattern, string $string[, string $message])`

Reports an error identified by `$message` if `$string` does not match the regular expression `$pattern`.

`assertDoesNotMatchRegularExpression()` is the inverse of this assertion and takes the same arguments.

Example 1.63

Usage of assertMatchesRegularExpression()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class MatchesRegularExpressionTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertMatchesRegularExpression('/foo/', 'bar');
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/MatchesRegularExpressionTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) MatchesRegularExpressionTest::testFailure
Failed asserting that 'bar' matches PCRE pattern "/foo/".

/path/to/tests/MatchesRegularExpressionTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertStringMatchesFormat()`

`assertStringMatchesFormat(string $format, string $string[, string $message])`

Reports an error identified by `$message` if the `$string` does not match the `$format` string.

`assertStringNotMatchesFormat()` is the inverse of this assertion and takes the same arguments.

Example 1.64

Usage of assertStringMatchesFormat()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class StringMatchesFormatTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertStringMatchesFormat('%i', 'foo');
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/StringMatchesFormatTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) StringMatchesFormatTest::testFailure
Failed asserting that string matches format description.
--- Expected
+++ Actual
@@ @@
-%i
+foo

/path/to/tests/StringMatchesFormatTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

The format string may contain the following placeholders:

- `%e`: Represents a directory separator, for example `/` on Linux.
- `%s`: One or more of anything (character or white space) except the end of line character.
- `%S`: Zero or more of anything (character or white space) except the end of line character.
- `%a`: One or more of anything (character or white space) including the end of line character.
- `%A`: Zero or more of anything (character or white space) including the end of line character.
- `%w`: Zero or more white space characters.
- `%i`: A signed integer value, for example `+3142`, `-3142`.
- `%d`: An unsigned integer value, for example `123456`.
- `%x`: One or more hexadecimal character. That is, characters in the range `0-9`, `a-f`, `A-F`.
- `%f`: A floating point number, for example: `3.142`, `-3.142`, `3.142E-10`, `3.142e+10`.
- `%c`: A single character of any sort.
- `%%`: A literal percent character: `%`.

Deprecation: `assertStringNotMatchesFormat()` is deprecated

As of PHPUnit 10.4, the `assertStringNotMatchesFormat()` method is soft-deprecated, meaning its declaration is annotated with `@deprecated` so that IDEs and static analysis tools can warn about its usage.

Starting with PHPUnit 11, using the `assertStringNotMatchesFormat()` method will trigger a deprecation warning. The method will be removed in PHPUnit 12.

### `assertStringMatchesFormatFile()`

`assertStringMatchesFormatFile(string $formatFile, string $string[, string $message])`

Reports an error identified by `$message` if the `$string` does not match the contents of the `$formatFile`.

`assertStringNotMatchesFormatFile()` is the inverse of this assertion and takes the same arguments.

Example 1.65

Usage of assertStringMatchesFormatFile()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class StringMatchesFormatFileTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertStringMatchesFormatFile(
            __DIR__ . '/expected-format.txt',
            'foo',
        );
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/StringMatchesFormatFileTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) StringMatchesFormatFileTest::testFailure
Failed asserting that string matches format description.
--- Expected
+++ Actual
@@ @@
-%i
+foo

/path/to/tests/StringMatchesFormatFileTest.php:8

FAILURES!
Tests: 1, Assertions: 3, Failures: 1.
```

Deprecation: `assertStringNotMatchesFormatFile()` is deprecated

As of PHPUnit 10.4, the `assertStringNotMatchesFormatFile()` method is soft-deprecated, meaning its declaration is annotated with `@deprecated` so that IDEs and static analysis tools can warn about its usage.

Starting with PHPUnit 11, using the `assertStringNotMatchesFormatFile()` method will trigger a deprecation warning. The method will be removed in PHPUnit 12.

### `assertFileMatchesFormat()`

`assertFileMatchesFormat(string $format, string $actualFile[, string $message])`

Reports an error identified by `$message` if the contents of `$actualFile` does not match the `$format` string.

### `assertFileMatchesFormatFile()`

`assertFileMatchesFormat(string $formatFile, string $actualFile[, string $message])`

Reports an error identified by `$message` if the contents of `$actualFile` does not match the contents of the `$formatFile`.

### `assertStringEqualsFile()`

`assertStringEqualsFile(string $expectedFile, string $actualString[, string $message])`

Reports an error identified by `$message` if the file specified by `$expectedFile` does not have `$actualString` as its contents.

`assertStringNotEqualsFile()` is the inverse of this assertion and takes the same arguments.

`assertStringEqualsFileCanonicalizing()` (and `assertStringNotEqualsFileCanonicalizing()`) as well as `assertStringEqualsFileIgnoringCase()` (and `assertStringNotEqualsFileIgnoringCase()`) do for files what `assertEqualsCanonicalizing()` (and `assertNotEqualsCanonicalizing()`) as well as `assertEqualsIgnoringCase()` (and `assertNotEqualsIgnoringCase()`) do for strings.

Example 1.66

Usage of assertStringEqualsFile()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class StringEqualsFileTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertStringEqualsFile(
            __DIR__ . '/expected.txt',
            'actual',
        );
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/StringEqualsFileTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) StringEqualsFileTest::testFailure
Failed asserting that two strings are equal.
--- Expected
+++ Actual
@@ @@
-'expected\n
-'
+'actual'

/path/to/tests/StringEqualsFileTest.php:8

FAILURES!
Tests: 1, Assertions: 2, Failures: 1.
```


## JSON

### `assertJson()`

`assertJson(string $actual[, string $message])`

Reports an error identified by `$message` if the value of `$actual` is not valid JSON.

Example 1.67

Usage of assertJson()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class JsonTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertJson('not-a-json-string');
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/JsonTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) JsonTest::testFailure
Failed asserting that a string is valid JSON (Syntax error, malformed JSON).

/path/to/tests/JsonTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertJsonFileEqualsJsonFile()`

`assertJsonFileEqualsJsonFile(string $expectedFile, string $actualFile[, string $message])`

Reports an error identified by `$message` if the value of `$actualFile` does not match the value of `$expectedFile`.

`assertJsonFileNotEqualsJsonFile()` is the inverse of this assertion and takes the same arguments.

Example 1.68

Usage of assertJsonFileEqualsJsonFile()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class JsonFileEqualsJsonFileTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertJsonFileEqualsJsonFile(
            __DIR__ . '/expected.json',
            __DIR__ . '/actual.json',
        );
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/JsonFileEqualsJsonFileTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) JsonFileEqualsJsonFileTest::testFailure
Failed asserting that '{"mascot":"elephant"}\n
' matches JSON string "{"mascot":"elePHPant"}
".
--- Expected
+++ Actual
@@ @@
 {
-    "mascot": "elePHPant"
+    "mascot": "elephant"
 }

/path/to/tests/JsonFileEqualsJsonFileTest.php:8

FAILURES!
Tests: 1, Assertions: 7, Failures: 1.
```

### `assertJsonStringEqualsJsonFile()`

`assertJsonStringEqualsJsonFile(string $expectedFile, string $actualJson[, string $message])`

Reports an error identified by `$message` if the value of `$actualJson` does not match the value of `$expectedFile`.

`assertJsonStringNotEqualsJsonFile()` is the inverse of this assertion and takes the same arguments.

Example 1.69

Usage of assertJsonStringEqualsJsonFile()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class JsonStringEqualsJsonFileTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertJsonStringEqualsJsonFile(
            __DIR__ . '/expected.json',
            json_encode(['mascot' => 'elephant']),
        );
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/JsonStringEqualsJsonFileTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) JsonStringEqualsJsonFileTest::testFailure
Failed asserting that '{"mascot":"elephant"}' matches JSON string "{"mascot":"elePHPant"}
".
--- Expected
+++ Actual
@@ @@
 {
-    "mascot": "elePHPant"
+    "mascot": "elephant"
 }

/path/to/tests/JsonStringEqualsJsonFileTest.php:8

FAILURES!
Tests: 1, Assertions: 5, Failures: 1.
```

### `assertJsonStringEqualsJsonString()`

`assertJsonStringEqualsJsonString(string $expectedJson, string $actualJson[, string $message])`

Reports an error identified by `$message` if the value of `$actualJson` does not match the value of `$expectedJson`.

`assertJsonStringNotEqualsJsonString()` is the inverse of this assertion and takes the same arguments.

Example 1.70

Usage of assertJsonStringEqualsJsonString()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class JsonStringEqualsJsonStringTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertJsonStringEqualsJsonString(
            json_encode(['mascot' => 'elePHPant']),
            json_encode(['mascot' => 'elephant']),
        );
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/JsonStringEqualsJsonStringTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) JsonStringEqualsJsonStringTest::testFailure
Failed asserting that '{"mascot":"elephant"}' matches JSON string "{"mascot":"elePHPant"}".
--- Expected
+++ Actual
@@ @@
 {
-    "mascot": "elePHPant"
+    "mascot": "elephant"
 }

/path/to/tests/JsonStringEqualsJsonStringTest.php:8

FAILURES!
Tests: 1, Assertions: 3, Failures: 1.
```


## XML

### `assertXmlFileEqualsXmlFile()`

`assertXmlFileEqualsXmlFile(string $expectedFile, string $actualFile[, string $message])`

Reports an error identified by `$message` if the XML document in `$actualFile` is not equal to the XML document in `$expectedFile`.

`assertXmlFileNotEqualsXmlFile()` is the inverse of this assertion and takes the same arguments.

Example 1.71

Usage of assertXmlFileEqualsXmlFile()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class XmlFileEqualsXmlFileTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertXmlFileEqualsXmlFile(
            __DIR__ . '/expected.xml',
            __DIR__ . '/actual.xml',
        );
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/XmlFileEqualsXmlFileTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) XmlFileEqualsXmlFileTest::testFailure
Failed asserting that two DOM documents are equal.
--- Expected
+++ Actual
@@ @@
 <?xml version="1.0"?>
 <foo>
-  <bar/>
+  <baz/>
 </foo>

/path/to/tests/XmlFileEqualsXmlFileTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertXmlStringEqualsXmlFile()`

`assertXmlStringEqualsXmlFile(string $expectedFile, string $actualXml[, string $message])`

Reports an error identified by `$message` if the XML document in `$actualXml` is not equal to the XML document in `$expectedFile`.

`assertXmlStringNotEqualsXmlFile()` is the inverse of this assertion and takes the same arguments.

Example 1.72

Usage of assertXmlStringEqualsXmlFile()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class XmlStringEqualsXmlFileTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertXmlStringEqualsXmlFile(
            __DIR__ . '/expected.xml',
            '<foo><baz/></foo>',
        );
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/XmlStringEqualsXmlFileTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) XmlStringEqualsXmlFileTest::testFailure
Failed asserting that two DOM documents are equal.
--- Expected
+++ Actual
@@ @@
 <?xml version="1.0"?>
 <foo>
-  <bar/>
+  <baz/>
 </foo>

/path/to/tests/XmlStringEqualsXmlFileTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertXmlStringEqualsXmlString()`

`assertXmlStringEqualsXmlString(string $expectedXml, string $actualXml[, string $message])`

Reports an error identified by `$message` if the XML document in `$actualXml` is not equal to the XML document in `$expectedXml`.

`assertXmlStringNotEqualsXmlString()` is the inverse of this assertion and takes the same arguments.

Example 1.73

Usage of assertXmlStringEqualsXmlString()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class XmlStringEqualsXmlStringTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertXmlStringEqualsXmlString(
            '<foo><bar/></foo>',
            '<foo><baz/></foo>',
        );
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/XmlStringEqualsXmlStringTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) XmlStringEqualsXmlStringTest::testFailure
Failed asserting that two DOM documents are equal.
--- Expected
+++ Actual
@@ @@
 <?xml version="1.0"?>
 <foo>
-  <bar/>
+  <baz/>
 </foo>

/path/to/tests/XmlStringEqualsXmlStringTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```


## Filesystem

### `assertDirectoryExists()`

`assertDirectoryExists(string $directory[, string $message])`

Reports an error identified by `$message` if the directory specified by `$directory` does not exist.

`assertDirectoryDoesNotExist()` is the inverse of this assertion and takes the same arguments.

Example 1.74

Usage of assertDirectoryExists()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class DirectoryExistsTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertDirectoryExists('/path/to/directory');
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/DirectoryExistsTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) DirectoryExistsTest::testFailure
Failed asserting that directory "/path/to/directory" exists.

/path/to/tests/DirectoryExistsTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertDirectoryIsReadable()`

`assertDirectoryIsReadable(string $directory[, string $message])`

Reports an error identified by `$message` if the directory specified by `$directory` is not a directory or is not readable.

`assertDirectoryIsNotReadable()` is the inverse of this assertion and takes the same arguments.

Example 1.75

Usage of assertDirectoryIsReadable()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class DirectoryIsReadableTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertDirectoryIsReadable('/path/to/directory');
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/DirectoryIsReadableTest.php
PHPUnit 10.0.11 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.2.3

F

Time: 00:00, Memory: 14.29 MB

There was 1 failure:

1) DirectoryIsReadableTest::testFailure
Failed asserting that "/path/to/directory" is readable.

/path/to/DirectoryIsReadableTest.php:6

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertDirectoryIsWritable()`

`assertDirectoryIsWritable(string $directory[, string $message])`

Reports an error identified by `$message` if the directory specified by `$directory` is not a directory or is not writable.

`assertDirectoryIsNotWritable()` is the inverse of this assertion and takes the same arguments.

Example 1.76

Usage of assertDirectoryIsWritable()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class DirectoryIsReadableTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertDirectoryIsReadable('/path/to/directory');
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/DirectoryIsWritableTest.php
PHPUnit 10.0.11 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.2.3

F

Time: 00:00, Memory: 14.29 MB

There was 1 failure:

1) DirectoryIsWritableTest::testFailure
Failed asserting that "/path/to/directory" is writable.

/path/to/DirectoryIsWritableTest.php:6

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertFileExists()`

`assertFileExists(string $filename[, string $message])`

Reports an error identified by `$message` if the file specified by `$filename` does not exist.

`assertFileDoesNotExist()` is the inverse of this assertion and takes the same arguments.

Example 1.77

Usage of assertFileExists()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class FileExistsTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertFileExists('/path/to/file');
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/FileExistsTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) FileExistsTest::testFailure
Failed asserting that file "/path/to/file" exists.

/path/to/tests/FileExistsTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertFileIsReadable()`

`assertFileIsReadable(string $filename[, string $message])`

Reports an error identified by `$message` if the file specified by `$filename` is not a file or is not readable.

`assertFileIsNotReadable()` is the inverse of this assertion and takes the same arguments.

Example 1.78

Usage of assertFileIsReadable()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class FileIsReadableTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertFileIsReadable('/path/to/file');
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/FileIsReadableTest.php
PHPUnit 10.0.11 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.2.3

F

Time: 00:00, Memory: 14.29 MB

There was 1 failure:

1) FileIsReadableTest::testFailure
Failed asserting that "/path/to/file" is readable.

/path/to/FileIsReadableTest.php:6

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertFileIsWritable()`

`assertFileIsWritable(string $filename[, string $message])`

Reports an error identified by `$message` if the file specified by `$filename` is not a file or is not writable.

`assertFileIsNotWritable()` is the inverse of this assertion and takes the same arguments.

Example 1.79

Usage of assertFileIsWritable()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class FileIsWritableTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertFileIsWritable('/path/to/file');
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/FileIsWritableTest.php
PHPUnit 10.0.11 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.2.3

F

Time: 00:00, Memory: 14.29 MB

There was 1 failure:

1) FileIsWritableTest::testFailure
Failed asserting that "/path/to/file" is writable.

/path/to/FileIsWritableTest.php:6

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertIsReadable()`

`assertIsReadable(string $filename[, string $message])`

Reports an error identified by `$message` if the file or directory specified by `$filename` is not readable.

`assertIsNotReadable()` is the inverse of this assertion and takes the same arguments.

Example 1.80

Usage of assertIsReadable()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class IsReadableTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertIsReadable('/path/to/unreadable');
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/IsReadableTest.php
PHPUnit 10.0.11 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.2.3

F

Time: 00:00, Memory: 14.29 MB

There was 1 failure:

1) IsReadableTest::testFailure
Failed asserting that "/path/to/unreadable" is readable.

/path/to/IsReadableTest.php:6

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertIsWritable()`

`assertIsWritable(string $filename[, string $message])`

Reports an error identified by `$message` if the file or directory specified by `$filename` is not writable.

`assertIsNotWritable()` is the inverse of this assertion and takes the same arguments.

Example 1.81

Usage of assertIsWritable()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class IsWritableTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertIsWritable('/path/to/unwritable');
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/IsWritableTest.php
PHPUnit 10.0.11 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.2.3

F

Time: 00:00, Memory: 14.29 MB

There was 1 failure:

1) IsWritableTest::testFailure
Failed asserting that "/path/to/unwritable" is writable.

/path/to/IsWritableTest.php:6

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```


## Math

### `assertInfinite()`

`assertInfinite(mixed $actual[, string $message])`

Reports an error identified by `$message` if `$actual` is not `INF`.

`assertFinite()` is the inverse of this assertion and takes the same arguments.

Example 1.82

Usage of assertInfinite()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class InfiniteTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertInfinite(1);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/InfiniteTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) InfiniteTest::testFailure
Failed asserting that 1 is infinite.

/path/to/tests/InfiniteTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertNan()`

`assertNan(mixed $actual[, string $message])`

Reports an error identified by `$message` if `$actual` is not `NAN`.

Example 1.83

Usage of assertNan()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class NanTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertNan(1);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/NanTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) NanTest::testFailure
Failed asserting that 1 is nan.

/path/to/tests/NanTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```


## Constraints

### `assertThat()`

`assertThat(mixed $value, PHPUnit\Framework\Constraint $constraint[, string $message])`

Reports an error identified by `$message` if the `$value` does not match the `$constraint`.

More complex assertions can be formulated using the `PHPUnit\Framework\Constraint` classes. They can be evaluated using the `assertThat()` method.

This example shows how the `logicalNot()` and `equalTo()` constraints can be used, for instance, to express the same assertion as `assertNotEquals()`:

Example 1.84

Usage of assertThat()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class BiscuitTest extends TestCase
{
    public function testEquals(): void
    {
        $theBiscuit = new Biscuit('Ginger');
        $myBiscuit  = new Biscuit('Ginger');

        $this->assertThat(
            $theBiscuit,
            $this->logicalNot(
                $this->equalTo($myBiscuit),
            ),
        );
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/BiscuitTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) BiscuitTest::testEquals
Failed asserting that Biscuit Object #356 (
    'name' => 'Ginger',
) is equal to Biscuit Object #373 (
    'name' => 'Ginger',
).

/path/to/tests/BiscuitTest.php:11

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

Table 1.1 shows the available `PHPUnit\Framework\Constraint` classes.

| Constraint | Meaning |
|---|---|
| `PHPUnit\Framework\Constraint\IsAnything anything()` | Constraint that accepts any input value. |
| `PHPUnit\Framework\Constraint\ArrayHasKey arrayHasKey(mixed $key)` | Constraint that asserts that the array has a given key. |
| `PHPUnit\Framework\Constraint\TraversableContains contains(mixed $value)` | Constraint that asserts that the `array` or object that implements the `Iterator` interface contains a given value. |
| `PHPUnit\Framework\Constraint\TraversableContainsOnly containsOnly(string $type)` | Constraint that asserts that the `array` or object that implements the `Iterator` interface contains only values of a given type. |
| `PHPUnit\Framework\Constraint\TraversableContainsOnly containsOnlyInstancesOf(string $classname)` | Constraint that asserts that the `array` or object that implements the `Iterator` interface contains only instances of a given classname. |
| `PHPUnit\Framework\Constraint\IsEqual equalTo($value, $delta = 0, $maxDepth = 10)` | Constraint that checks if one value is equal to another. |
| `PHPUnit\Framework\Constraint\DirectoryExists directoryExists()` | Constraint that checks if the directory exists. |
| `PHPUnit\Framework\Constraint\FileExists fileExists()` | Constraint that checks if the file(name) exists. |
| `PHPUnit\Framework\Constraint\IsReadable isReadable()` | Constraint that checks if the file(name) is readable. |
| `PHPUnit\Framework\Constraint\IsWritable isWritable()` | Constraint that checks if the file(name) is writable. |
| `PHPUnit\Framework\Constraint\GreaterThan greaterThan(mixed $value)` | Constraint that asserts that the value is greater than a given value. |
| `PHPUnit\Framework\Constraint\LogicalOr greaterThanOrEqual(mixed $value)` | Constraint that asserts that the value is greater than or equal to a given value. |
| `PHPUnit\Framework\Constraint\IsIdentical identicalTo(mixed $value)` | Constraint that asserts that one value is identical to another. |
| `PHPUnit\Framework\Constraint\IsFalse isFalse()` | Constraint that asserts that the value is `false`. |
| `PHPUnit\Framework\Constraint\IsInstanceOf isInstanceOf(string $className)` | Constraint that asserts that the object is an instance of a given class. |
| `PHPUnit\Framework\Constraint\IsNull isNull()` | Constraint that asserts that the value is `null`. |
| `PHPUnit\Framework\Constraint\IsTrue isTrue()` | Constraint that asserts that the value is `true`. |
| `PHPUnit\Framework\Constraint\IsType isType(string $type)` | Constraint that asserts that the value is of a specified type. |
| `PHPUnit\Framework\Constraint\LessThan lessThan(mixed $value)` | Constraint that asserts that the value is smaller than a given value. |
| `PHPUnit\Framework\Constraint\LogicalOr lessThanOrEqual(mixed $value)` | Constraint that asserts that the value is smaller than or equal to a given value. |
| `logicalAnd()` | Logical AND. |
| `logicalNot(PHPUnit\Framework\Constraint $constraint)` | Logical NOT. |
| `logicalOr()` | Logical OR. |
| `logicalXor()` | Logical XOR. |
| `PHPUnit\Framework\Constraint\PCREMatch matchesRegularExpression(string $pattern)` | Constraint that asserts that the string matches a regular expression. |
| `PHPUnit\Framework\Constraint\StringContains stringContains(string $string, bool $case)` | Constraint that asserts that the string contains a given string. |
| `PHPUnit\Framework\Constraint\StringEndsWith stringEndsWith(string $suffix)` | Constraint that asserts that the string ends with a given suffix. |
| `PHPUnit\Framework\Constraint\StringStartsWith stringStartsWith(string $prefix)` | Constraint that asserts that the string starts with a given prefix. |
