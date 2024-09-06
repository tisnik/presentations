from prompt_toolkit import HTML, print_formatted_text
from prompt_toolkit.output.vt100 import FG_ANSI_COLORS

for color in sorted(FG_ANSI_COLORS):
    message = "<style fg='{color}'>zpráva vypsaná barvou {color}</style>".format(
        color=color
    )
    print(message)

print("\n\n")

for color in sorted(FG_ANSI_COLORS):
    message = "<style fg='{color}'>zpráva vypsaná barvou {color}</style>".format(
        color=color
    )
    print_formatted_text(HTML(message))
