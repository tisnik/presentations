#!/usr/bin/env python3

import ctypes

libtest5 = ctypes.CDLL("target/debug/libtest5.so")

libtest5.print_string.argtypes = (ctypes.c_char_p,)

libtest5.print_string("Hello world!".encode("utf-8"))
libtest5.print_string("Příliš žluťoučký kůň".encode("utf-8"))
libtest5.print_string("Ну, погоди!".encode("utf-8"))
