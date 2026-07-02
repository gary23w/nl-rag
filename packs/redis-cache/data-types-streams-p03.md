---
title: "Redis Streams (part 3/5)"
source: https://redis.io/docs/latest/develop/data-types/streams/
domain: redis-cache
license: CC-BY-SA-4.0
tags: redis, in-memory data store, key-value cache, in-memory database
fetched: 2026-07-02
part: 3/5
---

## Consumer groups

When the task at hand is to consume the same stream from different clients, then `XREAD` already offers a way to *fan-out* to N clients, potentially also using replicas in order to provide more read scalability. However in certain problems what we want to do is not to provide the same stream of messages to many clients, but to provide a *different subset* of messages from the same stream to many clients. An obvious case where this is useful is that of messages which are slow to process: the ability to have N different workers that will receive different parts of the stream allows us to scale message processing, by routing different messages to different workers that are ready to do more work.

In practical terms, if we imagine having three consumers C1, C2, C3, and a stream that contains the messages 1, 2, 3, 4, 5, 6, 7 then what we want is to serve the messages according to the following diagram:

```
1 -> C1
2 -> C2
3 -> C3
4 -> C1
5 -> C2
6 -> C3
7 -> C1
```

In order to achieve this, Redis uses a concept called *consumer groups*. It is very important to understand that Redis consumer groups have nothing to do, from an implementation standpoint, with Kafka (TM) consumer groups. Yet they are similar in functionality, so I decided to keep Kafka's (TM) terminology, as it originally popularized this idea.

A consumer group is like a *pseudo consumer* that gets data from a stream, and actually serves multiple consumers, providing certain guarantees:

1. Each message is served to a different consumer so that it is not possible that the same message will be delivered to multiple consumers.
2. Consumers are identified, within a consumer group, by a name, which is a case-sensitive string that the clients implementing consumers must choose. This means that even after a disconnect, the stream consumer group retains all the state, since the client will claim again to be the same consumer. However, this also means that it is up to the client to provide a unique identifier.
3. Each consumer group has the concept of the *first ID never consumed* so that, when a consumer asks for new messages, it can provide just messages that were not previously delivered.
4. Consuming a message, however, requires an explicit acknowledgment using a specific command. Redis interprets the acknowledgment as: this message was correctly processed so it can be evicted from the consumer group.
5. A consumer group tracks all the messages that are currently pending, that is, messages that were delivered to some consumer of the consumer group, but are yet to be acknowledged as processed. Thanks to this feature, when accessing the message history of a stream, each consumer *will only see messages that were delivered to it*.

In a way, a consumer group can be imagined as some *amount of state* about a stream:

```
+----------------------------------------+
| consumer_group_name: mygroup           |
| consumer_group_stream: somekey         |
| last_delivered_id: 1292309234234-92    |
|                                        |
| consumers:                             |
|    "consumer-1" with pending messages  |
|       1292309234234-4                  |
|       1292309234232-8                  |
|    "consumer-42" with pending messages |
|       ... (and so forth)               |
+----------------------------------------+
```

If you see this from this point of view, it is very simple to understand what a consumer group can do, how it is able to just provide consumers with their history of pending messages, and how consumers asking for new messages will just be served with message IDs greater than `last_delivered_id`. At the same time, if you look at the consumer group as an auxiliary data structure for Redis streams, it is obvious that a single stream can have multiple consumer groups, that have a different set of consumers. Actually, it is even possible for the same stream to have clients reading without consumer groups via `XREAD`, and clients reading via `XREADGROUP` in different consumer groups.

Now it's time to zoom in to see the fundamental consumer group commands. They are the following:

- `XGROUP` is used in order to create, destroy and manage consumer groups.
- `XREADGROUP` is used to read from a stream via a consumer group.
- `XACK` is the command that allows a consumer to mark a pending message as correctly processed.
- `XNACK` is the command that allows a consumer to release pending messages back to the group without acknowledging them, making them immediately available for re-delivery to other consumers.
- `XACKDEL` combines acknowledgment and deletion in a single atomic operation with enhanced control over consumer group references.


## Creating a consumer group

Assuming I have a key `race:france` of type stream already existing, in order to create a consumer group I just need to do the following:

Foundational: Create a consumer group for a stream using XGROUP CREATE to enable coordinated message consumption

```plaintext
> XGROUP CREATE race:france france_riders $
OK
```

```python
res18 = r.xgroup_create("race:france", "france_riders", "$")
print(res18)  # >>> True
```

```node
const res18 = await client.xGroupCreate('race:france', 'france_riders', '$');
console.log(res18); // >>> OK
```

```java
    String res19 = jedis.xgroupCreate("race:france","france_riders",StreamEntryID.LAST_ENTRY,false);
    System.out.println(res19); // >>> OK
```

```go
	res19, err := rdb.XGroupCreate(ctx, "race:france", "france_riders", "$").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res19) // >>> OK
```

```c#
        bool res19 = db.StreamCreateConsumerGroup("race:france", "france_riders", "$");
        Console.WriteLine(res19);   // >>> true
```

```ruby
r.del('race:france')
r.xadd('race:france', {'rider' => 'Castilla'}, id: '1692632086370-0')
res18 = r.xgroup(:create, 'race:france', 'france_riders', '$')
puts res18 # OK
```

```rust
        if let Ok(res) = r.xgroup_create("race:france", "france_riders", "$") {
            let res: () = res;
            let _ = res;
            println!("OK"); // >>> OK
        }
```

```rust
        add_france_fixed(&mut r).await;
        if let Ok(res) = r.xgroup_create("race:france", "france_riders", "$").await {
            let res: () = res;
            let _ = res;
            println!("OK"); // >>> OK
        }
```

As you can see in the command above when creating the consumer group we have to specify an ID, which in the example is just `$`. This is needed because the consumer group, among the other states, must have an idea about what message to serve next at the first consumer connecting, that is, what was the *last message ID* when the group was just created. If we provide `$` as we did, then only new messages arriving in the stream from now on will be provided to the consumers in the group. If we specify `0` instead the consumer group will consume *all* the messages in the stream history to start with. Of course, you can specify any other valid ID. What you know is that the consumer group will start delivering messages that are greater than the ID you specify. Because `$` means the current greatest ID in the stream, specifying `$` will have the effect of consuming only new messages.

`XGROUP CREATE` also supports creating the stream automatically, if it doesn't exist, using the optional `MKSTREAM` subcommand as the last argument:

Create a consumer group and stream atomically using XGROUP CREATE with MKSTREAM option

```plaintext
> XGROUP CREATE race:italy italy_riders $ MKSTREAM
OK
```

```python
res19 = r.xgroup_create("race:italy", "italy_riders", "$", mkstream=True)
print(res19)  # >>> True
```

```node
const res19 = await client.xGroupCreate('race:italy', 'italy_riders', '$', {
  MKSTREAM: true
});
console.log(res19); // >>> OK
```

```java
    String res20 = jedis.xgroupCreate("race:italy","italy_riders",StreamEntryID.LAST_ENTRY,true);
    System.out.println(res20); // >>> OK
```

```go
	res20, err := rdb.XGroupCreateMkStream(ctx,
		"race:italy", "italy_riders", "$",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res20) // >>> OK
```

```c#
        bool res20 = db.StreamCreateConsumerGroup("race:italy", "italy_riders", "$", true);
        Console.WriteLine(res20);   // >>> true
```

```ruby
r.del('race:italy')
res19 = r.xgroup(:create, 'race:italy', 'italy_riders', '$', mkstream: true)
puts res19 # OK
```

```rust
        if let Ok(res) = r.xgroup_create_mkstream("race:italy", "italy_riders", "$") {
            let res: () = res;
            let _ = res;
            println!("OK"); // >>> OK
        }
```

```rust
        delete_keys(&mut r, &["race:italy"]).await;
        if let Ok(res) = r.xgroup_create_mkstream("race:italy", "italy_riders", "$").await {
            let res: () = res;
            let _ = res;
            println!("OK"); // >>> OK
        }
```

Now that the consumer group is created we can immediately try to read messages via the consumer group using the `XREADGROUP` command. We'll read from consumers, that we will call Alice and Bob, to see how the system will return different messages to Alice or Bob.

`XREADGROUP` is very similar to `XREAD` and provides the same **BLOCK** option, otherwise it is a synchronous command. However there is a *mandatory* option that must be always specified, which is **GROUP** and has two arguments: the name of the consumer group, and the name of the consumer that is attempting to read. The option **COUNT** is also supported and is identical to the one in `XREAD`.

We'll add riders to the race:italy stream and try reading something using the consumer group: Note: *here rider is the field name, and the name is the associated value. Remember that stream items are small dictionaries.*

Foundational: Read new messages from a stream using a consumer group with XREADGROUP and the > special ID

```plaintext
> XADD race:italy * rider Castilla
"1692632639151-0"
> XADD race:italy * rider Royce
"1692632647899-0"
> XADD race:italy * rider Sam-Bodden
"1692632662819-0"
> XADD race:italy * rider Prickett
"1692632670501-0"
> XADD race:italy * rider Norem
"1692632678249-0"
> XREADGROUP GROUP italy_riders Alice COUNT 1 STREAMS race:italy >
1) 1) "race:italy"
   2) 1) 1) "1692632639151-0"
         2) 1) "rider"
            2) "Castilla"
```

```python
r.xadd("race:italy", {"rider": "Castilla"})
r.xadd("race:italy", {"rider": "Royce"})
r.xadd("race:italy", {"rider": "Sam-Bodden"})
r.xadd("race:italy", {"rider": "Prickett"})
r.xadd("race:italy", {"rider": "Norem"})

res20 = r.xreadgroup(
    streams={"race:italy": ">"},
    consumername="Alice",
    groupname="italy_riders",
    count=1,
)
print(res20)  # >>> [['race:italy', [('1692629925771-0', {'rider': 'Castilla'})]]]
```

```node
await client.xAdd('race:italy', '*', {
  'rider': 'Castilla'
});
await client.xAdd('race:italy', '*', {
  'rider': 'Royce'
});
await client.xAdd('race:italy', '*', {
  'rider': 'Sam-Bodden'
});
await client.xAdd('race:italy', '*', {
  'rider': 'Prickett'
});
await client.xAdd('race:italy', '*', {
  'rider': 'Norem'
});

const res20 = await client.xReadGroup(
  'italy_riders',
  'Alice', {
    key: 'race:italy',
    id: '>'
  }, {
    COUNT: 1
  }
);
console.log(res20); // >>> [{ name: 'race:italy', messages: [{ id: '1692629925771-0', message: { rider: 'Castilla' } }] }]
```

```java
    StreamEntryID id1 = jedis.xadd("race:italy", new HashMap<String,String>(){{put("rider","Castilaa");}},XAddParams.xAddParams());
    StreamEntryID id2 = jedis.xadd("race:italy", new HashMap<String,String>(){{put("rider","Royce");}},XAddParams.xAddParams());
    StreamEntryID id3 = jedis.xadd("race:italy", new HashMap<String,String>(){{put("rider","Sam-Bodden");}},XAddParams.xAddParams());
    StreamEntryID id4 = jedis.xadd("race:italy", new HashMap<String,String>(){{put("rider","Prickett");}},XAddParams.xAddParams());
    StreamEntryID id5 = jedis.xadd("race:italy", new HashMap<String,String>(){{put("rider","Norem");}},XAddParams.xAddParams());

    List<Map.Entry<String, List<StreamEntry>>> res21 = jedis.xreadGroup("italy_riders","Alice", XReadGroupParams.xReadGroupParams().count(1),new HashMap<String,StreamEntryID>(){{put("race:italy",StreamEntryID.UNRECEIVED_ENTRY);}});
    System.out.println(res21); // >>> [race:italy=[1701766299006-0 {rider=Castilaa}]]
```

```go
	_, err = rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:italy",
		Values: map[string]interface{}{"rider": "Castilla"},
	}).Result()
	// >>> 1692632639151-0

	if err != nil {
		panic(err)
	}

	_, err = rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:italy",
		Values: map[string]interface{}{"rider": "Royce"},
	}).Result()
	// >>> 1692632647899-0

	if err != nil {
		panic(err)
	}

	_, err = rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:italy",
		Values: map[string]interface{}{"rider": "Sam-Bodden"},
	}).Result()
	// >>> 1692632662819-0

	if err != nil {
		panic(err)
	}

	_, err = rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:italy",
		Values: map[string]interface{}{"rider": "Prickett"},
	}).Result()
	// >>> 1692632670501-0

	if err != nil {
		panic(err)
	}

	_, err = rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:italy",
		Values: map[string]interface{}{"rider": "Norem"},
	}).Result()
	// >>> 1692632678249-0

	if err != nil {
		panic(err)
	}

	// fmt.Println(res25)

	res21, err := rdb.XReadGroup(ctx, &redis.XReadGroupArgs{
		Streams:  []string{"race:italy", ">"},
		Group:    "italy_riders",
		Consumer: "Alice",
		Count:    1,
	}).Result()

	if err != nil {
		panic(err)
	}

	// fmt.Println(res21)
	// >>> [{race:italy [{1692632639151-0 map[rider:Castilla] 0 0}]}]
```

```c#
        RedisValue groupRes = db.StreamAdd(
            "race:italy",
            [new("rider", "Castilla")]
        ); // 1712744323758-0

        groupRes = db.StreamAdd(
            "race:italy",
            [new("rider", "Royce")]
        ); // 1712744358384-0

        groupRes = db.StreamAdd(
            "race:italy",
            [new("rider", "Sam-Bodden")]
        ); // 1712744379676-0

        groupRes = db.StreamAdd(
            "race:italy",
            [new("rider", "Prickett")]
        ); // 1712744399401-0

        groupRes = db.StreamAdd(
            "race:italy",
            [new("rider", "Norem")]
        ); // 1712744413117-0

        StreamEntry[] res21 = db.StreamReadGroup("race:italy", "italy_riders", "Alice", ">", 1);

        foreach (StreamEntry entry in res21)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712744323758-0: [rider: Castilla]
```

```ruby
r.del('race:italy')
r.xgroup(:create, 'race:italy', 'italy_riders', '$', mkstream: true)
r.xadd('race:italy', {'rider' => 'Castilla'}, id: '1692632639151-0')
r.xadd('race:italy', {'rider' => 'Royce'}, id: '1692632647899-0')
r.xadd('race:italy', {'rider' => 'Sam-Bodden'}, id: '1692632662819-0')
r.xadd('race:italy', {'rider' => 'Prickett'}, id: '1692632670501-0')
r.xadd('race:italy', {'rider' => 'Norem'}, id: '1692632678249-0')

res20 = r.xreadgroup('italy_riders', 'Alice', ['race:italy'], ['>'], count: 1)
puts res20.inspect
# {"race:italy"=>[["1692632639151-0", {"rider"=>"Castilla"}]]}
```

```rust
        let italy_1: Option<String> = r
            .xadd("race:italy", "1692632639151-0", &[("rider", "Castilla")])
            .expect("italy1");
        let italy_1 = italy_1.expect("missing stream id");
        println!("{italy_1}"); // >>> 1692632639151-0
        let italy_2: Option<String> = r
            .xadd("race:italy", "1692632647899-0", &[("rider", "Royce")])
            .expect("italy2");
        let italy_2 = italy_2.expect("missing stream id");
        println!("{italy_2}"); // >>> 1692632647899-0
        let italy_3: Option<String> = r
            .xadd("race:italy", "1692632662819-0", &[("rider", "Sam-Bodden")])
            .expect("italy3");
        let italy_3 = italy_3.expect("missing stream id");
        println!("{italy_3}"); // >>> 1692632662819-0
        let italy_4: Option<String> = r
            .xadd("race:italy", "1692632670501-0", &[("rider", "Prickett")])
            .expect("italy4");
        let italy_4 = italy_4.expect("missing stream id");
        println!("{italy_4}"); // >>> 1692632670501-0
        let italy_5: Option<String> = r
            .xadd("race:italy", "1692632678249-0", &[("rider", "Norem")])
            .expect("italy5");
        let italy_5 = italy_5.expect("missing stream id");
        println!("{italy_5}"); // >>> 1692632678249-0

        let opts = StreamReadOptions::default().group("italy_riders", "Alice").count(1);
        if let Ok(res) = r.xread_options(&["race:italy"], &[">"], &opts) {
            let res: Option<StreamReadReply> = res;
            let view: Vec<_> = res
                .expect("xgroup read should return data")
                .keys
                .iter()
                .map(|stream| {
                    (
                        stream.key.clone(),
                        stream
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
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("race:italy", [("1692632639151-0", [("rider", "Castilla")])])]
        }
```

```rust
        let italy_1: Option<String> = r
            .xadd("race:italy", "1692632639151-0", &[("rider", "Castilla")])
            .await
            .expect("italy1");
        let italy_1 = italy_1.expect("missing stream id");
        println!("{italy_1}"); // >>> 1692632639151-0
        let italy_2: Option<String> = r
            .xadd("race:italy", "1692632647899-0", &[("rider", "Royce")])
            .await
            .expect("italy2");
        let italy_2 = italy_2.expect("missing stream id");
        println!("{italy_2}"); // >>> 1692632647899-0
        let italy_3: Option<String> = r
            .xadd("race:italy", "1692632662819-0", &[("rider", "Sam-Bodden")])
            .await
            .expect("italy3");
        let italy_3 = italy_3.expect("missing stream id");
        println!("{italy_3}"); // >>> 1692632662819-0
        let italy_4: Option<String> = r
            .xadd("race:italy", "1692632670501-0", &[("rider", "Prickett")])
            .await
            .expect("italy4");
        let italy_4 = italy_4.expect("missing stream id");
        println!("{italy_4}"); // >>> 1692632670501-0
        let italy_5: Option<String> = r
            .xadd("race:italy", "1692632678249-0", &[("rider", "Norem")])
            .await
            .expect("italy5");
        let italy_5 = italy_5.expect("missing stream id");
        println!("{italy_5}"); // >>> 1692632678249-0
        let opts = StreamReadOptions::default().group("italy_riders", "Alice").count(1);
        if let Ok(res) = r.xread_options(&["race:italy"], &[">"], &opts).await {
            let res: Option<StreamReadReply> = res;
            let view: Vec<_> = res
                .expect("xgroup read should return data")
                .keys
                .iter()
                .map(|stream| {
                    (
                        stream.key.clone(),
                        stream
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
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("race:italy", [("1692632639151-0", [("rider", "Castilla")])])]
        }
```

`XREADGROUP` replies are just like `XREAD` replies. Note however the `GROUP <group-name> <consumer-name>` provided above. It states that I want to read from the stream using the consumer group `mygroup` and I'm the consumer `Alice`. Every time a consumer performs an operation with a consumer group, it must specify its name, uniquely identifying this consumer inside the group.

There is another very important detail in the command line above, after the mandatory **STREAMS** option the ID requested for the key `race:italy` is the special ID `>`. This special ID is only valid in the context of consumer groups, and it means: **messages never delivered to other consumers so far**.

This is almost always what you want, however it is also possible to specify a real ID, such as `0` or any other valid ID, in this case, however, what happens is that we request from `XREADGROUP` to just provide us with the **history of pending messages**, and in such case, will never see new messages in the group. So basically `XREADGROUP` has the following behavior based on the ID we specify:

- If the ID is the special ID `>` then the command will return only new messages never delivered to other consumers so far, and as a side effect, will update the consumer group's *last ID*.
- If the ID is any other valid numerical ID, then the command will let us access our *history of pending messages*. That is, the set of messages that were delivered to this specified consumer (identified by the provided name), and never acknowledged so far with `XACK`.

We can test this behavior immediately specifying an ID of 0, without any **COUNT** option: we'll just see the only pending message, that is, the one about Castilla:

Access pending message history using XREADGROUP with a specific ID to retrieve unacknowledged messages

```plaintext
> XREADGROUP GROUP italy_riders Alice STREAMS race:italy 0
1) 1) "race:italy"
   2) 1) 1) "1692632639151-0"
         2) 1) "rider"
            2) "Castilla"
```

```python
res21 = r.xreadgroup(
    streams={"race:italy": 0},
    consumername="Alice",
    groupname="italy_riders",
    count=1,
)
print(res21)  # >>> [['race:italy', [('1692629925771-0', {'rider': 'Castilla'})]]]
```

```node
const res21 = await client.xReadGroup(
  'italy_riders',
  'Alice', {
    key: 'race:italy',
    id: '0'
  }, {
    COUNT: 1
  }
);
console.log(res21); // >>> [{ name: 'race:italy', messages: [{ id: '1692629925771-0', message: { rider: 'Castilla' } }] }]
```

```java
    List<Map.Entry<String, List<StreamEntry>>> res22 = jedis.xreadGroup("italy_riders","Alice", XReadGroupParams.xReadGroupParams().count(1),new HashMap<String,StreamEntryID>(){{put("race:italy",new StreamEntryID());}});
    System.out.println(res22); // >>> [race:italy=[1701766299006-0 {rider=Castilaa}]]
```

```go
	res22, err := rdb.XReadGroup(ctx, &redis.XReadGroupArgs{
		Streams:  []string{"race:italy", "0"},
		Group:    "italy_riders",
		Consumer: "Alice",
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res22)
	// >>> [{race:italy [{1692632639151-0 map[rider:Castilla] 0 0}]}]
```

```c#
        StreamEntry[] res22 = db.StreamReadGroup("race:italy", "italy_riders", "Alice", "0");

        foreach (StreamEntry entry in res22)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
            // >>> 1712744323758-0: [rider: Castilla]
        }
```

```ruby
res21 = r.xreadgroup('italy_riders', 'Alice', ['race:italy'], ['0'], count: 1)
puts res21.inspect
# {"race:italy"=>[["1692632639151-0", {"rider"=>"Castilla"}]]}
```

```rust
        let opts = StreamReadOptions::default().group("italy_riders", "Alice");
        if let Ok(res) = r.xread_options(&["race:italy"], &["0"], &opts) {
            let res: Option<StreamReadReply> = res;
            let view: Vec<_> = res
                .expect("xgroup history")
                .keys
                .iter()
                .map(|stream| {
                    (
                        stream.key.clone(),
                        stream
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
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("race:italy", [("1692632639151-0", [("rider", "Castilla")])])]
        }
```

```rust
        let opts = StreamReadOptions::default().group("italy_riders", "Alice");
        if let Ok(res) = r.xread_options(&["race:italy"], &["0"], &opts).await {
            let res: Option<StreamReadReply> = res;
            let view: Vec<_> = res
                .expect("xgroup history")
                .keys
                .iter()
                .map(|stream| {
                    (
                        stream.key.clone(),
                        stream
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
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("race:italy", [("1692632639151-0", [("rider", "Castilla")])])]
        }
```

However, if we acknowledge the message as processed, it will no longer be part of the pending messages history, so the system will no longer report anything:

Foundational: Acknowledge processed messages using XACK to mark them as handled by a consumer

```plaintext
> XACK race:italy italy_riders 1692632639151-0
(integer) 1
> XREADGROUP GROUP italy_riders Alice STREAMS race:italy 0
1) 1) "race:italy"
   2) (empty array)
```

```python
res22 = r.xack("race:italy", "italy_riders", "1692629925771-0")
print(res22)  # >>> 1

res23 = r.xreadgroup(
    streams={"race:italy": 0},
    consumername="Alice",
    groupname="italy_riders",
    count=1,
)
print(res23)  # >>> [['race:italy', []]]
```

```node
const res22 = await client.xAck('race:italy', 'italy_riders', '1692629925771-0')
console.log(res22); // >>> 1

const res23 = await client.xReadGroup(
  'italy_riders',
  'Alice', {
    key: 'race:italy',
    id: '0'
  }, {
    COUNT: 1
  }
);
console.log(res23); // >>> [{ name: 'race:italy', messages: [] }]
```

```java
    long res23 = jedis.xack("race:italy","italy_riders",id1);
    System.out.println(res23); // >>> 1

    List<Map.Entry<String, List<StreamEntry>>> res24 = jedis.xreadGroup("italy_riders","Alice", XReadGroupParams.xReadGroupParams().count(1),new HashMap<String,StreamEntryID>(){{put("race:italy",new StreamEntryID());}});
    System.out.println(res24); // >>> [race:italy=[]]
```

```go
	res23, err := rdb.XAck(ctx,
		"race:italy", "italy_riders", "1692632639151-0",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res23) // >>> 1

	res24, err := rdb.XReadGroup(ctx, &redis.XReadGroupArgs{
		Streams:  []string{"race:italy", "0"},
		Group:    "italy_riders",
		Consumer: "Alice",
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res24)
	// >>> [{race:italy []}]
```

```c#
        long res23 = db.StreamAcknowledge("race:italy", "italy_riders", "1712744323758-0");
        Console.WriteLine(res23);   // >>> 1

        StreamEntry[] res24 = db.StreamReadGroup("race:italy", "italy_riders", "Alice", "0");

        foreach (StreamEntry entry in res24)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> <empty array>
```

```ruby
res22 = r.xack('race:italy', 'italy_riders', '1692632639151-0')
puts res22 # 1

res23 = r.xreadgroup('italy_riders', 'Alice', ['race:italy'], ['0'])
puts res23.inspect
# {"race:italy"=>[]}
```

```rust
        if let Ok(res) = r.xack("race:italy", "italy_riders", &["1692632639151-0"]) {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        let opts = StreamReadOptions::default().group("italy_riders", "Alice");
        if let Ok(res) = r.xread_options(&["race:italy"], &["0"], &opts) {
            let res: Option<StreamReadReply> = res;
            let view: Vec<_> = res
                .expect("xgroup history")
                .keys
                .iter()
                .map(|stream| {
                    (
                        stream.key.clone(),
                        stream
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
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}"); // >>> [("race:italy", [])]
        }
```

```rust
        if let Ok(res) = r.xack("race:italy", "italy_riders", &["1692632639151-0"]).await {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }
        let opts = StreamReadOptions::default().group("italy_riders", "Alice");
        if let Ok(res) = r.xread_options(&["race:italy"], &["0"], &opts).await {
            let res: Option<StreamReadReply> = res;
            let view: Vec<_> = res
                .expect("xgroup history")
                .keys
                .iter()
                .map(|stream| {
                    (
                        stream.key.clone(),
                        stream
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
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}"); // >>> [("race:italy", [])]
        }
```

Don't worry if you yet don't know how `XACK` works, the idea is just that processed messages are no longer part of the history that we can access.

Now it's Bob's turn to read something:

Practical pattern: Demonstrate consumer group load balancing where different consumers receive different messages from the same stream

```plaintext
> XREADGROUP GROUP italy_riders Bob COUNT 2 STREAMS race:italy >
1) 1) "race:italy"
   2) 1) 1) "1692632647899-0"
         2) 1) "rider"
            2) "Royce"
      2) 1) "1692632662819-0"
         2) 1) "rider"
            2) "Sam-Bodden"
```

```python
res24 = r.xreadgroup(
    streams={"race:italy": ">"},
    consumername="Bob",
    groupname="italy_riders",
    count=2,
)
print(
    res24
)
# >>> [
#       ['race:italy', [
#           ('1692629925789-0',
#               {'rider': 'Royce'}
#           ),
#           ('1692629925790-0',
#               {'rider': 'Sam-Bodden'}
#           )
#       ]
#       ]
# ]
```

```node
const res24 = await client.xReadGroup(
  'italy_riders',
  'Bob', {
    key: 'race:italy',
    id: '>'
  }, {
    COUNT: 2
  }
);
console.log(res24); // >>> [{ name: 'race:italy', messages: [{ id: '1692629925789-0', message: { rider: 'Royce' } }, { id: '1692629925790-0', message: { rider: 'Sam-Bodden' } }] }]
```

```java
    List<Map.Entry<String, List<StreamEntry>>> res25 = jedis.xreadGroup("italy_riders","Bob", XReadGroupParams.xReadGroupParams().count(2),new HashMap<String,StreamEntryID>(){{put("race:italy",StreamEntryID.UNRECEIVED_ENTRY);}});
    System.out.println(res25); // >>> [race:italy=[1701767632261-1 {rider=Royce}, 1701767632262-0 {rider=Sam-Bodden}]]
```

```go
	res25, err := rdb.XReadGroup(ctx, &redis.XReadGroupArgs{
		Streams:  []string{"race:italy", ">"},
		Group:    "italy_riders",
		Consumer: "Bob",
		Count:    2,
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res25)
	// >>> [{race:italy [{1692632647899-0 map[rider:Royce] 0 0} {1692632662819-0 map[rider:Sam-Bodden] 0 0}]}]
```

```c#
        StreamEntry[] res25 = db.StreamReadGroup("race:italy", "italy_riders", "Bob", ">", 2);

        foreach (StreamEntry entry in res25)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712744358384-0: [rider: Royce]
        // >>> 1712744379676-0: [rider: Sam-Bodden]
```

```ruby
res24 = r.xreadgroup('italy_riders', 'Bob', ['race:italy'], ['>'], count: 2)
puts res24.inspect
# {"race:italy"=>[["1692632647899-0", {"rider"=>"Royce"}],
#                 ["1692632662819-0", {"rider"=>"Sam-Bodden"}]]}
```

```rust
        let opts = StreamReadOptions::default().group("italy_riders", "Bob").count(2);
        if let Ok(res) = r.xread_options(&["race:italy"], &[">"], &opts) {
            let res: Option<StreamReadReply> = res;
            let view: Vec<_> = res
                .expect("bob should receive data")
                .keys
                .iter()
                .map(|stream| {
                    (
                        stream.key.clone(),
                        stream
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
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("race:italy", [("1692632647899-0", [("rider", "Royce")]), ("1692632662819-0", [("rider", "Sam-Bodden")])])]
        }
```

```rust
        let opts = StreamReadOptions::default().group("italy_riders", "Bob").count(2);
        if let Ok(res) = r.xread_options(&["race:italy"], &[">"], &opts).await {
            let res: Option<StreamReadReply> = res;
            let view: Vec<_> = res
                .expect("bob should receive data")
                .keys
                .iter()
                .map(|stream| {
                    (
                        stream.key.clone(),
                        stream
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
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("race:italy", [("1692632647899-0", [("rider", "Royce")]), ("1692632662819-0", [("rider", "Sam-Bodden")])])]
        }
```

Bob asked for a maximum of two messages and is reading via the same group `mygroup`. So what happens is that Redis reports just *new* messages. As you can see the "Castilla" message is not delivered, since it was already delivered to Alice, so Bob gets Royce and Sam-Bodden and so forth.

This way Alice, Bob, and any other consumer in the group, are able to read different messages from the same stream, to read their history of yet to process messages, or to mark messages as processed. This allows creating different topologies and semantics for consuming messages from a stream.

There are a few things to keep in mind:

- Consumers are auto-created the first time they are mentioned, no need for explicit creation.
- Even with `XREADGROUP` you can read from multiple keys at the same time, however for this to work, you need to create a consumer group with the same name in every stream. This is not a common need, but it is worth mentioning that the feature is technically available.
- `XREADGROUP` is a *write command* because even if it reads from the stream, the consumer group is modified as a side effect of reading, so it can only be called on master instances.

An example of a consumer implementation, using consumer groups, written in the Ruby language could be the following. The Ruby code is aimed to be readable by virtually any experienced programmer, even if they do not know Ruby:

```ruby
require 'redis'

if ARGV.length == 0
    puts "Please specify a consumer name"
    exit 1
end

ConsumerName = ARGV[0]
GroupName = "mygroup"
r = Redis.new

def process_message(id,msg)
    puts "[#{ConsumerName}] #{id} = #{msg.inspect}"
end

$lastid = '0-0'

puts "Consumer #{ConsumerName} starting..."
check_backlog = true
while true
    # Pick the ID based on the iteration: the first time we want to
    # read our pending messages, in case we crashed and are recovering.
    # Once we consumed our history, we can start getting new messages.
    if check_backlog
        myid = $lastid
    else
        myid = '>'
    end

    items = r.xreadgroup('GROUP',GroupName,ConsumerName,'BLOCK','2000','COUNT','10','STREAMS',:my_stream_key,myid)

    if items == nil
        puts "Timeout!"
        next
    end

    # If we receive an empty reply, it means we were consuming our history
    # and that the history is now empty. Let's start to consume new messages.
    check_backlog = false if items[0][1].length == 0

    items[0][1].each{|i|
        id,fields = i

        # Process the message
        process_message(id,fields)

        # Acknowledge the message as processed
        r.xack(:my_stream_key,GroupName,id)

        $lastid = id
    }
end
```

As you can see the idea here is to start by consuming the history, that is, our list of pending messages. This is useful because the consumer may have crashed before, so in the event of a restart we want to re-read messages that were delivered to us without getting acknowledged. Note that we might process a message multiple times or one time (at least in the case of consumer failures, but there are also the limits of Redis persistence and replication involved, see the specific section about this topic).

Once the history was consumed, and we get an empty list of messages, we can switch to using the `>` special ID in order to consume new messages.
