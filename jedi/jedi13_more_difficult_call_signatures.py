#!/usr/bin/env python3

import jedi

src = """
def foo():
    return 0

def bar(x):
    return 1

def baz(x,y):
    return 2

foo()
bar(1)
baz(1,2)
baz(foo(), bar(1))
print(10, 20, 30, 40, 50)
print   (10, 20, 30, 40, 50)
print(

42)
"""


def print_call_signatures(script):
    call_signatures = script.call_signatures()

    for call_signature in call_signatures:
        print(
            call_signatures.__str__(),
            call_signature.index,
            call_signature.bracket_start,
        )

    print()


lines = src.count("\n")

script = jedi.Script(src, 11, len("foo("), "test.py")
print_call_signatures(script)

script = jedi.Script(src, 12, len("bar(1"), "test.py")
print_call_signatures(script)

script = jedi.Script(src, 13, len("baz(1,2"), "test.py")
print_call_signatures(script)

script = jedi.Script(src, 14, len("baz(foo(), bar(1"), "test.py")
print_call_signatures(script)

script = jedi.Script(src, 15, len("print(10, 20, 30, 40, "), "test.py")
print_call_signatures(script)

script = jedi.Script(src, 16, len("print   (10, 20, 30, 40, "), "test.py")
print_call_signatures(script)

script = jedi.Script(src, lines, 1, "test.py")
print_call_signatures(script)
