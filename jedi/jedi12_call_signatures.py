#!/usr/bin/env python3

import jedi

src = '''
def anagrams(word):
    """Very primitive anagram generator."""
    if len(word) < 2:
        return word
    else:
        tmp = []
        for i, letter in enumerate(word):
            for j in anagrams(word[:i]+word[i+1:]):
                tmp.append(j+letter)
    return tmp

anagrams("pokus")'''


lines = src.count("\n")
script = jedi.Script(src, lines + 1, len("anagrams("), "test.py")

call_signatures = script.call_signatures()

for call_signature in call_signatures:
    print(call_signatures.__str__(), call_signature.index, call_signature.bracket_start)
