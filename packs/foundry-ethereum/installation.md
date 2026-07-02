---
title: "Installation – foundry"
source: https://book.getfoundry.sh/getting-started/installation
domain: foundry-ethereum
license: Apache-2.0 / MIT (foundry book)
tags: foundry, forge testing, solidity fuzzing, anvil node
fetched: 2026-07-02
---

## Installation

Foundry is installed using **foundryup**, the official installer and version manager.

### Install foundryup

```
$ curl -L https://foundry.paradigm.xyz | bash
```

### Restart your terminal

Or run `source ~/.bashrc` / `source ~/.zshrc`.

### Install Foundry

```
$ foundryup
```

This installs the latest stable versions of `forge`, `cast`, `anvil`, and `chisel`.

## Updating

Run `foundryup` anytime to update to the latest stable release:

```
$ foundryup
```

## Installing specific versions

Install the nightly build

```
$ foundryup --install nightly
```

Install a specific version

```
$ foundryup --install 1.0.0
```

Install a specific nightly build

```
$ foundryup --install nightly-abc1234
```

Install from a branch

```
$ foundryup --branch master
```

## Tempo support

Tempo support ships in the main Foundry release as of v1.7.0. Install the normal toolchain:

```
$ foundryup
```

The old `foundryup -n tempo` / `foundryup --network tempo` flow is deprecated and ignored.

See the Tempo guide for project setup and MPP-backed RPC endpoints for paid RPC configuration.

## Binary verification

Foundry binaries are attested using GitHub artifact attestations. When installing via `foundryup`, binary hashes are automatically verified against the GitHub attestation.

To manually verify an installed binary:

```
$ gh attestation verify --owner foundry-rs $(which forge)
```

Use `foundryup --force` to skip verification and force a fresh install.

## Alternative installation methods

### Precompiled binaries

Download binaries directly from the GitHub releases page. Extract and add them to your `PATH`.

### Building from source

Requires Rust (latest stable). On Windows, also requires Visual Studio with the "Desktop Development With C++" workload.

Update Rust

```
$ rustup update stable
```

Install from GitHub

```
$ cargo install --git https://github.com/foundry-rs/foundry --profile release --locked forge cast chisel anvil
```

Or build from a local clone:

```
$ git clone https://github.com/foundry-rs/foundry.git
$ cd foundry
$ cargo install --path ./crates/forge --profile release --locked
$ cargo install --path ./crates/cast --profile release --locked
$ cargo install --path ./crates/anvil --profile release --locked
$ cargo install --path ./crates/chisel --profile release --locked
```

You can also use foundryup to build from source:

```
$ foundryup --branch master
$ foundryup --path /path/to/foundry
```

### Docker

```
$ docker pull ghcr.io/foundry-rs/foundry:latest
```

Or build locally from the repository:

```
$ docker build -t foundry .
```

### CI/CD

See the CI integration guide for GitHub Actions and other CI platforms.

## Uninstalling

Foundry stores all files in `~/.foundry`. To uninstall:

### Back up keystores

The `.foundry` directory may contain keystores with private keys.

### Remove the directory

```
$ rm -rf ~/.foundry
```

### Remove PATH entry

Edit your shell config (`.bashrc`, `.zshrc`, etc.) and remove the Foundry PATH line.

Was this helpful?

Suggest changes on GitHub
