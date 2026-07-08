# Intervals

## What intervals are all about

Interval problems deal with ranges that may overlap, touch, or need ordering.

### When to use interval patterns

- Merging overlapping intervals.
- Inserting a new interval.
- Counting meeting rooms.
- Removing overlaps.

## Pattern hacks to identify interval problems

- Keywords: `interval`, `meeting`, `start`, `end`, `overlap`, `merge`.
- The input is a list of `[start, end]` ranges.
- Sorting by start or end simplifies the problem.

## Common strategies

- Sort intervals by start time for merging.
- Sort by end time for removal or scheduling.
- Use a min-heap of end times for meeting rooms.
- Compare current start with previous end to detect overlap.

## Template

```python
intervals.sort()
merged = []

for start, end in intervals:
    if not merged or start > merged[-1][1]:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)
```

## Notes

Most interval problems become much easier after choosing the right sort order.
