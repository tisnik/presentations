from pygments import highlight
from pygments.filters import NameHighlightFilter
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer

code = """
for i in range(1, 11):
    print("Hello world!")
if x and y:
    print("yes")
if x or y:
    print("dunno")
if x xor y:
    print("different")
goto 10
"""


print(highlight(code, PythonLexer(), TerminalFormatter()))

print("-----------------------")

lexer = PythonLexer()

# pridani filtru
lexer.add_filter(NameHighlightFilter(names=["xor", "goto"]))

print(highlight(code, lexer, TerminalFormatter()))
