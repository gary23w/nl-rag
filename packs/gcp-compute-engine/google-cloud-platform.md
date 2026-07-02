---
title: "Google Cloud Platform"
source: https://en.wikipedia.org/wiki/Google_Cloud_Platform
domain: gcp-compute-engine
license: CC-BY-SA-4.0
tags: gcp compute engine, google compute engine, cloud virtual machine, gcp vm
fetched: 2026-07-02
---

# Google Cloud Platform

**Google Cloud** is a suite of cloud computing services offered by Google that provides a series of modular cloud services including computing, data storage, data analytics, and machine learning, alongside a set of management tools. It runs on the same infrastructure that Google uses internally for its end-user products, such as Google Search, Gmail, and Google Docs, according to Verma et al. Registration requires a credit card or bank account details.

Google Cloud provides infrastructure as a service, platform as a service, and serverless computing environments.

In April 2008, Google announced App Engine, a platform for developing and hosting web applications in Google-managed data centers, which was the first cloud computing service from the company. The service became generally available in November 2011. Since the announcement of App Engine, Google added multiple cloud services to the platform.

**Google Cloud** includes Google Cloud public cloud infrastructure, as well as Google Workspace (G Suite), enterprise versions of Android and ChromeOS, and application programming interfaces (APIs) for machine learning and enterprise mapping services. Since at least 2022, Google's official materials have stated that "Google Cloud" is the new name for "Google Cloud Platform," which may cause naming confusion.

## Products

Google lists over 100 products under the Google Cloud brand. Some of the key services are listed below.

### Compute

- App Engine – Platform as a Service to deploy applications developed with Java, PHP, Node.js, Python, C#, .Net, Ruby and Go programming languages
- Compute Engine – Infrastructure as a Service to run Microsoft Windows and Linux virtual machines.
- Google Kubernetes Engine (GKE) or GKE on-prem offered as part of Anthos platform – Containers as a Service based on Kubernetes
- Cloud Functions – Functions as a Service to run event-driven code written in Node.js, Java, Python, or Go
- Cloud Run – Compute execution environment based on Knative Offered as Cloud Run (fully managed) or as Cloud Run for Anthos. It currently supports GCP, AWS and VMware management.

### Storage and databases

- Cloud Storage – Object storage with integrated edge caching to store unstructured data
- Cloud SQL – Database as a Service based on MySQL, PostgreSQL and Microsoft SQL Server
- Cloud Bigtable – Managed NoSQL database service
- Cloud Spanner – Horizontally scalable, strongly consistent, relational database service
- Cloud Datastore – NoSQL database for web and mobile applications
- Persistent Disk – Block storage for Compute Engine virtual machines
- Cloud Memorystore – Managed in-memory data store based on Redis and Memcached
- Local SSD – High-performance, transient, local block storage
- Filestore – High-performance file storage for Google Cloud users
- AlloyDB – Fully managed PostgreSQL database service

### Networking

- VPC – Virtual Private Cloud for managing the software defined network of cloud resources
- Cloud Load Balancing – Software-defined, managed service for load balancing the traffic
- Cloud Armor – Web application firewall to protect workloads from DDoS attacks
- Cloud CDN – Content Delivery Network based on Google's globally distributed edge points of presence
- Cloud Interconnect – Service to connect a data center with Google Cloud
- Cloud DNS – Managed, authoritative DNS hosting service running on the same infrastructure as Google
- Network Service Tiers – Option to choose Premium vs Standard network tier for higher-performing network

### Big data

- BigQuery – Scalable, managed enterprise data warehouse for analytics
- Cloud Dataflow – Managed service based on Apache Beam for stream and batch data processing
- Cloud Data Fusion – A managed ETL service based on the Open Source Cask Data Application Platform
- Dataproc – Big data platform for running Apache Hadoop and Apache Spark jobs
- Cloud Composer – Managed workflow orchestration service built on Apache Airflow
- Cloud Datalab – Tool for data exploration, analysis, visualization and machine learning. It is a fully managed Jupyter Notebook service.
- Cloud Dataprep – Data service based on Trifacta to visually explore, clean, and prepare data for analysis
- Cloud Pub/Sub – Scalable event ingestion service based on message queues
- Looker Studio – Business intelligence tool to visualize data through dashboards and reports
- Looker – Business intelligence platform

### Cloud AI

- Cloud AutoML – Service to train and deploy custom machine learning models. As of September 2018, the service is in Beta.
- Cloud TPU – Accelerators used by Google to train machine learning models
- Cloud Machine Learning Engine – Managed service for training and building machine learning models based on mainstream frameworks
- Cloud Talent Solution (formerly Cloud Job Discovery) – Service based on Google's search and machine learning capabilities for the recruiting ecosystem
- Dialogflow Enterprise – Development environment based on Google's machine learning for building conversational interfaces
- Cloud Natural Language – Text analysis service based on Google Deep Learning models
- Cloud Speech-to-Text – Speech to text conversion service based on machine learning
- Cloud Text-to-Speech – Text to speech conversion service based on machine learning
- Cloud Translation API – Service to dynamically translate between thousands of available language pairs
- Cloud Vision API – Image analysis service based on machine learning
- Cloud Video Intelligence – Video analysis service based on machine learning

### Management tools

- Operations suite (formerly Stackdriver ) – Monitoring, logging, tracing, and diagnostics for applications on Google Cloud Platform
- Cloud Deployment Manager – Tool to deploy Google Cloud Platform resources defined in templates created in YAML, Python or Jinja2
- Cloud Console – Web interface to manage Google Cloud Platform resources
- Cloud Shell – Browser-based shell command-line access to manage Google Cloud Platform resources
- Cloud Console Mobile App – Android and iOS application to manage Google Cloud Platform resources
- Cloud APIs – APIs to programmatically access Google Cloud Platform resources

### Identity and security

- Cloud Identity – Single sign-on (SSO) service based on SAML 2.0 and OpenID
- Cloud IAM – Identity & Access Management (IAM) service for defining policies based on role-based access control
- Cloud Identity-Aware Proxy – Service to control access to cloud applications running on Google Cloud Platform without using a VPN
- Cloud Data Loss Prevention API – Service to automatically discover, classify, and redact sensitive data
- Security Key Enforcement – Two-step verification service based on a security key
- Cloud Key Management Service – Cloud-hosted key management service integrated with IAM and audit logging
- Cloud Resource Manager – Service to manage resources by project, folder, and organization based on the hierarchy
- Cloud Security Command Center – Security and data risk platform for data and services running in Google Cloud Platform
- Cloud Security Scanner – Automated vulnerability scanning service for applications deployed in App Engine
- Access Transparency – Near real-time audit logs providing visibility to Google Cloud Platform administrators
- VPC Service Controls – Service to manage security perimeters for sensitive data in Google Cloud Platform services

### Internet of things (IoT)

- Cloud IoT Core – Secure device connection and management service for Internet of Things
- Edge TPU – Purpose-built ASIC designed to run inference at the edge. As of 2018, this product is in private beta.
- Cloud IoT Edge – Brings AI to the edge computing layer

### API platform

- Maps Platform – APIs for maps, routes, and places based on Google Maps
- Apigee API Platform – Lifecycle management platform to design, secure, deploy, monitor, and scale APIs
- API Monetization – Tool for API providers to create revenue models, reports, payment gateways, and developer portal integrations
- Developer Portal – Self-service platform for developers to publish and manage APIs
- API Analytics – Service to analyze API-driven programs through monitoring, measuring, and managing APIs
- Apigee Sense – Enables API security by identifying and alerting administrators to suspicious API behaviors
- Cloud Endpoints – An NGINX-based proxy to deploy and manage APIs
- Service Infrastructure – A set of foundational services for building Google Cloud products

## Regions and zones

A region is a specific geographical location where users can deploy cloud resources. Each region is an independent geographic area that consists of zones.

A zone is a deployment area for Google Cloud Platform resources within a region. Zones should be considered a single failure domain within a region. Most regions have three zones.

As of Q1 2024, Google Cloud Platform is available in 40 regions and 121 zones. This is a list of those regions and zones:

| Region Name | Launch Date | Location | Zones |
|---|---|---|---|
| us-west1 | 2016-Q3 | The Dalles, Oregon, United States | us-west1-a us-west1-b us-west1-c |
| us-west2 | 2018-Q3 | Los Angeles, California, United States | us-west2-a us-west2-b us-west2-c |
| us-west3 | 2020-Q1 | Salt Lake City, Utah, United States | us-west3-a us-west3-b us-west3-c |
| us-west4 | 2020-Q2 | Las Vegas, Nevada, United States | us-west4-a us-west4-b us-west4-c |
| us-central1 | 2009 | Council Bluffs, Iowa, United States | us-central1-a us-central1-b us-central1-c us-central1-f |
| us-east1 | 2015-Q4 | Moncks Corner, South Carolina, United States | us-east1-b us-east1-c us-east1-d |
| us-east4 | 2017-Q2 | Ashburn, Virginia, United States | us-east4-a us-east4-b us-east4-c |
| us-east5 | 2022-Q2 | Columbus, Ohio, United States | us-east5-a us-east5-b us-east5-c |
| us-south1 | 2022-Q2 | Dallas, Texas, United States | us-south1-a us-south1-b us-south1-c |
| northamerica-northeast1 | 2018-Q1 | Montréal, Canada | northamerica-northeast1-a northamerica-northeast1-b northamerica-northeast1-c |
| northamerica-northeast2 | 2021-Q3 | Toronto, Canada | northamerica-northeast2-a northamerica-northeast2-b northamerica-northeast2-c |
| southamerica-east1 | 2017-Q3 | São Paulo, Brazil | southamerica-east1-a southamerica-east1-b southamerica-east1-c |
| southamerica-west1 | 2021-Q3 | Santiago, Chile | southamerica-west1-a southamerica-west1-b southamerica-west1-c |
| europe-west1 | 2013-Q4 | St. Ghislain, Belgium | europe-west1-b europe-west1-c europe-west1-d |
| europe-west2 | 2017-Q2 | London, UK | europe-west2-a europe-west2-b europe-west2-c |
| europe-west3 | 2017-Q3 | Frankfurt, Germany | europe-west3-a europe-west3-b europe-west3-c |
| europe-west4 | 2018-Q1 | Eemshaven, Netherlands | europe-west4-a europe-west4-b europe-west4-c |
| europe-west6 | 2019-Q1 | Zurich, Switzerland | europe-west6-a europe-west6-b europe-west6-c |
| europe-west8 | 2022-Q2 | Milan, Italy | europe-west8-a europe-west8-b europe-west8-c |
| europe-west9 | 2022-Q2 | Paris, France | europe-west9-a europe-west9-b europe-west9-c |
| europe-west10 | 2023-Q3 | Berlin, Germany | europe-west10-a europe-west10-b europe-west10-c |
| europe-west12 | 2023-Q1 | Turin, Italy | europe-west12-a europe-west12-b europe-west12-c |
| europe-central2 | 2021-Q2 | Warsaw, Poland | europe-central2-a europe-central2-b europe-central2-c |
| europe-north1 | 2018-Q2 | Hamina, Finland | europe-north1-a europe-north1-b europe-north1-c |
| europe-southwest1 | 2022-Q2 | Madrid, Spain | europe-southwest1-a europe-southwest1-b europe-southwest1-c |
| me-west1 | 2022-Q4 | Tel Aviv, Israel | me-west1-a me-west1-b me-west1-c |
| me-central1 | 2023-Q2 | Doha, Qatar | me-central1-a me-central1-b me-central1-c |
| me-central2 | 2023-Q4 | Dammam, Saudi Arabia | me-central2-a me-central2-b me-central2-c |
| asia-south1 | 2017-Q4 | Mumbai, India | asia-south1-a asia-south1-b asia-south1-c |
| asia-south2 | 2021-Q2 | Delhi, India | asia-south2-a asia-south2-b asia-south2-c |
| asia-southeast1 | 2017-Q2 | Jurong West, Singapore | asia-southeast1-a asia-southeast1-b asia-southeast1-c |
| asia-southeast2 | 2020-Q2 | Jakarta, Indonesia | asia-southeast2-a asia-southeast2-b asia-southeast2-c |
| asia-east1 | 2013-Q4 | Changhua County, Taiwan | asia-east1-a asia-east1-b asia-east1-c |
| asia-east2 | 2018-Q3 | Hong Kong | asia-east2-a asia-east2-b asia-east2-c |
| asia-northeast1 | 2016-Q4 | Tokyo, Japan | asia-northeast1-a asia-northeast1-b asia-northeast1-c |
| asia-northeast2 | 2019-Q2 | Osaka, Japan | asia-northeast2-a asia-northeast2-b asia-northeast2-c |
| asia-northeast3 | 2020-Q1 | Seoul, Korea | asia-northeast3-a asia-northeast3-b asia-northeast3-c |
| australia-southeast1 | 2017-Q3 | Sydney, Australia | australia-southeast1-a australia-southeast1-b australia-southeast1-c |
| australia-southeast2 | 2021-Q2 | Melbourne, Australia | australia-southeast2-a australia-southeast2-b australia-southeast2-c |
| africa-south1 | 2024-Q1 | Johannesburg, South Africa | africa-south1-a africa-south1-b africa-south1-c |

## Similarity to services by other cloud service providers

For those familiar with other notable cloud service providers, a comparison of similar services may be helpful in understanding Google Cloud Platform's offerings.

| Google Cloud Platform | Amazon Web Services | Microsoft Azure | Oracle Cloud |
|---|---|---|---|
| Google Compute Engine | Amazon EC2 | Azure Virtual Machines | Oracle Cloud Infra OCI |
| Google App Engine | AWS Elastic Beanstalk | Azure App Services | Oracle Application Container |
| Google Kubernetes Engine | Amazon Elastic Kubernetes Service | Azure Kubernetes Service | Oracle Kubernetes Service |
| Google Cloud Bigtable | Amazon DynamoDB | Azure Cosmos DB | Oracle NoSQL Database |
| Google BigQuery | Amazon Redshift | Azure Synapse Analytics | Oracle Autonomous Data Warehouse |
| Google Cloud Functions | AWS Lambda | Azure Functions | Oracle Cloud Fn |
| Google Cloud Datastore | Amazon DynamoDB | Azure Cosmos DB | Oracle NoSQL Database |
| Google Cloud Storage | Amazon S3 | Azure Blob Storage | Oracle Cloud Storage OCI |

## Timeline

- **April 2008** – Google App Engine announced in preview
- **May 2010** – Google Cloud Storage launched
- **May 2010** – Google BigQuery and Prediction API announced in preview
- **October 2011** – Google Cloud SQL is announced in preview
- **June 2012** – Google Compute Engine is launched in preview
- **May 2013** – Google Compute Engine is released to GA
- **August 2013** – Cloud Storage begins automatically encrypting each Storage object's data and metadata under the 128-bit Advanced Encryption Standard (AES-128), and each encryption key is itself encrypted with a regularly rotated set of master keys
- **February 2014** – Google Cloud SQL becomes GA
- **May 2014** – Stackdriver is acquired by Google
- **June 2014** – Kubernetes is announced as an open source container manager
- **June 2014** – Cloud Dataflow is announced in preview
- **October 2014** – Google acquires Firebase
- **November 2014** – Alpha release Google Kubernetes Engine (formerly Container Engine) is announced
- **January 2015** – Google Cloud Monitoring based on Stackdriver goes into Beta
- **March 2015** – Google Cloud Pub/Sub becomes available in Beta
- **April 2015** – Google Cloud DNS becomes generally available
- **April 2015** – Google Dataflow launched in beta
- **July 2015** – Google releases v1 of Kubernetes; Hands it over to The Cloud Native Computing Foundation
- **August 2015** – Google Cloud Dataflow, Google Cloud Pub/Sub, Google Kubernetes Engine, and Deployment Manager graduate to GA
- **November 2015** – Bebop is acquired, and Diane Greene joins Google
- **February 2016** – Google Cloud Functions becomes available in Alpha
- **September 2016** – Apigee, a provider of application programming interface (API) management company, is acquired by Google
- **September 2016** – Stackdriver becomes generally available
- **November 2016** – Qwiklabs, an EdTech company is acquired by Google
- **February 2017** – Cloud Spanner, highly available, globally-distributed database is released into Beta
- **March 2017** – Google acquires Kaggle, world's largest community of data scientists and machine learning enthusiasts
- **April 2017** – MIT professor Andrew Sutherland breaks the record for the largest ever Compute Engine cluster with 220,000 cores on Preemptible VMs.
- **May 2017** – Google Cloud IoT Core is launched in Beta
- **November 2017** – Google Kubernetes Engine gets certified by the CNCF
- **February 2018** – Google Cloud IoT Core becomes generally available
- **February 2018** – Google announces its intent to acquire Xively
- **February 2018** – Cloud TPUs, ML accelerators for Tensorflow, become available in Beta
- **May 2018** – Google Cloud Memorystore becomes available in Beta
- **April 2019** – Google Cloud Run (fully managed) Beta release
- **April 2019** – Google Anthos announced
- **November 2019** – Google Cloud Run (fully managed) General availability release
- **March 2020** – Due to the COVID-19 pandemic, Google Cloud postponed the online streaming version of its Google Cloud Next mega-conference, two weeks after it canceled the in-person version.
- **October 2020** – Google Cloud announced that it will become a block producer candidate for the EOS network and EOS.IO protocol. Currently the top block producers are cryptocurrency exchanges like OKEx and Binance.
- **February 2021** – Google Kubernetes Engine Autopilot is introduced.
- **May 2021** – Vertex AI announced at Google.io
- **June 2021** – In 2021, Apple was Google Cloud's biggest customer.
- **April 2022** – MobiledgeX acquired and joins Google Cloud.
- **March 2023** – Google brings generative AI capabilities to Google Cloud.
- **May 2024** Google Cloud partnered with Airtel.

## Public customers

Customers announced in 2023 include Kingfisher plc, the Government of Kuwait, Deutsche Börse Group, Unity Technologies, Uber, FanCode, Daimler, and Wix.com.
