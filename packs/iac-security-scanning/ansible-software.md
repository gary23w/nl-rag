---
title: "Ansible (software)"
source: https://en.wikipedia.org/wiki/Ansible_(software)
domain: iac-security-scanning
license: CC-BY-SA-4.0
tags: infrastructure as code security, iac misconfiguration scanning, policy as code enforcement, declarative provisioning audit
fetched: 2026-07-02
---

# Ansible (software)

**Ansible** is a suite of software tools that enables infrastructure as code. It is open-source and the suite includes software provisioning, configuration management, and application deployment functionality.

Originally written by Michael DeHaan in 2012, and acquired by Red Hat in 2015, Ansible is designed to configure both Unix-like systems and Microsoft Windows. Ansible is agentless, relying on temporary remote connections via SSH or Windows Remote Management which allows PowerShell execution. The Ansible control node runs on most Unix-like systems that are able to run Python, including Windows with Windows Subsystem for Linux installed. System configuration is defined in part by using its own declarative language.

## History

The term "ansible" was coined by Ursula K. Le Guin in her 1966 novel *Rocannon's World*, and refers to fictional instantaneous communication systems.

The Ansible tool was developed by Michael DeHaan, the author of the provisioning server application Cobbler and co-author of the Fedora Unified Network Controller (Func) framework for remote administration.

Ansible, Inc. (originally AnsibleWorks, Inc.) was the company founded in 2013 by DeHaan, Timothy Gerla, and Saïd Ziouani to commercially support and sponsor Ansible. Red Hat acquired Ansible in October 2015.

Ansible is included as part of the Fedora distribution of Linux, owned by Red Hat, and is also available for Red Hat Enterprise Linux, CentOS, openSUSE, SUSE Linux Enterprise, Debian, Ubuntu, Scientific Linux, Slackware via SlackBuilds, and Oracle Linux via Extra Packages for Enterprise Linux, as well as for other operating systems.

## Architecture

### Overview

Ansible helps to manage multiple machines by selecting portions of Ansible's inventory stored in simple plain text files. The inventory is configurable, and target machine inventory can be sourced dynamically or from cloud-based sources in different formats (YAML, INI).

Sensitive data can be stored in encrypted files using Ansible Vault since 2014. In contrast with other popular configuration-management software — such as Chef, Puppet, Salt and CFEngine — Ansible uses an *agentless* architecture, with Ansible software not normally running or even installed on the controlled node. Instead, Ansible orchestrates a node by installing and running *modules* on the node temporarily via SSH. For the duration of an orchestration task, a process running the module communicates with the controlling machine with a JSON-based protocol via its standard input and output. When Ansible is not managing a node, it does not consume resources on the node because no daemons are run or software installed.

#### Dependencies

Ansible requires Python to be installed on all managing machines, including pip package manager along with configuration-management software and its dependent packages. Managed network devices require no extra dependencies and are agentless.

### Control node

The control node (master host) is intended to manage (orchestrate) target machines (nodes termed as "inventory", see below). Control nodes can be run from Linux and Unix-like operating systems (including MacOS); Windows OSs are only supported through the Windows Subsystem for Linux. Multiple control nodes are allowed. Ansible does not require a single controlling machine for orchestration, ensuring that disaster recovery is simple. Nodes are managed by the controlling node over SSH.

### Design goals

The design goals of Ansible include:

- Minimal in nature. Management systems should not impose additional dependencies on the environment.
- Consistent. With Ansible, one should be able to create consistent environments.
- Secure. Ansible does not deploy agents to nodes. Only OpenSSH and Python are required on the managed nodes.
- Reliable. When carefully written, an Ansible playbook can be idempotent, to prevent unexpected side effects on the managed systems. It is possible to write playbooks that are not idempotent.
- Minimal learning required. Playbooks use an easy and descriptive language based on YAML and Jinja templates.

### Modules

Modules are mostly standalone and can be written in a standard scripting language (such as Python, Perl, Ruby, Bash, etc.). One of the guiding goals of modules is idempotency, which means that even if an operation is repeated multiple times (e.g., upon recovery from an outage), it will always place the system into the same state.

### Inventory configuration

Location of target nodes is specified through inventory configuration lists (INI or YAML formatted) located at `/etc/ansible/hosts` (on Linux). The configuration file lists either the IP address or hostname of each node that is accessible by Ansible. In addition, nodes can be assigned to groups.

An example inventory format (INI file):

```mw
192.168.6.1

[webservers]
foo.example.com
bar.example.com
```

This configuration file specifies three nodes: the first node is specified by an IP address, and the latter two nodes are specified by hostnames. Additionally, the latter two nodes are grouped under the `webservers` group.

Ansible can also use a custom *Dynamic Inventory* script, which can dynamically pull data from a different system, and supports groups of groups.

### Playbooks

Playbooks are YAML files that store lists of tasks for repeated executions on managed nodes. Each Playbook maps (associates) a group of hosts to a set of roles. Each role is represented by calls to Ansible tasks.

### Ansible Automation Platform

The Ansible Automation Platform (AAP) is a REST API, web service, and web-based interface (application) designed to make Ansible more accessible to people with a wide range of IT skillsets. It is a platform composed of multiple components including developer tooling, an operations interface, as well as an Automation Mesh to enable automation tasks at scale across data centers. AAP is a commercial product supported by Red Hat, Inc. but derived from 17+ upstream open source projects including the AWX upstream project (formerly Ansible Tower), which has been open source since September 2017.

There also is another open source alternative to Tower, Semaphore, written in Go.

## Platform support

Control machines have to be a Linux/Unix host (for example BSD, CentOS, Debian, macOS, Red Hat Enterprise Linux, SUSE Linux Enterprise, Ubuntu), and Python 2.7 or 3.5 is required.

Managed nodes, if they are Unix-like, must have Python 2.4 or later. For managed nodes with Python 2.5 or earlier, the `python-simplejson` package is also required. Since version 1.7, Ansible can also manage Windows nodes. In this case, native PowerShell remoting supported by the WS-Management protocol is used instead of SSH.

Ansible can deploy to bare metal hosts, virtual machines, and cloud environments.
