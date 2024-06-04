#!/usr/bin/env python
# __coconut_hash__ = 0x109f876f

# Compiled with Coconut version 1.3.0 [Dead Parrot]

# Coconut Header: -------------------------------------------------------------

# Compiled Coconut: -----------------------------------------------------------

import os

v1 = None
v2 = "Some"

print(v2 if v1 is None else v1)

v3 = "Some"
v4 = "Something else"

print(v4 if v3 is None else v3)

v5 = None
v6 = None

print(v6 if v5 is None else v5)

print(
    (
        lambda _coconut_none_coalesce_item: "notepad"
        if _coconut_none_coalesce_item is None
        else _coconut_none_coalesce_item
    )(os.getenv("EDITOR"))
)
print(
    (
        lambda _coconut_none_coalesce_item: "notepad"
        if _coconut_none_coalesce_item is None
        else _coconut_none_coalesce_item
    )(os.getenv("XXEDITOR"))
)
