from pygments import lex
from pygments.token import Token
from pygments.lexers import PythonLexer

from prompt_toolkit.formatted_text import PygmentsTokens
from prompt_toolkit import print_formatted_text

code = """
for i in range(1, 10):
    print(i)
    if i > 5:
        break
    do_something(i)
"""

tokens = list(lex(code, lexer=PythonLexer()))
print_formatted_text(PygmentsTokens(tokens))
