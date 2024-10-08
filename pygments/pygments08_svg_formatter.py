from pygments import highlight
from pygments.formatters import SvgFormatter
from pygments.lexers import PythonLexer

code = """
for i in range(1, 11):
    print("Hello world!")
"""

print(highlight(code, PythonLexer(), SvgFormatter()))
