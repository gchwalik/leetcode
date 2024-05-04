# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
# This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

from __future__ import annotations
from typing import Optional

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Node = left
        self.right: Node = right


def get_diameter(root: Node) -> int:
    def dfs(node: Optional[Node]) -> tuple[int, int]:
        # takes in tree node
        # returns:
        # - longest path from current node to leaf
        # - longest width from left to right, for current node or any children

        # call with None child node, path -1 to work with logic
        if not node:
            return (-1,0)
        if node.left is None and node.right is None:
            return (0,0)
        
        left_child_path, left_width = dfs(node.left)
        right_child_path, right_width = dfs(node.right)
        left_path = left_child_path+1
        right_path = right_child_path+1

        path = max(left_path, right_path)
        width = max(left_width, right_width, left_path+right_path)

        return path, width

    return max(dfs(root))


tree1 = Node(1, 
    left=Node(2, left=Node(4), right=Node(5)), 
    right=Node(3),
)
tree2 = Node(1, left=Node(2))
tree2_1 = Node(1, left=Node(2), right=Node(3, left=Node(4), right=Node(5)))
tree3 = Node(1, left=Node(2, left=Node(3, left=Node(6)), right=Node(4, right=Node(5))))


assert get_diameter(Node(1)) == 0
assert get_diameter(tree1) == 3
assert get_diameter(tree2_1) == 3
assert get_diameter(tree2) == 1
assert get_diameter(tree3) == 4