"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.
"""

from typing import Optional

from binary_tree import Node

def get_max_depth(root: Optional[Node] = None) -> int:
    def dfs(node:Node, depth:int) -> int:
        if node is None:
            return depth
        if node.left or node.right:
            left = dfs(node.left, depth+1)
            right = dfs(node.right, depth+1)
            return max(left, right)
        return depth+1

    return dfs(root,0)

tree1 = Node(1)   
tree2 = Node(1, left=Node(2))   
tree3 = Node(1, left=Node(2), right=Node(3))
tree4 = Node(1, left=Node(2, right=Node(3)))

assert get_max_depth(tree1) == 1
assert get_max_depth(tree2) == 2
assert get_max_depth(tree3) == 2
assert get_max_depth(tree4) == 3