from pygments import highlight
from pygments.formatters import Terminal256Formatter
from pygments.lexers import PythonLexer
from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Generic,
    Keyword,
    Name,
    Number,
    Operator,
    String,
)

code = """
for i in range(1, 11):
    print("Hello world!")
"""

print(highlight(code, PythonLexer(), Terminal256Formatter()))

print("-----------------------")


class NewStyle(Style):
    default_style = ""
    styles = {
        Comment: "italic #888",
        Keyword: "underline #f00",
        Name.Builtin: "bold #ff0",
        String: "#0f0 bg:#232",
    }


print(highlight(code, PythonLexer(), Terminal256Formatter(style=NewStyle)))
