---
title: "Metabase documentation"
source: https://www.metabase.com/docs/latest/
domain: metabase
license: CC-BY-SA-4.0
tags: metabase analytics, business intelligence tool, self service dashboards, data visualization, ad hoc querying
fetched: 2026-07-02
---

# Metabase documentation

Log in

Get started

##### Analytics

- Getting started
- Metabase concepts
- Queries and charts
  - Introduction
  - Query builder
    - Editor
    - Filtering
    - Summarizing and grouping
    - Joining data
    - Custom expressions
    - List of expressions
  - SQL and native queries
    - SQL editor
    - SQL parameters
    - Field filters
    - Basic SQL parameters
    - Time grouping parameters
    - Table variables
    - Optional variables
    - Filter widgets
    - Referencing models and questions
    - Snippets
    - Snippet folder permissions
  - Visualizations
    - Overview
    - Box plot
    - Combo chart
    - Details chart
    - Funnel chart
    - Gauge chart
    - Line, bar, and area charts
    - Maps
    - Number chart
    - Pie and sunburst charts
    - Pivot tables
    - Progress bar
    - Sankey chart
    - Scatterplot
    - Table
    - Trend chart
    - Waterfall chart
    - Tooltips
    - Custom visualizations
    - Drill-through
  - Metrics explorer
  - Alerts
  - Exporting data
- Dashboards
  - Overview
  - Dashboard filters
  - Linked filters
  - Dashboard interactivity
  - Charts with multiple series
  - Dashboard subscriptions
  - Actions on dashboards
- Documents
  - Overview
- AI
  - Overview
  - Metabot
  - Metabot in Slack
  - Settings
  - MCP server
  - Agent API
  - Agent-driven development
  - Customization
  - System prompts
  - Usage auditing
  - Usage controls
  - AI privacy
- Data modeling
  - Models
  - Model persistence
  - Metrics
  - Table metadata settings
  - Data and semantic types
  - Editable tables
  - Formatting defaults
  - Working with JSON
  - Segments
  - Actions
    - Overview
    - Basic actions
    - Custom actions
- Data Studio
  - Overview
  - Library
  - Managing tables
  - Measures
  - Segments
  - Glossary
  - Dependencies
    - Dependency graph
    - Dependency diagnostics
    - Replace data sources
  - Transforms
    - Overview
    - Query transforms
    - Python transforms
    - Python runner
    - Jobs and runs
    - Transform inspector
    - Add-ons
- Organization
  - Basic exploration
  - Keyboard shortcuts
  - Collections
  - Data reference
  - Events and timelines
  - X-rays
  - Content verification
  - History
  - Delete and restore

##### Embedding

- Overview
- Modular embedding
  - Overview
  - Components
  - Filters and parameters
  - Appearance
  - Authentication
  - Tenants
  - Modular embedding SDK
    - Overview
    - Quickstarts
    - Components
      - Questions
      - Dashboards
      - AI chat
      - Collections
      - Plugins
    - Configuration
      - Provider config
      - Working with Next.js
      - Versioning
    - Upgrading
    - API
  - Guest embedding
  - Translate embeds
- Full app embedding
  - Overview
  - Quickstart
  - Full app UI components
- Public links and embeds
- Securing embeds
- AI agent resources

##### Administration

- Installation
  - Installing Metabase
    - Installation overview
    - Metabase Cloud
    - Running the JAR file
    - Running in Docker
    - Other installation options
  - Upgrading Metabase
  - Configuring the Metabase application database
  - Activating Enterprise features
  - Migrating to a production application database
- Data sources
  - Adding and managing databases
  - Supported databases
    - Athena
    - Amazon RDS
    - BigQuery
    - ClickHouse
    - Databricks
    - Druid
    - MariaDB
    - MongoDB
    - MySQL
    - Oracle
    - PostgreSQL
    - Presto
    - Redshift
    - Snowflake
    - SQL Server
    - SQLite
    - Spark SQL
    - Starburst
    - Vertica
    - Community drivers
  - Database users, roles, and privileges
  - Writable connection
  - Syncing and scanning databases
  - Encrypting your database connection
  - SSH tunneling
  - SSL certificate
  - Setting up data uploads
  - Uploading data
  - Metabase Cloud Storage
  - Sync Google Sheets
- Configuration
  - Setting up Metabase
  - General settings
  - Set up email
  - Set up Slack
  - Webhooks
  - Environment variables
  - Configuration file
  - Config file template
  - Metabase log configuration
  - Timezones
  - Languages and localization
  - Appearance
  - Fonts
  - Caching query results
  - Custom maps
  - Customizing the Metabase Jetty webserver
- Operations and monitoring
  - Backing up Metabase
  - Development instances
  - Monitoring your Metabase
  - Observability with Prometheus
  - Serialization
  - Remote Sync
  - Commands
  - Metabase CLI
  - Usage analytics
  - Security center
  - Admin tools
- Authentication
  - Account settings
  - Password complexity
  - Session expiration
  - Google Sign-In
  - LDAP
  - User provisioning
  - API keys
  - Paid SSO options
    - JWT-based authentication
    - SAML-based authentication
    - SAML with Auth0
    - SAML with Microsoft Entra ID
    - SAML with Google
    - SAML with Keycloak
    - SAML with Okta
    - OIDC-based authentication
    - OIDC with Keycloak
- Permissions
  - Permissions introduction
  - Managing people and groups
  - Data permissions
  - Collection permissions
  - Application permissions
  - Row and column security
  - Row and column security examples
  - Database routing
  - Impersonation
  - Snippets folder permissions
  - Notification permissions
  - Configuring permissions for embedding

##### Other resources

- API
- Metabase Cloud
  - Cloud vs self-hosted
  - Custom domain
  - Cloud limitations
  - Change region
  - IP addresses to whitelist
  - Migrate from self-hosted to Cloud
  - Migrate from Cloud to self-hosted
  - Migrate from Heroku
- Billing
  - How billing works
  - Accounts and billing
- Troubleshooting
- Developer guide
- Pro and Enterprise features
- Accessibility
- Supported browsers
- Privacy
- About the anonymous usage data we collect

v0.62

- v0.61
- v0.60
- v0.59
- v0.58
- v0.57
- v0.56
- v0.55
- v0.54
- v0.53
- See more

What’s new

v0.62

- v0.61
- v0.60
- v0.59
- v0.58
- v0.57
- v0.56
- v0.55
- v0.54
- v0.53
- See more

# Metabase documentation

(Metabase dashboard)

Metabase is an open-source business intelligence platform. You can use Metabase to ask questions about your data, or embed Metabase in your app to let your customers explore their data on their own.

## First steps

### Metabase Cloud

The easiest way to get started with Metabase is to sign up for a free trial of Metabase Cloud. You get support, backups, upgrades, an SMTP server, SSL certificate, SoC2 Type 2 security auditing, and more (plus your money goes toward improving Metabase). Check out our quick overview of cloud vs self-hosting. If you need to, you can always switch to self-hosting Metabase at any time (or vice versa).

### Installing Metabase

Run as a JAR, using Docker, or on Metabase Cloud.

### Setting up Metabase

Once installed, set up your Metabase and connect to your data.

### Getting started

With your data connected, get started asking questions, creating dashboards, and sharing your work.

### A tour of Metabase

Metabase is a deep product with a lot of tools to simplify business intelligence, from embeddable charts and interactive dashboards, to GUI and SQL editors, to auditing and row and column security, and more.

## Documentation topics

Metabase’s reference documentation.

### Installation

- Installation overview
- Installing Metabase
- Upgrading Metabase
- Configuring the Metabase application database
- Backing up Metabase
- Migrating to a production application database
- Monitoring your Metabase
- Development instances
- Serialization
- Remote sync
- Metabase CLI
- Metabase JAR commands
- Supported browsers
- Privacy
- About the anonymous usage data we collect

### Databases

- Databases overview
- Adding and managing databases
- Database users, roles, and privileges
- Syncing and scanning databases
- Encrypting your database connection
- SSH tunneling
- SSL certificate
- Uploading data

### Questions

- Questions overview
- Alerts
- Exporting data

#### Query builder

- The query editor
- Filtering
- Summarizing and grouping
- Custom expressions
- List of expressions
- Joining data

#### SQL and native queries

- The SQL editor
- SQL parameters
- Table variables
- Referencing models and saved questions
- Snippets
- Snippet folder permissions

#### Visualizing data

- Visualizing data
- Box plots
- Combo charts
- Custom visualizations
- Detail
- Funnel charts
- Gauge charts
- Line, bar, and area charts
- Maps
- Numbers
- Pie or donut charts
- Pivot table
- Progress bar
- Sankey chart
- Scatterplot or bubble chart
- Table
- Tooltips
- Trend
- Waterfall chart

### Dashboards

- Dashboards overview
- Introduction to dashboards
- Dashboard filters
- Interactive dashboards
- Charts with multiple series
- Dashboard subscriptions
- Actions on dashboards

### Documents

- Introduction to documents

### Data modeling

- Data modeling overview
- Models
- Model persistence
- Metrics
- Table metadata admin settings
- Field types
- Formatting defaults
- Working with JSON
- Segments

### Actions

- Actions overview
- Introduction to actions
- Basic actions
- Custom actions

### AI

- AI overview
- Metabot
- AI settings
- AI usage controls
- AI usage auditing
- AI customization
- AI system prompts
- Agent API
- MCP server
- Metabot in Slack
- AI privacy

### Exploration and organization

- Organization overview
- Basic exploration
- Collections
- Keyboard shortcuts
- History
- Trash
- Data reference
- Events and timelines
- X-rays
- Content verification

### People

- People overview
- Account settings
- Managing people and groups
- Password complexity
- Session expiration
- Google Sign-In
- LDAP
- API keys

#### Paid SSO options

- JWT-based authentication
- OIDC-based authentication
  - OIDC with Keycloak
- SAML-based authentication
  - SAML with Auth0
  - SAML with Microsoft Entra ID
  - SAML with Google
  - SAML with Keycloak
  - SAML with Okta
- User provisioning with SCIM

### Permissions

- Permissions overview
- Permissions introduction
- Data permissions
- Collection permissions
- Application permissions
- Row and column security
- Row and column security examples
- Connection impersonation
- Database routing
- Snippets folder permissions
- Notification permissions
- Configuring permissions for embedding

### Embedding

- Embedding overview
- Embedding introduction
- Modular embedding
  - SSO
  - Guest
  - SDK
- Full app embedding
- Securing embeds
- AI agent resources

### Configuration

- Configuration overview
- Setting up Metabase
- General settings
- Email
- Slack
- Webhooks
- Environment variables
- Configuration file
- Metabase log configuration
- Timezones
- Languages and localization
- Appearance
- Caching query results
- Custom maps
- Customizing the Metabase Jetty webserver

### Tools

- Tools overview
- Usage analytics
- Admin tools

### Metabase Cloud

- Documentation for Metabase Cloud and Store

### Metabase API

- Metabase API documentation
- API tutorial

### Troubleshooting

- Troubleshooting guides

### Developer guide

- Developer guide

## Getting help

### Troubleshooting

- Troubleshooting guides
- Metabase forum
- Configuring logging

### Tutorials and guides

Learn Metabase has a ton of articles on how to use Metabase, data best practices, and more.

## More resources

### Discussion

Share and connect with other Metabasers.

### Community stories

Practical advice from our community.

### Metabase blog

News, updates, and ideas.

### Customers

Real companies, real data, real stories.

### Metabase Twitter

We tweet stuff.

### Source code repository on GitHub

Follow us on GitHub.

### List of releases

A list of all Metabase releases, including both the Enterprise Edition and the Open Source Edition.

### Developers guide

Contribute to the Metabase open source project!

### Data and Business Intelligence Glossary

Data jargon explained.

### Metabase Experts

If you’d like more technical resources to set up your data stack with Metabase, connect with a Metabase Expert.

Read docs for other versions of Metabase.
