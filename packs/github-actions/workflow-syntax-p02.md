---
title: "Workflow syntax for GitHub Actions (part 2/4)"
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
domain: github-actions
license: CC-BY-4.0 (GitHub docs)
tags: github actions, github workflow, actions runner
fetched: 2026-07-02
part: 2/4
---

## `concurrency`

Use `concurrency` to ensure that only a single job or workflow using the same concurrency group will run at a time. A concurrency group can be any string or expression. The expression can only use `github`, `inputs` and `vars` contexts. For more information about expressions, see Evaluate expressions in workflows and actions.

You can also specify `concurrency` at the job level. For more information, see `jobs.<job_id>.concurrency`.

This means that there can be at most one running job or workflow in a concurrency group at any time. When a concurrent job or workflow is queued, if another job or workflow using the same concurrency group in the repository is in progress, the queued job or workflow will be `pending`. By default, any existing `pending` job or workflow in the same concurrency group will be canceled and the new queued job or workflow will take its place.

To also cancel any currently running job or workflow in the same concurrency group, specify `cancel-in-progress: true`. To conditionally cancel currently running jobs or workflows in the same concurrency group, you can specify `cancel-in-progress` as an expression with any of the allowed expression contexts.

To allow more than one `pending` job or workflow run to wait in the same concurrency group, use the optional `queue` property. The `queue` property accepts the following values:

- `single` (default): At most one job or workflow run can be `pending` in the concurrency group. When a new job or workflow run is queued, any existing `pending` job or workflow run in the same group is canceled and replaced.
- `max`: Up to 100 jobs or workflow runs can be `pending` in the concurrency group. When the queue is full, any additional jobs or workflow runs are canceled.

The combination of `queue: max` and `cancel-in-progress: true` is not allowed and will result in a workflow validation error.

Note

- The concurrency group name is case insensitive. For example, `prod` and `Prod` will be treated as the same concurrency group.
- Jobs or workflow runs in the same concurrency group are processed in first-in-first-out (FIFO) order according to the time each one started waiting on the concurrency group, not the time each workflow was dispatched. Since the actual start time of a job or run may vary, ordering is not guaranteed.

### Example: Using concurrency and the default behavior

The default behavior of GitHub Actions is to allow multiple jobs or workflow runs to run concurrently. The `concurrency` keyword allows you to control the concurrency of workflow runs.

For example, you can use the `concurrency` keyword immediately after where trigger conditions are defined to limit the concurrency of entire workflow runs for a specific branch:

```yaml
on:
  push:
    branches:
      - main

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

You can also limit the concurrency of jobs within a workflow by using the `concurrency` keyword at the job level:

```yaml
on:
  push:
    branches:
      - main

jobs:
  job-1:
    runs-on: ubuntu-latest
    concurrency:
      group: example-group
      cancel-in-progress: true
```

### Example: Concurrency groups

Concurrency groups provide a way to manage and limit the execution of workflow runs or jobs that share the same concurrency key.

The `concurrency` key is used to group workflows or jobs together into a concurrency group. When you define a `concurrency` key, GitHub Actions ensures that only one workflow or job with that key runs at any given time. If a new workflow run or job starts with the same `concurrency` key, GitHub Actions will cancel any workflow or job already running with that key. The `concurrency` key can be a hard-coded string, or it can be a dynamic expression that includes context variables.

It is possible to define concurrency conditions in your workflow so that the workflow or job is part of a concurrency group.

This means that when a workflow run or job starts, GitHub will cancel any workflow runs or jobs that are already in progress in the same concurrency group. This is useful in scenarios where you want to prevent parallel runs for a certain set of a workflows or jobs, such as the ones used for deployments to a staging environment, in order to prevent actions that could cause conflicts or consume more resources than necessary.

In this example, `job-1` is part of a concurrency group named `staging_environment`. This means that if a new run of `job-1` is triggered, any runs of the same job in the `staging_environment` concurrency group that are already in progress will be cancelled.

```yaml
jobs:
  job-1:
    runs-on: ubuntu-latest
    concurrency:
      group: staging_environment
      cancel-in-progress: true
```

Alternatively, using a dynamic expression such as `concurrency: ci-${{ github.ref }}` in your workflow means that the workflow or job would be part of a concurrency group named `ci-` followed by the reference of the branch or tag that triggered the workflow. In this example, if a new commit is pushed to the main branch while a previous run is still in progress, the previous run will be cancelled and the new one will start:

```yaml
on:
  push:
    branches:
      - main

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true
```

### Example: Queueing multiple pending runs

By default, only one job or workflow run can be `pending` in a concurrency group at a time. To allow multiple runs to queue instead of being canceled, set `queue: max`. With `queue: max`, up to 100 jobs or workflow runs can wait in the concurrency group; once the queue is full, any additional runs are canceled.

For example, the following workflow queues deployments to the `production` environment, processing them one at a time in order based on when each run started waiting on the concurrency group:

```yaml
on:
  push:
    branches:
      - main

concurrency:
  group: production-deploy
  queue: max
```

Note that `queue: max` cannot be combined with `cancel-in-progress: true`, because the two options describe conflicting behaviors for handling in-progress runs.

### Example: Using concurrency to cancel any in-progress job or run

To use concurrency to cancel any in-progress job or run in GitHub Actions, you can use the `concurrency` key with the `cancel-in-progress` option set to `true`:

```yaml
concurrency:
  group: ${{ github.ref }}
  cancel-in-progress: true
```

Note that in this example, without defining a particular concurrency group, GitHub Actions will cancel *any* in-progress run of the job or workflow.

### Example: Using a fallback value

If you build the group name with a property that is only defined for specific events, you can use a fallback value. For example, `github.head_ref` is only defined on `pull_request` events. If your workflow responds to other events in addition to `pull_request` events, you will need to provide a fallback to avoid a syntax error. The following concurrency group cancels in-progress jobs or runs on `pull_request` events only; if `github.head_ref` is undefined, the concurrency group will fallback to the run ID, which is guaranteed to be both unique and defined for the run.

```yaml
concurrency:
  group: ${{ github.head_ref || github.run_id }}
  cancel-in-progress: true
```

### Example: Only cancel in-progress jobs or runs for the current workflow

If you have multiple workflows in the same repository, concurrency group names must be unique across workflows to avoid canceling in-progress jobs or runs from other workflows. Otherwise, any previously in-progress or pending job will be canceled, regardless of the workflow.

To only cancel in-progress runs of the same workflow, you can use the `github.workflow` property to build the concurrency group:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

### Example: Only cancel in-progress jobs on specific branches

If you would like to cancel in-progress jobs on certain branches but not on others, you can use conditional expressions with `cancel-in-progress`. For example, you can do this if you would like to cancel in-progress jobs on development branches but not on release branches.

To only cancel in-progress runs of the same workflow when not running on a release branch, you can set `cancel-in-progress` to an expression similar to the following:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: ${{ !contains(github.ref, 'release/')}}
```

In this example, multiple pushes to a `release/1.2.3` branch would not cancel in-progress runs. Pushes to another branch, such as `main`, would cancel in-progress runs.


## `jobs`

A workflow run is made up of one or more `jobs`, which run in parallel by default. To run jobs sequentially, you can define dependencies on other jobs using the `jobs.<job_id>.needs` keyword.

Each job runs in a runner environment specified by `runs-on`.

You can run an unlimited number of jobs as long as you are within the workflow usage limits. For more information, see Billing and usage for GitHub-hosted runners and Actions limits for self-hosted runner usage limits.

If you need to find the unique identifier of a job running in a workflow run, you can use the GitHub API. For more information, see REST API endpoints for GitHub Actions.


## `jobs.<job_id>`

Use `jobs.<job_id>` to give your job a unique identifier. The key `job_id` is a string and its value is a map of the job's configuration data. You must replace `<job_id>` with a string that is unique to the `jobs` object. The `<job_id>` must start with a letter or `_` and contain only alphanumeric characters, `-`, or `_`.

### Example: Creating jobs

In this example, two jobs have been created, and their `job_id` values are `my_first_job` and `my_second_job`.

```yaml
jobs:
  my_first_job:
    name: My first job
  my_second_job:
    name: My second job
```


## `jobs.<job_id>.name`

Use `jobs.<job_id>.name` to set a name for the job, which is displayed in the GitHub UI.


## `jobs.<job_id>.permissions`

For a specific job, you can use `jobs.<job_id>.permissions` to modify the default permissions granted to the `GITHUB_TOKEN`, adding or removing access as required, so that you only allow the minimum required access. For more information, see Use GITHUB_TOKEN for authentication in workflows.

By specifying the permission within a job definition, you can configure a different set of permissions for the `GITHUB_TOKEN` for each job, if required. Alternatively, you can specify the permissions for all jobs in the workflow. For information on defining permissions at the workflow level, see `permissions`.

For each of the available permissions, shown in the table below, you can assign one of the access levels: `read` (if applicable), `write`, or `none`. `write` includes `read`. If you specify the access for any of these permissions, all of those that are not specified are set to `none`.

Available permissions and details of what each allows an action to do:

| Permission | Allows an action using `GITHUB_TOKEN` to |
|---|---|
| `actions` | Work with GitHub Actions. For example, `actions: write` permits an action to cancel a workflow run. For more information, see Permissions required for GitHub Apps. |
| `artifact-metadata` | Work with artifact metadata. For example, `artifact-metadata: write` permits an action to create storage records on behalf of a build artifact. For more information, see REST API endpoints for artifact metadata. |
| `attestations` | Work with artifact attestations. For example, `attestations: write` permits an action to generate an artifact attestation for a build. For more information, see Using artifact attestations to establish provenance for builds |
| `checks` | Work with check runs and check suites. For example, `checks: write` permits an action to create a check run. For more information, see Permissions required for GitHub Apps. |
| `code-quality` | Work with code quality. For example, `code-quality: write` permits an action to upload code coverage reports. For more information, see About GitHub Code Quality. |
| `contents` | Work with the contents of the repository. For example, `contents: read` permits an action to list the commits, and `contents: write` allows the action to create a release. For more information, see Permissions required for GitHub Apps. |
| `deployments` | Work with deployments. For example, `deployments: write` permits an action to create a new deployment. For more information, see Permissions required for GitHub Apps. |
| `discussions` | Work with GitHub Discussions. For example, `discussions: write` permits an action to close or delete a discussion. For more information, see Using the GraphQL API for Discussions. |
| `id-token` | Fetch an OpenID Connect (OIDC) token. This requires `id-token: write`. For more information, see OpenID Connect |
| `issues` | Work with issues. For example, `issues: write` permits an action to add a comment to an issue. For more information, see Permissions required for GitHub Apps. |
| `models` | Generate AI inference responses with GitHub Models. For example, `models: read` permits an action to use the GitHub Models inference API. See Prototyping with AI models. |
| `packages` | Work with GitHub Packages. For example, `packages: write` permits an action to upload and publish packages on GitHub Packages. For more information, see About permissions for GitHub Packages. |
| `pages` | Work with GitHub Pages. For example, `pages: write` permits an action to request a GitHub Pages build. For more information, see Permissions required for GitHub Apps. |
| `pull-requests` | Work with pull requests. For example, `pull-requests: write` permits an action to add a label to a pull request. For more information, see Permissions required for GitHub Apps. |
| `security-events` | Work with GitHub code scanning alerts. For example, `security-events: read` permits an action to list the code scanning alerts for the repository, and `security-events: write` allows an action to update the status of a code scanning alert. For more information, see Repository permissions for "Code scanning alerts". For Dependabot alerts, use the `vulnerability-alerts` permission. Secret scanning alerts cannot be read with this permission and require a GitHub App or a personal access token. For more information, see Repository permissions for "Secret scanning alerts" in "Permissions required for GitHub Apps." |
| `statuses` | Work with commit statuses. For example, `statuses:read` permits an action to list the commit statuses for a given reference. For more information, see Permissions required for GitHub Apps. |
| `vulnerability-alerts` | Read Dependabot alerts. For example, `vulnerability-alerts: read` permits an action to list Dependabot alerts for the repository. Only `read` and `none` are supported; `write` is not valid. When `write-all` or `read-all` is used, `vulnerability-alerts` is automatically included as `read`. For more information, see Repository permissions for "Dependabot alerts". |

### Defining access for the `GITHUB_TOKEN` scopes

You can define the access that the `GITHUB_TOKEN` will permit by specifying `read`, `write`, or `none` as the value of the available permissions within the `permissions` key.

```yaml
permissions:
  actions: read|write|none
  artifact-metadata: read|write|none
  attestations: read|write|none
  checks: read|write|none
  code-quality: read|write|none
  contents: read|write|none
  deployments: read|write|none
  id-token: write|none
  issues: read|write|none
  models: read|none
  discussions: read|write|none
  packages: read|write|none
  pages: read|write|none
  pull-requests: read|write|none

  security-events: read|write|none
  statuses: read|write|none
  vulnerability-alerts: read|none
```

If you specify the access for any of these permissions, all of those that are not specified are set to `none`.

You can use the following syntax to define one of `read-all` or `write-all` access for all of the available permissions:

```yaml
permissions: read-all
```

```yaml
permissions: write-all
```

You can use the following syntax to disable permissions for all of the available permissions:

```yaml
permissions: {}
```

#### Changing the permissions in a forked repository

You can use the `permissions` key to add and remove read permissions for forked repositories, but typically you can't grant write access. The exception to this behavior is where an admin user has selected the **Send write tokens to workflows from pull requests** option in the GitHub Actions settings. For more information, see Managing GitHub Actions settings for a repository.

#### Example: Setting the `GITHUB_TOKEN` permissions for one job in a workflow

This example shows permissions being set for the `GITHUB_TOKEN` that will only apply to the job named `stale`. Write access is granted for the `issues` and `pull-requests` permissions. All other permissions will have no access.

```yaml
jobs:
  stale:
    runs-on: ubuntu-latest

    permissions:
      issues: write
      pull-requests: write

    steps:
      - uses: actions/stale@v10
```


## `jobs.<job_id>.needs`

Use `jobs.<job_id>.needs` to identify any jobs that must complete successfully before this job will run. It can be a string or array of strings. If a job fails or is skipped, all jobs that need it are skipped unless the jobs use a conditional expression that causes the job to continue. If a run contains a series of jobs that need each other, a failure or skip applies to all jobs in the dependency chain from the point of failure or skip onwards. If you would like a job to run even if a job it is dependent on did not succeed, use the `always()` conditional expression in `jobs.<job_id>.if`.

### Example: Requiring successful dependent jobs

```yaml
jobs:
  job1:
  job2:
    needs: job1
  job3:
    needs: [job1, job2]
```

In this example, `job1` must complete successfully before `job2` begins, and `job3` waits for both `job1` and `job2` to complete.

The jobs in this example run sequentially:

1. `job1`
2. `job2`
3. `job3`

### Example: Not requiring successful dependent jobs

```yaml
jobs:
  job1:
  job2:
    needs: job1
  job3:
    if: ${{ always() }}
    needs: [job1, job2]
```

In this example, `job3` uses the `always()` conditional expression so that it always runs after `job1` and `job2` have completed, regardless of whether they were successful. For more information, see Evaluate expressions in workflows and actions.


## `jobs.<job_id>.if`

You can use the `jobs.<job_id>.if` conditional to prevent a job from running unless a condition is met. You can use any supported context and expression to create a conditional. For more information on which contexts are supported in this key, see Contexts reference.

Note

The `jobs.<job_id>.if` condition is evaluated before `jobs.<job_id>.strategy.matrix` is applied.

When you use expressions in an `if` conditional, you can, optionally, omit the `${{ }}` expression syntax because GitHub Actions automatically evaluates the `if` conditional as an expression. However, this exception does not apply everywhere.

You must always use the `${{ }}` expression syntax or escape with `''`, `""`, or `()` when the expression starts with `!`, since `!` is reserved notation in YAML format. For example:

```yaml
if: ${{ ! startsWith(github.ref, 'refs/tags/') }}
```

For more information, see Evaluate expressions in workflows and actions.

### Example: Only run job for specific repository

This example uses `if` to control when the `production-deploy` job can run. It will only run if the repository is named `octo-repo-prod` and is within the `octo-org` organization. Otherwise, the job will be marked as *skipped*.

YAML

```
name: example-workflow
on: [push]
jobs:
  production-deploy:
    if: github.repository == 'octo-org/octo-repo-prod'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v4
        with:
          node-version: '14'
      - run: npm install -g bats
```

```yaml
name: example-workflow
on: [push]
jobs:
  production-deploy:
    if: github.repository == 'octo-org/octo-repo-prod'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v4
        with:
          node-version: '14'
      - run: npm install -g bats
```


## `jobs.<job_id>.runs-on`

Use `jobs.<job_id>.runs-on` to define the type of machine to run the job on.

- The destination machine can be either a GitHub-hosted runner, larger runner, or a self-hosted runner.
- You can target runners based on the labels assigned to them, or their group membership, or a combination of these.
- You can provide `runs-on` as:
  - A single string
  - A single variable containing a string
  - An array of strings, variables containing strings, or a combination of both
  - A `key: value` pair using the `group` or `labels` keys
- If you specify an array of strings or variables, your workflow will execute on any runner that matches all of the specified `runs-on` values. For example, here the job will only run on a self-hosted runner that has the labels `linux`, `x64`, and `gpu`: For more information, see Choosing self-hosted runners.
  ```
runs-on: [self-hosted, linux, x64, gpu]
  ```
- You can mix strings and variables in an array. For example:
  ```
on:
  workflow_dispatch:
    inputs:
      chosen-os:
        required: true
        type: choice
        options:
        - Ubuntu
        - macOS

jobs:
  test:
    runs-on: [self-hosted, "${{ inputs.chosen-os }}"]
    steps:
    - run: echo Hello world!
  ```
- If you would like to run your workflow on multiple machines, use `jobs.<job_id>.strategy`.

Note

Quotation marks are not required around simple strings like `self-hosted`, but they are required for expressions like `"${{ inputs.chosen-os }}"`.

### Choosing GitHub-hosted runners

If you use a GitHub-hosted runner, each job runs in a fresh instance of a runner image specified by `runs-on`.

The value for runs-on, when you are using a GitHub-hosted runner, is a workflow label or the name of a runner group. The labels for the standard GitHub-hosted runners are shown in the following tables.

For more information, see GitHub-hosted runners.

### Standard GitHub-hosted runners for public repositories

For public repositories, jobs using the workflow labels shown in the table below will run with the associated specifications. With the exception of single-CPU runners, each GitHub-hosted runner is a new virtual machine (VM) hosted by GitHub. Single-CPU runners are hosted in a container on a shared VM—see GitHub-hosted runners reference. Use of the standard GitHub-hosted runners is free and unlimited on public repositories.

| **Virtual machine / container** | **Processor (CPU)** | **Memory (RAM)** | **Storage (SSD)** | **Architecture** | **Workflow label** |
|---|---|---|---|---|---|
| Linux | 1 | 5 GB | 14 GB | x64 | `ubuntu-slim` |
| Linux | 4 | 16 GB | 14 GB | x64 | `ubuntu-latest`, `ubuntu-24.04`, `ubuntu-22.04`, `ubuntu-26.04` (Public preview) |
| Windows | 4 | 16 GB | 14 GB | x64 | `windows-latest`, `windows-2025`, `windows-2025-vs2026`, `windows-2022` |
| Linux | 4 | 16 GB | 14 GB | arm64 | `ubuntu-24.04-arm`, `ubuntu-22.04-arm`, `ubuntu-26.04-arm` (Public preview) |
| Windows | 4 | 16 GB | 14 GB | arm64 | `windows-11-arm`, `windows-11-vs2026-arm` (Public preview) |
| macOS | 4 | 14 GB | 14 GB | Intel | `macos-15-intel`, `macos-26-intel` |
| macOS | 3 (M1) | 7 GB | 14 GB | arm64 | `macos-latest`, `macos-14`, `macos-15`, `macos-26` |

### Standard GitHub-hosted runners for private repositories

For private repositories, jobs using the workflow labels shown in the table below will run on virtual machines with the associated specifications. These runners use your GitHub account's allotment of free minutes, and are then charged at the per minute rates. See Actions runner pricing.

| **Virtual Machine** | **Processor (CPU)** | **Memory (RAM)** | **Storage (SSD)** | **Architecture** | **Workflow label** |
|---|---|---|---|---|---|
| Linux | 1 | 5 GB | 14 GB | x64 | `ubuntu-slim` |
| Linux | 2 | 8 GB | 14 GB | x64 | `ubuntu-latest`, `ubuntu-24.04`, `ubuntu-22.04`, `ubuntu-26.04` (Public preview) |
| Windows | 2 | 8 GB | 14 GB | x64 | `windows-latest`, `windows-2025`, `windows-2022` |
| Linux | 2 | 8 GB | 14 GB | arm64 | `ubuntu-24.04-arm`, `ubuntu-22.04-arm`, `ubuntu-26.04-arm` (Public preview) |
| Windows | 2 | 8 GB | 14 GB | arm64 | `windows-11-arm`, `windows-11-vs2026-arm` (Public preview) |
| macOS | 4 | 14 GB | 14 GB | Intel | `macos-15-intel`, `macos-26-intel` |
| macOS | 3 (M1) | 7 GB | 14 GB | arm64 | `macos-latest`, `macos-14`, `macos-15`, `macos-26` |

In addition to the standard GitHub-hosted runners, GitHub offers customers on GitHub Team and GitHub Enterprise Cloud plans a range of managed virtual machines with advanced features - for example, more cores and disk space, GPU-powered machines, and ARM-powered machines. For more information, see Larger runners.

Note

The `-latest` runner images are the latest stable images that GitHub provides, and might not be the most recent version of the operating system available from the operating system vendor.

Warning

Beta and Deprecated Images are provided "as-is", "with all faults" and "as available" and are excluded from the service level agreement and warranty. Beta Images may not be covered by customer support.

#### Example: Specifying an operating system

```yaml
runs-on: ubuntu-latest
```

For more information, see GitHub-hosted runners.

### Choosing self-hosted runners

To specify a self-hosted runner for your job, configure `runs-on` in your workflow file with self-hosted runner labels.

Self-hosted runners may have the `self-hosted` label. When setting up a self-hosted runner, by default we will include the label `self-hosted`. You may pass in the `--no-default-labels` flag to prevent the self-hosted label from being applied. Labels can be used to create targeting options for runners, such as operating system or architecture, we recommend providing an array of labels that begins with `self-hosted` (this must be listed first) and then includes additional labels as needed. When you specify an array of labels, jobs will be queued on runners that have all the labels that you specify.

Note

Actions Runner Controller does not support the `self-hosted` label.

#### Example: Using labels for runner selection

```yaml
runs-on: [self-hosted, linux]
```

For more information, see Self-hosted runners and Using self-hosted runners in a workflow.

### Choosing runners in a group

You can use `runs-on` to target runner groups, so that the job will execute on any runner that is a member of that group. For more granular control, you can also combine runner groups with labels.

Runner groups can only have larger runners or self-hosted runners as members.

#### Example: Using groups to control where jobs are run

In this example, runners have been added to a group called `build-runners`. The `runs-on` key sends the job to any available runner in the `build-runners` group:

```yaml
name: learn-github-actions
on: [push]
jobs:
  check-bats-version:
    runs-on: 
      group: build-runners
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v4
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v
```

#### Example: Combining groups and labels

When you combine groups and labels, the runner must meet both requirements to be eligible to run the job.

In this example, the `runs-on` key combines `group` and `labels` so that the job is routed to any available runner within the group that also has a matching label:

```yaml
name: learn-github-actions
on: [push]
jobs:
  check-bats-version:
    runs-on:
      group: ubuntu-runners
      labels: ubuntu-24.04-16core
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v4
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v
```


## `jobs.<job_id>.snapshot`

You can use `jobs.<job_id>.snapshot` to generate a custom image.

Add the snapshot keyword to the job, using either the string syntax or mapping syntax as shown in Generating a custom image.

Each job that includes the snapshot keyword creates a separate image. To generate only one image or image version, include all workflow steps in a single job. Each successful run of a job that includes the snapshot keyword creates a new version of that image.

For more information, see Using custom images.


## `jobs.<job_id>.environment`

Use `jobs.<job_id>.environment` to define the environment that the job references.

You can provide the environment as only the environment `name`, or as an environment object with the `name` and `url`. The URL maps to `environment_url` in the deployments API. For more information about the deployments API, see REST API endpoints for repositories.

Note

All deployment protection rules must pass before a job referencing the environment is sent to a runner. For more information, see Managing environments for deployment.

### Example: Using a single environment name

```yaml
environment: staging_environment
```

### Example: Using environment name and URL

```yaml
environment:
  name: production_environment
  url: https://github.com
```

The value of `url` can be an expression. Allowed expression contexts: `github`, `inputs`, `vars`, `needs`, `strategy`, `matrix`, `job`, `runner`, `env`, and `steps`. For more information about expressions, see Evaluate expressions in workflows and actions.

### Example: Using output as URL

```yaml
environment:
  name: production_environment
  url: ${{ steps.step_id.outputs.url_output }}
```

The value of `name` can be an expression. Allowed expression contexts: `github`, `inputs`, `vars`, `needs`, `strategy`, and `matrix`. For more information about expressions, see Evaluate expressions in workflows and actions.

### Example: Using an expression as environment name

```yaml
environment:
  name: ${{ github.ref_name }}
```

### Example: Using an environment without creating a deployment

Set `deployment` to `false` to use an environment's secrets and variables without creating a deployment object.

```yaml
environment:
  name: testing
  deployment: false
```

Setting `deployment: false` is not compatible with custom deployment protection rules. For more information, see Deploying with GitHub Actions.


## `jobs.<job_id>.concurrency`

You can use `jobs.<job_id>.concurrency` to ensure that only a single job or workflow using the same concurrency group will run at a time. A concurrency group can be any string or expression. Allowed expression contexts: `github`, `inputs`, `vars`, `needs`, `strategy`, and `matrix`. For more information about expressions, see Evaluate expressions in workflows and actions.

You can also specify `concurrency` at the workflow level. For more information, see `concurrency`.

This means that there can be at most one running job or workflow in a concurrency group at any time. When a concurrent job or workflow is queued, if another job or workflow using the same concurrency group in the repository is in progress, the queued job or workflow will be `pending`. By default, any existing `pending` job or workflow in the same concurrency group will be canceled and the new queued job or workflow will take its place.

To also cancel any currently running job or workflow in the same concurrency group, specify `cancel-in-progress: true`. To conditionally cancel currently running jobs or workflows in the same concurrency group, you can specify `cancel-in-progress` as an expression with any of the allowed expression contexts.

To allow more than one `pending` job or workflow run to wait in the same concurrency group, use the optional `queue` property. The `queue` property accepts the following values:

- `single` (default): At most one job or workflow run can be `pending` in the concurrency group. When a new job or workflow run is queued, any existing `pending` job or workflow run in the same group is canceled and replaced.
- `max`: Up to 100 jobs or workflow runs can be `pending` in the concurrency group. When the queue is full, any additional jobs or workflow runs are canceled.

The combination of `queue: max` and `cancel-in-progress: true` is not allowed and will result in a workflow validation error.

Note

- The concurrency group name is case insensitive. For example, `prod` and `Prod` will be treated as the same concurrency group.
- Jobs or workflow runs in the same concurrency group are processed in first-in-first-out (FIFO) order according to the time each one started waiting on the concurrency group, not the time each workflow was dispatched. Since the actual start time of a job or run may vary, ordering is not guaranteed.

### Example: Using concurrency and the default behavior

The default behavior of GitHub Actions is to allow multiple jobs or workflow runs to run concurrently. The `concurrency` keyword allows you to control the concurrency of workflow runs.

For example, you can use the `concurrency` keyword immediately after where trigger conditions are defined to limit the concurrency of entire workflow runs for a specific branch:

```yaml
on:
  push:
    branches:
      - main

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

You can also limit the concurrency of jobs within a workflow by using the `concurrency` keyword at the job level:

```yaml
on:
  push:
    branches:
      - main

jobs:
  job-1:
    runs-on: ubuntu-latest
    concurrency:
      group: example-group
      cancel-in-progress: true
```

### Example: Concurrency groups

Concurrency groups provide a way to manage and limit the execution of workflow runs or jobs that share the same concurrency key.

The `concurrency` key is used to group workflows or jobs together into a concurrency group. When you define a `concurrency` key, GitHub Actions ensures that only one workflow or job with that key runs at any given time. If a new workflow run or job starts with the same `concurrency` key, GitHub Actions will cancel any workflow or job already running with that key. The `concurrency` key can be a hard-coded string, or it can be a dynamic expression that includes context variables.

It is possible to define concurrency conditions in your workflow so that the workflow or job is part of a concurrency group.

This means that when a workflow run or job starts, GitHub will cancel any workflow runs or jobs that are already in progress in the same concurrency group. This is useful in scenarios where you want to prevent parallel runs for a certain set of a workflows or jobs, such as the ones used for deployments to a staging environment, in order to prevent actions that could cause conflicts or consume more resources than necessary.

In this example, `job-1` is part of a concurrency group named `staging_environment`. This means that if a new run of `job-1` is triggered, any runs of the same job in the `staging_environment` concurrency group that are already in progress will be cancelled.

```yaml
jobs:
  job-1:
    runs-on: ubuntu-latest
    concurrency:
      group: staging_environment
      cancel-in-progress: true
```

Alternatively, using a dynamic expression such as `concurrency: ci-${{ github.ref }}` in your workflow means that the workflow or job would be part of a concurrency group named `ci-` followed by the reference of the branch or tag that triggered the workflow. In this example, if a new commit is pushed to the main branch while a previous run is still in progress, the previous run will be cancelled and the new one will start:

```yaml
on:
  push:
    branches:
      - main

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true
```

### Example: Queueing multiple pending runs

By default, only one job or workflow run can be `pending` in a concurrency group at a time. To allow multiple runs to queue instead of being canceled, set `queue: max`. With `queue: max`, up to 100 jobs or workflow runs can wait in the concurrency group; once the queue is full, any additional runs are canceled.

For example, the following workflow queues deployments to the `production` environment, processing them one at a time in order based on when each run started waiting on the concurrency group:

```yaml
on:
  push:
    branches:
      - main

concurrency:
  group: production-deploy
  queue: max
```

Note that `queue: max` cannot be combined with `cancel-in-progress: true`, because the two options describe conflicting behaviors for handling in-progress runs.

### Example: Using concurrency to cancel any in-progress job or run

To use concurrency to cancel any in-progress job or run in GitHub Actions, you can use the `concurrency` key with the `cancel-in-progress` option set to `true`:

```yaml
concurrency:
  group: ${{ github.ref }}
  cancel-in-progress: true
```

Note that in this example, without defining a particular concurrency group, GitHub Actions will cancel *any* in-progress run of the job or workflow.

### Example: Using a fallback value

If you build the group name with a property that is only defined for specific events, you can use a fallback value. For example, `github.head_ref` is only defined on `pull_request` events. If your workflow responds to other events in addition to `pull_request` events, you will need to provide a fallback to avoid a syntax error. The following concurrency group cancels in-progress jobs or runs on `pull_request` events only; if `github.head_ref` is undefined, the concurrency group will fallback to the run ID, which is guaranteed to be both unique and defined for the run.

```yaml
concurrency:
  group: ${{ github.head_ref || github.run_id }}
  cancel-in-progress: true
```

### Example: Only cancel in-progress jobs or runs for the current workflow

If you have multiple workflows in the same repository, concurrency group names must be unique across workflows to avoid canceling in-progress jobs or runs from other workflows. Otherwise, any previously in-progress or pending job will be canceled, regardless of the workflow.

To only cancel in-progress runs of the same workflow, you can use the `github.workflow` property to build the concurrency group:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

### Example: Only cancel in-progress jobs on specific branches

If you would like to cancel in-progress jobs on certain branches but not on others, you can use conditional expressions with `cancel-in-progress`. For example, you can do this if you would like to cancel in-progress jobs on development branches but not on release branches.

To only cancel in-progress runs of the same workflow when not running on a release branch, you can set `cancel-in-progress` to an expression similar to the following:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: ${{ !contains(github.ref, 'release/')}}
```

In this example, multiple pushes to a `release/1.2.3` branch would not cancel in-progress runs. Pushes to another branch, such as `main`, would cancel in-progress runs.


## `jobs.<job_id>.outputs`

You can use `jobs.<job_id>.outputs` to create a `map` of outputs for a job. Job outputs are available to all downstream jobs that depend on this job. For more information on defining job dependencies, see `jobs.<job_id>.needs`.

Outputs can be a maximum of 1 MB per job. The total of all outputs in a workflow run can be a maximum of 50 MB. Size is approximated based on UTF-16 encoding.

Job outputs containing expressions are evaluated on the runner at the end of each job. Outputs containing secrets are redacted on the runner and not sent to GitHub Actions.

If an output is skipped because it may contain a secret, you will see the following warning message: "Skip output `{output.Key}` since it may contain secret." For more information on how to handle secrets, please refer to the Example: Masking and passing a secret between jobs or workflows.

To use job outputs in a dependent job, you can use the `needs` context. For more information, see Contexts reference.

### Example: Defining outputs for a job

```yaml
jobs:
  job1:
    runs-on: ubuntu-latest
    
    outputs:
      output1: ${{ steps.step1.outputs.test }}
      output2: ${{ steps.step2.outputs.test }}
    steps:
      - id: step1
        run: echo "test=hello" >> "$GITHUB_OUTPUT"
      - id: step2
        run: echo "test=world" >> "$GITHUB_OUTPUT"
  job2:
    runs-on: ubuntu-latest
    needs: job1
    steps:
      - env:
          OUTPUT1: ${{needs.job1.outputs.output1}}
          OUTPUT2: ${{needs.job1.outputs.output2}}
        run: echo "$OUTPUT1 $OUTPUT2"
```

### Using Job Outputs in a Matrix Job

Matrices can be used to generate multiple outputs of different names. When using a matrix, job outputs will be combined from all jobs inside the matrix.

```yaml
jobs:
  job1:
    runs-on: ubuntu-latest
    outputs:
      output_1: ${{ steps.gen_output.outputs.output_1 }}
      output_2: ${{ steps.gen_output.outputs.output_2 }}
      output_3: ${{ steps.gen_output.outputs.output_3 }}
    strategy:
      matrix:
        version: [1, 2, 3]
    steps:
      - name: Generate output
        id: gen_output
        run: |
          version="${{ matrix.version }}"
          echo "output_${version}=${version}" >> "$GITHUB_OUTPUT"
  job2:
    runs-on: ubuntu-latest
    needs: [job1]
    steps:
      
      
      
      
      
      
      - run: echo '${{ toJSON(needs.job1.outputs) }}'
```

Warning

Actions does not guarantee the order that matrix jobs will run in. Ensure that the output name is unique, otherwise the last matrix job that runs will override the output value.


## `jobs.<job_id>.env`

A `map` of variables that are available to all steps in the job. You can set variables for the entire workflow or an individual step. For more information, see `env` and `jobs.<job_id>.steps[*].env`.

When more than one environment variable is defined with the same name, GitHub uses the most specific variable. For example, an environment variable defined in a step will override job and workflow environment variables with the same name, while the step executes. An environment variable defined for a job will override a workflow variable with the same name, while the job executes.

### Example of `jobs.<job_id>.env`

```yaml
jobs:
  job1:
    env:
      FIRST_NAME: Mona
```


## `jobs.<job_id>.defaults`

Use `jobs.<job_id>.defaults` to create a `map` of default settings that will apply to all steps in the job. You can also set default settings for the entire workflow. For more information, see `defaults`.

When more than one default setting is defined with the same name, GitHub uses the most specific default setting. For example, a default setting defined in a job will override a default setting that has the same name defined in a workflow.


## `jobs.<job_id>.defaults.run`

Use `jobs.<job_id>.defaults.run` to provide default `shell` and `working-directory` to all `run` steps in the job.

You can provide default `shell` and `working-directory` options for all `run` steps in a job. You can also set default settings for `run` for the entire workflow. For more information, see `defaults.run`.

These can be overridden at the `jobs.<job_id>.defaults.run` and `jobs.<job_id>.steps[*].run` levels.

When more than one default setting is defined with the same name, GitHub uses the most specific default setting. For example, a default setting defined in a job will override a default setting that has the same name defined in a workflow.


## `jobs.<job_id>.defaults.run.shell`

Use `shell` to define the `shell` for a step. This keyword can reference several contexts. For more information, see Contexts.

| Supported platform | `shell` parameter | Description | Command run internally |
|---|---|---|---|
| Linux / macOS | unspecified | The default shell on non-Windows platforms. Note that this runs a different command to when `bash` is specified explicitly. If `bash` is not found in the path, this is treated as `sh`. | `bash -e {0}` |
| All | `bash` | The default shell on non-Windows platforms with a fallback to `sh`. When specifying a bash shell on Windows, the bash shell included with Git for Windows is used. | `bash --noprofile --norc -eo pipefail {0}` |
| All | `pwsh` | The PowerShell Core. GitHub appends the extension `.ps1` to your script name. | `pwsh -command ". '{0}'"` |
| All | `python` | Executes the python command. | `python {0}` |
| Linux / macOS | `sh` | The fallback behavior for non-Windows platforms if no shell is provided and `bash` is not found in the path. | `sh -e {0}` |
| Windows | `cmd` | GitHub appends the extension `.cmd` to your script name and substitutes for `{0}`. | `%ComSpec% /D /E:ON /V:OFF /S /C "CALL "{0}""`. |
| Windows | `pwsh` | This is the default shell used on Windows. The PowerShell Core. GitHub appends the extension `.ps1` to your script name. If your self-hosted Windows runner does not have *PowerShell Core* installed, then *PowerShell Desktop* is used instead. | `pwsh -command ". '{0}'"`. |
| Windows | `powershell` | The PowerShell Desktop. GitHub appends the extension `.ps1` to your script name. | `powershell -command ". '{0}'"`. |

When more than one default setting is defined with the same name, GitHub uses the most specific default setting. For example, a default setting defined in a job will override a default setting that has the same name defined in a workflow.


## `jobs.<job_id>.defaults.run.working-directory`

Use `working-directory` to define the working directory for the `shell` for a step. This keyword can reference several contexts. For more information, see Contexts.

Tip

Ensure the `working-directory` you assign exists on the runner before you run your shell in it. When more than one default setting is defined with the same name, GitHub uses the most specific default setting. For example, a default setting defined in a job will override a default setting that has the same name defined in a workflow.

### Example: Setting default `run` step options for a job

```yaml
jobs:
  job1:
    runs-on: ubuntu-latest
    defaults:
      run:
        shell: bash
        working-directory: ./scripts
```


## `jobs.<job_id>.steps`

A job contains a sequence of tasks called `steps`. Steps can run commands, run setup tasks, or run an action in your repository, a public repository, or an action published in a Docker registry. Not all steps run actions, but all actions run as a step. Each step runs in its own process in the runner environment and has access to the workspace and filesystem. Because steps run in their own process, changes to environment variables are not preserved between steps. GitHub provides built-in steps to set up and complete a job.

GitHub only displays the first 1,000 checks, however, you can run an unlimited number of steps as long as you are within the workflow usage limits. For more information, see Billing and usage for GitHub-hosted runners and Actions limits for self-hosted runner usage limits.

### Example of `jobs.<job_id>.steps`

```yaml
name: Greeting from Mona

on: push

jobs:
  my-job:
    name: My Job
    runs-on: ubuntu-latest
    steps:
      - name: Print a greeting
        env:
          MY_VAR: Hi there! My name is
          FIRST_NAME: Mona
          MIDDLE_NAME: The
          LAST_NAME: Octocat
        run: |
          echo $MY_VAR $FIRST_NAME $MIDDLE_NAME $LAST_NAME.
```


## `jobs.<job_id>.steps[*].id`

A unique identifier for the step. You can use the `id` to reference the step in contexts. For more information, see Contexts reference.
