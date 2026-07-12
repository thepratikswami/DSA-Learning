# 211. Design Add and Search Words Data Structure

- **Difficulty:** Medium
- **Pattern:** trie
- **Companies:** Meta, Amazon, Google, Microsoft, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/design-add-and-search-words-data-structure/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Design a structure with `addWord(word)` and `search(word)`, where a search word
may contain `.` as a wildcard that matches any single character.

## Approaches

### Optimal

Store words in a trie. `search` runs a DFS indexed by position: a normal
character follows the single matching child, while `.` branches into every child
and succeeds if any branch matches the remaining suffix.

- Time: `O(L)` add; search is `O(L)` with no wildcards, up to `O(26^L)` worst
  case when every character is `.`
- Space: `O(total characters)` plus `O(L)` recursion

## Key insight

The trie reduces exact matching to a single path walk; only the `.` wildcard
forces branching, and even then it explores just the children that actually
exist.

## Edge cases

- Query of all dots (`"..."`) matches any stored word of that length.
- A prefix path exists but no full word ends there (must check `is_word`).
- No stored word of the queried length.

## Pitfalls

- On `.`, only recursing into some children instead of `any(...)` over all.
- Returning `True` on reaching the end without verifying `is_word`.

## Related problems

- 208 Implement Trie (Prefix Tree)
- 212 Word Search II
- 79 Word Search
- 745 Prefix and Suffix Search
