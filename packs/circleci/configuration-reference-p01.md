---
title: "Configuration reference (part 1/3)"
source: https://circleci.com/docs/configuration-reference/
domain: circleci
license: CC-BY-SA-4.0
tags: circleci pipeline, continuous integration, ci cd pipeline, build automation
fetched: 2026-07-02
part: 1/3
---

# Configuration reference

13 days ago

Cloud

Server v4+

- View markdown

This document is a reference for the CircleCI 2.x configuration keys that are used in the `.circleci/config.yml` file.

You can see a complete `config.yml` in our full example.


## **`version`**

The `version` field is intended to be used in order to issue warnings for deprecation or breaking changes.

| Key | Required | Type | Description |
|---|---|---|---|
| `version` | Y | String | `2`, `2.0`, or `2.1`. See the Reusable Configuration page for an overview of 2.1 keys available to simplify your `.circleci/config.yml` file, reuse, and parameterized jobs. |

**Example:**

Version

```dracula
version: 2.1
```


## **`setup`**

The `setup` field enables you to conditionally trigger configurations from outside the primary `.circleci` parent directory, update pipeline parameters, or generate customized configurations.

| Key | Required | Type | Description |
|---|---|---|---|
| `setup` | N | Boolean | Designates the `config.yaml` for use of CircleCI’s Dynamic Configuration feature. |

**Example:**

```dracula
version: 2.1

setup: true
```


## **`orbs`**

|   | The `orbs` key is supported in `version: 2.1` configuration |
|---|---|

Use the `orbs` key to reference or define reusable configuration blocks (orbs) for use in your configuration.

| Key | Required | Type | Description |
|---|---|---|---|
| `orbs` | N | Map | A map of user-selected names to either: orb references (strings) or orb definitions (maps). Orb definitions must be the orb-relevant subset of 2.1 config. See the Creating Orbs documentation for details. |
| `executors` | N | Map | A map of strings to executor definitions. See the **`executors`** section below. |
| `commands` | N | Map | A map of command names to command definitions. See the **`commands`** section below. |

The following example uses the `node` orb that exists in the certified `circleci` namespace. Refer to the Node orb page in the Orb Registry for more examples and information.

**Example:**

```dracula
version: 2.1

orbs:
  node: circleci/node@x.y

jobs:
  install-node-example:
    docker:
      - image: cimg/base:stable
    steps:
      - checkout
      - node/install:
          install-yarn: true
          node-version: '16.13'
      - run: node --version
workflows:
  test_my_app:
    jobs:
      - install-node-example
```

Documentation is available for orbs in the following sections:

- Using Orbs.
- Authoring Orbs.

Public orbs are listed in the Orb Registry.


## **`commands`**

|   | The `commands` key is supported in `version: 2.1` configuration |
|---|---|

A `command` defines a sequence of steps as a map to be executed in a job, enabling you to reuse a single command definition across multiple jobs. For more information see the Reusable Config Reference Guide.

| Key | Required | Type | Description |
|---|---|---|---|
| `steps` | Y | Sequence | A sequence of steps run inside the calling job of the command. |
| `parameters` | N | Map | A map of parameter keys. See the Parameter Syntax section of the Reusing Config document for details. |
| `description` | N | String | A string that describes the purpose of the command. |

**Example:**

```dracula
version: 2.1

commands:
  sayhello:
    description: "A very simple command for demonstration purposes"
    parameters:
      to:
        type: string
        default: "Hello World"
    steps:
      - run: echo << parameters.to >>
```


## **`parameters`**

|   | The pipeline `parameters` key is supported in `version: 2.1` configuration |
|---|---|

Use the `parameters` key at the top level of your config to declare *pipeline parameters* for use in the configuration. See Pipeline Values and Parameters for usage details.

| Key | Required | Type | Description |
|---|---|---|---|
| `parameters` | N | Map | A map of parameter keys. Supports `string`, `boolean`, `integer` and `enum` types. See Parameter Syntax for details. |

**Example:**

This example declares a pipeline parameter named `image-tag` with a type of `string` and a default value of `current`.

```dracula
version: 2.1

parameters:
  image-tag:
    type: string
    default: "current"
```

Once you have declared a pipeline parameter, you can pass a pipeline parameter value when triggering a pipeline via the API or from the CircleCI web app.


## **`executors`**

|   | The `executors` key is supported in `version: 2.1` configuration |
|---|---|

Executors define the execution environment where job steps run, letting you reuse a single executor definition across multiple jobs.

| Key | Required | Type | Description |
|---|---|---|---|
| `docker` | Y (1) | List | Options for Docker executor |
| `resource_class` | N | String | Amount of CPU and RAM allocated to each container in a job. |
| `machine` | Y (1) | Map | Options for machine executor |
| `macos` | Y (1) | Map | Options for macOS executor |
| `windows` | Y (1) | Map | Windows executor currently working with orbs. Check out the orb. |
| `shell` | N | String | Shell to use for execution command in all steps. Can be overridden by `shell` in each step (default: See Default Shell Options) |
| `working_directory` | N | String | The directory where steps run. CircleCI interprets this as an absolute path. |
| `environment` | N | Map | A map of environment variable names and values. |

(1) Specify one executor type per job. If you set more than one, CircleCI returns an error.

**Example:**

```dracula
version: 2.1
executors:
  my-executor:
    docker:
      - image: cimg/ruby:3.0.3-browsers

jobs:
  my-job:
    executor: my-executor
    steps:
      - run: echo "Hello executor!"
```

See the Using Parameters in Executors section of the Reusing Config page for examples of parameterized executors.


## **`jobs`**

A Workflow is comprised of one or more uniquely named jobs. Jobs are specified in the `jobs` map, see Sample Config.yml for two examples of a `job` map. The name of the job is the key in the map, and the value is a map describing the job.

Jobs have a maximum runtime based on pricing plan, as follows:

- 1 hour (Free).
- 3 hours (Performance).
- 5 hours (Scale).

If your jobs are timing out, consider the following:

- A larger **`resource_class`**.
- Using Parallelism.
- Run some of your jobs concurrently using Workflows.
- You can upgrade your pricing plan.

**Example:**

```dracula
version: 2.1

jobs:
  my-job:
    docker:
      - image: cimg/base:2024.12
    resource_class: xlarge
    steps:
      ... // other config
```

### **<`job_name`>**

Each job consists of the job’s name as a key and a map as a value. A name must be unique and case-insensitive within the `jobs` list. The value map has the following attributes:

| Key | Required | Type | Description |
|---|---|---|---|
| `type` | N | String | Job type, can be `build`, `release`, `no-op`, or `approval`. If not specified, defaults to `build`. |
| `docker` | Y (1) | List | Options for the Docker executor |
| `machine` | Y (1) | Map | Options for the machine executor |
| `macos` | Y (1) | Map | Options for the macOS executor |
| `executor` | Y (1) | String | Name of a declared reusable executor |
| `shell` | N | String | Shell to use for execution command in all steps. Can be overridden by `shell` in each step (default: See Default Shell Options) |
| `parameters` | N | Map | Parameters for making a `job` explicitly configurable in a `workflow`. |
| `steps` | Y | List | A list of steps to be performed |
| `working_directory` | N | String | The directory where steps run. CircleCI interprets this as an absolute path. Default: `~/project` (where `project` is a literal string, not your specific project name). Processes running during the job can use the `$CIRCLE_WORKING_DIRECTORY` environment variable to refer to this directory. **Note:** CircleCI does not expand paths in your YAML configuration file; if your `store_test_results.path` is `$CIRCLE_WORKING_DIRECTORY/tests`, CircleCI attempts to store the `test` subdirectory of the directory literally named `$CIRCLE_WORKING_DIRECTORY`, including the dollar sign `$`. CircleCI creates `working_directory` automatically if it doesn’t exist. |
| `parallelism` | N | Integer | Number of parallel instances of this job to run (default: 1) |
| `environment` | N | Map | A map of environment variable names and values. |
| `branches` | N | Map | This key is deprecated. Use workflows filtering to control which jobs run for which branches. |
| `resource_class` | N | String | Amount of CPU and RAM allocated to each container in a job. |
| `retention` | N | Map | Configure job retention periods for cache data (1-15 days, for example, "1d", "7d", "15d"). This reduces retention from the organization-level default, automatically removing cache data after the specified period. |

(1) Specify one executor type per job. If you set more than one, CircleCI returns an error.

**Example:**

In this example the job name is `my-job`.

```dracula
version: 2.1

jobs:
  my-job:
```

#### `type`

Configure a job type. Options are `release`, `approval`, `no-op`, `build` (default).

If a type is not specified, the job defaults to a `build` type.

**Example** of a job with a `build` type. `build` is the default type and does not need to be configured:

```dracula
jobs:
  my-job:
    docker:
      - image: cimg/base:2024.12
    resource_class: xlarge
    steps:
      ... // other config
```

Jobs with the `release` type are used to Connect Your Pipeline Configuration to a deployment in the CircleCI deploys UI. For full details, see the Deploys Overview page.

**Example** of a job with a `release` type:

```dracula
jobs:
  release-my-service:
    type: release
    plan_name: <my-service-release>
```

The `no-op` type is used to configure a job that performs no actions and consumes no credits. `no-op` is commonly used to organize the order of operations within a workflow and make it easier to maintain. Only the `type` is required for a `no-op` type job, no further job configuration is required. For some examples of using `no-op` jobs, see the Orchestration Cookbook.

**Example** of a job with a `no-op` type:

```dracula
jobs:
  my-no-op-job:
    type: no-op
```

The `approval` type is used to configure a manual approval step. No `job` configuration is required or allowed for an `approval` type job. The `approval` type is most commonly configured within a workflow rather than under the top-level `jobs` key. Only `approval` type jobs can have their `type` configured under `workflows`. See type under workflows section for full details.

**Example** of a job with an `approval` type, configured under `workflows`:

```dracula
workflows:
  my-workflow:
    jobs:
      - build
      - test:
          requires:
            - build
      - hold:
          type: approval
          requires:
            - test
      - deploy:
          requires:
            - hold
```

#### `environment`

A map of environment variable names and values. For more information on defining and using environment variables, and the order of precedence governing the various ways they can be set, see the Environment Variables page.

**Example** to show setting an environment variable named `FOO` with a value of `bar` for use in a job.

```dracula
version: 2.1

jobs:
  build:
    docker:
      - image: cimg/base:2022.04-20.04
    environment:
      FOO: bar
```

#### `retention`

Configure job retention periods to control how long job data is kept. Job retention specifically controls cache retention at the job level. This setting can be configured from 1 day to 15 days using string values (for example, "1d", "7d", "15d"). Job retention reduces the organization-level retention from the default by automatically removing cache data after the specified period.

**Example:**

```dracula
version: 2.1

jobs:
  test:
    docker:
      - image: cimg/node:18.0
    retention:
      caches: 7d
    steps:
      - checkout
      - run: npm install
      - run: npm test
```

For more information on cache retention, see the Persisting Data Overview page.

#### Common errors

When configuring job retention, you may encounter the following validation errors:

- **Invalid time format**: The retention period must use the format `^([1-9]|[12][0-9]|30)d$` (1-30 days with "d" suffix). For example, use `"7d"` instead of `"12h"` or `"1w"`.
- **Incorrect data type**: The `retention` key expects a map with `caches` as a string value, not a direct string.

**Examples:**

Incorrect - direct string value

```dracula
# Incorrect - direct string value
jobs:
  say-hello:
    retention: "12h"  # Error: expected type: String, found: Mapping
```

Incorrect - invalid time format

```dracula
#Incorrect - invalid time format
jobs:
  say-hello:
    retention:
      caches: "12h"  # Error: does not match pattern ^([1-9]|[12][0-9]|30)d$
```

Correct format

```dracula
# Correct format
jobs:
  say-hello:
    retention:
      caches: "7d"   # Valid: 7 days
```

#### `parallelism`

Use this feature to optimize test steps. If you set `parallelism` to N > 1, CircleCI sets up N independent executors, and each runs the job’s steps in parallel.

You can use the CircleCI CLI to split your test suite across parallel containers so the job completes in a shorter time.

- Read more about splitting tests across parallel execution environments on the Parallelism and Test Splitting page.
- Refer to the Use the CircleCI CLI to Split Tests how-to guide.
- Follow the Test Splitting Tutorial.

- Use an integer
- Use an expression

```dracula
jobs:
  build:
    docker:
      - image: cimg/base:2024.12
    environment:
      FOO: bar
    parallelism: 3
    resource_class: large
    working_directory: ~/my-app
    steps:
      - run: go list ./... | circleci tests run --command "xargs gotestsum --junitfile junit.xml --format testname --" --split-by=timings --timings-type=name
```

```dracula
jobs:
  build:
    docker:
      - image: cimg/base:2024.12
    environment:
      FOO: bar
    parallelism: << pipeline.git.branch == "main" and 10 or 1 >>
    resource_class: large
    working_directory: ~/my-app
    steps:
      - run: go list ./... | circleci tests run --command "xargs gotestsum --junitfile junit.xml --format testname --" --split-by=timings --timings-type=name
```

#### `parameters`

Job-level `parameters` can be used when calling a `job` in a `workflow`.

Reserved parameter-names:

- `name`
- `requires`
- `context`
- `type`
- `filters`
- `matrix`

See Parameter Syntax for definition details.

**Example** to show using a job parameter to set the parallelism for a job when a workflow is run.

```dracula
version: 2.1

jobs:
  build:
    parameters:
      my-parameter:
        type: integer
        default: 1
    parallelism: << parameters.my-parameter >>
    docker:
      - image: cimg/base:2023.11
    steps:
      - checkout

workflows:
  workflow:
    jobs:
      - build:
          my-parameter: 2
```


## Executor **`docker`** / **`machine`** / **`macos`**

CircleCI offers several execution environments in which to run your jobs. To specify an execution environment choose an *executor*, then specify an image and a resource class. An executor defines the underlying technology, environment, and operating system in which to run a job.

Set up your jobs to run using the `docker` (Linux), `machine` (LinuxVM, Windows, GPU, Arm), or `macos` executor, then specify an image with the tools and packages you need, and a resource class.

Learn more about execution environments and executors in the Introduction to Execution Environments.

### `docker`

Configure a job to use the Docker execution environment using the `docker` key which takes a list of maps:

| Key | Required | Type | Description |
|---|---|---|---|
| `image` | Y | String | The name of a custom Docker image to use. The first `image` listed under a job defines the job’s own primary container image where all steps will run. |
| `name` | N | String | `name` defines the hostname for the container (the default is `localhost`), which is used for reaching secondary (service) containers. By default, all services are exposed directly on `localhost`. This field is useful if you would rather have a different hostname instead of `localhost`, for example, if you are starting multiple versions of the same service. |
| `entrypoint` | N | String or List | The command used as executable when launching the container. `entrypoint` overrides the image’s `ENTRYPOINT`. |
| `command` | N | String or List | The command to use as PID 1 (or as arguments for entrypoint) when launching the container. `command` overrides the image’s `COMMAND`. If the image has an `ENTRYPOINT`, Docker uses `command` as arguments to it. If the image has no `ENTRYPOINT`, Docker uses `command` as the executable. |
| `user` | N | String | Which user to run commands as within the Docker container |
| `environment` | N | Map | A map of environment variable names and values. The `environment` settings apply to the entrypoint/command run by the Docker container, not the job steps. |
| `auth` | N | Map | Authentication for registries using standard `docker login` credentials |
| `aws_auth` | N | Map | Authentication for AWS Elastic Container Registry (ECR) |
| `gcp_auth` | N | Map | Authentication for GCP Artifact Registry using OIDC |

For a Primary Container, (the first container in the list) if neither `command` nor `entrypoint` is specified in the configuration, then any `ENTRYPOINT` and `COMMAND` in the image are ignored. The primary container is typically only used for running the `steps` and not for its `ENTRYPOINT`, and an `ENTRYPOINT` may consume significant resources or exit prematurely.

A Custom Image may disable this behavior and force the `ENTRYPOINT` to run.

You can specify image versions using tags or digest. You can use any public images from any public Docker registry (defaults to Docker Hub). Learn more about specifying images on the Using the Docker Execution Environment page.

**Example:**

```dracula
version: 2.1

jobs:
  hello-job:
    docker:
      - image: cimg/node:17.2.0 # the primary container, where your job's commands are run
    steps:
      - checkout # check out the code in the project directory
      - run: echo "hello world" # run the `echo` command

workflows:
  my-workflow:
    jobs:
      - hello-job
```

#### Docker registry authentication

Some registries, Docker Hub, for example, may rate limit anonymous Docker pulls. We recommend that you authenticate to pull private and public images. The username and password can be specified in the `auth` field. See Using Docker Authenticated Pulls for details.

**Example:**

```dracula
jobs:
  build:
    docker:
      - image: buildpack-deps:trusty # primary container
        auth:
          username: mydockerhub-user
          password: $DOCKERHUB_PASSWORD  # context / project UI env-var reference
        environment:
          ENV: CI

      - image: mongo:2.6.8
        auth:
          username: mydockerhub-user
          password: $DOCKERHUB_PASSWORD  # context / project UI env-var reference
        command: [--smallfiles]

      - image: postgres:14.2
        auth:
          username: mydockerhub-user
          password: $DOCKERHUB_PASSWORD  # context / project UI env-var reference
        environment:
          POSTGRES_USER: user

      - image: redis@sha256:54057dd7e125ca41afe526a877e8bd35ec2cdd33b9217e022ed37bdcf7d09673
        auth:
          username: mydockerhub-user
          password: $DOCKERHUB_PASSWORD  # context / project UI env-var reference

      - image: acme-private/private-image:321
        auth:
          username: mydockerhub-user
          password: $DOCKERHUB_PASSWORD  # context / project UI env-var reference
```

#### AWS authentication

Using an image hosted on AWS ECR requires authentication using AWS credentials. The two configuration options are described in the following sections.

#### Use OIDC

Authenticate using OpenID Connect (OIDC) using the `oidc_role_arn` field, as follows:

**Example:**

```dracula
jobs:
  job_name:
    docker:
      - image: <your-image-arn>
        aws_auth:
          oidc_role_arn: <your-iam-role-arn>
```

For steps to get set up with OIDC to pull images from AWS ECR, see the Pull an Image From AWS ECR With OIDC page.

#### Use environment variables

By default, CircleCI uses the AWS credentials you provide by setting the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` project environment variables. It is also possible to set the credentials by using the `aws_auth` field as in the following example:

**Example:**

```dracula
jobs:
  build:
    docker:
      - image: account-id.dkr.ecr.us-east-1.amazonaws.com/org/repo:0.1
        aws_auth:
          aws_access_key_id: AKIAQWERVA  # can specify string literal values
          aws_secret_access_key: $ECR_AWS_SECRET_ACCESS_KEY  # or project UI envar reference
```

#### GCP authentication

Using an image hosted on GCP Artifact Registry requires authentication using GCP credentials, either via OIDC, or by setting environment variables. The two configuration options are described in the following sections:

#### Use OIDC

Authenticate using OpenID Connect (OIDC) using the `gcp_auth` field, as follows:

**Example:**

```dracula
jobs:
  job_name:
    docker:
      - image: <region>-docker.pkg.dev/<project>/<repository>/<image>:<tag>
        gcp_auth:
          oidc_service_account: <service-account-email>
          workload_identity_pool: projects/<project-number>/locations/global/workloadIdentityPools/<pool-id>
          workload_identity_provider: <provider-id>
```

For steps to get set up with OIDC to pull images from GCP Artifact Registry, see the Pull an Image From GCP Artifact Registry With OIDC page.

#### Use environment variables

By default, CircleCI uses the GCP credentials you provide by setting the `GCP_OIDC_SERVICE_ACCOUNT`, `GCP_WORKLOAD_IDENTITY_POOL`, and `GCP_WORKLOAD_IDENTITY_PROVIDER` project environment variables or context environment variables. When these are set and the image is hosted on GCP Artifact Registry, CircleCI automatically authenticates without requiring a `gcp_auth` field in your configuration:

**Example:**

```dracula
jobs:
  build:
    docker:
      - image: us-docker.pkg.dev/my-project/my-repo/my-image:latest
```

### **`machine`**

|   | **Using CircleCI Cloud?** The use of `machine: true` is deprecated. You must specify an image to use. |
|---|---|

The machine executor is configured using the `machine` key, which takes a map:

| Key | Required | Type | Description |
|---|---|---|---|
| `image` | Y | String | The virtual machine image to use. View available images. **Note:** This key is **not** supported for Linux VMs on installations of CircleCI Server. For information about customizing `machine` executor images on CircleCI installed on your servers, see our Machine Provisioner Documentation. |
| `docker_layer_caching` | N | Boolean | Set this to `true` to enable Docker Layer Caching. |

**Example:**

- Cloud
- Server

```dracula
jobs:
  build: # name of your job
    machine: # executor type
      image: ubuntu-2004:current # recommended linux image

    steps:
      # Commands run in a Linux virtual machine environment
```

```dracula
jobs:
  build: # name of your job
    machine: true # executor type
    steps:
      # Commands run in a Linux virtual machine environment
```

#### Linux `machine` images

**Specifying an image in your configuration file is strongly recommended.** CircleCI supports multiple Linux machine images that can be specified in the `image` field. For a full list of supported image tags, refer to the following pages in the Developer Hub:

- Ubuntu-2204
- Ubuntu-2404
- Ubuntu-2604

More information on the software available in each image can be found in our Discuss forum.

The machine executor supports Docker Layer Caching, which is useful when you are building Docker images during your job or Workflow.

#### Linux `machine` images on server

If you are using CircleCI Server, contact your system administrator for details of available Linux machine images.

#### Linux GPU `machine` images

When using the Linux GPU Executor, the available images are:

- `linux-cuda-11:default` v11.4, v11.6, v11.8 (default), Docker v20.10.24.
- `linux-cuda-12:default` v12.0, v12.1 (default), Docker v20.10.24.

#### Android `machine` images

CircleCI supports running jobs on Android for testing and deploying Android applications.

To use the Android image directly with the machine executor, add the following to your job:

```dracula
version: 2.1

jobs:
  build:
    machine:
      image: android:2024.11.1
```

The Android image can also be accessed using the Android orb.

For examples, refer to the Using Android Images With the Machine Executor page.

#### Windows `machine` images

**Specifying an image in your configuration file is strongly recommended.** CircleCI supports multiple Windows machine images that can be specified in the `image` field.

For a full list of supported images, refer to one of the following:

- `windows-server-2022-gui` image
- `windows-server-2019` image

More information on what software is available in each image can be found in our Discuss forum.

Alternatively, use the Windows orb to manage your Windows execution environment. For examples, see the Using the Windows Execution Environment page.

#### Windows `machine` images on server

If you are using CircleCI Server, contact your system administrator for details of available Windows machine images.

#### Windows GPU `machine` image

When using the Windows GPU Executor, the available image is:

- `windows-server-2019-cuda`

**Example:**

```dracula
version: 2.1

jobs:
  build:
    machine:
      image: windows-server-2019-cuda:current
```

### **`macos`**

CircleCI supports running jobs on macOS, to allow you to build, test, and deploy apps for macOS, iOS, tvOS and watchOS. To run a job on a macOS virtual machine, add the `macos` key to the top-level configuration for your job and specify the version of Xcode to use.

| Key | Required | Type | Description |
|---|---|---|---|
| `xcode` | Y | String | The version of Xcode that is installed on the virtual machine, see the Supported Xcode Versions Section of the Testing iOS document for the complete list. |

**Example:** Use a macOS virtual machine with Xcode version 26.4.0:

```dracula
jobs:
  build:
    macos:
      xcode: 26.4.0
```

#### **`branches` - DEPRECATED**

This key is deprecated. Use workflows filtering to control which jobs run for which branches.


## **`resource_class`**

The `resource_class` feature allows you to configure CPU and RAM resources for each job. Resource classes are available for each execution environment, as described in the tables below. A resource class is also used as a label to identify a pool of self-hosted runners and to route a job to that pool. For full details on both uses, see the Resource Class Overview page.

We implement soft concurrency limits for each resource class to ensure our system remains stable for all customers. If you are on a Performance or Custom Plan and experience queuing for certain resource classes, it is possible you are hitting these limits. Contact CircleCI support to request a raise on these limits for your account.

If you do not specify a resource class, CircleCI uses a default value that can change. Specify a resource class instead of relying on a default.

|   | Java, Erlang and any other languages that introspect the `/proc` directory for information about CPU count may require additional configuration to prevent them from slowing down when using the CircleCI resource class feature. Programs with this issue may request 32 CPU cores and run slower than they would when requesting one core. Users of languages with this issue must pin their CPU count to their guaranteed CPU resources. |
|---|---|

|   | If you want to confirm how much memory you have been allocated, you can check the cgroup memory hierarchy limit with `grep hierarchical_memory_limit /sys/fs/cgroup/memory/memory.stat`. |
|---|---|

### Self-hosted runner

Use the `resource_class` key to configure a Self-hosted Runner Instance.

For example:

```dracula
jobs:
  job_name:
    machine: true
    resource_class: <my-namespace>/<my-runner>
```

### Docker execution environment

Set a resource class for a Docker job

```dracula
jobs:
  build:
    docker:
      - image: cimg/base:2024.12
    resource_class: xlarge
    steps:
      ... // other config
```

Set a resource class for a Docker job using an expression

```dracula
jobs:
  build:
    docker:
      - image: cimg/base:2024.12
    resource_class: << pipeline.git.branch == "main" and "xlarge" or "medium" >>
    steps:
      ... // other config
```

#### x86

|   | For credit and access information, see the Resource classes page. Resource class access is dependent on your Plan. |
|---|---|

| Class | vCPUs | RAM | Cloud | Server |
|---|---|---|---|---|
| `small` | 1 | 2GB | **Yes** | **Yes** |
| `medium` | 2 | 4GB | **Yes** | **Yes** |
| `medium+` | 3 | 6GB | **Yes** | **Yes** |
| `large` | 4 | 8GB | **Yes** | **Yes** |
| `xlarge` | 8 | 16GB | **Yes** | **Yes** |
| `2xlarge` | 16 | 32GB | **Yes** | **Yes** |
| `2xlarge+` | 20 | 40GB | **Yes** | **Yes** |

#### x86 (gen2)

|   | Docker gen2 resource classes are available on paid plans only. For credit and access information, see the Resource classes page. |
|---|---|

| Class | vCPUs | RAM | Cloud | Server |
|---|---|---|---|---|
| `small.gen2` | 1 | 2GB | **Yes** | **No** |
| `medium.gen2` | 2 | 4GB | **Yes** | **No** |
| `medium+.gen2` | 3 | 6GB | **Yes** | **No** |
| `large.gen2` | 4 | 8GB | **Yes** | **No** |
| `xlarge.gen2` | 8 | 16GB | **Yes** | **No** |
| `2xlarge.gen2` | 16 | 32GB | **Yes** | **No** |
| `2xlarge+.gen2` | 20 | 40GB | **Yes** | **No** |

Set a resource class for a Docker job

```dracula
jobs:
  build:
    docker:
      - image: cimg/base:2024.12
    resource_class: xlarge.gen2
    steps:
      ... // other config
```

Set a resource class for a Docker job using an expression

```dracula
jobs:
  build:
    docker:
      - image: cimg/base:2024.12
    resource_class: << pipeline.git.branch == "main" and "xlarge.gen2" or "medium.gen2" >>
    steps:
      ... // other config
```

#### Arm

**Arm on Docker** For credit and access information, see the Resource classes page. Resource class access is dependent on your Plan

To find out which CircleCI Docker convenience images support Arm resource classes, you can refer to Docker Hub:

1. Select the image (for example, `cimg/python`).
2. Select the **tags** tab.
3. View what is supported under **OS/ARCH** for the latest tags. For example, `cimg/python` has `linux/amd64` and `linux/arm64`, which means Arm **is** supported.

| Class | vCPUs | RAM | Cloud | Server |
|---|---|---|---|---|
| `arm.medium` | 2 | 8 GB | **Yes** | **No** |
| `arm.large` | 4 | 16 GB | **Yes** | **No** |
| `arm.xlarge` | 8 | 32 GB | **Yes** | **No** |
| `arm.2xlarge` | 16 | 64 GB | **Yes** | **No** |

#### LinuxVM execution environment

| Class | vCPUs | RAM | Disk Size | Cloud | Server |
|---|---|---|---|---|---|
| `medium` | 2 | 7.5 GB | 150GB | **Yes** | **Yes** |
| `large` | 4 | 15 GB | 150GB | **Yes** | **Yes** |
| `xlarge` | 8 | 32 GB | 150GB | **Yes** | **Yes** |
| `2xlarge` | 16 | 64 GB | 150GB | **Yes** | **Yes** |
| `2xlarge+` | 32 | 64 GB | 150GB | **Yes** | **Yes** |

**Example:**

- Cloud
- Server

```dracula
jobs:
  build:
    machine:
      image: ubuntu-2004:2024.01.2 # recommended linux image
    resource_class: large
    steps:
      ... // other config
```

```dracula
jobs:
  build:
    machine: true
    resource_class: large
    steps:
      ... // other config
```

#### LinuxVM (gen2) execution environment

| Class | vCPUs | RAM | Disk Size | Cloud | Server |
|---|---|---|---|---|---|
| `medium.gen2` | 2 | 8 GiB | 150GB | **Yes** | **No** |
| `large.gen2` | 4 | 16 GiB | 150GB | **Yes** | **No** |
| `xlarge.gen2` | 8 | 32 GiB | 150GB | **Yes** | **No** |
| `2xlarge.gen2` | 16 | 64 GiB | 150GB | **Yes** | **No** |
| `2xlarge+.gen2` | 32 | 128 GiB | 150GB | **Yes** | **No** |

**Example:**

```dracula
jobs:
  build:
    machine:
      image: ubuntu-2404:current # recommended linux image
    resource_class: large.gen2
    steps:
      ... // other config
```

#### macOS execution environment

| Class | vCPUs | RAM | Cloud | Server |
|---|---|---|---|---|
| `m4pro.medium` | 6 @ 4.51 GHz | 28GB | **Yes** | **No** |
| `m4pro.large` | 12 @ 4.51 GHz | 56GB | **Yes** | **No** |

**Example:**

```dracula
jobs:
  build:
    macos:
      xcode: 26.4.0
    resource_class: m4pro.medium
    steps:
      ... // other config
```

#### macOS execution environment on server

If you are working on CircleCI Server you can access the macOS execution environment using Self-hosted Runner.

#### Windows execution environment

| Class | vCPUs | RAM | Disk Size | Cloud | Server |
|---|---|---|---|---|---|
| `windows.medium` (default) | 4 | 16GB | 200 GB | **Yes** | **Yes** |
| `windows.large` | 8 | 32GB | 200 GB | **Yes** | **Yes** |
| `windows.xlarge` | 16 | 64GB | 200 GB | **Yes** | **Yes** |
| `windows.2xlarge` | 32 | 128GB | 200 GB | **Yes** | **Yes** |

|   | **Using server?** Check with your systems administrator whether you have access to the Windows execution environment. |
|---|---|

**Example:**

- Cloud
- Server

```dracula
version: 2.1

jobs:
  build: # name of your job
    resource_class: 'windows.medium'
    machine:
      image: 'windows-server-2022-gui:current'
      shell: 'powershell.exe -ExecutionPolicy Bypass'
    steps:
      # Commands are run in a Windows virtual machine environment
      - checkout
      - run: Write-Host 'Hello, Windows'
```

```dracula
version: 2.1

jobs:
  build: # name of your job
    machine:
      image: windows-default
    steps:
      # Commands are run in a Windows virtual machine environment
      - checkout
      - run: Write-Host 'Hello, Windows'
```

#### GPU execution environment (Linux)

Class

vCPUs

RAM

GPUs

GPU model

GPU Memory (GiB)

Disk Size (GiB)

Cloud

Server

`gpu.nvidia.small`

4

16

1

NVIDIA Tesla P4

16

150

**Yes**

**No**

`gpu.nvidia.small.gen2`

4

16

1

NVIDIA A10G

24

150

**Yes**

**No**

`gpu.nvidia.small.multi`

4

15

2

NVIDIA Tesla T4

16

150

**Yes**

**No**

`gpu.nvidia.medium.multi`

8

30

4

NVIDIA Tesla T4

16

150

**Yes**

**No**

`gpu.nvidia.medium`

8

30

1

NVIDIA Tesla T4

16

150

**Yes**

**No**

`gpu.nvidia.large`

8

30

1

NVIDIA Tesla V100

16

150

**Yes**

**No**

**Example:**

```dracula
version: 2.1

jobs:
  build:
    machine:
      image: linux-cuda-12:default
    resource_class: gpu.nvidia.medium
    steps:
      - run: nvidia-smi
      - run: docker run --gpus all nvidia/cuda:9.0-base nvidia-smi
```

See the Available Linux GPU images section for the full list of available images.

#### GPU execution environment (Windows)

Class

vCPUs

RAM

GPUs

GPU model

GPU Memory (GiB)

Disk Size (GiB)

Cloud

Server

`windows.gpu.nvidia.medium`

16

60

1

NVIDIA Tesla T4

16

200

**Yes**

**No**

**Example:**

```dracula
version: 2.1

orbs:
  win: circleci/windows@5.0.0

jobs:
  build:
    executor: win/server-2019-cuda
    steps:
      - checkout
      - run: '&"C:\Program Files\NVIDIA Corporation\NVSMI\nvidia-smi.exe"'
```

(2) *This resource requires review by our support team. Open a support ticket if you would like to request access.*

#### Arm VM execution environment

| Class | vCPUs | RAM | Disk Size | Cloud | Server |
|---|---|---|---|---|---|
| `arm.medium` (default) | 2 | 8GB | 100 GB | **Yes** | **Yes** |
| `arm.large` | 4 | 16GB | 100 GB | **Yes** | **Yes** |
| `arm.xlarge` | 8 | 32GB | 100 GB | **Yes** | **Yes** |
| `arm.2xlarge` | 16 | 64GB | 100 GB | **Yes** | **Yes** |

|   | **Using server?** Check with your systems administrator whether you have access to the Arm execution environment. |
|---|---|

**Example:**

- Cloud
- Server

```dracula
jobs:
  my-job:
    machine:
      image: ubuntu-2004:2024.01.2
    resource_class: arm.medium
    steps:
      - run: uname -a
      - run: echo "Hello, Arm!"
```

```dracula
jobs:
  my-job:
    machine:
      image: arm-default
    resource_class: arm.medium
    steps:
      - run: uname -a
      - run: echo "Hello, Arm!"
```
