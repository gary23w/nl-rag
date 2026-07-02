---
title: "Configuration reference (part 3/3)"
source: https://circleci.com/docs/configuration-reference/
domain: circleci
license: CC-BY-SA-4.0
tags: circleci pipeline, continuous integration, ci cd pipeline, build automation
fetched: 2026-07-02
part: 3/3
---

## **`jobs`**

A job can have the keys `requires`, `name`, `context`, `type`, and `filters`.

| Key | Required | Type | Description |
|---|---|---|---|
| `jobs` | Y | List | A list of jobs to run with their dependencies |

### **<`job_name`>**

A job name that exists in your `config.yml`.

```dracula
version: 2.1

jobs:
  my-job:
    docker:
      - image: cimg/node:20.18.1
    steps:
      - run: echo "Hello World"

workflows:
  my-workflow:
    jobs:
      - my-job
```

#### **`override-with`**

The `override-with` key is used to override the job configuration with a job from the referenced orb. For more information, see the How to Override Config page.

| Key | Required | Type | Description |
|---|---|---|---|
| `override-with` | N | String | The orb job name you use to override the existing job configuration. (Supports both URL-based and registry orbs) |

**Example:**

```dracula
version: 2.1

orbs:
  my-orb: << url-ref >>

jobs:
  build:
    steps: 
      - run: task build
  test:
    steps:
      - run: task test
  deploy:
    steps:
      - run: ccc deploy

workflows:
  - build-test-deploy:
      jobs:
        - build
        - test:
            override-with: my-orb/my-test
            requires: build
        - deploy:
            requires: test
```

In the example above, the `test` job in the workflow is being overridden with the orb job `my-orb/my-test`. The `my-orb/my-test` job might be defined with a different resource class or execution steps.

If the `my-orb/my-test` job is not defined inside the orb, the `test` job will compile using the local job definition.

#### `serial-group`

The `serial-group` key is used to add a property to a job to allow a group of jobs to run in series, rather than concurrently, across an organization. Serial groups control the orchestration of jobs across an organization, not just within projects and pipelines.

The `serial-group` key is configurable per job, or at the job group invocation level. To apply `serial-group` to an entire job group, see `job-groups`.

The value of the `serial-group` key is a string that is used to group jobs together to run one after another. The key must meet the following requirements:

- Must be 512 characters or fewer when compiled.
- Must not be blank.
- Must consist of alphanumeric characters plus, `.`, `-`, `_`, `/`.

Note the following features of serial groups:

- You can use pipeline values and parameters in the `serial-group` key.
- Serial groups wait for five hours. After this time, CircleCI cancels any jobs still waiting in the group. This does not affect the standard limits that apply to a job’s runtime.

|   | **Pipeline order protection in serial groups** Jobs in a serial group follow an order protection mechanism, as follows: Jobs start in the order they join the queue, but are *accepted* based on pipeline number. If a group is waiting/running and another job in the same project attempts to join the queue with a lower pipeline number, the job is skipped. This immediate skip process maintains order integrity, preventing unintended work in a build, such as a deployment job running a previous version. If there are no serial groups waiting/running, a pipeline with a lower number can start, such as restoring back to a previous pipeline via a rerun workflow. |
|---|---|

| Key | Required | Type | Description |
|---|---|---|---|
| `serial-group` | N | String | A string that is used across an org to group jobs together to run one after another. Can include pipeline values and parameters. Use this same serial group across multiple pipelines to control the orchestration of jobs across an organization. |

**Example:**

```dracula
# Creating multiple pipelines at the same time with the below config will result in
# all pipelines running test and build but only a single pipeline will run deploy at a time.

workflows:
  main-workflow:
    jobs:
      - test
      - build
      - deploy:
          serial-group: << pipeline.project.slug >>/deploy-group
          requires:
            - test
            - build
```

For more information, see the Controlling Serial Execution Across Your Organization page.

#### **`requires`**

Jobs are run concurrently by default, so you must explicitly require any dependencies by their job name if you need some jobs to run sequentially.

| Key | Required | Type | Description |
|---|---|---|---|
| `requires` | N | List | A list of jobs that must succeed a specified status before the job starts. **Note**: When jobs you list as dependencies do not execute (due to filters, for example), CircleCI ignores them as dependencies for other jobs. However, if all dependencies of a job are filtered, that job doesn’t execute either. Possible types of `requires` items: Job name (a required job that must succeed for the job to start). Map of job name to status (a required job that must attain the specified status for the job to start). Map of job name to a list of statuses (a required job that must attain one of the specified statuses for the job to start). The possible **status** values are: `success`, `failed`, `canceled`, `unauthorized`, `not_run`, and `terminal`. |

```dracula
workflows:
  my-workflow:
    jobs:
      - build
      - test:
          requires:
            - build
      - deploy:
          requires:
            - build
            - test
      - notify-build-canceled:
          requires:
            - build: canceled
      - cleanup:
          requires:
            - deploy:
              - success
              - failed
              - canceled
              - unauthorized
              - not_run
      - cleanup-shorthand:
          requires:
            - deploy: terminal  # equivalent to [success, failed, canceled, unauthorized, not_run]
```

#### **`name`**

The `name` key can be used to invoke reusable jobs across any number of workflows. Using the name key ensures numbers are not appended to your job name (for example, sayhello-1, sayhello-2, etc.). The name you assign to the `name` key needs to be unique, otherwise the numbers will still be appended to the job name.

| Key | Required | Type | Description |
|---|---|---|---|
| `name` | N | String | A replacement for the job name. Useful when calling a job multiple times. If you want to invoke the same job multiple times, and a job requires one of the duplicate jobs, this key is required. (2.1 only) |

```dracula
workflows:
  my-workflow:
    jobs:
      - my-job:
          name: my-alternative-job-name
```

#### **`context`**

Jobs may be configured to use global environment variables set for an organization, see the Contexts document for adding a context in the application settings.

| Key | Required | Type | Description |
|---|---|---|---|
| `context` | N | String/List | The name of the context(s). The initial default name is `org-global`. Each context name must be unique. If using CircleCI Server, only a single context per workflow is supported. **Note:** A maximum of 100 unique contexts across all workflows is allowed. |

Use a context for a job

```dracula
workflows:
  my-workflow:
    jobs:
      - my-job:
          context: org-global
```

It is also possible to use a list of contexts, as follows:

```dracula
workflows:
  my-workflow:
    jobs:
      - my-job:
          context:
            - org-global
            - project-global
```

You can also use an expression to determine the contexts for a job:

Use an expression to determine the contexts for a job

```dracula
workflows:
  my-workflow:
    jobs:
      - my-job:
          context: << pipeline.git.branch == "main" and "org-global" or "project-global" >>
```

#### **`type`**

A job may have a `type` of `approval` indicating it must be manually approved before downstream jobs may proceed. For more information see the Using Workflows to Orchestrate Jobs page.

Jobs run in the dependency order until the workflow processes a job with the `type: approval` key followed by a job on which it depends, for example:

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

An approval job can have any name. In the example above the approval job is named `hold`. The name you choose for an approval job must not be used to define a job in the main configuration. An approval job only exists as a workflow orchestration device.

#### **`filters`**

Filter job execution within a workflow based on the following:

- Branch
- Tag
- Expression-based condition

Job filters can have the keys `branches` or `tags`.

|   | Workflows will ignore job-level branching. If you use job-level branching and later add workflows, you must remove the branching at the job level and instead declare it in the workflows section of your `config.yml`. |
|---|---|

| Key | Required | Type | Description |
|---|---|---|---|
| `filters` | N | Map | A map or string to define rules for job execution. Branch and tag filters require a map. Expression-based filters require a string. |

The following is an example of how the CircleCI documentation project uses a regular expression to filter running a job in a workflow only on a specific branch:

```dracula
# ...
workflows:
  build-deploy:
    jobs:
      - js_build
      - build_server_pdfs: # << the job to conditionally run based on the filter-by-branch-name.
          filters:
            branches:
              only: /server\/.*/ # the job build_server_pdfs will only run when the branch being built starts with server/
```

You can read more about using regular expressions in your config in the Using Workflows to Schedule Jobs page.

#### Expression-based job filters

Expression-based job filters allow you to conditionally run jobs based on the following:

- Pipeline Values
- Pipeline Parameters

An expression-based job filter is a rule that is evaluated against pipeline values and parameters to decide whether a job runs.

Using expression-based job filters is one way to optimize your pipelines. Optimizations include the following:

- Lower costs.
- Decrease time to feedback.
- Run specific jobs based on the context of the source of change.

```dracula
workflows:
  deploy:
    jobs:
      - init-service
      - test-service
      - build-service-image:
          requires:
            - init-service
      - dry-run-service:
          requires:
            - init-service
          filters: pipeline.git.branch != "main" and pipeline.git.branch != "canary"
      - publish-service:
          requires:
            - build-service-image
            - test-service
          filters: pipeline.git.branch == "main" or pipeline.git.tag starts-with "release"
      - deploy-service:
          context:
            - org-global
          requires:
            - publish-service
          filters: pipeline.git.branch == "main" and pipeline.parameters.my-custom-param starts-with "DEPLOY:"
```

**Examples:**

Only run the job on the project’s `main` branch:

```dracula
filters: pipeline.git.branch == "main"
```

Only run the job on the project’s `main` branch, or branches starting with `integration-test`:

```dracula
filters: pipeline.git.branch == "main" or pipeline.git.branch starts-with "integration-test"
```

Only run the job on the `main` branch, and disallow use with pipelines Triggered With Unversioned Configuration:

```dracula
filters: pipeline.git.branch == "main" and not (pipeline.trigger_source starts-with "api")
```

Use pipeline parameters and the pipeline value `pipeline.git.branch` to run a job only on specific branches **or** when triggered via the API with a pipeline parameter set to true:

```dracula
version: 2.1

parameters:
  run-storybook-tests:
    type: boolean
    default: false

...
# jobs configuration omitted for brevity

workflows:
  build:
    jobs:
      - setup
      - storybook-tests:
          requires:
            - setup
          filters: |
            pipeline.parameters.run-storybook-tests
            or pipeline.git.branch == "dry-run-deploy"
            or pipeline.git.branch starts-with "deploy"
```

You can use the API to trigger a pipeline with a pipeline parameter set to true:

|   | **Using server?** If you are using CircleCI server, replace `https://circleci.com` with your server hostname when interacting with the CircleCI API. |
|---|---|

```dracula
curl -X POST https://circleci.com/api/v2/project/circleci/<org-id>/<project-id>/pipeline/run \
  --header "Circle-Token: $CIRCLE_TOKEN" \
  --header "content-type: application/json" \
  --data {
  "definition_id": "<pipeline-definition-id>",
  "config": {"branch": "<your-branch-name>"},
  "checkout": {"branch": "<your-branch-name>"},
  "parameters": {"run-storybook-tests": "true"}
  }
```

**Operators**

The operators you can use for expression-based job filters are described in the following table. You can also group sub-expressions with parentheses `(`, `)` as in the examples above.

| Operator type | Operators | Description |
|---|---|---|
| Logical | `and`, `or` | These are short-circuiting boolean operators. |
| Equality | `==`, `!=` | String, numeric, and boolean equality. If the operands are of different types then `==` will evaluate `false`, and `!=` will evaluate `true`. |
| Equality | `starts-with` | String prefix equality, `"hello world" starts-with "hello"` evaluates as `true`. It is an error to use a non-string type as an operand. |
| Numeric comparison | `>=`, `>`, `⇐`, `<` | Numeric comparisons. It is an error to use a non-numeric type as an operand. |
| Negation | `not` | Boolean negation. Note that `not` has very high precedence and so binds very tightly. Use sub-expressions to apply `not` to more complex expressions. For example, with `foo` being `true` and `bar` being `false`: `not foo and bar` evaluates to `false` `not (foo and bar)` evaluates to `true` |

#### **`branches`**

The branches filter can have the keys `only` and `ignore`, which map to a single string naming a branch. You may also use regular expressions to match against branches by enclosing them with slashes, or map to a list of such strings. Regular expressions must match the **entire** string.

- Any branches that match `only` run the job.
- Any branches that match `ignore` do not run the job.
- If you specify neither `only` nor `ignore`, the job runs on all branches.
- If you specify both `only` and `ignore`, CircleCI checks `only` before `ignore`.

| Key | Required | Type | Description |
|---|---|---|---|
| `branches` | N | Map | A map defining rules for execution on specific branches. |
| `only` | N | String, or list of strings | Either a single branch specifier, or a list of branch specifiers. |
| `ignore` | N | String, or list of strings | Either a single branch specifier, or a list of branch specifiers. |

```dracula
workflows:
  dev_stage_pre-prod:
    jobs:
      - test_dev:
          filters:  # using regex filters requires the entire branch to match
            branches:
              only:  # only branches matching the below regex filters will run
                - dev
                - /user-.*/
      - test_stage:
          filters:
            branches:
              only: stage
      - test_pre-prod:
          filters:
            branches:
              only: /pre-prod(?:-.+)?$/
```

#### **`tags`**

CircleCI does not run workflows for tags unless you explicitly specify tag filters. If a job requires any other jobs (directly or indirectly), you must specify tag filters for those jobs.

Tags can have the keys `only` and `ignore`. You may also use regular expressions to match against tags by enclosing them with slashes, or map to a list of such strings. Regular expressions must match the **entire** string. Both lightweight and annotated tags are supported.

- Any tags that match `only` runs the job.
- Any tags that match `ignore` do not run the job.
- If neither `only` nor `ignore` are specified then the job is skipped for all tags.
- If both `only` and `ignore` are specified the `only` is considered before `ignore`.

| Key | Required | Type | Description |
|---|---|---|---|
| `tags` | N | Map | A map defining rules for execution on specific tags |
| `only` | N | String, or List of Strings | Either a single tag specifier, or a list of tag specifiers |
| `ignore` | N | String, or List of Strings | Either a single tag specifier, or a list of tag specifiers |

For more information, see the Executing Workflows for a Git Tag section of the Workflows page.

```dracula
workflows:
  untagged-build:
    jobs:
      - build
  tagged-build:
    jobs:
      - build:
          filters:
            tags:
              only: /^v.*/
```

#### **`matrix`**

|   | The `matrix` key is supported in `version: 2.1` configuration |
|---|---|

The `matrix` stanza allows you to run a parameterized job multiple times with different arguments. For more information see the how-to guide on Using Matrix Jobs. In order to use the `matrix` stanza, you must use parameterized jobs.

| Key | Required | Type | Description |
|---|---|---|---|
| `parameters` | Y | Map | A map of parameter names to every value the job is called with |
| `exclude` | N | List | A list of argument maps to exclude from the matrix |
| `alias` | N | String | An alias for the matrix, usable from another job’s `requires` stanza. Defaults to the name of the job being executed |

**Example:**

The following is a basic example of using matrix jobs.

```dracula
workflows:
  workflow:
    jobs:
      - build:
          matrix:
            parameters:
              version: ["0.1", "0.2", "0.3"]
              platform: ["macos", "windows", "linux"]
```

This expands to 9 different `build` jobs, and could be equivalently written as:

```dracula
workflows:
  workflow:
    jobs:
      - build:
          name: build-macos-0.1
          version: "0.1"
          platform: macos
      - build:
          name: build-macos-0.2
          version: "0.2"
          platform: macos
      - build:
          name: build-macos-0.3
          version: "0.3"
          platform: macos
      - build:
          name: build-windows-0.1
          version: "0.1"
          platform: windows
      - ...
```

#### Excluding sets of parameters from a matrix

Sometimes you may wish to run a job with every combination of arguments *except* some value or values. You can use an `exclude` stanza to achieve this:

```dracula
workflows:
  workflow:
    jobs:
      - build:
          matrix:
            parameters:
              a: [1, 2, 3]
              b: [4, 5, 6]
            exclude:
              - a: 3
                b: 5
```

The matrix above would expand into 8 jobs: every combination of the parameters `a` and `b`, excluding `{a: 3, b: 5}`

#### Dependencies and matrix jobs

To require an entire matrix (every job within the matrix), use its `alias`. The `alias` defaults to the name of the job being invoked.

```dracula
workflows:
  workflow:
    jobs:
      - deploy:
          matrix:
            parameters:
              version: ["0.1", "0.2"]
      - another-job:
          requires:
            - deploy
```

This means that `another-job` will require both deploy jobs in the matrix to finish before it runs.

Matrix jobs expose their parameter values via `<< matrix.* >>` which can be used to generate more complex workflows. For example, here is a `deploy` matrix where each job waits for its respective `build` job in another matrix.

```dracula
workflows:
  workflow:
    jobs:
      - build:
          name: build-v<< matrix.version >>
          matrix:
            parameters:
              version: ["0.1", "0.2"]
      - deploy:
          name: deploy-v<< matrix.version >>
          matrix:
            parameters:
              version: ["0.1", "0.2"]
          requires:
            - build-v<< matrix.version >>
```

This workflow expands to:

```dracula
workflows:
  workflow:
    jobs:
      - build:
          name: build-v0.1
          version: "0.1"
      - build:
          name: build-v0.2
          version: "0.2"
      - deploy:
          name: deploy-v0.1
          version: "0.1"
          requires:
            - build-v0.1
      - deploy:
          name: deploy-v0.2
          version: "0.2"
          requires:
            - build-v0.2
```

#### **`pre-steps`** and **`post-steps`**

|   | Pre-steps and post-steps are supported in `version: 2.1` configuration |
|---|---|

Every job invocation in a workflow may optionally accept two special arguments: `pre-steps` and `post-steps`.

Steps under `pre-steps` are executed before any of the other steps in the job. The steps under `post-steps` are executed after all of the other steps.

Pre and post steps allow you to execute steps in a given job without modifying the job. Pre and post steps are useful, for example, to run custom setup steps before job execution.

```dracula
version: 2.1

jobs:
  bar:
    machine:
      image: ubuntu-2004:2024.05.1
    steps:
      - checkout
      - run:
          command: echo "building"
      - run:
          command: echo "testing"

workflows:
  build:
    jobs:
      - bar:
          pre-steps: # steps to run before steps defined in the job bar
            - run:
                command: echo "install custom dependency"
          post-steps: # steps to run after steps defined in the job bar
            - run:
                command: echo "upload artifact to s3"
```


## Logic statements

Certain dynamic configuration features accept logic statements as arguments. Logic statements are evaluated to boolean values at configuration compilation time, that is, before the workflow is run. The group of logic statements includes:

| Type | Arguments | `true` if | Example |
|---|---|---|---|
| YAML literal | None | is truthy | `true`/`42`/`"a string"` |
| Pipeline Value | None | resolves to a truthy value | `<< pipeline.git.branch >>` |
| Pipeline Parameter | None | resolves to a truthy value | `<< pipeline.parameters.my-parameter >>` |
| `and` | N logic statements | all arguments are truthy | `and: [ true, true, false ]` |
| `or` | N logic statements | any argument is truthy | `or: [ false, true, false ]` |
| `not` | 1 logic statement | the argument is not truthy | `not: true` |
| `equal` | N values | all arguments evaluate to equal values | `equal: [ 42, << pipeline.number >>]` |
| `matches` | `pattern` and `value` | `value` matches the `pattern` | `matches: { pattern: "^feature-.$", value: << pipeline.git.branch >> }+` |

The following logic values are considered falsy:

- false.
- null.
- 0
- NaN
- empty strings ("").
- statements with no arguments.

All other values are truthy. Also note that using logic with an empty list will cause a validation error.

Logic statements always evaluate to a boolean value at the top level, and coerce as necessary. They can be nested in an arbitrary fashion, according to their argument specifications, and to a maximum depth of 100 levels.

`matches` uses Java regular expressions for its `pattern`. A full match pattern must be provided, prefix matching is not an option. It is recommended to enclose a pattern in `^` and `$` to avoid accidental partial matches.

|   | When using logic statements at the workflow level, do not include the `condition:` key (the `condition` key is only needed for `job` level logic statements). |
|---|---|

**Example:**

```dracula
workflows:
  my-workflow:
    when:
      or:
        - equal: [ main, << pipeline.git.branch >> ]
        - equal: [ staging, << pipeline.git.branch >> ]
```


## Using expressions in your configuration

CircleCI configuration supports expressions for dynamic value evaluation. Expressions can include pipeline values, pipeline parameters, literals, and operators such as `and`, `or`, and comparison operators.

### Expressions in configuration fields

Configuration fields accept expressions either directly or as string values. When you provide a string value, you can use `<< >>` delimiters to mark a section of the string to be interpreted as an expression.

You can write the expression in a configuration field as shown in the following example:

Use expression to determine parallelism for a job

```dracula
jobs:
  test:
    docker:
      - image: cimg/base:current
    parallelism: << pipeline.git.branch == "main" and 10 or 1 >>
    steps:
      - checkout
      - run: run_tests
```

In this example, `parallelism` is set to `10` when running on the `main` branch, and `1` on all other branches.

Use direct expressions in job filters and using `when` or `unless` in your workflows. For example:

Direct expression in a job filter

```dracula
workflows:
  my-workflow:
    jobs:
      - build:
          filters: pipeline.git.branch == "main" or pipeline.git.branch starts-with "release/"
```

Workflow

when

expression

```dracula
workflows:
  deploy-workflow:
    when: pipeline.git.tag starts-with "v" and pipeline.trigger_source == "webhook"
    jobs:
      - deploy
```

For all other configuration fields, you must use the `<< >>` delimiters to mark the expression as an expression, as shown in other examples in this section.

### Expressions within strings

When you need to include an expression within a larger string value, use `<< >>` delimiters to mark the expression:

```dracula
- run:
    name: Print branch info
    command: |
      echo "Running on << pipeline.git.branch or "unknown branch" >>"
```

In this example, the `<< >>` delimiters mark `pipeline.git.branch or "unknown branch"` as an expression. If `pipeline.git.branch` is null (for example, when the pipeline is triggered for a tag rather than a branch), the `or` operator provides the fallback value "unknown branch".

### Conditional logic example

You can combine `and` and `or` to implement if-then-else style logic:

```dracula
parallelism: << pipeline.git.branch == "main" and 10 or 1 >>
```

- If the condition `pipeline.git.branch == "main"` is true, the `and` expression evaluates to its second operand `10`.
- If the condition is false, the `and` expression evaluates to false, and the `or` expression returns the fallback value `1`.

### Expression operators

The operators you can use for expressions are described in the following table. You can also group sub-expressions with parentheses `(`, `)`.

| Operator type | Operators | Description |
|---|---|---|
| Logical | `and`, `or` | These are short-circuiting boolean operators. |
| Equality | `==`, `!=` | String, numeric, and boolean equality. If the operands are of different types then `==` will evaluate `false`, and `!=` will evaluate `true`. |
| Equality | `starts-with` | String prefix equality, `"hello world" starts-with "hello"` evaluates as `true`. It is an error to use a non-string type as an operand. |
| Numeric comparison | `>=`, `>`, `⇐`, `<` | Numeric comparisons. It is an error to use a non-numeric type as an operand. |
| Negation | `not` | Boolean negation. Note that `not` has very high precedence and so binds very tightly. Use sub-expressions to apply `not` to more complex expressions. For example, with `foo` being `true` and `bar` being `false`: `not foo and bar` evaluates to `false` `not (foo and bar)` evaluates to `true` |

### Valid parameter names

To use a pipeline parameter in an expression, the parameter name must follow these rules:

- Start with a letter.
- Can contain upper-case letters (`A`-`Z`) and lower-case letters (`a`-`z`).
- Can contain digits (`0`-`9`).
- Can contain hyphens (`-`), underscores (`_`), and periods (`.`).
- Cannot contain consecutive periods (`..`).

|   | If a pipeline parameter has a name that does not follow these rules, CircleCI performs string replacement instead of evaluating an expression. |
|---|---|

### Logic statement and expression examples

You can find usage examples on the Orchestration Cookbook page.


## Example full configuration

|   | **Using Docker?** Authenticating Docker pulls from image registries is recommended when using the Docker execution environment. Authenticated pulls allow access to private Docker images, and may also grant higher rate limits, depending on your registry provider. For further information, see Using Docker authenticated pulls. |
|---|---|

```dracula
version: 2.1
jobs:
  build:
    docker:
      - image: ubuntu:23.04

      - image: mongo:6.0.14
        command: [mongod, --smallfiles]

      - image: postgres:14.12
        # some containers require setting environment variables
        environment:
          POSTGRES_USER: user

      - image: redis@sha256:54057dd7e125ca41afe526a877e8bd35ec2cdd33b9217e022ed37bdcf7d09673

      - image: rabbitmq:3.12.12

    environment:
      TEST_REPORTS: /tmp/test-reports

    working_directory: ~/my-project

    steps:
      - checkout

      - run:
          command: echo 127.0.0.1 devhost | sudo tee -a /etc/hosts

      # Create Postgres users and database
      # Note the YAML heredoc '|' for nicer formatting
      - run: |
          sudo -u root createuser -h localhost --superuser ubuntu &&
          sudo createdb -h localhost test_db

      - restore_cache:
          keys:
            - v1-my-project-{{ checksum "project.clj" }}
            - v1-my-project-

      - run:
          environment:
            SSH_TARGET: "localhost"
            TEST_ENV: "linux"
          command: |
            set -xu
            mkdir -p ${TEST_REPORTS}
            run-tests.sh
            cp out/tests/*.xml ${TEST_REPORTS}

      - run: |
          set -xu
          mkdir -p /tmp/artifacts
          create_jars.sh << pipeline.number >>
          cp *.jar /tmp/artifacts

      - save_cache:
          key: v1-my-project-{{ checksum "project.clj" }}
          paths:
            - ~/.m2

      # Save artifacts
      - store_artifacts:
          path: /tmp/artifacts
          destination: build

      # Upload test results
      - store_test_results:
          path: /tmp/test-reports

  deploy-stage:
    docker:
      - image: ubuntu:23.04
    working_directory: /tmp/my-project
    steps:
      - run:
          name: Deploy if tests pass and branch is Staging
          command: ansible-playbook site.yml -i staging

  deploy-prod:
    docker:
      - image: ubuntu:23.04
    working_directory: /tmp/my-project
    steps:
      - run:
          name: Deploy if tests pass and branch is Main
          command: ansible-playbook site.yml -i production

workflows:
  build-deploy:
    jobs:
      - build:
          filters:
            branches:
              ignore:
                - develop
                - /feature-.*/
      - deploy-stage:
          requires:
            - build
          filters:
            branches:
              only: staging
      - deploy-prod:
          requires:
            - build
          filters:
            branches:
              only: main
```
