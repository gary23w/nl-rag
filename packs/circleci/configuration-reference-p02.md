---
title: "Configuration reference (part 2/3)"
source: https://circleci.com/docs/configuration-reference/
domain: circleci
license: CC-BY-SA-4.0
tags: circleci pipeline, continuous integration, ci cd pipeline, build automation
fetched: 2026-07-02
part: 2/3
---

## **`steps`**

The `steps` setting in a job is a list of single key/value pairs, the key of which indicates the step type. The value may be either a configuration map or a string (depending on what that type of step requires). For example, using a map:

```dracula
jobs:
  build:
    docker:
      - image: cimg/base:2024.01
    working_directory: ~/canary-python
    environment:
      FOO: bar
    steps:
      - run:
          name: Running tests
          command: make test
```

Here `run` is a step type. The `name` attribute is used by the UI for display purposes. The `command` attribute is specific to the `run` step and defines the command to execute.

Some steps may implement a shorthand semantic. For example, `run` may also be called like this:

```dracula
jobs:
  build:
    docker:
      - image: cimg/base:2024.01
    steps:
      - run: make test
```

In its short form, the `run` step allows us to directly specify which `command` to execute as a string value. In this case the step itself provides default suitable values for other attributes (`name` here has the same value as `command`, for example).

Another shorthand, which is possible for some steps, is to use the step name as a string instead of a key/value pair:

```dracula
jobs:
  build:
    docker:
      - image: cimg/base:2024.01
    steps:
      - checkout
```

In this case, the `checkout` step checks out project source code into the job’s `working_directory`.

In general all steps can be described as:

| Key | Required | Type | Description |
|---|---|---|---|
| `<step_type>` | Y | Map or String | A configuration map for the step or some string whose semantics are defined by the step. |

Each built-in step is described in detail below.

### **`run`**

Use the `run` step to invoke command-line programs. The `run` step takes either a map of configuration values, or, when you call it in short-form, a string that serves as both the `command` and `name`. CircleCI executes `run` commands using non-login shells by default, so you must explicitly source any `dotfiles` as part of the command.

|   | The `run` step replaces the deprecated `deploy` step. If your job has a parallelism of 1, the deprecated `deploy` step can be swapped out directly for the `run` step. If your job has parallelism `> 1`, see Migrate From Deploy to Run. |
|---|---|

| Key | Required | Type | Description |
|---|---|---|---|
| `command` | Y | String | Command to run via the shell |
| `name` | N | String | Title of the step to be shown in the CircleCI UI (default: full `command`) |
| `shell` | N | String | Shell to use for execution command (default: See Default Shell Options) |
| `environment` | N | Map | Additional environment variables, locally scoped to command |
| `background` | N | Boolean | Whether or not this step runs in the background (default: false) |
| `working_directory` | N | String | The directory where this step runs. CircleCI interprets this relative to the `working_directory` of the job. (default: `.`) |
| `no_output_timeout` | N | String | Elapsed time the command can run without output. The string is a decimal with unit suffix, such as "20m", "1.25h", "5s". The default is 10 minutes and the maximum is governed by the maximum time a job is allowed to run. |
| `when` | N | String | Specify when to enable or disable the step. Takes the following values: `always`, `on_success`, `on_fail` (default: `on_success`) |
| `max_auto_reruns` | N | Integer | The maximum number of times to automatically rerun the step if it fails. Must be between `1` and `5`. |
| `auto_rerun_delay` | N | String | The delay between reruns of the step if it fails. This delay can only be set along with `max_auto_reruns`. The string is a decimal with unit suffix using either seconds `s` or minutes `m` up to a maximum of 10 minutes, such as "10s", "2m". |

Each `run` declaration represents a new shell. You can specify a multi-line `command` where each line runs in the same shell.

**Example:**

```dracula
jobs:
  my-job:
    docker:
      - image: cimg/base:2024.12
    resource_class: xlarge
    steps:
      - run:
          command: |
            echo Running test
            mkdir -p /tmp/test-results
            make test
```

You can also configure commands to run in the background if you do not want to wait for the step to complete before moving on to subsequent run steps.

#### *Default shell options*

For jobs that run on **Linux**, CircleCI defaults the `shell` option to `/bin/bash -eo pipefail` if `/bin/bash` exists in the build container. Otherwise, CircleCI uses `/bin/sh -eo pipefail`. The default shell is not a login shell (CircleCI does not specify `--login` or `-l`) and thus does not source your `~/.bash_profile`, `~/.bash_login`, or `~/.profile` files.

For jobs that run on **macOS**, the default shell is `/bin/bash --login -eo pipefail`. The shell is a non-interactive login shell. The shell executes `/etc/profile/` followed by `~/.bash_profile` before every step.

For more information about which files are executed when Bash is invoked, see the `INVOCATION` section of the `bash` manpage.

Descriptions of the `-eo pipefail` options are provided below.

#### `-e`

Exit immediately if any of the following exits with a non-zero status:

- A pipeline (which may consist of a single simple command).
- A subshell command enclosed in parentheses.
- One of the commands executed as part of a command list enclosed by braces.

In the previous example, `mkdir` failed to create a directory and returned a non-zero status, so the shell terminated command execution and marked the whole step as failed. If you want the opposite behavior, add `set +e` in your `command` or override the default `shell` in your `run` configuration map. For example:

**Example:**

```dracula
- run:
    command: |
      echo Running test
      set +e
      mkdir -p /tmp/test-results
      make test

- run:
    shell: /bin/sh
    command: |
      echo Running test
      mkdir -p /tmp/test-results
      make test
```

#### `-o pipefail`

If `pipefail` is enabled, the pipeline’s return status is the value of the last (rightmost) command to exit with a non-zero status, or zero if all commands exit successfully. The shell waits for all commands in the pipeline to terminate before returning a value.

**Example:**

```dracula
- run: make test | tee test-output.log
```

If `make test` fails, the `-o pipefail` option causes the whole step to fail. Without `-o pipefail`, the step always runs successfully because the result of the whole pipeline is determined by the last command (`tee test-output.log`), which always returns a zero status.

|   | If `make test` fails, the rest of the pipeline is executed. |
|---|---|

If you want to avoid this behavior, you can specify `set +o pipefail` in the command or override the whole `shell` (see example above).

We recommend using the default options (`-eo pipefail`) because they show errors in intermediate commands and simplify debugging job failures. For convenience, the UI displays the used shell and all active options for each `run` step.

For more information, see the Using Shell Scripts document.

#### *Background commands*

The `background` attribute enables you to configure commands to run in the background. Job execution proceeds to the next step rather than waiting for return of a command with the `background` attribute set to `true`. The following example shows the configuration for running the X virtual framebuffer in the background which is commonly required to run Selenium tests.

**Example:**

```dracula
- run:
    name: Running X virtual framebuffer
    command: Xvfb :99 -screen 0 1280x1024x24
    background: true

- run: make test
```

#### *Shorthand syntax*

`run` has a convenient shorthand syntax.

**Example:**

```dracula
- run: make test

# shorthanded command can also have multiple lines
- run: |
    mkdir -p /tmp/test-results
    make test
```

In this case, `command` and `name` become the string value of `run`, and the rest of the config map for that `run` have their default values.

#### The `when` attribute

By default, CircleCI executes job steps one at a time, in the order you define them in `config.yml`, until a step fails (returns a non-zero exit code). After a command fails, no further job steps execute.

Adding the `when` attribute to a job step allows you to override this default behavior, and selectively run or skip steps depending on the status of the job.

The `when` attribute accepts the following values:

**`on_success`**

The step runs only if all previous steps succeeded (returned exit code 0). `on_success` is the default value.

**`always`**

The step runs regardless of the exit status of previous steps. Use `always` when you have a task that must run whether previous steps succeed or fail. For example, you need to upload logs or code-coverage data.

**`on_fail`**

The step runs only if one of the preceding steps failed (returns a non-zero exit code). Common uses of `on_fail` include storing diagnostic data to debug test failures, or running custom notifications about the failure, such as sending emails or triggering alerts.

|   | Some steps, such as `store_artifacts` and `store_test_results`, always run, even if a **step has failed** (returned a non-zero exit code) previously. However, `store_artifacts`, `store_test_results`, and the `when` attribute are not run if the job has been **killed** by a cancel request or has reached the runtime timeout limit. |
|---|---|

**Example:**

```dracula
- run:
    name: Upload CodeCov.io Data
    command: bash <(curl -s https://codecov.io/bash) -F unittests
    when: always # Uploads code coverage results, pass or fail
```

#### Ending a job from within a `step`

A job can exit without failing by using `run: circleci-agent step halt`. However, if a step within the job is already failing, the job continues to fail. This can be useful in situations where jobs need to conditionally execute.

**Example:** `halt` is used to avoid running a job on the `develop` branch:

```dracula
- run: |
    if [ "$CIRCLE_BRANCH" = "develop" ]; then
        circleci-agent step halt
    fi
```

#### Automatic step reruns

The following attributes can be used to automatically rerun a step if it fails, and delay that rerun if required:

| Key | Required | Type | Description |
|---|---|---|---|
| `max_auto_reruns` | N | Integer | The maximum number of times to automatically rerun the step if it fails. Must be between `1` and `5`. |
| `auto_rerun_delay` | N | String | The delay between reruns of the step if it fails. This delay can only be set along with `max_auto_reruns`. The string is a decimal with unit suffix using either seconds `s` or minutes `m` up to a maximum of 10 minutes, such as "10s", "2m". If you do not supply a delay, the rerun starts directly after the step fails. |

Automatic reruns are only supported for `run` steps, not special steps like `checkout` or `setup_remote_docker`.

You must configure the `command` key for the step, you cannot use the short form run step configuration, for example, the following is not supported for use with automatic reruns: `- run: echo "Hello, world!"`

**Example:**

CircleCI job configured to automatically rerun a step up to 3 times if it fails with a 10 second delay between attempts

```dracula
version: 2.1

jobs:
  my-job:
    steps:
      - run:
          command: echo "Hello, world!"
          max_auto_reruns: 3
          auto_rerun_delay: 10s
```

For more information, see the Automatic Reruns page.

### **The `when` step**

|   | The `when` and `unless` steps are supported in `version: 2.1` configuration |
|---|---|

A conditional step consists of a step with the key `when` or `unless`. Under the `when` key are the subkeys `condition` and `steps`. The purpose of the `when` step is customizing commands and job configuration to run on custom conditions (determined at config-compile time) that are checked before a workflow runs. See the Conditional Steps Section of the Reusable Configuration Reference for more details.

| Key | Required | Type | Description |
|---|---|---|---|
| `condition` | Y | Logic | A Logic Statement |
| `steps` | Y | Sequence | A list of steps to execute when the condition is true |

**Example:**

```dracula
version: 2.1

jobs: # conditional steps may also be defined in `commands:`
  job_with_optional_custom_checkout:
    parameters:
      custom_checkout:
        type: string
        default: ""
    machine:
      image: ubuntu-2004:2024.11.1
    steps:
      - when:
          condition: <<parameters.custom_checkout>>
          steps:
            - run: echo "my custom checkout"
      - unless:
          condition: <<parameters.custom_checkout>>
          steps:
            - checkout
workflows:
  build-test-deploy:
    jobs:
      - job_with_optional_custom_checkout:
          custom_checkout: "any non-empty string is truthy"
      - job_with_optional_custom_checkout
```

### **`checkout`**

A special step used to check out source code to the configured `path` (defaults to the `working_directory`). The reason this is a special step is because it is more of a helper function designed to simplify the process of checking out code. For GitHub OAuth, GitLab, and Bitbucket pipelines, `checkout` configures git to check out over SSH. If you require git over HTTPS, do not use this step as it configures git to check out over SSH. For GitHub App pipelines (GitHub Cloud and GitHub Enterprise Server), `checkout` uses HTTPS.

| Key | Required | Type | Description |
|---|---|---|---|
| `method` | N | String | Checkout method. Valid options include `blobless` and `full`. (default: `blobless`) |
| `path` | N | String | The directory where CircleCI checks out code. CircleCI interprets this relative to the `working_directory` of the job. (default: `.`) |

If `path` already exists and is:

- A git repository - step does not clone whole repository, but rather fetches origin.
- NOT a git repository - step fails.

In the case of `checkout`, the step type is just a string with no additional attributes.

**Example:**

```dracula
jobs:
  build:
    docker:
      - image: cimg/go:1.24.2
    steps:
      - checkout
```

The checkout command automatically adds the required authenticity keys for interacting with GitHub and Bitbucket over SSH. These keys are detailed further in the Integration Guide. This guide is also helpful if you wish to implement a custom checkout command.

You can specify a checkout strategy by using the `method` key. CircleCI supports full clones or blobless clones. Blobless clones reduce the amount of data fetched from the remote by asking the remote to filter out objects that are not attached to the current commit.

**Example:**

```dracula
jobs:
  build:
    docker:
      - image: cimg/go:1.24.2
    steps:
      - checkout:
          method: blobless
```

|   | In certain cases, CircleCI falls back to a full checkout even though blobless was specified. This occurs if Git and SSH clients are not available in the current environment, or if Git version 2.41.0 is installed, which contained a known issue for blobless clones. |
|---|---|

If a downstream step requires those objects to exist for scanning or comparisons, a blobless clone can cause failures. In that case, you can specify a full checkout as shown in the following example:

```dracula
jobs:
  build:
    docker:
      - image: cimg/go:1.24.2
    steps:
      - checkout:
          method: full
```

CircleCI does not check out submodules. If your project requires submodules, add `run` steps with appropriate commands as shown in the following example:

```dracula
jobs:
  build:
    docker:
      - image: cimg/go:1.24.2
    steps:
      - checkout
      - run: git submodule sync
      - run: git submodule update --init
```

|   | The `checkout` step configures Git to skip automatic garbage collection. If you are caching your `.git` directory with **`restore_cache`** and want to use garbage collection to reduce its size, use a **`run`** step with `git gc` before doing so. |
|---|---|

### **`setup_remote_docker`**

|   | `setup_remote_docker` is not compatible with the `machine` executor. See Docker Layer Caching in Machine Executor for information on how to enable DLC with the `machine` executor. The `version` key is not currently supported on CircleCI Server. Contact your system administrator for information about the Docker version installed in your remote Docker environment. If you are on server 4.x, find the Default AWS AMI Lists. |
|---|---|

Allows Docker commands to be run locally. See Running Docker Commands for details.

| Key | Required | Type | Description |
|---|---|---|---|
| `docker_layer_caching` | N | boolean | Set this to `true` to enable Docker Layer Caching in the Remote Docker Environment (default: `false`) |
| `prefer_same_region` | N | boolean | Set this to `true` to attempt pulling images from the same region as the VM on a best-effort basis, falling back to the image’s original region if the pull fails (default: `false`) |
| `version` | N | String | Version string of Docker you would like to use (default: `24.0.9`). View the list of Supported Docker Versions. |

**Example:**

```dracula
jobs:
  build:
    docker:
      - image: cimg/base:2024.06
    steps:
      # ... steps for building/testing app ...
      - setup_remote_docker:
          version: default
```

### **`save_cache`**

Generates and stores a cache of a file or directory of files such as dependencies or source code. Caches are stored in CircleCI’s object storage. Later jobs can restore this cache. Learn more on the Caching Dependencies page.

Cache retention can be customized on the CircleCI web app by navigating to   **Usage Controls**.

| Key | Required | Type | Description |
|---|---|---|---|
| `paths` | Y | List | List of directories to add to the cache |
| `key` | Y | String | Unique identifier for this cache |
| `name` | N | String | Title of the step to be shown in the CircleCI UI (default: "Saving Cache") |
| `when` | N | String | Specify when to enable or disable the step. Takes the following values: `always`, `on_success`, `on_fail` (default: `on_success`) |

The cache for a specific `key` is immutable. If a cache already exists for the given `key`, CircleCI uses the existing cache and proceeds to the next step.

When storing a new cache, the `key` value may contain special, templated, values for your convenience:

| Template | Description |
|---|---|
| `{{ .Branch }}` | The VCS branch currently being built. |
| `{{ .BuildNum }}` | The CircleCI build number for this build. |
| `{{ .Revision }}` | The VCS revision currently being built. |
| `{{ .CheckoutKey }}` | The SSH key used to check out the repository. |
| `{{ .Environment.variableName }}` | The environment variable `variableName` (supports any environment variable Exported by CircleCI or added to a specific context--not any arbitrary environment variable). |
| `{{ checksum "filename" }}` | A base64 encoded SHA256 hash of the given filename’s contents. Commit this file to your repository, and reference it as an absolute or relative path from the current working directory. Good candidates are dependency manifests, such as `package-lock.json`, `pom.xml` or `project.clj`. This file must not change between `restore_cache` and `save_cache`, otherwise CircleCI saves the cache under a different cache key than the one it used at `restore_cache` time. |
| `{{ epoch }}` | The current time in seconds since the UNIX epoch. |
| `{{ arch }}` | The OS and CPU information. Useful when caching compiled binaries that depend on OS and CPU architecture, for example, `darwin amd64` versus `linux i386/32-bit`. |

During step execution, CircleCI replaces the templates above with runtime values and uses the resultant string as the `key`.

**Template examples:**

**`myapp-{{ checksum "package-lock.json" }}`**

CircleCI regenerates the cache every time you change something in the package-lock.json file. Different branches of this project generate the same cache key.

**`myapp-{{ .Branch }}-{{ checksum "package-lock.json" }}`**

Same as the previous one, but each branch generates a separate cache.

**`myapp-{{ epoch }}`**

Every job run generates a separate cache.

While choosing suitable templates for your cache `key`, keep in mind the following:

- Cache saving is not a free operation. See the billing section on the FAQ page.
- It takes time to upload the cache.
- Best practice is to have a `key` that generates a cache only if something actually changed, and avoid regenerating it every time a job is run.
- Because caches are immutable, start all your cache keys with a version prefix `v1-...`. This lets you regenerate all your caches by incrementing the version in this prefix.

**Examples:**

```dracula
- save_cache:
    key: v1-myapp-{{ arch }}-{{ checksum "project.clj" }}
    paths:
      - /home/ubuntu/.m2
```

```dracula
- save_cache:
    key: v1-{{ checksum "yarn.lock" }}
    paths:
      - node_modules/workspace-a
      - node_modules/workspace-c
```

|   | Wildcards are not currently supported in `save_cache` paths. Visit the Ideas board and vote for this feature if it would be useful for you or your organization. |
|---|---|

### **`restore_cache`**

Restores a previously saved cache based on a `key`. Cache needs to have been saved first for this key using the `save_cache` step. Learn more in The Caching Documentation.

| Key | Required | Type | Description |
|---|---|---|---|
| `key` | Y (1) | String | Single cache key to restore |
| `keys` | Y (1) | List | List of cache keys to check. CircleCI restores the cache from the first existing key. |
| `name` | N | String | Title of the step to be shown in the CircleCI UI (default: "Restoring Cache") |

(1) You must specify at least one attribute. If you provide both `key` and `keys`, CircleCI checks `key` first, then `keys`.

A key is searched against existing keys as a prefix.

|   | When multiple matches exist, CircleCI uses the **most recent match**, even if a more precise match exists. |
|---|---|

**Example:**

```dracula
steps:
  - save_cache:
      key: v1-myapp-cache
      paths:
        - ~/d1

  - save_cache:
      key: v1-myapp-cache-new
      paths:
        - ~/d2

  - run: rm -f ~/d1 ~/d2

  - restore_cache:
      key: v1-myapp-cache
```

In this case, CircleCI restores cache `v1-myapp-cache-new` because this is the most recent match with the `v1-myapp-cache` prefix, even though the first key (`v1-myapp-cache`) is an exact match.

For more information on key formatting, see the `key` section of `save_cache` step.

When CircleCI encounters a list of `keys`, it restores the cache from the first key that matches an existing cache. We recommend you use a more specific key first (for example, cache for exact version of `package-lock.json`) and more generic keys after (for example, any cache for this project). If no key matches an existing cache, CircleCI skips the step with a warning.

A path does not need to be specified here because CircleCI restores the cache to the location where it originally saved it.

**Example:**

```dracula
- restore_cache:
    keys:
      - v1-myapp-{{ arch }}-{{ checksum "project.clj" }}
      # if cache for exact version of `project.clj` is not present then load any most recent one
      - v1-myapp-

# ... Steps building and testing your application ...

# cache will be saved only once for each version of `project.clj`
- save_cache:
    key: v1-myapp-{{ arch }}-{{ checksum "project.clj" }}
    paths:
      - /foo
```

### **`deploy` - DEPRECATED**

See **`run`** for current processes. If you have parallelism `> 1` in your job, see the Migrate From Deploy to Run guide.

### **`store_artifacts`**

Step to store artifacts (for example logs, binaries, etc.) to be available in the web app or through the API. See the Uploading Artifacts page for more information.

| Key | Required | Type | Description |
|---|---|---|---|
| `path` | Y | String | Directory in the primary container to save as job artifacts |
| `destination` | N | String | Prefix added to the artifact paths in the artifacts API (default: the directory of the file specified in `path`) |

There can be multiple `store_artifacts` steps in a job. Using a unique prefix for each step prevents them from overwriting files.

Artifact storage retention can be customized on the CircleCI web app by navigating to   **Usage Controls**.

**Example:**

```dracula
- run:
    name: Build the Jekyll site
    command: bundle exec jekyll build --source jekyll --destination jekyll/_site/docs/
- store_artifacts:
    path: jekyll/_site/docs/
    destination: circleci-docs
```

### **`store_test_results`**

Special step used to upload and store test results for a build. Test results are visible on the CircleCI web application under each build’s **Test Summary** section. Storing test results is useful for timing analysis of your test suites. For more information on storing test results, see the Collecting Test Data page.

You can also store test results as build artifacts. For steps, refer to the `store_artifacts` step section.

| Key | Required | Type | Description |
|---|---|---|---|
| `path` | Y | String | Path (absolute, or relative to your `working_directory`) to directory containing `JUnit` XML test metadata files, or to a single test file. |

**Example:**

Directory structure:

```dracula
test-results
├── jest
│   └── results.xml
├── mocha
│   └── results.xml
└── rspec
    └── results.xml
```

`config.yml` syntax:

```dracula
- store_test_results:
    path: test-results
```

### **`persist_to_workspace`**

Special step used to persist a temporary file to be used by another job in the workflow. For more information on using workspaces, see the Using Workspaces to Share Data Between Jobs page.

`persist_to_workspace` adopts the storage settings from the storage customization controls on the CircleCI web app. If no custom setting is provided, `persist_to_workspace` defaults to 15 days.

Workspace storage retention can be customized on the CircleCI web app by navigating to   **Usage Controls**.

| Key | Required | Type | Description |
|---|---|---|---|
| `root` | Y | String | Either an absolute path or a path relative to `working_directory` |
| `paths` | Y | List | Glob identifying file(s), or a non-glob path to a directory to add to the shared workspace. Interpreted as relative to the workspace root. Must not be the workspace root itself. |

The root key is a directory on the container which is taken to be the root directory of the workspace. The path values are all relative to the root.

**Example for root Key:**

For example, the following step syntax persists the specified paths from `/tmp/dir` into the workspace, relative to the directory `/tmp/dir`.

```dracula
- persist_to_workspace:
    root: /tmp/dir
    paths:
      - foo/bar
      - baz
```

After this step completes, the following directories are added to the workspace:

```
/tmp/dir/foo/bar
/tmp/dir/baz
```

**Example for paths Key:**

```dracula
- persist_to_workspace:
    root: /tmp/workspace
    paths:
      - target/application.jar
      - build/*
```

The `paths` list uses `Glob` from Go, and the pattern matches filepath.Match.

```dracula
pattern:
        { term }
term:
        '*' matches any sequence of non-Separator characters
        '?' matches any single non-Separator character
        '[' [ '^' ] { character-range }
        ']' character class (must be non-empty)
        c matches character c (c != '*', '?', '\\', '[')
        '\\' c matches character c
character-range:
        c matches character c (c != '\\', '-', ']')
        '\\' c matches character c
        lo '-' hi matches character c for lo <= c <= hi
```

The Go documentation states that the pattern may describe hierarchical names such as `/usr/*/bin/ed` (assuming the Separator is '/').

|   | Everything must be relative to the workspace root directory. |
|---|---|

### **`attach_workspace`**

Special step used to attach the workflow’s workspace to the current container. The full contents of the workspace are downloaded and copied into the directory the workspace is being attached at. For more information on using workspaces, see the Using Workspaces page.

| Key | Required | Type | Description |
|---|---|---|---|
| `at` | Y | String | Directory to attach the workspace to. |

Workspace storage retention can be customized on the CircleCI web app by navigating to   **Usage Controls**.

**Example:**

```dracula
- attach_workspace:
    at: /tmp/workspace
```

|   | The lifetime of artifacts, workspaces, and caches can be customized on the CircleCI web app by navigating to   **Usage Controls**. Here you can control the storage retention periods for these objects. If no storage period is set, the default storage retention period of artifacts is 30 days, while the default storage retention period of workspaces and caches is 15 days. |
|---|---|

### **`add_ssh_keys`**

Special step that adds SSH keys from a project’s settings to a container. Also configures SSH to use these keys. For more information on SSH keys see the Add Additional SSH Keys page.

|   | **Using server?** CircleCI Server supports only MD5 fingerprints. You can see the MD5 fingerprint in CircleCI under   **SSH keys**  **Additional SSH keys**. An upcoming server release is planned to include SHA256 support. |
|---|---|

| Key | Required | Type | Description |
|---|---|---|---|
| `fingerprints` | N | List | List of fingerprints corresponding to the keys to be added (default: all keys added) |

```dracula
steps:
  - add_ssh_keys:
      fingerprints:
        - "b7:35:a6:4e:9b:0d:6d:d4:78:1e:9a:97:2a:66:6b:be"
        - "SHA256:NPj4IcXxqQEKGXOghi/QbG2sohoNfvZ30JwCcdSSNM0"
```

|   | Even though CircleCI uses `ssh-agent` to sign all added SSH keys, you **must** use the `add_ssh_keys` key to actually add keys to a container. |
|---|---|

### Using `pipeline` values

Pipeline values are available to all pipeline configurations and can be used without previous declaration. For a list of pipeline values, see the Pipeline Values and Parameters page.

**Example:**

```dracula
version: 2.1
jobs:
  build:
    docker:
      - image: cimg/node:20.18.1
    environment:
      IMAGETAG: latest
    working_directory: ~/main
    steps:
      - run: echo "This is pipeline ID << pipeline.id >>"
```


## **`circleci_ip_ranges`**

|   | A paid account on a Performance or Scale Plan is required to access IP ranges. |
|---|---|

Enables jobs to go through a set of well-defined IP address ranges. See IP Ranges for details.

**Example:**

```dracula
version: 2.1

jobs:
  build:
    circleci_ip_ranges: true # opts the job into the IP ranges feature
    docker:
      - image: curlimages/curl
    steps:
      - run: echo “Hello World”
workflows:
  build-workflow:
    jobs:
      - build
```


## **`job-groups`**

The `job-groups` key lets you define named sets of jobs at the top level of your config. A job group can be invoked in a workflow just like a regular job, and optionally serialized as an atomic unit by adding `serial-group` to the invocation.

### **<`group-name`>**

Each job group consists of the group’s name as a key and a map as a value. The value map has the following attributes:

| Key | Required | Type | Description |
|---|---|---|---|
| `jobs` | Y | List | A list of job invocations for the group, following the same format as workflow job entries. Jobs within the group can use `requires` to declare internal dependencies on other jobs in the same group. |

**Example:**

```dracula
# Use job-groups to define a reusable set of jobs.
# The group is expanded inline in the workflow without serialization.

job-groups:
  deploy-and-release:
    jobs:
      - deploy
      - release:
          requires:
            - deploy

workflows:
  main-workflow:
    jobs:
      - build
      - deploy-and-release:
          requires:
            - build
      - notify:
          requires:
            - deploy-and-release
```

For more information, see the Job Groups section of the Controlling Serial Execution Across Your Organization page.


## **`workflows`**

Used for orchestrating all jobs. Each workflow consists of the workflow name as a key and a map as a value. A name must be unique within the current `config.yml`. The top-level keys for the Workflows configuration are `version` and `jobs`. For more information, see the Using Workflows to Orchestrate Jobs page.

### **`version`**

|   | The workflows `version` key is **not** required for `version: 2.1` configuration |
|---|---|

The Workflows `version` field is used to issue warnings for deprecation or breaking changes.

| Key | Required | Type | Description |
|---|---|---|---|
| `version` | Y if config version is `2` | String | Must be `2` |

```dracula
workflows:
  version: 2
  my-workflow:
    jobs:
      - my-job
```

### **<`workflow_name`>**

A unique name for your workflow.

```dracula
workflows:
  my-workflow:
    jobs:
      - my-job
```

### **`max_auto_reruns`**

The `max_auto_reruns` key is used to configure the maximum number of automatic reruns for a workflow.

```dracula
version: 2.1

workflows:
  my-workflow:
    max_auto_reruns: 3
    jobs:
      - build
      - test
      - deploy:
          requires:
            - build
            - test
```

The value of `max_auto_reruns` can be an integer between 1 and 5.

For more information, see the Automatic Reruns page.

### **`triggers`**

Specifies which triggers will cause this workflow to be executed. Default behavior is to trigger the workflow when pushing to a branch.

| Key | Required | Type | Description |
|---|---|---|---|
| `triggers` | N | Array | Must be `schedule`. |

```dracula
workflows:
   nightly:
     triggers:
       - schedule:
           cron: "0 0 * * *"
           filters:
             branches:
               only:
                 - main
                 - beta
     jobs:
       - test
```

#### **`schedule`**

|   | Scheduled workflows are not available for projects integrated through the GitHub App, GitLab or Bitbucket Data Center. |
|---|---|

|   | Using **schedule triggers** rather than scheduled workflows offers several benefits. Visit the schedule triggers Migration Guide to find out how to migrate existing scheduled workflows to schedule triggers. If you would like to set up schedule triggers from scratch, visit the Schedule Triggers page. |
|---|---|

A workflow may have a `schedule` indicating it runs at a certain time, for example a nightly build that runs every day at 12am UTC:

```dracula
workflows:
   nightly:
     triggers:
       - schedule:
           cron: "0 0 * * *"
           filters:
             branches:
               only:
                 - main
                 - beta
     jobs:
       - test
```

#### **`cron`**

The `cron` key is defined using POSIX `crontab` syntax.

| Key | Required | Type | Description |
|---|---|---|---|
| `cron` | Y | String | See the `crontab` man page. |

```dracula
workflows:
   nightly:
     triggers:
       - schedule:
           cron: "0 0 * * *"
           filters:
             branches:
               only:
                 - main
                 - beta
     jobs:
       - test
```

#### **`filters`**

Trigger filters can have the key `branches`.

| Key | Required | Type | Description |
|---|---|---|---|
| `filters` | Y | Map | A map defining rules for execution on specific branches |

```dracula
workflows:
   nightly:
     triggers:
       - schedule:
           cron: "0 0 * * *"
           filters:
             branches:
               only:
                 - main
                 - beta
     jobs:
       - test
```

#### **`branches`**

The `branches` key controls whether the *current* branch has a schedule trigger created for it, where *current* branch is the branch containing the `config.yml` file with the `trigger` stanza. That is, a push on the `main` branch only schedules a workflow using Filters in Your Workflows for the `main` branch.

Branches can have the keys `only` and `ignore` which each map to a single string naming a branch. You may also use regular expressions to match against branches by enclosing them with `/’s, or map to a list of such strings. Regular expressions must match the **entire** string.

- The job runs on any branches that match `only`.
- The job does not run on any branches that match `ignore`.
- If you specify neither `only` nor `ignore`, the job runs on all branches. If you specify both `only` and `ignore`, CircleCI uses `only` and ignores `ignore`.

```dracula
workflows:
  commit:
    jobs:
      - test
      - deploy
  nightly:
    triggers:
      - schedule:
          cron: "0 0 * * *"
          filters:
            branches:
              only:
                - main
                - /^release\/.*/
    jobs:
      - coverage
```

| Key | Required | Type | Description |
|---|---|---|---|
| `branches` | Y | Map | A map defining rules for execution on specific branches |
| `only` 1 | N | String, or List of Strings | Either a single branch specifier, or a list of branch specifiers |
| `ignore` 1 | N | String, or List of Strings | Either a single branch specifier, or a list of branch specifiers |

1: One of either `only` or `ignore` branch filters must be specified. If both are present, `only` is used.

#### **Using `when` in workflows**

|   | Using `when` or `unless` under `workflows` is supported in `version: 2.1` configuration. Workflows are always run unless there is a `when` or `unless` filter that prevents the workflow from being run. If you want a workflow to run in every pipeline, do not add a `when` or `unless` filter. |
|---|---|

You may use a `when` clause (the inverse clause `unless` is also supported) under a workflow declaration with a logic statement to determine whether or not to run that workflow.

The example configuration below uses a pipeline parameter, `run_integration_tests` to drive the `integration_tests` workflow.

```dracula
version: 2.1

workflows:
  integration_tests:
    when: pipeline.git.branch == "main"
    jobs:
      - mytestjob

jobs:
...
```

This example prevents the workflow `integration_tests` from running unless the pipeline is triggered on the `main` branch.

Refer to the Workflows for more examples and conceptual information.
