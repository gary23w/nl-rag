---
title: "Getting Started with Version 11 of PHPUnit"
source: https://phpunit.de/getting-started/phpunit-11.html
domain: phpunit
license: CC-BY-SA-4.0
tags: phpunit php, php testing, unit testing, test assertions
fetched: 2026-07-02
---

# Getting Started with PHPUnit 11

This tutorial assumes that you use PHP 8.2 or PHP 8.3. You will learn how to write simple unit tests as well as how to download and run PHPUnit.

The documentation for PHPUnit 11 can be found here.

## Download

### PHP Archive (PHAR)

We distribute a PHP Archive (PHAR) that contains everything you need in order to use PHPUnit 11. Simply download it from here and make it executable:

### Composer

You can add PHPUnit as a local, per-project, development-time dependency to your project using Composer:

```
➜ wget -O phpunit https://phar.phpunit.de/phpunit-11.phar

➜ chmod +x phpunit

➜ ./phpunit --version
PHPUnit 11.0.0 by Sebastian Bergmann and contributors.
```

```
➜ composer require --dev phpunit/phpunit ^11

➜ ./vendor/bin/phpunit --version
PHPUnit 11.0.0 by Sebastian Bergmann and contributors.
```

Please refer to the documentation for details on how to verify PHAR releases of PHPUnit.

The example shown above assumes that `composer` is on your `$PATH`.

Your `composer.json` should look similar to this:

```
{
    "autoload": {
        "classmap": [
            "src/"
        ]
    },
    "require-dev": {
        "phpunit/phpunit": "^11"
    }
}
```

## Code

`src/Email.php`

```
<?php declare(strict_types=1);
final class Email
{
    private string $email;

    private function __construct(string $email)
    {
        $this->ensureIsValidEmail($email);

        $this->email = $email;
    }

    public static function fromString(string $email): self
    {
        return new self($email);
    }

    public function asString(): string
    {
        return $this->email;
    }

    private function ensureIsValidEmail(string $email): void
    {
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new InvalidArgumentException(
                sprintf(
                    '"%s" is not a valid email address',
                    $email
                )
            );
        }
    }
}
```

## Test Code

`tests/EmailTest.php`

```
<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class EmailTest extends TestCase
{
    public function testCanBeCreatedFromValidEmail(): void
    {
        $string = '[email protected]';

        $email = Email::fromString($string);

        $this->assertSame($string, $email->asString());
    }

    public function testCannotBeCreatedFromInvalidEmail(): void
    {
        $this->expectException(InvalidArgumentException::class);

        Email::fromString('invalid');
    }
}
```

## Test Execution

### PHP Archive (PHAR)

```
➜ ./phpunit --bootstrap src/autoload.php tests
PHPUnit 11.0.0 by Sebastian Bergmann and contributors.

..                                        2 / 2 (100%)

Time: 70 ms, Memory: 10.00MB

OK (2 tests, 2 assertions)
```

The above assumes that you have downloaded `phpunit.phar` and put it into your `$PATH` as `phpunit` and that `src/autoload.php` is a script that sets up autoloading for the classes that are to be tested. Such a script is commonly generated using a tool such as phpab.

### Composer

```
➜ ./vendor/bin/phpunit tests
PHPUnit 11.0.0 by Sebastian Bergmann and contributors.

..                                        2 / 2 (100%)

Time: 70 ms, Memory: 10.00MB

OK (2 tests, 2 assertions)
```

The above assumes that `vendor/autoload.php`, the autoloader script managed by Composer, exists and is able to load the code for the `Email` class. Depending on how you set up autoloading, you may need to run `composer dump-autoload` now.

`--bootstrap src/autoload.php` instructs the PHPUnit command-line test runner to include `src/autoload.php` before the tests are run.

`tests` instructs the PHPUnit command-line test runner to execute all tests found declared in `*Test.php` sourcecode files in the `tests` directory.

`tests` instructs the PHPUnit command-line test runner to execute all tests found declared in `*Test.php` sourcecode files in the `tests` directory.

## TestDox

Below you see an alternative output which is based on the idea that the name of a test can be used to document the behavior that is verified by the test:

```
➜ ./phpunit --bootstrap src/autoload.php --testdox tests
PHPUnit 11.0.0 by Sebastian Bergmann and contributors.

..                                        2 / 2 (100%)

Time: 70 ms, Memory: 10.00MB

Email
 ✔ Can be created from valid email address
 ✔ Cannot be created from invalid email address

OK (2 tests, 2 assertions)
```

```
➜ ./vendor/bin/phpunit --testdox tests
PHPUnit 11.0.0 by Sebastian Bergmann and contributors.

..                                        2 / 2 (100%)

Time: 70 ms, Memory: 10.00MB

Email
 ✔ Can be created from valid email address
 ✔ Cannot be created from invalid email address

OK (2 tests, 2 assertions)
```
