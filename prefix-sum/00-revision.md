# Prefix Sum Interview Revision

## Core idea

Store cumulative information so the value for a range can be computed from two saved states.

## How to recognize it

- You need sums over many ranges.
- The problem asks for subarrays with a target sum.
- You need to compare left and right totals.
- A brute-force solution repeatedly recomputes totals.

## Interview thinking steps

1. Define what the prefix value means.
2. Decide whether you need a prefix array or a running variable.
3. For counts, store previous prefix values in a dictionary.
4. Use `current - previous` to represent a subarray or range.
5. Initialize carefully, often with prefix value `0`.

## Pitfalls

- Off-by-one errors in prefix arrays.
- Forgetting `{0: 1}` for subarray count problems.
- Updating the map before checking when the current index should not count itself.
- Confusing subarray with subsequence.

## Complexity

Most prefix-sum solutions are `O(n)` time. Space is `O(1)` for a running sum, `O(n)` for a prefix array or hash map.

## Worked example

Subarray Sum Equals K on `nums = [1, 1, 1]`, `k = 2`, using a running prefix and a
count map seeded with `{0: 1}` (so prefixes that themselves equal `k` count):

1. Start `prefix = 0`, `counts = {0: 1}`, `ans = 0`.
2. num=1 -> `prefix = 1`. Need `prefix - k = -1`; `counts[-1]` absent -> `ans = 0`. Record -> `counts = {0:1, 1:1}`.
3. num=1 -> `prefix = 2`. Need `2 - 2 = 0`; `counts[0] = 1` -> `ans = 1`. Record -> `counts = {0:1, 1:1, 2:1}`.
4. num=1 -> `prefix = 3`. Need `3 - 2 = 1`; `counts[1] = 1` -> `ans = 2`. Record -> `counts = {0:1, 1:1, 2:1, 3:1}`.

Answer `2` (subarrays `[1,1]` at indices 0-1 and 1-2). Each subarray sum is
`prefix[j] - prefix[i]`, so counting earlier prefixes equal to `prefix - k` finds
them all in one `O(n)` pass.
