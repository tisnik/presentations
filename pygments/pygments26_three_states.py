from pygments import highlight
from pygments.filters import NameHighlightFilter
from pygments.formatters import RawTokenFormatter, TerminalFormatter
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
            (r"def function ", Keyword, "function_name"),
            (r".+", Generic.Normal),
            (r"\n", Generic.Normal),
        ],
        "function": [
            (r"end function", Keyword, "#pop:2"),
            (r".+", Comment),
            (r"\n", Comment),
        ],
        "function_name": [
            (r"[A-Za-z]+", Name.Function, "function"),
            (r".+", Comment),
            (r"\n", Comment),
        ],
    }


code = """
for i in range(1, 11)
begin
    print("Hello world!")
end

def function Foo
    for i in range(5):
        print("hello world!")
end function

while i < 10
begin
    inc i
    print(i)
end

def function Bar
    for i in range(5):
        print("hello world!")
end function

goto 10
"""


print(highlight(code, FooLangLexer(), TerminalFormatter()))
input()

tokens = highlight(code, FooLangLexer(), RawTokenFormatter())

tokens = tokens.decode()

for token in tokens.split("\n"):
    foobar = token.split("\t")
    if len(foobar) == 2:
        print("{token:30}    {value}".format(token=foobar[0], value=foobar[1]))
