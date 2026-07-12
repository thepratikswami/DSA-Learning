# 51. N-Queens

- **Difficulty:** Hard
- **Pattern:** backtracking
- **Companies:** Amazon, Google, Microsoft, Meta, Apple, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/n-queens/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Place `n` queens on an `n x n` board so that no two attack each other, and return
every distinct board configuration.

## Approaches

### Optimal

Place one queen per row via backtracking. Maintain three sets — occupied columns,
diagonals keyed by `row - col`, and anti-diagonals keyed by `row + col`. A square
is safe when none of the three sets contains its key. Place, recurse to the next
row, then remove the queen and its keys on backtrack.

- Time: `O(n!)` — the branching shrinks each row as columns get blocked
- Space: `O(n)` for the sets and recursion depth, plus the board

## Key insight

Every cell on the same `\` diagonal shares `row - col`, and every cell on the
same `/` diagonal shares `row + col`. Those two constants make diagonal conflict
checks `O(1)`.

## Edge cases

- `n = 1` -> a single board `[["Q"]]`.
- `n = 2` and `n = 3` -> no solutions, return `[]`.

## Pitfalls

- Mixing up the `row - col` and `row + col` keys.
- Forgetting to remove all three keys when undoing a placement.
- Scanning the whole board for conflicts instead of using the sets.

## Related problems

- 52 N-Queens II
- 37 Sudoku Solver
- 79 Word Search
