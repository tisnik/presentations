from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter


def show_help():
    print("""Help
--------
quit - quit this application
exit - exit from this application
eval - evaluate
""")


c = WordCompleter(["quit", "exit", "help", "eval"], ignore_case=True)
s = PromptSession(completer=c)

while True:
    try:
        cmd = s.prompt("Command: ", mouse_support=True,
                       enable_open_in_editor=True,
                       bottom_toolbar="Available commands: quit, exit, help, eval",
                       rprompt="Don't panic!")
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
