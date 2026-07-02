---
title: "Front controller"
source: https://en.wikipedia.org/wiki/Front_controller
domain: hanami-ruby
license: CC-BY-SA-4.0
tags: hanami ruby framework, clean architecture ruby, ruby web framework, hanami actions
fetched: 2026-07-02
---

# Front controller

The **front controller** software design pattern is listed in several pattern catalogs and is related to the design of web applications. It is "a controller that handles all requests for a website," which is a useful structure for web application developers to achieve flexibility and reuse without code redundancy.

## Instruction

Front controllers are often used in web applications to implement workflows. While not strictly required, it is much easier to control navigation across a set of related pages (for instance, multiple pages used in an online purchase) from a front controller than it is to assign individual pages responsibility for navigation.

The front controller may be implemented as a Java object, or as a script in a scripting language such as PHP, Raku, Python or Ruby that is called for every request of a web session. This script would handle all tasks that are common to the application or the framework, such as session handling, caching and input filtering. Based on the specific request, it would then instantiate further objects and call methods to handle the required tasks.

The alternative to a front controller is the usage of page controllers mapped to each site page or path. Although this may cause each individual controller to contain duplicate code, the page-controller approach delivers a high degree of specialization.

## Examples

Several web-tier application frameworks implement the front controller pattern:

- Apache Struts
- ASP.NET MVC
- Cairngorm framework in Adobe Flex
- Cro or Bailador frameworks in Raku
- Drupal
- MVC frameworks written in PHP, such as Yii, CakePHP, Laravel, Symfony, CodeIgniter and Laminas
- Spring Framework
- Yesod, written in Haskell

## Implementation

Front controllers may divided into three components:

1. XML mapping: files that map requests to the class that will handle the request processing.
2. Request processor: used for request processing and modifying or retrieving the appropriate model.
3. Flow manager: determines what will be shown on the next page.

### Participants and responsibilities

| Controller | Dispatcher | Helper | View |
|---|---|---|---|
| The controller is an entrance for users to handle requests in the system. It realizes authentication by playing the role of delegating helper or initiating contact retrieval. | Dispatchers can be used for navigation and managing the view output. Users will receive the next view that is determined by the dispatcher. Dispatchers are also flexible; they can be encapsulated within the controller directly or separated into another component. The dispatcher provides a static view along with the dynamic mechanism. | Helpers assist in the processing of views or controllers. On the view side, the helper collects data and sometimes stores data as an intermediate station. Helpers do certain preprocesses such as formatting of the data to web content or providing direct access to the raw data. Multiple helpers can collaborate with one view for most conditions. Additionally, a helper works as a transformer that adapts and converts the model into a suitable format. | With the collaboration of helpers, views display information to the client by processing data from a model. The view will display if the processing succeeds, and vice versa. |

### Java implementation example

The front controller implemented in Java code:

```mw
import java.io.IOException;

import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

private void doProcess(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
    // ...
    try {
        getRequestProcessor().processRequest(request);
        getScreenFlowManager().forwardToNextScreen(request, response);
    } catch (Throwable t) {
        String className = ex.getClass().getName();
        nextScreen = getScreenFlowManager().getExceptionScreen(t);
        // Put the exception in the request
        request.setAttribute("jakarta.servlet.jsp.JspException", t);
        if (nextScreen == null) {
            // Send to general error screen
            ex.printStackTrace();
            throw new ServletException("MainServlet: unknown exception: " + className);
        }
    }
```

## Benefits and liabilities

There are three primary benefits associated with the front controller pattern.

- **Centralized control**. The front controller handles all the requests to the web application. This implementation of centralized control that avoids using multiple controllers is desirable for enforcing application-wide policies such as user tracking and security.
- **Thread safety**. A new command object arises when receiving a new request, and the command objects are not meant to be thread-safe. Thus, it will be safe in the command classes. Though safety is not guaranteed when threading issues are gathered, code that interacts with commands is still thread-safe.
- **Configurability**. As only one front controller is employed in a web application, the application configuration may be greatly simplified. Because the handler shares the responsibility of dispatching, new commands may be added without changes needed to the code.

The front controller pattern may incur performance issues because the single controller is performing a great deal of work, and handlers may introduce bottlenecks if they involve database or document queries. The front controller approach is also more complex than that of page controllers.

## Relationship with MVC

1. In order to improve system reliability and maintainability, duplicate code should be avoided and centralized when it involves common logic used throughout the system.
2. The data for the application is best handled in a single location, obviating the need for duplicate data-retrieval code.
3. Different roles in the model–view–controller (MVC) pattern should be separated to increase testability, which is also true for the controller part in the MVC pattern.

## Comparison

The page-controller pattern is an alternative to the front controller approach in the MVC model.

|   | Page Controller | Front Controller |
|---|---|---|
| Base class | A base class is needed and will grow simultaneously with the development of the application. | The centralization of requests is easier to modify than is a base class. |
| Security | Low security because various objects react differently without consistency. | High, because the controller is implemented in a coordinated fashion. |
| Logical Page | Single object on each logical page. | Only one controller handles all requests. |
| Complexity | Low | High |
