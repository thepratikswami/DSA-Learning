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

## Worked example

Merge Intervals with `intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]`.

1. Sort by start: `[[1, 3], [2, 6], [8, 10], [15, 18]]` (already sorted).
2. Take `[1, 3]`. `merged` empty, so append. `merged = [[1, 3]]`.
3. Take `[2, 6]`. `2 <= 3` (last end), so overlap. Extend end to
   `max(3, 6) = 6`. `merged = [[1, 6]]`.
4. Take `[8, 10]`. `8 > 6`, no overlap. Append. `merged = [[1, 6], [8, 10]]`.
5. Take `[15, 18]`. `15 > 10`, no overlap. Append.
   `merged = [[1, 6], [8, 10], [15, 18]]`.

Result: `[[1, 6], [8, 10], [15, 18]]`. Each interval only ever compares against
the most recent merged interval, so after the `O(n log n)` sort the merge is a
single `O(n)` pass.
