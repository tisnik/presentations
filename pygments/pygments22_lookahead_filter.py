import itertools
import re

from pygments import highlight
from pygments.filter import simplefilter
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer
from pygments.token import Name, Punctuation
from pygments.util import get_bool_opt


def name_to_snake_case(name):
    results = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    results = re.sub("([a-z0-9])([A-Z])", r"\1_\2", results)
    return results.lower()


def is_function_call_token(current_type, next_type, next_value):
    return current_type is Name and next_type is Punctuation and next_value == "("


@simplefilter
def to_snake_case(self, lexer, stream, options):
    lookahead, tokens = itertools.tee(stream)
    next(lookahead)
    for current_token in tokens:
        current_type = current_token[0]
        current_value = current_token[1]
        next_token = next(lookahead)
        next_type = next_token[0]
        next_value = next_token[1]
        if current_type is Name.Function or is_function_call_token(
            current_type, next_type, next_value
        ):
            current_value = name_to_snake_case(current_value)
        yield current_type, current_value


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

input()
print("-----------------------")

lexer = PythonLexer()

# pridani filtru
lexer.add_filter(to_snake_case())

print(highlight(code, lexer, TerminalFormatter()))
