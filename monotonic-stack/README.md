# Monotonic Stack

## What the pattern is all about

A monotonic stack keeps its elements in sorted order (all increasing or all
decreasing) as you scan an array once. Before pushing a new item you pop every
element that breaks the order. Each popped element is being "resolved" by the
current item, which is exactly the answer to next-greater / next-smaller / span
style questions.

### When to use monotonic stack

- Next greater or next smaller element to the left or right.
- Distance or span until a bigger/smaller value appears.
- Building the lexicographically smallest/largest result by removing items.
- Grouping elements that "catch up" to each other (car fleets, stock spans).

## Pattern hacks to identify monotonic-stack problems

- Keywords: `next greater`, `next smaller`, `previous smaller`, `span`, `warmer`,
  `remove k digits`, `smallest result`, `fleet`.
- The answer for an element depends on the first later (or earlier) element that
  is bigger or smaller than it.
- A brute-force `O(n^2)` scan compares each element against others until a
  condition flips.
- You repeatedly discard dominated elements that can never be the answer again.

## Common strategies

- Decreasing stack -> finds the next greater element.
- Increasing stack -> finds the next smaller element.
- Store indices when you need distance, width, or span.
- Store values (or pairs) when you only need the resolved element itself.
- For "smallest/largest string" greedily pop while the top hurts the result and
  the popped character still appears later.
- Iterate `2n` with modulo indexing to simulate a circular array.

## Template

```python
def next_greater(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []  # holds indices, values strictly decreasing

    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            prev = stack.pop()
            ans[prev] = x  # x is the next greater element for prev
        stack.append(i)

    return ans
```

## Notes

Every element is pushed once and popped at most once, so a monotonic stack turns
an apparent `O(n^2)` comparison into a single `O(n)` pass. The hard part is
choosing the stack direction and deciding what each entry stores (index, value,
or a pair such as `(value, count)`).
