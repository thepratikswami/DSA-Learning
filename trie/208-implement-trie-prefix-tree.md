# 208. Implement Trie (Prefix Tree)

- **Difficulty:** Medium
- **Pattern:** trie
- **Companies:** Amazon, Google, Microsoft, Meta, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/implement-trie-prefix-tree/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Design a trie supporting `insert(word)`, `search(word)` (exact match), and
`startsWith(prefix)`.

## Approaches

### Optimal

Each node holds a `children` map (char -> node) and an `is_word` flag. `insert`
walks/creates nodes per character and marks the last as a word end. A shared
`_find_node` helper walks the path for both `search` and `startsWith`; `search`
additionally checks `is_word`.

- Time: `O(L)` per operation for word length `L`
- Space: `O(total characters inserted)`

## Key insight

Storing characters as tree edges lets words that share a prefix reuse the same
path, and a boolean end marker distinguishes a stored word from a mere prefix.

## Edge cases

- Empty string (if allowed) marks the root as a word.
- Searching a prefix that exists but was never inserted as a full word.
- Repeated inserts of the same word are idempotent.

## Pitfalls

- Treating "prefix exists" as "word exists" — `search` must check `is_word`.
- Forgetting to set `is_word` on the terminal node.

## Related problems

- 211 Design Add and Search Words Data Structure
- 212 Word Search II
- 648 Replace Words
- 677 Map Sum Pairs
