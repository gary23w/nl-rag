---
title: "What is Pulumi?"
source: https://www.pulumi.com/docs/concepts/
domain: pulumi
license: CC-BY-SA-4.0
tags: pulumi iac, infrastructure as code, cloud provisioning, declarative infrastructure
fetched: 2026-07-02
---

# What is Pulumi?

Pulumi is a modern infrastructure as code platform. It leverages existing programming languages—TypeScript, JavaScript, Python, Go, .NET, Java, and markup languages like YAML—and their native ecosystems to interact with cloud resources. A downloadable CLI, runtime, libraries, and a hosted service work together to deliver a robust platform for provisioning, updating, and managing cloud infrastructure.

If this is your first time using Pulumi, you likely want to begin with

the Getting Started guide

for your cloud of choice. It will walk you through an

AWS

,

Azure

,

Google Cloud

, or

Kubernetes

deployment from start to finish.

Pulumi is an infrastructure as code platform that allows you to use familiar programming languages and tools to build, deploy, and manage cloud infrastructure.

Pulumi is free, open source, and optionally pairs with Pulumi Cloud to make managing infrastructure secure, reliable, and hassle-free.

## Supported languages and SDKs

As a multi-language infrastructure as code tool, Pulumi supports many of today’s most common general-purpose programming and markup languages. Every Pulumi-supported language is equally capable of provisioning and managing infrastructure across all major clouds, though some languages may provide functionality that’s not yet available in others. The following languages and runtimes are currently supported:

- TypeScript & JavaScript (Node.js)
- Python
- Go
- C#, VB, F# (.NET)
- Java
- Pulumi YAML

If you don’t see your favorite language listed, it may be on its way soon.

Pulumi is open source

, and it is possible to

add your own language

. For additional language questions, visit

Pulumi’s languages and SDK docs

.

## How does Pulumi work?

The Pulumi platform comprises several components:

- **Software development kit (SDK)**: Pulumi Software Development Kit (SDK) provides bindings for each type of resource that the provider can manage. This provides the necessary tools and libraries for defining and managing cloud resources on any cloud and with any provider.
- **Command-Line interface (CLI)**: Pulumi is controlled primarily using the command line interface (CLI). It works in conjunction with Pulumi Cloud to deploy changes to your cloud apps and infrastructure. It keeps a history of who updated what in your team and when. This CLI has been designed for great inner loop productivity, in addition to continuous integration and delivery scenarios.
- **Deployment engine** The deployment engine is responsible for computing the set of operations needed to drive the current state of your infrastructure into the desired state expressed by your program.

This diagram illustrates the structure and major components of Pulumi.

(Pulumi programming model diagram.)

Pulumi *programs*, written in general-purpose programming languages, describe how your cloud infrastructure should be composed. To declare new infrastructure in your program, you allocate *resource* objects whose properties correspond to the desired state of your infrastructure. These properties are also used between resources to handle any necessary dependencies and can be exported outside of the stack, if needed.

Programs reside in a *project*, which is a directory that contains source code for the program and metadata on how to run the program. After writing your program, you run the Pulumi CLI command `pulumi up` from within your project directory. This command creates an isolated and configurable instance of your program, known as a *stack*. Stacks are similar to different deployment environments that you use when testing and rolling out application updates. For instance, you can have distinct development, staging, and production stacks that you create and test against.

### Example

To illustrate these concepts, the following program shows how to create an AWS EC2 security group named `web-sg` with a single ingress rule and a `t2.micro`-sized EC2 instance using that security group.

To use the security group, the EC2 resource requires the security group’s ID. Pulumi enables this through the output property `id` on the security group resource. Pulumi understands dependencies between resources and uses the relationships between resources to maximize parallelism and ensures correct ordering when a stack is instantiated.

Finally, the server’s resulting IP address and DNS name are exported as stack outputs so that their values can be accessed through either a CLI command or by another stack.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const group = new aws.ec2.SecurityGroup("web-sg", {
    description: "Enable HTTP access",
    ingress: [
        {
            protocol: "tcp",
            fromPort: 80,
            toPort: 80,
            cidrBlocks: ["0.0.0.0/0"],
        },
    ],
});

const server = new aws.ec2.Instance("web-server", {
    ami: "ami-0319ef1a70c93d5c8",
    instanceType: "t2.micro",
    vpcSecurityGroupIds: [group.id],
});

export const publicIp = server.publicIp;
export const publicDns = server.publicDns;
```

```python
import pulumi
import pulumi_aws as aws

group = aws.ec2.SecurityGroup(
    "web-sg",
    description="Enable HTTP access",
    ingress=[
        {
            "protocol": "tcp",
            "from_port": 80,
            "to_port": 80,
            "cidr_blocks": ["0.0.0.0/0"],
        }
    ],
)

server = aws.ec2.Instance(
    "web-server",
    ami="ami-0319ef1a70c93d5c8",
    instance_type="t2.micro",
    vpc_security_group_ids=[group.id],
)

pulumi.export("public_ip", server.public_ip)
pulumi.export("public_dns", server.public_dns)
```

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		group, err := ec2.NewSecurityGroup(ctx, "web-sg", &ec2.SecurityGroupArgs{
			Description: pulumi.String("Enable HTTP access"),
			Ingress: ec2.SecurityGroupIngressArray{
				ec2.SecurityGroupIngressArgs{
					Protocol:   pulumi.String("tcp"),
					FromPort:   pulumi.Int(80),
					ToPort:     pulumi.Int(80),
					CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
				},
			},
		})
		if err != nil {
			return err
		}
		server, err := ec2.NewInstance(ctx, "web-server", &ec2.InstanceArgs{
			Ami:                 pulumi.String("ami-0319ef1a70c93d5c8"),
			InstanceType:        pulumi.String("t2.micro"),
			VpcSecurityGroupIds: pulumi.StringArray{group.ID()},
		})
		if err != nil {
			return err
		}

		ctx.Export("publicIp", server.PublicIp)
		ctx.Export("publicHostName", server.PublicDns)
		return nil
	})
}
```

```csharp
using Pulumi;
using Pulumi.Aws.Ec2;
using Pulumi.Aws.Ec2.Inputs;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
{
    var group = new SecurityGroup("web-sg", new SecurityGroupArgs {
        Description = "Enable HTTP access",
        Ingress = {
            new SecurityGroupIngressArgs {
                Protocol = "tcp",
                FromPort = 80,
                ToPort = 80,
                CidrBlocks = { "0.0.0.0/0" }
            }
        }
    });

    var server = new Instance("web-server", new InstanceArgs {
        Ami = "ami-0319ef1a70c93d5c8",
        InstanceType = "t2.micro",
        VpcSecurityGroupIds = { group.Id }
    });

    return new Dictionary<string, object?>
    {
        ["publicIp"] = server.PublicIp,
        ["publicDns"] = server.PublicIp,
    };
});
```

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.aws.ec2.Instance;
import com.pulumi.aws.ec2.InstanceArgs;
import com.pulumi.aws.ec2.SecurityGroup;
import com.pulumi.aws.ec2.SecurityGroupArgs;
import com.pulumi.aws.ec2.inputs.SecurityGroupIngressArgs;

import java.util.List;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {

        var group = new SecurityGroup("web-sg",
            SecurityGroupArgs.builder()
            .description("Enable HTTP access")
            .ingress(SecurityGroupIngressArgs.builder()
                .protocol("tcp")
                .fromPort(80)
                .toPort(80)
                .cidrBlocks("0.0.0.0/0")
                .build())
            .build());

        var server = new Instance("web-server",
            InstanceArgs.builder()
                .ami("ami-0319ef1a70c93d5c8")
                .instanceType("t2.micro")
                .vpcSecurityGroupIds(group.id().applyValue(List::of))
                .build());

        ctx.export("publicIp", server.publicIp());
        ctx.export("publicDns", server.publicDns());
    }
}
```

```yaml
name: aws-ec2-instance-with-sg-yaml
runtime: yaml
description: An example that shows how to create an EC2 instance and security group.
resources:
  group:
    type: aws:ec2:SecurityGroup
    properties:
      description: Enable HTTP access
      ingress:
        - protocol: tcp
          fromPort: 80
          toPort: 80
          cidrBlocks:
            - 0.0.0.0/0
  server:
    type: aws:ec2:Instance
    properties:
      ami: ami-0319ef1a70c93d5c8
      instanceType: t2.micro
      vpcSecurityGroupIds:
        - ${group.id}
outputs:
  publicIp: ${server.publicIp}
  publicDns: ${server.publicDns}
```

## Concepts in depth

### Core concepts

- How Pulumi IaC Works — Learn how the language host, deployment engine, and resource providers work together under the hood.
- Pulumi Cloud — Learn how Pulumi Cloud relates to the open source tool and what it offers for teams.
- Projects — Learn how Pulumi projects are organized and configured.
- Stacks — Learn how to create and deploy stacks.
- Resources — Learn more about how to use and manage resources in your programs.
- Resource options — Learn more about how to use and manage resource options in your program.
- Inputs and outputs — Learn how to use resource properties to handle dependencies between resources.

### Configuration and state

- Configuration — Learn how to configure stacks for different deployment scenarios.
- Secrets — Learn how to handle sensitive data and store secret encrypted settings in Pulumi.
- Environments (ESC) — Learn how to configure your deployment environments with Pulumi ESC.
- State and backends — Learn how Pulumi stores state and manages concurrency.
- Update plans — Learn about how to constrain your deployments with update plans.

### Reference

- Glossary — Look up definitions for commonly used terms.
- Comparisons — Learn about how Pulumi compares to other infrastructure tools.
- Converters — Learn how to translate IaC from other tools into Pulumi programs.
