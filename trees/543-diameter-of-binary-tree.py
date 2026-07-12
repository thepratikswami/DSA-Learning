from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(node: Optional[TreeNode]) -> int:
            nonlocal diameter
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)

        height(root)
        return diameter


# DEBUG RUNNER START
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(Solution().diameterOfBinaryTree(root))
# DEBUG RUNNER END
