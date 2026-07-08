# Hashing Interview Revision

## Core idea

Hashing is used when you need fast lookup, counting, grouping, or duplicate detection. In LeetCode, this usually means using a `set` or `dict` so that checking whether something exists takes `O(1)` average time.

Most hashing problems replace a nested loop with one pass and a memory structure that remembers useful information from earlier elements.

Time complexity is usually `O(n)` and space complexity is usually `O(n)`.

## How to recognize it

- The problem asks for `duplicate`, `unique`, `frequency`, `count`, `seen`, or `exists`.
- You need to quickly check whether a value appeared before.
- You need to count how many times each value appears.
- You need to group items by a shared property, like anagrams.
- A brute-force solution checks every pair, but you only need to know if a complement exists.
- The problem involves prefix sums, remainders, or repeated states.

## Interview thinking steps

1. Decide what you need to look up quickly.
2. Choose `set` for existence or `dict` for counts/details.
3. Define the key clearly.
4. Decide what value to store for each key.
5. While iterating, check first or update first depending on the problem.
6. Update the answer using the stored information.
7. Handle missing keys and edge cases carefully.

## Set template

Use this when you only need to know whether something has appeared before.

```python
seen = set()

for x in nums:
    if x in seen:
        return True
    seen.add(x)

return False
```

Common use cases:

- Contains duplicate.
- First repeated element.
- Longest consecutive sequence.
- Fast membership checks.

## Frequency map template

Use this when the answer depends on counts.

```python
freq = {}

for x in nums:
    freq[x] = freq.get(x, 0) + 1

for key, count in freq.items():
    if condition(key, count):
        return key
```

Common use cases:

- Majority element.
- Valid anagram.
- Top K frequent elements.
- First unique character.

## Complement lookup template

Use this when you need pairs that satisfy a target condition.

```python
seen = {}

for i, x in enumerate(nums):
    need = target - x

    if need in seen:
        return [seen[need], i]

    seen[x] = i
```

Key point: check for the complement before storing the current value when the same element cannot be used twice.

## Grouping template

Use this when many items share the same transformed key.

```python
groups = {}

for item in items:
    key = transform(item)

    if key not in groups:
        groups[key] = []

    groups[key].append(item)

return list(groups.values())
```

For anagrams, common keys are:

- `''.join(sorted(word))`
- A tuple of 26 character counts.

Use a tuple for list-like keys because lists are not hashable.

## Prefix sum hash map template

Use this when the problem asks about subarray sums, counts, or repeated running states.

```python
count = {0: 1}
prefix = 0
ans = 0

for x in nums:
    prefix += x

    need = prefix - k
    ans += count.get(need, 0)

    count[prefix] = count.get(prefix, 0) + 1

return ans
```

Why this works:

- Current prefix sum is `prefix`.
- If an earlier prefix was `prefix - k`, then the subarray between that earlier point and now sums to `k`.
- `count` stores how many times each previous prefix sum appeared.

Common use cases:

- Subarray Sum Equals K.
- Continuous Subarray Sum.
- Binary subarrays with sum.
- Count subarrays divisible by K.

## Common variants

### Two Sum

- Store value -> index.
- For each value, check if `target - value` already exists.
- Return as soon as the complement is found.

### Valid Anagram

- Count characters in both strings, or increment for one string and decrement for the other.
- If all counts become zero, the strings are anagrams.

### Group Anagrams

- Convert each word into a canonical key.
- Store key -> list of words.
- Return the grouped values.

### Longest Consecutive Sequence

- Put all numbers in a set.
- Start counting only when `num - 1` is not in the set.
- Expand while `num + length` exists.

### Subarray Sum Equals K

- Use prefix sum counts.
- Add `count[prefix - k]` to the answer before storing current prefix.

### Count Subarrays Divisible By K

- Store remainder frequencies.
- If two prefix sums have the same remainder, the subarray between them is divisible by `k`.
- Normalize remainder if the language can produce negative remainders.

## Pitfalls to avoid

- Do not use a list as a dictionary key; use a tuple or string.
- Be careful with check-first vs update-first.
- Initialize prefix maps correctly, often with `{0: 1}`.
- For pair problems, avoid using the same index twice.
- For frequency maps, remember to delete keys with zero count if the number of distinct keys matters.
- Hash maps use extra space, usually `O(n)`.
- Average lookup is `O(1)`, but sorting-based alternatives may be better when memory is restricted.
- If order matters, remember that a set does not solve ordering by itself.

## What to say in an interview

Start with:

> I can use a hash map because I need fast lookups of previously seen values.

Then explain:

- What your key represents.
- What your value stores.
- Whether you check before or after updating the map.
- How the map helps avoid a nested loop.
- What edge cases the initialization handles.

End with:

> I scan the input once, and each hash map operation is average `O(1)`, so the time complexity is `O(n)` and the space complexity is `O(n)`.

## Quick self-check before coding

- Do I need a `set` or a `dict`?
- What exactly is the hash key?
- What value should I store for that key?
- Should I check the map before updating it?
- Do I need counts, indices, lists, or booleans?
- Have I initialized empty-prefix or empty-state cases?
- Can there be duplicates, negative numbers, or empty input?
