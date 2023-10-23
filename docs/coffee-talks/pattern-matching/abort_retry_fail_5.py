print("Not ready reading drive A")


def abort_retry_fail():
    response = input("Abort, Retry, Fail? ")

    match response:
        case "a" | "A":
            return "Abort"
        case "r" | "R":
            return "Retry"
        case "f" | "F":
            return "Fail"
        case _:
            return "Wrong response"


print(abort_retry_fail())
