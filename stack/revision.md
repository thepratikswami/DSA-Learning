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
