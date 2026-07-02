---
title: "Vert.x Core (part 8/8)"
source: https://vertx.io/docs/vertx-core/java/
domain: vertx
license: CC-BY-SA-4.0
tags: vert.x toolkit, eclipse vertx, reactive toolkit, event loop server
fetched: 2026-07-02
part: 8/8
---

## Logging

Vert.x logs using its internal logging API and supports various logging backends.

The logging backend is selected as follows:

1. the backend denoted by the `vertx.logger-delegate-factory-class-name` system property if present or,
2. JDK logging when a `vertx-default-jul-logging.properties` file is in the classpath or,
3. a backend present in the classpath, in the following order of preference: SLF4J Log4J2

Otherwise Vert.x defaults to JDK logging.

### Configuring with the system property

Set the `vertx.logger-delegate-factory-class-name` system property to:

- `io.vertx.core.logging.SLF4JLogDelegateFactory` for SLF4J or,
- `io.vertx.core.logging.Log4j2LogDelegateFactory` for Log4J2 or,
- `io.vertx.core.logging.JULLogDelegateFactory` for JDK logging

### Automatic configuration

When no `vertx.logger-delegate-factory-class-name` system property is set, Vert.x will try to find the most appropriate logger:

- use SLF4J when available on the classpath with an actual implementation (i.e. `LoggerFactory.getILoggerFactory()` is not an instance of `NOPLoggerFactory`)
- otherwise use Log4j2 when available on the classpath
- otherwise use JUL

### Configuring JUL logging

A JUL logging configuration file can be specified in the normal JUL way, by providing a system property named `java.util.logging.config.file` with the value being your configuration file. For more information on this and the structure of a JUL config file please consult the JDK logging documentation.

Vert.x also provides a slightly more convenient way to specify a configuration file without having to set a system property. Just provide a JUL config file with the name `vertx-default-jul-logging.properties` on your classpath (e.g. inside your fatjar) and Vert.x will use that to configure JUL.

### Netty logging

Netty does not rely on external logging configuration (e.g system properties). Instead, it implements a logging configuration based on the logging libraries visible from the Netty classes:

- use `SLF4J` library if it is visible
- otherwise use `Log4j` if it is visible
- otherwise use `Log4j2` if it is visible
- otherwise fallback to `java.util.logging`

|   | The eagle eyes among you might have noticed that Vert.x follows the same order of preference. |
|---|---|

The logger implementation can be forced to a specific implementation by setting Netty’s internal logger implementation directly on `io.netty.util.internal.logging.InternalLoggerFactory`:

```
// Force logging to Log4j 2
InternalLoggerFactory.setDefaultFactory(Log4J2LoggerFactory.INSTANCE);
```

### Troubleshooting

#### SLF4J warning at startup

If, when you start your application, you see the following message:

```
SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
```

It means that you have SLF4J-API in your classpath but no actual binding. Messages logged with SLF4J will be dropped. You should add a binding to your classpath. Check https://www.slf4j.org/manual.html#swapping to pick a binding and configure it.

Be aware that Netty looks for the SLF4-API jar and uses it by default.

#### Connection reset by peer

If your logs show a bunch of:

```
io.vertx.core.net.impl.ConnectionBase
SEVERE: java.io.IOException: Connection reset by peer
```

It means that the client is resetting the HTTP connection instead of closing it. This message also indicates that you may have not consumed the complete payload (the connection was cut before you were able to).


## Configuring SSL

### Server SSL/TLS configuration

#### Specifying key/certificate for the server

SSL/TLS servers usually provide certificates to clients in order to verify their identity to clients.

Certificates/keys can be configured for servers in several ways:

The first method is by specifying the location of a Java key-store which contains the certificate and private key.

Java key stores can be managed with the keytool utility which ships with the JDK.

The password for the key store should also be provided:

```
ServerSSLOptions options = new ServerSSLOptions()
  .setKeyCertOptions(
  new JksOptions().
    setPath("/path/to/your/server-keystore.jks").
    setPassword("password-of-your-keystore")
);
```

Alternatively you can read the key store yourself as a buffer and provide that directly:

```
Buffer myKeyStoreAsABuffer = vertx.fileSystem().readFileBlocking("/path/to/your/server-keystore.jks");
ServerSSLOptions options = new ServerSSLOptions()
  .setKeyCertOptions(
    new JksOptions().
      setValue(myKeyStoreAsABuffer).
      setPassword("password-of-your-keystore")
  );
```

Key/certificate in PKCS#12 format (http://en.wikipedia.org/wiki/PKCS_12), usually with the `.pfx` or the `.p12` extension can also be loaded in a similar fashion than JKS key stores:

```
ServerSSLOptions options = new ServerSSLOptions()
  .setKeyCertOptions(
    new PfxOptions().
      setPath("/path/to/your/server-keystore.pfx").
      setPassword("password-of-your-keystore")
  );
```

Buffer configuration is also supported:

```
Buffer myKeyStoreAsABuffer = vertx.fileSystem().readFileBlocking("/path/to/your/server-keystore.pfx");
ServerSSLOptions options = new ServerSSLOptions()
  .setKeyCertOptions(
    new PfxOptions().
      setValue(myKeyStoreAsABuffer).
      setPassword("password-of-your-keystore")
  );
```

Another way of providing server private key and certificate separately using `.pem` files.

```
ServerSSLOptions options = new ServerSSLOptions()
  .setKeyCertOptions(
    new PemKeyCertOptions().
      setKeyPath("/path/to/your/server-key.pem").
      setCertPath("/path/to/your/server-cert.pem")
  );
```

Buffer configuration is also supported:

```
Buffer myKeyAsABuffer = vertx.fileSystem().readFileBlocking("/path/to/your/server-key.pem");
Buffer myCertAsABuffer = vertx.fileSystem().readFileBlocking("/path/to/your/server-cert.pem");
ServerSSLOptions options = new ServerSSLOptions()
  .setKeyCertOptions(
    new PemKeyCertOptions().
      setKeyValue(myKeyAsABuffer).
      setCertValue(myCertAsABuffer)
  );
```

Vert.x supports reading of unencrypted RSA and/or ECC based private keys from PKCS8 PEM files. RSA based private keys can also be read from PKCS1 PEM files. X.509 certificates can be read from PEM files containing a textual encoding of the certificate as defined by RFC 7468, Section 5.

|   | Keep in mind that the keys contained in an unencrypted PKCS8 or a PKCS1 PEM file can be extracted by anybody who can read the file. Thus, make sure to put proper access restrictions on such PEM files in order to prevent misuse. |
|---|---|

Finally, you can also load generic Java keystore, it is useful for using other KeyStore implementations like Bouncy Castle:

```
ServerSSLOptions options = new ServerSSLOptions()
  .setKeyCertOptions(
    new KeyStoreOptions().
      setType("BKS").
      setPath("/path/to/your/server-keystore.bks").
      setPassword("password-of-your-keystore")
  );
```

#### Specifying trust for the server

SSL/TLS servers can use a certificate authority in order to verify the identity of the clients.

Certificate authorities can be configured for servers in several ways:

Java trust stores can be managed with the keytool utility which ships with the JDK.

The password for the trust store should also be provided:

```
ServerSSLOptions options = new ServerSSLOptions().
  setClientAuth(ClientAuth.REQUIRED).
  setTrustOptions(
    new JksOptions().
      setPath("/path/to/your/truststore.jks").
      setPassword("password-of-your-truststore")
  );
```

Alternatively you can read the trust store yourself as a buffer and provide that directly:

```
Buffer myTrustStoreAsABuffer = vertx.fileSystem().readFileBlocking("/path/to/your/truststore.jks");
ServerSSLOptions options = new ServerSSLOptions().
  setClientAuth(ClientAuth.REQUIRED).
  setTrustOptions(
    new JksOptions().
      setValue(myTrustStoreAsABuffer).
      setPassword("password-of-your-truststore")
  );
```

Certificate authority in PKCS#12 format (http://en.wikipedia.org/wiki/PKCS_12), usually with the `.pfx` or the `.p12` extension can also be loaded in a similar fashion than JKS trust stores:

```
ServerSSLOptions options = new ServerSSLOptions().
  setClientAuth(ClientAuth.REQUIRED).
  setTrustOptions(
    new PfxOptions().
      setPath("/path/to/your/truststore.pfx").
      setPassword("password-of-your-truststore")
  );
```

Buffer configuration is also supported:

```
Buffer myTrustStoreAsABuffer = vertx.fileSystem().readFileBlocking("/path/to/your/truststore.pfx");
ServerSSLOptions options = new ServerSSLOptions().
  setClientAuth(ClientAuth.REQUIRED).
  setTrustOptions(
    new PfxOptions().
      setValue(myTrustStoreAsABuffer).
      setPassword("password-of-your-truststore")
  );
```

Another way of providing server certificate authority using a list `.pem` files.

```
ServerSSLOptions options = new ServerSSLOptions().
  setClientAuth(ClientAuth.REQUIRED).
  setTrustOptions(
    new PemTrustOptions().
      addCertPath("/path/to/your/server-ca.pem")
  );
```

Buffer configuration is also supported:

```
Buffer myCaAsABuffer = vertx.fileSystem().readFileBlocking("/path/to/your/server-ca.pfx");
ServerSSLOptions options = new ServerSSLOptions().
  setClientAuth(ClientAuth.REQUIRED).
  setTrustOptions(
    new PemTrustOptions().
      addCertValue(myCaAsABuffer)
  );
```

#### Server Name Indication (SNI)

Server Name Indication (SNI) is a TLS extension by which a client specifies a hostname attempting to connect: during the TLS handshake the client gives a server name and the server can use it to respond with a specific certificate for this server name instead of the default deployed certificate.

If the server requires client authentication the server can use a specific trusted CA certificate depending on the indicated server name.

When SNI is active the server uses

- the certificate CN or SAN DNS (Subject Alternative Name with DNS) to do an exact match, e.g `www.example.com`
- the certificate CN or SAN DNS certificate to match a wildcard name, e.g `*.example.com`
- otherwise the first certificate when the client does not present a server name or the presented server name cannot be matched

When the server additionally requires client authentication:

- when `JksOptions` is `set on trust options` then an exact match with the trust store alias is done
- otherwise the available CA certificates are used in the same way as if no SNI is in place

|   | the server fails to bind with an error reporting an incorrect alias |
|---|---|

You can enable SNI on the server by setting `setSni` to `true` and configured the server with multiple key/certificate pairs.

Java KeyStore files or PKCS12 files can store multiple key/cert pairs out of the box.

```
ServerSSLOptions options = new ServerSSLOptions()
  .setKeyCertOptions(new JksOptions()
    .setPath("keystore.jks")
    .setPassword("wibble"))
  .setSni(true);
```

`PemKeyCertOptions` can be configured to hold multiple entries:

```
ServerSSLOptions options = new ServerSSLOptions()
  .setKeyCertOptions(new PemKeyCertOptions()
    .setKeyPaths(Arrays.asList("default-key.pem", "host1-key.pem", "etc..."))
    .setCertPaths(Arrays.asList("default-cert.pem", "host2-key.pem", "etc...")
    ))
  .setSni(true);
```

### Client SSL/TLS configuration

#### Client trust configuration

Like server configuration, the client trust can be configured in several ways:

The first method is by specifying the location of a Java trust-store which contains the certificate authority.

It is just a standard Java key store, the same as the key stores on the server side. The client trust store location is set by using the function `path` on the `jks options`. If a server presents a certificate during connection which is not in the client trust store, the connection attempt will not succeed.

```
ClientSSLOptions options = new ClientSSLOptions()
  .setTrustOptions(new JksOptions().
    setPath("/path/to/your/truststore.jks").
    setPassword("password-of-your-truststore")
  );
```

Buffer configuration is also supported:

```
Buffer myTrustStoreAsABuffer = vertx.fileSystem().readFileBlocking("/path/to/your/truststore.jks");
ClientSSLOptions options = new ClientSSLOptions()
  .setTrustOptions(new JksOptions().
    setValue(myTrustStoreAsABuffer).
    setPassword("password-of-your-truststore")
  );
```

Certificate authority in PKCS#12 format (http://en.wikipedia.org/wiki/PKCS_12), usually with the `.pfx` or the `.p12` extension can also be loaded in a similar fashion than JKS trust stores:

```
ClientSSLOptions options = new ClientSSLOptions()
  .setTrustOptions(new PfxOptions().
    setPath("/path/to/your/truststore.pfx").
    setPassword("password-of-your-truststore")
  );
```

Buffer configuration is also supported:

```
Buffer myTrustStoreAsABuffer = vertx.fileSystem().readFileBlocking("/path/to/your/truststore.pfx");
ClientSSLOptions options = new ClientSSLOptions()
  .setTrustOptions(new PfxOptions().
    setValue(myTrustStoreAsABuffer).
    setPassword("password-of-your-truststore")
  );
```

Another way of providing server certificate authority using a list `.pem` files.

```
ClientSSLOptions options = new ClientSSLOptions()
  .setTrustOptions(new PemTrustOptions().
    addCertPath("/path/to/your/ca-cert.pem")
  );
```

Buffer configuration is also supported:

```
Buffer myTrustStoreAsABuffer = vertx.fileSystem().readFileBlocking("/path/to/your/ca-cert.pem");
ClientSSLOptions options = new ClientSSLOptions()
  .setTrustOptions(new PemTrustOptions().
    addCertValue(myTrustStoreAsABuffer)
  );
```

If the `trustALl` is set to true on the client, then the client will trust all server certificates. The connection will still be encrypted but this mode is vulnerable to 'man in the middle' attacks. I.e. you can’t be sure who you are connecting to. Use this with caution. Default value is false.

```
ClientSSLOptions options = new ClientSSLOptions()
  .setTrustAll(true);
```

#### Specifying key/certificate for the client

If the server requires client authentication then the client must present its own certificate to the server when connecting. The client can be configured in several ways:

The first method is by specifying the location of a Java key-store which contains the key and certificate. Again it’s just a regular Java key store. The client keystore location is set by using the function `path` on the `jks options`.

```
ClientSSLOptions options = new ClientSSLOptions()
  .setKeyCertOptions(new JksOptions().
    setPath("/path/to/your/client-keystore.jks").
    setPassword("password-of-your-keystore")
  );
```

Buffer configuration is also supported:

```
Buffer myKeyStoreAsABuffer = vertx.fileSystem().readFileBlocking("/path/to/your/client-keystore.jks");
ClientSSLOptions options = new ClientSSLOptions()
  .setKeyCertOptions(new JksOptions().
    setValue(myKeyStoreAsABuffer).
    setPassword("password-of-your-keystore")
  );
```

Key/certificate in PKCS#12 format (http://en.wikipedia.org/wiki/PKCS_12), usually with the `.pfx` or the `.p12` extension can also be loaded in a similar fashion than JKS key stores:

```
ClientSSLOptions options = new ClientSSLOptions()
  .setKeyCertOptions(new PfxOptions().
    setPath("/path/to/your/client-keystore.pfx").
    setPassword("password-of-your-keystore")
  );
```

Buffer configuration is also supported:

```
Buffer myKeyStoreAsABuffer = vertx.fileSystem().readFileBlocking("/path/to/your/client-keystore.pfx");
ClientSSLOptions options = new ClientSSLOptions()
  .setKeyCertOptions(new PfxOptions().
    setValue(myKeyStoreAsABuffer).
    setPassword("password-of-your-keystore")
  );
```

Another way of providing server private key and certificate separately using `.pem` files.

```
ClientSSLOptions options = new ClientSSLOptions()
  .setKeyCertOptions(new PemKeyCertOptions().
    setKeyPath("/path/to/your/client-key.pem").
    setCertPath("/path/to/your/client-cert.pem")
  );
```

Buffer configuration is also supported:

```
Buffer myKeyAsABuffer = vertx.fileSystem().readFileBlocking("/path/to/your/client-key.pem");
Buffer myCertAsABuffer = vertx.fileSystem().readFileBlocking("/path/to/your/client-cert.pem");
ClientSSLOptions options = new ClientSSLOptions()
  .setKeyCertOptions(new PemKeyCertOptions().
    setKeyValue(myKeyAsABuffer).
    setCertValue(myCertAsABuffer)
  );
```

Keep in mind that pem configuration, the private key is not crypted.

### Revoking certificate authorities

Trust can be configured to use a certificate revocation list (CRL) for revoked certificates that should no longer be trusted. The `crlPath` configures the crl list to use:

```
ClientSSLOptions options = new ClientSSLOptions()
  .setTrustOptions(trustOptions)
  .addCrlPath("/path/to/your/crl.pem");
```

Buffer configuration is also supported:

```
Buffer myCrlAsABuffer = vertx.fileSystem().readFileBlocking("/path/to/your/crl.pem");
ClientSSLOptions options = new ClientSSLOptions()
  .setTrustOptions(trustOptions)
  .addCrlValue(myCrlAsABuffer);
```

### Configuring the Cipher suite

By default, the TLS configuration will use the list of Cipher suites of the SSL engine:

- JDK SSL engine when `JdkSSLEngineOptions` is used
- OpenSSL engine when `OpenSSLEngineOptions` is used

This Cipher suite can be configured with a suite of enabled ciphers:

```
ServerSSLOptions options = new ServerSSLOptions().
  setKeyCertOptions(keyStoreOptions).
  addEnabledCipherSuite("ECDHE-RSA-AES128-GCM-SHA256").
  addEnabledCipherSuite("ECDHE-ECDSA-AES128-GCM-SHA256").
  addEnabledCipherSuite("ECDHE-RSA-AES256-GCM-SHA384").
  addEnabledCipherSuite("CDHE-ECDSA-AES256-GCM-SHA384");
```

When the enabled cipher suites is defined (i.e not empty), it takes precedence over the default cipher suites of the SSL engine.

Cipher suite can be specified on the `ServerSSLOptions` or `ClientSSLOptions` configuration.

### Configuring TLS protocol versions

By default, the default TLS configuration enables the following protocols: TLSv1.2 and TLSv1.3. Protocol versions can be enabled by explicitly adding them:

```
ServerSSLOptions options = new ServerSSLOptions().
  setKeyCertOptions(keyStoreOptions).
  addEnabledSecureTransportProtocol("TLSv1.1");
```

They can also be removed:

```
ServerSSLOptions options = new ServerSSLOptions().
  setKeyCertOptions(keyStoreOptions).
  removeEnabledSecureTransportProtocol("TLSv1.2");
```

Protocol versions can be specified on the `ServerSSLOptions` or `ClientSSLOptions` configuration.

|   | TLS 1.0 (TLSv1) and TLS 1.1 (TLSv1.1) are widely deprecated and have been disabled by default since Vert.x 4.4.0. |
|---|---|

### SSL engine

The engine implementation can be configured to use OpenSSL instead of the JDK implementation. Before JDK started to use hardware intrinsics (CPU instructions) for AES in Java 8 and for RSA in Java 9, OpenSSL provided much better performances and CPU usage than the JDK engine.

```
ServerSSLOptions sslOptions = new ServerSSLOptions()
  .setKeyCertOptions(keyStoreOptions);

// Use JDK SSL engine
HttpServer server = vertx.createHttpServer(sslOptions);

// Use JDK SSL engine explicitly
server = vertx.httpServerBuilder()
  .with(sslOptions)
  .with(new JdkSSLEngineOptions())
  .build();

// Use OpenSSL engine
server = vertx.httpServerBuilder()
  .with(sslOptions)
  .with(new OpenSSLEngineOptions())
  .build();
```


## Host name resolution

Vert.x uses an an address resolver for resolving host name into IP addresses instead of the JVM built-in blocking resolver.

A host name resolves to an IP address using:

- the *hosts* file of the operating system
- otherwise DNS queries against a list of servers

By default it will use the list of the system DNS server addresses from the environment, if that list cannot be retrieved it will use Google’s public DNS servers `"8.8.8.8"` and `"8.8.4.4"`.

DNS servers can be also configured when creating a `Vertx` instance:

```
Vertx vertx = Vertx.vertx(new VertxOptions().
    setAddressResolverOptions(
        new AddressResolverOptions().
            addServer("192.168.0.1").
            addServer("192.168.0.2:40000"))
);
```

The default port of a DNS server is `53`, when a server uses a different port, this port can be set using a colon delimiter: `192.168.0.2:40000`.

|   | sometimes it can be desirable to use the JVM built-in resolver, the JVM system property *-Dvertx.disableDnsResolver=true* activates this behavior |
|---|---|

### Failover

When a server does not reply in a timely manner, the resolver will try the next one from the list, the search is limited by `setMaxQueries` (the default value is `4` queries).

A DNS query is considered as failed when the resolver has not received a correct answer within `getQueryTimeout` milliseconds (the default value is `5` seconds).

### Server list rotation

By default the dns server selection uses the first one, the remaining servers are used for failover.

You can configure `setRotateServers` to `true` to let the resolver perform a round-robin selection instead. It spreads the query load among the servers and avoids all lookup to hit the first server of the list.

Failover still applies and will use the next server in the list.

### Hosts mapping

The *hosts* file of the operating system is used to perform a hostname lookup for an ipaddress.

An alternative *hosts* file can be used instead:

```
Vertx vertx = Vertx.vertx(new VertxOptions().
    setAddressResolverOptions(
        new AddressResolverOptions().
            setHostsPath("/path/to/hosts"))
);
```

By default the resolver will use the system DNS search domains from the environment. Alternatively an explicit search domain list can be provided:

```
Vertx vertx = Vertx.vertx(new VertxOptions().
    setAddressResolverOptions(
        new AddressResolverOptions().addSearchDomain("foo.com").addSearchDomain("bar.com"))
);
```

When a search domain list is used, the threshold for the number of dots is `1` or loaded from `/etc/resolv.conf` on Linux, it can be configured to a specific value with `setNdots`.

### MacOS configuration

MacOS has a specific native extension to get the name server configuration of the system based on Apple’s open source mDNSResponder. When this extension is not present, Netty logs the following warning.

```
[main] WARN io.netty.resolver.dns.DnsServerAddressStreamProviders - Can not find io.netty.resolver.dns.macos.MacOSDnsServerAddressStreamProvider in the classpath, fallback to system defaults. This may result in incorrect DNS resolutions on MacOS.
```

This extension is not required as its absence does not prevent Vert.x to execute, yet is **recommended**.

You can add it to your classpath to improve the integration and remove the warning.

Intel-based Mac

```
<profile>
  <id>mac-intel</id>
  <activation>
    <os>
      <family>mac</family>
      <arch>x86_64</arch>
    </os>
  </activation>
  <dependencies>
    <dependency>
      <groupId>io.netty</groupId>
      <artifactId>netty-resolver-dns-native-macos</artifactId>
      <classifier>osx-x86_64</classifier>
      <!--<version>Should align with netty version that Vert.x uses</version>-->
    </dependency>
  </dependencies>
</profile>
```

M1/M2 Mac

```
<profile>
  <id>mac-silicon</id>
  <activation>
    <os>
      <family>mac</family>
      <arch>aarch64</arch>
    </os>
  </activation>
  <dependencies>
    <dependency>
      <groupId>io.netty</groupId>
      <artifactId>netty-resolver-dns-native-macos</artifactId>
      <classifier>osx-aarch_64</classifier>
      <!--<version>Should align with netty version that Vert.x uses</version>-->
    </dependency>
  </dependencies>
</profile>
```


## Native transports

Vert.x can run with native transports (when available) on BSD (OSX) and Linux:

```
Vertx vertx = Vertx.vertx(new VertxOptions().
  setPreferNativeTransport(true)
);

// True when native is available
boolean usingNative = vertx.isNativeTransportEnabled();
System.out.println("Running with native: " + usingNative);
```

|   | Preferring native transport will not prevent the application to execute (for example a native dependency might be missing).If your application requires native transport, you need to check `isNativeTransportEnabled`. |
|---|---|

You can also explicitly configure the transport to use:

```
Transport transport = Transport.nativeTransport();

// Or use a very specific transport
transport = Transport.EPOLL;

Vertx vertx = Vertx.builder()
  .withTransport(transport)
  .build();
```

### Native epoll

Native on Linux gives you extra networking options:

- `SO_REUSEPORT`
- `TCP_QUICKACK`
- `TCP_CORK`
- `TCP_FASTOPEN`
- `TCP_USER_TIMEOUT`

You need to add the following dependency in your classpath:

```
<dependency>
  <groupId>io.netty</groupId>
  <artifactId>netty-transport-native-epoll</artifactId>
  <classifier>linux-x86_64</classifier>
  <!--<version>Should align with netty version that Vert.x uses</version>-->
</dependency>
```

### Native io_uring

You need to add the following dependency in your classpath:

```
<dependency>
  <groupId>io.netty</groupId>
  <classifier>linux-x86_64</classifier>
  <artifactId>netty-transport-native-io_uring</artifactId>
  <!--<version>Should align with netty version that Vert.x uses</version>-->
</dependency>
```

### Native kqueue

You need to add the following dependency in your classpath:

Intel-based Mac

```
<dependency>
  <groupId>io.netty</groupId>
  <artifactId>netty-transport-native-kqueue</artifactId>
  <classifier>osx-x86_64</classifier>
  <!--<version>Should align with netty version that Vert.x uses</version>-->
</dependency>
```

M1/M2 Mac

```
<dependency>
<groupId>io.netty</groupId>
<artifactId>netty-transport-native-kqueue</artifactId>
<classifier>osx-aarch_64</classifier>
<!--<version>Should align with netty version that Vert.x uses</version>-->
</dependency>
```

MacOS Sierra and above are supported.

Native on BSD gives you extra networking options:

- `SO_REUSEPORT`

```
HttpServerConfig config = new HttpServerConfig();

TcpConfig tcpConfig = config
  .getTcpConfig()
  .getTransportConfig();

// Available on BSD
tcpConfig
  .setSoReusePort(reusePort);

vertx.createHttpServer(config);
```


## Security notes

Vert.x is a toolkit, not an opinionated framework where we force you to do things in a certain way. This gives you great power as a developer but with that comes great responsibility.

As with any toolkit, it’s possible to write insecure applications, so you should always be careful when developing your application especially if it’s exposed to the public (e.g. over the internet).

### Web applications

If writing a web application it’s highly recommended that you use Vert.x-Web instead of Vert.x core directly for serving resources and handling file uploads.

Vert.x-Web normalises the path in requests to prevent malicious clients from crafting URLs to access resources outside of the web root.

Similarly for file uploads Vert.x-Web provides functionality for uploading to a known place on disk and does not rely on the filename provided by the client in the upload which could be crafted to upload to a different place on disk.

Vert.x core itself does not provide such checks so it would be up to you as a developer to implement them yourself.

### Clustered event bus traffic

When clustering the event bus between different Vert.x nodes on a network, the traffic is sent un-encrypted across the wire, so do not use this if you have confidential data to send and your Vert.x nodes are not on a trusted network.

### Standard security best practices

Any service can have potentially vulnerabilities whether it’s written using Vert.x or any other toolkit so always follow security best practice, especially if your service is public facing.

For example you should always run them in a DMZ and with an user account that has limited rights in order to limit the extent of damage in case the service was compromised.


## Configuring Vert.x cache

When Vert.x needs to read a file from the classpath (embedded in a fat jar, in a jar form the classpath or a file that is on the classpath), it copies it to a cache directory. The reason behind this is simple: reading a file from a jar or from an input stream is blocking. So to avoid to pay the price every time, Vert.x copies the file to its cache directory and reads it from there every subsequent read. This behavior can be configured.

First, by default, Vert.x uses `$CWD/.vertx` as cache directory. It creates a unique directory inside this one to avoid conflicts. This location can be configured by using the `vertx.cacheDirBase` system property. For instance if the current working directory is not writable (such as in an immutable container context), launch your application with:

```
java -jar my-fat.jar vertx.cacheDirBase=/tmp/vertx-cache
```

|   | the directory must be **writable**. |
|---|---|

When you are editing resources such as HTML, CSS or JavaScript, this cache mechanism can be annoying as it serves only the first version of the file (and so you won’t see your edits if you reload your page). To avoid this behavior, launch your application with `-Dvertx.disableFileCaching=true`. With this setting, Vert.x still uses the cache, but always refresh the version stored in the cache with the original source. So if you edit a file served from the classpath and refresh your browser, Vert.x reads it from the classpath, copies it to the cache directory and serves it from there. Do not use this setting in production, it can kill your performances.

Finally, you can disable completely the cache by using `-Dvertx.disableFileCPResolving=true`. This setting is not without consequences. Vert.x would be unable to read any files from the classpath (only from the file system). Be very careful when using this setting.

FAQ

Application Launcher
