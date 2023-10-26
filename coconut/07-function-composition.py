(print)((hex)((abs)((ord)("B"))))

(print)((_coconut_forward_compose(ord, abs, hex))("B"))

(print)((sum)((reversed)(range(11))))

(print)((_coconut_forward_compose(reversed, sum))(range(11)))

@_coconut_tco
def evens(sequence):
    return _coconut_tail_call(filter, lambda x: x % 2 == 0, sequence)

(print)((_coconut_forward_compose(evens, sum))([1, 2, 3, 4, 5, 6, 30]))

