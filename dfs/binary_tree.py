from __future__ import annotations

from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Node = left
        self.right: Node = right
    
    def __repr__(self) -> str:
        if not self.val:
            return ""
        return f"Node(val={self.val}, left={self.left}, right={self.right})"


    @staticmethod
    def construct_tree(tree_nodes: list[int]) -> Node:
        # tree_nodes is a list of values of each node in bfs order
        def next(queue:  deque[int]):
            try: 
                return queue.popleft()
            except IndexError:
                return None

        if not tree_nodes:
            return None
        node_vals = deque(tree_nodes)
        root = Node(next(node_vals))
        bfs_queue = deque([root])
        while node_vals:
            node = next(bfs_queue)
            if not node:
                continue
            left = next(node_vals)
            if left:
                left = Node(left)
            right = next(node_vals)
            if right:
                right = Node(right)
            node.left = left
            node.right = right 
            bfs_queue.extend([left,right])
        return root
