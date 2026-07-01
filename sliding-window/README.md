# Sliding Window

## What sliding window is all about

Sliding window is a technique for solving problems on contiguous subarrays or substrings. It maintains a window of elements and moves the window across the input while updating a running state.

### When to use sliding window

- When the problem asks for maximum/minimum/average over subarrays or substrings.
- When the problem involves contiguous elements of an array or string.
- When you need to find the shortest or longest segment satisfying a condition.

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

## Template that solves >90% of questions

Most sliding-window problems can be solved with a fixed structure: expand the window, update state, and shrink when needed.

```python
start = 0
state = initialize_state()
result = default_value
for end, value in enumerate(nums):
    state = add(state, value)
    while should_shrink(state):
        result = update_result(result, state, start, end)
        state = remove(state, nums[start])
        start += 1
    result = update_result(result, state, start, end)
return result
```

- `add(state, value)` updates the window state as it expands.
- `should_shrink(state)` decides when the current window is too large or invalid.
- `remove(state, nums[start])` removes the leftmost value as the window shrinks.

## Notes

Sliding window often reduces brute-force O(n^2) checks to O(n). The key is to keep the state updated incrementally and avoid recomputing the full window each time.
