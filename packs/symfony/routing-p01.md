---
title: "Routing (Symfony Docs) (part 1/2)"
source: https://symfony.com/doc/current/routing.html
domain: symfony
license: CC-BY-SA-4.0
tags: symfony framework, twig template, doctrine orm, php components
fetched: 2026-07-02
part: 1/2
---

# Routing

When your application receives a request, it calls a controller action to generate the response. The routing configuration defines which action to run for each incoming URL. It also provides other useful features, like generating SEO-friendly URLs (e.g. `/read/intro-to-symfony` instead of `index.php?article_id=57`).

Routes can be configured in YAML, PHP or using attributes. All formats provide the same features and performance, so choose your favorite. Symfony recommends attributes because it's convenient to put the route and controller in the same place.

PHP attributes allow you to define routes next to the code of the controllers associated with those routes. Attributes are enabled by default in Symfony applications that use Symfony Flex, so you can start using them right away.

Note

If your project does not use Symfony Flex, you must enable attribute routing manually by creating the following configuration file:

```
1
2
3
```

```
controllers:
    resource: routing.controllers
```

This tells Symfony to look for `#[Route]` attributes across your application and register both the routes and their associated controllers.

Suppose you want to define a route for the `/blog` URL in your application. To do so, create a controller class like the following:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
```

```
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class BlogController extends AbstractController
{
    #[Route('/blog', name: 'blog_list')]
    public function list(): Response
    {
        
    }
}
```

This configuration defines a route called `blog_list` that matches when the user requests the `/blog` URL. When the match occurs, the application runs the `list()` method of the `BlogController` class.

Note

The query string of a URL is not considered when matching routes. In this example, URLs like `/blog?foo=bar` and `/blog?foo=bar&bar=foo` will also match the `blog_list` route.

Warning

If you define multiple PHP classes in the same file, Symfony only loads the routes of the first class, ignoring all the other routes. The route attribute always wins over routes defined in YAML or PHP files and Symfony will always load the route attribute.

The route name (`blog_list`) is not important for now, but it will be essential later when generating URLs. You only have to remember that each route name must be unique in the application.

Instead of defining routes in the controller classes, you can define them in a separate YAML or PHP file. The main advantage is that they don't require any extra dependency. The main drawback is that you have to work with multiple files when checking the routing of some controller action.

The following example shows how to define in YAML or PHP a route called `blog_list` that associates the `/blog` URL with the `list()` action of the `BlogController`:

```
1
2
3
4
5
6
7
8
9
```

```
blog_list:
    path: /blog
    
    controller: App\Controller\BlogController::list

    
    
    
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

use App\Controller\BlogController;

return Routes::config([
    'blog_list' => [
        'path' => '/blog',
        
        'controller' => [BlogController::class, 'list'],

        
        
        
    ],
]);
```

By default, routes match any HTTP verb (`GET`, `POST`, `PUT`, etc.) Use the `methods` option to restrict the verbs each route should respond to:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
```

```
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class BlogApiController extends AbstractController
{
    #[Route('/api/posts/{id}', methods: ['GET', 'HEAD'])]
    public function show(int $id): Response
    {
        
    }

    #[Route('/api/posts/{id}', methods: ['PUT'])]
    public function edit(int $id): Response
    {
        
    }
}
```

```
1
2
3
4
5
6
7
8
9
10
```

```
api_post_show:
    path:       /api/posts/{id}
    controller: App\Controller\BlogApiController::show
    methods:    GET|HEAD

api_post_edit:
    path:       /api/posts/{id}
    controller: App\Controller\BlogApiController::edit
    methods:    PUT
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

use App\Controller\BlogApiController;

return Routes::config([
    'api_post_show' => [
        'path' => '/api/posts/{id}',
        'controller' => [BlogApiController::class, 'show'],
        'methods' => ['GET', 'HEAD'],
    ],
    'api_post_edit' => [
        'path' => '/api/posts/{id}',
        'controller' => [BlogApiController::class, 'edit'],
        'methods' => ['PUT'],
    ],
]);
```

Tip

HTML forms only support `GET` and `POST` methods. If you're calling a route with a different method from an HTML form, add a hidden field called `_method` with the method to use (e.g. `<input type="hidden" name="_method" value="PUT">`). If you create your forms with Symfony Forms this is done automatically for you when the framework.http_method_override option is `true`.

For security, you can restrict which HTTP methods can be overridden using the framework.allowed_http_method_override option.

Use the `env` option to register a route only when the current configuration environment matches the given value:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
```

```
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class DefaultController extends AbstractController
{
    #[Route('/tools', name: 'tools', env: 'dev')]
    public function developerTools(): Response
    {
        
    }

    
    #[Route('/tools', name: 'tools', env: ['dev', 'test'])]
    public function developerTools(): Response
    {
        
    }
}
```

```
1
2
3
4
5
```

```
when@dev:
    tools:
        path: /tools
        controller: App\Controller\DefaultController::developerTools
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

use App\Controller\DefaultController;

return Routes::config([
    'when@dev' => [
        'tools' => [
            'path' => '/tools',
            'controller' => [DefaultController::class, 'developerTools'],
        ],
    ],
]);
```

Use the `condition` option if you need some route to match based on some arbitrary matching logic:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
```

```
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class DefaultController extends AbstractController
{
    #[Route(
        '/contact',
        name: 'contact',
        condition: "context.getMethod() in ['GET', 'HEAD'] and request.headers.get('User-Agent') matches '/firefox/i'",
        
        
    )]
    public function contact(): Response
    {
        
    }

    #[Route(
        '/posts/{id}',
        name: 'post_show',
        
        condition: "params['id'] < 1000"
    )]
    public function showPost(int $id): Response
    {
        
    }
}
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
```

```
contact:
    path:       /contact
    controller: App\Controller\DefaultController::contact
    condition:  "context.getMethod() in ['GET', 'HEAD'] and request.headers.get('User-Agent') matches '/firefox/i'"
    
    
    
    

post_show:
    path:       /posts/{id}
    controller: App\Controller\DefaultController::showPost
    
    condition:  "params['id'] < 1000"
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

use App\Controller\DefaultController;

return Routes::config([
    'contact' => [
        'path' => '/contact',
        'controller' => [DefaultController::class, 'contact'],
        'condition' => 'context.getMethod() in ["GET", "HEAD"] and request.headers.get("User-Agent") matches "/firefox/i"',
        
        
        
        
    ],
    'post_show' => [
        'path' => '/posts/{id}',
        'controller' => [DefaultController::class, 'showPost'],
        
        'condition' => 'params["id"] < 1000',
    ],
]);
```

The value of the `condition` option is an expression using any valid expression language syntax and can use any of these variables created by Symfony:

**`context`**

An instance of

RequestContext

, which holds the most fundamental information about the route being matched.

**`request`**

The

Symfony Request

object that represents the current request.

**`params`**

An array of matched

route parameters

for the current route.

You can also use these functions:

**`env(string $name)`**

Returns the value of a variable using

Environment Variable Processors

**`service(string $alias)`**

Returns a routing condition service.

First, add the `#[AsRoutingConditionService]` attribute or `routing.condition_service` tag to the services that you want to use in route conditions:

```
1
2
3
4
5
6
7
8
9
10
11
```

```
use Symfony\Bundle\FrameworkBundle\Routing\Attribute\AsRoutingConditionService;
use Symfony\Component\HttpFoundation\Request;

#[AsRoutingConditionService(alias: 'route_checker')]
class RouteChecker
{
    public function check(Request $request): bool
    {
        
    }
}
```

Then, use the `service()` function to refer to that service inside conditions:

```
1
2
3
4
```

```
#[Route(condition: "service('route_checker').check(request)")]

#[Route(condition: "service('App\\\Service\\\RouteChecker').check(request)")]
```

Internally, expressions are compiled down to raw PHP. Because of this, using the `condition` key causes no extra overhead beyond the time it takes for the underlying PHP to execute.

Warning

Conditions are *not* taken into account when generating URLs (which is explained later in this article).

As your application grows, you'll eventually have a *lot* of routes. Symfony includes some commands to help you debug routing issues. First, the `debug:router` command lists all your application routes in the same order in which Symfony evaluates them:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
```

```
$ php bin/console debug:router

----------------  -------  --------------------------------------------
Name              Method   Path
----------------  -------  --------------------------------------------
homepage          ANY      /
contact           GET      /contact
contact_process   POST     /contact
article_show      ANY      /articles/{_locale}/{year}/{title}.{_format}
blog              ANY      /blog/{page}
blog_show         ANY      /blog/{slug}
----------------  -------  --------------------------------------------

$ php bin/console debug:router --show-aliases

$ php bin/console debug:router --show-controllers

$ php bin/console debug:router --method=GET
$ php bin/console debug:router --method=ANY

$ php bin/console debug:router --sort=path
$ php bin/console debug:router --sort=name
```

8.1

The `--sort` option of `debug:router` was introduced in Symfony 8.1.

Pass the name (or part of the name) of some route to this argument to print the route details:

```
1
2
3
4
5
6
7
8
9
10
11
```

```
$ php bin/console debug:router app_lucky_number

+-------------+---------------------------------------------------------+
| Property    | Value                                                   |
+-------------+---------------------------------------------------------+
| Route Name  | app_lucky_number                                        |
| Path        | /lucky/number/{max}                                     |
| ...         | ...                                                     |
| Options     | compiler_class: Symfony\Component\Routing\RouteCompiler |
|             | utf8: true                                              |
+-------------+---------------------------------------------------------+
```

The other command is called `router:match` and it shows which route will match the given URL. It's useful to find out why some URL is not executing the controller action that you expect:

```
1
2
3
```

```
$ php bin/console router:match /lucky/number/8

  [OK] Route "app_lucky_number" matches
```

The previous examples defined routes where the URL never changes (e.g. `/blog`). However, it's common to define routes where some parts are variable. For example, the URL to display some blog post will probably include the title or slug (e.g. `/blog/my-first-post` or `/blog/all-about-symfony`).

In Symfony routes, variable parts are wrapped in `{ }`. For example, the route to display the blog post contents is defined as `/blog/{slug}`:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
```

```
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class BlogController extends AbstractController
{
    

    #[Route('/blog/{slug}', name: 'blog_show')]
    public function show(string $slug): Response
    {
        
        

        
    }
}
```

```
1
2
3
4
```

```
blog_show:
    path:       /blog/{slug}
    controller: App\Controller\BlogController::show
```

```
1
2
3
4
5
6
7
8
9
10
11
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

use App\Controller\BlogController;

return Routes::config([
    'blog_show' => [
        'path' => '/blog/{slug}',
        'controller' => [BlogController::class, 'show'],
    ],
]);
```

The name of the variable part (`{slug}` in this example) is used to create a PHP variable where that route content is stored and passed to the controller. If a user visits the `/blog/my-first-post` URL, Symfony executes the `show()` method in the `BlogController` class and passes a `$slug = 'my-first-post'` argument to the `show()` method.

Routes can define any number of parameters, but each of them can only be used once on each route (e.g. `/blog/posts-about-{category}/page/{pageNumber}`).

Imagine that your application has a `blog_show` route (URL: `/blog/{slug}`) and a `blog_list` route (URL: `/blog/{page}`). Given that route parameters accept any value, there's no way to differentiate both routes.

If the user requests `/blog/my-first-post`, both routes will match and Symfony will use the route which was defined first. To fix this, add some validation to the `{page}` parameter using the `requirements` option:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
```

```
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class BlogController extends AbstractController
{
    #[Route('/blog/{page}', name: 'blog_list', requirements: ['page' => '[0-9]+'])]
    public function list(int $page): Response
    {
        
    }

    #[Route('/blog/{slug}', name: 'blog_show')]
    public function show(string $slug): Response
    {
        
    }
}
```

```
1
2
3
4
5
6
7
8
9
10
```

```
blog_list:
    path:       /blog/{page}
    controller: App\Controller\BlogController::list
    requirements:
        page: '[0-9]+'

blog_show:
    path:       /blog/{slug}
    controller: App\Controller\BlogController::show
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

use App\Controller\BlogController;

return Routes::config([
    'blog_list' => [
        'path' => '/blog/{page}',
        'controller' => [BlogController::class, 'list'],
        'requirements' => ['page' => '[0-9]+'],
    ],
    'blog_show' => [
        'path' => '/blog/{slug}',
        'controller' => [BlogController::class, 'show'],
    ],
]);
```

The `requirements` option defines the PHP regular expressions that route parameters must match for the entire route to match. In this example, `[0-9]+` is a regular expression that matches a *digit* of any length. Now:

| URL | Route | Parameters |
|---|---|---|
| `/blog/2` | `blog_list` | `$page` = `2` |
| `/blog/my-first-post` | `blog_show` | `$slug` = `my-first-post` |

Tip

The Requirement enum contains a collection of commonly used regular-expression constants such as digits, dates and UUIDs which can be used as route parameter requirements.

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
```

```
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\Routing\Requirement\Requirement;

class BlogController extends AbstractController
{
    #[Route('/blog/{page}', name: 'blog_list', requirements: ['page' => Requirement::DIGITS])]
    public function list(int $page): Response
    {
        
    }
}
```

```
1
2
3
4
5
6
```

```
blog_list:
    path:       /blog/{page}
    controller: App\Controller\BlogController::list
    requirements:
        page: !php/const Symfony\Component\Routing\Requirement\Requirement::DIGITS
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

use App\Controller\BlogController;
use Symfony\Component\Routing\Requirement\Requirement;

return Routes::config([
    'blog_list' => [
        'path' => '/blog/{page}',
        'controller' => [BlogController::class, 'list'],
        'requirements' => ['page' => Requirement::DIGITS],
    ],
]);
```

Tip

Route requirements (and route paths too) can include configuration parameters, which is useful to define complex regular expressions once and reuse them in multiple routes.

Tip

Parameters also support PCRE Unicode properties, which are escape sequences that match generic character types. For example, `\p{Lu}` matches any uppercase character in any language, `\p{Greek}` matches any Greek characters, etc.

If you prefer, requirements can be inlined in each parameter using the syntax `{parameter_name<requirements>}`. This feature makes configuration more concise, but it can decrease route readability when requirements are complex:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
```

```
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class BlogController extends AbstractController
{
    #[Route('/blog/{page<[0-9]+>}', name: 'blog_list')]
    public function list(int $page): Response
    {
        
    }
}
```

```
1
2
3
4
```

```
blog_list:
    path:       /blog/{page<[0-9]+>}
    controller: App\Controller\BlogController::list
```

```
1
2
3
4
5
6
7
8
9
10
11
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

use App\Controller\BlogController;

return Routes::config([
    'blog_list' => [
        'path' => '/blog/{page<[0-9]+>}',
        'controller' => [BlogController::class, 'list'],
    ],
]);
```

In the previous example, the URL of `blog_list` is `/blog/{page}`. If users visit `/blog/1`, it will match. But if they visit `/blog`, it will **not** match. As soon as you add a parameter to a route, it must have a value.

You can make `blog_list` once again match when the user visits `/blog` by adding a default value for the `{page}` parameter. When using attributes, default values are defined in the arguments of the controller action. In the other configuration formats they are defined with the `defaults` option:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
```

```
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class BlogController extends AbstractController
{
    #[Route('/blog/{page}', name: 'blog_list', requirements: ['page' => '[0-9]+'])]
    public function list(int $page = 1): Response
    {
        
    }
}
```

```
1
2
3
4
5
6
7
8
9
10
11
```

```
blog_list:
    path:       /blog/{page}
    controller: App\Controller\BlogController::list
    defaults:
        page: 1
    requirements:
        page: '[0-9]+'

blog_show:
    
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

use App\Controller\BlogController;

return Routes::config([
    'blog_list' => [
        'path' => '/blog/{page}',
        'controller' => [BlogController::class, 'list'],
        'defaults' => ['page' => 1],
        'requirements' => ['page' => '[0-9]+'],
    ],
    'blog_show' => [
        
    ],
]);
```

Now, when the user visits `/blog`, the `blog_list` route will match and `$page` will default to a value of `1`.

Tip

The default value is allowed to not match the requirement.

Warning

You can have more than one optional parameter (e.g. `/blog/{slug}/{page}`), but everything after an optional parameter must be optional. For example, `/{page}/blog` is a valid path, but `page` will always be required (i.e. `/blog` will not match this route).

If you want to always include some default value in the generated URL (for example to force the generation of `/blog/1` instead of `/blog` in the previous example) add the `!` character before the parameter name: `/blog/{!page}`

As it happens with requirements, default values can also be inlined in each parameter using the syntax `{parameter_name?default_value}`. This feature is compatible with inlined requirements, so you can inline both in a single parameter:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
```

```
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class BlogController extends AbstractController
{
    #[Route('/blog/{page<[0-9]+>?1}', name: 'blog_list')]
    public function list(int $page): Response
    {
        
    }
}
```

```
1
2
3
4
```

```
blog_list:
    path:       /blog/{page<[0-9]+>?1}
    controller: App\Controller\BlogController::list
```

```
1
2
3
4
5
6
7
8
9
10
11
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

use App\Controller\BlogController;

return Routes::config([
    'blog_list' => [
        'path' => '/blog/{page<[0-9]+>?1}',
        'controller' => [BlogController::class, 'list'],
    ],
]);
```

Tip

To give a `null` default value to any parameter, add nothing after the `?` character (e.g. `/blog/{page?}`). If you do this, don't forget to update the types of the related controller arguments to allow passing `null` values (e.g. replace `int $page` by `?int $page`).

Symfony evaluates routes in the order they are defined. If the path of a route matches many different patterns, it might prevent other routes from being matched. In YAML or PHP config files you can move the route definitions up or down in the configuration file to control their priority. In routes defined as PHP attributes this is much harder to do, so you can set the optional `priority` parameter in those routes to control their priority:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
```

```
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class BlogController extends AbstractController
{
    
    #[Route('/blog/{slug}', name: 'blog_show')]
    public function show(string $slug): Response
    {
        
    }

    
    #[Route('/blog/list', name: 'blog_list', priority: 2)]
    public function list(): Response
    {
        
    }
}
```

The priority parameter expects an integer value. Routes with higher priority are sorted before routes with lower priority. The default value when it is not defined is `0`.

A common routing need is to convert the value stored in some parameter (e.g. an integer acting as the user ID) into another value (e.g. the object that represents the user). This feature is called a "param converter".

Now, keep the previous route configuration, but change the arguments of the controller action. Instead of `string $slug`, add `BlogPost $post`:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
```

```
namespace App\Controller;

use App\Entity\BlogPost;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class BlogController extends AbstractController
{
    

    #[Route('/blog/{slug:post}', name: 'blog_show')]
    public function show(BlogPost $post): Response
    {
        

        
    }
}
```

If your controller arguments include type-hints for objects (`BlogPost` in this case), the "param converter" makes a database request to find the object using the request parameters (`slug` in this case). If no object is found, Symfony generates a 404 response automatically.

The `{slug:post}` syntax maps the route parameter named `slug` to the controller argument named `$post`. It also hints the "param converter" to look up the corresponding `BlogPost` object from the database using the slug.

When mapping multiple entities from route parameters, name collisions can occur. In this example, the route tries to define two mappings: one for an author and one for a category; both using the same `name` parameter. This isn't allowed because the route ends up declaring `name` twice:

```
1
```

```
#[Route('/search-book/{name:author}/{name:category}')]
```

Such routes should instead be defined using the following syntax:

```
1
```

```
#[Route('/search-book/{authorName:author.name}/{categoryName:category.name}')]
```

This way, the route parameter names are unique (`authorName` and `categoryName`), and the "param converter" can correctly map them to controller arguments (`$author` and `$category`), loading them both by their name.

More advanced mappings can be achieved using the `#[MapEntity]` attribute. Check out the Doctrine param conversion documentation to learn how to customize the database queries used to fetch the object from the route parameter.

You can use PHP backed enumerations as route parameters because Symfony will convert them automatically to their scalar values.

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
```

```
namespace App\Controller;

use App\Enum\OrderStatusEnum;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class OrderController extends AbstractController
{
    #[Route('/orders/list/{status}', name: 'list_orders_by_status')]
    public function list(OrderStatusEnum $status = OrderStatusEnum::Paid): Response
    {
        
    }
}
```

In addition to your own parameters, routes can include any of the following special parameters created by Symfony:

**`_controller`**

This parameter is used to determine which controller and action is executed when the route is matched.

**`_format`**

The matched value is used to set the "request format" of the

Request

object. This is used for such things as setting the

Content-Type

of the response (e.g. a

json

format translates into a

Content-Type

of

application/json

).

**`_fragment`**

Used to set the URL fragment identifier (also called "hash" or "anchor"), which is the optional last part of a URL that starts with a

#

character and is used to identify a portion of a document.

**`_locale`**

Used to set the

locale

on the request.

**`_query`**

An array of query parameters to add to the generated URL.

You can include these attributes (except `_fragment`) both in individual routes and in route imports. Symfony defines some special attributes with the same name (except for the leading underscore) so you can define them easier:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
```

```
namespace App\Controller;

class ArticleController extends AbstractController
{
    #[Route(
        path: '/articles/{_locale}/search.{_format}',
        locale: 'en',
        format: 'html',
        query: ['page' => 1],
        requirements: [
            '_locale' => 'en|fr',
            '_format' => 'html|xml',
        ],
    )]
    public function search(): Response
    {
    }
}
```

```
1
2
3
4
5
6
7
8
9
10
11
```

```
article_search:
  path:        /articles/{_locale}/search.{_format}
  controller:  App\Controller\ArticleController::search
  locale:      en
  format:      html
  query:
      page:    1
  requirements:
      _locale: en|fr
      _format: html|xml
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

use App\Controller\ArticleController;

return Routes::config([
    'article_show' => [
        'path' => '/articles/{_locale}/search.{_format}',
        'controller' => [ArticleController::class, 'search'],
        'locale' => 'en',
        'format' => 'html',
        'query' => ['page' => 1],
        'requirements' => ['_locale' => 'en|fr', '_format' => 'html|xml'],
    ],
]);
```

In the `defaults` option of a route you can optionally define parameters not included in the route configuration. This is useful to pass extra arguments to the controllers of the routes:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
```

```
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class BlogController extends AbstractController
{
    #[Route('/blog/{page}', name: 'blog_index', defaults: ['page' => 1, 'title' => 'Hello world!'])]
    public function index(int $page, string $title): Response
    {
        
    }
}
```

```
1
2
3
4
5
6
7
```

```
blog_index:
    path:       /blog/{page}
    controller: App\Controller\BlogController::index
    defaults:
        page: 1
        title: "Hello world!"
```

```
1
2
3
4
5
6
7
8
9
10
11
12
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

use App\Controller\BlogController;

return Routes::config([
    'blog_index' => [
        'path' => '/blog/{page}',
        'controller' => [BlogController::class, 'index'],
        'defaults' => ['page' => 1, 'title' => 'Hello world!'],
    ],
]);
```

Route parameters can contain any values except the `/` slash character, because that's the character used to separate the different parts of the URLs. For example, if the `token` value in the `/share/{token}` route contains a `/` character, this route won't match.

A possible solution is to change the parameter requirements to be more permissive:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
```

```
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class DefaultController extends AbstractController
{
    #[Route('/share/{token}', name: 'share', requirements: ['token' => '.+'])]
    public function share($token): Response
    {
        
    }
}
```

```
1
2
3
4
5
6
```

```
share:
    path:       /share/{token}
    controller: App\Controller\DefaultController::share
    requirements:
        token: .+
```

```
1
2
3
4
5
6
7
8
9
10
11
12
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

use App\Controller\DefaultController;

return Routes::config([
    'share' => [
        'path' => '/share/{token}',
        'controller' => [DefaultController::class, 'share'],
        'requirements' => ['token' => '.+'],
    ],
]);
```

Note

If the route defines several parameters and you apply this permissive regular expression to all of them, you might get unexpected results. For example, if the route definition is `/share/{path}/{token}` and both `path` and `token` accept `/`, then `token` will only get the last part and the rest is matched by `path`.

Note

If the route includes the special `{_format}` parameter, you shouldn't use the `.+` requirement for the parameters that allow slashes. For example, if the pattern is `/share/{token}.{_format}` and `{token}` allows any character, the `/share/foo/bar.json` URL will consider `foo/bar.json` as the token and the format will be empty. This can be solved by replacing the `.+` requirement by `[^.]+` to allow any character except dots.

Route alias allows you to have multiple names for the same route and can be used to provide backward compatibility for routes that have been renamed. Let's say you have a route called `product_show`:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
```

```
namespace App\Controller;

use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class ProductController
{
    #[Route('/product/{id}', name: 'product_show')]
    public function show(): Response
    {
        
    }
}
```

```
1
2
3
4
```

```
product_show:
    path: /product/{id}
    controller: App\Controller\ProductController::show
```

```
1
2
3
4
5
6
7
8
9
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

return Routes::config([
    'product_show' => [
        'path' => '/product/{id}',
        'controller' => [ProductController::class, 'show'],
    ],
]);
```

Now, let's say you want to create a new route called `product_details` that acts exactly the same as `product_show`.

Instead of duplicating the original route, you can create an alias for it.

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
```

```
namespace App\Controller;

use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class ProductController
{
    
    
    #[Route('/product/{id}', name: 'product_show', alias: ['product_details'])]
    public function show(): Response
    {
        
    }
}
```

```
1
2
3
4
5
6
7
8
```

```
product_show:
    path: /product/{id}
    controller: App\Controller\ProductController::show

product_details:
    
    alias: product_show
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

return Routes::config([
    'product_show' => [
        'path' => '/product/{id}',
        'controller' => [ProductController::class, 'show'],
    ],
    'product_details' => [
        
        'alias' => ['product_show'],
    ],
]);
```

In this example, both `product_show` and `product_details` routes can be used in the application and will produce the same result.

Note

YAML and PHP configuration formats are the only ways to define an alias for a route that you do not own. You can't do this when using PHP attributes.

This allows you for example to use your own route name for URL generation, while still targeting a route defined by a third-party bundle. The alias and the original route do not need to be declared in the same file or format.

Route aliases can be used to provide backward compatibility for routes that have been renamed.

Now, let's say you want to replace the `product_show` route in favor of `product_details` and mark the old one as deprecated.

In the previous example, the alias `product_details` was pointing to `product_show` route.

To mark the `product_show` route as deprecated, you need to "switch" the alias. The `product_show` become the alias, and will now point to the `product_details` route. This way, the `product_show` alias could be deprecated.

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
```

```
namespace App\Controller;

use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\DeprecatedAlias;
use Symfony\Component\Routing\Attribute\Route;

class ProductController
{
    
    
    #[Route('/product/{id}',
        name: 'product_details',
        alias: new DeprecatedAlias(
            aliasName: 'product_show',
            package: 'acme/package',
            version: '1.2',
        ),
    )]
    
    #[Route('/product/{id}',
        name: 'product_details',
        alias: new DeprecatedAlias(
            aliasName: 'product_show',
            package: 'acme/package',
            version: '1.2',
            message: 'The "%alias_id%" route alias is deprecated. Please use "product_details" instead.',
        ),
    )]
    public function show(): Response
    {
        
    }
}
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
```

```
product_details:
    path: /product/{id}
    controller: App\Controller\ProductController::show

product_show:
    alias: product_details

    
    
    deprecated:
        package: 'acme/package'
        version: '1.2'

    

    
    deprecated:
        package: 'acme/package'
        version: '1.2'
        message: 'The "%alias_id%" route alias is deprecated. Please use "product_details" instead.'
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

use App\Controller\ProductController;

return Routes::config([
    
    'product_details' => [
        'path' => '/product/{id}',
        'controller' => [ProductController::class, 'show'],
    ],
    
    'product_show' => [
        'alias' => 'product_details',

        
        
        'deprecated' => [
            'package' => 'acme/package',
            'version' => '1.2',
        ],

        

        
        'deprecated' => [
            'package' => 'acme/package',
            'version' => '1.2',
            'message' => 'The "%alias_id%" route alias is deprecated. Please use "product_details" instead.',
        ],
    ],
]);
```

In this example, every time the `product_show` alias is used, a deprecation warning is triggered, advising you to stop using this route and prefer using `product_details`.

The message is actually a message template, which replaces occurrences of the `%alias_id%` placeholder by the route alias name. You **must** have at least one occurrence of the `%alias_id%` placeholder in your template.

It's common for a group of routes to share some options (e.g. all routes related to the blog start with `/blog`) That's why Symfony includes a feature to share route configuration.

When defining routes as attributes, put the common configuration in the `#[Route]` attribute of the controller class. In other routing formats, define the common configuration using options when importing the routes.

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
```

```
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/blog', requirements: ['_locale' => 'en|es|fr'], name: 'blog_')]
class BlogController extends AbstractController
{
    #[Route('/{_locale}', name: 'index')]
    public function index(): Response
    {
        
    }

    #[Route('/{_locale}/posts/{slug}', name: 'show')]
    public function show(string $slug): Response
    {
        
    }
}
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
```

```
controllers:
    resource: routing.controllers
    
    prefix: '/blog'
    
    name_prefix: 'blog_'
    
    requirements:
        _locale: 'en|es|fr'

    
    
    

    
    
    
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

return Routes::config([
    'controllers' => [
        'resource' => '../../src/Controller/',
        'type' => 'attribute',
        
        'prefix' => '/blog',
        
        'name_prefix' => 'blog_',
        
        'requirements' => ['_locale' => 'en|es|fr'],

        
        
        

        
        
        
    ],
]);
```

Warning

The `exclude` option only works when the `resource` value is a glob string. If you use a regular string (e.g. `'../src/Controller'`) the `exclude` value will be ignored.

In this example, the route of the `index()` action will be called `blog_index` and its URL will be `/blog/{_locale}`. The route of the `show()` action will be called `blog_show` and its URL will be `/blog/{_locale}/posts/{slug}`. Both routes will also validate that the `_locale` parameter matches the regular expression defined in the class attribute.

Note

If any of the prefixed routes defines an empty path, Symfony adds a trailing slash to it. In the previous example, an empty path prefixed with `/blog` will result in the `/blog/` URL. If you want to avoid this behavior, set the `trailing_slash_on_root` option to `false` (this option is not available when using PHP attributes):

```
1
2
3
4
5
6
```

```
controllers:
    resource: routing.controllers
    prefix:   '/blog'
    trailing_slash_on_root: false
    
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

return Routes::config([
    'controllers' => [
        'resource' => '../../src/Controller/',
        'type' => 'attribute',
        'prefix' => '/blog',
        'trailing_slash_on_root' => false,
    ],
]);

use Symfony\Component\Routing\Loader\Configurator\RoutingConfigurator;

return function (RoutingConfigurator $routes) {
    $routes->collection('...')
        ->prefix('/categories', trailingSlashOnRoot: false)
        
    ;
};
```

8.1

The `trailingSlashOnRoot` argument of `CollectionConfigurator::prefix()` was introduced in Symfony 8.1.

See also

Symfony can import routes from different sources and you can even create your own route loader.

The `Request` object created by Symfony stores all the route configuration (such as the name and parameters) in the "request attributes". You can get this information in a controller via the `Request` object:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
```

```
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class BlogController extends AbstractController
{
    #[Route('/blog', name: 'blog_list')]
    public function list(Request $request): Response
    {
        $routeName = $request->attributes->get('_route');
        $routeParameters = $request->attributes->get('_route_params');

        
        $allAttributes = $request->attributes->all();

        
    }
}
```

In services, you can get this information by injecting the RequestStack service. In templates, use the Twig global app variable to get the current route name (`app.current_route`) and its parameters (`app.current_route_parameters`).

Symfony defines some special controllers to render templates and redirect to other routes from the route configuration so you don't have to create a controller action.

Read the section about rendering a template from a route in the main article about Symfony templates.

Use the `RedirectController` to redirect to other routes and URLs:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
```

```
doc_shortcut:
    path: /doc
    controller: Symfony\Bundle\FrameworkBundle\Controller\RedirectController
    defaults:
        route: 'doc_page'
        
        page: 'index'
        version: 'current'
        
        permanent: true
        
        keepQueryParams: true
        
        
        
        keepRequestMethod: true
        
        ignoreAttributes: true
        
        

legacy_doc:
    path: /legacy/doc
    controller: Symfony\Bundle\FrameworkBundle\Controller\RedirectController
    defaults:
        
        path: 'https://legacy.example.com/doc'
        permanent: true
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

use Symfony\Bundle\FrameworkBundle\Controller\RedirectController;

return Routes::config([
    'doc_shortcut' => [
        'path' => '/doc',
        'controller' => [RedirectController::class, 'doc_page'],
        'defaults' => [
            'route' => 'doc_page',
            
            'page' => 'index',
            'version' => 'current',
            
            'permanent' => true,
            
            'keepQueryParams' => true,
            
            
            
            'keepRequestMethod' => true,
            
            'ignoreAttributes' => true,
            
            
        ],
    ],
    'legacy_doc' => [
        'path' => '/legacy/doc',
        'controller' => [RedirectController::class, 'legacy_doc'],
        'defaults' => [
            
            'path' => 'https://legacy.example.com/doc',
            'permanent' => true,
        ],
    ],
]);
```

Tip

Symfony also provides some utilities to redirect inside controllers

Historically, URLs have followed the UNIX convention of adding trailing slashes for directories (e.g. `https://example.com/foo/`) and removing them to refer to files (`https://example.com/foo`). Although serving different contents for both URLs is OK, nowadays it's common to treat both URLs as the same URL and redirect between them.

Symfony follows this logic to redirect between URLs with and without trailing slashes (but only for `GET` and `HEAD` requests):

| Route URL | If the requested URL is `/foo` | If the requested URL is `/foo/` |
|---|---|---|
| `/foo` | It matches (`200` status response) | It makes a `301` redirect to `/foo` |
| `/foo/` | It makes a `301` redirect to `/foo/` | It matches (`200` status response) |

Routes can configure a `host` option to require that the HTTP host of the incoming requests matches some specific value. In the following example, both routes match the same path (`/`) but one of them only responds to a specific host name:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
```

```
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class MainController extends AbstractController
{
    #[Route('/', name: 'mobile_homepage', host: 'm.example.com')]
    public function mobileHomepage(): Response
    {
        
    }

    #[Route('/', name: 'homepage')]
    public function homepage(): Response
    {
        
    }
}
```

```
1
2
3
4
5
6
7
8
9
```

```
mobile_homepage:
    path:       /
    host:       m.example.com
    controller: App\Controller\MainController::mobileHomepage

homepage:
    path:       /
    controller: App\Controller\MainController::homepage
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

use App\Controller\MainController;

return Routes::config([
    'mobile_homepage' => [
        'path' => '/',
        'host' => 'm.example.com',
        'controller' => [MainController::class, 'mobileHomepage'],
    ],
    'homepage' => [
        'path' => '/',
        'controller' => [MainController::class, 'homepage'],
    ],
]);
```

The value of the `host` option can include parameters (which is useful in multi-tenant applications) and these parameters can be validated too with `requirements`:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
```

```
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
