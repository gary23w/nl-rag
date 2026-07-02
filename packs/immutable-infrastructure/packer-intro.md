---
title: "Introduction to Packer"
source: https://developer.hashicorp.com/packer/docs/intro
domain: immutable-infrastructure
license: CC-BY-SA-4.0
tags: immutable infrastructure, replace not patch, baked machine image, phoenix server
fetched: 2026-07-02
---

# Introduction to Packer

This introduction describes Packer benefits and how you can get started with it.

## What is Packer?

Packer is a community tool for creating identical machine images for multiple platforms from a single source configuration. Packer is lightweight, runs on every major operating system, and is highly performant, creating machine images for multiple platforms in parallel. Packer does not replace configuration management like Chef or Puppet. In fact, when building images, Packer is able to use tools like Chef or Puppet to install software onto the image.

A *machine image* is a single static unit that contains a pre-configured operating system and installed software which is used to quickly create new running machines. Machine image formats change for each platform. Some examples include AMIs for EC2, VMDK and VMX files for VMware, and OVF exports for VirtualBox.

## HCP Packer

For information about using HCP Packer to store metadata about build artifacts, refer to the HCP Packer documentation or sign into HCP to explore HCP Packer features.
