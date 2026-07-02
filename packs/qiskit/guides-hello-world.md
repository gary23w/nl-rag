---
title: "Run your first circuit on hardware"
source: https://docs.quantum.ibm.com/guides/hello-world
domain: qiskit
license: Apache-2.0
tags: qiskit sdk, quantum sdk, quantum primitives, quantum circuit library
fetched: 2026-07-02
---

# Run your first circuit on hardware

- The code on this page was developed using the following requirements. We recommend using these versions or newer.`qiskit[all]~=2.4.0 qiskit-ibm-runtime~=0.46.1`

This example contains two parts. You will first create a simple "Hello world" quantum program and run it on a quantum processing unit (QPU). Because actual quantum research requires much more robust programs, in the second section (Scale to large numbers of qubits), you will scale the simple program up to utility level.

## Install and authenticate

1. If you have not already installed Qiskit, find instructions in the Quickstart guide.
  - Install Qiskit Runtime to run jobs on quantum hardware: `pip install qiskit-ibm-runtime`
  - Set up an environment to run Jupyter notebooks locally: `pip install jupyter`
2. Set up your authentication for access to quantum hardware through the free Open Plan. (If you were emailed an invitation to join an account, follow the steps for invited users instead.)
  - Go to IBM Quantum Platform to log in or create an account. ImportantIf you connect through a proxy server, you must use Qiskit Runtime v0.44.0 or later.
  - Generate your API key (also called an *API token*) on the dashboard, then copy it to a secure location.
  - Go to the Instances page and find the instance you want to use. Hover over its CRN and click to copy it.
  - Save your credentials locally with this code: from qiskit_ibm_runtime import QiskitRuntimeService QiskitRuntimeService.save_account( # For `token`, use the 44-character API_KEY you created # and saved from the IBM Quantum Platform Home dashboard token="<your-api-key>", instance="<CRN>", # Optional )
3. Now you can use this Python code any time you want to authenticate to the Qiskit Runtime Service: `from qiskit_ibm_runtime import QiskitRuntimeService # Run every time you need the service service = QiskitRuntimeService()`

Not using a trusted Python environment?

If you are using a public computer or other unsecured environment, follow the manual authentication instructions instead to keep your authentication credentials safe.

## Create and run a simple quantum program

The four steps to writing a quantum program using Qiskit patterns are:

1. Map the problem to a quantum-native format.
2. Optimize the circuits and operators.
3. Execute using a quantum primitive function.
4. Analyze the results.

### Step 1. Map the problem to a quantum-native format

In a quantum program, *quantum circuits* are the native format in which to represent quantum instructions, and *operators* represent the observables to be measured. When creating a circuit, you'll usually create a new `QuantumCircuit` object, then add instructions to it in sequence.

The following code cell creates a circuit that produces a *Bell state,* which is a state wherein two qubits are fully entangled with each other.

Note: bit ordering

The Qiskit SDK uses the LSb 0 bit numbering where the $n^{th}$ nth digit has value $1 \ll n$ 1≪n or $2^n$ 2n. For more details, see the Bit-ordering in the Qiskit SDK topic.

```
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime import EstimatorOptions
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from matplotlib import pyplot as plt
# Uncomment the next line if you want to use a simulator:
# from qiskit_ibm_runtime.fake_provider import FakeBelemV2

# Create a new circuit with two qubits
qc = QuantumCircuit(2)

# Add a Hadamard gate to qubit 0
qc.h(0)

# Perform a controlled-X gate on qubit 1, controlled by qubit 0
qc.cx(0, 1)

# Return a drawing of the circuit using MatPlotLib ("mpl").
# These guides are written by using Jupyter notebooks, which
# display the output of the last line of each cell.
# If you're running this in a script, use `print(qc.draw())` to
# print a text drawing.
qc.draw("mpl")
```

Output:

See `QuantumCircuit` in the documentation for all available operations.

When creating quantum circuits, you must also consider what type of data you want returned after execution. Qiskit provides two ways to return data: you can obtain sampling output for a set of qubits you choose to measure, or you can obtain the expectation value of an observable. Prepare your workload to measure your circuit in one of these two ways with Qiskit primitives (explained in detail in Step 3).

This example measures expectation values by using the `qiskit.quantum_info` submodule, which is specified by using operators (mathematical objects used to represent an action or process that changes a quantum state). The following code cell creates six two-qubit Pauli operators: `IZ`, `IX`, `ZI`, `XI`, `ZZ`, and `XX`.

```
# Set up six different observables.

observables_labels = ["IZ", "IX", "ZI", "XI", "ZZ", "XX"]
observables = [SparsePauliOp(label) for label in observables_labels]
```

Operator Notation

Here, something like the `ZZ` operator is a shorthand for the tensor product $Z\otimes Z$ Z⊗Z, which means measuring Z on qubit 1 and Z on qubit 0 together, and obtaining information about the correlation between qubit 1 and qubit 0. Expectation values like this are also typically written as $\langle Z_1 Z_0 \rangle$ ⟨Z1Z0⟩.

If the state is entangled, then the measurement of $\langle Z_1 Z_0 \rangle$ ⟨Z1Z0⟩ should be different from the measurement of $\langle I_1 \otimes Z_0 \rangle \langle Z_1 \otimes I_0 \rangle$ ⟨I1⊗Z0⟩⟨Z1⊗I0⟩. For the specific entangled state created by our circuit described above, the measurement of $\langle Z_1 Z_0 \rangle$ ⟨Z1Z0⟩ should be 1 and the measurement of $\langle I_1 \otimes Z_0 \rangle \langle Z_1 \otimes I_0 \rangle$ ⟨I1⊗Z0⟩⟨Z1⊗I0⟩ should be zero.

### Step 2. Optimize the circuits and operators

When executing circuits on a device, it is important to optimize the set of instructions that the circuit contains and minimize the overall depth (roughly the number of instructions) of the circuit. This ensures that you obtain the best results possible by reducing the effects of error and noise. Additionally, the circuit's instructions must conform to a backend device's Instruction Set Architecture (ISA) and must consider the device's basis gates and qubit connectivity.

The following code instantiates a real device to submit a job to and transforms the circuit and observables to match that backend's ISA. It requires that you have already saved your credentials

```
service = QiskitRuntimeService()

backend = service.least_busy(simulator=False, operational=True)

# Convert to an ISA circuit and layout-mapped observables.
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(qc)

isa_circuit.draw("mpl", idle_wires=False)
```

Output:

### Step 3. Execute using the quantum primitives

Quantum computers can produce random results, so you usually collect a sample of the outputs by running the circuit many times. You can estimate the value of the observable by using the `Estimator` class. `Estimator` is one of two primitives; the other is `Sampler`, which can be used to get data from a quantum computer. These objects possess a `run()` method that executes the selection of circuits, observables, and parameters (if applicable), using a primitive unified bloc (PUB).

```
# Construct the Estimator instance.

estimator = Estimator(mode=backend)
estimator.options.resilience_level = 1
estimator.options.default_shots = 5000

mapped_observables = [
    observable.apply_layout(isa_circuit.layout) for observable in observables
]

# One pub, with one circuit to run against five different observables.
job = estimator.run([(isa_circuit, mapped_observables)])

# Use the job ID to retrieve your job data later
print(f">>> Job ID: {job.job_id()}")
```

Output:

```
>>> Job ID: d8286mfoha1c73bl8hrg
```

After a job is submitted, you can wait until either the job is completed within your current python instance, or use the `job_id` to retrieve the data at a later time. (See the section on retrieving jobs for details.)

After the job completes, examine its output through the job's `result()` attribute.

```
# This is the result of the entire submission.  You submitted one Pub,
# so this contains one inner result (and some metadata of its own).
job_result = job.result()

# This is the result from our single pub, which had six observables,
# so contains information on all six.
pub_result = job.result()[0]
```

Alternative: run the example using a simulator

When you run your quantum program on a real device, your workload must wait in a queue before it runs. To save time, you can instead use the following code to run this small workload on the `fake_provider` with the Qiskit Runtime local testing mode. Note that this is only possible for a small circuit. When you scale up in the next section, you will need to use a real device.

```
# Use the following code instead if you want to run on a simulator:

from qiskit_ibm_runtime.fake_provider import FakeBelemV2
backend = FakeBelemV2()
estimator = Estimator(backend)

# Convert to an ISA circuit and layout-mapped observables.

pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(qc)
mapped_observables = [
    observable.apply_layout(isa_circuit.layout) for observable in observables
]

job = estimator.run([(isa_circuit, mapped_observables)])
result = job.result()

# This is the result of the entire submission. You submitted one Pub,
# so this contains one inner result (and some metadata of its own).

job_result = job.result()

# This is the result from our single pub, which had five observables,
# so contains information on all five.

pub_result = job.result()[0]
```

### Step 4. Analyze the results

The analyze step is typically where you might post-process your results using, for example, measurement error mitigation or zero noise extrapolation (ZNE). You might feed these results into another workflow for further analysis or prepare a plot of the key values and data. In general, this step is specific to your problem. For this example, plot each of the expectation values that were measured for our circuit.

The expectation values and standard deviations for the observables you specified to Estimator are accessed through the job result's `PubResult.data.evs` and `PubResult.data.stds` attributes. To obtain the results from Sampler, use the `PubResult.data.meas.get_counts()` function, which will return a `dict` of measurements in the form of bitstrings as keys and counts as their corresponding values. For more information, see the Sampler quickstart guide.

```
# Plot the result

values = pub_result.data.evs

errors = pub_result.data.stds

# plotting graph
plt.plot(observables_labels, values, "-o")
plt.xlabel("Observables")
plt.ylabel("Values")
plt.show()
```

Output:

Notice that for qubits 0 and 1, the independent expectation values of both X and Z are 0, while the correlations (`XX` and `ZZ`) are 1. This is a hallmark of quantum entanglement.

## Scale to large numbers of qubits

In quantum computing, utility-scale work is crucial for making progress in the field. Such work requires computations to be done on a much larger scale; working with circuits that might use over 100 qubits and over 1000 gates. This example demonstrates how you can accomplish utility-scale work on IBM® QPUs by creating and analyzing a 100-qubit GHZ state. It uses the Qiskit patterns workflow and ends by measuring the expectation value $\langle Z_0 Z_i \rangle$ ⟨Z0Zi⟩ for each qubit.

### Step 1. Map the problem

Write a function that returns a `QuantumCircuit` that prepares an n n-qubit GHZ state (essentially an extended Bell state), then use that function to prepare a 100-qubit GHZ state and collect the observables to be measured.

```
def get_qc_for_n_qubit_GHZ_state(n: int) -> QuantumCircuit:
    """This function will create a qiskit.QuantumCircuit (qc)
        for an n-qubit GHZ state.

    Args:
        n (int): Number of qubits in the n-qubit GHZ state

    Returns:
        QuantumCircuit: Quantum circuit that generate the n-qubit GHZ state,
            assuming all qubits start in the 0 state
    """
    if isinstance(n, int) and n >= 2:
        qc = QuantumCircuit(n)
        qc.h(0)
        for i in range(n - 1):
            qc.cx(i, i + 1)
    else:
        raise Exception("n is not a valid input")
    return qc

# Create a new circuit with 100 qubits in the GHZ state
n = 100
qc = get_qc_for_n_qubit_GHZ_state(n)
```

Next, map to the operators of interest. This example uses the `ZZ` operators between qubits to examine the behavior as they get farther apart. Increasingly inaccurate (corrupted) expectation values between distant qubits would reveal the level of noise present.

```
# ZZII...II, ZIZI...II, ... , ZIII...IZ
operator_strings = [
    "Z" + "I" * i + "Z" + "I" * (n - 2 - i) for i in range(n - 1)
]

operators = [SparsePauliOp(operator) for operator in operator_strings]
```

### Step 2. Optimize the problem for execution on quantum hardware

The following code transforms the circuit and observables to match the backend's ISA. It requires that you have already saved your credentials

```
service = QiskitRuntimeService()

backend = service.least_busy(
    simulator=False, operational=True, min_num_qubits=100
)
pm = generate_preset_pass_manager(optimization_level=1, backend=backend)

isa_circuit = pm.run(qc)
isa_operators_list = [op.apply_layout(isa_circuit.layout) for op in operators]
```

### Step 3. Execute on hardware

Submit the job and enable error suppression by using a technique to reduce errors called dynamical decoupling. The resilience level specifies how much resilience to build against errors. Higher levels generate more accurate results, at the expense of longer processing times. For further explanation of the options set in the following code, see Configure error mitigation for Qiskit Runtime.

```
options = EstimatorOptions()
options.resilience_level = 1
options.dynamical_decoupling.enable = True
options.dynamical_decoupling.sequence_type = "XY4"

# Create an Estimator object
estimator = Estimator(backend, options=options)
```

```
# Submit the circuit to Estimator
job = estimator.run([(isa_circuit, isa_operators_list)])
job_id = job.job_id()
print(job_id)
```

Output:

```
d828aeo0bvlc73d1vs20
```

### Step 4. Post-process results

After the job completes, plot the results and notice that $\langle Z_0 Z_i \rangle$ ⟨Z0Zi⟩ decreases with increasing i i, even though in an ideal simulation all $\langle Z_0 Z_i \rangle$ ⟨Z0Zi⟩ should be 1.

```
# data
data = list(range(1, len(operators) + 1))  # Distance between the Z operators
result = job.result()[0]
values = result.data.evs  # Expectation value at each Z operator.
values = [
    v / values[0] for v in values
]  # Normalize the expectation values to evaluate how they decay with distance.

# plotting graph
plt.plot(data, values, marker="o", label="100-qubit GHZ state")
plt.xlabel("Distance between qubits $i$")
plt.ylabel(r"$\langle Z_i Z_0 \rangle / \langle Z_1 Z_0 \rangle $")
plt.legend()
plt.show()
```

Output:

The previous plot shows that as the distance between qubits increases, the signal decays because of the presence of noise.

## Next steps

Recommendations

- Try one of these tutorials:
  - Ground-state energy estimation of the Heisenberg chain with VQE
  - Solve optimization problems using QAOA
  - Train quantum kernel models for machine learning tasks
- Find detailed installation instructions in the Install Qiskit guide.
- If you prefer not to install Qiskit locally, read about options to use Qiskit in an online development environment.
- To save multiple account credentials or to specify other account options, see detailed instructions in the Save your login credentials guide.

Report a bug, typo, or request content on

GitHub

.
