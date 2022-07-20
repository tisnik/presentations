#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xbe97918d

# Compiled with Coconut version 1.3.0 [Dead Parrot]

# Coconut Header: -------------------------------------------------------------


# Compiled Coconut: -----------------------------------------------------------

slovnik = {"prvni": 1, "druhy": 2, "treti": 3, "posledni": None}

print(slovnik)

slovnik["prvni"] = 1000 if slovnik["prvni"] is None else slovnik["prvni"]

print(slovnik)

slovnik["posledni"] = 1000 if slovnik["posledni"] is None else slovnik["posledni"]

print(slovnik)

slovnik["neexistujici"] = (
    10 if slovnik["neexistujici"] is None else slovnik["neexistujici"]
)

print(slovnik)
