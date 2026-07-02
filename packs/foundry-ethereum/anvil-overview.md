---
title: "Anvil – foundry"
source: https://book.getfoundry.sh/anvil/overview
domain: foundry-ethereum
license: Apache-2.0 / MIT (foundry book)
tags: foundry, forge testing, solidity fuzzing, anvil node
fetched: 2026-07-02
---

## Anvil

Anvil is a fast local Ethereum node for development and testing. It runs entirely in-memory and supports forking from any EVM-compatible chain.

### Key capabilities

| Feature | Description |
|---|---|
| **Local development** | Start a local node with pre-funded accounts and instant mining |
| **Forking** | Fork mainnet or any chain at a specific block |
| **State management** | Dump and load chain state for reproducible testing |
| **Custom RPC methods** | Impersonate accounts, manipulate time, and control mining |
| **Tracing** | Debug transactions with full execution traces |

### Common workflows

```
$ anvil
```

```
$ anvil --accounts 20
```

```
$ anvil --fork-url https://ethereum.reth.rs/rpc
```

```
$ anvil --fork-url https://ethereum.reth.rs/rpc --fork-block-number 18000000
```

Auto-impersonate

```
$ anvil --auto-impersonate
```

### Default accounts

Anvil generates 10 development accounts with 10,000 ETH each. The default mnemonic is:

```
test test test test test test test test test test test junk
```

You can customize accounts with `--accounts`, `--balance`, and `--mnemonic`.

### Learn more

- Forking — Fork mainnet and other chains
- State management — Dump and load chain state
- Custom methods — Impersonation, mining control, and time manipulation

Was this helpful?

Suggest changes on GitHub
