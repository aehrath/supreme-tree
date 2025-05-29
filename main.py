from dataclasses import dataclass

@dataclass
class Node:
    pass

@dataclass
class Node:
    name: str = ""
    left: Node = Node()
    right: Node = Node()

test_node: Node = Node()
left_node: Node = Node()
right_node: Node = Node()

test_node.right = right_node
test_node.left = left_node
test_node.name = "test_node"
right_node.name = "right_node"
left_node.name = "left_node"

print(test_node.name)
print(left_node.name)
print(right_node.name)