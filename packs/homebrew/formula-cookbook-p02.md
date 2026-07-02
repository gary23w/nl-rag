---
title: "Homebrew Documentation: Formula Cookbook (part 2/2)"
source: https://docs.brew.sh/Formula-Cookbook
domain: homebrew
license: CC-BY-SA-4.0
tags: homebrew macos, package manager, formula cookbook, unix packages
fetched: 2026-07-02
part: 2/2
---

## Advanced formula tricks

See the `Formula` class API documentation for the full list of methods available within a formula. If anything isn’t clear, you can usually figure it out by `grep`ping the `$(brew --repository homebrew/core)` directory for examples. Please submit a pull request to amend this document if you think it will help!

### Handling different system configurations

Often, formulae need different dependencies, resources, patches, conflicts, deprecations or `keg_only` statuses on different OSes and architectures. In these cases, the components can be nested inside `on_macos`, `on_linux`, `on_arm` or `on_intel` blocks. For example, here’s how to add `gcc` as a Linux-only dependency:

```ruby
on_linux do
  depends_on "gcc"
end
```

Components can also be declared for specific macOS versions or version ranges. For example, to declare a dependency only on Sequoia, nest the `depends_on` call inside an `on_sequoia` block. Add an `:or_older` or `:or_newer` parameter to the `on_sequoia` method to add the dependency to all macOS versions that meet the condition. For example, to add `gettext` as a build dependency on Sequoia and all later macOS versions, use:

```ruby
on_sequoia :or_newer do
  depends_on "gettext" => :build
end
```

Sometimes, a dependency is needed on certain macOS versions *and* on Linux. In these cases, a special `on_system` method can be used:

```ruby
on_system :linux, macos: :sonoma_or_older do
  depends_on "gettext" => :build
end
```

To check multiple conditions, nest the corresponding blocks. For example, the following code adds a `gettext` build dependency when on ARM *and* macOS:

```ruby
on_macos do
  on_arm do
    depends_on "gettext" => :build
  end
end
```

#### Inside `def install` and `test do`

Inside `def install` and `test do`, don’t use these `on_*` methods. Instead, use `if` statements and the following conditionals:

- `OS.mac?` and `OS.linux?` return `true` or `false` based on the OS
- `Hardware::CPU.arm?` and `Hardware::CPU.intel?` return `true` or `false` based on the arch
- `MacOS.version` returns the current macOS version. Use `==`, `<=` or `>=` to compare to symbols corresponding to macOS versions (e.g. `if MacOS.version >= :tahoe`)

See the `icoutils` formula for an example.

### `livecheck` blocks

When `brew livecheck` is unable to identify versions for a formula, we can control its behavior using a `livecheck` block. Here is a simple example to check a page for links containing a filename like `example-1.2.tar.gz`:

```ruby
livecheck do
  url "https://www.example.com/downloads/"
  regex(/href=.*?example[._-]v?(\d+(?:\.\d+)+)\.t/i)
end
```

For `url`/`regex` guidelines and additional `livecheck` block examples, refer to the `brew livecheck` documentation. For more technical information on the methods used in a `livecheck` block, please refer to the `Livecheck` class documentation.

### Excluding formula from autobumping

By default, all new formulae in the `Homebrew/homebrew-core` repository are autobumped. This means that future updates are handled automatically by Homebrew CI jobs, and contributors do not have to submit pull requests.

Sometimes, we want to exclude a formula from this list, for one reason or another. This can be done by adding the `no_autobump!` method in the formula definition; a reason must be provided with the `because:` parameter. It accepts a string or a symbol that corresponds to a preset reason, for example:

```ruby
no_autobump! because: :bumped_by_upstream
```

A complete list of allowed symbols can be found in `NO_AUTOBUMP_REASONS_LIST`.

See our Autobump documentation for more information about the autobump process.

### URL download strategies

When parsing a download URL, Homebrew auto-detects the resource type it points to, whether archive (e.g. tarball, zip) or version control repository (e.g. Git, Subversion, Mercurial) and chooses an appropriate download strategy. Some strategies can be passed additional options to alter what’s downloaded. For example, to fetch a formula’s source code and infer its version number from a specific tag in a Git repository (useful for packages that rely on Git submodules), specify `url` with the `:tag` and `:revision` options, like so:

```ruby
class Foo < Formula
  # ...
  url "https://github.com/some/package.git",
      tag:      "v1.6.2",
      revision: "344cd2ee3463abab4c16ac0f9529a846314932a2"
end
```

If fetching from a Subversion or Mercurial repository, specify `revision` and `version` separately:

```ruby
class Bar < Formula
  # ...
  url "https://svn.code.sf.net/p/package/code/stable", revision: "4687"
  version "12.1.8"
end
```

To fetch specific revisions of Subversion externals, specify `revisions`:

```ruby
class Baz < Formula
  # ...
  url "svn://source.something.org/package/trunk/",
      revisions: { trunk: "22916", "libsomething" => "31045" }
  version "7.2.11"
end
```

If not inferable, specify which of Homebrew’s built-in download strategies to use with the `using:` option. For example:

```ruby
class Nginx < Formula
  desc "HTTP(S) server and reverse proxy, and IMAP/POP3 proxy server"
  homepage "https://nginx.org/"
  url "https://nginx.org/download/nginx-1.23.2.tar.gz", using: :homebrew_curl
  sha256 "a80cc272d3d72aaee70aa8b517b4862a635c0256790434dbfc4d618a999b0b46"
  head "https://hg.nginx.org/nginx/", using: :hg
end
```

Homebrew offers these anonymous download strategies.

| `using:` value | download strategy | requirements |
|---|---|---|
| `:bzr` | fetch from Bazaar repository | `breezy` installed |
| `:curl` | download using `curl` (default) |   |
| `:cvs` | fetch from CVS repository | `cvs` installed |
| `:fossil` | fetch from Fossil repository | `fossil` installed |
| `:git` | fetch from Git repository | `git` installed |
| `:hg` | fetch from Mercurial repository | `hg` installed |
| `:homebrew_curl` | download using brewed `curl` | `curl` installed |
| `:nounzip` | download without decompressing |   |
| `:post` | download using `curl` via POST | `data:` hash of parameters |
| `:svn` | fetch from Subversion repository | `svn` installed |

If you need more control over the way files are downloaded and staged, you can create a custom download strategy and specify it with the `:using` option:

```ruby
class MyDownloadStrategy < SomeHomebrewDownloadStrategy
  def fetch(timeout: nil, **options)
    opoo "Unhandled options in #{self.class}#fetch: #{options.keys.join(", ")}" unless options.empty?

    # downloads output to `temporary_path`
  end
end

class Foo < Formula
  url "something", using: MyDownloadStrategy
end
```

### Unstable versions (`head`)

Formulae can specify an alternate download for the upstream project’s development/cutting-edge source (e.g. `master`/`main`/`trunk`) using `head`, which can be activated by passing `--HEAD` when installing. Specifying it is done in the same manner as `url`, with added conventions for fetching from version control repositories:

- Git repositories **must always** specify `branch:`. If the repository is very large, specify `only_path` to limit the checkout to one path.

```sh
head "<https://github.com/some/package.git>", branch: "main"
```

- Mercurial repositories need `branch:` specified to fetch a branch other than “default”.
- Subversion repositories can specify `trust_cert: true` to skip interactive certificate prompts.
- CVS repositories can specify `module:` to check out a specific module.

You can also bundle the URL and any `head`-specific dependencies and resources in a `head do` block.

```ruby
class Foo < Formula
  # ...

  head do
    url "https://hg.sr.ht/~user/foo", using: :hg, branch: "develop"

    depends_on "pkgconf" => :build

    resource "package" do
      url "https://github.com/other/package.git", branch: "main"
    end
  end
end
```

You can test whether the `head` is being built with `build.head?` in the `install` method.

### Compiler selection

Sometimes a package fails to build when using a certain compiler. Since recent Xcode versions no longer include a GCC compiler we cannot simply force the use of GCC. Instead, the correct way to declare this is with the `fails_with` DSL method. A properly constructed `fails_with` block documents the latest compiler build version known to cause compilation to fail, and the cause of the failure. For example:

```ruby
fails_with :clang do
  build 211
  cause "Miscompilation resulting in segfault on queries"
end

fails_with :gcc do
  version "5" # fails with GCC 5.x and earlier
  cause "Requires C++17 support"
end

fails_with gcc: "7" do
  version "7.1" # fails with GCC 7.0 and 7.1 but not 7.2, or any other major GCC version
  cause <<-EOS
    warning: dereferencing type-punned pointer will break strict-aliasing rules
    Fixed in GCC 7.2, see https://gcc.gnu.org/bugzilla/show_bug.cgi?id=42136
  EOS
end
```

For `:clang`, `build` takes an integer (you can find this number in your `brew --config` output), while `:gcc` uses either just `version` which takes a string to indicate the last problematic GCC version, or a major version argument combined with `version` to single out a range of specific GCC releases. `cause` takes a string, and the use of heredocs is encouraged to improve readability and allow for more comprehensive documentation.

`fails_with` declarations can be used with any of `:gcc`, `:llvm`, and `:clang`. Homebrew will use this information to select a working compiler (if one is available).

### Just moving some files

When your code in the install function is run, the current working directory is set to the extracted tarball. This makes it easy to just move some files:

```ruby
prefix.install "file1", "file2"
```

Or everything:

```ruby
prefix.install Dir["output/*"]
```

Or just the tarball’s top-level files like README, LICENSE etc.:

```ruby
prefix.install_metafiles
```

Generally we’d rather you were specific about which files or directories need to be installed rather than installing everything.

#### Variables for directory locations

| name | default path | example |
|---|---|---|
| **`HOMEBREW_PREFIX`** | same as output of `$(brew --prefix)` | `/opt/homebrew` |
| **`etc`** | `#{HOMEBREW_PREFIX}/etc` | `/opt/homebrew/etc` |
| **`pkgetc`** | `#{HOMEBREW_PREFIX}/etc/#{name}` | `/opt/homebrew/etc/foo` |
| **`var`** | `#{HOMEBREW_PREFIX}/var` | `/opt/homebrew/var` |
| **`prefix`** | `#{HOMEBREW_PREFIX}/Cellar/#{name}/#{version}` | `/opt/homebrew/Cellar/foo/0.1` |
| **`opt_prefix`** | `#{HOMEBREW_PREFIX}/opt/#{name}` | `/opt/homebrew/opt/foo` |
| **`bin`** | `#{prefix}/bin` | `/opt/homebrew/Cellar/foo/0.1/bin` |
| **`opt_bin`** | `#{opt_prefix}/bin` | `/opt/homebrew/opt/foo/bin` |
| **`doc`** | `#{prefix}/share/doc/#{name}` | `/opt/homebrew/Cellar/foo/0.1/share/doc/foo` |
| **`include`** | `#{prefix}/include` | `/opt/homebrew/Cellar/foo/0.1/include` |
| **`opt_include`** | `#{opt_prefix}/include` | `/opt/homebrew/opt/foo/include` |
| **`info`** | `#{prefix}/share/info` | `/opt/homebrew/Cellar/foo/0.1/share/info` |
| **`lib`** | `#{prefix}/lib` | `/opt/homebrew/Cellar/foo/0.1/lib` |
| **`opt_lib`** | `#{opt_prefix}/lib` | `/opt/homebrew/opt/foo/lib` |
| **`libexec`** | `#{prefix}/libexec` | `/opt/homebrew/Cellar/foo/0.1/libexec` |
| **`opt_libexec`** | `#{opt_prefix}/libexec` | `/opt/homebrew/opt/foo/libexec` |
| **`man`** | `#{prefix}/share/man` | `/opt/homebrew/Cellar/foo/0.1/share/man` |
| **`man[1-8]`** | `#{prefix}/share/man/man[1-8]` | `/opt/homebrew/Cellar/foo/0.1/share/man/man[1-8]` |
| **`sbin`** | `#{prefix}/sbin` | `/opt/homebrew/Cellar/foo/0.1/sbin` |
| **`opt_sbin`** | `#{opt_prefix}/sbin` | `/opt/homebrew/opt/foo/sbin` |
| **`share`** | `#{prefix}/share` | `/opt/homebrew/Cellar/foo/0.1/share` |
| **`opt_share`** | `#{opt_prefix}/share` | `/opt/homebrew/opt/foo/share` |
| **`pkgshare`** | `#{prefix}/share/#{name}` | `/opt/homebrew/Cellar/foo/0.1/share/foo` |
| **`opt_pkgshare`** | `#{opt_prefix}/share/#{name}` | `/opt/homebrew/opt/foo/share/foo` |
| **`elisp`** | `#{prefix}/share/emacs/site-lisp/#{name}` | `/opt/homebrew/Cellar/foo/0.1/share/emacs/site-lisp/foo` |
| **`opt_elisp`** | `#{opt_prefix}/share/emacs/site-lisp/#{name}` | `/opt/homebrew/opt/foo/share/emacs/site-lisp/foo` |
| **`frameworks`** | `#{prefix}/Frameworks` | `/opt/homebrew/Cellar/foo/0.1/Frameworks` |
| **`opt_frameworks`** | `#{opt_prefix}/Frameworks` | `/opt/homebrew/opt/foo/Frameworks` |
| **`kext_prefix`** | `#{prefix}/Library/Extensions` | `/opt/homebrew/Cellar/foo/0.1/Library/Extensions` |
| **`bash_completion`** | `#{prefix}/etc/bash_completion.d` | `/opt/homebrew/Cellar/foo/0.1/etc/bash_completion.d` |
| **`fish_completion`** | `#{prefix}/share/fish/vendor_completions.d` | `/opt/homebrew/Cellar/foo/0.1/share/fish/vendor_completions.d` |
| **`fish_function`** | `#{prefix}/share/fish/vendor_functions.d` | `/opt/homebrew/Cellar/foo/0.1/share/fish/vendor_functions.d` |
| **`zsh_completion`** | `#{prefix}/share/zsh/site-functions` | `/opt/homebrew/Cellar/foo/0.1/share/zsh/site-functions` |
| **`zsh_function`** | `#{prefix}/share/zsh/site-functions` | `/opt/homebrew/Cellar/foo/0.1/share/zsh/site-functions` |
| **`pwsh_completion`** | `#{prefix}/share/pwsh/completions` | `/opt/homebrew/Cellar/foo/0.1/share/pwsh/completions` |
| **`buildpath`** | temporary working directory during builds | `/private/tmp/foo-20250205-69197-po5981/foo-0.1` |
| **`testpath`** | temporary working directory during tests | `/private/tmp/foo-test-20250205-84567-4hfs9m` |

These can be used, for instance, in code such as:

```ruby
bin.install Dir["output/*"]
```

to move binaries into their correct location within the Cellar, and:

```ruby
man.mkpath
```

to create the directory structure for the manual page location.

To install man pages into specific locations, use `man1.install "foo.1", "bar.1"`, `man2.install "foo.2"`, etc.

The `opt_` variants generate paths that are stable between updates, which can be useful for e.g. replacing versioned paths in files:

```ruby
inreplace lib/"pkgconfig/zlib.pc", prefix, opt_prefix
```

Note that in the context of Homebrew, `libexec` is reserved for private use by the formula and therefore is not symlinked into `HOMEBREW_PREFIX`.

### File-level operations

You can use the file utilities provided by Ruby’s `FileUtils`. These are included in the `Formula` class, so you do not need the `FileUtils.` prefix to use them.

When creating symlinks, take special care to ensure they are *relative* symlinks. This makes it easier to create a relocatable bottle. For example, to create a symlink in `bin` to an executable in `libexec`, use:

```ruby
bin.install_symlink libexec/"name"
```

instead of:

```ruby
ln_s libexec/"name", bin
```

The symlinks created by `install_symlink` are guaranteed to be relative. `ln_s` will only produce a relative symlink when given a relative path.

Several other utilities for Ruby’s `Pathname` can simplify some common operations.

- To perform several operations within a directory, enclose them within a `cd <path> do` block:

```ruby
cd "src" do
  system "./configure", "--disable-debug", "--prefix=#{prefix}"
  system "make", "install"
end
```

- To surface one or more binaries buried in `libexec` or a macOS `.app` package, use `write_exec_script` or `write_jar_script`:

```ruby
bin.write_exec_script Dir[libexec/"bin/*"]
bin.write_exec_script prefix/"Package.app/Contents/MacOS/package"
bin.write_jar_script libexec/jar_file, "jarfile", java_version: "11"
```

- For binaries that require setting one or more environment variables to function properly, use `write_env_script` or `env_script_all_files`:

```ruby
(bin/"package").write_env_script libexec/"package", PACKAGE_ROOT: libexec
bin.env_script_all_files(libexec/"bin", PERL5LIB: ENV.fetch("PERL5LIB", nil))
```

### Rewriting a script shebang

Some formulae install executable scripts written in an interpreted language such as Python or Perl. Homebrew provides a `rewrite_shebang` method to rewrite the shebang of a script. This replaces a script’s original interpreter path with the one the formula depends on. This guarantees that the correct interpreter is used at execution time. This isn’t required if the build system already handles it (e.g. often with `pip` or Perl `ExtUtils::MakeMaker`).

For example, the `icdiff` formula uses this utility. Note that it is necessary to include the utility in the formula; for example with Python one must use `include Language::Python::Shebang`.

### Adding optional steps

**Note:** `option`s are not allowed in Homebrew/homebrew-core as they are not tested by CI.

If you want to add an `option`:

```ruby
class Yourformula < Formula
  # ...
  url "https://example.com/yourformula-1.0.tar.gz"
  sha256 "abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc1"
  # ...
  option "with-ham", "Description of the option"
  option "without-spam", "Another description"

  depends_on "bar" => :recommended
  depends_on "foo" => :optional # automatically adds a with-foo option # automatically adds a without-bar option
  # ...
end
```

And then to define the effects the `option`s have:

```ruby
if build.with? "ham"
  # note, no "with" in the option name (it is added by the build.with? method)
end

if build.without? "ham"
  # works as you'd expect. True if `--without-ham` was given.
end
```

`option` names should be prefixed with the words `with` or `without`. For example, an option to run a test suite should be named `--with-test` or `--with-check` rather than `--test`, and an option to enable a shared library `--with-shared` rather than `--shared` or `--enable-shared`. See the alternative `ffmpeg` formula for examples.

`option`s that aren’t `build.with?` or `build.without?` should be deprecated with `deprecated_option`. See the `wget` formula for a historical example.

### Running commands after installation

Any initialization steps that aren’t necessarily part of the install process can be located in a `post_install` block, such as setup commands or data directory creation. This block can be re-run separately with `brew postinstall <formula>`.

For simple file preparation, prefer `post_install_steps`. These steps are stored in the JSON API and do not require evaluating formula Ruby. A `post_install_steps` block may only contain the supported step calls with literal arguments. It cannot call the wider formula DSL or arbitrary Ruby code.

```ruby
class Foo < Formula
  # ...
  url "https://example.com/foo-1.0.tar.gz"

  post_install_steps do
    mkdir_p "log/foo"
    touch "foo/state"
    mv "default.conf", "foo/default.conf"
    ln_s "cert.pem", "foo/cert.pem", source_base: :relative
  end
  # ...
end
```

A formula may define either `post_install_steps` or `post_install`, not both.

#### File preparation steps

`mkdir`, `mkdir_p` and `touch` default to paths relative to `var`. `move`, `mv`, `move_children`, `symlink`, `ln_s` and `ln_sf` default their source and target paths to `prefix`. Use `base:`, `source_base:` or `target_base:` when a step needs another formula path such as `pkgetc`; use `source_base: :relative` for relative symlink sources.

- `mkdir`: create one directory; example: `mkdir "log/foo"`.
- `mkdir_p`: create a directory and any missing parents; example: `mkdir_p "log/foo"`.
- `touch`: create or update a file timestamp; example: `touch "foo/state"`.
- `move`: move one file or directory; example: `move "default.conf", "foo/default.conf"`.
- `mv`: alias for `move`; example: `mv "default.conf", "foo/default.conf"`.
- `move_children`: move the contents of one directory into another; example: `move_children "defaults", "foo/defaults"`.
- `symlink`: create a symlink; example: `symlink "cert.pem", "foo/cert.pem", source_base: :relative`.
- `ln_s`: alias for `symlink`; example: `ln_s "cert.pem", "foo/cert.pem", source_base: :relative`.
- `ln_sf`: create or replace a symlink; example: `ln_sf "cert.pem", "foo/cert.pem", source_base: :relative`.

#### Default config and template steps

`write` creates a default configuration or data file from literal content. It defaults to the same base as the other file preparation steps; pass `base:` (such as `base: :etc`) to target another formula path. By default `write` does not overwrite an existing file, so user edits are preserved across upgrades; pass `overwrite: true` to always replace the file.

- `write`: write literal content to a file unless it already exists; example: `write "foo.conf", "key = value", base: :etc`.
- `write` with `overwrite: true`: always replace the file; example: `write "foo/version", "1.0", overwrite: true`.

A trailing newline is appended unless the content already ends with one, so written files end in a newline as POSIX expects.

Content may use a fixed set of `tokens that are expanded at install time so paths are not hardcoded into the JSON API:`, `,`, `,`, `,`, `and`. Any other `` is left verbatim, so literal braces are never rewritten. Use tokens instead of Ruby interpolation, for example `write "foo.conf", "prefix = ", base: :etc`.

#### Desktop and cache rebuild steps

These steps rebuild shared desktop and cache state using Homebrew-owned tools.

- `compile_gsettings_schemas`: compile GSettings schemas in `share/glib-2.0/schemas`.
- `gio_querymodules`: rebuild the GIO module cache in `lib/gio/modules`.
- `gdk_pixbuf_query_loaders`: update the GDK Pixbuf loader cache.
- `gtk_update_icon_cache`: refresh the `hicolor` GTK icon cache.
- `update_mime_database`: rebuild the shared MIME database in `share/mime`.
- `update_desktop_database`: rebuild the desktop entry database in `share/applications`.

```ruby
class Foo < Formula
  # ...
  url "https://example.com/foo-1.0.tar.gz"

  def post_install
    rm pkgetc/"cert.pem" if File.exist?(pkgetc/"cert.pem")
    pkgetc.install_symlink Formula["ca-certificates"].pkgetc/"cert.pem"
  end
  # ...
end
```

In the above example, the `libressl` formula replaces its stock list of certificates with a symlink to that of the `ca-certificates` formula.

### Handling files that should persist over formula upgrades

For example, Ruby 1.9’s gems should be installed to `var/lib/ruby/` so that gems don’t need to be reinstalled when upgrading Ruby. You can usually do this with symlink trickery, or (ideally) a configure option.

Another example would be configuration files that should not be overwritten on package upgrades. If after installation you find that to-be-persisted configuration files are not copied but instead *symlinked* into `$(brew --prefix)/etc/` from the Cellar, this can often be rectified by passing an appropriate argument to the package’s configure script. That argument will vary depending on a given package’s configure script and/or Makefile, but one example might be: `--sysconfdir=#{etc}`

### Service files

There are two ways to add `launchd` plists and `systemd` services to a formula, so that `brew services` can pick them up:

#### Package-provided service file

If the package already provides a service file, it can be installed into the `prefix` directory and referenced by name:

```ruby
service do
  name macos: "custom.launchd.name",
       linux: "custom.systemd.name"
end
```

To find the file we append `.plist` to the `launchd` service name and `.service` to the `systemd` service name internally.

#### Formula-defined service file

If the formula does not provide a service file you can generate one using the following stanza:

```ruby
# 1. An individual command
service do
  run opt_bin/"script"
end

# 2. A command with arguments
service do
  run [opt_bin/"script", "--config", etc/"dir/config.yml"]
end

# 3. OS specific commands (If you omit one, the service file won't get generated for that OS.)
service do
  run macos: [opt_bin/"macos_script", "standalone"],
      linux: var/"special_linux_script"
end
```

#### Service block methods

This table lists the options you can set within a `service` block. The `run` or `name` field must be defined inside the service block. If `name` is defined without `run`, then Homebrew makes no attempt to change the package-provided service file according these fields. The `run` field indicates what command to run, instructs Homebrew to create a service description file using options set in the block, and therefore is required before using fields other than `name` and `require_root`.

| method | default | macOS | Linux | description |
|---|---|---|---|---|
| `run` | - | yes | yes | command to execute: an array with arguments or a path |
| `run_type` | `:immediate` | yes | yes | type of service: `:immediate`, `:interval` or `:cron` |
| `interval` | - | yes | yes | controls the start interval, required for the `:interval` type |
| `cron` | - | yes | yes | controls the trigger times, required for the `:cron` type |
| `keep_alive` | `false` | yes | yes | sets contexts in which the service will keep the process running |
| `launch_only_once` | `false` | yes | yes | whether the command should only run once |
| `require_root` | `false` | yes | yes | whether the service requires root access. If true, Homebrew hints at using `sudo` on various occasions, but does not enforce it |
| `environment_variables` | - | yes | yes | hash of variables to set |
| `working_dir` | - | yes | yes | directory to operate from |
| `root_dir` | - | yes | yes | directory to use as a chroot for the process |
| `input_path` | - | yes | yes | path to use as input for the process |
| `log_path` | - | yes | yes | path to write `stdout` to |
| `error_log_path` | - | yes | yes | path to write `stderr` to |
| `restart_delay` | - | yes | yes | number of seconds to delay before restarting a process |
| `throttle_interval` | - | yes | no-op | minimum seconds to wait before invocations (macOS default is `10`) |
| `process_type` | - | yes | no-op | type of process to manage: `:background`, `:standard`, `:interactive` or `:adaptive` |
| `macos_legacy_timers` | - | yes | no-op | timers created by `launchd` jobs are coalesced unless this is set |
| `sockets` | - | yes | no-op | socket that is created as an accesspoint to the service |
| `nice` | - | yes | yes | default scheduling priority (nice level), from `-20` highest to `19` lowest. **Note:** Negative nice values (higher priority) require `require_root: true` to be set. |
| `name` | - | yes | yes | a hash with the `launchd` service name on macOS and/or the `systemd` service name on Linux. Homebrew generates a default name for the service file if this is not present |

For services that are kept alive after starting you can use the default `run_type`:

```ruby
service do
  run [opt_bin/"beanstalkd", "test"]
  keep_alive true
  run_type :immediate # This should be omitted since it's the default
end
```

If a service needs to run on an interval, use `run_type :interval` and specify an interval:

```ruby
service do
  run [opt_bin/"beanstalkd", "test"]
  run_type :interval
  interval 500
end
```

If a service needs to run at certain times, use `run_type :cron` and specify a time with the crontab syntax:

```ruby
service do
  run [opt_bin/"beanstalkd", "test"]
  run_type :cron
  cron "5 * * * *"
end
```

Environment variables can be set with a hash. For the `PATH` there is the helper method `std_service_path_env` which returns `#{HOMEBREW_PREFIX}/bin:#{HOMEBREW_PREFIX}/sbin:/usr/bin:/bin:/usr/sbin:/sbin` so the service can find other `brew`-installed commands.

```ruby
service do
  run opt_bin/"beanstalkd"
  environment_variables PATH: std_service_path_env
end
```

#### `keep_alive` options

The standard options keep the service alive regardless of any status or circumstances:

```ruby
service do
  run [opt_bin/"beanstalkd", "test"]
  keep_alive true # or false
end
```

Same as above in hash form:

```ruby
service do
  run [opt_bin/"beanstalkd", "test"]
  keep_alive always: true
end
```

Keep alive until the service exits with a non-zero return code:

```ruby
service do
  run [opt_bin/"beanstalkd", "test"]
  keep_alive successful_exit: true
end
```

Keep alive only if the job crashed:

```ruby
service do
  run [opt_bin/"beanstalkd", "test"]
  keep_alive crashed: true
end
```

Keep alive as long as a file exists:

```ruby
service do
  run [opt_bin/"beanstalkd", "test"]
  keep_alive path: "/some/path"
end
```

#### `sockets` format

The `sockets` method accepts a formatted socket definition as `<type>://<host>:<port>`.

- `type`: `udp` or `tcp`
- `host`: host to run the socket on, e.g. `0.0.0.0`
- `port`: port number the socket should listen on

Please note that sockets will be accessible on IPv4 and IPv6 addresses by default.

If you only need one socket and you don’t care about the name (the default is `listeners`):

```rb
service do
  run [opt_bin/"beanstalkd", "test"]
  sockets "tcp://127.0.0.1:80"
end
```

If you need multiple sockets and/or you want to specify the name:

```rb
service do
  run [opt_bin/"beanstalkd", "test"]
  sockets http: "tcp://0.0.0.0:80", https: "tcp://0.0.0.0:443"
end
```

### Using environment variables

Homebrew has multiple levels of environment variable filtering which affects which variables are available to formulae.

Firstly, the overall environment in which Homebrew runs is filtered to avoid environment contamination breaking from-source builds. In particular, this process filters all but a select list of variables, plus allowing any prefixed with `HOMEBREW_`. The specific implementation is found in `bin/brew`.

The second level of filtering removes sensitive environment variables (such as credentials like keys, passwords or tokens) to prevent malicious subprocesses from obtaining them. This has the effect of preventing any such variables from reaching a formula’s Ruby code since they are filtered before it is called. The specific implementation is found in the `ENV.clear_sensitive_environment!` method.

In summary, any environment variables intended for use by a formula need to conform to these filtering rules in order to be available.

#### Setting environment variables during installation

You can set environment variables in a formula’s `install` or `test` blocks using `ENV["VARIABLE_NAME"] = "VALUE"`. An example can be seen in the `csound` formula.

Environment variables can also be set temporarily using the `with_env` method; any variables defined in the call to that method will be restored to their original values at the end of the block. An example can be seen in the `gh` formula.

There are also `ENV` helper methods available for many common environment variable setting and retrieval operations, such as:

- `ENV.cxx11` - compile with C++11 features enabled
- `ENV.deparallelize` - compile with only one job at a time; pass a block to have it only influence specific install steps
- `ENV.O0`, `ENV.O1`, `ENV.O3` - set a specific compiler optimization level (*default:* macOS: `-Os`, Linux: `-O2`)
- `ENV.runtime_cpu_detection` - account for formulae that detect CPU features at runtime
- `ENV.append_to_cflags` - add a value to `CFLAGS` `CXXFLAGS` `OBJCFLAGS` `OBJCXXFLAGS` all at once
- `ENV.prepend_create_path` - create and prepend a path to an existing list of paths
- `ENV.remove` - remove a string from an environment variable value
- `ENV.delete` - unset an environment variable

The full list can be found in the `SharedEnvExtension` module and `Superenv` module documentation.

### Deprecating and disabling a formula

See our Deprecating, Disabling and Removing documentation for more information about how and when to deprecate or disable a formula, cask or Homebrew code.


## Updating formulae

When a new version of the software is released, use `brew bump-formula-pr` to automatically update the `url` and `sha256`, remove any `revision` lines, and submit a pull request. See our How to Open a Homebrew Pull Request documentation for more information.


## Troubleshooting for new formulae

### Version detection failures

Homebrew tries to automatically determine the `version` from the `url` to avoid duplication. If the tarball has an unusual name you may need to manually assign the `version`.

### Bad makefiles

If a project’s makefile will not run in parallel, try to deparallelize by adding these lines to the formula’s `install` method:

```ruby
ENV.deparallelize
system "make" # separate compilation and installation steps
system "make", "install"
```

If that fixes it, please open an issue with the upstream project so that we can fix it for everyone.

### Still won’t work?

Check out what MacPorts and Fink do:

```sh
brew search --macports foo
brew search --fink foo
```

### Superenv notes

`superenv` is our “super environment” that isolates builds by removing `/usr/local/bin` and all user `PATH`s that are not essential for the build. It does this because user `PATH`s are often full of stuff that breaks builds. `superenv` also removes bad flags from the commands passed to `clang`/`gcc` and injects others (for example all `keg_only` dependencies are added to the `-I` and `-L` flags).

If in your local Homebrew build of your new formula, you see `Operation not permitted` errors, this will be because your new formula tried to write to the disk outside of your sandbox area. This is enforced on macOS by `sandbox-exec`.

### Fortran

Some software requires a Fortran compiler. This can be declared by adding `depends_on "gcc"` to a formula.

### MPI

Packages requiring MPI should use OpenMPI by adding `depends_on "open-mpi"` to the formula, rather than MPICH. These packages have conflicts and provide the same standardised interfaces. Choosing a default implementation and requiring its adoption allows software to link against multiple libraries that rely on MPI without creating unanticipated incompatibilities due to differing MPI runtimes.

### Linear algebra libraries

Packages requiring BLAS/LAPACK linear algebra interfaces should link to OpenBLAS by adding `depends_on "openblas"` and (if built with CMake) passing `-DBLA_VENDOR=OpenBLAS` to CMake, rather than Apple’s Accelerate framework or the default reference `lapack` implementation. Apple’s implementation of BLAS/LAPACK is outdated and may introduce hard-to-debug problems. The reference `lapack` formula is fine, although it is not actively maintained or tuned.


## How to start over (reset to upstream)

Have you created a real mess in Git which stops you from creating a commit you want to submit to us? You might want to consider starting again from scratch. Your changes to the Homebrew `main` branch can be reset by running:

```sh
git checkout -f main
git reset --hard origin/HEAD
```
