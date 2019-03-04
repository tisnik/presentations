
Manuální potvrzování zpráv v konzumentovi
-----------------------------------------
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
