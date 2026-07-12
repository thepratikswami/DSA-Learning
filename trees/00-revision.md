# Trees Interview Revision

## Core idea

Break the problem into a question about one node plus the same question for its children.

## How to recognize it

- Input has `TreeNode`.
- The problem asks about depth, levels, paths, ancestors, or BST properties.
- A subtree result can be combined into a parent result.
- Level order suggests BFS.

## Interview thinking steps

1. Pick DFS or BFS.
2. Define the return value of your recursive function.
3. Set the base case for `None`.
4. Combine left and right subtree results.
5. For BST problems, use inorder order or valid value bounds.

## Pitfalls

- Not defining the recursive return clearly.
- Using global state when a return value would be cleaner.
- Forgetting that BST validity uses full ancestor bounds.
- Recursion depth on very skewed trees.

## Complexity

Most tree traversals are `O(n)` time. Space is `O(h)` for recursion, or `O(w)` for BFS queue width.

## Worked example

Compute `maxDepth` on this tree with a post-order DFS (visit children, then combine):

```
        3
       / \
      9   20
         /  \
        15   7
```

1. `dfs(3)` needs `dfs(9)` and `dfs(20)`.
2. `dfs(9)`: no children -> `1 + max(dfs(None)=0, dfs(None)=0)` = `1`.
3. `dfs(20)` needs `dfs(15)` and `dfs(7)`.
4. `dfs(15)`: leaf -> `1`.
5. `dfs(7)`: leaf -> `1`.
6. Back in `dfs(20)`: `1 + max(1, 1)` = `2`.
7. Back in `dfs(3)`: `1 + max(dfs(9)=1, dfs(20)=2)` = `3`.

The answer `3` bubbles up because each node returns one number summarizing its
whole subtree, exactly the "solve one node, combine children" template.
