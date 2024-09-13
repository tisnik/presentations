from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import PygmentsTokens
from pygments.token import Token

text = [
    (Token.Keyword, "print"),
    (Token.Punctuation, "("),
    (Token.Literal.String.Double, '"'),
    (Token.Literal.String, "hello"),
    (Token.Literal.String.Double, '"'),
    (Token.Punctuation, ","),
    (Token.Text.Whitespace, " "),
    (Token.Literal.String.Single, '"'),
    (Token.Literal.String, "world"),
    (Token.Literal.String.Single, '"'),
    (Token.Punctuation, ")"),
    (Token.Text, "\n"),
]

print_formatted_text(PygmentsTokens(text))
