from pygments import highlight
from pygments.formatters import RawTokenFormatter
from pygments.lexers import PythonLexer

code = """
for i in range(1, 11):
    print("Hello world!")
"""

tokens = highlight(code, PythonLexer(), RawTokenFormatter())

tokens = tokens.decode()

for token in tokens.split("\n"):
    foobar = token.split("\t")
    if len(foobar) == 2:
        print("{token:30}    {value}".format(token=foobar[0], value=foobar[1]))
