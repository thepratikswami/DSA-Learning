# Study Roadmap

A pattern-first path to interview readiness. Work top to bottom: each tier builds
on the previous one. Check problems off in the [Progress Tracker](../README.md#progress-tracker)
as you solve them, and run `python create_solution.py --progress` to see your
completion per topic.

## Difficulty progression

1. **Foundations (Easy-heavy).** Learn the pattern template on simple inputs.
2. **Core (Medium).** The bulk of interview questions live here.
3. **Stretch (Hard).** A few per topic to build confidence and depth.

## Recommended topic order

Solve topics in this order — earlier patterns are prerequisites for later ones.

| # | Topic | Why here |
| - | ----- | -------- |
| 1 | hashing | Hash maps/sets underpin almost everything. |
| 2 | two-pointers | Simple, high-frequency, sorted-array intuition. |
| 3 | sliding-window | Builds on two-pointers. |
| 4 | prefix-sum | Range-sum trick used across many problems. |
| 5 | binary-search | Search space + monotonic-condition thinking. |
| 6 | stack | Parsing, matching, nearest-element setup. |
| 7 | monotonic-stack | Specialization of stack for next-greater/smaller. |
| 8 | linked-list | Pointer mechanics, fast/slow. |
| 9 | trees | Recursion + BFS/DFS core. |
| 10 | trie | Prefix trees, string design. |
| 11 | heap | Top-K, streaming medians, scheduling. |
| 12 | intervals | Sorting + sweep. |
| 13 | greedy | Local-choice proofs. |
| 14 | backtracking | Exhaustive search with pruning. |
| 15 | graphs | BFS/DFS/topological/union-find. |
| 16 | advanced-graphs | Dijkstra, Bellman-Ford, MST. |
| 17 | dynamic-programming | 1-D then 2-D DP. |
| 18 | bit-manipulation | Bit tricks and masks. |
| 19 | math-geometry | Matrix + number theory. |
| 20 | design | Compose data structures (LRU, etc.). |

## Time-boxed plans

Pick the plan that matches your runway. Each assumes reading the topic
`README.md`, then `00-revision.md`, then solving problems while writing your own
notes before reading the sidecar `.md`.

### 1-week sprint (last-minute)

- **Days 1-2:** hashing, two-pointers, sliding-window, prefix-sum, binary-search.
- **Days 3-4:** stack, monotonic-stack, linked-list, trees, heap.
- **Days 5-6:** graphs, backtracking, dynamic-programming (Easy + Medium only).
- **Day 7:** intervals, greedy, design + re-review every `00-revision.md`.

### 4-week plan (balanced)

- **Week 1:** topics 1-6 (foundations + binary search + stack).
- **Week 2:** topics 7-12 (linked-list, trees, trie, heap, intervals).
- **Week 3:** topics 13-17 (greedy, backtracking, graphs, DP).
- **Week 4:** topics 18-20 + Hard problems + full mock interviews.

### 8-week plan (thorough)

- Same order as the 4-week plan but at half pace, adding:
  - A second pass over every Hard problem.
  - Two timed mock interviews per week (see
    [mock-interview-checklist.md](mock-interview-checklist.md)).
  - Weekly spaced-repetition reviews (see
    [spaced-repetition.md](spaced-repetition.md)).

## How to solve each problem

1. Read the problem; restate it in one sentence.
2. Identify the pattern using [pattern-flashcards.md](pattern-flashcards.md).
3. Brute force out loud, then optimize.
4. Code it without looking at the solution.
5. Trace one example by hand; test edge cases.
6. Only then read the sidecar `.md` note and compare approaches.
7. Check the box in the tracker and schedule a review.
