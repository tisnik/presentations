# NATS

## Intro

* Scalable and resilient message broker
* Written in Go
    - Initial version written in Ruby (Derek Collison)
* Multiple cooperating components

## NATS components

* Server (gnatsd)
* Interfaces for various ecosystems
* NATS Streaming Server
* NATS Connector Framework

## NATS ecosystems support

### Official

1. C
1. C#
1. Elixir
1. Go
1. Java
1. NGINX
1. Node.js
1. Python Asyncio
1. Python Tornado
1. Ruby
1. TypeScript

### Unofficial

1. .NET
1. Arduino
1. Clojure
1. Elm
1. Erlang
1. Haskell
1. Lua
1. MicroPython
1. PHP
1. Perl
1. Python
1. Python Twisted
1. Qt5 C++
1. Rust
1. Scala
1. Spring API
1. Swift

## Communication strategies

* pub-sub
    - using *subjects* (similar to *topics*)
* push-pull (via queues)
* request-reply
    - point-to-point
    - one-to-many
    - (based on *inbox* for replies)


## Protocol used by NATS

* text-based
    - but data can be binary
* possible to test it via *telnet*

```
Command send by
INFO 	server
CONNECT client
PUB 	client
SUB 	client
UNSUB 	client
MSG 	server
PING 	client and server
PONG 	client and server
+OK 	server
-ERR 	server
```

## Communicating with NATS

### The simplest producer

```go
package main
 
import nats "github.com/nats-io/go-nats"
 
const Subject = "test1"
 
func main() {
        conn, _ := nats.Connect(nats.DefaultURL)
 
        conn.Publish(Subject, []byte("Hello World"))
 
        conn.Flush()
}
```

### Better producer

* With error checks etc.

```go
package main
 
import (
        nats "github.com/nats-io/go-nats"
        "log"
)
 
const Subject = "test1"
 
func main() {
        conn, err := nats.Connect(nats.DefaultURL)
 
        if err != nil {
                log.Fatal(err)
        }
 
        defer conn.Close()
 
        println("Connected")
 
        err2 := conn.Publish(Subject, []byte("Hello World"))
 
        if err2 != nil {
                log.Fatal(err2)
        }
 
        conn.Flush()
 
        println("Message sent")
}
```

### Usage of channels

```go
package main
 
import (
        nats "github.com/nats-io/go-nats"
        "log"
)
 
const Subject = "test1"
 
func main() {
        conn, err := nats.Connect(nats.DefaultURL)
 
        if err != nil {
                log.Fatal(err)
        }
 
        defer conn.Close()
 
        println("Connected")
 
        econn, err2 := nats.NewEncodedConn(conn, nats.DEFAULT_ENCODER)
 
        if err2 != nil {
                log.Fatal(err)
        }
 
        defer econn.Close()
 
        channel := make(chan string)
        econn.BindSendChan(Subject, channel)
 
        println("Channel created")
 
        channel <- "Hello World #1"
        channel <- "Hello World #2"
        channel <- "Hello World #3"
 
        println("All messages sent")
}
```

### The simplest consumer

```go
package main
 
import (
        "fmt"
        "sync"

        nats "github.com/nats-io/go-nats"
)
 
const Subject = "test1"
 
func main() {
        conn, _ := nats.Connect(nats.DefaultURL)
 
        wg := sync.WaitGroup{}
        wg.Add(1)
 
        conn.Subscribe(Subject, func(m *nats.Msg) {
                fmt.Printf("Received a message: %s\n", string(m.Data))
                wg.Done()
        })
        wg.Wait()
}
```

### Better consumer

* Again with error checks etc.

```go
package main
 
import (
        "fmt"
        nats "github.com/nats-io/go-nats"
        "log"
        "sync"
)
 
const Subject = "test1"
 
func main() {
        conn, err := nats.Connect(nats.DefaultURL)
 
        if err != nil {
                log.Fatal(err)
        }
 
        defer conn.Close()
 
        wg := sync.WaitGroup{}
        wg.Add(1)
 
        sub, err2 := conn.Subscribe(Subject, func(m *nats.Msg) {
                fmt.Printf("Received a message: %s\n", string(m.Data))
                wg.Done()
        })
 
        if err2 != nil {
                log.Fatal(err2)
        }
 
        println("Subscribed", sub)
 
        wg.Wait()
 
        println("Finished waiting for message")
 
        err3 := sub.Unsubscribe()
        if err3 != nil {
                log.Fatal(err3)
        }
 
        println("Unsubscribed")
}
```

### Usage of channels in consumer code

### Multi-channel consumer

* interesting solution for some subtle communication patterns

## NATS Streaming Server

* Extension to the standard message broker
    - message persistence (optional)
    - ensure message delivery for producer (optional)
    - ensure message delivery for consumer (optional)
    - configurable publisher rate limit
    - configurable rate limiting per subscriber
    - messages are replayable

* NATS Streaming support
    1. C
    1. C#
    1. Go
    1. Java
    1. Node.js
    1. Python Asyncio
    1. Ruby

## Links

### Czech articles about NATS

* [Komunikace s message brokery z programovacího jazyka Go](https://www.root.cz/clanky/komunikace-s-message-brokery-z-programovaciho-jazyka-go/#k15)
* [Použití message brokeru NATS](https://www.root.cz/clanky/pouziti-message-brokeru-nats/)
* [NATS Streaming Server](https://www.root.cz/clanky/nats-streaming-server/)

