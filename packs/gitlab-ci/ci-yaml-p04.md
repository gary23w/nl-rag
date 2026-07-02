---
title: "CI/CD YAML syntax reference (part 4/4)"
source: https://docs.gitlab.com/ee/ci/yaml/
domain: gitlab-ci
license: CC-BY-SA-4.0
tags: gitlab ci, gitlab pipeline, ci cd pipeline, continuous integration
fetched: 2026-07-02
part: 4/4
---

# CI/CD YAML syntax reference

```yaml
job:
  script: echo "Hello, Rules!"
  interruptible: true
  rules:
    - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
      interruptible: false  # Override interruptible defined at the job level.
    - when: on_success
```

**Additional details**:

- The rule-level `rules:interruptible` overrides the job-level `interruptible`, and only applies when the specific rule triggers the job.

### `run`

- Status: Experiment

- Introduced in GitLab 17.3 with a flag named `pipeline_run_keyword`. Disabled by default. Requires GitLab Runner 17.1.
- Feature flag `pipeline_run_keyword` removed in GitLab 17.5.

This feature is available for testing, but not ready for production use.

Use `run` to define a series of steps to be executed in a job. Each step can be either a script or a predefined step.

You can also provide optional environment variables and inputs.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- An array of hashes, where each hash represents a step with the following possible keys:
  - `name`: A string representing the name of the step.
  - `script`: A string containing shell commands to execute.
  - `step`: A string identifying a predefined step to run.
  - `env`: Optional. A hash of environment variables specific to this step.
  - `inputs`: Optional. A hash of input parameters for predefined steps.

Each array entry must have a `name`, and one `script` or `step` (but not both).

**Example of `run`**:

```yaml
job:
  run:
    - name: 'hello_steps'
      script: 'echo "hello from step1"'
    - name: 'bye_steps'
      step: gitlab.com/gitlab-org/ci-cd/runner-tools/echo-step@main
      inputs:
        echo: 'bye steps!'
      env:
        var1: 'value 1'
```

In this example, the job has two steps:

- `hello_steps` runs the `echo` shell command.
- `bye_steps` uses a predefined step with an environment variable and an input parameter.

**Additional details**:

- A step can have either a `script` or a `step` key, but not both.
- A `run` configuration cannot be used together with existing `script`, `after_script` or `before_script` keywords.
- Multi-line scripts can be defined using YAML block scalar syntax.

### `script`

Use `script` to specify commands for the runner to execute.

All jobs except trigger jobs require a `script` keyword.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**: An array including:

- Single line commands.
- Long commands split over multiple lines.
- YAML anchors.

CI/CD variables are supported.

**Example of `script`**:

```yaml
job1:
  script: "bundle exec rspec"

job2:
  script:
    - uname -a
    - bundle exec rspec
```

**Additional details**:

- When you use these special characters in `script`, you must use single quotes (`'`) or double quotes (`"`).

**Related topics**:

- You can ignore non-zero exit codes.
- Use color codes with `script` to make job logs easier to review.
- Create custom collapsible sections to simplify job log output.

### `secrets`

- Tier: Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

Use `secrets` to specify CI/CD secrets to:

- Retrieve from an external secrets provider.
- Make available in the job as CI/CD variables (`file` type by default).

#### `secrets:vault`

Use `secrets:vault` to specify secrets provided by a HashiCorp Vault.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- `engine:name`: Name of the secrets engine. Can be one of `kv-v2` (default), `kv-v1`, or `generic`.
- `engine:path`: Path to the secrets engine.
- `path`: Path to the secret.
- `field`: Name of the field where the password is stored.

**Example of `secrets:vault`**:

To specify all details explicitly and use the KV-V2 secrets engine:

```yaml
job:
  secrets:
    DATABASE_PASSWORD:  # Store the path to the secret in this CI/CD variable
      vault:  # Translates to secret: `ops/data/production/db`, field: `password`
        engine:
          name: kv-v2
          path: ops
        path: production/db
        field: password
```

You can shorten this syntax. With the short syntax, `engine:name` and `engine:path` both default to `kv-v2`:

```yaml
job:
  secrets:
    DATABASE_PASSWORD:  # Store the path to the secret in this CI/CD variable
      vault: production/db/password  # Translates to secret: `kv-v2/data/production/db`, field: `password`
```

To specify a custom secrets engine path in the short syntax, add a suffix that starts with `@`:

```yaml
job:
  secrets:
    DATABASE_PASSWORD:  # Store the path to the secret in this CI/CD variable
      vault: production/db/password@ops  # Translates to secret: `ops/data/production/db`, field: `password`
```

#### `secrets:gcp_secret_manager`

Use `secrets:gcp_secret_manager` to specify secrets provided by GCP Secret Manager.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- `name`: Name of the secret.
- `version`: Version of the secret.

**Example of `secrets:gcp_secret_manager`**:

```yaml
job:
  secrets:
    DATABASE_PASSWORD:
      gcp_secret_manager:
        name: 'test'
        version: 2
```

**Related topics**:

- Use GCP Secret Manager secrets in GitLab CI/CD.

#### `secrets:gitlab_secrets_manager`

- Introduced in GitLab 19.0. Requires GitLab Runner 19.0 or later.

Use `secrets:gitlab_secrets_manager` to specify secrets from the GitLab Secrets Manager.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- `name`: Name of the secret.
- `source`: Optional. Source of the secret. Defaults to the current project when not specified. For a group secret, use `group/<full-path-to-group>`.

**Example of `secrets:gitlab_secrets_manager`**:

```yaml
job:
  secrets:
    MY_DEPLOY_SECRET:
      gitlab_secrets_manager:
        name: deployment_token
```

#### `secrets:azure_key_vault`

Use `secrets:azure_key_vault` to specify secrets provided by a Azure Key Vault.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- `name`: Name of the secret.
- `version`: Version of the secret.

**Example of `secrets:azure_key_vault`**:

```yaml
job:
  secrets:
    DATABASE_PASSWORD:
      azure_key_vault:
        name: 'test'
        version: 'test'
```

**Related topics**:

- Use Azure Key Vault secrets in GitLab CI/CD.

#### `secrets:file`

Use `secrets:file` to configure the secret to be stored as either a `file` or `variable` type CI/CD variable

By default, the secret is passed to the job as a `file` type CI/CD variable. The value of the secret is stored in the file and the variable contains the path to the file.

If your software can’t use `file` type CI/CD variables, set `file: false` to store the secret value directly in the variable.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- `true` (default) or `false`.

**Example of `secrets:file`**:

```yaml
job:
  secrets:
    DATABASE_PASSWORD:
      vault: production/db/password@ops
      file: false
```

**Additional details**:

- The `file` keyword is a setting for the CI/CD variable and must be nested under the CI/CD variable name, not in the `vault` section.

#### `secrets:token`

Use `secrets:token` to explicitly select a token to use when authenticating with the external secrets provider by referencing the token’s CI/CD variable.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- The name of an ID token

**Example of `secrets:token`**:

```yaml
job:
  id_tokens:
    AWS_TOKEN:
      aud: https://aws.example.com
    VAULT_TOKEN:
      aud: https://vault.example.com
  secrets:
    DB_PASSWORD:
      vault: gitlab/production/db
      token: $VAULT_TOKEN
```

**Additional details**:

- When the `token` keyword is not set and there is only one token defined, the defined token will automatically be used.
- If there is more than one token defined, you should specify which token to use by setting the `token` keyword. If you do not specify which token to use, it is not possible to predict which token is used each time the job runs.

### `services`

Use `services` to specify any additional Docker images that your scripts require to run successfully. The `services` image is linked to the image specified in the `image` keyword.

Job configuration and default configuration does not merge together. If the pipeline has `default:services` defined, and the job also has `services`, the job configuration takes precedence and the default configuration is not used.

To enable inter-service networking, set `FF_NETWORK_PER_BUILD` to `true`. Without this flag, services may not work properly. For more information, see feature flags

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**: The name of the services image, including the registry path if needed, in one of these formats:

- `<image-name>` (Same as using `<image-name>` with the `latest` tag)
- `<image-name>:<tag>`
- `<image-name>@<digest>`

CI/CD variables are supported, but not for `alias`. To customize `alias` dynamically, use CI/CD inputs instead.

**Example of `services`**:

```yaml
default:
  image:
    name: ruby:2.6
    entrypoint: ["/bin/bash"]

  services:
    - name: my-postgres:11.7
      alias: db-postgres
      entrypoint: ["/usr/local/bin/db-postgres"]
      command: ["start"]

  before_script:
    - bundle install

test:
  script:
    - bundle exec rake spec
```

In this example, GitLab launches two containers for the job:

- A Ruby container that runs the `script` commands.
- A PostgreSQL container. The `script` commands in the Ruby container can connect to the PostgreSQL database at the `db-postgres` hostname.

**Additional details**:

- Using `services` at the top level, but not in the `default` section, is deprecated.

**Related topics**:

- Available settings for `services`.
- Define `services` in the `.gitlab-ci.yml` file.
- Run your CI/CD jobs in Docker containers.
- Use Docker to build Docker images.

#### `services:name`

The full name of the image to use for the service.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**: The name of the service image, including the registry path if needed, in one of these formats:

- `<image-name>` (Same as using `<image-name>` with the `latest` tag)
- `<image-name>:<tag>`
- `<image-name>@<digest>`

CI/CD variables are supported.

**Example of `services:name`**:

```yaml
services:
  - name: postgres:11.7
  - name: registry.example.com/my-org/custom-service:latest
```

**Additional details**:

- Use `alias` to define unique name aliases when using multiple identical service images, or when the service image name is long.
- When used with other service options like `entrypoint`, `command`, or `variables`, the `name` keyword is required.
- For more information, see accessing the services.

#### `services:alias`

- Introduced in GitLab Runner 17.9.

Additional aliases to access the service from the job’s container.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**: A string with one or more aliases separated by spaces or commas.

**Example of `services:alias`**:

```yaml
services:
  - name: postgres:11.7
    alias: db,postgres,pg
  - name: mysql:latest
    alias: mysql-1
```

**Additional details**:

- Multiple aliases can be separated by spaces or commas.
- For more information, see accessing the services. and using aliases as service container names for the Kubernetes executor.

#### `services:docker`

Use `services:docker` to pass options to the Docker executor of a GitLab Runner.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

A hash of options for the Docker executor, which can include:

- `platform`: Selects the architecture of the image to pull. When not specified, the default is the same platform as the host runner.
- `user`: Specify the username or UID to use when running the container.

**Example of `services:docker`**:

```yaml
arm-sql-job:
  script: echo "Run sql tests in service container"
  image: ruby:2.6
  services:
    - name: super/sql:experimental
      docker:
        platform: arm64/v8
        user: dave
```

**Additional details**:

- `services:docker:platform` maps to the `docker pull --platform` option.
- `services:docker:user` maps to the `docker run --user` option.

#### `services:kubernetes`

- Introduced in GitLab 18.0. Requires GitLab Runner 17.11 or later.
- `user` input option introduced in GitLab Runner 17.11.
- `user` input option extended to support `uid:gid` format in GitLab 18.0.

Use `services:kubernetes` to pass options to the GitLab Runner Kubernetes executor.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

A hash of options for the Kubernetes executor, which can include:

- `user`: Specify the username or UID to use when the container runs. You can also use it to set GID by using the `UID:GID` format.

**Example of `services:kubernetes` with only UID**:

```yaml
arm-sql-job:
  script: echo "Run sql tests"
  image: ruby:2.6
  services:
    - name: super/sql:experimental
      kubernetes:
        user: "1001"
```

**Example of `services:kubernetes` with both UID and GID**:

```yaml
arm-sql-job:
  script: echo "Run sql tests"
  image: ruby:2.6
  services:
    - name: super/sql:experimental
      kubernetes:
        user: "1001:1001"
```

#### `services:entrypoint`

A command or script to execute as the container’s entrypoint.

When the Docker container is created, the `entrypoint` is translated to the Docker `--entrypoint` option. The syntax is similar to the Dockerfile `ENTRYPOINT` directive, where each shell token is a separate string in the array.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**: An array of strings representing the entrypoint command.

**Example of `services:entrypoint`**:

```yaml
services:
  - name: my-postgres:11.7
    entrypoint: ["/usr/local/bin/db-postgres"]
```

#### `services:command`

Command or script that should be used as the container’s command.

It’s translated to arguments passed to Docker after the image’s name. The syntax is similar to the Dockerfile `CMD` directive, where each shell token is a separate string in the array.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**: An array of strings representing the command.

**Example of `services:command`**:

```yaml
services:
  - name: super/sql:latest
    command: ["/usr/bin/super-sql", "run"]
```

#### `services:variables`

Additional environment variables that are passed exclusively to the service. Service variables are passed exclusively to the service container and are not available to the job container.

The syntax is the same as job variables.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**: A hash of environment variable names and values.

**Example of `services:variables`**:

```yaml
services:
  - name: postgres:11.7
    alias: db
    variables:
      POSTGRES_DB: "my_custom_db"
      POSTGRES_USER: "postgres"
      POSTGRES_PASSWORD: "example"
      PGDATA: "/var/lib/postgresql/data"
```

**Additional details**:

- Service variables cannot reference themselves, they do not support variable expansion or interpolation.
- Variables defined at the job or pipeline level are automatically passed to services. See passing CI/CD variables to services for more information.
- Service variables are only available to the specific service they are defined for.

#### `services:pull_policy`

The pull policy that the runner uses to fetch the Docker image. Requires GitLab Runner 15.1 or later.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- A single pull policy, or multiple pull policies in an array. Can be `always`, `if-not-present`, or `never`.

**Examples of `services:pull_policy`**:

```yaml
job1:
  script: echo "A single pull policy."
  services:
    - name: postgres:11.6
      pull_policy: if-not-present

job2:
  script: echo "Multiple pull policies."
  services:
    - name: postgres:11.6
      pull_policy: [always, if-not-present]
```

**Additional details**:

- If the runner does not support the defined pull policy, the job fails with an error similar to: `ERROR: Job failed (system failure): the configured PullPolicies ([always]) are not allowed by AllowedPullPolicies ([never])`.

**Related topics**:

- Run your CI/CD jobs in Docker containers.
- Configure how runners pull images.
- Set multiple pull policies.

### `stage`

Use `stage` to define which stage a job runs in. Jobs in the same `stage` can execute in parallel (see **Additional details**).

If `stage` is not defined, the job uses the `test` stage by default.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**: A string, which can be a:

- Default stage.
- User-defined stages.

**Example of `stage`**:

```yaml
stages:
  - build
  - test
  - deploy

job1:
  stage: build
  script:
    - echo "This job compiles code."

job2:
  stage: test
  script:
    - echo "This job tests the compiled code. It runs when the build stage completes."

job3:
  script:
    - echo "This job also runs in the test stage."

job4:
  stage: deploy
  script:
    - echo "This job deploys the code. It runs when the test stage completes."
  environment: production
```

**Additional details**:

- The stage name must be 255 characters or fewer.
- Jobs can run in parallel if they run on different runners.
- If you have only one runner, jobs can run in parallel if the runner’s `concurrent` setting is greater than `1`.

#### `stage: .pre`

Use the `.pre` stage to make a job run at the start of a pipeline. By default, `.pre` is the first stage in a pipeline. User-defined stages execute after `.pre`. You do not have to define `.pre` in `stages`.

If a pipeline contains only jobs in the `.pre` or `.post` stages, it does not run. There must be at least one other job in a different stage.

**Keyword type**: You can only use it with a job’s `stage` keyword.

**Example of `stage: .pre`**:

```yaml
stages:
  - build
  - test

job1:
  stage: build
  script:
    - echo "This job runs in the build stage."

first-job:
  stage: .pre
  script:
    - echo "This job runs in the .pre stage, before all other stages."

job2:
  stage: test
  script:
    - echo "This job runs in the test stage."
```

**Additional details**:

- If a pipeline has jobs with `needs: []` and jobs in the `.pre` stage, they will all start as soon as the pipeline is created. Jobs with `needs: []` start immediately, ignoring any stage configuration.
- A pipeline execution policy can define a `.pipeline-policy-pre` stage which runs before `.pre`.

#### `stage: .post`

Use the `.post` stage to make a job run at the end of a pipeline. By default, `.post` is the last stage in a pipeline. User-defined stages execute before `.post`. You do not have to define `.post` in `stages`.

If a pipeline contains only jobs in the `.pre` or `.post` stages, it does not run. There must be at least one other job in a different stage.

**Keyword type**: You can only use it with a job’s `stage` keyword.

**Example of `stage: .post`**:

```yaml
stages:
  - build
  - test

job1:
  stage: build
  script:
    - echo "This job runs in the build stage."

last-job:
  stage: .post
  script:
    - echo "This job runs in the .post stage, after all other stages."

job2:
  stage: test
  script:
    - echo "This job runs in the test stage."
```

**Additional details**:

- A pipeline execution policy can define a `.pipeline-policy-post` stage which runs after `.post`.

### `tags`

Use `tags` to select a specific runner from the list of all runners that are available for the project.

When you register a runner, you can specify the runner’s tags, for example `ruby`, `postgres`, or `development`. To pick up and run a job, a runner must be assigned every tag listed in the job.

Job configuration and default configuration does not merge together. If the pipeline has `default:tags` defined, and the job also has `tags`, the job configuration takes precedence and the default configuration is not used.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- An array of tag names, which are case-sensitive.
- CI/CD variables are supported.

**Example of `tags`**:

```yaml
job:
  tags:
    - ruby
    - postgres
```

In this example, only runners with both the `ruby` and `postgres` tags can run the job.

**Additional details**:

- The number of tags must be less than `50`.

**Related topics**:

- Use tags to control which jobs a runner can run
- Select different runner tags for each parallel matrix job
- Runner tags for hosted runners:
  - Hosted runners on Linux
  - GPU-enabled hosted runners
  - Hosted runners on macOS
  - Hosted runners on Windows

### `timeout`

Use `timeout` to configure a timeout for a specific job. If the job runs for longer than the timeout, the job fails.

The job-level timeout can be longer than the project-level timeout, but can’t be longer than the runner’s timeout.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**: A period of time written in natural language. For example, these are all equivalent:

- `3600 seconds`
- `60 minutes`
- `one hour`

**Example of `timeout`**:

```yaml
build:
  script: build.sh
  timeout: 3 hours 30 minutes

test:
  script: rspec
  timeout: 3h 30m
```

**Additional details**:

- The `timeout` keyword is not supported in the `default` configuration. Define `timeout` in individual job configurations instead. For more information, see issue 213634.

### `trigger`

Use `trigger` to declare that a job is a “trigger job” which starts a downstream pipeline that is either:

- A multi-project pipeline.
- A child pipeline.

Trigger jobs can use only a limited set of GitLab CI/CD configuration keywords. The keywords available for use in trigger jobs are:

- `allow_failure`.
- `extends`.
- `needs`, but not `needs:project`.
- `only` and `except`.
- `parallel`.
- `rules`.
- `stage`.
- `trigger`.
- `variables`.
- `when` (only with a value of `on_success`, `on_failure`, `always`, or `manual`).
- `resource_group`.
- `environment`.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- For multi-project pipelines, the path to the downstream project. CI/CD variables are supported in GitLab 15.3 and later, but not job-only variables. Alternatively, use `trigger:project`.
- For child pipelines, use `trigger:include`.

**Example of `trigger`**:

```yaml
trigger-multi-project-pipeline:
  trigger: my-group/my-project
```

**Additional details**:

- You can use `when:manual` in the same job as `trigger`, but you cannot use the API to start `when:manual` trigger jobs. See issue 284086 for more details.
- You cannot manually specify CI/CD variables before running a manual trigger job.
- CI/CD variables defined in a top-level `variables` section (globally) or in the trigger job are forwarded to the downstream pipeline as trigger variables.
- Pipeline variables are not passed to downstream pipelines by default. Use `trigger:forward` to forward these variables to downstream pipelines.
- Job-only variables are not available in trigger jobs.
- Environment variables defined in the runner’s `config.toml` are not available to trigger jobs and are not passed to downstream pipelines.
- You cannot use `needs:pipeline:job` in a trigger job.

**Related topics**:

- Multi-project pipeline configuration examples.
- To run a pipeline for a specific branch, tag, or commit, you can use a trigger token to authenticate with the pipeline triggers API. The trigger token is different than the `trigger` keyword.

#### `trigger:inputs`

- Introduced in GitLab 17.11.

Use `trigger:inputs` to set the inputs for a multi-project pipeline when the downstream pipeline configuration uses `spec:inputs`.

**Example of `trigger:inputs`**:

```yaml
trigger:
  - project: 'my-group/my-project'
    inputs:
      website: "My website"
```

#### `trigger:include`

Use `trigger:include` to declare that a job is a “trigger job” which starts a child pipeline.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- The path to the child pipeline’s configuration file.

**Example of `trigger:include`**:

```yaml
trigger-child-pipeline:
  trigger:
    include: path/to/child-pipeline.gitlab-ci.yml
```

**Additional details**:

Use:

- `trigger:include:artifact` to trigger a dynamic child pipeline.
- `trigger:include:inputs` to set the inputs when the downstream pipeline configuration uses `spec:inputs`.
- `trigger:include:local` for a path to a child pipeline configuration file when:
  - Combining multiple child pipeline configuration files.
  - Combined with `trigger:include:inputs` to pass inputs to the child pipeline. For example:`staging-job: trigger: include: - local: path/to/child-pipeline.yml inputs: environment: staging`
- `trigger:include:project` to trigger a child pipeline with a configuration file in a different project. If the file contains additional `include` entries, GitLab looks for the files in the project running the pipeline, not the project hosting the file.
- `trigger:include:template` to trigger a child pipeline with a CI/CD template.

**Related topics**:

- Child pipeline configuration examples.

#### `trigger:include:inputs`

- Introduced in GitLab 17.11.

Use `trigger:include:inputs` to set the inputs for a child pipeline when the downstream pipeline configuration uses `spec:inputs`.

**Example of `trigger:inputs`**:

```yaml
trigger-job:
  trigger:
    include:
      - local: path/to/child-pipeline.yml
        inputs:
          website: "My website"
```

#### `trigger:project`

Use `trigger:project` to declare that a job is a “trigger job” which starts a multi-project pipeline.

By default, the multi-project pipeline triggers for the default branch. Use `trigger:branch` to specify a different branch.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- The path to the downstream project. CI/CD variables are supported in GitLab 15.3 and later, but not job-only variables.

**Example of `trigger:project`**:

```yaml
trigger-multi-project-pipeline:
  trigger:
    project: my-group/my-project
```

**Example of `trigger:project` for a different branch**:

```yaml
trigger-multi-project-pipeline:
  trigger:
    project: my-group/my-project
    branch: development
```

**Related topics**:

- Multi-project pipeline configuration examples.
- To run a pipeline for a specific branch, tag, or commit, you can also use a trigger token to authenticate with the pipeline triggers API. The trigger token is different than the `trigger` keyword.

#### `trigger:strategy`

- `strategy:mirror` option introduced in GitLab 18.2.

Use `trigger:strategy` to force the `trigger` job to wait for the downstream pipeline to complete before it is marked as **success**.

This behavior is different than the default, which is for the `trigger` job to be marked as **success** as soon as the downstream pipeline is created.

This setting makes your pipeline execution linear rather than parallel.

**Supported values**:

- `mirror`: Mirrors the status of the downstream pipeline exactly.
- `depend`: Not recommended, use `mirror` instead. The trigger job status shows **failed**, **success**, or **running**, depending on the downstream pipeline status. See additional details.

**Example of `trigger:strategy`**:

```yaml
trigger_job:
  trigger:
    include: path/to/child-pipeline.yml
    strategy: mirror
```

In this example, jobs from subsequent stages wait for the triggered pipeline to successfully complete before starting.

**Additional details**:

- Optional manual jobs in the downstream pipeline do not affect the status of the downstream pipeline or the upstream trigger job. The downstream pipeline can complete successfully without running any optional manual jobs.
- By default, jobs in later stages do not start until the trigger job completes.
- Blocking manual jobs in the downstream pipeline must run before the trigger job is marked as successful or failed.
- When using `strategy:depend` (no longer recommended, use `strategy:mirror` instead):
  - The trigger job shows **running** ( ) if the downstream pipeline status is **waiting for manual action** ( ) due to manual jobs.
  - If the downstream pipeline has a failed job, but the job uses `allow_failure: true`, the downstream pipeline is considered successful and the trigger job shows **success**.

#### `trigger:forward`

Use `trigger:forward` to specify what to forward to the downstream pipeline. You can control what is forwarded to both parent-child pipelines and multi-project pipelines.

Forwarded variables do not get forwarded again in nested downstream pipelines by default, unless the nested downstream trigger job also uses `trigger:forward`.

**Supported values**:

- `yaml_variables`: `true` (default), or `false`. When `true`, variables defined in the trigger job are passed to downstream pipelines.
- `pipeline_variables`: `true` or `false` (default). When `true`, pipeline variables are passed to the downstream pipeline.

**Example of `trigger:forward`**:

Run this pipeline manually, with the CI/CD variable `MYVAR = my value`:

```yaml
variables: # default variables for each job
  VAR: value

---

# Default behavior:
---

# - VAR is passed to the child
---

# - MYVAR is not passed to the child
child1:
  trigger:
    include: .child-pipeline.yml

---

# Forward pipeline variables:
---

# - VAR is passed to the child
---

# - MYVAR is passed to the child
child2:
  trigger:
    include: .child-pipeline.yml
    forward:
      pipeline_variables: true

---

# Do not forward YAML variables:
---

# - VAR is not passed to the child
---

# - MYVAR is not passed to the child
child3:
  trigger:
    include: .child-pipeline.yml
    forward:
      yaml_variables: false
```

**Additional details**:

- CI/CD variables forwarded to downstream pipelines with `trigger:forward` are pipeline variables, which have high precedence. If a variable with the same name is defined in the downstream pipeline, that variable is usually overwritten by the forwarded variable.

### `when`

Use `when` to configure the conditions for when jobs run. If not defined in a job, the default value is `when: on_success`.

**Keyword type**: Job keyword. You can use it as part of a job. `when: always` and `when: never` can also be used in `workflow:rules`.

**Supported values**:

- `on_success` (default): Run the job only when no jobs in earlier stages fail.
- `on_failure`: Run the job only when at least one job in an earlier stage fails.
- `never`: Don’t run the job regardless of the status of jobs in earlier stages. Can only be used in a `rules` section or `workflow: rules`.
- `always`: Run the job regardless of the status of jobs in earlier stages.
- `manual`: Add the job to the pipeline as a manual job.
- `delayed`: Add the job to the pipeline as a delayed job.

**Example of `when`**:

```yaml
stages:
  - build
  - cleanup_build
  - test
  - deploy
  - cleanup

build_job:
  stage: build
  script:
    - make build

cleanup_build_job:
  stage: cleanup_build
  script:
    - cleanup build when failed
  when: on_failure

test_job:
  stage: test
  script:
    - make test

deploy_job:
  stage: deploy
  script:
    - make deploy
  when: manual
  environment: production

cleanup_job:
  stage: cleanup
  script:
    - cleanup after jobs
  when: always
```

In this example, the script:

1. Executes `cleanup_build_job` only when `build_job` fails.
2. Always executes `cleanup_job` as the last step in pipeline regardless of success or failure.
3. Executes `deploy_job` when you run it manually in the GitLab UI.

**Additional details**:

- When evaluating the status of jobs for `on_success` and `on_failure`:
  - Jobs with `allow_failure: true` in earlier stages are considered successful, even if they failed.
  - Skipped jobs in earlier stages, for example manual jobs that have not been started, are considered successful.
- The default value for `allow_failure` is `true` with `when: manual`. The default value changes to `false` with `rules:when: manual`.

**Related topics**:

- `when` can be used with `rules` for more dynamic job control.
- `when` can be used with `workflow` to control when a pipeline can start.

#### `manual_confirmation`

- Introduced in GitLab 17.1.
- Support for environment stop jobs introduced in GitLab 18.3.

Use `manual_confirmation` with `when: manual` to define a custom confirmation message for manual jobs. If no manual job is defined with `when: manual`, this keyword has no effect.

Manual confirmation works with all manual jobs, including environment stop jobs that use `environment:action: stop`.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- A string with the confirmation message.

**Example of `manual_confirmation`**:

```yaml
delete_job:
  stage: post-deployment
  script:
    - make delete
  when: manual
  manual_confirmation: 'Are you sure you want to delete this environment?'

stop_production:
  stage: cleanup
  script:
    - echo "Stopping production environment"
  environment:
    name: production
    action: stop
  when: manual
  manual_confirmation: "Are you sure you want to stop the production environment?"
```

### `start_in`

Use `start_in` to delay the execution of a job for a specified duration after the job is created. You must configure `when: delayed` for the job.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Possible inputs**: A period of time in seconds, minutes, or hours. Must be less than or equal to one week. Examples of valid values:

- `'5'` (5 seconds)
- `'10 seconds'`
- `'30 minutes'`
- `'1 hour'`
- `'1 day'`

**Example of `start_in`**:

```yaml
deploy_production:
  stage: deploy
  script:
    - echo "Deploying to production"
  when: delayed
  start_in: 30 minutes
```

In this example, the `deploy_production` job starts 30 minutes after the previous stage completes.

**Additional details**:

- The timer starts when the job’s stage begins, not when the previous job finishes.
- To manually start a delayed job immediately, select **Play** ( ) in the pipeline view.
- The minimum delay period is one second and the maximum delay is one week.
- `start_in` only works when `when` is set to `delayed`. If you use any other value for `when`, the configuration is invalid. If a job uses `rules`, `start_in` and `when` must be defined in the `rules`, not at the job level. Otherwise, you receive a validation error: `config key may not be used with 'rules': start_in`.
- `start_in` is not supported with `workflow:rules`, but does not cause any syntax violation.

**Related topics**:

- Run a job after a delay


## `variables`

Use `variables` to define CI/CD variables.

Variables can be defined in a CI/CD job, or as a top-level (global) keyword to define default CI/CD variables for all jobs.

**Additional details**:

- All YAML-defined variables are also set to any linked Docker service containers.
- YAML-defined variables are meant for non-sensitive project configuration. Store sensitive information in protected variables or CI/CD secrets.
- Manual pipeline variables and scheduled pipeline variables are not passed to downstream pipelines by default. Use `trigger:forward` to forward these variables to downstream pipelines.

**Related topics**:

- Predefined variables are variables the runner automatically creates and makes available in the job.
- You can configure runner behavior with variables.

### Job `variables`

You can use job variables in commands in the job’s `script`, `before_script`, or `after_script` sections, and also with some job keywords. Check the **Supported values** section of each job keyword to see if it supports variables.

You cannot use job variables as values for global keywords like `include`.

**Supported values**: Variable name and value pairs:

- The name can use only numbers, letters, and underscores (`_`). In some shells, the first character must be a letter.
- The value must be a string.

CI/CD variables are supported.

**Example of job `variables`**:

```yaml
review_job:
  variables:
    DEPLOY_SITE: "https://dev.example.com/"
    REVIEW_PATH: "/review"
  script:
    - deploy-review-script --url $DEPLOY_SITE --path $REVIEW_PATH
```

In this example:

- `review_job` has `DEPLOY_SITE` and `REVIEW_PATH` job variables defined. Both job variables can be used in the `script` section.

### Default `variables`

Variables defined in a top-level `variables` section act as default variables for all jobs.

Each default variable is made available to every job in the pipeline, except when the job already has a variable defined with the same name. The variable defined in the job takes precedence, so the value of the default variable with the same name cannot be used in the job.

Like job variables, you cannot use default variables as values for other global keywords, like `include`.

**Supported values**: Variable name and value pairs:

- The name can use only numbers, letters, and underscores (`_`). In some shells, the first character must be a letter.
- The value must be a string.

CI/CD variables are supported.

**Examples of `variables`**:

```yaml
variables:
  DEPLOY_SITE: "https://example.com/"

deploy_job:
  stage: deploy
  script:
    - deploy-script --url $DEPLOY_SITE --path "/"
  environment: production

deploy_review_job:
  stage: deploy
  variables:
    DEPLOY_SITE: "https://dev.example.com/"
    REVIEW_PATH: "/review"
  script:
    - deploy-review-script --url $DEPLOY_SITE --path $REVIEW_PATH
  environment: production
```

In this example:

- `deploy_job` has no variables defined. The default `DEPLOY_SITE` variable is copied to the job and can be used in the `script` section.
- `deploy_review_job` already has a `DEPLOY_SITE` variable defined, so the default `DEPLOY_SITE` is not copied to the job. The job also has a `REVIEW_PATH` job variable defined. Both job variables can be used in the `script` section.

#### `variables:description`

Use the `description` keyword to define a description for a default variable. The description displays with the prefilled variable name when running a pipeline manually.

**Keyword type**: You can only use this keyword with default `variables`, not job `variables`.

**Supported values**:

- A string. You can use Markdown.

**Example of `variables:description`**:

```yaml
variables:
  DEPLOY_NOTE:
    description: "The deployment note. Explain the reason for this deployment."
```

**Additional details**:

- When used without `value`, the variable exists in pipelines that were not triggered manually, and the default value is an empty string (`''`).

#### `variables:value`

Use the `value` keyword to define a pipeline-level (default) variable’s value. When used with `variables: description`, the variable value is prefilled when running a pipeline manually.

**Keyword type**: You can only use this keyword with default `variables`, not job `variables`.

**Supported values**:

- A string.

**Example of `variables:value`**:

```yaml
variables:
  DEPLOY_ENVIRONMENT:
    value: "staging"
    description: "The deployment target. Change this variable to 'canary' or 'production' if needed."
```

**Additional details**:

- If used without `variables: description`, the behavior is the same as `variables`.

#### `variables:options`

Use `variables:options` to define an array of values that are selectable in the UI when running a pipeline manually.

Must be used with `variables: value`, and the string defined for `value`:

- Must also be one of the strings in the `options` array.
- Is the default selection.

If there is no `description`, this keyword has no effect.

**Keyword type**: You can only use this keyword with default `variables`, not job `variables`.

**Supported values**:

- An array of strings.

**Example of `variables:options`**:

```yaml
variables:
  DEPLOY_ENVIRONMENT:
    value: "staging"
    options:
      - "production"
      - "staging"
      - "canary"
    description: "The deployment target. Set to 'staging' by default."
```

### `variables:expand`

Use the `expand` keyword to configure a variable to be expandable or not.

**Keyword type**: You can use this keyword with both default and job `variables`.

**Supported values**:

- `true` (default): The variable is expandable.
- `false`: The variable is not expandable.

**Example of `variables:expand`**:

```yaml
variables:
  VAR1: value1
  VAR2: value2 $VAR1
  VAR3:
    value: value3 $VAR1
    expand: false
```

- The result of `VAR2` is `value2 value1`.
- The result of `VAR3` is `value3 $VAR1`.

**Additional details**:

- The `expand` keyword can only be used with default and job `variables` keywords. You can’t use it with `rules:variables` or `workflow:rules:variables`.
