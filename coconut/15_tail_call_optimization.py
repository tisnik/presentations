#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x8f8983fe

# Compiled with Coconut version 1.3.0 [Dead Parrot]

# Coconut Header: -------------------------------------------------------------


# Compiled Coconut: -----------------------------------------------------------


@_coconut_tco
def factorial_tco(n, acc=1):
    def _coconut_mock_func(n, acc=1):
        return n, acc

    while True:
        _coconut_match_to = n
        _coconut_match_check = False
        if _coconut_match_to == 0:
            _coconut_match_check = True
        if _coconut_match_check:
            return acc
        if not _coconut_match_check:
            if _coconut_match_to == 1:
                _coconut_match_check = True
            if _coconut_match_check:
                return acc
        if not _coconut_match_check:
            if _coconut.isinstance(_coconut_match_to, int):
                _coconut_match_check = True
            if _coconut_match_check and not (n > 1):
                _coconut_match_check = False
            if _coconut_match_check:
                if factorial_tco is _coconut_recursive_func_0:
                    n, acc = _coconut_mock_func(n - 1, acc * n)
                    continue
                else:
                    return _coconut_tail_call(factorial_tco, n - 1, acc * n)
        if not _coconut_match_check:
            raise TypeError("expecting integer >= 0")

        return None


_coconut_recursive_func_0 = factorial_tco
for n in range(11):
    print("{n}!={f}".format(n=n, f=factorial_tco(n)))

print(factorial_tco(1000))
print(factorial_tco(10000))
