from __future__ import annotations
from typing import Optional

from collections import deque
from pprint import pp, pformat

class Node:
    def __init__(self, val=None, left=None, right=None):
        if not val:
            return None

        self.val: int = val
        self.left: Node = left
        self.right: Node = right
    
    def __repr__(self) -> str:
        def repr1() -> str:
            node = {"val":self.val}
            if self.left:
                node["left"] = self.left
            if self.right:
                node["right"] = self.right
            return pformat(node)
        def repr2() -> str:
            return pformat(f"Node(val={self.val}, \nleft={self.left}, \nright={self.right})")

        return repr2()


    @staticmethod
    def construct_tree(tree_nodes: list[int]) -> Node:
        # tree_nodes is a list of values of each node in bfs order
        if not tree_nodes:
            return None
        node_vals = deque(tree_nodes)
        root = Node(node_vals.popleft())
        bfs_queue = deque([root])
        while node_vals:
            node = bfs_queue.popleft()
            left = Node(node_vals.popleft())
            node.left = left
            bfs_queue.append(left)
            if node_vals:
                right = Node(node_vals.popleft())
                node.right = right 
                bfs_queue.append(right)
        return root
    
tree_lists = [
    [],
    [1],
    [1,2,3,None,None,4,5],
    [1,2,3,None,None,4,5],
]
for l in tree_lists:
    pp(Node.construct_tree(l))
