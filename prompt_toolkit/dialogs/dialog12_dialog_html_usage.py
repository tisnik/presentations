from enum import Enum

from prompt_toolkit import HTML
from prompt_toolkit.shortcuts import button_dialog, message_dialog
from prompt_toolkit.styles import Style

dialog_stylesheet_1 = Style.from_dict(
    {
        "dialog": "bg:yellow",
        "dialog frame-label": "bg:white black",
        "dialog.body": "bg:#000000 #00ff00",
        "dialog shadow": "bg:#00aa00",
    }
)

Response = Enum("Response", "abort retry fail")

response = button_dialog(
    title=HTML("Tento program provedl <white>neplatnou</white> operaci"),
    text=HTML("Not <u>ready</u> reading drive <b>A</b>"),
    buttons=[
        ("Abort", Response.abort),
        ("Retry", Response.retry),
        ("Fail", Response.fail),
    ],
    style=dialog_stylesheet_1,
)


dialog_stylesheet_2 = Style.from_dict(
    {
        "dialog": "bg:black",
        "dialog frame-label": "bg:white black",
    }
)

message_dialog(
    title="Zadali jste volbu",
    text=HTML("<red>Příkaz:</red> <blue>{response}</blue>".format(response=response)),
    style=dialog_stylesheet_2,
)
