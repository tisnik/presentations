#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import jedi

src = """
anybody=True
answer="42"
an"""

script = jedi.Script(src, 4, len("an"), "")
print(script.completions())
