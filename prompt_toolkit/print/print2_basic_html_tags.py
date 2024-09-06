from prompt_toolkit import HTML, print_formatted_text

print_formatted_text(HTML("zpráva obsahující <b>tučný text</b>"))
print_formatted_text(HTML("zpráva s <i>textem tištěným kurzivou</i>"))
print_formatted_text(HTML("text obsahující <u>tato podtržená slova</u>"))
print_formatted_text(HTML("test kombinace <b><i>tučné kurzivy</i></b>"))
print_formatted_text(HTML("test kombinace <b><u>tučného podtrženého textu</u></b>"))
print_formatted_text(
    HTML("test kombinace <i><u>podtrženého textu psaného kurzivou</u></i>")
)
