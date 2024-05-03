# Given the root of a binary tree and an integer targetSum, 
# return true if the tree has a root-to-leaf path such that 
# adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

from __future__ import annotations
from typing import Optional

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Node = left
        self.right: Node = right

tree_example = Node(5, 
    left=Node(4, left=Node(11, left=Node(7), right=Node(2))), 
    right=Node(8, left=Node(13), right=Node(4, right=Node(1)))
)
tree_example2 = Node(1, left=Node(2), right=Node(3))
tree_negatives = Node(4, 
    left=Node(-10, right=Node(2)), 
    right=Node(13, 
        left=Node(-50), 
        right=Node(20, left=Node(-4)),
    ),
)
tree_dup = Node(4, 
    left=Node(-10, right=Node(2)), 
    right=Node(13, 
        left=Node(-50), 
        right=Node(20, left=Node(-4), right=Node(4)),
    ),
)

# have to recurse, and cannot do in loop, because have to traverse every 
# root-to-leaf path, and there's a lot of branching. cannot reasonably do sequentially

def sum_path_exists(node: Optional[Node], target: int) -> bool:
    def get_value(node: Optional[Node]) -> int:
        if not node: 
            # since summing a null node should have no val
            # so 0 makes sense
            return 0
        return node.val

    def has_children(node: Optional[Node]) -> bool:
        # what if not node?
        # plan to never pass null nodes, but we will see
        if node and (node.left or node.right):
            return True
        return False

    def recurse(node: Optional[Node], target: int, sum: int = 0) -> bool:
        # base cases
        if not node:
            return False
        
        curr_sum = sum + get_value(node)
        if not has_children(node):
            if target == curr_sum:
                return True
            return False

        # still has children, need to keep recursing
        # return or because just need one true
        return recurse(node.left, target, curr_sum) or recurse(node.right, target, curr_sum)

    if not node:
        return False
    return recurse(node, target)


assert sum_path_exists(Node(1), 1) == True
assert sum_path_exists(Node(1, right=Node(2)), 3) == True
assert sum_path_exists(Node(1, left=Node(2)), 1) == False

assert sum_path_exists(tree_example, 22) == True
assert sum_path_exists(tree_example2, 5) == False
assert sum_path_exists(None, 2) == False

# include negative example
assert sum_path_exists(tree_negatives, 33) == True
assert sum_path_exists(tree_negatives, 31) == False
assert sum_path_exists(tree_dup, 33) == True