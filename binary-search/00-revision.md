# Binary Search Interview Revision

## Core idea

Binary search is useful when the search space is ordered or monotonic. Each step asks one question: can I safely remove half of the remaining options?

Time complexity is usually `O(log n)` for direct array search. For binary search on answer space, it is usually `O(log range * cost_of_check)`.

## How to recognize it

- The input is sorted, rotated sorted, or can be treated as ordered.
- The question asks for `first`, `last`, `minimum`, `maximum`, `smallest`, `largest`, `closest`, or an insertion position.
- The problem has a yes/no condition that changes once, like `False False False True True`.
- The answer is not necessarily an index; it may be a value in a possible range.
- A brute-force solution tries every possible answer, but checking one answer is easy.

## Interview thinking steps

1. Identify the search space: indices, values, capacity, speed, day, distance, etc.
2. Decide what `lo` and `hi` mean.
3. Define the condition clearly.
4. Check if the condition is monotonic.
5. Decide whether you need the first valid answer, last valid answer, or exact match.
6. Move only one boundary each iteration.
7. Return the boundary or saved result intentionally.

## Standard exact-search template

Use this when searching for a target in a sorted array.

```python
lo, hi = 0, len(nums) - 1

while lo <= hi:
    mid = (lo + hi) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1

return -1
```

## Boundary-search template

Use this for first occurrence, last occurrence, insertion position, and minimum valid answer.

```python
lo, hi = 0, len(nums) - 1
ans = -1

while lo <= hi:
    mid = (lo + hi) // 2

    if condition(mid):
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1

return ans
```

For last valid answer, keep `ans = mid` but move `lo = mid + 1` when the condition is true.

## Binary search on answer

Use this when the answer lies in a numeric range and a helper function can check feasibility.

Examples:

- Minimum speed to arrive on time.
- Minimum capacity to ship packages within days.
- Minimum eating speed.
- Kth smallest value in a sorted matrix.

Thinking pattern:

```python
def can(answer):
    # return True if this answer is possible
    pass

lo, hi = minimum_possible, maximum_possible

while lo < hi:
    mid = (lo + hi) // 2

    if can(mid):
        hi = mid
    else:
        lo = mid + 1

return lo
```

Key point: `can(mid)` must be monotonic. If a speed works, then any bigger speed also works. If a capacity works, then any bigger capacity also works.

## Common variants

### First occurrence

- Condition: `nums[mid] >= target`
- Move left when condition is true.
- After the loop, verify `nums[lo] == target` if needed.

### Last occurrence

- Condition: `nums[mid] <= target`
- Move right when condition is true.
- Save answer only when `nums[mid] == target`, or verify after the loop.

### Search insert position

- Find the first index where `nums[i] >= target`.
- Return `lo` after the loop.

### Rotated sorted array

- At every `mid`, one half is still sorted.
- First identify the sorted half.
- Then check whether the target lies inside that half.
- Discard the other half.

### Minimum in rotated sorted array

- Compare `nums[mid]` with `nums[hi]`.
- If `nums[mid] > nums[hi]`, the minimum is on the right.
- Otherwise, the minimum is at `mid` or on the left.

## Pitfalls to avoid

- Do not use binary search unless the search space is sorted or monotonic.
- Be clear whether your loop is `while lo <= hi` or `while lo < hi`.
- Avoid infinite loops by ensuring `lo` or `hi` changes every iteration.
- For boundary questions, do not return immediately when you find the target; keep searching left or right.
- For answer-space problems, spend most of the explanation on the `can()` function.
- Watch empty arrays, single-element arrays, duplicate values, and target outside the range.
- In languages with fixed integer sizes, compute mid as `lo + (hi - lo) // 2`.

## What to say in an interview

Start with:

> Since the search space is monotonic, I can use binary search and eliminate half of the options each time.

Then explain:

- What the search space is.
- What condition you are checking at `mid`.
- Why the condition is monotonic.
- Which side you discard and why.
- What the return value represents.

End with:

> The loop runs logarithmically over the search space, and each check costs `X`, so the total time is `O(log n)` or `O(log range * X)`.

## Quick self-check before coding

- What are `lo` and `hi` initialized to?
- Am I finding an exact value, first valid value, or last valid value?
- Is my condition monotonic?
- When condition is true, do I move left or right?
- What should I return if the target does not exist?
- Does the solution work for one element?
