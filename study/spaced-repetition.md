# Spaced Repetition

Solving a problem once is not enough to recall it under interview pressure. Use
spaced repetition to move patterns into long-term memory with minimal time.

## The schedule

When you solve a problem, schedule reviews at increasing intervals. A review
means: re-read your own note, then re-derive the optimal idea from memory
(you do not have to re-type the whole solution unless you struggle).

| Review | When | What to do |
| ------ | ---- | ---------- |
| R1 | Same day, a few hours later | Recall the key insight and complexity. |
| R2 | Day 3 | Re-derive the approach from the problem statement. |
| R3 | Day 7 | Re-code the core loop from scratch. |
| R4 | Day 14 | Explain it out loud as if teaching. |
| R5 | Day 30 | Quick confidence check; retire if solid. |

If you fail a review (could not recall the approach), reset that problem to R1.

## Confidence ratings

After each attempt, tag yourself mentally:

- **Green** — solved cleanly from memory. Follow the schedule above.
- **Yellow** — solved with hints. Shorten intervals (review again in 1-2 days).
- **Red** — could not solve. Re-study today, review tomorrow, restart the ladder.

## A lightweight tracking method

The [Progress Tracker](../README.md#progress-tracker) checkboxes mark what you
have solved at least once. For review scheduling, keep a simple running list
(a plain text file or a spreadsheet) with three columns:

```
problem            next-review   confidence
graphs/200         2026-07-16    green
dynamic-programming/322  2026-07-11   yellow
```

Sort by `next-review` and work the top of the list each day. Run
`python create_solution.py --progress` any time to see overall coverage.

## Interleaving beats blocking

Do not grind one topic to completion and forget it. Mix topics within a session
(e.g. one graph + one DP + one review problem). Interleaving is harder in the
moment but produces far better retention and pattern-recognition transfer, which
is exactly what interviews test.
