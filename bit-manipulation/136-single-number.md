# 136. Single Number

- **Difficulty:** Easy
- **Pattern:** bit-manipulation
- **Companies:** Amazon, Google, Microsoft, Bloomberg, Apple, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/single-number/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Every element appears twice except one. Return that single element using `O(1)`
extra space.

## Approaches

### Brute force

Count occurrences with a hash map and return the key with count 1.

- Time: `O(n)`
- Space: `O(n)`

### Optimal

XOR all numbers together. Equal values cancel (`x ^ x == 0`) and `0 ^ x == x`, so
only the unpaired number survives.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

XOR is associative and commutative with self-inverse `x ^ x = 0`, which cancels
every duplicated pair regardless of order.

## Edge cases

- Single-element array -> that element.
- Negative numbers work — XOR is bitwise, sign included.

## Pitfalls

- Using OR or addition instead of XOR.
- Assuming this generalizes to elements appearing three times (that needs a
  different bit-counting trick — see 137).

## Related problems

- 137 Single Number II
- 260 Single Number III
- 268 Missing Number
- 389 Find the Difference
