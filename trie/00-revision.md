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

## Worked example

Insert `"app"` and `"apple"`, then run a few queries.

```
insert("app"):     root -> a -> p -> p(is_word=True)
insert("apple"):   reuse a -> p -> p, then -> l -> e(is_word=True)
```

Resulting trie (shared prefix `app`):

```
root -> a -> p -> p(*) -> l -> e(*)
                  (*) marks is_word=True
```

1. `search("app")`: walk `a -> p -> p`, node exists and `is_word=True` -> `True`.
2. `search("ap")`:  walk `a -> p`, node exists but `is_word=False` -> `False`.
3. `startsWith("appl")`: walk `a -> p -> p -> l`, node exists -> `True`.
4. `search("apples")`: after `...e`, next char `s` not in children -> `False`.

The key move: `"app"` and `"apple"` share the same three nodes, and only the
`is_word` flag distinguishes a stored word from a passing-through prefix.
