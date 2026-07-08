# Prefix Sum

## What prefix sum is all about

Prefix sum stores the running total up to each position so range and subarray questions can be answered quickly.

### When to use prefix sum

- When the problem asks about subarray sums or range sums.
- When repeated range calculations would otherwise be too slow.
- When you need to compare left-side and right-side totals.
- When prefix sums can be combined with a hash map for counting.

## Pattern hacks to identify prefix-sum problems

- Keywords: `subarray`, `range sum`, `pivot`, `sum equals`, `product except self`, `running total`.
- Brute force recomputes the same sums many times.
- The answer depends on the difference between two cumulative states.

## Common strategies

- Build a prefix array where `prefix[i]` stores the sum before index `i`.
- Use a running sum when you only need the current prefix.
- Use a hash map to count previous prefix sums.
- For product problems, combine left and right accumulated values.

## Template

```python
prefix = 0
for x in nums:
    prefix += x
```

For range sum from `left` to `right`, use `prefix[right + 1] - prefix[left]`.

## Notes

Prefix sum turns many repeated `O(n)` range calculations into `O(1)` lookups after one pass.
