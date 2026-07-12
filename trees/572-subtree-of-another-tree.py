from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self._same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def _same(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self._same(p.left, q.left) and self._same(p.right, q.right)


# DEBUG RUNNER START
if __name__ == "__main__":
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    sub_root = TreeNode(4, TreeNode(1), TreeNode(2))
    print(Solution().isSubtree(root, sub_root))

    not_sub = TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0)))
    print(Solution().isSubtree(root, not_sub))
# DEBUG RUNNER END
