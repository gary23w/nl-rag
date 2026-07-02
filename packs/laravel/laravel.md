---
title: "Laravel"
source: https://en.wikipedia.org/wiki/Laravel
domain: laravel
license: CC-BY-SA-4.0
tags: laravel framework, eloquent orm, php framework, blade templating
fetched: 2026-07-02
---

# Laravel

**Laravel** is a free and open-source PHP-based web framework for building web applications. It was created by Taylor Otwell and intended for the development of web applications following the model–view–controller (MVC) architectural pattern and based on Symfony. Some of the features of Laravel include modular packaging system with a dedicated dependency manager, different ways for accessing relational databases, utilities that aid in application deployment and maintenance, and its orientation toward syntactic sugar.

The source code of Laravel is hosted on GitHub and licensed under the terms of the MIT License.

## History

Taylor Otwell created Laravel as an attempt to provide a more advanced alternative to the CodeIgniter framework, which did not provide certain features such as built-in support for user authentication and authorization. Laravel's first beta release was made available on June 9, 2011, followed by the Laravel 1 release later in the same month.

On September 5, 2024, Laravel announced that they had received $57 million in Series A funding from Accel.

## Framework history

Laravel 1 included built-in support for authentication, localisation, models, views, sessions, routing and other mechanisms, but lacked support for controllers that prevented it from being a true MVC framework.

Laravel 2 was released in September 2011, bringing various improvements from the author and community. Major new features included the support for controllers, which made Laravel 2 a fully MVC-compliant framework, built-in support for the inversion of control (IoC) principle, and a templating system called *Blade*. As a downside, support for third-party packages was removed in Laravel 2.

Laravel 3 was released in February 2012 with a set of new features including the cmd command-line interface (CLI) named *Artisan*, built-in support for more database management systems, database migrations as a form of version control for database layouts, support for handling events, and a packaging system called *Bundles*. An increase of Laravel's userbase and popularity lined up with the release of Laravel 3.

Laravel 4, codenamed *Illuminate*, was released in May 2013. It was made as a complete rewrite of the Laravel framework, migrating its layout into a set of separate packages distributed through Composer, which serves as an application-level package manager. Such a layout improved the extensibility of Laravel 4, which was paired with its official regular release schedule spanning six months between minor point releases. Other new features in the Laravel 4 release include database seeding for the initial population of databases, support for message queues, built-in support for sending different types of email, and support for delayed deletion of database records called *soft deletion*.

Laravel 5 was released in February 2015 as a result of internal changes that ended up in renumbering the then-future Laravel 4.3 release. New features in the Laravel 5 release include support for scheduling periodically executed tasks through a package called *Scheduler*, an abstraction layer called *Flysystem* that allows remote storage to be used in the same way as local file systems, improved handling of package assets through *Elixir*, and simplified externally handled authentication through the optional *Socialite* package. Laravel 5 also introduced a new internal directory tree structure for developed applications.

Lumen 5.0 is the initial release of the Lumen framework, a light derivative of Laravel optimized for speed. This initial release is based on the Laravel 5.x series of PHP components, and following versions reflect the Laravel versions with which it shares common infrastructure. As of 2022, authors no longer recommend the use of Lumen for gaining these advantages, and promote Laravel Octane instead.

Laravel 5.1, released in June 2015, was the first release of Laravel to receive long-term support (LTS). New LTS versions were planned for one every two years.

Laravel 5.3 was released on August 23, 2016. The new features in 5.3 are focused on improving developer speed by adding additional out of the box improvements for common tasks.

Laravel 5.4 was released on January 24, 2017, with many new features like Laravel Dusk, Laravel Mix, Blade Components and Slots, Markdown Emails, Automatic Facades, Route Improvements, Higher Order Messaging for Collections, and many others.

Laravel 6 was released on September 3, 2019. It incorporated shift blueprint code generation, semantic versioning, compatibility with Laravel Vapor, improved authorization responses, improved job middleware, lazy collections, and sub-query improvements. The frontend scaffolding was removed from the main package and moved into the laravel/ui package.

Laravel 7 was released on March 3, 2020, with new features like Laravel Sanctum, Custom Eloquent Casts, Blade Component Tags, Fluent String Operations and Route Model Binding Improvements.

Laravel 8 was released on September 8, 2020, with new features like Laravel Jetstream, model factory classes, migration squashing, Tailwind CSS for pagination views and other usability improvements.

Laravel 9 was released on February 8, 2022.

Laravel 10 was released on February 14, 2023.

Laravel 11 was released on March 12, 2024. It was announced on the Laravel blog and other social media, it was also discussed in detail at Laracon EU in Amsterdam on 5–6 February. Along with Laravel 11, a first-party websocket server called Laravel Reverb was released.

### Release history

Starting with Laravel 5 and up to Laravel 8, versions designated LTS were supported with bug fixes for 2 years and security fixes for 3 years. Other releases were supported with bug fixes for 6 months and security fixes for 1 year. As of version 8, major versions are released yearly, and the support timeline was changed to provide every version with 18 months of bugfixes and 2 years of security fixes. For additional libraries, only the latest major release receives bug fixes.

| Version | Release date | Bug Fixes Until | Security Fixes Until | PHP version |
|---|---|---|---|---|
| Unsupported: 1.0 | June 2011 |   |   |   |
| Unsupported: 2.0 | September 2011 |   |   |   |
| Unsupported: 3.0 | February 22, 2012 |   |   |   |
| Unsupported: 3.1 | March 27, 2012 |   |   |   |
| Unsupported: 3.2 | May 22, 2012 |   |   |   |
| Unsupported: 4.0 | May 28, 2013 |   |   | ≥ 5.3.0 |
| Unsupported: 4.1 | December 12, 2013 |   |   | ≥ 5.3.0 |
| Unsupported: 4.2 | June 1, 2014 |   |   | ≥ 5.4.0 |
| Unsupported: 5.0 | February 4, 2015 | August 4, 2015 | February 4, 2016 | ≥ 5.4.0 |
| Unsupported: 5.1 LTS | June 9, 2015 | June 9, 2017 | June 9, 2018 | ≥ 5.5.9 |
| Unsupported: 5.2 | December 21, 2015 | June 21, 2016 | December 21, 2016 | ≥ 5.5.9 |
| Unsupported: 5.3 | August 23, 2016 | February 23, 2017 | August 23, 2017 | ≥ 5.6.4 |
| Unsupported: 5.4 | January 24, 2017 | July 24, 2017 | January 24, 2018 | ≥ 5.6.4 |
| Unsupported: 5.5 LTS | August 30, 2017 | August 30, 2019 | August 30, 2020 | ≥ 7.0.0 |
| Unsupported: 5.6 | February 7, 2018 | August 7, 2018 | February 7, 2019 | ≥ 7.1.3 |
| Unsupported: 5.7 | September 4, 2018 | March 4, 2019 | September 4, 2019 | ≥ 7.1.3 |
| Unsupported: 5.8 | February 26, 2019 | August 26, 2019 | February 26, 2020 | ≥ 7.1.3 |
| Unsupported: 6 LTS | September 3, 2019 | January 25, 2022 | September 6, 2022 | 7.2 – 8.0 |
| Unsupported: 7 | March 3, 2020 | October 6, 2020 | March 3, 2021 | 7.2 – 8.0 |
| Unsupported: 8 | September 8, 2020 | July 26, 2022 | January 24, 2023 | 7.3 – 8.1 |
| Unsupported: 9 | February 8, 2022 | August 8, 2023 | February 6, 2024 | 8.0 – 8.2 |
| Unsupported: 10 | February 14, 2023 | August 6, 2024 | February 4, 2025 | 8.1 – 8.3 |
| Unsupported: 11 | March 12, 2024 | September 3, 2025 | March 12, 2026 | 8.2 – 8.4 |
| Supported: 12 | February 24, 2025 | August 13, 2026 | February 24, 2027 | ≥ 8.2 |
| Latest version: 13 | March 17, 2026 | Q3 2027 | March 17, 2028 | 8.3 – 8.5 |
| Future version: 14 | Q1 2027 |   |   |   |

Legend:

Unsupported

Supported

Latest version

Preview version

Future version

## Laracon

*Laracon* is the official Laravel conference centered around the Laravel framework, covering its development, uses, and related general software development topics. Laracon has taken place in the United States, Europe, India, Australia and online in the past. Typically, the conference happens in the United States and Europe every year. 2017 was the first year a Laracon was held as an online event only. 2018 was the first year a Laracon was held in Australia. Each year the conference has a different variety of sponsors and organizers, but Laravel, Laravel News and UserScape are usually the primary organizers.

While the numerous Laracon conferences are officially run, a number of other conferences are run under the name of Laravel Live. Currently, there are yearly held Laravel Live UK, Laravel Live Denmark, Laravel Live Pakistan and Laravel Live India conferences. While these are not officially run, they have permission from Taylor Otwell to use the name Laravel.
