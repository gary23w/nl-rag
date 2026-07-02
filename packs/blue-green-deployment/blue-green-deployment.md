---
title: "Blue–green deployment"
source: https://en.wikipedia.org/wiki/Blue%E2%80%93green_deployment
domain: blue-green-deployment
license: CC-BY-SA-4.0
tags: blue green deployment, zero downtime deployment, release strategy, traffic switching
fetched: 2026-07-02
---

# Blue–green deployment

In software engineering, **blue–green deployment** is a method of installing changes to a web, app, or database server by swapping alternating production and staging servers.

## Overview

In blue–green deployments, two servers are maintained: a "blue" server and a "green" server. At any given time, only one server is handling requests (e.g., being pointed to by the DNS). For example, public requests may be routed to the blue server, making it the production server and the green server the staging server, which can only be accessed on a private network. Changes are installed on the non-live server, which is then tested through the private network to verify the changes work as expected. Once verified, the non-live server is swapped with the live server, effectively making the deployed changes live.

Using this method of software deployment offers the ability to quickly roll back to a previous state if anything goes wrong. This rollback is achieved by simply routing traffic back to the previous live server, which still does not have the deployed changes. An additional benefit to the blue–green method of deployment is the reduced downtime for the server. Because requests are routed instantly from one server to the other, there is ideally no period where requests will be unfulfilled.

The blue–green deployment technique is often contrasted with the canary release deployment technique and it has similarities with A/B testing.

## History

Dan North and Jez Humble encountered differences between their test environments and the production environment while running Oracle WebLogic Server for a client sometime around 2005. To ensure safe deployment, they introduced a method where the new application version was deployed alongside the live system. This approach allowed for thorough testing and easy rollback in case of issues. The team initially considered naming these environments A and B but decided against it to avoid the perception that one was primary and the other secondary. They instead chose color-based names like blue, green, orange, and yellow, eventually using only blue and green since "having two was sufficient". This naming convention was adopted while working on the original Continuous delivery book published in 2010 and became a common term in the industry afterwards.

## Benefits and challenges

Blue–green deployment is widely recognized for its ability to reduce downtime during application updates and minimize the risk of introducing defects into production environments. By maintaining two separate environments—blue (the current live environment) and green (the environment with the updated version)—traffic can easily be switched between the two, ensuring that updates are rolled out without disrupting users. This method enables quick rollback in case of deployment failure, thus improving overall system resilience and user experience.

While blue–green deployment reduces risks during updates, it also requires additional resources since two environments need to be maintained simultaneously. The cost of running duplicate infrastructure, even temporarily, can be prohibitive for smaller organizations. Furthermore, complex database migrations may pose challenges, as the system must ensure that both the blue and green environments have consistent data. Solutions to these issues often involve using database migration tools that allow for backward compatibility between environments.

## Implementation

There are several approaches to implementing blue–green deployments, each offering varying levels of automation and ease of use depending on the platform and tools available.

### AWS CodeDeploy

AWS CodeDeploy facilitates blue–green deployments by automating the entire process across services such as Amazon EC2 and AWS Lambda. The service shifts traffic between the old (blue) environment and the new (green) environment, minimizing downtime and ensuring a smooth transition. AWS CodeDeploy also allows the use of lifecycle event hooks, enabling developers to run tests and verification steps before routing traffic to the green environment.

Sample CodeDeploy configuration:

```mw
version: 0.0
os: linux
files:
  - source: /
    destination: /var/www/html
hooks:
  AfterInstall:
    - location: scripts/start_server.sh
      timeout: 300
      runas: root
```

Deployment command:

```mw
aws deploy create-deployment --application-name MyApp --deployment-group-name MyDeploymentGroup --s3-location bucket=my-bucket,key=my-app.zip,bundleType=zip
```

### Kubernetes

Kubernetes supports blue–green deployments through its native service capabilities. Using multiple deployments and services, Kubernetes allows operators to manage traffic routing between blue and green environments with minimal risk of service interruptions. Tools like ArgoCD or Spinnaker further enhance automation by integrating deployment pipelines directly with Kubernetes clusters.

### Google Cloud Deployment Manager

Google Cloud offers blue–green deployment capabilities through Deployment Manager. By defining resources in a declarative format, Deployment Manager allows users to create, update, and delete resources as part of a blue–green deployment process. Like AWS CodeDeploy, it minimizes downtime by shifting traffic from the old to the new environment after performing necessary tests.

Setting up the environment:

- Install the `gcloud` CLI or use Google Cloud Shell.
- Set your default project:

```mw
gcloud config set project <YOUR_PROJECT_ID>
```

Cloning the sample repository:

```mw
gcloud source repos clone copy-of-gcp-mig-simple
cd copy-of-gcp-mig-simple
```

To modify the configuration, navigate to the configuration file (e.g., `infra/main.tfvars`) and update the environment from blue to green:

```mw
sed -i'' -e 's/blue/green/g' infra/main.tfvars
```

Adding, committing, and pushing your changes to trigger the deployment:

```mw
git add .
git commit -m "Promote green"
git push
```

Example of how the `main.tfvars` file might look like:

```mw
# main.tfvars
project_id = "<YOUR_PROJECT_ID>"
region = "us-central1"
zone = "us-central1-a"

# Load balancer settings
blue_instance_group = "blue-instance-group"
green_instance_group = "green-instance-group"

# Health check settings
health_check = {
  name                = "http-health-check"
  request_path        = "/"
  check_interval_sec  = 10
  timeout_sec         = 5
  healthy_threshold   = 2
  unhealthy_threshold = 2
}
```

### Azure Container Apps

Azure Container Apps provides blue–green deployment capabilities by using container app revisions, traffic weights, and revision labels. In this deployment model, two identical environments—referred to as "blue" and "green"—are used. The blue environment hosts the current stable version of the application, while the green environment holds the new version. Once the green environment is fully tested, production traffic is routed to it, and the blue environment is deprecated until the next deployment cycle.

To implement blue–green deployment, you create revisions of the container apps and assign traffic weights. The blue revision is assigned 100% of the traffic initially, while the green revision is deployed with no production traffic. After successful testing of the green revision, the traffic is switched over smoothly without downtime. If any issues arise in the green environment, a rollback is easily executed, routing traffic back to the blue revision.

Create a container app with a new revision:

```mw
az containerapp create --name $APP_NAME \
     --environment $APP_ENVIRONMENT_NAME \
     --resource-group $RESOURCE_GROUP \
     --image mcr.microsoft.com/k8se/samples/test-app:$BLUE_COMMIT_ID \
     --revision-suffix $BLUE_COMMIT_ID \
     --ingress external \
     --target-port 80 \
     --revisions-mode multiple
```

Deploy a new green revision:

```mw
az containerapp update --name $APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --image mcr.microsoft.com/k8se/samples/test-app:$GREEN_COMMIT_ID \
  --revision-suffix $GREEN_COMMIT_ID \
  --set-env-vars REVISION_COMMIT_ID=$GREEN_COMMIT_ID
```

Switch 100% of production traffic to the green revision:

```mw
az containerapp ingress traffic set \
  --name $APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --label-weight blue=0 green=100
```
