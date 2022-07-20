# Compiled Coconut: -----------------------------------------------------------

(print)((abs)(-42))  # line 1

(print)((hex)((abs)((ord)("B"))))  # line 3

(print)((sum)(range(11)))  # line 5

(print)((sum)((reversed)(range(11))))  # line 7


@_coconut_tco  # line 9
def evens(sequence):  # line 9
    return _coconut_tail_call(filter, lambda x: x % 2 == 0, sequence)  # line 10


(print)((sum)((evens)([1, 2, 3, 4, 5, 6, 30])))  # line 12
