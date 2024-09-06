from enum import Enum

from prompt_toolkit.shortcuts import button_dialog, message_dialog

Response = Enum("Response", "abort retry fail")

response = button_dialog(
    title="Tento program provedl neplatnou operaci",
    text="Not ready reading drive A",
    buttons=[
        ("Abort", Response.abort),
        ("Retry", Response.retry),
        ("Fail", Response.fail),
    ],
)

message_dialog(title="Zadali jste volbu", text=str(response))
