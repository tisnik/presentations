from prompt_toolkit import HTML, print_formatted_text
from prompt_toolkit.output.vt100 import BG_ANSI_COLORS, FG_ANSI_COLORS

for bg_color in sorted(BG_ANSI_COLORS):
    for fg_color in sorted(FG_ANSI_COLORS):
        message = "<p fg='{fg_color}' bg='{bg_color}'> test </p>".format(
            fg_color=fg_color, bg_color=bg_color
        )
        print_formatted_text(HTML(message), end="")

    print()
