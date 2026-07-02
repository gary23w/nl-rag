---
title: "Kibana"
source: https://en.wikipedia.org/wiki/Kibana
domain: elastic-security
license: CC-BY-SA-4.0
tags: elastic security stack, log search indexing, full text search engine, security dashboard visualization, security event correlation
fetched: 2026-07-02
---

# Kibana

**Kibana** is a source-available data visualization dashboard for Elasticsearch, developed by Elastic NV. It is written in TypeScript and JavaScript and runs as a browser-based application backed by a Node.js server. Kibana lets users create bar, line, and scatter charts, pie charts, maps, and other visualizations against data stored in an Elasticsearch cluster, and arrange those visualizations into shared dashboards.

Kibana is a component of the Elastic Stack, a collection of tools for ingesting, storing, and querying log and event data. The stack was originally called the ELK stack after its three original components: Elasticsearch, Logstash, and Kibana. Elastic NV renamed it the Elastic Stack in 2015 when it added Beats, a family of lightweight data shippers.

Kibana was originally released under the Apache License 2.0. In January 2021, Elastic re-licensed it under the proprietary Elastic License 2.0 and the Server Side Public License, removing it from open-source distribution. In August 2024, Elastic added the GNU Affero General Public License as a third licensing option, making the source again available under an OSI-approved free and open-source license.

## History

Kibana was created by Rashid Khan in 2013 as a front end for Elasticsearch. The project was released under the Apache License 2.0 and quickly adopted alongside Elasticsearch and Logstash. The three tools together became known as the ELK stack, a common pattern for centralizing and searching log data.

In 2015, Elastic NV, the company behind all three tools, rebranded the ELK stack as the Elastic Stack after introducing Beats, a set of lightweight agents for shipping data to Elasticsearch. Kibana became the standard visualization layer of that stack. Elastic provides Beats packages that include pre-built Kibana dashboards for common database and application technologies.

In October 2018, Elastic shipped **Canvas**, a presentation feature within Kibana that lets users build slide decks pulling live data directly from Elasticsearch.

In December 2019, Elastic introduced **Lens**, a drag and drop interface for building visualizations without writing aggregation queries.

### License changes

In January 2021, Elastic re-licensed both Elasticsearch and Kibana from the Apache License 2.0 to the Elastic License 2.0 and the Server Side Public License (SSPL). Elastic cited cloud providers offering Elasticsearch as a managed service without contributing back to the project as the reason for the change. Neither the Elastic License 2.0 nor the SSPL is approved by the Open Source Initiative, so the re-licensed versions were no longer considered open source by that definition.

In response, Amazon Web Services forked both Elasticsearch and Kibana at their last Apache-licensed versions. The resulting projects, released in April 2021 under the name OpenSearch, included **OpenSearch Dashboards** as the Kibana-derived visualization component.

In August 2024, Elastic added the GNU Affero General Public License (AGPLv3) as a third licensing option for both Elasticsearch and Kibana, allowing use under an OSI-approved license. The Elastic License 2.0 and SSPL options remain available alongside AGPLv3.

## Architecture

Kibana runs as a Node.js web server that connects to an Elasticsearch cluster over its REST API. The browser-based frontend is written in TypeScript and React. All persistent state, including saved searches, visualization definitions, and dashboard configurations, is stored as JSON documents in a dedicated Elasticsearch index.

Kibana exposes a query interface based on the Kibana Query Language (KQL), a simplified syntax for filtering documents by field values. It also supports the older Lucene query syntax and Elasticsearch SQL for users who require full query expressiveness.

The plugin architecture allows additional capabilities to be packaged and loaded at startup. Elastic ships several first-party plugins, including Maps (geospatial visualization), Canvas, Lens, and the Observability and Security solution views. Third-party plugins can be installed from the command line.

Logstash provides a common input path to Elasticsearch for structured and unstructured log data, which Kibana then surfaces through dashboards. The Elastic Stack also supports ingestion directly through Beats agents or the Elasticsearch ingest pipeline without Logstash.
