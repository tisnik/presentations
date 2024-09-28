import re

from pygments import highlight
from pygments.filters import NameHighlightFilter
from pygments.formatters import Terminal256Formatter
from pygments.lexer import *
from pygments.style import Style
from pygments.token import *

# odvozeno od tridy QBasicLexer
# http://pygments.org/docs/lexers/#lexers-for-basic-like-languages-other-than-vb-net


class BasicLexer(RegexLexer):
    name = "Basic"
    aliases = ["basic"]
    filenames = ["*.BAS", "*.bas"]
    mimetypes = ["text/basic"]

    declarations = ("DATA", "LET")

    functions = (
        "ABS",
        "ASC",
        "ATN",
        "COS",
        "DATE$",
        "EXP",
        "FRE",
        "INKEY$",
        "INPUT$",
        "LEN",
        "LOG",
        "PEEK",
        "SGN",
        "SIN",
        "SQR",
        "STICK",
        "STR$",
        "STRIG",
        "TAN",
        "TIME$",
        "VAL",
    )

    operators = ("AND", "OR", "XOR", "NOT")

    statements = (
        "BEEP",
        "CLEAR",
        "CLS",
        "DATA",
        "DATE$",
        "DIM",
        "PLOT",
        "DRAWTO",
        "FOR",
        "NEXT",
        "GOSUB",
        "GOTO",
        "IF",
        "THEN",
        "INPUT",
        "LET",
        "LINE",
        "POKE",
        "PRINT",
        "PRINT #",
        "PRINT USING",
        "REM",
        "RETURN",
        "RUN",
        "STOP",
        "STRIG",
        "TIME$",
    )

    tokens = {
        "root": [
            (r"\n+", Text),
            (r"\s+", Text.Whitespace),
            (
                r"^(\s*)(\d*)(\s*)(REM .*)$",
                bygroups(Text.Whitespace, Name.Label, Text.Whitespace, Comment.Single),
            ),
            (
                r"^(\s*)(\d+)(\s*)",
                bygroups(Text.Whitespace, Name.Label, Text.Whitespace),
            ),
            (r"(?=[\s]*)(\w+)(?=[\s]*=)", Name.Variable.Global),
            (r'(?=[^"]*)\'.*$', Comment.Single),
            (r'"[^\n"]*"', String.Double),
            (
                r"(DIM)(\s+)([^\s(]+)",
                bygroups(Keyword.Declaration, Text.Whitespace, Name.Variable.Global),
            ),
            (
                r"^(\s*)([a-zA-Z_]+)(\s*)(\=)",
                bygroups(
                    Text.Whitespace, Name.Variable.Global, Text.Whitespace, Operator
                ),
            ),
            (
                r"(GOTO|GOSUB)(\s+)(\w+\:?)",
                bygroups(Keyword.Reserved, Text.Whitespace, Name.Label),
            ),
            include("declarations"),
            include("functions"),
            include("operators"),
            include("statements"),
            (r"[a-zA-Z_]\w*[$@#&!]", Name.Variable.Global),
            (r"[a-zA-Z_]\w*\:", Name.Label),
            (r"\-?\d*\.\d+[@|#]?", Number.Float),
            (r"\-?\d+[@|#]", Number.Float),
            (r"\-?\d+#?", Number.Integer.Long),
            (r"\-?\d+#?", Number.Integer),
            (r"!=|==|:=|\.=|<<|>>|[-~+/\\*%=<>&^|?:!.]", Operator),
            (r"[\[\]{}(),;]", Punctuation),
            (r"[\w]+", Name.Variable.Global),
        ],
        "declarations": [
            (
                r"\b(%s)(?=\(|\b)" % "|".join(map(re.escape, declarations)),
                Keyword.Declaration,
            ),
        ],
        "functions": [
            (r"\b(%s)(?=\(|\b)" % "|".join(map(re.escape, functions)), Name.Builtin),
        ],
        "operators": [
            (r"\b(%s)(?=\(|\b)" % "|".join(map(re.escape, operators)), Operator.Word),
        ],
        "statements": [
            (r"\b(%s)\b" % "|".join(map(re.escape, statements)), Keyword.Reserved),
        ],
    }


code = """
1500 REM === DRAW a LINE. Ported from C version
1510 REM Inputs are X1, Y1, X2, Y2: Destroys value of X1, Y1
1520 DX = ABS(X2 - X1):SX = -1:IF X1 < X2 THEN SX = 1
1530 DY = ABS(Y2 - Y1):SY = -1:IF Y1 < Y2 THEN SY = 1
1540 ER = -DY
1545 IF DX > DY THEN ER = DX
1550 ER = INT(ER / 2)
1555 REM This command may differ depending ON BASIC dialect
1560 PLOT X1,Y1
1570 IF X1 = X2 AND Y1 = Y2 THEN RETURN
1580 E2 = ER
1590 IF E2 > -DX THEN ER = ER - DY:X1 = X1 + SX
1600 IF E2 < DY THEN ER = ER + DX:Y1 = Y1 + SY
1610 GOTO 1560
"""


class NewStyle(Style):
    default_style = ""
    styles = {
        Comment: "#888",
        Keyword.Declaration: "#ansired",
        Keyword.Reserved: "#88f",
        Name.Builtin: "nobold #ansiyellow",
        String: "#ansilightgray",
        Operator.Word: "#f0f",
        Name.Label: "#fff",
    }


print(highlight(code, BasicLexer(), Terminal256Formatter(style=NewStyle)))
