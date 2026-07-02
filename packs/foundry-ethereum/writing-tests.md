---
title: "Testing – foundry"
source: https://book.getfoundry.sh/forge/writing-tests
domain: foundry-ethereum
license: Apache-2.0 / MIT (foundry book)
tags: foundry, forge testing, solidity fuzzing, anvil node
fetched: 2026-07-02
---

## Testing

Forge runs tests written in Solidity. Test files live in `test/` and test functions are prefixed with `test`.

```
$ forge test
```

```
Compiling...
No files changed, compilation skipped
Ran 2 tests for test/Counter.t.sol:CounterTest
[PASS] testFuzz_SetNumber(uint256) (runs: 256, μ: 50111, ~: 52529)
[PASS] test_Increment() (gas: 51847)
Suite result: ok. 2 passed; 0 failed; 0 skipped; finished in 6.23ms (5.99ms CPU time)
Ran 1 test suite in 9.07ms (6.23ms CPU time): 2 tests passed, 0 failed, 0 skipped (2 total tests)
```

### Writing tests

Create a test contract that inherits from `Test`:

test/Counter.t.sol

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;
 
import {Test} from "forge-std/Test.sol";
import {Counter} from "../src/Counter.sol";
 
contract CounterTest is Test {
    Counter counter;
 
    function setUp() public {
        counter = new Counter();
    }
 
    function test_Increment() public {
        counter.increment();
        assertEq(counter.number(), 1);
    }
 
    function test_SetNumber() public {
        counter.setNumber(42);
        assertEq(counter.number(), 42);
    }
}
```

Key conventions:

- Test files end with `.t.sol`
- Test contracts inherit from `forge-std/Test.sol`
- Test functions start with `test_` or `test`
- `setUp()` runs before each test

### Call isolation

Forge runs tests with call isolation enabled by default. In isolation mode, each top-level external call made by a test is executed as a separate transaction in a separate EVM context. This gives more precise gas accounting and transaction state changes for each call.

Because those calls use separate transaction contexts, a test function is not always equivalent to one normal transaction with warmed accounts or storage slots shared across every external call in the function body. For example, repeated calls to the same contract can be charged as cold again under isolation. If a test intentionally asserts behavior that depends on warm accounts or slots carrying across repeated calls in one transaction, run it with `--no-isolate` or set `isolate = false` in `foundry.toml`.

### Traces

Traces show a tree of all calls made during a test, helping you understand execution flow and debug failures.

#### Stack traces

When a test fails, use `-vvv` to see a stack trace showing exactly where the revert occurred. This is the most common way to debug test failures.

```
$ forge test -vvv
```

```
Solc 0.8.10 finished in 679.02ms
Compiler run successful!
Ran 1 test for test/FailingTest.t.sol:VaultTest
[FAIL: Unauthorized()] test_WithdrawAsNotOwner() (gas: 8418)
Traces:
  [8418] VaultTest::test_WithdrawAsNotOwner()
    ├─ [0] VM::prank(ECRecover: [0x0000000000000000000000000000000000000001])
    │   └─ ← [Return]
    ├─ [191] Vault::withdraw() [staticcall]
    │   └─ ← [Revert] Unauthorized()
    └─ ← [Revert] Unauthorized()
Backtrace:
  at Vault.withdraw
  at VaultTest.test_WithdrawAsNotOwner
Suite result: FAILED. 0 passed; 1 failed; 0 skipped; finished in 291.23µs (54.12µs CPU time)
Ran 1 test suite in 8.11ms (291.23µs CPU time): 0 tests passed, 1 failed, 0 skipped (1 total tests)
```

The trace shows the call hierarchy with the revert bubbling up, and the **Backtrace** pinpoints the exact location in your code.

#### Full traces

Use `-vvvv` to see traces for all tests, including passing ones. This helps you understand execution flow, verify call order, and check gas usage for individual operations.

```
$ forge test -vvvv
```

```
Compiling...
No files changed, compilation skipped
Ran 1 test for test/OwnerUpOnly.t.sol:OwnerUpOnlyTest
[PASS] test_IncrementAsOwner() (gas: 59372)
Traces:
  [59372] OwnerUpOnlyTest::test_IncrementAsOwner()
    ├─ [2407] OwnerUpOnly::count() [staticcall]
    │   └─ ← [Return] 0
    ├─ [43524] OwnerUpOnly::increment()
    │   └─ ← [Stop]
    ├─ [2407] OwnerUpOnly::count() [staticcall]
    │   └─ ← [Return] 1
    └─ ← [Stop]
Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 308.72µs (61.55µs CPU time)
Ran 1 test suite in 6.96ms (308.72µs CPU time): 1 tests passed, 0 failed, 0 skipped (1 total tests)
```

#### Reading traces

- **Gas costs** appear in brackets: `[29808]`
- **Contract and function names** are color-coded
- **Call types** are annotated: `[staticcall]` for view/pure functions
- **Return values** show what each call returned: `← [Return] 0` for a value, `← [Stop]` for void
- **Indentation** shows the call hierarchy—nested calls are indented under their parent

### Verbosity levels

Control how much detail Forge outputs with `-v` flags:

| Flag | Shows |
|---|---|
| (none) | Pass/fail summary only |
| `-v` | Test names |
| `-vv` | Logs emitted during tests |
| `-vvv` | Traces for failing tests |
| `-vvvv` | Traces for all tests, including setup |
| `-vvvvv` | Traces with storage changes |

Use `-vvv` for debugging failures, `-vvvv` when you need to see successful test execution, and `-vvvvv` when tracking state changes.

### Filtering tests

Run specific tests:

By name:

```
$ forge test --match-test test_DepositETH
```

```
Solc 0.8.10 finished in 706.49ms
Compiler run successful!
Ran 1 test for test/ComplicatedContract.t.sol:ComplicatedContractTest
[PASS] test_DepositETH() (gas: 107628)
Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 633.90µs (437.72µs CPU time)
Ran 1 test suite in 7.44ms (633.90µs CPU time): 1 tests passed, 0 failed, 0 skipped (1 total tests)
```

By contract:

```
$ forge test --match-contract ComplicatedContractTest
```

```
Compiling...
No files changed, compilation skipped
Ran 2 tests for test/ComplicatedContract.t.sol:ComplicatedContractTest
[PASS] test_DepositERC20() (gas: 179207)
[PASS] test_DepositETH() (gas: 107628)
Suite result: ok. 2 passed; 0 failed; 0 skipped; finished in 1.36ms (1.79ms CPU time)
Ran 1 test suite in 7.47ms (1.36ms CPU time): 2 tests passed, 0 failed, 0 skipped (2 total tests)
```

By path:

```
$ forge test --match-path test/ContractB.t.sol
```

```
Solc 0.8.10 finished in 668.46ms
Compiler run successful!
Ran 1 test for test/ContractB.t.sol:ContractBTest
[PASS] testExample() (gas: 257)
Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 202.65µs (35.48µs CPU time)
Ran 1 test suite in 6.84ms (202.65µs CPU time): 1 tests passed, 0 failed, 0 skipped (1 total tests)
```

Combine filters:

```
$ forge test --match-contract ComplicatedContractTest --match-test test_Deposit
```

```
Compiling...
No files changed, compilation skipped
Ran 2 tests for test/ComplicatedContract.t.sol:ComplicatedContractTest
[PASS] test_DepositERC20() (gas: 179207)
[PASS] test_DepositETH() (gas: 107628)
Suite result: ok. 2 passed; 0 failed; 0 skipped; finished in 1.62ms (1.94ms CPU time)
Ran 1 test suite in 7.50ms (1.62ms CPU time): 2 tests passed, 0 failed, 0 skipped (2 total tests)
```

Exclude tests with `--no-match-*` variants:

```
$ forge test --no-match-test test_Skip
```

### Fuzz testing

Forge automatically fuzzes test functions that take parameters:

```
function testFuzz_SetNumber(uint256 x) public {
    counter.setNumber(x);
    assertEq(counter.number(), x);
}
```

Forge generates random inputs and runs the test multiple times (256 by default):

```
$ forge test
```

```
Solc 0.8.10 finished in 668.68ms
Compiler run successful!
Ran 1 test for test/Safe.t.sol:SafeTest
[PASS] testFuzz_Withdraw(uint96) (runs: 256, μ: 40722, ~: 40932)
Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 6.52ms (6.19ms CPU time)
Ran 1 test suite in 8.91ms (6.52ms CPU time): 1 tests passed, 0 failed, 0 skipped (1 total tests)
```

Configure fuzzing:

foundry.toml

```
[fuzz]
runs = 1000
max_test_rejects = 65536
seed = "0x1234"
```

Constrain inputs with `vm.assume()`:

```
function testFuzz_Transfer(uint256 amount) public {
    vm.assume(amount > 0 && amount <= 1000 ether);
    // Test with constrained amount
}
```

Or use `bound()` to clamp values:

```
function testFuzz_Transfer(uint256 amount) public {
    amount = bound(amount, 1, 1000 ether);
    // Test with bounded amount
}
```

### Table testing

Foundry v1.3.0 comes with support for table testing, which enables the definition of a dataset (the "table") and the execution of a test function for each entry in that dataset. This approach helps ensure that certain combinations of inputs and conditions are tested.

In forge, table tests are functions named with `table` prefix that accepts datasets as one or multiple arguments:

```
function tableSumsTest(TestCase memory sums) public
```

```
function tableSumsTest(TestCase memory sums, bool enable) public
```

The datasets are defined as forge fixtures which can be:

- storage arrays prefixed with `fixture` prefix and followed by dataset name
- functions named with `fixture` prefix, followed by dataset name. Function should return an (fixed size or dynamic) array of values.

#### Single dataset

In following example, `tableSumsTest` test will be executed twice, with inputs from `fixtureSums` dataset: once with `TestCase(1, 2, 3)` and once with `TestCase(4, 5, 9)`.

```
struct TestCase {
    uint256 a;
    uint256 b;
    uint256 expected;
}
 
function fixtureSums() public returns (TestCase[] memory) {
    TestCase[] memory entries = new TestCase[](2);
    entries[0] = TestCase(1, 2, 3);
    entries[1] = TestCase(4, 5, 9);
    return entries;
}
 
function tableSumsTest(TestCase memory sums) public pure {
    require(sums.a + sums.b == sums.expected, "wrong sum");
}
```

It is required to name the `tableSumsTest`'s `TestCase` parameter `sums` as the parameter name is resolved against the available fixtures (`fixtureSums`). In this example, if the parameter is not named `sums` the following error is raised: `[FAIL: Table test should have fixtures defined]`.

#### Multiple datasets

`tableSwapTest` test will be executed twice, by using values at the same position from `fixtureWallet` and `fixtureSwap` datasets.

```
struct Wallet {
    address owner;
    uint256 amount;
}
 
struct Swap {
    bool swap;
    uint256 amount;
}
 
Wallet[] public fixtureWallet;
Swap[] public fixtureSwap;
 
function setUp() public {
    // first table test input
    fixtureWallet.push(Wallet(address(11), 11));
    fixtureSwap.push(Swap(true, 11));
 
    // second table test input
    fixtureWallet.push(Wallet(address(12), 12));
    fixtureSwap.push(Swap(false, 12));
}
 
function tableSwapTest(Wallet memory wallet, Swap memory swap) public pure {
    require(
        (wallet.owner == address(11) && swap.swap) || (wallet.owner == address(12) && !swap.swap), "not allowed"
    );
}
```

The same naming requirement mentioned above is relevant here.

### Mutation testing

Mutation testing checks the strength of your test suite by making small changes, or mutants, to your source code and re-running your tests. A mutant is killed when at least one test fails. A mutant survives when the changed code still passes the selected tests.

Run mutation testing with `forge test --mutate`:

```
$ forge test --mutate
```

Forge first runs the selected tests as a baseline. Mutation testing only starts if the baseline has at least one passing test and no failing tests.

#### Selecting files

Pass paths to mutate only those files:

```
$ forge test --mutate src/Vault.sol src/Token.sol
```

Use `--mutate-path` to select files with a glob pattern:

```
$ forge test --mutate --mutate-path 'src/**/*.sol'
```

Use `--mutate-contract` to select contracts by name:

```
$ forge test --mutate --mutate-contract 'Vault|Token'
```

`--mutate-path` and `--mutate-contract` cannot be combined. `--mutate-path` also cannot be combined with explicit paths passed to `--mutate`.

#### Selecting tests

Regular test filters still select the baseline tests and the tests run against each mutant:

```
$ forge test --mutate src/Vault.sol --match-contract VaultTest
```

This lets you scope a mutation run to the tests that should detect changes in a specific contract.

#### Parallel workers

Forge runs mutants in parallel. By default, it uses the number of logical CPU cores.

Set the worker count with `--mutation-jobs`:

```
$ forge test --mutate src/Vault.sol --mutation-jobs 4
```

Passing `0` also uses the number of logical CPU cores:

```
$ forge test --mutate src/Vault.sol --mutation-jobs 0
```

Parallel mutation testing uses isolated temporary workspaces per mutant. Dependency directories such as `lib`, `node_modules`, and `dependencies` are symlinked into those workspaces for performance.

#### Timeouts

Use `--mutation-timeout` to set a best-effort wall-clock timeout, in seconds, for each mutant:

```
$ forge test --mutate src/Vault.sol --mutation-timeout 30
```

Timed-out mutants are reported separately from killed, survived, skipped, and invalid mutants.

You can also configure the timeout in `foundry.toml`:

foundry.toml

```
[mutation]
timeout = 30
```

#### Operators

Mutation testing supports these operator groups:

- `assembly`
- `assignment`
- `binary-op`
- `delete-expression`
- `elim-delegate`
- `require`
- `unary-op`

All operator groups are enabled by default. Exclude specific operators in `foundry.toml`:

foundry.toml

```
[mutation]
exclude_operators = ["assembly", "elim-delegate"]
```

Use `include_operators` to re-enable operators that are excluded by default:

foundry.toml

```
[mutation]
include_operators = ["assembly"]
```

#### Reports

The report includes counts for:

- **Survived**: mutants that passed the selected tests
- **Killed**: mutants that caused a test failure
- **Invalid**: mutants that could not be compiled or run
- **Skipped**: redundant mutants on a span or expression after another mutant in that span survived
- **Timed out**: mutants that exceeded `mutation.timeout` or `--mutation-timeout`

Skipped and invalid counts can vary with `--mutation-jobs`, because higher parallelism can start more mutants before a survivor is known.

The mutation score is:

```
killed / (killed + survived)
```

Focus on survived mutants first. Each survived mutant points to the source location and mutation that your tests did not catch.

Survived mutants do not currently make `forge test --mutate` fail, and there is no threshold flag yet. To gate mutation testing in CI, run with `--json` and enforce your own threshold from the JSON output.

```
$ forge test --mutate --json
```

The JSON output has this shape:

```
{
  "summary": {
    "total": 12,
    "killed": 8,
    "survived": 2,
    "invalid": 1,
    "skipped": 1,
    "timed_out": 0,
    "mutation_score": 80.0,
    "duration_secs": 12.34
  },
  "survived_mutants": {
    "src/Vault.sol": [
      {
        "line": 42,
        "column": 17,
        "original": ">",
        "mutant": ">="
      }
    ]
  }
}
```

#### Limitations

Mutation testing cannot be combined with `--list`, `--debug`, `--flamegraph`, `--flamechart`, `--junit`, `--dump`, `--showmap`, or `--showmap-out`.

Mutation testing also rejects projects with `ffi = true`, write-capable file-system permissions that can reach symlinked dependency directories, or inline per-test network overrides.

### Symbolic testing

Symbolic testing explores your code with symbolic inputs instead of concrete ones, searching feasible execution paths within the current symbolic EVM model and configured bounds for a counterexample that violates a property. When Forge reports a failure, it first replays the concrete input or invariant sequence through the normal executor, so the failure is backed by a concrete example.

Symbolic tests are Solidity functions named `check*` or `prove*`. They are only discovered when symbolic mode is enabled with `--symbolic`:

```
contract MathSymbolicTest is Test {
    function check_average(uint256 a, uint256 b) external pure {
        uint256 average;
        unchecked {
            average = (a + b) / 2;
        }
 
        // Forge should find an overflow counterexample.
        assertGe(average, a <= b ? a : b);
    }
}
```

Run it with:

```
$ forge test --symbolic --match-test check_average
```

Symbolic testing requires an SMT solver to be installed. The default solver is `z3`:

```
$ brew install z3        # macOS
$ sudo apt-get install z3 # Ubuntu
```

#### Writing symbolic tests

Function parameters become symbolic inputs derived from the ABI, and the executor explores the feasible paths:

- `require(...)` and `vm.assume(...)` prune paths when their condition is false.
- `assert`, forge-std assertions, and DSTest failure signals are treated as properties to disprove.
- User reverts terminate the current path.

When `--symbolic` is enabled, `invariant*` and `statefulFuzz*` functions are explored as bounded symbolic call sequences instead of using the normal fuzzer.

#### Results

Forge reports symbolic outcomes as:

- **`PASS`**: every explored path finished without a feasible failure under the currently modeled semantics and configured bounds.
- **`FAIL`**: the solver found a failing input or invariant sequence, and Forge replayed it concretely before reporting it.
- **`FAIL: incomplete symbolic execution (...)` / `Incomplete`**: Forge could not complete the search or validate a counterexample. Treat this as "not established", not as a proof.

A `PASS` is scoped to the current symbolic model and configured bounds; it does not cover skipped dynamic lengths, deeper invariant sequences, larger loop bounds, unmodeled behavior, arbitrary unknown external code, or cryptographic preimage/collision properties.

#### Configuration

Tune the exploration bounds and solver in `foundry.toml`:

foundry.toml

```
[profile.default.symbolic]
solver = "z3"
timeout = 30
max_depth = 10000
max_paths = 1024
max_solver_queries = 10000
```

Symbolic exploration is bounded by configuration, including `symbolic.max_depth`, `symbolic.max_paths`, `symbolic.max_solver_queries`, dynamic calldata length settings, and `symbolic.invariant_depth`.

Bounds can also be set per test with inline `forge-config` annotations:

```
/// forge-config: default.symbolic.invariant_depth = 4
function invariant_counterNeverFive() public view {
    assertTrue(counter.value() != 5);
}
```

#### Limitations

The symbolic engine is not a complete revm-equivalent EVM model. Unsupported constructs report `incomplete` rather than a proof, and some supported semantics are bounded or approximate. Notable gaps include gas accounting, Cancun+ `SELFDESTRUCT`, arbitrary unknown external code, and cryptographic preimage or collision properties. The exact unsupported-feature reason is preserved in the test output.

### Testing reverts

Use `vm.expectRevert()` to test that a call reverts:

```
function test_RevertWhen_Unauthorized() public {
    vm.expectRevert("Not authorized");
    restricted.doSomething();
}
```

Match a custom error:

```
function test_RevertWhen_InsufficientBalance() public {
    vm.expectRevert(Token.InsufficientBalance.selector);
    token.transfer(address(0), 1000);
}
```

```
$ forge test --match-test "test_IncrementAsOwner|test_RevertWhen_CallerIsNotOwner" --match-path test/OwnerUpOnly.t.sol
```

```
Solc 0.8.10 finished in 698.47ms
Compiler run successful!
Ran 2 tests for test/OwnerUpOnly.t.sol:OwnerUpOnlyTest
[PASS] test_IncrementAsOwner() (gas: 59372)
[PASS] test_RevertWhen_CallerIsNotOwner() (gas: 29987)
Suite result: ok. 2 passed; 0 failed; 0 skipped; finished in 433.02µs (231.37µs CPU time)
Ran 1 test suite in 7.24ms (433.02µs CPU time): 2 tests passed, 0 failed, 0 skipped (2 total tests)
```

### Testing events

Use `vm.expectEmit()` to verify events are emitted:

```
function test_EmitsTransfer() public {
    vm.expectEmit(true, true, false, true);
    emit Transfer(alice, bob, 100);
    
    token.transfer(bob, 100);
}
```

The four booleans specify which topics and data to check.

### Forking

Test against live chain state:

```
$ forge test --fork-url https://ethereum.reth.rs/rpc
```

Or configure in `foundry.toml`:

foundry.toml

```
[profile.default]
eth_rpc_url = "https://ethereum.reth.rs/rpc"
```

Pin to a specific block for reproducible tests:

```
$ forge test --fork-url https://ethereum.reth.rs/rpc --fork-block-number 18000000
```

### Cheatcodes

Forge provides cheatcodes via the `vm` object to manipulate the test environment:

```
// Set block timestamp
vm.warp(1700000000);
 
// Set block number
vm.roll(18000000);
 
// Impersonate an address
vm.prank(alice);
contract.doSomething();
 
// Give ETH to an address
vm.deal(alice, 100 ether);
 
// Modify storage
vm.store(address(token), bytes32(0), bytes32(uint256(1000)));
```

See the cheatcodes reference for the full list.

### Watch mode

Re-run tests when files change:

```
$ forge test --watch
```

Was this helpful?

Suggest changes on GitHub
