# 84. Largest Rectangle in Histogram

- **Difficulty:** Hard
- **Pattern:** stack
- **Companies:** Amazon, Google, Microsoft, Meta, Bloomberg, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/largest-rectangle-in-histogram/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given bar heights of a histogram, find the area of the largest rectangle that
fits entirely within the bars.

## Approaches

### Brute force

For every pair of bars treat them as boundaries and take the minimum height
between them, or expand left/right from each bar.

- Time: `O(n^2)`
- Space: `O(1)`

### Optimal

Maintain a monotonic increasing stack of `(start_index, height)`. When a shorter
bar arrives, pop taller bars and compute `height * (current_index - start_index)`
for each, letting the current bar inherit the leftmost popped start. A trailing
sentinel height of `0` flushes the stack.

- Time: `O(n)`
- Space: `O(n)`

## Key insight

Each popped bar's rectangle extends from its recorded start up to the current
index, so widths are known exactly when a bar is popped by a shorter one.

## Edge cases

- Strictly increasing heights only resolve at the sentinel.
- All-equal heights form one wide rectangle.
- Single bar.

## Pitfalls

- Forgetting the sentinel `0`, leaving bars unpopped.
- Losing the extended start index when popping consecutive taller bars.

## Related problems

- 85 Maximal Rectangle
- 42 Trapping Rain Water
- 1504 Count Submatrices With All Ones
