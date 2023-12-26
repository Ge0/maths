class Leaf:
    def __init__(self, value):
        self.element = value
    
    def __str__(self):
        return str(self.element)

    def eval(self):
        return int(self.element)

class Node:
    def __init__(self, operand, left, right):
        self.operand = operand
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"({self.left} {self.operand} {self.right})"

    def eval(self):
        if self.operand == "+":
            return self.left.eval() + self.right.eval()
        elif self.operand == "-":
            return self.left.eval() - self.right.eval()
        elif self.operand == "x":
            return self.left.eval() * self.right.eval()
        elif self.operand == "/":
            return self.left.eval() / self.right.eval()


def build_tree(stack):
    element = stack.pop(0)
    if element.isdigit():
        return Leaf(element)
    else:
        left = build_tree(stack)
        right = stack.pop(0)
        if right.isdigit():
            return Node(operand=element, left=left, right=Leaf(right))
        else:
            stack.insert(0, right)
            return Node(operand=element, left=left, right=build_tree(stack))


tree = build_tree(list("x-567"))
print(tree)
print(tree.eval())

tree = build_tree(list("x3+45"))
print(tree)
print(tree.eval())