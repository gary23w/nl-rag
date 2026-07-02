---
title: "AWS Elastic Beanstalk"
source: https://en.wikipedia.org/wiki/AWS_Elastic_Beanstalk
domain: aws-elastic-beanstalk
license: CC-BY-SA-4.0
tags: aws elastic beanstalk, managed app platform, platform as a service, app deployment service
fetched: 2026-07-02
---

# AWS Elastic Beanstalk

**AWS Elastic Beanstalk** is an orchestration service offered by Amazon Web Services for deploying applications which orchestrates various AWS services, including EC2, S3, Simple Notification Service (SNS), CloudWatch, autoscaling, and Elastic Load Balancers. Elastic Beanstalk provides an additional layer of abstraction over the bare server and OS; users instead see a pre-built combination of OS and platform, such as "64bit Amazon Linux 2014.03 v1.1.0 running Ruby 2.0 (Puma)" or "64bit Debian jessie v2.0.7 running Python 3.4 (Preconfigured - Docker)". Deployment requires a number of components to be defined: an *'application'* as a logical container for the project, a *'version'* which is a deployable build of the application executable, a *'configuration template'* that contains configuration information for both the Beanstalk environment and for the product. Finally an *'environment'* combines a *'version'* with a *'configuration'* and deploys them. Executables themselves are uploaded as archive files to S3 beforehand and the *'version'* is just a pointer to this.

## Applications and software stacks

Supported applications and software stacks include:

- Apache Tomcat for Java applications
- Apache HTTP Server for PHP applications
- Apache HTTP Server for Python applications
- Nginx or Apache HTTP Server for Node.js applications
- Passenger or Puma for Ruby applications
- Microsoft IIS 7.5, 8.0, and 8.5 for .NET applications
- Java SE
- Docker
- Go
