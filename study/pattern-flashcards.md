# Pattern Recognition Flashcards

The hardest interview skill is mapping a novel problem to a known pattern within
the first two minutes. Use these cues. Read the "If you see..." column, then try
to recall the pattern before looking.

| If you see... | Reach for | Topic |
| ------------- | --------- | ----- |
| "sorted array" + find target / boundary / peak | Binary search | binary-search |
| "minimize the max" / "maximum feasible X in a range" | Binary search on the answer | binary-search |
| Pair/triple summing to a target in a **sorted** array | Two pointers | two-pointers |
| Longest/shortest contiguous subarray/substring meeting a rule | Sliding window | sliding-window |
| Many range-sum or "subarray sums to K" queries | Prefix sum (+ hash map) | prefix-sum, hashing |
| "have I seen this before?" / dedupe / group by key | Hash map / set | hashing |
| Matching brackets, undo, nearest unresolved item | Stack | stack |
| "next greater/smaller element" / spans | Monotonic stack | monotonic-stack |
| Reverse / detect cycle / find middle of a list | Fast & slow pointers | linked-list |
| Anything on a binary tree | Recursion (DFS) or BFS | trees |
| Prefix lookups / autocomplete / word dictionary | Trie | trie |
| "top K", "K largest/closest", running median | Heap | heap |
| Overlapping ranges, meetings, merge/insert | Sort + sweep | intervals |
| Locally optimal choice provably gives global optimum | Greedy | greedy |
| Generate all combinations / permutations / subsets | Backtracking | backtracking |
| Grid/network connectivity, shortest unweighted path | BFS/DFS/union-find | graphs |
| Weighted shortest path / MST / dependency order | Dijkstra/Bellman-Ford/topo/MST | advanced-graphs |
| "count ways" / "min/max cost" with overlapping subproblems | Dynamic programming | dynamic-programming |
| Toggle/XOR/subset via bits, count set bits | Bit manipulation | bit-manipulation |
| Rotate/spiral a matrix, digit math, fast power | Math & geometry | math-geometry |
| "Design a structure with O(1)/O(log n) operations" | Compose map + list/heap/DLL | design |

## Two-minute triage

1. **What is the output?** (an index, a count, a boolean, a structure)
2. **Is the input ordered or can it be sorted cheaply?** -> binary search / two pointers / intervals.
3. **Contiguous vs. any-subset?** contiguous -> window/prefix; any-subset -> DP/backtracking.
4. **Is there overlap in subproblems?** -> DP.
5. **Is it a graph in disguise?** (states + transitions) -> BFS/DFS.
6. **What operation must be fast/repeated?** -> pick the data structure that makes it O(1)/O(log n).

## Complexity targets to state up front

| Input size `n` | Expected complexity |
| -------------- | ------------------- |
| n <= 10-12 | Exponential is fine (backtracking, bitmask). |
| n <= 20-25 | `O(2^n)` or `O(n * 2^n)` bitmask DP. |
| n <= 500 | `O(n^3)`. |
| n <= 5,000 | `O(n^2)`. |
| n <= 10^6 | `O(n log n)` or `O(n)`. |
| n > 10^7 | `O(n)` or `O(log n)`; likely math/greedy. |
