# 79. Word Search

- **Difficulty:** Medium
- **Pattern:** backtracking
- **Companies:** Amazon, Microsoft, Facebook, Bloomberg, Google
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/word-search/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an `m x n` grid of characters `board` and a string `word`, return `true` if
`word` exists in the grid. The word must be constructed from sequentially adjacent
cells (horizontally or vertically), and the same cell may not be used more than
once.

## Approaches

### DFS backtracking with in-place marking

Try starting a DFS from every cell. At each step match the current character,
temporarily mark the cell as visited (overwrite with a sentinel like `#`), then
explore the four neighbors for the next character. Restore the cell on the way out
so other paths can reuse it.

- Time: `O(m * n * 4^L)` where `L = len(word)`.
- Space: `O(L)` recursion depth.

## Key insight

Mutating the board in place to mark visited cells avoids a separate `visited` set
and gives `O(1)` extra space per cell. Restoring the original character on backtrack
keeps the board clean for the next starting position.

## Edge cases

- Word longer than the number of cells — impossible, returns `false`.
- Single-cell board and single-character word.
- Repeated letters forcing the algorithm to explore multiple branches.

## Pitfalls

- Forgetting to restore the cell after recursion corrupts other search paths.
- Checking bounds after indexing the board causes an out-of-range error; check
  bounds first.

## Related problems

- 212 Word Search II (trie)
- 200 Number of Islands
- 130 Surrounded Regions
