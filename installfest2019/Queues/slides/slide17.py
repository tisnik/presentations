
Redis Queue (RQ) - "padající" worker
------------------------------------
▶ Worker může vyhodit výjimku a být ukončen 
    ◆ Platí pro jednu úlohu
▶ Můžeme si to vyzkoušet
  
from time import sleep
  
  
def do_work():
    print("Working")
    sleep(2)
    # výjimka je zachycena až samotným systémem RQ
    assert False
    print("Done")
