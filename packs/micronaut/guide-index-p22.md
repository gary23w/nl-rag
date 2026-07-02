---
title: "Micronaut Core (part 22/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 22/27
---

## 9.2 HTTP filters context propagation

Modifying the propagated context is a common scenario. Usually, you want to extend the context to include the request-related values.

To use a non-reactive HTTP filter API, you need to add a method parameter MutablePropagatedContext and modify the propagated context elements by adding or removing the existing ones:

Example of adding a new MDC propagated context element

```java
@ServerFilter(MATCH_ALL_PATTERN)
public class MdcFilter {

    @RequestFilter
    public void myRequestFilter(HttpRequest<?> request, MutablePropagatedContext mutablePropagatedContext) {
        try {
            String trackingId = request.getHeaders().get("X-TrackingId");
            MDC.put("trackingId", trackingId);
            mutablePropagatedContext.add(new MdcPropagationContext());
        } finally {
            MDC.remove("trackingId");
        }
    }

}
```

The next filter in the chain will have the new propagated context available. Any of the thread-local context elements will be set for the next filter or the controller method invocation.

To use the legacy reactive HTTP filters, simply modify and propagate the context bound to the following chain invocation:

Example of adding a new MDC propagated context element for the reactive filter:

```java
@Filter(MATCH_ALL_PATTERN)
public class MdcLegacyFilter implements HttpServerFilter {

    @Override
    public Publisher<MutableHttpResponse<?>> doFilter(HttpRequest<?> request,
                                                      ServerFilterChain chain) {
        try {
            String trackingId = request.getHeaders().get("X-TrackingId");
            MDC.put("trackingId", trackingId);
            return PropagatedContext.get().plus(new MdcPropagationContext())
                .propagate(() -> chain.proceed(request));
        } finally {
            MDC.remove("trackingId");
        }
    }

}
```

# 10 Cloud Native Features

The majority of JVM frameworks in use today were designed before the rise of cloud deployments and microservice architectures. Applications built with these frameworks were intended to be deployed to traditional Java containers. As a result, cloud support in these frameworks typically comes as an add-on rather than as core design features.

Micronaut framework was designed from the ground up for building microservices for the cloud. As a result, many key features that typically require external libraries or services are available within your application itself. To override one of the industry’s current favorite buzzwords, Micronaut applications are "natively cloud-native".

The following are some cloud-specific features that are integrated directly into the Micronaut runtime:

- Distributed Configuration
- Service Discovery
- Client-Side Load-Balancing
- Distributed Tracing
- Serverless Functions

Many features in the Micronaut framework are heavily inspired by features from Spring and Grails. This is by design and helps developers who are already familiar with systems such as Spring Cloud.

The following sections cover these features and how to use them.


## 10.1 Cloud Configuration

Applications built for the Cloud often need to adapt to running in a Cloud environment, read and share configuration in a distributed manner, and externalize configuration to the environment where necessary.

Micronaut’s Environment concept can be configured to be Cloud platform-aware and makes the best effort to detect the underlying active Cloud environment.

To enable this feature you can:

1. call `deduceCloudEnvironment(true)` on the ApplicationContextBuilder interface when starting Micronaut. For example: Enabling Cloud Environment Detection `public static void main(String...args) { Micronaut.build(args) .deduceCloudEnvironment(true) .start(); }`
2. Set the `micronaut.env.cloud-deduction` property to `true` in your configuration.
3. Provide an environment variable `MICRONAUT_ENV_CLOUD_DEDUCTION` set to `true`.

You can then use the Requires annotation to conditionally load bean definitions.

The following table summarizes the constants in the Environment interface and provides an example:

| Constant | Description | Requires Example | Environment name |
|---|---|---|---|
| ANDROID | The application is running as an Android application | `@Requires(env = Environment.ANDROID)` | `android` |
| TEST | The application is running within a JUnit or Spock test | `@Requires(env = Environment.TEST)` | `test` |
| CLOUD | The application is running in a Cloud environment (present for all other cloud platform types) | `@Requires(env = Environment.CLOUD)` | `cloud` |
| AMAZON_EC2 | Running on Amazon EC2 | `@Requires(env = Environment.AMAZON_EC2)` | `ec2` |
| GOOGLE_COMPUTE | Running on Google Compute | `@Requires(env = Environment.GOOGLE_COMPUTE)` | `gcp` |
| KUBERNETES | Running on Kubernetes | `@Requires(env = Environment.KUBERNETES)` | `k8s` |
| HEROKU | Running on Heroku | `@Requires(env = Environment.HEROKU)` | `heroku` |
| CLOUD_FOUNDRY | Running on Cloud Foundry | `@Requires(env = Environment.CLOUD_FOUNDRY)` | `pcf` |
| AZURE | Running on Microsoft Azure | `@Requires(env = Environment.AZURE)` | `azure` |
| IBM | Running on IBM Cloud | `@Requires(env = Environment.IBM)` | `ibm` |
| DIGITAL_OCEAN | Running on Digital Ocean | `@Requires(env = Environment.DIGITAL_OCEAN)` | `digitalocean` |
| ORACLE_CLOUD | Running on Oracle Cloud | `@Requires(env = Environment.ORACLE_CLOUD)` | `oraclecloud` |

Note that you can have multiple environments active, for example when running in Kubernetes on AWS.

In addition, using the value of the constants defined in the table above you can create environment-specific configuration files. For example if you create a `src/main/resources/application-gcp.yml` file, it is only loaded when running on Google Compute.

|   | Any configuration property in the Environment can also be set via an environment variable. For example, setting the `CONSUL_CLIENT_HOST` environment variable overrides the `host` property in ConsulConfiguration. |
|---|---|

When the Micronaut framework detects it is running on a supported cloud platform, on startup it populates the interface ComputeInstanceMetadata.

|   | As of Micronaut framework 2.1.x this logic depends on the presence of the appropriate core Cloud module for Oracle Cloud, AWS, or GCP. |
|---|---|

All this data is merged together into the `metadata` property for the running ServiceInstance.

To access the metadata for your application instance you can use the interface EmbeddedServerInstance, and call `getMetadata()` which returns a Map of the metadata.

If you connect remotely via a client, the instance metadata can be referenced once you have retrieved a ServiceInstance from either the LoadBalancer or DiscoveryClient APIs.

|   | The Netflix Ribbon client-side load balancer can be configured to use the metadata to do zone-aware client-side load balancing. See Client-Side Load Balancing |
|---|---|

To obtain metadata for a service via Service Discovery use the LoadBalancerResolver interface to resolve a LoadBalancer and obtain a reference to a service by identifier:

Obtaining Metadata for a Service instance

```java
LoadBalancer loadBalancer = loadBalancerResolver.resolve("some-service");
Flux.from(
    loadBalancer.select()
).subscribe((instance) ->
    ConvertibleValues<String> metaData = instance.getMetadata();
    ...
);
```

The EmbeddedServerInstance is available through event listeners that listen for the ServiceReadyEvent. The @EventListener annotation makes it easy to listen for the event in your beans.

To obtain metadata for the locally running server, use an EventListener for the ServiceReadyEvent:

Obtaining Metadata for a Local Server

```java
@EventListener
void onServiceStarted(ServiceReadyEvent event) {
    ServiceInstance serviceInstance = event.getSource();
    ConvertibleValues<String> metadata = serviceInstance.getMetadata();
}
```


## 10.1.1 Distributed Configuration

As you can see, the Micronaut framework features a robust system for externalizing and adapting configuration to the environment inspired by similar approaches in Grails and Spring Boot.

However, what if you want multiple microservices to share configuration? The Micronaut framework includes APIs for distributed configuration.

For new applications and new integrations, the recommended approach is to use configuration import via `micronaut.config.import` instead of relying on the bootstrap context. Configuration imports let you load remote or shared configuration as part of normal property source resolution, and custom remote sources can be integrated with PropertySourceImporter implementations.

The ConfigurationClient interface has a `getPropertySources` method that can be implemented to read and resolve configuration from distributed sources.

The `getPropertySources` returns a Publisher that emits zero or many PropertySource instances.

The default implementation is DefaultCompositeConfigurationClient which merges all registered `ConfigurationClient` beans into a single bean.

You can either implement your own ConfigurationClient or use the implementations provided by Micronaut. For new work, prefer implementing distributed configuration through configuration import support and `PropertySourceImporter`. The following sections cover the available integrations.

|   | The bootstrap context is still available for legacy integrations and compatibility scenarios, but it is no longer the recommended default for distributed configuration. If you still load distributed configuration during bootstrap, implementing ConfigurationClient alone is not enough. The application also needs the discovery client infrastructure, which normally comes from the `io.micronaut.discovery:micronaut-discovery-client` dependency, and any beans involved in resolving that configuration must still be bootstrap-compatible. See Bootstrap Configuration for those legacy requirements. |
|---|---|


## 10.1.2 HashiCorp Consul Support

Consul is a popular Service Discovery and Distributed Configuration server provided by HashiCorp. The Micronaut framework features a native ConsulClient that uses Micronaut’s support for Declarative HTTP Clients.


## Starting Consul

The quickest way to start using Consul is via Docker:

1. Starting Consul with Docker

```
docker run -p 8500:8500 consul
```

Alternatively you can install and run a local Consul instance.


## Enabling Distributed Configuration with Consul

|   | Using the CLI If you create your project using the Micronaut CLI, supply the `config-consul` feature to enable Consul’s distributed configuration in your project: $ mn create-app my-app --features config-consul |
|---|---|

To enable distributed configuration make sure [bootstrap] is enabled and create a `src/main/resources/bootstrap.[yml/toml/properties]` file with the following configuration:

```properties
micronaut.application.name=hello-world
micronaut.config-client.enabled=true
consul.client.defaultZone=${CONSUL_HOST:localhost}:${CONSUL_PORT:8500}
```

```yaml
micronaut:
  application:
    name: hello-world
  config-client:
    enabled: true
consul:
  client:
    defaultZone: "${CONSUL_HOST:localhost}:${CONSUL_PORT:8500}"
```

```toml
[micronaut]
  [micronaut.application]
    name="hello-world"
  [micronaut.config-client]
    enabled=true
[consul]
  [consul.client]
    defaultZone="${CONSUL_HOST:localhost}:${CONSUL_PORT:8500}"
```

```groovy
micronaut {
  application {
    name = "hello-world"
  }
  configClient {
    enabled = true
  }
}
consul {
  client {
    defaultZone = "${CONSUL_HOST:localhost}:${CONSUL_PORT:8500}"
  }
}
```

```hocon
{
  micronaut {
    application {
      name = "hello-world"
    }
    config-client {
      enabled = true
    }
  }
  consul {
    client {
      defaultZone = "${CONSUL_HOST:localhost}:${CONSUL_PORT:8500}"
    }
  }
}
```

```json
{
  "micronaut": {
    "application": {
      "name": "hello-world"
    },
    "config-client": {
      "enabled": true
    }
  },
  "consul": {
    "client": {
      "defaultZone": "${CONSUL_HOST:localhost}:${CONSUL_PORT:8500}"
    }
  }
}
```

After enabling distributed configuration, store the configuration to share in Consul’s key/value store. There are a number of ways to do that.


## Storing Configuration as Key/Value Pairs

One way is to store the keys and values directly in Consul. In this case by default the Micronaut framework looks for configuration in the Consul `/config` directory.

|   | You can alter the path searched for by setting `consul.client.config.path` |
|---|---|

Within the `/config` directory Micronaut searches values within the following directories in order of precedence:

| Directory | Description |
|---|---|
| `/config/application` | Configuration shared by all applications |
| `/config/application,prod` | Configuration shared by all applications for the `prod` Environment |
| `/config/[APPLICATION_NAME]` | Application-specific configuration, example `/config/hello-world` |
| `/config/[APPLICATION_NAME],prod` | Application-specific configuration for an active Environment |

The value of `APPLICATION_NAME` is whatever your have configured `micronaut.application.name` to be in your `bootstrap` configuration file.

To see this in action, use the following cURL command to store a property called `foo.bar` with a value of `myvalue` in the directory `/config/application`.

Using cURL to Write a Value

```bash
curl -X PUT -d @- localhost:8500/v1/kv/config/application/foo.bar <<< myvalue
```

If you now define a `@Value("${foo.bar}")` or call `environment.getProperty(..)` the value `myvalue` will be resolved from Consul.


## Storing Configuration in YAML, JSON etc.

Some Consul users prefer storing configuration in blobs of a certain format, such as YAML. The Micronaut framework supports this mode and supports storing configuration in either YAML, JSON, or Java properties format.

|   | The ConfigDiscoveryConfiguration has a number of configuration options for configuring how distributed configuration is discovered. |
|---|---|

You can set the `consul.client.config.format` option to configure the format with which properties are read.

For example, to configure JSON:

```properties
consul.client.config.format=JSON
```

```yaml
consul:
  client:
    config:
      format: JSON
```

```toml
[consul]
  [consul.client]
    [consul.client.config]
      format="JSON"
```

```groovy
consul {
  client {
    config {
      format = "JSON"
    }
  }
}
```

```hocon
{
  consul {
    client {
      config {
        format = "JSON"
      }
    }
  }
}
```

```json
{
  "consul": {
    "client": {
      "config": {
        "format": "JSON"
      }
    }
  }
}
```

Now write your configuration in JSON format to Consul:

Using cURL to write JSON

```bash
curl -X PUT  localhost:8500/v1/kv/config/application \
-d @- << EOF
{ "foo": {  "bar": "myvalue" } }
EOF
```


## Storing Configuration as File References

Another popular option is git2consul which mirrors the contents of a Git repository to Consul’s key/value store.

You can set up a Git repository that contains files like `application.yml`, `hello-world-test.json`, etc., and the contents of these files will be cloned to Consul.

In this case, each key in Consul represents a file with an extension, for example `/config/application.yml`, and you must configure the `FILE` format:

```properties
consul.client.config.format=FILE
```

```yaml
consul:
  client:
    config:
      format: FILE
```

```toml
[consul]
  [consul.client]
    [consul.client.config]
      format="FILE"
```

```groovy
consul {
  client {
    config {
      format = "FILE"
    }
  }
}
```

```hocon
{
  consul {
    client {
      config {
        format = "FILE"
      }
    }
  }
}
```

```json
{
  "consul": {
    "client": {
      "config": {
        "format": "FILE"
      }
    }
  }
}
```


## 10.1.3 HashiCorp Vault Support

The Micronaut framework integrates with HashiCorp Vault as a distributed configuration source.

To enable distributed configuration make sure [bootstrap] is enabled and create a `src/main/resources/bootstrap.[yml/toml/properties]` file with the following configuration:

Integrating with HashiCorp Vault

```properties
micronaut.application.name=hello-world
micronaut.config-client.enabled=true
vault.client.uri=http://localhost:8200
vault.client.config.enabled=true
```

```yaml
micronaut:
  application:
    name: hello-world
  config-client:
    enabled: true

vault:
  client:
    uri: http://localhost:8200
    config:
      enabled: true
```

```toml
[micronaut]
  [micronaut.application]
    name="hello-world"
  [micronaut.config-client]
    enabled=true
[vault]
  [vault.client]
    uri="http://localhost:8200"
    [vault.client.config]
      enabled=true
```

```groovy
micronaut {
  application {
    name = "hello-world"
  }
  configClient {
    enabled = true
  }
}
vault {
  client {
    uri = "http://localhost:8200"
    config {
      enabled = true
    }
  }
}
```

```hocon
{
  micronaut {
    application {
      name = "hello-world"
    }
    config-client {
      enabled = true
    }
  }
  vault {
    client {
      uri = "http://localhost:8200"
      config {
        enabled = true
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "application": {
      "name": "hello-world"
    },
    "config-client": {
      "enabled": true
    }
  },
  "vault": {
    "client": {
      "uri": "http://localhost:8200",
      "config": {
        "enabled": true
      }
    }
  }
}
```

See the configuration reference for all configuration options.

The Micronaut framework uses the configured `micronaut.application.name` to lookup property sources for the application from Vault.

| Secret Path | Description |
|---|---|
| `/application` | Configuration shared by all applications |
| `/[APPLICATION_NAME]` | Application-specific configuration |
| `/application/[ENV_NAME]` | Configuration shared by all applications for an active environment name |
| `/[APPLICATION_NAME]/[ENV_NAME]` | Application-specific configuration for an active environment name |

See the Documentation for HashiCorp Vault for more information on how to set up the server.


## 10.1.4 Spring Cloud Config Support

Since 1.1, the Micronaut framework features a native Spring Cloud Configuration for those who have not switched to a dedicated more complete solution like Consul.

To enable distributed configuration make sure [bootstrap] is enabled and create a `src/main/resources/bootstrap.[yml/toml/properties]` file with the following configuration:

Integrating with Spring Cloud Configuration

```properties
micronaut.application.name=hello-world
micronaut.config-client.enabled=true
spring.cloud.config.enabled=true
spring.cloud.config.uri=http://localhost:8888/
spring.cloud.config.retry-attempts=4
spring.cloud.config.retry-delay=2s
```

```yaml
micronaut:
  application:
    name: hello-world
  config-client:
    enabled: true
spring:
  cloud:
    config:
      enabled: true
      uri: http://localhost:8888/
      retry-attempts: 4
      retry-delay: 2s
```

```toml
[micronaut]
  [micronaut.application]
    name="hello-world"
  [micronaut.config-client]
    enabled=true
[spring]
  [spring.cloud]
    [spring.cloud.config]
      enabled=true
      uri="http://localhost:8888/"
      retry-attempts=4
      retry-delay="2s"
```

```groovy
micronaut {
  application {
    name = "hello-world"
  }
  configClient {
    enabled = true
  }
}
spring {
  cloud {
    config {
      enabled = true
      uri = "http://localhost:8888/"
      retryAttempts = 4
      retryDelay = "2s"
    }
  }
}
```

```hocon
{
  micronaut {
    application {
      name = "hello-world"
    }
    config-client {
      enabled = true
    }
  }
  spring {
    cloud {
      config {
        enabled = true
        uri = "http://localhost:8888/"
        retry-attempts = 4
        retry-delay = "2s"
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "application": {
      "name": "hello-world"
    },
    "config-client": {
      "enabled": true
    }
  },
  "spring": {
    "cloud": {
      "config": {
        "enabled": true,
        "uri": "http://localhost:8888/",
        "retry-attempts": 4,
        "retry-delay": "2s"
      }
    }
  }
}
```

- `retry-attempts` is optional, and specifies the number of times to retry
- `retry-delay` is optional, and specifies the delay between retries

The Micronaut framework uses the configured `micronaut.application.name` to look up property sources for the application from Spring Cloud config server configured via `spring.cloud.config.uri`.

See the Documentation for Spring Cloud Config Server for more information on how to set up the server.


## 10.1.5 AWS Parameter Store Support

The Micronaut framework supports configuration sharing via AWS System Manager Parameter Store. You need the following dependencies configured:

`implementation("io.micronaut.aws:micronaut-aws-parameter-store")` `<dependency> <groupId>io.micronaut.aws</groupId> <artifactId>micronaut-aws-parameter-store</artifactId> </dependency>`

To enable distributed configuration, make sure [bootstrap] is enabled and create a `src/main/resources/bootstrap.yml` file with the following configuration:

```properties
micronaut.application.name=hello-world
micronaut.config-client.enabled=true
aws.client.system-manager.parameterstore.enabled=true
```

```yaml
micronaut:
  application:
    name: hello-world
  config-client:
    enabled: true
aws:
  client:
    system-manager:
      parameterstore:
        enabled: true
```

```toml
[micronaut]
  [micronaut.application]
    name="hello-world"
  [micronaut.config-client]
    enabled=true
[aws]
  [aws.client]
    [aws.client.system-manager]
      [aws.client.system-manager.parameterstore]
        enabled=true
```

```groovy
micronaut {
  application {
    name = "hello-world"
  }
  configClient {
    enabled = true
  }
}
aws {
  client {
    systemManager {
      parameterstore {
        enabled = true
      }
    }
  }
}
```

```hocon
{
  micronaut {
    application {
      name = "hello-world"
    }
    config-client {
      enabled = true
    }
  }
  aws {
    client {
      system-manager {
        parameterstore {
          enabled = true
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "application": {
      "name": "hello-world"
    },
    "config-client": {
      "enabled": true
    }
  },
  "aws": {
    "client": {
      "system-manager": {
        "parameterstore": {
          "enabled": true
        }
      }
    }
  }
}
```

See the configuration reference for all configuration options.

You can configure shared properties from the AWS Console → System Manager → Parameter Store.

The Micronaut framework uses a hierarchy to read configuration values, and supports `String`, `StringList`, and `SecureString` types.

You can create environment-specific configurations as well by including the environment name after an underscore `_`. For example if `micronaut.application.name` is set to `helloworld`, specifying configuration values under `helloworld_test` will be applied only to the `test` environment.

| Directory | Description |
|---|---|
| `/config/application` | Configuration shared by all applications |
| `/config/[APPLICATION_NAME]` | Application-specific configuration, example `/config/hello-world` |
| `/config/application_prod` | Configuration shared by all applications for the `prod` Environment |
| `/config/[APPLICATION_NAME]_prod` | Application-specific configuration for an active Environment |

For example, if the configuration name `/config/application_test/server.url` is configured in AWS Parameter Store, any application connecting to that parameter store can retrieve the value using `server.url`. If the application has `micronaut.application.name` configured to be `myapp`, a value with the name `/config/myapp_test/server.url` overrides the value just for that application.

Each level of the tree can be composed of key=value pairs. For multiple key/value pairs, set the type to `StringList`.

For special secure information, such as keys or passwords, use the type `SecureString`. KMS will be automatically invoked when you add and retrieve values, and will decrypt them with the default key store for your account. If you set the configuration to not use secure strings, they will be returned to you encrypted, and you must manually decrypt them.


## 10.1.6 Oracle Cloud Vault Support

See the Secure Distributed Configuration with Oracle Cloud Vault documentation.


## 10.1.7 Google Cloud Secret Manager Support

See the Micronaut GCP Distributed Configuration documentation.


## 10.1.8 Kubernetes Support

See the Kubernetes Configuration Client documentation.


## 10.2 Service Discovery

Service Discovery enables Microservices to find each other without knowing the physical location or IP address of associated services.

The Micronaut framework integrates with multiple tools and libraries. See Micronaut Service Discovery documentation for more details.


## 10.2.1 Consul Support

See the Micronaut Consul documentation.


## 10.2.2 Eureka Support

See the Micronaut Eureka documentation.


## 10.2.3 Kubernetes Support

Kubernetes is a container runtime with many features including integrated Service Discovery and Distributed Configuration.

The Micronaut framework includes first-class integration with Kubernetes. See the Micronaut Kubernetes documentation for more details.


## 10.2.4 AWS Route 53 Support

To use Route 53 Service Discovery, you must meet the following criteria:

- Run EC2 instances of some type
- Have a domain name hosted in Route 53
- Have a newer version of AWS-CLI (such as 14+)

Assuming you have those things, you are ready. It is not as fancy as Consul or Eureka, but other than some initial setup with the AWS-CLI, there is no other software running to go wrong. You can even support health checks if you add a custom health check to your service. To test if your account can create and use Service Discovery, see the Integration Test section. More information is available at https://docs.aws.amazon.com/Route53/latest/APIReference/overview-service-discovery.html.

Here are the steps:

1. Use AWS-CLI to create a namespace. You can make either a public or private one depending on the IPs or subnets you use
2. Create a service with DNS Records with AWS-CLI command
3. Add health checks or custom health checks (optional)
4. Add Service ID to your application configuration file like so:

Sample application configuration

```properties
aws.route53.registration.enabled=true
aws.route53.registration.aws-service-id=srv-978fs98fsdf
aws.route53.registration.namespace=micronaut.io
micronaut.application.name=something
```

```yaml
aws:
  route53:
    registration:
        enabled: true
        aws-service-id: srv-978fs98fsdf
        namespace: micronaut.io
micronaut:
  application:
    name: something
```

```toml
[aws]
  [aws.route53]
    [aws.route53.registration]
      enabled=true
      aws-service-id="srv-978fs98fsdf"
      namespace="micronaut.io"
[micronaut]
  [micronaut.application]
    name="something"
```

```groovy
aws {
  route53 {
    registration {
      enabled = true
      awsServiceId = "srv-978fs98fsdf"
      namespace = "micronaut.io"
    }
  }
}
micronaut {
  application {
    name = "something"
  }
}
```

```hocon
{
  aws {
    route53 {
      registration {
        enabled = true
        aws-service-id = "srv-978fs98fsdf"
        namespace = "micronaut.io"
      }
    }
  }
  micronaut {
    application {
      name = "something"
    }
  }
}
```

```json
{
  "aws": {
    "route53": {
      "registration": {
        "enabled": true,
        "aws-service-id": "srv-978fs98fsdf",
        "namespace": "micronaut.io"
      }
    }
  },
  "micronaut": {
    "application": {
      "name": "something"
    }
  }
}
```

1. Make sure you have the following dependencies in your build file:

`implementation("io.micronaut.aws:micronaut-aws-route53")` `<dependency> <groupId>io.micronaut.aws</groupId> <artifactId>micronaut-aws-route53</artifactId> </dependency>`

1. On the client side, you need the same dependencies and fewer configuration options:

```properties
aws.route53.discovery.client.enabled=true
aws.route53.discovery.client.aws-service-id=srv-978fs98fsdf
aws.route53.discovery.client.namespace-id=micronaut.io
```

```yaml
aws:
  route53:
    discovery:
      client:
        enabled: true
        aws-service-id: srv-978fs98fsdf
        namespace-id: micronaut.io
```

```toml
[aws]
  [aws.route53]
    [aws.route53.discovery]
      [aws.route53.discovery.client]
        enabled=true
        aws-service-id="srv-978fs98fsdf"
        namespace-id="micronaut.io"
```

```groovy
aws {
  route53 {
    discovery {
      client {
        enabled = true
        awsServiceId = "srv-978fs98fsdf"
        namespaceId = "micronaut.io"
      }
    }
  }
}
```

```hocon
{
  aws {
    route53 {
      discovery {
        client {
          enabled = true
          aws-service-id = "srv-978fs98fsdf"
          namespace-id = "micronaut.io"
        }
      }
    }
  }
}
```

```json
{
  "aws": {
    "route53": {
      "discovery": {
        "client": {
          "enabled": true,
          "aws-service-id": "srv-978fs98fsdf",
          "namespace-id": "micronaut.io"
        }
      }
    }
  }
}
```

You can then use the DiscoveryClient API to find other services registered via Route 53. For example:

Sample code for client

```java
DiscoveryClient discoveryClient = embeddedServer.getApplicationContext().getBean(DiscoveryClient.class);
List<String> serviceIds = Flux.from(discoveryClient.getServiceIds()).blockFirst();
List<ServiceInstance> instances = Flux.from(discoveryClient.getInstances(serviceIds.get(0))).blockFirst();
```

#### Creating the Namespace

Namespaces are similar to a regular Route53 hosted zone, and they appear in the Route53 console, but the console doesn’t support modifying them. You must use the AWS-CLI at this time for any Service Discovery functionality.

First decide if you are creating a public-facing namespace or a private one, as the commands are different:

Creating Namespace

```bash
$ aws servicediscovery create-public-dns-namespace --name micronaut.io --create-request-id create-1522767790 --description adescriptionhere

or

$ aws servicediscovery create-private-dns-namespace --name micronaut.internal.io --create-request-id create-1522767790 --description adescriptionhere --vpc yourvpcID
```

When you run this you will get an operation ID. You can check the status with the `get-operation` CLI command:

Get Operation Results

```bash
$ aws servicediscovery get-operation --operation-id asdffasdfsda
```

You can use this command to get the status of any call you make that returns an operation ID.

The result of the command will tell you the ID of the namespace. Write that down, you’ll need it for the next steps. If you get an error it will say what the error was.

#### Creating the Service and DNS Records

The next step is creating the Service and DNS records.

Create Service

```bash
$ aws create-service --name yourservicename --create-request-id somenumber --description someservicedescription --dns-config NamespaceId=yournamespaceid,RoutingPolicy=WEIGHTED,DnsRecords=[{Type=A,TTL=1000},{Type=A,TTL=1000}]
```

The `DnsRecord` type can be `A`(ipv4),`AAAA`(ipv6),`SRV`, or `CNAME`. `RoutingPolicy` can be `WEIGHTED` or `MULTIVALUE`. Keep in mind `CNAME` must use weighted routing type, `SRV` must have a valid port configured.

To add a health check, use the following syntax on the CLI:

Specifying a Health Check

```bash
Type=string,ResourcePath=string,FailureThreshold=integer
```

Type can be 'HTTP','HTTPS', or 'TCP'. You can only use a standard health check on a public namespace. See Custom Health Checks for private namespaces. Resource path should be a URL that returns `200 OK` if it is healthy.

For a custom health check, you only need to specify `--health-check-custom-config FailureThreshold=integer` which works on private namespaces as well.

This is also good because the Micronaut framework sends out pulsation commands to let AWS know the instance is still healthy.

For more help run 'aws discoveryservice create-service help'.

You will get a service ID and an ARN back from this command if successful. Write that down, it is going to go into the Micronaut configuration.

#### Setting up the configuration in Micronaut

#### Auto Naming Registration

Add the configuration to make your applications register with Route 53 Auto-discovery:

Registration Properties

```properties
aws.route53.registration.enabled=true
aws.route53.registration.aws-service-id=<enter the service id you got after creation on aws cli>
aws.route53.discovery.namespace-id=<enter the namespace id you got after creating the namespace>
```

```yaml
aws:
  route53:
    registration:
      enabled: true
      aws-service-id: <enter the service id you got after creation on aws cli>
    discovery:
      namespace-id: <enter the namespace id you got after creating the namespace>
```

```toml
[aws]
  [aws.route53]
    [aws.route53.registration]
      enabled=true
      aws-service-id="<enter the service id you got after creation on aws cli>"
    [aws.route53.discovery]
      namespace-id="<enter the namespace id you got after creating the namespace>"
```

```groovy
aws {
  route53 {
    registration {
      enabled = true
      awsServiceId = "<enter the service id you got after creation on aws cli>"
    }
    discovery {
      namespaceId = "<enter the namespace id you got after creating the namespace>"
    }
  }
}
```

```hocon
{
  aws {
    route53 {
      registration {
        enabled = true
        aws-service-id = "<enter the service id you got after creation on aws cli>"
      }
      discovery {
        namespace-id = "<enter the namespace id you got after creating the namespace>"
      }
    }
  }
}
```

```json
{
  "aws": {
    "route53": {
      "registration": {
        "enabled": true,
        "aws-service-id": "<enter the service id you got after creation on aws cli>"
      },
      "discovery": {
        "namespace-id": "<enter the namespace id you got after creating the namespace>"
      }
    }
  }
}
```

#### Discovery Client Configuration

Discovery Properties

```properties
aws.route53.discovery.client.enabled=true
aws.route53.discovery.client.aws-service-id=<enter the service id you got after creation on aws cli>
```

```yaml
aws:
  route53:
    discovery:
      client:
        enabled: true
        aws-service-id: <enter the service id you got after creation on aws cli>
```

```toml
[aws]
  [aws.route53]
    [aws.route53.discovery]
      [aws.route53.discovery.client]
        enabled=true
        aws-service-id="<enter the service id you got after creation on aws cli>"
```

```groovy
aws {
  route53 {
    discovery {
      client {
        enabled = true
        awsServiceId = "<enter the service id you got after creation on aws cli>"
      }
    }
  }
}
```

```hocon
{
  aws {
    route53 {
      discovery {
        client {
          enabled = true
          aws-service-id = "<enter the service id you got after creation on aws cli>"
        }
      }
    }
  }
}
```

```json
{
  "aws": {
    "route53": {
      "discovery": {
        "client": {
          "enabled": true,
          "aws-service-id": "<enter the service id you got after creation on aws cli>"
        }
      }
    }
  }
}
```

You can also call the following methods by getting the bean "Route53AutoNamingClient":

Discovery Methods

```java
// if serviceId is null it will use property "aws.route53.discovery.client.awsServiceId"
Publisher<List<ServiceInstance>> getInstances(String serviceId)
// reads property "aws.route53.discovery.namespaceId"
Publisher<List<String>> getServiceIds()
```

#### Integration Tests

If you set the environment variable AWS_SUBNET_ID and have credentials configured in your home directory that are valid (in `~/.aws/credentials`) you can run the integration tests. You need a domain hosted on Route53 as well. This test will create a t2.nano instance, a namespace, service, and register that instance to service discovery. When the test completes it will remove/terminate all resources it spun up.


## 10.2.5 Manual Service Discovery Configuration

If you do not wish to involve a service discovery server like Consul or you interact with a third-party service that cannot register with Consul you can instead manually configure services that are available via Service discovery.

To do this, use the `micronaut.http.services` setting. For example:

Manually configuring services

```properties
micronaut.http.services.foo.urls[0]=http://foo1
micronaut.http.services.foo.urls[1]=http://foo2
```

```yaml
micronaut:
  http:
    services:
      foo:
        urls:
          - http://foo1
          - http://foo2
```

```toml
[micronaut]
  [micronaut.http]
    [micronaut.http.services]
      [micronaut.http.services.foo]
        urls=[
          "http://foo1",
          "http://foo2"
        ]
```

```groovy
micronaut {
  http {
    services {
      foo {
        urls = ["http://foo1", "http://foo2"]
      }
    }
  }
}
```

```hocon
{
  micronaut {
    http {
      services {
        foo {
          urls = ["http://foo1", "http://foo2"]
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "http": {
      "services": {
        "foo": {
          "urls": ["http://foo1", "http://foo2"]
        }
      }
    }
  }
}
```

You can then inject a client with `@Client("foo")`, and it will use the above configuration to load balance between the two configured servers.

|   | When using `@Client` with service discovery, the service id must be specified in the annotation in kebab-case. The configuration in the example above however can be in camel case. |
|---|---|

|   | You can override this configuration in production by specifying an environment variable such as `MICRONAUT_HTTP_SERVICES_FOO_URLS=http://prod1,http://prod2` |
|---|---|

Note that by default no health checking will happen to assert that the referenced services are operational. You can alter that by enabling health checking and optionally specifying a health check path (the default is `/health`):

Enabling Health Checking

```properties
micronaut.http.services.foo.health-check=true
micronaut.http.services.foo.health-check-interval=15s
micronaut.http.services.foo.health-check-uri=/health
```

```yaml
micronaut:
  http:
    services:
      foo:
        health-check: true
        health-check-interval: 15s
        health-check-uri: /health
```

```toml
[micronaut]
  [micronaut.http]
    [micronaut.http.services]
      [micronaut.http.services.foo]
        health-check=true
        health-check-interval="15s"
        health-check-uri="/health"
```

```groovy
micronaut {
  http {
    services {
      foo {
        healthCheck = true
        healthCheckInterval = "15s"
        healthCheckUri = "/health"
      }
    }
  }
}
```

```hocon
{
  micronaut {
    http {
      services {
        foo {
          health-check = true
          health-check-interval = "15s"
          health-check-uri = "/health"
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "http": {
      "services": {
        "foo": {
          "health-check": true,
          "health-check-interval": "15s",
          "health-check-uri": "/health"
        }
      }
    }
  }
}
```

- `health-check` indicates whether to health check the service
- `health-check-interval` is the interval between checks
- `health-check-uri` specifies the endpoint URI of the health check request

The Micronaut framework starts a background thread to check the health status of the service and if any of the configured services respond with an error code, they are removed from the list of available services.


## 10.3 Client Side Load Balancing

When discovering services from Consul, Eureka, or other Service Discovery servers, the DiscoveryClient emits a list of available ServiceInstance.

The Micronaut framework by default automatically performs Round Robin client-side load balancing using the servers in this list. This combined with Retry Advice adds extra resiliency to your Microservice infrastructure.

The load balancing is handled by the LoadBalancer interface, which has a LoadBalancer.select() method that returns a `Publisher` which emits a ServiceInstance.

The Publisher is returned because the process for selecting a ServiceInstance may result in a network operation depending on the Service Discovery strategy employed.

The default implementation of the LoadBalancer interface is DiscoveryClientRoundRobinLoadBalancer. You can replace this strategy with another implementation to customize how client side load balancing is handled in Micronaut, since there are many different ways to optimize load balancing.

For example, you may wish to load balance between services in a particular zone, or to load balance between servers that have the best overall response time.

To replace the LoadBalancer, define a bean that replaces the DiscoveryClientLoadBalancerFactory.

In fact that is exactly what the Netflix Ribbon support does, described in the next section.


## 10.3.1 Netflix Ribbon Support

|   | Using the CLI If you create your project using the Micronaut CLI, supply the `netflix-ribbon` feature to configure Netflix Ribbon in your project: $ mn create-app my-app --features netflix-ribbon |
|---|---|

Netflix Ribbon is an inter-process communication library used at Netflix with support for customizable load balancing strategies.

If you need more flexibility in how your application performs client-side load balancing, you can use Micronaut’s Netflix Ribbon support.

To add Ribbon support to your application, add the `netflix-ribbon` configuration to your build:

`implementation("io.micronaut.netflix:micronaut-netflix-ribbon")` `<dependency> <groupId>io.micronaut.netflix</groupId> <artifactId>micronaut-netflix-ribbon</artifactId> </dependency>`

The LoadBalancer implementations will now be RibbonLoadBalancer instances.

Ribbon’s Configuration options can be set using the `ribbon` namespace in configuration. For example in your configuration file (e.g `application.yml`):

Configuring Ribbon

```properties
ribbon.VipAddress=test
ribbon.ServerListRefreshInterval=2000
```

```yaml
ribbon:
  VipAddress: test
  ServerListRefreshInterval: 2000
```

```toml
[ribbon]
  VipAddress="test"
  ServerListRefreshInterval=2000
```

```groovy
ribbon {
  VipAddress = "test"
  ServerListRefreshInterval = 2000
}
```

```hocon
{
  ribbon {
    VipAddress = "test"
    ServerListRefreshInterval = 2000
  }
}
```

```json
{
  "ribbon": {
    "VipAddress": "test",
    "ServerListRefreshInterval": 2000
  }
}
```

Each discovered client can also be configured under `ribbon.clients`. For example given a `@Client(id = "hello-world")` you can configure Ribbon settings with:

Per Client Ribbon Settings

```properties
ribbon.clients.hello-world.VipAddress=test
ribbon.clients.hello-world.ServerListRefreshInterval=2000
```

```yaml
ribbon:
  clients:
    hello-world:
      VipAddress: test
      ServerListRefreshInterval: 2000
```

```toml
[ribbon]
  [ribbon.clients]
    [ribbon.clients.hello-world]
      VipAddress="test"
      ServerListRefreshInterval=2000
```

```groovy
ribbon {
  clients {
    helloWorld {
      VipAddress = "test"
      ServerListRefreshInterval = 2000
    }
  }
}
```

```hocon
{
  ribbon {
    clients {
      hello-world {
        VipAddress = "test"
        ServerListRefreshInterval = 2000
      }
    }
  }
}
```

```json
{
  "ribbon": {
    "clients": {
      "hello-world": {
        "VipAddress": "test",
        "ServerListRefreshInterval": 2000
      }
    }
  }
}
```

By default, the Micronaut framework registers a DiscoveryClientServerList for each client that integrates Ribbon with the Micronaut framework’s DiscoveryClient.


## 10.4 Distributed Tracing

See the documentation for Micronaut Tracing for more information adding distributed tracing to your applications.

# 11 Serverless Functions

Serverless architectures, where you deploy functions that are fully managed by a Cloud environment and are executed in ephemeral processes, require a unique approach.

Traditional frameworks like Grails and Spring are not really suitable since low memory consumption and fast startup time are critical, since the Function as a Service (FaaS) server typically spins up your function for a period using a cold start and then keeps it warm.

Micronaut’s compile-time approach, fast startup time, and low memory footprint make it a great candidate for developing functions, and the Micronaut framework includes dedicated support for developing and deploying functions to AWS Lambda, Google Cloud Function, Azure Function, and any FaaS system that supports running functions as containers (such as OpenFaaS, Rift or Fn).

There are generally two approaches to writing functions with Micronaut:

1. Low-level functions written using the native API of the function platform
2. Higher-level functions where you simply define controllers as you normally do in a typical Micronaut application and deploy to the function platform.

The first has marginally less startup time overhead and is typically used for non-HTTP functions such as functions that listen to an event or background functions.

The second is only for HTTP functions and is useful for users who want to take a slice of an existing application and deploy it as a serverless function. If cold start performance is a concern it is recommended that you consider building a native image with GraalVM for this option.


## 11.1 AWS Lambda

Support for AWS Lambda is implemented in the Micronaut AWS subproject.

#### Simple Functions with AWS Lambda

You can implement AWS Request Handlers with the Micronaut framework that directly implement the AWS Lambda SDK API. See the documentation on Micronaut Request Handlers for more information.

|   | Using the CLI To create an AWS Lambda Function: $ mn create-function-app my-app --features aws-lambda Or with Micronaut Launch $ curl https://launch.micronaut.io/create/function/example\?features\=aws-lambda -o example.zip $ unzip example.zip -d example |
|---|---|

#### HTTP Functions with AWS Lambda

You can deploy regular Micronaut applications that use @Controller, etc. using Micronaut’s support for AWS API Gateway. See the documentation on AWS Application Types, Lambda Runtimes, Dependencies for more information.

|   | Using the CLI To create an AWS API Gateway Proxy application: $ mn create-app my-app --features aws-lambda Or with Micronaut Launch $ curl https://launch.micronaut.io/example.zip\?features\=aws-lambda -o example.zip $ unzip example.zip -d example |
|---|---|


## 11.2 Google Cloud Function

Support for Google Cloud Function is implemented in the Micronaut GCP subproject.

#### Simple Functions with Cloud Function

You can implement Cloud Functions with the Micronaut framework that directly implement the Cloud Function Framework API. See the documentation on Simple Functions for more information.

|   | Using the CLI To create a Google Cloud Function: $ mn create-function-app my-app --features google-cloud-function Or with Micronaut Launch $ curl https://launch.micronaut.io/create/function/example\?features\=google-cloud-function -o example.zip $ unzip example.zip -d example |
|---|---|

#### HTTP Functions with Cloud Function

You can deploy regular Micronaut applications that use @Controller etc. using Micronaut’s support for HTTP Functions. See the documentation on Google Cloud HTTP Functions for more information.

|   | Using the CLI To create a Google Cloud HTTP Function: $ mn create-app my-app --features google-cloud-function Or with Micronaut Launch $ curl https://launch.micronaut.io/example.zip\?features\=google-cloud-function -o example.zip $ unzip example.zip -d example |
|---|---|
