# Trie Interview Revision

## Core idea

Store strings by prefix so search and prefix checks walk one character at a time.

## How to recognize it

- The problem asks for prefix lookup.
- You need to add and search words repeatedly.
- Wildcard or board search can prune by prefixes.
- Many words share starting characters.

## Interview thinking steps

1. Define a trie node with children and end marker.
2. Insert words character by character.
3. Search by walking through children.
4. For wildcard search, DFS over all children when needed.
5. For board search, combine grid DFS with trie pruning.

## Pitfalls

- Forgetting to mark the end of a word.
- Treating prefix existence as full-word existence.
- Excessive memory from unnecessary node fields.
- Not backtracking visited cells in board search.

## Complexity

Insert and exact search are `O(L)` for word length `L`. Space is proportional to the total characters stored.
