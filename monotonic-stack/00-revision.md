# Monotonic Stack Interview Revision

## Core idea

Keep the stack sorted (increasing or decreasing) as you scan. When a new item
breaks the order, pop the dominated elements and resolve each one with the
current item.

## How to recognize it

- Next greater, next smaller, next warmer.
- Span or distance until a bigger/smaller value.
- Building an optimal string by removing characters or digits.
- Elements that merge or catch up (car fleets, stock spans).

## Interview thinking steps

1. Decide the stack direction: decreasing for next-greater, increasing for
   next-smaller.
2. Decide what each entry stores: index, value, or a pair like `(price, span)`.
3. Define the pop condition (strict vs non-strict comparison).
4. Define the answer produced when an element is popped.
5. Push the current item if it is still unresolved; handle leftovers after the
   loop.

## Pitfalls

- Wrong monotonic direction for the question asked.
- Using `<` vs `<=` incorrectly, which matters for duplicates and stability.
- Storing values when indices are needed for distance/width.
- For circular problems, forgetting to iterate `2n` with modulo indexing.
- For "smallest result" problems, popping a character that never reappears.

## Complexity

Usually `O(n)` time and `O(n)` space because each element is pushed and popped at
most once.

## Worked example

Next Greater Element with `nums = [2, 1, 2, 4, 3]`, using a decreasing stack of
indices and `ans = [-1, -1, -1, -1, -1]`.

1. `i=0, x=2`. Stack empty. Push `0`. Stack `[0]`.
2. `i=1, x=1`. `nums[0]=2 > 1`, no pop. Push `1`. Stack `[0, 1]`.
3. `i=2, x=2`. `nums[1]=1 < 2`, pop `1`, set `ans[1] = 2`.
   `nums[0]=2` is not `< 2`, stop. Push `2`. Stack `[0, 2]`,
   `ans = [-1, 2, -1, -1, -1]`.
4. `i=3, x=4`. `nums[2]=2 < 4`, pop `2`, set `ans[2] = 4`.
   `nums[0]=2 < 4`, pop `0`, set `ans[0] = 4`. Push `3`. Stack `[3]`,
   `ans = [4, 2, 4, -1, -1]`.
5. `i=4, x=3`. `nums[3]=4 > 3`, no pop. Push `4`. Stack `[3, 4]`.
6. Loop ends. Indices `3` and `4` stay `-1` (no greater element to the right).

Result: `ans = [4, 2, 4, -1, -1]`. Each index is pushed and popped once, giving
`O(n)`.
