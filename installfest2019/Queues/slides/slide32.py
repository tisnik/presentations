
Publisher pro RabbitMQ a Pika
-------------------------------
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
