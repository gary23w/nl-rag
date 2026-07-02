"""Web backend frameworks, ORMs, and server-side concepts."""

from .common import CC_BY_SA, WIKI, wiki

DOMAINS = {
    "spring-boot": {
        "tags": ["spring boot", "spring framework", "java backend", "spring security"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Spring_Boot",
            "Spring_Framework",
            "Spring_Security",
            "Java_(programming_language)",
            "Enterprise_JavaBeans",
        ) + [
            "https://docs.spring.io/spring-boot/index.html",
        ],
    },
    "aspnet-core": {
        "tags": ["asp.net core", "asp.net mvc", "dotnet web", "razor pages"],
        "license": CC_BY_SA,
        "pages": wiki(
            "ASP.NET_Core",
            "ASP.NET",
            "ASP.NET_MVC",
            ".NET",
            "C_Sharp_(programming_language)",
            "Model%E2%80%93view%E2%80%93controller",
        ),
    },
    "laravel": {
        "tags": ["laravel framework", "eloquent orm", "php framework", "blade templating"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Laravel",
            "PHP",
            "Composer_(software)",
            "Object-relational_mapping",
        ) + [
            "https://laravel.com/docs/11.x/routing",
            "https://laravel.com/docs/11.x/eloquent",
        ],
    },
    "symfony": {
        "tags": ["symfony framework", "twig template", "doctrine orm", "php components"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Symfony",
            "Twig_(template_engine)",
            "Doctrine_(PHP)",
            "PHP",
        ) + [
            "https://symfony.com/doc/current/routing.html",
            "https://symfony.com/doc/current/page_creation.html",
        ],
    },
    "sinatra": {
        "tags": ["sinatra framework", "ruby microframework", "rack interface", "ruby web dsl"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Sinatra_(software)",
            "Ruby_(programming_language)",
            "Rack_(web_server_interface)",
            "Domain-specific_language",
        ) + [
            "https://sinatrarb.com/intro.html",
            "https://sinatrarb.com/configuration.html",
        ],
    },
    "nestjs": {
        "tags": ["nestjs framework", "nest modules", "typescript backend", "node.js framework"],
        "license": CC_BY_SA,
        "pages": wiki(
            "NestJS",
            "TypeScript",
            "Node.js",
            "Dependency_injection",
            "Modular_programming",
        ) + [
            "https://docs.nestjs.com/",
        ],
    },
    "koa": {
        "tags": ["koa web framework", "koa middleware", "async middleware", "node.js framework"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Express.js",
            "Middleware_(distributed_applications)",
            "Node.js",
            "JavaScript",
            "Callback_(computer_programming)",
        ) + [
            "https://koajs.com/",
        ],
    },
    "hapi": {
        "tags": ["hapi framework", "hapijs server", "node.js framework", "server configuration"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Hapi",
            "Node.js",
            "Web_framework",
            "Web_server",
            "JavaScript",
            "Plug-in_(computing)",
        ),
    },
    "fastify": {
        "tags": ["fastify framework", "fastify plugin", "node.js framework", "json schema validation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Fastify",
            "Node.js",
            "JSON",
            "JSON_Schema",
            "Plug-in_(computing)",
        ) + [
            "https://fastify.dev/docs/latest/Guides/Getting-Started/",
        ],
    },
    "gin-gonic": {
        "tags": ["gin gonic", "gin framework", "go web framework", "gin router"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Go_(programming_language)",
            "Web_framework",
            "Middleware_(distributed_applications)",
            "Routing",
            "Web_application",
        ) + [
            "https://gin-gonic.com/en/docs/",
        ],
    },
    "echo-framework": {
        "tags": ["echo framework", "echo golang", "go web framework", "echo middleware"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Go_(programming_language)",
            "Web_framework",
            "Front_controller",
            "Web_server",
            "Routing",
        ) + [
            "https://echo.labstack.com/docs",
        ],
    },
    "fiber-framework": {
        "tags": ["fiber framework", "fiber golang", "go web framework", "fasthttp server"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Go_(programming_language)",
            "Web_framework",
            "Green_thread",
            "Web_server",
            "Concurrent_computing",
        ) + [
            "https://docs.gofiber.io/",
        ],
    },
    "actix-web": {
        "tags": ["actix web", "actix rust", "rust web framework", "actor model server"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Actix",
            "Rust_(programming_language)",
            "Web_framework",
            "Actor_model",
            "Reactor_pattern",
        ) + [
            "https://actix.rs/docs/",
        ],
    },
    "axum-rust": {
        "tags": ["axum framework", "axum rust", "tokio web", "rust web framework"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Rust_(programming_language)",
            "Web_framework",
            "Async/await",
            "Tokio_(software)",
            "Middleware_(distributed_applications)",
            "Non-blocking_I/O_(Java)",
        ),
    },
    "rocket-rust": {
        "tags": ["rocket framework", "rocket rust", "rust web framework", "type-safe routing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Rust_(programming_language)",
            "Web_framework",
            "Routing",
            "Request%E2%80%93response",
            "Macro_(computer_science)",
            "Server_(computing)",
        ),
    },
    "phoenix-framework": {
        "tags": ["phoenix framework", "phoenix liveview", "elixir web", "erlang otp"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Phoenix_(web_framework)",
            "Elixir_(programming_language)",
            "Erlang_(programming_language)",
            "Concurrent_computing",
            "Model%E2%80%93view%E2%80%93controller",
        ) + [
            "https://hexdocs.pm/phoenix/overview.html",
        ],
    },
    "play-framework": {
        "tags": ["play framework", "scala web", "reactive web framework", "akka backend"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Play_Framework",
            "Scala_(programming_language)",
            "Reactive_programming",
            "Actor_model",
            "Non-blocking_I/O_(Java)",
        ) + [
            "https://www.playframework.com/documentation/latest/Home",
        ],
    },
    "ktor": {
        "tags": ["ktor framework", "kotlin server", "kotlin coroutines", "asynchronous server"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Ktor",
            "Kotlin_(programming_language)",
            "Coroutine",
            "Async/await",
            "Web_server",
        ) + [
            "https://ktor.io/docs/welcome.html",
        ],
    },
    "quarkus": {
        "tags": ["quarkus framework", "quarkus native", "graalvm native", "jakarta ee"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Quarkus",
            "GraalVM",
            "Jakarta_EE",
            "Microservices",
            "Java_(programming_language)",
        ) + [
            "https://quarkus.io/guides/getting-started",
        ],
    },
    "micronaut": {
        "tags": ["micronaut framework", "micronaut jvm", "compile-time injection", "microservices framework"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Micronaut",
            "Dependency_injection",
            "Microservices",
            "Java_(programming_language)",
            "Modular_programming",
        ) + [
            "https://docs.micronaut.io/latest/guide/index.html",
        ],
    },
    "vertx": {
        "tags": ["vert.x toolkit", "eclipse vertx", "reactive toolkit", "event loop server"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Vert.x",
            "Reactive_programming",
            "Event_loop",
            "Non-blocking_I/O_(Java)",
            "Reactor_pattern",
        ) + [
            "https://vertx.io/docs/vertx-core/java/",
        ],
    },
    "tornado-web": {
        "tags": ["tornado web server", "tornado framework", "python async server", "non-blocking python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Tornado_(web_server)",
            "Python_(programming_language)",
            "Event_loop",
            "Coroutine",
        ) + [
            "https://www.tornadoweb.org/en/stable/guide.html",
            "https://www.tornadoweb.org/en/stable/httpserver.html",
        ],
    },
    "sanic": {
        "tags": ["sanic framework", "sanic python", "async python web", "asgi server"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Sanic",
            "Python_(programming_language)",
            "Asynchronous_Server_Gateway_Interface",
            "Async/await",
            "Event_loop",
        ) + [
            "https://sanic.dev/en/guide/getting-started.html",
        ],
    },
    "aiohttp": {
        "tags": ["aiohttp library", "asyncio http", "python async web", "asyncio coroutines"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Python_(programming_language)",
            "Asynchronous_Server_Gateway_Interface",
            "Coroutine",
            "Async/await",
            "Futures_and_promises",
        ) + [
            "https://docs.aiohttp.org/en/stable/web_quickstart.html",
        ],
    },
    "bottle-py": {
        "tags": ["bottle framework", "bottle python", "python microframework", "wsgi application"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Python_(programming_language)",
            "Web_Server_Gateway_Interface",
            "Web_framework",
            "Template_processor",
            "Routing",
        ) + [
            "https://bottlepy.org/docs/dev/tutorial.html",
        ],
    },
    "falcon-api": {
        "tags": ["falcon framework", "falcon python", "python rest framework", "wsgi application"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Python_(programming_language)",
            "Web_Server_Gateway_Interface",
            "Representational_state_transfer",
            "Web_API",
            "Web_service",
        ) + [
            "https://falcon.readthedocs.io/en/stable/user/quickstart.html",
        ],
    },
    "hibernate-orm": {
        "tags": ["hibernate orm", "jpa persistence", "hql query", "java persistence"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Hibernate_(framework)",
            "Jakarta_Persistence",
            "Java_Persistence_Query_Language",
            "Object-relational_mapping",
            "Lazy_loading",
        ) + [
            "https://hibernate.org/orm/documentation/getting-started/",
        ],
    },
    "sqlalchemy": {
        "tags": ["sqlalchemy orm", "sqlalchemy core", "python orm", "declarative mapping"],
        "license": CC_BY_SA,
        "pages": wiki(
            "SQLAlchemy",
            "Object-relational_mapping",
            "Data_mapper_pattern",
            "Python_(programming_language)",
            "SQL",
        ) + [
            "https://docs.sqlalchemy.org/en/20/orm/quickstart.html",
        ],
    },
    "prisma-orm": {
        "tags": ["prisma orm", "prisma schema", "prisma client", "typescript orm"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Prisma",
            "Object-relational_mapping",
            "TypeScript",
            "Schema_migration",
            "Database_schema",
        ) + [
            "https://www.prisma.io/docs/orm/prisma-schema/overview",
        ],
    },
    "typeorm": {
        "tags": ["typeorm library", "typescript orm", "data mapper pattern", "entity decorators"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Object-relational_mapping",
            "TypeScript",
            "Data_mapper_pattern",
            "Active_record_pattern",
            "Decorator_pattern",
        ) + [
            "https://typeorm.io/",
        ],
    },
    "sequelize": {
        "tags": ["sequelize orm", "node.js orm", "javascript orm", "model definition"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Object-relational_mapping",
            "Node.js",
            "JavaScript",
            "Active_record_pattern",
            "Foreign_key",
        ) + [
            "https://www.sequelize.org/docs/v6/core-concepts/model-basics/",
        ],
    },
    "entity-framework": {
        "tags": ["entity framework", "ef core", "linq to entities", "dotnet orm"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Entity_Framework",
            "Language_Integrated_Query",
            "Object-relational_mapping",
            ".NET",
            "C_Sharp_(programming_language)",
        ) + [
            "https://learn.microsoft.com/en-us/ef/core/",
        ],
    },
    "activerecord-orm": {
        "tags": ["active record pattern", "rails activerecord", "ruby orm", "database migrations"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Active_record_pattern",
            "Ruby_on_Rails",
            "Object-relational_mapping",
            "Schema_migration",
            "Create,_read,_update_and_delete",
        ) + [
            "https://guides.rubyonrails.org/active_record_basics.html",
        ],
    },
    "drizzle-orm": {
        "tags": ["drizzle orm", "typescript query builder", "sql-like orm", "type-safe queries"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Drizzle",
            "Object-relational_mapping",
            "TypeScript",
            "Query_language",
            "SQL",
        ) + [
            "https://orm.drizzle.team/docs/overview",
        ],
    },
    "jinja-templating": {
        "tags": ["jinja template", "jinja2 engine", "python templating", "template inheritance"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Jinja_(template_engine)",
            "Template_processor",
            "Web_template_system",
            "Comparison_of_web_template_engines",
            "Escape_character",
        ) + [
            "https://jinja.palletsprojects.com/en/stable/templates/",
        ],
    },
    "thymeleaf": {
        "tags": ["thymeleaf engine", "thymeleaf template", "java templating", "natural templates"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Thymeleaf",
            "Template_processor",
            "JavaServer_Pages",
            "Web_template_system",
            "HTML",
        ) + [
            "https://www.thymeleaf.org/documentation.html",
        ],
    },
    "razor-pages": {
        "tags": ["razor pages", "razor markup", "asp.net templating", "cshtml views"],
        "license": CC_BY_SA,
        "pages": wiki(
            "ASP.NET_Razor",
            "ASP.NET_Core",
            "Template_processor",
            "Web_template_system",
            "Model%E2%80%93view%E2%80%93viewmodel",
            "Model%E2%80%93view%E2%80%93controller",
        ),
    },
    "server-side-rendering": {
        "tags": ["server-side rendering", "dynamic web page", "server-side scripting", "html hydration"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Dynamic_web_page",
            "Server-side_scripting",
            "Hydration_(web_development)",
            "Progressive_enhancement",
            "Web_template_system",
            "Document_Object_Model",
        ),
    },
    "session-management": {
        "tags": ["session management", "http session", "session identifier", "session cookie"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Session_(computer_science)",
            "Session_ID",
            "HTTP_cookie",
            "Stateless_protocol",
            "State_(computer_science)",
            "Access_token",
        ),
    },
    "web-middleware": {
        "tags": ["web middleware", "request pipeline", "middleware chain", "front controller pattern"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Middleware_(distributed_applications)",
            "Front_controller",
            "Reactor_pattern",
            "Web_server",
            "Application_server",
            "Decorator_pattern",
        ),
    },
    "api-authentication": {
        "tags": ["api authentication", "oauth flow", "openid connect", "bearer token"],
        "license": CC_BY_SA,
        "pages": wiki(
            "OAuth",
            "OpenID_Connect",
            "JSON_Web_Token",
            "API_key",
            "Access_token",
            "Basic_access_authentication",
            "Single_sign-on",
        ),
    },
    "api-pagination": {
        "tags": ["api pagination", "cursor pagination", "page navigation", "result paging"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Pagination",
            "Web_API",
            "Representational_state_transfer",
            "Rate_limiting",
            "Query_language",
            "Uniform_Resource_Identifier",
        ),
    },
    "csrf-protection": {
        "tags": ["csrf protection", "cross-site request forgery", "same-origin policy", "anti-forgery token"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cross-site_request_forgery",
            "Same-origin_policy",
            "Cross-origin_resource_sharing",
            "HTTP_cookie",
            "Session_ID",
            "Cross-site_scripting",
        ),
    },
    "content-negotiation": {
        "tags": ["content negotiation", "media type", "accept header", "mime type"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Content_negotiation",
            "Media_type",
            "HTTP_header",
            "Hypertext_Transfer_Protocol",
            "List_of_HTTP_status_codes",
            "Character_encoding",
        ),
    },
    "background-jobs": {
        "tags": ["background jobs", "job queue", "scheduled task", "batch processing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Job_queue",
            "Scheduling_(computing)",
            "Batch_processing",
            "Cron",
            "Celery_(software)",
            "Task_(computing)",
        ),
    },
    "task-queues": {
        "tags": ["task queue", "message queue", "distributed task", "worker queue"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Message_queue",
            "Celery_(software)",
            "RabbitMQ",
            "Apache_Kafka",
            "Publish%E2%80%93subscribe_pattern",
            "Producer%E2%80%93consumer_problem",
        ),
    },
    "websocket-server": {
        "tags": ["websocket server", "server-sent events", "long polling", "push technology"],
        "license": CC_BY_SA,
        "pages": wiki(
            "WebSocket",
            "Server-sent_events",
            "Push_technology",
            "Long_polling",
            "Comet_(programming)",
            "HTTP_persistent_connection",
        ),
    },
    "connection-pooling": {
        "tags": ["connection pooling", "database connection", "object pool pattern", "connection reuse"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Connection_pool",
            "Database_connection",
            "Object_pool_pattern",
            "Thread_pool",
            "Database_transaction",
            "Load_balancing_(computing)",
        ),
    },
    "dependency-injection-web": {
        "tags": ["dependency injection", "inversion of control", "ioc container", "service injection"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Dependency_injection",
            "Inversion_of_control",
            "Data_access_object",
            "Microservices",
            "Modular_programming",
            "Plug-in_(computing)",
        ),
    },
    "request-validation": {
        "tags": ["request validation", "input validation", "schema validation", "data validation rules"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Data_validation",
            "Input_validation",
            "JSON_Schema",
            "XML_schema",
            "Regular_expression",
            "Cross-site_scripting",
        ),
    },
    "api-versioning": {
        "tags": ["api versioning", "software versioning", "rest versioning", "backward compatibility"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Software_versioning",
            "Semantic_versioning",
            "Backward_compatibility",
            "Representational_state_transfer",
            "Web_API",
            "Idempotence",
        ),
    },
}
