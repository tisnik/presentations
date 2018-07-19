from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter
from pygments.filters import VisibleWhitespaceFilter

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
