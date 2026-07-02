---
title: "Redis Streams (part 1/5)"
source: https://redis.io/docs/latest/develop/data-types/streams/
domain: redis-cache
license: CC-BY-SA-4.0
tags: redis, in-memory data store, key-value cache, in-memory database
fetched: 2026-07-02
part: 1/5
---

# Redis Streams

Introduction to Redis streams

Stream command summary

(view reference, 30 commands)

- XACK v5.0.0 @write @stream @fast Returns the number of messages that were successfully acknowledged by the consumer group member of a stream. O(1) for each message ID processed.
- XACKDEL v8.2.0 @write @stream @fast Acknowledges and deletes one or multiple messages for a stream consumer group. O(1) for each message ID processed.
- XADD v5.0.0 @write @stream @fast Appends a new message to a stream. Creates the key if it doesn't exist. O(1) when adding a new entry, O(N) when trimming where N being the number of entries evicted.
- XAUTOCLAIM v6.2.0 @write @stream @fast Changes, or acquires, ownership of messages in a consumer group, as if the messages were delivered to as consumer group member. O(1) if COUNT is small.
- XCFGSET v8.6.0 @write @stream @fast Sets the IDMP configuration parameters for a stream. O(1)
- XCLAIM v5.0.0 @write @stream @fast Changes, or acquires, ownership of a message in a consumer group, as if the message was delivered a consumer group member. O(log N) with N being the number of messages in the PEL of the consumer group.
- XDEL v5.0.0 @write @stream @fast Returns the number of messages after removing them from a stream. O(1) for each single item to delete in the stream, regardless of the stream size.
- XDELEX v8.2.0 @write @stream @fast Deletes one or multiple entries from the stream. O(1) for each single item to delete in the stream, regardless of the stream size.
- XGROUP v5.0.0 @slow A container for consumer groups commands. Depends on subcommand.
- XGROUP CREATE v5.0.0 @write @stream @slow Creates a consumer group. O(1)
- XGROUP CREATECONSUMER v6.2.0 @write @stream @slow Creates a consumer in a consumer group. O(1)
- XGROUP DELCONSUMER v5.0.0 @write @stream @slow Deletes a consumer from a consumer group. O(1)
- XGROUP DESTROY v5.0.0 @write @stream @slow Destroys a consumer group. O(N) where N is the number of entries in the group's pending entries list (PEL).
- XGROUP HELP v5.0.0 @stream @slow Returns helpful text about the different subcommands. O(1)
- XGROUP SETID v5.0.0 @write @stream @slow Sets the last-delivered ID of a consumer group. O(1)
- XIDMPRECORD v8.6.2 @write @stream @fast An internal command for setting IDMP metadata on an existing stream message. O(1)
- XINFO v5.0.0 @slow A container for stream introspection commands. Depends on subcommand.
- XINFO CONSUMERS v5.0.0 @read @stream @slow Returns a list of the consumers in a consumer group. O(1)
- XINFO GROUPS v5.0.0 @read @stream @slow Returns a list of the consumer groups of a stream. O(1)
- XINFO HELP v5.0.0 @stream @slow Returns helpful text about the different subcommands. O(1)
- XINFO STREAM v5.0.0 @read @stream @slow Returns information about a stream. O(1)
- XLEN v5.0.0 @read @stream @fast Return the number of messages in a stream. O(1)
- XNACK v8.8.0 @write @stream @fast Releases claimed messages back to the group's PEL without acknowledging them, making them available for re-delivery. O(1) for each message ID processed.
- XPENDING v5.0.0 @read @stream @slow Returns the information and entries from a stream consumer group's pending entries list. O(N) with N being the number of elements returned, so asking for a small fixed number of entries per call is O(1). O(M), where M is the total number of entries scanned when used with the IDLE filter. When the command returns just the summary and the list of consumers is small, it runs in O(1) time; otherwise, an additional O(N) time for iterating every consumer.
- XRANGE v5.0.0 @read @stream @slow Returns the messages from a stream within a range of IDs. O(N) with N being the number of elements being returned. If N is constant (e.g. always asking for the first 10 elements with COUNT), you can consider it O(1).
- XREAD v5.0.0 @read @stream @slow @blocking Returns messages from multiple streams with IDs greater than the ones requested. Blocks until a message is available otherwise.
- XREADGROUP v5.0.0 @write @stream @slow @blocking Returns new or historical messages from a stream for a consumer in a group. Blocks until a message is available otherwise. For each stream mentioned: O(M) with M being the number of elements returned. If M is constant (e.g. always asking for the first 10 elements with COUNT), you can consider it O(1). On the other side when XREADGROUP blocks, XADD will pay the O(N) time in order to serve the N clients blocked on the stream getting new data.
- XREVRANGE v5.0.0 @read @stream @slow Returns the messages from a stream within a range of IDs in reverse order. O(N) with N being the number of elements returned. If N is constant (e.g. always asking for the first 10 elements with COUNT), you can consider it O(1).
- XSETID v5.0.0 @write @stream @fast An internal command for replicating stream values. O(1)
- XTRIM v5.0.0 @write @stream @slow Deletes messages from the beginning of a stream. O(N), with N being the number of evicted entries. Constant times are very small however, since entries are organized in macro nodes containing multiple entries that can be released with a single deallocation.

A Redis stream is a data structure that acts like an append-only log but also implements several operations to overcome some of the limits of a typical append-only log. These include random access in O(1) time and complex consumption strategies, such as consumer groups. You can use streams to record and simultaneously syndicate events in real time. Examples of Redis stream use cases include:

- Event sourcing (e.g., tracking user actions, clicks, etc.)
- Sensor monitoring (e.g., readings from devices in the field)
- Notifications (e.g., storing a record of each user's notifications in a separate stream)

Redis generates a unique ID for each stream entry. You can use these IDs to retrieve their associated entries later or to read and process all subsequent entries in the stream. Note that because these IDs are related to time, the ones shown here may vary and will be different from the IDs you see in your own Redis instance.

Redis streams support several trimming strategies (to prevent streams from growing unbounded) and more than one consumption strategy (see `XREAD`, `XREADGROUP`, and `XRANGE`). Starting with Redis 8.2, the `XACKDEL`, `XDELEX`, `XADD`, and `XTRIM` commands provide fine-grained control over how stream operations interact with multiple consumer groups, simplifying the coordination of message processing across different applications.

Beginning with Redis 8.6, Redis streams support idempotent message processing (at-most-once production) to prevent duplicate entries when using at-least-once delivery patterns. This feature enables reliable message submission with automatic deduplication. See Idempotent Message Processing for more information.


## Examples

- When our racers pass a checkpoint, we add a stream entry for each racer that includes the racer's name, speed, position, and location ID: Foundational: Add entries to a stream using XADD with auto-generated IDs (creates new entries with field-value pairs) `> XADD race:france * rider Castilla speed 30.2 position 1 location_id 1 "1692632086370-0" > XADD race:france * rider Norem speed 28.8 position 3 location_id 1 "1692632094485-0" > XADD race:france * rider Prickett speed 29.7 position 2 location_id 1 "1692632102976-0"` `res1 = r.xadd( "race:france", {"rider": "Castilla", "speed": 30.2, "position": 1, "location_id": 1}, ) print(res1) # >>> 1692629576966-0 res2 = r.xadd( "race:france", {"rider": "Norem", "speed": 28.8, "position": 3, "location_id": 1}, ) print(res2) # >>> 1692629594113-0 res3 = r.xadd( "race:france", {"rider": "Prickett", "speed": 29.7, "position": 2, "location_id": 1}, ) print(res3) # >>> 1692629613374-0` `const res1 = await client.xAdd( 'race:france', '*', { 'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1' } ); console.log(res1); // >>> 1700073067968-0 N.B. actual values will differ from these examples const res2 = await client.xAdd( 'race:france', '*', { 'rider': 'Norem', 'speed': '28.8', 'position': '3', 'location_id': '1' }, ); console.log(res2); // >>> 1692629594113-0 const res3 = await client.xAdd( 'race:france', '*', { 'rider': 'Prickett', 'speed': '29.7', 'position': '2', 'location_id': '1' }, ); console.log(res3); // >>> 1692629613374-0` `StreamEntryID res1 = jedis.xadd("race:france",new HashMap<String,String>(){{put("rider","Castilla");put("speed","30.2");put("position","1");put("location_id","1");}} , XAddParams.xAddParams()); System.out.println(res1); // >>> 1701760582225-0 StreamEntryID res2 = jedis.xadd("race:france",new HashMap<String,String>(){{put("rider","Norem");put("speed","28.8");put("position","3");put("location_id","1");}} , XAddParams.xAddParams()); System.out.println(res2); // >>> 1701760582225-1 StreamEntryID res3 = jedis.xadd("race:france",new HashMap<String,String>(){{put("rider","Prickett");put("speed","29.7");put("position","2");put("location_id","1");}} , XAddParams.xAddParams()); System.out.println(res3); // >>> 1701760582226-0` `res1, err := rdb.XAdd(ctx, &redis.XAddArgs{ Stream: "race:france", Values: map[string]interface{}{ "rider": "Castilla", "speed": 30.2, "position": 1, "location_id": 1, }, }).Result() if err != nil { panic(err) } // fmt.Println(res1) // >>> 1692632086370-0 res2, err := rdb.XAdd(ctx, &redis.XAddArgs{ Stream: "race:france", Values: map[string]interface{}{ "rider": "Norem", "speed": 28.8, "position": 3, "location_id": 1, }, }).Result() if err != nil { panic(err) } // fmt.PrintLn(res2) // >>> 1692632094485-0 res3, err := rdb.XAdd(ctx, &redis.XAddArgs{ Stream: "race:france", Values: map[string]interface{}{ "rider": "Prickett", "speed": 29.7, "position": 2, "location_id": 1, }, }).Result() if err != nil { panic(err) } // fmt.Println(res3) // >>> 1692632102976-0` `RedisValue res1 = db.StreamAdd( "race:france", [ new("rider", "Castilla"), new("speed", 30.2), new("position", 1), new("location_id", 1) ] ); Console.WriteLine(res1); // >>> 1712668482289-0 RedisValue res2 = db.StreamAdd( "race:france", [ new("rider", "Norem"), new("speed", 28.8), new("position", 3), new("location_id", 1) ] ); Console.WriteLine(res2); // >>> 1712668766534-1 RedisValue res3 = db.StreamAdd( "race:france", [ new("rider", "Prickett"), new("speed", 29.7), new("position", 2), new("location_id", 1) ] ); Console.WriteLine(res3); // >>> 1712669055705-0` `res1 = r.xadd('race:france', { 'rider' => 'Castilla', 'speed' => 30.2, 'position' => 1, 'location_id' => 1 }) puts res1 # 1692632086370-0, for example res2 = r.xadd('race:france', { 'rider' => 'Norem', 'speed' => 28.8, 'position' => 3, 'location_id' => 1 }) puts res2 # 1692632094485-0, for example res3 = r.xadd('race:france', { 'rider' => 'Prickett', 'speed' => 29.7, 'position' => 2, 'location_id' => 1 }) puts res3 # 1692632102976-0, for example` `let res1 = { let res: Option<String> = r .xadd( "race:france", "*", &[ ("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1"), ], ) .expect("xadd 1"); res.expect("missing stream id") }; println!("{res1}"); // >>> 1692632086370-0 let res2 = { let res: Option<String> = r .xadd( "race:france", "*", &[ ("rider", "Norem"), ("speed", "28.8"), ("position", "3"), ("location_id", "1"), ], ) .expect("xadd 2"); res.expect("missing stream id") }; println!("{res2}"); // >>> 1692632094485-0 let res3 = { let res: Option<String> = r .xadd( "race:france", "*", &[ ("rider", "Prickett"), ("speed", "29.7"), ("position", "2"), ("location_id", "1"), ], ) .expect("xadd 3"); res.expect("missing stream id") }; println!("{res3}"); // >>> 1692632102976-0` `let res1: Option<String> = r .xadd( "race:france", "*", &[ ("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1"), ], ) .await .expect("xadd 1"); let res1 = res1.expect("missing stream id"); println!("{res1}"); // >>> 1692632086370-0 let res2: Option<String> = r .xadd( "race:france", "*", &[ ("rider", "Norem"), ("speed", "28.8"), ("position", "3"), ("location_id", "1"), ], ) .await .expect("xadd 2"); let res2 = res2.expect("missing stream id"); println!("{res2}"); // >>> 1692632094485-0 let res3: Option<String> = r .xadd( "race:france", "*", &[ ("rider", "Prickett"), ("speed", "29.7"), ("position", "2"), ("location_id", "1"), ], ) .await .expect("xadd 3"); let res3 = res3.expect("missing stream id"); println!("{res3}"); // >>> 1692632102976-0`
- Read two stream entries starting at ID `1692632086370-0`: Foundational: Retrieve stream entries within a range of IDs using XRANGE when you need to access historical data `> XRANGE race:france 1692632086370-0 + COUNT 2 1) 1) "1692632086370-0" 2) 1) "rider" 2) "Castilla" 3) "speed" 4) "30.2" 5) "position" 6) "1" 7) "location_id" 8) "1" 2) 1) "1692632094485-0" 2) 1) "rider" 2) "Norem" 3) "speed" 4) "28.8" 5) "position" 6) "3" 7) "location_id" 8) "1"` `res4 = r.xrange("race:france", "1691765278160-0", "+", 2) print( res4 ) # >>> [ # ('1692629576966-0', # {'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1'} # ), # ('1692629594113-0', # {'rider': 'Norem', 'speed': '28.8', 'position': '3', 'location_id': '1'} # ) # ]` `const res4 = await client.xRange('race:france', '1691765278160-0', '+', {COUNT: 2}); console.log(res4); // >>> [{ id: '1692629576966-0', message: { rider: 'Castilla', speed: '30.2', position: '1', location_id: '1' } }, { id: '1692629594113-0', message: { rider: 'Norem', speed: '28.8', position: '3', location_id: '1' } }]` `List<StreamEntry> res4 = jedis.xrange("race:france","1701760582225-0","+",2); System.out.println(res4); // >>> [1701760841292-0 {rider=Castilla, speed=30.2, location_id=1, position=1}, 1701760841292-1 {rider=Norem, speed=28.8, location_id=1, position=3}]` `res4, err := rdb.XRangeN(ctx, "race:france", "1691765278160-0", "+", 2).Result() if err != nil { panic(err) } fmt.Println(res4) // >>> [{1692632086370-0 map[location_id:1 position:1 rider:Castilla...` `StreamEntry[] res4 = db.StreamRange("race:france", "1712668482289-0", "+", 2); foreach (StreamEntry entry in res4) { Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]"); } // >>> 1712668482289-0: [rider: Castilla, speed: 30.199999999999999, position: 1, location_id: 1] // >>> 1712668766534-1: [rider: Norem, speed: 28.800000000000001, position: 3, location_id: 1]` `r.del('race:france') r.xadd('race:france', { 'rider' => 'Castilla', 'speed' => '30.2', 'position' => '1', 'location_id' => '1' }, id: '1692632086370-0') r.xadd('race:france', { 'rider' => 'Norem', 'speed' => '28.8', 'position' => '3', 'location_id' => '1' }, id: '1692632094485-0') r.xadd('race:france', { 'rider' => 'Prickett', 'speed' => '29.7', 'position' => '2', 'location_id' => '1' }, id: '1692632102976-0') r.xadd('race:france', { 'rider' => 'Castilla', 'speed' => '29.9', 'position' => '1', 'location_id' => '2' }, id: '1692632147973-0') res4 = r.xrange('race:france', '1692632086370-0', '+', count: 2) puts res4.inspect # [["1692632086370-0", {"rider"=>"Castilla", "speed"=>"30.2", "position"=>"1", "location_id"=>"1"}], # ["1692632094485-0", {"rider"=>"Norem", "speed"=>"28.8", "position"=>"3", "location_id"=>"1"}]]` `if let Ok(res) = r.xrange_count("race:france", "1692632086370-0", "+", 2) { let res: StreamRangeReply = res; let view: Vec<_> = res .ids .iter() .map(|entry| { ( entry.id.clone(), vec![ ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")), ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")), ("position".to_string(), entry.get::<String>("position").expect("missing position")), ( "location_id".to_string(), entry.get::<String>("location_id").expect("missing location_id"), ), ], ) }) .collect(); println!("{view:?}"); // >>> [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")]), ("1692632094485-0", [("rider", "Norem"), ("speed", "28.8"), ("position", "3"), ("location_id", "1")])] }` `if let Ok(res) = r.xrange_count("race:france", "1692632086370-0", "+", 2).await { let res: StreamRangeReply = res; let view: Vec<_> = res .ids .iter() .map(|entry| { ( entry.id.clone(), vec![ ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")), ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")), ("position".to_string(), entry.get::<String>("position").expect("missing position")), ( "location_id".to_string(), entry.get::<String>("location_id").expect("missing location_id"), ), ], ) }) .collect(); println!("{view:?}"); // >>> [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")]), ("1692632094485-0", [("rider", "Norem"), ("speed", "28.8"), ("position", "3"), ("location_id", "1")])] }`
- Read up to 100 new stream entries, starting at the end of the stream, and block for up to 300 ms if no entries are being written: Use XREAD with BLOCK to wait for new entries when you need to consume messages as they arrive `> XREAD COUNT 100 BLOCK 300 STREAMS race:france $ (nil)` `res5 = r.xread(streams={"race:france": 0}, count=100, block=300) print( res5 ) # >>> [ # ['race:france', # [('1692629576966-0', # {'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1'} # ), # ('1692629594113-0', # {'rider': 'Norem', 'speed': '28.8', 'position': '3', 'location_id': '1'} # ), # ('1692629613374-0', # {'rider': 'Prickett', 'speed': '29.7', 'position': '2', 'location_id': '1'} # )] # ] # ]` `const res5 = await client.xRead({ key: 'race:france', id: '0-0' }, { COUNT: 100, BLOCK: 300 }); console.log(res5); // >>> [{ name: 'race:france', messages: [{ id: '1692629576966-0', message: { rider: 'Castilla', speed: '30.2', position: '1', location_id: '1' } }, { id: '1692629594113-0', message: { rider: 'Norem', speed: '28.8', position: '3', location_id: '1' } }, { id: '1692629613374-0', message: { rider: 'Prickett', speed: '29.7', position: '2', location_id: '1' } }] }]` `List<Map.Entry<String, List<StreamEntry>>> res5= jedis.xread(XReadParams.xReadParams().block(300).count(100),new HashMap<String,StreamEntryID>(){{put("race:france",new StreamEntryID());}}); System.out.println( res5 ); // >>> [race:france=[1701761996660-0 {rider=Castilla, speed=30.2, location_id=1, position=1}, 1701761996661-0 {rider=Norem, speed=28.8, location_id=1, position=3}, 1701761996661-1 {rider=Prickett, speed=29.7, location_id=1, position=2}]]` `res5, err := rdb.XRead(ctx, &redis.XReadArgs{ Streams: []string{"race:france", "0"}, Count: 100, Block: 300, }).Result() if err != nil { panic(err) } fmt.Println(res5) // >>> // [{race:france [{1692632086370-0 map[location_id:1 position:1...` `StreamEntry[] res5 = db.StreamRead("race:france", 0, 100); foreach (StreamEntry entry in res4) { Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]"); } // >>> 1712668482289-0: [rider: Castilla, speed: 30.199999999999999, position: 1, location_id: 1] // >>> 1712668766534-1: [rider: Norem, speed: 28.800000000000001, position: 3, location_id: 1] // >>> 1712669055705-0: [rider: Prickett, speed: 29.699999999999999, position: 2, location_id: 1]` `r.del('race:france') r.xadd('race:france', {'rider' => 'Castilla'}, id: '1692632086370-0') res5 = r.xread(['race:france'], ['$'], count: 100, block: 300) puts res5.inspect # {}` `let opts = StreamReadOptions::default().count(100).block(300); if let Ok(res) = r.xread_options(&["race:france"], &["$"], &opts) { let res: Option<StreamReadReply> = res; println!("{res:?}"); // >>> None }` `let opts = StreamReadOptions::default().count(100).block(300); if let Ok(res) = r.xread_options(&["race:france"], &["$"], &opts).await { let res: Option<StreamReadReply> = res; println!("{res:?}"); // >>> None }`


## Performance

Adding an entry to a stream is O(1). Accessing any single entry is O(n), where *n* is the length of the ID. Since stream IDs are typically short and of a fixed length, this effectively reduces to a constant time lookup. For details on why, note that streams are implemented as radix trees.

Simply put, Redis streams provide highly efficient inserts and reads. See each command's time complexity for the details.


## Streams basics

Streams are an append-only data structure. The fundamental write command, called `XADD`, appends a new entry to the specified stream.

Each stream entry consists of one or more field-value pairs, somewhat like a dictionary or a Redis hash:

Foundational: Add a single entry to a stream with multiple field-value pairs using XADD

```plaintext
> XADD race:france * rider Castilla speed 29.9 position 1 location_id 2
"1692632147973-0"
```

```python
res6 = r.xadd(
    "race:france",
    {"rider": "Castilla", "speed": 29.9, "position": 1, "location_id": 2},
)
print(res6)  # >>> 1692629676124-0
```

```node
const res6 = await client.xAdd(
  'race:france', '*', {
    'rider': 'Castilla',
    'speed': '29.9',
    'position': '1',
    'location_id': '2'
  }
);
console.log(res6); // >>> 1692629676124-0
```

```java
    StreamEntryID res6 = jedis.xadd("race:france",new HashMap<String,String>(){{put("rider","Castilla");put("speed","29.9");put("position","2");put("location_id","1");}} , XAddParams.xAddParams());
    System.out.println(res6); // >>> 1701762285679-0
```

```go
	res6, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:france",
		Values: map[string]interface{}{
			"rider":       "Castilla",
			"speed":       29.9,
			"position":    1,
			"location_id": 2,
		},
	}).Result()

	if err != nil {
		panic(err)
	}

	//fmt.Println(res6) // >>> 1692632147973-0
```

```c#
        RedisValue res6 = db.StreamAdd(
            "race:france",
            [
                new("rider", "Castilla"),
                new("speed", 29.9),
                new("position", 1),
                new("location_id", 2)
            ]
        );

        Console.WriteLine(res6);    // >>> 1712675674750-0
```

```ruby
res6 = r.xadd('race:france', {
  'rider' => 'Castilla',
  'speed' => 29.9,
  'position' => 1,
  'location_id' => 2
})
puts res6 # 1692632147973-0, for example
```

```rust
        if let Ok(res) = r.xadd(
            "race:france",
            "*",
            &[
                ("rider", "Castilla"),
                ("speed", "29.9"),
                ("position", "1"),
                ("location_id", "2"),
            ],
        ) {
            let res: Option<String> = res;
            let res = res.expect("missing stream id");
            println!("{res}"); // >>> 1692632147973-0
        }
```

```rust
        if let Ok(res) = r
            .xadd(
                "race:france",
                "*",
                &[
                    ("rider", "Castilla"),
                    ("speed", "29.9"),
                    ("position", "1"),
                    ("location_id", "2"),
                ],
            )
            .await
        {
            let res: Option<String> = res;
            let res = res.expect("missing stream id");
            println!("{res}"); // >>> 1692632147973-0
        }
```

The above call to the `XADD` command adds an entry `rider: Castilla, speed: 29.9, position: 1, location_id: 2` to the stream at key `race:france`, using an auto-generated entry ID, which is the one returned by the command, specifically `1692632147973-0`. It gets as its first argument the key name `race:france`, the second argument is the entry ID that identifies every entry inside a stream. However, in this case, we passed `*` because we want the server to generate a new ID for us. Every new ID will be monotonically increasing, so in more simple terms, every new entry added will have a higher ID compared to all the past entries. Auto-generation of IDs by the server is almost always what you want, and the reasons for specifying an ID explicitly are very rare. We'll talk more about this later. The fact that each Stream entry has an ID is another similarity with log files, where line numbers, or the byte offset inside the file, can be used in order to identify a given entry. Returning back at our `XADD` example, after the key name and ID, the next arguments are the field-value pairs composing our stream entry.

It is possible to get the number of items inside a Stream just using the `XLEN` command:

Foundational: Get the total number of entries in a stream using XLEN

```plaintext
> XLEN race:france
(integer) 4
```

```python
res7 = r.xlen("race:france")
print(res7)  # >>> 4
```

```node
const res7 = await client.xLen('race:france');
console.log(res7); // >>> 4
```

```java
    long res7 = jedis.xlen("race:france");
    System.out.println(res7); // >>> 4
```

```go
	res7, err := rdb.XLen(ctx, "race:france").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7) // >>> 4
```

```c#
        long res7 = db.StreamLength("race:france");
        Console.WriteLine(res7);    // >>> 4
```

```ruby
r.del('race:france')
r.xadd('race:france', {'rider' => 'Castilla'}, id: '1692632086370-0')
r.xadd('race:france', {'rider' => 'Norem'}, id: '1692632094485-0')
r.xadd('race:france', {'rider' => 'Prickett'}, id: '1692632102976-0')
r.xadd('race:france', {'rider' => 'Castilla'}, id: '1692632147973-0')
res7 = r.xlen('race:france')
puts res7 # 4
```

```rust
        if let Ok(res) = r.xlen("race:france") {
            let res: usize = res;
            println!("{res}"); // >>> 4
        }
```

```rust
        add_france_fixed(&mut r).await;
        if let Ok(res) = r.xlen("race:france").await {
            let res: usize = res;
            println!("{res}"); // >>> 4
        }
```

### Entry IDs

The entry ID returned by the `XADD` command, and identifying univocally each entry inside a given stream, is composed of two parts:

```
<millisecondsTime>-<sequenceNumber>
```

The milliseconds time part is actually the local time in the local Redis node generating the stream ID, however if the current milliseconds time happens to be smaller than the previous entry time, then the previous entry time is used instead, so if a clock jumps backward the monotonically incrementing ID property still holds. The sequence number is used for entries created in the same millisecond. Since the sequence number is 64 bit wide, in practical terms there is no limit to the number of entries that can be generated within the same millisecond.

The format of such IDs may look strange at first, and the gentle reader may wonder why the time is part of the ID. The reason is that Redis streams support range queries by ID. Because the ID is related to the time the entry is generated, this gives the ability to query for time ranges basically for free. We will see this soon while covering the `XRANGE` command.

If for some reason the user needs incremental IDs that are not related to time but are actually associated to another external system ID, as previously mentioned, the `XADD` command can take an explicit ID instead of the `*` wildcard ID that triggers auto-generation, like in the following examples:

Specify explicit stream entry IDs instead of auto-generated ones when you need to use external system IDs

```plaintext
> XADD race:usa 0-1 racer Castilla
0-1
> XADD race:usa 0-2 racer Norem
0-2
```

```python
res8 = r.xadd("race:usa", {"racer": "Castilla"}, id="0-1")
print(res8)  # >>> 0-1

res9 = r.xadd("race:usa", {"racer": "Norem"}, id="0-2")
print(res9)  # >>> 0-2
```

```node
const res8 = await client.xAdd('race:usa', '0-1', {
  'racer': 'Castilla'
});
console.log(res8); // >>> 0-1

const res9 = await client.xAdd('race:usa', '0-2', {
  'racer': 'Norem'
});
console.log(res9); // >>> 0-2
```

```java
    StreamEntryID res8 = jedis.xadd("race:usa", new HashMap<String,String>(){{put("racer","Castilla");}},XAddParams.xAddParams().id("0-1"));
    System.out.println(res8); // >>> 0-1

    StreamEntryID res9 = jedis.xadd("race:usa", new HashMap<String,String>(){{put("racer","Norem");}},XAddParams.xAddParams().id("0-2"));
    System.out.println(res9); // >>> 0-2
```

```go
	res8, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:usa",
		Values: map[string]interface{}{
			"racer": "Castilla",
		},
		ID: "0-1",
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res8) // >>> 0-1

	res9, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:usa",
		Values: map[string]interface{}{
			"racer": "Norem",
		},
		ID: "0-2",
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res9) // >>> 0-2
```

```c#
        RedisValue res8 = db.StreamAdd(
            "race:usa",
            [
                new("racer", "Castilla")
            ],
            "0-1"
        );
        Console.WriteLine(res8);    // >>> 0-1

        RedisValue res9 = db.StreamAdd(
            "race:usa",
            [
                new("racer", "Norem")
            ],
            "0-2"
        );
        Console.WriteLine(res9);    // >>> 0-2
```

```ruby
r.del('race:usa')
res8 = r.xadd('race:usa', {'racer' => 'Castilla'}, id: '0-1')
puts res8 # 0-1

res9 = r.xadd('race:usa', {'racer' => 'Norem'}, id: '0-2')
puts res9 # 0-2
```

```rust
        if let Ok(res) = r.xadd("race:usa", "0-1", &[("racer", "Castilla")]) {
            let res: Option<String> = res;
            let res = res.expect("missing stream id");
            println!("{res}"); // >>> 0-1
        }

        if let Ok(res) = r.xadd("race:usa", "0-2", &[("racer", "Norem")]) {
            let res: Option<String> = res;
            let res = res.expect("missing stream id");
            println!("{res}"); // >>> 0-2
        }
```

```rust
        delete_keys(&mut r, &["race:usa"]).await;
        if let Ok(res) = r.xadd("race:usa", "0-1", &[("racer", "Castilla")]).await {
            let res: Option<String> = res;
            let res = res.expect("missing stream id");
            println!("{res}"); // >>> 0-1
        }
        if let Ok(res) = r.xadd("race:usa", "0-2", &[("racer", "Norem")]).await {
            let res: Option<String> = res;
            let res = res.expect("missing stream id");
            println!("{res}"); // >>> 0-2
        }
```

Note that in this case, the minimum ID is 0-1 and that the command will not accept an ID equal or smaller than a previous one:

Understand ID validation - XADD rejects IDs that are not monotonically increasing

```plaintext
> XADD race:usa 0-1 racer Prickett
(error) ERR The ID specified in XADD is equal or smaller than the target stream top item
```

```python
try:
    res10 = r.xadd("race:usa", {"racer": "Prickett"}, id="0-1")
    print(res10)  # >>> 0-1
except redis.exceptions.ResponseError as e:
    print(e)  # >>> WRONGID
```

```node
try {
  const res10 = await client.xAdd('race:usa', '0-1', {
    'racer': 'Prickett'
  });
  console.log(res10); // >>> 0-1
} catch (error) {
  console.error(error); // >>> [SimpleError: ERR The ID specified in XADD is equal or smaller than the target stream top item]
}
```

```java
    try {
      StreamEntryID res10 = jedis.xadd("race:usa", new HashMap<String,String>(){{put("racer","Prickett");}},XAddParams.xAddParams().id("0-1"));
      System.out.println(res10); // >>> 0-1
    }
    catch (JedisDataException e){
      System.out.println(e); // >>> ERR The ID specified in XADD is equal or smaller than the target stream top item
    }
```

```go
	res10, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Values: map[string]interface{}{
			"racer": "Prickett",
		},
		ID: "0-1",
	}).Result()

	if err != nil {
		// fmt.Println(err)
		// >>> ERR The ID specified in XADD is equal or smaller than the target stream top item
	}
```

```c#
        try
        {
            RedisValue res10 = db.StreamAdd(
                "race:usa",
                [
                    new("racer", "Prickett")
                ],
                "0-1"
            );
        }
        catch (RedisServerException ex)
        {
            Console.WriteLine(ex);  // >>> ERR The ID specified in XADD is equal or smaller than the target stream top item
        }
```

```ruby
begin
  r.xadd('race:usa', {'racer' => 'Prickett'}, id: '0-1')
rescue Redis::CommandError => e
  puts e.message
  # ERR The ID specified in XADD is equal or smaller than the target stream top item
end
```

```rust
        let res: redis::RedisResult<Option<String>> =
            r.xadd("race:usa", "0-1", &[("racer", "Prickett")]);
        match res {
            Ok(_) => {}
            Err(e) => {
                let msg = e.to_string();
                println!("{msg}");
                // >>> An error was signalled by the server - ResponseError: The ID specified in XADD is equal or smaller than the target stream top item
            }
        }
```

```rust
        let res: redis::RedisResult<Option<String>> =
            r.xadd("race:usa", "0-1", &[("racer", "Prickett")]).await;
        match res {
            Ok(_) => {}
            Err(e) => {
                let msg = e.to_string();
                println!("{msg}");
                // >>> An error was signalled by the server - ResponseError: The ID specified in XADD is equal or smaller than the target stream top item
            }
        }
```

If you're running Redis 7 or later, you can also provide an explicit ID consisting of the milliseconds part only. In this case, the sequence portion of the ID will be automatically generated. To do this, use the syntax below:

Use partial explicit IDs with XADD to specify milliseconds while letting Redis auto-generate the sequence number

```plaintext
> XADD race:usa 0-* racer Prickett
0-3
```

```python
# Not yet implemented
```

```node
const res11a = await client.xAdd('race:usa', '0-*', { racer: 'Norem' });
console.log(res11a); // >>> 0-3
```

```java
    StreamEntryID res11 = jedis.xadd("race:usa", new HashMap<String,String>(){{put("racer","Norem");}},XAddParams.xAddParams().id("0-*"));
    System.out.println(res11);
```

```go
	res11, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:usa",
		Values: map[string]interface{}{
			"racer": "Prickett",
		},
		ID: "0-*",
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res11) // >>> 0-3
```

```c#
        RedisValue res11 = "";
        Version version = muxer.GetServer("localhost:6379").Version;
        if (version.Major >= 7)
        {
            res11 = db.StreamAdd(
                "race:usa",
                [
                    new("rider", "Norem")
                ],
                "0-*"
            );

            Console.WriteLine(res11);   // >>> "0-3"
        }
```

```ruby
r.del('race:usa')
r.xadd('race:usa', {'racer' => 'Castilla'}, id: '0-1')
r.xadd('race:usa', {'racer' => 'Norem'}, id: '0-2')
res10 = r.xadd('race:usa', {'racer' => 'Prickett'}, id: '0-*')
puts res10 # 0-3
```

```rust
        if let Ok(res) = r.xadd("race:usa", "0-*", &[("racer", "Prickett")]) {
            let res: Option<String> = res;
            let res = res.expect("missing stream id");
            println!("{res}"); // >>> 0-3
        }
```

```rust
        seed_usa_fixed(&mut r).await;
        if let Ok(res) = r.xadd("race:usa", "0-*", &[("racer", "Prickett")]).await {
            let res: Option<String> = res;
            let res = res.expect("missing stream id");
            println!("{res}"); // >>> 0-3
        }
```
