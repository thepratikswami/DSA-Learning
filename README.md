# DSA Learning

This repository is organized around core DSA patterns and contains solved
LeetCode-style Python problems for each pattern.

- `binary-search`
- `sliding-window`
- `two-pointers`
- `hashing`
- `prefix-sum`
- `stack`
- `heap`
- `linked-list`
- `trees`
- `graphs`
- `backtracking`
- `dynamic-programming`
- `greedy`
- `intervals`
- `bit-manipulation`
- `trie`

Each topic folder contains:

- `README.md`: a beginner-friendly overview of the pattern.
- `revision.md`: a quick interview revision sheet to read before solving problems.
- Named problem files with `Solution` implementations.
- A small debug runner block in most problem files for quick local execution.

## How To Use

1. Start with the `README.md` in each subfolder.
2. Read the pattern identification tips.
3. Review `revision.md` before solving problems in that folder.
4. Open a problem file and study the matching pattern implementation.
5. Run or debug the file locally when a debug block is present.

## Add New Problems

Create a new starter file whenever you want to solve a problem:

```bash
python3 create_solution.py
```

`create_solution.py` asks you to choose a topic folder and enter the LeetCode
method name. It creates a starter file in that folder using the snake_case
version of the method name.