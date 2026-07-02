---
title: "GitHub"
source: https://github.com/taskforcesh/bullmq
domain: bullmq-queue
license: CC-BY-SA-4.0
tags: bullmq queue, redis job queue, background job processing, worker task scheduler
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

taskforcesh

/

bullmq

Public

- Notifications You must be signed in to change notification settings
- Fork 642
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History3,478 Commits3,478 Commits |   |   |   |
| .github | .github |   |   |
| .husky | .husky |   |   |
| config | config |   |   |
| docs/gitbook | docs/gitbook |   |   |
| elixir | elixir |   |   |
| php | php |   |   |
| python | python |   |   |
| rust | rust |   |   |
| scripts | scripts |   |   |
| src | src |   |   |
| tests | tests |   |   |
| .gitbook.yaml | .gitbook.yaml |   |   |
| .gitignore | .gitignore |   |   |
| .madgerc | .madgerc |   |   |
| .mocharc.js | .mocharc.js |   |   |
| .npmignore | .npmignore |   |   |
| .prettierignore | .prettierignore |   |   |
| .prettierrc.js | .prettierrc.js |   |   |
| CHANGELOG.md | CHANGELOG.md |   |   |
| CODE_OF_CONDUCT.md | CODE_OF_CONDUCT.md |   |   |
| LICENSE | LICENSE |   |   |
| README.md | README.md |   |   |
| commitlint.config.js | commitlint.config.js |   |   |
| composer.json | composer.json |   |   |
| contributing.md | contributing.md |   |   |
| docker-compose.yml | docker-compose.yml |   |   |
| eslint.config.mjs | eslint.config.mjs |   |   |
| mocha.setup.ts | mocha.setup.ts |   |   |
| osv-scanner.toml | osv-scanner.toml |   |   |
| package.json | package.json |   |   |
| renovate.json | renovate.json |   |   |
| tsconfig-cjs.json | tsconfig-cjs.json |   |   |
| tsconfig.json | tsconfig.json |   |   |
| tsdoc.json | tsdoc.json |   |   |
| vitest.adapter-conformance.config.ts | vitest.adapter-conformance.config.ts |   |   |
| vitest.bun.config.ts | vitest.bun.config.ts |   |   |
| vitest.bun.setup.ts | vitest.bun.setup.ts |   |   |
| vitest.config.ts | vitest.config.ts |   |   |
| vitest.coverage.config.ts | vitest.coverage.config.ts |   |   |
| vitest.ioredis.config.ts | vitest.ioredis.config.ts |   |   |
| vitest.node-redis.config.ts | vitest.node-redis.config.ts |   |   |
| vitest.node-redis.setup.ts | vitest.node-redis.setup.ts |   |   |
| vitest.setup.ts | vitest.setup.ts |   |   |
| yarn.lock | yarn.lock |   |   |
|   |   |   |   |

## Repository files navigation

The fastest, most reliable, Redis-based distributed queue for Node.js, Python, Rust, and more. Carefully written for rock solid stability and atomicity.

Read the

documentation

*Follow Us for *important* Bull/BullMQ/BullMQ-Pro news and updates!*

# 🛠 Tutorials

You can find tutorials and news in this blog: https://blog.taskforce.sh/

# News 🚀

## 🌐 Language agnostic BullMQ

BullMQ is available natively in multiple languages:

- **Node.js / Bun** — This repository (`npm install bullmq`)
- **Python** — `python/` directory (`pip install bullmq`)
- **Rust** — `rust/` directory (`cargo add bullmq`)
- **Elixir** — `elixir/` directory (`{:bullmq, "~> x.x"}`)
- **PHP** — `php/` directory

For other platforms, check out the BullMQ Proxy.

# Official FrontEnd

(Taskforce.sh, Inc)

Supercharge your queues with a professional front end:

- Get a complete overview of all your queues.
- Inspect jobs, search, retry, or promote delayed jobs.
- Metrics and statistics.
- and many more features.

Sign up at Taskforce.sh

# 🚀 Sponsors 🚀

| (Dragonfly) | Dragonfly is a new Redis™ drop-in replacement that is fully compatible with BullMQ and brings some important advantages over Redis™ such as massive better performance by utilizing all CPU cores available and faster and more memory efficient data structures. Read more here on how to use it with BullMQ. |
|---|---|

# Used by

Some notable organizations using BullMQ:

| (Microsoft) | (Vendure) | (Datawrapper) | (Nest) | (Langfuse) |
|---|---|---|---|---|
| (Curri) | (Novu) | (NoCodeDB) | (Infisical) |   |

# The gist

Install:

```
$ yarn add bullmq
```

If you use the node-redis adapter (`createNodeRedisClient`), install `redis` v5 or newer (`redis >= 5.0.0`).

Add jobs to the queue:

```highlight
import { Queue } from 'bullmq';

const queue = new Queue('Paint');

queue.add('cars', { color: 'blue' });
```

Process the jobs in your workers:

```highlight
import { Worker } from 'bullmq';

const worker = new Worker('Paint', async job => {
  if (job.name === 'cars') {
    await paintCar(job.data.color);
  }
});
```

Listen to jobs for completion:

```highlight
import { QueueEvents } from 'bullmq';

const queueEvents = new QueueEvents('Paint');

queueEvents.on('completed', ({ jobId }) => {
  console.log('done painting');
});

queueEvents.on(
  'failed',
  ({ jobId, failedReason }: { jobId: string; failedReason: string }) => {
    console.error('error painting', failedReason);
  },
);
```

Adds jobs with parent-child relationship:

```highlight
import { FlowProducer } from 'bullmq';

const flow = new FlowProducer();

const originalTree = await flow.add({
  name: 'root-job',
  queueName: 'topQueueName',
  data: {},
  children: [
    {
      name: 'child-job',
      data: { idx: 0, foo: 'bar' },
      queueName: 'childrenQueueName',
      children: [
        {
          name: 'grandchild-job',
          data: { idx: 1, foo: 'bah' },
          queueName: 'grandChildrenQueueName',
        },
        {
          name: 'grandchild-job',
          data: { idx: 2, foo: 'baz' },
          queueName: 'grandChildrenQueueName',
        },
      ],
    },
    {
      name: 'child-job',
      data: { idx: 3, foo: 'foo' },
      queueName: 'childrenQueueName',
    },
  ],
});
```

This is just scratching the surface, check all the features and more in the official documentation

# Feature Comparison

Since there are a few job queue solutions, here is a table comparing them:

| Feature | BullMQ-Pro | BullMQ | Bull | Kue | Bee | Agenda |
|---|---|---|---|---|---|---|
| Backend | redis | redis | redis | redis | redis | mongo |
| Observables | ✓ |   |   |   |   |   |
| Group Rate Limit | ✓ |   |   |   |   |   |
| Group Support | ✓ |   |   |   |   |   |
| Batches Support | ✓ |   |   |   |   |   |
| Parent/Child Dependencies | ✓ | ✓ |   |   |   |   |
| Deduplication (Debouncing) | ✓ | ✓ | ✓ |   |   |   |
| Deduplication (Throttling) | ✓ | ✓ | ✓ |   |   |   |
| Priorities | ✓ | ✓ | ✓ | ✓ |   | ✓ |
| Concurrency | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Delayed jobs | ✓ | ✓ | ✓ | ✓ |   | ✓ |
| Global events | ✓ | ✓ | ✓ | ✓ |   |   |
| Rate Limiter | ✓ | ✓ | ✓ |   |   |   |
| Pause/Resume | ✓ | ✓ | ✓ | ✓ |   |   |
| Sandboxed worker | ✓ | ✓ | ✓ |   |   |   |
| Repeatable jobs | ✓ | ✓ | ✓ |   |   | ✓ |
| Atomic ops | ✓ | ✓ | ✓ |   | ✓ |   |
| Persistence | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| UI | ✓ | ✓ | ✓ | ✓ |   | ✓ |
| Optimized for | Jobs / Messages | Jobs / Messages | Jobs / Messages | Jobs | Messages | Jobs |

## Contributing

Fork the repo, make some changes, submit a pull-request! Here is the contributing doc that has more details.

# Thanks

Thanks for all the contributors that made this library possible, also a special mention to Leon van Kammen that kindly donated his npm bullmq repo.
