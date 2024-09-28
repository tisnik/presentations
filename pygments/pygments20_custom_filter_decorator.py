import re

from pygments import highlight
from pygments.filter import simplefilter
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer
from pygments.token import Name
from pygments.util import get_bool_opt


@simplefilter
def to_snake_case(self, lexer, stream, options):
    for ttype, value in stream:
        if ttype is Name.Function or ttype is Name:
            results = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", value)
            results = re.sub("([a-z0-9])([A-Z])", r"\1_\2", results)
            value = results.lower()
        yield ttype, value


code = """
for i in range(1, 11):
    print("Hello world!")

if x and y:
    print("yes")

if x or y:
    print("dunno")

globalVariable = 42

def helloWorld():
    print("Hello world!")

helloWorld()

print(globalVariable)
"""


print(highlight(code, PythonLexer(), TerminalFormatter()))

print("-----------------------")

lexer = PythonLexer()

# pridani filtru
lexer.add_filter(to_snake_case())

print(highlight(code, lexer, TerminalFormatter()))
