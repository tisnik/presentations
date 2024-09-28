from pygments import highlight
from pygments.filters import KeywordCaseFilter
from pygments.formatters import TerminalFormatter
from pygments.lexers.pascal import DelphiLexer

code = """
procedure change(s:string);
begin
  s[10]:='a';
end;

const
  c:packed array [0..1000] of char = 'staticky retezec';
var
  s1:string[10];
  s2:string;
  i:integer;
begin
  s1:='hello';
  writeln('"', s1, '"');
  s1:=s1+' world';
  writeln('"', s1, '"');
  for i:=0 to 1000 do begin
      s2:=s2+'*';
  end;
  change(s2);
  writeln(s2);
end.
"""


print(highlight(code, DelphiLexer(), TerminalFormatter()))

input()

print("-----------------------")

lexer = DelphiLexer()
lexer.add_filter(KeywordCaseFilter(case="lower"))

print(highlight(code, lexer, TerminalFormatter()))

input()

print("-----------------------")

lexer = DelphiLexer()
lexer.add_filter(KeywordCaseFilter(case="upper"))

print(highlight(code, lexer, TerminalFormatter()))

input()

print("-----------------------")

lexer = DelphiLexer()
lexer.add_filter(KeywordCaseFilter(case="capitalize"))

print(highlight(code, lexer, TerminalFormatter()))
