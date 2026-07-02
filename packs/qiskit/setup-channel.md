---
title: "Set up your IBM Cloud account"
source: https://docs.quantum.ibm.com/guides/setup-channel
domain: qiskit
license: Apache-2.0
tags: qiskit sdk, quantum sdk, quantum primitives, quantum circuit library
fetched: 2026-07-02
---

# Set up your IBM Cloud account

If you were emailed an invitation to join an account, follow the steps in Set up your IBM Cloud account - invited users instead.

You can run workloads on IBM® quantum processing units (QPUs) by setting up an account on IBM Cloud®. You will also need to install and set up Qiskit and Qiskit Runtime.

Your user account is associated with one or more instances identified by *Cloud Resource Names* (CRNs) that give access to IBM Quantum services. Additionally, a unique API token (also called a key) is assigned to each account, allowing for IBM Quantum access from Qiskit. For instructions to choose a specific instance, see Connect to an instance.

## Set up to use IBM Cloud

### Before you begin

1. If you do not already have one, set up an IBM Cloud account. NoteYou can be part of multiple IBM Cloud accounts. You can access any of your IBM Cloud accounts at any time from the account switcher in the header of the IBM Quantum Platform interface.
2. Log in to IBM Quantum Platform with an IBMid or Google account. If you don't have one, you are guided through creating one. (These login credentials are not your IBM Cloud account credentials.)
3. Make sure that the correct account and region are selected in the account switcher in the header, as shown in the following image. The region controls where your jobs are run and where the job data is kept. You can access either region by using the same API key, but you can only see and access the instances that were created in the region that you're logged in to. (The IBM Quantum Platform header is shown. The account switcher is to the right of the search bar. The region switcher is to the right of the account switcher.)

### 1. Create an instance

You can create an instance from the IBM Quantum Platform Instances page. See Create an instance for detailed instructions.

### 2. Optional: Save your access credentials

If you are using a trusted Python environment, such as a personal laptop, it is recommended that you use the `save_account()` method to save your credentials locally.

### 3. Connect Qiskit with your service instance

- Initialize the service in a **trusted Python environment**
- Initialize the service in an **untrusted environment** (such as a public computer)

Notes

- Follow these instructions if you want to connect by using the REST API instead of using Qiskit.
- If necessary, use this information to configure your firewall to enable access to the IBM Quantum API endpoints.

## Next steps

Recommendations

- Overview of available plans.
- Configure the Qiskit SDK locally.
- View your available QPUs.
- Follow the steps in the Run your first circuit on hardware guide to write and run a quantum program.
- Set up to use IBM Quantum Platform with REST API.
- Try a tutorial.

Report a bug, typo, or request content on

GitHub

.
