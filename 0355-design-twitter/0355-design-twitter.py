class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append((self.timestamp, tweetId))

        
    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        users = self.followers[userId]
        users.add(userId)


        for user in users:
            for timestamp, tweetId in self.tweets[user][-10:]:
                heapq.heappush(max_heap, (-timestamp, tweetId))
        
        feed = []

        while max_heap and len(feed) < 10:
            feed.append(heapq.heappop(max_heap)[1])
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
      
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)