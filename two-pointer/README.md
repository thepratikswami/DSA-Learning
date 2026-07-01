# Two-Pointer

## What two-pointer is all about

Two-pointer is a technique that uses two indices moving through a data structure to solve problems efficiently. It is most common on sorted arrays or linked lists.

### When to use two-pointer

- When the array is sorted or can be treated in order.
- When you need to find pairs or triplets satisfying a condition.
- When you need to check for palindromes or compare opposite ends.

## Pattern hacks to identify two-pointer problems

- Keywords: `sorted`, `pair`, `sum`, `triplet`, `close`, `next`, `left`, `right`, `palindrome`, `reverse`.
- When the problem asks for pairs or combinations from a list with a target.
- When you can shrink the search space by moving pointers inward or outward.

## Common strategies

- Use `left` and `right` pointers on a sorted array to find sums.
- Move one pointer forward or backward based on the current condition.
- Use one pointer to iterate and the other to search or compare.
- Use opposite ends for palindrome checking or partitioning.

## Example problems

1. Two Sum II - Input Array Is Sorted: use left and right pointers to find a pair that sums to target.
2. Container With Most Water: maximize area by moving the lower-height pointer.
3. 3Sum: fix one value and use two-pointer to find remaining pair.
4. Valid Palindrome: compare characters from both ends toward the center.

## Template that solves >90% of questions

Two-pointer problems usually use a small template: initialize pointers, evaluate the current pair, and move one pointer based on the condition.

```python
left, right = 0, len(nums) - 1
result = default_value
while left < right:
    current = evaluate(nums[left], nums[right])
    if condition(current):
        result = update_result(result, left, right)
        left += 1  # or right -= 1 depending on problem
    else:
        right -= 1  # or left += 1 based on comparison
return result
```

- `evaluate(nums[left], nums[right])` computes the current pair state.
- `condition(current)` is problem-specific: sum, difference, or match.
- Update the pointer movement rule depending on sorted order or palindrome checks.

## Notes

Two-pointer is powerful when the input order helps reduce complexity from O(n^2) to O(n). It is a strong alternative to nested loops for sorted or sequential data.
