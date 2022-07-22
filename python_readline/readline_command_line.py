import readline


def show_help():
    print(
        """Help
--------
quit - quit this application
exit - exit from this application
eval - evaluate
"""
    )


while True:
    cmd = input("Command: ")
    if cmd in {"q", "quit", "Quit", "exit", "Exit"}:
        break
    elif cmd in {"help", "Help", "?"}:
        show_help()
    elif cmd == "eval":
        print("42")
