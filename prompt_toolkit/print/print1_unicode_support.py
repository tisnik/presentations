from prompt_toolkit import print_formatted_text
from urllib.request import urlopen

input = urlopen("http://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt")

for line in input:
    line = line.strip().decode("utf-8")
    print_formatted_text(line)
