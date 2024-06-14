#!/usr/bin/env python3

"""Simple preprocessor for Markdown files that handles @ character as include statement."""

input_file = "pattern-matching-.md"
output_file = "pattern-matching.md"

source_prefix = (
    "https://github.com/tisnik/presentations/blob/master/docs/coffee-talks/pattern-matching"
)

with open(input_file, "r") as fin:
    with open(output_file, "w") as fout:
        for line in fin.readlines():
            # handle @ character at the beginning of line as include statement
            if line[0:2] == "@ ":
                # retrieve file name of file to be included
                include = line[2:].strip()
                print("including:", include)

                # perform the inclusion within ```python block
                fout.write("```python\n")
                with open(include, "r") as inc:
                    included = inc.read()
                fout.write(included)
                fout.write("```\n\n")
                fout.write("[Source code]({}/{})".format(source_prefix, include))
                fout.write("\n")
            # other lines are to be output in its original form
            else:
                fout.write(line)
