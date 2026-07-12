# 210. Course Schedule II

- **Difficulty:** Medium
- **Pattern:** graphs
- **Companies:** Amazon, Google, Microsoft, Meta, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/course-schedule-ii/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given `numCourses` and a list of `[course, prereq]` pairs, return any valid order
in which to take all courses. If it is impossible (a cycle exists), return an
empty list.

## Approaches

### Optimal (Kahn's topological sort)

Build an adjacency list and an in-degree array. Start a queue with every course
whose in-degree is `0`. Repeatedly pop a course, append it to the order, and
decrement its neighbors' in-degrees, enqueuing any that drop to `0`. If the final
order contains all courses, return it; otherwise a cycle blocked some courses.

- Time: `O(V + E)`
- Space: `O(V + E)`

## Key insight

A valid ordering exists iff the graph is a DAG. Kahn's algorithm both produces the
order and detects cycles: leftover courses mean a cycle.

## Edge cases

- No prerequisites returns any permutation (here `0..n-1`).
- A cycle returns `[]`.
- A single course with no prerequisites.

## Pitfalls

- Reversing edge direction: an edge must go `prereq -> course`.
- Returning a partial order without checking that its length equals
  `numCourses`.

## Related problems

- 207 Course Schedule
- 269 Alien Dictionary
- 310 Minimum Height Trees
