from enum import Enum

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
    title="Tento program provedl neplatnou operaci",
    text="Not ready reading drive A",
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

message_dialog(title="Zadali jste volbu", text=str(response), style=dialog_stylesheet_2)
