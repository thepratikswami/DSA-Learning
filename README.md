# DSA Learning

This learning repository focuses on core algorithmic patterns used in problem solving:

- `hashing`
- `two-pointer`
- `sliding-window`
- `binary-search`

Each folder contains:

- `README.md`: a beginner-friendly overview of the pattern.
- `revision.md`: a quick interview revision sheet to read before solving problems.
- `problem_01.py` to `problem_10.py`: generic LeetCode-style starter templates.

## How to use this repository

1. Start with the `README.md` in each subfolder.
2. Read the pattern identification tips.
3. Read `revision.md` before starting LeetCode problems.
4. Walk through the example problems and solutions.
5. Practice by applying the technique to new problems.

## Python problem templates

Each pattern folder has 10 starter files. Pick one, replace `defaultMethodName`
with the LeetCode method name, add your arguments and solution, then run:

```bash
python3 rename_solutions.py
```

The script scans every folder, finds `class Solution`, and renames any template
whose method is no longer `defaultMethodName`. For example, changing the method
to `findSubString` renames the file to `find_sub_string.py` and updates the
`main()` call to use `solution.findSubString(...)`.

To preview changes first:

```bash
python3 rename_solutions.py --dry-run
```
