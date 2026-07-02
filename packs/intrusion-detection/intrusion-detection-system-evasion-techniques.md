---
title: "Intrusion detection system evasion techniques"
source: https://en.wikipedia.org/wiki/Intrusion_detection_system_evasion_techniques
domain: intrusion-detection
license: CC-BY-SA-4.0
tags: intrusion detection system, host based intrusion detection, network intrusion detection, intrusion prevention system, anomaly detection
fetched: 2026-07-02
---

# Intrusion detection system evasion techniques

**Intrusion detection system evasion techniques** are modifications made to attacks in order to prevent detection by an intrusion detection system (IDS). Almost all published evasion techniques modify network attacks. The 1998 paper *Insertion, Evasion, and Denial of Service: Eluding Network Intrusion Detection* popularized IDS evasion, and discussed both evasion techniques and areas where the correct interpretation was ambiguous depending on the targeted computer system. The 'fragroute' and 'fragrouter' programs implement evasion techniques discussed in the paper. Many web vulnerability scanners, such as 'Nikto', 'whisker' and 'Sandcat', also incorporate IDS evasion techniques.

Most IDSs have been modified to detect or even reverse basic evasion techniques, but IDS evasion (and countering IDS evasion) are still active fields.

## Obfuscation

An IDS can be evaded by obfuscating or encoding the attack payload in a way that the target computer will reverse but the IDS will not. In this way, an attacker can exploit the end host without alerting the IDS.

### Encoding

Application layer protocols like HTTP allow for multiple encodings of data which are interpreted as the same value. For example, the string "cgi-bin" in a URL can be encoded as "%63%67%69%2d%62%69%6e" (i.e., in hexadecimal). A web server will view these as the same string and act on them accordingly. An IDS must be aware of all of the possible encodings that its end hosts accept in order to match network traffic to known-malicious signatures.

Attacks on encrypted protocols such as HTTPS cannot be read by an IDS unless the IDS has a copy of the private key used by the server to encrypt the communication. The IDS won't be able to match the encrypted traffic to signatures if it doesn't account for this.

### Polymorphism

Signature-based IDS often look for common attack patterns to match malicious traffic to signatures. To detect buffer overflow attacks, an IDS might look for the evidence of NOP slides which are used to weaken the protection of address space layout randomization.

To obfuscate their attacks, attackers can use polymorphic shellcode to create unique attack patterns. This technique typically involves encoding the payload in some fashion (e.g., XOR-ing each byte with 0x95), then placing a decoder in front of the payload before sending it. When the target executes the code, it runs the decoder which rewrites the payload into its original form which the target then executes.

Polymorphic attacks don't have a single detectable signature, making them very difficult for signature-based IDS, and even some anomaly-based IDS, to detect. Shikata ga nai ("it cannot be helped") is a popular polymorphic encoder in the Metasploit framework used to convert malicious shellcode into difficult-to-detect polymorphic shellcode using XOR additive feedback.

## Evasion

Attackers can evade IDS by crafting packets in such a way that the end host interprets the attack payload correctly while the IDS either interprets the attack incorrectly or determines that the traffic is benign too quickly.

### Fragmentation and small packets

One basic technique is to split the attack payload into multiple small packets, so that the IDS must reassemble the packet stream to detect the attack. A simple way of splitting packets is by fragmenting them, but an adversary can also simply craft packets with small payloads. The 'whisker' evasion tool calls crafting packets with small payloads 'session splicing'.

By itself, small packets will not evade any IDS that reassembles packet streams. However, small packets can be further modified in order to complicate reassembly and detection. One evasion technique is to pause between sending parts of the attack, hoping that the IDS will time out before the target computer does. A second evasion technique is to send the packets out of order,

### Overlapping fragments and TCP segments

Another evasion technique is to craft a series of packets with TCP sequence numbers configured to overlap. For example, the first packet will include 80 bytes of payload but the second packet's sequence number will be 76 bytes after the start of the first packet. When the target computer reassembles the TCP stream, they must decide how to handle the four overlapping bytes. Some operating systems will take the older data, and some will take the newer data. If the IDS doesn't reassemble the TCP in the same way as the target, it can be manipulated into either missing a portion of the attack payload or seeing benign data inserted into the malicious payload, breaking the attack signature. This technique can also be used with IP fragmentation in a similar manner.

### Ambiguities

Some IDS evasion techniques involve deliberately manipulating TCP or IP protocols in a way the target computer will handle differently from the IDS. For example, the TCP urgent pointer is handled differently on different operating systems. If the IDS doesn't handle these protocol violations in a manner consistent with its end hosts, it is vulnerable to insertion and evasion techniques similar to those mentioned earlier.

### Low-bandwidth attacks

Attacks which are spread out across a long period of time or a large number of source IPs, such as nmap's slow scan, can be difficult to pick out of the background of benign traffic. An online password cracker which tests one password for each user every day will look nearly identical to a normal user who mistyped their password.

## Denial of service

Due to the fact that passive IDS are inherently fail-open (as opposed to fail-closed), launching a denial-of-service attack against the IDS on a network is a feasible method of circumventing its protection. An adversary can accomplish this by exploiting a bug in the IDS, consuming all of the computational resources on the IDS, or deliberately triggering a large number of alerts to disguise the actual attack.

### CPU exhaustion

Packets captured by an IDS are stored in a kernel buffer until the CPU is ready to process them. If the CPU is under high load, it can't process the packets quickly enough and this buffer fills up. New (and possibly malicious) packets are then dropped because the buffer is full.

An attacker can exhaust the IDS's CPU resources in a number of ways. For example, signature-based intrusion detection systems use pattern matching algorithms to match incoming packets against signatures of known attacks. Naturally, some signatures are more computational expensive to match against than others. Exploiting this fact, an attacker can send specially-crafted network traffic to force the IDS to use the maximum amount of CPU time as possible to run its pattern matching algorithm on the traffic. This algorithmic complexity attack can overwhelm the IDS with a relatively small amount of bandwidth.

An IDS that also monitors encrypted traffic can spend a large portion of its CPU resources on decrypting incoming data.

### Memory exhaustion

In order to match certain signatures, an IDS is required to keep state related to the connections it is monitoring. For example, an IDS must maintain "TCP control blocks" (TCBs), chunks of memory which track information such as sequence numbers, window sizes, and connection states (ESTABLISHED, RELATED, CLOSED, etc.), for each TCP connection monitored by the IDS. Once all of the IDS's random-access memory (RAM) is consumed, it is forced to utilize virtual memory on the hard disk which is much slower than RAM, leading to performance problems and dropped packets similar to the effects of CPU exhaustion.

If the IDS doesn't garbage collect TCBs correctly and efficiently, an attacker can exhaust the IDS's memory by starting a large number of TCP connections very quickly. Similar attacks can be made by fragmenting a large number of packets into a larger number of smaller packets, or send a large number of out-of-order TCP segments.

### Operator fatigue

Alerts generated by an IDS have to be acted upon in order for them to have any value. An attacker can reduce the "availability" of an IDS by overwhelming the human operator with an inordinate number of alerts by sending large amounts of "malicious" traffic intended to generate alerts on the IDS. The attacker can then perform the actual attack using the alert noise as cover. The tools 'stick' and 'snot' were designed for this purpose. They generate a large number of IDS alerts by sending attack signature across the network, but will not trigger alerts in IDS that maintain application protocol context.
