---
title: "Symfony"
source: https://en.wikipedia.org/wiki/Symfony
domain: symfony
license: CC-BY-SA-4.0
tags: symfony framework, twig template, doctrine orm, php components
fetched: 2026-07-02
---

# Symfony

**Symfony** is a free and open-source PHP web application framework and a set of reusable PHP component libraries. It was published as free software on October 18, 2005, and released under the MIT License.

## Goal

Symfony aims to speed up the creation and maintenance of web applications and to replace repetitive coding tasks. It's also aimed at building robust applications in an enterprise context, and aims to give developers full control over the configuration: from the directory structure to third-party libraries, almost everything can be customized. To match enterprise development guidelines, Symfony is bundled with additional tools to help developers test, debug and document projects.

Symfony has a low performance overhead used with a bytecode cache.

## Technical

Symfony was heavily inspired by the Spring Framework.

It makes heavy use of existing PHP open-source projects as part of the framework, including:

- PDO database abstraction layer (1.1, with Doctrine and Propel 1.3)
- PHPUnit, a unit testing framework
- Twig, a templating engine

Symfony also makes use of its own components, which are freely available on the Symfony Components site for various other projects:

- Symfony YAML, a YAML parser based upon Spyc
- Symfony Event Dispatcher
- Symfony Dependency Injector, a dependency injector
- Symfony Templating, a templating engine

## Sponsors

Symfony is sponsored by SensioLabs, a French software developer and professional services provider. The first name was Sensio Framework, and all classes were therefore prefixed with *sf*. Later, when it was decided to launch it as an open-source framework, the brainstorming resulted in the name symfony (renamed to Symfony from version 2 onward), which matched the existing theme and class name prefixes.

## Real-world usage

- Symfony is used by the open-source Q&A service Askeet and many more applications, including Delicious website.
- At one time it was used for 20 million users of Yahoo! Bookmarks.
- As of February 2009, Dailymotion.com has ported part of its code to use Symfony, and is continuing the transition.
- Symfony is used by OpenSky, a social shopping platform, and the Symfony framework is also used by the massively multiplayer online browser game eRepublik, and by the content management framework eZ Publish in version 5.
- Drupal 8, phpBB and a number of other large applications have incorporated components of Symfony.
- Symfony is also used by Meetic, one of the largest online dating platforms in the world, on most of its websites for implementing its business logic in the backend.
- Symfony components are also used in other web application frameworks including Laravel, which is another full-stack framework, and Silex, which is a microframework.
- Vogue Paris's website is also built on the Symfony framework

Symfony's own website has a comprehensive list of projects using Symfony and a showcase of websites built with Symfony.

## Releases

Symfony manages its releases through a time-based model; a new Symfony release comes out every six months: one in May and one in November. This release process has been adopted as of Symfony 2.2, and all the "rules" explained in this document must be strictly followed as of Symfony 2.4.

The standard version of Symfony is maintained for eight months, whereas long-term support (LTS) versions are supported for three years. A new LTS release is published biennially.

The latest stable release is version 7.3 and current LTS release is version 6.4.

| Color | Meaning |
|---|---|
| Red | Release no longer supported |
| Amber | security fixes only |
| Green | Release still supported |
| Blue | Future release |

| Version | Release date | Support | PHP version | End of maintenance | Notes |
|---|---|---|---|---|---|
| 1.0 | January 2007 | Three years | ≥ 5.0 | January 2010 |   |
| 1.1 | June 2008 | One year | ≥ 5.1 | June 2009 | Security-related patches were applied until June 2010 |
| 1.2 | December 2008 | One year | ≥ 5.2 | November 2009 |   |
| 1.3 | November 2009 | One year | ≥ 5.2.4 | November 2010 |   |
| 1.4 | November 2009 | Three years | ≥ 5.2.4 | November 2012 | LTS version. 1.4 is identical to 1.3, but it does not support the 1.3 deprecated features. |
| 2.0 | July 2011 |   | ≥ 5.3.2 | March 2013 | Last 2.0.x release was Symfony 2.0.25 |
| 2.1 | September 2012 | Eight months | ≥ 5.3.3 | June 2013 | More components are part of the stable API. |
| 2.2 | March 2013 | Eight months | ≥ 5.3.3 | November 2013 | Various new features. |
| 2.3 | June 2013 | Three years | ≥ 5.3.3 | May 2016 | The first LTS release, only three months development, normally six months. |
| 2.4 | November 2013 | Eight months | ≥ 5.3.3 | July 2014 | The first 2.x branch release with complete backwards compatibility. |
| 2.5 | May 2014 | Eight months | ≥ 5.3.3 | January 2015 |   |
| 2.6 | November 2014 | Eight months | ≥ 5.3.3 | July 2015 |   |
| 2.7 | May 2015 | Three years | ≥ 5.3.9 | May 2018 | LTS release. |
| 2.8 | November 2015 | Three years | ≥ 5.3.9 | November 2018 | LTS release. |
| 3.0 | November 2015 | Eight months | ≥ 5.5.9 | July 2016 |   |
| 3.1 | May 2016 | Eight months | ≥ 5.5.9 | January 2017 |   |
| 3.2 | November 2016 | Eight months | ≥ 5.5.9 | July 2017 |   |
| 3.3 | June 2017 | Eight months | ≥ 5.5.9 | January 2018 |   |
| 3.4 | November 2017 | Three years | ≥ 5.5.9 | November 2020 | LTS release. |
| 4.0 | November 2017 | Eight months | ≥ 7.1.3 | July 2018 | Dropping support for HHVM |
| 4.1 | May 2018 | Eight months | ≥ 7.1.3 | January 2019 |   |
| 4.2 | November 2018 | Eight months | ≥ 7.1.3 | July 2019 |   |
| 4.3 | May 2019 | Eight months | ≥ 7.1.3 | January 2020 |   |
| 4.4 | November 2019 | Three years | ≥ 7.1.3 | November 2022 | LTS release. |
| 5.0 | November 2019 | Eight months | ≥ 7.2.5 | July 2020 | Live released by Fabien Potencier during his Keynote at SymfonyCon Amsterdam (11/21/19). |
| 5.1 | May 2020 | Eight months | ≥ 7.2.5 | January 2021 |   |
| 5.2 | November 2020 | Eight months | ≥ 7.2.5 | July 2021 |   |
| 5.3 | May 2021 | Eight months | ≥ 7.2.5 | January 2022 | Stable release. |
| 5.4 | November 2021 | Three years | ≥ 7.2.5 | November 2024 | LTS release; security releases available until February 2029 |
| 6.0 | November 2021 | Eight months | ≥ 8.0.2 | January 2023 | Maintenance period extended by six months. |
| 6.1 | May 2022 | Eight months | ≥ 8.1 | January 2023 |   |
| 6.2 | November 2022 | Eight months | ≥ 8.1 | July 2023 |   |
| 6.3 | May 2023 | Eight months | ≥ 8.1 | January 2024 |   |
| 6.4 | November 2023 | Three years | ≥ 8.1 | November 2027 | LTS release. |
| 7.0 | November 2023 | Eight months | ≥ 8.2 | July 2024 |   |
| 7.1 | May 2024 | Eight months | ≥ 8.2 | January 2025 |   |
| 7.2 | November 2024 | Eight months | ≥ 8.2 | July 2025 |   |
| 7.3 | May 2025 | Eight months | ≥ 8.2 | January 2026 |   |
| 7.4 | November 2025 | Three years | ≥ 8.2 | November 2028 | LTS release; security releases available until November 2029 |
| 8.0 | November 2025 | Eight months | ≥ 8.4 | July 2026 |   |
| 8.1 | May 2026 | Eight months | ≥ 8.4 | January 2027 | Under development. Scheduled release date May 2026 |
