# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

from __future__ import annotations

import collections
from dataclasses import dataclass


@dataclass
class Node:
    val: int
    left: Node = None
    right: Node = None

def min_depth(root: Optional[Node] = None) -> int:
    if not root:
        return 0

    visited = collections.deque()
    visited.extend([root, None])

    depth = 1
    while visited:
        curr_node = visited.popleft()
        if curr_node:
            if not curr_node.left and not curr_node.right:
                return depth
            if curr_node.left:
                visited.append(curr_node.left)
            if curr_node.right:
                visited.append(curr_node.right)
            continue
        
        depth += 1
        if visited and visited[-1]:
            visited.append(None)



tree0 = Node(3)
tree1 = Node(3, left=Node(9), right=Node(20, left=15,right=7))
tree1_5 = Node(3, left=Node(9))
tree2 = Node(2,right=Node(3,right=Node(4,right=Node(5, right=Node(6)))))
tree3 = Node(2, left=Node(3, left=Node(4)))

assert min_depth() == 0
assert min_depth(None) == 0
assert min_depth(tree0) == 1
assert min_depth(tree1_5) == 2
assert min_depth(tree1) == 2
assert min_depth(tree2) == 5
assert min_depth(tree3) == 3

