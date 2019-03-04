
Redis Queue (RQ) - implementace workera
---------------------------------------
from time import sleep
  
  
def do_work(param):
    print("Working, received parameter {}".format(param))
    # simulace práce :-)
    sleep(2)
    print("Done")
