from prompt_toolkit import PromptSession
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles import Style
from pygments.lexer import RegexLexer
from pygments.token import *


class CommandLexer(RegexLexer):
    name = "command"
    aliases = ["command"]
    filenames = ["*.command"]

    tokens = {
        "root": [
            (r"quit", Keyword),
            (r"exit", Keyword),
            (r"help", Keyword),
            (r"eval", Keyword),
            (r".+", Generic.Error),
        ]
    }


def show_help():
    print(
        """Help
--------
quit - quit this application
exit - exit from this application
eval - evaluate
"""
    )


new_tui_style = Style.from_dict(
    {
        "rprompt": "bg:#ff0066 #ffffff",
        "bottom-toolbar": "bg:#ffffff #333333 reverse",
        "prompt": "bg:#ansiyellow #000000",
    }
)


s = PromptSession()

while True:
    try:
        cmd = s.prompt(
            "Command: ",
            validate_while_typing=True,
            enable_open_in_editor=True,
            bottom_toolbar="Available commands: quit, exit, help, eval",
            rprompt="Don't panic!",
            style=new_tui_style,
            lexer=PygmentsLexer(CommandLexer),
        )
        if cmd in {"q", "quit", "Quit", "exit", "Exit"}:
            break
        elif cmd in {"help", "Help", "?"}:
            show_help()
        elif cmd == "eval":
            print("42")
    except KeyboardInterrupt:
        continue
    except EOFError:
        break
