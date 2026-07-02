"""More web backend frameworks and server-side patterns."""
from .common import CC_BY_SA, wiki

DOMAINS = {
    "rails-deep": {
        "tags": ["ruby on rails", "rails active record", "convention over configuration", "rails mvc framework"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Ruby_on_Rails",
            "Active_record_pattern",
            "Model%E2%80%93view%E2%80%93controller",
            "Convention_over_configuration",
            "Object%E2%80%93relational_mapping",
            "Web_service",
        ) + [
            "https://guides.rubyonrails.org/active_record_basics.html",
        ],
    },
    "sinatra-deep": {
        "tags": ["sinatra ruby framework", "rack web interface", "ruby microframework", "sinatra routing dsl"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Sinatra_(software)",
            "Rack_(web_server_interface)",
            "Ruby_(programming_language)",
            "Web_framework",
            "Domain-specific_language",
        ) + [
            "https://sinatrarb.com/intro.html",
        ],
    },
    "hanami-ruby": {
        "tags": ["hanami ruby framework", "clean architecture ruby", "ruby web framework", "hanami actions"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Ruby_(programming_language)",
            "Web_framework",
            "Model%E2%80%93view%E2%80%93controller",
            "Separation_of_concerns",
            "Front_controller",
        ) + [
            "https://guides.hanamirb.org/introduction/getting-started/",
        ],
    },
    "roda-ruby": {
        "tags": ["roda ruby framework", "rack routing tree", "ruby routing framework", "roda plugin system"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Rack_(web_server_interface)",
            "Ruby_(programming_language)",
            "Web_framework",
            "Routing",
            "Tree_(abstract_data_type)",
        ) + [
            "https://roda.jeremyevans.net/documentation.html",
        ],
    },
    "phoenix-liveview": {
        "tags": ["phoenix liveview elixir", "server rendered interactivity", "elixir web framework", "liveview stateful process"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Phoenix_(web_framework)",
            "Elixir_(programming_language)",
            "WebSocket",
            "Server-sent_events",
            "Erlang_(programming_language)",
        ) + [
            "https://hexdocs.pm/phoenix_live_view/welcome.html",
        ],
    },
    "plug-elixir": {
        "tags": ["plug elixir specification", "elixir middleware composition", "erlang web adapter", "plug connection pipeline"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Elixir_(programming_language)",
            "Erlang_(programming_language)",
            "Middleware_(distributed_applications)",
            "Web_server",
            "Function_composition_(computer_science)",
        ) + [
            "https://hexdocs.pm/plug/readme.html",
        ],
    },
    "litestar-python": {
        "tags": ["litestar python framework", "asgi python framework", "python type hints api", "litestar dependency injection"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Python_(programming_language)",
            "Asynchronous_Server_Gateway_Interface",
            "Web_framework",
            "Type_signature",
            "Dependency_injection",
        ) + [
            "https://docs.litestar.dev/2/",
        ],
    },
    "robyn-python": {
        "tags": ["robyn python framework", "rust runtime python web", "async python framework", "robyn multi core"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Python_(programming_language)",
            "Rust_(programming_language)",
            "Web_framework",
            "Multi-core_processor",
            "Event_loop",
        ) + [
            "https://robyn.tech/documentation",
        ],
    },
    "blacksheep-python": {
        "tags": ["blacksheep python framework", "asgi web framework", "python async server", "blacksheep openapi generation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Python_(programming_language)",
            "Asynchronous_Server_Gateway_Interface",
            "Web_framework",
            "OpenAPI_Specification",
            "Async/await",
        ) + [
            "https://www.neoteroi.dev/blacksheep/",
        ],
    },
    "quart-async": {
        "tags": ["quart async framework", "asgi flask compatible", "python asynchronous framework", "quart websocket support"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Python_(programming_language)",
            "Asynchronous_Server_Gateway_Interface",
            "Web_Server_Gateway_Interface",
            "WebSocket",
            "Async/await",
        ) + [
            "https://quart.palletsprojects.com/en/latest/",
        ],
    },
    "pyramid-framework": {
        "tags": ["pyramid python framework", "pylons pyramid web", "python wsgi framework", "pyramid traversal routing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Pylons_project",
            "Python_(programming_language)",
            "Web_Server_Gateway_Interface",
            "Web_framework",
            "Routing",
        ) + [
            "https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/introduction.html",
        ],
    },
    "cherrypy-server": {
        "tags": ["cherrypy python framework", "object oriented web framework", "python wsgi server", "cherrypy http toolkit"],
        "license": CC_BY_SA,
        "pages": wiki(
            "CherryPy",
            "Python_(programming_language)",
            "Web_Server_Gateway_Interface",
            "Object-oriented_programming",
            "Web_server",
        ) + [
            "https://docs.cherrypy.dev/en/latest/tutorials.html",
        ],
    },
    "web2py-framework": {
        "tags": ["web2py python framework", "full stack python framework", "python web framework", "web2py database abstraction"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Web2py",
            "Python_(programming_language)",
            "Web_framework",
            "Model%E2%80%93view%E2%80%93controller",
            "Database_abstraction_layer",
            "Don%27t_repeat_yourself",
        ),
    },
    "masonite-python": {
        "tags": ["masonite python framework", "developer friendly python", "python web framework", "masonite service container"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Python_(programming_language)",
            "Web_framework",
            "Model%E2%80%93view%E2%80%93controller",
            "Inversion_of_control",
            "Active_record_pattern",
        ) + [
            "https://docs.masoniteproject.com/",
        ],
    },
    "adonisjs-node": {
        "tags": ["adonisjs node framework", "typescript node framework", "node.js mvc framework", "adonis lucid orm"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Node.js",
            "TypeScript",
            "Web_framework",
            "Model%E2%80%93view%E2%80%93controller",
            "Active_record_pattern",
        ) + [
            "https://docs.adonisjs.com/guides/preface/introduction",
        ],
    },
    "feathersjs-node": {
        "tags": ["feathersjs node framework", "real time api framework", "node.js service framework", "feathers service hooks"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Node.js",
            "JavaScript",
            "Representational_state_transfer",
            "WebSocket",
            "Web_service",
        ) + [
            "https://feathersjs.com/guides/",
        ],
    },
    "loopback-node": {
        "tags": ["loopback node framework", "ibm loopback api", "node.js api framework", "loopback model driven"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Create,_read,_update_and_delete",
            "Node.js",
            "Representational_state_transfer",
            "OpenAPI_Specification",
            "Web_API",
        ) + [
            "https://loopback.io/doc/en/lb4/",
        ],
    },
    "sails-node": {
        "tags": ["sails node framework", "sails mvc framework", "node.js realtime framework", "waterline orm adapter"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Sails.js",
            "Node.js",
            "Model%E2%80%93view%E2%80%93controller",
            "WebSocket",
            "Object-relational_mapping",
        ) + [
            "https://sailsjs.com/documentation/reference",
        ],
    },
    "restify-node": {
        "tags": ["restify node framework", "rest api node server", "node.js rest framework", "restify request handler"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Node.js",
            "Representational_state_transfer",
            "Web_API",
            "JavaScript",
            "Hypertext_Transfer_Protocol",
        ) + [
            "http://restify.com/docs/home/",
        ],
    },
    "polka-node": {
        "tags": ["polka node microframework", "minimal node router", "node.js http server", "polka middleware chain"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Node.js",
            "JavaScript",
            "Web_server",
            "Middleware_(distributed_applications)",
            "Routing",
        ) + [
            "https://github.com/lukeed/polka",
        ],
    },
    "hono-framework": {
        "tags": ["hono web framework", "edge runtime framework", "javascript web framework", "hono multi runtime"],
        "license": CC_BY_SA,
        "pages": wiki(
            "JavaScript",
            "TypeScript",
            "Web_framework",
            "Edge_computing",
            "Serverless_computing",
        ) + [
            "https://hono.dev/docs/",
        ],
    },
    "elysia-bun": {
        "tags": ["elysia bun framework", "bun runtime web", "typescript bun framework", "elysia end to end typing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "TypeScript",
            "JavaScript_engine",
            "Web_framework",
            "Type_signature",
            "OpenAPI_Specification",
        ) + [
            "https://elysiajs.com/",
        ],
    },
    "oak-deno": {
        "tags": ["oak deno framework", "deno middleware framework", "deno web server", "oak context router"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Deno_(software)",
            "TypeScript",
            "Web_framework",
            "Middleware_(distributed_applications)",
            "Routing",
        ) + [
            "https://jsr.io/@oak/oak",
        ],
    },
    "fresh-deno": {
        "tags": ["fresh deno framework", "deno island architecture", "deno web framework", "fresh server rendering"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Deno_(software)",
            "TypeScript",
            "Web_framework",
            "Server-side_scripting",
            "Hydration_(web_development)",
        ) + [
            "https://fresh.deno.dev/docs/introduction",
        ],
    },
    "buffalo-go": {
        "tags": ["buffalo go framework", "go rapid web development", "golang full stack framework", "buffalo asset pipeline"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Go_(programming_language)",
            "Web_framework",
            "Model%E2%80%93view%E2%80%93controller",
            "Rapid_application_development",
            "Object-relational_mapping",
        ) + [
            "https://gobuffalo.io/documentation/getting_started/",
        ],
    },
    "beego-framework": {
        "tags": ["beego go framework", "golang mvc framework", "go rest framework", "beego bee tool"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Scaffold_(programming)",
            "Go_(programming_language)",
            "Model%E2%80%93view%E2%80%93controller",
            "Web_framework",
            "Representational_state_transfer",
        ) + [
            "https://beego.me/docs/intro/",
        ],
    },
    "revel-go": {
        "tags": ["revel go framework", "golang full stack framework", "go web framework", "revel hot reload"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Go_(programming_language)",
            "Web_framework",
            "Model%E2%80%93view%E2%80%93controller",
            "Hot_swapping",
            "Front_controller",
        ) + [
            "https://revel.github.io/manual/index.html",
        ],
    },
    "iris-go": {
        "tags": ["iris go framework", "golang web framework", "go http framework", "iris mvc router"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Go_(programming_language)",
            "Web_framework",
            "Model%E2%80%93view%E2%80%93controller",
            "Routing",
            "Web_server",
        ) + [
            "https://www.iris-go.com/docs/",
        ],
    },
    "chi-router-go": {
        "tags": ["chi router golang", "go http router", "golang lightweight router", "chi middleware stack"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Go_(programming_language)",
            "Routing",
            "Middleware_(distributed_applications)",
            "Web_server",
            "Representational_state_transfer",
        ) + [
            "https://go-chi.io/#/",
        ],
    },
    "fasthttp-server": {
        "tags": ["fasthttp go server", "golang high performance http", "zero allocation http", "fasthttp request context"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Go_(programming_language)",
            "Web_server",
            "Hypertext_Transfer_Protocol",
            "Memory_management",
            "Concurrent_computing",
        ) + [
            "https://pkg.go.dev/github.com/valyala/fasthttp",
        ],
    },
    "warp-rust-web": {
        "tags": ["warp rust framework", "rust filter composition", "tokio rust web", "warp reply rejection"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Rust_(programming_language)",
            "Web_framework",
            "Function_composition_(computer_science)",
            "Tokio_(software)",
            "Async/await",
        ) + [
            "https://docs.rs/warp/latest/warp/",
        ],
    },
    "tide-rust-web": {
        "tags": ["tide rust framework", "async-std web framework", "rust minimal framework", "tide middleware endpoint"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Rust_(programming_language)",
            "Web_framework",
            "Async/await",
            "Middleware_(distributed_applications)",
            "Futures_and_promises",
        ) + [
            "https://docs.rs/tide/latest/tide/",
        ],
    },
    "poem-rust-web": {
        "tags": ["poem rust framework", "rust openapi framework", "rust async web", "poem endpoint middleware"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Rust_(programming_language)",
            "Web_framework",
            "OpenAPI_Specification",
            "Async/await",
            "Middleware_(distributed_applications)",
        ) + [
            "https://docs.rs/poem/latest/poem/",
        ],
    },
    "salvo-rust-web": {
        "tags": ["salvo rust framework", "rust web server framework", "rust handler tree", "salvo flexible middleware"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Rust_(programming_language)",
            "Web_framework",
            "Routing",
            "Async/await",
            "Tokio_(software)",
        ) + [
            "https://docs.rs/salvo/latest/salvo/",
        ],
    },
    "dropwizard-java": {
        "tags": ["dropwizard java framework", "java restful microservice", "jvm ops friendly framework", "dropwizard jetty jersey"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Java_(programming_language)",
            "Representational_state_transfer",
            "Microservices",
            "Jetty_(web_server)",
            "Web_service",
        ) + [
            "https://www.dropwizard.io/en/stable/getting-started.html",
        ],
    },
    "javalin-java": {
        "tags": ["javalin jvm framework", "kotlin java web framework", "lightweight jvm framework", "javalin jetty embedded"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Java_(programming_language)",
            "Kotlin_(programming_language)",
            "Web_framework",
            "Jetty_(web_server)",
            "Representational_state_transfer",
        ) + [
            "https://javalin.io/documentation",
        ],
    },
    "spark-java-web": {
        "tags": ["spark java framework", "java microframework", "jvm expressive routes", "sparkjava embedded jetty"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Representational_state_transfer",
            "Java_(programming_language)",
            "Web_framework",
            "Jetty_(web_server)",
            "Routing",
        ) + [
            "https://sparkjava.com/documentation",
        ],
    },
    "vaadin-flow": {
        "tags": ["vaadin flow framework", "java server side ui", "jvm web components", "vaadin component model"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Vaadin",
            "Java_(programming_language)",
            "Web_Components",
            "Rich_web_application",
            "Server-side_scripting",
        ) + [
            "https://vaadin.com/docs/latest/getting-started",
        ],
    },
    "grails-framework": {
        "tags": ["grails groovy framework", "groovy on grails", "jvm convention framework", "gorm grails orm"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Grails_(framework)",
            "Apache_Groovy",
            "Convention_over_configuration",
            "Object-relational_mapping",
            "Model%E2%80%93view%E2%80%93controller",
        ) + [
            "https://docs.grails.org/latest/guide/introduction.html",
        ],
    },
    "ktor-server": {
        "tags": ["ktor kotlin server", "kotlin coroutines web", "jetbrains kotlin framework", "ktor plugin pipeline"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Ktor",
            "Kotlin_(programming_language)",
            "Coroutine",
            "Web_framework",
            "Async/await",
        ) + [
            "https://ktor.io/docs/server-create-a-new-project.html",
        ],
    },
    "http4k-server": {
        "tags": ["http4k kotlin toolkit", "server as function", "kotlin functional http", "http4k lens contract"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kotlin_(programming_language)",
            "Functional_programming",
            "Web_server",
            "Pure_function",
            "Hypertext_Transfer_Protocol",
        ) + [
            "https://www.http4k.org/guide/reference/core/",
        ],
    },
    "finatra-scala": {
        "tags": ["finatra scala framework", "twitter finagle services", "scala services framework", "finatra dependency injection"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Scala_(programming_language)",
            "Remote_procedure_call",
            "Microservices",
            "Dependency_injection",
            "Futures_and_promises",
        ) + [
            "https://twitter.github.io/finatra/user-guide/index.html",
        ],
    },
    "akka-http-scala": {
        "tags": ["akka http scala", "akka actor streams", "scala reactive http", "akka routing directives"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Akka_(toolkit)",
            "Scala_(programming_language)",
            "Actor_model",
            "Reactive_Streams",
            "Non-blocking_I/O_(Java)",
        ) + [
            "https://doc.akka.io/libraries/akka-http/current/introduction.html",
        ],
    },
    "servant-haskell": {
        "tags": ["servant haskell framework", "type level api haskell", "haskell web api", "servant api combinators"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Haskell",
            "Type_system",
            "Web_API",
            "Representational_state_transfer",
            "Domain-specific_language",
        ) + [
            "https://docs.servant.dev/en/latest/tutorial/index.html",
        ],
    },
    "yesod-haskell": {
        "tags": ["yesod haskell framework", "type safe haskell web", "haskell web framework", "yesod template haskell"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Yesod_(web_framework)",
            "Haskell",
            "Type_safety",
            "Web_framework",
            "Domain-specific_language",
        ) + [
            "https://www.yesodweb.com/book/basics",
        ],
    },
    "scotty-haskell": {
        "tags": ["scotty haskell framework", "haskell sinatra like", "haskell microframework", "warp haskell server"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Haskell",
            "Web_framework",
            "Domain-specific_language",
            "Monad_(functional_programming)",
            "Routing",
        ) + [
            "https://hackage.haskell.org/package/scotty",
        ],
    },
    "actix-actor-model": {
        "tags": ["actix actor system", "rust actor framework", "message passing actors", "actix supervised actors"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Actix",
            "Actor_model",
            "Rust_(programming_language)",
            "Message_passing",
            "Concurrent_computing",
        ) + [
            "https://actix.rs/docs/actix/actor/",
        ],
    },
    "tower-middleware": {
        "tags": ["tower rust middleware", "rust service abstraction", "tower layer stack", "async service trait"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Rust_(programming_language)",
            "Middleware_(distributed_applications)",
            "Async/await",
            "Load_balancing_(computing)",
            "Rate_limiting",
        ) + [
            "https://docs.rs/tower/latest/tower/",
        ],
    },
    "api-gateway-patterns": {
        "tags": ["api gateway pattern", "microservices gateway routing", "reverse proxy aggregation", "gateway request routing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "API_management",
            "Microservices",
            "Reverse_proxy",
            "Load_balancing_(computing)",
            "Rate_limiting",
            "Service-oriented_architecture",
        ),
    },
    "backend-for-frontend": {
        "tags": ["backend for frontend pattern", "bff service layer", "client specific backend", "api aggregation layer"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Microservices",
            "Front_and_back_ends",
            "Service-oriented_architecture",
            "Web_API",
            "Representational_state_transfer",
            "Separation_of_concerns",
        ),
    },
    "saga-orchestration": {
        "tags": ["saga distributed transaction", "compensating transaction pattern", "distributed transaction coordination", "saga choreography orchestration"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Compensating_transaction",
            "Distributed_transaction",
            "Two-phase_commit_protocol",
            "Eventual_consistency",
            "Microservices",
            "Atomicity_(database_systems)",
        ),
    },
    "circuit-breaker-pattern": {
        "tags": ["circuit breaker pattern", "fault tolerance resilience", "cascading failure prevention", "bulkhead isolation pattern"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Circuit_breaker_design_pattern",
            "Fault_tolerance",
            "Graceful_degradation",
            "Timeout_(computing)",
            "Failover",
            "Resilience_(network)",
        ),
    },
}
