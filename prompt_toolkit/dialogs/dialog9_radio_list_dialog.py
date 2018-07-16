from prompt_toolkit.shortcuts import message_dialog, radiolist_dialog

response = radiolist_dialog(
    title='Zadání příkazu',
    text='Zadejte příkaz (quit, exit, help, eval):',
    values=[
        ('quit', 'Quit'),
        ('exit', 'Exit'),
        ('help', 'Help'),
        ('eval', 'Eval')])

if response is not None:
    message_dialog(
        title='Zadání příkazu',
        text='zadali jste: {command}'.format(command=response if response else 'nic :)'))
else:
    message_dialog(
        title='Zadání uživatelského jména',
        text='Příkaz nebyl zadán')
