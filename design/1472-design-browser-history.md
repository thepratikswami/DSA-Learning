# 1472. Design Browser History

- **Difficulty:** Medium
- **Pattern:** design
- **Companies:** Amazon, Microsoft, Bloomberg, Google
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/design-browser-history/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Design a browser history that starts on a homepage and supports `visit(url)`,
`back(steps)`, and `forward(steps)`. Visiting a page clears all forward history.
`back` and `forward` are clamped to the available range.

## Approaches

### Array + current pointer

Store visited urls in a list with a `current` index. `visit` truncates
everything after `current`, appends the new url, and advances the pointer.
`back` and `forward` move the pointer, clamped to `[0, len - 1]`.

- `visit`: amortized `O(1)` (plus truncation)
- `back` / `forward`: `O(1)`
- Space: `O(n)`

### Two stacks

Keep a back stack and a forward stack. `visit` pushes onto the back stack and
clears the forward stack; `back`/`forward` transfer between the two.

- Time: `O(steps)` per navigation
- Space: `O(n)`

## Key insight

A single index into an array captures the entire back/forward state, and
truncating on `visit` naturally discards the now-invalid forward pages.

## Edge cases

- `forward` after a fresh `visit` moves nowhere (forward history cleared).
- `back` or `forward` beyond bounds clamps to the first or last page.
- Visiting from a middle position drops all pages ahead.

## Pitfalls

- Forgetting to clear forward history on `visit`.
- Not clamping `steps` to valid bounds.
- Off-by-one when truncating with a slice.

## Related problems

- 146 LRU Cache
- 155 Min Stack
- 1381 Design a Stack With Increment Operation
