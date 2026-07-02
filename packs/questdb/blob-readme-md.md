---
title: "questdb/README.md at master · questdb/questdb · GitHub"
source: https://github.com/questdb/questdb/blob/master/README.md
domain: questdb
license: CC-BY-SA-4.0
tags: questdb database, time series database, sql time series, column-oriented dbms
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

questdb

/

questdb

Public

- Notifications You must be signed in to change notification settings
- Fork 1.6k
- Star

## Expand file tree

More file actions

More file actions

## Latest commit

## History

History

History

## File metadata and controls

429 lines (353 loc) · 50.4 KB

Outline

(QuestDB open source contributors)

English | 简体中文

QuestDB is an open-source time-series database offering blazingly fast ingestion and dynamic, low-latency SQL queries.

QuestDB delivers a multi-tier storage engine (WAL → native → Parquet on object storage), and the core engine is implemented in zero-GC Java and C++; QuestDB Enterprise includes additional components in Rust.

We achieve high performance via a column-oriented storage model, parallelized vector execution, SIMD instructions, and low-latency techniques. In addition, QuestDB is hardware efficient, with quick setup and operational efficiency.

> Ready to go? Jump to the Get started section.

*QuestDB Web Console - click to launch demo*

## Benefits of QuestDB

Feature highlights include:

- Low-latency, high-throughput ingestion — from single events to millions/sec
- Low-latency SQL with time-series extensions (ASOF JOIN, WINDOW JOIN, HORIZON JOIN, SAMPLE BY, LATEST ON)
- SIMD-accelerated, parallel execution
- Multi-tier storage: WAL → native columnar → Parquet (time-partitioned and time-ordered)
- Postgres protocol (PGwire) and REST API
- Views, materialized views, and n-dimensional arrays (incl. 2D arrays for order books)
- Web console for queries and data management
- Apache 2.0 open source and open formats — no vendor lock-in
- Finance functions and orderbook analytics

QuestDB excels with:

- financial market data (tick data, trades, order books, OHLC)
- Sensor/telemetry data with high data cardinality
- real-time dashboards and monitoring
- AI coding agents for automated data pipelines and analytics

And why use a time-series database?

Beyond performance and efficiency, with a specialized time-series database, you don't need to worry about:

- out-of-order data
- deduplication and exactly one semantics
- Continuous streaming ingest with many concurrent queries
- streaming data (low latency)
- volatile and "bursty" data
- adding new columns - change schema "on the fly" while streaming data

## Try QuestDB, demo and dashboards

The live, public demo is provisioned with the latest QuestDB release and sample datasets:

- Trades: live crypto trades with 30M+ rows per month (OKX exchange)
- FX order book: live charts with orderbook FX pairs.
- Trips: 10 years of NYC taxi trips with 1.6 billion rows

We also have some public, real-time demo dashboards using our Grafana-native plugin:

- Real-time crypto trades: executed trades on OKX from more than 20 assets in real time
- FX order book: live depth/imbalance charts for major FX pairs

### QuestDB performance vs. other databases

QuestDB performs very well in performance benchmarks compared to alternatives.

For deep dives into internals and performance, see the following blog posts:

- QuestDB vs InfluxDB
- QuestDB vs Kdb+
- QuestDB vs TimescaleDB
- QuestDB vs MongoDB

As always, we encourage you to run your own benchmarks.

## AI coding agents

QuestDB works out of the box with AI coding agents. Install the QuestDB agent skill and go from prompt to production in under 60 seconds: streaming ingestion, materialized views, and real-time analytics with zero manual code.

## Get started

Use Docker to start quickly:

```highlight
docker run -p 9000:9000 -p 9009:9009 -p 8812:8812 questdb/questdb
```

Or macOS users can use Homebrew:

```highlight
brew install questdb
brew services start questdb
```

```highlight
questdb start
questdb stop
```

Alternatively, to kickoff the full onboarding journey, start with our concise quick start guide.

### First-party ingestion clients

QuestDB clients for ingesting data via the InfluxDB Line Protocol:

- Python
- .NET
- C/C++
- Go
- Java
- NodeJS
- Rust

### Connect to QuestDB

Interact with QuestDB and your data via the following interfaces:

- Web Console for an interactive SQL editor and CSV import on port `9000`
- InfluxDB Line Protocol for streaming ingestion on port `9000`
- PostgreSQL Wire Protocol for programmatic queries on port `8812`
- REST API for CSV import and cURL on port `9000`

### Popular third-party tools

Popular tools that integrate with QuestDB include:

- Kafka
- Redpanda
- Grafana
- Polars
- Pandas
- PowerBI
- Superset
- Apache Flink
- Telegraf
- MindsDB

### End-to-end code scaffolds

From streaming ingestion to visualization with Grafana, start with code scaffolds from our quickstart repository.

### Configure QuestDB for production workloads

Find our capacity planning to fine-tune QuestDB for production workloads.

### QuestDB Enterprise

For secure operation at greater scale or within larger organizations.

Additional features include:

- high availability and read replica(s)
- multi-primary ingestion
- cold storage integration
- role-based access control
- TLS encryption
- native querying of Parquet files via object storage
- support SLAs, enhanced monitoring and more

Visit the Enterprise page for further details and contact information.

## Additional resources

### 📚 Read the docs

- QuestDB documentation: begin the journey
- Product roadmap: check out our plan for upcoming releases
- Tutorials: learn what's possible with QuestDB, step by step

### ❓ Get support

- Community Discourse forum: join technical discussions, ask questions, and meet other users!
- Public Slack: chat with the QuestDB team and community members
- GitHub issues: report bugs or issues with QuestDB
- Stack Overflow: look for common troubleshooting solutions

### 🚢 Deploy QuestDB

- AWS
- Google Cloud Platform
- Official Docker image
- DigitalOcean
- Kubernetes Helm charts

## Contribute

Contributions welcome!

We appreciate:

- source code
- documentation (see our documentation repository)
- bug reports
- feature requests or feedback.

To get started with contributing:

- Have a look through GitHub issues labelled "Good first issue"
- For Hacktoberfest, see the relevant labelled issues
- Read the contribution guide
- For details on building QuestDB, see the build instructions
- Create a fork of QuestDB and submit a pull request with your proposed changes
- Stuck? Join our public Slack for assistance

✨ As a sign of our gratitude, we send QuestDB swag to our contributors!

A big thanks goes to the following wonderful people who have contributed to QuestDB emoji key:

| **clickingbuttons** 💻 🤔 📓 | **ideoma** 💻 📓 ⚠️ | **tonytamwk** 💻 📓 | **sirinath** 🤔 | **igor-suhorukov** 💻 🤔 | **mick2004** 💻 📦 | **rawkode** 💻 🚇 |
|---|---|---|---|---|---|---|
| **solidnerd** 💻 🚇 | **solanav** 💻 📖 | **shantanoo-desai** 📝 💡 | **alexprut** 💻 🚧 | **lbowman** 💻 ⚠️ | **chankeypathak** 📝 | **upsidedownsmile** 💻 |
| **Nagriar** 💻 | **piotrrzysko** 💻 ⚠️ | **mpsq** 💻 | **siddheshlatkar** 💻 | **Yitaek** ✅ 💡 | **gabor-boros** ✅ 💡 | **kovid-r** ✅ 💡 |
| **TimBo93** 🐛 📓 | **zikani03** 💻 | **jaugsburger** 💻 🚧 | **TheTanc** 📆 🖋 🤔 | **davidgs** 🐛 🖋 | **kaishin** 💻 💡 | **bluestreak01** 💻 🚧 ⚠️ |
| **patrickSpaceSurfer** 💻 🚧 ⚠️ | **chenrui333** 🚇 | **bsmth** 📖 🖋 | **Ugbot** 💬 📓 📢 | **lepolac** 💻 🔧 | **tiagostutz** 📓 🐛 📆 | **Lyncee59** 🤔 💻 |
| **rrjanbiah** 🐛 | **sarunas-stasaitis** 🐛 | **RiccardoGiro** 🐛 | **duggar** 🐛 | **postol** 🐛 | **petrjahoda** 🐛 | **t00** 🐛 |
| **snenkov** 📓 🐛 🤔 | **marregui** 💻 🤔 🎨 | **bratseth** 💻 🤔 📓 | **welly87** 🤔 | **fuzzthink** 🤔 📓 | **nexthack** 💻 | **g-metan** 🐛 |
| **tim2skew** 🐛 📓 | **ospqsp** 🐛 | **SuperFluffy** 🐛 | **nu11ptr** 🐛 | **comunidadio** 🐛 | **mugendi** 🤔 🐛 📖 | **paulwoods222** 🐛 |
| **mingodad** 🤔 🐛 📖 | **houarizegai** 📖 | **jjsaunier** 🐛 | **zanek** 🤔 📆 | **Geekaylee** 📓 🤔 | **lg31415** 🐛 📆 | **null-dev** 🐛 📆 |
| **ultd** 🤔 📆 | **ericsun2** 🤔 🐛 📆 | **giovannibonetti** 📓 🐛 📆 | **wavded** 📓 🐛 | **puzpuzpuz** 📖 💻 📓 | **rstreics** 💻 🚇 📖 | **mariusgheorghies** 💻 🚇 📖 |
| **pswu11** 🖋 🤔 🎨 | **insmac** 💻 🤔 🎨 | **eugenels** 💻 🤔 🚧 | **bziobrowski** 💻 📆 | **Zapfmeister** 💻 📓 | **mkaruza** 💻 | **DylanDKnight** 📓 🐛 |
| **enolal826** 💻 | **glasstiger** 💻 | **argshook** 💻 🤔 🎨 🐛 | **amunra** 💻 📖 🐛 | **GothamsJoker** 💻 | **kocko** 💻 | **jerrinot** 💻 🤔 🐛 |
| **rberrelleza** 💻 | **Cobalt-27** 💻 | **eschultz** 💻 | **XinyiQiao** 💻 | **terasum** 📖 | **PlamenHristov** 💻 | **tris0laris** 📝 🤔 |
| **HeZean** 💻 🐛 | **iridess** 💻 📖 | **selmanfarukyilmaz** 🐛 | **donet5** 🤔 🐛 | **Zahlii** 🐛 | **salsasepp** 🐛 | **EmmettM** 🐛 ⚠️ |
| **robd003** 🤔 | **AllenEdison** 🐛 | **CSharpDummy** 🐛 | **shimondoodkin** 🐛 🤔 | **huuhait** 🐛 🤔 | **alexey-milovidov** 🐛 | **suconghou** 🐛 |
| **allegraharris** 💻 | **oliver-daniel** 💻 | **kerimsenturk5734** 📖 |   |   |   |   |

This project adheres to the all-contributors specification. Contributions of any kind are welcome!
