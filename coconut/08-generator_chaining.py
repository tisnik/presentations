#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xaec2ab88

# Compiled with Coconut version 1.3.0 [Dead Parrot]

# Coconut Header: -------------------------------------------------------------

# Compiled Coconut: -----------------------------------------------------------


def generator1():
    values = ["a1", "b1", "c1", "d1"]
    for value in values:
        yield value


def generator2():
    values = ["a2", "b2", "c2", "d2"]
    for value in values:
        yield value


for v in _coconut.itertools.chain.from_iterable(
    (f() for f in (lambda: generator1(), lambda: generator2()))
):
    print(v)


def generator3(suffix):
    values = ["a", "b", "c", "d", "e"]
    for value in values:
        yield "{v}{s}".format(v=value, s=suffix)


for v in _coconut.itertools.chain.from_iterable(
    (
        f()
        for f in (
            lambda: generator3("1"),
            lambda: generator3("2"),
            lambda: generator3("3"),
        )
    )
):
    print(v)
