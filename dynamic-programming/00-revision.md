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

## Worked example

House Robber on `[2, 7, 9, 3, 1]` with the two rolling states
`rob` (best if we take the current house) and `skip` (best if we do not):

1. Start `rob=0, skip=0`.
2. num=2 -> `rob = skip + 2 = 2`, `skip = max(0,0) = 0` -> `(2, 0)`.
3. num=7 -> `rob = 0 + 7 = 7`, `skip = max(2,0) = 2` -> `(7, 2)`.
4. num=9 -> `rob = 2 + 9 = 11`, `skip = max(7,2) = 7` -> `(11, 7)`.
5. num=3 -> `rob = 7 + 3 = 10`, `skip = max(11,7) = 11` -> `(10, 11)`.
6. num=1 -> `rob = 11 + 1 = 12`, `skip = max(10,11) = 11` -> `(12, 11)`.

Answer `max(12, 11) = 12` (rob houses 2, 9, 1). The recurrence
`dp[i] = max(dp[i-1], dp[i-2] + num)` is compressed into two scalars, giving
`O(n)` time and `O(1)` space.
