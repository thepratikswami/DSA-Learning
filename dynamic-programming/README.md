# Dynamic Programming

## What dynamic programming is all about

Dynamic programming solves problems by reusing answers to overlapping subproblems.

### When to use dynamic programming

- Counting ways.
- Finding maximum or minimum value.
- Problems with choices at each position.
- Subproblems repeat.
- The current answer depends on earlier answers.

## Pattern hacks to identify DP problems

- Keywords: `ways`, `minimum`, `maximum`, `longest`, `can partition`, `choose`.
- Recursive brute force repeats the same states.
- You can define a state like `dp[i]`, `dp[i][j]`, or `(index, remaining)`.

## Common strategies

- Start with the recursive recurrence.
- Memoize repeated states.
- Convert to bottom-up tabulation when convenient.
- Optimize space when only recent states are needed.

## Template

```python
dp = [0] * (n + 1)
dp[0] = base_value

for i in range(1, n + 1):
    dp[i] = transition_from_previous_states
```

## Notes

The hardest part is defining the state. Once the state is clear, the transition usually follows.
