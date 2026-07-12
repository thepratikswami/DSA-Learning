# 1046. Last Stone Weight

- **Difficulty:** Easy
- **Pattern:** heap
- **Companies:** Amazon, Google, Microsoft, Facebook, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/last-stone-weight/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Each turn, smash the two heaviest stones together. If they are equal, both are
destroyed; otherwise the lighter is destroyed and the heavier keeps the weight
difference. Return the weight of the last remaining stone, or `0` if none remain.

## Approaches

### Max-heap simulation

Python only ships a min-heap, so negate every weight to emulate a max-heap. Repeatedly
pop the two largest (most negative) stones, and if they differ push back the
difference. Continue until at most one stone remains.

- Time: `O(n log n)`.
- Space: `O(n)`.

## Key insight

Negating values turns `heapq` into a max-heap, giving `O(log n)` access to the two
heaviest stones each round without sorting the whole list repeatedly.

## Edge cases

- Empty input returns `0`.
- Single stone returns its weight.
- All stones cancel out to `0`.

## Pitfalls

- Forgetting to re-negate when reading values back out of the heap.
- Pushing back a `0` difference; skip the push when the two stones are equal.

## Related problems

- 703 Kth Largest Element in a Stream
- 215 Kth Largest Element in an Array
- 2208 Minimum Operations to Halve Array Sum
