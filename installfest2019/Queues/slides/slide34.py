
„Dělba práce“ mezi workery
-------------------------------
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_receive,
                      queue='test',
                      no_ack=False)
