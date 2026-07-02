---
title: "Vagrant (software)"
source: https://en.wikipedia.org/wiki/Vagrant_(software)
domain: vagrant
license: CC-BY-SA-4.0
tags: hashicorp vagrant, development environment, virtual machine provisioning, reproducible dev environment
fetched: 2026-07-02
---

# Vagrant (software)

**Vagrant** is a source-available software product for building and maintaining portable virtual software development environments; e.g., for VirtualBox, KVM, Hyper-V, Docker containers, VMware, Parallels, and AWS. It tries to simplify the software configuration management of virtualization in order to increase development productivity. Vagrant is written in the Ruby language, but its ecosystem supports development in a few other languages.

## History

Vagrant was first started as a personal side-project by Mitchell Hashimoto in January 2010. The first version of Vagrant was released in March 2010. In October 2010, Engine Yard declared that they were going to sponsor the Vagrant project. The first stable version, Vagrant 1.0, was released in March 2012, exactly two years after the original version was released. In November 2012, Mitchell formed an organization called HashiCorp to support the full-time development of Vagrant; Vagrant remained permissively licensed free software. HashiCorp now works on creating commercial editions and provides professional support and training for Vagrant.

Vagrant was originally tied to VirtualBox, but version 1.1 added support for other virtualization software such as VMware and KVM, and for server environments like Amazon EC2. Vagrant is written in Ruby, but it can be used in projects written in other programming languages such as PHP, Python, Java, C#, and JavaScript. Since version 1.6, Vagrant natively supports Docker containers, which in some cases can serve as a substitute for a fully virtualized operating system.

## Architecture

Vagrant uses "Provisioners" and "Providers" as building blocks to manage the development environments. Provisioners are tools that allow users to customize the configuration of virtual environments. Puppet and Chef are the two most widely used provisioners in the Vagrant ecosystem (Ansible has been available since at least 2014). Providers are the services that Vagrant uses to set up and create virtual environments. Support for VirtualBox, Hyper-V, and Docker virtualization ships with Vagrant, while VMware and AWS are supported via plugins.

Vagrant sits on top of virtualization software as a wrapper and helps the developer interact easily with the providers. It automates the configuration of virtual environments using Chef or Puppet, and the user does not have to directly use any other virtualization software. Machine and software requirements are written in a file called "Vagrantfile" to execute necessary steps in order to create a development-ready box. "Box" is a format and an extension (.box) for Vagrant environments that is copied to another machine in order to replicate the same environment. The official Vagrant documentation details the installation, command line usage, and relevant configuration of Vagrant.

## License change

HashiCorp announced on Aug 10, 2023 that it changed the license of Vagrant from the MIT license to the Business Source License 1.1.
