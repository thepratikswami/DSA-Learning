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
