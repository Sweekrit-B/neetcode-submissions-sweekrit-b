class Twitter:

    def __init__(self):
        self.posts_dict = {}
        self.followers_dict = {}
        self.currTweetNum = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts_dict[userId] = self.posts_dict.get(userId, []) + [(-self.currTweetNum, tweetId)]
        self.currTweetNum += 1
        # print(self.posts_dict)
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        # My solution
        all_posts = []
        for followee in self.followers_dict.get(userId, [userId]):
            for post in self.posts_dict.get(followee, []):
                heapq.heappush(all_posts, post)
        top_10 = []
        for _ in range(min(10, len(all_posts))):
            _, tweetId = heapq.heappop(all_posts)
            top_10.append(tweetId)
        return top_10

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers_dict.setdefault(followerId, {followerId}).add(followeeId)
        # print(self.followers_dict)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers_dict[followerId].discard(followeeId)
        if len(self.followers_dict[followerId]) == 0:
            self.followers_dict[followerId] = {followerId}
        return
