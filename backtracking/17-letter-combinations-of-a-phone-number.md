# 17. Letter Combinations of a Phone Number

- **Difficulty:** Medium
- **Pattern:** backtracking
- **Companies:** Amazon, Google, Facebook, Microsoft, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/letter-combinations-of-a-phone-number/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a string `digits` containing digits `2-9`, return all possible letter
combinations that the number could spell, using the standard telephone keypad
mapping. Return an empty list for empty input.

## Approaches

### Backtracking over digit positions

Map each digit to its letters. Recurse position by position: for the current digit,
append each candidate letter, recurse to the next digit, then pop. When the path
length matches the number of digits, record the assembled string.

- Time: `O(4^n * n)` where `n = len(digits)` (up to 4 letters per digit).
- Space: `O(n)` recursion depth (excluding the output).

## Key insight

This is a Cartesian product built incrementally. Each digit contributes one choice
per level, so the recursion tree has depth `n` and branching factor 3 or 4.

## Edge cases

- Empty `digits` must return `[]`, not `[""]`.
- Single digit returns that digit's letters directly.
- Digits `7` and `9` map to four letters, widening the tree.

## Pitfalls

- Returning `[""]` for empty input instead of `[]`.
- Joining the path only at the leaves — building strings by concatenation at every
  level wastes work.

## Related problems

- 39 Combination Sum
- 46 Permutations
- 22 Generate Parentheses
