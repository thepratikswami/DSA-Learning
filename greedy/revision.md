# Greedy Interview Revision

## Core idea

Make a locally optimal choice that can be proven safe for the whole problem.

## How to recognize it

- The problem asks for minimum or maximum.
- Sorting by start, end, cost, or value makes the choice clear.
- You can maintain one best frontier or candidate.
- A DP solution can be compressed into a simple invariant.

## Interview thinking steps

1. Identify the greedy choice.
2. Define the invariant that stays true while scanning.
3. Sort if order matters.
4. Update the best reachable or selected value.
5. Explain why another choice would not improve the answer.

## Pitfalls

- Using greedy without proof.
- Sorting by the wrong key.
- Missing edge cases like empty input.
- Confusing reachability with exact landing.

## Complexity

Usually `O(n)` if no sorting is needed, or `O(n log n)` when sorting is required.
