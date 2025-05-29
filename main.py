from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    pass

@dataclass
class Node:
    name: str
    left: Optional[Node]
    right: Optional[Node]

def print_right_nodes(current_node):
    if (not current_node):
        return
    print(current_node.name)
    current_node = current_node.right
    print_right_nodes(current_node)

def print_left_nodes(current_node):
    if (not current_node.left):
        print_right_nodes(current_node)
        return
    print(current_node.name)
    current_node = current_node.left
    print_left_nodes(current_node)

left2_node: Node = Node("left2_node", None, None)
left_node: Node = Node("left_node", left2_node, None)
right_node: Node = Node("right_node", None, None)
test_node: Node = Node("test_node", left_node, right_node)

test_node.name = "test_node"
right_node.name = "right_node"
left_node.name = "left_node"

print_left_nodes(test_node)


