from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import Terminal256Formatter
from pygments.style import Style
from pygments.token import (
    Keyword,
    Name,
    Comment,
    String,
    Error,
    Number,
    Operator,
    Generic,
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
        Comment: "italic #ansidarkgray",
        Keyword: "underline #ansired",
        Name.Builtin: "bold #ansiyellow",
        String: "#ansilightgray",
    }


print(highlight(code, PythonLexer(), Terminal256Formatter(style=NewStyle)))
