import readline

WORDS = ("quit", "exit", "eval", "help")


def completer(text, state):
    # print(text, state)
    if state >= 1:
        return None
    n = len(text)
    for word in WORDS:
        if text == word[:n]:
            return word
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
