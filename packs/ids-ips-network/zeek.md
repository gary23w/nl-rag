---
title: "Zeek"
source: https://en.wikipedia.org/wiki/Zeek
domain: ids-ips-network
license: CC-BY-SA-4.0
tags: intrusion detection, intrusion prevention, signature detection, network sensors
fetched: 2026-07-02
---

# Zeek

**Zeek** is a free and open-source software network analysis framework. Vern Paxson began development work on Zeek in 1995 at Lawrence Berkeley National Lab. Zeek is a network security monitor (NSM) but can also be used as a network intrusion detection system (NIDS). The Zeek project releases the software under the BSD license.

## Output

Zeek's purpose is to inspect network traffic and generate a variety of logs describing the activity it sees. A complete list of log files is available at the project documentation site.

## Log example

The following is an example of one entry in JSON format from the conn.log:

```mw
{
  "ts": 1554410064.698965,
  "uid": "CMreaf3tGGK2whbqhh",
  "id.orig_h": "192.168.144.130",
  "id.orig_p": 64277,
  "id.resp_h": "192.168.144.2",
  "id.resp_p": 53,
  "proto": "udp",
  "service": "dns",
  "duration": 0.320463,
  "orig_bytes": 94,
  "resp_bytes": 316,
  "conn_state": "SF",
  "missed_bytes": 0,
  "history": "Dd",
  "orig_pkts": 2,
  "orig_ip_bytes": 150,
  "resp_pkts": 2,
  "resp_ip_bytes": 372,
  "tunnel_parents": []
}
```

## Threat hunting

One of Zeek's primary use cases involves cyber threat hunting.

## Name

The principal author, Paxson, originally named the software "Bro" as a warning regarding George Orwell's Big Brother from the novel *Nineteen Eighty-Four*. In 2018 the project leadership team decided to rename the software. At LBNL in the 1990s, the developers ran their sensors as a pseudo-user named "zeek", thereby inspiring the name change in 2018.

## Zeek deployment

Security teams identify locations on their network where they desire visibility. They deploy one or more network taps or enable switch SPAN ports for port mirroring to gain access to traffic. They deploy Zeek on servers with access to those visibility points. The Zeek software on the server deciphers network traffic as logs, writing them to local disk or remote storage.

## Zeek application architecture and analyzers

Zeek's event engine analyzes live or recorded network traffic to generate neutral event logs. Zeek uses common ports and dynamic protocol detection (involving signatures as well as behavioral analysis) to identify network protocols.

Developers write Zeek policy scripts in the Turing complete Zeek scripting language. By default Zeek logs information about events to files, but analysts can also configure Zeek to take other actions, such as sending an email, raising an alert, executing a system command, updating an internal metric, or calling another Zeek script.

Zeek analyzers perform application layer decoding, anomaly detection, signature matching and connection analysis. Zeek's developers designed the software to incorporate additional analyzers. The latest method for creating new protocol analyzers relies on the Spicy framework.
