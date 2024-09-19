from pygments import highlight
from pygments.formatters import Terminal256Formatter
from pygments.lexers import PythonLexer

code = """
for i in range(1, 11):
    print("Hello world!")
"""

print(highlight(code, PythonLexer(), Terminal256Formatter()))
