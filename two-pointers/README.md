# Two-Pointer

## What two-pointer is all about

Two-pointer is a technique that uses two indices moving through a data structure to solve problems efficiently. It is most common on sorted arrays or linked lists.

### When to use two-pointer

- When the array is sorted or can be treated in order.
- When you need to find pairs or triplets satisfying a condition.
- When you need to check for palindromes or compare opposite ends.
- When you need fast/slow pointer traversal in a linked list or repeated-state problem.

## Pattern hacks to identify two-pointer problems

- Keywords: `sorted`, `pair`, `sum`, `triplet`, `close`, `next`, `left`, `right`, `palindrome`, `reverse`.
- When the problem asks for pairs or combinations from a list with a target.
- When you can shrink the search space by moving pointers inward or outward.

## Common strategies

- Use `left` and `right` pointers on a sorted array to find sums.
- Move one pointer forward or backward based on the current condition.
- Use one pointer to read and another to write for in-place array edits.
- Use opposite ends for palindrome checking or partitioning.
- Use fast and slow pointers for cycle detection or finding a middle point.

## Example problems

1. Two Sum II - Input Array Is Sorted: use left and right pointers to find a pair that sums to target.
2. Container With Most Water: maximize area by moving the lower-height pointer.
3. 3Sum: fix one value and use two-pointer to find remaining pair.
4. Valid Palindrome: compare characters from both ends toward the center.

## Opposite-ends template

Use this for sorted pair problems, palindrome checks, and inward scans.

```python
left, right = 0, len(nums) - 1
result = default_value

while left < right:
    current = evaluate(nums[left], nums[right])

    if current == target:
        result = update_result(result, left, right)
        left += 1
        right -= 1
    elif current < target:
        left += 1
    else:
        right -= 1

return result
```

- `evaluate(nums[left], nums[right])` computes the current pair state.
- Move `left` when you need a larger value from a sorted array.
- Move `right` when you need a smaller value from a sorted array.
- For palindromes, move both pointers inward when values match.

## Notes

Two-pointer is powerful when the input order helps reduce complexity from O(n^2) to O(n). It is a strong alternative to nested loops for sorted or sequential data.

For a quick pre-practice refresher, read `revision.md`.
