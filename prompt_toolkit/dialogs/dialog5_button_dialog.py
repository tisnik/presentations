from prompt_toolkit.shortcuts import button_dialog, message_dialog

response = button_dialog(
    title="Tento program provedl neplatnou operaci",
    text="Not ready reading drive A",
    buttons=[("Abort", "abort"), ("Retry", "retry"), ("Fail", "fail")],
)

message_dialog(title="Zadali jste volbu", text=response)
