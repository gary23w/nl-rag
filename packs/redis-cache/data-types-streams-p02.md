---
title: "Redis Streams (part 2/5)"
source: https://redis.io/docs/latest/develop/data-types/streams/
domain: redis-cache
license: CC-BY-SA-4.0
tags: redis, in-memory data store, key-value cache, in-memory database
fetched: 2026-07-02
part: 2/5
---

## Getting data from Streams

Now we are finally able to append entries in our stream via `XADD`. However, while appending data to a stream is quite obvious, the way streams can be queried in order to extract data is not so obvious. If we continue with the analogy of the log file, one obvious way is to mimic what we normally do with the Unix command `tail -f`, that is, we may start to listen in order to get the new messages that are appended to the stream. Note that unlike the blocking list operations of Redis, where a given element will reach a single client which is blocking in a *pop style* operation like `BLPOP`, with streams we want multiple consumers to see the new messages appended to the stream (the same way many `tail -f` processes can see what is added to a log). Using the traditional terminology we want the streams to be able to *fan out* messages to multiple clients.

However, this is just one potential access mode. We could also see a stream in quite a different way: not as a messaging system, but as a *time series store*. In this case, maybe it's also useful to get the new messages appended, but another natural query mode is to get messages by ranges of time, or alternatively to iterate the messages using a cursor to incrementally check all the history. This is definitely another useful access mode.

Finally, if we see a stream from the point of view of consumers, we may want to access the stream in yet another way, that is, as a stream of messages that can be partitioned to multiple consumers that are processing such messages, so that groups of consumers can only see a subset of the messages arriving in a single stream. In this way, it is possible to scale the message processing across different consumers, without single consumers having to process all the messages: each consumer will just get different messages to process. This is basically what Kafka (TM) does with consumer groups. Reading messages via consumer groups is yet another interesting mode of reading from a Redis Stream.

Redis Streams support all three of the query modes described above via different commands. The next sections will show them all, starting from the simplest and most direct to use: range queries.

### Querying by range: XRANGE and XREVRANGE

To query the stream by range we are only required to specify two IDs, *start* and *end*. The range returned will include the elements having start or end as ID, so the range is inclusive. The two special IDs `-` and `+` respectively mean the smallest and the greatest ID possible.

Foundational: Retrieve all entries in a stream using XRANGE with - and + special IDs

```plaintext
> XRANGE race:france - +
1) 1) "1692632086370-0"
   2) 1) "rider"
      2) "Castilla"
      3) "speed"
      4) "30.2"
      5) "position"
      6) "1"
      7) "location_id"
      8) "1"
2) 1) "1692632094485-0"
   2) 1) "rider"
      2) "Norem"
      3) "speed"
      4) "28.8"
      5) "position"
      6) "3"
      7) "location_id"
      8) "1"
3) 1) "1692632102976-0"
   2) 1) "rider"
      2) "Prickett"
      3) "speed"
      4) "29.7"
      5) "position"
      6) "2"
      7) "location_id"
      8) "1"
4) 1) "1692632147973-0"
   2) 1) "rider"
      2) "Castilla"
      3) "speed"
      4) "29.9"
      5) "position"
      6) "1"
      7) "location_id"
      8) "2"
```

```python
res11 = r.xrange("race:france", "-", "+")
print(
    res11
)
# >>> [
#   ('1692629576966-0',
#       {'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1'}
#   ),
#   ('1692629594113-0',
#       {'rider': 'Norem', 'speed': '28.8', 'position': '3', 'location_id': '1'}
#   ),
#   ('1692629613374-0',
#       {'rider': 'Prickett', 'speed': '29.7', 'position': '2', 'location_id': '1'}
#   ),
#   ('1692629676124-0',
#       {'rider': 'Castilla', 'speed': '29.9', 'position': '1', 'location_id': '2'}
#   )
# ]
```

```node
const res11 = await client.xRange('race:france', '-', '+');
console.log(res11); // >>> [{ id: '1692629576966-0', message: { rider: 'Castilla', speed: '30.2', position: '1', location_id: '1' } }, { id: '1692629594113-0', message: { rider: 'Norem', speed: '28.8', position: '3', location_id: '1' } }, { id: '1692629613374-0', message: { rider: 'Prickett', speed: '29.7', position: '2', location_id: '1' } }, { id: '1692629676124-0', message: { rider: 'Castilla', speed: '29.9', position: '1', location_id: '2' } }]
```

```java
    List<StreamEntry> res12 = jedis.xrange("race:france","-","+");
    System.out.println(
      res12
    ); // >>> [1701764734160-0 {rider=Castilla, speed=30.2, location_id=1, position=1}, 1701764734160-1 {rider=Norem, speed=28.8, location_id=1, position=3}, 1701764734161-0 {rider=Prickett, speed=29.7, location_id=1, position=2}, 1701764734162-0 {rider=Castilla, speed=29.9, location_id=1, position=2}]
```

```go
	res12, err := rdb.XRange(ctx, "race:france", "-", "+").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res12)
	// >>> [{1692632086370-0 map[location_id:1 position:1 rider:Castilla...
```

```c#
        StreamEntry[] res12 = db.StreamRange("race:france", "-", "+");

        foreach (StreamEntry entry in res12)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712668482289-0: [rider: Castilla, speed: 30.199999999999999, position: 1, location_id: 1]
        // >>> 1712668766534-1: [rider: Norem, speed: 28.800000000000001, position: 3, location_id: 1]
        // >>> 1712669055705-0: [rider: Prickett, speed: 29.699999999999999, position: 2, location_id: 1]
        // >>> 1712675674750-0: [rider: Castilla, speed: 29.899999999999999, position: 1, location_id: 2]
```

```ruby
r.del('race:france')
r.xadd('race:france', {'rider' => 'Castilla', 'speed' => '30.2', 'position' => '1', 'location_id' => '1'}, id: '1692632086370-0')
r.xadd('race:france', {'rider' => 'Norem', 'speed' => '28.8', 'position' => '3', 'location_id' => '1'}, id: '1692632094485-0')
r.xadd('race:france', {'rider' => 'Prickett', 'speed' => '29.7', 'position' => '2', 'location_id' => '1'}, id: '1692632102976-0')
r.xadd('race:france', {'rider' => 'Castilla', 'speed' => '29.9', 'position' => '1', 'location_id' => '2'}, id: '1692632147973-0')
res11 = r.xrange('race:france', '-', '+')
puts res11.inspect
# [["1692632086370-0", {"rider"=>"Castilla", "speed"=>"30.2", "position"=>"1", "location_id"=>"1"}],
#  ["1692632094485-0", {"rider"=>"Norem", "speed"=>"28.8", "position"=>"3", "location_id"=>"1"}],
#  ["1692632102976-0", {"rider"=>"Prickett", "speed"=>"29.7", "position"=>"2", "location_id"=>"1"}],
#  ["1692632147973-0", {"rider"=>"Castilla", "speed"=>"29.9", "position"=>"1", "location_id"=>"2"}]]
```

```rust
        if let Ok(res) = r.xrange_all("race:france") {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")]), ("1692632094485-0", [("rider", "Norem"), ("speed", "28.8"), ("position", "3"), ("location_id", "1")]), ("1692632102976-0", [("rider", "Prickett"), ("speed", "29.7"), ("position", "2"), ("location_id", "1")]), ("1692632147973-0", [("rider", "Castilla"), ("speed", "29.9"), ("position", "1"), ("location_id", "2")])]
        }
```

```rust
        add_france_fixed(&mut r).await;
        if let Ok(res) = r.xrange_all("race:france").await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")]), ("1692632094485-0", [("rider", "Norem"), ("speed", "28.8"), ("position", "3"), ("location_id", "1")]), ("1692632102976-0", [("rider", "Prickett"), ("speed", "29.7"), ("position", "2"), ("location_id", "1")]), ("1692632147973-0", [("rider", "Castilla"), ("speed", "29.9"), ("position", "1"), ("location_id", "2")])]
        }
```

Each entry returned is an array of two items: the ID and the list of field-value pairs. We already said that the entry IDs have a relation with the time, because the part at the left of the `-` character is the Unix time in milliseconds of the local node that created the stream entry, at the moment the entry was created (however note that streams are replicated with fully specified `XADD` commands, so the replicas will have identical IDs to the master). This means that I could query a range of time using `XRANGE`. In order to do so, however, I may want to omit the sequence part of the ID: if omitted, in the start of the range it will be assumed to be 0, while in the end part it will be assumed to be the maximum sequence number available. This way, querying using just two milliseconds Unix times, we get all the entries that were generated in that range of time, in an inclusive way. For instance, if I want to query a two milliseconds period I could use:

Query stream entries by time range using millisecond timestamps instead of full IDs

```plaintext
> XRANGE race:france 1692632086369 1692632086371
1) 1) "1692632086370-0"
   2) 1) "rider"
      2) "Castilla"
      3) "speed"
      4) "30.2"
      5) "position"
      6) "1"
      7) "location_id"
      8) "1"
```

```python
res12 = r.xrange("race:france", 1692629576965, 1692629576967)
print(
    res12
)
# >>> [
#       ('1692629576966-0',
#           {'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1'}
#       )
# ]
```

```node
const res12 = await client.xRange('race:france', '1692629576965', '1692629576967');
console.log(res12); // >>> [{ id: '1692629576966-0', message: { rider: 'Castilla', speed: '30.2', position: '1', location_id: '1' } }]
```

```java
    List<StreamEntry> res13 = jedis.xrange("race:france",String.valueOf(System.currentTimeMillis()-1000),String.valueOf(System.currentTimeMillis()+1000));
    System.out.println(
      res13
    ); // >>> [1701764734160-0 {rider=Castilla, speed=30.2, location_id=1, position=1}, 1701764734160-1 {rider=Norem, speed=28.8, location_id=1, position=3}, 1701764734161-0 {rider=Prickett, speed=29.7, location_id=1, position=2}, 1701764734162-0 {rider=Castilla, speed=29.9, location_id=1, position=2}]
```

```go
	res13, err := rdb.XRange(ctx, "race:france",
		"1692632086369", "1692632086371",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res13)
	// >>> [{1692632086370-0 map[location_id:1 position:1 rider:Castilla speed:30.2] 0 0}]
```

```c#
        StreamEntry[] res13 = db.StreamRange("race:france", 1712668482289, 1712668482291);

        foreach (StreamEntry entry in res13)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712668482289-0: [rider: Castilla, speed: 30.199999999999999, position: 1, location_id: 1]
```

```ruby
r.del('race:france')
r.xadd('race:france', {'rider' => 'Castilla', 'speed' => '30.2', 'position' => '1', 'location_id' => '1'}, id: '1692632086370-0')
r.xadd('race:france', {'rider' => 'Norem', 'speed' => '28.8', 'position' => '3', 'location_id' => '1'}, id: '1692632094485-0')
res12 = r.xrange('race:france', '1692632086369', '1692632086371')
puts res12.inspect
# [["1692632086370-0", {"rider"=>"Castilla", "speed"=>"30.2", "position"=>"1", "location_id"=>"1"}]]
```

```rust
        if let Ok(res) = r.xrange("race:france", "1692632086369", "1692632086371") {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")])]
        }
```

```rust
        add_france_fixed(&mut r).await;
        if let Ok(res) = r.xrange("race:france", "1692632086369", "1692632086371").await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")])]
        }
```

I have only a single entry in this range. However in real data sets, I could query for ranges of hours, or there could be many items in just two milliseconds, and the result returned could be huge. For this reason, `XRANGE` supports an optional **COUNT** option at the end. By specifying a count, I can just get the first *N* items. If I want more, I can get the last ID returned, increment the sequence part by one, and query again. Let's see this in the following example. Let's assume that the stream `race:france` was populated with 4 items. To start my iteration, getting 2 items per command, I start with the full range, but with a count of 2.

Practical pattern: Paginate stream entries using XRANGE with COUNT to retrieve results in batches

```plaintext
> XRANGE race:france - + COUNT 2
1) 1) "1692632086370-0"
   2) 1) "rider"
      2) "Castilla"
      3) "speed"
      4) "30.2"
      5) "position"
      6) "1"
      7) "location_id"
      8) "1"
2) 1) "1692632094485-0"
   2) 1) "rider"
      2) "Norem"
      3) "speed"
      4) "28.8"
      5) "position"
      6) "3"
      7) "location_id"
      8) "1"
```

```python
res13 = r.xrange("race:france", "-", "+", 2)
print(
    res13
)
# >>> [
#   ('1692629576966-0',
#       {'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1'}
#   ),
#   ('1692629594113-0',
#       {'rider': 'Norem', 'speed': '28.8', 'position': '3', 'location_id': '1'}
#   )
# ]
```

```node
const res13 = await client.xRange('race:france', '-', '+', {COUNT: 2});
console.log(res13); // >>> [{ id: '1692629576966-0', message: { rider: 'Castilla', speed: '30.2', position: '1', location_id: '1' } }, { id: '1692629594113-0', message: { rider: 'Norem', speed: '28.8', position: '3', location_id: '1' } }]
```

```java
    List<StreamEntry> res14 = jedis.xrange("race:france","-","+",2);
    System.out.println(res14); // >>> [1701764887638-0 {rider=Castilla, speed=30.2, location_id=1, position=1}, 1701764887638-1 {rider=Norem, speed=28.8, location_id=1, position=3}]
```

```go
	res14, err := rdb.XRangeN(ctx, "race:france", "-", "+", 2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res14)
	// >>> [{1692632086370-0 map[location_id:1 position:1 rider:Castilla speed:30.2] 0 0} {1692632094485-0 map[location_id:1 position:3 rider:Norem speed:28.8] 0 0}]
```

```c#
        StreamEntry[] res14 = db.StreamRange("race:france", "-", "+", 2);

        foreach (StreamEntry entry in res14)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712668482289-0: [rider: Castilla, speed: 30.199999999999999, position: 1, location_id: 1]
        // >>> 1712668766534-1: [rider: Norem, speed: 28.800000000000001, position: 3, location_id: 1]
```

```ruby
r.del('race:france')
r.xadd('race:france', {'rider' => 'Castilla', 'speed' => '30.2', 'position' => '1', 'location_id' => '1'}, id: '1692632086370-0')
r.xadd('race:france', {'rider' => 'Norem', 'speed' => '28.8', 'position' => '3', 'location_id' => '1'}, id: '1692632094485-0')
r.xadd('race:france', {'rider' => 'Prickett', 'speed' => '29.7', 'position' => '2', 'location_id' => '1'}, id: '1692632102976-0')
r.xadd('race:france', {'rider' => 'Castilla', 'speed' => '29.9', 'position' => '1', 'location_id' => '2'}, id: '1692632147973-0')
res13 = r.xrange('race:france', '-', '+', count: 2)
puts res13.inspect
# [["1692632086370-0", {"rider"=>"Castilla", "speed"=>"30.2", "position"=>"1", "location_id"=>"1"}],
#  ["1692632094485-0", {"rider"=>"Norem", "speed"=>"28.8", "position"=>"3", "location_id"=>"1"}]]
```

```rust
        if let Ok(res) = r.xrange_count("race:france", "-", "+", 2) {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")]), ("1692632094485-0", [("rider", "Norem"), ("speed", "28.8"), ("position", "3"), ("location_id", "1")])]
        }
```

```rust
        add_france_fixed(&mut r).await;
        if let Ok(res) = r.xrange_count("race:france", "-", "+", 2).await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")]), ("1692632094485-0", [("rider", "Norem"), ("speed", "28.8"), ("position", "3"), ("location_id", "1")])]
        }
```

To continue the iteration with the next two items, I have to pick the last ID returned, that is `1692632094485-0`, and add the prefix `(` to it. The resulting exclusive range interval, that is `(1692632094485-0` in this case, can now be used as the new *start* argument for the next `XRANGE` call:

Practical pattern: Continue pagination using exclusive range syntax with ( prefix to skip the last retrieved entry

```plaintext
> XRANGE race:france (1692632094485-0 + COUNT 2
1) 1) "1692632102976-0"
   2) 1) "rider"
      2) "Prickett"
      3) "speed"
      4) "29.7"
      5) "position"
      6) "2"
      7) "location_id"
      8) "1"
2) 1) "1692632147973-0"
   2) 1) "rider"
      2) "Castilla"
      3) "speed"
      4) "29.9"
      5) "position"
      6) "1"
      7) "location_id"
      8) "2"
```

```python
res14 = r.xrange("race:france", "(1692629594113-0", "+", 2)
print(
    res14
)
# >>> [
#   ('1692629613374-0',
#       {'rider': 'Prickett', 'speed': '29.7', 'position': '2', 'location_id': '1'}
#   ),
#   ('1692629676124-0',
#       {'rider': 'Castilla', 'speed': '29.9', 'position': '1', 'location_id': '2'}
#   )
# ]
```

```node
const res14 = await client.xRange('race:france', '(1692629594113-0', '+', {COUNT: 2});
console.log(res14); // >>> [{ id: '1692629613374-0', message: { rider: 'Prickett', speed: '29.7', position: '2', location_id: '1' } }, { id: '1692629676124-0', message: { rider: 'Castilla', speed: '29.9', position: '1', location_id: '2' } }]
```

```java
    List<StreamEntry> res15 = jedis.xrange("race:france",String.valueOf(System.currentTimeMillis()-1000)+"-0","+",2);
    System.out.println(res15); // >>> [1701764887638-0 {rider=Castilla, speed=30.2, location_id=1, position=1}, 1701764887638-1 {rider=Norem, speed=28.8, location_id=1, position=3}]
```

```go
	res15, err := rdb.XRangeN(ctx, "race:france",
		"(1692632094485-0", "+", 2,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res15)
	// >>> [{1692632102976-0 map[location_id:1 position:2 rider:Prickett speed:29.7] 0 0} {1692632147973-0 map[location_id:2 position:1 rider:Castilla speed:29.9] 0 0}]
```

```c#
        StreamEntry[] res15 = db.StreamRange("race:france", "(1712668766534-1", "+", 2);

        foreach (StreamEntry entry in res15)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712669055705-0: [rider: Prickett, speed: 29.699999999999999, position: 2, location_id: 1]
        // >>> 1712675674750-0: [rider: Castilla, speed: 29.899999999999999, position: 1, location_id: 2]
```

```ruby
r.del('race:france')
r.xadd('race:france', {'rider' => 'Castilla', 'speed' => '30.2', 'position' => '1', 'location_id' => '1'}, id: '1692632086370-0')
r.xadd('race:france', {'rider' => 'Norem', 'speed' => '28.8', 'position' => '3', 'location_id' => '1'}, id: '1692632094485-0')
r.xadd('race:france', {'rider' => 'Prickett', 'speed' => '29.7', 'position' => '2', 'location_id' => '1'}, id: '1692632102976-0')
r.xadd('race:france', {'rider' => 'Castilla', 'speed' => '29.9', 'position' => '1', 'location_id' => '2'}, id: '1692632147973-0')
res14 = r.xrange('race:france', '(1692632094485-0', '+', count: 2)
puts res14.inspect
# [["1692632102976-0", {"rider"=>"Prickett", "speed"=>"29.7", "position"=>"2", "location_id"=>"1"}],
#  ["1692632147973-0", {"rider"=>"Castilla", "speed"=>"29.9", "position"=>"1", "location_id"=>"2"}]]
```

```rust
        if let Ok(res) = r.xrange_count("race:france", "(1692632094485-0", "+", 2) {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632102976-0", [("rider", "Prickett"), ("speed", "29.7"), ("position", "2"), ("location_id", "1")]), ("1692632147973-0", [("rider", "Castilla"), ("speed", "29.9"), ("position", "1"), ("location_id", "2")])]
        }
```

```rust
        add_france_fixed(&mut r).await;
        if let Ok(res) = r.xrange_count("race:france", "(1692632094485-0", "+", 2).await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632102976-0", [("rider", "Prickett"), ("speed", "29.7"), ("position", "2"), ("location_id", "1")]), ("1692632147973-0", [("rider", "Castilla"), ("speed", "29.9"), ("position", "1"), ("location_id", "2")])]
        }
```

Now that we've retrieved 4 items out of a stream that only had 4 entries in it, if we try to retrieve more items, we'll get an empty array:

Practical pattern: Handle empty results when pagination reaches the end of the stream

```plaintext
> XRANGE race:france (1692632147973-0 + COUNT 2
(empty array)
```

```python
res15 = r.xrange("race:france", "(1692629676124-0", "+", 2)
print(res15)  # >>> []
```

```node
const res15 = await client.xRange('race:france', '(1692629676124-0', '+', {COUNT: 2});
console.log(res15); // >>> []
```

```java
    List<StreamEntry> res16 = jedis.xrange("race:france",String.valueOf(System.currentTimeMillis()+1000)+"-0","+",2);
    System.out.println(res16); // >>> []
```

```go
	res16, err := rdb.XRangeN(ctx, "race:france",
		"(1692632147973-0", "+", 2,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res16)
	// >>> []
```

```c#
        StreamEntry[] res16 = db.StreamRange("race:france", "(1712675674750-0", "+", 2);

        foreach (StreamEntry entry in res16)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> <empty array>
```

```ruby
res15 = r.xrange('race:france', '(1692632147973-0', '+', count: 2)
puts res15.inspect # []
```

```rust
        if let Ok(res) = r.xrange_count("race:france", "(1692632147973-0", "+", 2) {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}"); // >>> []
        }
```

```rust
        add_france_fixed(&mut r).await;
        if let Ok(res) = r.xrange_count("race:france", "(1692632147973-0", "+", 2).await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}"); // >>> []
        }
```

Since `XRANGE` complexity is *O(log(N))* to seek, and then *O(M)* to return M elements, with a small count the command has a logarithmic time complexity, which means that each step of the iteration is fast. So `XRANGE` is also the de facto *streams iterator* and does not require an **XSCAN** command.

The command `XREVRANGE` is the equivalent of `XRANGE` but returning the elements in inverted order, so a practical use for `XREVRANGE` is to check what is the last item in a Stream:

Foundational: Retrieve stream entries in reverse order using XREVRANGE when you need the most recent entries first

```plaintext
> XREVRANGE race:france + - COUNT 1
1) 1) "1692632147973-0"
   2) 1) "rider"
      2) "Castilla"
      3) "speed"
      4) "29.9"
      5) "position"
      6) "1"
      7) "location_id"
      8) "2"
```

```python
res16 = r.xrevrange("race:france", "+", "-", 1)
print(
    res16
)
# >>> [
#       ('1692629676124-0',
#           {'rider': 'Castilla', 'speed': '29.9', 'position': '1', 'location_id': '2'}
#       )
# ]
```

```node
const res16 = await client.xRevRange('race:france', '+', '-', {COUNT: 1});
console.log(
  res16
); // >>> [{ id: '1692629676124-0', message: { rider: 'Castilla', speed: '29.9', position: '1', location_id: '2' } }]
```

```java
    List<StreamEntry> res17 = jedis.xrevrange("race:france","+","-",1);
    System.out.println(res17); // >>> [1701765218592-0 {rider=Castilla, speed=29.9, location_id=1, position=2}]
```

```go
	res17, err := rdb.XRevRangeN(ctx, "race:france", "+", "-", 1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res17)
	// >>> [{1692632147973-0 map[location_id:2 position:1 rider:Castilla speed:29.9] 0 0}]
```

```c#
        StreamEntry[] res17 = db.StreamRange("race:france", "+", "-", 1, Order.Descending);

        foreach (StreamEntry entry in res17)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712675674750-0: [rider: Castilla, speed: 29.899999999999999, position: 1, location_id: 2]
```

```ruby
res16 = r.xrevrange('race:france', '+', '-', count: 1)
puts res16.inspect
# [["1692632147973-0", {"rider"=>"Castilla", "speed"=>"29.9", "position"=>"1", "location_id"=>"2"}]]
```

```rust
        if let Ok(res) = r.xrevrange_count("race:france", "+", "-", 1) {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632147973-0", [("rider", "Castilla"), ("speed", "29.9"), ("position", "1"), ("location_id", "2")])]
        }
```

```rust
        add_france_fixed(&mut r).await;
        if let Ok(res) = r.xrevrange_count("race:france", "+", "-", 1).await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632147973-0", [("rider", "Castilla"), ("speed", "29.9"), ("position", "1"), ("location_id", "2")])]
        }
```

Note that the `XREVRANGE` command takes the *start* and *stop* arguments in reverse order.


## Listening for new items with XREAD

When we do not want to access items by a range in a stream, usually what we want instead is to *subscribe* to new items arriving to the stream. This concept may appear related to Redis Pub/Sub, where you subscribe to a channel, or to Redis blocking lists, where you wait for a key to get new elements to fetch, but there are fundamental differences in the way you consume a stream:

1. A stream can have multiple clients (consumers) waiting for data. Every new item, by default, will be delivered to *every consumer* that is waiting for data in a given stream. This behavior is different than blocking lists, where each consumer will get a different element. However, the ability to *fan out* to multiple consumers is similar to Pub/Sub.
2. While in Pub/Sub messages are *fire and forget* and are never stored anyway, and while when using blocking lists, when a message is received by the client it is *popped* (effectively removed) from the list, streams work in a fundamentally different way. All the messages are appended in the stream indefinitely (unless the user explicitly asks to delete entries): different consumers will know what is a new message from its point of view by remembering the ID of the last message received.
3. Streams Consumer Groups provide a level of control that Pub/Sub or blocking lists cannot achieve, with different groups for the same stream, explicit acknowledgment of processed items, ability to inspect the pending items, claiming of unprocessed messages, and coherent history visibility for each single client, that is only able to see its private past history of messages.

The command that provides the ability to listen for new messages arriving into a stream is called `XREAD`. It's a bit more complex than `XRANGE`, so we'll start showing simple forms, and later the whole command layout will be provided.

Foundational: Read entries from a stream starting from a specific ID using XREAD (non-blocking form)

```plaintext
> XREAD COUNT 2 STREAMS race:france 0
1) 1) "race:france"
   2) 1) 1) "1692632086370-0"
         2) 1) "rider"
            2) "Castilla"
            3) "speed"
            4) "30.2"
            5) "position"
            6) "1"
            7) "location_id"
            8) "1"
      2) 1) "1692632094485-0"
         2) 1) "rider"
            2) "Norem"
            3) "speed"
            4) "28.8"
            5) "position"
            6) "3"
            7) "location_id"
            8) "1"
```

```python
res17 = r.xread(streams={"race:france": 0}, count=2)
print(
    res17
)
# >>> [
#       ['race:france', [
#       ('1692629576966-0',
#           {'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1'}
#       ),
#       ('1692629594113-0',
#           {'rider': 'Norem', 'speed': '28.8', 'position': '3', 'location_id': '1'}
#       )
#       ]
#       ]
#   ]
```

```node
const res17 = await client.xRead({
  key: 'race:france',
  id: '0-0'
}, {
  COUNT: 2
});
console.log(res17); // >>> [{ name: 'race:france', messages: [{ id: '1692629576966-0', message: { rider: 'Castilla', speed: '30.2', position: '1', location_id: '1' } }, { id: '1692629594113-0', message: { rider: 'Norem', speed: '28.8', position: '3', location_id: '1' } }] }]
```

```java
    List<Map.Entry<String, List<StreamEntry>>> res18= jedis.xread(XReadParams.xReadParams().count(2),new HashMap<String,StreamEntryID>(){{put("race:france",new StreamEntryID());}});
    System.out.println(
      res18
    ); // >>> [race:france=[1701765384638-0 {rider=Castilla, speed=30.2, location_id=1, position=1}, 1701765384638-1 {rider=Norem, speed=28.8, location_id=1, position=3}]]
```

```go
	res18, err := rdb.XRead(ctx, &redis.XReadArgs{
		Streams: []string{"race:france", "0"},
		Count:   2,
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res18)
	// >>> [{race:france [{1692632086370-0 map[location_id:1 position:1 rider:Castilla speed:30.2] 0 0} {1692632094485-0 map[location_id:1 position:3 rider:Norem speed:28.8] 0 0}]}]
```

```c#
        StreamEntry[] res18 = db.StreamRead("race:france", 0, 2);

        foreach (StreamEntry entry in res18)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712668482289-0: [rider: Castilla, speed: 30.199999999999999, position: 1, location_id: 1]
        // >>> 1712668766534-1: [rider: Norem, speed: 28.800000000000001, position: 3, location_id: 1]
```

```ruby
res17 = r.xread(['race:france'], ['0'], count: 2)
puts res17.inspect
# {"race:france"=>[["1692632086370-0", {"rider"=>"Castilla", "speed"=>"30.2", "position"=>"1", "location_id"=>"1"}],
#                  ["1692632094485-0", {"rider"=>"Norem", "speed"=>"28.8", "position"=>"3", "location_id"=>"1"}]]}
```

```rust
        let opts = StreamReadOptions::default().count(2);
        if let Ok(res) = r.xread_options(&["race:france"], &["0"], &opts) {
            let res: Option<StreamReadReply> = res;
            let reply = res.expect("xread should return data");
            let view: Vec<_> = reply
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
                                    vec![
                                        ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                                        ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                                        ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                                        (
                                            "location_id".to_string(),
                                            entry.get::<String>("location_id").expect("missing location_id"),
                                        ),
                                    ],
                                )
                            })
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("race:france", [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")]), ("1692632094485-0", [("rider", "Norem"), ("speed", "28.8"), ("position", "3"), ("location_id", "1")])])]
        }
```

```rust
        add_france_fixed(&mut r).await;
        let opts = StreamReadOptions::default().count(2);
        if let Ok(res) = r.xread_options(&["race:france"], &["0"], &opts).await {
            let res: Option<StreamReadReply> = res;
            let view: Vec<_> = res
                .expect("xread should return data")
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
                                    vec![
                                        ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                                        ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                                        ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                                        (
                                            "location_id".to_string(),
                                            entry.get::<String>("location_id").expect("missing location_id"),
                                        ),
                                    ],
                                )
                            })
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("race:france", [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")]), ("1692632094485-0", [("rider", "Norem"), ("speed", "28.8"), ("position", "3"), ("location_id", "1")])])]
        }
```

The above is the non-blocking form of `XREAD`. Note that the **COUNT** option is not mandatory, in fact the only mandatory option of the command is the **STREAMS** option, that specifies a list of keys together with the corresponding maximum ID already seen for each stream by the calling consumer, so that the command will provide the client only with messages with an ID greater than the one we specified.

In the above command we wrote `STREAMS race:france 0` so we want all the messages in the Stream `race:france` having an ID greater than `0-0`. As you can see in the example above, the command returns the key name, because actually it is possible to call this command with more than one key to read from different streams at the same time. I could write, for instance: `STREAMS race:france race:italy 0 0`. Note how after the **STREAMS** option we need to provide the key names, and later the IDs. For this reason, the **STREAMS** option must always be the last option. Any other options must come before the **STREAMS** option.

Apart from the fact that `XREAD` can access multiple streams at once, and that we are able to specify the last ID we own to just get newer messages, in this simple form the command is not doing something so different compared to `XRANGE`. However, the interesting part is that we can turn `XREAD` into a *blocking command* easily, by specifying the **BLOCK** argument:

```
> XREAD BLOCK 0 STREAMS race:france $
```

Note that in the example above, other than removing **COUNT**, I specified the new **BLOCK** option with a timeout of 0 milliseconds (that means to never timeout). Moreover, instead of passing a normal ID for the stream `race:france` I passed the special ID `$`. This special ID means that `XREAD` should use as last ID the maximum ID already stored in the stream `race:france`, so that we will receive only *new* messages, starting from the time we started listening. This is similar to the `tail -f` Unix command in some way.

Note that when the **BLOCK** option is used, we do not have to use the special ID `$`. We can use any valid ID. If the command is able to serve our request immediately without blocking, it will do so, otherwise it will block. Normally if we want to consume the stream starting from new entries, we start with the ID `$`, and after that we continue using the ID of the last message received to make the next call, and so forth.

The blocking form of `XREAD` is also able to listen to multiple Streams, just by specifying multiple key names. If the request can be served synchronously because there is at least one stream with elements greater than the corresponding ID we specified, it returns with the results. Otherwise, the command will block and will return the items of the first stream which gets new data (according to the specified ID).

Similarly to blocking list operations, blocking stream reads are *fair* from the point of view of clients waiting for data, since the semantics is FIFO style. The first client that blocked for a given stream will be the first to be unblocked when new items are available.

`XREAD` has no other options than **COUNT** and **BLOCK**, so it's a pretty basic command with a specific purpose to attach consumers to one or multiple streams. More powerful features to consume streams are available using the consumer groups API, however reading via consumer groups is implemented by a different command called `XREADGROUP`, covered in the next section of this guide.
