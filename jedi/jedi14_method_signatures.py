#!/usr/bin/env python3

import jedi

src = """
class C1:
    def foo(self):
        return 0

    def bar(self, x):
        return 1

    def baz(self, x,y):
        return 2

obj = C1()
obj.foo()
obj.bar(1)
obj.baz(1,2)
obj.baz(obj.foo(), obj.bar(1))"""


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

script = jedi.Script(src, lines - 2, len("obj.foo("), "test.py")
print_call_signatures(script)

script = jedi.Script(src, lines - 1, len("obj.bar(1"), "test.py")
print_call_signatures(script)

script = jedi.Script(src, lines, len("obj.baz(1,2"), "test.py")
print_call_signatures(script)

script = jedi.Script(src, lines + 1, len("obj.baz(obj.foo(), obj.bar(1"), "test.py")
print_call_signatures(script)
