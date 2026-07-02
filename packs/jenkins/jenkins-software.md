---
title: "Jenkins (software)"
source: https://en.wikipedia.org/wiki/Jenkins_(software)
domain: jenkins
license: CC-BY-SA-4.0
tags: jenkins ci, continuous integration, build automation, jenkins pipeline
fetched: 2026-07-02
---

# Jenkins (software)

**Jenkins** is an open source automation server. It helps automate the parts of software development related to building, testing, and deploying, facilitating continuous integration, and continuous delivery. It is a server-based system that runs in servlet containers such as Apache Tomcat, or by default as a stand-alone web-application in co-bundled Eclipse Jetty. It supports version control tools, including AccuRev, CVS, Subversion, Git, Mercurial, Perforce, ClearCase, and RTC, and can execute Apache Ant, Apache Maven, and sbt based projects as well as arbitrary shell scripts and Windows batch commands.

## History

The Jenkins project was originally named *Hudson*, and was renamed in 2011 after a dispute with Oracle, which had forked the project and claimed rights to the project name. The Oracle fork, *Hudson*, continued to be developed for a time before being donated to the Eclipse Foundation. Oracle's Hudson is no longer maintained and was announced as obsolete in February 2017.

Around 2007 Hudson became known as a better alternative to Cruise Control and other open-source build-servers. At the JavaOne conference in May 2008 the software won the Duke's Choice Award in the Developer Solutions category.

During November 2010, after the acquisition of Sun Microsystems by Oracle, an issue arose in the Hudson community with respect to the infrastructure used, which grew to encompass questions over the stewardship and control by Oracle. Negotiations between the principal project contributors and Oracle took place, and although there were many areas of agreement a key sticking point was the trademarked name "Hudson," after Oracle claimed the right to the name and applied for a trademark in December 2010. As a result, on January 11, 2011, a call for votes was made to change the project name from "Hudson" to "Jenkins." The proposal was overwhelmingly approved by a community vote on January 29, 2011, creating the Jenkins project.

On February 1, 2011, Oracle said that they intended to continue development of Hudson, and considered Jenkins a fork rather than a rename. Jenkins and Hudson therefore continued as two independent projects, each claiming the other was the fork. As of June 2019, the Jenkins organization on GitHub had 667 project members and around 2,200 public repositories, compared with Hudson's 28 project members and 20 public repositories with the last update in 2016.

In 2011, creator Kohsuke Kawaguchi received an O'Reilly Open Source Award for his work on the Hudson/Jenkins project.

On April 20, 2016, version 2 was released with the *Pipeline* plugin enabled by default. The plugin allows for writing build instructions using a domain specific language based on Apache Groovy.

Jenkins replaced Hudson since February 8, 2017 in Eclipse.

In March 2018 Jenkins X software project for Kubernetes was publicly presented as a Jenkins sub-project, with support for different cloud providers including AWS EKS among others. Later, Jenkins X became an independent project under the Continuous Delivery Foundation.

In March 2019, Jenkins joined the Continuous Delivery Foundation, a new subsidiary of the Linux Foundation, as a founding project. In August 2020, Jenkins reached the graduated status in the foundation.

## Builds

Builds can be triggered by various means, for example:

- a webhook that gets triggered upon pushed commits in a version control system.
- scheduling via a cron-like mechanism.
- requesting a specific build URL.
- completion of preceding builds within the execution queue.
- Direct invocation by dependent upstream builds.

## Plugins

Plugins have been released for Jenkins that extend its use to projects written in languages other than Java. Plugins are available for integrating Jenkins with most version control systems and bug databases. Many build tools are supported via their respective plugins. Plugins can also change the way Jenkins looks or add new functionality. There are a set of plugins dedicated for the purpose of unit testing that generate test reports in various formats (for example, JUnit bundled with Jenkins, MSTest, NUnit, etc.) and automated testing that supports automated tests. Builds can generate test reports in various formats supported by plugins (JUnit support is currently bundled) and Jenkins can display the reports and generate trends and render them in the GUI.

## Mailer

Allows configuring email notifications for build results. Jenkins will send emails to the specified recipients whenever a certain important event occurs, such as:

1. Failed build.
2. Unstable build.
3. Successful build execution following a prior failure, indicating project recovery.
4. Unstable build after a successful one, indicating a regression.

## Credentials

Allows storing credentials in Jenkins. Provides a standardized API for other plugins to store and retrieve different types of credentials.

## Monitoring external jobs

Adds the ability to monitor the result of externally executed jobs.

## SSH agents

This plugin allows managing agents (formerly known as slaves) running on *nix machines over SSH. It adds a new type of agent launch method. This launch method will

1. Open a SSH connection to the specified host as the specified username,
2. Check the default version of Java for that user,
3. [not implemented yet] If the default version is not compatible with Jenkins's agent.jar, try to find a proper version of Java,
4. Once it has a suitable version of Java, copy the latest agent.jar via SFTP (falling back to scp if SFTP is not available),
5. Start the agent process.

### Javadoc

This plugin adds Javadoc support to Jenkins. This functionality used to be a part of the core, but as of Jenkins 1.431, it was split off into separate plugins.

The plugin enables the selection of "Publish Javadoc" as a post-build action, specifying the directory where the Javadoc is to be gathered and if retention is expected for each successful build.

### Online explanation

The platform provides a graphical user interface (GUI) to facilitate the scheduling and monitoring of shell scripts, reducing reliance on command-line execution.

## Security

Jenkins' security depends on two factors: access control and protection from external threats. Access control can be customized via two ways: user authentication and authorization. Protection from external threats such as CSRF attacks and malicious builds is supported as well.

## Awards and recognition

- InfoWorld Bossie Award (Best of Open Source Software Award) in 2011.
- Received Geek Choice Award in 2014.
