from time import sleep

from prompt_toolkit.shortcuts import message_dialog, progress_dialog


def simple_callback(set_percentage_function, log_text_function):
    for counter in range(0, 101, 5):
        log_text_function("Pocitam: {counter}\n".format(counter=counter))
        set_percentage_function(counter)
        sleep(0.5)
    sleep(2)


response = progress_dialog(
    title="Výpočet",
    text="Probíhá výpočet, prosím čekejte",
    run_callback=simple_callback,
)
