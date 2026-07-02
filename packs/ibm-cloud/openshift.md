---
title: "OpenShift"
source: https://en.wikipedia.org/wiki/OpenShift
domain: ibm-cloud
license: CC-BY-SA-4.0
tags: ibm cloud platform, ibm cloud watson, ibm cloud compute, enterprise cloud ibm
fetched: 2026-07-02
---

# OpenShift

**OpenShift** is a family of containerization software products developed by Red Hat. Its flagship product, **OpenShift Container Platform**, is a hybrid cloud platform as a service built around Linux containers orchestrated and managed by Kubernetes on a foundation of Red Hat Enterprise Linux. **OKD** (Origin Community Distribution) serves as the community-driven upstream.

The family's other products provide this platform through different environments. Deployment methods include self-managed; cloud native under **ROSA** (Red Hat OpenShift Service on AWS), **ARO** (Azure Red Hat OpenShift) and **RHOIC** (Red Hat OpenShift on IBM Cloud); OpenShift Online as software as a service; and OpenShift Dedicated as a managed service.

The OpenShift Console has developer and administrator oriented views. Administrator views allow one to monitor container resources and health, manage users and work with operators. Developer views are oriented around working with application resources within a namespace. OpenShift also provides a CLI that supports a superset of the actions provided by the Kubernetes CLI.

## History

OpenShift originated from Red Hat's acquisition of Makara, a company marketing a platform as a service (PaaS) based on Linux containers, in November 2010. It was announced in May 2011 as proprietary technology and only became open-source in May 2012. Until version 3, released in June 2015, OpenShift used custom developed technologies. Version 3 adopted Docker as the container technology and Kubernetes as the orchestration engine. Version 4 further changed the architecture, notably adopting CRI-O as the container runtime (and Podman for interacting with pods and containers), and Buildah as the container build tool, thus removing the dependency on Docker.

### OpenShift Online v2

Online offered version 2 of the OKD project source code, which is also available under the Apache License Version 2.0. This version supported a variety of languages, frameworks, and databases via pre-built "cartridges" running under resource-quota "gears". Developers could add other languages, databases, or components via the OpenShift Cartridge application programming interface. This was deprecated in favour of OpenShift 3, and was withdrawn on 30 September 2017 for non-paying customers and 31 December 2017 for paying customers.

## Architecture

The main difference between OpenShift and vanilla Kubernetes is its extension of the platform with build-related artifacts as first-class Kubernetes resources upon which standard Kubernetes operations can apply. OpenShift's *oc* client offers a superset of the standard *kubectl* (Kubernetes standard client) capabilities., including direct interaction with build resources via sub-commands like *new-build* or *start-build*. It also provided out of the box an OpenShift-native pod builds technology called Source-to-Image (S2I), though this is slowly being phased out in favor of Tekton, a cloud-native CI/CD framework for Kubernetes.

Other differences include:

1. An out-of-the-box integrated container image registry.
2. Unique resources like ImageStreams (a sequence of pointers to images which can be associated with deployments) and Templates (a packaging mechanism for application components).
3. The *new-app* command, which initiates an application deployment, automatically applies the *app* label (with the value of the label taken from the *--name* argument) to all created resources, simplifying management.
4. Support for multiple infrastructure platforms, including AWS, Azure, IBM Cloud, vSphere, and bare metal.
5. OpenShift’s implementation of Deployment, called DeploymentConfig is logic-based in comparison to Kubernetes' controller-based Deployment objects. As of v4.5, OpenShift is steering more towards Deployments by changing the default behavior of its CLI.
6. An embedded OperatorHub, a web GUI for browsing and installing a library of Kubernetes Operators packaged for easy life cycle management, including Red Hat authored Operators, Red Hat Certified Operators and Community Operators.

OpenShift v4 tightly controls the operating systems for "control plane" components. They must run on Red Hat CoreOS, enabling automated, reliable upgrades and patches. The compute (worker) nodes can run any Linux OS or even Windows.

OpenShift introduced the concept of *routes* -- points of traffic ingress into the cluster. This later influenced the Kubernetes ingress concept.

OpenShift also bundles various software components from the Kubernetes ecosystem for enhanced functionality. For observability, it includes Prometheus, Fluentd, Vector, Loki, and Istio (branded as Red Hat Service Mesh, based on the Maistra open source project).

## Products

### OpenShift Container Platform

OpenShift Container Platform (formerly known as OpenShift Enterprise) is Red Hat's on-premises private platform as a service product, built around application containers powered by CRI-O, with orchestration and management provided by Kubernetes, on Red Hat Enterprise Linux and Red Hat Enterprise Linux CoreOS.

### OKD

OKD, known until August 2018 as OpenShift Origin (Origin Community Distribution) is the upstream community project for OpenShift. Built around a core of CRI-O container runtime and Kubernetes cluster management, OKD is augmented by application life cycle management functionality and DevOps tooling. All source code for the OKD project is available under the Apache License (Version 2.0) on GitHub.

### Red Hat OpenShift Online

Red Hat OpenShift Online (RHOO) is a public cloud application development and hosting software as a service (SaaS) that runs on AWS and IBM Cloud. OpenShift Online is limited to running containers that do not require root.

### OpenShift Dedicated

OpenShift Dedicated (OSD) is Red Hat's managed private cluster offering on the marketplaces of Amazon Web Services (AWS), IBM Cloud, Google Cloud Platform (GCP) since December 2016. A similar managed service is offered on Microsoft Azure under the name Azure Red Hat OpenShift (ARO).

### OpenShift Data Foundation

OpenShift Data Foundation (ODF) provides cloud-native storage, data management and data protection for applications running on the OpenShift platform in cloud, on-premises, and hybrid/multi-cloud environments.

### OpenShift Database Access

Red Hat OpenShift Database Access (RHODA) is a capability for managed OpenShift environments (OSD and ROSA) that enables administrators to set up connections to database-as-a-service offerings from different providers. Its initial alpha release included support for MongoDB Atlas for MongoDB and Crunchy Bridge for PostgreSQL.
