## Redis Streams

![Redis logo](images/redis-logo.jpg)

### Info about Redis

* Written in C
* Optimized
* Binary size ~ 1.8 MB

### Support for streams in Redis

* Introduced in Redis 5
* Updated in Redis 6

### Basic operations

* Append message to a stream
* Read message from selected stream
* Blocking read (waiting for messages)

### Advanced operations

* Read more messages from selected stream
* Read range of messages specified by timestamp or offset
* Read more messages from more streams
* Blocking read from multiple streams
* Fan-out
* Consumer groups
* Acking messages in consumer groups

### Messages

* Have a structure (key+value)
* Have an ID
   - two parts
   - usually Unix timestamp in ms
   - sequence number within that ms

### New commands

* `XADD`
* `XLEN`
* `XREAD`
* `XRANGE`
* `XREVRANGE`
* `XREADGROUP`
* `XACK`
* `XPENDING`
* `XDEL`
* `XAUTOCLAIM`
* `XINFO`

### Support in other languages

* C
* Java
* Go
* Python

## Examples

### redis-cli

* Append new messages with explicit ID

```
xadd stream1 1 x 10 y 20
xadd stream1 2 x 10 y 20
```

* ID is splitted into two parts: main number (timestamp) + sequence number

```
xadd stream2 0-1 data first
xadd stream2 0-2 data second
xadd stream2 1-0 data third
```

* Automatic ID generation

```
xadd stream3 * x 1 y 2
xadd stream3 * x 2 y 1
xadd stream3 * x 3 y 0
```

* Read message specified by its ID

```
xread streams stream3 0
```

* Blocking read (waiting for new messages)

```
xread BLOCK 0 streams stream3 $
```

* Stream as time-event database

```
xrange stream2 - +
xrange stream3 0-1 0-4
xrevrange stream1 + -
```

* More streams consumed by one consumer

```
xread BLOCK 0 streams streamA streamB $ $
```

* Acking messages

```
XADD streamZ * foo 42
XGROUP CREATE streamZ groupZ $

XADD streamZ * m 1
XADD streamZ * m 2
XADD streamZ * m 3
XADD streamZ * m 4
XADD streamZ * m 5
XADD streamZ * m 6

XREADGROUP GROUP groupZ consumer1 COUNT 1 STREAMS streamZ >
XREADGROUP GROUP groupZ consumer1 STREAMS streamZ >

XACK streamZ groupZ 1611603108014-0
XPENDING streamZ groupZ
```

### Python

* Message producer

```python
from walrus import Database

db = Database()
stream = db.Stream("streamX")

message_id = stream.add({"foo": 10,
                         "bar": 20})
print(message_id)
```

* Message consumer

```python
from walrus import Database

db = Database()
stream = db.Stream("streamX")

messages = list(stream)
print(messages)
```

* Blocking read (waiting for new message)

```python
from walrus import Database

db = Database()
stream = db.Stream("streamX")

message = stream.read(block=0, last_id="$")
print(message)
```

* Read messages explicitly specified by its ID

```python
from walrus import Database

db = Database()
stream = db.Stream("streamY")

counter = 0

last_id = "0"

while True:
    messages = stream.read(block=0, last_id=last_id, count=1)
    message = messages[0]
    last_id = message[0]
    content = message[1]
    counter += 1
    if b"last" in content and content[b"last"] == b"y":
        break
```

* Consumer group usage

```python
from walrus import Database

db = Database()

cg = db.consumer_group("a-group", ["streamX"])
cg.create()
cg.set_id('$')

while True:
    messages = cg.read(block=0)
    for message in messages:
        print(message)
```
