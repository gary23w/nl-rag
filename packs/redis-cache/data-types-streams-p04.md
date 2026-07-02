---
title: "Redis Streams (part 4/5)"
source: https://redis.io/docs/latest/develop/data-types/streams/
domain: redis-cache
license: CC-BY-SA-4.0
tags: redis, in-memory data store, key-value cache, in-memory database
fetched: 2026-07-02
part: 4/5
---

## Recovering from permanent failures

The example above allows us to write consumers that participate in the same consumer group, each taking a subset of messages to process, and when recovering from failures re-reading the pending messages that were delivered just to them. However in the real world consumers may permanently fail and never recover. What happens to the pending messages of the consumer that never recovers after stopping for any reason?

Redis consumer groups offer a feature that is used in these situations in order to *claim* the pending messages of a given consumer so that such messages will change ownership and will be re-assigned to a different consumer. The feature is very explicit. A consumer has to inspect the list of pending messages, and will have to claim specific messages using a special command, otherwise the server will leave the messages pending forever and assigned to the old consumer. In this way different applications can choose if to use such a feature or not, and exactly how to use it.

The first step of this process is just a command that provides observability of pending entries in the consumer group and is called `XPENDING`. This is a read-only command which is always safe to call and will not change ownership of any message. In its simplest form, the command is called with two arguments, which are the name of the stream and the name of the consumer group.

View pending message summary for a consumer group using XPENDING to monitor unacknowledged messages

```plaintext
> XPENDING race:italy italy_riders
1) (integer) 2
2) "1692632647899-0"
3) "1692632662819-0"
4) 1) 1) "Bob"
      2) "2"
```

```python
res25 = r.xpending("race:italy", "italy_riders")
print(
    res25
)
# >>> {
#       'pending': 2, 'min': '1692629925789-0', 'max': '1692629925790-0',
#       'consumers': [{'name': 'Bob', 'pending': 2}]
# }
```

```node
const res25 = await client.xPending('race:italy', 'italy_riders');
console.log(res25); // >>> {'pending': 2, 'firstId': '1692629925789-0', 'lastId': '1692629925790-0', 'consumers': [{'name': 'Bob', 'deliveriesCounter': 2}]}
```

```java
    StreamPendingSummary res26 = jedis.xpending("race:italy","italy_riders");
    System.out.println(res26.getConsumerMessageCount()); // >>> {Bob=2}
```

```go
	res26, err := rdb.XPending(ctx, "race:italy", "italy_riders").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res26)
	// >>> &{2 1692632647899-0 1692632662819-0 map[Bob:2]}
```

```c#
        StreamPendingInfo res26 = db.StreamPending("race:italy", "italy_riders");
        Console.WriteLine($"pending: {res26.PendingMessageCount}, min: {res26.LowestPendingMessageId}, max: {res26.HighestPendingMessageId}, consumers:[{string.Join(", ", res26.Consumers.Select(c => $"{c.Name}: {c.PendingMessageCount}"))}]");
        // >>> pending: 2, min: 1712747506906-0, max: 1712747506907-0, consumers:[name: Bob, pending:2]
```

```ruby
res25 = r.xpending('race:italy', 'italy_riders')
puts res25.inspect
# {"size"=>2, "min_entry_id"=>"1692632647899-0", "max_entry_id"=>"1692632662819-0", "consumers"=>{"Bob"=>"2"}}
```

```rust
        if let Ok(res) = r.xpending("race:italy", "italy_riders") {
            let res: StreamPendingReply = res;
            let view = match res {
                StreamPendingReply::Empty => None,
                StreamPendingReply::Data(data) => Some((
                    data.count,
                    data.start_id.clone(),
                    data.end_id.clone(),
                    data.consumers
                        .iter()
                        .map(|consumer| (consumer.name.clone(), consumer.pending))
                        .collect::<Vec<_>>(),
                )),
            }
            .expect("pending summary");
            println!("{view:?}");
            // >>> (2, "1692632647899-0", "1692632662819-0", [("Bob", 2)])
        }
```

```rust
        if let Ok(res) = r.xpending("race:italy", "italy_riders").await {
            let res: StreamPendingReply = res;
            let view = match res {
                StreamPendingReply::Empty => None,
                StreamPendingReply::Data(data) => Some((
                    data.count,
                    data.start_id.clone(),
                    data.end_id.clone(),
                    data.consumers
                        .iter()
                        .map(|consumer| (consumer.name.clone(), consumer.pending))
                        .collect::<Vec<_>>(),
                )),
            }
            .expect("pending summary");
            println!("{view:?}");
            // >>> (2, "1692632647899-0", "1692632662819-0", [("Bob", 2)])
        }
```

When called in this way, the command outputs the total number of pending messages in the consumer group (two in this case), the lower and higher message ID among the pending messages, and finally a list of consumers and the number of pending messages they have. We have only Bob with two pending messages because the single message that Alice requested was acknowledged using `XACK`.

We can ask for more information by giving more arguments to `XPENDING`, because the full command signature is the following:

```
XPENDING <key> <groupname> [[IDLE <min-idle-time>] <start-id> <end-id> <count> [<consumer-name>]]
```

By providing a start and end ID (that can be just `-` and `+` as in `XRANGE`) and a count to control the amount of information returned by the command, we are able to know more about the pending messages. The optional final argument, the consumer name, is used if we want to limit the output to just messages pending for a given consumer, but won't use this feature in the following example.

Get detailed pending message information including idle time and delivery count using XPENDING with range

```plaintext
> XPENDING race:italy italy_riders - + 10
1) 1) "1692632647899-0"
   2) "Bob"
   3) (integer) 74642
   4) (integer) 1
2) 1) "1692632662819-0"
   2) "Bob"
   3) (integer) 74642
   4) (integer) 1
```

```python
res26 = r.xpending_range("race:italy", "italy_riders", "-", "+", 10)
print(
    res26
)
# >>> [
#       {
#           'message_id': '1692629925789-0', 'consumer': 'Bob',
#           'time_since_delivered': 31084, 'times_delivered': 1
#       },
#       {
#           'message_id': '1692629925790-0', 'consumer': 'Bob',
#           'time_since_delivered': 31084, 'times_delivered': 1
#       }
# ]
```

```node
const res26 = await client.xPendingRange('race:italy', 'italy_riders', '-', '+', 10);
console.log(res26); // >>> [{'id': '1692629925789-0', 'consumer': 'Bob', 'millisecondsSinceLastDelivery': 31084, 'deliveriesCounter:': 1}, {'id': '1692629925790-0', 'consumer': 'Bob', 'millisecondsSinceLastDelivery': 31084, 'deliveriesCounter': 1}]
```

```java
    List<StreamPendingEntry> res27 = jedis.xpending("race:italy","italy_riders",XPendingParams.xPendingParams().start(StreamEntryID.MINIMUM_ID).end(StreamEntryID.MAXIMUM_ID).count(10));
    System.out.println(res27); // >>> [1701768567412-1 Bob idle:0 times:1, 1701768567412-2 Bob idle:0 times:1]
```

```go
	res27, err := rdb.XPendingExt(ctx, &redis.XPendingExtArgs{
		Stream: "race:italy",
		Group:  "italy_riders",
		Start:  "-",
		End:    "+",
		Count:  10,
	}).Result()

	if err != nil {
		panic(err)
	}

	// fmt.Println(res27)
	// >>> [{1692632647899-0 Bob 0s 1} {1692632662819-0 Bob 0s 1}]
```

```c#
        StreamPendingMessageInfo[] res27 = db.StreamPendingMessages(
            "race:italy", "italy_riders", 10, "", "-", "+"
        );

        foreach (StreamPendingMessageInfo info in res27)
        {
            Console.WriteLine($"message_id: {info.MessageId}, consumer: {info.ConsumerName}, time_since_delivered: {info.IdleTimeInMilliseconds}, times_delivered: {info.DeliveryCount}");
        }
        // >>> message_id: min: 1712747506906-0, consumer: Bob, time_since_delivered: 31084, times_delivered: 1
        // >>> message_id: min: 1712747506907-0, consumer: Bob, time_since_delivered: 31084, times_delivered: 1
```

```ruby
res26 = r.xpending('race:italy', 'italy_riders', '-', '+', 10)
puts res26.inspect
```

```rust
        if let Ok(res) = r.xpending_count("race:italy", "italy_riders", "-", "+", 10) {
            let res: StreamPendingCountReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        entry.consumer.clone(),
                        entry.last_delivered_ms,
                        entry.times_delivered,
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632647899-0", "Bob", 5, 1), ("1692632662819-0", "Bob", 5, 1)]
        }
```

```rust
        if let Ok(res) = r.xpending_count("race:italy", "italy_riders", "-", "+", 10).await {
            let res: StreamPendingCountReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        entry.consumer.clone(),
                        entry.last_delivered_ms,
                        entry.times_delivered,
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632647899-0", "Bob", 5, 1), ("1692632662819-0", "Bob", 5, 1)]
        }
```

Now we have the details for each message: the ID, the consumer name, the *idle time* in milliseconds, which is how many milliseconds have passed since the last time the message was delivered to some consumer, and finally the number of times that a given message was delivered. We have two messages from Bob, and they are idle for 60000+ milliseconds, about a minute.

Note that nobody prevents us from checking what the first message content was by just using `XRANGE`.

Retrieve the content of pending messages using XRANGE to inspect what needs to be processed

```plaintext
> XRANGE race:italy 1692632647899-0 1692632647899-0
1) 1) "1692632647899-0"
   2) 1) "rider"
      2) "Royce"
```

```python
res27 = r.xrange("race:italy", "1692629925789-0", "1692629925789-0")
print(res27)  # >>> [('1692629925789-0', {'rider': 'Royce'})]
```

```node
const res27 = await client.xRange('race:italy', '1692629925789-0', '1692629925789-0');
console.log(res27); // >>> [{ id: '1692629925789-0', message: { rider: 'Royce' } }]
```

```java
    List<StreamEntry> res28 = jedis.xrange("race:italy",id2.toString(),id2.toString());
    System.out.println(res28); // >>> [1701768744819-1 {rider=Royce}]
```

```go
	res28, err := rdb.XRange(ctx, "race:italy",
		"1692632647899-0", "1692632647899-0",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res28) // >>> [{1692632647899-0 map[rider:Royce] 0 0}]
```

```c#
        StreamEntry[] res28 = db.StreamRange("race:italy", "1712744358384-0", "1712744358384-0");

        foreach (StreamEntry entry in res28)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712744358384-0: [rider: Royce]
```

```ruby
res27 = r.xrange('race:italy', '1692632647899-0', '1692632647899-0')
puts res27.inspect
# [["1692632647899-0", {"rider"=>"Royce"}]]
```

```rust
        if let Ok(res) = r.xrange("race:italy", "1692632647899-0", "1692632647899-0") {
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
            println!("{view:?}"); // >>> [("1692632647899-0", [("rider", "Royce")])]
        }
```

```rust
        if let Ok(res) = r.xrange("race:italy", "1692632647899-0", "1692632647899-0").await {
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
            println!("{view:?}"); // >>> [("1692632647899-0", [("rider", "Royce")])]
        }
```

We have just to repeat the same ID twice in the arguments. Now that we have some ideas, Alice may decide that after 1 minute of not processing messages, Bob will probably not recover quickly, and it's time to *claim* such messages and resume the processing in place of Bob. To do so, we use the `XCLAIM` command.

This command is very complex and full of options in its full form, since it is used for replication of consumer groups changes, but we'll use just the arguments that we need normally. In this case it is as simple as:

```
XCLAIM <key> <group> <consumer> <min-idle-time> <ID-1> <ID-2> ... <ID-N>
```

Basically we say, for this specific key and group, I want that the message IDs specified will change ownership, and will be assigned to the specified consumer name `<consumer>`. However, we also provide a minimum idle time, so that the operation will only work if the idle time of the mentioned messages is greater than the specified idle time. This is useful because maybe two clients are retrying to claim a message at the same time:

```
Client 1: XCLAIM race:italy italy_riders Alice 60000 1692632647899-0
Client 2: XCLAIM race:italy italy_riders Lora 60000 1692632647899-0
```

However, as a side effect, claiming a message will reset its idle time and will increment its number of deliveries counter, so the second client will fail claiming it. In this way we avoid trivial re-processing of messages (even if in the general case you cannot obtain exactly once processing).

This is the result of the command execution:

Claim pending messages from another consumer using XCLAIM when a consumer fails to process messages

```plaintext
> XCLAIM race:italy italy_riders Alice 60000 1692632647899-0
1) 1) "1692632647899-0"
   2) 1) "rider"
      2) "Royce"
```

```python
res28 = r.xclaim("race:italy", "italy_riders", "Alice", 60000, ["1692629925789-0"])
print(res28)  # >>> [('1692629925789-0', {'rider': 'Royce'})]
```

```node
const res28 = await client.xClaim(
  'race:italy', 'italy_riders', 'Alice', 60000, ['1692629925789-0']
);
console.log(res28); // >>> [{ id: '1692629925789-0', message: { rider: 'Royce' } }]
```

```java
    List<StreamEntry> res29 = jedis.xclaim("race:italy","italy_riders","Alice", 0L, XClaimParams.xClaimParams().time(60000),id2);
    System.out.println(res29); // >>> [1701769004195-1 {rider=Royce}]
```

```go
	res29, err := rdb.XClaim(ctx, &redis.XClaimArgs{
		Stream:   "race:italy",
		Group:    "italy_riders",
		Consumer: "Alice",
		MinIdle:  0,
		Messages: []string{"1692632647899-0"},
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res29)
```

```c#
        StreamEntry[] res29 = db.StreamClaim(
            "race:italy", "italy_riders", "Alice", 60000, [1712744358384 - 0]
        );

        foreach (StreamEntry entry in res29)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712744358384-0: [rider: Royce]
```

```ruby
res28 = r.xclaim('race:italy', 'italy_riders', 'Alice', 0, '1692632647899-0')
puts res28.inspect
# [["1692632647899-0", {"rider"=>"Royce"}]]
```

```rust
        if let Ok(res) = r.xclaim("race:italy", "italy_riders", "Alice", 1, &["1692632647899-0"]) {
            let res: redis::streams::StreamClaimReply = res;
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
            println!("{view:?}"); // >>> [("1692632647899-0", [("rider", "Royce")])]
        }
```

```rust
        if let Ok(res) = r
            .xclaim("race:italy", "italy_riders", "Alice", 1, &["1692632647899-0"])
            .await
        {
            let res: redis::streams::StreamClaimReply = res;
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
            println!("{view:?}"); // >>> [("1692632647899-0", [("rider", "Royce")])]
        }
```

The message was successfully claimed by Alice, who can now process the message and acknowledge it, and move things forward even if the original consumer is not recovering.

It is clear from the example above that as a side effect of successfully claiming a given message, the `XCLAIM` command also returns it. However this is not mandatory. The **JUSTID** option can be used in order to return just the IDs of the message successfully claimed. This is useful if you want to reduce the bandwidth used between the client and the server (and also the performance of the command) and you are not interested in the message because your consumer is implemented in a way that it will rescan the history of pending messages from time to time.

Claiming may also be implemented by a separate process: one that just checks the list of pending messages, and assigns idle messages to consumers that appear to be active. Active consumers can be obtained using one of the observability features of Redis streams. This is the topic of the next section.


## Automatic claiming

The `XAUTOCLAIM` command, added in Redis 6.2, implements the claiming process that we've described above. `XPENDING` and `XCLAIM` provide the basic building blocks for different types of recovery mechanisms. This command optimizes the generic process by having Redis manage it and offers a simple solution for most recovery needs.

`XAUTOCLAIM` identifies idle pending messages and transfers ownership of them to a consumer. The command's signature looks like this:

```
XAUTOCLAIM <key> <group> <consumer> <min-idle-time> <start> [COUNT count] [JUSTID]
```

So, in the example above, I could have used automatic claiming to claim a single message like this:

Practical pattern: Automatically claim idle pending messages using XAUTOCLAIM for simplified consumer failure recovery

```plaintext
> XAUTOCLAIM race:italy italy_riders Alice 60000 0-0 COUNT 1
1) "0-0"
2) 1) 1) "1692632662819-0"
      2) 1) "rider"
         2) "Sam-Bodden"
```

```python
res29 = r.xautoclaim("race:italy", "italy_riders", "Alice", 1, "0-0", 1)
print(res29)  # >>> ['1692629925790-0', [('1692629925789-0', {'rider': 'Royce'})]]
```

```node
const res29 = await client.xAutoClaim('race:italy', 'italy_riders', 'Alice', 1, '0-0', {
  COUNT: 1
});
console.log(res29); // >>> { nextId: '1692629925790-0', messages: [{ id: '1692629925789-0', message: { rider: 'Royce' } }], deletedMessages: [] }
```

```java
    Map.Entry<StreamEntryID, List<StreamEntry>> res30 = jedis.xautoclaim("race:italy","italy_riders","Alice",1L,new StreamEntryID("0-0"),XAutoClaimParams.xAutoClaimParams().count(1));
    System.out.println(res30); // >>> [1701769266831-2=[1701769266831-1 {rider=Royce}]
```

```go
	res30, res30a, err := rdb.XAutoClaim(ctx, &redis.XAutoClaimArgs{
		Stream:   "race:italy",
		Group:    "italy_riders",
		Consumer: "Alice",
		Start:    "0-0",
		Count:    1,
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res30)  // >>> [{1692632647899-0 map[rider:Royce] 0 0}]
	fmt.Println(res30a) // >>> 1692632662819-0
```

```c#
        StreamAutoClaimResult res30 = db.StreamAutoClaim(
            "race:italy", "italy_riders", "Alice", 1, "0-0", 1
        );

        Console.WriteLine($"{res30.NextStartId}, ({string.Join(", ", res30.ClaimedEntries.Select(entry => $"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]"))})");
        // >>> 1712744379676-0, (1712744358384-0: [rider: Royce])
```

```ruby
res29 = r.xautoclaim('race:italy', 'italy_riders', 'Alice', 0, '0-0', count: 1)
puts res29.inspect
# {"next"=>"1692632662819-0", "entries"=>[["1692632647899-0", {"rider"=>"Royce"}]]}
```

```rust
        let opts = StreamAutoClaimOptions::default().count(1);
        if let Ok(res) = r.xautoclaim_options("race:italy", "italy_riders", "Alice", 1, "0-0", opts) {
            let res: redis::streams::StreamAutoClaimReply = res;
            let claimed: Vec<_> = res
                .claimed
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
            println!("{:?}", (res.next_stream_id.clone(), &claimed));
            // >>> ("1692632662819-0", [("1692632647899-0", [("rider", "Royce")])])
        }
```

```rust
        let opts = StreamAutoClaimOptions::default().count(1);
        if let Ok(res) = r
            .xautoclaim_options("race:italy", "italy_riders", "Alice", 1, "0-0", opts)
            .await
        {
            let res: redis::streams::StreamAutoClaimReply = res;
            let claimed: Vec<_> = res
                .claimed
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
            println!("{:?}", (res.next_stream_id.clone(), &claimed));
            // >>> ("1692632662819-0", [("1692632647899-0", [("rider", "Royce")])])
        }
```

Like `XCLAIM`, the command replies with an array of the claimed messages, but it also returns a stream ID that allows iterating the pending entries. The stream ID is a cursor, and I can use it in my next call to continue in claiming idle pending messages:

Continue automatic claiming using the cursor returned by XAUTOCLAIM to iterate through pending messages

```plaintext
> XAUTOCLAIM race:italy italy_riders Lora 60000 (1692632662819-0 COUNT 1
1) "1692632662819-0"
2) 1) 1) "1692632647899-0"
      2) 1) "rider"
         2) "Royce"
```

```python
res30 = r.xautoclaim("race:italy", "italy_riders", "Alice", 1, "(1692629925789-0", 1)
print(res30)  # >>> ['0-0', [('1692629925790-0', {'rider': 'Sam-Bodden'})]]
```

```node
const res30 = await client.xAutoClaim(
  'race:italy', 'italy_riders', 'Alice', 1, '(1692629925789-0',
  {
    COUNT: 1
  }
);
console.log(res30); // >>> { nextId: '0-0', messages: [{ id: '1692629925790-0', message: { rider: 'Sam-Bodden' } }], deletedMessages: [] }
```

```java
    Map.Entry<StreamEntryID, List<StreamEntry>> res31 = jedis.xautoclaim("race:italy","italy_riders","Alice",1L,new StreamEntryID(id2.toString()),XAutoClaimParams.xAutoClaimParams().count(1));
    System.out.println(res31); // >>> [0-0=[1701769605847-2 {rider=Sam-Bodden}]
```

```go
	res31, res31a, err := rdb.XAutoClaim(ctx, &redis.XAutoClaimArgs{
		Stream:   "race:italy",
		Group:    "italy_riders",
		Consumer: "Lora",
		Start:    "(1692632662819-0",
		Count:    1,
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res31)  // >>> []
	fmt.Println(res31a) // >>> 0-0
```

```c#
        StreamAutoClaimResult res31 = db.StreamAutoClaim(
            "race:italy", "italy_riders", "Alice", 1, "(1712744358384-0", 1
        );

        Console.WriteLine($"{res31.NextStartId}, ({string.Join(", ", res31.ClaimedEntries.Select(entry => $"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]"))})");
        // >>> 0-0, (1712744379676-0: [rider: Sam-Bodden])
```

```ruby
res30 = r.xautoclaim('race:italy', 'italy_riders', 'Lora', 0, res29['next'], count: 1)
puts res30.inspect
# {"next"=>"0-0", "entries"=>[["1692632662819-0", {"rider"=>"Sam-Bodden"}]]}
```

```rust
        let next_opts = StreamAutoClaimOptions::default().count(1);
        if let Ok(res) = r.xautoclaim_options(
            "race:italy",
            "italy_riders",
            "Lora",
            1,
            "(1692632647899-0",
            next_opts,
        ) {
            let res: redis::streams::StreamAutoClaimReply = res;
            let claimed: Vec<_> = res
                .claimed
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
            println!("{:?}", (res.next_stream_id.clone(), &claimed));
            // >>> ("0-0", [("1692632662819-0", [("rider", "Sam-Bodden")])])
        }
```

```rust
        let next_opts = StreamAutoClaimOptions::default().count(1);
        if let Ok(res) = r
            .xautoclaim_options(
                "race:italy",
                "italy_riders",
                "Lora",
                1,
                "(1692632647899-0",
                next_opts,
            )
            .await
        {
            let res: redis::streams::StreamAutoClaimReply = res;
            let claimed: Vec<_> = res
                .claimed
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
            println!("{:?}", (res.next_stream_id.clone(), &claimed));
            // >>> ("0-0", [("1692632662819-0", [("rider", "Sam-Bodden")])])
        }
```

When `XAUTOCLAIM` returns the "0-0" stream ID as a cursor, that means that it reached the end of the consumer group pending entries list. That doesn't mean that there are no new idle pending messages, so the process continues by calling `XAUTOCLAIM` from the beginning of the stream.


## Claiming and the delivery counter

The counter that you observe in the `XPENDING` output is the number of deliveries of each message. The counter is incremented in two ways: when a message is successfully claimed via `XCLAIM` or when an `XREADGROUP` call is used in order to access the history of pending messages.

When there are failures, it is normal that messages will be delivered multiple times, but eventually they usually get processed and acknowledged. However there might be a problem processing some specific message, because it is corrupted or crafted in a way that triggers a bug in the processing code. In such a case what happens is that consumers will continuously fail to process this particular message. Because we have the counter of the delivery attempts, we can use that counter to detect messages that for some reason are not processable. So once the deliveries counter reaches a given large number that you chose, it is probably wiser to put such messages in another stream and send a notification to the system administrator. This is basically the way that Redis Streams implements the *dead letter* concept.


## Releasing messages back to the group: XNACK

Starting with Redis 8.8, the `XNACK` command provides a way for consumers to explicitly release pending messages back to the group without acknowledging them. This is the opposite of claiming - instead of taking ownership of messages from other consumers, a consumer can release its own messages back to the group for immediate re-delivery.

This capability addresses several common scenarios:

1. **Graceful shutdown**: When a consumer is shutting down, it can release all its pending messages so other consumers can pick them up immediately without waiting for idle timeouts.
2. **Consumer-side failures**: When a consumer encounters consumer-side issues (like network connectivity problems or resource constraints), it can release messages it cannot process rather than letting them sit idle.
3. **Resource management**: A consumer under resource pressure can release complex or large messages that it cannot handle, allowing other consumers with more resources to process them.
4. **Poison message handling**: A consumer can mark messages as permanently failed when it detects invalid or malicious content.

The command provides three modes that control how the delivery counter is adjusted:

- **SILENT**: Decrements the delivery counter, essentially "undoing" the delivery. Use this for graceful shutdowns or when the failure is unrelated to the message content.
- **FAIL**: Keeps the delivery counter unchanged. Use this when the current consumer cannot handle the message but others might be able to.
- **FATAL**: Sets the delivery counter to maximum value, marking the message as permanently failed for dead letter processing.

Released messages are placed in a special "NACK zone" at the head of the consumer group's PEL, ensuring they are prioritized for re-delivery over other idle pending messages. This makes recovery much faster than traditional claiming mechanisms that rely on idle timeouts.

```
> XNACK mystream mygroup FAIL IDS 1 1526569498055-0
(integer) 1
```

After NACKing, the message appears with an empty consumer in `XPENDING` output and becomes immediately available for claiming or consumption via `XREADGROUP` with the CLAIM option.


## Working with multiple consumer groups

Redis Streams can be associated with multiple consumer groups, where each entry is delivered to all the stream's consumer groups. Within each consumer group, consumers handle a portion of the entries collaboratively. This design enables different applications or services to process the same stream data independently.

Traditionally, when a consumer processesed a message, it acknowledged it using the `XACK` command, which removed the entry reference from the Pending Entries List (PEL) of that specific consumer group. However, the entry remained in the stream and in the PELs of other consumer groups until they also acknowledge it. Applications needed to implement complex logic to delete entries from the stream only after all consumer groups had acknowledged them. This coordination was challenging to implement correctly and efficiently.

### Enhanced deletion control in Redis 8.2

Starting with Redis 8.2, several commands provide enhanced control over how entries are handled with respect to multiple consumer groups:

- `XADD` with trimming options now supports `KEEPREF`, `DELREF`, and `ACKED` modes
- `XTRIM` supports the same reference handling options
- `XDELEX` provides fine-grained deletion control
- `XACKDEL` combines acknowledgment and deletion atomically

These options control how consumer group references are handled:

- **KEEPREF** (default): Preserves existing references to entries in all consumer groups' PELs, maintaining backward compatibility
- **DELREF**: Removes all references to entries from all consumer groups' PELs, effectively cleaning up all traces of the messages
- **ACKED**: Only processes entries that have been acknowledged by all consumer groups

The `ACKED` option is particularly useful as it automates the complex logic of coordinating deletion across multiple consumer groups, ensuring entries are only removed when all groups have finished processing them.


## Streams observability

Messaging systems that lack observability are very hard to work with. Not knowing who is consuming messages, what messages are pending, the set of consumer groups active in a given stream, makes everything opaque. For this reason, Redis Streams and consumer groups have different ways to observe what is happening. We already covered `XPENDING`, which allows us to inspect the list of messages that are under processing at a given moment, together with their idle time and number of deliveries.

However we may want to do more than that, and the `XINFO` command is an observability interface that can be used with sub-commands in order to get information about streams or consumer groups.

This command uses subcommands in order to show different information about the status of the stream and its consumer groups. For instance **XINFO STREAM** reports information about the stream itself.

Get detailed stream information including length, encoding, and consumer groups using XINFO STREAM

```plaintext
> XINFO STREAM race:italy
 1) "length"
 2) (integer) 5
 3) "radix-tree-keys"
 4) (integer) 1
 5) "radix-tree-nodes"
 6) (integer) 2
 7) "last-generated-id"
 8) "1692632678249-0"
 9) "groups"
10) (integer) 1
11) "first-entry"
12) 1) "1692632639151-0"
    2) 1) "rider"
       2) "Castilla"
13) "last-entry"
14) 1) "1692632678249-0"
    2) 1) "rider"
       2) "Norem"
```

```python
res31 = r.xinfo_stream("race:italy")
print(
    res31
)
# >>> {
#       'length': 5, 'radix-tree-keys': 1, 'radix-tree-nodes': 2,
#       'last-generated-id': '1692629926436-0', 'groups': 1,
#       'first-entry': ('1692629925771-0', {'rider': 'Castilla'}),
#       'last-entry': ('1692629926436-0', {'rider': 'Norem'})
# }
```

```node
const res31 = await client.xInfoStream('race:italy');
console.log(res31); // >>> { length: 5, 'radix-tree-keys': 1, 'radix-tree-nodes': 2, 'last-generated-id': '1692629926436-0', 'max-deleted-entry-id': '0-0', 'entries-added': 5, 'recorded-first-entry-id': '1692629925771-0', groups: 1, 'first-entry': { id: '1692629925771-0', message: { rider: 'Castilla' } }, 'last-entry': { id: '1692629926436-0', message: { rider: 'Norem' } } }
```

```java
    StreamInfo res32 = jedis.xinfoStream("race:italy");
    System.out.println(
      res32.getStreamInfo()
    ); // >>> {radix-tree-keys=1, radix-tree-nodes=2, entries-added=5, length=5, groups=1, max-deleted-entry-id=0-0, first-entry=1701769637612-0 {rider=Castilaa}, last-generated-id=1701769637612-4, last-entry=1701769637612-4 {rider=Norem}, recorded-first-entry-id=1701769637612-0}
```

```go
	res33, err := rdb.XInfoStream(ctx, "race:italy").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res33.Length)
	// >>> 5
	fmt.Println(res33.FirstEntry)
	// >>> {1692632639151-0 map[rider:Castilla] 0 0}
```

```c#
        StreamInfo res32 = db.StreamInfo("race:italy");
        Console.WriteLine($"length: {res32.Length}, radix-tree-keys: {res32.RadixTreeKeys}, radix-tree-nodes: {res32.RadixTreeNodes}, last-generated-id: {res32.LastGeneratedId}, first-entry: {$"{res32.FirstEntry.Id}: [{string.Join(", ", res32.FirstEntry.Values.Select(b => $"{b.Name}: {b.Value}"))}]"}, last-entry: {$"{res32.LastEntry.Id}: [{string.Join(", ", res32.LastEntry.Values.Select(b => $"{b.Name}: {b.Value}"))}]"}");
        // >>> length: 5, radix-tree-keys: 1, radix-tree-nodes: 2, last-generated-id: 1712756762686-1, first-entry: 1712756762685-0: [rider: Castilla], last-entry: 1712756762686-1: [rider: Norem]
```

```ruby
res31 = r.xinfo(:stream, 'race:italy')
puts res31.inspect
```

```rust
        if let Ok(res) = r.xinfo_stream("race:italy") {
            let res: StreamInfoStreamReply = res;
            let view = (
                res.length,
                res.radix_tree_keys,
                res.groups,
                res.last_generated_id.clone(),
                res.first_entry.id.clone(),
                res.last_entry.id.clone(),
            );
            println!("{view:?}");
            // >>> (5, 1, 1, "1692632678249-0", "1692632639151-0", "1692632678249-0")
        }
```

```rust
        if let Ok(res) = r.xinfo_stream("race:italy").await {
            let res: StreamInfoStreamReply = res;
            let view = (
                res.length,
                res.radix_tree_keys,
                res.groups,
                res.last_generated_id.clone(),
                res.first_entry.id.clone(),
                res.last_entry.id.clone(),
            );
            println!("{view:?}");
            // >>> (5, 1, 1, "1692632678249-0", "1692632639151-0", "1692632678249-0")
        }
```

The output shows information about how the stream is encoded internally, and also shows the first and last message in the stream. Another piece of information available is the number of consumer groups associated with this stream. We can dig further asking for more information about the consumer groups.

List all consumer groups for a stream using XINFO GROUPS to see group status and pending message counts

```plaintext
> XINFO GROUPS race:italy
1) 1) "name"
   2) "italy_riders"
   3) "consumers"
   4) (integer) 3
   5) "pending"
   6) (integer) 2
   7) "last-delivered-id"
   8) "1692632662819-0"
```

```python
res32 = r.xinfo_groups("race:italy")
print(
    res32
)
# >>> [
#       {
#           'name': 'italy_riders', 'consumers': 2, 'pending': 2,
#           'last-delivered-id': '1692629925790-0'
#       }
# ]
```

```node
const res32 = await client.xInfoGroups('race:italy');
console.log(res32); // >>> [{ name: 'italy_riders', consumers: 2, pending: 3, 'last-delivered-id': '1692629925790-0', 'entries-read': 3, lag: 2 }]
```

```java
    List<StreamGroupInfo> res33 = jedis.xinfoGroups("race:italy");
    for (StreamGroupInfo a : res33){
      System.out.println(
        a.getGroupInfo()
      ); // >>> {last-delivered-id=1701770253659-0, lag=2, pending=2, name=italy_riders, consumers=2, entries-read=3}
    }
```

```go
	res34, err := rdb.XInfoGroups(ctx, "race:italy").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res34)
	// >>> [{italy_riders 3 2 1692632662819-0 3 2}]
```

```c#
        StreamGroupInfo[] res33 = db.StreamGroupInfo("race:italy");

        foreach (StreamGroupInfo info in res33)
        {
            Console.WriteLine($"name: {info.Name}, consumers: {info.ConsumerCount}, pending: {info.PendingMessageCount}, last-delivered-id: {info.LastDeliveredId}");
        }
        // >>> name: italy_riders, consumers: 2, pending: 2, last-delivered-id: 1712757192730-2
```

```ruby
res32 = r.xinfo(:groups, 'race:italy')
puts res32.inspect
```

```rust
        if let Ok(res) = r.xinfo_groups("race:italy") {
            let res: StreamInfoGroupsReply = res;
            let view: Vec<_> = res
                .groups
                .iter()
                .map(|group| {
                    (
                        group.name.clone(),
                        group.consumers,
                        group.pending,
                        group.last_delivered_id.clone(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("italy_riders", 3, 2, "1692632662819-0")]
        }
```

```rust
        if let Ok(res) = r.xinfo_groups("race:italy").await {
            let res: StreamInfoGroupsReply = res;
            let view: Vec<_> = res
                .groups
                .iter()
                .map(|group| {
                    (
                        group.name.clone(),
                        group.consumers,
                        group.pending,
                        group.last_delivered_id.clone(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("italy_riders", 3, 2, "1692632662819-0")]
        }
```

As you can see in this and in the previous output, the `XINFO` command outputs a sequence of field-value items. Because it is an observability command this allows the human user to immediately understand what information is reported, and allows the command to report more information in the future by adding more fields without breaking compatibility with older clients. Other commands that must be more bandwidth efficient, like `XPENDING`, just report the information without the field names.

The output of the example above, where the **GROUPS** subcommand is used, should be clear observing the field names. We can check in more detail the state of a specific consumer group by checking the consumers that are registered in the group.

Get detailed consumer information for a group using XINFO CONSUMERS to monitor individual consumer status

```plaintext
> XINFO CONSUMERS race:italy italy_riders
1) 1) "name"
   2) "Alice"
   3) "pending"
   4) (integer) 1
   5) "idle"
   6) (integer) 177546
2) 1) "name"
   2) "Bob"
   3) "pending"
   4) (integer) 0
   5) "idle"
   6) (integer) 424686
3) 1) "name"
   2) "Lora"
   3) "pending"
   4) (integer) 1
   5) "idle"
   6) (integer) 72241
```

```python
res33 = r.xinfo_consumers("race:italy", "italy_riders")
print(
    res33
)
# >>> [
#       {'name': 'Alice', 'pending': 2, 'idle': 199332},
#       {'name': 'Bob', 'pending': 0, 'idle': 489170}
# ]
```

```node
const res33 = await client.xInfoConsumers('race:italy', 'italy_riders');
console.log(res33); // >>> [{ name: 'Alice', pending: 3, idle: 170582, inactive: 170582 }, { name: 'Bob', pending: 0, idle: 489404, inactive: 489404 }]
```

```java
    List<StreamConsumersInfo> res34 = jedis.xinfoConsumers("race:italy","italy_riders");
    for (StreamConsumerInfo a : res34){
      System.out.println(
        a.getConsumerInfo()
      ); // {inactive=1, idle=1, pending=1, name=Alice} , {inactive=3, idle=3, pending=1, name=Bob}
    }
```

```go
	res35, err := rdb.XInfoConsumers(ctx, "race:italy", "italy_riders").Result()

	if err != nil {
		panic(err)
	}

	// fmt.Println(res35)
	// >>> [{Alice 1 1ms 1ms} {Bob 1 2ms 2ms} {Lora 0 1ms -1ms}]
```

```c#
        StreamConsumerInfo[] res34 = db.StreamConsumerInfo("race:italy", "italy_riders");

        foreach (StreamConsumerInfo info in res34)
        {
            Console.WriteLine($"name: {info.Name}, pending: {info.PendingMessageCount}, idle: {info.IdleTimeInMilliseconds}");
        }
        // >>> name: Alice, pending: 1, idle: 7717
        // >>> name: Bob, pending: 0, idle: 7722
```

```ruby
res33 = r.xinfo(:consumers, 'race:italy', 'italy_riders')
puts res33.inspect
```

```rust
        if let Ok(res) = r.xinfo_consumers("race:italy", "italy_riders") {
            let res: StreamInfoConsumersReply = res;
            let mut view: Vec<_> = res
                .consumers
                .iter()
                .map(|consumer| (consumer.name.clone(), consumer.pending, consumer.idle))
                .collect();
            view.sort_by(|a, b| a.0.cmp(&b.0));
            println!("{view:?}");
            // >>> [("Alice", 1, 5), ("Bob", 0, 5), ("Lora", 1, 5)]
        }
```

```rust
        if let Ok(res) = r.xinfo_consumers("race:italy", "italy_riders").await {
            let res: StreamInfoConsumersReply = res;
            let mut view: Vec<_> = res
                .consumers
                .iter()
                .map(|consumer| (consumer.name.clone(), consumer.pending, consumer.idle))
                .collect();
            view.sort_by(|a, b| a.0.cmp(&b.0));
            println!("{view:?}");
            // >>> [("Alice", 1, 5), ("Bob", 0, 5), ("Lora", 1, 5)]
        }
```

In case you do not remember the syntax of the command, just ask the command itself for help:

```
> XINFO HELP
1) XINFO <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
2) CONSUMERS <key> <groupname>
3)     Show consumers of <groupname>.
4) GROUPS <key>
5)     Show the stream consumer groups.
6) STREAM <key> [FULL [COUNT <count>]
7)     Show information about the stream.
8) HELP
9)     Prints this help.
```


## Differences with Kafka (TM) partitions

Consumer groups in Redis streams may resemble in some way Kafka (TM) partitioning-based consumer groups, however note that Redis streams are, in practical terms, very different. The partitions are only *logical* and the messages are just put into a single Redis key, so the way the different clients are served is based on who is ready to process new messages, and not from which partition clients are reading. For instance, if the consumer C3 at some point fails permanently, Redis will continue to serve C1 and C2 all the new messages arriving, as if now there are only two *logical* partitions.

Similarly, if a given consumer is much faster at processing messages than the other consumers, this consumer will receive proportionally more messages in the same unit of time. This is possible since Redis tracks all the unacknowledged messages explicitly, and remembers who received which message and the ID of the first message never delivered to any consumer.

However, this also means that in Redis if you really want to partition messages in the same stream into multiple Redis instances, you have to use multiple keys and some sharding system such as Redis Cluster or some other application-specific sharding system. A single Redis stream is not automatically partitioned to multiple instances.

We could say that schematically the following is true:

- If you use 1 stream -> 1 consumer, you are processing messages in order.
- If you use N streams with N consumers, so that only a given consumer hits a subset of the N streams, you can scale the above model of 1 stream -> 1 consumer.
- If you use 1 stream -> N consumers, you are load balancing to N consumers, however in that case, messages about the same logical item may be consumed out of order, because a given consumer may process message 3 faster than another consumer is processing message 4.

So basically Kafka partitions are more similar to using N different Redis keys, while Redis consumer groups are a server-side load balancing system of messages from a given stream to N different consumers.
