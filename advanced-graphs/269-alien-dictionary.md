# 269. Alien Dictionary

- **Difficulty:** Hard
- **Pattern:** advanced-graphs
- **Companies:** Amazon, Google, Meta, Airbnb, Microsoft
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/alien-dictionary/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a list of `words` sorted lexicographically in an unknown alien language,
derive an order of the characters consistent with that sorting. Return any valid
order, or `""` if no valid order exists.

## Approaches

### Brute force

Try permutations of the distinct characters and check each against every adjacent
word pair. This is factorial in the alphabet size and impractical.

- Time: `O(a! * total length)`
- Space: `O(a)`

### Optimal

Build a graph: for each adjacent word pair, the first differing character gives an
edge `a -> b`. Topologically sort with Kahn's algorithm (BFS on indegrees). If the
result omits any character, a cycle exists and the answer is `""`.

- Time: `O(C)` where `C` is total characters across all words
- Space: `O(1)` graph (bounded 26-letter alphabet) plus indegree map

## Key insight

Only the first differing character between two adjacent words carries ordering
information; everything after it is unconstrained by that pair.

## Edge cases

- Prefix conflict: a longer word appears before its own prefix (e.g. `["abc","ab"]`)
  is invalid, return `""`.
- Single word or all identical characters: any order of present letters is valid.
- Cycle in constraints: return `""`.

## Pitfalls

- Forgetting the prefix-conflict check before scanning for a differing character.
- Adding duplicate edges and double-counting indegree.
- Not seeding indegree for every character that appears.

## Related problems

- 207 Course Schedule
- 210 Course Schedule II
- 444 Sequence Reconstruction
