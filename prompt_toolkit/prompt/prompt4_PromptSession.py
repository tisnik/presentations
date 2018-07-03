from prompt_toolkit import PromptSession


def show_help():
    print("""Help
--------
quit - quit this application
exit - exit from this application
eval - evaluate
""")


s = PromptSession()

while True:
    cmd = s.prompt("Command: ")
    if cmd in {"q", "quit", "Quit", "exit", "Exit"}:
        break
    elif cmd in {"help", "Help", "?"}:
        show_help()
    elif cmd == "eval":
        print("42")
