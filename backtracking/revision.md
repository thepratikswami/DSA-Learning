# Backtracking Interview Revision

## Core idea

Explore a decision tree by choosing, recursing, and undoing.

## How to recognize it

- The problem asks for all valid outputs.
- You need combinations, permutations, subsets, or arrangements.
- Brute force is acceptable with pruning.
- The same partial path grows and shrinks.

## Interview thinking steps

1. Define what `path` contains.
2. Define the stopping condition.
3. Decide which choices are available at each step.
4. Add pruning rules.
5. Undo every mutation after the recursive call.

## Pitfalls

- Appending `path` instead of `path[:]`.
- Forgetting `path.pop()`.
- Creating duplicates by starting every recursion from index `0`.
- Not sorting when duplicate skipping depends on order.

## Complexity

Backtracking is often exponential. Explain complexity in terms of the size of the search tree.
