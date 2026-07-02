---
title: "pre-commit (part 2/2)"
source: https://pre-commit.com/
domain: pre-commit-framework
license: CC-BY-SA-4.0
tags: pre-commit framework, pre-commit hooks, git hook manager, code linting hooks
fetched: 2026-07-02
part: 2/2
---

## `pre-commit hazmat`

"hazardous materials"

pre-commit provides a few `entry` prefix "helpers" for unusual situations.

in case it's not clear, using these is *usually* a bad idea.

*note*: hazmat helpers do not work on languages which adjust `entry` (`docker` / `docker_image` / `fail` / `julia` / `pygrep` / `r` / `unsupported_script`).

### `pre-commit hazmat cd`

*new in 4.5.0*

for "monorepo" usage one can use this to target a subdirectory.

this entry prefix will cd to the target subdir and adjust filename arguments

example usage:

```yaml
# recommended:
# minimum_pre_commit_version: 4.5.0
repos:
-   repo: ...
    rev: ...
    hooks:
    -   id: example
        alias: example-repo1
        name: example (repo1)
        files: ^repo1/
        # important! ends with `--`
        # important! copy `args: [...]` to entry and blank out `args: []`
        entry: pre-commit hazmat cd repo1 example-bin --arg1 --
        args: []

    -   id: example
        alias: example-repo2
        name: example (repo2)
        files: ^repo2/
        entry: pre-commit hazmat cd repo2 example-bin --arg1 --
        args: []

    # ... etc.
```

### `pre-commit hazmat ignore-exit-code`

*new in 4.5.0*

it's a bad idea to introduce warning noise but this gives you a way to do it.

example:

```yaml
# recommended:
# minimum_pre_commit_version: 4.5.0
repos:
-   repo: ...
    rev: ...
    hooks:
    -   id: example
        # important! copy `args: [...]` to entry and blank out `args: []`
        entry: pre-commit hazmat ignore-exit-code example-bin --arg1 --
        args: []
        # otherwise the output will always be hidden
        verbose: true
```

### `pre-commit hazmat n1`

*new in 4.5.0*

some hooks only take one filename argument. this runs them one at a time (which is super slow!)

example:

```yaml
# recommended:
# minimum_pre_commit_version: 4.5.0
repos:
-   repo: ...
    rev: ...
    hooks:
    -   id: example
        # important! ends with `--`
        # important! copy `args: [...]` to entry and blank out `args: []`
        entry: pre-commit hazmat n1 example-bin --arg1 --
        args: []
```


## usage with git 2.54+ hook configuration

*new in 4.6.0*: pre-commit improved support for `git config`-based hooks. a later version will change `pre-commit install` to use this approach.

git 2.54 introduced a new way to install git hook tools via `git config`.

the basic gist is the following enables a hook in a git repo:

```bash
git config set hook.<name>.event pre-push
git config set hook.<name>.command 'some command here'
```

an example setup with `pre-commit` might look like:

```bash
# note, the "hook" name here is `pre-commit.pre-commit`
# for the `pre-commit` "tool" and the `pre-commit` "event"
git config set hook.pre-commit.pre-commit.event pre-commit
git config set hook.pre-commit.pre-commit.command 'pre-commit hook-impl --hook-type pre-commit --'

# please follow that naming scheme for future compatibility with `pre-commit install`

# an example with pre-push:
#
# git config set hook.pre-commit.pre-push.event pre-push
# git config set hook.pre-commit.pre-push.command 'pre-commit hook-impl --hook-type pre-push --'
```

`pre-commit hook-impl` is a "hidden" implementation command with these options:

- `--hook-type ...`: the hook type to use
- `--config ...`: (optional) path to `.pre-commit-config.yaml`
- `--skip-on-missing-config`: silently pass when a config is missing

some interesting applications of this:

### "global" installation of pre-commit

with `git config set --global ...` this can automatically enable pre-commit for all repositories:

```bash
git config set --global hook.pre-commit.pre-commit.event pre-commit
git config set --global hook.pre-commit.pre-commit.command 'pre-commit hook-impl --hook-type pre-commit --skip-on-missing-config --'
```

- this setup **not recommended** as it can lead to accidentally running hooks when interacting with an untrusted repository.
- `--skip-on-missing-config` is recommended here as arbitrary git repositories may not have a `.pre-commit-config.yaml`.

### always running a hook on all files

since you can configure pre-commit as many times as you want you *could* invoke pre-commit to run a particular hook always and on all files

```bash
git config set hook.pre-commit.pre-commit-always.event pre-commit
git config set hook.pre-commit.pre-commit-always.command 'pre-commit run hookid --hook-stage pre-commit --all-files'
```

*note*: this is not recommended as it has the tendancy to be slow and deviates from the normal expectations of pre-commit.


## automatically enabling pre-commit on repositories

*note*: if you are on a new-enough version of `git` you may want to use this approach instead.

`pre-commit init-templatedir` can be used to set up a skeleton for `git`'s `init.templateDir` option. This means that any newly cloned repository will automatically have the hooks set up without the need to run `pre-commit install`.

To configure, first set `git`'s `init.templateDir` -- in this example I'm using `~/.git-template` as my template directory.

```console
$ git config --global init.templateDir ~/.git-template
$ pre-commit init-templatedir ~/.git-template
pre-commit installed at /home/asottile/.git-template/hooks/pre-commit
```

Now whenever you clone a pre-commit enabled repo, the hooks will already be set up!

```pre
$ git clone -q [email protected]:asottile/pyupgrade
$ cd pyupgrade
$ git commit --allow-empty -m 'Hello world!'
Check docstring is first.............................(no files to check)Skipped
Check Yaml...........................................(no files to check)Skipped
Debug Statements (Python)............................(no files to check)Skipped
...
```

`init-templatedir` uses the `--allow-missing-config` option from `pre-commit install` so repos without a config will be skipped:

```console
$ git init sample
Initialized empty Git repository in /tmp/sample/.git/
$ cd sample
$ git commit --allow-empty -m 'Initial commit'
`.pre-commit-config.yaml` config file not found. Skipping `pre-commit`.
[main (root-commit) d1b39c1] Initial commit
```

To still require opt-in, but prompt the user to set up pre-commit use a template hook as follows (for example in `~/.git-template/hooks/pre-commit`).

```bash
#!/usr/bin/env bash
if [ -f .pre-commit-config.yaml ]; then
    echo 'pre-commit configuration detected, but `pre-commit install` was never run' 1>&2
    exit 1
fi
```

With this, a forgotten `pre-commit install` produces an error on commit:

```console
$ git clone -q https://github.com/asottile/pyupgrade
$ cd pyupgrade/
$ git commit -m 'foo'
pre-commit configuration detected, but `pre-commit install` was never run
```


## Filtering files with types

Filtering with `types` provides several advantages over traditional filtering with `files`.

- no error-prone regular expressions
- files can be matched by their shebang (even when extensionless)
- symlinks / submodules can be easily ignored

`types` is specified per hook as an array of tags. The tags are discovered through a set of heuristics by the identify library. `identify` was chosen as it is a small portable pure python library.

Some of the common tags you'll find from identify:

- `file`
- `symlink`
- `directory` - in the context of pre-commit this will be a submodule
- `executable` - whether the file has the executable bit set
- `text` - whether the file looks like a text file
- `binary` - whether the file looks like a binary file
- tags by extension / naming convention
- tags by shebang (`#!`)

To discover the type of any file on disk, you can use `identify`'s cli:

```console
$ identify-cli setup.py
["file", "non-executable", "python", "text"]
$ identify-cli some-random-file
["file", "non-executable", "text"]
$ identify-cli --filename-only some-random-file; echo $?
1
```

If a file extension you use is not supported, please submit a pull request!

`types`, `types_or`, and `files` are evaluated together with `AND` when filtering. Tags within `types` are also evaluated using `AND`.

Tags within `types_or` are evaluated using `OR`.

For example:

```yaml
    files: ^foo/
    types: [file, python]
```

will match a file `foo/1.py` but will not match `setup.py`.

Another example:

```yaml
    files: ^foo/
    types_or: [javascript, jsx, ts, tsx]
```

will match any of `foo/bar.js` / `foo/bar.jsx` / `foo/bar.ts` / `foo/bar.tsx` but not `baz.js`.

If you want to match a file path that isn't included in a `type` when using an existing hook you'll need to revert back to `files` only matching by overriding the `types` setting. Here's an example of using `check-json` against non-json files:

```yaml
    -   id: check-json
        types: [file]  # override `types: [json]`
        files: \.(json|myext)$
```

Files can also be matched by shebang. With `types: python`, an `exe` starting with `#!/usr/bin/env python3` will also be matched.

As with `files` and `exclude`, you can also exclude types if necessary using `exclude_types`.


## Regular expressions

The patterns for `files` and `exclude` are python regular expressions and are matched with `re.search`.

As such, you can use any of the features that python regexes support.

If you find that your regular expression is becoming unwieldy due to a long list of excluded / included things, you may find a verbose regular expression useful. One can enable this with yaml's multiline literals and the `(?x)` regex flag.

```yaml
# ...
    -   id: my-hook
        exclude: |
            (?x)^(
                path/to/file1.py|
                path/to/file2.py|
                path/to/file3.py
            )$
```


## Overriding language version

Sometimes you only want to run the hooks on a specific version of the language. For each language, they default to using the system installed language (So for example if I’m running `python3.7` and a hook specifies `python`, pre-commit will run the hook using `python3.7`). Sometimes you don’t want the default system installed version so you can override this on a per-hook basis by setting the `language_version`.

```yaml
-   repo: https://github.com/pre-commit/mirrors-scss-lint
    rev: v0.54.0
    hooks:
    -   id: scss-lint
        language_version: 2.1.5
```

This tells pre-commit to use ruby `2.1.5` to run the `scss-lint` hook.

Valid values for specific languages are listed below:

- python: Whatever system installed python interpreters you have. The value of this argument is passed as the `-p` to `virtualenv`.
  - on windows the pep394 name will be translated into a py launcher call for portability. So continue to use names like `python3` (`py -3`) or `python3.6` (`py -3.6`) even on windows.
- node: See nodeenv.
- ruby: See ruby-build.
- rust: `language_version` is passed to `rustup`
- *new in 3.0.0* golang: use the versions on go.dev/dl such as `1.19.5`

you can set `default_language_version` at the top level in your configuration to control the default versions across all hooks of a language.

```yaml
default_language_version:
    # force all unspecified python hooks to run python3
    python: python3
    # force all unspecified ruby hooks to run ruby 2.1.5
    ruby: 2.1.5
```


## badging your repository

you can add a badge to your repository to show your contributors / users that you use pre-commit!

(pre-commit)

- Markdown: [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
- HTML: <a href="https://github.com/pre-commit/pre-commit"><img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit" alt="pre-commit" style="max-width:100%;"></a>
- reStructuredText: .. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit :target: https://github.com/pre-commit/pre-commit :alt: pre-commit
- AsciiDoc: image:https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit[pre-commit, link=https://github.com/pre-commit/pre-commit]


## Usage in continuous integration

pre-commit can also be used as a tool for continuous integration. For instance, adding `pre-commit run --all-files` as a CI step will ensure everything stays in tip-top shape. To check only files which have changed, which may be faster, use something like `pre-commit run --from-ref origin/HEAD --to-ref HEAD`


## Managing CI Caches

`pre-commit` by default places its repository store in `~/.cache/pre-commit` -- this can be configured in two ways:

- `PRE_COMMIT_HOME`: if set, pre-commit will use that location instead.
- `XDG_CACHE_HOME`: if set, pre-commit will use `$XDG_CACHE_HOME/pre-commit` following the XDG Base Directory Specification.

### pre-commit.ci example

no additional configuration is needed to run in pre-commit.ci!

pre-commit.ci also has the following benefits:

- it's faster than other free CI solutions
- it will autofix pull requests
- it will periodically autoupdate your configuration

(pre-commit.ci speed comparison)

### appveyor example

```yaml
cache:
- '%USERPROFILE%\.cache\pre-commit'
```

### azure pipelines example

note: azure pipelines uses immutable caches so the python version and `.pre-commit-config.yaml` hash must be included in the cache key. for a repository template, see [email protected].

```yaml
jobs:
- job: precommit

  # ...

  variables:
    PRE_COMMIT_HOME: $(Pipeline.Workspace)/pre-commit-cache

  steps:

  # ...

  - script: echo "##vso[task.setvariable variable=PY]$(python -VV)"
  - task: CacheBeta@0
    inputs:
      key: pre-commit | .pre-commit-config.yaml | "$(PY)"
      path: $(PRE_COMMIT_HOME)
```

### circleci example

like azure pipelines, circleci also uses immutable caches:

```yaml
  steps:
  - run:
    command: |
      cp .pre-commit-config.yaml pre-commit-cache-key.txt
      python --version --version >> pre-commit-cache-key.txt
  - restore_cache:
    keys:
    - v1-pc-cache-{{ checksum "pre-commit-cache-key.txt" }}

  # ...

  - save_cache:
    key: v1-pc-cache-{{ checksum "pre-commit-cache-key.txt" }}
    paths:
      - ~/.cache/pre-commit
```

(source: @chriselion)

### github actions example

**see the official pre-commit github action**

like azure pipelines, github actions also uses immutable caches:

```yaml
    - name: set PY
      run: echo "PY=$(python -VV | sha256sum | cut -d' ' -f1)" >> $GITHUB_ENV
    - uses: actions/cache@v3
      with:
        path: ~/.cache/pre-commit
        key: pre-commit|${{ env.PY }}|${{ hashFiles('.pre-commit-config.yaml') }}
```

### gitlab CI example

See the Gitlab caching best practices to fine tune the cache scope.

```yaml
my_job:
  variables:
    PRE_COMMIT_HOME: ${CI_PROJECT_DIR}/.cache/pre-commit
  cache:
    paths:
      - ${PRE_COMMIT_HOME}
```

pre-commit's cache requires to be served from a constant location between the different builds. This isn't the default when using k8s runners on GitLab. In case you face the error `InvalidManifestError`, set `builds_dir` to something static e.g `builds_dir = "/builds"` in your `[[runner]]` config

### travis-ci example

```yaml
cache:
  directories:
  - $HOME/.cache/pre-commit
```


## Usage with tox

tox is useful for configuring test / CI tools such as pre-commit. One feature of `tox>=2` is it will clear environment variables such that tests are more reproducible. Under some conditions, pre-commit requires a few environment variables and so they must be allowed to be passed through.

When cloning repos over ssh (`repo: [email protected]:...`), `git` requires the `SSH_AUTH_SOCK` variable and will otherwise fail:

```pre
[INFO] Initializing environment for [email protected]:pre-commit/pre-commit-hooks.
An unexpected error has occurred: CalledProcessError: command: ('/usr/bin/git', 'fetch', 'origin', '--tags')
return code: 128
expected return code: 0
stdout: (none)
stderr:
    [email protected]: Permission denied (publickey).
    fatal: Could not read from remote repository.

    Please make sure you have the correct access rights
    and the repository exists.

Check the log at /home/asottile/.cache/pre-commit/pre-commit.log
```

Add the following to your tox testenv:

```ini
[testenv]
passenv = SSH_AUTH_SOCK
```

Likewise, when cloning repos over http / https (`repo: https://github.com:...`), you might be working behind a corporate http(s) proxy server, in which case `git` requires the `http_proxy`, `https_proxy` and `no_proxy` variables to be set, or the clone may fail:

```ini
[testenv]
passenv = http_proxy https_proxy no_proxy
```


## Using the latest version for a repository

`pre-commit` configuration aims to give a repeatable and fast experience and therefore intentionally doesn't provide facilities for "unpinned latest version" for hook repositories.

Instead, `pre-commit` provides tools to make it easy to upgrade to the latest versions with `pre-commit autoupdate`. If you need the absolute latest version of a hook (instead of the latest tagged version), pass the `--bleeding-edge` parameter to `autoupdate`.

`pre-commit` assumes that the value of `rev` is an immutable ref (such as a tag or SHA) and will cache based on that. Using a branch name (or `HEAD`) for the value of `rev` is not supported and will only represent the state of that mutable ref at the time of hook installation (and will *NOT* update automatically).

# Contributing

We’re looking to grow the project and get more contributors especially to support more languages/versions. We’d also like to get the .pre-commit-hooks.yaml files added to popular linters without maintaining forks / mirrors.

Feel free to submit bug reports, pull requests, and feature requests.


## Sponsoring

If you or your company would like to support the development of pre-commit one can contribute in the following ways:

- GitHub Sponsors (asottile)
- Open Collective


## Getting help

There are several ways to get help for pre-commit:

- Ask a question on stackoverflow tagged pre-commit.com
- Create an issue on pre-commit/pre-commit
- Ask in the #pre-commit channel in asottile's twitch discord


## Contributors

- website by Molly Finkle
- created by Anthony Sottile
- core developers: Ken Struys, Chris Kuehl
- framework contributors
- core hook contributors
- and users like you!
