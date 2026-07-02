---
title: "1. Assertions (part 2/3)"
source: https://docs.phpunit.de/en/11.5/assertions.html
domain: phpunit
license: CC-BY-SA-4.0
tags: phpunit php, php testing, unit testing, test assertions
fetched: 2026-07-02
part: 2/3
---

## Iterable

### `assertArrayHasKey()`

`assertArrayHasKey(int|string $key, array|ArrayAccess $array[, string $message])`

Reports an error identified by `$message` if `$array` does not have the `$key`.

`assertArrayNotHasKey()` is the inverse of this assertion and takes the same arguments.

Example 1.20

Usage of assertArrayHasKey()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ArrayHasKeyTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertArrayHasKey('foo', ['bar' => 'baz']);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ArrayHasKeyTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ArrayHasKeyTest::testFailure
Failed asserting that an array has the key 'foo'.

/path/to/tests/ArrayHasKeyTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertContains()`

`assertContains(mixed $needle, iterable $haystack[, string $message])`

Reports an error identified by `$message` if `$needle` is not an element of `$haystack`.

`assertNotContains()` is the inverse of this assertion and takes the same arguments.

Example 1.21

Usage of assertContains()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ContainsTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertContains(4, [1, 2, 3]);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ContainsTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ContainsTest::testFailure
Failed asserting that an array contains 4.

/path/to/tests/ContainsTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

Whether `$needle` is an element of `$haystack` is checked using the `===` operator. You can use `assertContainsEquals()` (and `assertNotContainsEquals()`) if you need the comparison logic implemented by the `==` operator.

### `assertContainsOnly()`

`assertContainsOnly(string $type, iterable $haystack[, boolean $isNativeType = null, string $message = ''])`

Reports an error identified by `$message` if `$haystack` does not contain only variables of type `$type`.

`$isNativeType` is a flag used to indicate whether `$type` is a native PHP type.

These are the strings supported for `$type` when `$isNativeType` is `true`: `array`, `bool`, `boolean`, `callable`, `double`, `float`, `int`, `integer`, `iterable`, `null`, `numeric`, `object`, `real`, `resource`, `scalar`, or `string`.

`assertNotContainsOnly()` is the inverse of this assertion and takes the same arguments.

Example 1.22

Usage of assertContainsOnly()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ContainsOnlyTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertContainsOnly('string', ['1', '2', 3]);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ContainsOnlyTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ContainsOnlyTest::testFailure
Failed asserting that Array &0 [
    0 => '1',
    1 => '2',
    2 => 3,
] contains only values of type "string".

/path/to/tests/ContainsOnlyTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

Deprecation: `assertContainsOnly()` is deprecated

As of PHPUnit 11.5, the `assertContainsOnly()` method is soft-deprecated, meaning its declaration is annotated with `@deprecated` so that IDEs and static analysis tools can warn about its usage.

Starting with PHPUnit 12, using the `assertContainsOnly()` method will trigger a deprecation warning. The method will be removed in PHPUnit 13.

### `assertContainsOnlyArray()`

`assertContainsOnlyArray(iterable $haystack[, string $message])`

Reports an error identified by `$message` if `$haystack` does not contain only values of type `array`.

`assertContainsNotOnlyArray()` is the inverse of this assertion and takes the same arguments.

Example 1.23

Usage of assertContainsOnlyArray()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ContainsOnlyArrayTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertContainsOnlyArray([null]);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ContainsOnlyArrayTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ContainsOnlyArrayTest::testFailure
Failed asserting that Array &0 [
    0 => null,
] contains only values of type "array".

/path/to/tests/ContainsOnlyArrayTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertContainsOnlyBool()`

`assertContainsOnlyBool(iterable $haystack[, string $message])`

Reports an error identified by `$message` if `$haystack` does not contain only values of type `bool`.

`assertContainsNotOnlyBool()` is the inverse of this assertion and takes the same arguments.

Example 1.24

Usage of assertContainsOnlyBool()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ContainsOnlyBoolTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertContainsOnlyBool([null]);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ContainsOnlyBoolTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ContainsOnlyBoolTest::testFailure
Failed asserting that Array &0 [
    0 => null,
] contains only values of type "bool".

/path/to/tests/ContainsOnlyBoolTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertContainsOnlyCallable()`

`assertContainsOnlyCallable(iterable $haystack[, string $message])`

Reports an error identified by `$message` if `$haystack` does not contain only values of type `callable`.

`assertContainsNotOnlyCallable()` is the inverse of this assertion and takes the same arguments.

Example 1.25

Usage of assertContainsOnlyCallable()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ContainsOnlyCallableTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertContainsOnlyCallable([null]);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ContainsOnlyCallableTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ContainsOnlyCallableTest::testFailure
Failed asserting that Array &0 [
    0 => null,
] contains only values of type "callable".

/path/to/tests/ContainsOnlyCallableTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertContainsOnlyFloat()`

`assertContainsOnlyFloat(iterable $haystack[, string $message])`

Reports an error identified by `$message` if `$haystack` does not contain only values of type `float`.

`assertContainsNotOnlyFloat()` is the inverse of this assertion and takes the same arguments.

Example 1.26

Usage of assertContainsOnlyFloat()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ContainsOnlyFloatTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertContainsOnlyFloat([null]);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ContainsOnlyFloatTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ContainsOnlyFloatTest::testFailure
Failed asserting that Array &0 [
    0 => null,
] contains only values of type "float".

/path/to/tests/ContainsOnlyFloatTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertContainsOnlyInt()`

`assertContainsOnlyInt(iterable $haystack[, string $message])`

Reports an error identified by `$message` if `$haystack` does not contain only values of type `int`.

`assertContainsNotOnlyInt()` is the inverse of this assertion and takes the same arguments.

Example 1.27

Usage of assertContainsOnlyInt()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ContainsOnlyIntTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertContainsOnlyInt([null]);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ContainsOnlyIntTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ContainsOnlyIntTest::testFailure
Failed asserting that Array &0 [
    0 => null,
] contains only values of type "int".

/path/to/tests/ContainsOnlyIntTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertContainsOnlyIterable()`

`assertContainsOnlyIterable(iterable $haystack[, string $message])`

Reports an error identified by `$message` if `$haystack` does not contain only values of type `iterable`.

`assertContainsNotOnlyIterable()` is the inverse of this assertion and takes the same arguments.

Example 1.28

Usage of assertContainsOnlyIterable()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ContainsOnlyIterableTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertContainsOnlyIterable([null]);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ContainsOnlyIterableTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ContainsOnlyIterableTest::testFailure
Failed asserting that Array &0 [
    0 => null,
] contains only values of type "iterable".

/path/to/tests/ContainsOnlyIterableTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertContainsOnlyNull()`

`assertContainsOnlyNull(iterable $haystack[, string $message])`

Reports an error identified by `$message` if `$haystack` does not contain only values of type `null`.

`assertContainsNotOnlyNull()` is the inverse of this assertion and takes the same arguments.

Example 1.29

Usage of assertContainsOnlyNull()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ContainsOnlyNullTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertContainsOnlyNull(['string']);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ContainsOnlyNullTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ContainsOnlyNullTest::testFailure
Failed asserting that Array &0 [
    0 => 'string',
] contains only values of type "null".

/path/to/tests/ContainsOnlyNullTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertContainsOnlyNumeric()`

`assertContainsOnlyNumeric(iterable $haystack[, string $message])`

Reports an error identified by `$message` if `$haystack` does not contain only values of type `numeric`.

`assertContainsNotOnlyNumeric()` is the inverse of this assertion and takes the same arguments.

Example 1.30

Usage of assertContainsOnlyNumeric()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ContainsOnlyNumericTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertContainsOnlyNumeric([null]);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ContainsOnlyNumericTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ContainsOnlyNumericTest::testFailure
Failed asserting that Array &0 [
    0 => null,
] contains only values of type "numeric".

/path/to/tests/ContainsOnlyNumericTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertContainsOnlyObject()`

`assertContainsOnlyObject(iterable $haystack[, string $message])`

Reports an error identified by `$message` if `$haystack` does not contain only values of type `object`.

`assertContainsNotOnlyObject()` is the inverse of this assertion and takes the same arguments.

Example 1.31

Usage of assertContainsOnlyObject()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ContainsOnlyObjectTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertContainsOnlyObject([null]);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ContainsOnlyObjectTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ContainsOnlyObjectTest::testFailure
Failed asserting that Array &0 [
    0 => null,
] contains only values of type "object".

/path/to/tests/ContainsOnlyObjectTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertContainsOnlyResource()`

`assertContainsOnlyResource(iterable $haystack[, string $message])`

Reports an error identified by `$message` if `$haystack` does not contain only values of type `resource`.

`assertContainsNotOnlyResource()` is the inverse of this assertion and takes the same arguments.

Example 1.32

Usage of assertContainsOnlyResource()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ContainsOnlyResourceTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertContainsOnlyResource([null]);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ContainsOnlyResourceTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ContainsOnlyResourceTest::testFailure
Failed asserting that Array &0 [
    0 => null,
] contains only values of type "resource".

/path/to/tests/ContainsOnlyResourceTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertContainsOnlyClosedResource()`

`assertContainsOnlyClosedResource(iterable $haystack[, string $message])`

Reports an error identified by `$message` if `$haystack` does not contain only values of type `resource (closed)`.

`assertContainsNotOnlyClosedResource()` is the inverse of this assertion and takes the same arguments.

Example 1.33

Usage of assertContainsOnlyClosedResource()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ContainsOnlyClosedResourceTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertContainsOnlyClosedResource([null]);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ContainsOnlyClosedResourceTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ContainsOnlyClosedResourceTest::testFailure
Failed asserting that Array &0 [
    0 => null,
] contains only values of type "resource (closed)".

/path/to/tests/ContainsOnlyClosedResourceTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertContainsOnlyScalar()`

`assertContainsOnlyScalar(iterable $haystack[, string $message])`

Reports an error identified by `$message` if `$haystack` does not contain only values of type `scalar`.

`assertContainsNotOnlyScalar()` is the inverse of this assertion and takes the same arguments.

Example 1.34

Usage of assertContainsOnlyScalar()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ContainsOnlyScalarTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertContainsOnlyScalar([null]);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ContainsOnlyScalarTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ContainsOnlyScalarTest::testFailure
Failed asserting that Array &0 [
    0 => null,
] contains only values of type "scalar".

/path/to/tests/ContainsOnlyScalarTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertContainsOnlyString()`

`assertContainsOnlyString(iterable $haystack[, string $message])`

Reports an error identified by `$message` if `$haystack` does not contain only values of type `string`.

`assertContainsNotOnlyString()` is the inverse of this assertion and takes the same arguments.

Example 1.35

Usage of assertContainsOnlyString()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ContainsOnlyStringTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertContainsOnlyString([null]);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ContainsOnlyStringTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ContainsOnlyStringTest::testFailure
Failed asserting that Array &0 [
    0 => null,
] contains only values of type "string".

/path/to/tests/ContainsOnlyStringTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertContainsOnlyInstancesOf()`

`assertContainsOnlyInstancesOf(string $type, iterable $haystack[, string $message])`

Reports an error identified by `$message` if `$haystack` does not contain only instances of class or interface `$type`.

`assertContainsNotOnlyInstancesOf()` is the inverse of this assertion and takes the same arguments.

Example 1.36

Usage of assertContainsOnlyInstancesOf()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ContainsOnlyInstancesOfTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertContainsOnlyInstancesOf(
            Foo::class,
            [new Foo, new Bar, new Foo],
        );
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ContainsOnlyInstancesOfTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ContainsOnlyInstancesOfTest::testFailure
Failed asserting that Array &0 [
    0 => Foo Object #356 (),
    1 => Bar Object #373 (),
    2 => Foo Object #360 (),
] contains only values of type "Foo".

/path/to/tests/ContainsOnlyInstancesOfTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```


## Objects

### `assertObjectHasProperty()`

`assertObjectHasProperty(string $propertyName, object $object, string $message = '')`

Reports an error identified by `$message` if `$object` does not have a property with the name `$propertyName`.

`assertObjectNotHasProperty()` is the inverse of this assertion and takes the same arguments.

Example 1.37

Usage of assertObjectHasProperty()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ObjectHasPropertyTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertObjectHasProperty('propertyName', new stdClass);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ObjectHasPropertyTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ObjectHasPropertyTest::testFailure
Failed asserting that object of class "stdClass" has property "propertyName".

/path/to/tests/ObjectHasPropertyTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```


## Cardinality

### `assertCount()`

`assertCount(int $expectedCount, Countable|iterable $haystack[, string $message])`

Reports an error identified by `$message` if the number of elements in `$haystack` is not `$expectedCount`.

`assertNotCount()` is the inverse of this assertion and takes the same arguments.

Example 1.38

Usage of assertCount()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class CountTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertCount(0, ['foo']);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/CountTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) CountTest::testFailure
Failed asserting that actual size 1 matches expected size 0.

/path/to/tests/CountTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

Note

Please note that `assertCount()` and `assertNotCount()` do not support generators. Generators can only be iterated over once and they cannot be cloned. Passing a generator to `assertCount()` or `assertNotCount()` would therefore change the state of something that is supposed to be only verified.

### `assertSameSize()`

`assertSameSize(Countable|iterable $expected, Countable|iterable $actual[, string $message])`

Reports an error identified by `$message` if the sizes of `$actual` and `$expected` are not the same.

`assertNotSameSize()` is the inverse of this assertion and takes the same arguments.

Example 1.39

Usage of assertSameSize()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class SameSizeTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertSameSize([1, 2], [1]);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/SameSizeTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) SameSizeTest::testFailure
Failed asserting that actual size 1 matches expected size 2.

/path/to/tests/SameSizeTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

Note

Please note that `assertSameSize()` and `assertNotSameSize()` do not support generators. Generators can only be iterated over once and they cannot be cloned. Passing a generator to `assertSameSize()` or `assertNotSameSize()` would therefore change the state of something that is supposed to be only verified.

### `assertEmpty()`

`assertEmpty(mixed $actual[, string $message])`

Reports an error identified by `$message` if `$actual` is not empty.

`assertNotEmpty()` is the inverse of this assertion and takes the same arguments.

Example 1.40

Usage of assertEmpty()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class EmptyTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertEmpty(['foo']);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/EmptyTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) EmptyTest::testFailure
Failed asserting that an array is empty.

/path/to/tests/EmptyTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

Note

Please note that `assertEmpty()` and `assertNotEmpty()` do not support generators. Generators can only be iterated over once and they cannot be cloned. Passing a generator to `assertEmpty()` or `assertNotEmpty()` would therefore change the state of something that is supposed to be only verified.

### `assertGreaterThan()`

`assertGreaterThan(mixed $expected, mixed $actual[, string $message])`

Reports an error identified by `$message` if the value of `$actual` is not greater than the value of `$expected`.

Example 1.41

Usage of assertGreaterThan()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class GreaterThanTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertGreaterThan(2, 1);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/GreaterThanTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) GreaterThanTest::testFailure
Failed asserting that 1 is greater than 2.

/path/to/tests/GreaterThanTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertGreaterThanOrEqual()`

`assertGreaterThanOrEqual(mixed $expected, mixed $actual[, string $message])`

Reports an error identified by `$message` if the value of `$actual` is not greater than or equal to the value of `$expected`.

Example 1.42

Usage of assertGreaterThanOrEqual()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class GreaterThanOrEqualTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertGreaterThanOrEqual(2, 1);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/GreaterThanOrEqualTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) GreaterThanOrEqualTest::testFailure
Failed asserting that 1 is equal to 2 or is greater than 2.

/path/to/tests/GreaterThanOrEqualTest.php:8

FAILURES!
Tests: 1, Assertions: 2, Failures: 1.
```

### `assertLessThan()`

`assertLessThan(mixed $expected, mixed $actual[, string $message])`

Reports an error identified by `$message` if the value of `$actual` is not less than the value of `$expected`.

Example 1.43

Usage of assertLessThan()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class LessThanTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertLessThan(1, 2);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/LessThanTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) LessThanTest::testFailure
Failed asserting that 2 is less than 1.

/path/to/tests/LessThanTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertLessThanOrEqual()`

`assertLessThanOrEqual(mixed $expected, mixed $actual[, string $message])`

Reports an error identified by `$message` if the value of `$actual` is not less than or equal to the value of `$expected`.

Example 1.44

Usage of assertLessThanOrEqual()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class LessThanOrEqualTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertLessThanOrEqual(1, 2);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/LessThanOrEqualTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) LessThanOrEqualTest::testFailure
Failed asserting that 2 is equal to 1 or is less than 1.

/path/to/tests/LessThanOrEqualTest.php:8

FAILURES!
Tests: 1, Assertions: 2, Failures: 1.
```


## Types

### `assertInstanceOf()`

`assertInstanceOf(string $expected, mixed $actual[, string $message])`

Reports an error identified by `$message` if `$actual` is not an instance of `$expected`.

`assertNotInstanceOf()` is the inverse of this assertion and takes the same arguments.

Example 1.45

Usage of assertInstanceOf()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class InstanceOfTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertInstanceOf(RuntimeException::class, new Exception);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/InstanceOfTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) InstanceOfTest::testFailure
Failed asserting that an instance of class Exception is an instance of class RuntimeException.

/path/to/tests/InstanceOfTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertIsArray()`

`assertIsArray(mixed $actual[, string $message])`

Reports an error identified by `$message` if `$actual` is not of type `array`.

`assertIsNotArray()` is the inverse of this assertion and takes the same arguments.

Example 1.46

Usage of assertIsArray()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class IsArrayTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertIsArray(null);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/IsArrayTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) IsArrayTest::testFailure
Failed asserting that null is of type array.

/path/to/tests/IsArrayTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertIsList()`

`assertIsList(mixed $actual[, string $message])`

Reports an error identified by `$message` if `$actual` is not an array where the keys are consecutive numbers from 0 to `count($actual) - 1`.

Example 1.47

Usage of assertIsList()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class IsListTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertIsList([1 => 'foo', '3' => 'bar']);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/IsListTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) IsListTest::testFailure
Failed asserting that an array is a list.

/path/to/tests/IsListTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertIsBool()`

`assertIsBool(mixed $actual[, string $message])`

Reports an error identified by `$message` if `$actual` is not of type `bool`.

`assertIsNotBool()` is the inverse of this assertion and takes the same arguments.

Example 1.48

Usage of assertIsBool()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class IsBoolTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertIsBool(null);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/IsBoolTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) IsBoolTest::testFailure
Failed asserting that null is of type bool.

/path/to/tests/IsBoolTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertIsCallable()`

`assertIsCallable(mixed $actual[, string $message])`

Reports an error identified by `$message` if `$actual` is not of type `callable`.

`assertIsNotCallable()` is the inverse of this assertion and takes the same arguments.

Example 1.49

Usage of assertIsCallable()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class IsCallableTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertIsCallable(null);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/IsCallableTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) IsCallableTest::testFailure
Failed asserting that null is of type callable.

/path/to/tests/IsCallableTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertIsFloat()`

`assertIsFloat(mixed $actual[, string $message])`

Reports an error identified by `$message` if `$actual` is not of type `float`.

`assertIsNotFloat()` is the inverse of this assertion and takes the same arguments.

Example 1.50

Usage of assertIsFloat()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class IsFloatTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertIsFloat(null);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/IsFloatTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) IsFloatTest::testFailure
Failed asserting that null is of type float.

/path/to/tests/IsFloatTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertIsInt()`

`assertIsInt(mixed $actual[, string $message])`

Reports an error identified by `$message` if `$actual` is not of type `int`.

`assertIsNotInt()` is the inverse of this assertion and takes the same arguments.

Example 1.51

Usage of assertIsInt()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class IsIntTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertIsInt(null);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/IsIntTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) IsIntTest::testFailure
Failed asserting that null is of type int.

/path/to/tests/IsIntTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertIsIterable()`

`assertIsIterable(mixed $actual[, string $message])`

Reports an error identified by `$message` if `$actual` is not of type `iterable`.

`assertIsNotIterable()` is the inverse of this assertion and takes the same arguments.

Example 1.52

Usage of assertIsIterable()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class IsIterableTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertIsIterable(null);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/IsIterableTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) IsIterableTest::testFailure
Failed asserting that null is of type iterable.

/path/to/tests/IsIterableTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertIsNumeric()`

`assertIsNumeric(mixed $actual[, string $message])`

Reports an error identified by `$message` if `$actual` is not of type `numeric`.

`assertIsNotNumeric()` is the inverse of this assertion and takes the same arguments.

Example 1.53

Usage of assertIsNumeric()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class IsNumericTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertIsNumeric(null);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/IsNumericTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) IsNumericTest::testFailure
Failed asserting that null is of type numeric.

/path/to/tests/IsNumericTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertIsObject()`

`assertIsObject(mixed $actual[, string $message])`

Reports an error identified by `$message` if `$actual` is not of type `object`.

`assertIsNotObject()` is the inverse of this assertion and takes the same arguments.

Example 1.54

Usage of assertIsObject()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class IsObjectTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertIsObject(null);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/IsObjectTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) IsObjectTest::testFailure
Failed asserting that null is of type object.

/path/to/tests/IsObjectTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertIsResource()`

`assertIsResource(mixed $actual[, string $message])`

Reports an error identified by `$message` if `$actual` is not of type `resource`.

`assertIsNotResource()` is the inverse of this assertion and takes the same arguments.

`assertIsClosedResource()` (and `assertIsNotClosedResource()`) are provided to explicitly check for closed resources.

Example 1.55

Usage of assertIsResource()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class IsResourceTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertIsResource(null);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/IsResourceTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) IsResourceTest::testFailure
Failed asserting that null is of type resource.

/path/to/tests/IsResourceTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertIsScalar()`

`assertIsScalar(mixed $actual[, string $message])`

Reports an error identified by `$message` if `$actual` is not of type `scalar`.

`assertIsNotScalar()` is the inverse of this assertion and takes the same arguments.

Example 1.56

Usage of assertIsScalar()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class IsScalarTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertIsScalar(null);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/IsScalarTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) IsScalarTest::testFailure
Failed asserting that null is of type scalar.

/path/to/tests/IsScalarTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertIsString()`

`assertIsString(mixed $actual[, string $message])`

Reports an error identified by `$message` if `$actual` is not of type `string`.

`assertIsNotString()` is the inverse of this assertion and takes the same arguments.

Example 1.57

Usage of assertIsString()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class IsStringTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertIsString(null);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/IsStringTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) IsStringTest::testFailure
Failed asserting that null is of type string.

/path/to/tests/IsStringTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### `assertNull()`

`assertNull(mixed $actual[, string $message])`

Reports an error identified by `$message` if `$actual` is not `null`.

`assertNotNull()` is the inverse of this assertion and takes the same arguments.

Example 1.58

Usage of assertNull()

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class NullTest extends TestCase
{
    public function testFailure(): void
    {
        $this->assertNull('foo');
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/NullTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) NullTest::testFailure
Failed asserting that 'foo' is null.

/path/to/tests/NullTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```
