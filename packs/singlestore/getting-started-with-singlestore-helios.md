---
title: "Getting Started with SingleStore Helios · SingleStore Helios Documentation"
source: https://docs.singlestore.com/cloud/getting-started-with-singlestore-helios/
domain: singlestore
license: CC-BY-SA-4.0
tags: singlestore database, memsql database, distributed sql, htap database
fetched: 2026-07-02
---

# Getting Started with SingleStore Helios · SingleStore Helios Documentation

AI agents/LLMs: Fetch /llms.txt first to access the documentation index. Remove the trailing slash and append .md to any URL to access lighter, easier-to-parse Markdown pages instead of HTML

(this page is accessible at https://docs.singlestore.com/cloud/getting-started-with-singlestore-helios.md)

.

# Getting Started with SingleStore Helios

## On this page

SingleStore allows you to build your applications for free with the Free Shared Edition. To register, go to Cloud Portal. The Free Shared Edition offers a free Shared workspace with one attached database. Refer to Shared Edition for more information on Shared workspace.

**Disclaimer:**

Shared workspaces are not intended for Production environments.

## Shared Workspace Compute and Storage

A Shared workspace uses a shared compute environment with a compressed storage limit of 1 GB. Refer to Operational Limits for Shared Workspace for more information.

## Connection Options

SingleStore Helios supports various connection options to connect and query your data.

### Connect to SingleStore

You can connect to SingleStore using your workspace via various application development tools.

To connect using the Shared workspace:

1. Select **Workspaces** in the left navigation pane.
2. Select **<your_shared_workspace>** from the list of workspaces, and then select **Connect**. You can connect to your Shared workspace using any of the supported tools.

#### CLI Client

Select **<your_shared_workspace> > Connect > External Tools > CLI Client**. Use any of the following tools to connect:

| Tool | How to Connect |
|---|---|
| MySQL Client | Select **CLI Client > MySQL Client**. Refer to Connect with MySQL Client for more information. |
| SingleStore Endpoints | Select **CLI Client > SingleStore Endpoints**. Refer to SingleStore Helios Endpoints for more information. |

For more information on supported CLI clients, refer to Connect to SingleStore.

#### SQL IDE

Select **<your_shared_workspace> > Connect > External Tools > SQL IDE**. Use any of the following tools to connect:

| Tool | How to Connect |
|---|---|
| Sequel Pro | Select **SQL IDE > Sequel Pro**. Refer to Connect with Sequel Pro for more information. |
| SQL Workbench | Select **SQL IDE > SQL Workbench**. Refer to Connect with SQL Workbench for more information. |

For more information on supported SQL IDEs, refer to Connect to SingleStore.

#### BI Tools

Select **<your_shared_workspace> > Connect > External Tools > BI Tools**. Use any of the following tools to connect:

| Tool | How to Connect |
|---|---|
| Tableau | Select **BI Tools > Tableau**. Refer to Connect with Tableau for more information. |
| Looker | Select **BI Tools > Looker**. Refer to Connect with Looker for more information. |
| Power BI | Select **BI Tools > Power BI**. Refer to Connect with Power BI for more information. |
| Other | Select **BI Tools > Others**. Refer to Connect with Analytics and BI Tools for more information. |

#### Your App

Select **<your_shared_workspace> > Connect > External Tools > Your App**. Use any of the following application tools to connect:

| Tool | How to Connect |
|---|---|
| Python | Select **Your App > Python**. Refer to Connect using the SingleStore Python Client for more information. |
| Node.js | Select **Your App > Node.js**. Refer to Connect with Node.js for more information. |
| Ruby on Rails | Select **Your App > Ruby on Rails**. Refer to Connect with Ruby for more information. |
| Perl | Select **Your App > Perl**. Refer to Connect with Perl for more information. |
| Java/JDBC | Select **Your App > Java/JDBC**. Refer to Connect with Java/JDBC for more information. |
| HTTP | Select **Your App > HTTP**. Refer to Data API for more information. |

For more information on supported application development tools and programming languages, refer to Connect with Application Development Tools.

#### MongoDB® Client

You can connect to your Shared workspace from supported MongoDB® tools and drivers using the `mongodb://` endpoint,  select **<your_shared_workspace> > Connect > External Tools > MongoDB Client**. Here's a sample connection string:

```
mongodb://<user>^<database>:<password>@svc-XXXX-shared-mongo.XXXX.svc.singlestore.com:27017/?authMechanism=PLAIN&tls=true&loadBalanced=true&dbName=<database>
```

For more information on supported tools and drivers, refer to Supported Tools.

### Query Data from the Cloud Portal

You can query your SingleStore database from the Cloud Portal.

#### SQL Editor

You can query the attached database of your Shared workspace using the SQL Editor. Select **Editor** in the left navigation, and then select **Open SQL Editor** on the right. Alternatively, you can select **<your_shared_workspace> > Connect > SQL Editor**.

Refer to Connect with the SQL Editor for more information.

#### Kai Shell

You can run MongoDB® commands on your Shared workspace using SingleStore Kai. Select **Editor** in the left navigation, and then select **Open Kai Shell**. Alternatively, you can select **<your_shared_workspace> > Connect > Kai Shell**. Refer to Kai Shell for more information.

#### Notebooks

SingleStore Helios offers Notebooks in the Shared workspace that supports SQL and Python development within a secure and seamless connection environment. Refer to Notebooks for more information.

Gallery is a collection of notebooks designed for use with SingleStore. You can also access this collection externally through Spaces. You can contribute to Spaces by following the steps in the SingleStore Spaces GitHub repository.
