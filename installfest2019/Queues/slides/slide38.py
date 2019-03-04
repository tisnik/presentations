
Rozvětvení (fanout) zpráv do většího množství front
---------------------------------------------------
def use_fanout(channel, exchange_name='fanout_exchange'):
    print(exchange_name)
    channel.exchange_declare(exchange=exchange_name,
                             exchange_type='fanout')
  
use_fanout(channel)
bind_queue(channel, 'fronta1')
bind_queue(channel, 'fronta2')
bind_queue(channel, 'fronta3')
  
$ sudo rabbitmqctl list_queues
  
Listing queues
t3      0
testX   0
test    0
t1      2
t2      0
fronta2 1
fronta1 1
fronta3 1
