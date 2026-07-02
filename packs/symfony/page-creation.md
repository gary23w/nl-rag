---
title: "Create your First Page in Symfony (Symfony Docs)"
source: https://symfony.com/doc/current/page_creation.html
domain: symfony
license: CC-BY-SA-4.0
tags: symfony framework, twig template, doctrine orm, php components
fetched: 2026-07-02
---

# Create your First Page in Symfony

Creating a new page - whether it's an HTML page or a JSON endpoint - is a two-step process:

1. **Create a controller**: A controller is the PHP function you write that builds the page. You take the incoming request information and use it to create a Symfony `Response` object, which can hold HTML content, a JSON string or even a binary file like an image or PDF;
2. **Create a route**: A route is the URL (e.g. `/about`) to your page and points to a controller.

Screencast

Do you prefer video tutorials? Check out the Cosmic Coding with Symfony screencast series.

See also

Symfony *embraces* the HTTP Request-Response lifecycle. To find out more, see Symfony and HTTP Fundamentals.

Tip

Before continuing, make sure you've read the Setup article and can access your new Symfony app in the browser.

Suppose you want to create a page - `/lucky/number` - that generates a lucky (well, random) number and prints it. To do that, create a "Controller" class and a "number" method inside of it:

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
<?php

namespace App\Controller;

use Symfony\Component\HttpFoundation\Response;

class LuckyController
{
    public function number(): Response
    {
        $number = random_int(0, 100);

        return new Response(
            '<html><body>Lucky number: '.$number.'</body></html>'
        );
    }
}
```

Now you need to associate this controller function with a public URL (e.g. `/lucky/number`) so that the `number()` method is called when a user browses to it. This association is defined with the `#[Route]` attribute (in PHP, attributes are used to add metadata to code):

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
// src/Controller/LuckyController.php

  // ...
+ use Symfony\Component\Routing\Attribute\Route;

  class LuckyController
  {
+     #[Route('/lucky/number')]
      public function number(): Response
      {
          // this looks exactly the same
      }
  }
```

That's it! If you are using the Symfony web server, try it out by going to: http://localhost:8000/lucky/number

Tip

Symfony recommends defining routes as attributes to have the controller code and its route configuration at the same location. However, if you prefer, you can define routes in separate files using the YAML or PHP formats.

If you see a lucky number being printed back to you, congratulations! But before you run off to play the lottery, check out how this works. Remember the two steps to create a page?

1. *Create a controller and a method*: This is a function where *you* build the page and ultimately return a `Response` object. You'll learn more about controllers in their own section, including how to return JSON responses;
2. *Create a route*: The route defines the URL path to your page and what controller method to call. You'll learn more about routing in its own section, including how to make *variable* URLs.

Your project already has a powerful debugging tool inside: the `bin/console` command. Try running it:

```
1
```

```
$ php bin/console
```

You should see a list of commands that can give you debugging information, help generate code, generate database migrations and a lot more. As you install more packages, you'll see more commands.

To get a list of *all* of the routes in your system, use the `debug:router` command:

```
1
```

```
$ php bin/console debug:router
```

You should see your `app_lucky_number` route in the list:

```
1
2
3
4
5
```

```
----------------  -------  --------------
Name              Method   Path
----------------  -------  --------------
app_lucky_number  ANY      /lucky/number
----------------  -------  --------------
```

You will also see debugging routes besides `app_lucky_number` -- more on the debugging routes in the next section.

You'll learn about many more commands as you continue!

Tip

If your shell is supported, you can also set up console completion support. This autocompletes commands and other input when using `bin/console`. See the Console document for more information on how to set up completion.

One of Symfony's *amazing* features is the Web Debug Toolbar: a bar that displays a *huge* amount of debugging information along the bottom of your page while developing. This is all included by default when using a Symfony pack called `symfony/profiler-pack`.

You will see a dark bar along the bottom of the page. You'll learn more about all the information it holds along the way, but feel free to experiment: hover over and click the different icons to get information about routing, performance, logging and more.

If you're returning HTML from your controller, you'll probably want to render a template. Fortunately, Symfony comes with Twig: a templating language that's minimal, powerful and actually quite fun.

Install the twig package with:

```
1
```

```
$ composer require twig
```

Make sure that `LuckyController` extends Symfony's base AbstractController class:

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
// src/Controller/LuckyController.php

  // ...
+ use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;

- class LuckyController
+ class LuckyController extends AbstractController
  {
      // ...
  }
```

Now, use the handy `render()` method to render a template. Pass it a `number` variable so you can use it in Twig:

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
namespace App\Controller;

use Symfony\Component\HttpFoundation\Response;

class LuckyController extends AbstractController
{
    #[Route('/lucky/number')]
    public function number(): Response
    {
        $number = random_int(0, 100);

        return $this->render('lucky/number.html.twig', [
            'number' => $number,
        ]);
    }
}
```

Template files live in the `templates/` directory, which was created for you automatically when you installed Twig. Create a new `templates/lucky` directory with a new `number.html.twig` file inside:

```
1
2
```

```
<h1>Your lucky number is {{ number }}</h1>
```

The `{{ number }}` syntax is used to *print* variables in Twig. Refresh your browser to get your *new* lucky number!

> http://localhost:8000/lucky/number

Now you may wonder where the Web Debug Toolbar has gone: that's because there is no `</body>` tag in the current template. You can add the body element yourself, or extend `base.html.twig`, which contains all default HTML elements.

In the templates article, you'll learn all about Twig: how to loop, render other templates and leverage its powerful layout inheritance system.

Great news! You've already worked inside the most important directories in your project:

**`config/`**

Contains configuration. You will configure routes,

services

and packages.

**`src/`**

All your PHP code lives here.

**`templates/`**

All your Twig templates live here.

Most of the time, you'll be working in `src/`, `templates/` or `config/`. As you keep reading, you'll learn what can be done inside each of these.

So what about the other directories in the project?

**`bin/`**

The famous

bin/console

file lives here (and other, less important executable files).

**`var/`**

This is where automatically-created files are stored, like cache files (

var/cache/

) and logs (

var/log/

).

**`vendor/`**

Third-party (i.e. "vendor") libraries live here! These are downloaded via the

Composer

package manager.

**`public/`**

This is the document root for your project: you put any publicly accessible files here.

And when you install new packages, new directories will be created automatically when needed.

Congrats! You're already starting to learn Symfony and discover a whole new way of building beautiful, functional, fast and maintainable applications.

OK, time to finish learning the fundamentals by reading these articles:

- Routing
- Controller
- Creating and Using Templates
- Front-end Tools: Handling CSS & JavaScript
- Configuring Symfony

Then, learn about other important topics like the service container, the form system, using Doctrine (if you need to query a database) and more!

Have fun!

This work, including the code samples, is licensed under a

Creative Commons BY-SA 3.0

license.

Version
