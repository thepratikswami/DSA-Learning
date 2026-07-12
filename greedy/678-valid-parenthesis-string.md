# 678. Valid Parenthesis String

- **Difficulty:** Medium
- **Pattern:** greedy
- **Companies:** Amazon, Google, Microsoft, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/valid-parenthesis-string/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a string `s` containing `(`, `)`, and `*`, return whether it is valid. A
`*` can be treated as `(`, `)`, or an empty string. A valid string has balanced
parentheses with every `(` closed by a later `)`.

## Approaches

### Optimal (range of open counts)

Track the possible range `[low, high]` of unmatched open parentheses. `(` raises
both, `)` lowers both, `*` widens the range (lower by treating as `)`, raise by
treating as `(`). If `high` ever goes negative there are too many `)`, so fail.
Clamp `low` at `0` since open counts cannot go below zero. Valid iff `low == 0`
at the end.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

Instead of committing each `*` to one role, carry the full range of feasible open
counts. As long as zero stays reachable within that range, a valid assignment
exists.

## Edge cases

- All stars: valid (all treated as empty).
- Empty string: valid.

## Pitfalls

- Letting `low` go negative — clamp it to `0`, or `*` overuse corrupts the range.
- Returning `high == 0` instead of `low == 0`.

## Related problems

- 20 Valid Parentheses
- 32 Longest Valid Parentheses
- 921 Minimum Add to Make Parentheses Valid
