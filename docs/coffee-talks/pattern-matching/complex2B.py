def test_number(value):
    match value:
        case [0, 0]:
            print("Zero")
        case [real, 0] if real>0:
            print(f"Positive real number {real}")
        case [real, 0]:
            print(f"Negative real number {real}")
        case [0, imag] if imag<0:
            print(f"Negative imaginary number {imag}")
        case [0, imag]:
            print(f"Negative imaginary number {imag}")
        case [real, imag]:
            print(f"Complex number {real}+i{imag}")
        case _:
            raise ValueError("Not a complex number")


test_number([0,0])
test_number([1,0])
test_number([-1,0])
test_number([0,1])
test_number([0,-1])
test_number([1,1])
