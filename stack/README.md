# Stack

## What stack is all about

A stack stores items in last-in, first-out order. It is useful when the newest unresolved item should be handled first.

### When to use stack

- Matching parentheses, brackets, or nested structures.
- Finding next greater or next smaller elements.
- Maintaining a monotonic increasing or decreasing sequence.
- Decoding nested strings or expressions.

## Pattern hacks to identify stack problems

- Keywords: `valid`, `parentheses`, `next greater`, `previous smaller`, `histogram`, `decode`.
- You need to remember unfinished work.
- The latest item is the first one that can be resolved.

## Common strategies

- Use a normal stack for matching and parsing.
- Use a monotonic stack for next greater/smaller problems.
- Store indices when distance or width matters.
- Push unresolved items and pop them when the answer becomes known.

## Template

```python
stack = []

for i, x in enumerate(nums):
    while stack and condition(stack[-1], x):
        prev = stack.pop()
        # resolve prev using current item
    stack.append(i)
```

## Notes

Stacks often convert nested loops into a single pass because each item is pushed and popped at most once.
