---
title: "CNCF Distribution"
source: https://distribution.github.io/distribution/
domain: container-registry
license: CC-BY-SA-4.0
tags: container registry, container image registry, oci image, image distribution
fetched: 2026-07-02
---

# CNCF Distribution

Edit page

# Distribution Registry

## What it is

The Registry is a stateless, highly scalable server side application that stores and lets you distribute container images and other content. The Registry is open-source, under the permissive Apache license.

## Why use it

You should use the Registry if you want to:

- tightly control where your images are being stored
- fully own your images distribution pipeline
- integrate image storage and distribution tightly into your in-house development workflow

## Alternatives

Users looking for a zero maintenance, ready-to-go solution are encouraged to use one of the existing registry services. Many of these provide support and security scanning, and are free for public repositories. For example:

- Docker Hub
- Quay.io
- GitHub Packages

Cloud infrastructure providers such as AWS, Azure, Google Cloud and IBM Cloud also have container registry services available at a cost.

## Compatibility

The distribution registry implements the OCI Distribution Spec version 1.0.1.

## Basic commands

Start your registry

```sh
docker run -d -p 5000:5000 --name registry registry:3
```

Pull (or build) some image from the hub

```sh
docker pull ubuntu
```

Tag the image so that it points to your registry

```sh
docker image tag ubuntu localhost:5000/myfirstimage
```

Push it

```sh
docker push localhost:5000/myfirstimage
```

Pull it back

```sh
docker pull localhost:5000/myfirstimage
```

Now stop your registry and remove all data

```sh
docker container stop registry && docker container rm -v registry
```

## Next

You should now read the detailed introduction about the registry, or jump directly to deployment instructions.
