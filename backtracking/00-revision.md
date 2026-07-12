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

## Worked example

Subsets of `[1, 2]` using the choose/recurse/undo template:

1. `backtrack(start=0, path=[])` -> record `[]`.
2. Choose `1` -> `path=[1]`, recurse `backtrack(1, [1])` -> record `[1]`.
3. Inside, choose `2` -> `path=[1, 2]`, recurse `backtrack(2, [1,2])` -> record `[1, 2]`.
4. Loop ends (start == len), return; **undo** `pop()` -> `path=[1]`.
5. Loop ends at this level, return; **undo** `pop()` -> `path=[]`.
6. Back at top, choose `2` -> `path=[2]`, recurse `backtrack(2, [2])` -> record `[2]`.
7. Return and **undo** `pop()` -> `path=[]`. Done.

Result: `[[], [1], [1,2], [2]]`. Notice each result is copied with `path[:]`, every
`append` has a matching `pop`, and `start` only moves forward to avoid duplicates.
