from prompt_toolkit.shortcuts import message_dialog, yes_no_dialog

response = yes_no_dialog(
    title="Tento program provedl neplatnou operaci",
    text="Nevíme, co se stalo, známe jen kód chyby:\n#12345678.ABCDEFFF\n\nProvést restart?",
    yes_text="Ano",
    no_text="Ne",
)

message_dialog(title="Zadali jste volbu", text="Ano" if response else "Ne")
