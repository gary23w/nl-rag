---
title: "Cheatcodes Reference – foundry"
source: https://book.getfoundry.sh/forge/cheatcodes
domain: foundry-ethereum
license: Apache-2.0 / MIT (foundry book)
tags: foundry, forge testing, solidity fuzzing, anvil node
fetched: 2026-07-02
---

## Cheatcodes Reference

Cheatcodes give you powerful assertions, the ability to alter the state of the EVM, mock data, and more.

Cheatcodes are made available through use of the cheatcode address (`0x7109709ECfa91a80626fF3989D68f67F5b1DD12D`).

You can also access cheatcodes easily via `vm` available in Forge Standard Library's `Test` contract.

### Cheatcode Categories

Environment

Manipulate the EVM state: block timestamp, number, msg.sender, storage, balances, and more.

Assertions

Expect reverts, events, and calls in your tests.

Fuzzer

Control fuzzer behavior with assumptions and constraints.

Forking

Create and manage forks of live networks.

External

Interact with the outside world: run commands, read environment variables, parse JSON/TOML.

Signing

Sign messages and EIP-7702 delegations.

Utilities

Helper functions for addresses, labels, parsing, and wallets.

Files

Read and write files from your tests and scripts.

RPC

Register and interact with RPC endpoints.

State Snapshots

Snapshot and restore EVM state.

### Forge Standard Library

Forge Std implements wrappers around cheatcodes, which combine multiple standard cheatcodes to improve development experience. See Std Cheats for more details.

### Contributing

If you need a new cheatcode, consider contributing to the Foundry codebase.

### Cheatcodes Interface

The complete Solidity interface for all cheatcodes is available in the forge-std repository.

Was this helpful?

Suggest changes on GitHub
