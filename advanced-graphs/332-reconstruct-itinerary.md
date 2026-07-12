# 332. Reconstruct Itinerary

- **Difficulty:** Hard
- **Pattern:** advanced-graphs
- **Companies:** Amazon, Google, Microsoft, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/reconstruct-itinerary/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a list of airline `tickets` `[from, to]`, reconstruct the itinerary that
uses every ticket exactly once, starting from `"JFK"`. When multiple valid
itineraries exist, return the one with the smallest lexical order.

## Approaches

### Brute force

Backtrack over ticket orderings starting from `JFK`, trying destinations in sorted
order and undoing when stuck. Correct but exponential in the worst case.

- Time: exponential
- Space: `O(E)` recursion

### Optimal

Hierholzer's algorithm for an Eulerian path. Store each airport's destinations in a
structure that yields the smallest lexical option, walk edges greedily on a stack,
and append an airport to the route when it has no outgoing edges left. Reverse the
route at the end.

- Time: `O(E log E)` (sorting the destinations)
- Space: `O(E)`

## Key insight

Post-order append plus final reverse handles dead-ends correctly: a stuck airport is
placed at the tail of the itinerary, and reversing yields a valid Eulerian path.

## Edge cases

- Multiple tickets between the same pair of airports.
- An airport with no outgoing tickets (a terminal stop).
- Guaranteed at least one valid itinerary per constraints.

## Pitfalls

- Sorting destinations ascending but forgetting `pop()` takes the last element, so
  sort **descending** to pop the smallest lexical airport.
- Forgetting to reverse the collected route before returning.

## Related problems

- 753 Cracking the Safe
- 2097 Valid Arrangement of Pairs
- 207 Course Schedule
