from pygments import highlight
from pygments.filters import VisibleWhitespaceFilter
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer

code = """
for i in range(1, 11):
\tprint("Hello world!")
if x and y:
        print("yes")
if x or y:
\tprint("dunno")
"""


print(highlight(code, PythonLexer(), TerminalFormatter()))

print("-----------------------")

lexer = PythonLexer()
lexer.add_filter(VisibleWhitespaceFilter(tabs=True))

print(highlight(code, lexer, TerminalFormatter()))
