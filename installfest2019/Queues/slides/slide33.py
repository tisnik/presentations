
Subscriber pro RabbitMQ a Pika
-------------------------------
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
