#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import ctypes

libtest5 = ctypes.CDLL("target/debug/libtest5.so")

libtest5.print_string.argtypes = (ctypes.c_char_p,)

libtest5.print_string("Hello world!".encode())
libtest5.print_string("Příliš žluťoučký kůň".encode())
libtest5.print_string("Ну, погоди!".encode())
