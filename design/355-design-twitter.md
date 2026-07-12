# 355. Design Twitter

- **Difficulty:** Medium
- **Pattern:** design
- **Companies:** Amazon, Twitter, Meta, Microsoft, Google
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/design-twitter/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Design a simplified Twitter supporting `postTweet`, `getNewsFeed` (the 10 most
recent tweet ids from the user and everyone they follow), `follow`, and
`unfollow`.

## Approaches

### Hash maps + heap merge

Keep a global timestamp counter, a map of `user -> list of (time, tweetId)`,
and a map of `user -> set of followees`. For the feed, merge the recent tweets
of the user and followees with a heap, keeping only the 10 newest.

- `getNewsFeed`: `O(k log 10)` where `k` is candidate tweets
- Other operations: `O(1)`
- Space: `O(users + tweets)`

## Key insight

A monotonically increasing timestamp gives a total order across users, so a
size-bounded heap can merge many tweet streams and surface the 10 most recent
without sorting everything.

## Edge cases

- A user follows themselves implicitly (include self in the feed).
- Unfollowing someone not followed is a no-op.
- Fewer than 10 total tweets returns all of them, newest first.

## Pitfalls

- Forgetting to include the user's own tweets in the feed.
- Returning tweets oldest-first instead of newest-first.
- Letting a user follow themselves twice or unfollow themselves.

## Related problems

- 23 Merge k Sorted Lists
- 146 LRU Cache
- 1046 Last Stone Weight
