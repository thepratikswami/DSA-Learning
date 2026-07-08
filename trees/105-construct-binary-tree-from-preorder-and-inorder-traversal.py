from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {value: i for i, value in enumerate(inorder)}
        pre_index = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal pre_index
            if left > right:
                return None

            value = preorder[pre_index]
            pre_index += 1
            root = TreeNode(value)
            mid = inorder_index[value]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)


# DEBUG RUNNER START
if __name__ == "__main__":
    root = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(root.val, root.left.val, root.right.val)
# DEBUG RUNNER END
