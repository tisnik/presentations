import ast

with open("primes.py") as fin:
    code = fin.read()
    tree = ast.parse(code)

print(ast.dump(tree))
