# 1442. Count Triplets That Can Form Two Arrays of Equal XOR

- **Difficulty:** Medium
- **Pattern:** hashing (prefix XOR)
- **Companies:** Amazon
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Count triplets `(i, j, k)` with `i < j <= k` where the XOR of `arr[i..j-1]`
equals the XOR of `arr[j..k]`.

## Approaches

### Brute force

Precompute prefix XORs, then try all `(i, k)` pairs; any `j` in between works
when `prefix[i] == prefix[k+1]`.

- Time: `O(n^2)` (or `O(n^3)` naively)
- Space: `O(n)`

### Optimal

The two halves have equal XOR exactly when `prefix[i] == prefix[k+1]`. For each
`k`, every earlier index with the same prefix XOR contributes `(k - i)` valid
`j` positions. Maintain, per prefix value, both its count and the sum of its
indices to add all contributions in one pass.

- Time: `O(n)`
- Space: `O(n)`

## Key insight

`equal XOR of the two halves` ⇔ `total XOR of arr[i..k] is 0` ⇔
`prefix[i] == prefix[k+1]`, which collapses `j` into a free choice and lets a
count + index-sum map accumulate all triplets linearly.

## Edge cases

- Zeros in the array (still contribute valid triplets).
- Single matching prefix pair yields multiple `j` values.

## Pitfalls

- Off-by-one in aligning prefix indices with the `i < j <= k` bounds.
- Tracking only counts without the index sums, which forces `O(n^2)`.

## Related problems

- 560 Subarray Sum Equals K
- 1310 XOR Queries of a Subarray
