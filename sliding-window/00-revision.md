# Sliding Window Interview Revision

## Core idea

Sliding window is used for problems about contiguous subarrays or substrings. Instead of recomputing every possible segment, keep a running state for the current window and move the window across the input.

Most sliding-window problems use two pointers:

- `left` marks the start of the window.
- `right` expands the window one element at a time.

Time complexity is usually `O(n)` because each pointer moves forward at most `n` times.

## How to recognize it

- The problem asks for a `subarray`, `substring`, `window`, or contiguous segment.
- The question asks for the longest, shortest, maximum, minimum, or count of valid windows.
- You can update the answer by adding one new element and removing old elements.
- A brute-force solution checks every start and end index.
- The condition depends on a running sum, frequency map, unique characters, or number of distinct values.

## Interview thinking steps

1. Confirm the problem is about contiguous elements.
2. Decide what state the window must maintain.
3. Move `right` to expand the window.
4. Update state using the new right-side value.
5. Decide when the window is invalid or ready to shrink.
6. Move `left` while updating state correctly.
7. Update the answer at the correct time.

## Variable-size window template

Use this for longest or shortest windows where the size changes.

```python
left = 0
state = initialize_state()
ans = default_value

for right, value in enumerate(nums):
    add value to state

    while window_is_invalid(state):
        remove nums[left] from state
        left += 1

    ans = update_answer(ans, left, right, state)

return ans
```

Key point: for longest valid window, usually shrink until valid, then update the answer.

## Minimum-size window template

Use this when you need the shortest window that satisfies a condition.

```python
left = 0
state = initialize_state()
ans = float("inf")

for right, value in enumerate(nums):
    add value to state

    while window_is_valid(state):
        ans = min(ans, right - left + 1)
        remove nums[left] from state
        left += 1

return 0 if ans == float("inf") else ans
```

Key point: when the window is valid, try to shrink it because you want the smallest valid answer.

## Fixed-size window template

Use this when every window has size `k`.

```python
window_sum = 0
ans = default_value

for right, value in enumerate(nums):
    window_sum += value

    if right >= k:
        window_sum -= nums[right - k]

    if right >= k - 1:
        ans = update_answer(ans, window_sum)

return ans
```

Key point: start updating the answer only when the window has exactly `k` elements.

## Frequency-map window template

Use this for substrings or subarrays with character counts, distinct values, or required matches.

```python
left = 0
freq = {}
ans = default_value

for right, value in enumerate(nums):
    freq[value] = freq.get(value, 0) + 1

    while window_is_invalid(freq):
        left_value = nums[left]
        freq[left_value] -= 1

        if freq[left_value] == 0:
            del freq[left_value]

        left += 1

    ans = update_answer(ans, left, right, freq)

return ans
```

Key point: delete zero-count keys when the number of distinct keys matters.

## Common variants

### Longest Substring Without Repeating Characters

- Maintain a window where every character appears at most once.
- If the new character count becomes more than `1`, shrink from the left.
- Update answer after the window becomes valid again.

### Minimum Size Subarray Sum

- Expand by adding to the sum.
- While `sum >= target`, update minimum length and shrink.
- Works cleanly when numbers are positive.

### Find All Anagrams in a String

- Use a fixed-size window of length `len(pattern)`.
- Compare frequency maps or maintain a match count.
- Record `left` when the window matches.

### Longest Repeating Character Replacement

- Maintain character counts and the max frequency in the current window.
- Window is valid if `window_size - max_freq <= k`.
- Shrink when more than `k` replacements are needed.

### Sliding Window Maximum

- Use a deque, not just a frequency map.
- Keep indices of useful candidates in decreasing value order.
- Remove indices that fall outside the window.

## Pitfalls to avoid

- Sliding window usually requires contiguous elements.
- Do not use it blindly when negative numbers break a sum condition's monotonic behavior.
- Be clear whether you update the answer before shrinking, during shrinking, or after shrinking.
- Use `right - left + 1` for window length.
- For fixed-size windows, do not update answer before the first full window.
- When using counts, remove zero-count keys if `len(freq)` matters.
- Remember that `while` shrinking is often needed, not just `if`.
- Empty strings, one-element arrays, and `k = 0` can expose bad initialization.

## What to say in an interview

Start with:

> Since the problem is asking about a contiguous window, I can scan once while maintaining the current window state.

Then explain:

- What `left` and `right` represent.
- What state you maintain.
- When the window becomes invalid or valid.
- Why moving `left` restores the condition.
- When you update the answer.

End with:

> Each element is added once and removed at most once, so the time complexity is `O(n)`. The space complexity depends on the state, usually `O(1)` or `O(k)`.

## Quick self-check before coding

- Is the problem definitely about contiguous elements?
- Is the window fixed size or variable size?
- Am I finding longest, shortest, maximum, or count?
- What condition makes the window invalid?
- Should I shrink with `while` or only once?
- When exactly should I update the answer?
- Does the logic still work for empty input and one element?

## Worked example

Variable-size window for the longest substring without repeating characters.
Input: `s = "abcabcbb"`. Keep a `seen` set and `left = 0`.

1. `right = 0..2` add `a, b, c` -> window `"abc"`, best length `3`.
2. `right = 3` value `a` already in `seen`. Shrink: remove `s[left]='a'`, `left = 1`.
   Now `a` is free; add it. Window `"bca"`, length still `3`.
3. `right = 4` value `b` repeats. Remove `s[1]='b'`, `left = 2`, add `b`.
   Window `"cab"`, length `3`.
4. `right = 5` value `c` repeats. Remove `s[2]='c'`, `left = 3`, add `c`.
   Window `"abc"`, length `3`.
5. `right = 6,7` value `b` then `b` force shrinking down to `"b"`.

Each character is added once and removed at most once, so the pass is `O(n)` and
the answer is `3`.
