---
title: "2. Writing Tests for PHPUnit"
source: https://docs.phpunit.de/en/11.5/writing-tests-for-phpunit.html
domain: phpunit
license: CC-BY-SA-4.0
tags: phpunit php, php testing, unit testing, test assertions
fetched: 2026-07-02
---

# 2. Writing Tests for PHPUnit

## Asserting Return Values

This first example introduces the basic conventions and steps for writing tests with PHPUnit:

1. The tests for a class `Greeter` go into a class `GreeterTest`.
2. `GreeterTest` inherits from `PHPUnit\Framework\TestCase`.
3. The tests are public methods that are named `test*`. Alternatively, you can use the `PHPUnit\Framework\Attributes\Test` attribute on a method to mark it as a test method. See the section on the Test attribute for details.
4. Inside the test methods, assertion methods such as `assertSame()` (see Assertions) are used to assert that an actual value matches an expected value, for instance.

Example 2.1

A class named

Greeter

(declared in

src/Greeter.php

)

```php
<?php declare(strict_types=1);
final class Greeter
{
    public function greet(string $name): string
    {
        return 'Hello, ' . $name . '!';
    }
}
```

Example 2.2

A test class named

GreeterTest

(declared in

tests/GreeterTest.php

)

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class GreeterTest extends TestCase
{
    public function testGreetsWithName(): void
    {
        $greeter = new Greeter;

        $greeting = $greeter->greet('Alice');

        $this->assertSame('Hello, Alice!', $greeting);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/GreeterTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

.                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

OK (1 test, 1 assertion)
```

Martin Fowler once said:

> Whenever you are tempted to type something into a `print` statement or a debugger expression, write it as a test instead.

## Expecting Exceptions

Example 2.3 shows how to use the `expectException()` method to test whether an exception is thrown by the code under test.

Example 2.3

Using the expectException() method

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ExceptionTest extends TestCase
{
    public function testException(): void
    {
        $this->expectException(InvalidArgumentException::class);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ExceptionTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ExceptionTest::testException
Failed asserting that exception of type "InvalidArgumentException" is thrown.

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

The `expectException()` method has to be used **before** the exception you expect to be thrown is thrown. Ideally, `expectException()` is called immediately before the code is called that is expected to throw the exception.

In addition to the `expectException()` method the `expectExceptionCode()`, `expectExceptionMessage()`, and `expectExceptionMessageMatches()` methods exist to set up expectations for exceptions raised by the code under test.

Note

Note that `expectExceptionMessage()` asserts that the `$actual` message contains the `$expected` message and does not perform an exact string comparison.

Asserting return values and expecting exceptions are two of the three most commonly performed operations in a test method. The third is verifying side effects. The verification of side effects in object collaboration is discussed in the chapter on Test Doubles.

## Data Providers

A test method can accept arbitrary arguments. These arguments are to be provided by one or more data provider methods (`additionProvider()` in the example shown below). The data provider method to be used is specified using the `PHPUnit\Framework\Attributes\DataProvider` or the `PHPUnit\Framework\Attributes\DataProviderExternal` attribute.

A data provider method must be `public` and `static` and its name must not start with `test`. It must return a value that is iterable, either an array or an object that implements the `Traversable` interface. In each iteration step, it must yield an array. For each of these arrays, the test method will be called with the contents of the array as its arguments.

Example 2.4

Using a data provider that returns an array of arrays

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\TestCase;

final class NumericDataSetsTest extends TestCase
{
    public static function additionProvider(): array
    {
        return [
            [0, 0, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 3],
        ];
    }

    #[DataProvider('additionProvider')]
    public function testAdd(int $a, int $b, int $expected): void
    {
        $this->assertSame($expected, $a + $b);
    }
}
```

Example 2.5

Using an external data provider that returns an array of arrays

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\Attributes\DataProviderExternal;
use PHPUnit\Framework\TestCase;

final class NumericDataSetsTestUsingExternalDataProvider extends TestCase
{
    #[DataProviderExternal(ExternalDataProvider::class, 'additionProvider')]
    public function testAdd(int $a, int $b, int $expected): void
    {
        $this->assertSame($expected, $a + $b);
    }
}

final class ExternalDataProvider
{
    public static function additionProvider(): array
    {
        return [
            [0, 0, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 3],
        ];
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/NumericDataSetsTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

...F                                                                4 / 4 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) NumericDataSetsTest::testAdd with data set #3 (1, 1, 3)
Failed asserting that 2 is identical to 3.

/path/to/tests/NumericDataSetsTest.php:20

FAILURES!
Tests: 4, Assertions: 4, Failures: 1.
```

It is useful to name each one with a string key. Output will be more verbose as it will contain that name of a dataset that breaks a test.

Example 2.6

Using a data provider with named data sets

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\TestCase;

final class NamedDataSetsTest extends TestCase
{
    public static function additionProvider(): array
    {
        return [
            'adding zeros'  => [0, 0, 0],
            'zero plus one' => [0, 1, 1],
            'one plus zero' => [1, 0, 1],
            'one plus one'  => [1, 1, 3],
        ];
    }

    #[DataProvider('additionProvider')]
    public function testAdd(int $a, int $b, int $expected): void
    {
        $this->assertSame($expected, $a + $b);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/NamedDataSetsTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

...F                                                                4 / 4 (100%)

Time: 00:00.001, Memory: 25.40 MB

There was 1 failure:

1) NamedDataSetsTest::testAdd with data set "one plus one" (1, 1, 3)
Failed asserting that 2 is identical to 3.

/path/to/tests/NamedDataSetsTest.php:20

FAILURES!
Tests: 4, Assertions: 4, Failures: 1.
```

Note

You can make the test output more verbose by defining a sentence and using the test’s parameter names as placeholders (`$a`, `$b` and `$expected` in the example above) with the TestDox attribute (or the @testdox annotation). You can also refer to the name of a named data set with `$_dataName`.

When a test receives input from both a data provider method and from one or more tests it depends on, the arguments from the data provider will come before the ones from depended-upon tests. The arguments from depended-upon tests will be the same for each data set.

When a test depends on a test that uses data providers, the depending test will be executed when the test it depends upon is successful for at least one data set. The result of a test that uses data providers cannot be injected into a depending test.

Note

All data providers, including those for test methods that will not be run due to `--filter` or `--exclude-group`, for example, are executed before both the call to the `setUpBeforeClass()` static method and the first call to the `setUp()` method. You cannot access any properties of the actual test case object in methods such as `setUpBeforeClass()` or `setUp()` within a data provider.

Note

No code coverage data is collected while data provider methods are executed.

Note

The data sets provided by a data provider method should only contain (arrays of) scalar values, immutable value objects, or Test Stubs. Services or large objects graphs should not be created in a data provider method. Mock Objects cannot be created in a data provider method.

## Testing Output

Sometimes you want to assert that the execution of a method, for instance, generates an expected output (via `echo` or `print`, for example). The `PHPUnit\Framework\TestCase` class uses PHP’s Output Buffering feature to provide the functionality that is necessary for this.

Example 2.7 shows how to use the `expectOutputString()` method to set the expected output. If this expected output is not generated, the test will be counted as a failure.

Example 2.7

Testing the output of a function or method

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class OutputTest extends TestCase
{
    public function testExpectFooActualFoo(): void
    {
        $this->expectOutputString('foo');

        print 'foo';
    }

    public function testExpectBarActualBaz(): void
    {
        $this->expectOutputString('bar');

        print 'baz';
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/OutputTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

.F                                                                  2 / 2 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) OutputTest::testExpectBarActualBaz
Failed asserting that two strings are identical.
--- Expected
+++ Actual
@@ @@
-'bar'
+'baz'

FAILURES!
Tests: 2, Assertions: 2, Failures: 1.
```

Table 2.1 shows the methods provided for testing output

| Method | Meaning |
|---|---|
| `void expectOutputRegex(string $regularExpression)` | Set up the expectation that the output matches a `$regularExpression`. |
| `void expectOutputString(string $expectedString)` | Set up the expectation that the output is equal to an `$expectedString`. |

Note

Only one expectation on output can be configured. `expectOutputString()` and `expectOutputRegex()` cannot be combined and must not be called more than once.

## Incomplete Tests

When you are working on a new test case class, you might want to begin by writing empty test methods such as:

```php
public function testSomething(): void
{
}
```

to keep track of the tests that you have to write.

Note

Do yourself a favour and never use pointless names such as `testSomething` for your test methods.

The problem with empty test methods is that they cannot fail and may be misinterpreted as a success. This misinterpretation leads to the test reports being useless – you cannot see whether a test is actually successful or just not implemented yet.

Calling `$this->assertTrue(false)`, for instance, in the unfinished test method does not help either, since then the test will be interpreted as a failure. This would be just as wrong as interpreting an unimplemented test as a success.

If we think of a successful test as a green light and a test failure as a red light, then we need an additional yellow light to mark a test as being incomplete or not yet implemented.

By calling the method `markTestIncomplete()` in a test method, we can mark the test as incomplete:

Example 2.8

Marking a test as incomplete

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class WorkInProgressTest extends TestCase
{
    public function testSomething(): void
    {
        // Optional: Test anything here, if you want.
        $this->assertTrue(true, 'This should already work.');

        // Stop here and mark this test as incomplete.
        $this->markTestIncomplete(
            'This test has not been implemented yet.',
        );
    }
}
```

An incomplete test is denoted by an `I` in the output of the PHPUnit command-line test runner, as shown in the following example:

```
./tools/phpunit --display-incomplete tests/WorkInProgressTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

I                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 incomplete test:

1) WorkInProgressTest::testSomething
This test has not been implemented yet.

/path/to/tests/WorkInProgressTest.php:12

OK, but there were issues!
Tests: 1, Assertions: 1, Incomplete: 1.
```

## Skipping Tests

Not all tests can be run in every environment. Consider, for instance, a database abstraction layer that has several drivers for the different database systems it supports. The tests for the MySQL driver can only be run if a MySQL server is available.

Example 2.9 shows a test case class, `DatabaseTest`, that contains one test method, `testConnection()`. In the test case class’ `setUp()` template method we check whether the MySQLi extension is available and use the `markTestSkipped()` method to skip the test if it is not.

Example 2.9

Skipping a test

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class DatabaseTest extends TestCase
{
    protected function setUp(): void
    {
        if (!extension_loaded('pgsql')) {
            $this->markTestSkipped(
                'The PostgreSQL extension is not available',
            );
        }
    }

    public function testConnection(): void
    {
        // ...
    }
}
```

A test that has been skipped is denoted by an `S` in the output of the PHPUnit command-line test runner, as shown in the following example:

```
./tools/phpunit --display-skipped tests/DatabaseTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

S                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 skipped test:

1) DatabaseTest::testConnection
The PostgreSQL extension is not available

OK, but some tests were skipped!
Tests: 1, Assertions: 0, Skipped: 1.
```

### Skipping Tests using Attributes

In addition to the above methods it is also possible to use attributes to express common preconditions for a test case:

- `RequiresFunction(string $functionName)` skips the test when no function with the specified name is declared
- `RequiresMethod(string $className, string $functionName)` skips the test when no method with the specified name is declared
- `RequiresOperatingSystem(string $regularExpression)` skips the test when the operating system’s name does not match the specified regular expression
- `RequiresOperatingSystemFamily(string $operatingSystemFamily)` skips the test when the operating system’s family is not the specified one
- `RequiresPhp(string $versionRequirement)` skips the test when the PHP version does not match the specified one
- `RequiresPhpExtension(string $extension, ?string $versionRequirement)` skips the test when the specified PHP extension is not available
- `RequiresPhpunit(string $versionRequirement)` skips the test when the PHPUnit version does not match the specified one
- `RequiresSetting(string $setting, string $value)` skips the test when the specified PHP configuration setting is not set to the specified value

All attributes listed above are declared in the `PHPUnit\Framework\Attributes` namespace.

Example 2.10

Skipping a test using attributes

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\Attributes\RequiresPhpExtension;
use PHPUnit\Framework\TestCase;

#[RequiresPhpExtension('pgsql')]
final class DatabaseTest extends TestCase
{
    public function testConnection(): void
    {
        // ...
    }
}
```

## Test Dependencies

Adrian Kuhn et. al. wrote:

> Unit Tests are primarily written as a good practice to help developers identify and fix bugs, to refactor code and to serve as documentation for a unit of software under test. To achieve these benefits, unit tests ideally should cover all the possible paths in a program. One unit test usually covers one specific path in one function or method. However a test method is not necessarily an encapsulated, independent entity. Often there are implicit dependencies between test methods, hidden in the implementation scenario of a test.

PHPUnit supports the declaration of explicit dependencies between test methods. Such dependencies do not define the order in which the test methods are to be executed but they allow the returning of an instance of the test fixture by a producer and passing it to the dependent consumers.

- A producer is a test method that yields its unit under test as return value.
- A consumer is a test method that depends on one or more producers and their return values.

This example shows how to use the `PHPUnit\Framework\Attributes\Depends` attribute to express dependencies between test methods:

Example 2.11

Using the

Depends

attribute to express dependencies

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\Attributes\Depends;
use PHPUnit\Framework\TestCase;

final class StackTest extends TestCase
{
    public function testEmpty(): array
    {
        $stack = [];
        $this->assertEmpty($stack);

        return $stack;
    }

    #[Depends('testEmpty')]
    public function testPush(array $stack): array
    {
        $stack[] = 'foo';
        $this->assertSame('foo', $stack[count($stack) - 1]);
        $this->assertNotEmpty($stack);

        return $stack;
    }

    #[Depends('testPush')]
    public function testPop(array $stack): void
    {
        $this->assertSame('foo', array_pop($stack));
        $this->assertEmpty($stack);
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/StackTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

...                                                                 3 / 3 (100%)

Time: 00:00, Memory: 25.40 MB

OK (3 tests, 5 assertions)
```

In the example above, the first test, `testEmpty()`, creates a new array and asserts that it is empty. The test then returns the fixture as its result. The second test, `testPush()`, depends on `testEmpty()` and is passed the result of that depended-upon test as its argument. Finally, `testPop()` depends upon `testPush()`.

Note

The return value yielded by a producer is passed “as-is” to its consumers by default. This means that when a producer returns an object, a reference to that object is passed to the consumers. Instead of a reference either (a) a (deep) copy via `DependsUsingDeepClone`, or (b) a (normal shallow) clone (based on PHP keyword `clone`) via `DependsUsingShallowClone` are possible, too.

To localize defects, we want our attention to be focussed on relevant failing tests. This is why PHPUnit skips the execution of a test when a depended-upon test has failed. This improves defect localization by exploiting the dependencies between tests as shown in Example 2.12.

Example 2.12

Leveraging the dependencies between tests

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\Attributes\Depends;
use PHPUnit\Framework\TestCase;

final class DependencyFailureTest extends TestCase
{
    public function testOne(): void
    {
        $this->assertTrue(false);
    }

    #[Depends('testOne')]
    public function testTwo(): void
    {
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit --display-skipped tests/DependencyFailureTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

FS                                                                  2 / 2 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) DependencyFailureTest::testOne
Failed asserting that false is true.

/path/to/tests/DependencyFailureTest.php:9

--

There was 1 skipped test:

1) DependencyFailureTest::testTwo
This test depends on "DependencyFailureTest::testOne" to pass

FAILURES!
Tests: 2, Assertions: 1, Failures: 1, Skipped: 1.
```

A test may have more than one test dependency attribute.

By default, PHPUnit does not change the order in which tests are executed, so you have to ensure that the dependencies of a test can actually be met before the test is run.

A test that has more than one test dependency attribute will get a fixture from the first producer as the first argument, a fixture from the second producer as the second argument, and so on.

## Failure Output

Whenever a test fails, PHPUnit tries its best to provide you with as much context as possible that can help to identify the problem.

Example 2.13

Output generated when an array comparison fails

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ArrayDiffTest extends TestCase
{
    public function testEquality(): void
    {
        $this->assertSame(
            [1, 2,  3, 4, 5, 6],
            [1, 2, 33, 4, 5, 6],
        );
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ArrayDiffTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ArrayDiffTest::testEquality
Failed asserting that two arrays are identical.
--- Expected
+++ Actual
@@ @@
 Array &0 [
     0 => 1,
     1 => 2,
-    2 => 3,
+    2 => 33,
     3 => 4,
     4 => 5,
     5 => 6,
 ]

/path/to/tests/ArrayDiffTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

In this example only one of the array values differs and the other values are shown to provide context on where the error occurred.

When the generated output would be long to read PHPUnit will split it up and provide a few lines of context around every difference.

Example 2.14

Output when an array comparison of a long array fails

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class LongArrayDiffTest extends TestCase
{
    public function testEquality(): void
    {
        $this->assertSame(
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,  3, 4, 5, 6],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 33, 4, 5, 6],
        );
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/LongArrayDiffTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) LongArrayDiffTest::testEquality
Failed asserting that two arrays are identical.
--- Expected
+++ Actual
@@ @@
     11 => 0,
     12 => 1,
     13 => 2,
-    14 => 3,
+    14 => 33,
     15 => 4,
     16 => 5,
     17 => 6,
 ]

/path/to/tests/LongArrayDiffTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

### Edge Cases

When a comparison fails PHPUnit creates textual representations of the input values and compares those. Due to that implementation a diff might show more problems than actually exist.

This only happens when using `assertEquals()` or other “weak” comparison functions on arrays or objects.

Example 2.15

Edge case in the diff generation when using weak comparison

```php
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class ArrayWeakComparisonTest extends TestCase
{
    public function testEquality(): void
    {
        $this->assertEquals(
            [1, 2, 3, 4, 5, 6],
            ['1', 2, 33, 4, 5, 6],
        );
    }
}
```

Running the test shown above yields the output shown below:

```
./tools/phpunit tests/ArrayWeakComparisonTest.php
PHPUnit 11.5.27 by Sebastian Bergmann and contributors.

Runtime:       PHP 8.4.10

F                                                                   1 / 1 (100%)

Time: 00:00, Memory: 25.40 MB

There was 1 failure:

1) ArrayWeakComparisonTest::testEquality
Failed asserting that two arrays are equal.
--- Expected
+++ Actual
@@ @@
 Array (
-    0 => 1
+    0 => '1'
     1 => 2
-    2 => 3
+    2 => 33
     3 => 4
     4 => 5
     5 => 6
 )

/path/to/tests/ArrayWeakComparisonTest.php:8

FAILURES!
Tests: 1, Assertions: 1, Failures: 1.
```

In this example the difference in the first index between `1` and `'1'` is reported even though `assertEquals()` considers the values as a match.
