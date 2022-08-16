import ast

tree = ast.parse("1+2*3")

print(ast.dump(tree, indent=4))
