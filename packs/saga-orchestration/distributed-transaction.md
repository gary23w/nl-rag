---
title: "Distributed transaction"
source: https://en.wikipedia.org/wiki/Distributed_transaction
domain: saga-orchestration
license: CC-BY-SA-4.0
tags: saga distributed transaction, compensating transaction pattern, distributed transaction coordination, saga choreography orchestration
fetched: 2026-07-02
---

# Distributed transaction

A **distributed transaction** operates within a distributed environment, typically involving multiple nodes across a network depending on the location of the data. A key aspect of distributed transactions is atomicity, which ensures that the transaction is completed in its entirety or not executed at all. It's essential to note that distributed transactions are not limited to databases.

The Open Group, a vendor consortium, proposed the X/Open Distributed Transaction Processing Model (X/Open XA), which became a de facto standard for the behavior of transaction model components.

Databases are common transactional resources and, often, transactions span a couple of such databases. In this case, a distributed transaction can be seen as a database transaction that must be synchronized (or provide ACID properties) among multiple participating databases which are distributed among different physical locations. The isolation property (the I of ACID) poses a special challenge for multi database transactions, since the (global) serializability property could be violated, even if each database provides it (see also global serializability). In practice most commercial database systems use strong strict two-phase locking (SS2PL) for concurrency control, which ensures global serializability, if all the participating databases employ it.

A common algorithm for ensuring correct completion of a distributed transaction is the two-phase commit (2PC). This algorithm is usually applied for updates able to commit in a short period of time, ranging from couple of milliseconds to couple of minutes.

There are also long-lived distributed transactions, for example a transaction to book a trip, which consists of booking a flight, a rental car and a hotel. Since booking the flight might take up to a day to get a confirmation, two-phase commit is not applicable here, it will lock the resources for this long. In this case more sophisticated techniques that involve multiple undo levels are used. The way you can undo the hotel booking by calling a desk and cancelling the reservation, a system can be designed to undo certain operations (unless they are irreversibly finished).

In practice, long-lived distributed transactions are implemented in systems based on web services. Usually these transactions utilize principles of compensating transactions, Optimism and Isolation Without Locking. The X/Open standard does not cover long-lived distributed transactions.

Several technologies, including Jakarta Enterprise Beans and Microsoft Transaction Server fully support distributed transaction standards.

## Synchronization

In event-driven architectures, distributed transactions can be synchronized through using request–response paradigm and it can be implemented in two ways:

- Creating two separate queues: one for requests and the other for replies. The event producer must wait until it receives the response.
- Creating one dedicated ephemeral queue for each request.
