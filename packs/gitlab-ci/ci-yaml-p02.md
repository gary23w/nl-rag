---
title: "CI/CD YAML syntax reference (part 2/4)"
source: https://docs.gitlab.com/ee/ci/yaml/
domain: gitlab-ci
license: CC-BY-SA-4.0
tags: gitlab ci, gitlab pipeline, ci cd pipeline, continuous integration
fetched: 2026-07-02
part: 2/4
---

## Job keywords

The following topics explain how to use keywords to configure CI/CD pipelines.

### `after_script`

- Running `after_script` commands for canceled jobs introduced in GitLab 17.0.

Use `after_script` to define an array of commands to run last, after a job’s `before_script` and `script` sections complete. `after_script` commands also run when:

- The job is canceled while the `before_script` or `script` sections are still running.
- The job fails with failure type of `script_failure`, but not other failure types.

Job configuration and default configuration does not merge together. If the pipeline has `default:after_script` defined, and the job also has `after_script`, the job configuration takes precedence and the default configuration is not used.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**: An array including:

- Single line commands.
- Long commands split over multiple lines.
- YAML anchors.

CI/CD variables are supported.

**Example of `after_script`**:

```yaml
job:
  script:
    - echo "An example script section."
  after_script:
    - echo "Execute this command after the `script` section completes."
```

**Additional details**:

Scripts you specify in `after_script` execute in a new shell, separate from any `before_script` or `script` commands. As a result, they:

- Have the current working directory set back to the default (according to the variables which define how the runner processes Git requests).
- Don’t have access to changes done by commands defined in the `before_script` or `script`, including:
  - Command aliases and variables exported in `script` scripts.
  - Changes outside of the working tree (depending on the runner executor), like software installed by a `before_script` or `script` script.
- Have a separate timeout. For GitLab Runner 16.4 and later, this defaults to 5 minutes, and can be configured with the `RUNNER_AFTER_SCRIPT_TIMEOUT` variable. In GitLab 16.3 and earlier, the timeout is hard-coded to 5 minutes.
- Don’t affect the job’s exit code. If the `script` section succeeds and the `after_script` times out or fails, the job exits with code `0` (`Job Succeeded`).
- For jobs that time out:
  - `after_script` commands do not execute by default.
  - You can configure timeout values to ensure `after_script` runs by setting appropriate `RUNNER_SCRIPT_TIMEOUT` and `RUNNER_AFTER_SCRIPT_TIMEOUT` values that don’t exceed the job’s timeout.
- Using `after_script` at the top level, but not in the `default` section, is deprecated.

**Execution timing and file inclusion**:

`after_script` commands execute before cache and artifact upload operations.

- If you configured artifact collection:
  - Files created or modified in `after_script` are included in artifacts.
  - Changes made in `after_script` are included in cache uploads.
- Any files that `after_script` creates or modifies in the specified cache or artifact paths are captured and uploaded. You can use this timing for scenarios like:
  - Generating test reports or coverage data after the main script.
  - Creating summary files or logs.
  - Post-processing build outputs.

In the following example, the only files that are not included are those created or modified after the artifact or cache upload stages:

```yaml
job:
  script:
    - echo "main" > output.txt
    - build_something

  after_script:
    - echo "modified in after_script" >> output.txt  # This WILL be in the artifact
    - generate_test_report > report.html            # This WILL be in the artifact

  artifacts:
    paths:
      - output.txt
      - report.html

  cache:
    paths:
      - output.txt  # Will include the "modified in after_script" line
```

For more information, see job execution flow.

**Related topics**:

- Use `after_script` with `default` to define a default array of commands that should run after all jobs.
- You can configure a job to skip `after_script` commands if the job is canceled.
- You can ignore non-zero exit codes.
- Use color codes with `after_script` to make job logs easier to review.
- Create custom collapsible sections to simplify job log output.
- You can ignore errors in `after_script`.

### `allow_failure`

Use `allow_failure` to determine whether a pipeline should continue running when a job fails.

- To let the pipeline continue running subsequent jobs, use `allow_failure: true`.
- To stop the pipeline from running subsequent jobs, use `allow_failure: false`.

When jobs are allowed to fail (`allow_failure: true`) an orange warning ( ) indicates that a job failed. However, the pipeline is successful and the associated commit is marked as passed with no warnings.

This same warning is displayed when:

- All other jobs in the stage are successful.
- All other jobs in the pipeline are successful.

The default value for `allow_failure` is:

- `true` for manual jobs.
- `false` for jobs that use `when: manual` inside `rules`.
- `false` in all other cases.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- `true` or `false`.

**Example of `allow_failure`**:

```yaml
job1:
  stage: test
  script:
    - execute_script_1

job2:
  stage: test
  script:
    - execute_script_2
  allow_failure: true

job3:
  stage: deploy
  script:
    - deploy_to_staging
  environment: staging
```

In this example, `job1` and `job2` run in parallel:

- If `job1` fails, jobs in the `deploy` stage do not start.
- If `job2` fails, jobs in the `deploy` stage can still start.

**Additional details**:

- You can use `allow_failure` as a subkey of `rules`.
- If `allow_failure: true` is set, the job is always considered successful, and later jobs with `when: on_failure` don’t start if this job fails.
- You can use `allow_failure: false` with a manual job to create a blocking manual job. A blocked pipeline does not run any jobs in later stages until the manual job is started and completes successfully.

#### `allow_failure:exit_codes`

Use `allow_failure:exit_codes` to control when a job should be allowed to fail. The job is `allow_failure: true` for any of the listed exit codes, and `allow_failure` false for any other exit code.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- A single exit code.
- An array of exit codes.

**Example of `allow_failure`**:

```yaml
test_job_1:
  script:
    - echo "Run a script that results in exit code 1. This job fails."
    - exit 1
  allow_failure:
    exit_codes: 137

test_job_2:
  script:
    - echo "Run a script that results in exit code 137. This job is allowed to fail."
    - exit 137
  allow_failure:
    exit_codes:
      - 137
      - 255
```

### `artifacts`

- Updated in GitLab Runner 18.1. During the caching process, `symlinks` are no longer followed, which happened in some edge cases with previous GitLab Runner versions.

Use `artifacts` to specify which files to save as job artifacts. Job artifacts are a list of files and directories that are attached to the job when it succeeds, fails, or always.

The artifacts are sent to GitLab after the job finishes. They are available for download in the GitLab UI if the size is smaller than the maximum artifact size.

By default, jobs in later stages automatically download all the artifacts created by jobs in earlier stages. You can control artifact download behavior in jobs with `dependencies`.

When using the `needs` keyword, jobs can only download artifacts from the jobs defined in the `needs` configuration.

Job artifacts are only collected for successful jobs by default, and artifacts are restored after caches.

Job configuration and default configuration does not merge together. If the pipeline has `default:artifacts` defined, and the job also has `artifacts`, the job configuration takes precedence and the default configuration is not used.

Read more about artifacts.

#### `artifacts:paths`

Paths are relative to the project directory (`$CI_PROJECT_DIR`) and can’t directly link outside it.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- An array of file paths, relative to the project directory.
- You can use Wildcards that use glob patterns and `doublestar.Glob` patterns.
- For GitLab Pages job:
  - In GitLab 17.10 and later, the `pages.publish` path is automatically appended to `artifacts:paths`, so you don’t need to specify it again.
  - In GitLab 17.10 and later, when the `pages.publish` path is not specified, the `public` directory is automatically appended to `artifacts:paths`.

CI/CD variables are supported.

**Example of `artifacts:paths`**:

```yaml
job:
  artifacts:
    paths:
      - binaries/
      - .config
```

This example creates an artifact with `.config` and all the files in the `binaries` directory.

**Additional details**:

- If not used with `artifacts:name`, the artifacts file is named `artifacts`, which becomes `artifacts.zip` when downloaded.

**Related topics**:

- To restrict which jobs a specific job fetches artifacts from, see `dependencies`.
- Create job artifacts.

#### `artifacts:exclude`

Use `artifacts:exclude` to prevent files from being added to an artifacts archive.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- An array of file paths, relative to the project directory.
- You can use Wildcards that use glob or `doublestar.PathMatch` patterns.

**Example of `artifacts:exclude`**:

```yaml
artifacts:
  paths:
    - binaries/
  exclude:
    - binaries/**/*.o
```

This example stores all files in `binaries/`, but not `*.o` files located in subdirectories of `binaries/`.

**Additional details**:

- `artifacts:exclude` paths are not searched recursively.
- Files matched by `artifacts:untracked` can be excluded using `artifacts:exclude` too.

**Related topics**:

- Exclude files from job artifacts.

#### `artifacts:expire_in`

Use `expire_in` to specify how long job artifacts are stored before they expire and are deleted. The `expire_in` setting does not affect:

- Artifacts from the latest job, unless keeping the latest job artifacts is disabled at the project level or instance-wide.

After their expiry, artifacts are deleted hourly by default (using a cron job), and are not accessible anymore.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**: The expiry time. If no unit is provided, the time is in seconds. Valid values include:

- `'42'`
- `42 seconds`
- `3 mins 4 sec`
- `2 hrs 20 min`
- `2h20min`
- `6 mos 1 day`
- `47 yrs 6 mos and 4d`
- `3 weeks and 2 days`
- `never`

**Example of `artifacts:expire_in`**:

```yaml
job:
  artifacts:
    expire_in: 1 week
```

**Additional details**:

- The expiration time period begins when the artifact is uploaded and stored on GitLab. If the expiry time is not defined, it defaults to the instance wide setting.
- To override the expiration date and protect artifacts from being automatically deleted:
  - Select **Keep** on the job page.
  - Set the value of `expire_in` to `never`.
- If the expiry time is too short, jobs in later stages of a long pipeline might try to fetch expired artifacts from earlier jobs. If the artifacts are expired, jobs that try to fetch them fail with a `could not retrieve the needed artifacts` error. Set the expiry time to be longer, or use `dependencies` in later jobs to ensure they don’t try to fetch expired artifacts.
- `artifacts:expire_in` doesn’t affect GitLab Pages deployments. To configure Pages deployments’ expiry, use `pages.expire_in`.

#### `artifacts:expose_as`

Use the `artifacts:expose_as` keyword to expose artifacts in the merge request UI.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- The name to display in the merge request UI for the artifacts download link. Must be combined with `artifacts:paths`.

**Example of `artifacts:expose_as`**:

```yaml
test:
  script: ["echo 'test' > file.txt"]
  artifacts:
    expose_as: 'artifact 1'
    paths: ['file.txt']
```

**Additional details**:

- You can use `expose_as` only once per job, with a maximum of 10 jobs per merge request.
- Glob patterns are not supported.
- Artifacts are always sent to GitLab. They are displayed in the UI unless `artifacts:paths` values:
  - Use CI/CD variables.
  - Define a directory, but do not end with `/`. For example, `directory/` works with `artifacts:expose_as`, but `directory` does not.
- If `artifacts:paths` only includes a single file, the link opens the file directly. In all other cases, the link opens the artifacts browser.
- Linked files are downloaded by default. If GitLab Pages is enabled, you can preview some artifacts file extensions directly in your browser. See Browse the contents of the artifacts archive for details.

**Related topics**:

- Expose job artifacts in the merge request UI.

#### `artifacts:name`

Use the `artifacts:name` keyword to define the name of the created artifacts archive. You can specify a unique name for every archive.

If not defined, the default name is `artifacts`, which becomes `artifacts.zip` when downloaded.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- The name of the artifacts archive. CI/CD variables are supported. Must be combined with `artifacts:paths`.

**Example of `artifacts:name`**:

To create an archive with a name of the current job:

```yaml
job:
  artifacts:
    name: "job1-artifacts-file"
    paths:
      - binaries/
```

**Related topics**:

- Use CI/CD variables to define the artifacts configuration

#### `artifacts:public`

`artifacts:public` is now superseded by `artifacts:access` which has more options.

Use `artifacts:public` to control whether job artifacts in public pipelines are available for download with the GitLab UI and API by anonymous users, or Guest and Reporter roles.

This option only affects GitLab UI and API access. CI/CD jobs using job tokens could still access artifacts with the runner API, regardless of this setting. To restrict job token access, configure your project’s CI/CD visibility settings to **Only project members**.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- `true` (default): Artifacts in a job in public pipelines are available for download by anyone, including anonymous users, or Guest and Reporter roles.
- `false`: Artifacts in the job are only available for download by users with the Developer, Maintainer, or Owner role.

**Example of `artifacts:public`**:

```yaml
job:
  artifacts:
    public: false
```

#### `artifacts:access`

- `maintainer` option introduced in GitLab 18.4.

Use `artifacts:access` to determine who can access the job artifacts from the GitLab UI or API. This option does not prevent you from forwarding artifacts to downstream pipelines.

You cannot use `artifacts:public` and `artifacts:access` in the same job.

This option only affects GitLab UI and API access. CI/CD jobs using job tokens could still access artifacts with the runner API, regardless of this setting. To restrict job token access, configure your project’s CI/CD visibility settings to **Only project members**.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- `all` (default): Artifacts in a job in public pipelines are available for download by anyone, including anonymous, guest, and reporter users.
- `developer`: Artifacts in the job are only available for download by users with the Developer, Maintainer, or Owner role.
- `maintainer`: Artifacts in the job are only available for download by users with the Maintainer or Owner role.
- `none`: Artifacts in the job are not available for download by anyone.

**Example of `artifacts:access`**:

```yaml
job:
  artifacts:
    access: 'developer'
```

**Additional details**:

- `artifacts:access` affects all `artifacts:reports` too, so you can also restrict access to artifacts for reports.

#### `artifacts:reports`

Use `artifacts:reports` to collect artifacts generated by included templates in jobs.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- See list of available artifacts reports types.

**Example of `artifacts:reports`**:

```yaml
rspec:
  stage: test
  script:
    - bundle install
    - rspec --format RspecJunitFormatter --out rspec.xml
  artifacts:
    reports:
      junit: rspec.xml
```

**Additional details**:

- Combining reports in parent pipelines using artifacts from child pipelines is not supported. For more information, see epic 8205.
- To be able to browse and download the report output files, include the `artifacts:paths` keyword. This uploads and stores the artifact twice.
- Artifacts created for `artifacts: reports` are always uploaded, regardless of the job results (success or failure). You can use `artifacts:expire_in` to set an expiration date for the artifacts.

#### `artifacts:untracked`

Use `artifacts:untracked` to add all Git untracked files as artifacts (along with the paths defined in `artifacts:paths`). `artifacts:untracked` ignores configuration in the repository’s `.gitignore`, so matching artifacts in `.gitignore` are included.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- `true` or `false` (default if not defined).

**Example of `artifacts:untracked`**:

Save all Git untracked files:

```yaml
job:
  artifacts:
    untracked: true
```

**Related topics**:

- Add untracked files to artifacts.

#### `artifacts:when`

Use `artifacts:when` to upload artifacts on job failure or despite the failure.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- `on_success` (default): Upload artifacts only when the job succeeds.
- `on_failure`: Upload artifacts only when the job fails.
- `always`: Always upload artifacts (except when jobs time out). For example, when uploading artifacts required to troubleshoot failing tests.

**Example of `artifacts:when`**:

```yaml
job:
  artifacts:
    when: on_failure
```

**Additional details**:

- The artifacts created for `artifacts:reports` are always uploaded, regardless of the job results (success or failure). `artifacts:when` does not change this behavior.

### `before_script`

Use `before_script` to define an array of commands that should run before each job’s `script` commands, but after artifacts are restored.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**: An array including:

- Single line commands.
- Long commands split over multiple lines.
- YAML anchors.

CI/CD variables are supported.

**Example of `before_script`**:

```yaml
job:
  before_script:
    - echo "Execute this command before any 'script:' commands."
  script:
    - echo "This command executes after the job's 'before_script' commands."
```

**Additional details**:

- Scripts you specify in `before_script` are concatenated with any scripts you specify in the main `script`. The combined scripts execute together in a single shell.
- Using `before_script` at the top level, but not in the `default` section, is deprecated.

**Related topics**:

- Use `before_script` with `default` to define a default array of commands that should run before the `script` commands in all jobs.
  - Job configuration and default configuration does not merge together. If the pipeline has `default:before_script` defined, and the job also has `before_script`, the job configuration takes precedence and the default configuration is not used.
- You can ignore non-zero exit codes.
- Use color codes with `before_script` to make job logs easier to review.
- Create custom collapsible sections to simplify job log output.

### `cache`

- Updated in GitLab Runner 18.1. During the caching process, `symlinks` are no longer followed, which happened in some edge cases with previous GitLab Runner versions.

Use `cache` to specify a list of files and directories to cache between jobs. You can only use paths that are in the local working copy.

Caches are:

- Shared between pipelines and jobs.
- By default, not shared between protected and unprotected branches.
- Restored before artifacts.
- Limited to a maximum of four different caches.

You can disable caching for specific jobs, for example to override:

- A default cache defined with `default`.
- The configuration for a job added with `include`.

Job configuration and default configuration does not merge together. If the pipeline has `default:cache` defined, and the job also has `cache`, the job configuration takes precedence and the default configuration is not used.

For more information about caches, see Caching in GitLab CI/CD.

Using `cache` at the top level, but not in the `default` section, is deprecated.

#### `cache:paths`

Use the `cache:paths` keyword to choose which files or directories to cache.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- An array of paths relative to the project directory (`$CI_PROJECT_DIR`). You can use wildcards that use glob and `doublestar.Glob` patterns.

CI/CD variables are supported.

**Example of `cache:paths`**:

Cache all files in `binaries` that end in `.apk` and the `.config` file:

```yaml
rspec:
  script:
    - echo "This job uses a cache."
  cache:
    key: binaries-cache
    paths:
      - binaries/*.apk
      - .config
```

**Additional details**:

- The `cache:paths` keyword includes files even if they are untracked or in your `.gitignore` file.

**Related topics**:

- See the CI/CD caching examples for more `cache:paths` examples.

#### `cache:key`

Use the `cache:key` keyword to give each cache a unique identifying key. All jobs that use the same cache key use the same cache, including in different pipelines.

If not set, the default key is `default`. All jobs with the `cache` keyword but no `cache:key` share the `default` cache.

Must be used with `cache: paths`, or nothing is cached.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- A string.
- A predefined CI/CD variable.
- A combination of both.

**Example of `cache:key`**:

```yaml
cache-job:
  script:
    - echo "This job uses a cache."
  cache:
    key: binaries-cache-$CI_COMMIT_REF_SLUG
    paths:
      - binaries/
```

**Additional details**:

- If you use **Windows Batch** to run your shell scripts you must replace `$` with `%`. For example: `key: %CI_COMMIT_REF_SLUG%`
- The `cache:key` value can’t contain:
  - The `/` character, or the equivalent URI-encoded `%2F`.
  - Only the `.` character (any number), or the equivalent URI-encoded `%2E`.
- The cache is shared between jobs, so if you’re using different paths for different jobs, you should also set a different `cache:key`. Otherwise cache content can be overwritten.

**Related topics**:

- You can specify a fallback cache key to use if the specified `cache:key` is not found.
- You can use multiple cache keys in a single job.
- See the CI/CD caching examples for more `cache:key` examples.

##### `cache:key:files`

Use `cache:key:files` to generate a new cache key when the content of the specified files change. If the content remains unchanged, the cache key remains consistent across branches and pipelines. You can reuse caches and rebuild them less often, which speeds up subsequent pipeline runs.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- An array of up to two file paths or patterns.

CI/CD variables are not supported.

**Example of `cache:key:files`**:

```yaml
cache-job:
  script:
    - echo "This job uses a cache."
  cache:
    key:
      files:
        - Gemfile.lock
        - package.json
    paths:
      - vendor/ruby
      - node_modules
```

This example creates a cache for Ruby and Node.js dependencies. The cache is tied to the current versions of the `Gemfile.lock` and `package.json` files. When one of these files changes, a new cache key is computed and a new cache is created. Any future job runs that use the same `Gemfile.lock` and `package.json` with `cache:key:files` use the new cache, instead of rebuilding the dependencies.

**Additional details**:

- The cache `key` is a SHA computed from the content of the listed files. If a file doesn’t exist, it’s ignored in the key calculation. If none of the specified files exist, the fallback key is `default`.
- Wildcard patterns like `**/package.json` can be used.
- A maximum of two files can be specified. For updates on increasing the number of allowed paths or patterns, see issue 301161.

##### `cache:key:files_commits`

Use `cache:key:files_commits` to generate a new cache key when the latest commit changes for the specified files. `cache:key:files_commits` cache keys change whenever the specified files have a new commit, even if the file content remains identical.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- An array of up to two file paths or patterns.

**Example of `cache:key:files_commits`**:

```yaml
cache-job:
  script:
    - echo "This job uses a commit-based cache."
  cache:
    key:
      files_commits:
        - package.json
        - yarn.lock
    paths:
      - node_modules
```

This example creates a cache based on the commit history of `package.json` and `yarn.lock`. If the commit history changes for these files, a new cache key is computed and a new cache is created.

**Additional details**:

- The cache `key` is a SHA computed from the most recent commit for each specified file.
- If a file doesn’t exist, it’s ignored in the key calculation.
- If none of the specified files exist, the fallback key is `default`.
- Cannot be used together with `cache:key:files` in the same cache configuration.

##### `cache:key:prefix`

Use `cache:key:prefix` to combine a prefix with the SHA computed for `cache:key:files`.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- A string.
- A predefined CI/CD variable.
- A combination of both.

**Example of `cache:key:prefix`**:

```yaml
rspec:
  script:
    - echo "This rspec job uses a cache."
  cache:
    key:
      files:
        - Gemfile.lock
      prefix: $CI_JOB_NAME
    paths:
      - vendor/ruby
```

For example, adding a `prefix` of `$CI_JOB_NAME` causes the key to look like `rspec-feef9576d21ee9b6a32e30c5c79d0a0ceb68d1e5`. If a branch changes `Gemfile.lock`, that branch has a new SHA checksum for `cache:key:files`. A new cache key is generated, and a new cache is created for that key. If `Gemfile.lock` is not found, the prefix is added to `default`, so the key in the example would be `rspec-default`.

**Additional details**:

- If no file in `cache:key:files` is changed in any commits, the prefix is added to the `default` key.

#### `cache:untracked`

Use `untracked: true` to cache all files that are untracked in your Git repository. Untracked files include files that are:

- Ignored due to `.gitignore` configuration.
- Created, but not added to the checkout with `git add`.

Caching untracked files can create unexpectedly large caches if the job downloads:

- Dependencies, like gems or node modules, which are usually untracked.
- Artifacts from a different job. Files extracted from the artifacts are untracked by default.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- `true` or `false` (default).

**Example of `cache:untracked`**:

```yaml
rspec:
  script: test
  cache:
    untracked: true
```

**Additional details**:

- You can combine `cache:untracked` with `cache:paths` to cache all untracked files, as well as files in the configured paths. Use `cache:paths` to cache any specific files, including tracked files, or files that are outside of the working directory, and use `cache: untracked` to also cache all untracked files. For example:`rspec: script: test cache: untracked: true paths: - binaries/`In this example, the job caches all untracked files in the repository, as well as all the files in `binaries/`. If there are untracked files in `binaries/`, they are covered by both keywords.

#### `cache:unprotect`

Use `cache:unprotect` to set a cache to be shared between protected and unprotected branches.

When set to `true`, users without access to protected branches can read and write to cache keys used by protected branches.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- `true` or `false` (default).

**Example of `cache:unprotect`**:

```yaml
rspec:
  script: test
  cache:
    unprotect: true
```

#### `cache:when`

Use `cache:when` to define when to save the cache, based on the status of the job.

Must be used with `cache: paths`, or nothing is cached.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- `on_success` (default): Save the cache only when the job succeeds.
- `on_failure`: Save the cache only when the job fails.
- `always`: Always save the cache.

**Example of `cache:when`**:

```yaml
rspec:
  script: rspec
  cache:
    paths:
      - rspec/
    when: 'always'
```

This example stores the cache whether or not the job fails or succeeds.

#### `cache:policy`

To change the upload and download behavior of a cache, use the `cache:policy` keyword. By default, the job downloads the cache when the job starts, and uploads changes to the cache when the job ends. This caching style is the `pull-push` policy (default).

To set a job to only download the cache when the job starts, but never upload changes when the job finishes, use `cache:policy:pull`.

To set a job to only upload a cache when the job finishes, but never download the cache when the job starts, use `cache:policy:push`.

Use the `pull` policy when you have many jobs executing in parallel that use the same cache. This policy speeds up job execution and reduces load on the cache server. You can use a job with the `push` policy to build the cache.

Must be used with `cache: paths`, or nothing is cached.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- `pull`
- `push`
- `pull-push` (default)
- CI/CD variables.

**Example of `cache:policy`**:

```yaml
prepare-dependencies-job:
  stage: build
  cache:
    key: gems
    paths:
      - vendor/bundle
    policy: push
  script:
    - echo "This job only downloads dependencies and builds the cache."
    - echo "Downloading dependencies..."

faster-test-job:
  stage: test
  cache:
    key: gems
    paths:
      - vendor/bundle
    policy: pull
  script:
    - echo "This job script uses the cache, but does not update it."
    - echo "Running tests..."
```

**Related topics**:

- You can use a variable to control a job’s cache policy.

#### `cache:fallback_keys`

Use `cache:fallback_keys` to specify a list of keys to try to restore cache from if there is no cache found for the `cache:key`. Caches are retrieved in the order specified in the `fallback_keys` section.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- An array of cache keys

**Example of `cache:fallback_keys`**:

```yaml
rspec:
  script: rspec
  cache:
    key: gems-$CI_COMMIT_REF_SLUG
    paths:
      - rspec/
    fallback_keys:
      - gems
    when: 'always'
```

### `coverage`

Use `coverage` with a custom regular expression to configure how code coverage is extracted from the job output. GitLab displays the matched percentage in the MR widget, pipeline job list, and analytics graphs.

**Supported values**:

- An RE2 regular expression. Must start and end with `/`. Must match the coverage number. May match surrounding text as well, so you don’t need to use a regular expression character group to capture the exact number. Because it uses RE2 syntax, all groups must be non-capturing.

**Example of `coverage`**:

```yaml
job1:
  script: rspec
  coverage: '/Code coverage: \d+(?:\.\d+)?/'
```

In this example:

1. GitLab checks the job log for a match with the regular expression. A line like `Code coverage: 67.89% of lines covered` matches.
2. GitLab then checks the matched fragment against `\d+(?:\.\d+)?` to extract the number. The sample regex matches `67.89`.

**Additional details**:

- If there is more than one matched line in the job output, the last line is used.
- If there are multiple matches in a single line, the last match is used.
- If there are multiple coverage numbers in the matched fragment, the first number is used.
- Leading zeros are removed.
- Coverage output from child pipelines is not recorded. See issue 280818.
- To display line-by-line diff annotations in the MR diff, configure `artifacts:reports:coverage_report` separately. Configuring one does not enable the other.

**Related topics**:

- Coverage regex patterns
- Coverage visualization

### `dast_configuration`

- Tier: Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

Use the `dast_configuration` keyword to specify a site profile and scanner profile to be used in a CI/CD configuration. Both profiles must first have been created in the project. The job’s stage must be `dast`.

**Keyword type**: Job keyword. You can use only as part of a job.

**Supported values**: One each of `site_profile` and `scanner_profile`.

- Use `site_profile` to specify the site profile to be used in the job.
- Use `scanner_profile` to specify the scanner profile to be used in the job.

**Example of `dast_configuration`**:

```yaml
stages:
  - build
  - dast

include:
  - template: DAST.gitlab-ci.yml

dast:
  dast_configuration:
    site_profile: "Example Co"
    scanner_profile: "Quick Passive Test"
```

In this example, the `dast` job extends the `dast` configuration added with the `include` keyword to select a specific site profile and scanner profile.

**Additional details**:

- Settings contained in either a site profile or scanner profile take precedence over those contained in the DAST template.

**Related topics**:

- Site profile.
- Scanner profile.

### `dependencies`

Use the `dependencies` keyword to define a list of specific jobs to fetch artifacts from. The specified jobs must all be in earlier stages. You can also set a job to download no artifacts at all.

When `dependencies` is not defined in a job, all jobs in earlier stages are considered dependent and the job fetches all artifacts from those jobs.

To fetch artifacts from a job in the same stage, you must use `needs:artifacts`. You should not combine `dependencies` with `needs` in the same job.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- The names of jobs to fetch artifacts from.
- An empty array (`[]`), to configure the job to not download any artifacts.

**Example of `dependencies`**:

```yaml
build mac:
  stage: build
  script: make build:mac
  artifacts:
    paths:
      - binaries/

build linux:
  stage: build
  script: make build:linux
  artifacts:
    paths:
      - binaries/

test mac:
  stage: test
  script: make test:mac
  dependencies:
    - build mac

test linux:
  stage: test
  script: make test:linux
  dependencies:
    - build linux

deploy:
  stage: deploy
  script: make deploy
  environment: production
```

In this example, two jobs have artifacts: `build mac` and `build linux`. When `test mac` is executed, the artifacts from `build mac` are downloaded and extracted in the context of the build. The same thing happens for `test linux` and artifacts from `build linux`.

The `deploy` job downloads artifacts from all previous jobs because of the stage precedence.

**Additional details**:

- If the earlier job does not generate artifacts, or is a manual job that didn’t run, the dependent job still runs and does not generate an error.
- If the artifacts of a dependent job are expired or deleted, then the job fails.

### `environment`

Use `environment` to define the environment that a job deploys to.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**: The name of the environment the job deploys to, in one of these formats:

- Plain text, including letters, digits, spaces, and these characters: `-`, `_`, `/`, `$`, `{`, `}`.
- CI/CD variables, including predefined, project, group, instance, or variables defined in the `.gitlab-ci.yml` file. You can’t use variables defined in a `script` section.

**Example of `environment`**:

```yaml
deploy to production:
  stage: deploy
  script: git push production HEAD:main
  environment: production
```

**Additional details**:

- If you specify an `environment` and no environment with that name exists, an environment is created.

#### `environment:name`

Set a name for an environment.

Common environment names are `qa`, `staging`, and `production`, but you can use any name.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**: The name of the environment the job deploys to, in one of these formats:

- Plain text, including letters, digits, spaces, and these characters: `-`, `_`, `/`, `$`, `{`, `}`.
- CI/CD variables, including predefined, project, group, instance, or variables defined in the `.gitlab-ci.yml` file. You can’t use variables defined in a `script` section.

**Example of `environment:name`**:

```yaml
deploy to production:
  stage: deploy
  script: git push production HEAD:main
  environment:
    name: production
```

#### `environment:url`

Set a URL for an environment.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**: A single URL, in one of these formats:

- Plain text, like `https://prod.example.com`.
- CI/CD variables, including predefined, project, group, instance, or variables defined in the `.gitlab-ci.yml` file. You can’t use variables defined in a `script` section.

**Example of `environment:url`**:

```yaml
deploy to production:
  stage: deploy
  script: git push production HEAD:main
  environment:
    name: production
    url: https://prod.example.com
```

**Additional details**:

- After the job completes, you can access the URL by selecting a button in the merge request, environment, or deployment pages.

#### `environment:on_stop`

Closing (stopping) environments can be achieved with the `on_stop` keyword defined under `environment`. It declares a different job that runs to close the environment.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Additional details**:

- See `environment:action` for more details and an example.

#### `environment:action`

Use the `action` keyword to specify how the job interacts with the environment.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**: One of the following keywords:

| **Value** | **Description** |
|---|---|
| `start` | Default value. Indicates that the job starts the environment. The deployment is created after the job starts. |
| `prepare` | Indicates that the job is only preparing the environment. It does not trigger deployments. Read more about preparing environments. |
| `stop` | Indicates that the job stops an environment. Read more about stopping an environment. |
| `verify` | Indicates that the job is only verifying the environment. It does not trigger deployments. Read more about verifying environments. |
| `access` | Indicates that the job is only accessing the environment. It does not trigger deployments. Read more about accessing environments. |

**Example of `environment:action`**:

```yaml
stop_review_app:
  stage: deploy
  variables:
    GIT_STRATEGY: none
  script: make delete-app
  when: manual
  environment:
    name: review/$CI_COMMIT_REF_SLUG
    action: stop
```

#### `environment:auto_stop_in`

- Updated to support `prepare`, `access` and `verify` environment actions in GitLab 17.7.

The `auto_stop_in` keyword specifies the lifetime of the environment. When an environment expires, GitLab automatically stops it.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**: A period of time written in natural language. For example, these are all equivalent:

- `168 hours`
- `7 days`
- `one week`
- `never`

CI/CD variables are supported.

**Example of `environment:auto_stop_in`**:

```yaml
review_app:
  script: deploy-review-app
  environment:
    name: review/$CI_COMMIT_REF_SLUG
    auto_stop_in: 1 day
```

When the environment for `review_app` is created, the environment’s lifetime is set to `1 day`. Every time the review app is deployed, that lifetime is also reset to `1 day`.

The `auto_stop_in` keyword can be used for all environment actions except `stop`. Some actions can be used to reset the scheduled stop time for the environment. For more information, see Access an environment for preparation or verification purposes.

**Related topics**:

- Environments auto-stop documentation.

#### `environment:kubernetes`

- `agent` keyword introduced in GitLab 17.6.
- `namespace` and `flux_resource_path` keywords introduced in GitLab 17.7.
- `namespace` and `flux_resource_path` keywords deprecated in GitLab 18.4.
- `dashboard:namespace` and `dashboard:flux_resource_path` keywords introduced in GitLab 18.4.

Use the `kubernetes` keyword to configure the dashboard for Kubernetes and GitLab-managed Kubernetes resources for an environment.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- `agent`: A string specifying the GitLab agent for Kubernetes. The format is `path/to/agent/project:agent-name`. If the agent is connected to the project running the pipeline, use `$CI_PROJECT_PATH:agent-name`.
- `dashboard:namespace`: A string representing the Kubernetes namespace where the environment is deployed. The namespace must be set together with the `agent` keyword. `namespace` is deprecated.
- `dashboard:flux_resource_path`: A string representing the full path to the Flux resource, such as a `HelmRelease`. The Flux resource must be set together with the `agent` and `dashboard:namespace` keywords. `flux_resource_path` is deprecated.
- `managed_resources`: A hash with the `enabled` keyword to configure the GitLab-managed Kubernetes resources for the environment.
  - `managed_resources:enabled`: A boolean value indicating whether GitLab-managed Kubernetes resources are enabled for the environment.
- `dashboard`: A hash with the `dashboard:namespace` and `dashboard:flux_resource_path` keywords to configure the dashboard for Kubernetes for the environment.

**Example of `environment:kubernetes`**:

```yaml
deploy:
  stage: deploy
  script: make deploy-app
  environment:
    name: production
    kubernetes:
      agent: path/to/agent/project:agent-name
      dashboard:
        namespace: my-namespace
        flux_resource_path: helm.toolkit.fluxcd.io/v2/namespaces/flux-system/helmreleases/helm-release-resource
```

**Example of `environment:kubernetes`** when disabling managed resources:

```yaml
deploy:
  stage: deploy
  script: make deploy-app
  environment:
    name: production
    kubernetes:
      agent: path/to/agent/project:agent-name
      managed_resources:
        enabled: false
      dashboard:
        namespace: my-namespace
        flux_resource_path: helm.toolkit.fluxcd.io/v2/namespaces/flux-system/helmreleases/helm-release-resource
```

This configuration:

- Sets up the `deploy` job to deploy to the `production` environment.
- Associates the agent named `agent-name` with the environment.
- Configures the dashboard for Kubernetes for an environment with the namespace `my-namespace` and the `flux_resource_path` set to `helm.toolkit.fluxcd.io/v2/namespaces/flux-system/helmreleases/helm-release-resource`.

**Additional details**:

- To use the dashboard, you must install the GitLab agent for Kubernetes and configure `user_access` for the environment’s project or its parent group.
- The user running the job must be authorized to access the cluster agent. Otherwise, the dashboard ignores the `agent`, `namespace`, and `flux_resource_path` attributes.
- If you only want to set the `agent`, you do not have to set the `namespace`, and cannot set `flux_resource_path`. However, this configuration lists all namespaces in a cluster in the dashboard for Kubernetes.

#### `environment:deployment_tier`

- Support for CI/CD variables added in GitLab 18.5.

Use the `deployment_tier` keyword to specify the tier of the deployment environment.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**: One of the following:

- `production`
- `staging`
- `testing`
- `development`
- `other`
- CI/CD variables, including predefined, project, group, instance, or variables defined in the `.gitlab-ci.yml` file. You can’t use variables defined in a `script` section.

**Example of `environment:deployment_tier`**:

```yaml
deploy:
  script: echo
  environment:
    name: customer-portal
    deployment_tier: production
```

**Additional details**:

- Environments created from this job definition are assigned a tier based on this value.
- Existing environments don’t have their tier updated if this value is added later. Existing environments must have their tier updated via the Environments API.

**Related topics**:

- Deployment tier of environments.

#### Dynamic environments

Use CI/CD variables to dynamically name environments.

For example:

```yaml
deploy as review app:
  stage: deploy
  script: make deploy
  environment:
    name: review/$CI_COMMIT_REF_SLUG
    url: https://$CI_ENVIRONMENT_SLUG.example.com/
```

The `deploy as review app` job is marked as a deployment to dynamically create the `review/$CI_COMMIT_REF_SLUG` environment. `$CI_COMMIT_REF_SLUG` is a CI/CD variable set by the runner. The `$CI_ENVIRONMENT_SLUG` variable is based on the environment name, but suitable for inclusion in URLs. If the `deploy as review app` job runs in a branch named `pow`, this environment would be accessible with a URL like `https://review-pow.example.com/`.

The common use case is to create dynamic environments for branches and use them as review apps. You can see an example that uses review apps at https://gitlab.com/gitlab-examples/review-apps-nginx/.

### `extends`

Use `extends` to reuse configuration sections. It’s an alternative to YAML anchors and is a little more flexible and readable.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- The name of another job in the pipeline.
- A list (array) of names of other jobs in the pipeline.

**Example of `extends`**:

```yaml
.tests:
  stage: test
  image: ruby:3.0

rspec:
  extends: .tests
  script: rake rspec

rubocop:
  extends: .tests
  script: bundle exec rubocop
```

In this example, the `rspec` job uses the configuration from the `.tests` template job. When creating the pipeline, GitLab:

- Performs a reverse deep merge based on the keys.
- Merges the `.tests` content with the `rspec` job.
- Doesn’t merge the values of the keys.

The combined configuration is equivalent to these jobs:

```yaml
rspec:
  stage: test
  image: ruby:3.0
  script: rake rspec

rubocop:
  stage: test
  image: ruby:3.0
  script: bundle exec rubocop
```

**Additional details**:

- You can use multiple parents for `extends`.
- The `extends` keyword supports up to eleven levels of inheritance, but you should avoid using more than three levels.
- In the previous example, `.tests` is a hidden job, but you can extend configuration from regular jobs as well.

**Related topics**:

- Reuse configuration sections by using `extends`.
- Use `extends` to reuse configuration from included configuration files.

### `hooks`

Use `hooks` to specify lists of commands to execute on the runner at certain stages of job execution, like before retrieving the Git repository.

Job configuration and default configuration does not merge together. If the pipeline has `default:hooks` defined, and the job also has `hooks`, the job configuration takes precedence and the default configuration is not used.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- A hash of hooks and their commands. Available hooks: `pre_get_sources_script`.

#### `hooks:pre_get_sources_script`

Use `hooks:pre_get_sources_script` to specify a list of commands to execute on the runner before cloning the Git repository and any submodules. You can use it for example to:

- Adjust the Git configuration.
- Export tracing variables.

**Supported values**: An array including:

- Single line commands.
- Long commands split over multiple lines.
- YAML anchors.

CI/CD variables are supported.

**Example of `hooks:pre_get_sources_script`**:

```yaml
job1:
  hooks:
    pre_get_sources_script:
      - echo 'hello job1 pre_get_sources_script'
  script: echo 'hello job1 script'
```

**Related topics**:

- GitLab Runner configuration

### `identity`

- Tier: Free, Premium, Ultimate
- Offering: GitLab.com
- Status: Beta

- Introduced in GitLab 16.9 with a flag named `google_cloud_support_feature_flag`. This feature is in beta.
- Enabled on GitLab.com in GitLab 17.1. Feature flag `google_cloud_support_feature_flag` removed.

This feature is in beta.

Use `identity` to authenticate with third party services using identity federation.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**: An identifier. Supported providers:

- `google_cloud`: Google Cloud. Must be configured with the Google Cloud IAM integration.

**Example of `identity`**:

```yaml
job_with_workload_identity:
  identity: google_cloud
  script:
    - gcloud compute instances list
```

**Related topics**:

- Workload Identity Federation.
- Google Cloud IAM integration.

### `id_tokens`

Use `id_tokens` to create ID tokens to authenticate with third party services. All JWTs created this way support OIDC authentication. The required `aud` sub-keyword is used to configure the `aud` claim for the JWT.

Job configuration and default configuration does not merge together. If the pipeline has `default:id_tokens` defined, and the job also has `id_tokens`, the job configuration takes precedence and the default configuration is not used.

**Supported values**:

- Token names with their `aud` claims. `aud` supports:
  - A single string.
  - An array of strings.
  - CI/CD variables.

**Example of `id_tokens`**:

```yaml
job_with_id_tokens:
  id_tokens:
    ID_TOKEN_1:
      aud: https://vault.example.com
    ID_TOKEN_2:
      aud:
        - https://gcp.com
        - https://aws.com
    SIGSTORE_ID_TOKEN:
      aud: sigstore
  script:
    - command_to_authenticate_with_vault $ID_TOKEN_1
    - command_to_authenticate_with_aws $ID_TOKEN_2
    - command_to_authenticate_with_gcp $ID_TOKEN_2
```

**Related topics**:

- ID token authentication.
- Connect to cloud services.
- Keyless signing with Sigstore.

### `image`

Use `image` to specify a Docker image that the job runs in.

Job configuration and default configuration does not merge together. If the pipeline has `default:image` defined, and the job also has `image`, the job configuration takes precedence and the default configuration is not used.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**: The name of the image, including the registry path if needed, in one of these formats:

- `<image-name>` (Same as using `<image-name>` with the `latest` tag)
- `<image-name>:<tag>`
- `<image-name>@<digest>`

CI/CD variables are supported.

**Example of `image`**:

```yaml
default:
  image: ruby:3.0

rspec:
  script: bundle exec rspec

rspec 2.7:
  image: registry.example.com/my-group/my-project/ruby:2.7
  script: bundle exec rspec
```

In this example, the `ruby:3.0` image is the default for all jobs in the pipeline. The `rspec 2.7` job does not use the default, because it overrides the default with a job-specific `image` section.

**Additional details**:

- Using `image` at the top level, but not in the `default` section, is deprecated.

**Related topics**:

- Run your CI/CD jobs in Docker containers.

#### `image:name`

The name of the Docker image that the job runs in. Similar to `image` used by itself.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**: The name of the image, including the registry path if needed, in one of these formats:

- `<image-name>` (Same as using `<image-name>` with the `latest` tag)
- `<image-name>:<tag>`
- `<image-name>@<digest>`

CI/CD variables are supported.

**Example of `image:name`**:

```yaml
test-job:
  image:
    name: "registry.example.com/my/image:latest"
  script: echo "Hello world"
```

**Related topics**:

- Run your CI/CD jobs in Docker containers.

#### `image:entrypoint`

Command or script to execute as the container’s entry point.

When the Docker container is created, the `entrypoint` is translated to the Docker `--entrypoint` option. The syntax is similar to the Dockerfile `ENTRYPOINT` directive, where each shell token is a separate string in the array.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- A string.

**Example of `image:entrypoint`**:

```yaml
test-job:
  image:
    name: super/sql:experimental
    entrypoint: [""]
  script: echo "Hello world"
```

**Related topics**:

- Override the entrypoint of an image.

#### `image:docker`

Use `image:docker` to pass options to runners using the Docker executor or the Kubernetes executor. This keyword does not work with other executor types.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

A hash of options for the Docker executor, which can include:

- `platform`: Selects the architecture of the image to pull. When not specified, the default is the same platform as the host runner.
- `user`: Specify the username or UID to use when running the container.

**Example of `image:docker`**:

```yaml
arm-sql-job:
  script: echo "Run sql tests"
  image:
    name: super/sql:experimental
    docker:
      platform: arm64/v8
      user: dave
```

**Additional details**:

- `image:docker:platform` maps to the `docker pull --platform` option.
- `image:docker:user` maps to the `docker run --user` option.

#### `image:kubernetes`

- Introduced in GitLab 18.0. Requires GitLab Runner 17.11 or later.
- `user` input option introduced in GitLab Runner 17.11.
- `user` input option extended to support `uid:gid` format in GitLab 18.0.

Use `image:kubernetes` to pass options to the GitLab Runner Kubernetes executor. This keyword does not work with other executor types.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

A hash of options for the Kubernetes executor, which can include:

- `user`: Specify the username or UID to use when the container runs. You can also use it to set GID by using the `UID:GID` format.

**Example of `image:kubernetes` with only UID**:

```yaml
arm-sql-job:
  script: echo "Run sql tests"
  image:
    name: super/sql:experimental
    kubernetes:
      user: "1001"
```

**Example of `image:kubernetes` with both UID and GID**:

```yaml
arm-sql-job:
  script: echo "Run sql tests"
  image:
    name: super/sql:experimental
    kubernetes:
      user: "1001:1001"
```

#### `image:pull_policy`

The pull policy that the runner uses to fetch the Docker image. Requires GitLab Runner 15.1 or later.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- A single pull policy, or multiple pull policies in an array. Can be `always`, `if-not-present`, or `never`.

**Examples of `image:pull_policy`**:

```yaml
job1:
  script: echo "A single pull policy."
  image:
    name: ruby:3.0
    pull_policy: if-not-present

job2:
  script: echo "Multiple pull policies."
  image:
    name: ruby:3.0
    pull_policy: [always, if-not-present]
```

**Additional details**:

- If the runner does not support the defined pull policy, the job fails with an error similar to: `ERROR: Job failed (system failure): the configured PullPolicies ([always]) are not allowed by AllowedPullPolicies ([never])`.

**Related topics**:

- Run your CI/CD jobs in Docker containers.
- Configure how runners pull images.
- Set multiple pull policies.

### `inputs`

- Introduced in GitLab 18.10.

Use `inputs` to define typed and validated inputs for a job. Job inputs can be overridden when manually running or retrying a job.

Job inputs are parameters that provide type safety and validation. Unlike CI/CD variables, only inputs explicitly defined in the job can be specified when running or retrying the job. All job input names must be predefined.

Reference job input values with the `${{ job.inputs.INPUT_NAME }}` Moa expression syntax.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

A hash of input names, where each input is configured with one or more subkeys:

- `default` (required)
- `type`
- `options`
- `description`
- `regex`

**Example of `inputs`**:

```yaml
test_job:
  inputs:
    test_suite:
      default: unit
      description: Which test suite to run
      options: [unit, integration, e2e]
    parallel_count:
      type: number
      default: 5
      description: Number of parallel test runners
    verbose:
      type: boolean
      default: false
      description: Enable verbose test output
  script:
    - 'echo "Running ${{ job.inputs.test_suite }} tests"'
    - 'if [ "${{ job.inputs.verbose }}" == "true" ]; then export TEST_VERBOSE=1; fi'
    - ./run_tests.sh --suite ${{ job.inputs.test_suite }} --parallel ${{ job.inputs.parallel_count }}
```

**Additional details**:

- Job inputs are validated when the job is created and when you try to retry a job with new input values. If validation fails, the job does not start.
- Job inputs are scoped to the job where they are defined and cannot be accessed by other jobs.
- For a complete list of keywords that support job inputs, see where you can use job inputs.

#### `inputs:default`

All job inputs must have a default value defined with `default`.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**: Any value matching the input’s `type`.

**Example of `inputs:default`**:

```yaml
test_job:
  inputs:
    environment:
      default: staging
    timeout:
      type: number
      default: 30
```

#### `inputs:type`

Use `type` to define the data type of the input value.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- `string` (default)
- `number`
- `boolean`
- `array`.

**Example of `inputs:type`**:

```yaml
test_job:
  inputs:
    count:
      type: number
      default: 5
    enabled:
      type: boolean
      default: true
```

#### `inputs:description`

Use `description` to provide information about the input’s purpose. The description does not affect the input’s behavior.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**: A string.

**Example of `inputs:description`**:

```yaml
deploy_job:
  inputs:
    environment:
      default: staging
      description: Target deployment environment
```

#### `inputs:options`

Use `options` to specify a list of allowed values for an input.

The input value must match one of the listed options exactly (case-sensitive). Validation fails if the value does not match an option.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**: An array of allowed values.

**Example of `inputs:options`**:

```yaml
deploy_job:
  inputs:
    environment:
      default: staging
      options: [development, staging, production]
```

#### `inputs:regex`

Use `regex` to specify a regular expression pattern that the input value must match.

Validation fails if the value does not match the regular expression.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**: A regular expression string.

**Example of `inputs:regex`**:

```yaml
deploy_job:
  inputs:
    version:
      default: v1.0.0
      regex: ^v\d+\.\d+\.\d+$
```

In this example, an input value of `v1.1.1` passes the regex validation, but an input of `v1.1.1-beta` does not.

### `inherit`

Use `inherit` to control inheritance of default keywords and variables.

#### `inherit:default`

Use `inherit:default` to control the inheritance of default keywords.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- `true` (default) or `false` to enable or disable the inheritance of all default keywords.
- A list of specific default keywords to inherit.

**Example of `inherit:default`**:

```yaml
default:
  retry: 2
  image: ruby:3.0
  interruptible: true

job1:
  script: echo "This job does not inherit any default keywords."
  inherit:
    default: false

job2:
  script: echo "This job inherits only the two listed default keywords. It does not inherit 'interruptible'."
  inherit:
    default:
      - retry
      - image
```

**Additional details**:

- You can also list default keywords to inherit on one line: `default: [keyword1, keyword2]`

#### `inherit:variables`

Use `inherit:variables` to control the inheritance of default variables keywords.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- `true` (default) or `false` to enable or disable the inheritance of all default variables.
- A list of specific variables to inherit.

**Example of `inherit:variables`**:

```yaml
variables:
  VARIABLE1: "This is default variable 1"
  VARIABLE2: "This is default variable 2"
  VARIABLE3: "This is default variable 3"

job1:
  script: echo "This job does not inherit any default variables."
  inherit:
    variables: false

job2:
  script: echo "This job inherits only the two listed default variables. It does not inherit 'VARIABLE3'."
  inherit:
    variables:
      - VARIABLE1
      - VARIABLE2
```

**Additional details**:

- You can also list default variables to inherit on one line: `variables: [VARIABLE1, VARIABLE2]`

### `interruptible`

Use `interruptible` to configure the auto-cancel redundant pipelines feature to cancel a job before it completes if a new pipeline on the same ref starts for a newer commit. If the feature is disabled, the keyword has no effect. The new pipeline must be for a commit with new changes. For example, the **Auto-cancel redundant pipelines** feature has no effect if you select **New pipeline** in the UI to run a pipeline for the same commit.

The behavior of the **Auto-cancel redundant pipelines** feature can be controlled by the `workflow:auto_cancel:on_new_commit` setting.

**Keyword type**: Job keyword. You can use it only as part of a job or in the `default` section.

**Supported values**:

- `true` or `false` (default).

**Example of `interruptible` with the default behavior**:

```yaml
workflow:
  auto_cancel:
    on_new_commit: conservative # the default behavior

stages:
  - stage1
  - stage2
  - stage3

step-1:
  stage: stage1
  script:
    - echo "Can be canceled."
  interruptible: true

step-2:
  stage: stage2
  script:
    - echo "Can not be canceled."

step-3:
  stage: stage3
  script:
    - echo "Because step-2 can not be canceled, this step can never be canceled, even though it's set as interruptible."
  interruptible: true
```

In this example, a new pipeline causes a running pipeline to be:

- Canceled, if only `step-1` is running or pending.
- Not canceled, after `step-2` starts.

**Example of `interruptible` with the `auto_cancel:on_new_commit:interruptible` setting**:

```yaml
workflow:
  auto_cancel:
    on_new_commit: interruptible

stages:
  - stage1
  - stage2
  - stage3

step-1:
  stage: stage1
  script:
    - echo "Can be canceled."
  interruptible: true

step-2:
  stage: stage2
  script:
    - echo "Can not be canceled."

step-3:
  stage: stage3
  script:
    - echo "Can be canceled."
  interruptible: true
```

In this example, a new pipeline causes a running pipeline to cancel `step-1` and `step-3` if they are running or pending.

**Additional details**:

- Only set `interruptible: true` if the job can be safely canceled after it has started, like a build job. Deployment jobs usually shouldn’t be canceled, to prevent partial deployments.
- When using the default behavior or `workflow:auto_cancel:on_new_commit: conservative`:
  - A job that has not started yet is always considered `interruptible: true`, regardless of the job’s configuration. The `interruptible` configuration is only considered after the job starts.
  - **Running** pipelines are only canceled if all running jobs are configured with `interruptible: true` or no jobs configured with `interruptible: false` have started at any time. After a job with `interruptible: false` starts, the entire pipeline is no longer considered interruptible.
  - If the pipeline triggered a downstream pipeline, but no job with `interruptible: false` in the downstream pipeline has started yet, the downstream pipeline is also canceled.
- You can add an optional manual job with `interruptible: false` in the first stage of a pipeline to allow users to manually prevent a pipeline from being automatically canceled. After a user starts the job, the pipeline cannot be canceled by the **Auto-cancel redundant pipelines** feature.
- When using `interruptible` with a trigger job:
  - The triggered downstream pipeline is never affected by the trigger job’s `interruptible` configuration.
  - If `workflow:auto_cancel` is set to `conservative`, the trigger job’s `interruptible` configuration has no effect.
  - If `workflow:auto_cancel` is set to `interruptible`, a trigger job with `interruptible: true` can be automatically canceled.

### `needs`

Use `needs` to execute jobs out-of-order. Relationships between jobs that use `needs` can be visualized as a directed acyclic graph.

You can ignore stage ordering and run some jobs without waiting for others to complete. Jobs in multiple stages can run concurrently.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- An array of jobs (maximum of 50 jobs).
- An empty array (`[]`), to set the job to start as soon as the pipeline is created.

**Example of `needs`**:

```yaml
linux:build:
  stage: build
  script: echo "Building linux..."

mac:build:
  stage: build
  script: echo "Building mac..."

lint:
  stage: test
  needs: []
  script: echo "Linting..."

linux:rspec:
  stage: test
  needs: ["linux:build"]
  script: echo "Running rspec on linux..."

mac:rspec:
  stage: test
  needs: ["mac:build"]
  script: echo "Running rspec on mac..."

production:
  stage: deploy
  script: echo "Running production..."
  environment: production
```

This example creates four paths of execution:

- Linter: The `lint` job runs immediately without waiting for the `build` stage to complete because it has no needs (`needs: []`).
- Linux path: The `linux:rspec` job runs as soon as the `linux:build` job finishes, without waiting for `mac:build` to finish.
- macOS path: The `mac:rspec` jobs runs as soon as the `mac:build` job finishes, without waiting for `linux:build` to finish.
- The `production` job runs as soon as all previous jobs finish: `lint`, `linux:build`, `linux:rspec`, `mac:build`, `mac:rspec`.

**Additional details**:

- The maximum number of jobs that a single job can have in the `needs` array is limited:
  - For GitLab.com, the limit is 50. For more information, see issue 350398.
  - For GitLab Self-Managed and GitLab Dedicated, the default limit is 50. This limit can be changed by updating the CI/CD limits in the Admin area.
- If `needs` refers to a job that uses the `parallel` keyword, it depends on all jobs created in parallel, not just one job. It also downloads artifacts from all the parallel jobs by default. If the artifacts have the same name, they overwrite each other and only the last one downloaded is saved.
  - To have `needs` refer to a subset of parallelized jobs (and not all of the parallelized jobs), use the `needs:parallel:matrix` keyword.
- You can refer to jobs in the same stage as the job you are configuring.
- If `needs` refers to a job that might not be added to a pipeline because of `only`, `except`, or `rules`, the pipeline might fail to create. Use the `needs:optional` keyword to resolve a failed pipeline creation.
- If a pipeline has jobs with `needs: []` and jobs in the `.pre` stage, they will all start as soon as the pipeline is created. Jobs with `needs: []` start immediately, and jobs in the `.pre` stage also start immediately.

#### `needs:artifacts`

When a job uses `needs`, it no longer downloads all artifacts from previous stages by default, because jobs with `needs` can start before earlier stages complete. With `needs` you can only download artifacts from the jobs listed in the `needs` configuration.

Use `artifacts: true` (default) or `artifacts: false` to control when artifacts are downloaded in jobs that use `needs`.

**Keyword type**: Job keyword. You can use it only as part of a job. Must be used with `needs:job`.

**Supported values**:

- `true` (default) or `false`.

**Example of `needs:artifacts`**:

```yaml
test-job1:
  stage: test
  needs:
    - job: build_job1
      artifacts: true

test-job2:
  stage: test
  needs:
    - job: build_job2
      artifacts: false

test-job3:
  needs:
    - job: build_job1
      artifacts: true
    - job: build_job2
    - build_job3
```

In this example:

- The `test-job1` job downloads the `build_job1` artifacts
- The `test-job2` job does not download the `build_job2` artifacts.
- The `test-job3` job downloads the artifacts from all three `build_jobs`, because `artifacts` is `true`, or defaults to `true`, for all three needed jobs.

**Additional details**:

- You should not combine `needs` with `dependencies` in the same job.

#### `needs:project`

- Tier: Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

Use `needs:project` to download artifacts from up to five jobs in other pipelines. The artifacts are downloaded from the latest successful specified job for the specified ref. To specify multiple jobs, add each as separate array items under the `needs` keyword.

If there is a pipeline running for the ref, a job with `needs:project` does not wait for the pipeline to complete. Instead, the artifacts are downloaded from the latest successful run of the specified job.

`needs:project` must be used with `job`, `ref`, and `artifacts`.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- `needs:project`: A full project path, including namespace and group.
- `job`: The job to download artifacts from.
- `ref`: The ref to download artifacts from.
- `artifacts`: Must be `true` to download artifacts.

**Examples of `needs:project`**:

```yaml
build_job:
  stage: build
  script:
    - ls -lhR
  needs:
    - project: namespace/group/project-name
      job: build-1
      ref: main
      artifacts: true
    - project: namespace/group/project-name-2
      job: build-2
      ref: main
      artifacts: true
```

In this example, `build_job` downloads the artifacts from the latest successful `build-1` and `build-2` jobs on the `main` branches in the `group/project-name` and `group/project-name-2` projects.

You can use CI/CD variables in `needs:project`, for example:

```yaml
build_job:
  stage: build
  script:
    - ls -lhR
  needs:
    - project: $CI_PROJECT_PATH
      job: $DEPENDENCY_JOB_NAME
      ref: $ARTIFACTS_DOWNLOAD_REF
      artifacts: true
```

**Additional details**:

- To download artifacts from a different pipeline in the current project, set `project` to be the same as the current project, but use a different ref than the current pipeline. Concurrent pipelines running on the same ref could override the artifacts.
- The user running the pipeline must have the Reporter, Developer, Maintainer, or Owner role for the group or project, or the group/project must have public visibility.
- You can’t use `needs:project` in the same job as `trigger`.
- When using `needs:project` to download artifacts from another pipeline, the job does not wait for the needed job to complete. Using `needs` to wait for jobs to complete is limited to jobs in the same pipeline. Make sure that the needed job in the other pipeline completes before the job that needs it tries to download the artifacts.
- You can’t download artifacts from jobs that run in `parallel`.
- Support CI/CD variables in `project`, `job`, and `ref`.

**Related topics**:

- To download artifacts between parent-child pipelines, use `needs:pipeline:job`.

#### `needs:pipeline:job`

A child pipeline can download artifacts from a successfully finished job in its parent pipeline or another child pipeline in the same parent-child pipeline hierarchy.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- `needs:pipeline`: A pipeline ID. Must be a pipeline present in the same parent-child pipeline hierarchy.
- `job`: The job to download artifacts from.

**Example of `needs:pipeline:job`**:

- Parent pipeline (`.gitlab-ci.yml`):`stages: - build - test create-artifact: stage: build script: echo "sample artifact" > artifact.txt artifacts: paths: [artifact.txt] child-pipeline: stage: test trigger: include: child.yml strategy: mirror variables: PARENT_PIPELINE_ID: $CI_PIPELINE_ID`
- Child pipeline (`child.yml`):`use-artifact: script: cat artifact.txt needs: - pipeline: $PARENT_PIPELINE_ID job: create-artifact`

In this example, the `create-artifact` job in the parent pipeline creates some artifacts. The `child-pipeline` job triggers a child pipeline, and passes the `CI_PIPELINE_ID` variable to the child pipeline as a new `PARENT_PIPELINE_ID` variable. The child pipeline can use that variable in `needs:pipeline` to download artifacts from the parent pipeline. Having the `create-artifact` and `child-pipeline` jobs in subsequent stages ensures that the `use-artifact` job only executes when `create-artifact` has successfully finished.

**Additional details**:

- The `pipeline` attribute does not accept the current pipeline ID (`$CI_PIPELINE_ID`). To download artifacts from a job in the current pipeline, use `needs:artifacts`.
- You cannot use `needs:pipeline:job` in a trigger job, or to fetch artifacts from a multi-project pipeline. To fetch artifacts from a multi-project pipeline use `needs:project`.
- The job listed in `needs:pipeline:job` must complete with a status of `success` or the artifacts can’t be fetched. Issue 367229 proposes to allow fetching artifacts from any job with artifacts.

#### `needs:optional`

To need a job that sometimes does not exist in the pipeline, add `optional: true` to the `needs` configuration. If not defined, `optional: false` is the default.

Jobs that use `rules`, `only`, or `except` and that are added with `include` might not always be added to a pipeline. GitLab checks the `needs` relationships before starting a pipeline:

- If the `needs` entry has `optional: true` and the needed job is present in the pipeline, the job waits for it to complete before starting.
- If the needed job is not present, the job can start when all other needs requirements are met.
- If the `needs` section contains only optional jobs, and none are added to the pipeline, the job starts immediately (the same as an empty `needs` entry: `needs: []`).
- If a needed job has `optional: false`, but it was not added to the pipeline, the pipeline fails to start with an error similar to: `'job1' job needs 'job2' job, but it was not added to the pipeline`.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Example of `needs:optional`**:

```yaml
build-job:
  stage: build

test-job1:
  stage: test

test-job2:
  stage: test
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH

deploy-job:
  stage: deploy
  needs:
    - job: test-job2
      optional: true
    - job: test-job1
  environment: production

review-job:
  stage: deploy
  needs:
    - job: test-job2
      optional: true
  environment: review
```

In this example:

- `build-job`, `test-job1`, and `test-job2` start in stage order.
- When the branch is the default branch, `test-job2` is added to the pipeline, so:
  - `deploy-job` waits for both `test-job1` and `test-job2` to complete.
  - `review-job` waits for `test-job2` to complete.
- When the branch is not the default branch, `test-job2` is not added to the pipeline, so:
  - `deploy-job` waits for only `test-job1` to complete, and does not wait for the missing `test-job2`.
  - `review-job` has no other needed jobs and starts immediately (at the same time as `build-job`), like `needs: []`.

**Additional details**:

- You cannot use `needs:optional` with `needs:parallel:matrix`.

#### `needs:pipeline`

You can mirror the pipeline status from an upstream pipeline to a job by using the `needs:pipeline` keyword. The latest pipeline status from the default branch is replicated to the job.

**Keyword type**: Job keyword. You can use it only as part of a job.

**Supported values**:

- A full project path, including namespace and group. If the project is in the same group or namespace, you can omit them from the `project` keyword. For example: `project: group/project-name` or `project: project-name`.

**Example of `needs:pipeline`**:

```yaml
upstream_status:
  stage: test
  needs:
    pipeline: other/project
```

**Additional details**:

- If you add the `job` keyword to `needs:pipeline`, the job no longer mirrors the pipeline status. The behavior changes to `needs:pipeline:job`.

#### `needs:parallel:matrix`

Jobs can use `parallel:matrix` to run a job multiple times in parallel in a single pipeline, but with different variable values for each instance of the job.

Use `needs:parallel:matrix` to execute jobs out-of-order depending on parallelized jobs.

**Keyword type**: Job keyword. You can use it only as part of a job. Must be used with `needs:job`.

**Supported values**: An array of hashes of matrix identifiers:

- The identifiers and values must be selected from the identifiers and values defined in the `parallel:matrix` job.
- You can use matrix expressions.

**Example of `needs:parallel:matrix`**:

```yaml
linux:build:
  stage: build
  script: echo "Building linux..."
  parallel:
    matrix:
      - PROVIDER: aws
        STACK:
          - monitoring
          - app1
          - app2

linux:rspec:
  stage: test
  needs:
    - job: linux:build
      parallel:
        matrix:
          - PROVIDER: aws
            STACK: app1
  script: echo "Running rspec on linux..."
```

The previous example generates the following jobs:

```plaintext
linux:build: [aws, monitoring]
linux:build: [aws, app1]
linux:build: [aws, app2]
linux:rspec
```

The `linux:rspec` job runs as soon as the `linux:build: [aws, app1]` job finishes.

**Additional details**:

- You cannot use `needs:parallel:matrix` with `needs:optional`.
- The order of the matrix identifiers in `needs:parallel:matrix` must match the order of the matrix variables in the needed job. For example, reversing the order of the variables in the `linux:rspec` job in the previous example would be invalid:linux:rspec: stage: test needs: - job: linux:build parallel: matrix: - STACK: app1 # The variable order does not match `linux:build` and is invalid. PROVIDER: aws script: echo "Running rspec on linux..."

**Related topics**:

- Specify a parallelized job using needs with multiple parallelized jobs.
- Matrix expressions in `needs:parallel:matrix`.
