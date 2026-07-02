---
title: "Side-channel attack"
source: https://en.wikipedia.org/wiki/Side-channel_attack
domain: power-analysis-defense
license: CC-BY-SA-4.0
tags: power analysis countermeasure, differential power analysis defense, masking side channel defense, hiding leakage countermeasure
fetched: 2026-07-02
---

# Side-channel attack

In computer security, a **side-channel attack** is a type of security exploit that uses information inadvertently leaked by a system—such as timing, power consumption, or electromagnetic or acoustic emissions—to gain unauthorized access to sensitive information. These attacks differ from those targeting flaws in the design of cryptographic protocols or algorithms (notwithstanding the fact that cryptanalysis may identify vulnerabilities relevant to both types of attacks).

Some side-channel attacks require technical knowledge of the internal operation of the system, others such as differential power analysis are effective as black-box attacks. The rise of Web 2.0 applications and software-as-a-service has also significantly raised the possibility of side-channel attacks on the web, even when transmissions between a web browser and server are encrypted (e.g. through HTTPS or WiFi encryption), according to researchers from Microsoft Research and Indiana University.

Attempts to break a cryptosystem by deceiving or coercing people with legitimate access are not typically considered side-channel attacks: see social engineering and rubber-hose cryptanalysis.

General classes of side-channel attack include:

- Cache attack – attacks based on attacker's ability to monitor cache accesses made by the victim in a shared physical system as in virtualized environment or a type of cloud service.
- Timing attack – attacks based on measuring how much time various computations (such as, say, comparing an attacker's given password with the victim's unknown one) take to perform.
- Power-monitoring attack – attacks that make use of varying power consumption by the hardware during computation.
- Electromagnetic attack – attacks based on leaked electromagnetic radiation, which can directly provide plaintexts and other information. Such measurements can be used to infer cryptographic keys using techniques equivalent to those in power analysis or can be used in non-cryptographic attacks, e.g. TEMPEST (aka Van Eck phreaking or radiation monitoring) attacks.
- Acoustic cryptanalysis – attacks that exploit sound produced during a computation (rather like power analysis).
- Differential fault analysis – in which secrets are discovered by introducing faults in a computation.
- Data remanence – in which sensitive data are read after supposedly having been deleted. (e.g. cold boot attack)
- Software-initiated fault attacks – Currently a rare class of side channels, row hammer is an example in which off-limits memory can be changed by accessing adjacent memory too often (causing state retention loss).
- Whitelist – attacks based on the fact that the whitelisting devices will behave differently when communicating with whitelisted (sending back the responses) and non-whitelisted (not responding to the devices at all) devices. Whitelist-based side channel may be used to track Bluetooth MAC addresses.
- Optical – in which secrets and sensitive data can be read by visual recording using a high resolution camera, or other devices that have such capabilities (see examples below).

In all cases, the underlying principle is that physical effects caused by the operation of a cryptosystem (*on the side*) can provide useful extra information about secrets in the system, for example, the cryptographic key, partial state information, full or partial plaintexts and so forth. The term cryptophthora (secret degradation) is sometimes used to express the degradation of secret key material resulting from side-channel leakage.

## Examples

A **cache side-channel attack** works by monitoring security critical operations such as AES T-table entry or modular exponentiation or multiplication or memory accesses. The attacker then is able to recover the secret key depending on the accesses made (or not made) by the victim, deducing the encryption key. Also, unlike some of the other side-channel attacks, this method does not create a fault in the ongoing cryptographic operation and is invisible to the victim.

In 2017, two CPU vulnerabilities (dubbed Meltdown and Spectre) were discovered, which can use a cache-based side channel to allow an attacker to leak memory contents of other processes and the operating system itself.

*Timing attacks* monitor data movement into and out of the CPU or memory on the hardware running the cryptosystem or algorithm. Simply by observing variations in how long it takes to perform cryptographic operations, it might be possible to determine the entire secret key. Such attacks involve statistical analysis of timing measurements and have even been demonstrated across networks.

A *power analysis* attack can provide even more detailed information by observing the power consumption of a hardware device such as CPU or cryptographic circuit. These attacks are roughly categorized into simple power analysis (SPA) and differential power analysis (DPA). One example is Collide+Power, which affects nearly all CPUs. Other examples use machine learning approaches.

Fluctuations in current also generate radio waves, enabling attacks that analyze measurements of electromagnetic (EM) emanations. These attacks typically involve similar statistical techniques as power-analysis attacks.

A *deep-learning-based side-channel attack*, using the power and EM information across multiple devices has been demonstrated with the potential to break the secret key of a different but identical device in as low as a single trace.

Historical analogues to modern side-channel attacks are known. A recently declassified NSA document reveals that as far back as 1943, an engineer with Bell telephone observed decipherable spikes on an oscilloscope associated with the decrypted output of a certain encrypting teletype. According to former MI5 officer Peter Wright, the British Security Service analyzed emissions from French cipher equipment in the 1960s. In the 1980s, Soviet eavesdroppers were suspected of having planted bugs inside IBM Selectric typewriters to monitor the electrical noise generated as the type ball rotated and pitched to strike the paper; the characteristics of those signals could determine which key was pressed.

Power consumption of devices causes heating, which is offset by cooling effects. Temperature changes create thermally induced mechanical stress. This stress can create low level acoustic emissions from operating CPUs (about 10 kHz in some cases). Recent research by Shamir et al. has suggested that information about the operation of cryptosystems and algorithms can be obtained in this way as well. This is an *acoustic cryptanalysis attack*.

If the surface of the CPU chip, or in some cases the CPU package, can be observed, infrared images can also provide information about the code being executed on the CPU, known as a *thermal-imaging attack*.

An *optical side-channel attack* examples include gleaning information from the hard disk activity indicator to reading a small number of photons emitted by transistors as they change state.

*Allocation-based side channels* also exist and refer to the information that leaks from the allocation (as opposed to the use) of a resource such as network bandwidth to clients that are concurrently requesting the contended resource.

## Countermeasures

There are two primary categories of measures to counter side-channel attacks:

1. Eliminating or reducing emissions: This involves minimizing the unintended release of signals, such as electromagnetic radiation or timing variations, that attackers could exploit.
2. Transforming the secret data: Typically achieved through randomization, this approach ensures:
  - The cryptographic operation does not leak information that could be correlated with the secret data.
  - A subsequent transformation restores the intended result after the cryptographic operation.

Under the first category, displays with special shielding to lessen electromagnetic emissions, reducing susceptibility to TEMPEST attacks, are now commercially available. Power line conditioning and filtering can help deter power-monitoring attacks, although such measures must be used cautiously, since even very small correlations can remain and compromise security. Physical enclosures can reduce the risk of surreptitious installation of microphones (to counter acoustic attacks) and other micro-monitoring devices (against CPU power-draw or thermal-imaging attacks).

Another countermeasure (still in the first category) is to jam the emitted channel with noise. For instance, a random delay can be added to deter timing attacks, although adversaries can compensate for these delays by averaging multiple measurements (or, more generally, using more measurements in the analysis). When the amount of noise in the side channel increases, the adversary needs to collect more measurements.

Another countermeasure under the first category is to use security analysis software to identify certain classes of side-channel attacks that can be found during the design stages of the underlying hardware itself. Timing attacks and cache attacks are both identifiable through certain commercially available security analysis software platforms, which allow for testing to identify the attack vulnerability itself, as well as the effectiveness of the architectural change to circumvent the vulnerability. The most comprehensive method to employ this countermeasure is to create a Secure Development Lifecycle for hardware, which includes utilizing all available security analysis platforms at their respective stages of the hardware development lifecycle.

In the case of timing attacks against targets whose computation times are quantized into discrete clock cycle counts, an effective countermeasure against is to design the software to be isochronous, that is to run in an exactly constant amount of time, independently of secret values. This makes timing attacks impossible. Such countermeasures can be difficult to implement in practice, since even individual instructions can have variable timing on some CPUs.

One partial countermeasure against simple power attacks, but not differential power-analysis attacks, is to design the software so that it is "PC-secure" in the "program counter security model". In a PC-secure program, the execution path does not depend on secret values. In other words, all conditional branches depend only on public information. (This is a more restrictive condition than isochronous code, but a less restrictive condition than branch-free code.) Even though multiply operations draw more power than NOP on practically all CPUs, using a constant execution path prevents such operation-dependent power differences (differences in power from choosing one branch over another) from leaking any secret information. On architectures where the instruction execution time is not data-dependent, a PC-secure program is also immune to timing attacks.

Another way in which code can be non-isochronous is that modern CPUs have a memory cache: accessing infrequently used information incurs a large timing penalty, revealing some information about the frequency of use of memory blocks. Cryptographic code designed to resist cache attacks attempts to use memory in only a predictable fashion (like accessing only the input, outputs and program data, and doing so according to a fixed pattern). For example, data-dependent table lookups must be avoided because the cache could reveal which part of the lookup table was accessed.

Other partial countermeasures attempt to reduce the amount of information leaked from data-dependent power differences. Some operations use power that is correlated to the number of 1 bits in a secret value. Using a constant-weight code (such as using Fredkin gates or dual-rail encoding) can reduce the leakage of information about the Hamming weight of the secret value, although exploitable correlations are likely to remain unless the balancing is perfect. This "balanced design" can be approximated in software by manipulating both the data and its complement together.

Several "secure CPUs" have been built as asynchronous CPUs; they have no global timing reference. While these CPUs were intended to make timing and power attacks more difficult, subsequent research found that timing variations in asynchronous circuits are harder to remove.

Recently, white-box modeling was utilized to develop a low-overhead generic circuit-level countermeasure against both EM as well as power side-channel attacks. To minimize the effects of the higher-level metal layers in an IC acting as more efficient antennas, the idea is to embed the crypto core with a signature suppression circuit, routed locally within the lower-level metal layers, leading towards both power and EM side-channel attack immunity.

### Blinding

As a countermeasure for message encryption, **masking** (also known as **blinding**) is effective against all side-channel attacks. The principle of masking is to avoid manipulating any sensitive value y directly, but rather manipulate a sharing of it: a set of variables (called "shares") $y_{1},...,y_{d}$ such that $y=y_{1}\oplus ...\oplus y_{d}$ (where $\oplus$ is the XOR operation). An attacker must recover all the values of the shares to get any meaningful information.

In the case of RSA decryption with secret exponent d and corresponding encryption exponent e and modulus m , the technique applies as follows (for simplicity, the modular reduction by *m* is omitted in the formulas): before decrypting, that is, before computing the result of $y^{d}$ for a given ciphertext y , the system picks a random number r and encrypts it with public exponent e to obtain $r^{e}$ . Then, the decryption is done on $y\cdot r^{e}$ to obtain ${(y\cdot r^{e})}^{d}=y^{d}\cdot r^{e\cdot d}=y^{d}\cdot r$ . Since the decrypting system chose r , it can compute its inverse modulo m to cancel out the factor r in the result and obtain $y^{d}$ , the actual result of the decryption. For attacks that require collecting side-channel information from operations with data *controlled by the attacker*, blinding is an effective countermeasure, since the actual operation is executed on a randomized version of the data, over which the attacker has no control or even knowledge.
