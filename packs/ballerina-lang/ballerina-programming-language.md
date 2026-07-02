---
title: "Ballerina (programming language)"
source: https://en.wikipedia.org/wiki/Ballerina_(programming_language)
domain: ballerina-lang
license: CC-BY-SA-4.0
tags: ballerina language, ballerina lang, ballerina integration
fetched: 2026-07-02
---

# Ballerina (programming language)

**Ballerina** is a general-purpose programming language designed by WSO2 for cloud computing application software. It is free and open-source software released under Apache License 2.

The project began in 2015 by architects from WSO2 as a code-based alternative to the configuration-based integration tools such as enterprise application integration (EAI), enterprise service bus (ESB), and workflow products.

It has various constructs for cloud-native development including support for various data formats and protocols, reliability, distributed transactions, application programming interfaces (APIs), and event streams.

## History

Ballerina was first publicly announced in 2017 and version 1.0 was released on September 10, 2019.

## Design

Ballerina is a general-purpose language with a familiar syntax along with a direct graphical representation of the code in the form of sequence diagrams. It has fundamental abstractions designed to make integration problems easier to program. Ballerina was designed by WSO2 to improve productivity for application developers that have to work with distributed computing. It is easy to write and modify and is suitable for application programmers.

The designers, who provided enterprise integration products for over 10 years, used their knowledge of the industry when designing the language, says WSO2 director and Ballerina founder James Clark.

## Examples

### Hello World

The regular Hello World program:

```mw
import ballerina/io;

public function main() {
    io:println("Hello World!");
}
```

To execute the above program, place the source code in a `.bal` file and provide the path of the file to the `bal run` command.

```mw
$ ballerina run hello_world.bal
Hello World!
```

The service version of the Hello World program:

```mw
import ballerina/http;

service /greet on new http:Listener(9090) {
    resource function get . () returns string {
        return "Hello World!";
    }
}
```

Services are executed in the same manner, except they don't terminate like regular programs do. Once the service is up and running, one can use an HTTP client to invoke the service. For example, the above service can be invoked using the following cURL command:

```mw
$ curl http://localhost:9090/greet 
Hello World!
```

### REST API

```mw
import ballerina/http;

service on new http:Listener(9090) {
    resource function post factorial(@http:Payload string payload) returns http:Ok|http:BadRequest {
        int|error num = int:fromString(payload);

        if num is error {
            return <http:BadRequest>{body: "Invalid integer: " + payload};
        }

        if num < 0 {
            return <http:BadRequest>{body: "Integer should be >= 0"};
        }

        int result = 1;

        foreach int i in 2 ... num {
            result *= i;
        }

        return <http:Ok>{body: result};
    }
}
```

```mw
$ curl http://localhost:9090/factorial -d 5
120
```

### GraphQL API

```mw
import ballerina/graphql;

service /stocks on new graphql:Listener(4000) {
    resource function get quote() returns StockQuote {
        return {
            ticker: "EXPO",
            price: 287.5,
            open: 285,
            prevClose: 285.5,
            low: 276.25,
            high: 297
        };
    }
}

type StockQuote record {|
    string ticker;
    float price;
    float open;
    float prevClose;
    float low;
    float high;
|};
```

```mw
$ curl -H "Content-type: application/json" -d '{"query": "{ quote { ticker, price } }" }' 'http://localhost:4000/stocks' 
{"data":{"quote":{"ticker":"EXPO", "price":287.5}}}
```

### Sequence diagram

The generated sequence diagram is a canonical representation of the source code. The two representations can be used interchangeably. The diagram support is provided through the Ballerina VS Code plugin. The following are a couple of such generated sequence diagrams, compared with its associated code.

A sample program for retrieving and processing COVID-19 data:

A sample program for creating a report out of pull request data retrieved from GitHub:

### JSON support

The language provides support for working with JSON values. The builtin type `json` is defined as the following union: `()|boolean|int|float|decimal|string|json[]|map<json>`

```mw
import ballerina/io;

public function main() returns error {
    // Syntax for `json` object values is very similar to the syntax of JSON
    json person = {name: "John Doe", age: 25};

    // Serialized `json` values conforms to the JSON specification 
    io:println(person);

    // The fields of the `json` value can be accessed as follows
    string name = check person.name;
    int age = check person.age;
}
```

### Code to cloud

Docker and Kubernetes artifacts required for deploying the code to the cloud can be generated when building the code. Values required for these artifacts are derived from the code. Additionally, one can override these values as well using the `Cloud.toml` file. To enable generation of the cloud artifacts, the users can use the `cloud` build option in the `Ballerina.toml` file. Use `docker` to generate just the Docker image and the Dockerfile and use `k8s` to generate Kubernetes artifacts as well. Minimal sample config TOML files would look something like the following:

`Ballerina.toml` file:

```mw
[package]
distribution = "2201.0.0"

[build-options]
cloud="k8s"
```

`Cloud.toml` file:

```mw
[container.image]
repository="bal_user"
name="greet"
tag="v0.1.0"
```

### Workers

```mw
import ballerina/http;
import ballerina/lang.'int;
import ballerina/io;

// Workers interact with each other by sending and receiving messages.
// Ballerina validates every worker interaction (send and receive)
// to avoid deadlocks.
public function main() {
    @strand {thread: "any"}
    worker w1 {
        int w1val = checkpanic calculate("2*3");
        // Sends a message asynchronously to the worker `w2`.
        w1val -> w2;
        // Receives a message from the worker `w2`.
        int w2val = <- w2;
        io:println("[w1] Message from w2: ", w2val);
        // Sends messages synchronously to the worker `w3`. The worker `w1` will wait
        // until the worker `w3` receives the message.
        w1val ->> w3;
        w2val -> w3;
        // Flushes all messages sent asynchronously to the worker `w3`. The worker
        // will halt at this point until all messages are sent or until the worker `w3`
        // fails.
        checkpanic flush w3;
    }

    // A worker can have an explicit return type, or else, if a return type is not mentioned,
    // it is equivalent to returning ().
    @strand {thread: "any"}
    worker w2 {
        int w2val = checkpanic calculate("17*5");
        // Receives a message from the worker `w1`.
        int w1val = <- w1;
        io:println("[w2] Message from w1: ", w1val);
        // Sends a message asynchronously to the worker `w1`.
        w1val + w2val -> w1;
    }

    worker w3 {
        int|error w1val = <- w1;
        int|error w2val = <- w1;
        io:println("[w3] Messages from w1: ", w1val, ", ", w2val);
    }

    // Waits for the worker `w1`to finish.
    wait w1;
}

function calculate(string expr) returns int|error {
    http:Client httpClient = check new ("https://api.mathjs.org");
    string response = check httpClient->get(string `/v4/?expr=${expr}`);
    return check 'int:fromString(response);
}
```
