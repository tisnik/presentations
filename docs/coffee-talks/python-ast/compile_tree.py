import ast


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.nest_level = 1

    def visit(self, node):
        indent = " " * self.nest_level * 2
        print(indent, node)
        self.nest_level += 1
        self.generic_visit(node)
        self.nest_level -= 1


tree = ast.parse("print(1+2*(1-3/4)+5)", mode="exec")

visitor = Visitor()
visitor.visit(tree)

print("Executing")

exec(compile(tree, filename="<ast>", mode="exec"))

print("Done")
