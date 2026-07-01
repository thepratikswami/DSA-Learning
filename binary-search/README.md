# Binary Search

## What binary search is all about

Binary search is a divide-and-conquer technique for finding a value in a sorted range. It repeatedly halves the search interval until the target is found or the interval is empty.

### When to use binary search

- When the input is sorted or can be treated as monotonic.
- When the problem asks for a position, boundary, or threshold.
- When the decision function is true/false and changes only once.

## Pattern hacks to identify binary-search problems

- Keywords: `sorted`, `search`, `find`, `first`, `last`, `minimum`, `maximum`, `threshold`, `closest`, `smallest`, `largest`.
- When you can answer the question with a yes/no check over an index or value.
- When the solution space is not the actual array but a range of possible answers.

## Common strategies

- Use binary search on array indices for direct lookup.
- Use binary search on answer space for optimization or feasibility checks.
- Define a helper condition that is monotonic.
- Return left or right boundary carefully for first/last occurrences.

## Example problems

1. Classic Binary Search: search for a target in a sorted array.
2. Search Insert Position: find where a value fits in order.
3. Find First and Last Position of Element in Sorted Array: binary search for leftmost and rightmost indices.
4. Kth Smallest Element in a Sorted Matrix: search over value range with a count condition.

## Template that solves >90% of questions

Most binary-search problems can be solved with a core template. Keep the structure the same and replace only the condition or update logic for each question.

```python
lo, hi = 0, len(nums) - 1
result = default_value

while lo <= hi:
    mid = (lo + hi) // 2
    if condition(mid):
        result = update_result(mid)
        hi = mid - 1  # or lo = mid + 1 based on boundary
    else:
        lo = mid + 1

return result
```

- `condition(mid)` is the problem-specific check.
- `update_result(mid)` is the answer update logic.
- Change the boundary movement depending on first/last occurrence or feasibility search.

## Notes

Binary search is not only for arrays; it is also useful for any ordered search space. The most important insight is to make the decision function monotonic and keep the boundary updates consistent.

For a quick pre-practice refresher, read `revision.md`.
