---
title: "GitHub (part 1/2)"
source: https://github.com/redis/ioredis
domain: ioredis-client
license: CC-BY-SA-4.0
tags: ioredis client, redis node client, redis cluster connection, pub/sub command pipeline
fetched: 2026-07-02
part: 1/2
---

### Uh oh!

There was an error while loading. Please reload this page.

redis

/

ioredis

Public

- Notifications You must be signed in to change notification settings
- Fork 1.2k
- Star

Branches

Tags

Open more actions menu


## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History1,394 Commits1,394 Commits |   |   |   |
| .agents/skills | .agents/skills |   |   |
| .claude | .claude |   |   |
| .github | .github |   |   |
| benchmarks | benchmarks |   |   |
| bin | bin |   |   |
| docs | docs |   |   |
| examples | examples |   |   |
| lib | lib |   |   |
| resources | resources |   |   |
| test | test |   |   |
| .eslintrc.json | .eslintrc.json |   |   |
| .gitignore | .gitignore |   |   |
| .prettierignore | .prettierignore |   |   |
| .releaserc.json | .releaserc.json |   |   |
| AGENTS.md | AGENTS.md |   |   |
| CHANGELOG.md | CHANGELOG.md |   |   |
| CLAUDE.md | CLAUDE.md |   |   |
| CODE_OF_CONDUCT.md | CODE_OF_CONDUCT.md |   |   |
| LICENSE | LICENSE |   |   |
| README.md | README.md |   |   |
| logo.svg | logo.svg |   |   |
| package-lock.json | package-lock.json |   |   |
| package.json | package.json |   |   |
| tsconfig.json | tsconfig.json |   |   |
|   |   |   |   |


## Repository files navigation

(ioredis)

(Build Status) (Coverage Status) (Commitizen friendly) (semantic-release)

(Discord) (Twitch) (YouTube) (Twitter)

A robust, performance-focused and full-featured Redis client for Node.js.

Supports Redis >= 2.6.12. Completely compatible with Redis 7.x.

ioredis is a stable project and maintenance is done on a best-effort basis for relevant issues (contributions to ioredis will still be evaluated, reviewed, and merged when they benefit the project). For new projects, node-redis is the recommended client library. node-redis is the open-source (MIT license) Redis JavaScript client library redesigned from the ground up and actively maintained. node-redis supports new (hash-field expiration) and future commands and the capabilities available in Redis Stack and Redis 8 (search, JSON, time-series, probabilistic data structures).

# Features

ioredis is a robust, full-featured Redis client that is used in the world's biggest online commerce company Alibaba and many other awesome companies.

1. Full-featured. It supports Cluster, Sentinel, Streams, Pipelining, and of course Lua scripting, Redis Functions, Pub/Sub (with the support of binary messages).
2. High performance 🚀.
3. Delightful API 😄. It works with Node callbacks and Native promises.
4. Transformation of command arguments and replies.
5. Transparent key prefixing.
6. Abstraction for Lua scripting, allowing you to define custom commands.
7. Supports binary data.
8. Supports TLS 🔒.
9. Supports offline queue and ready checking.
10. Supports ES6 types, such as `Map` and `Set`.
11. Supports GEO commands 📍.
12. Supports Redis ACL.
13. Sophisticated error handling strategy.
14. Supports NAT mapping.
15. Supports autopipelining.

**100% written in TypeScript and official declarations are provided:**

(TypeScript Screenshot)

# Versions

| Version | Branch | Node.js Version | Redis Version |
|---|---|---|---|
| 5.x.x (latest) | main | >= 12 | 2.6.12 ~ latest |
| 4.x.x | v4 | >= 8 | 2.6.12 ~ 7 |

Refer to CHANGELOG.md for features and bug fixes introduced in v5.

🚀 Upgrading from v4 to v5

# Links

- API Documentation (Redis, Cluster)
- Changelog

# Quick Start


## Install

```highlight
npm install ioredis
```

In a TypeScript project, you may want to add TypeScript declarations for Node.js:

```highlight
npm install --save-dev @types/node
```


## Basic Usage

```highlight
// Import ioredis.
// You can also use `import { Redis } from "ioredis"`
// if your project is a TypeScript project,
// Note that `import Redis from "ioredis"` is still supported,
// but will be deprecated in the next major version.
const Redis = require("ioredis");

// Create a Redis instance.
// By default, it will connect to localhost:6379.
// We are going to cover how to specify connection options soon.
const redis = new Redis();

redis.set("mykey", "value"); // Returns a promise which resolves to "OK" when the command succeeds.

// ioredis supports the node.js callback style
redis.get("mykey", (err, result) => {
  if (err) {
    console.error(err);
  } else {
    console.log(result); // Prints "value"
  }
});

// Or ioredis returns a promise if the last argument isn't a function
redis.get("mykey").then((result) => {
  console.log(result); // Prints "value"
});

redis.zadd("sortedSet", 1, "one", 2, "dos", 4, "quatro", 3, "three");
redis.zrange("sortedSet", 0, 2, "WITHSCORES").then((elements) => {
  // ["one", "1", "dos", "2", "three", "3"] as if the command was `redis> ZRANGE sortedSet 0 2 WITHSCORES`
  console.log(elements);
});

// All arguments are passed directly to the redis server,
// so technically ioredis supports all Redis commands.
// The format is: redis[SOME_REDIS_COMMAND_IN_LOWERCASE](ARGUMENTS_ARE_JOINED_INTO_COMMAND_STRING)
// so the following statement is equivalent to the CLI: `redis> SET mykey hello EX 10`
redis.set("mykey", "hello", "EX", 10);
```

See the `examples/` folder for more examples. For example:

- TTL
- Strings
- Hashes
- Lists
- Sets
- Sorted Sets
- Streams
- Redis Modules e.g. RedisJSON

All Redis commands are supported. See the documentation for details.


## Connect to Redis

When a new `Redis` instance is created, a connection to Redis will be created at the same time. You can specify which Redis to connect to by:

```highlight
new Redis(); // Connect to 127.0.0.1:6379
new Redis(6380); // 127.0.0.1:6380
new Redis(6379, "192.168.1.1"); // 192.168.1.1:6379
new Redis("/tmp/redis.sock");
new Redis({
  port: 6379, // Redis port
  host: "127.0.0.1", // Redis host
  username: "default", // needs Redis >= 6
  password: "my-top-secret",
  db: 0, // Defaults to 0
});
```

You can also specify connection options as a `redis://` URL or `rediss://` URL when using TLS encryption:

```highlight
// Connect to 127.0.0.1:6380, db 4, using password "authpassword":
new Redis("redis://:authpassword@127.0.0.1:6380/4");

// Username can also be passed via URI.
new Redis("redis://username:authpassword@127.0.0.1:6380/4");
```

See API Documentation for all available options.


## Pub/Sub

Redis provides several commands for developers to implement the Publish–subscribe pattern. There are two roles in this pattern: publisher and subscriber. Publishers are not programmed to send their messages to specific subscribers. Rather, published messages are characterized into channels, without knowledge of what (if any) subscribers there may be.

By leveraging Node.js's built-in events module, ioredis makes pub/sub very straightforward to use. Below is a simple example that consists of two files, one is publisher.js that publishes messages to a channel, the other is subscriber.js that listens for messages on specific channels.

```highlight
// publisher.js

const Redis = require("ioredis");
const redis = new Redis();

setInterval(() => {
  const message = { foo: Math.random() };
  // Publish to my-channel-1 or my-channel-2 randomly.
  const channel = `my-channel-${1 + Math.round(Math.random())}`;

  // Message can be either a string or a buffer
  redis.publish(channel, JSON.stringify(message));
  console.log("Published %s to %s", message, channel);
}, 1000);
```

```highlight
// subscriber.js

const Redis = require("ioredis");
const redis = new Redis();

redis.subscribe("my-channel-1", "my-channel-2", (err, count) => {
  if (err) {
    // Just like other commands, subscribe() can fail for some reasons,
    // ex network issues.
    console.error("Failed to subscribe: %s", err.message);
  } else {
    // `count` represents the number of channels this client are currently subscribed to.
    console.log(
      `Subscribed successfully! This client is currently subscribed to ${count} channels.`
    );
  }
});

redis.on("message", (channel, message) => {
  console.log(`Received ${message} from ${channel}`);
});

// There's also an event called 'messageBuffer', which is the same as 'message' except
// it returns buffers instead of strings.
// It's useful when the messages are binary data.
redis.on("messageBuffer", (channel, message) => {
  // Both `channel` and `message` are buffers.
  console.log(channel, message);
});
```

It's worth noticing that a connection (aka a `Redis` instance) can't play both roles at the same time. More specifically, when a client issues `subscribe()` or `psubscribe()`, it enters the "subscriber" mode. From that point, only commands that modify the subscription set are valid. Namely, they are: `subscribe`, `psubscribe`, `unsubscribe`, `punsubscribe`, `ping`, and `quit`. When the subscription set is empty (via `unsubscribe`/`punsubscribe`), the connection is put back into the regular mode.

If you want to do pub/sub in the same file/process, you should create a separate connection:

```highlight
const Redis = require("ioredis");
const sub = new Redis();
const pub = new Redis();

sub.subscribe(/* ... */); // From now, `sub` enters the subscriber mode.
sub.on("message" /* ... */);

setInterval(() => {
  // `pub` can be used to publish messages, or send other regular commands (e.g. `hgetall`)
  // because it's not in the subscriber mode.
  pub.publish(/* ... */);
}, 1000);
```

`PSUBSCRIBE` is also supported in a similar way when you want to subscribe all channels whose name matches a pattern:

```highlight
redis.psubscribe("pat?ern", (err, count) => {});

// Event names are "pmessage"/"pmessageBuffer" instead of "message/messageBuffer".
redis.on("pmessage", (pattern, channel, message) => {});
redis.on("pmessageBuffer", (pattern, channel, message) => {});
```


## Streams

Redis v5 introduces a new data type called streams. It doubles as a communication channel for building streaming architectures and as a log-like data structure for persisting data. With ioredis, the usage can be pretty straightforward. Say we have a producer publishes messages to a stream with `redis.xadd("mystream", "*", "randomValue", Math.random())` (You may find the official documentation of Streams as a starter to understand the parameters used), to consume the messages, we'll have a consumer with the following code:

```highlight
const Redis = require("ioredis");
const redis = new Redis();

const processMessage = (message) => {
  console.log("Id: %s. Data: %O", message[0], message[1]);
};

async function listenForMessage(lastId = "$") {
  // `results` is an array, each element of which corresponds to a key.
  // Because we only listen to one key (mystream) here, `results` only contains
  // a single element. See more: https://redis.io/commands/xread#return-value
  const results = await redis.xread("BLOCK", 0, "STREAMS", "mystream", lastId);
  const [key, messages] = results[0]; // `key` equals to "mystream"

  messages.forEach(processMessage);

  // Pass the last id of the results to the next round.
  await listenForMessage(messages[messages.length - 1][0]);
}

listenForMessage();
```


## Expiration

Redis can set a timeout to expire your key, after the timeout has expired the key will be automatically deleted. (You can find the official Expire documentation to understand better the different parameters you can use), to set your key to expire in 60 seconds, we will have the following code:

```highlight
redis.set("key", "data", "EX", 60);
// Equivalent to redis command "SET key data EX 60", because on ioredis set method,
// all arguments are passed directly to the redis server.
```


## Handle Binary Data

Binary data support is out of the box. Pass buffers to send binary data:

```highlight
redis.set("foo", Buffer.from([0x62, 0x75, 0x66]));
```

Every command that returns a bulk string has a variant command with a `Buffer` suffix. The variant command returns a buffer instead of a UTF-8 string:

```highlight
const result = await redis.getBuffer("foo");
// result is `<Buffer 62 75 66>`
```

It's worth noticing that you don't need the `Buffer` suffix variant in order to **send** binary data. That means in most case you should just use `redis.set()` instead of `redis.setBuffer()` unless you want to get the old value with the `GET` parameter:

```highlight
const result = await redis.setBuffer("foo", "new value", "GET");
// result is `<Buffer 62 75 66>` as `GET` indicates returning the old value.
```


## Pipelining

If you want to send a batch of commands (e.g. > 5), you can use pipelining to queue the commands in memory and then send them to Redis all at once. This way the performance improves by 50%~300% (See benchmark section).

`redis.pipeline()` creates a `Pipeline` instance. You can call any Redis commands on it just like the `Redis` instance. The commands are queued in memory and flushed to Redis by calling the `exec` method:

```highlight
const pipeline = redis.pipeline();
pipeline.set("foo", "bar");
pipeline.del("cc");
pipeline.exec((err, results) => {
  // `err` is always null, and `results` is an array of responses
  // corresponding to the sequence of queued commands.
  // Each response follows the format `[err, result]`.
});

// You can even chain the commands:
redis
  .pipeline()
  .set("foo", "bar")
  .del("cc")
  .exec((err, results) => {});

// `exec` also returns a Promise:
const promise = redis.pipeline().set("foo", "bar").get("foo").exec();
promise.then((result) => {
  // result === [[null, 'OK'], [null, 'bar']]
});
```

Each chained command can also have a callback, which will be invoked when the command gets a reply:

```highlight
redis
  .pipeline()
  .set("foo", "bar")
  .get("foo", (err, result) => {
    // result === 'bar'
  })
  .exec((err, result) => {
    // result[1][1] === 'bar'
  });
```

In addition to adding commands to the `pipeline` queue individually, you can also pass an array of commands and arguments to the constructor:

```highlight
redis
  .pipeline([
    ["set", "foo", "bar"],
    ["get", "foo"],
  ])
  .exec(() => {
    /* ... */
  });
```

`#length` property shows how many commands in the pipeline:

```highlight
const length = redis.pipeline().set("foo", "bar").get("foo").length;
// length === 2
```


## Transaction

Most of the time, the transaction commands `multi` & `exec` are used together with pipeline. Therefore, when `multi` is called, a `Pipeline` instance is created automatically by default, so you can use `multi` just like `pipeline`:

```highlight
redis
  .multi()
  .set("foo", "bar")
  .get("foo")
  .exec((err, results) => {
    // results === [[null, 'OK'], [null, 'bar']]
  });
```

If there's a syntax error in the transaction's command chain (e.g. wrong number of arguments, wrong command name, etc), then none of the commands would be executed, and an error is returned:

```highlight
redis
  .multi()
  .set("foo")
  .set("foo", "new value")
  .exec((err, results) => {
    // err:
    //  { [ReplyError: EXECABORT Transaction discarded because of previous errors.]
    //    name: 'ReplyError',
    //    message: 'EXECABORT Transaction discarded because of previous errors.',
    //    command: { name: 'exec', args: [] },
    //    previousErrors:
    //     [ { [ReplyError: ERR wrong number of arguments for 'set' command]
    //         name: 'ReplyError',
    //         message: 'ERR wrong number of arguments for \'set\' command',
    //         command: [Object] } ] }
  });
```

In terms of the interface, `multi` differs from `pipeline` in that when specifying a callback to each chained command, the queueing state is passed to the callback instead of the result of the command:

```highlight
redis
  .multi()
  .set("foo", "bar", (err, result) => {
    // result === 'QUEUED'
  })
  .exec(/* ... */);
```

If you want to use transaction without pipeline, pass `{ pipeline: false }` to `multi`, and every command will be sent to Redis immediately without waiting for an `exec` invocation:

```highlight
redis.multi({ pipeline: false });
redis.set("foo", "bar");
redis.get("foo");
redis.exec((err, result) => {
  // result === [[null, 'OK'], [null, 'bar']]
});
```

The constructor of `multi` also accepts a batch of commands:

```highlight
redis
  .multi([
    ["set", "foo", "bar"],
    ["get", "foo"],
  ])
  .exec(() => {
    /* ... */
  });
```

Inline transactions are supported by pipeline, which means you can group a subset of commands in the pipeline into a transaction:

```highlight
redis
  .pipeline()
  .get("foo")
  .multi()
  .set("foo", "bar")
  .get("foo")
  .exec()
  .get("foo")
  .exec();
```


## Lua Scripting

ioredis supports all of the scripting commands such as `EVAL`, `EVALSHA` and `SCRIPT`. However, it's tedious to use in real world scenarios since developers have to take care of script caching and to detect when to use `EVAL` and when to use `EVALSHA`. ioredis exposes a `defineCommand` method to make scripting much easier to use:

```highlight
const redis = new Redis();

// This will define a command myecho:
redis.defineCommand("myecho", {
  numberOfKeys: 2,
  lua: "return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}",
});

// Now `myecho` can be used just like any other ordinary command,
// and ioredis will try to use `EVALSHA` internally when possible for better performance.
redis.myecho("k1", "k2", "a1", "a2", (err, result) => {
  // result === ['k1', 'k2', 'a1', 'a2']
});

// `myechoBuffer` is also defined automatically to return buffers instead of strings:
redis.myechoBuffer("k1", "k2", "a1", "a2", (err, result) => {
  // result[0] equals to Buffer.from('k1');
});

// And of course it works with pipeline:
redis.pipeline().set("foo", "bar").myecho("k1", "k2", "a1", "a2").exec();
```

### Dynamic Keys

If the number of keys can't be determined when defining a command, you can omit the `numberOfKeys` property and pass the number of keys as the first argument when you call the command:

```highlight
redis.defineCommand("echoDynamicKeyNumber", {
  lua: "return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}",
});

// Now you have to pass the number of keys as the first argument every time
// you invoke the `echoDynamicKeyNumber` command:
redis.echoDynamicKeyNumber(2, "k1", "k2", "a1", "a2", (err, result) => {
  // result === ['k1', 'k2', 'a1', 'a2']
});
```

### As Constructor Options

Besides `defineCommand()`, you can also define custom commands with the `scripts` constructor option:

```highlight
const redis = new Redis({
  scripts: {
    myecho: {
      numberOfKeys: 2,
      lua: "return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}",
    },
  },
});
```

### TypeScript Usages

You can refer to the example for how to declare your custom commands.


## Transparent Key Prefixing

This feature allows you to specify a string that will automatically be prepended to all the keys in a command, which makes it easier to manage your key namespaces.

**Warning** This feature won't apply to commands like KEYS and SCAN that take patterns rather than actual keys(#239), and this feature also won't apply to the replies of commands even if they are key names (#325).

```highlight
const fooRedis = new Redis({ keyPrefix: "foo:" });
fooRedis.set("bar", "baz"); // Actually sends SET foo:bar baz

fooRedis.defineCommand("myecho", {
  numberOfKeys: 2,
  lua: "return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}",
});

// Works well with pipelining/transaction
fooRedis
  .pipeline()
  // Sends SORT foo:list BY foo:weight_*->fieldname
  .sort("list", "BY", "weight_*->fieldname")
  // Supports custom commands
  // Sends EVALSHA xxx foo:k1 foo:k2 a1 a2
  .myecho("k1", "k2", "a1", "a2")
  .exec();
```


## Transforming Arguments & Replies

Most Redis commands take one or more Strings as arguments, and replies are sent back as a single String or an Array of Strings. However, sometimes you may want something different. For instance, it would be more convenient if the `HGETALL` command returns a hash (e.g. `{ key: val1, key2: v2 }`) rather than an array of key values (e.g. `[key1, val1, key2, val2]`).

ioredis has a flexible system for transforming arguments and replies. There are two types of transformers, argument transformer and reply transformer:

```highlight
const Redis = require("ioredis");

// Here's the built-in argument transformer converting
// hmset('key', { k1: 'v1', k2: 'v2' })
// or
// hmset('key', new Map([['k1', 'v1'], ['k2', 'v2']]))
// into
// hmset('key', 'k1', 'v1', 'k2', 'v2')
Redis.Command.setArgumentTransformer("hmset", (args) => {
  if (args.length === 2) {
    if (args[1] instanceof Map) {
      // utils is a internal module of ioredis
      return [args[0], ...utils.convertMapToArray(args[1])];
    }
    if (typeof args[1] === "object" && args[1] !== null) {
      return [args[0], ...utils.convertObjectToArray(args[1])];
    }
  }
  return args;
});

// Here's the built-in reply transformer converting the HGETALL reply
// ['k1', 'v1', 'k2', 'v2']
// into
// { k1: 'v1', 'k2': 'v2' }
Redis.Command.setReplyTransformer("hgetall", (result) => {
  if (Array.isArray(result)) {
    const obj = {};
    for (let i = 0; i < result.length; i += 2) {
      obj[result[i]] = result[i + 1];
    }
    return obj;
  }
  return result;
});
```

There are three built-in transformers, two argument transformers for `hmset` & `mset` and a reply transformer for `hgetall`. Transformers for `hmset` and `hgetall` were mentioned above, and the transformer for `mset` is similar to the one for `hmset`:

```highlight
redis.mset({ k1: "v1", k2: "v2" });
redis.get("k1", (err, result) => {
  // result === 'v1';
});

redis.mset(
  new Map([
    ["k3", "v3"],
    ["k4", "v4"],
  ])
);
redis.get("k3", (err, result) => {
  // result === 'v3';
});
```

Another useful example of a reply transformer is one that changes `hgetall` to return array of arrays instead of objects which avoids an unwanted conversation of hash keys to strings when dealing with binary hash keys:

```highlight
Redis.Command.setReplyTransformer("hgetall", (result) => {
  const arr = [];
  for (let i = 0; i < result.length; i += 2) {
    arr.push([result[i], result[i + 1]]);
  }
  return arr;
});
redis.hset("h1", Buffer.from([0x01]), Buffer.from([0x02]));
redis.hset("h1", Buffer.from([0x03]), Buffer.from([0x04]));
redis.hgetallBuffer("h1", (err, result) => {
  // result === [ [ <Buffer 01>, <Buffer 02> ], [ <Buffer 03>, <Buffer 04> ] ];
});
```


## Monitor

Redis supports the MONITOR command, which lets you see all commands received by the Redis server across all client connections, including from other client libraries and other computers.

The `monitor` method returns a monitor instance. After you send the MONITOR command, no other commands are valid on that connection. ioredis will emit a monitor event for every new monitor message that comes across. The callback for the monitor event takes a timestamp from the Redis server and an array of command arguments.

Here is a simple example:

```highlight
redis.monitor((err, monitor) => {
  monitor.on("monitor", (time, args, source, database) => {});
});
```

Here is another example illustrating an `async` function and `monitor.disconnect()`:

```highlight
async () => {
  const monitor = await redis.monitor();
  monitor.on("monitor", console.log);
  // Any other tasks
  monitor.disconnect();
};
```


## Streamify Scanning

Redis 2.8 added the `SCAN` command to incrementally iterate through the keys in the database. It's different from `KEYS` in that `SCAN` only returns a small number of elements each call, so it can be used in production without the downside of blocking the server for a long time. However, it requires recording the cursor on the client side each time the `SCAN` command is called in order to iterate through all the keys correctly. Since it's a relatively common use case, ioredis provides a streaming interface for the `SCAN` command to make things much easier. A readable stream can be created by calling `scanStream`:

```highlight
const redis = new Redis();
// Create a readable stream (object mode)
const stream = redis.scanStream();
stream.on("data", (resultKeys) => {
  // `resultKeys` is an array of strings representing key names.
  // Note that resultKeys may contain 0 keys, and that it will sometimes
  // contain duplicates due to SCAN's implementation in Redis.
  for (let i = 0; i < resultKeys.length; i++) {
    console.log(resultKeys[i]);
  }
});
stream.on("end", () => {
  console.log("all keys have been visited");
});
```

`scanStream` accepts an option, with which you can specify the `MATCH` pattern, the `TYPE` filter, and the `COUNT` argument:

```highlight
const stream = redis.scanStream({
  // only returns keys following the pattern of `user:*`
  match: "user:*",
  // only return objects that match a given type,
  // (requires Redis >= 6.0)
  type: "zset",
  // returns approximately 100 elements per call
  count: 100,
});
```

Just like other commands, `scanStream` has a binary version `scanBufferStream`, which returns an array of buffers. It's useful when the key names are not utf8 strings.

There are also `hscanStream`, `zscanStream` and `sscanStream` to iterate through elements in a hash, zset and set. The interface of each is similar to `scanStream` except the first argument is the key name:

```highlight
const stream = redis.zscanStream("myhash", {
  match: "age:??",
});
```

The `hscanStream` also accepts the `noValues` option to specify whether Redis should return only the keys in the hash table without their corresponding values.

```highlight
const stream = redis.hscanStream("myhash", {
  match: "age:??",
  noValues: true,
});
```

You can learn more from the Redis documentation.

**Useful Tips** It's pretty common that doing an async task in the `data` handler. We'd like the scanning process to be paused until the async task to be finished. `Stream#pause()` and `Stream#resume()` do the trick. For example if we want to migrate data in Redis to MySQL:

```highlight
const stream = redis.scanStream();
stream.on("data", (resultKeys) => {
  // Pause the stream from scanning more keys until we've migrated the current keys.
  stream.pause();

  Promise.all(resultKeys.map(migrateKeyToMySQL)).then(() => {
    // Resume the stream here.
    stream.resume();
  });
});

stream.on("end", () => {
  console.log("done migration");
});
```


## Auto-reconnect

By default, ioredis will try to reconnect when the connection to Redis is lost except when the connection is closed manually by `redis.disconnect()` or `redis.quit()`.

It's very flexible to control how long to wait to reconnect after disconnection using the `retryStrategy` option:

```highlight
const redis = new Redis({
  // This is the default value of `retryStrategy`
  retryStrategy(times) {
    const delay = Math.min(times * 50, 2000);
    return delay;
  },
});
```

`retryStrategy` is a function that will be called when the connection is lost. The argument `times` means this is the nth reconnection being made and the return value represents how long (in ms) to wait to reconnect. When the return value isn't a number, ioredis will stop trying to reconnect, and the connection will be lost forever if the user doesn't call `redis.connect()` manually.

When reconnected, the client will auto subscribe to channels that the previous connection subscribed to. This behavior can be disabled by setting the `autoResubscribe` option to `false`.

And if the previous connection has some unfulfilled commands (most likely blocking commands such as `brpop` and `blpop`), the client will resend them when reconnected. This behavior can be disabled by setting the `autoResendUnfulfilledCommands` option to `false`.

By default, all pending commands will be flushed with an error every 20 retry attempts. That makes sure commands won't wait forever when the connection is down. You can change this behavior by setting `maxRetriesPerRequest`:

```highlight
const redis = new Redis({
  maxRetriesPerRequest: 1,
});
```

Set maxRetriesPerRequest to `null` to disable this behavior, and every command will wait forever until the connection is alive again (which is the default behavior before ioredis v4).

### Blocking Command Timeout

ioredis can apply a client-side timeout to blocking commands (such as `blpop`, `brpop`, `bzpopmin`, `bzmpop`, `blmpop`, `xread`, `xreadgroup`, etc.). This protects against scenarios where the TCP connection becomes a zombie (e.g., due to a silent network failure like a Docker network disconnect) and Redis never replies.

This feature is **opt-in**. It is **disabled by default** and is only enabled when `blockingTimeout` is set to a positive number of milliseconds. If `blockingTimeout` is omitted, `0`, or negative (for example `-1`), ioredis does not arm any client-side timeouts for blocking commands and their behavior matches Redis exactly.

```highlight
const redis = new Redis({
  blockingTimeout: 30000, // Enable blocking timeout protection
});
```

When enabled:

- For commands with a finite timeout (e.g., `blpop("key", 5)`), ioredis sets a client-side deadline based on the command's timeout plus a small grace period (`blockingTimeoutGrace`, default 100ms). If no reply arrives before the deadline, the command resolves with `null`—the same value Redis returns when a blocking command times out normally.
- For commands that block forever (e.g., `timeout = 0` or `BLOCK 0`), the `blockingTimeout` value is used as a safety net.

### Reconnect on Error

Besides auto-reconnect when the connection is closed, ioredis supports reconnecting on certain Redis errors using the `reconnectOnError` option. Here's an example that will reconnect when receiving `READONLY` error:

```highlight
const redis = new Redis({
  reconnectOnError(err) {
    const targetError = "READONLY";
    if (err.message.includes(targetError)) {
      // Only reconnect when the error contains "READONLY"
      return true; // or `return 1;`
    }
  },
});
```

This feature is useful when using Amazon ElastiCache instances with Auto-failover disabled. On these instances, test your `reconnectOnError` handler by manually promoting the replica node to the primary role using the AWS console. The following writes fail with the error `READONLY`. Using `reconnectOnError`, we can force the connection to reconnect on this error in order to connect to the new master. Furthermore, if the `reconnectOnError` returns `2`, ioredis will resend the failed command after reconnecting.

On ElastiCache instances with Auto-failover enabled, `reconnectOnError` does not execute. Instead of returning a Redis error, AWS closes all connections to the master endpoint until the new primary node is ready. ioredis reconnects via `retryStrategy` instead of `reconnectOnError` after about a minute. On ElastiCache instances with Auto-failover enabled, test failover events with the `Failover primary` option in the AWS console.


## Connection Events

The Redis instance will emit some events about the state of the connection to the Redis server.

| Event | Description |
|---|---|
| connect | emits when a connection is established to the Redis server. |
| ready | If `enableReadyCheck` is `true`, client will emit `ready` when the server reports that it is ready to receive commands (e.g. finish loading data from disk). Otherwise, `ready` will be emitted immediately right after the `connect` event. |
| error | emits when an error occurs while connecting. However, ioredis emits all `error` events silently (only emits when there's at least one listener) so that your application won't crash if you're not listening to the `error` event. When `redis.connect()` is explicitly called the error will also be rejected from the returned promise, in addition to emitting it. If `redis.connect()` is not called explicitly and `lazyConnect` is true, ioredis will try to connect automatically on the first command and emit the `error` event silently. |
| close | emits when an established Redis server connection has closed. |
| reconnecting | emits after `close` when a reconnection will be made. The argument of the event is the time (in ms) before reconnecting. |
| end | emits after `close` when no more reconnections will be made, or the connection is failed to establish. |
| wait | emits when `lazyConnect` is set and will wait for the first command to be called before connecting. |

You can also check out the `Redis#status` property to get the current connection status.

Besides the above connection events, there are several other custom events:

| Event | Description |
|---|---|
| select | emits when the database changed. The argument is the new db number. |


## Diagnostics Channel

ioredis publishes telemetry through Node.js `diagnostics_channel`, allowing APM tools and custom instrumentation to observe commands, connections, and batch operations without modifying application code.

These channels use `TracingChannel#tracePromise()` and emit `start`, `end`, `asyncStart`, `asyncEnd`, and `error` sub-events. Requires Node.js >= 18.19.0; on older versions the channels are silently unavailable (zero overhead). Subscribe via `tracing:<name>:<event>`:

```highlight
import dc from "node:diagnostics_channel";

dc.subscribe("tracing:ioredis:command:start", ({ command, args }) => {
  console.log(`> ${command}`, args);
});

dc.subscribe("tracing:ioredis:command:asyncEnd", ({ command }) => {
  console.log(`${command} settled`);
});

dc.subscribe("tracing:ioredis:command:error", ({ command, error }) => {
  console.error(`${command} failed:`, error);
});
```

| Channel name | Payload | Description |
|---|---|---|
| `ioredis:command` | `CommandTraceContext` | Individual command (standalone, pipeline, or within MULTI) |
| `ioredis:batch` | `BatchOperationContext` | MULTI transaction as a whole |
| `ioredis:connect` | `ConnectTraceContext` | Socket connection attempt |

Command arguments are sanitized before emission using rules adapted from `@opentelemetry/redis-common`. Sensitive values (e.g. values in `SET`, `AUTH` passwords) are replaced with `?`, while read-only commands like `GET` and `DEL` retain all arguments. This is safe by default: unlisted or custom commands have all arguments redacted.

Context types (`CommandTraceContext`, `BatchOperationContext`, `ConnectTraceContext`) are exported from `ioredis`.


## Offline Queue

When a command can't be processed by Redis (being sent before the `ready` event), by default, it's added to the offline queue and will be executed when it can be processed. You can disable this feature by setting the `enableOfflineQueue` option to `false`:

```highlight
const redis = new Redis({ enableOfflineQueue: false });
```


## TLS Options

Redis doesn't support TLS natively, however if the redis server you want to connect to is hosted behind a TLS proxy (e.g. stunnel) or is offered by a PaaS service that supports TLS connection (e.g. Redis.com), you can set the `tls` option:

```highlight
const redis = new Redis({
  host: "localhost",
  tls: {
    // Refer to `tls.connect()` section in
    // https://nodejs.org/api/tls.html
    // for all supported options
    ca: fs.readFileSync("cert.pem"),
  },
});
```

Alternatively, specify the connection through a `rediss://` URL.

```highlight
const redis = new Redis("rediss://redis.my-service.com");
```

If you do not want to use a connection string, you can also specify an empty `tls: {}` object:

```highlight
const redis = new Redis({
  host: "redis.my-service.com",
  tls: {},
});
```

### TLS Profiles

> **Warning** TLS profiles described in this section are going to be deprecated in the next major version. Please provide TLS options explicitly.

To make it easier to configure we provide a few pre-configured TLS profiles that can be specified by setting the `tls` option to the profile's name or specifying a `tls.profile` option in case you need to customize some values of the profile.

Profiles:

- `RedisCloudFixed`: Contains the CA for Redis.com Cloud fixed subscriptions
- `RedisCloudFlexible`: Contains the CA for Redis.com Cloud flexible subscriptions

```highlight
const redis = new Redis({
  host: "localhost",
  tls: "RedisCloudFixed",
});

const redisWithClientCertificate = new Redis({
  host: "localhost",
  tls: {
    profile: "RedisCloudFixed",
    key: "123",
  },
});
```


## Sentinel

ioredis supports Sentinel out of the box. It works transparently as all features that work when you connect to a single node also work when you connect to a sentinel group. Make sure to run Redis >= 2.8.12 if you want to use this feature. Sentinels have a default port of 26379.

To connect using Sentinel, use:

```highlight
const redis = new Redis({
  sentinels: [
    { host: "localhost", port: 26379 },
    { host: "localhost", port: 26380 },
  ],
  name: "mymaster",
});

redis.set("foo", "bar");
```

The arguments passed to the constructor are different from the ones you use to connect to a single node, where:

- `name` identifies a group of Redis instances composed of a master and one or more slaves (`mymaster` in the example);
- `sentinelPassword` (optional) password for Sentinel instances.
- `sentinels` are a list of sentinels to connect to. The list does not need to enumerate all your sentinel instances, but a few so that if one is down the client will try the next one.
- `role` (optional) with a value of `slave` will return a random slave from the Sentinel group.
- `preferredSlaves` (optional) can be used to prefer a particular slave or set of slaves based on priority. It accepts a function or array.
- `enableTLSForSentinelMode` (optional) set to true if connecting to sentinel instances that are encrypted

ioredis **guarantees** that the node you connected to is always a master even after a failover. When a failover happens, instead of trying to reconnect to the failed node (which will be demoted to slave when it's available again), ioredis will ask sentinels for the new master node and connect to it. All commands sent during the failover are queued and will be executed when the new connection is established so that none of the commands will be lost.

It's possible to connect to a slave instead of a master by specifying the option `role` with the value of `slave` and ioredis will try to connect to a random slave of the specified master, with the guarantee that the connected node is always a slave. If the current node is promoted to master due to a failover, ioredis will disconnect from it and ask the sentinels for another slave node to connect to.

If you specify the option `preferredSlaves` along with `role: 'slave'` ioredis will attempt to use this value when selecting the slave from the pool of available slaves. The value of `preferredSlaves` should either be a function that accepts an array of available slaves and returns a single result, or an array of slave values priorities by the lowest `prio` value first with a default value of `1`.

```highlight
// available slaves format
const availableSlaves = [{ ip: "127.0.0.1", port: "31231", flags: "slave" }];

// preferredSlaves array format
let preferredSlaves = [
  { ip: "127.0.0.1", port: "31231", prio: 1 },
  { ip: "127.0.0.1", port: "31232", prio: 2 },
];

// preferredSlaves function format
preferredSlaves = function (availableSlaves) {
  for (let i = 0; i < availableSlaves.length; i++) {
    const slave = availableSlaves[i];
    if (slave.ip === "127.0.0.1") {
      if (slave.port === "31234") {
        return slave;
      }
    }
  }
  // if no preferred slaves are available a random one is used
  return false;
};

const redis = new Redis({
  sentinels: [
    { host: "127.0.0.1", port: 26379 },
    { host: "127.0.0.1", port: 26380 },
  ],
  name: "mymaster",
  role: "slave",
  preferredSlaves: preferredSlaves,
});
```

Besides the `retryStrategy` option, there's also a `sentinelRetryStrategy` in Sentinel mode which will be invoked when all the sentinel nodes are unreachable during connecting. If `sentinelRetryStrategy` returns a valid delay time, ioredis will try to reconnect from scratch. The default value of `sentinelRetryStrategy` is:

```highlight
function (times) {
  const delay = Math.min(times * 10, 1000);
  return delay;
}
```
