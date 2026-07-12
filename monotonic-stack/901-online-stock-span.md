# 901. Online Stock Span

- **Difficulty:** Medium
- **Pattern:** monotonic-stack
- **Companies:** Amazon, Google, Bloomberg, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/online-stock-span/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Implement `StockSpanner`. Each call to `next(price)` returns the span: the number
of consecutive days (including today) whose price was less than or equal to
today's price, counting backwards.

## Approaches

### Brute force

Keep a list of all prices and scan backwards on every call.

- Time: `O(n)` per call, `O(n^2)` overall
- Space: `O(n)`

### Optimal

Maintain a monotonic stack of `(price, span)` pairs with strictly decreasing
prices. On each `next`, start with span `1` and pop every entry whose price is
`<= price`, accumulating its span into the current one.

- Time: amortized `O(1)` per call
- Space: `O(n)`

## Key insight

Collapsing dominated days into a single `(price, span)` pair means each day is
pushed and popped at most once, so the total work is linear.

## Edge cases

- Strictly increasing prices -> span grows every call.
- Equal consecutive prices -> counted (`<=` comparison).

## Pitfalls

- Using `<` instead of `<=`, which drops equal-price days from the span.
- Forgetting to add popped spans onto the current day's span.

## Related problems

- 739 Daily Temperatures (stack)
- 496 Next Greater Element I (monotonic-stack)
- 84 Largest Rectangle in Histogram (stack)
