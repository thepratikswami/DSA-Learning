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
