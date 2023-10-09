#
# Čítač realizovaný uzávěrem: varianta pro Python 2
#

def createCounter():
    counter = [0]
    def next():
        counter[0] += 1
        return counter[0]
    return next
