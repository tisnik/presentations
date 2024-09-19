from pygments import highlight
from pygments.formatters import RawTokenFormatter
from pygments.lexers import PythonLexer

code = """
range(1, "FDA") for while with i
except for for i else
    print("Hello world!")
"""

tokens = highlight(code, PythonLexer(), RawTokenFormatter())

tokens = tokens.decode()

for token in tokens.split("\n"):
    foobar = token.split("\t")
    if len(foobar) == 2:
        print("{token:30}    {value}".format(token=foobar[0], value=foobar[1]))
