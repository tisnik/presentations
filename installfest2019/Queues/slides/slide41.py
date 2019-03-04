
Specifikace priority posílané zprávy
------------------------------------
prop = BasicProperties(priority=priority)
  
channel.basic_publish(exchange='',
                      routing_key='priority_queue_2',
                      body='Hello World! #{i} msg with priority {p}'.format(i=i, p=priority),
                      properties=prop)
