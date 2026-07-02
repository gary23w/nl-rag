---
title: "GitHub"
source: https://github.com/winstonjs/winston
domain: winston-logging
license: CC-BY-SA-4.0
tags: winston logging, node logging library, log transport, structured log level
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

winstonjs

/

winston

Public

- Notifications You must be signed in to change notification settings
- Fork 1.8k
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History1,652 Commits1,652 Commits |   |   |   |
| .github | .github |   |   |
| docs | docs |   |   |
| examples | examples |   |   |
| lib | lib |   |   |
| test | test |   |   |
| .babelrc | .babelrc |   |   |
| .editorconfig | .editorconfig |   |   |
| .eslintrc | .eslintrc |   |   |
| .gitattributes | .gitattributes |   |   |
| .gitignore | .gitignore |   |   |
| .npmignore | .npmignore |   |   |
| .prettierrc | .prettierrc |   |   |
| CHANGELOG.md | CHANGELOG.md |   |   |
| CODE_OF_CONDUCT.md | CODE_OF_CONDUCT.md |   |   |
| CONTRIBUTING.md | CONTRIBUTING.md |   |   |
| LICENSE | LICENSE |   |   |
| README.md | README.md |   |   |
| SECURITY.md | SECURITY.md |   |   |
| UPGRADE-3.0.md | UPGRADE-3.0.md |   |   |
| eslint.config.cjs | eslint.config.cjs |   |   |
| index.d.ts | index.d.ts |   |   |
| jest.config.js | jest.config.js |   |   |
| package-lock.json | package-lock.json |   |   |
| package.json | package.json |   |   |
| publishing.md | publishing.md |   |   |
| tsconfig.json | tsconfig.json |   |   |
|   |   |   |   |

## Repository files navigation

# winston

A logger for just about everything.

(Version npm) (npm Downloads) (build status) (coverage status)

(NPM)

## winston@3

See the Upgrade Guide for more information. Bug reports and PRs welcome!

## Looking for `winston@2.x` documentation?

Please note that the documentation below is for `winston@3`. Read the `winston@2.x` documentation.

## Motivation

`winston` is designed to be a simple and universal logging library with support for multiple transports. A transport is essentially a storage device for your logs. Each `winston` logger can have multiple transports (see: Transports) configured at different levels (see: Logging levels). For example, one may want error logs to be stored in a persistent remote location (like a database), but all logs output to the console or a local file.

`winston` aims to decouple parts of the logging process to make it more flexible and extensible. Attention is given to supporting flexibility in log formatting (see: Formats) & levels (see: Using custom logging levels), and ensuring those APIs decoupled from the implementation of transport logging (i.e. how the logs are stored / indexed, see: Adding Custom Transports) to the API that they exposed to the programmer.

## Quick Start

TL;DR? Check out the quick start example in `./examples/`. There are a number of other examples in `./examples/*.js`. Don't see an example you think should be there? Submit a pull request to add it!

## Usage

The recommended way to use `winston` is to create your own logger. The simplest way to do this is using `winston.createLogger`:

```highlight
const winston = require('winston');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  defaultMeta: { service: 'user-service' },
  transports: [
    //
    // - Write all logs with importance level of `error` or higher to `error.log`
    //   (i.e., error, fatal, but not other levels)
    //
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    //
    // - Write all logs with importance level of `info` or higher to `combined.log`
    //   (i.e., fatal, error, warn, and info, but not trace)
    //
    new winston.transports.File({ filename: 'combined.log' }),
  ],
});

//
// If we're not in production then log to the `console` with the format:
// `${info.level}: ${info.message} JSON.stringify({ ...rest }) `
//
if (process.env.NODE_ENV !== 'production') {
  logger.add(new winston.transports.Console({
    format: winston.format.simple(),
  }));
}
```

You may also log directly via the default logger exposed by `require('winston')`, but this merely intended to be a convenient shared logger to use throughout your application if you so choose. Note that the default logger doesn't have any transports by default. You need add transports by yourself, and leaving the default logger without any transports may produce a high memory usage issue.

## Table of contents

- Motivation
- Quick Start
- Usage
- Table of Contents
- Logging
  - Creating your logger
  - Streams, `objectMode`, and `info` objects
- Formats
  - Combining formats
  - String interpolation
  - Filtering `info` Objects
  - Creating custom formats
- Logging levels
  - Using logging levels
  - Using custom logging levels
- Transports
  - Multiple transports of the same type
  - Adding Custom Transports
  - Common Transport options
- Exceptions
  - Handling Uncaught Exceptions with winston
  - To Exit or Not to Exit
- Rejections
  - Handling Uncaught Promise Rejections with winston
- Profiling
- Streaming Logs
- Querying Logs
- Further Reading
  - Using the default logger
  - Awaiting logs to be written in `winston`
  - Working with multiple Loggers in `winston`
  - Routing Console transport messages to the console instead of stdout and stderr
- Installation
- Run Tests

## Logging

Logging levels in `winston` conform to the severity ordering specified by RFC5424: *severity of all levels is assumed to be numerically **ascending** from most important to least important.*

```highlight
const levels = {
  error: 0,
  warn: 1,
  info: 2,
  http: 3,
  verbose: 4,
  debug: 5,
  silly: 6
};
```

### Creating your own Logger

You get started by creating a logger using `winston.createLogger`:

```highlight
const logger = winston.createLogger({
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'combined.log' })
  ]
});
```

A logger accepts the following parameters:

| Name | Default | Description |
|---|---|---|
| `level` | `'info'` | Log only if `info.level` is less than or equal to this level |
| `levels` | `winston.config.npm.levels` | Levels (and colors) representing log priorities |
| `format` | `winston.format.json` | Formatting for `info` messages (see: Formats) |
| `transports` | `[]` *(No transports)* | Set of logging targets for `info` messages |
| `exitOnError` | `true` | If false, handled exceptions will not cause `process.exit` |
| `silent` | `false` | If true, all logs are suppressed |

The levels provided to `createLogger` will be defined as convenience methods on the `logger` returned.

```highlight
//
// Logging
//
logger.log({
  level: 'info',
  message: 'Hello distributed log files!'
});

logger.info('Hello again distributed logs');
```

You can add or remove transports from the `logger` once it has been provided to you from `winston.createLogger`:

```highlight
const files = new winston.transports.File({ filename: 'combined.log' });
const console = new winston.transports.Console();

logger
  .clear()          // Remove all transports
  .add(console)     // Add console transport
  .add(files)       // Add file transport
  .remove(console); // Remove console transport
```

You can also wholesale reconfigure a `winston.Logger` instance using the `configure` method:

```highlight
const logger = winston.createLogger({
  level: 'info',
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'combined.log' })
  ]
});

//
// Replaces the previous transports with those in the
// new configuration wholesale.
//
const DailyRotateFile = require('winston-daily-rotate-file');
logger.configure({
  level: 'verbose',
  transports: [
    new DailyRotateFile(opts)
  ]
});
```

### Creating child loggers

You can create child loggers from existing loggers to pass metadata overrides:

```highlight
const logger = winston.createLogger({
  transports: [
    new winston.transports.Console(),
  ]
});

const childLogger = logger.child({ requestId: '451' });
```

> `.child` is likely to be bugged if you're also extending the `Logger` class, due to some implementation details that make `this` keyword to point to unexpected things. Use with caution.

### Streams, `objectMode`, and `info` objects

In `winston`, both `Logger` and `Transport` instances are treated as `objectMode` streams that accept an `info` object.

The `info` parameter provided to a given format represents a single log message. The object itself is mutable. Every `info` must have at least the `level` and `message` properties:

```highlight
const info = {
  level: 'info',                 // Level of the logging message
  message: 'Hey! Log something?' // Descriptive message being logged.
};
```

Properties **besides level and message** are considered as "`meta`". i.e.:

```highlight
const { level, message, ...meta } = info;
```

Several of the formats in `logform` itself add additional properties:

| Property | Format added by | Description |
|---|---|---|
| `splat` | `splat()` | String interpolation splat for `%d %s`-style messages. |
| `timestamp` | `timestamp()` | timestamp the message was received. |
| `label` | `label()` | Custom label associated with each message. |
| `ms` | `ms()` | Number of milliseconds since the previous log message. |

As a consumer you may add whatever properties you wish – *internal state is maintained by `Symbol` properties:*

- `Symbol.for('level')` ***(READ-ONLY)**:* equal to `level` property. **Is treated as immutable by all code.**
- `Symbol.for('message'):` complete string message set by "finalizing formats":
  - `json`
  - `logstash`
  - `printf`
  - `prettyPrint`
  - `simple`
- `Symbol.for('splat')`: additional string interpolation arguments. *Used exclusively by `splat()` format.*

These Symbols are stored in another package: `triple-beam` so that all consumers of `logform` can have the same Symbol reference. i.e.:

```highlight
const { LEVEL, MESSAGE, SPLAT } = require('triple-beam');

console.log(LEVEL === Symbol.for('level'));
// true

console.log(MESSAGE === Symbol.for('message'));
// true

console.log(SPLAT === Symbol.for('splat'));
// true
```

> **NOTE:** any `{ message }` property in a `meta` object provided will automatically be concatenated to any `msg` already provided: For example the below will concatenate 'world' onto 'hello':
> 
> ```highlight
> logger.log('error', 'hello', { message: 'world' });
> logger.info('hello', { message: 'world' });
> ```

## Formats

Formats in `winston` can be accessed from `winston.format`. They are implemented in `logform`, a separate module from `winston`. This allows flexibility when writing your own transports in case you wish to include a default format with your transport.

In modern versions of `node` template strings are very performant and are the recommended way for doing most end-user formatting. If you want to bespoke format your logs, `winston.format.printf` is for you:

```highlight
const { createLogger, format, transports } = require('winston');
const { combine, timestamp, label, printf } = format;

const myFormat = printf(({ level, message, label, timestamp }) => {
  return `${timestamp} [${label}] ${level}: ${message}`;
});

const logger = createLogger({
  format: combine(
    label({ label: 'right meow!' }),
    timestamp(),
    myFormat
  ),
  transports: [new transports.Console()]
});
```

To see what built-in formats are available and learn more about creating your own custom logging formats, see `logform`.

### Combining formats

Any number of formats may be combined into a single format using `format.combine`. Since `format.combine` takes no `opts`, as a convenience it returns pre-created instance of the combined format.

```highlight
const { createLogger, format, transports } = require('winston');
const { combine, timestamp, label, prettyPrint } = format;

const logger = createLogger({
  format: combine(
    label({ label: 'right meow!' }),
    timestamp(),
    prettyPrint()
  ),
  transports: [new transports.Console()]
})

logger.log({
  level: 'info',
  message: 'What time is the testing at?'
});
// Outputs:
// { level: 'info',
//   message: 'What time is the testing at?',
//   label: 'right meow!',
//   timestamp: '2017-09-30T03:57:26.875Z' }
```

### String interpolation

The `log` method provides the string interpolation using util.format. **It must be enabled using `format.splat()`.**

Below is an example that defines a format with string interpolation of messages using `format.splat` and then serializes the entire `info` message using `format.simple`.

```highlight
const { createLogger, format, transports } = require('winston');
const logger = createLogger({
  format: format.combine(
    format.splat(),
    format.simple()
  ),
  transports: [new transports.Console()]
});

// info: test message my string {}
logger.log('info', 'test message %s', 'my string');

// info: test message 123 {}
logger.log('info', 'test message %d', 123);

// info: test message first second {number: 123}
logger.log('info', 'test message %s, %s', 'first', 'second', { number: 123 });
```

### Filtering `info` Objects

If you wish to filter out a given `info` Object completely when logging then simply return a falsey value.

```highlight
const { createLogger, format, transports } = require('winston');

// Ignore log messages if they have { private: true }
const ignorePrivate = format((info, opts) => {
  if (info.private) { return false; }
  return info;
});

const logger = createLogger({
  format: format.combine(
    ignorePrivate(),
    format.json()
  ),
  transports: [new transports.Console()]
});

// Outputs: {"level":"error","message":"Public error to share"}
logger.log({
  level: 'error',
  message: 'Public error to share'
});

// Messages with { private: true } will not be written when logged.
logger.log({
  private: true,
  level: 'error',
  message: 'This is super secret - hide it.'
});
```

Use of `format.combine` will respect any falsey values return and stop evaluation of later formats in the series. For example:

```highlight
const { format } = require('winston');
const { combine, timestamp, label } = format;

const willNeverThrow = format.combine(
  format(info => { return false })(), // Ignores everything
  format(info => { throw new Error('Never reached') })()
);
```

### Creating custom formats

Formats are prototypal objects (i.e. class instances) that define a single method: `transform(info, opts)` and return the mutated `info`:

- `info`: an object representing the log message.
- `opts`: setting specific to the current instance of the format.

They are expected to return one of two things:

- **An `info` Object** representing the modified `info` argument. Object references need not be preserved if immutability is preferred. All current built-in formats consider `info` mutable, but [immutablejs] is being considered for future releases.
- **A falsey value** indicating that the `info` argument should be ignored by the caller. (See: Filtering `info` Objects) below.

`winston.format` is designed to be as simple as possible. To define a new format, simply pass it a `transform(info, opts)` function to get a new `Format`.

The named `Format` returned can be used to create as many copies of the given `Format` as desired:

```highlight
const { format } = require('winston');

const volume = format((info, opts) => {
  if (opts.yell) {
    info.message = info.message.toUpperCase();
  } else if (opts.whisper) {
    info.message = info.message.toLowerCase();
  }

  return info;
});

// `volume` is now a function that returns instances of the format.
const scream = volume({ yell: true });
console.dir(scream.transform({
  level: 'info',
  message: `sorry for making you YELL in your head!`
}, scream.options));
// {
//   level: 'info'
//   message: 'SORRY FOR MAKING YOU YELL IN YOUR HEAD!'
// }

// `volume` can be used multiple times to create different formats.
const whisper = volume({ whisper: true });
console.dir(whisper.transform({
  level: 'info',
  message: `WHY ARE THEY MAKING US YELL SO MUCH!`
}, whisper.options));
// {
//   level: 'info'
//   message: 'why are they making us yell so much!'
// }
```

## Logging Levels

Logging levels in `winston` conform to the severity ordering specified by RFC5424: *severity of all levels is assumed to be numerically **ascending** from most important to least important.*

Each `level` is given a specific integer priority. The higher the priority the more important the message is considered to be, and the lower the corresponding integer priority. For example, as specified exactly in RFC5424 the `syslog` levels are prioritized from 0 to 7 (highest to lowest).

```highlight
{
  emerg: 0,
  alert: 1,
  crit: 2,
  error: 3,
  warning: 4,
  notice: 5,
  info: 6,
  debug: 7
}
```

Similarly, `npm` logging levels are prioritized from 0 to 6 (highest to lowest):

```highlight
{
  error: 0,
  warn: 1,
  info: 2,
  http: 3,
  verbose: 4,
  debug: 5,
  silly: 6
}
```

If you do not explicitly define the levels that `winston` should use, the `npm` levels above will be used.

### Using Logging Levels

Setting the level for your logging message can be accomplished in one of two ways. You can pass a string representing the logging level to the log() method or use the level specified methods defined on every winston Logger.

```highlight
//
// Any logger instance
//
logger.log('silly', "127.0.0.1 - there's no place like home");
logger.log('debug', "127.0.0.1 - there's no place like home");
logger.log('verbose', "127.0.0.1 - there's no place like home");
logger.log('info', "127.0.0.1 - there's no place like home");
logger.log('warn', "127.0.0.1 - there's no place like home");
logger.log('error', "127.0.0.1 - there's no place like home");
logger.info("127.0.0.1 - there's no place like home");
logger.warn("127.0.0.1 - there's no place like home");
logger.error("127.0.0.1 - there's no place like home");

//
// Default logger
//
winston.log('info', "127.0.0.1 - there's no place like home");
winston.info("127.0.0.1 - there's no place like home");
```

`winston` allows you to define a `level` property on each transport which specifies the **maximum** level of messages that a transport should log. For example, using the `syslog` levels you could log only `error` messages to the console and everything `info` and below to a file (which includes `error` messages):

```highlight
const logger = winston.createLogger({
  levels: winston.config.syslog.levels,
  transports: [
    new winston.transports.Console({ level: 'error' }),
    new winston.transports.File({
      filename: 'combined.log',
      level: 'info'
    })
  ]
});
```

You may also dynamically change the log level of a transport:

```highlight
const transports = {
  console: new winston.transports.Console({ level: 'warn' }),
  file: new winston.transports.File({ filename: 'combined.log', level: 'error' })
};

const logger = winston.createLogger({
  transports: [
    transports.console,
    transports.file
  ]
});

logger.info('Will not be logged in either transport!');
transports.console.level = 'info';
transports.file.level = 'info';
logger.info('Will be logged in both transports!');
```

`winston` supports customizable logging levels, defaulting to npm style logging levels. Levels must be specified at the time of creating your logger.

### Using Custom Logging Levels

In addition to the predefined `npm`, `syslog`, and `cli` levels available in `winston`, you can also choose to define your own:

```highlight
const myCustomLevels = {
  levels: {
    foo: 0,
    bar: 1,
    baz: 2,
    foobar: 3
  },
  colors: {
    foo: 'blue',
    bar: 'green',
    baz: 'yellow',
    foobar: 'red'
  }
};

const customLevelLogger = winston.createLogger({
  levels: myCustomLevels.levels
});

customLevelLogger.foobar('some foobar level-ed message');
```

Although there is slight repetition in this data structure, it enables simple encapsulation if you do not want to have colors. If you do wish to have colors, in addition to passing the levels to the Logger itself, you must make winston aware of them:

```highlight
winston.addColors(myCustomLevels.colors);
```

This enables loggers using the `colorize` formatter to appropriately color and style the output of custom levels.

Additionally, you can also change background color and font style. For example,

```highlight
baz: 'italic yellow',
foobar: 'bold red cyanBG'
```

Possible options are below.

- Font styles: `bold`, `dim`, `italic`, `underline`, `inverse`, `hidden`, `strikethrough`.
- Font foreground colors: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `gray`, `grey`.
- Background colors: `blackBG`, `redBG`, `greenBG`, `yellowBG`, `blueBG` `magentaBG`, `cyanBG`, `whiteBG`

### Colorizing Standard logging levels

To colorize the standard logging level add

```highlight
winston.format.combine(
  winston.format.colorize(),
  winston.format.simple()
);
```

where `winston.format.simple()` is whatever other formatter you want to use. The `colorize` formatter must come before any formatters adding text you wish to color.

### Colorizing full log line when json formatting logs

To colorize the full log line with the json formatter you can apply the following

```highlight
winston.format.combine(
  winston.format.json(),
  winston.format.colorize({ all: true })
);
```

## Transports

There are several core transports included in `winston`, which leverage the built-in networking and file I/O offered by Node.js core. In addition, there are additional transports written by members of the community.

## Multiple transports of the same type

It is possible to use multiple transports of the same type e.g. `winston.transports.File` when you construct the transport.

```highlight
const logger = winston.createLogger({
  transports: [
    new winston.transports.File({
      filename: 'combined.log',
      level: 'info'
    }),
    new winston.transports.File({
      filename: 'errors.log',
      level: 'error'
    })
  ]
});
```

If you later want to remove one of these transports you can do so by using the transport itself. e.g.:

```highlight
const combinedLogs = logger.transports.find(transport => {
  return transport.filename === 'combined.log'
});

logger.remove(combinedLogs);
```

## Adding Custom Transports

Adding a custom transport is easy. All you need to do is accept any options you need, implement a log() method, and consume it with `winston`.

```highlight
const Transport = require('winston-transport');
const util = require('util');

//
// Inherit from `winston-transport` so you can take advantage
// of the base functionality and `.exceptions.handle()`.
//
module.exports = class YourCustomTransport extends Transport {
  constructor(opts) {
    super(opts);
    //
    // Consume any custom options here. e.g.:
    // - Connection information for databases
    // - Authentication information for APIs (e.g. loggly, papertrail,
    //   logentries, etc.).
    //
  }

  log(info, callback) {
    setImmediate(() => {
      this.emit('logged', info);
    });

    // Perform the writing to the remote service
    callback();
  }
};
```

## Common Transport options

As every transport inherits from winston-transport, it's possible to set a custom format and a custom log level on each transport separately:

```highlight
const logger = winston.createLogger({
  transports: [
    new winston.transports.File({
      filename: 'error.log',
      level: 'error',
      format: winston.format.json()
    }),
    new winston.transports.Http({
      level: 'warn',
      format: winston.format.json()
    }),
    new winston.transports.Console({
      level: 'info',
      format: winston.format.combine(
        winston.format.colorize(),
        winston.format.simple()
      )
    })
  ]
});
```

## Exceptions

### Handling Uncaught Exceptions with winston

With `winston`, it is possible to catch and log `uncaughtException` events from your process. With your own logger instance you can enable this behavior when it's created or later on in your applications lifecycle:

```highlight
const { createLogger, transports } = require('winston');

// Enable exception handling when you create your logger.
const logger = createLogger({
  transports: [
    new transports.File({ filename: 'combined.log' })
  ],
  exceptionHandlers: [
    new transports.File({ filename: 'exceptions.log' })
  ]
});

// Or enable it later on by adding a transport or using `.exceptions.handle`
const logger = createLogger({
  transports: [
    new transports.File({ filename: 'combined.log' })
  ]
});

// Call exceptions.handle with a transport to handle exceptions
logger.exceptions.handle(
  new transports.File({ filename: 'exceptions.log' })
);
```

If you want to use this feature with the default logger, simply call `.exceptions.handle()` with a transport instance.

```highlight
//
// You can add a separate exception logger by passing it to `.exceptions.handle`
//
winston.exceptions.handle(
  new winston.transports.File({ filename: 'path/to/exceptions.log' })
);

//
// Alternatively you can set `handleExceptions` to true when adding transports
// to winston.
//
winston.add(new winston.transports.File({
  filename: 'path/to/combined.log',
  handleExceptions: true
}));
```

### To Exit or Not to Exit

By default, winston will exit after logging an uncaughtException. If this is not the behavior you want, set `exitOnError = false`

```highlight
const logger = winston.createLogger({ exitOnError: false });

//
// or, like this:
//
logger.exitOnError = false;
```

When working with custom logger instances, you can pass in separate transports to the `exceptionHandlers` property or set `handleExceptions` on any transport.

##### Example 1

```highlight
const logger = winston.createLogger({
  transports: [
    new winston.transports.File({ filename: 'path/to/combined.log' })
  ],
  exceptionHandlers: [
    new winston.transports.File({ filename: 'path/to/exceptions.log' })
  ]
});
```

##### Example 2

```highlight
const logger = winston.createLogger({
  transports: [
    new winston.transports.Console({
      handleExceptions: true
    })
  ],
  exitOnError: false
});
```

The `exitOnError` option can also be a function to prevent exit on only certain types of errors:

```highlight
function ignoreEpipe(err) {
  return err.code !== 'EPIPE';
}

const logger = winston.createLogger({ exitOnError: ignoreEpipe });

//
// or, like this:
//
logger.exitOnError = ignoreEpipe;
```

## Rejections

### Handling Uncaught Promise Rejections with winston

With `winston`, it is possible to catch and log `unhandledRejection` events from your process. With your own logger instance you can enable this behavior when it's created or later on in your applications lifecycle:

```highlight
const { createLogger, transports } = require('winston');

// Enable rejection handling when you create your logger.
const logger = createLogger({
  transports: [
    new transports.File({ filename: 'combined.log' })
  ],
  rejectionHandlers: [
    new transports.File({ filename: 'rejections.log' })
  ]
});

// Or enable it later on by adding a transport or using `.rejections.handle`
const logger = createLogger({
  transports: [
    new transports.File({ filename: 'combined.log' })
  ]
});

// Call rejections.handle with a transport to handle rejections
logger.rejections.handle(
  new transports.File({ filename: 'rejections.log' })
);
```

If you want to use this feature with the default logger, simply call `.rejections.handle()` with a transport instance.

```highlight
//
// You can add a separate rejection logger by passing it to `.rejections.handle`
//
winston.rejections.handle(
  new winston.transports.File({ filename: 'path/to/rejections.log' })
);

//
// Alternatively you can set `handleRejections` to true when adding transports
// to winston.
//
winston.add(new winston.transports.File({
  filename: 'path/to/combined.log',
  handleRejections: true
}));
```

## Profiling

In addition to logging messages and metadata, `winston` also has a simple profiling mechanism implemented for any logger:

```highlight
//
// Start profile of 'test'
//
logger.profile('test');

setTimeout(function () {
  //
  // Stop profile of 'test'. Logging will now take place:
  //   '17 Jan 21:00:00 - info: test duration=1000ms'
  //
  logger.profile('test');
}, 1000);
```

Also you can start a timer and keep a reference that you can call `.done()` on:

```highlight
 // Returns an object corresponding to a specific timing. When done
 // is called the timer will finish and log the duration. e.g.:
 //
 const profiler = logger.startTimer();
 setTimeout(function () {
   profiler.done({ message: 'Logging message' });
 }, 1000);
```

All profile messages are set to 'info' level by default, and both message and metadata are optional. For individual profile messages, you can override the default log level by supplying a metadata object with a `level` property:

```highlight
logger.profile('test', { level: 'debug' });
```

## Querying Logs

`winston` supports querying of logs with Loggly-like options. See Loggly Search API. Specifically: `File`, `Couchdb`, `Redis`, `Loggly`, `Nssocket`, and `Http`.

```highlight
const options = {
  from: new Date() - (24 * 60 * 60 * 1000),
  until: new Date(),
  limit: 10,
  start: 0,
  order: 'desc',
  fields: ['message']
};

//
// Find items logged between today and yesterday.
//
logger.query(options, function (err, results) {
  if (err) {
    /* TODO: handle me */
    throw err;
  }

  console.log(results);
});
```

## Streaming Logs

Streaming allows you to stream your logs back from your chosen transport.

```highlight
//
// Start at the end.
//
winston.stream({ start: -1 }).on('log', function(log) {
  console.log(log);
});
```
