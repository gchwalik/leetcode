# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

from __future__ import annotations

import collections
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    val: int
    left: Node = None
    right: Node = None

    def has_children(self) -> bool:
        if self.left or self.right:
            return True
        return False


def min_depth(root: Optional[Node] = None) -> int:
    def recurse(node: Node, depth: int) -> int:
        if not node:
            return float("inf")
        if not node.has_children():
            return depth
        return min(recurse(node.left, depth+1), recurse(node.right, depth+1))

    if not root:
        return 0
    return recurse(root, 1)


tree0 = Node(3)
tree1 = Node(3, left=Node(9), right=Node(20, left=Node(15),right=Node(7)))
tree1_5 = Node(3, left=Node(9))
tree2 = Node(2,right=Node(3,right=Node(4,right=Node(5, right=Node(6)))))
tree3 = Node(2, left=Node(3, left=Node(4)))

# assert min_depth() == 0
# assert min_depth(None) == 0
# assert min_depth(tree0) == 1
# assert min_depth(tree1_5) == 2
# assert min_depth(tree1) == 2
assert min_depth(tree2) == 5
assert min_depth(tree3) == 3
