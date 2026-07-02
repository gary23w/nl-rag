---
title: "Flagger"
source: https://flagger.app/
domain: progressive-delivery-deep
license: CC-BY-SA-4.0
tags: progressive delivery, automated canary analysis, gradual traffic shift, release promotion gate
fetched: 2026-07-02
---

# Flagger

Progressive Delivery Operator for Kubernetes

## Safer Releases

Reduce the risk of introducing a new software version in production by gradually shifting traffic to the new version while measuring metrics like HTTP/gRPC request success rate and latency.

## Flexible Traffic Routing

Shift and route traffic between app versions automatically using an ingress controller or a service mesh compatible with Kubernetes Gateway API.

## Extensible Validation

Besides the builtin metrics checks, you can extend your application analysis with custom metrics and webhooks for running acceptance tests, load tests, or any other custom validation.

## # Progressive Delivery

Flagger was designed to give developers confidence in automating production releases with progressive delivery techniques.

Canary release

A benefit of using canary releases is the ability to do capacity testing of the new version in a production environment with a safe rollback strategy if issues are found. By slowly ramping up the load, you can monitor and capture metrics about how the new version impacts the production environment.

Martin Fowler (opens new window)

Flagger can run automated application analysis, testing, promotion and rollback for the following deployment strategies:

- **Canary** (progressive traffic shifting with session affinity)
  - Istio (opens new window), Linkerd (opens new window), Kuma Service Mesh (opens new window), Gateway API (opens new window)
  - Contour (opens new window), Gloo (opens new window), NGINX (opens new window), Skipper (opens new window), Traefik (opens new window), Apache APISIX (opens new window), Knative (opens new window)
- **A/B Testing** (HTTP headers and cookies traffic routing)
  - Istio (opens new window), Gateway API (opens new window), Contour (opens new window), NGINX (opens new window)
- **Blue/Green** (traffic switching and mirroring)
  - Kubernetes CNI (opens new window), Istio (opens new window), Linkerd, Kuma, Contour, Gloo, NGINX, Skipper, Traefik, Apache

Flagger's application analysis can be extended with metric queries targeting Prometheus, Datadog, CloudWatch, New Relic, Graphite, Dynatrace, InfluxDB and Google Cloud Monitoring.

Flagger can be configured to send notifications (opens new window) to Slack, Microsoft Teams, Discord and Rocket. It will post messages when a deployment has been initialised, when a new revision has been detected and if the canary analysis failed or succeeded.

## # GitOps

(GitOps with Flagger and Flux)

You can build fully automated GitOps pipelines for canary deployments with Flagger and Flux (opens new window).

GitOps

GitOps is a way to do Kubernetes cluster management and application delivery. It works by using Git as a single source of truth for declarative infrastructure and applications. With Git at the center of your delivery pipelines, developers can make pull requests to accelerate and simplify application deployments and operations tasks to Kubernetes.

## # Getting Help

If you have any questions about Flagger and progressive delivery:

- Read the Flagger docs (opens new window).
- Invite yourself to the CNCF community slack (opens new window) and join the #flagger (opens new window) channel.
- Check out the Flux talks section (opens new window) and to see a list of online talks, hands-on training and meetups.
- File an issue (opens new window).

Your feedback is always welcome!

## # License

Flagger is Apache 2.0 (opens new window) licensed and accepts contributions via GitHub pull requests.

Flagger was initially developed in 2018 at Weaveworks by Stefan Prodan. In 2020 Flagger became a Cloud Native Computing Foundation (opens new window) project, part of Flux (opens new window) family of GitOps tools.

(CNCF) (opens new window)
