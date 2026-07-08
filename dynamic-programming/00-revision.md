# Dynamic Programming Interview Revision

## Core idea

Use saved subproblem answers when the same state appears multiple times.

## How to recognize it

- The problem asks for count, min, max, longest, or possible/impossible.
- Choices branch recursively.
- The same `(index, remaining)` or `(i, j)` state repeats.
- Greedy local choices are not obviously safe.

## Interview thinking steps

1. Define the state.
2. Define the recurrence.
3. Define base cases.
4. Choose memoization or tabulation.
5. Identify answer location.
6. Optimize space only after correctness is clear.

## Pitfalls

- Vague state definitions.
- Missing base cases.
- Using greedy when future choices matter.
- Incorrect iteration order for 0/1 knapsack-style problems.

## Complexity

Time is usually number of states times transition cost. Space is usually number of states unless optimized.
