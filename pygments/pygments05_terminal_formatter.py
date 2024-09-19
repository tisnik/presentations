from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer

code = """
for i in range(1, 11):
    print("Hello world!")
"""

print(highlight(code, PythonLexer(), TerminalFormatter()))

print("-----------------------")

print(highlight(code, PythonLexer(), TerminalFormatter(linenos=True)))

print("-----------------------")

print(highlight(code, PythonLexer(), TerminalFormatter(bg="light")))

print("-----------------------")

print(highlight(code, PythonLexer(), TerminalFormatter(bg="dark")))
