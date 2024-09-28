from pygments import highlight
from pygments.filters import NameHighlightFilter
from pygments.formatters import TerminalFormatter
from pygments.lexer import RegexLexer
from pygments.token import *


class FooLangLexer(RegexLexer):
    name = "foolang"
    aliases = ["foolang"]
    filenames = ["*.foolang"]

    tokens = {
        "root": [
            (r"\ *print", Name.Function),
            (r"for", Keyword),
            (r"while", Keyword),
            (r"goto", Generic.Error),
            (r"begin", Keyword),
            (r"end", Keyword),
            (r".+", Generic.Normal),
        ]
    }


code = """
for i in range(1, 11)
begin
    print("Hello world!")
end

while i < 10
begin
    inc i
    print(i)
end

goto 10
"""


print(highlight(code, FooLangLexer(), TerminalFormatter()))
