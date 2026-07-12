import heapq
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)      # user_id -> list of (time, tweet_id)
        self.following = defaultdict(set)    # user_id -> set of followee ids

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list:
        # Users whose tweets are visible: self plus everyone followed.
        users = self.following[userId] | {userId}
        heap = []
        for uid in users:
            for time, tweet_id in self.tweets[uid]:
                heapq.heappush(heap, (time, tweet_id))
                if len(heap) > 10:
                    heapq.heappop(heap)
        # Heap holds the 10 most recent; return newest first.
        return [tweet_id for _, tweet_id in sorted(heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# DEBUG RUNNER START
if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))   # [5]
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))   # [6, 5]
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))   # [5]
# DEBUG RUNNER END
