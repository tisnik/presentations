def foo(bar=[]):
    bar.append("baz")
    return bar


print(foo())
print(foo())
print(foo())
