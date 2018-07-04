from heapq import *


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.sequence = 0
        self.followList = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.d:
            self.d[userId] = [(-self.sequence, tweetId)]
        else:
            self.d[userId].append((-self.sequence, tweetId))
        if userId not in self.followList:
            self.followList[userId] = set([userId])
        else:
            self.followList[userId].add(userId)
        self.sequence += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        heap = []
        ans = []
        if userId in self.followList:
            for elem in self.followList[userId]:
                if elem in self.d:
                    for e in self.d[elem]:
                        heappush(heap, e)

        while heap and len(ans) < 10:
            elem = heappop(heap)
            ans.append(elem[1])
        return ans

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.followList:
            self.followList[followerId].add(followeeId)
        else:
            self.followList[followerId] = set([followeeId])

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.followList and followeeId in self.followList[followerId]:
            self.followList[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
