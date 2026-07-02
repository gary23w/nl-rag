---
title: "Memcached"
source: https://en.wikipedia.org/wiki/Memcached
domain: aws-elasticache
license: CC-BY-SA-4.0
tags: aws elasticache, amazon elasticache, managed cache, in-memory data store
fetched: 2026-07-02
---

# Memcached

In computing **Memcached** (pronounced either /mɛmkæʃˈdiː/ *mem-cash-DEE* ["dee/d" being for daemon], or /ˈmɛmkæʃt/ *MEM-cashed*) is a general-purpose distributed memory-caching system. It is often used to speed up dynamic database-driven websites by caching data and objects in RAM to reduce the number of times an external data source (such as a database or API) must be read. Memcached is free and open-source software, licensed under the Revised BSD license. Memcached runs on Unix-like operating systems (Linux and macOS) and on Microsoft Windows. It depends on the libevent library.

Memcached's APIs provide a large hash table distributed across multiple machines. When the table is full, subsequent inserts cause older data to be purged in least recently used (LRU) order. Applications using Memcached typically layer requests and additions into RAM before falling back on a slower backing store, such as a database.

Memcached has no internal mechanism to track misses which may happen. However, some third party utilities provide this functionality.

Memcached was first developed by Brad Fitzpatrick for his website LiveJournal, on May 22, 2003. It was originally written in Perl, then later rewritten in C by Anatoly Vorobey, who was employed by LiveJournal at the time. Memcached is now used by many other systems, including YouTube, Reddit, Facebook, Pinterest, Twitter, Wikipedia, and Method Studios. Google App Engine, Google Cloud Platform, Microsoft Azure, IBM Bluemix and Amazon Web Services also offer a Memcached service through an API.

## Software architecture

The system uses a client–server architecture. The servers maintain a key–value associative array; the clients populate this array and query it by key. Keys are up to 250 bytes long and values can be at most 1 megabyte in size.

Clients use client-side libraries to contact the servers which, by default, expose their service at port 11211. Both TCP and UDP are supported. Each client knows all servers; the servers do not communicate with each other. If a client wishes to set or read the value corresponding to a certain key, the client's library first computes a hash of the key to determine which server to use. This gives a simple form of sharding and scalable shared-nothing architecture across the servers. The server computes a second hash of the key to determine where to store or read the corresponding value. The servers keep the values in RAM (and, starting in 1.6.0, in auxiliary cache on disk using an external storage server option); if a server runs out of available memory or disk, it discards the oldest values. Therefore, clients must treat Memcached as a transitory cache; they cannot assume that data stored in Memcached is still there when they need it. Other databases, such as MemcacheDB, Couchbase Server, provide persistent storage while maintaining Memcached protocol compatibility.

If all client libraries use the same hashing algorithm to determine servers, then clients can read each other's cached data.

A typical deployment has several servers and many clients. However, it is possible to use Memcached on a single computer, acting simultaneously as client and server. The size of its hash table is often very large. It is limited to available memory across all the servers in the cluster of servers in a data center. Where high-volume, wide-audience Web publishing requires it, this may stretch to many gigabytes. Memcached can be equally valuable for situations where either the number of requests for content is high, or the cost of generating a particular piece of content is high. Applications with particularly high-demand caching needs can use a built-in proxy to define and configure complex client-server routes.

### Security

Most deployments of Memcached are within trusted networks where clients may freely connect to any server. However, sometimes Memcached is deployed in untrusted networks or where administrators want to exercise control over the clients that are connecting. For this purpose Memcached can be compiled with optional SASL authentication support. The SASL support requires the binary protocol.

A presentation at BlackHat USA 2010 revealed that a number of large public websites had left Memcached open to inspection, analysis, retrieval, and modification of data.

Even within a trusted organisation, the flat trust model of memcached may have security implications. For efficient simplicity, all Memcached operations are treated equally. Clients with a valid need for access to low-security entries within the cache gain access to *all* entries within the cache, even when these are higher-security and that client has no justifiable need for them. If the cache key can be either predicted, guessed or found by exhaustive searching, its cache entry may be retrieved.

Some attempt to isolate setting and reading data may be made in situations such as high volume web publishing. A farm of outward-facing content servers have *read* access to memcached containing published pages or page components, but no write access. Where new content is published (and is not yet in memcached), a request is instead sent to content generation servers that are not publicly accessible to create the content unit and add it to memcached. The content server then retries to retrieve it and serve it outwards.

#### Used as a DDoS attack vector

In February 2018, CloudFlare reported that misconfigured memcached servers were used to launch DDoS attacks in large scale. The memcached protocol over UDP has a huge amplification factor, of more than 51000. Victims of the DDoS attacks include GitHub, which was flooded with 1.35 Tbit/s peak incoming traffic.

This issue was mitigated in Memcached version 1.5.6, which disabled UDP protocol by default.

## Example code

*Note that all functions described on this page are pseudocode only. Memcached calls and programming languages may vary based on the API used.*

Converting database or object creation queries to use Memcached is simple. Typically, when using straight database queries, example code would be as follows:

```mw
 function get_foo(int userid)
     data = db_select("SELECT * FROM users WHERE userid = ?", userid)
     return data
```

After conversion to Memcached, the same call might look like the following

```mw
 function get_foo(int userid)
     /* first try the cache */
     data = memcached_fetch("userrow:" + userid)
     if not data
         /* not found : request database */
         data = db_select("SELECT * FROM users WHERE userid = ?", userid)
         /* then store in cache until next get */
         memcached_add("userrow:" + userid, data)
     end

     return data
```

The client would first check whether a Memcached value with the unique key "userrow:userid" exists, where userid is some number. If the result does not exist, it would select from the database as usual, and set the unique key using the Memcached API add function call.

However, if only this API call were modified, the server would end up fetching incorrect data following any database update actions: the Memcached "view" of the data would become out of date. Therefore, in addition to creating an "add" call, an update call would also be needed using the Memcached set function.

```mw
 function update_foo(int userid, string dbUpdateString)
     /* first update database */
     result = db_execute(dbUpdateString)
     if result
         /* database update successful : fetch data to be stored in cache */
         data = db_select("SELECT * FROM users WHERE userid = ?", userid)
         /* the previous line could also look like data = createDataFromDBString(dbUpdateString) */
         /* then store in cache until next get */
         memcached_set("userrow:" + userid, data)
```

This call would update the currently cached data to match the new data in the database, assuming the database query succeeds. An alternative approach would be to invalidate the cache with the Memcached delete function, so that subsequent fetches result in a cache miss. Similar action would need to be taken when database records were deleted, to maintain either a correct or incomplete cache.

An alternate cache-invalidation strategy is to store a random number in an agreed-upon cache entry and to incorporate this number into all keys that are used to store a particular kind of entry. To invalidate all such entries at once, change the random number. Existing entries (which were stored using the old number) will no longer be referenced and so will eventually expire or be recycled.

```mw
  function store_xyz_entry(int key, string value)
      /* Retrieve the random number - use zero if none exists yet.
      *  The key-name used here is arbitrary. */ 
      seed = memcached_fetch(":xyz_seed:")
      if not seed
          seed = 0
      /* Build the key used to store the entry and store it.
      *  The key-name used here is also arbitrary. Notice that the "seed" and the user's "key"
      *  are stored as separate parts of the constructed hashKey string: ":xyz_data:(seed):(key)." 
      *  This is not mandatory, but is recommended. */
      string hashKey = sprintf(":xyz_data:%d:%d", seed, key)
      memcached_set(hashKey, value)

  /* "fetch_entry," not shown, follows identical logic to the above. */

  function invalidate_xyz_cache()
      existing_seed = memcached_fetch(":xyz_seed:")
      /* Coin a different random seed */
      do
          seed = rand()
      until seed != existing_seed
      /* Now store it in the agreed-upon place. All future requests will use this number. 
      *  Therefore, all existing entries become un-referenced and will eventually expire. */
      memcached_set(":xyz_seed:", seed)
```

## Usage

- MySQL - directly supports the Memcached API as of version 5.6.
- Oracle Coherence - directly supports the Memcached API as of version 12.1.3.
- Infinispan - directly supports Memcached.
