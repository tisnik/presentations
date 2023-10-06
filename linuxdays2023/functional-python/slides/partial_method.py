#
# Částečně vyhodnocená metoda
#

class Foo:
    def __init__(self):
        self._enabled = False

    def set_enabled(self, state):
        self._enabled = state

    enable = partialmethod(set_enabled, True)
    disable = partialmethod(set_enabled, False)

    def __str__(self):
        return "Foo that is " + ("enabled" if self._enabled else "disabled")
