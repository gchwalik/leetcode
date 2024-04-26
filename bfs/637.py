# Given the root of a binary tree, return the average value of the nodes 
# on each level in the form of an array.
# Answers within 10-5 of the actual answer will be accepted.

from __future__ import annotations
from dataclasses import dataclass
from collections import deque

@dataclass
class Node:
    val: int
    left: Node = None
    right: Node = None

def averages(root: Optional[Node] = None) -> list[float]:
    if not root:
        return []
    
    visited = deque()
    visited.append(root)
    visited.append(None)

    averages = []
    vals = []
    while visited:
        curr_node = visited.popleft()
        if curr_node:
            vals.append(curr_node.val)
            if curr_node.left:
                visited.append(curr_node.left)
            if curr_node.right:
                visited.append(curr_node.right)
            continue
        mean = sum(vals) / len(vals)
        averages.append(mean)
        vals = []

        if visited and visited[-1].val:
            visited.append(None)

    return averages



tree0 = Node(3)
tree1 = Node(3, left=Node(9))
tree2 = Node(3, right=Node(9))
tree3 = Node(3, left=Node(9), right=Node(20))
tree4 = Node(3, left=Node(9), right=Node(20, left=Node(15), right=Node(7)))


def test(val, expected) -> None:
    print(val == expected)


for tree, expected in [
    # (None, []),
    # (tree0, [3]), 
    # (tree1, [3,9]),
    # (tree2, [3,9]),
    # (tree3, [3,14.5]),
    (tree4, [3,14.5,11]),
]:
    test(averages(tree), expected)
