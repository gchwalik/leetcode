# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
# This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

T


def get_diameter(root: Node) -> int:
    def dfs(node: Optional[Node]) -> tuple[int, int]:
        # takes in tree node
        # returns:
        # - longest path from current node to leaf
        # - longest width from left to right, for current node or any children

        # call with None child node, path -1 to work with logic
        if not node:
            return (-1,0)
        if node.left is None and node.right is None:
            return (0,0)
        
        left_child_path, left_width = dfs(node.left)
        right_child_path, right_width = dfs(node.right)
        left_path = left_child_path+1
        right_path = right_child_path+1

        path = max(left_path, right_path)
        width = max(left_width, right_width, left_path+right_path)

        return path, width

    def leetcode_solution(root: Optional[Node]) -> int:
        # this is an optimization of the above logic
        # its space and time complixity are much less because
        # i'm keeping track of significantly fewer vars
        # and this is clever about the implicit logic of the max width

        width = [0]
        def dfs(node: Optional[Node]) -> tuple[int, int]:
            # returns:
            # - longest path from node to leaf
            # don't stop at leaves, simplifies logic for non childs and leafs
            if not node:
                return 0

            left_path = dfs(node.left)
            right_path = dfs(node.right)
            width[0] = max(width[0], left_path+right_path)
            return max(left_path, right_path)+1

        dfs(root)
        return width[0]

    return leetcode_solution(root)
    # return max(dfs(root))


tree1 = Node(1, 
    left=Node(2, left=Node(4), right=Node(5)), 
    right=Node(3),
)
tree2 = Node(1, left=Node(2))
tree2_1 = Node(1, left=Node(2), right=Node(3, left=Node(4), right=Node(5)))
tree3 = Node(1, left=Node(2, left=Node(3, left=Node(6)), right=Node(4, right=Node(5))))


assert get_diameter(Node(1)) == 0
assert get_diameter(tree1) == 3
assert get_diameter(tree2_1) == 3
assert get_diameter(tree2) == 1
assert get_diameter(tree3) == 4