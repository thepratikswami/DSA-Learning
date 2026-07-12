# Stack Interview Revision

## Core idea

Use a stack when the most recent unresolved value should be resolved before older values.

## How to recognize it

- Parentheses or nested expressions.
- Next greater, next warmer, next smaller.
- Removing or resolving elements based on nearby values.
- Histogram or rectangle-width questions.

## Interview thinking steps

1. Decide what each stack entry stores: value, index, pair, or state.
2. Define when to pop.
3. Define what answer is produced when an item is popped.
4. Push the current item if it remains unresolved.
5. Handle remaining stack items after the loop if needed.

## Pitfalls

- Storing values when indices are needed for distance or width.
- Using the wrong monotonic direction.
- Forgetting sentinel values for histogram-style problems.
- Not validating final stack emptiness for parentheses.

## Complexity

Usually `O(n)` time and `O(n)` space because each item is pushed and popped at most once.

## Worked example

Daily Temperatures with `temps = [73, 74, 75, 71, 76]`, using a monotonic
decreasing stack of indices and `ans = [0, 0, 0, 0, 0]`.

1. `i=0, temp=73`. Stack empty. Push `0`. Stack `[0]`.
2. `i=1, temp=74`. `temps[0]=73 < 74`, pop `0`, set `ans[0] = 1 - 0 = 1`.
   Push `1`. Stack `[1]`, `ans = [1, 0, 0, 0, 0]`.
3. `i=2, temp=75`. `temps[1]=74 < 75`, pop `1`, set `ans[1] = 2 - 1 = 1`.
   Push `2`. Stack `[2]`, `ans = [1, 1, 0, 0, 0]`.
4. `i=3, temp=71`. `temps[2]=75 > 71`, no pop. Push `3`. Stack `[2, 3]`.
5. `i=4, temp=76`. `temps[3]=71 < 76`, pop `3`, `ans[3] = 4 - 3 = 1`.
   `temps[2]=75 < 76`, pop `2`, `ans[2] = 4 - 2 = 2`. Push `4`. Stack `[4]`.
6. Loop ends. Remaining index `4` stays `0` (no warmer day).

Result: `ans = [1, 1, 2, 1, 0]`. Each index is pushed and popped once, giving
`O(n)`.
