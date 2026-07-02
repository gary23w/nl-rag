"""Popular JavaScript/TypeScript libraries and Node.js ecosystem."""

from .common import CC_BY_SA, CC_BY_SA_25, mdn, wiki

DOMAINS = {
    "lodash-utils": {
        "tags": ["lodash utility", "javascript utility library", "functional helpers", "collection iteration"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Lodash",
            "Underscore.js",
            "JavaScript_library",
            "Functional_programming",
        ) + [
            mdn("Web/JavaScript/Reference/Global_Objects/Array"),
            mdn("Web/JavaScript/Reference/Global_Objects/Object"),
            "https://lodash.com/docs/",
            "https://github.com/lodash/lodash",
        ],
    },
    "ramda-functional": {
        "tags": ["ramda functional", "point-free style", "javascript currying", "immutable pipeline"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Functional_programming",
            "Currying",
            "Higher-order_function",
            "Pure_function",
        ) + [
            mdn("Web/JavaScript/Reference/Global_Objects/Array/reduce"),
            "https://ramdajs.com/docs/",
            "https://github.com/ramda/ramda",
        ],
    },
    "axios-http": {
        "tags": ["axios http", "promise http client", "javascript ajax", "request interceptor"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Ajax_(programming)",
            "XMLHttpRequest",
            "Hypertext_Transfer_Protocol",
        ) + [
            mdn("Web/API/XMLHttpRequest"),
            mdn("Web/JavaScript/Reference/Global_Objects/Promise"),
            "https://axios-http.com/docs/intro",
            "https://github.com/axios/axios",
        ],
    },
    "ky-fetch": {
        "tags": ["ky fetch", "fetch wrapper", "javascript http client", "request retry"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Ajax_(programming)",
            "Futures_and_promises",
            "Hypertext_Transfer_Protocol",
        ) + [
            mdn("Web/API/Fetch_API"),
            mdn("Web/API/AbortController"),
            mdn("Web/API/Response"),
            "https://github.com/sindresorhus/ky",
        ],
    },
    "rxjs-observable": {
        "tags": ["rxjs observable", "reactive extensions", "observable stream", "async event pipeline"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Reactive_programming",
            "Reactive_extensions",
            "Observer_pattern",
        ) + [
            mdn("Web/JavaScript/Guide/Iterators_and_generators"),
            mdn("Web/API/Streams_API"),
            "https://rxjs.dev/guide/overview",
            "https://github.com/ReactiveX/rxjs",
        ],
    },
    "zod-schema": {
        "tags": ["zod schema", "typescript validation", "schema inference", "runtime type checking"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Data_validation",
            "Type_system",
            "Static_type_checking",
        ) + [
            mdn("Glossary/Type_conversion"),
            mdn("Web/JavaScript/Data_structures"),
            "https://zod.dev/",
            "https://github.com/colinhacks/zod",
        ],
    },
    "yup-validation": {
        "tags": ["yup validation", "object schema validation", "form schema", "javascript validator"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Data_validation",
            "Database_schema",
            "Type_system",
        ) + [
            mdn("Web/JavaScript/Reference/Global_Objects/Object"),
            mdn("Web/API/FormData"),
            "https://github.com/jquense/yup",
        ],
    },
    "joi-validation": {
        "tags": ["joi validation", "object schema description", "node validator", "input constraint"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Data_validation",
            "JSON_Schema",
            "Database_schema",
        ) + [
            mdn("Web/JavaScript/Reference/Global_Objects/Object"),
            "https://joi.dev/",
            "https://github.com/hapijs/joi",
        ],
    },
    "immer-immutable": {
        "tags": ["immer immutable", "immutable update", "structural sharing", "draft state"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Immutable_object",
            "Persistent_data_structure",
            "Deep_copy",
        ) + [
            mdn("Web/JavaScript/Reference/Global_Objects/Proxy"),
            mdn("Web/API/structuredClone"),
            mdn("Web/JavaScript/Reference/Operators/Spread_syntax"),
            "https://github.com/immerjs/immer",
        ],
    },
    "immutable-js": {
        "tags": ["immutable.js", "persistent collection", "immutable map list", "structural sharing collection"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Persistent_data_structure",
            "Immutable_object",
            "Deep_copy",
        ) + [
            mdn("Web/JavaScript/Reference/Global_Objects/Map"),
            mdn("Web/JavaScript/Reference/Global_Objects/Set"),
            "https://immutable-js.com/",
            "https://github.com/immutable-js/immutable-js",
        ],
    },
    "date-fns-toolkit": {
        "tags": ["date-fns", "date utility functions", "immutable date library", "javascript date formatting"],
        "license": CC_BY_SA,
        "pages": wiki(
            "ISO_8601",
            "Calendar_date",
            "Gregorian_calendar",
        ) + [
            mdn("Web/JavaScript/Reference/Global_Objects/Date"),
            mdn("Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat"),
            "https://github.com/date-fns/date-fns",
        ],
    },
    "dayjs-datetime": {
        "tags": ["dayjs library", "lightweight date library", "moment alternative", "immutable datetime"],
        "license": CC_BY_SA,
        "pages": wiki(
            "ISO_8601",
            "Unix_time",
            "Time_zone",
        ) + [
            mdn("Web/JavaScript/Reference/Global_Objects/Date"),
            mdn("Web/JavaScript/Reference/Global_Objects/Intl"),
            "https://day.js.org/docs/en/installation/installation",
            "https://day.js.org/docs/en/parse/parse",
        ],
    },
    "luxon-datetime": {
        "tags": ["luxon datetime", "immutable datetime", "timezone handling", "duration interval"],
        "license": CC_BY_SA,
        "pages": wiki(
            "ISO_8601",
            "Time_zone",
            "Coordinated_Universal_Time",
        ) + [
            mdn("Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat"),
            mdn("Web/JavaScript/Reference/Global_Objects/Date"),
            "https://github.com/moment/luxon",
        ],
    },
    "moment-legacy": {
        "tags": ["moment.js legacy", "legacy date library", "mutable moment object", "date parsing library"],
        "license": CC_BY_SA,
        "pages": wiki(
            "ISO_8601",
            "Unix_time",
            "Time_zone",
            "Gregorian_calendar",
        ) + [
            mdn("Web/JavaScript/Reference/Global_Objects/Date"),
            mdn("Web/JavaScript/Guide/Using_promises"),
        ],
    },
    "uuid-generation": {
        "tags": ["uuid generation", "universally unique identifier", "rfc 4122 uuid", "random identifier"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Universally_unique_identifier",
            "Random_number_generation",
            "Collision_(computer_science)",
        ) + [
            mdn("Web/API/Crypto/randomUUID"),
            mdn("Web/API/Crypto/getRandomValues"),
            "https://github.com/uuidjs/uuid",
        ],
    },
    "nanoid-ids": {
        "tags": ["nanoid generator", "compact unique id", "url-safe identifier", "collision resistant id"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Random_number_generation",
            "Universally_unique_identifier",
            "Base64",
        ) + [
            mdn("Web/API/Crypto/getRandomValues"),
            mdn("Web/API/SubtleCrypto"),
            "https://github.com/ai/nanoid",
        ],
    },
    "validator-strings": {
        "tags": ["validator.js", "string validation library", "email validator", "sanitize input string"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Data_validation",
            "Email_address",
            "Regular_expression",
        ) + [
            mdn("Web/JavaScript/Reference/Global_Objects/RegExp"),
            mdn("Web/JavaScript/Guide/Regular_expressions"),
            "https://github.com/validatorjs/validator.js",
        ],
    },
    "chalk-terminal": {
        "tags": ["chalk terminal", "terminal string styling", "ansi color output", "cli text color"],
        "license": CC_BY_SA,
        "pages": wiki(
            "ANSI_escape_code",
            "Terminal_emulator",
            "Standard_streams",
            "String_(computer_science)",
        ) + [
            mdn("Web/API/console"),
            mdn("Web/JavaScript/Reference/Global_Objects/String"),
            "https://github.com/chalk/chalk",
        ],
    },
    "commander-cli": {
        "tags": ["commander.js", "cli argument parser", "command line framework", "subcommand definition"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Command-line_interface",
            "Command-line_argument_parsing",
            "Getopt",
        ) + [
            mdn("Web/API/console"),
            mdn("Glossary/Callback_function"),
            "https://github.com/tj/commander.js",
        ],
    },
    "yargs-cli": {
        "tags": ["yargs parser", "cli option parsing", "command builder", "argv parsing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Command-line_interface",
            "Command-line_argument_parsing",
            "Standard_streams",
            "Getopt",
        ) + [
            mdn("Web/JavaScript/Reference/Global_Objects/Object"),
            mdn("Web/JavaScript/Reference/Global_Objects/Array"),
            "https://github.com/yargs/yargs",
        ],
    },
    "inquirer-prompts": {
        "tags": ["inquirer prompts", "interactive cli prompt", "terminal questionnaire", "command line input"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Command-line_interface",
            "Terminal_emulator",
            "Standard_streams",
        ) + [
            mdn("Glossary/Asynchronous"),
            mdn("Web/JavaScript/Reference/Global_Objects/Promise"),
            "https://github.com/SBoudrias/Inquirer.js",
        ],
    },
    "dotenv-config": {
        "tags": ["dotenv config", "environment variable loading", "dotenv file", "twelve-factor config"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Environment_variable",
            "Configuration_file",
            "Twelve-Factor_App_methodology",
            "Modular_programming",
        ) + [
            mdn("Glossary/Type_conversion"),
            mdn("Web/JavaScript/Reference/Global_Objects/JSON"),
            "https://github.com/motdotla/dotenv",
        ],
    },
    "winston-logging": {
        "tags": ["winston logging", "node logging library", "log transport", "structured log level"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Logging_(computing)",
            "Log_file",
            "Syslog",
        ) + [
            mdn("Web/API/console"),
            mdn("Web/JavaScript/Reference/Global_Objects/JSON"),
            "https://github.com/winstonjs/winston",
        ],
    },
    "pino-logging": {
        "tags": ["pino logging", "fast json logger", "low overhead logging", "node structured logs"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Logging_(computing)",
            "Syslog",
            "Serialization",
        ) + [
            mdn("Web/API/console"),
            mdn("Web/JavaScript/Reference/Global_Objects/JSON"),
            "https://github.com/pinojs/pino",
        ],
    },
    "express-middleware": {
        "tags": ["express middleware", "express router", "request handler chain", "node web middleware"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Express.js",
            "Middleware",
            "Representational_state_transfer",
        ) + [
            mdn("Web/HTTP/Methods"),
            mdn("Web/HTTP/Status"),
            "https://expressjs.com/en/guide/using-middleware.html",
            "https://github.com/expressjs/express",
        ],
    },
    "cors-middleware": {
        "tags": ["cors middleware", "cross-origin resource sharing", "preflight request", "same-origin policy"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cross-origin_resource_sharing",
            "Same-origin_policy",
            "HTTP_header",
        ) + [
            mdn("Web/HTTP/CORS"),
            mdn("Web/HTTP/Methods"),
            "https://github.com/expressjs/cors",
        ],
    },
    "helmet-security": {
        "tags": ["helmet security", "http security headers", "content security policy header", "express hardening"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Content_Security_Policy",
            "Cross-site_scripting",
            "HTTP_header",
        ) + [
            mdn("Web/HTTP/CSP"),
            mdn("Web/HTTP/Headers"),
            "https://helmetjs.github.io/",
            "https://github.com/helmetjs/helmet",
        ],
    },
    "passport-auth": {
        "tags": ["passport auth", "authentication strategy", "oauth login flow", "node auth middleware"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Authentication",
            "OAuth",
            "OpenID_Connect",
            "Session_(computer_science)",
        ) + [
            mdn("Web/HTTP/Authentication"),
            mdn("Web/HTTP/Session"),
            "https://www.passportjs.org/concepts/authentication/",
            "https://github.com/jaredhanson/passport",
        ],
    },
    "jsonwebtoken-node": {
        "tags": ["jsonwebtoken node", "json web token signing", "jwt verify", "bearer token claims"],
        "license": CC_BY_SA,
        "pages": wiki(
            "JSON_Web_Token",
            "Authentication",
            "Cryptographic_hash_function",
            "Base64",
        ) + [
            mdn("Web/Security"),
            mdn("Web/HTTP/Authentication"),
            "https://github.com/auth0/node-jsonwebtoken",
        ],
    },
    "bcrypt-hashing": {
        "tags": ["bcrypt hashing", "password hashing library", "salt rounds", "key derivation function"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Bcrypt",
            "Salt_(cryptography)",
            "Key_derivation_function",
            "Password_hashing",
        ) + [
            mdn("Web/API/SubtleCrypto"),
            "https://github.com/kelektiv/node.bcrypt.js",
        ],
    },
    "socket-io-realtime": {
        "tags": ["socket.io realtime", "bidirectional event messaging", "realtime websocket rooms", "event emitter transport"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Socket.IO",
            "Server-sent_events",
            "Publish%E2%80%93subscribe_pattern",
        ) + [
            mdn("Web/API/WebSocket"),
            mdn("Web/API/EventSource"),
            "https://socket.io/docs/v4/",
            "https://github.com/socketio/socket.io",
        ],
    },
    "ws-websocket": {
        "tags": ["ws websocket", "node websocket server", "websocket protocol library", "duplex socket connection"],
        "license": CC_BY_SA,
        "pages": wiki(
            "WebSocket",
            "Full-duplex",
            "Transmission_Control_Protocol",
        ) + [
            mdn("Web/API/WebSockets_API"),
            mdn("Web/API/CloseEvent"),
            "https://github.com/websockets/ws",
        ],
    },
    "node-fetch-http": {
        "tags": ["node-fetch", "fetch api for node", "http request module", "whatwg fetch polyfill"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Ajax_(programming)",
            "Hypertext_Transfer_Protocol",
            "HTTP/2",
        ) + [
            mdn("Web/API/Fetch_API/Using_Fetch"),
            mdn("Web/API/Request"),
            "https://github.com/node-fetch/node-fetch",
        ],
    },
    "undici-client": {
        "tags": ["undici client", "node http client", "connection pooling", "keep-alive dispatcher"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Hypertext_Transfer_Protocol",
            "HTTP/2",
            "Connection_pool",
            "Keep-alive",
        ) + [
            mdn("Web/API/Fetch_API"),
            "https://undici.nodejs.org/",
            "https://github.com/nodejs/undici",
        ],
    },
    "cheerio-parsing": {
        "tags": ["cheerio parsing", "server-side html parsing", "jquery-like dom traversal", "scraping markup selector"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Parsing",
            "Document_Object_Model",
            "Web_scraping",
        ) + [
            mdn("Web/API/DOMParser"),
            mdn("Web/API/Document_Object_Model/Introduction"),
            "https://cheerio.js.org/docs/intro",
            "https://github.com/cheeriojs/cheerio",
        ],
    },
    "puppeteer-automation": {
        "tags": ["puppeteer automation", "headless chrome control", "devtools protocol driver", "browser scripting"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Puppeteer_(software)",
            "Headless_browser",
            "Web_scraping",
        ) + [
            mdn("Glossary/Asynchronous"),
            "https://pptr.dev/",
            "https://github.com/puppeteer/puppeteer",
        ],
    },
    "playwright-automation": {
        "tags": ["playwright automation", "cross-browser automation", "headless browser control", "auto-waiting locator"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Headless_browser",
            "Test_automation",
            "Web_browser",
        ) + [
            mdn("Glossary/Asynchronous"),
            "https://playwright.dev/docs/intro",
            "https://github.com/microsoft/playwright",
        ],
    },
    "sharp-imaging": {
        "tags": ["sharp imaging", "high performance image processing", "image resize pipeline", "libvips binding"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Image_processing",
            "Image_scaling",
            "WebP",
            "Lossy_compression",
        ) + [
            mdn("Web/API/Blob"),
            "https://sharp.pixelplumbing.com/",
            "https://github.com/lovell/sharp",
        ],
    },
    "multer-upload": {
        "tags": ["multer upload", "multipart form data handling", "file upload middleware", "express file parsing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "File_upload",
            "Media_type",
            "Express.js",
        ) + [
            mdn("Web/API/FormData"),
            mdn("Web/API/File"),
            "https://github.com/expressjs/multer",
        ],
    },
    "nodemailer-email": {
        "tags": ["nodemailer email", "send email node", "smtp transport", "mail message composition"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Email",
            "Simple_Mail_Transfer_Protocol",
            "Email_address",
        ) + [
            mdn("Glossary/Asynchronous"),
            mdn("Web/JavaScript/Reference/Global_Objects/Promise"),
            "https://github.com/nodemailer/nodemailer",
        ],
    },
    "bullmq-queue": {
        "tags": ["bullmq queue", "redis job queue", "background job processing", "worker task scheduler"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Message_queue",
            "Job_scheduler",
            "Task_queue",
            "Redis",
        ) + [
            mdn("Glossary/Asynchronous"),
            "https://docs.bullmq.io/",
            "https://github.com/taskforcesh/bullmq",
        ],
    },
    "ioredis-client": {
        "tags": ["ioredis client", "redis node client", "redis cluster connection", "pub/sub command pipeline"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Redis",
            "In-memory_database",
            "Publish%E2%80%93subscribe_pattern",
        ) + [
            mdn("Glossary/Asynchronous"),
            mdn("Web/JavaScript/Reference/Global_Objects/Promise"),
            "https://github.com/redis/ioredis",
        ],
    },
    "mongoose-odm": {
        "tags": ["mongoose odm", "mongodb object modeling", "schema-based document model", "odm population query"],
        "license": CC_BY_SA,
        "pages": wiki(
            "MongoDB",
            "Document-oriented_database",
            "Object_database",
        ) + [
            mdn("Web/JavaScript/Reference/Global_Objects/JSON"),
            "https://mongoosejs.com/docs/guide.html",
            "https://github.com/Automattic/mongoose",
        ],
    },
    "knex-querybuilder": {
        "tags": ["knex query builder", "sql query builder", "database migration tool", "fluent sql interface"],
        "license": CC_BY_SA,
        "pages": wiki(
            "SQL",
            "Query_language",
            "Data_access_layer",
        ) + [
            mdn("Web/JavaScript/Reference/Global_Objects/Promise"),
            "https://knexjs.org/guide/",
            "https://github.com/knex/knex",
        ],
    },
    "prisma-client": {
        "tags": ["prisma client", "type-safe orm", "prisma schema", "database migration engine"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Object-relational_mapping",
            "Data_mapper_pattern",
            "SQL",
        ) + [
            mdn("Web/JavaScript/Reference/Global_Objects/Object"),
            "https://www.prisma.io/docs/orm/overview/introduction/what-is-prisma",
            "https://github.com/prisma/prisma",
        ],
    },
    "drizzle-orm": {
        "tags": ["drizzle orm", "typescript sql orm", "type-safe query builder", "sql-like schema"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Object-relational_mapping",
            "SQL",
            "Type_safety",
        ) + [
            mdn("Web/JavaScript/Reference/Global_Objects/Object"),
            "https://orm.drizzle.team/docs/overview",
            "https://github.com/drizzle-team/drizzle-orm",
        ],
    },
    "graphql-js": {
        "tags": ["graphql.js", "graphql reference implementation", "schema resolver execution", "query type system"],
        "license": CC_BY_SA,
        "pages": wiki(
            "GraphQL",
            "Query_language",
            "API",
        ) + [
            mdn("Web/API/fetch"),
            "https://graphql.org/learn/",
            "https://github.com/graphql/graphql-js",
        ],
    },
    "apollo-client": {
        "tags": ["apollo client", "graphql client cache", "normalized query cache", "react graphql hooks"],
        "license": CC_BY_SA,
        "pages": wiki(
            "GraphQL",
            "Cache_(computing)",
            "Query_language",
        ) + [
            mdn("Web/API/Fetch_API"),
            "https://www.apollographql.com/docs/react/",
            "https://github.com/apollographql/apollo-client",
        ],
    },
    "trpc-typesafe": {
        "tags": ["trpc typesafe", "end-to-end type safety", "typescript rpc", "typed api procedure"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Remote_procedure_call",
            "Type_safety",
            "API",
        ) + [
            mdn("Web/JavaScript/Reference/Global_Objects/Promise"),
            "https://trpc.io/docs/concepts",
            "https://github.com/trpc/trpc",
        ],
    },
    "vitest-testing": {
        "tags": ["vitest testing", "vite-native test runner", "unit test framework", "javascript test assertions"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Unit_testing",
            "Software_testing",
            "Assertion_(software_development)",
            "Mock_object",
        ) + [
            mdn("Glossary/Callback_function"),
            "https://vitest.dev/guide/",
        ],
    },
    "cypress-e2e": {
        "tags": ["cypress e2e", "end-to-end browser testing", "cypress test runner", "in-browser assertion"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cypress_(software)",
            "Test_automation",
            "End-to-end_principle",
        ) + [
            mdn("Glossary/Asynchronous"),
            "https://docs.cypress.io/app/get-started/why-cypress",
            "https://github.com/cypress-io/cypress",
        ],
    },
    "storybook-ui": {
        "tags": ["storybook ui", "component workshop", "isolated component development", "ui component catalog"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Component-based_software_engineering",
            "User_interface_design",
            "Graphical_user_interface",
        ) + [
            mdn("Web/API/Web_components"),
            "https://storybook.js.org/docs/get-started/why-storybook",
            "https://github.com/storybookjs/storybook",
        ],
    },
    "tanstack-table": {
        "tags": ["tanstack table", "headless table library", "data grid state", "sorting pagination model"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Table_(information)",
            "Pagination",
            "Component-based_software_engineering",
        ) + [
            mdn("Web/API/HTMLTableElement"),
            mdn("Web/JavaScript/Reference/Global_Objects/Array"),
            "https://tanstack.com/table/latest/docs/introduction",
            "https://github.com/TanStack/table",
        ],
    },
    "framer-motion": {
        "tags": ["framer motion", "react animation library", "declarative motion", "spring gesture animation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Animation",
            "Motion_graphics",
            "Interpolation",
        ) + [
            mdn("Web/API/Web_Animations_API"),
            mdn("Web/CSS/transform"),
            "https://motion.dev/docs",
            "https://github.com/framer/motion",
        ],
    },
}
