# 207. Course Schedule

- **Difficulty:** Medium
- **Pattern:** graphs
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/course-schedule/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given `numCourses` and a list of prerequisite pairs, decide whether all courses
can be finished (i.e. the prerequisite graph has no cycle).

## Approaches

### Brute force

Run DFS from every node tracking the current recursion path; if you revisit a node
already on the path there is a cycle. Repeated work makes this wasteful.

- Time: `O(V * (V + E))`
- Space: `O(V + E)`

### Optimal

Kahn's algorithm (BFS topological sort). Build an adjacency list and an indegree
array, enqueue all zero-indegree courses, then repeatedly pop a course, count it,
and decrement its neighbors' indegrees, enqueueing any that reach zero. All courses
can finish iff every node gets processed.

- Time: `O(V + E)`
- Space: `O(V + E)`

## Key insight

A directed graph is schedulable exactly when it is acyclic; topological sort
processes every node once precisely when no cycle blocks the ordering.

## Edge cases

- No prerequisites at all (always finishable).
- Self-dependency `[a, a]` forms an immediate cycle.
- Disconnected components.

## Pitfalls

- Reversing the edge direction: `graph[prereq].append(course)` is intentional.
- Comparing `completed` against the wrong total instead of `numCourses`.
- Forgetting isolated nodes have indegree 0 and must be seeded.

## Related problems

- 210 Course Schedule II
- 269 Alien Dictionary
- 310 Minimum Height Trees
- 802 Find Eventual Safe States
