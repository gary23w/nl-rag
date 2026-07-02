---
title: "Getting started with Hardhat"
source: https://hardhat.org/hardhat-runner/docs/getting-started
domain: hardhat
license: MIT (hardhat docs)
tags: hardhat, hardhat network, solidity testing, contract deployment
fetched: 2026-07-02
---

# Getting started with Hardhat

TIP

**Hardhat 2 is reaching end of life and is being replaced by Hardhat 3**

Hardhat 3 is stable and production ready, and teams are already migrating. Hardhat 2 will be upgraded to support the Glamsterdam hardfork and will continue to receive bug fixes and security fixes until its **end of life** — the earlier of the **Hegota mainnet activation** or the **1st of June 2027**. After that, there will be no further Hardhat 2 releases.

**Start your next project with Hardhat 3** with our getting started guide

## # Overview

Hardhat is a development environment for Ethereum software. It consists of different components for editing, compiling, debugging and deploying your smart contracts and dApps, all of which work together to create a complete development environment.

Hardhat Runner is the main component you interact with when using Hardhat. It's a flexible and extensible task runner that helps you manage and automate the recurring tasks inherent to developing smart contracts and dApps.

Hardhat Runner is designed around the concepts of **tasks** and **plugins**. Every time you're running Hardhat from the command-line, you're running a task. For example, `npx hardhat compile` runs the built-in `compile` task. Tasks can call other tasks, allowing complex workflows to be defined. Users and plugins can override existing tasks, making those workflows customizable and extendable.

This guide will take you through the installation of our recommended setup, but as most of Hardhat's functionality comes from plugins, you are free to customize it or choose a completely different path.

## # Installation

TIP

Hardhat for Visual Studio Code is the official Hardhat extension that adds advanced support for Solidity to VSCode. If you use Visual Studio Code, give it a try!

Hardhat is used through a local installation in your project. This way your environment will be reproducible, and you will avoid future version conflicts.

To install it, you need to create an npm project by going to an empty folder, running `npm init`, and following its instructions. You can use another package manager, like yarn, but we recommend you use npm 7 or later, as it makes installing Hardhat plugins simpler.

Once your project is ready, you should run

npm 7+

npm 6

yarn

pnpm

```markup
npm install --save-dev hardhat@hh2
```

```markup
npm install --save-dev hardhat@hh2
```

```markup
yarn add --dev hardhat@hh2
```

```markup
pnpm add -D hardhat@hh2
```

To use your local installation of Hardhat, you need to use `npx` to run it (i.e. `npx hardhat init`).

## # Quick Start

TIP

If you are using Windows, we **strongly recommend** using WSL 2 to follow this guide.

We will explore the basics of creating a Hardhat project with a sample contract, tests of that contract, and a Hardhat Ignition module to deploy it.

To create the sample project, run `npx hardhat init` in your project folder:

```markup
$ npx hardhat init
888    888                      888 888               888
888    888                      888 888               888
888    888                      888 888               888
8888888888  8888b.  888d888 .d88888 88888b.   8888b.  888888
888    888     "88b 888P"  d88" 888 888 "88b     "88b 888
888    888 .d888888 888    888  888 888  888 .d888888 888
888    888 888  888 888    Y88b 888 888  888 888  888 Y88b.
888    888 "Y888888 888     "Y88888 888  888 "Y888888  "Y888

👷 Welcome to Hardhat v2.28.6 👷‍

? What do you want to do? …
❯ Create a JavaScript project
  Create a TypeScript project
  Create a TypeScript project (with Viem)
  Create an empty hardhat.config.js
  Quit
```

Let's create the JavaScript or TypeScript project and go through these steps to compile, test and deploy the sample contract. We recommend using TypeScript, but if you are not familiar with it just pick JavaScript.

### #Running tasks

To first get a quick sense of what's available and what's going on, run `npx hardhat` in your project folder:

```markup
$ npx hardhat
Hardhat version 2.9.9

Usage: hardhat [GLOBAL OPTIONS] <TASK> [TASK OPTIONS]

GLOBAL OPTIONS:

  --config              A Hardhat config file.
  --emoji               Use emoji in messages.
  --help                Shows this message, or a task's help if its name is provided
  --max-memory          The maximum amount of memory that Hardhat can use.
  --network             The network to connect to.
  --show-stack-traces   Show stack traces.
  --tsconfig            A TypeScript config file.
  --verbose             Enables Hardhat verbose logging
  --version             Shows hardhat's version.

AVAILABLE TASKS:

  check                 Check whatever you need
  clean                 Clears the cache and deletes all artifacts
  compile               Compiles the entire project, building all artifacts
  console               Opens a hardhat console
  coverage              Generates a code coverage report for tests
  flatten               Flattens and prints contracts and their dependencies
  help                  Prints this message
  node                  Starts a JSON-RPC server on top of Hardhat Network
  run                   Runs a user-defined script after compiling the project
  test                  Runs mocha tests
  typechain             Generate Typechain typings for compiled contracts
  verify                Verifies contract on Etherscan

To get help for a specific task run: npx hardhat help [task]
```

The list of available tasks includes the built-in ones and also those that came with any installed plugins. `npx hardhat` is your starting point to find out what tasks are available to run.

### #Compiling your contracts

Next, if you take a look in the `contracts/` folder, you'll see `Lock.sol`:

```sol
pragma solidity ^0.8.28;

contract Lock {
    uint public unlockTime;
    address payable public owner;

    event Withdrawal(uint amount, uint when);

    constructor(uint _unlockTime) payable {
        require(
            block.timestamp < _unlockTime,
            "Unlock time should be in the future"
        );

        unlockTime = _unlockTime;
        owner = payable(msg.sender);
    }

    function withdraw() public {
        
        

        require(block.timestamp >= unlockTime, "You can't withdraw yet");
        require(msg.sender == owner, "You aren't the owner");

        emit Withdrawal(address(this).balance, block.timestamp);

        owner.transfer(address(this).balance);
    }
}
```

To compile it, simply run:

```markup
npx hardhat compile
```

If you created a TypeScript project, this task will also generate TypeScript bindings using TypeChain.

### #Testing your contracts

Your project comes with tests that use Mocha, Chai, Ethers.js and Hardhat Ignition.

If you take a look in the `test/` folder, you'll see a test file:

TypeScript

JavaScript

```ts
import {
  time,
  loadFixture,
} from "@nomicfoundation/hardhat-toolbox/network-helpers";
import { anyValue } from "@nomicfoundation/hardhat-chai-matchers/withArgs";
import { expect } from "chai";
import hre from "hardhat";

describe("Lock", function () {
  
  
  
  async function deployOneYearLockFixture() {
    const ONE_YEAR_IN_SECS = 365 * 24 * 60 * 60;
    const ONE_GWEI = 1_000_000_000;

    const lockedAmount = ONE_GWEI;
    const unlockTime = (await time.latest()) + ONE_YEAR_IN_SECS;

    
    const [owner, otherAccount] = await hre.ethers.getSigners();

    const Lock = await hre.ethers.getContractFactory("Lock");
    const lock = await Lock.deploy(unlockTime, { value: lockedAmount });

    return { lock, unlockTime, lockedAmount, owner, otherAccount };
  }

  describe("Deployment", function () {
    it("Should set the right unlockTime", async function () {
      const { lock, unlockTime } = await loadFixture(deployOneYearLockFixture);

      expect(await lock.unlockTime()).to.equal(unlockTime);
    });

    it("Should set the right owner", async function () {
      const { lock, owner } = await loadFixture(deployOneYearLockFixture);

      expect(await lock.owner()).to.equal(owner.address);
    });

    it("Should receive and store the funds to lock", async function () {
      const { lock, lockedAmount } = await loadFixture(
        deployOneYearLockFixture
      );

      expect(await hre.ethers.provider.getBalance(lock.target)).to.equal(
        lockedAmount
      );
    });

    it("Should fail if the unlockTime is not in the future", async function () {
      
      const latestTime = await time.latest();
      const Lock = await hre.ethers.getContractFactory("Lock");
      await expect(Lock.deploy(latestTime, { value: 1 })).to.be.revertedWith(
        "Unlock time should be in the future"
      );
    });
  });

  describe("Withdrawals", function () {
    describe("Validations", function () {
      it("Should revert with the right error if called too soon", async function () {
        const { lock } = await loadFixture(deployOneYearLockFixture);

        await expect(lock.withdraw()).to.be.revertedWith(
          "You can't withdraw yet"
        );
      });

      it("Should revert with the right error if called from another account", async function () {
        const { lock, unlockTime, otherAccount } = await loadFixture(
          deployOneYearLockFixture
        );

        
        await time.increaseTo(unlockTime);

        
        await expect(lock.connect(otherAccount).withdraw()).to.be.revertedWith(
          "You aren't the owner"
        );
      });

      it("Shouldn't fail if the unlockTime has arrived and the owner calls it", async function () {
        const { lock, unlockTime } = await loadFixture(
          deployOneYearLockFixture
        );

        
        await time.increaseTo(unlockTime);

        await expect(lock.withdraw()).not.to.be.reverted;
      });
    });

    describe("Events", function () {
      it("Should emit an event on withdrawals", async function () {
        const { lock, unlockTime, lockedAmount } = await loadFixture(
          deployOneYearLockFixture
        );

        await time.increaseTo(unlockTime);

        await expect(lock.withdraw())
          .to.emit(lock, "Withdrawal")
          .withArgs(lockedAmount, anyValue); 
      });
    });

    describe("Transfers", function () {
      it("Should transfer the funds to the owner", async function () {
        const { lock, unlockTime, lockedAmount, owner } = await loadFixture(
          deployOneYearLockFixture
        );

        await time.increaseTo(unlockTime);

        await expect(lock.withdraw()).to.changeEtherBalances(
          [owner, lock],
          [lockedAmount, -lockedAmount]
        );
      });
    });
  });
});
```

```js
const {
  time,
  loadFixture,
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");
const { anyValue } = require("@nomicfoundation/hardhat-chai-matchers/withArgs");
const { expect } = require("chai");

describe("Lock", function () {
  
  
  
  async function deployOneYearLockFixture() {
    const ONE_YEAR_IN_SECS = 365 * 24 * 60 * 60;
    const ONE_GWEI = 1_000_000_000;

    const lockedAmount = ONE_GWEI;
    const unlockTime = (await time.latest()) + ONE_YEAR_IN_SECS;

    
    const [owner, otherAccount] = await ethers.getSigners();

    const Lock = await ethers.getContractFactory("Lock");
    const lock = await Lock.deploy(unlockTime, { value: lockedAmount });

    return { lock, unlockTime, lockedAmount, owner, otherAccount };
  }

  describe("Deployment", function () {
    it("Should set the right unlockTime", async function () {
      const { lock, unlockTime } = await loadFixture(deployOneYearLockFixture);

      expect(await lock.unlockTime()).to.equal(unlockTime);
    });

    it("Should set the right owner", async function () {
      const { lock, owner } = await loadFixture(deployOneYearLockFixture);

      expect(await lock.owner()).to.equal(owner.address);
    });

    it("Should receive and store the funds to lock", async function () {
      const { lock, lockedAmount } = await loadFixture(
        deployOneYearLockFixture
      );

      expect(await ethers.provider.getBalance(lock.target)).to.equal(
        lockedAmount
      );
    });

    it("Should fail if the unlockTime is not in the future", async function () {
      
      const latestTime = await time.latest();
      const Lock = await ethers.getContractFactory("Lock");
      await expect(Lock.deploy(latestTime, { value: 1 })).to.be.revertedWith(
        "Unlock time should be in the future"
      );
    });
  });

  describe("Withdrawals", function () {
    describe("Validations", function () {
      it("Should revert with the right error if called too soon", async function () {
        const { lock } = await loadFixture(deployOneYearLockFixture);

        await expect(lock.withdraw()).to.be.revertedWith(
          "You can't withdraw yet"
        );
      });

      it("Should revert with the right error if called from another account", async function () {
        const { lock, unlockTime, otherAccount } = await loadFixture(
          deployOneYearLockFixture
        );

        
        await time.increaseTo(unlockTime);

        
        await expect(lock.connect(otherAccount).withdraw()).to.be.revertedWith(
          "You aren't the owner"
        );
      });

      it("Shouldn't fail if the unlockTime has arrived and the owner calls it", async function () {
        const { lock, unlockTime } = await loadFixture(
          deployOneYearLockFixture
        );

        
        await time.increaseTo(unlockTime);

        await expect(lock.withdraw()).not.to.be.reverted;
      });
    });

    describe("Events", function () {
      it("Should emit an event on withdrawals", async function () {
        const { lock, unlockTime, lockedAmount } = await loadFixture(
          deployOneYearLockFixture
        );

        await time.increaseTo(unlockTime);

        await expect(lock.withdraw())
          .to.emit(lock, "Withdrawal")
          .withArgs(lockedAmount, anyValue); 
      });
    });

    describe("Transfers", function () {
      it("Should transfer the funds to the owner", async function () {
        const { lock, unlockTime, lockedAmount, owner } = await loadFixture(
          deployOneYearLockFixture
        );

        await time.increaseTo(unlockTime);

        await expect(lock.withdraw()).to.changeEtherBalances(
          [owner, lock],
          [lockedAmount, -lockedAmount]
        );
      });
    });
  });
});
```

You can run your tests with `npx hardhat test`:

TypeScript

JavaScript

```markup
$ npx hardhat test
Generating typings for: 2 artifacts in dir: typechain-types for target: ethers-v6
Successfully generated 6 typings!
Compiled 2 Solidity files successfully

  Lock
    Deployment
      ✔ Should set the right unlockTime (610ms)
      ✔ Should set the right owner
      ✔ Should receive and store the funds to lock
      ✔ Should fail if the unlockTime is not in the future
    Withdrawals
      Validations
        ✔ Should revert with the right error if called too soon
        ✔ Should revert with the right error if called from another account
        ✔ Shouldn't fail if the unlockTime has arrived and the owner calls it
      Events
        ✔ Should emit an event on withdrawals
      Transfers
        ✔ Should transfer the funds to the owner

  9 passing (790ms)
```

```markup
$ npx hardhat test
Compiled 2 Solidity files successfully

  Lock
    Deployment
      ✔ Should set the right unlockTime (610ms)
      ✔ Should set the right owner
      ✔ Should receive and store the funds to lock
      ✔ Should fail if the unlockTime is not in the future
    Withdrawals
      Validations
        ✔ Should revert with the right error if called too soon
        ✔ Should revert with the right error if called from another account
        ✔ Shouldn't fail if the unlockTime has arrived and the owner calls it
      Events
        ✔ Should emit an event on withdrawals
      Transfers
        ✔ Should transfer the funds to the owner

  9 passing (790ms)
```

### #Deploying your contracts

Next, to deploy the contract we will use a Hardhat Ignition module.

Inside the `ignition/modules` folder you will find a file with the following code:

TypeScript

JavaScript

```ts
import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

const JAN_1ST_2030 = 1893456000;
const ONE_GWEI: bigint = 1_000_000_000n;

const LockModule = buildModule("LockModule", (m) => {
  const unlockTime = m.getParameter("unlockTime", JAN_1ST_2030);
  const lockedAmount = m.getParameter("lockedAmount", ONE_GWEI);

  const lock = m.contract("Lock", [unlockTime], {
    value: lockedAmount,
  });

  return { lock };
});

export default LockModule;
```

```js
const { buildModule } = require("@nomicfoundation/hardhat-ignition/modules");

const JAN_1ST_2030 = 1893456000;
const ONE_GWEI = 1_000_000_000n;

module.exports = buildModule("LockModule", (m) => {
  const unlockTime = m.getParameter("unlockTime", JAN_1ST_2030);
  const lockedAmount = m.getParameter("lockedAmount", ONE_GWEI);

  const lock = m.contract("Lock", [unlockTime], {
    value: lockedAmount,
  });

  return { lock };
});
```

TypeScript

JavaScript

You can deploy it using `npx hardhat ignition deploy ./ignition/modules/Lock.ts`:

```markup
$ npx hardhat ignition deploy ./ignition/modules/Lock.ts
Compiled 1 Solidity file successfully (evm target: paris).
You are running Hardhat Ignition against an in-process instance of Hardhat Network.
This will execute the deployment, but the results will be lost.
You can use --network <network-name> to deploy to a different network.

Hardhat Ignition 🚀

Deploying [ LockModule ]

Batch #1
  Executed LockModule#Lock

[ LockModule ] successfully deployed 🚀

Deployed Addresses

LockModule#Lock - 0x5FbDB2315678afecb367f032d93F642f64180aa3
```

You can deploy it using `npx hardhat ignition deploy ./ignition/modules/Lock.js`:

```markup
$ npx hardhat ignition deploy ./ignition/modules/Lock.js
Compiled 1 Solidity file successfully (evm target: paris).
You are running Hardhat Ignition against an in-process instance of Hardhat Network.
This will execute the deployment, but the results will be lost.
You can use --network <network-name> to deploy to a different network.

Hardhat Ignition 🚀

Deploying [ LockModule ]

Batch #1
  Executed LockModule#Lock

[ LockModule ] successfully deployed 🚀

Deployed Addresses

LockModule#Lock - 0x5FbDB2315678afecb367f032d93F642f64180aa3
```

To learn more check out the Hardhat Ignition documentation.

### #Connecting a wallet or Dapp to Hardhat Network

By default, Hardhat will spin up a new in-memory instance of Hardhat Network on startup. It's also possible to run Hardhat Network in a standalone fashion so that external clients can connect to it. This could be a wallet, your Dapp front-end, or a Hardhat Ignition deployment.

To run Hardhat Network in this way, run `npx hardhat node`:

```markup
$ npx hardhat node
Started HTTP and WebSocket JSON-RPC server at http://127.0.0.1:8545/
```

This will expose a JSON-RPC interface to Hardhat Network. To use it connect your wallet or application to `http://127.0.0.1:8545`.

If you want to connect Hardhat to this node, for example to run a deployment against it, you simply need to run it using `--network localhost`.

To try this, start a node with `npx hardhat node` and re-run the deployment using the `network` option:

TypeScript

JavaScript

```markup
npx hardhat ignition deploy ./ignition/modules/Lock.ts --network localhost
```

```markup
npx hardhat ignition deploy ./ignition/modules/Lock.js --network localhost
```

To run Hardhat Network on specific port and allow incoming requests from a specific network interface or hostname, run `npx hardhat node --hostname 127.0.0.1 --port 8545`.

If you want to allow incoming requests from anywhere, including external ips, use `--hostname 0.0.0.0`.

Congrats! You have created a project and compiled, tested and deployed a smart contract.

Show us some love by starring our repository on GitHub!️
