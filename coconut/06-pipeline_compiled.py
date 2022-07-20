# Compiled Coconut: -----------------------------------------------------------

(print)((abs)(-42))

(print)((hex)((abs)((ord)("B"))))

(print)((sum)(range(11)))

(print)((sum)((reversed)(range(11))))


@_coconut_tco
def evens(sequence):
    return _coconut_tail_call(filter, lambda x: x % 2 == 0, sequence)


(print)((sum)((evens)([1, 2, 3, 4, 5, 6, 30])))
