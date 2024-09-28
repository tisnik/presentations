import readline

WORDS = ("quit", "exit", "eval", "help")


def completer(text, state):
    # print(text, state)
    matches = []
    n = len(text)
    for word in WORDS:
        if text == word[:n]:
            matches.append(word)
    if len(matches) >= state:
        return matches[state]
    else:
        return None


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
