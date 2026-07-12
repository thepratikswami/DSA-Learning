# 763. Partition Labels

- **Difficulty:** Medium
- **Pattern:** greedy
- **Companies:** Amazon, Google, Microsoft, Facebook
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/partition-labels/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a string `s`, partition it into as many parts as possible so that each
letter appears in at most one part. Return a list of the sizes of these parts.

## Approaches

### Optimal (last-occurrence sweep)

Record the last index of every character. Sweep left to right, tracking the
farthest last-occurrence seen so far as the current partition's end. When the
current index equals that end, the partition is complete: record its size and
start a new one.

- Time: `O(n)`
- Space: `O(1)` (fixed alphabet)

## Key insight

A partition can close only once the current index reaches the farthest last
occurrence of any character seen inside it, guaranteeing no letter spills over.

## Edge cases

- All-distinct characters: every character is its own partition.
- All-identical characters: a single partition.

## Pitfalls

- Extending the partition end but closing before reaching it.
- Forgetting to reset `start` after closing a partition.

## Related problems

- 56 Merge Intervals
- 435 Non-overlapping Intervals
- 452 Minimum Number of Arrows to Burst Balloons
