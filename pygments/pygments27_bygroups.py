import re

from pygments import highlight
from pygments.filters import NameHighlightFilter
from pygments.formatters import Terminal256Formatter
from pygments.lexer import *
from pygments.lexer import RegexLexer, bygroups
from pygments.style import Style
from pygments.token import *


# viz http://pygments.org/docs/lexerdevelopment/
class IniFileLexer(RegexLexer):
    name = "INI"
    aliases = ["ini", "cfg"]
    filenames = ["*.ini", "*.cfg"]

    tokens = {
        "root": [
            (r"\s+", Text),
            (r";.*?$", Comment),
            (r"\[.*?\]$", Keyword),
            (
                r"(.*?)(\s*)(=)(\s*)(.*?)$",
                bygroups(Name.Attribute, Text, Operator, Text, String),
            ),
        ]
    }


code = """
; komentar

[sekce]
x=10
y=20

[dalsi-sekce]
foo=bar
"""


class NewStyle(Style):
    default_style = ""
    styles = {
        Comment: "#888",
        Text: "#ansired",
        Keyword: "#88f",
        Name.Attribute: "nobold #ansiyellow",
    }


print(highlight(code, IniFileLexer(), Terminal256Formatter(style=NewStyle)))
