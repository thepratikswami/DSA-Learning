# Mock Interview Checklist

Solving problems alone is necessary but not sufficient. Interviews also test
communication, structured problem solving, and coding under a clock. Run timed
mocks (35-45 minutes) and grade yourself against this checklist.

## Before you code (first 5-10 minutes)

- [ ] Restate the problem in your own words.
- [ ] Ask clarifying questions (input size, ranges, types, duplicates, empty input, negatives, sorted?).
- [ ] State at least one concrete example, including an edge case.
- [ ] Say a brute-force idea and its complexity out loud.
- [ ] Identify the pattern (use `study/pattern-flashcards.md`).
- [ ] Describe the optimal approach and target complexity **before** coding.
- [ ] Get the interviewer's buy-in on the approach.

## While coding

- [ ] Narrate what you are writing and why.
- [ ] Use clear names; keep functions small.
- [ ] Handle edge cases you called out earlier.
- [ ] Avoid silent assumptions; verbalize invariants (e.g. "lo is the first index where...").
- [ ] Do not go silent for long stretches — think out loud.

## After coding

- [ ] Dry-run the code on your example, tracing variables line by line.
- [ ] Test edge cases: empty, single element, all-same, max size, negatives.
- [ ] State final time and space complexity.
- [ ] Mention one possible optimization or trade-off.

## Communication rubric (self-grade 1-5)

| Dimension | 1 (weak) | 5 (strong) |
| --------- | -------- | ---------- |
| Clarifying | Jumped straight to code | Asked precise, relevant questions |
| Approach | Coded before a plan | Justified optimal plan up front |
| Coding | Messy, buggy | Clean, correct, incremental |
| Testing | Skipped | Traced + covered edge cases |
| Communication | Silent | Continuous, structured narration |

## Common failure modes to avoid

- Optimizing prematurely before a working idea exists.
- Not verifying the brute force is correct before optimizing.
- Off-by-one errors from not defining what `lo`/`hi`/pointers mean.
- Forgetting to handle empty or single-element inputs.
- Claiming a complexity without justifying it.
- Freezing silently — always say what you are considering next.

## Weekly mock cadence

- 2 mocks per week during focused prep.
- Alternate a topic you are strong in with one you are weak in.
- After each mock, log the problem in your spaced-repetition list with a
  confidence rating (see `study/spaced-repetition.md`).
