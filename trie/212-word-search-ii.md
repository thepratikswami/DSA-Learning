# 212. Word Search II

- **Difficulty:** Hard
- **Pattern:** trie
- **Companies:** Amazon, Google, Meta, Microsoft, Uber, Airbnb
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/word-search-ii/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a grid of letters and a list of words, return every word that can be formed
by a path of horizontally/vertically adjacent cells (no cell reused within a
word).

## Approaches

### Brute force

Run a separate grid DFS for each word independently, re-exploring the board once
per word.

- Time: `O(W * R * C * 4^L)`
- Space: `O(L)`

### Optimal

Insert all words into a trie, then DFS the board once, advancing through trie
nodes in lockstep with the path. Mark cells as visited with a sentinel (`#`) and
restore on backtrack. When a node stores a word, collect it and clear its marker
to avoid duplicates; prune leaf nodes to shrink the search space.

- Time: `O(R * C * 4^L)` where `L` is the longest word
- Space: `O(total characters in words)`

## Key insight

Sharing prefixes in a trie lets one board traversal test all words at once, and
the trie instantly prunes any path whose prefix no word contains.

## Edge cases

- Duplicate words in the list (dedupe via clearing the stored word).
- Words longer than any board path — pruned naturally.
- Single-cell board or single-letter words.

## Pitfalls

- Forgetting to restore the cell after backtracking (`board[r][c] = char`).
- Re-adding a word already found — null out `node.word` once collected.
- Skipping leaf pruning, which slows large boards significantly.

## Related problems

- 79 Word Search
- 208 Implement Trie (Prefix Tree)
- 211 Design Add and Search Words Data Structure
- 425 Word Squares
