---
title: "Download Options for KeyDB"
source: https://docs.keydb.dev/docs/download/
domain: keydb
license: CC-BY-SA-4.0
tags: keydb database, multithreaded redis fork, in-memory data store, key-value cache
fetched: 2026-07-02
---

# Download Options for KeyDB

KeyDB offers a variety of packages for easy installation accross different distributions and architectures.

## KeyDB Managed Packages

The packages and distribution methods outlined below are actively managed by KeyDB.

| Type | Distribution Method Description | Link |
|---|---|---|
|   | Use our Docker Image to run your own containers. Follow this link to visit our docker page outlining pull and usage options. This image is manifested and supports x86 & ARM archtectures, a simple `docker pull eqalpha/keydb` will pull correct version. |   |
|   | Using Ubuntu? KeyDB has DEB packages for **Focal/Bionic/Xenial** packages for both x86_64/ARM_64 architectures. This includes binary and service installations. Just add the KeyDB Freight PPA to your /etc/apt/sources.list.d to be able to 'apt install keydb`. Click this link for full instructions, or go to the source link for individual .deb downloads. | source dir |
|   | KeyDB Debian packages are now available through the KeyDB Freight repo. **Bullseye/Buster/Stretch** packages for x86_64 & ARM64 are available. Similar to Ubuntu, add the repo to your /etc/apt/sources.list/d to be able to `apt install keydb`. You can also go to the sources link to download .deb packages individually. | source dir |
|   | **Centos7/8** RPM packages are available for individual download (x86_64 & ARM64). Click the button for instructions or the source link to go directly to the RPM package directory. The RPM packages will install the binaries as well as the service files. | source dir |
|   | For instructions on building KeyDB yourself select this option. You will find instructions for building on Centos 7/8, Ubuntu/Debian, Archlinux, Alpine and Fedora. Additional notes on build flags, and packaging dependencies are also here. |   |
|   | Go directly to the github page to see the sourcecode, create and issue or PR, or clone and download from there. |   |

## Community Contributed Offerings

The KeyDB Community has created and is managing some great distribution channels! Please see options below.

| Type | Distribution Method Description | Link |
|---|---|---|
|   | **Homebrew formulae** for KeyDB is available. Click this option to go to the Homebrew page, or simply run `brew install keydb`. Support avaialble for Intel (Monterey/Big Sur/Catalina/64-Bit Linux) and Apple Silicon(Monterey/Big Sur). | source dir |
|   | **KeyDB Multimaster Helm Chart** - this is a helm chart that supports KeyDB's multimaster/active-replication setups simplifying Kubernetes deployments. Select this option to view on ArtifactHUB of source for the github link. | source dir |
|   | **Archlinux Package** is available here as a user repository. See link and source for more info. | source dir |

Edit this page
