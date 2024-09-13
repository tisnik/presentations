from prompt_toolkit import PromptSession, enums
from prompt_toolkit.completion import WordCompleter


def show_help():
    print(
        """Help
--------
quit - quit this application
exit - exit from this application
eval - evaluate
"""
    )


c = WordCompleter(["quit", "exit", "help", "eval"], ignore_case=True)
s = PromptSession(completer=c, editing_mode=enums.EditingMode.EMACS)

while True:
    cmd = s.prompt("Command: ")
    if cmd in {"quit", "Quit", "exit", "Exit"}:
        break
    elif cmd in {"help", "Help", "?"}:
        show_help()
    elif cmd == "eval":
        print("42")
