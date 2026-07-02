---
title: "Micronaut Core (part 17/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 17/27
---

## systemd socket activation support

The HTTP server can be configured to use an existing file descriptor. With this feature, you can use socket created by systemd and passed to the micronaut process:

```properties
micronaut.netty.event-loops.parent.transport=epoll
micronaut.netty.event-loops.default.transport=epoll
micronaut.netty.listeners.systemd.fd=3
micronaut.netty.listeners.systemd.bind=false
```

```yaml
micronaut:
  netty:
    event-loops:
      # use epoll transport
      parent:
        transport: epoll
      default:
        transport: epoll
    listeners:
      systemd:
        fd: 3 # systemd passes the server socket as fd 3
        bind: false # do not bind again, systemd already did this
```

```toml
[micronaut]
  [micronaut.netty]
    [micronaut.netty.event-loops]
      [micronaut.netty.event-loops.parent]
        transport="epoll"
      [micronaut.netty.event-loops.default]
        transport="epoll"
    [micronaut.netty.listeners]
      [micronaut.netty.listeners.systemd]
        fd=3
        bind=false
```

```groovy
micronaut {
  netty {
    eventLoops {
      parent {
        transport = "epoll"
      }
      'default' {
        transport = "epoll"
      }
    }
    listeners {
      systemd {
        fd = 3
        bind = false
      }
    }
  }
}
```

```hocon
{
  micronaut {
    netty {
      event-loops {
        parent {
          transport = "epoll"
        }
        default {
          transport = "epoll"
        }
      }
      listeners {
        systemd {
          fd = 3
          bind = false
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "netty": {
      "event-loops": {
        "parent": {
          "transport": "epoll"
        },
        "default": {
          "transport": "epoll"
        }
      },
      "listeners": {
        "systemd": {
          "fd": 3,
          "bind": false
        }
      }
    }
  }
}
```

Example `app.service` file:

```
[Unit]
Description=Micronaut HTTP server with socket activation
After=network.target app.socket
Requires=app.socket

[Service]
Type=simple
ExecStart=/usr/bin/java -jar /app.jar
```

Example `app.socket` file:

```
[Socket]
ListenStream=127.0.0.1:8080

[Install]
WantedBy=sockets.target
```

Now your Micronaut application can be started by a client connecting to `http://127.0.0.1:8080`.

|   | The nio transport only supports `fd: 0` ("inetd style"), through the JDK `System.inheritedChannel()` API. If you wish to use the default `fd: 3` recommended by systemd, you must use the epoll transport. |
|---|---|

### inetd-style socket activation

systemd also supports inetd-style socket activation. In that mode, instead of passing a listening socket fd (`ServerSocketChannel`), systemd will pass an already accepted fd (`SocketChannel`) representing an individual TCP connection. systemd will start a new instance of the service for each new TCP connection.

The Micronaut HTTP server supports this mode through the `accepted-fd` config option. An `accepted-fd` will be registered with the listener it is declared on, and essentially treated like a connection that was accepted by the listener. The netty parent channel will be set to the listener server socket, which is important to avoid a netty bug in connection with HTTP/2.

|   | Epoll does not support setting the parent channel, so HTTP/2 may not work with `accepted-fd` and epoll. |
|---|---|

```properties
micronaut.netty.listeners.systemd.accepted-fd=0
micronaut.netty.listeners.systemd.bind=false
```

```yaml
micronaut:
  netty:
    listeners:
      systemd:
        accepted-fd: 0 # inetd-style socket activation typically uses fd 0 (stdin)
        bind: false # do not bind, we only use the server channel as the parent
```

```toml
[micronaut]
  [micronaut.netty]
    [micronaut.netty.listeners]
      [micronaut.netty.listeners.systemd]
        accepted-fd=0
        bind=false
```

```groovy
micronaut {
  netty {
    listeners {
      systemd {
        acceptedFd = 0
        bind = false
      }
    }
  }
}
```

```hocon
{
  micronaut {
    netty {
      listeners {
        systemd {
          accepted-fd = 0
          bind = false
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "netty": {
      "listeners": {
        "systemd": {
          "accepted-fd": 0,
          "bind": false
        }
      }
    }
  }
}
```

By setting `server-socket: false`, you can disable the parent channel entirely. This may save some slight startup time, but may cause problems with HTTP/2.

|   | Because inetd-style socket activation typically uses fd 0, it hijacks stdin and stdout. You must take care to never emit any output on stdout, as this may corrupt the HTTP response, or even show up for the user. In particular, you must configure logback to log to `System.err` instead, and disable the Micronaut startup banner. |
|---|---|


## 6.33.5 Configuring CORS

The Micronaut framework supports CORS (Cross Origin Resource Sharing) out of the box. By default, CORS requests are rejected.

|   | See the guide for Configure CORS in a Micronaut Application to learn more. |
|---|---|


## 6.33.5.1 Annotation-based CORS Configuration

Micronaut CORS configuration applies by default to all endpoints in the running application.

As an alternative, CORS configuration can be applied in a more fine-grained manner to specific routes using the @CrossOrigin annotation. This is applied to `@Controller` to apply the CORS configuration to all endpoints in the controller. Alternatively, the annotation can be applied to specific endpoints on a controller, for even more fine-grained control.

The `@CrossOrigin` annotation maps with a one-to-one correspondence to application-wide CorsOriginConfiguration configuration properties. To specify just an allowed origin, use `@CrossOrigin("https://foo.com")`. To specify additional configuration details, use a combination of annotation attributes the same as you would for specifying global `CorsOriginConfiguration` properties.

```java
@CrossOrigin(
	allowedOrigins = { "http://foo.com" },
	allowedOriginsRegex = "^http(|s):\\/\\/www\\.google\\.com$",
	allowedMethods = { HttpMethod.POST, HttpMethod.PUT },
	allowedHeaders = { HttpHeaders.CONTENT_TYPE, HttpHeaders.AUTHORIZATION },
	exposedHeaders = { HttpHeaders.CONTENT_TYPE, HttpHeaders.AUTHORIZATION },
	allowCredentials = false,
	allowPrivateNetwork = false,
	maxAge = 3600
)
```

The following example demonstrates how the annotation might be applied to a specific endpoint. To enable CORS for all endpoints in the controller, move the annotation to the class level and configure it appropriately.

@CrossOrigin Example

```java
import io.micronaut.context.annotation.Requires;
import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.Produces;
import io.micronaut.http.server.cors.CrossOrigin;

@Controller("/hello")
public class CorsController {
    @CrossOrigin("https://myui.com") // (1)
    @Get(produces = MediaType.TEXT_PLAIN) // (2)
    public String cors() {
        return "Welcome to the worlds of CORS";
    }

    @Produces(MediaType.TEXT_PLAIN)
    @Get("/nocors") // (3)
    public String nocorstoday() {
        return "No more CORS for you";
    }
}
```

@CrossOrigin Example

```groovy
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.annotation.Produces
import io.micronaut.http.server.cors.CrossOrigin

@Controller("/hello")
class CorsController {
    @CrossOrigin("https://myui.com") // (1)
    @Get(produces = MediaType.TEXT_PLAIN) // (2)
    String cors() {
        return "Welcome to the worlds of CORS"
    }

    @Produces(MediaType.TEXT_PLAIN)
    @Get("/nocors") // (3)
    String nocorstoday() {
        return "No more CORS for you"
    }
}
```

| **1** | The @CrossOrigin annotation is applied to a specific endpoint, making the CORS configuration fine-grained. |
|---|---|
| **2** | The `GET /hello` endpoint has "https://myui.com" as an allowed cross-origin endpoint |
| **3** | The `GET /hello/nocors` endpoint cannot use "https://myui.com" as an origin, since it doesn’t have a CORS configuration that allows it. |

|   | The `@CrossOrigin` annotation uses the same defaults as the application configuration alternative, when corresponding annotation attributes are not set. See CORS configuration for details. |
|---|---|


## 6.33.5.2 CORS via Configuration

To enable processing of CORS requests, modify your configuration in the application configuration file:

CORS Configuration Example

```properties
micronaut.server.cors.enabled=true
```

```yaml
micronaut:
  server:
    cors:
      enabled: true
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.cors]
      enabled=true
```

```groovy
micronaut {
  server {
    cors {
      enabled = true
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      cors {
        enabled = true
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "cors": {
        "enabled": true
      }
    }
  }
}
```

By only enabling CORS processing, a "wide open" strategy is adopted that allows requests from any origin.

To change the settings for all origins or a specific origin, change the configuration to provide one or more "configurations". By providing any configuration, the default "wide open" configuration is not configured.

CORS Configurations

```properties
micronaut.server.cors.enabled=true
micronaut.server.cors.configurations.all=...
micronaut.server.cors.configurations.web=...
micronaut.server.cors.configurations.mobile=...
```

```yaml
micronaut:
  server:
    cors:
      enabled: true
      configurations:
        all:
          ...
        web:
          ...
        mobile:
          ...
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.cors]
      enabled=true
      [micronaut.server.cors.configurations]
        all="..."
        web="..."
        mobile="..."
```

```groovy
micronaut {
  server {
    cors {
      enabled = true
      configurations {
        all = "..."
        web = "..."
        mobile = "..."
      }
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      cors {
        enabled = true
        configurations {
          all = "..."
          web = "..."
          mobile = "..."
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "cors": {
        "enabled": true,
        "configurations": {
          "all": "...",
          "web": "...",
          "mobile": "..."
        }
      }
    }
  }
}
```

In the above example, three configurations are provided. Their names (`all`, `web`, `mobile`) are not important and have no significance inside Micronaut. They are there purely to be able to easily recognize the intended user of the configuration.

The same configuration properties can be applied to each configuration. See CorsOriginConfiguration for properties that can be defined. The values of each configuration supplied will default to the default values of the corresponding fields.

When a CORS request is made, configurations are searched for allowed origins that match exactly or match the request origin through a regular expression.


## 6.33.5.3 Allowed Origins

Don’t define `allowed-origins` or `allowed-origins-regex` to allow any origin for a given configuration.

For multiple valid origins, set the `allowed-origins` key of the configuration to a list of strings.

You can also define via `allowed-origins-regex` a regular expression (`^http(|s)://www\.google\.com$`). The Regular expression is passed to Pattern#compile and compared to the request origin with Matcher#matches.

Example CORS Configuration

```properties
micronaut.server.cors.enabled=true
micronaut.server.cors.configurations.web.allowed-origins-regex=^http(|s):\/\/www\.google\.com$
micronaut.server.cors.configurations.web.allowed-origins[0]=http://foo.com
```

```yaml
micronaut:
  server:
    cors:
      enabled: true
      configurations:
        web:
          allowed-origins-regex: '^http(|s):\/\/www\.google\.com$'
          allowed-origins:
            - http://foo.com
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.cors]
      enabled=true
      [micronaut.server.cors.configurations]
        [micronaut.server.cors.configurations.web]
          allowed-origins-regex="^http(|s):\\/\\/www\\.google\\.com$"
          allowed-origins=[
            "http://foo.com"
          ]
```

```groovy
micronaut {
  server {
    cors {
      enabled = true
      configurations {
        web {
          allowedOriginsRegex = "^http(|s):\\/\\/www\\.google\\.com$"
          allowedOrigins = ["http://foo.com"]
        }
      }
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      cors {
        enabled = true
        configurations {
          web {
            allowed-origins-regex = "^http(|s):\\/\\/www\\.google\\.com$"
            allowed-origins = ["http://foo.com"]
          }
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "cors": {
        "enabled": true,
        "configurations": {
          "web": {
            "allowed-origins-regex": "^http(|s):\\/\\/www\\.google\\.com$",
            "allowed-origins": ["http://foo.com"]
          }
        }
      }
    }
  }
}
```

|   | Use the `allowed-origins-regex` configuration judiciously. You may accidentally make an insecure configuration which could be targeted by an attacker registering domains targeting the regular expression. |
|---|---|

|   | `allowed-origins-regex` and `allowed-origins` can be combined. However, if using the former and the latter is not set explicitly then `allowed-origins` defaults to *none* rather than *any* to avoid unexpected allowed origins. |
|---|---|


## 6.33.5.4 Allowed Methods

To allow any request method for a given configuration, don’t include the `allowed-methods` key in your configuration.

For multiple allowed methods, set the `allowed-methods` key of the configuration to a list of strings.

Example CORS Configuration

```properties
micronaut.server.cors.enabled=true
micronaut.server.cors.configurations.web.allowed-methods[0]=POST
micronaut.server.cors.configurations.web.allowed-methods[1]=PUT
```

```yaml
micronaut:
  server:
    cors:
      enabled: true
      configurations:
        web:
          allowed-methods:
            - POST
            - PUT
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.cors]
      enabled=true
      [micronaut.server.cors.configurations]
        [micronaut.server.cors.configurations.web]
          allowed-methods=[
            "POST",
            "PUT"
          ]
```

```groovy
micronaut {
  server {
    cors {
      enabled = true
      configurations {
        web {
          allowedMethods = ["POST", "PUT"]
        }
      }
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      cors {
        enabled = true
        configurations {
          web {
            allowed-methods = ["POST", "PUT"]
          }
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "cors": {
        "enabled": true,
        "configurations": {
          "web": {
            "allowed-methods": ["POST", "PUT"]
          }
        }
      }
    }
  }
}
```


## 6.33.5.5 Allowed Headers

To allow any request header for a given configuration, don’t include the `allowed-headers` key in your configuration.

For multiple allowed headers, set the `allowed-headers` key of the configuration to a list of strings.

Example CORS Configuration

```properties
micronaut.server.cors.enabled=true
micronaut.server.cors.configurations.web.allowed-headers[0]=Content-Type
micronaut.server.cors.configurations.web.allowed-headers[1]=Authorization
```

```yaml
micronaut:
  server:
    cors:
      enabled: true
      configurations:
        web:
          allowed-headers:
            - Content-Type
            - Authorization
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.cors]
      enabled=true
      [micronaut.server.cors.configurations]
        [micronaut.server.cors.configurations.web]
          allowed-headers=[
            "Content-Type",
            "Authorization"
          ]
```

```groovy
micronaut {
  server {
    cors {
      enabled = true
      configurations {
        web {
          allowedHeaders = ["Content-Type", "Authorization"]
        }
      }
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      cors {
        enabled = true
        configurations {
          web {
            allowed-headers = ["Content-Type", "Authorization"]
          }
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "cors": {
        "enabled": true,
        "configurations": {
          "web": {
            "allowed-headers": ["Content-Type", "Authorization"]
          }
        }
      }
    }
  }
}
```


## 6.33.5.6 Exposed Headers

To configure the headers that are sent in the response to a CORS request through the `Access-Control-Expose-Headers` header, include a list of strings for the `exposed-headers` key in your configuration. None are exposed by default.

Example CORS Configuration

```properties
micronaut.server.cors.enabled=true
micronaut.server.cors.configurations.web.exposed-headers[0]=Content-Type
micronaut.server.cors.configurations.web.exposed-headers[1]=Authorization
```

```yaml
micronaut:
  server:
    cors:
      enabled: true
      configurations:
        web:
          exposed-headers:
            - Content-Type
            - Authorization
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.cors]
      enabled=true
      [micronaut.server.cors.configurations]
        [micronaut.server.cors.configurations.web]
          exposed-headers=[
            "Content-Type",
            "Authorization"
          ]
```

```groovy
micronaut {
  server {
    cors {
      enabled = true
      configurations {
        web {
          exposedHeaders = ["Content-Type", "Authorization"]
        }
      }
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      cors {
        enabled = true
        configurations {
          web {
            exposed-headers = ["Content-Type", "Authorization"]
          }
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "cors": {
        "enabled": true,
        "configurations": {
          "web": {
            "exposed-headers": ["Content-Type", "Authorization"]
          }
        }
      }
    }
  }
}
```


## 6.33.5.7 Allow Credentials

Credentials are disabled by default for CORS requests. To allow credentials, set the `allow-credentials` option to `true`.

Example CORS Configuration

```properties
micronaut.server.cors.enabled=true
micronaut.server.cors.configurations.web.allow-credentials=true
```

```yaml
micronaut:
  server:
    cors:
      enabled: true
      configurations:
        web:
          allow-credentials: true
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.cors]
      enabled=true
      [micronaut.server.cors.configurations]
        [micronaut.server.cors.configurations.web]
          allow-credentials=true
```

```groovy
micronaut {
  server {
    cors {
      enabled = true
      configurations {
        web {
          allowCredentials = true
        }
      }
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      cors {
        enabled = true
        configurations {
          web {
            allow-credentials = true
          }
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "cors": {
        "enabled": true,
        "configurations": {
          "web": {
            "allow-credentials": true
          }
        }
      }
    }
  }
}
```


## 6.33.5.8 Allow Private Network

Access from private network is allowed by default for CORS requests. To disallow acces from local network, set the `allow-private-network` option to `false`.

Example CORS Configuration

```properties
micronaut.server.cors.enabled=true
micronaut.server.cors.configurations.web.allow-private-network=false
```

```yaml
micronaut:
  server:
    cors:
      enabled: true
      configurations:
        web:
          allow-private-network: false
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.cors]
      enabled=true
      [micronaut.server.cors.configurations]
        [micronaut.server.cors.configurations.web]
          allow-private-network=false
```

```groovy
micronaut {
  server {
    cors {
      enabled = true
      configurations {
        web {
          allowPrivateNetwork = false
        }
      }
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      cors {
        enabled = true
        configurations {
          web {
            allow-private-network = false
          }
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "cors": {
        "enabled": true,
        "configurations": {
          "web": {
            "allow-private-network": false
          }
        }
      }
    }
  }
}
```


## 6.33.5.9 Max Age

The default maximum age that preflight requests can be cached is 30 minutes. To change that behavior, specify a value in seconds.

Example CORS Configuration

```properties
micronaut.server.cors.enabled=true
micronaut.server.cors.configurations.web.max-age=3600
```

```yaml
micronaut:
  server:
    cors:
      enabled: true
      configurations:
        web:
          max-age: 3600 # 1 hour
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.cors]
      enabled=true
      [micronaut.server.cors.configurations]
        [micronaut.server.cors.configurations.web]
          max-age=3600
```

```groovy
micronaut {
  server {
    cors {
      enabled = true
      configurations {
        web {
          maxAge = 3600
        }
      }
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      cors {
        enabled = true
        configurations {
          web {
            max-age = 3600
          }
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "cors": {
        "enabled": true,
        "configurations": {
          "web": {
            "max-age": 3600
          }
        }
      }
    }
  }
}
```


## 6.33.5.10 Multiple Header Values

By default, when a header has multiple values, multiple headers are sent, each with a single value. It is possible to change the behavior to send a single header with a comma-separated list of values by setting a configuration option.

```properties
micronaut.server.cors.single-header=true
```

```yaml
micronaut:
  server:
    cors:
      single-header: true
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.cors]
      single-header=true
```

```groovy
micronaut {
  server {
    cors {
      singleHeader = true
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      cors {
        single-header = true
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "cors": {
        "single-header": true
      }
    }
  }
}
```


## 6.33.6 Securing the Server with HTTPS

The Micronaut framework supports HTTPS out of the box. By default, HTTPS is disabled and all requests are served using HTTP. To enable HTTPS support, define TLS material using named certificate providers and reference them from your SSL configuration. See Certificate providers for details.

HTTPS Configuration Example (self-signed for development)

```properties
micronaut.server.ssl.enabled=true
micronaut.server.ssl.key-name=cert-a
micronaut.certificate.self-signed.cert-a=
```

```yaml
micronaut:
  server:
    ssl:
      enabled: true
      # Reference the named provider below
      key-name: cert-a

  certificate:
    self-signed:
      # Declare a self-signed provider named "cert-a"
      cert-a: ""
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.ssl]
      enabled=true
      key-name="cert-a"
  [micronaut.certificate]
    [micronaut.certificate.self-signed]
      cert-a=""
```

```groovy
micronaut {
  server {
    ssl {
      enabled = true
      keyName = "cert-a"
    }
  }
  certificate {
    selfSigned {
      certA = ""
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      ssl {
        enabled = true
        key-name = "cert-a"
      }
    }
    certificate {
      self-signed {
        cert-a = ""
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "ssl": {
        "enabled": true,
        "key-name": "cert-a"
      }
    },
    "certificate": {
      "self-signed": {
        "cert-a": ""
      }
    }
  }
}
```

- The Micronaut framework will create a self-signed certificate.

|   | By default, a Micronaut application with HTTPS support starts on port `8443` but you can change the port with the property `micronaut.server.ssl.port`. |
|---|---|

For generating self-signed certificates, the Micronaut HTTP server will use netty-pkitesting, which requires this dependency:

`runtimeOnly("io.netty:netty-pkitesting")` `<dependency> <groupId>io.netty</groupId> <artifactId>netty-pkitesting</artifactId> <scope>runtime</scope> </dependency>`

|   | This configuration will generate a warning in the browser. |
|---|---|


## Using a valid X.509 certificate (PEM)

It is also possible to configure a Micronaut application to use an existing valid x509 certificate, for example one created with Let’s Encrypt. You will need the `server.crt` and `server.key` files.

HTTPS Configuration Example

```properties
micronaut.server.ssl.enabled=true
micronaut.server.ssl.key-name=cert-a
micronaut.certificate.file.cert-a.format=pem
micronaut.certificate.file.cert-a.path=server.key
micronaut.certificate.file.cert-a.certificate-path=server.crt
```

```yaml
micronaut:
  server:
    ssl:
      enabled: true
      key-name: cert-a

  certificate:
    file:
      cert-a:
        format: pem
        path: server.key
        certificate-path: server.crt
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.ssl]
      enabled=true
      key-name="cert-a"
  [micronaut.certificate]
    [micronaut.certificate.file]
      [micronaut.certificate.file.cert-a]
        format="pem"
        path="server.key"
        certificate-path="server.crt"
```

```groovy
micronaut {
  server {
    ssl {
      enabled = true
      keyName = "cert-a"
    }
  }
  certificate {
    file {
      certA {
        format = "pem"
        path = "server.key"
        certificatePath = "server.crt"
      }
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      ssl {
        enabled = true
        key-name = "cert-a"
      }
    }
    certificate {
      file {
        cert-a {
          format = "pem"
          path = "server.key"
          certificate-path = "server.crt"
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "ssl": {
        "enabled": true,
        "key-name": "cert-a"
      }
    },
    "certificate": {
      "file": {
        "cert-a": {
          "format": "pem",
          "path": "server.key",
          "certificate-path": "server.crt"
        }
      }
    }
  }
}
```

With this configuration, if we start a Micronaut application and connect to `https://localhost:8443` we still see the warning in the browser, but if we inspect the certificate we can check that it is the one generated by Let’s Encrypt.

Finally, we can test that the certificate is valid for the browser by adding an alias to the domain in `/etc/hosts` file:

```bash
$ cat /etc/hosts
...
127.0.0.1   my-domain.org
...
```

Now we can connect to `https://my-domain.org:8443`:


## Using a PKCS#12 key store

The more traditional approach to managing certificates in Java is with a key store, either in PKCS#12 or the older JKS format. You can convert your PEM files to PKCS#12 as follows:

```bash
$ openssl pkcs12 -export \
                 -in server.crt \ (1)
                 -inkey server.key \ (2)
                 -out server.p12 \ (3)
                 -name someAlias \ (4)
                 -chain -CAfile ca.crt -caname root
```

| **1** | The original `server.crt` file |
|---|---|
| **2** | The original `server.key` file |
| **3** | The `server.p12` file to create |
| **4** | The alias for the certificate |

Reference the PKCS#12 in a provider and point SSL to it:

HTTPS Configuration Example

```properties
micronaut.server.ssl.enabled=true
micronaut.server.ssl.key-name=cert-a
micronaut.certificate.resource.cert-a.resource=classpath:server.p12
micronaut.certificate.resource.cert-a.password=mypassword
```

```yaml
micronaut:
  server:
    ssl:
      enabled: true
      key-name: cert-a

  certificate:
    resource:
      cert-a:
        resource: classpath:server.p12
        password: mypassword
        # format: pkcs12  # optional, auto-detected
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.ssl]
      enabled=true
      key-name="cert-a"
  [micronaut.certificate]
    [micronaut.certificate.resource]
      [micronaut.certificate.resource.cert-a]
        resource="classpath:server.p12"
        password="mypassword"
```

```groovy
micronaut {
  server {
    ssl {
      enabled = true
      keyName = "cert-a"
    }
  }
  certificate {
    resource {
      certA {
        resource = "classpath:server.p12"
        password = "mypassword"
      }
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      ssl {
        enabled = true
        key-name = "cert-a"
      }
    }
    certificate {
      resource {
        cert-a {
          resource = "classpath:server.p12"
          password = "mypassword"
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "ssl": {
        "enabled": true,
        "key-name": "cert-a"
      }
    },
    "certificate": {
      "resource": {
        "cert-a": {
          "resource": "classpath:server.p12",
          "password": "mypassword"
        }
      }
    }
  }
}
```

- Specify the `p12` file path
- Also provide the `password` defined during the export


## Using a JKS key store

You can optionally convert the `p12` store to a JKS one:

```bash
$ keytool -importkeystore \
          -deststorepass newPassword -destkeypass newPassword \ (1)
          -destkeystore server.keystore \ (2)
          -srckeystore server.p12 -srcstoretype PKCS12 -srcstorepass mypassword \ (3)
          -alias someAlias (4)
```

| **1** | It is necessary to define the password for the keystore |
|---|---|
| **2** | The file to create |
| **3** | The PKCS12 file created previously, and the password defined during the creation |
| **4** | The alias used before |

|   | If either `srcstorepass` or `alias` are not the same as defined in the `p12` file, the conversion will fail. |
|---|---|

Now modify your configuration:

HTTPS Configuration Example

```properties
micronaut.server.ssl.enabled=true
micronaut.server.ssl.key-name=cert-a
micronaut.certificate.resource.cert-a.resource=classpath:server.keystore
micronaut.certificate.resource.cert-a.password=newPassword
```

```yaml
micronaut:
  server:
    ssl:
      enabled: true
      key-name: cert-a

  certificate:
    resource:
      cert-a:
        resource: classpath:server.keystore
        password: newPassword
        # format: jks  # optional, auto-detected
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.ssl]
      enabled=true
      key-name="cert-a"
  [micronaut.certificate]
    [micronaut.certificate.resource]
      [micronaut.certificate.resource.cert-a]
        resource="classpath:server.keystore"
        password="newPassword"
```

```groovy
micronaut {
  server {
    ssl {
      enabled = true
      keyName = "cert-a"
    }
  }
  certificate {
    resource {
      certA {
        resource = "classpath:server.keystore"
        password = "newPassword"
      }
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      ssl {
        enabled = true
        key-name = "cert-a"
      }
    }
    certificate {
      resource {
        cert-a {
          resource = "classpath:server.keystore"
          password = "newPassword"
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "ssl": {
        "enabled": true,
        "key-name": "cert-a"
      }
    },
    "certificate": {
      "resource": {
        "cert-a": {
          "resource": "classpath:server.keystore",
          "password": "newPassword"
        }
      }
    }
  }
}
```

Start Micronaut, and the application will run on `https://localhost:8443` using the certificate in the keystore.


## Refreshing/Reloading HTTPS Certificates

Keeping HTTPS certificates up-to-date after expiry can be a challenge. A great solution to this is Automated Certificate Management Environment (ACME) and the Micronaut ACME Module which provides support for automatically refreshing certificates from a certificate authority.

If the use of a certificate authority is not possible, and you need to manually update certificates from disk then you should use the file-based certificate provider. As long as the underlying file system supports file watching, the provider will automatically recognize an updated key or certificate file.


## 6.33.7 Enabling HTTP and HTTPS

The Micronaut framework supports binding both HTTP and HTTPS. To enable dual protocol support, modify your configuration. For example:

Dual Protocol Configuration Example

```properties
micronaut.server.ssl.enabled=true
micronaut.server.ssl.build-self-signed=true
micronaut.server.dual-protocol=true
```

```yaml
micronaut:
  server:
    ssl:
      enabled: true
      build-self-signed: true
    dual-protocol : true
```

```toml
[micronaut]
  [micronaut.server]
    dual-protocol=true
    [micronaut.server.ssl]
      enabled=true
      build-self-signed=true
```

```groovy
micronaut {
  server {
    ssl {
      enabled = true
      buildSelfSigned = true
    }
    dualProtocol = true
  }
}
```

```hocon
{
  micronaut {
    server {
      ssl {
        enabled = true
        build-self-signed = true
      }
      dual-protocol = true
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "ssl": {
        "enabled": true,
        "build-self-signed": true
      },
      "dual-protocol": true
    }
  }
}
```

- You must configure SSL for HTTPS to work. In this example we are just using a self-signed certificate with `build-self-signed`, but see Securing the Server with HTTPS for other configurations
- `dual-protocol` enables both HTTP and HTTPS is an opt-in feature - setting the `dualProtocol` flag enables it. By default, the Micronaut framework only enables one.

It is also possible to redirect automatically all HTTP request to HTTPS. Besides the previous configuration, you need to enable this option. For example:

Enable HTTP to HTTPS Redirects

```properties
micronaut.server.ssl.enabled=true
micronaut.server.ssl.build-self-signed=true
micronaut.server.dual-protocol=true
micronaut.server.http-to-https-redirect=true
```

```yaml
micronaut:
  server:
    ssl:
      enabled: true
      build-self-signed: true
    dual-protocol : true
    http-to-https-redirect: true
```

```toml
[micronaut]
  [micronaut.server]
    dual-protocol=true
    http-to-https-redirect=true
    [micronaut.server.ssl]
      enabled=true
      build-self-signed=true
```

```groovy
micronaut {
  server {
    ssl {
      enabled = true
      buildSelfSigned = true
    }
    dualProtocol = true
    httpToHttpsRedirect = true
  }
}
```

```hocon
{
  micronaut {
    server {
      ssl {
        enabled = true
        build-self-signed = true
      }
      dual-protocol = true
      http-to-https-redirect = true
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "ssl": {
        "enabled": true,
        "build-self-signed": true
      },
      "dual-protocol": true,
      "http-to-https-redirect": true
    }
  }
}
```

- `http-to-https-redirect` enables HTTP to HTTPS redirects


## 6.33.8 Enabling Access Logger

In the spirit of apache mod_log_config and Tomcat Access Log Valve, it is possible to enable an access logger for the HTTP server (this works for both HTTP/1 and HTTP/2).

To enable and configure the access logger, in your configuration file (e.g `application.yml`) set:

Enabling the access logger

```properties
micronaut.server.netty.access-logger.enabled=true
micronaut.server.netty.access-logger.logger-name=my-access-logger
micronaut.server.netty.access-logger.log-format=common
```

```yaml
micronaut:
  server:
    netty:
      access-logger:
        enabled: true
        logger-name: my-access-logger
        log-format: common
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.netty]
      [micronaut.server.netty.access-logger]
        enabled=true
        logger-name="my-access-logger"
        log-format="common"
```

```groovy
micronaut {
  server {
    netty {
      accessLogger {
        enabled = true
        loggerName = "my-access-logger"
        logFormat = "common"
      }
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      netty {
        access-logger {
          enabled = true
          logger-name = "my-access-logger"
          log-format = "common"
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "netty": {
        "access-logger": {
          "enabled": true,
          "logger-name": "my-access-logger",
          "log-format": "common"
        }
      }
    }
  }
}
```

- `enabled` Enables the access logger
- optionally specify a `logger-name`, which defaults to `HTTP_ACCESS_LOGGER`
- optionally specify a `log-format`, which defaults to the Common Log Format

#### Filtering access logs

If you wish to not log access to certain paths, you can specify regular expression filters in the configuration:

Filtering the access logs

```properties
micronaut.server.netty.access-logger.enabled=true
micronaut.server.netty.access-logger.logger-name=my-access-logger
micronaut.server.netty.access-logger.log-format=common
micronaut.server.netty.access-logger.exclusions[0]=/health
micronaut.server.netty.access-logger.exclusions[1]=/path/.+
```

```yaml
micronaut:
  server:
    netty:
      access-logger:
        enabled: true
        logger-name: my-access-logger
        log-format: common
        exclusions:
          - /health
          - /path/.+
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.netty]
      [micronaut.server.netty.access-logger]
        enabled=true
        logger-name="my-access-logger"
        log-format="common"
        exclusions=[
          "/health",
          "/path/.+"
        ]
```

```groovy
micronaut {
  server {
    netty {
      accessLogger {
        enabled = true
        loggerName = "my-access-logger"
        logFormat = "common"
        exclusions = ["/health", "/path/.+"]
      }
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      netty {
        access-logger {
          enabled = true
          logger-name = "my-access-logger"
          log-format = "common"
          exclusions = ["/health", "/path/.+"]
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "netty": {
        "access-logger": {
          "enabled": true,
          "logger-name": "my-access-logger",
          "log-format": "common",
          "exclusions": ["/health", "/path/.+"]
        }
      }
    }
  }
}
```

- `enabled` Enables the access logger
- optionally specify a `logger-name`, which defaults to `HTTP_ACCESS_LOGGER`
- optionally specify a `log-format`, which defaults to the Common Log Format

#### Logback Configuration

In addition to enabling the access logger, you must add a logger for the specified or default logger name. For instance using the default logger name for logback:

Logback configuration

```xml
<appender
    name="httpAccessLogAppender"
    class="ch.qos.logback.core.rolling.RollingFileAppender">
    <append>true</append>
    <file>log/http-access.log</file>
    <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
        <!-- daily rollover -->
        <fileNamePattern>log/http-access-%d{yyyy-MM-dd}.log
        </fileNamePattern>
        <maxHistory>7</maxHistory>
    </rollingPolicy>
    <encoder>
        <charset>UTF-8</charset>
        <pattern>%msg%n</pattern>
    </encoder>
    <immediateFlush>true</immediateFlush>
</appender>

<logger name="HTTP_ACCESS_LOGGER" additivity="false" level="info">
    <appender-ref ref="httpAccessLogAppender" />
</logger>
```

The pattern should only have the message marker, as other elements will be processed by the access logger.

#### Log Format

The syntax is based on Apache httpd log format.

These are the supported markers:

- **%a** - Remote IP address
- **%A** - Local IP address
- **%b** - Bytes sent, excluding HTTP headers, or '-' if no bytes were sent
- **%B** - Bytes sent, excluding HTTP headers
- **%h** - Remote host name
- **%H** - Request protocol
- **%{<header>}i** - Request header. If the argument is omitted (**%i**) all headers are printed
- **%{<header>}o** - Response header. If the argument is omitted (**%o**) all headers are printed
- **%{<cookie>}C** - Request cookie (COOKIE). If the argument is omitted (**%C**) all cookies are printed
- **%{<cookie>}c** - Response cookie (SET_COOKIE). If the argument is omitted (**%c**) all cookies are printed
- **%l** - Remote logical username from identd (always returns '-')
- **%m** - Request method
- **%p** - Local port
- **%q** - Query string (excluding the '?' character)
- **%r** - First line of the request
- **%s** - HTTP status code of the response
- **%{<format>}t** - Date and time. If the argument is omitted, Common Log Format is used ("'['dd/MMM/yyyy:HH:mm:ss Z']'"). If the format starts with begin: (default) the time is taken at the beginning of the request processing. If it starts with end: it is the time when the log entry gets written, close to the end of the request processing. The format should follow `DateTimeFormatter` syntax.
- **%{property}u** - Remote authenticated user. When **micronaut-session** is on the classpath, returns the session id if the argument is omitted, or the specified property otherwise prints '-'
- **%U** - Requested URI
- **%v** - Local server name
- **%D** - Time taken to process the request, in milliseconds
- **%T** - Time taken to process the request, in seconds

In addition, you can use the following aliases for common patterns:

- **common** - `%h %l %u %t "%r" %s %b` for Common Log Format (CLF)
- **combined** - `%h %l %u %t "%r" %s %b "%{Referer}i" "%{User-Agent}i"` for Combined Log Format
