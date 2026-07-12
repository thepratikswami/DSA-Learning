# 286. Walls and Gates

- **Difficulty:** Medium
- **Pattern:** graphs
- **Companies:** Meta, Google, Amazon, Microsoft
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/walls-and-gates/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

A grid contains `-1` (wall), `0` (gate), and `INF` (`2147483647`, an empty room).
Fill each empty room with the distance to its nearest gate, or leave it `INF` if
no gate can reach it. Modify the grid in place.

## Approaches

### Optimal (multi-source BFS)

Seed a queue with every gate at distance `0`. BFS outward; for each empty room
(`INF`) reached, set its distance to the current cell's distance plus one and
enqueue it. Because all gates expand simultaneously, the first time a room is
reached is via its nearest gate.

- Time: `O(m * n)`
- Space: `O(m * n)`

## Key insight

Pushing all gates into the queue at once means BFS reaches each room by the
shortest path first, so a single traversal fills every distance—no per-room
search needed.

## Edge cases

- Empty grid or empty first row.
- Rooms fully walled off from every gate stay `INF`.
- Grid with no gates leaves all rooms `INF`.

## Pitfalls

- Running BFS separately from each gate is correct but `O(gates * m * n)`; a
  single multi-source pass is far faster.
- Only overwrite cells still equal to `INF`; checking any non-gate value would
  corrupt walls.

## Related problems

- 994 Rotting Oranges
- 542 01 Matrix
- 1091 Shortest Path in Binary Matrix
