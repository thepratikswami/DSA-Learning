# 150. Evaluate Reverse Polish Notation

- **Difficulty:** Medium
- **Pattern:** stack
- **Companies:** Amazon, Google, LinkedIn, Microsoft, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/evaluate-reverse-polish-notation/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Evaluate an arithmetic expression given in Reverse Polish Notation (postfix). The
valid operators are `+`, `-`, `*`, and `/`; division truncates toward zero.

## Approaches

### Optimal (stack)

Scan tokens left to right. Push numbers onto a stack. On an operator, pop the top
two operands (`b` first, then `a`), apply `a op b`, and push the result. The last
remaining stack value is the answer.

- Time: `O(n)`
- Space: `O(n)`

## Key insight

Postfix notation encodes evaluation order directly, so a stack replays that order
without any parsing of precedence or parentheses.

## Edge cases

- Single-number input like `["42"]`.
- Negative operands and negative results.
- Division that must truncate toward zero (e.g. `6 / -132` -> `0`).

## Pitfalls

- Popping operands in the wrong order breaks non-commutative `-` and `/`.
- Using Python floor division `//` truncates toward negative infinity; use
  `int(a / b)` to truncate toward zero.

## Related problems

- 20 Valid Parentheses (stack)
- 224 Basic Calculator
- 227 Basic Calculator II
