# Greedy

## What greedy is all about

Greedy algorithms make the best local choice and rely on a proof that this choice leads to a global optimum.

### When to use greedy

- Jump and reachability problems.
- Interval scheduling.
- Problems where sorting reveals a safe choice.
- Minimizing or maximizing with exchange-style reasoning.

## Pattern hacks to identify greedy problems

- Keywords: `minimum`, `maximum`, `fewest`, `can reach`, `intervals`, `non-overlapping`.
- A local best choice seems safe and can be justified.
- DP works, but a simpler state summary is enough.

## Common strategies

- Track the farthest reachable point.
- Sort intervals by end time for scheduling.
- Keep the best current candidate while scanning.
- Prove that replacing any other choice with the greedy one does not hurt.

## Template

```python
best = initial_value
for x in items:
    best = update_best_choice(best, x)
```

## Notes

Greedy needs a reason. In interviews, explain why the local choice is safe.
