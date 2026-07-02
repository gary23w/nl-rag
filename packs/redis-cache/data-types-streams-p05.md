---
title: "Redis Streams (part 5/5)"
source: https://redis.io/docs/latest/develop/data-types/streams/
domain: redis-cache
license: CC-BY-SA-4.0
tags: redis, in-memory data store, key-value cache, in-memory database
fetched: 2026-07-02
part: 5/5
---

## Capped Streams

Many applications do not want to collect data into a stream forever. Sometimes it is useful to have at maximum a given number of items inside a stream, other times once a given size is reached, it is useful to move data from Redis to a storage which is not in memory and not as fast but suited to store the history for, potentially, decades to come. Redis streams have some support for this. One is the **MAXLEN** option of the `XADD` command. This option is very simple to use:

Limit stream size using MAXLEN option with XADD to automatically evict old entries and maintain constant memory usage

```plaintext
> XADD race:italy MAXLEN 2 * rider Jones
"1692633189161-0"
> XADD race:italy MAXLEN 2 * rider Wood
"1692633198206-0"
> XADD race:italy MAXLEN 2 * rider Henshaw
"1692633208557-0"
> XLEN race:italy
(integer) 2
> XRANGE race:italy - +
1) 1) "1692633198206-0"
   2) 1) "rider"
      2) "Wood"
2) 1) "1692633208557-0"
   2) 1) "rider"
      2) "Henshaw"
```

```python
r.xadd("race:italy", {"rider": "Jones"}, maxlen=2)
r.xadd("race:italy", {"rider": "Wood"}, maxlen=2)
r.xadd("race:italy", {"rider": "Henshaw"}, maxlen=2)

res34 = r.xlen("race:italy")
print(res34)  # >>> 8

res35 = r.xrange("race:italy", "-", "+")
print(
    res35
)
# >>> [
#       ('1692629925771-0', {'rider': 'Castilla'}),
#       ('1692629925789-0', {'rider': 'Royce'}),
#       ('1692629925790-0', {'rider': 'Sam-Bodden'}),
#       ('1692629925791-0', {'rider': 'Prickett'}),
#       ('1692629926436-0', {'rider': 'Norem'}),
#       ('1692630612602-0', {'rider': 'Jones'}),
#       ('1692630641947-0', {'rider': 'Wood'}),
#       ('1692630648281-0', {'rider': 'Henshaw'})
# ]

r.xadd("race:italy", {"rider": "Smith"}, maxlen=2, approximate=False)

res36 = r.xrange("race:italy", "-", "+")
print(
    res36
)
# >>> [
#       ('1692630648281-0', {'rider': 'Henshaw'}),
#       ('1692631018238-0', {'rider': 'Smith'})
# ]
```

```node
await client.xAdd('race:italy', '*', {
  'rider': 'Jones'
}, {
  TRIM: {
    strategy: 'MAXLEN',
    strategyModifier: '~',
    threshold: 2
  }
});
await client.xAdd('race:italy', '*', {
  'rider': 'Wood'
}, {
  TRIM: {
    strategy: 'MAXLEN',
    strategyModifier: '~',
    threshold: 2
  }
});
await client.xAdd('race:italy', '*', {
  'rider': 'Henshaw'
}, {
  TRIM: {
    strategy: 'MAXLEN',
    strategyModifier: '~',
    threshold: 2
  }
});

const res34 = await client.xLen('race:italy');
console.log(res34); // >>> 8

const res35 = await client.xRange('race:italy', '-', '+');
console.log(res35); // >>> [{ id: '1692629925771-0', message: { rider: 'Castilla' } }, { id: '1692629925789-0', message: { rider: 'Royce' } }, { id: '1692629925790-0', message: { rider: 'Sam-Bodden' } }, { id: '1692629925791-0', message: { rider: 'Prickett' } }, { id: '1692629926436-0', message: { rider: 'Norem' } }, { id: '1692630612602-0', message: { rider: 'Jones' } }, { id: '1692630641947-0', message: { rider: 'Wood' } }, { id: '1692630648281-0', message: { rider: 'Henshaw' } }]

await client.xAdd('race:italy', '*', {
  'rider': 'Smith'
}, {
  TRIM: {
    strategy: 'MAXLEN',
    strategyModifier: '=',
    threshold: 2
  }
});

const res36 = await client.xRange('race:italy', '-', '+');
console.log(res36); // >>> [{ id: '1692630648281-0', message: { rider: 'Henshaw' } }, { id: '1692631018238-0', message: { rider: 'Smith' } }]
```

```java
    jedis.xadd("race:italy", new HashMap<String,String>(){{put("rider","Jones");}},XAddParams.xAddParams().maxLen(10));
    jedis.xadd("race:italy", new HashMap<String,String>(){{put("rider","Wood");}},XAddParams.xAddParams().maxLen(10));
    jedis.xadd("race:italy", new HashMap<String,String>(){{put("rider","Henshaw");}},XAddParams.xAddParams().maxLen(10));
    long res35 = jedis.xlen("race:italy");
    System.out.println(res35); // >>> 8

    List<StreamEntry> res36 = jedis.xrange("race:italy","-","+");
    System.out.println(res36); // >>> [1701771219852-0 {rider=Castilaa}, 1701771219852-1 {rider=Royce}, 1701771219853-0 {rider=Sam-Bodden}, 1701771219853-1 {rider=Prickett}, 1701771219853-2 {rider=Norem}, 1701771219858-0 {rider=Jones}, 1701771219858-1 {rider=Wood}, 1701771219859-0 {rider=Henshaw}]

    StreamEntryID id6 = jedis.xadd("race:italy", new HashMap<String,String>(){{put("rider","Smith");}},XAddParams.xAddParams().maxLen(2));

    List<StreamEntry> res37 = jedis.xrange("race:italy","-","+");
    System.out.println(res37); // >>> [1701771067332-1 {rider=Henshaw}, 1701771067332-2 {rider=Smith}]
```

```go
	_, err = rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:italy",
		MaxLen: 2,
		Values: map[string]interface{}{"rider": "Jones"},
	},
	).Result()

	if err != nil {
		panic(err)
	}

	_, err = rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:italy",
		MaxLen: 2,
		Values: map[string]interface{}{"rider": "Wood"},
	},
	).Result()

	if err != nil {
		panic(err)
	}

	_, err = rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:italy",
		MaxLen: 2,
		Values: map[string]interface{}{"rider": "Henshaw"},
	},
	).Result()

	if err != nil {
		panic(err)
	}

	res36, err := rdb.XLen(ctx, "race:italy").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res36) // >>> 2

	res37, err := rdb.XRange(ctx, "race:italy", "-", "+").Result()

	if err != nil {
		panic(err)
	}

	// fmt.Println(res37)
	// >>> [{1726649529170-1 map[rider:Wood] 0 0} {1726649529171-0 map[rider:Henshaw] 0 0}]
```

```c#
        db.StreamAdd(
            "race:italy", [new("rider", "Jones")], null, 2, true
        );

        db.StreamAdd(
            "race:italy", [new("rider", "Wood")], null, 2, true
        );

        db.StreamAdd(
            "race:italy", [new("rider", "Henshaw")], null, 2, true
        );

        long res35 = db.StreamLength("race:italy");
        Console.WriteLine(res35); // >>> 8

        StreamEntry[] res36 = db.StreamRange("race:italy", "-", "+");

        foreach (StreamEntry entry in res36)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712758336128-0: [rider: Castilla]
        // >>> 1712758336128-1: [rider: Royce]
        // >>> 1712758336128-2: [rider: Sam-Bodden]
        // >>> 1712758336129-0: [rider: Prickett]
        // >>> 1712758336139-0: [rider: Norem]
        // >>> 1712758340854-0: [rider: Jones]
        // >>> 1712758341645-0: [rider: Wood]
        // >>> 1712758342134-0: [rider: Henshaw]

        db.StreamAdd(
            "race:italy", [new("rider", "Smith")], null, 2, false
        );

        StreamEntry[] res37 = db.StreamRange("race:italy", "-", "+");

        foreach (StreamEntry entry in res37)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // 1712758746476-1: [rider: Henshaw]
        // 1712758746477-0: [rider: Smith]
```

```ruby
r.del('race:italy')
r.xadd('race:italy', {'rider' => 'Castilla'}, id: '1692632639151-0')
r.xadd('race:italy', {'rider' => 'Royce'}, id: '1692632647899-0')
r.xadd('race:italy', {'rider' => 'Sam-Bodden'}, id: '1692632662819-0')
r.xadd('race:italy', {'rider' => 'Prickett'}, id: '1692632670501-0')
r.xadd('race:italy', {'rider' => 'Norem'}, id: '1692632678249-0')
r.xadd('race:italy', {'rider' => 'Jones'}, id: '1692633189161-0', maxlen: 2)
r.xadd('race:italy', {'rider' => 'Wood'}, id: '1692633198206-0', maxlen: 2)
r.xadd('race:italy', {'rider' => 'Henshaw'}, id: '1692633208557-0', maxlen: 2)

res34 = r.xlen('race:italy')
puts res34 # 2

res35 = r.xrange('race:italy', '-', '+')
puts res35.inspect
# [["1692633198206-0", {"rider"=>"Wood"}], ["1692633208557-0", {"rider"=>"Henshaw"}]]
```

```rust
        delete_keys(&mut r, &["race:italy"]);
        let max1: Option<String> = r
            .xadd_maxlen("race:italy", StreamMaxlen::Equals(2), "1-0", &[("rider", "Jones")])
            .expect("maxlen add 1");
        let max1 = max1.expect("missing stream id");
        println!("{max1}"); // >>> 1-0
        let max2: Option<String> = r
            .xadd_maxlen("race:italy", StreamMaxlen::Equals(2), "2-0", &[("rider", "Wood")])
            .expect("maxlen add 2");
        let max2 = max2.expect("missing stream id");
        println!("{max2}"); // >>> 2-0
        let max3: Option<String> = r
            .xadd_maxlen("race:italy", StreamMaxlen::Equals(2), "3-0", &[("rider", "Henshaw")])
            .expect("maxlen add 3");
        let max3 = max3.expect("missing stream id");
        println!("{max3}"); // >>> 3-0

        if let Ok(res) = r.xlen("race:italy") {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }

        if let Ok(res) = r.xrange_all("race:italy") {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("2-0", [("rider", "Wood")]), ("3-0", [("rider", "Henshaw")])]
        }
```

```rust
        delete_keys(&mut r, &["race:italy"]).await;
        let max1: Option<String> = r
            .xadd_maxlen("race:italy", StreamMaxlen::Equals(2), "1-0", &[("rider", "Jones")])
            .await
            .expect("maxlen add 1");
        let max1 = max1.expect("missing stream id");
        println!("{max1}"); // >>> 1-0
        let max2: Option<String> = r
            .xadd_maxlen("race:italy", StreamMaxlen::Equals(2), "2-0", &[("rider", "Wood")])
            .await
            .expect("maxlen add 2");
        let max2 = max2.expect("missing stream id");
        println!("{max2}"); // >>> 2-0
        let max3: Option<String> = r
            .xadd_maxlen("race:italy", StreamMaxlen::Equals(2), "3-0", &[("rider", "Henshaw")])
            .await
            .expect("maxlen add 3");
        let max3 = max3.expect("missing stream id");
        println!("{max3}"); // >>> 3-0
        if let Ok(res) = r.xlen("race:italy").await {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }
        if let Ok(res) = r.xrange_all("race:italy").await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("2-0", [("rider", "Wood")]), ("3-0", [("rider", "Henshaw")])]
        }
```

Using **MAXLEN** the old entries are automatically evicted when the specified length is reached, so that the stream is left at a constant size. There is currently no option to tell the stream to just retain items that are not older than a given period, because such command, in order to run consistently, would potentially block for a long time in order to evict items. Imagine for example what happens if there is an insertion spike, then a long pause, and another insertion, all with the same maximum time. The stream would block to evict the data that became too old during the pause. So it is up to the user to do some planning and understand what is the maximum stream length desired. Moreover, while the length of the stream is proportional to the memory used, trimming by time is less simple to control and anticipate: it depends on the insertion rate which often changes over time (and when it does not change, then to just trim by size is trivial).

However trimming with **MAXLEN** can be expensive: streams are represented by macro nodes into a radix tree, in order to be very memory efficient. Altering the single macro node, consisting of a few tens of elements, is not optimal. So it's possible to use the command in the following special form:

```
XADD race:italy MAXLEN ~ 1000 * ... entry fields here ...
```

The `~` argument between the **MAXLEN** option and the actual count means, I don't really need this to be exactly 1000 items. It can be 1000 or 1010 or 1030, just make sure to save at least 1000 items. With this argument, the trimming is performed only when we can remove a whole node. This makes it much more efficient, and it is usually what you want. You'll note here that the client libraries have various implementations of this. For example, the Python client defaults to approximate and has to be explicitly set to a true length.

There is also the `XTRIM` command, which performs something very similar to what the **MAXLEN** option does above, except that it can be run by itself:

Trim a stream to a maximum length using XTRIM MAXLEN to remove old entries

```plaintext
> XTRIM race:italy MAXLEN 10
(integer) 0
```

```python
res37 = r.xtrim("race:italy", maxlen=10, approximate=False)
print(res37)  # >>> 0
```

```node
const res37 = await client.xTrim('race:italy', 'MAXLEN', 10, {
  strategyModifier: '=',
});
console.log(res37); // >>> 0
```

```java
    long res38 = jedis.xtrim("race:italy",XTrimParams.xTrimParams().maxLen(10).exactTrimming());
    System.out.println(res38); /// >>> 0
```

```go
	res38, err := rdb.XTrimMaxLen(ctx, "race:italy", 10).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res38) // >>> 0
```

```c#
        long res38 = db.StreamTrim("race:italy", 10, false);
        Console.WriteLine(res38);   // >>> 0
```

```ruby
res36 = r.xtrim('race:italy', 10, approximate: false)
puts res36 # 0
```

```rust
        delete_keys(&mut r, &["race:italy"]);
        let _: Option<String> = r.xadd("race:italy", "1-0", &[("rider", "Wood")]).expect("trim seed 1");
        let _: Option<String> = r.xadd("race:italy", "2-0", &[("rider", "Henshaw")]).expect("trim seed 2");
        if let Ok(res) = r.xtrim("race:italy", StreamMaxlen::Equals(10)) {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }
```

```rust
        delete_keys(&mut r, &["race:italy"]).await;
        let _: Option<String> = r.xadd("race:italy", "1-0", &[("rider", "Wood")]).await.expect("trim seed 1");
        let _: Option<String> = r.xadd("race:italy", "2-0", &[("rider", "Henshaw")]).await.expect("trim seed 2");
        if let Ok(res) = r.xtrim("race:italy", StreamMaxlen::Equals(10)).await {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }
```

Or, as for the `XADD` option:

Use approximate trimming with XTRIM MAXLEN ~ for more efficient memory management

```plaintext
> XTRIM mystream MAXLEN ~ 10
(integer) 0
```

```python
res38 = r.xtrim("race:italy", maxlen=10)
print(res38)  # >>> 0
```

```node
const res38 = await client.xTrim('race:italy', "MAXLEN", 10);
console.log(res38); // >>> 0
```

```java
    long res39 = jedis.xtrim("race:italy",XTrimParams.xTrimParams().maxLen(10));
    System.out.println(res39); /// >>> 0
```

```go
	res39, err := rdb.XTrimMaxLenApprox(ctx, "race:italy", 10, 20).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res39) // >>> 0
```

```c#
        long res39 = db.StreamTrim("race:italy", 10, true);
        Console.WriteLine(res39);   // >>> 0
```

```ruby
r.del('mystream')
1.upto(10) do |n|
  r.xadd('mystream', {'field' => 'value'}, id: "#{n}-0")
end
res37 = r.xtrim('mystream', 10, approximate: true)
puts res37 # 0
```

```rust
        seed_trim_stream(&mut r);
        if let Ok(res) = r.xtrim_options(
            "mystream",
            &StreamTrimOptions::maxlen(StreamTrimmingMode::Approx, 10),
        ) {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }
```

```rust
        seed_trim_stream(&mut r).await;
        if let Ok(res) = r
            .xtrim_options(
                "mystream",
                &StreamTrimOptions::maxlen(StreamTrimmingMode::Approx, 10),
            )
            .await
        {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }
```

However, `XTRIM` is designed to accept different trimming strategies. Another trimming strategy is **MINID**, that evicts entries with IDs lower than the one specified.

As `XTRIM` is an explicit command, the user is expected to know about the possible shortcomings of different trimming strategies.

### Trimming with consumer group awareness

Starting with Redis 8.2, both `XADD` with trimming options and `XTRIM` support enhanced control over how trimming interacts with consumer groups through the `KEEPREF`, `DELREF`, and `ACKED` options:

```
XADD mystream KEEPREF MAXLEN 1000 * field value
XTRIM mystream ACKED MAXLEN 1000
```

- **KEEPREF** (default): Trims entries according to the strategy but preserves references in consumer group PELs
- **DELREF**: Trims entries and removes all references from consumer group PELs
- **ACKED**: Only trims entries that have been acknowledged by all consumer groups

The `ACKED` option is particularly useful for maintaining data integrity across multiple consumer groups, ensuring that entries are only removed when all groups have finished processing them.

Another useful eviction strategy that may be added to `XTRIM` in the future, is to remove by a range of IDs to ease use of `XRANGE` and `XTRIM` to move data from Redis to other storage systems if needed.


## Special IDs in the streams API

You may have noticed that there are several special IDs that can be used in the Redis API. Here is a short recap, so that they can make more sense in the future.

The first two special IDs are `-` and `+`, and are used in range queries with the `XRANGE` command. Those two IDs respectively mean the smallest ID possible (that is basically `0-1`) and the greatest ID possible (that is `18446744073709551615-18446744073709551615`). As you can see it is a lot cleaner to write `-` and `+` instead of those numbers.

Then there are APIs where we want to say, the ID of the item with the greatest ID inside the stream. This is what `$` means. So for instance if I want only new entries with `XREADGROUP` I use this ID to signify I already have all the existing entries, but not the new ones that will be inserted in the future. Similarly when I create or set the ID of a consumer group, I can set the last delivered item to `$` in order to just deliver new entries to the consumers in the group.

As you can see `$` does not mean `+`, they are two different things, as `+` is the greatest ID possible in every possible stream, while `$` is the greatest ID in a given stream containing given entries. Moreover APIs will usually only understand `+` or `$`, yet it was useful to avoid loading a given symbol with multiple meanings.

Another special ID is `>`, that is a special meaning only related to consumer groups and only when the `XREADGROUP` command is used. This special ID means that we want only entries that were never delivered to other consumers so far. So basically the `>` ID is the *last delivered ID* of a consumer group.

Finally the special ID `*`, that can be used only with the `XADD` command, means to auto select an ID for us for the new entry.

So we have `-`, `+`, `$`, `>` and `*`, and all have a different meaning, and most of the time, can be used in different contexts.


## Persistence, replication and message safety

A Stream, like any other Redis data structure, is asynchronously replicated to replicas and persisted into AOF and RDB files. However what may not be so obvious is that also the consumer groups full state is propagated to AOF, RDB and replicas, so if a message is pending in the master, also the replica will have the same information. Similarly, after a restart, the AOF will restore the consumer groups' state.

However note that Redis streams and consumer groups are persisted and replicated using the Redis default replication, so:

- AOF must be used with a strong fsync policy if persistence of messages is important in your application.
- By default the asynchronous replication will not guarantee that `XADD` commands or consumer groups state changes are replicated: after a failover something can be missing depending on the ability of replicas to receive the data from the master.
- The `WAIT` command may be used in order to force the propagation of the changes to a set of replicas. However note that while this makes it very unlikely that data is lost, the Redis failover process as operated by Sentinel or Redis Cluster performs only a *best effort* check to failover to the replica which is the most updated, and under certain specific failure conditions may promote a replica that lacks some data.

So when designing an application using Redis streams and consumer groups, make sure to understand the semantical properties your application should have during failures, and configure things accordingly, evaluating whether it is safe enough for your use case.


## Removing single items from a stream

Streams also have a special command for removing items from the middle of a stream, just by ID. Normally for an append only data structure this may look like an odd feature, but it is actually useful for applications involving, for instance, privacy regulations. The command is called `XDEL` and receives the name of the stream followed by the IDs to delete:

Delete specific entries from a stream by ID using XDEL for privacy or data cleanup purposes

```plaintext
> XRANGE race:italy - + COUNT 2
1) 1) "1692633198206-0"
   2) 1) "rider"
      2) "Wood"
2) 1) "1692633208557-0"
   2) 1) "rider"
      2) "Henshaw"
> XDEL race:italy 1692633208557-0
(integer) 1
> XRANGE race:italy - + COUNT 2
1) 1) "1692633198206-0"
   2) 1) "rider"
      2) "Wood"
```

```python
res39 = r.xrange("race:italy", "-", "+")
print(
    res39
)
# >>> [
#       ('1692630648281-0', {'rider': 'Henshaw'}),
#       ('1692631018238-0', {'rider': 'Smith'})
# ]

res40 = r.xdel("race:italy", "1692631018238-0")
print(res40)  # >>> 1

res41 = r.xrange("race:italy", "-", "+")
print(res41)  # >>> [('1692630648281-0', {'rider': 'Henshaw'})]
```

```node
const res39 = await client.xRange('race:italy', '-', '+');
console.log(res39); // >>> [{ id: '1692630648281-0', message: { rider: 'Henshaw' } }, { id: '1692631018238-0', message: { rider: 'Smith' } }]

const res40 = await client.xDel('race:italy', '1692631018238-0');
console.log(res40); // >>> 1

const res41 = await client.xRange('race:italy', '-', '+');
console.log(res41); // >>> [{ id: '1692630648281-0', message: { rider: 'Henshaw' } }]
```

```java
    List<StreamEntry> res40 = jedis.xrange("race:italy","-","+");
    System.out.println(res40); // >>> [1701771356428-2 {rider=Henshaw}, 1701771356429-0 {rider=Smith}]

    long res41 = jedis.xdel("race:italy",id6);
    System.out.println(res41); // >>> 1

    List<StreamEntry> res42 = jedis.xrange("race:italy","-","+");
    System.out.println(res42); // >>> [1701771517639-1 {rider=Henshaw}]
```

```go
	res39, err := rdb.XRangeN(ctx, "race:italy", "-", "+", 2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res39)
	// >>> [{1692633198206-0 map[rider:Wood] 0 0} {1692633208557-0 map[rider:Henshaw] 0 0}]

	res40, err := rdb.XDel(ctx, "race:italy", "1692633208557-0").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res40) // 1

	res41, err := rdb.XRangeN(ctx, "race:italy", "-", "+", 2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res41)
	// >>> [{1692633198206-0 map[rider:Wood] 0 0}]
```

```c#
        StreamEntry[] res40 = db.StreamRange("race:italy", "-", "+");

        foreach (StreamEntry entry in res40)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712759694003-0: [rider: Henshaw]
        // >>> 1712759694003-1: [rider: Smith]

        long res41 = db.StreamDelete("race:italy", ["1712759694003-1"]);
        Console.WriteLine(res41);   // >>> 1

        StreamEntry[] res42 = db.StreamRange("race:italy", "-", "+");

        foreach (StreamEntry entry in res42)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");

        }
        // >>> 1712759694003-0: [rider: Henshaw]
```

```ruby
r.del('race:italy')
r.xadd('race:italy', {'rider' => 'Wood'}, id: '1692633198206-0')
r.xadd('race:italy', {'rider' => 'Henshaw'}, id: '1692633208557-0')
res38 = r.xrange('race:italy', '-', '+', count: 2)
puts res38.inspect
# [["1692633198206-0", {"rider"=>"Wood"}], ["1692633208557-0", {"rider"=>"Henshaw"}]]

res39 = r.xdel('race:italy', '1692633208557-0')
puts res39 # 1

res40 = r.xrange('race:italy', '-', '+', count: 2)
puts res40.inspect
# [["1692633198206-0", {"rider"=>"Wood"}]]
```

```rust
        delete_keys(&mut r, &["race:italy"]);
        let _: Option<String> = r.xadd("race:italy", "2-0", &[("rider", "Wood")]).expect("xdel seed 1");
        let _: Option<String> = r.xadd("race:italy", "3-0", &[("rider", "Henshaw")]).expect("xdel seed 2");
        if let Ok(res) = r.xrange_count("race:italy", "-", "+", 2) {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{view:?}"); // >>> [("2-0", [("rider", "Wood")]), ("3-0", [("rider", "Henshaw")])]
        }

        if let Ok(res) = r.xdel("race:italy", &["3-0"]) {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.xrange_count("race:italy", "-", "+", 2) {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{view:?}"); // >>> [("2-0", [("rider", "Wood")])]
        }
```

```rust
        delete_keys(&mut r, &["race:italy"]).await;
        let _: Option<String> = r.xadd("race:italy", "2-0", &[("rider", "Wood")]).await.expect("xdel seed 1");
        let _: Option<String> = r.xadd("race:italy", "3-0", &[("rider", "Henshaw")]).await.expect("xdel seed 2");
        if let Ok(res) = r.xrange_count("race:italy", "-", "+", 2).await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{view:?}"); // >>> [("2-0", [("rider", "Wood")]), ("3-0", [("rider", "Henshaw")])]
        }
        if let Ok(res) = r.xdel("race:italy", &["3-0"]).await {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }
        if let Ok(res) = r.xrange_count("race:italy", "-", "+", 2).await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{view:?}"); // >>> [("2-0", [("rider", "Wood")])]
        }
```

### Enhanced deletion with XDELEX

Starting with Redis 8.2, the `XDELEX` command provides enhanced control over entry deletion, particularly when working with consumer groups. Like other enhanced commands, it supports `KEEPREF`, `DELREF`, and `ACKED` options:

```
XDELEX mystream ACKED IDS 2 1692633198206-0 1692633208557-0
```

This allows you to delete entries only when they have been acknowledged by all consumer groups (`ACKED`), remove all consumer group references (`DELREF`), or preserve existing references (`KEEPREF`).


## Zero length streams

A difference between streams and other Redis data structures is that when the other data structures no longer have any elements, as a side effect of calling commands that remove elements, the key itself will be removed. So for instance, a sorted set will be completely removed when a call to `ZREM` will remove the last element in the sorted set. Streams, on the other hand, are allowed to stay at zero elements, both as a result of using a **MAXLEN** option with a count of zero (`XADD` and `XTRIM` commands), or because `XDEL` was called.

The reason why such an asymmetry exists is because Streams may have associated consumer groups, and we do not want to lose the state that the consumer groups defined just because there are no longer any items in the stream. Currently the stream is not deleted even when it has no associated consumer groups.


## Total latency of consuming a message

Non blocking stream commands like `XRANGE` and `XREAD` or `XREADGROUP` without the BLOCK option are served synchronously like any other Redis command, so to discuss latency of such commands is meaningless: it is more interesting to check the time complexity of the commands in the Redis documentation. It should be enough to say that stream commands are at least as fast as sorted set commands when extracting ranges, and that `XADD` is very fast and can easily insert from half a million to one million items per second in an average machine if pipelining is used.

However latency becomes an interesting parameter if we want to understand the delay of processing a message, in the context of blocking consumers in a consumer group, from the moment the message is produced via `XADD`, to the moment the message is obtained by the consumer because `XREADGROUP` returned with the message.


## How serving blocked consumers works

Before providing the results of performed tests, it is interesting to understand what model Redis uses in order to route stream messages (and in general actually how any blocking operation waiting for data is managed).

- The blocked client is referenced in a hash table that maps keys for which there is at least one blocking consumer, to a list of consumers that are waiting for such key. This way, given a key that received data, we can resolve all the clients that are waiting for such data.
- When a write happens, in this case when the `XADD` command is called, it calls the `signalKeyAsReady()` function. This function will put the key into a list of keys that need to be processed, because such keys may have new data for blocked consumers. Note that such *ready keys* will be processed later, so in the course of the same event loop cycle, it is possible that the key will receive other writes.
- Finally, before returning into the event loop, the *ready keys* are finally processed. For each key the list of clients waiting for data is scanned, and if applicable, such clients will receive the new data that arrived. In the case of streams the data is the messages in the applicable range requested by the consumer.

As you can see, basically, before returning to the event loop both the client calling `XADD` and the clients blocked to consume messages, will have their reply in the output buffers, so the caller of `XADD` should receive the reply from Redis at about the same time the consumers will receive the new messages.

This model is *push-based*, since adding data to the consumers buffers will be performed directly by the action of calling `XADD`, so the latency tends to be quite predictable.


## Latency tests results

In order to check these latency characteristics a test was performed using multiple instances of Ruby programs pushing messages having as an additional field the computer millisecond time, and Ruby programs reading the messages from the consumer group and processing them. The message processing step consisted of comparing the current computer time with the message timestamp, in order to understand the total latency.

Results obtained:

```
Processed between 0 and 1 ms -> 74.11%
Processed between 1 and 2 ms -> 25.80%
Processed between 2 and 3 ms -> 0.06%
Processed between 3 and 4 ms -> 0.01%
Processed between 4 and 5 ms -> 0.02%
```

So 99.9% of requests have a latency <= 2 milliseconds, with the outliers that remain still very close to the average.

Adding a few million unacknowledged messages to the stream does not change the gist of the benchmark, with most queries still processed with very short latency.

A few remarks:

- Here we processed up to 10k messages per iteration, this means that the `COUNT` parameter of `XREADGROUP` was set to 10000. This adds a lot of latency but is needed in order to allow the slow consumers to be able to keep with the message flow. So you can expect a real world latency that is a lot smaller.
- The system used for this benchmark is very slow compared to today's standards.


## Learn more

- Redis Streams Explained is an entertaining introduction to streams in Redis.
- Redis University's RU202 is a free, online course dedicated to Redis Streams.


## On this page
