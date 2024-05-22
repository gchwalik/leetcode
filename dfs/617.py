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
    def get_val(node: Node) -> int:
        if node is None:
            return 0
        return node.val
    
    def recurse(node1: Node, node2: Node) -> Node:
        sum = get_val(node1) + get_val(node2)
        new_node = Node(sum)
        if node1.left or node2.left:
            new_node.left = recurse(node1.left, node2.left)
        if node1.right or node2.right:
            new_node.right = recurse(node1.left, node2.left)
        return new_node
    
    return recurse(root1, root2)



