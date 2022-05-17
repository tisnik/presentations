# Concurrency and parallelism in Python

* Concurrency is not parallelism

## Concurrency and parallelism

* Serial: runs tasks in an order with one CPU core
* Concurrent: runs many tasks simultaneously with a less number of CPU cores (or even 1)
* Parallel: runs n tasks simultaneously with n CPU cores

### Concurrency

* when multiple tasks can run in overlapping periods
* needs only one CPU core
* main problem: interruptions

### Parallelism
* needs more than one CPU core
* main problem: isolation


## Concurrency and parallelism in Python

* processes
* threads
* coroutines

### `multiprocessing` package

```python
from multiprocessing import Process, Pipe
import time
 
 
def worker(name, conn):
    while True:
        cmd = conn.recv()
        print("{} received {}".format(name, cmd))
        if cmd == "quit":
            return
        else:
            conn.send("{} accepted {}".format(name, cmd))
        time.sleep(1)
 
 
def main():
    parent_conn, child_conn = Pipe()
 
    p = Process(target=worker, args=("Worker", child_conn))
    p.start()
 
    for i in range(10):
        parent_conn.send("command {}".format(i))
        print(parent_conn.recv())
 
    parent_conn.send("quit")
 
    p.join()
 
 
if __name__ == '__main__':
    main()
```

### `threading` package

```python
import threading
import time
 
 
def worker(threadName, delay, n):
    for counter in range(1, n+1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(threadName, counter, n, time.ctime(time.time())))
 
 
threading.Thread(target=worker, args=("Thread-1", 0.5, 10)).start()
threading.Thread(target=worker, args=("Thread-2", 1.0, 10)).start()
threading.Thread(target=worker, args=("Thread-3", 1.5, 10)).start()
```

### Queues to communicate between threads

* "Don't communicate by sharing memory, share memory by communicating"

* Queue
* LifoQueue
* PriorityQueue
* SimpleQueue

### Producer-consumer based on threads and queue

```python
import time
import threading
import queue
 
 
q = queue.Queue()
 
 
def producer():
    name = threading.current_thread().name
    for job in range(10):
        print(f'{name} thread: Starting producing {job}')
        q.put(job)
        time.sleep(0.3)
        print(f'{name} thread: Produced {job}')
 
 
def consumer():
    name = threading.current_thread().name
    while True:
        job = q.get()
        print(f'{name} thread: Starting consuming {job}')
        time.sleep(0.4)
        print(f'{name} thread: Consumed {job}')
        q.task_done()
 
 
threading.Thread(target=consumer, daemon=True, name="1st").start()
threading.Thread(target=consumer, daemon=True, name="2nd").start()
threading.Thread(target=consumer, daemon=True, name="3rd").start()
 
threading.Thread(target=producer, daemon=True, name="1st").start()
threading.Thread(target=producer, daemon=True, name="2nd").start()
threading.Thread(target=producer, daemon=True, name="3rd").start()
threading.Thread(target=producer, daemon=True, name="3rd").start()
 
q.join()
print('Done')
```

### Pool of threads and processes

### `ThreadPoolExecutor`

```python
from concurrent.futures.thread import ThreadPoolExecutor
import time
 
 
def worker(threadName, delay, n):
    for counter in range(1, n + 1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(threadName, counter, n, time.ctime(time.time())))
 
 
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(worker, "Thread-1", 0.5, 10)
    executor.submit(worker, "Thread-2", 1.0, 10)
    executor.submit(worker, "Thread-3", 1.5, 10)
 
 
print("Done!")
```

### `ProcessPoolExecutor`

```python
from concurrent.futures import ProcessPoolExecutor
import time
 
 
def worker(processName, delay, n):
    for counter in range(1, n + 1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(processName, counter, n, time.ctime(time.time())))
 
 
with ProcessPoolExecutor(max_workers=3) as executor:
    executor.submit(worker, "Process-1", 0.5, 10)
    executor.submit(worker, "Process-2", 1.0, 10)
    executor.submit(worker, "Process-3", 1.5, 10)
 
 
print("Done!")
```

## Coroutines in Python

### `asyncio`


```python
import asyncio
import time
 
 
async def task(name):
    print(f"{name} task started")
    await asyncio.sleep(5)
    print(f"{name} task finished")
    return name[::-1]
 
 
async def main():
    task1 = asyncio.create_task(task("first"))
    print("first task created")
 
    task2 = asyncio.create_task(task("second"))
    print("second task created")
 
    task3 = asyncio.create_task(task("third"))
    print("third task created")
 
    print("result of task #1:", await task1)
    print("result of task #2:", await task2)
    print("result of task #3:", await task3)
 
    print("done")
 
 
asyncio.run(main())
```

### `asyncio` and queues

```python
import asyncio
import time
 
 
async def task(name, queue):
    while not queue.empty():
        param = await queue.get()
        print(f"Task named {name} started with parameter {param}")
        await asyncio.sleep(5)
        print(f"{name} task finished")
 
 
async def main():
    queue = asyncio.Queue()
 
    for i in range(20):
        await queue.put(i)
 
    for n in range(1, 2):
        asyncio.create_task(task(f"{n}", queue))
 
 
asyncio.run(main())
```

### `aiohttp`

```python
import asyncio
import aiohttp
import time
 
 
async def download(name, queue):
    async with aiohttp.ClientSession() as session:
        while not queue.empty():
            url = await queue.get()
            print(f"Task named {name} getting URL: {url}")
            async with session.get(url) as response:
                t = await response.text()
                print(f"Task named {name} downloaded {len(t)} characters")
            print(f"Task named {name} finished")
 
 
async def main():
    queue = asyncio.Queue()
 
    for url in (
        "http://www.root.cz",
        "http://duckduckgo.com",
        "http://seznam.com",
        "https://www.root.cz/programovaci-jazyky/",
        "https://www.root.cz/clanky/soubezne-a-paralelne-bezici-ulohy-naprogramovane-v-pythonu/",
        "https://github.com/"
    ):
        await queue.put(url)
 
    await asyncio.gather(
            asyncio.create_task(download(1, queue)),
            asyncio.create_task(download(2, queue)))
 
 
asyncio.run(main())
```

### Concurrency in `aiohttp`

```python
import aiohttp
import time
 
 
async def download(name, queue, results):
    async with aiohttp.ClientSession() as session:
        while not queue.empty():
            url = await queue.get()
            t1 = time.time()
            print(f"Task named {name} getting URL: {url}")
            async with session.get(url) as response:
                t = await response.text()
                t2 = time.time()
                print(f"Task named {name} downloaded {len(t)} characters in {t2-t1} seconds")
                await results.put(t2-t1)
            print(f"Task named {name} finished")
 
 
async def main():
    queue = asyncio.Queue()
    results = asyncio.Queue()
 
    t1 = time.time()
 
    for url in (
        "http://www.root.cz",
        "http://duckduckgo.com",
        "http://seznam.com",
        "https://www.root.cz/programovaci-jazyky/",
        "https://www.root.cz/clanky/soubezne-a-paralelne-bezici-ulohy-naprogramovane-v-pythonu/",
        "https://www.root.cz/clanky/pywebio-interaktivni-webove-dialogy-a-formulare-v-cistem-pythonu/",
        "https://streamlit.io/",
        "https://pglet.io/",
        "https://www.root.cz/serialy/graficke-uzivatelske-rozhrani-v-pythonu/",
        "https://github.com/"
    ):
        await queue.put(url)
 
    await asyncio.gather(
            asyncio.create_task(download(1, queue, results)),
            asyncio.create_task(download(2, queue, results)),
            asyncio.create_task(download(3, queue, results)))
 
    process_time = 0
    while not results.empty():
        process_time += await results.get()
 
    print(f"Process time: {process_time} seconds")
 
    t2 = time.time()
    print(f"Total time:   {t2-t1} seconds")
 
asyncio.run(main())
```

* 3 coroutines

```
Task named 1 getting URL: http://www.root.cz
Task named 2 getting URL: http://duckduckgo.com
Task named 3 getting URL: http://seznam.com
Task named 2 downloaded 5775 characters in 0.31725001335144043 seconds
Task named 2 finished
Task named 2 getting URL: https://www.root.cz/programovaci-jazyky/
Task named 3 downloaded 1555 characters in 0.43852806091308594 seconds
Task named 3 finished
Task named 3 getting URL: https://www.root.cz/clanky/soubezne-a-paralelne-bezici-ulohy-naprogramovane-v-pythonu/
Task named 1 downloaded 249707 characters in 0.535081148147583 seconds
Task named 1 finished
Task named 1 getting URL: https://www.root.cz/clanky/pywebio-interaktivni-webove-dialogy-a-formulare-v-cistem-pythonu/
Task named 2 downloaded 251515 characters in 0.3788483142852783 seconds
Task named 2 finished
Task named 2 getting URL: https://streamlit.io/
Task named 1 downloaded 235679 characters in 0.2868804931640625 seconds
Task named 1 finished
Task named 1 getting URL: https://pglet.io/
Task named 3 downloaded 236045 characters in 0.41786885261535645 seconds
Task named 3 finished
Task named 3 getting URL: https://www.root.cz/serialy/graficke-uzivatelske-rozhrani-v-pythonu/
Task named 2 downloaded 444341 characters in 0.3120858669281006 seconds
Task named 2 finished
Task named 2 getting URL: https://github.com/
Task named 1 downloaded 10145 characters in 0.21546196937561035 seconds
Task named 1 finished
Task named 3 downloaded 263683 characters in 0.29593372344970703 seconds
Task named 3 finished
Task named 2 downloaded 209173 characters in 0.28455424308776855 seconds
Task named 2 finished
Process time: 3.482492685317993 seconds
Total time:   1.2949903011322021 seconds
```

* 10 coroutines

```python
Task named 1 getting URL: http://www.root.cz
Task named 2 getting URL: http://duckduckgo.com
Task named 3 getting URL: http://seznam.com
Task named 4 getting URL: https://www.root.cz/programovaci-jazyky/
Task named 5 getting URL: https://www.root.cz/clanky/soubezne-a-paralelne-bezici-ulohy-naprogramovane-v-pythonu/
Task named 6 getting URL: https://www.root.cz/clanky/pywebio-interaktivni-webove-dialogy-a-formulare-v-cistem-pythonu/
Task named 7 getting URL: https://streamlit.io/
Task named 8 getting URL: https://pglet.io/
Task named 9 getting URL: https://www.root.cz/serialy/graficke-uzivatelske-rozhrani-v-pythonu/
Task named 10 getting URL: https://github.com/
Task named 8 downloaded 10145 characters in 0.2201550006866455 seconds
Task named 8 finished
Task named 10 downloaded 209167 characters in 0.26105284690856934 seconds
Task named 10 finished
Task named 7 downloaded 444341 characters in 0.31197690963745117 seconds
Task named 7 finished
Task named 2 downloaded 5775 characters in 0.3665473461151123 seconds
Task named 2 finished
Task named 4 downloaded 252883 characters in 0.41240453720092773 seconds
Task named 4 finished
Task named 9 downloaded 265455 characters in 0.41875481605529785 seconds
Task named 9 finished
Task named 3 downloaded 1555 characters in 0.46982383728027344 seconds
Task named 3 finished
Task named 6 downloaded 235728 characters in 0.4692232608795166 seconds
Task named 6 finished
Task named 1 downloaded 250629 characters in 0.4968068599700928 seconds
Task named 1 finished
Task named 5 downloaded 236190 characters in 0.5269002914428711 seconds
Task named 5 finished
Process time: 3.953645706176758 seconds
Total time:   0.529677152633667 seconds
```

### `trio` library

```python
import trio
 
 
async def task():
    print("task started")
    await trio.sleep(5)
    print("task finished")
 
 
def main():
    print("main started")
    trio.run(task)
    print("done")
 
 
main()
```

* "Structured concurrency"
    - like structured programming vs. GOTO

```python
import trio
 
 
async def task(name, n, s):
    print(f"{name} task started")
 
    for i in range(n):
        print(f"{name} {i+1}/{n}")
        await trio.sleep(s)
 
    print(f"{name} task finished")
 
 
async def main():
    print("main started")
    async with trio.open_nursery() as nursery:
        nursery.start_soon(task, "1st", 10, 1)
        nursery.start_soon(task, "2nd", 10, 1)
        nursery.start_soon(task, "3rd", 10, 1)
    print("done")
 
 
trio.run(main)
```

* Multi-errors
    - very important in practise

```python
import trio
 
 
async def task1():
    dct = {}
    return dct["foo"]
 
 
async def task2():
    l = []
    return l[10]
 
 
async def task3():
    x = 0
    return 1/x
 
 
async def main():
    print("main started")
    async with trio.open_nursery() as nursery:
        nursery.start_soon(task1)
        nursery.start_soon(task2)
        nursery.start_soon(task3)
    print("done")
 
 
trio.run(main)
```

### Limits

* 10000 processes -> a big problem
* 10000 threads -> a big problem
* 10000 coroutines -> not a problem

```python
import trio
 
 
async def task(name, n, s):
    print(f"{name} task started")
 
    for i in range(n):
        print(f"{name} {i+1}/{n}")
        await trio.sleep(s)
 
    print(f"{name} task finished")
 
 
async def main():
    print("main started")
    async with trio.open_nursery() as nursery:
        for i in range(10000):
            nursery.start_soon(task, f"Task {i}", 1, 10000)
    print("done")
 
 
trio.run(main)
```

```
$ ps ax |grep python
    614 ?        Ss     0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
   4410 ?        S      0:59 /usr/bin/python3 /usr/share/system-config-printer/applet.py
   4428 ?        S      0:00 python3 /usr/lib/blueberry/safechild /usr/sbin/rfkill event
3049130 pts/2    Ss+    0:00 python3 trio_11.py
3049132 pts/3    S+     0:00 grep --color=auto python
```

```
$ pmap 3049130
3049128:   python3 trio_11.py
 
00007fa95aed5000     28K r--s- gconv-modules.cache
00007fa95aedc000      4K r---- ld-2.31.so
00007fa95aedd000    140K r-x-- ld-2.31.so
00007fa95af00000     32K r---- ld-2.31.so
00007fa95af09000      4K r---- ld-2.31.so
00007fa95af0a000      4K rw--- ld-2.31.so
00007fa95af0b000      4K rw---   [ anon ]
00007fff488fe000    132K rw---   [ stack ]
00007fff489f8000     12K r----   [ anon ]
00007fff489fb000      4K r-x--   [ anon ]
ffffffffff600000      4K --x--   [ anon ]
 total            87168K
```

### Producent-consumer in Trio

```python
import trio
 
 
async def producer(send_channel):
    for i in range(1, 10):
        message = f"message {i}"
        print(f"Producer: {message}")
        await send_channel.send(message)
 
 
async def consumer(receive_channel):
    async for value in receive_channel:
        print(f"Consumer: received{value!r}")
        await trio.sleep(1)
 
 
async def main():
    async with trio.open_nursery() as nursery:
        send_channel, receive_channel = trio.open_memory_channel(0)
        nursery.start_soon(producer, send_channel)
        nursery.start_soon(consumer, receive_channel)
 
 
trio.run(main)
```

## Stay tuned...

## Useful links

* [Concurrency vs Parallelism: The Main Differences](https://oxylabs.io/blog/concurrency-vs-parallelism)
* [What is the difference between concurrency and parallelism?](https://iamsorush.com/posts/concurrent-vs-parallel/)
* [Souběžné a paralelně běžící úlohy naprogramované v Pythonu](https://www.root.cz/clanky/soubezne-a-paralelne-bezici-ulohy-naprogramovane-v-pythonu/)
* [Souběžné a paralelně běžící úlohy naprogramované v Pythonu (2)](https://www.root.cz/clanky/soubezne-a-paralelne-bezici-ulohy-naprogramovane-v-pythonu-2/)
* [Souběžné a paralelně běžící úlohy naprogramované v Pythonu – Curio a Trio](https://www.root.cz/clanky/soubezne-a-paralelne-bezici-ulohy-naprogramovane-v-pythonu-curio-a-trio/)
* [Souběžné a paralelně běžící úlohy naprogramované v Pythonu – knihovna Trio](https://www.root.cz/clanky/soubezne-a-paralelne-bezici-ulohy-naprogramovane-v-pythonu-knihovna-trio/)
* [Souběžné a paralelně běžící úlohy naprogramované v Pythonu – knihovna Trio (2)](https://www.root.cz/clanky/soubezne-a-paralelne-bezici-ulohy-naprogramovane-v-pythonu-knihovna-trio-2/)
