"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node 
of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined 
between two nodes p and q as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
okay, so i BST is balanced so all left children have vals < node.val
and all right children have vals > node.val

we want to find a node where...
"""

from binary_tree import Node

class Solution:
    def lowestCommonAncestor(
        self, root: Node, node1: Node, node2: Node
    ) -> Node:
        def dfs(node: Node) -> Node:
            if node1.val < node.val and node2.val < node.val:
                return dfs(node.left)
            elif node1.val > node.val and node2.val > node.val:
                return dfs(node.right)
            else:
                return node

        return dfs(root)
