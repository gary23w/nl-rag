---
title: "1. Assertions (part 1/3)"
source: https://docs.phpunit.de/en/11.5/assertions.html
domain: phpunit
license: CC-BY-SA-4.0
tags: phpunit php, php testing, unit testing, test assertions
fetched: 2026-07-02
part: 1/3
---

# 1. Assertions

This appendix lists the various assertion methods that are available.


## Static vs. Non-Static Usage of Assertion Methods

PHPUnit’s assertions are implemented in `PHPUnit\Framework\Assert`. `PHPUnit\Framework\TestCase` inherits from `PHPUnit\Framework\Assert`.

The assertion methods are declared static and can be invoked from any context using `PHPUnit\Framework\Assert::assertTrue()`, for instance, or using `$this->assertTrue()` or `self::assertTrue()`, for instance, in a class that extends `PHPUnit\Framework\TestCase`. You can even use global function wrappers such as `assertTrue()`.

A common question, especially from developers new to PHPUnit, is whether using `$this->assertTrue()` or `self::assertTrue()`, for instance, is “the right way” to invoke an assertion. The short answer is: there is no right way. And there is no wrong way, either. It is a matter of personal preference.

For most people it just “feels right” to use `$this->assertTrue()` because the test method is invoked on a test object. The fact that the assertion methods are declared static allows for (re)using them outside the scope of a test object. Lastly, the global function wrappers allow developers to type less characters (`assertTrue()` instead of `$this->assertTrue()` or `self::assertTrue()`).


## Boolean

### `assertTrue()`

`assertTrue(bool $condition[, string $message])`

Reports an error identified by `$message` if `$condition` is `false`.

`assertNotTrue()` is the inverse of this assertion and takes the same arguments.

Example 1.1

Usage of assertTrue()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class TrueTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertTrue(false);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/TrueTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) TrueTest::testFailure
Failed asserting that false is true.

/path/to/tests/TrueTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertFalse()`

`assertFalse(bool $condition[, string $message])`

Reports an error identified by `$message` if `$condition` is `true`.

`assertNotFalse()` is the inverse of this assertion and takes the same arguments.

Example 1.2

Usage of assertFalse()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class FalseTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertFalse(true);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/FalseTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) FalseTest::testFailure
Failed asserting that true is false.

/path/to/tests/FalseTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```


## Identity

### `assertSame()`

`assertSame(mixed $expected, mixed $actual[, string $message])`

Reports an error identified by `$message` if the two variables `$expected` and `$actual` do not have the same type and value.

`assertNotSame()` is the inverse of this assertion and takes the same arguments.

Example 1.3

Usage of assertSame()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class SameWithMixedTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertSame('2204', 2204);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/SameWithMixedTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) SameWithMixedTest::testFailure
Failed asserting that 2204 is identical to '2204'.

/path/to/tests/SameWithMixedTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

`assertSame(object $expected, object $actual[, string $message])`

Reports an error identified by `$message` if the two variables `$expected` and `$actual` do not reference the same object.

Example 1.4

Usage of assertSame() with objects

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class SameWithObjectsTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertSame(new stdClass, new stdClass);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/SameWithObjectsTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) SameWithObjectsTest::testFailure
Failed asserting that two variables reference the same object.

/path/to/tests/SameWithObjectsTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

Identity is checked using the `===` operator.

### `assertArrayIsIdenticalToArrayOnlyConsideringListOfKeys()`

`assertArrayIsIdenticalToArrayOnlyConsideringListOfKeys(array $expected, array $actual, array $keysToBeConsidered[, string $message])`

Reports an error identified by `$message` if two arrays are not identical while only considering array elements for which the keys have been specified.

Example 1.5

Usage of assertArrayIsIdenticalToArrayOnlyConsideringListOfKeys()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ArrayIsIdenticalToArrayOnlyConsideringListOfKeysTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertArrayIsIdenticalToArrayOnlyConsideringListOfKeys(
            [
                'timestamp' => time(),
                'foo'       => 'bar',
            ],
            [
                'timestamp' => time(),
                'foo'       => 'baz',
            ],
            [
                'foo',
            ],
        );
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ArrayIsIdenticalToArrayOnlyConsideringListOfKeysTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ArrayIsIdenticalToArrayOnlyConsideringListOfKeysTest::testFailure
Failed asserting that two arrays are identical.
--- Expected
+++ Actual
@@ @@
 Array &0 [
-    'foo' => 'bar',
+    'foo' => 'baz',
 ]

/path/to/tests/ArrayIsIdenticalToArrayOnlyConsideringListOfKeysTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertArrayIsIdenticalToArrayIgnoringListOfKeys()`

`assertArrayIsIdenticalToArrayIgnoringListOfKeys(array $expected, array $actual, array $keysToBeIgnored[, string $message])`

Reports an error identified by `$message` if two arrays are not identical while only ignoring array elements for which the keys have been specified.

Example 1.6

Usage of assertArrayIsIdenticalToArrayIgnoringListOfKeys()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ArrayIsIdenticalToArrayIgnoringListOfKeysTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertArrayIsIdenticalToArrayIgnoringListOfKeys(
            [
                'timestamp' => time(),
                'foo'       => 'bar',
            ],
            [
                'timestamp' => time(),
                'foo'       => 'baz',
            ],
            [
                'timestamp',
            ],
        );
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ArrayIsIdenticalToArrayIgnoringListOfKeysTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ArrayIsIdenticalToArrayIgnoringListOfKeysTest::testFailure
Failed asserting that two arrays are identical.
--- Expected
+++ Actual
@@ @@
 Array &0 [
-    'foo' => 'bar',
+    'foo' => 'baz',
 ]

/path/to/tests/ArrayIsIdenticalToArrayIgnoringListOfKeysTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```


## Equality

### `assertEquals()`

`assertEquals(mixed $expected, mixed $actual[, string $message])`

Reports an error identified by `$message` if the two variables `$expected` and `$actual` are not equal.

`assertNotEquals()` is the inverse of this assertion and takes the same arguments.

Example 1.7

Usage of assertEquals()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class EqualsTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertEquals(1, 0);
    }

    public function testFailure2(): void
    {
        $this->assertEquals('bar', 'baz');
    }

    public function testFailure3(): void
    {
        $this->assertEquals("foo\nbar\nbaz\n", "foo\nbah\nbaz\n");
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/EqualsTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

FFF                                                                 3 / 3 (100%)

Time: 00:00, Memory: 25.40 MB

There were 3 failures:

1) EqualsTest::testFailure
Failed asserting that 0 matches expected 1.

/path/to/tests/EqualsTest.php:8

2) EqualsTest::testFailure2
Failed asserting that two strings are equal.
--- Expected
+++ Actual
@@ @@
-'bar'
+'baz'

/path/to/tests/EqualsTest.php:13

3) EqualsTest::testFailure3
Failed asserting that two strings are equal.
--- Expected
+++ Actual
@@ @@
 'foo\n
-bar\n
+bah\n
 baz\n
 '

/path/to/tests/EqualsTest.php:18

FAILURES!
Tests: 3, Assertions: 3, Failures: 3.
```

Equality is checked using the `==` operator, but more specialized comparisons are used for specific argument types for `$expected` and `$actual`, see below.

`assertEquals(DateTimeInterface $expected, DateTimeInterface $actual[, string $message])`

Reports an error identified by `$message` if the two points in time represented by the two `DateTimeInterface` objects `$expected` and `$actual` are not equal.

Example 1.8

Usage of assertEquals() with DateTimeImmutable objects

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class EqualsWithDateTimeImmutableTest extends TestCase
{
    public function testFailure(): void
    {
        $expected = new DateTimeImmutable('2023-02-23 01:23:45');
        $actual   = new DateTimeImmutable('2023-02-23 01:23:46');

        $this->assertEquals($expected, $actual);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/EqualsWithDateTimeImmutableTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) EqualsWithDateTimeImmutableTest::testFailure
Failed asserting that two DateTime objects are equal.
--- Expected
+++ Actual
@@ @@
-2023-02-23T01:23:45.000000+0100
+2023-02-23T01:23:46.000000+0100

/path/to/tests/EqualsWithDateTimeImmutableTest.php:11

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

`assertEquals(DOMDocument $expected, DOMDocument $actual[, string $message])`

Reports an error identified by `$message` if the uncommented canonical form of the XML documents represented by the two `DOMDocument` objects `$expected` and `$actual` are not equal.

Example 1.9

Usage of assertEquals() with DOMDocument objects

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class EqualsWithDomDocumentTest extends TestCase
{
    public function testFailure(): void
    {
        $expected = new DOMDocument;
        $expected->loadXML('<foo><bar/></foo>');

        $actual = new DOMDocument;
        $actual->loadXML('<bar><foo/></bar>');

        $this->assertEquals($expected, $actual);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/EqualsWithDomDocumentTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00.001, Memory: 25.40 MB

There was 1 failure:

1) EqualsWithDomDocumentTest::testFailure
Failed asserting that two DOM documents are equal.
--- Expected
+++ Actual
@@ @@
 <?xml version="1.0"?>
-<foo>
-  <bar/>
-</foo>
+<bar>
+  <foo/>
+</bar>

/path/to/tests/EqualsWithDomDocumentTest.php:14

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

`assertEquals(object $expected, object $actual[, string $message])`

Reports an error identified by `$message` if the two objects `$expected` and `$actual` do not have equal property values.

Example 1.10

Usage of assertEquals() with objects

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class EqualsWithObjectsTest extends TestCase
{
    public function testFailure(): void
    {
        $expected      = new stdClass;
        $expected->foo = 'foo';
        $expected->bar = 'bar';

        $actual      = new stdClass;
        $actual->foo = 'bar';
        $actual->baz = 'bar';

        $this->assertEquals($expected, $actual);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/EqualsWithObjectsTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00.001, Memory: 25.40 MB

There was 1 failure:

1) EqualsWithObjectsTest::testFailure
Failed asserting that two objects are equal.
--- Expected
+++ Actual
@@ @@
 stdClass Object (
-    'foo' => 'foo'
-    'bar' => 'bar'
+    'foo' => 'bar'
+    'baz' => 'bar'
 )

/path/to/tests/EqualsWithObjectsTest.php:16

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

`assertEquals(array $expected, array $actual[, string $message])`

Reports an error identified by `$message` if the two arrays `$expected` and `$actual` are not equal.

Example 1.11

Usage of assertEquals() with arrays

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class EqualsWithArraysTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertEquals(['a', 'b', 'c'], ['a', 'c', 'd']);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/EqualsWithArraysTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) EqualsWithArraysTest::testFailure
Failed asserting that two arrays are equal.
--- Expected
+++ Actual
@@ @@
 Array (
     0 => 'a'
-    1 => 'b'
-    2 => 'c'
+    1 => 'c'
+    2 => 'd'
 )

/path/to/tests/EqualsWithArraysTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertEqualsCanonicalizing()`

`assertEqualsCanonicalizing(mixed $expected, mixed $actual[, string $message])`

Reports an error identified by `$message` if the two variables `$expected` and `$actual` are not equal.

The contents of `$expected` and `$actual` are canonicalized before they are compared. For instance, when the two variables `$expected` and `$actual` are arrays, then these arrays are sorted before they are compared. When `$expected` and `$actual` are objects, each object is converted to an array containing all private, protected and public properties.

`assertNotEqualsCanonicalizing()` is the inverse of this assertion and takes the same arguments.

Example 1.12

Usage of assertEqualsCanonicalizing()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class EqualsWithArraysCanonicalizingTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertEqualsCanonicalizing([3, 2, 1], [2, 3, 0, 1]);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/EqualsWithArraysCanonicalizingTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) EqualsWithArraysCanonicalizingTest::testFailure
Failed asserting that two arrays are equal.
--- Expected
+++ Actual
@@ @@
 Array (
-    0 => 1
-    1 => 2
-    2 => 3
+    0 => 0
+    1 => 1
+    2 => 2
+    3 => 3
 )

/path/to/tests/EqualsWithArraysCanonicalizingTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertEqualsIgnoringCase()`

`assertEqualsIgnoringCase(mixed $expected, mixed $actual[, string $message])`

Reports an error identified by `$message` if the two variables `$expected` and `$actual` are not equal.

Differences in casing are ignored for the comparison of `$expected` and `$actual`.

`assertNotEqualsIgnoringCase()` is the inverse of this assertion and takes the same arguments.

Example 1.13

Usage of assertEqualsIgnoringCase()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class EqualsWithStringsIgnoringCaseTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertEqualsIgnoringCase('foo', 'BAR');
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/EqualsWithStringsIgnoringCaseTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) EqualsWithStringsIgnoringCaseTest::testFailure
Failed asserting that two strings are equal.
--- Expected
+++ Actual
@@ @@
-'foo'
+'BAR'

/path/to/tests/EqualsWithStringsIgnoringCaseTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertEqualsWithDelta()`

`assertEqualsWithDelta(mixed $expected, mixed $actual, float $delta[, string $message])`

Reports an error identified by `$message` if the absolute difference between `$expected` and `$actual` is greater than `$delta`.

Please read “What Every Computer Scientist Should Know About Floating-Point Arithmetic” to understand why `$delta` is necessary.

`assertNotEqualsWithDelta()` is the inverse of this assertion and takes the same arguments.

Example 1.14

Usage of assertEqualsWithDelta()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class EqualsWithFloatsAndDeltaTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertEqualsWithDelta(1.0, 1.5, 0.1);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/EqualsWithFloatsAndDeltaTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) EqualsWithFloatsAndDeltaTest::testFailure
Failed asserting that 1.5 matches expected 1.0.

/path/to/tests/EqualsWithFloatsAndDeltaTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertObjectEquals()`

`assertObjectEquals(object $expected, object $actual, string $method = 'equals'[, string $message])`

Reports an error identified by `$message` if `$actual` is not equal to `$expected` according to `$actual->$method($expected)`.

It is a bad practice to use `assertEquals()` (and its inverse, `assertNotEquals()`) on objects without registering a custom comparator that customizes how objects are compared. Unfortunately, though, implementing custom comparators for each and every object you want to assert in your tests is inconvenient at best.

The most common use case for custom comparators are Value Objects. These objects usually have an `equals(self $other): bool` method (or a method just like that but with a different name) for comparing two instances of the Value Object’s type. `assertObjectEquals()` makes custom comparison of objects convenient for this common use case:

`assertObjectNotEquals()` is the inverse of this assertion and takes the same arguments.

Example 1.15

Usage of assertObjectEquals()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ObjectEqualsTest extends TestCase
{
    public function testSomething(): void
    {
        $a = new Email('user@example.org');
        $b = new Email('user@example.org');
        $c = new Email('user@example.com');

        // This passes
        $this->assertObjectEquals($a, $b);

        // This fails
        $this->assertObjectEquals($a, $c);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ObjectEqualsTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ObjectEqualsTest::testSomething
Failed asserting that two objects are equal.

/path/to/tests/ObjectEqualsTest.php:16

FAILURES!
Tests: 1, Assertions: 2, Failures: 1.
```

Example 1.16

Email value object with equals() method

```php
<?php declare(strict_types=1);
final class Email
{
    private string $email;

    public function __construct(string $email)
    {
        $this->ensureIsValidEmail($email);

        $this->email = $email;
    }

    public function asString(): string
    {
        return $this->email;
    }

    public function equals(self $other): bool
    {
        return $this->asString() === $other->asString();
    }

    private function ensureIsValidEmail(string $email): void
    {
        // ...
    }
}
```

Please note:

- A method with name `$method` must exist on the `$actual` object
- The method must accept exactly one argument
- The respective parameter must have a declared type
- The `$expected` object must be compatible with this declared type
- The method must have a declared `bool` return type

If any of the aforementioned assumptions is not fulfilled or if `$actual->$method($expected)` returns `false` then the assertion fails.

### `assertFileEquals()`

`assertFileEquals(string $expected, string $actual[, string $message])`

Reports an error identified by `$message` if the file specified by `$expected` does not have the same contents as the file specified by `$actual`.

`assertFileNotEquals()` is the inverse of this assertion and takes the same arguments.

`assertFileEqualsCanonicalizing()` (and `assertFileNotEqualsCanonicalizing()`) as well as `assertFileEqualsIgnoringCase()` (and `assertFileNotEqualsIgnoringCase()`) do for files what `assertEqualsCanonicalizing()` (and `assertNotEqualsCanonicalizing()`) as well as `assertEqualsIgnoringCase()` (and `assertNotEqualsIgnoringCase()`) do for strings.

Example 1.17

Usage of assertFileEquals()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class FileEqualsTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertFileEquals(
            __DIR__ . '/expected.txt',
            __DIR__ . '/actual.txt',
        );
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/FileEqualsTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) FileEqualsTest::testFailure
Failed asserting that two strings are equal.
--- Expected
+++ Actual
@@ @@
-'expected\n
+'actual\n
 '

/path/to/tests/FileEqualsTest.php:8

FAILURES!
Tests: 1, Assertions: 3, Failures: 1.
```

### `assertArrayIsEqualToArrayOnlyConsideringListOfKeys()`

`assertArrayIsEqualToArrayOnlyConsideringListOfKeys(array $expected, array $actual, array $keysToBeConsidered[, string $message])`

Reports an error identified by `$message` if two arrays are not equal while only considering array elements for which the keys have been specified.

Example 1.18

Usage of assertArrayIsEqualToArrayOnlyConsideringListOfKeys()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ArrayIsEqualToArrayOnlyConsideringListOfKeysTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertArrayIsEqualToArrayOnlyConsideringListOfKeys(
            [
                'timestamp' => time(),
                'foo'       => 'bar',
            ],
            [
                'timestamp' => time(),
                'foo'       => 'baz',
            ],
            [
                'foo',
            ],
        );
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ArrayIsEqualToArrayOnlyConsideringListOfKeysTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ArrayIsEqualToArrayOnlyConsideringListOfKeysTest::testFailure
Failed asserting that two arrays are equal.
--- Expected
+++ Actual
@@ @@
 Array (
-    'foo' => 'bar'
+    'foo' => 'baz'
 )

/path/to/tests/ArrayIsEqualToArrayOnlyConsideringListOfKeysTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertArrayIsEqualToArrayIgnoringListOfKeys()`

`assertArrayIsEqualToArrayIgnoringListOfKeys(array $expected, array $actual, array $keysToBeIgnored[, string $message])`

Reports an error identified by `$message` if two arrays are not equal while only ignoring array elements for which the keys have been specified.

Example 1.19

Usage of assertArrayIsEqualToArrayIgnoringListOfKeys()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ArrayIsEqualToArrayIgnoringListOfKeysTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertArrayIsEqualToArrayIgnoringListOfKeys(
            [
                'timestamp' => time(),
                'foo'       => 'bar',
            ],
            [
                'timestamp' => time(),
                'foo'       => 'baz',
            ],
            [
                'timestamp',
            ],
        );
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ArrayIsEqualToArrayIgnoringListOfKeysTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ArrayIsEqualToArrayIgnoringListOfKeysTest::testFailure
Failed asserting that two arrays are equal.
--- Expected
+++ Actual
@@ @@
 Array (
-    'foo' => 'bar'
+    'foo' => 'baz'
 )

/path/to/tests/ArrayIsEqualToArrayIgnoringListOfKeysTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```
