---
title: "Database"
source: https://supabase.com/docs/guides/database/overview
domain: supabase
license: CC-BY-SA-4.0
tags: supabase, backend as a service, postgres platform, cloud database
fetched: 2026-07-02
---

# Database

Database

# Database

Use Supabase to connect, manage, and secure your Postgres database.

Every Supabase project gets a full Postgres database, not a Postgres abstraction. This database is the foundation that Auth, Storage, Realtime, and Edge Functions are built on, and Supabase manages daily database backups and offers point-in-time recovery on paid plans.

Work with your project's database in the following ways:

- Visually using the **Table Editor** section of the Dashboard.
- With query syntax using the **SQL Editor** section of the Dashboard.
- Programmatically using a variety of different methods.

## Get started

If you're new to the database section, these are the pages to read first:

- Connect to your databaseConnection strings, the Supavisor connection pooler, and when to use direct, transaction, or session mode.
- Tables and dataCreate tables and relationships, and edit rows from the Dashboard.
- Import dataLoad existing data from CSV files, `pg_dump`, or another Postgres database.
- Secure your dataRow Level Security (RLS) is how Supabase makes the database safe to query directly from the client. Read this before exposing any table to your app.
- ExtensionsAdd Postgres extensions from the Dashboard, including `pgvector` for embeddings, `PostGIS` for geospatial data, and `pg_cron` for scheduled jobs.
- Run SQL commandsUse the Dashboard's SQL Editor for ad-hoc queries and saved snippets.

## Next steps

Once you've covered the basics, these guides help with other use cases and features:

- Database functionsRun logic inside the database in response to inserts, updates, or deletes.
- TriggersRun logic inside the database in response to inserts, updates, or deletes.
- Database webhooksSend row changes to an external HTTP endpoint.
- Replication and read replicasStream changes to other systems or read from a geographically closer replica.
- BackupsDaily backups on every project, with point-in-time recovery on paid plans. Backups cover the database itself; objects stored through the Storage API are not included.
- Query performance and optimizationIndexes, the query planner, and tools for finding slow queries.
- Roles and permissionsThe Postgres roles Supabase ships with and how to add your own.

### AI Tools

Ask ChatGPT

Ask Claude
