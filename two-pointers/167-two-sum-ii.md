# 167. Two Sum II - Input Array Is Sorted

- **Difficulty:** Medium
- **Pattern:** two-pointers
- **Companies:** Amazon, Google, Apple, Microsoft, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a 1-indexed sorted array `numbers` and a `target`, return the two 1-based
indices whose values add up to `target`.

## Approaches

### Brute force

Test every pair `(i, j)` for `numbers[i] + numbers[j] == target`.

- Time: `O(n^2)`
- Space: `O(1)`

### Optimal

Place `left` at the start and `right` at the end. If the sum is too small move
`left` right to increase it; if too large move `right` left to decrease it; when
it equals the target return the 1-based indices.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

Sorted order makes the sum monotonic in each pointer, so every move safely
discards one impossible value without missing the answer.

## Edge cases

- Exactly two elements.
- Negative numbers and zero.
- Duplicate values forming the target.

## Pitfalls

- Returning 0-based indices instead of the required 1-based ones.
- Using a hash map here wastes the sorted-input advantage and extra space.

## Related problems

- 1 Two Sum
- 15 3Sum
- 170 Two Sum III - Data Structure Design
