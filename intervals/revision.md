# Intervals Interview Revision

## Core idea

Sort intervals so overlaps and ordering decisions become local comparisons.

## How to recognize it

- Input contains start and end times.
- The question asks to merge, insert, remove, or count overlaps.
- Meeting room questions involve simultaneous active intervals.

## Interview thinking steps

1. Decide whether to sort by start or end.
2. Define what overlap means for the problem.
3. Keep the current merged interval or active end times.
4. For meeting rooms, use a min-heap of end times.
5. Be clear whether touching endpoints count as overlap.

## Pitfalls

- Sorting by start when end time is needed for greedy scheduling.
- Mishandling `start == end` or touching intervals.
- Mutating input unexpectedly when that matters.
- Forgetting empty input.

## Complexity

Most interval solutions are `O(n log n)` time due to sorting and `O(n)` space.
