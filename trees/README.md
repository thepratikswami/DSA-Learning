# Trees

## What trees are all about

Tree problems use recursive or iterative traversal to process hierarchical data.

### When to use tree patterns

- Traversing every node.
- Computing depth, height, or path information.
- Validating binary search tree rules.
- Building a tree from traversal orders.
- Finding ancestors or kth values.

## Pattern hacks to identify tree problems

- Keywords: `root`, `left`, `right`, `depth`, `level`, `ancestor`, `BST`.
- The answer for a node depends on answers from its children.
- The problem can be solved with preorder, inorder, postorder, or BFS.

## Common strategies

- Use DFS recursion for subtree calculations.
- Use BFS queue for level-order traversal.
- Use inorder traversal for BST sorted order.
- Use bounds to validate a BST.

## Template

```python
def dfs(node):
    if not node:
        return base_value

    left = dfs(node.left)
    right = dfs(node.right)
    return combine(node, left, right)
```

## Notes

Choose traversal based on when you need to process the node: before children, between children, after children, or level by level.
