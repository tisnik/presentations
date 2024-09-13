from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.validation import ValidationError, Validator


def show_help():
    print(
        """Help
--------
quit - quit this application
exit - exit from this application
eval - evaluate
"""
    )


class CommandValidator(Validator):
    def validate(self, document):
        user_input = document.text

        if user_input and not user_input.isalpha():
            index = 0

            for index, char in enumerate(user_input):
                if not char.isalpha():
                    break

            msg = "Wrong character '{c}' on index {i}".format(c=char, i=index + 1)
            raise ValidationError(message=msg, cursor_position=index)


def get_user_input(prompt_session):
    # nejprve ziskame objekt typu Buffer
    buffer = prompt_session.default_buffer
    # z bufferu ziskame objekt typu Document
    document = buffer.document
    # ktery obsahuje atribut 'text'
    return document.text


def right_prompt_callback():
    user_input = get_user_input(s)
    return "Typed {c} characters".format(c=len(user_input))


def bottom_toolbar_callback():
    user_input = get_user_input(s)
    if user_input in {"quit", "exit", "eval", "help"}:
        return "Valid command, press Enter"
    else:
        return "???"


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
            validator=CommandValidator(),
            validate_while_typing=True,
            enable_open_in_editor=True,
            bottom_toolbar=bottom_toolbar_callback,
            rprompt=right_prompt_callback,
            style=new_tui_style,
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
