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

## Worked example

Non-overlapping Intervals on `[[1,2], [2,3], [3,4], [1,3]]`, greedy by earliest
end time (invariant: `end` = finish of the last interval we kept):

1. Sort by end -> `[[1,2], [2,3], [1,3], [3,4]]`. Start `end = -inf`, `removed = 0`.
2. `[1,2]`: `1 >= -inf` -> keep, `end = 2`.
3. `[2,3]`: `2 >= 2` -> keep, `end = 3`.
4. `[1,3]`: `1 < 3` -> overlaps, `removed = 1` (drop it, `end` unchanged).
5. `[3,4]`: `3 >= 3` -> keep, `end = 4`.

Answer `removed = 1`. The greedy choice (always keep the interval that finishes
earliest) leaves maximum room for the rest, so no other removal set is smaller.
