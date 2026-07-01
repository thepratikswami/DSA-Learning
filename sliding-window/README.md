# Sliding Window

## What sliding window is all about

Sliding window is a technique for solving problems on contiguous subarrays or substrings. It maintains a window of elements and moves the window across the input while updating a running state.

### When to use sliding window

- When the problem asks for maximum/minimum/average over subarrays or substrings.
- When the problem involves contiguous elements of an array or string.
- When you need to find the shortest or longest segment satisfying a condition.
- When the window state can be updated by adding one element and removing another.

## Pattern hacks to identify sliding-window problems

- Keywords: `subarray`, `substring`, `window`, `longest`, `shortest`, `at most`, `exactly`, `continuous`, `consecutive`, `contains all`, `sum`, `average`.
- When the input asks for real-time or sequential scanning of consecutive values.
- When you can update results by adding one element and removing another.

## Common strategies

- Use a start and end pointer to define the window.
- Expand the window by moving the end pointer.
- Shrink the window by moving the start pointer once the condition is met or exceeded.
- Maintain counts, sums, or other aggregates as you slide.

## Example problems

1. Minimum Size Subarray Sum: find the smallest window with sum at least target.
2. Longest Substring Without Repeating Characters: expand and shrink the window while tracking unique chars.
3. Sliding Window Maximum: maintain a deque of candidate values for each window.
4. Find All Anagrams in a String: use a fixed-size window with count matching.

## Template that solves most variable-size questions

Most variable-size sliding-window problems follow this structure: expand the window, update state, shrink while needed, then update the answer.

```python
left = 0
state = initialize_state()
result = default_value

for right, value in enumerate(nums):
    state = add(state, value)

    while window_is_invalid(state):
        state = remove(state, nums[left])
        left += 1

    result = update_result(result, state, left, right)

return result
```

- `add(state, value)` updates the window state as it expands.
- `window_is_invalid(state)` decides when the current window must shrink.
- `remove(state, nums[left])` removes the leftmost value as the window shrinks.
- For minimum-size windows, update the result inside a `while window_is_valid(...)` loop before shrinking.

## Notes

Sliding window often reduces brute-force O(n^2) checks to O(n). The key is to keep the state updated incrementally and avoid recomputing the full window each time.

For a quick pre-practice refresher, read `revision.md`.
