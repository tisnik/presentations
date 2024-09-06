from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import PygmentsTokens
from pygments import lex
from pygments.lexers.basic import CbmBasicV2Lexer
from pygments.token import Token

code = """
10 FOR I=0 TO 63
20 FOR J=43 TO 0 STEP -1
30 LET CX=(I-52)/31
40 LET CY=(J-22)/31
50 LET ZX=0
60 LET ZY=0
70 LET ITER=0
80 LET ZX2=ZX*ZX
85 LET ZY2=ZY*ZY
90 LET ZY=2*ZX*ZY+CY
100 LET ZX=ZX2-ZY2+CX
110 LET ITER=ITER+1
120 IF ZX2+ZY2<=4 AND ITER<200 THEN GOTO 80
130 IF ITER=200 THEN PLOT I, J
140 NEXT J
150 NEXT I
"""

tokens = list(lex(code, lexer=CbmBasicV2Lexer()))
print_formatted_text(PygmentsTokens(tokens))
