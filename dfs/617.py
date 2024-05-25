# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other, 
# some nodes of the two trees are overlapped while the others are not. 
# You need to merge the two trees into a new binary tree. 

# The merge rule is that if two nodes overlap, then sum node values up 
# as the new value of the merged node. 
# Otherwise, the NOT null node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.

from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    val: int = 0
    left: Node = None
    right: Node = None


def merge_trees(root1: Node, root2: Node) -> Node:
        # takes in two trees and merges them returning the root of the new tree
        def recurse(node1: Node, node2: Node) -> Node:
            if node1 and node2:
                sum = node1.val + node2.val
                new_node = Node(sum)
                new_node.left = recurse(node1.left, node2.left)
                new_node.right = recurse(node1.right, node2.right)
                return new_node
            else: 
                return node1 or node2

        return recurse(root1, root2)

""" Why does this work? This works because once you hit a None node, you don't need to keep passing
None down the line and reconstructing the branch with new pointers
"""
