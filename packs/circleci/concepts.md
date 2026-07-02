---
title: "Concepts"
source: https://circleci.com/docs/concepts/
domain: circleci
license: CC-BY-SA-4.0
tags: circleci pipeline, continuous integration, ci cd pipeline, build automation
fetched: 2026-07-02
---

# Concepts

13 days ago

Cloud

Server v4+

- View markdown

## Introduction

This guide introduces some basic concepts to help you understand how CircleCI manages your CI/CD pipelines.

## Concurrency

In CircleCI, *concurrency* refers to utilizing multiple containers to run multiple jobs at the same time. Concurrency is different from CircleCI *parallelism*, which splits the tests of a single job across multiple containers. To keep the system stable for all CircleCI customers, we use different soft concurrency limits on each of the Resource Classes for different executors. If you experience queueing on your jobs, you may be hitting these limits. Customers on annual plans can request an increase to those limits at no extra charge.

See the Concurrency page for more information.

## Configuration

CircleCI believes in *configuration as code*. A single file called `config.yml` orchestrates your entire CI/CD process. This file lives in a folder called `.circleci` at the root of your project and defines the entire pipeline.

Example of a directory setup using CircleCI:

```dracula
├── .circleci
│   ├── config.yml
├── README
└── all-other-project-files-and-folders
```

You can adapt your CircleCI configuration to fit the different needs of your project. The following terms, sorted in order of granularity and dependence, describe the components of most common CircleCI projects:

- **Pipeline**: Represents the entirety of your configuration.
- **Workflows**: Responsible for orchestrating multiple *jobs*.
- **Jobs**: Responsible for running a series of *steps* that perform commands.
- **Steps**: Run commands (such as installing dependencies or running tests) and shell scripts to do the work required for your project.

The following illustration uses an example Java application to show the various configuration elements:

Figure 1. Configuration elements

CircleCI configurations use YAML. See the Introduction to YAML Configurations page for basic guidance. For a full overview of what is possible in a configuration file, see the Configuration Reference page.

## Contexts

Contexts provide a mechanism for securing and sharing environment variables across projects. You define environment variables as name/value pairs, and CircleCI injects them at runtime. The process to use a context is as follows:

1. Create a context.
2. Add environment variables to the context.
3. Use the `context` key in the workflows section of a project’s configuration file to give access to the environment variables stored in the context.

Figure 2. Contexts overview

See the Using Contexts page for more information.

## Data persistence

Persist data to move data between jobs and speed up your build. Persist data using one of three methods in CircleCI:

- Artifacts
- Caches
- Workspaces.

Figure 3. Workflow illustration

Note the following distinctions between artifacts, caches, and workspaces:

| Type | Lifetime | Use | Example |
|---|---|---|---|
| Artifacts | Months | Preserve long-term artifacts. | Available in the Artifacts tab of the **Job** page under the `tmp/circle-artifacts.<hash>/container` or similar directory. |
| Caches | Months | Store non-vital data that may help the job run faster, for example npm or Gem packages. | The `save_cache` job step with a `path` to a list of directories to add and a `key` to uniquely identify the cache (for example, the branch, build number, or revision). Restore the cache with `restore_cache` and the appropriate `key`. |
| Workspaces | Duration of workflow | Attach the workspace in a downstream container with the `attach_workspace:` step. | The `attach_workspace` copies and recreates the entire workspace content when it runs. |

### Artifacts

Artifacts persist data after a workflow completes and provide longer-term storage of the outputs of your build process.

```dracula
version: 2.1

jobs:
  build1:
    docker:
      - image: cimg/base:2023.03
    steps:
      - persist_to_workspace: # Persist the specified paths (workspace/echo-output)
      # into the workspace for use in downstream job. Must be an absolute path,
      # or relative path from working_directory. This is a directory on the container which is
      # taken to be the root directory of the workspace.
          root: workspace
            # Must be relative path from root
          paths:
            - echo-output

  build2:
    machine:
      image: ubuntu-2204:2024.01.2
    steps:
      - attach_workspace:
        # Must be absolute path or relative path from working_directory
          at: /tmp/workspace
  build3:
    docker:
      - image: cimg/base:2023.03
    steps:
      - store_artifacts: # See circleci.com/docs/artifacts/ for more details.
          path: /tmp/artifact-1
          destination: artifact-file

workflows:
  my-workflow:
    jobs:
      - build1
      - build2:
          requires:
            - build1
      - build3:
          requires:
            - build1
            - build2
```

See the Storing Build Artifacts page for more information.

### Caches

A cache stores a file or directory of files such as dependencies or source code in object storage. To speed up the build, each job may contain special steps for caching dependencies from previous jobs.

If you need to clear your cache, refer to the Caching Dependencies page for more information.

```dracula
version: 2.1

jobs:
  build1:
    docker: # Each job requires specifying an executor
    # (either docker, macos, or machine), see
    # circleci.com/docs/executor-intro/ for a comparison
    # and more examples.
      - image: cimg/ruby:2.4-node
      - image: cimg/postgres:9.4.12
    steps:
      - checkout
      - save_cache: # Caches dependencies with a cache key
      # template for an environment variable,
      # see circleci.com/docs/caching/
          key: v1-repo-{{ .Environment.CIRCLE_SHA1 }}
          paths:
            - ~/circleci-demo-workflows

  build2:
    docker:
      - image: cimg/ruby:2.4-node
      - image: cimg/postgres:9.4.12
    steps:
      - restore_cache: # Restores the cached dependency.
          key: v1-repo-{{ .Environment.CIRCLE_SHA1 }}

workflows:
  my-workflow:
    jobs:
      - build1
      - build2:
          requires:
            - build1
```

For more information see the Caching Dependencies page.

### Workspaces

Workspaces are a workflow-aware storage mechanism. A workspace stores data unique to the job, which downstream jobs may need. Each workflow has a temporary workspace associated with it. Use the workspace to pass along unique data built during a job to other jobs in the same workflow.

See the Using Workspaces page for more information.

## Docker layer caching

Docker layer caching (DLC) caches the individual layers of Docker images built during your CircleCI jobs. CircleCI uses any unchanged layers on subsequent runs, rather than rebuilding the image each time.

In the `.circleci/config.yml` snippet below, the `build_elixir` job builds an image using the `ubuntu-2004:202104-01` Dockerfile. Adding `docker_layer_caching: true` below the `machine` executor key ensures CircleCI saves each Docker image layer as the Elixir image is built.

```dracula
version: 2.1

jobs:
  build_elixir:
    machine:
      image: ubuntu-2004:202104-01
      docker_layer_caching: true
    steps:
      - checkout
      - run:
          name: build Elixir image
          command: docker build -t circleci/elixir:example .

workflows:
  my-workflow:
    jobs:
      - build_elixir
```

On subsequent commits, if the Dockerfile has not changed, DLC pulls each Docker image layer from cache during the `build Elixir image` step and the image builds faster.

See the Docker Layer Caching page for more information.

## Dynamic configuration

Instead of manually creating your configuration for each CircleCI project, you can generate this configuration dynamically, based on specific pipeline parameters or file paths. Dynamic configuration is helpful where your team is working on a monorepo (or a single repository). Dynamic configuration allows you to trigger builds from *specific* parts of your project, rather than rebuilding everything each time.

See the Dynamic Configuration page for more information.

## Execution environments

Each separate job defined within your configuration runs in a unique execution environment, known as executors. An executor can be a Docker container, or a virtual machine running Linux, Windows, or macOS. In some of these instances, you can set up an environment using GPU, or Arm. CircleCI also provides a machine-based and container-based self-hosted runner solution.

Figure 4. Illustration of a CircleCI job

An *image* is a packaged system that includes instructions for creating a running container or virtual machine, and you can define an image for each executor. CircleCI provides a range of images for use with the Docker executor, called *convenience images* (details in the images section).

|   | **Using Docker?** Authenticating Docker pulls from image registries is recommended when using the Docker execution environment. Authenticated pulls allow access to private Docker images, and may also grant higher rate limits, depending on your registry provider. For further information, see Using Docker authenticated pulls. |
|---|---|

- Cloud
- Server

```dracula
version: 2.1

jobs:
  build1: # job name
    docker: # Specifies the primary container image,
      - image: cimg/base:2022.04-20.04
      - image: postgres:14.2 # Specifies the database image
        # for the secondary or service container run in a common
        # network where ports exposed on the primary container are
        # available on localhost.
        environment: # Specifies the POSTGRES_USER authentication
        # environment variable, see circleci.com/docs/env-vars/
        # for instructions about using environment variables.
          POSTGRES_USER: user
    steps:
      - checkout
#...
  build2:
    machine: # Specifies a machine image that uses
      # an Ubuntu version 20.04 image with Docker 20.10.12
      # and docker compose 1.29.2, follow CircleCI Discuss Announcements
      # for new image releases.
      image: ubuntu-2004:current
    steps:
      - checkout

#...
  build3:
    macos: # Specifies a macOS virtual machine with Xcode version 12.5.1
      xcode: "12.5.1"
    steps:
      - checkout
# ...

workflows:
  my-workflow:
    jobs:
      - build1
      - build2
      - build3
```

```dracula
version: 2.1

jobs:
  build1: # job name
    docker: # Specifies the primary container image,
      - image: cimg/base:2022.04-20.04
      - image: postgres:14.2 # Specifies the database image
        # for the secondary or service container run in a common
        # network where ports exposed on the primary container are
        # available on localhost.
        environment: # Specifies the POSTGRES_USER authentication
        # environment variable, see circleci.com/docs/env-vars/
        # for instructions about using environment variables.
          POSTGRES_USER: user
    steps:
      - checkout
#...
  build2:
    machine: true
   # Contact your system administrator for details of the image.
    steps:
      - checkout
#...

workflows:
  my-workflow:
    jobs:
      - build1
      - build2
```

The first image listed in the `.circleci/config.yml` file defines the primary container. CircleCI executes commands in the primary container. The Docker executor spins up a container with a Docker image. The machine executor spins up a complete Ubuntu virtual machine image. You can add further images to spin up secondary/service containers.

For added security when using the Docker executor and running Docker commands, use the `setup_remote_docker` key to spin up another Docker container in which to run these commands. For more information see the Running Docker Commands page.

For more information, see the Execution Environments Overview page.

## Images

An image is a packaged system that includes instructions for creating a running container. The first image listed in a `.circleci/config.yml` file defines the primary container. CircleCI executes commands for jobs in the primary container, using the Docker or machine executor.

The **Docker executor** spins up a container with a Docker image. CircleCI maintains Convenience Images for popular languages on Docker Hub.

|   | **Using Docker?** Authenticating Docker pulls from image registries is recommended when using the Docker execution environment. Authenticated pulls allow access to private Docker images, and may also grant higher rate limits, depending on your registry provider. For further information, see Using Docker authenticated pulls. |
|---|---|

The **machine executor** spins up a complete Ubuntu virtual machine image, giving you full access to OS resources and complete control over the job environment. For more information, see the Using Machine page.

```dracula
version: 2.1

jobs:
  build1: # job name
    docker: # Specifies the primary container image,
      - image: cimg/base:2022.04-20.04
      - image: postgres:14.2 # Specifies the database image
        # for the secondary or service container run in a common
        # network where ports exposed on the primary container are
        # available on localhost.
        environment: # Specifies the POSTGRES_USER authentication
        # environment variable, see circleci.com/docs/env-vars/
        # for instructions about using environment variables.
          POSTGRES_USER: user
    steps:
      - checkout
#...
  build2:
    machine: # Specifies a machine image that uses
      # an Ubuntu version 22.04 image
      image: ubuntu-2204:2024.01.2
    steps:
      - checkout

#...
  build3:
    macos: # Specifies a macOS virtual machine with Xcode version 12.5.1
      xcode: "12.5.1"
    steps:
      - checkout
# ...

workflows:
  my-workflow:
    jobs:
      - build1
      - build2
      - build3
```

See the CircleCI Images page for more information.

## Jobs

Jobs are the building blocks of your configuration. Jobs are collections of steps, which run commands/scripts as required. Each job must declare an executor that is either `docker`, `machine`, `windows`, or `macos`. For `docker` you must Specify an Image to use for the primary container. For `macos` you must specify an Xcode Version. For `windows` you must use the Windows Orb.

Figure 5. Illustration of a CircleCI job

For more information, see the Jobs and Steps page.

## Orbs

Orbs are reusable snippets of code that help automate repeated processes, accelerate project setup, and help you to integrate with third-party tools.

The illustration in the Configuration section showing an example Java configuration simplifies using orbs. The following illustration demonstrates a simplified configuration with the Maven orb. Here, the orb sets up a default executor that can execute steps with Maven and run a common job (`maven/test`).

Figure 6. Configuration using Maven orb

See Using Orbs for details on how to use orbs in your configuration and an introduction to orb design. Visit the Orbs registry to search for orbs to help simplify your configuration.

## Parallelism

The more tests your project involves, the longer it takes for them to complete on a single machine. Using *test splitting* and *parallelism*, you can spread your tests across a specified number of separate executors.

You conventionally define test suites at the Job level in your `.circleci/config.yml` file. The `parallelism` key specifies how CircleCI sets up independent executors to run the steps of a job. You can use the `circleci tests` commands to split your test suite to run across your parallel executors.

To run a job’s steps in parallel, set the `parallelism` key to a value greater than `1`.

```dracula
jobs:
  build:
    docker:
      - image: cimg/go:1.18.1
    parallelism: 4
    resource_class: large
    steps:
      - run: go list ./... | circleci tests run --command "xargs gotestsum --junitfile junit.xml --format testname --" --split-by=timings --timings-type=name
```

Figure 7. Executor types with parallelism

See Test Splitting and Parallelism page for more information.

## Pipelines

A CircleCI pipeline is the full set of processes you run when you trigger work on your projects. Pipelines encompass your workflows, which in turn coordinate your jobs. Pipelines are defined in your project configuration file.

Pipelines represent methods for interacting with your configuration:

- Trigger a pipeline through the API with the trigger a pipeline endpoint.
- Use pipeline parameters to trigger Conditional Workflows.
- Use `version 2.1` configuration, which provides access to:
- Reusable Configuration elements, including executors, commands and jobs.
- Packaged reusable configuration, known as Orbs.
- Improved configuration validation error messages.
- Option to enable auto-cancel, within **Advanced** project settings in the web app to terminate workflows when pipelines trigger on non-default branches.

|   | Consider the impact of enabling the auto-cancel feature, for example, if you have configured automated deployment jobs on non-default branches. |
|---|---|

See the Pipelines Overview page for more information.

## Projects

For GitHub OAuth app and Bitbucket Cloud accounts, a *project* in CircleCI is tied to, and shares the name of the associated code repository in your VCS.

For GitHub App, GitLab SaaS and self-managed and Bitbucket Data Center users, a *project* in CircleCI is standalone. You create a project and then connect your code (stored in your GitHub, GitLab or Bitbucket Data Center repository) to that project.

**Project names** must meet the following requirements:

- Begin with a letter.
- 3-40 characters long.
- Contain only letters, numbers, spaces, or the following characters `" - _ . : ! & + [ ] " ;`.

A standalone project can have:

- One or more configurations (pipeline definitions), including, but not limited to, a `.circleci/config.yml` file in the repository associated with the project.
- One or more triggers (events from a source of change), including, but not limited to, a VCS. A trigger determines which configuration to use to start a pipeline.

Select **Projects** in the CircleCI web app sidebar to enter the projects dashboard. On the dashboard, you can set up and follow any project you have access to.

- *Set Up* or *Create* any project that you are the owner of in your VCS.
- *Follow* any project in your organization to gain access to its pipelines and to subscribe to Email Notifications for the project’s status.

Figure 8. The projects dashboard in the CircleCI web app for a circleci organization

If you do not see the **Create project** button you are in a `GitHub` or `Bitbucket` organization. You can use the **Set up** button to start building your project on CircleCI. For more information on organization types, see the Users, Organizations, and Integrations Guide page.

Figure 9. The projects dashboard in the CircleCI web app for a GitHub or bitbucket organization

## Resource class

A resource class is a configuration option that allows you to control available compute resources (CPU and RAM) for your jobs. When you specify an execution environment for a job, CircleCI sets a default resource class value for the environment *unless* you define the resource class in your configuration. Define the resource class as best practice, instead of relying on a default.

The example below shows how to define a resource class in the Docker execution environment.

```dracula
version: 2.1

jobs:
  build:
    docker:
      - image: cimg/node:current
    # resource class declaration
    resource_class: large
    steps:
      - checkout
```

Examples for all execution environments are available on the following pages:

- Using the Docker Execution Environment
- Using the LinuxVM Execution Environment
- Using the macOS Execution Environment
- Using the Windows Execution Environment
- Using the GPU Execution Environment
- Using the Arm VM Execution Environment

Pricing and plans information for the various resource classes can be found on the Resource classes product page.

The `resource_class` key is also used to configure a Self-Hosted Runner Instance.

For full details on both uses of resource classes, see the Resource Class Overview page.

## Steps

Steps are collections of the executable commands required to complete your job. For example, the `checkout` step (which is a built-in step available across all CircleCI projects) checks out the source code for a job over SSH. The `run` step allows you to run custom commands, such as executing the command `make test`, using a non-login shell by default. You can also define commands outside the job declaration, making them reusable across your configuration.

```dracula
version: 2.1

jobs:
  build:
    docker:
      - image: cimg/base:2024.02
    steps:
      - checkout # Special step to checkout your source code
      - run: # Run step to execute commands, see
      # circleci.com/docs/configuration-reference/#run
          name: Running tests
          command: make test # executable command run in
          # non-login shell with /bin/bash -eo pipefail option
          # by default.
```

See the Jobs and Steps page for more information.

## User roles

CircleCI sets up roles differently depending on your Organization Type.

To check your organization type, check your organization slug at   **Overview**. `github` and `bitbucket` type organizations are OAuth authenticated orgs and the organization slug is structured as follows:

- `github/<your-org-name>` or `gh/<your-org-name>`
- `bitbucket/<your-org-name>` or `bb/<your-org-name>`

An organization slug for a `circleci` type organization is in the following format:

- `circleci/<UID>`

### GitHub App, GitLab and Bitbucket Data Center users

For `circleci` type organizations, you set roles at the organization and project level. These roles are separate from permissions and roles in your version control system. The available roles are:

- Admin
- Contributor
- Viewer

For an overview of organization and project role permissions, see the Roles and Permissions Overview page.

See the Manage Roles and Permissions page for steps to add, remove, and change org and project level roles. You can also manage roles and permissions in Groups.

### GitHub OAuth app and Bitbucket Cloud users

CircleCI has various user roles with permissions inherited from VCS accounts.

- The *Organization Administrator* is a permission level inherited from your VCS: GitHub: **Owner** and following at least one project building on CircleCI. Bitbucket: **Admin** and following at least one project building on CircleCI.
- The *Project Administrator* is the user who adds a GitHub or Bitbucket repository to CircleCI as a Project.
- A *User* is an individual user within an organization, inherited from your VCS.
- A CircleCI user is anyone who can log in to the CircleCI platform with a username and password. You must add users to an org in the VCS to view or follow associated CircleCI projects. Users may not view project data stored in environment variables.

## Workflows

Workflows orchestrate jobs. A workflow defines a list of jobs and their run order. You can run jobs concurrently, sequentially, on a schedule, or with a manual gate using an approval job.

Figure 10. Workflows illustration

The following configuration example shows two workflows with modern features:

- `build_and_test` runs on every commit with concurrent job execution.
- `deploy` is a conditional workflow that includes manual approval and flexible job dependencies.

|   | **Using Docker?** Authenticating Docker pulls from image registries is recommended when using the Docker execution environment. Authenticated pulls allow access to private Docker images, and may also grant higher rate limits, depending on your registry provider. For further information, see Using Docker authenticated pulls. |
|---|---|

```dracula
version: 2.1

parameters:
  run_deploy_workflow:
    type: boolean
    default: false

jobs:
  build:
    docker:
      - image: cimg/base:current
    steps:
      - checkout
      - run:
          name: Build application
          command: echo "Building application..."

  lint:
    docker:
      - image: cimg/base:current
    steps:
      - checkout
      - run:
          name: Run linter
          command: echo "Running linter checks..."

  test:
    docker:
      - image: cimg/base:current
    steps:
      - checkout
      - run:
          name: Run tests
          command: echo "Running test suite..."

  deploy:
    docker:
      - image: cimg/base:current
    steps:
      - checkout
      - run:
          name: Deploy application
          command: echo "Deploying to production..."

  cleanup:
    docker:
      - image: cimg/base:current
    steps:
      - run:
          name: Cleanup resources
          command: echo "Cleaning up resources..."

  notify-failure:
    docker:
      - image: cimg/base:current
    steps:
      - run:
          name: Send failure notification
          command: echo "Deploy failed - sending notification..."

workflows:
  # This workflow runs on every commit
  build_and_test:
    jobs:
      - build
      - lint:
          requires:
            - build
      - test:
          requires:
            - build

  # This workflow only runs when the parameter is true
  deploy:
    when: << pipeline.parameters.run_deploy_workflow >>
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
      - cleanup:
          requires:
            - deploy: terminal
      - notify-failure:
          requires:
            - deploy:
              - failed
              - canceled
```

See the Using Workflows page for more information.
