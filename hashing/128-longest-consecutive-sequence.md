# 128. Longest Consecutive Sequence

- **Difficulty:** Medium
- **Pattern:** hashing
- **Companies:** Google, Amazon, Meta, Microsoft, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/longest-consecutive-sequence/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an unsorted array, return the length of the longest run of consecutive
integers. Must run in `O(n)`.

## Approaches

### Brute force

Sort the array, then scan for the longest consecutive run.

- Time: `O(n log n)`
- Space: `O(1)` (or `O(n)` depending on sort)

### Optimal

Put all values in a set. Only start counting a run from a number that has no
left neighbor (`num - 1` not in the set), then walk upward while `num + length`
exists. Each value is visited at most twice overall.

- Time: `O(n)`
- Space: `O(n)`

## Key insight

Starting a count only at sequence *starts* guarantees each element is extended
once, keeping the total work linear despite the inner `while` loop.

## Edge cases

- Empty array returns `0`.
- Duplicates collapse in the set and must not inflate the length.

## Pitfalls

- Counting from every element without the "is this a start?" guard degrades to
  `O(n^2)`.
- Forgetting to dedupe first.

## Related problems

- 1 Two Sum
- 217 Contains Duplicate
