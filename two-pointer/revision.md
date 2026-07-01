# Two-Pointer Interview Revision

## Core idea

Two-pointer is used when two indices can move through the input to avoid checking every pair or every position. It is especially useful for sorted arrays, palindromes, reversals, partitioning, and linked-list problems.

The main idea is to move pointers based on information from the current state, instead of using nested loops.

Time complexity is usually `O(n)` after sorting, or `O(n log n)` if sorting is required first.

## How to recognize it

- The input is sorted, or sorting is allowed.
- The problem asks for a pair, triplet, closest sum, or target sum.
- You need to compare values from both ends.
- The problem asks for palindrome checking, reversing, merging, or partitioning.
- A brute-force solution checks all pairs, but sorted order can tell you which pointer to move.
- You need fast and slow pointers in a linked list or array.

## Interview thinking steps

1. Decide which two pointers you need.
2. Decide where they start.
3. Define what the current pointer state means.
4. Use the current comparison to move one pointer.
5. Make sure every move discards only impossible choices.
6. Update the answer before or after moving pointers intentionally.
7. Stop when the pointers cross or when the traversal is complete.

## Opposite-ends template

Use this for sorted pair problems, palindrome checks, and inward scans.

```python
left, right = 0, len(nums) - 1
ans = default_value

while left < right:
    current = evaluate(nums[left], nums[right])

    if current == target:
        ans = update_answer(ans, left, right)
        left += 1
        right -= 1
    elif current < target:
        left += 1
    else:
        right -= 1

return ans
```

Key point: in a sorted array, if the sum is too small, move `left` right to increase it. If the sum is too large, move `right` left to decrease it.

## Same-direction template

Use this when one pointer scans and the other stores the next write position or valid boundary.

```python
write = 0

for read in range(len(nums)):
    if should_keep(nums[read]):
        nums[write] = nums[read]
        write += 1

return write
```

Common use cases:

- Remove duplicates from sorted array.
- Move zeroes.
- Remove element.
- Partition array.

## Fast and slow pointer template

Use this for cycle detection, middle of linked list, or finding a meeting point.

```python
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

return slow
```

Common use cases:

- Linked list cycle.
- Middle of linked list.
- Happy number.
- Find duplicate number.

## Triplet template

Use this when the problem asks for three values and sorting is allowed.

```python
nums.sort()
ans = []

for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    left, right = i + 1, len(nums) - 1

    while left < right:
        total = nums[i] + nums[left] + nums[right]

        if total == 0:
            ans.append([nums[i], nums[left], nums[right]])
            left += 1
            right -= 1

            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif total < 0:
            left += 1
        else:
            right -= 1

return ans
```

Key point: sort first, fix one value, then solve the remaining pair problem with two pointers.

## Common variants

### Two Sum II

- Input is already sorted.
- Start with `left = 0` and `right = n - 1`.
- Move `left` if sum is too small.
- Move `right` if sum is too large.

### 3Sum

- Sort the array.
- Fix one number.
- Use two pointers for the remaining target.
- Skip duplicates for both the fixed number and inner pointers.

### Container With Most Water

- Area is `min(height[left], height[right]) * width`.
- Move the pointer with the smaller height.
- Moving the taller one cannot improve the limiting height.

### Valid Palindrome

- Compare characters from both ends.
- Move both pointers inward when they match.
- Skip non-alphanumeric characters if the problem asks for it.

### Remove Duplicates From Sorted Array

- Use `read` to scan.
- Use `write` to place the next unique value.
- Return the final write index as the new length.

### Linked List Cycle

- Move `slow` by one and `fast` by two.
- If they meet, there is a cycle.
- If `fast` reaches the end, there is no cycle.

## Pitfalls to avoid

- Two-pointer pair logic usually needs sorted order.
- If you sort, check whether the problem requires original indices.
- Do not skip duplicate values before recording a valid answer.
- Be careful with `left < right` vs `left <= right`.
- Make sure each loop iteration moves at least one pointer.
- For linked lists, always check `fast` and `fast.next` before moving two steps.
- For in-place problems, know whether to return the modified array or the new length.
- Sorting changes time complexity to `O(n log n)`.

## What to say in an interview

Start with:

> Since the input order gives me a way to discard impossible choices, I can use two pointers instead of checking every pair.

Then explain:

- Where each pointer starts.
- What the current pair or state means.
- Why the chosen pointer movement is correct.
- How duplicates or edge cases are handled.
- Whether sorting is required.

End with:

> Each pointer moves in one direction and visits each element at most once, so the scan is `O(n)`. If sorting is needed, the total time is `O(n log n)`.

## Quick self-check before coding

- Are the values sorted, or am I allowed to sort them?
- Do I need original indices?
- Should pointers start at opposite ends or move in the same direction?
- What exact condition moves `left`?
- What exact condition moves `right`?
- Can duplicates affect the answer?
- Does the loop stop correctly for arrays of length `0`, `1`, and `2`?
