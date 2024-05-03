# Given the roots of two binary trees p and q, write a function to check 
# if they are the same or not. 

# Two binary trees are considered the same if they are structurally identical, 
# and the nodes have the same value.

# need to dfs both trees simultaneously 

from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Node = left
        self.right: Node = right

tree0 = Node(3)
tree0_1 = Node(4)
tree1 = Node(3, left=Node(9), right=Node(20, left=15,right=7))
tree1_1 = Node(3, left=Node(9))
tree1_2 = Node(3, left=Node(9), right=Node(20))
tree2 = Node(2,right=Node(3,right=Node(4,right=Node(5, right=Node(6)))))
tree2 = Node(2,right=Node(3,right=Node(4,left=Node(5, right=Node(6)))))
tree3 = Node(2, left=Node(3, left=Node(4)))


def get_value(node: Optional[Node]) -> int:
    if not node:
        return float("inf")
    return node.val

def same_siblings(node1: Node, node2: Node) -> bool:
    if (
        get_value(node1.left) == get_value(node2.left)
        and get_value(node1.right) == get_value(node2.right)
    ):
        return True
    return False

def recurse(node1: Optional[Node], node2: Optional[Node]) -> bool:
    # assumes that self matches, and only considers children
    # base case - don't share the same siblings
    # return False
    if not (node1 or node2):
        return True

    if get_value(node1) != get_value(node2):
        return False

    if not same_siblings(node1, node2):
        return False
    # base case - no children
    # return True
    return recurse(node1.left, node2.left) and recurse(node1.right, node2.right)

    # other case
    # children match, return recurse(left) or recurse(right)

def is_same_tree(node1: Optional[Node] = None, node2: Optional[Node] = None) -> bool:
    return recurse(node1, node2)
        
assert get_value(Node(3)) == 3
assert get_value(None) == float("inf")

assert same_siblings(tree1_2, tree1_2) == True

assert is_same_tree() == True
assert is_same_tree(tree0, tree0) == True
assert is_same_tree(tree0, tree0_1) == False
assert is_same_tree(tree1_1, tree0) == False
assert is_same_tree(tree1_2, tree1_2) == True

