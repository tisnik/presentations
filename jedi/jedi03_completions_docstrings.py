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

anybody=True
answer="42"
an'''

lines = src.count("\n")
script = jedi.Script(src, lines + 1, len("an"), "")

completions = script.completions()

for completion in completions:
    print(completion.name)
    print("-" * 40)
    print(completion.docstring())
    print("\n" * 3)
