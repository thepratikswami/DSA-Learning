# Backtracking

## What backtracking is all about

Backtracking explores choices step by step and undoes each choice before trying the next one.

### When to use backtracking

- Generating all combinations, permutations, subsets, or boards.
- Finding all valid arrangements.
- Problems where choices form a decision tree.
- Constraints allow pruning invalid branches.

## Pattern hacks to identify backtracking problems

- Keywords: `all`, `generate`, `permutations`, `subsets`, `combinations`, `queens`.
- The output is a list of valid possibilities.
- You make a choice, recurse, then undo the choice.

## Common strategies

- Use `path` to hold the current partial answer.
- Use `start` to avoid duplicate combinations.
- Use `used` to avoid reusing items in permutations.
- Prune early when constraints fail.

## Template

```python
def backtrack(path, start):
    if is_complete(path):
        ans.append(path[:])
        return

    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(path, i + 1)
        path.pop()
```

## Notes

Backtracking is about clean state management. Every choice should have a matching undo.
