from prompt_toolkit.shortcuts import input_dialog, message_dialog

response = input_dialog(title="Zadání uživatelského jména", text="Uživatelské jméno:")

if response is not None:
    message_dialog(
        title="Zadání uživatelského jména",
        text="zadali jste: {name}".format(name=response if response else "nic :)"),
    )
else:
    message_dialog(title="Zadání uživatelského jména", text="Jméno nebylo zadáno")
