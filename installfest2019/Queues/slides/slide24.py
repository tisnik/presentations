
RQ - Implementace workera akceptujícího parametr
------------------------------------------------
from time import sleep
  
  
def do_work(param):
    print("Working, received parameter {}".format(param))
    sleep(2)
    print("Done")
