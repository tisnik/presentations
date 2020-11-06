# Nástroje implementující fronty zpráv

* Autor    Pavel Tišnovský, Red Hat
* Email    <ptisnovs 0x40 redhat 0x2e com>
* Datum    2019-03-01

## Obsah přednášky

* Message broker a fronty zpráv
* Proč vlastně používat tuto technologii?
* Modifikace architektury aplikací
* Základní komunikační strategie
* Protokoly
* Vybrané implementace message brokerů
    - Redis Queue (RQ)
    - RabbitMQ
    - Apache Active MQ
    - Celery
* Message queuing service(s)
* Další užitečné technologie

## Message broker a fronty zpráv

* Message broker
    - Aplikace či služba zajišťující přenos zpráv mezi zdroji a příjemci
    - Typicky podporuje fronty zpráv a témata (topic)
    - Další operace
        - Persistence zpráv
        - Ověření identity
        - Práva k přístupu ke frontám a zprávám atd.
        - Uživatelské rozhraní pro sledování činnosti brokera
        - Programové rozhraní  -//-
        - Škálování
* Message queue (fronta zpráv)
    - Součást message brokera
    - Front bývá více, jsou pojmenované
    - Dvě základní operace
        - Enqueue
        - Dequeue (neplést s deque - oboustrannou frontou)
    - Speciální případy
        - Prioritní fronty
        - DLQ (Dead Letter Queue)
        - Zprávy s časem, kdy má být zpráva doručena
        - Zprávy s časem zahození v případě nedoručení

## Topic (téma)

* Topic (téma)
    - Použito při komunikaci PUB-SUB
    - Většinou textové návěští přiřazené zprávě
    - Může být hierarchické
        - region.téma.podtéma
        - region/téma/podtéma
        - atd.
    - Některé systému umožňují deklarovat pravidla pro směrování zpráv
        - routing na základě hlavičky, tématu, klíče...

## Další často používané termíny v oboru MQ

* Publisher
    - Zdroj zpráv
    - Může zprávy posílat do několika front a/nebo témat
* Subscriber
    - Příjemce zpráv
    - Může zprávy přijímat z několika front a/nebo témat
* Úlohy
    - Task
    - Job
    - Termín používaný ve chvíli, kdy zprávy obsahují "příkaz k práci"
* Worker
    - Termín používaný pro příjemce úloh

## Proč vůbec používat tuto technologii?

* Minimálně deset důvodů
    - Asynchronní komunikace
    - Oddělení jednotlivých modulů aplikace
    - Možnost jasné (a centralizované) definice toku dat
    - Garance doručení posílaných zpráv
        - (popř. zajištění jejich perzistence)
    - Garance pořadí zpráv
    - Odolnost architektury vůči výpadkům (resiliency)
    - Škálovatelnost
    - Možnost snadné redundance některých částí
    - Pružné reakce na změny zatížení systému (e-shopy)
    - Funkce vyrovnávací paměti

## Modifikace architektury aplikací

* Možnost oddělení jednotlivých modulů
    - Původní vazby M:N
        - Někdy "mesh"
        - Problémy vznikají ve chvíli, kdy nějaký uzel přestane komunikovat
    - Po zavedení message brokera M:1 a 1:N
        - Producenti ⇒ Message broker ⇒ Konzumenti
        - DLQ
        - Opakované doručení zprávy atd.

## Základní komunikační strategie

* PUSH-PULL
    - Zprávy se posílají do zvolené fronty
        - Jeden či více zdrojů zpráv
        - Fronty bývají jednoznačně pojmenované
    - K výstupu fronty se může připojit více workerů
    - Zpráva je doručena jednomu z nich
        - Typicky se používá nějaká forma algoritmu round-robin
    - Pokud žádný worker nemůže zprávu zpracovat, zůstane ve frontě
    - (Nezpracované zprávy se mohou přesunout do jiné fronty - DLQ)
* PUB-SUB
    - Zprávy se posílají s udáním takzvaného tématu (topic)
        - Jeden či více zdrojů zpráv
        - Témata buď prosté jméno či hierarchie
            - `cz.eshop-brno.pokladna1`
            - `us.eshop-nyc.pokladna42`
    - K výstupu fronty se může připojit více příjemců
    - Zpráva je doručena všem aktuálně připojeným příjemcům
    - Pokud žádný příjemce nemůže zprávu zpracovat bude ztracena

## Příklady použití komunikačních strategií

* PUSH-PULL
    - Typická business logika
        - Objednávky
        - Potvrzovací maily
        - B2B
    - Jenkins CI
        - a podobně koncipované systémy
* PUB-SUB
    - IoT čidla
    - Aktuální stav (či změna stavu) nějakého systému
        - Tímto způsobem lze získat informace z AMQ
        - (viz další slajdy)
    - Podobné některým komunikačním protokolům (IRC)
* Kombinace předchozích strategií
* Pipeline

## Protokoly používané pro komunikaci

* AMQP
    - Advanced Message Queuing Protocol
    - binární formát
    - podpora SASL a TLS
* STOMP
    - Streaming Text Oriented Messaging Protocol
    - inspirován protokolem HTTP
        - (hlavičky atd.)
    - velmi jednoduchá implementace klienta
    - je možné otestovat například i v telnetu
    - podpora transakcí
* MQTT
    - Message Queuing Telemetry Transport)
    - používán v oblasti IoT

## Další protokoly používané pro komunikaci

* CoAP
    - Constrained Application Protocol
* WAMP
    - Web Application Messaging Protocol
    - založeno na WebSocketech
    - Publish-Subscribe
    - RPC
* (XMPP)
    - extensible Message Oriented Middleware
    - xMOM

## STOMP

* Samotné příkazy posílané ve formě plain textu
* Data (zprávy) mohou být binární
* Pouze několik typů zpráv
    - `CONNECT`
    - `SEND`
    - `SUBSCRIBE`
    - `UNSUBSCRIBE`
    - `BEGIN`
    - `COMMIT`
    - `ABORT`
    - `ACK`
    - `NACK`
    - `DISCONNECT`

## Vybrané implementace message brokerů

* Redis Queue (RQ)
* RabbitMQ
* Apache Active MQ (AMQ)
* Celery
* (další užitečné technologie)

## Redis Queue (RQ)

* Postaveno nad databází Redis
    - Strategie PUSH-PULL
    - Producenti ⇒ Message broker ⇒ Konzumenti
* Pravděpodobně nejjednodušší cesta k využití message brokerů
* Balíček `rq` dostupný na PyPI
* CLI nástroj nazvaný taktéž `rq`
    - Spuštění workera
    - Pozastavení všech workerů
    - Znovuspuštění úloh, které nebyly dokončeny
    - Vymazání úloh z vybrané fronty
    - Zobrazení stavu úloh

## Redis Queue (RQ) - vytvoření úlohy

```python
from redis import Redis
from rq import Queue
  
from worker import do_work
  
  
q = Queue(connection=Redis())
  
for i in range(10):
    result = q.enqueue(do_work, i)
    print(result)
```

## Redis Queue (RQ) - implementace workera

```python
from time import sleep
  
  
def do_work(param):
    print("Working, received parameter {}".format(param))
    # simulace práce :-)
    sleep(2)
    print("Done")
```

## Spuštění workera

```bash
$ rq worker
```

```
16:59:02 RQ worker 'rq:worker:localhost.32100' started, version 0.12.0
16:59:02 *** Listening on default...
16:59:02 Cleaning registries for queue: default
```

Povšimněte si použití výchozí fronty nazvané "defaut"

## Redis Queue (RQ) - "padající" worker

* Worker může vyhodit výjimku a být ukončen 
    - Platí pro jednu úlohu
* Můžeme si to vyzkoušet
  
```python
from time import sleep
  
  
def do_work():
    print("Working")
    sleep(2)
    # výjimka je zachycena až samotným systémem RQ
    assert False
    print("Done")
```

## Pád workera

* Toto chování je "očekáváno"
    - Systém jako celek se nezhroutí
    - (ostatně komu záleží na nějaké výjimce :-)

```
16:59:03 default: worker.do_work() (c5468250-e2c5-494f-8bd8-f1f51b9a81f2)
Working
16:59:05 AssertionError
Traceback (most recent call last):
  File "/home/tester/.local/lib/python3.6/site-packages/rq/worker.py", line 793, in perform_job
    rv = job.perform()
  File "/home/tester/.local/lib/python3.6/site-packages/rq/job.py", line 599, in perform
    self._result = self._execute()
  File "/home/tester/.local/lib/python3.6/site-packages/rq/job.py", line 605, in _execute
    return self.func(*self.args, **self.kwargs)
  File "./worker.py", line 7, in do_work
    assert False
AssertionError
Traceback (most recent call last):
  File "/home/tester/.local/lib/python3.6/site-packages/rq/worker.py", line 793, in perform_job
    rv = job.perform()
  File "/home/tester/.local/lib/python3.6/site-packages/rq/job.py", line 599, in perform
    self._result = self._execute()
  File "/home/tester/.local/lib/python3.6/site-packages/rq/job.py", line 605, in _execute
    return self.func(*self.args, **self.kwargs)
  File "./worker.py", line 7, in do_work
    assert False
AssertionError
16:59:05 Moving job to 'failed' queue
```

## Redis Queue (RQ) - informace o nezpracovaných úlohách

* Zhavarované úlohy se ukládají do fronty "failed"
  
```python
from redis import Redis
from rq import Queue
from time import sleep
  
from worker import do_work
  
# speciální fronta s úlohami, které nebyly dokončeny
q_failed = Queue("failed", connection=Redis())
  
print("Reading failed jobs")
  
job_ids = q_failed.job_ids
  
print(job_ids)
  
for job_id in job_ids:
    print(job_id)
    job = q_failed.fetch_job(job_id)
    # podrobnější informace o těchto úlohách
    print(job.origin)
    print(job.enqueued_at)
    print(job.started_at)
    print(job.ended_at)
    print(job.exc_info)
```

## Redis Queue (RQ) - informace o nezpracovaných úlohách

* Pamatuje se především samotný stack trace
  
```
Reading failed jobs
['62d5d473-cc31-4738-8397-7dd18b09fe64']
62d5d473-cc31-4738-8397-7dd18b09fe64
default
2018-11-28 16:24:45.094810
2018-11-28 16:24:45.103332
2018-11-28 16:24:47.107423
Traceback (most recent call last):
  File "/home/tester/.local/lib/python3.6/site-packages/rq/worker.py", line 793, in perform_job
    rv = job.perform()
  File "/home/tester/.local/lib/python3.6/site-packages/rq/job.py", line 599, in perform
    self._result = self._execute()
  File "/home/tester/.local/lib/python3.6/site-packages/rq/job.py", line 605, in _execute
    return self.func(*self.args, **self.kwargs)
  File "./worker.py", line 7, in do_work
    assert False
AssertionError
```

## Opětovné spuštění zhavarovaných úloh

```bash
$ rq requeue 
```

```
  Requeueing 1 jobs from failed queue
  [####################################]  100%
```

## Využití takzvaného burst režimu workerů

* Vybrané workery lze spustit v takzvaném burst režimu
    - takový worker se pokusí zpracovat všechny úlohy ze specifikované fronty
    - následně se ukončí
* Jedná se o koncept dávkového zpracování
    - například do systému přidáme výkonný stroj ve chvíli, kdy je nutné dokončit nějaké úlohy
    - ovšem tento stroj se nemá stát součástí „clusteru“

```bash
$ rq worker 
```

## RQ - předávání parametrů workerům

```python
from redis import Redis
from rq import Queue
  
from worker import do_work
  
  
q_low = Queue("low", connection=Redis())
q_high = Queue("high", connection=Redis())
  
  
for i in range(10):
    result = q_low.enqueue(do_work, i)
    result = q_high.enqueue(do_work, i)
    print(result)
```

## RQ - Implementace workera akceptujícího parametr

```python
from time import sleep
  
  
def do_work(param):
    print("Working, received parameter {}".format(param))
    sleep(2)
    print("Done")
```

## Zjištění stavu front

```bash
$ rq info
```
  
```
low          |██████████ 10
failed       |██ 2
default      | 0
high         |██████████ 10
4 queues, 22 jobs total
  
localhost.4312 idle: default
1 workers, 4 queues
  
Updated: 2018-11-26 13:22:06.236766
```

## Dashboard Redis Queue pro sledování stavu front a workerů

* rq-dashboard
    - Naprogramováno v Pythonu
    - Používá Flask (tj. webová aplikace)
    - (screenshot)

## RabbitMQ

* Jedna z nejúspěšnějších implementací brokera
* Vyvinut v Erlangu
    - Využívá knihovny a nástroje Open Telecom Platform
        ■ OTP
* Výhody Erlangu (nejenom) v této oblasti
    - Odolnost proti selhání
    - Vysoce dostupné aplikace
    - Distribuované systémy
    - Funkcionální paradigma

## RabbitMQ

* Rozhraní pro různé programovací jazyky (platformy)
    - Java
    - JavaScript (Node.js)
    - Python
    - Ruby
    - PHP
    - C#
    - Go
    - Elixir
    - (Java) Spring AMQP
    - Swift
    - Objective-C
    - Clojure

## RabbitMQ

* Podporované protokoly
    -  AMQP
        - verze 0-9-1
        - 0-9
        - 0-8
    -  STOMP
    -  MQTT

## RabbitMQ

* Směrování zpráv před jejich vložením do fronty
* Tzv. "exchange"
    -  (screenshot)
* Strategie
    -  Direct
        - fronta nalezena podle klíče
        - klíč je součástí zprávy
    -  Topic
        - opět se používá klíč
        - využití regulárních výrazů
        - hierarchie front atd.
    -  Headers
        - využívá hlavičky připojené ke zprávě
    -  Fanout
        - zduplikování zprávy do několika front
        - (přeposlání na různé servery)

## RabbitMQ a Python

*  Knihovna Pika
    -  Na PyPi
        - https://pypi.org/project/pika/

## Publisher pro RabbitMQ a Pika

```python
import pika
  
# připojení k serveru RabbitMQ a vytvoření komunikačního kanálu
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
  
# žádost o vytvoření či o použití fronty „test“
channel.queue_declare(queue='test')
  
# poslání zprávy se strategií direct
channel.basic_publish(exchange='',
                      routing_key='test',
                      body='Hello World!')
  
print("Sent 'Hello World!'")
# uzavření komunikace
connection.close()
```

## Subscriber pro RabbitMQ a Pika

```python
#!/usr/bin/env python
import pika
  
# připojení k serveru RabbitMQ a vytvoření komunikačního kanálu
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
  
# pokus o nové vytvoření fronty ve skutečnosti neovlivní již existující frontu
# pokud samozřejmě existuje
channel.queue_declare(queue='test')
  
  
# callback funkce volaná při přijetí zprávy
def on_receive(ch, method, properties, body):
    print("Received %r" % body)
  
  
# přihlášení se k odebírání zpráv z fronty "test"
channel.basic_consume(on_receive,
                      queue='test',
                      no_ack=True)
  
print('Waiting for messages. To exit press CTRL+C')
print("...")
  
# smyčka s odebíráním zpráv
channel.start_consuming()
```

## „Dělba práce“ mezi workery

```python
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_receive,
                      queue='test',
                      no_ack=False)
```

## Potvrzování zpráv

* Automatické

```python
channel.basic_consume(on_receive,
                      queue='test',
                      no_ack=True)
```

* Manuální

```python
channel.basic_consume(on_receive,
                      queue='test',
                      no_ack=False)
```

* Potvrzení zprávy

```python
channel.basic_ack(delivery_tag = method.delivery_tag)
```

## Manuální potvrzování zpráv v konzumentovi

```python
from time import sleep
from rabbitmq_connect import connect
  
connection, channel = connect()
  
def on_receive(ch, method, properties, body):
    print("Received %r" % body)
    sleep(5)
    print("Done processing %r" % body)
    ch.basic_ack(delivery_tag = method.delivery_tag)
  
  
channel.basic_consume(on_receive,
                      queue='test',
                      no_ack=False)
  
print('Waiting for messages. To exit press CTRL+C')
print("...")
channel.start_consuming()
```

## Příkaz `rabbitmqctl`

* Změna konfigurace serveru
* Správa clusterů
* Zjištění informací o tom, jaké fronty v daném okamžiku existují
* Zjištění, jaké jsou k dispozici směrovače (exchange)
  
```bash
$ sudo rabbitmqctl node_health_check
```
  
```
Timeout: 70.0 seconds
Checking health of node rabbit@localhost
Health check passed
```
  
```bash
$ sudo rabbitmqctl list_users
```
  
```
Listing users
guest   [administrator]
```
  
```bash
$ sudo rabbitmqctl list_queues
```
  
```
Listing queues
t3      0
testX   0
test    0
t1      2
t2      0
```
  
```bash
$ sudo rabbitmqctl list_exchanges
```
  
```
Listing exchanges
amq.topic           topic
amq.rabbitmq.log    topic
amq.headers         headers
amq.fanout          fanout
                    direct <- výchozí směrovač beze jména
amq.rabbitmq.trace  topic
amq.match           headers
amq.direct          direct
```

## Rozvětvení (fanout) zpráv do většího množství front

```python
def use_fanout(channel, exchange_name='fanout_exchange'):
    print(exchange_name)
    channel.exchange_declare(exchange=exchange_name,
                             exchange_type='fanout')
  
use_fanout(channel)
bind_queue(channel, 'fronta1')
bind_queue(channel, 'fronta2')
bind_queue(channel, 'fronta3')
```
  
```bash
$ sudo rabbitmqctl list_queues
```
  
```
Listing queues
t3      0
testX   0
test    0
t1      2
t2      0
fronta2 1
fronta1 1
fronta3 1
```

## Směrování zpráv do front na základě klíče a nakonfigurovaných výrazů

* Třetí komunikační strategie
    - Prozatím jsme si ukázali "direct" a "fanout"
* Založeno na klíči posílaném se zprávou
* Obsah klíče je porovnáván se specifickým regulárním výrazem
    - `*` - libovolné slovo
    - `#` - libovolné množství slov

```  
Výraz        Fronta
europe.*     europe_queue
asia.*       asia_queue
americas.*   americas_queue
*.org        org_queue
*.*.rabbit   rabbit_queue
#.other      other_queue
```

```python
def bind_queue(channel, queue_name, routing_pattern='', exchange_name='fanout_exchange'):
    channel.queue_declare(queue=queue_name)
    channel.queue_bind(exchange=exchange_name,
                       queue=queue_name,
                       routing_key=routing_pattern)
  
    bind_queue(channel, 'europe_queue',
               routing_pattern='europe.*', exchange_name='topic_exchange')
    bind_queue(channel, 'asia_queue',
               routing_pattern='asia.*', exchange_name='topic_exchange')
    bind_queue(channel, 'americas_queue',
               routing_pattern='americas.*', exchange_name='topic_exchange')
```

## Prioritní fronty

* Fronta musí být nastavena jako prioritní
* Zprávy s vyšší prioritou budou přesunuty směrem k začátku front
* Systém ovšem nezaručuje, že pořadí zpráv ve frontě bude přesně odpovídat zadané prioritě
* Priorita zprávy specifikována celým kladným číslem popř. nulou
    - (Tolik teorie)
    - Priorita zprávy může být reprezentována jediným bajtem.
    - Prakticky jsme tedy omezeni hodnotami ležícími v rozsahu 0 až 255
  
```python
channel.queue_declare(queue=queue_name, arguments={"x-max-priority": max_priority})
  
def open_channel(connection, queue_name='test', max_priority=10):
    # pokus o nové vytvoření fronty ve skutečnosti neovlivní již existující frontu
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, arguments={"x-max-priority": max_priority})
    return channel
```

## Specifikace priority posílané zprávy

```python
prop = BasicProperties(priority=priority)
  
channel.basic_publish(exchange='',
                      routing_key='priority_queue_2',
                      body='Hello World! #{i} msg with priority {p}'.format(i=i, p=priority),
                      properties=prop)
```

## Apache Active MQ

* Vytvořen v Javě
    - Snadná instalace (rozbalení tarballu)
* Strategie PUSH-PULL i PUB-SUB
* Sledování činnosti AMQ
    - Webové rozhraní
    - JMX (JConsole)
    - Speciální témata (eventy)

## Podporované protokoly

* AMQP 1.0
* STOMP
* MQTT
* OpenWire
* REST
* RSS a Atom
* WSIF
* WS Notification        
* XMPP

## Apache Active MQ

* Řízení AMQ
        bin/activemq
* Práce se zprávami bez implementace klientů
    - Producent
        `./activemq producer##`
        `./activemq producer##`
        `./activemq producer`
    - Konzument
        `./activemq consumer`

## Apache Active MQ + STOMP + Python

* Knihovna `stomp.py`
* Klient ovládaný z CLI: `stomp`
 
## CLI klient `stomp`

* Spuštění

```bash
$ stomp
```

```
CONNECTED
server: ActiveMQ/5.15.8
heart-beat: 0,0
session: ID:localhost.localdomain-38215-1549567803551-3:3
version: 1.1
```
   
## CLI klient `stomp`

* Poslání zprávy
```
send /queue/test hello world
```
  
```
MESSAGE
content-length: 11
expires: 0
destination: /queue/test
```

## CLI klient `stomp`

* Přihlášení se k odběru zpráv z fronty „test“:
```
subscribe /queue/test
```
   
```
Subscribing to "/queue/test" with acknowledge set to "auto", id set to "1"
subscription: 1
priority: 4
message-id: ID:localhost.localdomain-38215-1549567803551-3:3:-1:1:1
timestamp: 1549631641256
   
hello world
```

## Producent zpráv (stomp.py)

```python
#!/usr/bin/env python
   
import time
import stomp
   
   
destination1 = "/topic/event"
destination2 = "/topic/event2"
  
MESSAGES = 10
 
conn = stomp.Connection(host_and_ports=[("localhost", 61613)])
conn.start()
conn.connect(login="admin", passcode="admin")
  
  
for i in range(0, MESSAGES):
    message = "Hello world #{i}!".format(i=i)
    conn.send(destination1, message, persistent='true')
    conn.send(destination2, message, persistent='true')
 
 
conn.disconnect()
```

## Konzument zpráv (stomp.py)

```python
#!/usr/bin/env python
  
import time
import stomp
  
  
class SimpleListener:
  
    def __init__(self, conn):
        self.conn = conn
  
    def on_message(self, headers, message):
        print("Received message: {m}".format(m=message))
  
    def on_error(self, headers, message):
        print("Received an error {e}".format(e=message))
  
  
destination = "/topic/event"
  
conn = stomp.Connection(host_and_ports=[("localhost", 61613)])
conn.set_listener('', SimpleListener(conn))
conn.start()
  
conn.connect(login="admin", passcode="admin")
conn.subscribe(id='simple_listener', destination=destination, ack='auto')
  
print("Waiting for messages...")
   
while True:
    time.sleep(10)
```


## Celery

* Asynchronní fronty úloh pro Python
* Více flexibility, zejména v porovnání s Redis Queue (RQ)
* Sledování systému
* Vzdálené ovládání workerů
    - (remote control)
* Systém událostí
    - (events)
* Návaznost na různé brokery

## Brokeři podporovaní nástrojem Celery 

```
 Broker           Současný stav   Monitoring  Vzdálené ovládání workerů
 RabbitMQ         stabilní        ✓           ✓
 Redis            stabilní        ✓           ✓
 Amazon SQS       stabilní        ×           ×
 Apache Zookeeper experimentální  ×           ×
```

## Message queuing service

* "Messaging as a Service"
* Někdy je lepší použít MQ ve formě služby
* Výhody/nevýhody
    - podobné jako u dalších cloudových služeb
* AMQ Online
* IBM MQ
* Amazon Simple Queue Service
* AnypointMQ
* Oracle Messaging Cloud Service
* Microsoft Azure Service Bus
* StormMQ

## Další užitečné technologie

* 0MQ
* Nanomsg
