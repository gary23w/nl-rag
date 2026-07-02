---
title: "Deploying your contracts"
source: https://hardhat.org/hardhat-runner/docs/guides/deploying
domain: hardhat
license: MIT (hardhat docs)
tags: hardhat, hardhat network, solidity testing, contract deployment
fetched: 2026-07-02
---

# #Deploying your contracts

To deploy your contracts, you can use Hardhat Ignition, our declarative deployment system. You can deploy the `Lock` contract from the sample project by using its accompanying Ignition module. An Ignition module is a TypeScript or JavaScript file that allows you to specify what needs to be deployed.

In the sample project, the Ignition module `LockModule` which deploys the `Lock` contract, is under the `./ignition/modules` directory and looks like this:

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

You can deploy in the `localhost` network following these steps:

1. Start a local node `npx hardhat node`
2. Open a new terminal and deploy the Hardhat Ignition module in the `localhost` network TypeScriptJavaScript`npx hardhat ignition deploy ./ignition/modules/Lock.ts --network localhost``npx hardhat ignition deploy ./ignition/modules/Lock.js --network localhost`

As a general rule, you can target any network from your Hardhat config using:

```markup
npx hardhat ignition deploy ./ignition/modules/Lock.js --network <your-network>
```

If no network is specified, Hardhat Ignition will run against an in-memory instance of Hardhat Network.

In the sample `LockModule` above, two module parameters are used: `unlockTime` which will default to the 1st of Jan 2030 and `lockedAmount` which will default to one Gwei. You can learn more about overriding these values by providing your own module parameters during deployment in our Deploying a module guide.

Read more about Hardhat Ignition generally in the Hardhat Ignition documentation.
