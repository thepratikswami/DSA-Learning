# Hashing

## What hashing is all about

Hashing is a technique for storing and looking up values quickly using keys. It is often implemented with hash tables, dictionaries, maps, or sets.

### When to use hashing

- When a problem asks to count frequency, find duplicates, or check membership.
- When you need O(1) average-time lookups or inserts.
- When the order of elements does not matter.

## Pattern hacks to identify hashing problems

- Keywords: `duplicate`, `unique`, `frequency`, `count`, `anagram`, `pair sum`, `two sum`, `subarray sum`, `window with unique`.
- Problem asks for quickly checking if a value has already been seen.
- Problem involves grouping by a characteristic (e.g. same letters, same remainder, same difference).

## Common strategies

- Use a dictionary or map to count values.
- Use a set to track seen items and detect duplicates.
- Use a hash map for value-to-index lookups.
- Use a map from transformed key -> list of values for grouping.
- Use prefix sums with a hash map for subarray count problems.

## Example problems

1. Two Sum: find two numbers that add up to a target using a hash map.
2. Longest Substring Without Repeating Characters: use a sliding window plus a hash map to check unique characters.
3. Group Anagrams: map each sorted word or character-frequency signature to a list of words.
4. Subarray Sum Equals K: use prefix sums and a hash map to count how many prior prefixes can form target.

## Template that solves >90% of questions

A hashing problem often follows this template: build a map or set, iterate once, and update the answer using lookup results.

```python
seen = {}
result = default_value
for item in items:
    key = transform(item)
    if key in seen:
        result = update_result(item, seen[key])
    seen[key] = store_info(item)
return result
```

- `transform(item)` generates the hash key based on the problem.
- `update_result` contains the logic specific to counts, pairs, or grouping.
- `store_info(item)` saves the data you need for later lookups.

## Notes

Hashing is a great first approach when you need fast membership tests, counting, grouping, or lookup of earlier states. Always consider edge cases like duplicates, empty input, and whether you should check the map before updating it.

For a quick pre-practice refresher, read `00-revision.md`.
