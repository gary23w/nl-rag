---
title: "PHP - Wikipedia (part 2/2)"
source: https://en.wikipedia.org/wiki/PHP
domain: laravel
license: CC-BY-SA-4.0
tags: laravel framework, eloquent orm, php framework, blade templating
fetched: 2026-07-02
part: 2/2
---

## Use

PHP is a general-purpose scripting language that is especially suited to server-side web development, in which case PHP generally runs on a web server. Any PHP code in a requested file is executed by the PHP runtime, usually to create dynamic web page content or dynamic images used on websites or elsewhere. It can also be used for command-line scripting and client-side graphical user interface (GUI) applications. PHP can be deployed on most web servers, many operating systems and platforms, and can be used with many relational database management systems (RDBMS). Most web hosting providers support PHP for use by their clients. It is available free of charge, and the PHP Group provides the complete source code for users to build, customize and extend for their own use.

Originally designed to create dynamic web pages, PHP now focuses mainly on server-side scripting, and it is similar to other server-side scripting languages that provide dynamic content from a web server to a client, such as Python, Microsoft's ASP.NET, Sun Microsystems' JavaServer Pages, and `mod_perl`. PHP has also attracted the development of many software frameworks that provide building blocks and a design structure to promote rapid application development (RAD). Some of these include PRADO, CakePHP, Symfony, CodeIgniter, Laravel, Yii Framework, Phalcon and Laminas, offering features similar to other web frameworks.

The LAMP architecture has become popular in the web industry as a way of deploying web applications. PHP is commonly used as the *P* in this bundle alongside Linux, Apache and MySQL, although the *P* may also refer to Python, Perl, or some mix of the three. Similar packages, WAMP and MAMP, are also available for Windows and macOS, with the first letter standing for the respective operating system. Although both PHP and Apache are provided as part of the macOS base install, users of these packages seek a simpler installation mechanism that can be more easily kept up to date.

For specific and more advanced usage scenarios, PHP offers a well-defined and documented way for writing custom extensions in C or C++. Besides extending the language itself in form of additional libraries, extensions are providing a way for improving execution speed where it is critical and there is room for improvements by using a true compiled language. PHP also offers well-defined ways for embedding itself into other software projects. That way PHP can be easily used as an internal scripting language for another project, also providing tight interfacing with the project's specific internal data structures.

PHP received mixed reviews due to lacking support for multithreading at the core language level, though using threads is made possible by the "pthreads" PECL extension.

A command line interface, php-cli, and two ActiveX Windows Script Host scripting engines for PHP have been produced.

### Popularity and usage statistics

PHP is used for Web content management systems including MediaWiki, WordPress, Joomla, Drupal, Moodle, eZ Publish, eZ Platform, and SilverStripe.

As of January 2013, PHP was used in more than 240 million websites (39% of those sampled) and was installed on 2.1 million web servers.

As of 20 February 2026 (three months after PHP 8.5's release), PHP is used as the server-side programming language on 72% of websites where the language could be determined; PHP 8 is the most used version of the language with 56.6% of websites using PHP being on that version, while 34.3% use PHP 7, 9% use PHP 5 and 0.1% use PHP 4.

PHP 8

56.6%

PHP 7

34.3%

PHP 5

9%

PHP 4

0.1%

|   |   |   |   |
|---|---|---|---|

Usage share of PHP versions on 20 February 2026:

three months after PHP 8.5's release

1. PHP 8.5: 0.50% of PHP 8 (0.28%)
2. PHP 8.4: 8.20% of PHP 8 (4.64%)
3. PHP 8.3: 24.0% of PHP 8 (13.6%)
4. PHP 8.2: 36.4% of PHP 8 (20.6%)
5. PHP 8.1: 21.4% of PHP 8 (12.1%)
6. PHP 8.0: 9.00% of PHP 8 (5.09%)
7. PHP 7.4: 73.8% of PHP 7 (25.3%)
8. PHP 7.3: 10.7% of PHP 7 (3.67%)
9. PHP 7.2: 8.40% of PHP 7 (2.88%)
10. PHP 7.1: 3.50% of PHP 7 (1.20%)
11. PHP 7.0: 3.70% of PHP 7 (1.27%)
12. PHP 5.6: 55.0% of PHP 5 (4.95%)
13. PHP 5.5: 8.00% of PHP 5 (0.72%)
14. PHP 5.4: 15.0% of PHP 5 (1.35%)
15. PHP 5.3: 14.9% of PHP 5 (1.34%)
16. PHP 5.2: 6.60% of PHP 5 (0.59%)
17. PHP 5.1: 0.40% of PHP 5 (0.04%)
18. PHP 5.0: <0.1% of PHP 5 (0.00%)
19. PHP 4.4: 73.8% of PHP 4 (0.07%)
20. PHP 4.3: 22.2% of PHP 4 (0.02%)
21. PHP 4.2: 2.60% of PHP 4 (0.00%)
22. PHP 4.1: 0.70% of PHP 4 (0.00%)
23. PHP 4.0: 0.70% of PHP 4 (0.00%)


## Security

In 2019, 11% of all vulnerabilities listed by the National Vulnerability Database were linked to PHP; historically, about 30% of all vulnerabilities listed since 1996 in this database are linked to PHP. Technical security flaws of the language itself or of its core libraries are not frequent (22 in 2009, about 1% of the total although PHP applies to about 20% of programs listed). Recognizing that programmers make mistakes, some languages include taint checking to automatically detect the lack of input validation which induces many issues. Such a feature has been proposed for PHP in the past, but either been rejected or the proposal abandoned.

Third-party projects such as Suhosin and Snuffleupagus aim to remove or change dangerous parts of the language.

Historically, old versions of PHP had some configuration parameters and default values for such runtime settings that made some PHP applications prone to security issues. Among these, `magic_quotes_gpc` and `register_globals` configuration directives were the best known; the latter made any URL parameters become PHP variables, opening a path for serious security vulnerabilities by allowing an attacker to set the value of any uninitialized global variable and interfere with the execution of a PHP script. Support for "magic quotes" and "register globals" settings has been deprecated since PHP 5.3.0, and removed from PHP 5.4.0.

Another example for the potential runtime-settings vulnerability comes from failing to disable PHP execution (for example by using the `engine` configuration directive) for the directory where uploaded files are stored; enabling it can result in the execution of malicious code embedded within the uploaded files. The best practice is to either locate the image directory outside the document root available to the web server and serve it via an intermediary script or disable PHP execution for the directory which stores the uploaded files.

Also, enabling the dynamic loading of PHP extensions (via `enable_dl` configuration directive) in a shared web hosting environment can lead to security issues.

Implied type conversions that result in different values being treated as equal, sometimes against the programmer's intent, can lead to security issues. For example, the result of the comparison `'0e1234' == '0'` is `true`, because strings that are parsable as numbers are converted to numbers; in this case, the first compared value is treated as scientific notation having the value (0×101234), which is zero. Errors like this resulted in authentication vulnerabilities in Simple Machines Forum, Typo3 and phpBB when MD5 password hashes were compared. The recommended way is to use `hash_equals()` (for timing attack safety), `strcmp` or the identity operator (`===`), as `'0e1234' === '0'` results in `false`.

In a 2013 analysis of over 170,000 website defacements, published by Zone-H, the most frequently (53%) used technique was the exploitation of file inclusion vulnerability, mostly related to insecure usage of the PHP language constructs `include`, `require`, and `allow_url_fopen`.

### Cryptographic security

PHP includes `rand()` and `mt_rand()` functions which use a pseudorandom number generator, and are not cryptographically secure. As of version 8.1, the `random_int()` function is included, which uses a cryptographically secure source of randomness provided by the system.

There are two attacks that can be performed over PHP entropy sources: "seed attack" and "state recovery attack". As of 2012, a $250 GPU can perform up to 230 MD5 calculations per second, while a $750 GPU can perform four times as many calculations at the same time. In combination with a "birthday attack" this can lead to serious security vulnerabilities.

### Long-term support

The PHP development team provides official bug fixes for two years following release of each minor version followed by another two years where only security fixes are released. After this, the release is considered end of life and no longer officially supported.

Extended long-term support beyond this is available from commercial providers, such as Zend and others
