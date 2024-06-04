#!/usr/bin/env python
# __coconut_hash__ = 0x3d5464d

# Compiled with Coconut version 1.3.0 [Dead Parrot]

# Coconut Header: -------------------------------------------------------------


# Compiled Coconut: -----------------------------------------------------------

result = 60 * 7 / 10
print(result)

if result >= 40 and result <= 50:
    print("very close")

print(1 << 10)
print(1 ^ 255)

(print)((abs)(-42))

(print)((hex)((abs)((ord)("B"))))

(print)((sum)(range(11)))

(print)((sum)((reversed)(range(11))))

(print)((_coconut_forward_compose(ord, abs, hex))("B"))

(print)((_coconut_forward_compose(reversed, sum))(range(11)))
