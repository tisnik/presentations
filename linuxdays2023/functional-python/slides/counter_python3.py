#
# Čítač realizovaný uzávěrem: varianta pro Python 3
#

def createCounter():
    counter = 0
    def next():
        nonlocal counter
        counter += 1
        return counter
    return next
