# Trie

## What trie is all about

A trie is a prefix tree used to store strings character by character.

### When to use trie

- Prefix search.
- Word dictionary operations.
- Wildcard search.
- Word search on a board with many target words.

## Pattern hacks to identify trie problems

- Keywords: `prefix`, `dictionary`, `word`, `search`, `startsWith`.
- Many strings share prefixes.
- Repeated prefix checks would be expensive with plain scanning.

## Common strategies

- Store children in dictionaries.
- Mark word endings with a boolean or stored word.
- Use DFS with trie pruning for board search.
- Remove found words or dead branches when useful.

## Template

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
```

## Notes

Tries trade memory for fast prefix operations.
