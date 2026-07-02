---
title: "CI/CD YAML syntax reference (part 1/4)"
source: https://docs.gitlab.com/ee/ci/yaml/
domain: gitlab-ci
license: CC-BY-SA-4.0
tags: gitlab ci, gitlab pipeline, ci cd pipeline, continuous integration
fetched: 2026-07-02
part: 1/4
---

# CI/CD YAML syntax reference

- Tier: Free, Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

This document lists the configuration options for the GitLab `.gitlab-ci.yml` file. This file is where you define the CI/CD jobs that make up your pipeline.

- If you are already familiar with basic CI/CD concepts, try creating your own `.gitlab-ci.yml` file by following a tutorial that demonstrates a simple or complex pipeline.
- For a collection of examples, see GitLab CI/CD examples.
- To view a large `.gitlab-ci.yml` file used in an enterprise, see the `.gitlab-ci.yml` file for `gitlab`.

When you are editing your `.gitlab-ci.yml` file, you can validate it with the CI Lint tool.

GitLab CI/CD configuration uses YAML formatting, so the order of keywords is not important unless otherwise specified.

Use CI/CD expressions for more dynamic pipeline configuration options.


## Keywords

A GitLab CI/CD pipeline configuration includes:

- Global keywords that configure pipeline behavior:KeywordDescription`default`Custom default values for job keywords.`include`Import configuration from other YAML files.`stages`The names and order of the pipeline stages.`variables`Define default CI/CD variables for all jobs in the pipeline.`workflow`Control what types of pipeline run.
- Header keywordsKeywordDescription`spec`Define specifications for external configuration files.
- Jobs configured with job keywords:KeywordDescription`after_script`Override a set of commands that are executed after job.`allow_failure`Allow job to fail. A failed job does not cause the pipeline to fail.`artifacts`List of files and directories to attach to a job on success.`before_script`Override a set of commands that are executed before job.`cache`List of files that should be cached between subsequent runs.`coverage`Code coverage settings for a given job.`dast_configuration`Use configuration from DAST profiles on a job level.`dependencies`Restrict which artifacts are passed to a specific job by providing a list of jobs to fetch artifacts from.`environment`Name of an environment to which the job deploys.`extends`Configuration entries that this job inherits from.`identity`Authenticate with third party services using identity federation.`image`Use Docker images.`inherit`Select which global defaults all jobs inherit.`interruptible`Defines if a job can be canceled when made redundant by a newer run.`manual_confirmation`Define a custom confirmation message for a manual job.`needs`Execute jobs earlier than the stage ordering.`pages`Upload the result of a job to use with GitLab Pages.`parallel`How many instances of a job should be run in parallel.`release`Instructs the runner to generate a release object.`resource_group`Limit job concurrency.`retry`When and how many times a job can be auto-retried in case of a failure.`rules`List of conditions to evaluate and determine selected attributes of a job, and whether or not it’s created.`script`Shell script that is executed by a runner.`run`Run configuration that is executed by a runner.`secrets`The CI/CD secrets the job needs.`services`Use Docker services images.`stage`Defines a job stage.`start_in`Delay job execution for a specified duration. Requires `when: delayed`.`tags`List of tags that are used to select a runner.`timeout`Define a custom job-level timeout that takes precedence over the project-wide setting.`trigger`Defines a downstream pipeline trigger.`variables`Define CI/CD variables for individual jobs.`when`When to run job.
- Deprecated keywords that are no longer recommended for use.


## Global keywords

Some keywords are not defined in a job. These keywords control pipeline behavior or import additional pipeline configuration.

### `default`

You can set global defaults for some keywords. Each default keyword is copied to every job that doesn’t already have it defined.

Default configuration does not merge with job configuration. If the job already has a keyword defined, the job keyword takes precedence and the default configuration for that keyword is not used.

**Keyword type**: Global keyword.

**Supported values**: These keywords can have custom defaults:

- `after_script`
- `artifacts`
- `before_script`
- `cache`
- `hooks`
- `id_tokens`
- `image`
- `interruptible`
- `retry`
- `services`
- `tags`

**Example of `default`**:

```yaml
default:
  image: ruby:3.0
  retry: 2

rspec:
  script: bundle exec rspec

rspec 2.7:
  image: ruby:2.7
  script: bundle exec rspec
```

In this example:

- `image: ruby:3.0` and `retry: 2` are the default keywords for all jobs in the pipeline.
- The `rspec` job does not have `image` or `retry` defined, so it uses the defaults of `image: ruby:3.0` and `retry: 2`.
- The `rspec 2.7` job does not have `retry` defined, but it does have `image` explicitly defined. It uses the default `retry: 2`, but ignores the default `image` and uses the `image: ruby:2.7` defined in the job.

**Additional details**:

- Control inheritance of default keywords in jobs with `inherit:default`.
- Global defaults are not passed to downstream pipelines, which run independently of the upstream pipeline that triggered the downstream pipeline.

### `include`

Use `include` to include external YAML files in your CI/CD configuration. You can split one long `.gitlab-ci.yml` file into multiple files to increase readability, or reduce duplication of the same configuration in multiple places.

You can also store template files in a central repository and include them in projects.

The `include` files are:

- Merged with those in the `.gitlab-ci.yml` file.
- Always evaluated first and then merged with the content of the `.gitlab-ci.yml` file, regardless of the position of the `include` keyword.

The time limit to resolve all files is 30 seconds.

**Keyword type**: Global keyword.

**Supported values**: The `include` subkeys:

- `include:component`
- `include:local`
- `include:project`
- `include:remote`
- `include:template`

And optionally:

- `include:inputs`
- `include:rules`
- `include:integrity`
- `include:cache`

**Additional details**:

- Only certain CI/CD variables can be used with `include` keywords.
- Use merging to customize and override included CI/CD configurations with local
- You can override included configuration by having the same job name or global keyword in the `.gitlab-ci.yml` file. The two configurations are merged together, and the configuration in the `.gitlab-ci.yml` file takes precedence over the included configuration.
- If you rerun a:
  - Job, the `include` files are not fetched again. All jobs in a pipeline use the configuration fetched when the pipeline was created. Any changes to the source `include` files do not affect job reruns.
  - Pipeline, the `include` files are fetched again. If they changed after the last pipeline run, the new pipeline uses the changed configuration.
- You can have up to 150 includes per pipeline by default, including nested. Additionally:
  - Users on GitLab Self-Managed can change the maximum includes value.
  - In nested includes, the same file can be included multiple times, but duplicated includes count towards the limit.

#### `include:component`

Use `include:component` to add a CI/CD component to the pipeline configuration.

**Keyword type**: Global keyword.

**Supported values**: The full address of the CI/CD component, formatted as `<fully-qualified-domain-name>/<project-path>/<component-name>@<specific-version>`.

**Example of `include:component`**:

```yaml
include:
  - component: $CI_SERVER_FQDN/my-org/security-components/secret-detection@1.0
```

**Additional details**:

- If the component’s source project is private, the user running the pipeline must have at least the Reporter role For internal projects, any authenticated non-external user can access the component. For public projects, no membership is required.

**Related topics**:

- Use a CI/CD component.

#### `include:local`

Use `include:local` to include a file that is in the same repository and branch as the configuration file containing the `include` keyword. Use `include:local` instead of symbolic links.

**Keyword type**: Global keyword.

**Supported values**:

A full path relative to the root directory (`/`):

- The YAML file must have the extension `.yml` or `.yaml`.
- You can use `*` and `**` wildcards in the file path.
- You can use certain CI/CD variables.

**Example of `include:local`**:

```yaml
include:
  - local: '/templates/.gitlab-ci-template.yml'
```

You can also use shorter syntax to define the path:

```yaml
include: '.gitlab-ci-production.yml'
```

**Additional details**:

- The `.gitlab-ci.yml` file and the local file must be on the same branch.
- You can’t include local files through Git submodules paths.
- `include` configuration is always evaluated based on the location of the file containing the `include` keyword, not the project running the pipeline. If a nested `include` is in a configuration file in a different project, `include: local` checks that other project for the file.

#### `include:project`

To include files from another private project on the same GitLab instance, use `include:project` and `include:file`.

**Keyword type**: Global keyword.

**Supported values**:

- `include:project`: The full GitLab project path.
- `include:file` A full file path, or array of file paths, relative to the root directory (`/`). The YAML files must have the `.yml` or `.yaml` extension.
- `include:ref`: Optional. The ref to retrieve the file from. Defaults to the `HEAD` of the project when not specified.
- You can use certain CI/CD variables.

**Example of `include:project`**:

```yaml
include:
  - project: 'my-group/my-project'
    file: '/templates/.gitlab-ci-template.yml'
  - project: 'my-group/my-subgroup/my-project-2'
    file:
      - '/templates/.builds.yml'
      - '/templates/.tests.yml'
```

You can also specify a `ref`:

```yaml
include:
  - project: 'my-group/my-project'
    ref: main                                      # Git branch
    file: '/templates/.gitlab-ci-template.yml'
  - project: 'my-group/my-project'
    ref: v1.0.0                                    # Git Tag
    file: '/templates/.gitlab-ci-template.yml'
  - project: 'my-group/my-project'
    ref: 787123b47f14b552955ca2786bc9542ae66fee5b  # Git SHA
    file: '/templates/.gitlab-ci-template.yml'
```

**Additional details**:

- `include` configuration is always evaluated based on the location of the file containing the `include` keyword, not the project running the pipeline. If a nested `include` is in a configuration file in a different project, `include: local` checks that other project for the file.
- When the pipeline starts, the `.gitlab-ci.yml` file configuration included by all methods is evaluated. The configuration is a snapshot in time and persists in the database. GitLab does not reflect any changes to the referenced `.gitlab-ci.yml` file configuration until the next pipeline starts.
- For any private project in `include:project`, the user running the pipeline must have at least the Reporter role. For internal projects, any authenticated non-external user can access the included files. For public projects, no membership is required. A `not found or access denied` error is displayed if the user does not have sufficient permissions on the included project.
- Be careful when including another project’s CI/CD configuration file. No pipelines or notifications trigger when CI/CD configuration files change. From a security perspective, this is similar to pulling a third-party dependency. For the `ref`, consider:
  - Using a specific SHA hash, which should be the most stable option. Use the full 40-character SHA hash to ensure the desired commit is referenced, because using a short SHA hash for the `ref` might be ambiguous.
  - Applying both protected branch and protected tag rules to the `ref` in the other project. Protected tags and branches are more likely to pass through change management before changing.

#### `include:remote`

Use `include:remote` with a full URL to include a file from a different location.

**Keyword type**: Global keyword.

**Supported values**:

A public URL accessible by an HTTP/HTTPS `GET` request:

- Authentication with the remote URL is not supported.
- The YAML file must have the extension `.yml` or `.yaml`.
- You can use certain CI/CD variables.

**Example of `include:remote`**:

```yaml
include:
  - remote: 'https://gitlab.com/example-project/-/raw/main/.gitlab-ci.yml'
```

**Additional details**:

- All nested includes are executed without context as a public user, so you can only include public projects or templates. No variables are available in the `include` section of nested includes.
- Be careful when including another project’s CI/CD configuration file. No pipelines or notifications trigger when the other project’s files change. From a security perspective, this is similar to pulling a third-party dependency. To verify the integrity of the included file, consider using the `integrity` keyword. If you link to another GitLab project you own, consider the use of both protected branches and protected tags to enforce change management rules.

#### `include:template`

Use `include:template` to include `.gitlab-ci.yml` templates.

**Keyword type**: Global keyword.

**Supported values**:

- The filename of a CI/CD template, for example `Auto-DevOps.gitlab-ci.yml`.
- You can use certain CI/CD variables.

**Example of `include:template`**:

```yaml
# File sourced from the GitLab template collection
include:
  - template: Auto-DevOps.gitlab-ci.yml
```

Multiple `include:template` files:

```yaml
include:
  - template: Android-Fastlane.gitlab-ci.yml
  - template: Auto-DevOps.gitlab-ci.yml
```

**Additional details**:

- All templates can be viewed in `lib/gitlab/ci/templates`. Not all templates are designed to be used with `include:template`, so check template comments before using one.
- All nested includes are executed without context as a public user, so you can only include public projects or templates. No variables are available in the `include` section of nested includes.

#### `include:inputs`

- Made generally available in GitLab 17.0.

Use `include:inputs` to set the values for input parameters when the included configuration uses `spec:inputs` and is added to the pipeline.

**Keyword type**: Global keyword.

**Supported values**: A string, numeric value, or boolean.

**Example of `include:inputs`**:

```yaml
include:
  - local: 'custom_configuration.yml'
    inputs:
      website: "My website"
```

In this example:

- The configuration contained in `custom_configuration.yml` is added to the pipeline, with a `website` input set to a value of `My website` for the included configuration.

**Additional details**:

- If the included configuration file uses `spec:inputs:type`, the input value must match the defined type.
- If the included configuration file uses `spec:inputs:options`, the input value must match one of the listed options.

**Related topics**:

- Set input values when using `include`.

#### `include:rules`

You can use `rules` with `include` to conditionally include other configuration files.

**Keyword type**: Global keyword.

**Supported values**: These `rules` subkeys:

- `rules:if`.
- `rules:exists`.
- `rules:changes`.

Some CI/CD variables are supported.

**Example of `include:rules`**:

```yaml
include:
  - local: build_jobs.yml
    rules:
      - if: $INCLUDE_BUILDS == "true"

test-job:
  stage: test
  script: echo "This is a test job"
```

In this example, if the `INCLUDE_BUILDS` variable is:

- `true`, the `build_jobs.yml` configuration is included in the pipeline.
- Not `true` or does not exist, the `build_jobs.yml` configuration is not included in the pipeline.

**Related topics**:

- Examples of using `include` with:
  - `rules:if`.
  - `rules:changes`.
  - `rules:exists`.

#### `include:integrity`

- Introduced in GitLab 17.9.

Use `integrity` with `include:remote` to specify a SHA256 hash of the included remote file. If `integrity` does not match the actual content, the remote file is not processed and the pipeline fails.

**Keyword type**: Global keyword.

**Supported values**: Base64-encoded SHA256 hash of the included content.

**Example of `include:integrity`**:

```yaml
include:
  - remote: 'https://gitlab.com/example-project/-/raw/main/.gitlab-ci.yml'
    integrity: 'sha256-L3/GAoKaw0Arw6hDCKeKQlV1QPEgHYxGBHsH4zG1IY8='
```

#### `include:cache`

- Introduced in GitLab 18.9 as an experiment with a feature flag named `ci_cache_remote_includes`. Disabled by default.
- Generally available in GitLab 19.0. Feature flag `ci_cache_remote_includes` removed.

Use `cache` with `include:remote` to cache the fetched remote file content and reduce HTTP requests. When enabled, the remote file is cached for a specified time-to-live (TTL), improving pipeline performance for configurations that use the same remote includes repeatedly.

Consider the trade-off between performance and freshness when setting cache durations. Longer cache durations improve performance but might use stale content if the remote file changes frequently.

When `cache` is not defined, the remote file is fetched every time.

**Keyword type**: Global keyword.

**Supported values**:

- `true`: Enable caching with a default time-to-live (TTL) of 1 hour.
- A duration (string): Valid TTL duration strings use time units like `minutes`, `hours`, or `days` (minimum `1 minute`).

**Example of `include:cache`**:

```yaml
include:
  - remote: 'https://gitlab.com/example-project/-/raw/main/sample1.gitlab-ci.yml'
    cache: true
  - remote: 'https://gitlab.com/example-project/-/raw/main/sample2.gitlab-ci.yml'
    cache: '1 day'
```

**Additional details**:

- Caching is only available for `include:remote`.
- After the remote file is cached, the cached version continues to be used until the TTL expires, even if the remote file content changes.
- If you use `integrity` with `cache`, the integrity check is performed on every pipeline run, even when using cached content.

### `stages`

Use `stages` to define stages that contain groups of jobs. Use `stage` in a job to configure the job to run in a specific stage.

If `stages` is not defined in the `.gitlab-ci.yml` file, the default pipeline stages are:

- `.pre`
- `build`
- `test`
- `deploy`
- `.post`

The order of the items in `stages` defines the execution order for jobs:

- Jobs in the same stage run in parallel.
- Jobs in the next stage run after the jobs from the previous stage complete successfully.

If a pipeline contains only jobs in the `.pre` or `.post` stages, it does not run. There must be at least one other job in a different stage.

**Keyword type**: Global keyword.

**Example of `stages`**:

```yaml
stages:
  - build
  - test
  - deploy
```

In this example:

1. All jobs in `build` execute in parallel.
2. If all jobs in `build` succeed, the `test` jobs execute in parallel.
3. If all jobs in `test` succeed, the `deploy` jobs execute in parallel.
4. If all jobs in `deploy` succeed, the pipeline is marked as `passed`.

If any job fails, the pipeline is marked as `failed` and jobs in later stages do not start. Jobs in the current stage are not stopped and continue to run.

**Additional details**:

- If a job does not specify a `stage`, the job is assigned the `test` stage.
- If a stage is defined but no jobs use it, the stage is not visible in the pipeline, which can help compliance pipeline configurations:
  - Stages can be defined in the compliance configuration but remain hidden if not used.
  - The defined stages become visible when developers use them in job definitions.

**Related topics**:

- To make a job start earlier and ignore the stage order, use the `needs` keyword.

### `workflow`

Use `workflow` to control pipeline behavior.

You can use some predefined CI/CD variables in `workflow` configuration, but not variables that are only defined when jobs start.

**Related topics**:

- `workflow: rules` examples
- Switch between branch pipelines and merge request pipelines

#### `workflow:auto_cancel:on_new_commit`

Use `workflow:auto_cancel:on_new_commit` to configure the behavior of the auto-cancel redundant pipelines feature.

**Supported values**:

- `conservative`: Cancel the pipeline, but only if no jobs with `interruptible: false` have started yet. Default when not defined.
- `interruptible`: Cancel only jobs with `interruptible: true`.
- `none`: Do not auto-cancel any jobs.

**Example of `workflow:auto_cancel:on_new_commit`**:

```yaml
workflow:
  auto_cancel:
    on_new_commit: interruptible

job1:
  interruptible: true
  script: sleep 60

job2:
  interruptible: false  # Default when not defined.
  script: sleep 60
```

In this example:

- When a new commit is pushed to a branch, GitLab creates a new pipeline and `job1` and `job2` start.
- If a new commit is pushed to the branch before the jobs complete, only `job1` is canceled.

#### `workflow:auto_cancel:on_job_failure`

Use `workflow:auto_cancel:on_job_failure` to configure which jobs should be canceled as soon as one job fails.

**Supported values**:

- `all`: Cancel the pipeline and all running jobs as soon as one job fails.
- `none`: Do not auto-cancel any jobs.

**Example of `workflow:auto_cancel:on_job_failure`**:

```yaml
stages: [stage_a, stage_b]

workflow:
  auto_cancel:
    on_job_failure: all

job1:
  stage: stage_a
  script: sleep 60

job2:
  stage: stage_a
  script:
    - sleep 30
    - exit 1

job3:
  stage: stage_b
  script:
    - sleep 30
```

In this example, if `job2` fails, `job1` is canceled if it is still running and `job3` does not start.

**Related topics**:

- Auto-cancel the parent pipeline from a downstream pipeline

#### `workflow:name`

You can use `name` in `workflow:` to define a name for pipelines.

All pipelines are assigned the defined name. Any leading or trailing spaces in the name are removed.

**Supported values**:

- A string.
- CI/CD variables.
- A combination of both.

**Examples of `workflow:name`**:

A simple pipeline name with a predefined variable:

```yaml
workflow:
  name: 'Pipeline for branch: $CI_COMMIT_BRANCH'
```

A configuration with different pipeline names depending on the pipeline conditions:

```yaml
variables:
  PROJECT1_PIPELINE_NAME: 'Default pipeline name'  # A default is not required

workflow:
  name: '$PROJECT1_PIPELINE_NAME'
  rules:
    - if: '$CI_MERGE_REQUEST_LABELS =~ /pipeline:run-in-ruby3/'
      variables:
        PROJECT1_PIPELINE_NAME: 'Ruby 3 pipeline'
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
      variables:
        PROJECT1_PIPELINE_NAME: 'MR pipeline: $CI_MERGE_REQUEST_SOURCE_BRANCH_NAME'
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH  # For default branch pipelines, use the default name
```

**Additional details**:

- If the name is an empty string, the pipeline is not assigned a name. A name consisting of only CI/CD variables could evaluate to an empty string if all the variables are also empty.
- `workflow:rules:variables` become default variables available in all jobs, including `trigger` jobs which forward variables to downstream pipelines by default. If the downstream pipeline uses the same variable, the variable is overwritten by the upstream variable value. Be sure to either:
  - Use a unique variable name in every project’s pipeline configuration, like `PROJECT1_PIPELINE_NAME`.
  - Use `inherit:variables` in the trigger job and list the exact variables you want to forward to the downstream pipeline.

#### `workflow:rules`

The `rules` keyword in `workflow` is similar to `rules` defined in jobs, but controls whether or not a whole pipeline is created.

When no rules evaluate to true, the pipeline does not run.

**Supported values**: You can use some of the same keywords as job-level `rules`:

- `rules: if`.
- `rules: changes`.
- `rules: exists`.
- `when`, can only be `always` or `never` when used with `workflow`.
- `variables`.

**Example of `workflow:rules`**:

```yaml
workflow:
  rules:
    - if: $CI_COMMIT_TITLE =~ /-draft$/
      when: never
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
```

In this example, pipelines run if the commit title (first line of the commit message) does not end with `-draft` and the pipeline is for either:

- A merge request
- The default branch.

**Additional details**:

- If your rules match both branch pipelines (other than the default branch) and merge request pipelines, duplicate pipelines can occur.
- `start_in`, `allow_failure`, and `needs` are not supported in `workflow:rules`, but do not cause a syntax violation. Though they have no effect, do not use them in `workflow:rules` as it could cause syntax failures in the future. See issue 436473 for more details.

**Related topics**:

- Common `if` clauses for `workflow:rules`.
- Use `rules` to run merge request pipelines.

#### `workflow:rules:variables`

You can use `variables` in `workflow:rules` to define variables for specific pipeline conditions.

When the condition matches, the variable is created and can be used by all jobs in the pipeline. If the variable is already defined at the top level as a default variable, the `workflow` variable takes precedence and overrides the default variable.

**Keyword type**: Global keyword.

**Supported values**: Variable name and value pairs:

- The name can use only numbers, letters, and underscores (`_`).
- The value must be a string.

**Example of `workflow:rules:variables`**:

```yaml
variables:
  DEPLOY_VARIABLE: "default-deploy"

workflow:
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
      variables:
        DEPLOY_VARIABLE: "deploy-production"  # Override globally-defined DEPLOY_VARIABLE
    - if: $CI_COMMIT_BRANCH =~ /feature/
      variables:
        IS_A_FEATURE: "true"                  # Define a new variable.
    - if: $CI_COMMIT_BRANCH                   # Run the pipeline in other cases

job1:
  variables:
    DEPLOY_VARIABLE: "job1-default-deploy"
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
      variables:                                   # Override DEPLOY_VARIABLE defined
        DEPLOY_VARIABLE: "job1-deploy-production"  # at the job level.
    - when: on_success                             # Run the job in other cases
  script:
    - echo "Run script with $DEPLOY_VARIABLE as an argument"
    - echo "Run another script if $IS_A_FEATURE exists"

job2:
  script:
    - echo "Run script with $DEPLOY_VARIABLE as an argument"
    - echo "Run another script if $IS_A_FEATURE exists"
```

When the branch is the default branch:

- job1’s `DEPLOY_VARIABLE` is `job1-deploy-production`.
- job2’s `DEPLOY_VARIABLE` is `deploy-production`.

When the branch is `feature`:

- job1’s `DEPLOY_VARIABLE` is `job1-default-deploy`, and `IS_A_FEATURE` is `true`.
- job2’s `DEPLOY_VARIABLE` is `default-deploy`, and `IS_A_FEATURE` is `true`.

When the branch is something else:

- job1’s `DEPLOY_VARIABLE` is `job1-default-deploy`.
- job2’s `DEPLOY_VARIABLE` is `default-deploy`.

**Additional details**:

- `workflow:rules:variables` become default variables available in all jobs, including `trigger` jobs which forward variables to downstream pipelines by default. If the downstream pipeline uses the same variable, the variable is overwritten by the upstream variable value. Be sure to either:
  - Use unique variable names in every project’s pipeline configuration, like `PROJECT1_VARIABLE_NAME`.
  - Use `inherit:variables` in the trigger job and list the exact variables you want to forward to the downstream pipeline.

#### `workflow:rules:auto_cancel`

Use `workflow:rules:auto_cancel` to configure the behavior of the `workflow:auto_cancel:on_new_commit` or the `workflow:auto_cancel:on_job_failure` features.

**Supported values**:

- `on_new_commit`: `workflow:auto_cancel:on_new_commit`
- `on_job_failure`: `workflow:auto_cancel:on_job_failure`

**Example of `workflow:rules:auto_cancel`**:

```yaml
workflow:
  auto_cancel:
    on_new_commit: interruptible
    on_job_failure: all
  rules:
    - if: $CI_COMMIT_REF_PROTECTED == 'true'
      auto_cancel:
        on_new_commit: none
        on_job_failure: none
    - when: always                  # Run the pipeline in other cases

test-job1:
  script: sleep 10
  interruptible: false

test-job2:
  script: sleep 10
  interruptible: true
```

In this example, `workflow:auto_cancel:on_new_commit` is set to `interruptible` and `workflow:auto_cancel:on_job_failure` is set to `all` for all jobs by default. But if a pipeline runs for a protected branch, the rule overrides the default with `on_new_commit: none` and `on_job_failure: none`. For example, if a pipeline is running for:

- A non-protected branch and a new commit is pushed, `test-job1` continues to run and `test-job2` is canceled.
- A protected branch and a new commit is pushed, both `test-job1` and `test-job2` continue to run.


## Header keywords

Some keywords must be defined in a header section of a YAML configuration file. The header must be at the top of the file, separated from the rest of the configuration with `---`.

### `spec`

Add a `spec` section to the header of a YAML file to configure the behavior of a pipeline when a configuration is added to the pipeline with the `include` keyword.

Specs must be declared at the top of a configuration file, in a header section separated from the rest of the configuration with `---`.

#### `spec:inputs`

You can use `spec:inputs` to define inputs for the CI/CD configuration.

Use the interpolation format `$[[ inputs.input-id ]]` to reference the values outside of the header section. Inputs are evaluated and interpolated when the configuration is fetched during pipeline creation. When using `inputs`, interpolation completes before the configuration is merged with the contents of the `.gitlab-ci.yml` file.

**Keyword type**: Header keyword. `spec` must be declared at the top of the configuration file, in a header section.

**Supported values**: A hash of strings representing the expected inputs.

**Example of `spec:inputs`**:

```yaml
spec:
  inputs:
    environment:
    job-stage:
---

scan-website:
  stage: $[[ inputs.job-stage ]]
  script: ./scan-website $[[ inputs.environment ]]
```

**Additional details**:

- Inputs are mandatory unless you use `spec:inputs:default` to set a default value. Avoid mandatory inputs unless you only use inputs with `include:inputs`.
- Inputs expect strings unless you use `spec:inputs:type` to set a different input type.
- A string containing an interpolation block must not exceed 1 MB.
- The string inside an interpolation block must not exceed 1 KB.
- You can define input values when running a new pipeline.

**Related topics**:

- Define input parameters with `spec:inputs`.

##### `spec:inputs:default`

Inputs are mandatory when included, unless you set a default value with `spec:inputs:default`.

Use `default: ''` to have no default value.

**Keyword type**: Header keyword. `spec` must be declared at the top of the configuration file, in a header section.

**Supported values**: A string representing the default value, or `''`.

**Example of `spec:inputs:default`**:

```yaml
spec:
  inputs:
    website:
    user:
      default: 'test-user'
    flags:
      default: ''
---
# The pipeline configuration would follow...
```

In this example:

- `website` is mandatory and must be defined.
- `user` is optional. If not defined, the value is `test-user`.
- `flags` is optional. If not defined, it has no value.

**Additional details**:

- The pipeline fails with a validation error when the input:
  - Uses both `default` and `options`, but the default value is not one of the listed options.
  - Uses both `default` and `regex`, but the default value does not match the regular expression.
  - Value does not match the `type`.

##### `spec:inputs:description`

Use `description` to give a description to a specific input. The description does not affect the behavior of the input and is only used to help users of the file understand the input.

**Keyword type**: Header keyword. `spec` must be declared at the top of the configuration file, in a header section.

**Supported values**: A string representing the description.

**Example of `spec:inputs:description`**:

```yaml
spec:
  inputs:
    flags:
      description: 'Sample description of the `flags` input details.'
---
# The pipeline configuration would follow...
```

##### `spec:inputs:options`

- Support for array type inputs introduced in GitLab 19.0.

Inputs can use `options` to specify a list of allowed values for an input. The limit is 50 options per input.

**Keyword type**: Header keyword. `spec` must be declared at the top of the configuration file, in a header section.

**Supported values**: An array of input options.

**Example of `spec:inputs:options`**:

```yaml
spec:
  inputs:
    environment:
      options:
        - development
        - staging
        - production
---
# The pipeline configuration would follow...
```

In this example:

- `environment` is mandatory and must be defined with one of the values in the list.

**Additional details**:

- The pipeline fails with a validation error when:
  - The input uses both `options` and `default`, but the default value is not one of the listed options.
  - Any of the input options do not match the `type`, which can be either `string` or `number`, but not `boolean` when using `options`.

##### `spec:inputs:regex`

Use `spec:inputs:regex` to specify a regular expression that the input must match.

**Keyword type**: Header keyword. `spec` must be declared at the top of the configuration file, in a header section.

**Supported values**: Must be a regular expression.

**Example of `spec:inputs:regex`**:

```yaml
spec:
  inputs:
    version:
      regex: ^v\d\.\d+(\.\d+)?$
---
# The pipeline configuration would follow...
```

In this example, inputs of `v1.0` or `v1.2.3` match the regular expression and pass validation. An input of `v1.A.B` does not match the regular expression and fails validation.

**Additional details**:

- `inputs:regex` can only be used with a `type` of `string`, not `number` or `boolean`.
- Do not enclose the regular expression with the `/` character. For example, use `regex.*`, not `/regex.*/`.
- `inputs:regex` uses RE2 to parse regular expressions.
- Validation of the input against the regular expression happens before variable expansion. If the input text includes a variable name, the raw value of the input (the variable name) is validated, not the variable value.

##### `spec:inputs:rules`

- Introduced in GitLab 18.7.

Use `spec:inputs:rules` to define conditional `options` and `default` values for an input based on the values of other inputs.

**Keyword type**: Header keyword. `spec` must be declared at the top of the configuration file, in a header section.

**Supported values**: An array of rule objects. Each rule can have:

- `if`: A conditional expression to check input values, using `$[[ inputs.input-id ]]` syntax.
- `options`: An array of allowed values for the input.
- `default`: The default value for the input when this rule matches. Use `default: null` to allow users to enter their own value for the input.

**Example of `spec:inputs:rules`**:

```yaml
spec:
  inputs:
    environment:
      options: ['development', 'production']
      default: 'development'

    instance_type:
      description: 'VM instance size'
      rules:
        - if: $[[ inputs.environment ]] == 'development'
          options: ['small', 'medium']
          default: 'small'
        - if: $[[ inputs.environment ]] == 'production'
          options: ['large', 'xlarge']
          default: 'large'
---

deploy:
  script: echo "Deploying $[[ inputs.instance_type ]] instance"
```

In this example, when `environment` is `development`, users can only select `small` or `medium` instances. When `environment` is `production`, only `large` or `xlarge` instances are available.

**Additional details**:

- Rules are evaluated in order. The first rule with a matching `if` condition is used.
- A rule without an `if` condition acts as a fallback when no other rules match.
- Fallback rules must define `options` with at least one value.
- All rules with `options` must also define a `default` value that exists in the `options` list.
- You cannot use both `rules` and top-level `options` or `default` for the same input.

**Related topics**:

- Define conditional input options with `spec:inputs:rules`.

##### `spec:inputs:type`

By default, inputs expect strings. Use `spec:inputs:type` to set a different required type for inputs.

**Keyword type**: Header keyword. `spec` must be declared at the top of the configuration file, in a header section.

**Supported values**: Can be one of:

- `array`, to accept an array of inputs.
- `string`, to accept string inputs (default when not defined).
- `number`, to only accept numeric inputs.
- `boolean`, to only accept `true` or `false` inputs.

**Example of `spec:inputs:type`**:

```yaml
spec:
  inputs:
    job_name:
    website:
      type: string
    port:
      type: number
    available:
      type: boolean
    array_input:
      type: array
---
# The pipeline configuration would follow...
```

#### `spec:include`

- Introduced in GitLab 18.6 with a flag named `ci_file_inputs`. Disabled by default.
- Generally available in GitLab 18.9. Feature flag `ci_file_inputs` removed.

Use `spec:include` to include external input definitions from other files. You can share and reuse input definitions across multiple pipeline configurations.

**Keyword type**: Header keyword. `spec` must be declared at the top of the configuration file, in a header section.

**Supported values**: An array of include locations. Supports `local`, `remote`, and `project` includes only.

**Example of `spec:include`**:

```yaml
spec:
  include:
    - local: /shared-inputs.yml
  inputs:
    environment:
      default: production
---

deploy:
  script: echo "Deploying to $[[ inputs.environment ]]"
```

With multiple includes from different sources:

```yaml
spec:
  include:
    - local: /base-inputs.yml
    - remote: 'https://example.com/ci/common-inputs.yml'
    - project: 'my-group/shared-configs'
      ref: main
      file: '/ci/team-inputs.yml'
  inputs:
    environment:
      default: production
---

deploy:
  script: echo "Deploying to $[[ inputs.environment ]]"
```

**Additional details**:

- You cannot use `spec:include` in CI/CD components.
- External input files must contain only the `inputs` key. Other keys cause validation errors.
- External inputs are merged first, then inline inputs are applied.
- Inline inputs cannot have the same name as included inputs.
- When you include multiple input files, they are merged in the order specified.
- Supports `local`, `remote`, and `project` include types. Does not support `template`, `component`, or `artifact` includes.

**Related topics**:

- Use inputs from external files.

#### `spec:component`

- Introduced in GitLab 18.6 as a beta with a flag named `ci_component_context_interpolation`. Enabled by default.
- Generally available in GitLab 18.7. Feature flag `ci_component_context_interpolation` removed.

Use `spec:component` to define which component context data is available for interpolation in a CI/CD component.

Component context provides metadata about the component itself, such as its name, version, and the commit SHA. This allows component templates to reference their own metadata dynamically.

Use the interpolation format `$[[ component.field-name ]]` to reference component context values in the component template.

**Keyword type**: Header keyword. `spec` must be declared at the top of the configuration file, in a header section.

**Supported values**: An array of strings. Each string must be one of:

- `name`: The component name as specified in the component path.
- `sha`: The commit SHA of the component.
- `version`: The resolved semantic version from the catalog resource. Returns `null` if:
  - The component is not a catalog resource.
  - The reference is a branch name or commit SHA (not a released version).
- `reference`: The original reference specified after `@` in the component path. For example, `1.0`, `~latest`, a branch name, or a commit SHA.

**Example of `spec:component`**:

```yaml
spec:
  component: [name, version, reference]
  inputs:
    stage:
      default: build
---

build-image:
  stage: $[[ inputs.stage ]]
  image: registry.example.com/$[[ component.name ]]:$[[ component.version ]]
  script:
    - echo "Building with component version $[[ component.version ]]"
    - echo "Component reference: $[[ component.reference ]]"
```

**Additional details**:

- The `version` field resolves to the actual semantic version when using:
  - A full version like `@1.0.0` (returns `1.0.0`)
  - A partial version like `@1.0` (returns the latest matching version, for example `1.0.2`)
  - `@~latest` (returns the latest version)
- The `reference` field always returns the exact value specified after `@`:
  - `@1.0` returns `1.0` (while `version` might return `1.0.2`)
  - `@~latest` returns `~latest` (while `version` returns the actual version number)
  - `@abc123` returns `abc123` (while `version` returns `null`)

**Related topics**:

- Use component context in components.

#### `spec:description`

- Introduced in GitLab 18.10.

Use `spec:description` to provide a short description of the component. The description is displayed in the CI/CD Catalog on the component details page, above the inputs table.

**Keyword type**: Header keyword. `spec` must be declared at the top of the configuration file, in a header section.

**Supported values**: A string describing the component.

**Example of `spec:description`**:

```yaml
spec:
  description: "A description of the component visible to users in the CI/CD Catalog."
  inputs:
    stage:
      default: test
---
scan-job:
  stage: $[[ inputs.stage ]]
  script: ./run-scan.sh
```
