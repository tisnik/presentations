from prompt_toolkit.shortcuts import message_dialog, button_dialog

response = button_dialog(
    title="Tento program provedl neplatnou operaci",
    text="Not ready reading drive A",
    buttons=[("Abort", "abort"), ("Retry", "retry"), ("Fail", "fail")],
)

message_dialog(title="Zadali jste volbu", text=response)
