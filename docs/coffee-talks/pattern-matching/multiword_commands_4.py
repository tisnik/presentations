def perform_command():
    response = input("> ")

    match response.split():
        case ["quit"]:
            return "Quit"
        case ["list", obj]:
            match obj:
                case "employees":
                    return "List employees"
                case "departments":
                    return "List departments"
                case "rooms":
                    return "List rooms"
                case _:
                    return "Invalid object type: employees, departments, or rooms expected"
        case ["info", subject]:
            return f"Info about subject '{subject}'"
        case _:
            return "Wrong command"


print(perform_command())
