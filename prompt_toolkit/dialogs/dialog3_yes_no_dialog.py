from prompt_toolkit.shortcuts import message_dialog, yes_no_dialog

response = yes_no_dialog(
    title='Software failure',
    text='Guru Meditation #12345678.ABCDEFFF\nRestart system?')

message_dialog(
    title='Your choice',
    text='Yes' if response else 'No')
