---
title: "CI/CD YAML syntax reference (part 3/4)"
source: https://docs.gitlab.com/ee/ci/yaml/
domain: gitlab-ci
license: CC-BY-SA-4.0
tags: gitlab ci, gitlab pipeline, ci cd pipeline, continuous integration
fetched: 2026-07-02
part: 3/4
---

### `pages`

Use `pages` to define a GitLab Pages job that uploads static content to GitLab. The content is then published as a website.

You must:

- Define `pages: true` to publish a directory named `public`
- Alternatively, define `pages.publish` if want to use a different content directory.
- Have a non-empty `index.html` file in the root of the content directory.

**Keyword type**: Job keyword or Job name (deprecated). You can use it only as part of a job.

**Supported Values**:

- A boolean. Uses the default configuration when set to `true`
- A hash of configuration options, see the following sections for details.

**Example of `pages`**:

```yaml
create-pages:
  stage: deploy
  script:
    - mv my-html-content public
  pages: true  # specifies that this is a Pages job and publishes the default public directory
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
  environment: production
```

This example renames the `my-html-content/` directory to `public/`. This directory is exported as an artifact and published with GitLab Pages.

**Example using a configuration hash**:

```yaml
create-pages:
  stage: deploy
  script:
    - echo "nothing to do here"
  pages:  # specifies that this is a Pages job and publishes the default public directory
    publish: my-html-content
    expire_in: "1 week"
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
  environment: production
```

This example does not move the directory, but uses the `publish` property directly. It also configures the pages deployment to be unpublished after a week.

**Additional details**:

- Using `pages` as a job name is deprecated.
- To use `pages` as a job name without triggering a Pages deployment, set the `pages` property to false

#### `pages.publish`

- Changed to allow variables when passed to `publish` property in GitLab 17.9.
- Moved the `publish` property under the `pages` keyword in GitLab 17.9.
- Appended the `pages.publish` path automatically to `artifacts:paths` in GitLab 17.10.

Use `pages.publish` to configure the content directory of a `pages` job.

**Keyword type**: Job keyword. You can use it only as part of a `pages` job.

**Supported values**: A path to a directory containing the Pages content. In GitLab 17.10 and later, if not specified, the default `public` directory is used and if specified, this path is automatically appended to `artifacts:paths`.

**Example of `pages.publish`**:

```yaml
create-pages:
  stage: deploy
  script:
    - npx @11ty/eleventy --input=path/to/eleventy/root --output=dist
  pages:
    publish: dist  # this path is automatically appended to artifacts:paths
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
  environment: production
```

This example uses Eleventy to generate a static website and output the generated HTML files into a the `dist/` directory. This directory is exported as an artifact and published with GitLab Pages.

It is also possible to use variables in the `pages.publish` field. For example:

```yaml
create-pages:
  stage: deploy
  script:
    - mkdir -p $CUSTOM_FOLDER/$CUSTOM_PATH
    - cp -r public $CUSTOM_FOLDER/$CUSTOM_SUBFOLDER
  pages:
    publish: $CUSTOM_FOLDER/$CUSTOM_SUBFOLDER  # this path is automatically appended to artifacts:paths
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
  variables:
    CUSTOM_FOLDER: "custom_folder"
    CUSTOM_SUBFOLDER: "custom_subfolder"
```

The publish path specified must be relative to the build root.

**Additional details**:

- The top-level `publish` keyword is deprecated and must now be nested under the `pages` keyword

#### `pages.path_prefix`

- Tier: Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated
- Status: Beta

- Introduced in GitLab 16.7 as an experiment with a flag named `pages_multiple_versions_setting`, disabled by default.
- Enabled on GitLab.com, GitLab Self-Managed, and GitLab Dedicated in GitLab 17.4.
- Changed to allow periods in GitLab 17.8.
- Generally available in GitLab 17.9. Feature flag `pages_multiple_versions_setting` removed.

Use `pages.path_prefix` to configure a path prefix for parallel deployments of GitLab Pages.

**Keyword type**: Job keyword. You can use it only as part of a `pages` job.

**Supported values**:

- A string
- CI/CD variables
- A combination of both

The given value is converted to lowercase and shortened to 63 bytes. Everything except alphanumeric characters or periods is replaced with a hyphen. Leading and trailing hyphens or periods are not permitted.

**Example of `pages.path_prefix`**:

```yaml
create-pages:
  stage: deploy
  script:
    - echo "Pages accessible through ${CI_PAGES_URL}"
  pages:  # specifies that this is a Pages job and publishes the default public directory
    path_prefix: "$CI_COMMIT_BRANCH"
```

In this example, a different pages deployment is created for each branch.

#### `pages.expire_in`

- Tier: Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

- Introduced in GitLab 17.4.
- Support for variables introduced in GitLab 17.11.

Use `expire_in` to specify how long a deployment should be available before it expires. After the deployment is expired, it’s deactivated by a cron job running every 10 minutes.

By default, parallel deployments expire automatically after 24 hours. To disable this behavior, set the value to `never`.

**Keyword type**: Job keyword. You can use it only as part of a `pages` job.

**Supported values**: The expiry time. If no unit is provided, the time is in seconds. Variables are also supported. Valid values include:

- `'42'`
- `42 seconds`
- `3 mins 4 sec`
- `2 hrs 20 min`
- `2h20min`
- `6 mos 1 day`
- `47 yrs 6 mos and 4d`
- `3 weeks and 2 days`
- `never`
- `$DURATION`

**Example of `pages.expire_in`**:

```yaml
create-pages:
  stage: deploy
  script:
    - echo "Pages accessible through ${CI_PAGES_URL}"
  pages:  # specifies that this is a Pages job and publishes the default public directory
    expire_in: 1 week
```

### `parallel`

Use `parallel` to run a job multiple times in parallel in a single pipeline.

Multiple runners must exist, or a single runner must be configured to run multiple jobs concurrently.

Parallel jobs are named sequentially from `job_name 1/N` to `job_name N/N`.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- A numeric value from `1` to `200`.

**Example of `parallel`**:

```yaml
test:
  script: rspec
  parallel: 5
```

This example creates 5 jobs that run in parallel, named `test 1/5` to `test 5/5`.

**Additional details**:

- Every parallel job has a `CI_NODE_INDEX` and `CI_NODE_TOTAL` predefined CI/CD variable set.
- A pipeline with jobs that use `parallel` might:
  - Create more jobs running in parallel than available runners. Excess jobs are queued and marked `pending` while waiting for an available runner.
  - Fail with a `job_activity_limit_exceeded` error if creating the pipeline would cause the total number of jobs across all active pipelines to exceed the instance limit.

**Related topics**:

- Parallelize large jobs.

#### `parallel:matrix`

Use `parallel:matrix` to run a job multiple times in parallel in a single pipeline, but with different variable values for each instance of the job.

Multiple runners must exist, or a single runner must be configured to run multiple jobs concurrently.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**: An array of hashes of variables:

- The matrix identifiers, which become the variable names, can use only numbers, letters, and underscores (`_`).
- The values must be either a string, or an array of strings.
- The number of permutations cannot exceed 200.

**Example of `parallel:matrix`**:

```yaml
deploystacks:
  stage: deploy
  script:
    - bin/deploy
  parallel:
    matrix:
      - PROVIDER: aws
        STACK:
          - monitoring
          - app1
          - app2
      - PROVIDER: [gcp, vultr]
        STACK: [data, processing]
  environment: $PROVIDER/$STACK
```

The example generates 7 parallel `deploystacks` jobs, each with different values for `PROVIDER` and `STACK`:

- `deploystacks: [aws, monitoring]`
- `deploystacks: [aws, app1]`
- `deploystacks: [aws, app2]`
- `deploystacks: [gcp, data]`
- `deploystacks: [gcp, processing]`
- `deploystacks: [vultr, data]`
- `deploystacks: [vultr, processing]`

**Additional details**:

- `parallel:matrix` jobs add the matrix values to the job names to differentiate the jobs from each other. However, long values can cause job names to exceed the 255-character limit. For more information, see epic 11791.
- Matrix variable values are available as CI/CD variables in `rules:if` expressions. For more information, see Use matrix variables in `rules:if`.
- You cannot create multiple matrix configurations with the same values but different names. Job names are generated from the matrix values, not the names, so matrix entries with identical values generate identical job names that overwrite each other.For example, this `test` configuration would try to create two series of identical jobs, but the `OS2` versions overwrite the `OS` versions:`test: parallel: matrix: - OS: [ubuntu] PROVIDER: [aws, gcp] - OS2: [ubuntu] PROVIDER: [aws, gcp]`

**Related topics**:

- Run a one-dimensional matrix of parallel jobs.
- Run a matrix of triggered parallel jobs.
- Select different runner tags for each parallel matrix job.
- Use matrix variables in rules.
- Matrix expressions in `needs:parallel:matrix`.

### `release`

Use `release` to create a release.

The release job must have access to the `glab` CLI, which must be in the `$PATH`.

If you use the Docker executor, you can use this image from the GitLab container registry: `registry.gitlab.com/gitlab-org/cli:latest`

If you use the Shell executor or similar, install `glab` CLI on the server where the runner is registered.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**: The `release` subkeys:

- `tag_name`
- `tag_message` (optional)
- `name` (optional)
- `description`
- `ref` (optional)
- `milestones` (optional)
- `released_at` (optional)
- `assets:links` (optional)

**Example of `release` keyword**:

```yaml
release_job:
  stage: release
  image: registry.gitlab.com/gitlab-org/cli:latest
  rules:
    - if: $CI_COMMIT_TAG                  # Run this job when a tag is created manually
  script:
    - echo "Running the release job."
  release:
    tag_name: $CI_COMMIT_TAG
    name: 'Release $CI_COMMIT_TAG'
    description: 'Release created using the CLI.'
```

This example creates a release:

- When you push a Git tag.
- When you add a Git tag in the UI at **Code** > **Tags**.

**Additional details**:

- Release jobs must include the `script` keyword. A release job can use the output from script commands. If you don’t need the script, you can use a placeholder:`script: - echo "release job"`For more details, see issue 223856, which aims to remove this restriction.
- The `release` section executes after the `script` keyword and before the `after_script`.
- A release is created only if the job’s main script succeeds.
- If the release already exists, it is not updated and the job with the `release` keyword fails.

**Related topics**:

- CI/CD example of the `release` keyword.
- Create multiple releases in a single pipeline.
- Use a custom SSL CA certificate authority.

#### `release:tag_name`

Required. The Git tag for the release.

If the tag does not exist in the project yet, it is created at the same time as the release. New tags use the SHA associated with the pipeline.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- A tag name.

CI/CD variables are supported.

**Example of `release:tag_name`**:

To create a release when a new tag is added to the project:

- Use the `$CI_COMMIT_TAG` CI/CD variable as the `tag_name`.
- Use `rules:if` to configure the job to run only for new tags.

```yaml
job:
  script: echo "Running the release job for the new tag."
  release:
    tag_name: $CI_COMMIT_TAG
    description: 'Release description'
  rules:
    - if: $CI_COMMIT_TAG
```

To create a release and a new tag at the same time, your `rules` should not configure the job to run only for new tags. A semantic versioning example:

```yaml
job:
  script: echo "Running the release job and creating a new tag."
  release:
    tag_name: ${MAJOR}_${MINOR}_${REVISION}
    description: 'Release description'
  rules:
    - if: $CI_PIPELINE_SOURCE == "schedule"
```

#### `release:tag_message`

If the tag does not exist, the newly created tag is annotated with the message specified by `tag_message`. If omitted, a lightweight tag is created.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- A text string.

**Example of `release:tag_message`**:

```yaml
  release_job:
    stage: release
    release:
      tag_name: $CI_COMMIT_TAG
      description: 'Release description'
      tag_message: 'Annotated tag message'
```

#### `release:name`

The release name. If omitted, it is populated with the value of `release: tag_name`.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- A text string.

**Example of `release:name`**:

```yaml
  release_job:
    stage: release
    release:
      name: 'Release $CI_COMMIT_TAG'
```

#### `release:description`

The long description of the release.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- A string with the long description.
- The path to a file that contains the description.
  - The file location must be relative to the project directory (`$CI_PROJECT_DIR`).
  - If the file is a symbolic link, it must be in the `$CI_PROJECT_DIR`.
  - The `./path/to/file` and filename can’t contain spaces.

**Example of `release:description`**:

```yaml
job:
  release:
    tag_name: ${MAJOR}_${MINOR}_${REVISION}
    description: './path/to/CHANGELOG.md'
```

**Additional details**:

- The `description` is evaluated by the shell that runs `glab`. You can use CI/CD variables to define the description, but some shells use different syntax to reference variables. Similarly, some shells might require special characters to be escaped. For example, backticks (`) might need to be escaped with a backslash (`\`).

#### `release:ref`

The `ref` for the release, if the `release: tag_name` doesn’t exist yet.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- A commit SHA, another tag name, or a branch name.

#### `release:milestones`

The title of each milestone the release is associated with.

#### `release:released_at`

The date and time when the release is ready.

**Supported values**:

- A date enclosed in quotes and expressed in ISO 8601 format.

**Example of `release:released_at`**:

```yaml
released_at: '2021-03-15T08:00:00Z'
```

**Additional details**:

- If it is not defined, the current date and time is used.

#### `release:assets:links`

Use `release:assets:links` to include asset links in the release.

**Example of `release:assets:links`**:

```yaml
assets:
  links:
    - name: 'asset1'
      url: 'https://example.com/assets/1'
    - name: 'asset2'
      url: 'https://example.com/assets/2'
      filepath: '/pretty/url/1' # optional
      link_type: 'other' # optional
```

### `resource_group`

Use `resource_group` to create a resource group that ensures a job is mutually exclusive across different pipelines for the same project.

For example, if multiple jobs that belong to the same resource group are queued simultaneously, only one of the jobs starts. The other jobs wait until the `resource_group` is free.

Resource groups behave similar to semaphores in other programming languages.

You can choose a process mode to strategically control the job concurrency for your deployment preferences. The default process mode is `unordered`. To change the process mode of a resource group, use the API to send a request to edit an existing resource group.

You can define multiple resource groups per environment. For example, when deploying to physical devices, you might have multiple physical devices. Each device can be deployed to, but only one deployment can occur per device at any given time.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- Only letters, digits, `-`, `_`, `/`, `$`, `{`, `}`, `.`, and spaces. It can’t start or end with `/`. CI/CD variables are supported.

**Example of `resource_group`**:

```yaml
deploy-to-production:
  script: deploy
  resource_group: production
```

In this example, two `deploy-to-production` jobs in two separate pipelines can never run at the same time. As a result, you can ensure that concurrent deployments never happen to the production environment.

**Related topics**:

- Pipeline-level concurrency control with cross-project/parent-child pipelines.

### `retry`

Use `retry` to configure how many times a job is retried if it fails. If not defined, defaults to `0` and jobs do not retry.

When a job fails, the job is processed up to two more times, until it succeeds or reaches the maximum number of retries.

By default, all failure types cause the job to be retried. Use `retry:when` or `retry:exit_codes` to select which failures to retry on.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- `0` (default), `1`, or `2`.

**Example of `retry`**:

```yaml
test:
  script: rspec
  retry: 2

test_advanced:
  script:
    - echo "Run a script that results in exit code 137."
    - exit 137
  retry:
    max: 2
    when: runner_system_failure
    exit_codes: 137
```

`test_advanced` will be retried up to 2 times if the exit code is `137` or if it had a runner system failure.

#### `retry:when`

Use `retry:when` with `retry:max` to retry jobs for only specific failure cases. `retry:max` is the maximum number of retries, like `retry`, and can be `0`, `1`, or `2`.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- A single failure type, or an array of one or more failure types:

- `always`: Retry on any failure (default).
- `unknown_failure`: Retry when the failure reason is unknown.
- `script_failure`: Retry when:
  - The script failed.
  - The runner failed to pull the Docker image. For `docker`, `docker+machine`, `kubernetes` executors.
  - Introduced in GitLab 19.1, some failures are changed from `script_failure` to the more accurate `runner_configuration_error`.
- `api_failure`: Retry on API failure.
- `stuck_or_timeout_failure`: Retry when the job got stuck or timed out. Deprecated in GitLab 19.1. Retries on any of `stuck_pending_with_matching_runners`, `stuck_pending_no_matching_runners`, `no_updates_running`, or `no_updates_canceling`. Use those values instead.
- `runner_system_failure`: Retry if there is a runner system failure (for example, job setup failed).
  - Introduced in GitLab 19.1, some failures are changed from `runner_system_failure` to the more accurate `runner_external_dependency_failure` or `runner_interrupted`.
- `runner_configuration_error`: Retry if the job failed because of a CI/CD or runner configuration error, for example an invalid image or tag, an incompatible pull policy, or a misconfigured runner.
- `runner_external_dependency_failure`: Retry if the runner could not reach an external dependency like an image registry because of a network or DNS problem.
- `runner_interrupted`: Retry if the runner was interrupted while the job was running, for example by a restart, shutdown, or host reclamation.
- `runner_unsupported`: Retry if the runner is unsupported.
- `stale_schedule`: Retry if a delayed job could not be executed.
- `job_execution_timeout`: Retry if the script exceeded the maximum execution time set for the job. Deprecated in GitLab 19.1. Retries on either `server_timeout_running` or `server_timeout_canceling`. Use those values instead.
- `archived_failure`: Retry if the job is archived and can’t be run.
- `unmet_prerequisites`: Retry if the job failed to complete prerequisite tasks.
- `scheduler_failure`: Retry if the scheduler failed to assign the job to a runner.
- `data_integrity_failure`: Retry if there is an unknown job problem.

**Example of `retry:when`** (single failure type):

```yaml
test:
  script: rspec
  retry:
    max: 2
    when: runner_system_failure
```

If there is a failure other than a runner system failure, the job is not retried.

**Example of `retry:when`** (array of failure types):

```yaml
test:
  script: rspec
  retry:
    max: 2
    when:
      - runner_system_failure
      - stuck_or_timeout_failure
```

#### `retry:exit_codes`

- Introduced in GitLab 16.10 with a flag named `ci_retry_on_exit_codes`. Disabled by default.
- Enabled on GitLab.com and GitLab Self-Managed in GitLab 16.11.
- Generally available in GitLab 17.5. Feature flag `ci_retry_on_exit_codes` removed.

Use `retry:exit_codes` with `retry:max` to retry jobs for only specific failure cases. `retry:max` is the maximum number of retries, like `retry`, and can be `0`, `1`, or `2`.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- A single exit code.
- An array of exit codes.

**Example of `retry:exit_codes`**:

```yaml
test_job_1:
  script:
    - echo "Run a script that results in exit code 1. This job isn't retried."
    - exit 1
  retry:
    max: 2
    exit_codes: 137

test_job_2:
  script:
    - echo "Run a script that results in exit code 137. This job will be retried."
    - exit 137
  retry:
    max: 1
    exit_codes:
      - 255
      - 137
```

**Related topics**:

You can specify the number of retry attempts for certain stages of job execution using variables.

### `rules`

Use `rules` to include or exclude jobs in pipelines.

Rules are evaluated when the pipeline is created, and evaluated in order. When a match is found, no more rules are checked and the job is either included or excluded from the pipeline depending on the configuration. If no rules match, the job is not added to the pipeline.

`rules` accepts an array of rules. Each rules must have at least one of:

- `if`
- `changes`
- `exists`
- `when`

Rules can also optionally be combined with:

- `allow_failure`
- `needs`
- `variables`
- `interruptible`

You can combine multiple keywords together for complex rules.

The job is added to the pipeline:

- If an `if`, `changes`, or `exists` rule matches, and is configured with `when: on_success` (default if not defined), `when: delayed`, or `when: always`.
- If a rule is reached that is only `when: on_success`, `when: delayed`, or `when: always`.

The job is not added to the pipeline:

- If no rules match.
- If a rule matches and has `when: never`.

For additional examples, see Specify when jobs run with `rules`.

#### `rules:if`

Use `rules:if` clauses to specify when to add a job to a pipeline:

- If an `if` statement is true, add the job to the pipeline.
- If an `if` statement is true, but it’s combined with `when: never`, do not add the job to the pipeline.
- If an `if` statement is false, check the next `rules` item (if any more exist).

`if` clauses are evaluated:

- Based on the values of CI/CD variables or predefined CI/CD variables, with some exceptions.
- In order, following `rules` execution flow.

**Keyword type**: Job-specific and pipeline-specific. You can use it as part of a job to configure the job behavior, or with `workflow` to configure the pipeline behavior.

**Supported values**:

- A CI/CD variable expression.

**Example of `rules:if`**:

```yaml
job:
  script: echo "Hello, Rules!"
  rules:
    - if: $CI_MERGE_REQUEST_SOURCE_BRANCH_NAME =~ /^feature/ && $CI_MERGE_REQUEST_TARGET_BRANCH_NAME != $CI_DEFAULT_BRANCH
      when: never
    - if: $CI_MERGE_REQUEST_SOURCE_BRANCH_NAME =~ /^feature/
      when: manual
      allow_failure: true
    - if: $CI_MERGE_REQUEST_SOURCE_BRANCH_NAME
```

**Additional details**:

- You cannot use nested variables with `if`. See issue 327780 for more details.
- If a rule matches and has no `when` defined, the rule uses the `when` defined for the job, which defaults to `on_success` if not defined.
- You can mix `when` at the job-level with `when` in rules. `when` configuration in `rules` takes precedence over `when` at the job-level.
- Unlike variables in `script` sections, variables in rules expressions are always formatted as `$VARIABLE`.
  - You can use `rules:if` with `include` to conditionally include other configuration files.
- CI/CD variables on the right side of `=~` and `!~` expressions are evaluated as regular expressions.

**Related topics**:

- Common `if` expressions for `rules`.
- Avoid duplicate pipelines.
- Use `rules` to run merge request pipelines.

#### `rules:changes`

Use `rules:changes` to specify when to add a job to a pipeline by checking for changes to specific files.

For new branch pipelines or when there is no Git `push` event, `rules: changes` always evaluates to true and the job always runs. Pipelines like tag pipelines, scheduled pipelines, and manual pipelines, all do not have a Git `push` event associated with them. To cover these cases, use `rules: changes: compare_to` to specify the branch to compare against the pipeline ref.

If you do not use `compare_to`, you should use `rules: changes` only with branch pipelines or merge request pipelines, though `rules: changes` still evaluates to true when creating a new branch. With:

- Merge request pipelines, `rules:changes` compares the changes with the target MR branch.
- Branch pipelines, `rules:changes` compares the changes with the previous commit on the branch.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

An array including any number of:

- Paths to files. The file paths can include CI/CD variables.
- Wildcard paths for:
  - Single directories, for example `path/to/directory/*`.
  - A directory and all its subdirectories, for example `path/to/directory/**/*`.
- Wildcard glob paths for all files with the same extension or multiple extensions, for example `*.md` or `path/to/directory/*.{rb,py,sh}`.
- Wildcard paths to files in the root directory, or all directories, wrapped in double quotes. For example `"*.json"` or `"**/*.json"`.

**Example of `rules:changes`**:

```yaml
docker build:
  script: docker build -t my-image:$CI_COMMIT_REF_SLUG .
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      changes:
        - Dockerfile
      when: manual
      allow_failure: true

docker build alternative:
  variables:
    DOCKERFILES_DIR: 'path/to/dockerfiles'
  script: docker build -t my-image:$CI_COMMIT_REF_SLUG .
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      changes:
        - $DOCKERFILES_DIR/**/*
```

In this example:

- If the pipeline is a merge request pipeline, check `Dockerfile` and the files in `$DOCKERFILES_DIR/**/*` for changes.
- If `Dockerfile` has changed, add the job to the pipeline as a manual job, and the pipeline continues running even if the job is not triggered (`allow_failure: true`).
- If a file in `$DOCKERFILES_DIR/**/*` has changed, add the job to the pipeline.
- If no listed files have changed, do not add either job to any pipeline (same as `when: never`).

**Additional details**:

- Glob patterns are interpreted with Ruby’s `File.fnmatch` with the flags `File::FNM_PATHNAME | File::FNM_DOTMATCH | File::FNM_EXTGLOB`.
- For performance reasons, GitLab performs a maximum of 50,000 checks against `changes` patterns or file paths. After the 50,000th check, rules with patterned globs always match. In other words, the `changes` rule always assumes a match when more than 50,000 files changed, or if there are fewer than 50,000 changed files but the `changes` rules are checked more than 50,000 times.
- A maximum of 50 patterns or file paths can be defined per `rules:changes` section.
- `changes` resolves to `true` if any of the matching files are changed (an `OR` operation).
- For additional examples, see Specify when jobs run with `rules`.
- You can use the `$` character for both variables and paths. For example, if the `$VAR` variable exists, its value is used. If it does not exist, the `$` is interpreted as being part of a path.
- Do not use `./`, double slashes (`//`), or any other kind of relative path. Paths are matched with exact string comparison, they are not evaluated like in a shell.

**Related topics**:

- Jobs or pipelines can run unexpectedly when using `rules: changes`.

##### `rules:changes:paths`

Use `rules:changes` to specify that a job only be added to a pipeline when specific files are changed, and use `rules:changes:paths` to specify the files.

`rules:changes:paths` is the same as using `rules:changes` without any subkeys. All additional details and related topics are the same.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- Same as `rules:changes`.

**Example of `rules:changes:paths`**:

```yaml
docker-build-1:
  script: docker build -t my-image:$CI_COMMIT_REF_SLUG .
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      changes:
        - Dockerfile

docker-build-2:
  script: docker build -t my-image:$CI_COMMIT_REF_SLUG .
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      changes:
        paths:
          - Dockerfile
```

In this example, both jobs have the same behavior.

##### `rules:changes:compare_to`

- Support for CI/CD variables introduced in GitLab 17.2.

Use `rules:changes:compare_to` to specify which ref to compare against for changes to the files listed under `rules:changes:paths`.

**Keyword type**: Job keyword. You can use it only as part of a job, and it must be combined with `rules:changes:paths`.

**Supported values**:

- A branch name, like `main`, `branch1`, or `refs/heads/branch1`.
- A tag name, like `tag1` or `refs/tags/tag1`.
- A commit SHA, like `2fg31ga14b`.

CI/CD variables are supported.

**Example of `rules:changes:compare_to`**:

```yaml
docker build:
  script: docker build -t my-image:$CI_COMMIT_REF_SLUG .
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      changes:
        paths:
          - Dockerfile
        compare_to: 'refs/heads/branch1'
```

In this example, the `docker build` job is only included when the `Dockerfile` has changed relative to `refs/heads/branch1` and the pipeline source is a merge request event.

**Additional details**:

- Using `compare_to` in some situation can cause unexpected results:
  - With merged results pipelines, because the comparison base is an internal commit that GitLab creates.
  - In a forked project, see issue 424584.

**Related topics**:

- You can use `rules:changes:compare_to` to skip a job if the branch is empty.

##### `rules:changes:regexp`

- Introduced in GitLab 19.2 with a flag named `ci_rules_regexp`. Disabled by default. When disabled, a job with `regexp:` always runs.

Use `rules:changes:regexp` to match changed file paths using a Ruby regular expression instead of glob patterns.

`regexp:` and `paths:` are mutually exclusive. Use exactly one per `rules:changes` block.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- A Ruby regular expression string. Maximum length is 255 characters. The pattern is matched against each changed file path. The rule is satisfied if at least one path matches.

CI/CD variables are supported. Variables in the pattern are expanded before the pattern is matched. The 255-character limit also applies to the expanded pattern.

**Example of `rules:changes:regexp`**:

```yaml
backend-tests:
  script: rspec
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      changes:
        regexp: '\A(?!docs/).*'
```

In this example, `backend-tests` runs when at least one changed file is outside the `docs/` directory.

**Additional details**:

- The pattern matches any part of the path unless you anchor it. To match the full path, anchor the pattern with `\A` and `\z`.
- Anchor patterns with `\A` and `\z` instead of `^` and `$`. Git allows newlines in file paths, and `^` and `$` match at newline boundaries. A pattern like `^(?!docs/)` can match a crafted path that contains a newline, such as a file under `docs/` followed by a newline and another path.
- Unlike `rules:if`, which uses RE2, `rules:changes:regexp` uses Ruby’s native regular expression engine.
- Lookahead and lookbehind are supported.
- To prevent ReDoS attacks, the pattern is bounded by two timeouts. Each single-path match has a 50 ms timeout, and evaluation across all paths has a 2-second total budget. If either timeout is exceeded, the pipeline fails with a configuration error.
- If the expanded pattern is longer than 255 characters, the pipeline fails with a configuration error.
- For performance reasons, if more than 50,000 files changed, the rule evaluates to `true` without running the pattern.
- You can combine `regexp:` with `compare_to:` to control which ref to compare against.

#### `rules:exists`

- Maximum number of checks against `exists` patterns or file paths increased from 10,000 to 50,000 in GitLab 17.7.
- Support for directory paths introduced in GitLab 18.2.

Use `exists` to run a job when certain files or directories exist in the repository.

**Keyword type**: Job keyword. You can use it as part of a job or an `include`.

**Supported values**:

- An array of file or directory paths. Paths are relative to the project directory (`$CI_PROJECT_DIR`) and can’t directly link outside it. File paths can use glob patterns and CI/CD variables.

**Example of `rules:exists`**:

```yaml
job1:
  script: docker build -t my-image:$CI_COMMIT_REF_SLUG .
  rules:
    - exists:
        - Dockerfile

job2:
  variables:
    DOCKERPATH: "**/Dockerfile"
  script: docker build -t my-image:$CI_COMMIT_REF_SLUG .
  rules:
    - exists:
        - $DOCKERPATH
```

In this example:

- `job1` runs if a `Dockerfile` exists in the root directory of the repository.
- `job2` runs if a `Dockerfile` exists anywhere in the repository.

**Additional details**:

- Glob patterns are interpreted with Ruby’s `File.fnmatch` with the flags `File::FNM_PATHNAME | File::FNM_DOTMATCH | File::FNM_EXTGLOB`.
- For performance reasons, GitLab performs a maximum of 50,000 checks against `exists` patterns or file paths. After the 50,000th check, rules with patterned globs always match. In other words, the `exists` rule always assumes a match in projects with more than 50,000 files, or if there are fewer than 50,000 files but the `exists` rules are checked more than 50,000 times.
  - If there are multiple patterned globs, the limit is 50,000 divided by the number of globs. For example, a rule with 5 patterned globs has file limit of 10,000.
- A maximum of 50 patterns or file paths can be defined per `rules:exists` section.
- `exists` resolves to `true` if any of the listed files are found (an `OR` operation).
- With job-level `rules:exists`, GitLab searches for the files in the project and ref that runs the pipeline. When using `include` with `rules:exists`, GitLab searches for the files or directories in the project and ref of the file that contains the `include` section. The project containing the `include` section can be different than the project running the pipeline when using:
  - Nested includes.
  - Compliance pipelines.
- `rules:exists` cannot search for the presence of artifacts, because `rules` evaluation happens before jobs run and artifacts are fetched.
- To test the existence of a directory, the path must end with a forward slash (/)

##### `rules:exists:paths`

- Introduced in GitLab 16.11 with a flag named `ci_support_rules_exists_paths_and_project`. Disabled by default.
- Generally available in GitLab 17.0. Feature flag `ci_support_rules_exists_paths_and_project` removed.

`rules:exists:paths` is the same as using `rules:exists` without any subkeys. All additional details are the same.

**Keyword type**: Job keyword. You can use it as part of a job or an `include`.

**Supported values**:

- An array of file paths.

**Example of `rules:exists:paths`**:

```yaml
docker-build-1:
  script: docker build -t my-image:$CI_COMMIT_REF_SLUG .
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      exists:
        - Dockerfile

docker-build-2:
  script: docker build -t my-image:$CI_COMMIT_REF_SLUG .
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      exists:
        paths:
          - Dockerfile
```

In this example, both jobs have the same behavior.

##### `rules:exists:project`

- Introduced in GitLab 16.11 with a flag named `ci_support_rules_exists_paths_and_project`. Disabled by default.
- Generally available in GitLab 17.0. Feature flag `ci_support_rules_exists_paths_and_project` removed.

Use `rules:exists:project` to specify the location in which to search for the files listed under `rules:exists:paths`. Must be used with `rules:exists:paths`.

**Keyword type**: Job keyword. You can use it as part of a job or an `include`, and it must be combined with `rules:exists:paths`.

**Supported values**:

- `exists:project`: A full project path, including namespace and group.
- `exists:ref`: Optional. The commit ref to use to search for the file. The ref can be a tag, branch name, or SHA. Defaults to the `HEAD` of the project when not specified.

**Example of `rules:exists:project`**:

```yaml
docker build:
  script: docker build -t my-image:$CI_COMMIT_REF_SLUG .
  rules:
    - exists:
        paths:
          - Dockerfile
        project: my-group/my-project
        ref: v1.0.0
```

In this example, the `docker build` job is only included when the `Dockerfile` exists in the project `my-group/my-project` on the commit tagged with `v1.0.0`.

##### `rules:exists:regexp`

- Introduced in GitLab 19.2 with a flag named `ci_rules_regexp`. Disabled by default. When disabled, a job with `regexp:` always runs.

Use `rules:exists:regexp` to match file paths in the repository using a Ruby regular expression instead of glob patterns.

`regexp:` and `paths:` are mutually exclusive. Use exactly one per `rules:exists` block.

**Keyword type**: Job keyword. You can use it as part of a job or an `include`.

**Supported values**:

- A Ruby regular expression string. Maximum length is 255 characters. The pattern is matched against every file path in the repository. The rule is satisfied if at least one path matches.

CI/CD variables are supported. Variables in the pattern are expanded before the pattern is matched. The 255-character limit also applies to the expanded pattern.

**Example of `rules:exists:regexp`**:

```yaml
run-if-go-files-exist:
  script: go test ./...
  rules:
    - exists:
        regexp: '\.go$'
```

In this example, the job runs if any `.go` file exists anywhere in the repository.

**Additional details**:

- The pattern matches any part of the path unless you anchor it. To match the full path, anchor the pattern with `\A` and `\z`.
- Anchor patterns with `\A` and `\z` instead of `^` and `$`. Git allows newlines in file paths, and `^` and `$` match at newline boundaries. A pattern like `^(?!docs/)` can match a crafted path that contains a newline, such as a file under `docs/` followed by a newline and another path.
- Unlike `rules:if`, which uses RE2, `rules:exists:regexp` uses Ruby’s native regular expression engine.
- Lookahead and lookbehind are supported.
- To prevent ReDoS attacks, the pattern is bounded by two timeouts. Each single-path match has a 50 ms timeout, and evaluation across all paths has a 2-second total budget. If either timeout is exceeded, the pipeline fails with a configuration error.
- If the expanded pattern is longer than 255 characters, the pipeline fails with a configuration error.
- For performance reasons, if the repository contains more than 50,000 files, the rule evaluates to `true` without running the pattern.
- You can combine `regexp:` with `project:` and `ref:` to search in a different project.

#### `rules:when`

Use `rules:when` alone or as part of another rule to control conditions for adding a job to a pipeline. `rules:when` is similar to `when`, but with slightly different input options.

If a `rules:when` rule is not combined with `if`, `changes`, or `exists`, it always matches if reached when evaluating a job’s rules.

**Keyword type**: Job-specific. You can use it only as part of a job.

**Supported values**:

- `on_success` (default): Run the job only when no jobs in earlier stages fail.
- `on_failure`: Run the job only when at least one job in an earlier stage fails.
- `never`: Don’t run the job regardless of the status of jobs in earlier stages.
- `always`: Run the job regardless of the status of jobs in earlier stages.
- `manual`: Add the job to the pipeline as a manual job. The default value for `allow_failure` changes to `false`.
- `delayed`: Add the job to the pipeline as a delayed job.

**Example of `rules:when`**:

```yaml
job1:
  rules:
    - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
    - if: $CI_COMMIT_REF_NAME =~ /feature/
      when: delayed
    - when: manual
  script:
    - echo
```

In this example, `job1` is added to pipelines:

- For the default branch, with `when: on_success` which is the default behavior when `when` is not defined.
- For feature branches as a delayed job.
- In all other cases as a manual job.

**Additional details**:

- When evaluating the status of jobs for `on_success` and `on_failure`:
  - Jobs with `allow_failure: true` in earlier stages are considered successful, even if they failed.
  - Skipped jobs in earlier stages, for example manual jobs that have not been started, are considered successful.
- When using `rules:when: manual` to add a manual job:
  - `allow_failure` becomes `false` by default. This default is the opposite of using `when: manual` to add a manual job.
  - To achieve the same behavior as `when: manual` defined outside of `rules`, set `rules: allow_failure` to `true`.

#### `rules:allow_failure`

Use `allow_failure: true` in `rules` to allow a job to fail without stopping the pipeline.

You can also use `allow_failure: true` with a manual job. The pipeline continues running without waiting for the result of the manual job. `allow_failure: false` combined with `when: manual` in rules causes the pipeline to wait for the manual job to run before continuing.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- `true` or `false`. Defaults to `false` if not defined.

**Example of `rules:allow_failure`**:

```yaml
job:
  script: echo "Hello, Rules!"
  rules:
    - if: $CI_MERGE_REQUEST_TARGET_BRANCH_NAME == $CI_DEFAULT_BRANCH
      when: manual
      allow_failure: true
```

If the rule matches, then the job is a manual job with `allow_failure: true`.

**Additional details**:

- The rule-level `rules:allow_failure` overrides the job-level `allow_failure`, and only applies when the specific rule triggers the job.

#### `rules:needs`

Use `needs` in rules to update a job’s `needs` for specific conditions. When a condition matches a rule, the job’s `needs` configuration is completely replaced with the `needs` in the rule.

**Keyword type**: Job-specific. You can use it only as part of a job.

**Supported values**:

- An array of job names as strings.
- A hash with a job name, optionally with additional attributes.
- An empty array (`[]`), to set the job needs to none when the specific condition is met.

**Example of `rules:needs`**:

```yaml
build-dev:
  stage: build
  rules:
    - if: $CI_COMMIT_BRANCH != $CI_DEFAULT_BRANCH
  script: echo "Feature branch, so building dev version..."

build-prod:
  stage: build
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
  script: echo "Default branch, so building prod version..."

tests:
  stage: test
  rules:
    - if: $CI_COMMIT_BRANCH != $CI_DEFAULT_BRANCH
      needs: ['build-dev']
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
      needs: ['build-prod']
  script: echo "Running dev specs by default, or prod specs when default branch..."
```

In this example:

- If the pipeline runs on a branch that is not the default branch, and therefore the rule matches the first condition, the `specs` job needs the `build-dev` job.
- If the pipeline runs on the default branch, and therefore the rule matches the second condition, the `specs` job needs the `build-prod` job.

**Additional details**:

- `needs` in rules override any `needs` defined at the job-level. When overridden, the behavior is same as job-level `needs`.
- `needs` in rules can accept `artifacts` and `optional`.

#### `rules:variables`

Use `variables` in `rules` to define variables for specific conditions.

**Keyword type**: Job-specific. You can use it only as part of a job.

**Supported values**:

- A hash of variables in the format `VARIABLE-NAME: value`.

**Example of `rules:variables`**:

```yaml
job:
  variables:
    DEPLOY_VARIABLE: "default-deploy"
  rules:
    - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
      variables:                              # Override DEPLOY_VARIABLE defined
        DEPLOY_VARIABLE: "deploy-production"  # at the job level.
    - if: $CI_COMMIT_REF_NAME =~ /feature/
      variables:
        IS_A_FEATURE: "true"                  # Define a new variable.
  script:
    - echo "Run script with $DEPLOY_VARIABLE as an argument"
    - echo "Run another script if $IS_A_FEATURE exists"
```

#### `rules:interruptible`

Use `interruptible` in rules to update a job’s `interruptible` value for specific conditions.

**Keyword type**: Job-specific. You can use it only as part of a job.

**Supported values**:

- `true` or `false`.

**Example of `rules:interruptible`**:
