from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        out = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                out.append("#")
                return
            out.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(out)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = deque(data.split(","))

        def dfs() -> Optional[TreeNode]:
            token = values.popleft()
            if token == "#":
                return None
            node = TreeNode(int(token))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# DEBUG RUNNER START
def _level_order(root):
    if not root:
        return []
    ans = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        ans.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return ans


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    codec = Codec()
    data = codec.serialize(root)
    print(data)
    restored = codec.deserialize(data)
    print(_level_order(restored))
# DEBUG RUNNER END
