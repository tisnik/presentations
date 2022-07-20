# Compiled Coconut: -----------------------------------------------------------

(print)((abs)(-42))  # line 1: -42 |> abs |> print

(print)((hex)((abs)((ord)("B"))))  # line 3: "B" |> ord |> abs |> hex |> print

(print)((sum)(range(11)))  # line 5: range(11) |> sum |> print

(print)((sum)((reversed)(range(11))))  # line 7: range(11) |> reversed |> sum |> print


@_coconut_tco  # line 9: def evens(sequence):
def evens(sequence):  # line 9: def evens(sequence):
    return _coconut_tail_call(
        filter, lambda x: x % 2 == 0, sequence
    )  # line 10:     return filter(lambda x: x % 2 == 0, sequence)


(print)(
    (sum)((evens)([1, 2, 3, 4, 5, 6, 30]))
)  # line 12: [1, 2, 3, 4, 5, 6, 30] |> evens |> sum |> print
