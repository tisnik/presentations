
Redis Queue (RQ) - vytvoření úlohy
----------------------------------
from redis import Redis
from rq import Queue
  
from worker import do_work
  
  
q = Queue(connection=Redis())
  
for i in range(10):
    result = q.enqueue(do_work, i)
    print(result)
