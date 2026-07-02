---
title: "Hello from OpenAPI Generator"
source: https://openapi-generator.tech/
domain: openapi-codegen
license: CC-BY-SA-4.0
tags: openapi codegen, openapi specification, api client generation, swagger code generation
fetched: 2026-07-02
---

### Easy to Use

With *50+* client generators, you can easily generate code to interact with any server which exposes an OpenAPI document.

Maintainers of APIs may also automatically generate and distribute clients as part of official SDKs.

Each client supports different options and features, but all templates can be replaced with your own Mustache-based templates.

See

Customization

for details.

### Servers

Getting started with server development can be tough, especially if you're evaluating technologies. We can reduce the burden when you bring your own OpenAPI document.

Generate server stubs for 40+ different languages and technologies, including Java, Kotlin, Go, and PHP.

Some generators support *Inversion of Control*, allowing you to iterate on design via your OpenAPI document without worrying about blowing away your entire domain layer when you regenerate code.

### Schemas/Configs

Ever wanted to iteratively design a MySQL database, but writing table declarations was too tedious?

OpenAPI Generator offers some special generators such as Apache2 Configuration, MySQL and GraphQL schema generators.

You can easily extend these generators and their templates to create derivative generators!

### Documentation

OpenAPI documents allow you to convert the metadata about your API into some other format.

We include documentation formats such as HTML and Cwiki, which allow you to distribute static documentation to your consumers.

We also support generating from OpenAPI 2.0 to newer JSON/YAML OpenAPI 3.x documents.

## Learn How

OpenAPI Generator supports many different integrations and use cases, including (but not limited to):

- Maven Plugin
- Gradle Plugin
- Bazel Plugin
- SBT Plugin
- Cake Plugin
- CLI via Homebrew
- CLI via Docker
- CLI via npm
- Generator SaaS

For details, see Workflow Integrations

Generation also allows for easy customization via options, custom templates, or even custom generators on your classpath. See Customization for details.

## Active Community

**Connect** with us on Slack!

We're a very community-oriented project. We have an active community of users, contributors, and core team members on Slack. Slack is often a good place to start if you're looking for guidance about where to begin contributing, if you have an idea you're not sure fits the project, or if you just want to ask a question or say hello.

Slack is free to download, and our workspace is free to sign up.

## Try via npm

The npm package wrapper is cross-platform wrapper around the .jar artifact.

**Install** globally, exposing the CLI on the command line:

```bash
npm install @openapitools/openapi-generator-cli -g

openapi-generator-cli version-manager set 7.23.0

npm install @openapitools/openapi-generator-cli -D
                
```

Then, **generate** a ruby client from a valid petstore.yaml doc:

```bash
                openapi-generator-cli generate -i petstore.yaml -g ruby -o /tmp/test/
                
```

## Try via Homebrew

**Install** via homebrew:

```bash
brew install openapi-generator
```

Then, **generate** a ruby client from a valid petstore.yaml doc:

```bash
openapi-generator generate -i petstore.yaml -g ruby -o /tmp/test/
```

## Try via Docker

The OpenAPI Generator image acts as a standalone executable. It can be used as an alternative to installing via homebrew, or for developers who are unable to install Java or upgrade the installed version.

To generate code from a valid petstore.yaml doc with this image, you'll need to mount a local location as a volume.

```bash
docker run --rm \
    -v $PWD:/local openapitools/openapi-generator-cli generate \
    -i /local/petstore.yaml \
    -g go \
    -o /local/out/go
                
```

For a full list of our docker images, check out u/openapitools on Docker Hub.
