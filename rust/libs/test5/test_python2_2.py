#!/usr/bin/env python2

import ctypes

libtest5 = ctypes.CDLL("target/debug/libtest5.so")

libtest5.print_string.argtypes = (ctypes.c_char_p,)

libtest5.print_string("Hello world!")
libtest5.print_string("Příliš žluťoučký kůň")
libtest5.print_string("Ну, погоди!")
