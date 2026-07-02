---
title: "Routing (Symfony Docs) (part 2/2)"
source: https://symfony.com/doc/current/routing.html
domain: symfony
license: CC-BY-SA-4.0
tags: symfony framework, twig template, doctrine orm, php components
fetched: 2026-07-02
part: 2/2
---

# Routing (Symfony Docs)

class MainController extends AbstractController
{
    #[Route(
        '/',
        name: 'mobile_homepage',
        host: '{subdomain}.example.com',
        defaults: ['subdomain' => 'm'],
        requirements: ['subdomain' => 'm|mobile'],
    )]
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
10
11
12
13
```

```
mobile_homepage:
    path:       /
    host:       "{subdomain}.example.com"
    controller: App\Controller\MainController::mobileHomepage
    defaults:
        subdomain: m
    requirements:
        subdomain: m|mobile

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
17
18
```

```
namespace Symfony\Component\Routing\Loader\Configurator;

use App\Controller\MainController;

return Routes::config([
    'mobile_homepage' => [
        'path' => '/',
        'host' => '{subdomain}.example.com',
        'controller' => [MainController::class, 'mobileHomepage'],
        'defaults' => ['subdomain' => 'm'],
        'requirements' => ['subdomain' => 'm|mobile'],
    ],
    'homepage' => [
        'path' => '/',
        'controller' => [MainController::class, 'homepage'],
    ],
]);
```

In the above example, the `subdomain` parameter defines a default value because otherwise you need to include a subdomain value each time you generate a URL using these routes.

Tip

You can also set the `host` option when importing routes to make all of them require that host name.

Note

When using sub-domain routing, you must set the `Host` HTTP headers in functional tests or routes won't match:

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
$crawler = $client->request(
    'GET',
    '/',
    [],
    [],
    ['HTTP_HOST' => 'm.example.com']
    
    
);
```

Tip

You can also use the inline defaults and requirements format in the `host` option: `{subdomain<m|mobile>?m}.example.com`

If your application is translated into multiple languages, each route can define a different URL per each translation locale. This avoids the need for duplicating routes, which also reduces the potential bugs:

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

class CompanyController extends AbstractController
{
    #[Route(path: [
        'en' => '/about-us',
        'nl' => '/over-ons'
        
        
        '/about-us',
    ], name: 'about_us')]
    public function about(): Response
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
about_us:
    path:
        en: /about-us
        nl: /over-ons
    controller: App\Controller\CompanyController::about
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

use App\Controller\CompanyController;

return Routes::config([
    'about_us' => [
        'path' => [
            'en' => '/about-us',
            'nl' => '/over-ons',
            
            
            '/about-us',
        ],
        'controller' => [CompanyController::class, 'about'],
    ],
]);
```

Note

When using PHP attributes for localized routes, you have to use the `path` named parameter to specify the array of paths.

When a localized route is matched, Symfony uses the same locale automatically during the entire request.

Tip

When the application uses full "language + territory" locales (e.g. `fr_FR`, `fr_BE`), if the URLs are the same in all related locales, routes can use only the language part (e.g. `fr`) to avoid repeating the same URLs.

A common requirement for internationalized applications is to prefix all routes with a locale. This can be done by defining a different prefix for each locale (and setting an empty prefix for your default locale if you prefer it):

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
    prefix:
        en: '' 
        nl: '/nl'
    resource: routing.controllers
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
    'controllers' => [
        'resource' => '../../src/Controller/',
        'type' => 'attribute',
        'prefix' => [
            'en' => '', 
            'nl' => '/nl',
        ],
    ],
]);
```

Note

If a route being imported includes the special _locale parameter in its own definition, Symfony will only import it for that locale and not for the other configured locale prefixes.

E.g. if a route contains `locale: 'en'` in its definition and it's being imported with `en` (prefix: empty) and `nl` (prefix: `/nl`) locales, that route will be available only in `en` locale and not in `nl`.

Another common requirement is to host the website on a different domain according to the locale. This can be done by defining a different host for each locale.

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
    host:
        en: 'www.example.com'
        nl: 'www.example.nl'
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
    'controllers' => [
        'resource' => '../../src/Controller/',
        'type' => 'attribute',
        'host' => [
            'en' => 'www.example.com',
            'nl' => 'www.example.nl',
        ],
    ],
]);
```

Sometimes, when an HTTP response should be cached, it is important to ensure that can happen. However, whenever a session is started during a request, Symfony turns the response into a private non-cacheable response.

For details, see HTTP Cache.

Routes can configure a `stateless` boolean option in order to declare that the session shouldn't be used when matching a request:

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

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\Routing\Attribute\Route;

class MainController extends AbstractController
{
    #[Route('/', name: 'homepage', stateless: true)]
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
```

```
homepage:
    controller: App\Controller\MainController::homepage
    path: /
    stateless: true
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

use App\Controller\MainController;

return Routes::config([
    'homepage' => [
        'controller' => [MainController::class, 'homepage'],
        'path' => '/',
        'stateless' => true,
    ],
]);
```

Now, if the session is used, the application will report it based on your `kernel.debug` parameter:

- `enabled`: will throw an UnexpectedSessionUsageException exception
- `disabled`: will log a warning

It will help you understand and hopefully fixing unexpected behavior in your application.

Routing systems are bidirectional:

1. they associate URLs with controllers (as explained in the previous sections);
2. they generate URLs for a given route.

Generating URLs from routes allows you to not write the `<a href="...">` values manually in your HTML templates. Also, if the URL of some route changes, you only have to update the route configuration and all links will be updated.

To generate a URL, you need to specify the name of the route (e.g. `blog_show`) and the values of the parameters defined by the route (e.g. `slug = my-blog-post`).

For that reason each route has an internal name that must be unique in the application. If you don't set the route name explicitly with the `name` option, Symfony generates an automatic name based on the controller and action.

Symfony declares route aliases based on the FQCN if the target class has an `__invoke()` method that adds a route **and** if the target class added one route exactly. Symfony also automatically adds an alias for every method that defines only one route. Consider the following class:

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

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\Routing\Attribute\Route;

final class MainController extends AbstractController
{
    #[Route('/', name: 'homepage')]
    public function homepage(): Response
    {
        
    }
}
```

Symfony will add a route alias named `App\Controller\MainController::homepage`.

If your controller extends from the AbstractController, use the `generateUrl()` helper:

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
use Symfony\Component\Routing\Generator\UrlGeneratorInterface;

class BlogController extends AbstractController
{
    #[Route('/blog', name: 'blog_list')]
    public function list(): Response
    {
        
        $signUpPage = $this->generateUrl('sign_up');

        
        $userProfilePage = $this->generateUrl('user_profile', [
            'username' => $user->getUserIdentifier(),
        ]);

        
        
        $signUpPage = $this->generateUrl('sign_up', [], UrlGeneratorInterface::ABSOLUTE_URL);

        
        
        $signUpPageInDutch = $this->generateUrl('sign_up', ['_locale' => 'nl']);

        
    }
}
```

Note

If you pass to the `generateUrl()` method some parameters that are not part of the route definition, they are included in the generated URL as a query string:

```
1
2
3
```

```
$this->generateUrl('blog', ['page' => 2, 'category' => 'Symfony']);
```

Warning

While objects are converted to string when used as placeholders, they are not converted when used as extra parameters. So, if you're passing an object (e.g. an Uuid) as value of an extra parameter, you need to explicitly convert it to a string:

```
1
```

```
$this->generateUrl('blog', ['uuid' => (string) $entity->getUuid()]);
```

If your controller does not extend from `AbstractController`, you'll need to fetch services in your controller and follow the instructions of the next section.

Inject the `router` Symfony service into your own services and use its `generate()` method. When using service autowiring you only need to add an argument in the service constructor and type-hint it with the UrlGeneratorInterface class:

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
```

```
namespace App\Service;

use Symfony\Component\Routing\Generator\UrlGeneratorInterface;

class SomeService
{
    public function __construct(
        private UrlGeneratorInterface $urlGenerator,
    ) {
    }

    public function someMethod(): void
    {
        

        
        $signUpPage = $this->urlGenerator->generate('sign_up');

        
        $userProfilePage = $this->urlGenerator->generate('user_profile', [
            'username' => $user->getUserIdentifier(),
        ]);

        
        
        $signUpPage = $this->urlGenerator->generate('sign_up', [], UrlGeneratorInterface::ABSOLUTE_URL);

        
        
        $signUpPageInDutch = $this->urlGenerator->generate('sign_up', ['_locale' => 'nl']);
    }
}
```

Read the section about creating links between pages in the main article about Symfony templates.

If your JavaScript code is included in a Twig template, you can use the `path()` and `url()` Twig functions to generate the URLs and store them in JavaScript variables. The `escape()` filter is needed to escape any non-JavaScript-safe values:

```
1
2
3
```

```
<script>
    const route = "{{ path('blog_show', {slug: 'my-blog-post'})|escape('js') }}";
</script>
```

If you need to generate URLs dynamically or if you are using pure JavaScript code, this solution doesn't work. In those cases, consider using the FOSJsRoutingBundle.

Generating URLs in commands works the same as generating URLs in services. The only difference is that commands are not executed in the HTTP context. Therefore, if you generate absolute URLs, you'll get `http://localhost/` as the host name instead of your real host name.

The solution is to configure the `default_uri` option to define the "request context" used by commands when they generate URLs:

```
1
2
3
4
5
```

```
framework:
    router:
        
        default_uri: 'https://example.org/my/path/'
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
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        'router' => [
            'default_uri' => 'https://example.org/my/path/',
        ],
    ],
]);
```

Now you'll get the expected results when generating URLs in your commands:

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
```

```
namespace App\Command;

use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Style\SymfonyStyle;
use Symfony\Component\Routing\Generator\UrlGeneratorInterface;

#[AsCommand(name: 'app:my-command')]
class MyCommand
{
    public function __construct(
        private UrlGeneratorInterface $urlGenerator,
    ) {
    }

    public function __invoke(SymfonyStyle $io): int
    {
        
        $signUpPage = $this->urlGenerator->generate('sign_up');

        
        $userProfilePage = $this->urlGenerator->generate('user_profile', [
            'username' => $user->getUserIdentifier(),
        ]);

        
        
        $signUpPage = $this->urlGenerator->generate('sign_up', [], UrlGeneratorInterface::ABSOLUTE_URL);

        
        
        $signUpPageInDutch = $this->urlGenerator->generate('sign_up', ['_locale' => 'nl']);

        
    }
}
```

Note

By default, the URLs generated for web assets use the same `default_uri` value, but you can change it with the `asset.request_context.base_path` and `asset.request_context.secure` container parameters.

Note

By default, routes generated outside the HTTP context use the default locale as the value of the `_locale` parameter. You can override this by providing a different value for the `_locale` parameter when generating each route.

In highly dynamic applications, it may be necessary to check whether a route exists before using it to generate a URL. In those cases, don't use the getRouteCollection() method because that regenerates the routing cache and slows down the application.

Instead, try to generate the URL and catch the RouteNotFoundException thrown when the route doesn't exist:

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
use Symfony\Component\Routing\Exception\RouteNotFoundException;

try {
    $url = $this->router->generate($routeName, $routeParameters);
} catch (RouteNotFoundException $e) {
    
}
```

Note

If your server runs behind a proxy that terminates SSL, make sure to configure Symfony to work behind a proxy

The configuration for the scheme is only used for non-HTTP requests. The `schemes` option together with incorrect proxy configuration will lead to a redirect loop.

By default, generated URLs use the same HTTP scheme as the current request. In console commands, where there is no HTTP request, URLs use `http` by default. You can change this per command (via the router's `getContext()` method) or globally with the default_uri option:

```
1
2
3
4
```

```
framework:
    router:
        default_uri: 'https://example.org'
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
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        'router' => [
            'default_uri' => 'https://example.org',
        ],
    ],
]);
```

8.1

The `router.request_context.scheme` and `router.request_context.host` container parameters were deprecated in Symfony 8.1. Use the `framework.router.default_uri` option instead.

Outside of console commands, use the `schemes` option to define the scheme of each route explicitly:

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

class SecurityController extends AbstractController
{
    #[Route('/login', name: 'login', schemes: ['https'])]
    public function login(): Response
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
login:
    path:       /login
    controller: App\Controller\SecurityController::login
    schemes:    [https]
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

use App\Controller\SecurityController;

return Routes::config([
    'login' => [
        'path' => '/login',
        'controller' => [SecurityController::class, 'login'],
        'schemes' => ['https'],
    ],
]);
```

The URL generated for the `login` route will always use HTTPS. This means that when using the `path()` Twig function to generate URLs, you may get an absolute URL instead of a relative URL if the HTTP scheme of the original request is different from the scheme used by the route:

```
1
2
3
4
5
6
```

```
{{ path('login') }}

{{ path('login') }}
```

The scheme requirement is also enforced for incoming requests. If you try to access the `/login` URL with HTTP, you will automatically be redirected to the same URL, but with the HTTPS scheme.

If you want to force a group of routes to use HTTPS, you can define the default scheme when importing them. The following example forces HTTPS on all routes defined as attributes:

```
1
2
3
4
```

```
controllers:
    schemes: [https]
    resource: routing.controllers
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
namespace Symfony\Component\Routing\Loader\Configurator;

return Routes::config([
    'controllers' => [
        'resource' => '../../src/Controller/',
        'type' => 'attribute',
        'schemes' => ['https'],
    ],
]);
```

Note

The Security component provides another way to enforce HTTP or HTTPS via the `requires_channel` setting.

A signed URI is an URI that includes a hash value that depends on the contents of the URI. This way, you can later check the integrity of the signed URI by recomputing its hash value and comparing it with the hash included in the URI.

Symfony provides a utility to sign URIs via the UriSigner service, which you can inject in your services or controllers:

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
namespace App\Service;

use Symfony\Component\HttpFoundation\UriSigner;

class SomeService
{
    public function __construct(
        private UriSigner $uriSigner,
    ) {
    }

    public function someMethod(): void
    {
        

        
        $url = 'https://example.com/foo/bar?sort=desc';

        
        $signedUrl = $this->uriSigner->sign($url);
        

        
        $uriSignatureIsValid = $this->uriSigner->check($signedUrl);
        

        
        
        $uriSignatureIsValid = $this->uriSigner->checkRequest($request);
    }
}
```

For security reasons, it's common to make signed URIs expire after some time (e.g. when using them to reset user credentials). By default, signed URIs don't expire, but you can define an expiration date/time using the `$expiration` argument of sign():

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
namespace App\Service;

use Symfony\Component\HttpFoundation\UriSigner;

class SomeService
{
    public function __construct(
        private UriSigner $uriSigner,
    ) {
    }

    public function someMethod(): void
    {
        

        
        $url = 'https://example.com/foo/bar?sort=desc';

        
        $signedUrl = $this->uriSigner->sign($url, new \DateTimeImmutable('2050-01-01'));
        

        
        $signedUrl = $this->uriSigner->sign($url, new \DateInterval('PT10S'));  
        

        
        $signedUrl = $this->uriSigner->sign($url, 4070908800); 
        
    }
}
```

Note

The expiration date/time is included in the signed URIs as a timestamp via the `_expiration` query parameter.

If you need to know the reason why a signed URI is invalid, you can use the `verify()` method which throws exceptions on failure:

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
use Symfony\Component\HttpFoundation\Exception\ExpiredSignedUriException;
use Symfony\Component\HttpFoundation\Exception\UnsignedUriException;
use Symfony\Component\HttpFoundation\Exception\UnverifiedSignedUriException;

try {
    $uriSigner->verify($uri); 

    
} catch (UnsignedUriException) {
    
} catch (UnverifiedSignedUriException) {
    
} catch (ExpiredSignedUriException) {
    
}
```

Tip

If `symfony/clock` is installed, it will be used to create and verify expirations. This allows you to mock the current time in your tests.

Another way to validate incoming requests is to use the `#[IsSignatureValid]` attribute.

In the following example, all incoming requests to this controller action will be verified for a valid signature. If the signature is missing or invalid, a `SignedUriException` will be thrown:

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
use Symfony\Component\HttpKernel\Attribute\IsSignatureValid;

#[IsSignatureValid]
public function someAction(): Response
{
    
}
```

To restrict signature validation to specific HTTP methods, use the `methods` argument. This can be a string or an array of methods:

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
#[IsSignatureValid(methods: 'POST')]
public function createItem(): Response
{
    
}

#[IsSignatureValid(methods: ['POST', 'PUT'])]
public function updateItem(): Response
{
    
}
```

You can also apply `#[IsSignatureValid]` at the controller class level. This way, all actions within the controller will automatically be protected by signature validation:

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
use Symfony\Component\HttpKernel\Attribute\IsSignatureValid;

#[IsSignatureValid]
class SecureController extends AbstractController
{
    public function index(): Response
    {
        
    }

    public function submit(): Response
    {
        
    }
}
```

This attribute provides a declarative way to enforce request signature validation directly at the controller level, helping to keep your security logic consistent and maintainable.

Here are some common errors you might see while working with routing:

```
1
2
```

```
Controller "App\\Controller\\BlogController::show()" requires that you
provide a value for the "$slug" argument.
```

This happens when your controller method has an argument (e.g. `$slug`):

```
1
2
3
4
```

```
public function show(string $slug): Response
{
    
}
```

But your route path does *not* have a `{slug}` parameter (e.g. it is `/blog/show`). Add a `{slug}` to your route path: `/blog/show/{slug}` or give the argument a default value (i.e. `$slug = null`).

```
1
2
```

```
Some mandatory parameters are missing ("slug") to generate a URL for route
"blog_show".
```

This means that you're trying to generate a URL to the `blog_show` route but you are *not* passing a `slug` value (which is required, because it has a `{slug}` parameter in the route path). To fix this, pass a `slug` value when generating the route:

```
1
```

```
$this->generateUrl('blog_show', ['slug' => 'slug-value']);
```

or, in Twig:

```
1
```

```
{{ path('blog_show', {slug: 'slug-value'}) }}
```

This work, including the code samples, is licensed under a

Creative Commons BY-SA 3.0

license.

Version
