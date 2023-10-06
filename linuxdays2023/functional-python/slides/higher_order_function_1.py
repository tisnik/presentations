#
# Funkce vyššího řádu vracející jinou funkci
#

def foo():
    def bar():
        print("BAR")
    return bar

x = foo()
x()
