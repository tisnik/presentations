import readline


def completer(text, state):
    # print(text, state)
    if state >= 1:
        return None
    if text in {"q", "qu", "qui"}:
        return "quit"
    elif text in {"e", "ex", "exi"}:
        return "exit"
    elif text in {"h", "he", "hel"}:
        return "help"
    else:
        return text


def show_help():
    print(
        """Help
--------
quit - quit this application
exit - exit from this application
eval - evaluate
"""
    )


readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

while True:
    cmd = input("Command: ")
    if cmd in {"quit", "Quit", "exit", "Exit"}:
        break
    elif cmd in {"help", "Help", "?"}:
        show_help()
    elif cmd == "eval":
        print("42")
