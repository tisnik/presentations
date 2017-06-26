#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import ctypes

libtest5 = ctypes.CDLL("target/debug/libtest5.so")

libtest5.print_string.argtypes = (ctypes.c_char_p,)

libtest5.print_string(ctypes.c_char_p("Hello world!"))
libtest5.print_string(ctypes.c_char_p("Příliš žluťoučký kůň"))
libtest5.print_string(ctypes.c_char_p("Ну, погоди!"))
