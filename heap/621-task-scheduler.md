# 621. Task Scheduler

- **Difficulty:** Medium
- **Pattern:** heap
- **Companies:** Facebook, Amazon, Google, Microsoft, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/task-scheduler/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a list of CPU `tasks` (labeled by letters) and a cooldown `n`, each identical
task must be separated by at least `n` intervals. In each interval the CPU runs one
task or idles. Return the minimum number of intervals required to finish all tasks.

## Approaches

### Greedy max-heap with cooldown queue

Count task frequencies and push them into a max-heap. Each tick, run the most
frequent available task and, if it still has work left, place it in a cooldown queue
tagged with the time it becomes ready again (`time + n`). When a queued task's
ready-time arrives, push it back onto the heap. Advance the clock until both the heap
and queue are empty.

- Time: `O(total_tasks * log 26)` = `O(total_tasks)`.
- Space: `O(26)` = `O(1)`.

## Key insight

Always scheduling the currently most frequent task greedily packs the timeline and
minimizes idle time. The cooldown queue enforces the `n`-interval gap without manual
bookkeeping of each task's last run.

## Edge cases

- `n == 0` — no cooldown, answer equals the number of tasks.
- One task type dominating forces idle slots between its runs.
- Many distinct tasks fill the gaps so no idling is needed.

## Pitfalls

- Off-by-one on the ready time: a task cooling down at interval `t` becomes available
  at `t + n`.
- Pushing back tasks whose remaining count is `0`.

## Related problems

- 767 Reorganize String
- 358 Rearrange String k Distance Apart
- 1834 Single-Threaded CPU
