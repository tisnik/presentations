from prompt_toolkit.shortcuts import input_dialog, message_dialog

response = input_dialog(title="Zadání hesla", text="Heslo:", password=True)

if response is not None:
    message_dialog(
        title="Zadání hesla",
        text="zadali jste: {password}".format(
            password=response if response else "nic :)"
        ),
    )
else:
    message_dialog(title="Zadání hesla", text="Heslo nebylo zadáno")
