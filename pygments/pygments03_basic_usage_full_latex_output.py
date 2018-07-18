from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import LatexFormatter

code = """
for i in range(1, 11):
    print("Hello world!")
"""

print(highlight(code, PythonLexer(), LatexFormatter()))
