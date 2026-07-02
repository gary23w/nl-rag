---
title: "Download"
source: https://nixos.org/download/
domain: nixos
license: CC-BY-SA-4.0
tags: nixos distribution, declarative linux distribution, reproducible system configuration, immutable operating system
fetched: 2026-07-02
---

# Download

## Nix : the package manager

Current version

2.34.7

### Multi-user installation (recommended)

Install Nix via the recommended multi-user installation:

```
$ curl --proto '=https' --tlsv1.2 -L https://nixos.org/nix/install | sh -s -- --daemon
```

We recommend the multi-user install if you are on Linux running systemd, with SELinux disabled and you can authenticate with `sudo`.

### Single-user installation

Install Nix via the single-user installation:

```
$ curl --proto '=https' --tlsv1.2 -L https://nixos.org/nix/install | sh -s -- --no-daemon
```

Above command will perform a single-user installation of Nix, meaning that `nix` is owned by the invoking user. You should run this under your usual user account, not as `root`. The script will invoke `sudo` to create `/nix` if it doesn’t already exist.

### Which type of installation should you choose?

This depends on your requirements, but here is a short list of reasons why we recommend multi-user installation:

#### Pros

- Better build isolation (and that is what Nix is all about)
- Better security (a build can not write somewhere in your home)
- Sharing builds between users

#### Cons

- Requires `root` to run the daemon
- More involved installation (creation of `nixbld* users`, installing a systemd unit, …
- Harder to uninstall

### Multi-user installation

> **Updating to macOS 15 Sequoia**
> 
> If you recently updated to macOS 15 Sequoia and are getting
> 
> ```
> error: the user '_nixbld1' in the group 'nixbld' does not exist
> ```
> 
> when running Nix commands, refer to GitHub issue NixOS/nix#10892 for instructions to fix your installation without reinstalling.

Install Nix via the **recommended** multi-user installation. Open a Terminal (by pressing [Cmd] + [Space] and typing `terminal`) and run the following command:

```
$ curl --proto '=https' --tlsv1.2 -L https://nixos.org/nix/install | sh
```

We believe we have ironed out how to cleanly support the read-only root on modern macOS. Please consult the manual on details what the installation script does.

### Multi-user installation (Requires WSL with systemd enabled)

WSL versions 0.67.6 and above has systemd support. Follow Microsoft’s systemd guide to configure it, and then install Nix using:

```
$ curl --proto '=https' --tlsv1.2 -L https://nixos.org/nix/install | sh -s -- --daemon
```

### Single-user installation

Install Nix via the single-user installation

```
$ curl --proto '=https' --tlsv1.2 -L https://nixos.org/nix/install | sh -s -- --no-daemon
```

Start a Docker shell with Nix:

```
$ docker run -it nixos/nix
```

Or start a Docker shell with Nix exposing a `workdir` directory:

```
$ mkdir workdir
$ docker run -it -v $(pwd)/workdir:/workdir nixos/nix
```

The `workdir` example from above can be also used to start hacking on nixpkgs:

```
$ git clone --depth=1 https://github.com/NixOS/nixpkgs.git
$ docker run -it -v $(pwd)/nixpkgs:/nixpkgs nixos/nix
docker> nix-build -I nixpkgs=/nixpkgs -A hello nixpkgs/default.nix
docker> find ./result # this symlink points to the build package
```

The following release items are also available:

- Release notes
- Manual. Please read the “Quick Start” section of the manual for an overview of how to install and use Nix.
- Old releases are also available.

## NixOS : the Linux distribution

Current version

26.05
