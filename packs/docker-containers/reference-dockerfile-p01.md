---
title: "Dockerfile reference (part 1/3)"
source: https://docs.docker.com/reference/dockerfile/
domain: docker-containers
license: Apache-2.0
tags: docker, container, dockerfile, kubernetes, docker compose
fetched: 2026-07-02
part: 1/3
---

# Dockerfile reference

Table of contents

Docker can build images automatically by reading the instructions from a Dockerfile. A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. This page describes the commands you can use in a Dockerfile.


## Overview

The Dockerfile supports the following instructions:

| Instruction | Description |
|---|---|
| `ADD` | Add local or remote files and directories. |
| `ARG` | Use build-time variables. |
| `CMD` | Specify default commands. |
| `COPY` | Copy files and directories. |
| `ENTRYPOINT` | Specify default executable. |
| `ENV` | Set environment variables. |
| `EXPOSE` | Describe which ports your application is listening on. |
| `FROM` | Create a new build stage from a base image. |
| `HEALTHCHECK` | Check a container's health on startup. |
| `LABEL` | Add metadata to an image. |
| `MAINTAINER` | Specify the author of an image. |
| `ONBUILD` | Specify instructions for when the image is used in a build. |
| `RUN` | Execute build commands. |
| `SHELL` | Set the default shell of an image. |
| `STOPSIGNAL` | Specify the system call signal for exiting a container. |
| `USER` | Set user and group ID. |
| `VOLUME` | Create volume mounts. |
| `WORKDIR` | Change working directory. |


## Format

Here is the format of the Dockerfile:

```dockerfile
# Comment
INSTRUCTION arguments
```

The instruction is not case-sensitive. However, convention is for them to be UPPERCASE to distinguish them from arguments more easily.

Docker runs instructions in a Dockerfile in order. A Dockerfile **must begin with a `FROM` instruction**. This may be after parser directives, comments, and globally scoped ARGs. The `FROM` instruction specifies the base image from which you are building. `FROM` may only be preceded by one or more `ARG` instructions, which declare arguments that are used in `FROM` lines in the Dockerfile.

BuildKit treats lines that begin with `#` as a comment, unless the line is a valid parser directive. A `#` marker anywhere else in a line is treated as an argument. This allows statements like:

```dockerfile
# Comment
RUN echo 'we are running some # of cool things'
```

Comment lines are removed before the Dockerfile instructions are executed. The comment in the following example is removed before the shell executes the `echo` command.

```dockerfile
RUN echo hello \
# comment
world
```

The following examples is equivalent.

```dockerfile
RUN echo hello \
world
```

Comments don't support line continuation characters.

> Note
> 
> **Note on whitespace**
> 
> For backward compatibility, leading whitespace before comments (`#`) and instructions (such as `RUN`) are ignored, but discouraged. Leading whitespace is not preserved in these cases, and the following examples are therefore equivalent:
> 
> ```dockerfile
>         # this is a comment-line
>     RUN echo hello
> RUN echo world
> ```
> 
> ```dockerfile
> # this is a comment-line
> RUN echo hello
> RUN echo world
> ```
> 
> Whitespace in instruction arguments, however, isn't ignored. The following example prints `hello world` with leading whitespace as specified:
> 
> ```dockerfile
> RUN echo "\
>      hello\
>      world"
> ```


## Parser directives

Parser directives are optional, and affect the way in which subsequent lines in a Dockerfile are handled. Parser directives don't add layers to the build, and don't show up as build steps. Parser directives are written as a special type of comment in the form `# directive=value`. A single directive may only be used once.

The following parser directives are supported:

- `syntax`
- `escape`
- `check` (since Dockerfile v1.8.0)

Once a comment, empty line or builder instruction has been processed, BuildKit no longer looks for parser directives. Instead it treats anything formatted as a parser directive as a comment and doesn't attempt to validate if it might be a parser directive. Therefore, all parser directives must be at the top of a Dockerfile.

Parser directive keys, such as `syntax` or `check`, aren't case-sensitive, but they're lowercase by convention. Values for a directive are case-sensitive and must be written in the appropriate case for the directive. For example, `#check=skip=jsonargsrecommended` is invalid because the check name must use Pascal case, not lowercase. It's also conventional to include a blank line following any parser directives. Line continuation characters aren't supported in parser directives.

Due to these rules, the following examples are all invalid:

Invalid due to line continuation:

```dockerfile
# direc \
tive=value
```

Invalid due to appearing twice:

```dockerfile
# directive=value1
# directive=value2

FROM ImageName
```

Treated as a comment because it appears after a builder instruction:

```dockerfile
FROM ImageName
# directive=value
```

Treated as a comment because it appears after a comment that isn't a parser directive:

```dockerfile
# About my dockerfile
# directive=value
FROM ImageName
```

The following `unknowndirective` is treated as a comment because it isn't recognized. The known `syntax` directive is treated as a comment because it appears after a comment that isn't a parser directive.

```dockerfile
# unknowndirective=value
# syntax=value
```

Non line-breaking whitespace is permitted in a parser directive. Hence, the following lines are all treated identically:

```dockerfile
#directive=value
# directive =value
#	directive= value
# directive = value
#	  dIrEcTiVe=value
```

### syntax

Use the `syntax` parser directive to declare the Dockerfile syntax version to use for the build. If unspecified, BuildKit uses a bundled version of the Dockerfile frontend. Declaring a syntax version lets you automatically use the latest Dockerfile version without having to upgrade BuildKit or Docker Engine, or even use a custom Dockerfile implementation.

Most users will want to set this parser directive to `docker/dockerfile:1`, which causes BuildKit to pull the latest stable version of the Dockerfile syntax before the build.

```dockerfile
# syntax=docker/dockerfile:1
```

For more information about how the parser directive works, see Custom Dockerfile syntax.

### escape

```dockerfile
# escape=\
```

Or

```dockerfile
# escape=`
```

The `escape` directive sets the character used to escape characters in a Dockerfile. If not specified, the default escape character is `\`.

The escape character is used both to escape characters in a line, and to escape a newline. This allows a Dockerfile instruction to span multiple lines. Note that regardless of whether the `escape` parser directive is included in a Dockerfile, escaping is not performed in a `RUN` command, except at the end of a line.

Setting the escape character to ` is especially useful on `Windows`, where `\` is the directory path separator. ` is consistent with Windows PowerShell.

Consider the following example which would fail in a non-obvious way on Windows. The second `\` at the end of the second line would be interpreted as an escape for the newline, instead of a target of the escape from the first `\`. Similarly, the `\` at the end of the third line would, assuming it was actually handled as an instruction, cause it be treated as a line continuation. The result of this Dockerfile is that second and third lines are considered a single instruction:

```dockerfile
FROM microsoft/nanoserver
COPY testfile.txt c:\\
RUN dir c:\
```

Results in:

```console
PS E:\myproject> docker build -t cmd .

Sending build context to Docker daemon 3.072 kB
Step 1/2 : FROM microsoft/nanoserver
 ---> 22738ff49c6d
Step 2/2 : COPY testfile.txt c:\RUN dir c:
GetFileAttributesEx c:RUN: The system cannot find the file specified.
PS E:\myproject>
```

One solution to the above would be to use `/` as the target of both the `COPY` instruction, and `dir`. However, this syntax is, at best, confusing as it is not natural for paths on Windows, and at worst, error prone as not all commands on Windows support `/` as the path separator.

By adding the `escape` parser directive, the following Dockerfile succeeds as expected with the use of natural platform semantics for file paths on Windows:

```dockerfile
# escape=`

FROM microsoft/nanoserver
COPY testfile.txt c:\
RUN dir c:\
```

Results in:

```console
PS E:\myproject> docker build -t succeeds --no-cache=true .

Sending build context to Docker daemon 3.072 kB
Step 1/3 : FROM microsoft/nanoserver
 ---> 22738ff49c6d
Step 2/3 : COPY testfile.txt c:\
 ---> 96655de338de
Removing intermediate container 4db9acbb1682
Step 3/3 : RUN dir c:\
 ---> Running in a2c157f842f5
 Volume in drive C has no label.
 Volume Serial Number is 7E6D-E0F7

 Directory of c:\

10/05/2016  05:04 PM             1,894 License.txt
10/05/2016  02:22 PM    <DIR>          Program Files
10/05/2016  02:14 PM    <DIR>          Program Files (x86)
10/28/2016  11:18 AM                62 testfile.txt
10/28/2016  11:20 AM    <DIR>          Users
10/28/2016  11:20 AM    <DIR>          Windows
           2 File(s)          1,956 bytes
           4 Dir(s)  21,259,096,064 bytes free
 ---> 01c7f3bef04f
Removing intermediate container a2c157f842f5
Successfully built 01c7f3bef04f
PS E:\myproject>
```

### check

```dockerfile
# check=skip=<checks|all>
# check=error=<boolean>
```

The `check` directive is used to configure how build checks are evaluated. By default, all checks are run, and failures are treated as warnings.

You can disable specific checks using `#check=skip=<check-name>`. To specify multiple checks to skip, separate them with a comma:

```dockerfile
# check=skip=JSONArgsRecommended,StageNameCasing
```

To disable all checks, use `#check=skip=all`.

By default, builds with failing build checks exit with a zero status code despite warnings. To make the build fail on warnings, set `#check=error=true`.

```dockerfile
# check=error=true
```

> Note
> 
> When using the `check` directive, with `error=true` option, it is recommended to pin the Dockerfile syntax to a specific version. Otherwise, your build may start to fail when new checks are added in the future versions.

To combine both the `skip` and `error` options, use a semi-colon to separate them:

```dockerfile
# check=skip=JSONArgsRecommended;error=true
```

To see all available checks, see the build checks reference. Note that the checks available depend on the Dockerfile syntax version. To make sure you're getting the most up-to-date checks, use the `syntax` directive to specify the Dockerfile syntax version to the latest stable version.


## Environment replacement

Environment variables (declared with the `ENV` statement) can also be used in certain instructions as variables to be interpreted by the Dockerfile. Escapes are also handled for including variable-like syntax into a statement literally.

Environment variables are notated in the Dockerfile either with `$variable_name` or `${variable_name}`. They are treated equivalently and the brace syntax is typically used to address issues with variable names with no whitespace, like `${foo}_bar`.

The `${variable_name}` syntax also supports a few of the standard `bash` modifiers as specified below:

- `${variable:-word}` indicates that if `variable` is set and non-empty then the result will be that value. If `variable` is unset or empty then `word` will be the result.
- `${variable-word}` indicates that if `variable` is set (even if empty) then the result will be that value. If `variable` is unset then `word` will be the result.
- `${variable:+word}` indicates that if `variable` is set and non-empty then `word` will be the result, otherwise the result is the empty string.
- `${variable+word}` indicates that if `variable` is set (even if empty) then `word` will be the result, otherwise the result is the empty string.

The following variable replacements are supported in a pre-release version of Dockerfile syntax, when using the `# syntax=docker/dockerfile-upstream:master` syntax directive in your Dockerfile:

- `${variable#pattern}` removes the shortest match of `pattern` from `variable`, seeking from the start of the string.`str=foobarbaz echo ${str#f*b} # arbaz`
- `${variable##pattern}` removes the longest match of `pattern` from `variable`, seeking from the start of the string.`str=foobarbaz echo ${str##f*b} # az`
- `${variable%pattern}` removes the shortest match of `pattern` from `variable`, seeking backwards from the end of the string.`string=foobarbaz echo ${string%b*} # foobar`
- `${variable%%pattern}` removes the longest match of `pattern` from `variable`, seeking backwards from the end of the string.`string=foobarbaz echo ${string%%b*} # foo`
- `${variable/pattern/replacement}` replace the first occurrence of `pattern` in `variable` with `replacement``string=foobarbaz echo ${string/ba/fo} # fooforbaz`
- `${variable//pattern/replacement}` replaces all occurrences of `pattern` in `variable` with `replacement``string=foobarbaz echo ${string//ba/fo} # fooforfoz`

In all cases, `word` can be any string, including additional environment variables.

`pattern` is a glob pattern where `?` matches any single character and `*` any number of characters (including zero). To match literal `?` and `*`, use a backslash escape: `\?` and `\*`.

You can escape whole variable names by adding a `\` before the variable: `\$foo` or `\${foo}`, for example, will translate to `$foo` and `${foo}` literals respectively.

Example (parsed representation is displayed after the `#`):

```dockerfile
FROM busybox
ENV FOO=/bar
WORKDIR ${FOO}   # WORKDIR /bar
ADD . $FOO       # ADD . /bar
COPY \$FOO /quux # COPY $FOO /quux
```

Environment variables are supported by the following list of instructions in the Dockerfile:

- `ADD`
- `COPY`
- `ENV`
- `EXPOSE`
- `FROM`
- `LABEL`
- `STOPSIGNAL`
- `USER`
- `VOLUME`
- `WORKDIR`
- `ONBUILD` (when combined with one of the supported instructions above)

You can also use environment variables with `RUN`, `CMD`, and `ENTRYPOINT` instructions, but in those cases the variable substitution is handled by the command shell, not the builder. Note that instructions using the exec form don't invoke a command shell automatically. See Variable substitution.

Environment variable substitution use the same value for each variable throughout the entire instruction. Changing the value of a variable only takes effect in subsequent instructions. Consider the following example:

```dockerfile
ENV abc=hello
ENV abc=bye def=$abc
ENV ghi=$abc
```

- The value of `def` becomes `hello`
- The value of `ghi` becomes `bye`


## .dockerignore file

You can use `.dockerignore` file to exclude files and directories from the build context. For more information, see .dockerignore file.


## Shell and exec form

The `RUN`, `CMD`, and `ENTRYPOINT` instructions all have two possible forms:

- `INSTRUCTION ["executable","param1","param2"]` (exec form)
- `INSTRUCTION command param1 param2` (shell form)

The exec form makes it possible to avoid shell string munging, and to invoke commands using a specific command shell, or any other executable. It uses a JSON array syntax, where each element in the array is a command, flag, or argument.

The shell form is more relaxed, and emphasizes ease of use, flexibility, and readability. The shell form automatically uses a command shell, whereas the exec form does not.

### Exec form

The exec form is parsed as a JSON array, which means that you must use double-quotes (") around words, not single-quotes (').

```dockerfile
ENTRYPOINT ["/bin/bash", "-c", "echo hello"]
```

The exec form is best used to specify an `ENTRYPOINT` instruction, combined with `CMD` for setting default arguments that can be overridden at runtime. For more information, see ENTRYPOINT.

#### Variable substitution

Using the exec form doesn't automatically invoke a command shell. This means that normal shell processing, such as variable substitution, doesn't happen. For example, `RUN [ "echo", "$HOME" ]` won't handle variable substitution for `$HOME`.

If you want shell processing then either use the shell form or execute a shell directly with the exec form, for example: `RUN [ "sh", "-c", "echo $HOME" ]`. When using the exec form and executing a shell directly, as in the case for the shell form, it's the shell that's doing the environment variable substitution, not the builder.

#### Backslashes

In exec form, you must escape backslashes. This is particularly relevant on Windows where the backslash is the path separator. The following line would otherwise be treated as shell form due to not being valid JSON, and fail in an unexpected way:

```dockerfile
RUN ["c:\windows\system32\tasklist.exe"]
```

The correct syntax for this example is:

```dockerfile
RUN ["c:\\windows\\system32\\tasklist.exe"]
```

### Shell form

Unlike the exec form, instructions using the shell form always use a command shell. The shell form doesn't use the JSON array format, instead it's a regular string. The shell form string lets you escape newlines using the escape character (backslash by default) to continue a single instruction onto the next line. This makes it easier to use with longer commands, because it lets you split them up into multiple lines. For example, consider these two lines:

```dockerfile
RUN source $HOME/.bashrc && \
echo $HOME
```

They're equivalent to the following line:

```dockerfile
RUN source $HOME/.bashrc && echo $HOME
```

You can also use heredocs with the shell form to break up supported commands.

```dockerfile
RUN <<EOF
  source $HOME/.bashrc
  echo $HOME
EOF
```

For more information about heredocs, see Here-documents.

### Use a different shell

You can change the default shell using the `SHELL` command. For example:

```dockerfile
SHELL ["/bin/bash", "-c"]
RUN echo hello
```

For more information, see SHELL.


## FROM

```dockerfile
FROM [--platform=<platform>] <image> [AS <name>]
```

Or

```dockerfile
FROM [--platform=<platform>] <image>[:<tag>] [AS <name>]
```

Or

```dockerfile
FROM [--platform=<platform>] <image>[@<digest>] [AS <name>]
```

The `FROM` instruction initializes a new build stage and sets the base image for subsequent instructions. As such, a valid Dockerfile must start with a `FROM` instruction. The image can be any valid image.

- `ARG` is the only instruction that may precede `FROM` in the Dockerfile. See Understand how ARG and FROM interact.
- `FROM` can appear multiple times within a single Dockerfile to create multiple images or use one build stage as a dependency for another. Simply make a note of the last image ID output by the commit before each new `FROM` instruction. Each `FROM` instruction clears any state created by previous instructions.
- Optionally a name can be given to a new build stage by adding `AS name` to the `FROM` instruction. The name can be used in subsequent `FROM <name>`, `COPY --from=<name>`, and `RUN --mount=type=bind,from=<name>` instructions to refer to the image built in this stage.Using a previous build stage as the base for a subsequent stage is a common pattern for sharing a common base environment:`FROM ubuntu AS base RUN apt-get update && apt-get install -y shared-tooling FROM base AS dev RUN apt-get install -y dev-tooling FROM base AS prod COPY --from=build /app /app`
- The `tag` or `digest` values are optional. If you omit either of them, the builder assumes a `latest` tag by default. The builder returns an error if it can't find the `tag` value.

The optional `--platform` flag can be used to specify the platform of the image in case `FROM` references a multi-platform image. For example, `linux/amd64`, `linux/arm64`, or `windows/amd64`. By default, the target platform of the build request is used. Global build arguments can be used in the value of this flag, for example automatic platform ARGs allow you to force a stage to native build platform (`--platform=$BUILDPLATFORM`), and use it to cross-compile to the target platform inside the stage.

### Understand how ARG and FROM interact

`FROM` instructions support variables that are declared by any `ARG` instructions that occur before the first `FROM`.

```dockerfile
ARG  CODE_VERSION=latest
FROM base:${CODE_VERSION}
CMD  /code/run-app

FROM extras:${CODE_VERSION}
CMD  /code/run-extras
```

An `ARG` declared before a `FROM` is outside of a build stage, so it can't be used in any instruction after a `FROM`. To use the default value of an `ARG` declared before the first `FROM` use an `ARG` instruction without a value inside of a build stage:

```dockerfile
ARG VERSION=latest
FROM busybox:$VERSION
ARG VERSION
RUN echo $VERSION > image_version
```


## RUN

The `RUN` instruction will execute any commands to create a new layer on top of the current image. The added layer is used in the next step in the Dockerfile. `RUN` has two forms:

```dockerfile
# Shell form:
RUN [OPTIONS] <command> ...
# Exec form:
RUN [OPTIONS] [ "<command>", ... ]
```

For more information about the differences between these two forms, see shell or exec forms.

The shell form is most commonly used, and lets you break up longer instructions into multiple lines, either using newline escapes, or with heredocs:

```dockerfile
RUN <<EOF
apt-get update
apt-get install -y curl
EOF
```

The available `[OPTIONS]` for the `RUN` instruction are:

| Option | Minimum Dockerfile version |
|---|---|
| `--device` | 1.14-labs |
| `--mount` | 1.2 |
| `--network` | 1.3 |
| `--security` | 1.20 |

### Cache invalidation for RUN instructions

The cache for `RUN` instructions isn't invalidated automatically during the next build. The cache for an instruction like `RUN apt-get dist-upgrade -y` will be reused during the next build. The cache for `RUN` instructions can be invalidated by using the `--no-cache` flag, for example `docker build --no-cache`.

See the Dockerfile Best Practices guide for more information.

The cache for `RUN` instructions can be invalidated by `ADD` and `COPY` instructions.

### RUN --device

> Note
> 
> Not yet available in stable syntax, use `docker/dockerfile:1-labs` version. It also needs BuildKit 0.20.0 or later.

```dockerfile
RUN --device=name,[required]
```

`RUN --device` allows build to request CDI devices to be available to the build step.

> Warning
> 
> The use of `--device` is protected by the `device` entitlement, which needs to be enabled when starting the buildkitd daemon with `--allow-insecure-entitlement device` flag or in buildkitd config, and for a build request with `--allow device` flag.

The device `name` is provided by the CDI specification registered in BuildKit.

In the following example, multiple devices are registered in the CDI specification for the `vendor1.com/device` vendor.

```yaml
cdiVersion: "0.6.0"
kind: "vendor1.com/device"
devices:
  - name: foo
    containerEdits:
      env:
        - FOO=injected
  - name: bar
    annotations:
      org.mobyproject.buildkit.device.class: class1
    containerEdits:
      env:
        - BAR=injected
  - name: baz
    annotations:
      org.mobyproject.buildkit.device.class: class1
    containerEdits:
      env:
        - BAZ=injected
  - name: qux
    annotations:
      org.mobyproject.buildkit.device.class: class2
    containerEdits:
      env:
        - QUX=injected
annotations:
  org.mobyproject.buildkit.device.autoallow: true
```

The device name format is flexible and accepts various patterns to support multiple device configurations:

- `vendor1.com/device`: request the first device found for this vendor
- `vendor1.com/device=foo`: request a specific device
- `vendor1.com/device=*`: request all devices for this vendor
- `class1`: request devices by `org.mobyproject.buildkit.device.class` annotation

> Note
> 
> Annotations are supported by the CDI specification since 0.6.0.

> Note
> 
> To automatically allow all devices registered in the CDI specification, you can set the `org.mobyproject.buildkit.device.autoallow` annotation. You can also set this annotation for a specific device.

#### Example: CUDA-Powered LLaMA Inference

In this example we use the `--device` flag to run `llama.cpp` inference using an NVIDIA GPU device through CDI:

```dockerfile
# syntax=docker/dockerfile:1-labs

FROM scratch AS model
ADD https://huggingface.co/bartowski/Llama-3.2-1B-Instruct-GGUF/resolve/main/Llama-3.2-1B-Instruct-Q4_K_M.gguf /model.gguf

FROM scratch AS prompt
COPY <<EOF prompt.txt
Q: Generate  a list of 10 unique biggest countries by population in JSON with their estimated poulation in 1900 and 2024. Answer only newline formatted JSON with keys "country", "population_1900", "population_2024" with 10 items.
A:
[
    {

EOF

FROM ghcr.io/ggml-org/llama.cpp:full-cuda-b5124
RUN --device=nvidia.com/gpu=all \
    --mount=from=model,target=/models \
    --mount=from=prompt,target=/tmp \
    ./llama-cli -m /models/model.gguf -no-cnv -ngl 99 -f /tmp/prompt.txt
```

### RUN --mount

```dockerfile
RUN --mount=[type=<TYPE>][,option=<value>[,option=<value>]...]
```

`RUN --mount` allows you to create filesystem mounts that the build can access. This can be used to:

- Create bind mount to the host filesystem or other build stages
- Access build secrets or ssh-agent sockets
- Use a persistent package management cache to speed up your build

The supported mount types are:

| Type | Description |
|---|---|
| `bind` (default) | Bind-mount context directories (read-only). |
| `cache` | Mount a temporary directory to cache directories for compilers and package managers. |
| `tmpfs` | Mount a `tmpfs` in the build container. |
| `secret` | Allow the build container to access secure files such as private keys without baking them into the image or build cache. |
| `ssh` | Allow the build container to access SSH keys via SSH agents, with support for passphrases. |

### RUN --mount=type=bind

This mount type allows binding files or directories to the build container. A bind mount is read-only by default.

| Option | Description |
|---|---|
| `target`, `dst`, `destination`1 | Mount path. |
| `source` | Source path in the `from`. Defaults to the root of the `from`. |
| `from` | Build stage, context, or image name for the root of the source. Defaults to the build context. |
| `rw`,`readwrite` | Allow writes on the mount. Written data will be discarded after the `RUN` instruction completes and will not be committed to the image layer. |

### RUN --mount=type=cache

This mount type allows the build container to cache directories for compilers and package managers.

| Option | Description |
|---|---|
| `id` | Optional ID to identify separate/different caches. Defaults to value of `target`. |
| `target`, `dst`, `destination`1 | Mount path. |
| `ro`,`readonly` | Read-only if set. |
| `sharing` | One of `shared`, `private`, or `locked`. Defaults to `shared`. A `shared` cache mount can be used concurrently by multiple writers. `private` creates a new mount if there are multiple writers. `locked` pauses the second writer until the first one releases the mount. |
| `from` | Build stage, context, or image name to use as a base of the cache mount. Defaults to empty directory. |
| `source` | Subpath in the `from` to mount. Defaults to the root of the `from`. |
| `mode` | File mode for new cache directory in octal. Default `0755`. |
| `uid` | User ID for new cache directory. Default `0`. |
| `gid` | Group ID for new cache directory. Default `0`. |

Contents of the cache directories persists between builder invocations without invalidating the instruction cache. Cache mounts should only be used for better performance. Your build should work with any contents of the cache directory as another build may overwrite the files or GC may clean it if more storage space is needed.

#### Example: cache Go packages

```dockerfile
# syntax=docker/dockerfile:1
FROM golang
RUN --mount=type=cache,target=/root/.cache/go-build \
  go build ...
```

#### Example: cache apt packages

```dockerfile
# syntax=docker/dockerfile:1
FROM ubuntu
RUN rm -f /etc/apt/apt.conf.d/docker-clean; echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
  --mount=type=cache,target=/var/lib/apt,sharing=locked \
  apt-get update && apt-get --no-install-recommends install -y gcc
```

Apt needs exclusive access to its data, so the caches use the option `sharing=locked`, which will make sure multiple parallel builds using the same cache mount will wait for each other and not access the same cache files at the same time. You could also use `sharing=private` if you prefer to have each build create another cache directory in this case.

### RUN --mount=type=tmpfs

This mount type allows mounting `tmpfs` in the build container.

| Option | Description |
|---|---|
| `target`, `dst`, `destination`1 | Mount path. |
| `size` | Specify an upper limit on the size of the filesystem. |

### RUN --mount=type=secret

This mount type allows the build container to access secret values, such as tokens or private keys, without baking them into the image.

By default, the secret is mounted as a file. You can also mount the secret as an environment variable by setting the `env` option.

| Option | Description |
|---|---|
| `id` | ID of the secret. Defaults to basename of the target path. |
| `target`, `dst`, `destination` | Mount the secret to the specified path. Defaults to `/run/secrets/` + `id` if unset and if `env` is also unset. |
| `env` | Mount the secret to an environment variable instead of a file, or both. (since Dockerfile v1.10.0) |
| `required` | If set to `true`, the instruction errors out when the secret is unavailable. Defaults to `false`. |
| `mode` | File mode for secret file in octal. Default `0400`. |
| `uid` | User ID for secret file. Default `0`. |
| `gid` | Group ID for secret file. Default `0`. |

#### Example: access to S3

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3
RUN pip install awscli
RUN --mount=type=secret,id=aws,target=/root/.aws/credentials \
  aws s3 cp s3://... ...
```

```console
$ docker buildx build --secret id=aws,src=$HOME/.aws/credentials .
```

#### Example: Mount as environment variable

The following example takes the secret `API_KEY` and mounts it as an environment variable with the same name.

```dockerfile
# syntax=docker/dockerfile:1
FROM alpine
RUN --mount=type=secret,id=API_KEY,env=API_KEY \
    some-command --token-from-env $API_KEY
```

Assuming that the `API_KEY` environment variable is set in the build environment, you can build this with the following command:

```console
$ docker buildx build --secret id=API_KEY .
```

### RUN --mount=type=ssh

This mount type allows the build container to access SSH keys via SSH agents, with support for passphrases.

| Option | Description |
|---|---|
| `id` | ID of SSH agent socket or key. Defaults to "default". |
| `target`, `dst`, `destination` | SSH agent socket path. Defaults to `/run/buildkit/ssh_agent.${N}`. |
| `required` | If set to `true`, the instruction errors out when the key is unavailable. Defaults to `false`. |
| `mode` | File mode for socket in octal. Default `0600`. |
| `uid` | User ID for socket. Default `0`. |
| `gid` | Group ID for socket. Default `0`. |

#### Example: access to GitLab

```dockerfile
# syntax=docker/dockerfile:1
FROM alpine
RUN apk add --no-cache openssh-client
RUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan gitlab.com >> ~/.ssh/known_hosts
RUN --mount=type=ssh \
  ssh -q -T git@gitlab.com 2>&1 | tee /hello
# "Welcome to GitLab, @GITLAB_USERNAME_ASSOCIATED_WITH_SSHKEY" should be printed here
# with the type of build progress is defined as `plain`.
```

```console
$ eval $(ssh-agent)
$ ssh-add ~/.ssh/id_rsa
(Input your passphrase here)
$ docker buildx build --ssh default=$SSH_AUTH_SOCK .
```

You can also specify a path to `*.pem` file on the host directly instead of `$SSH_AUTH_SOCK`. However, pem files with passphrases are not supported.

### RUN --network

```dockerfile
RUN --network=<TYPE>
```

`RUN --network` allows control over which networking environment the command is run in.

The supported network types are:

| Type | Description |
|---|---|
| `default` (default) | Run in the default network. |
| `none` | Run with no network access. |
| `host` | Run in the host's network environment. |

### RUN --network=default

Equivalent to not supplying a flag at all, the command is run in the default network for the build.

### RUN --network=none

The command is run with no network access (`lo` is still available, but is isolated to this process)

#### Example: isolating external effects

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.6
ADD mypackage.tgz wheels/
RUN --network=none pip install --find-links wheels mypackage
```

`pip` will only be able to install the packages provided in the tarfile, which can be controlled by an earlier build stage.

### RUN --network=host

The command is run in the host's network environment (similar to `docker build --network=host`, but on a per-instruction basis)

> Warning
> 
> The use of `--network=host` is protected by the `network.host` entitlement, which needs to be enabled when starting the buildkitd daemon with `--allow-insecure-entitlement network.host` flag or in buildkitd config, and for a build request with `--allow network.host` flag.

### RUN --security

```dockerfile
RUN --security=<sandbox|insecure>
```

The default security mode is `sandbox`. With `--security=insecure`, the builder runs the command without sandbox in insecure mode, which allows to run flows requiring elevated privileges (e.g. containerd). This is equivalent to running `docker run --privileged`.

> Warning
> 
> In order to access this feature, entitlement `security.insecure` should be enabled when starting the buildkitd daemon with `--allow-insecure-entitlement security.insecure` flag or in buildkitd config, and for a build request with `--allow security.insecure` flag.

Default sandbox mode can be activated via `--security=sandbox`, but that is no-op.

#### Example: check entitlements

```dockerfile
# syntax=docker/dockerfile:1
FROM ubuntu
RUN --security=insecure cat /proc/self/status | grep CapEff
```

```text
#84 0.093 CapEff:	0000003fffffffff
```


## CMD

The `CMD` instruction sets the command to be executed when running a container from an image.

You can specify `CMD` instructions using shell or exec forms:

- `CMD ["executable","param1","param2"]` (exec form)
- `CMD ["param1","param2"]` (exec form, as default parameters to `ENTRYPOINT`)
- `CMD command param1 param2` (shell form)

There can only be one `CMD` instruction in a Dockerfile. If you list more than one `CMD`, only the last one takes effect.

The purpose of a `CMD` is to provide defaults for an executing container. These defaults can include an executable, or they can omit the executable, in which case you must specify an `ENTRYPOINT` instruction as well.

If you would like your container to run the same executable every time, then you should consider using `ENTRYPOINT` in combination with `CMD`. See `ENTRYPOINT`. If the user specifies arguments to `docker run` then they will override the default specified in `CMD`, but still use the default `ENTRYPOINT`.

If `CMD` is used to provide default arguments for the `ENTRYPOINT` instruction, both the `CMD` and `ENTRYPOINT` instructions should be specified in the exec form.

> Note
> 
> Don't confuse `RUN` with `CMD`. `RUN` actually runs a command and commits the result; `CMD` doesn't execute anything at build time, but specifies the intended command for the image.


## LABEL

```dockerfile
LABEL <key>=<value> [<key>=<value>...]
```

The `LABEL` instruction adds metadata to an image. A `LABEL` is a key-value pair. To include spaces within a `LABEL` value, use quotes and backslashes as you would in command-line parsing. A few usage examples:

```dockerfile
LABEL "com.example.vendor"="ACME Incorporated"
LABEL com.example.label-with-value="foo"
LABEL version="1.0"
LABEL description="This text illustrates \
that label-values can span multiple lines."
```

An image can have more than one label. You can specify multiple labels on a single line. Prior to Docker 1.10, this decreased the size of the final image, but this is no longer the case. You may still choose to specify multiple labels in a single instruction, in one of the following two ways:

```dockerfile
LABEL multi.label1="value1" multi.label2="value2" other="value3"
```

```dockerfile
LABEL multi.label1="value1" \
      multi.label2="value2" \
      other="value3"
```

> Note
> 
> Be sure to use double quotes and not single quotes. Particularly when you are using string interpolation (e.g. `LABEL example="foo-$ENV_VAR"`), single quotes will take the string as is without unpacking the variable's value.

Labels included in base images (images in the `FROM` line) are inherited by your image. If a label already exists but with a different value, the most-recently-applied value overrides any previously-set value.

In a multi-stage build, labels from intermediate stages are only present in the final image if the final stage is directly or indirectly based on them (via `FROM`). Labels from a stage that you only reference with `COPY --from` or `RUN --mount=from=` are not included in the output image. Labels from the base image specified in the final `FROM` instruction are always inherited.

To view an image's labels, use the `docker image inspect` command. You can use the `--format` option to show just the labels;

```console
$ docker image inspect --format='{{json .Config.Labels}}' myimage
```

```json
{
  "com.example.vendor": "ACME Incorporated",
  "com.example.label-with-value": "foo",
  "version": "1.0",
  "description": "This text illustrates that label-values can span multiple lines.",
  "multi.label1": "value1",
  "multi.label2": "value2",
  "other": "value3"
}
```


## MAINTAINER (deprecated)

```dockerfile
MAINTAINER <name>
```

The `MAINTAINER` instruction sets the *Author* field of the generated images. The `LABEL` instruction is a much more flexible version of this and you should use it instead, as it enables setting any metadata you require, and can be viewed easily, for example with `docker inspect`. To set a label corresponding to the `MAINTAINER` field you could use:

```dockerfile
LABEL org.opencontainers.image.authors="SvenDowideit@home.org.au"
```

This will then be visible from `docker inspect` with the other labels.


## EXPOSE

```dockerfile
EXPOSE <port> [<port>/<protocol>...]
```

The `EXPOSE` instruction informs Docker that the container listens on the specified network ports at runtime. You can specify whether the port listens on TCP or UDP, and the default is TCP if you don't specify a protocol.

The `EXPOSE` instruction doesn't actually publish the port. It functions as a type of documentation between the person who builds the image and the person who runs the container, about which ports are intended to be published. To publish the port when running the container, use the `-p` flag on `docker run` to publish and map one or more ports, or the `-P` flag to publish all exposed ports and map them to high-order ports.

By default, `EXPOSE` assumes TCP. You can also specify UDP:

```dockerfile
EXPOSE 80/udp
```

To expose on both TCP and UDP, include two lines:

```dockerfile
EXPOSE 80/tcp
EXPOSE 80/udp
```

In this case, if you use `-P` with `docker run`, the port will be exposed once for TCP and once for UDP. Remember that `-P` uses an ephemeral high-ordered host port on the host, so TCP and UDP doesn't use the same port.

Regardless of the `EXPOSE` settings, you can override them at runtime by using the `-p` flag. For example

```console
$ docker run -p 80:80/tcp -p 80:80/udp ...
```

To set up port redirection on the host system, see using the -P flag. The `docker network` command supports creating networks for communication among containers without the need to expose or publish specific ports, because the containers connected to the network can communicate with each other over any port. For detailed information, see the overview of this feature.


## ENV

```dockerfile
ENV <key>=<value> [<key>=<value>...]
```

The `ENV` instruction sets the environment variable `<key>` to the value `<value>`. This value will be in the environment for all subsequent instructions in the build stage and can be replaced inline in many as well. The value will be interpreted for other environment variables, so quote characters will be removed if they are not escaped. Like command line parsing, quotes and backslashes can be used to include spaces within values.

Example:

```dockerfile
ENV MY_NAME="John Doe"
ENV MY_DOG=Rex\ The\ Dog
ENV MY_CAT=fluffy
```

The `ENV` instruction allows for multiple `<key>=<value> ...` variables to be set at one time, and the example below will yield the same net results in the final image:

```dockerfile
ENV MY_NAME="John Doe" MY_DOG=Rex\ The\ Dog \
    MY_CAT=fluffy
```

The environment variables set using `ENV` will persist when a container is run from the resulting image. You can view the values using `docker inspect`, and change them using `docker run --env <key>=<value>`.

A stage inherits any environment variables that were set using `ENV` by its parent stage or any ancestor. Refer to the multi-stage builds section in the manual for more information.

Environment variable persistence can cause unexpected side effects. For example, setting `ENV DEBIAN_FRONTEND=noninteractive` changes the behavior of `apt-get`, and may confuse users of your image.

If an environment variable is only needed during build, and not in the final image, consider setting a value for a single command instead:

```dockerfile
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y ...
```

Or using `ARG`, which is not persisted in the final image:

```dockerfile
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y ...
```

> Note
> 
> **Alternative syntax**
> 
> The `ENV` instruction also allows an alternative syntax `ENV <key> <value>`, omitting the `=`. For example:
> 
> ```dockerfile
> ENV MY_VAR my-value
> ```
> 
> This syntax does not allow for multiple environment-variables to be set in a single `ENV` instruction, and can be confusing. For example, the following sets a single environment variable (`ONE`) with value `"TWO= THREE=world"`:
> 
> ```dockerfile
> ENV ONE TWO= THREE=world
> ```
> 
> The alternative syntax is supported for backward compatibility, but discouraged for the reasons outlined above, and may be removed in a future release.
