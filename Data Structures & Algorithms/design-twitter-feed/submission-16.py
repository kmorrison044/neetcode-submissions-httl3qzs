class User:
    def __init__(self):
        self.following = {}
        self.posts = []
        self.n = 10
    
    def add_post(self, tweetId):
        # if len(self.posts) < self.n:
        #     heapq.heappush(self.posts, -tweetId)
        # else:
        #     heapq.heappushpop(self.posts, -tweetId)
        self.posts.append(tweetId)

class Twitter:

    def __init__(self):
        self.user_map = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_map:
            new_user = User()
            self.user_map[userId] = new_user

        user = self.user_map[userId]
        user.add_post((self.timestamp, tweetId))
        self.timestamp += 1

        # for u in user.following.values():
        #     u.add_post(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.user_map[userId]
        temp = []

        for item in user.posts:
            if len(temp) < 10:
                heapq.heappush(temp, item)
            else:
                heapq.heappushpop(temp, item)

        for u in user.following.values():
            if u != user:
                for item in u.posts:
                    if len(temp) < 10:
                        heapq.heappush(temp, item)
                    else:
                        heapq.heappushpop(temp, item)
        
        n = len(temp)
        ret = n*[0]
        while temp:
            ret[n-1] = heapq.heappop(temp)[1]
            n -= 1
        
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_map:
            new_user = User()
            self.user_map[followerId] = new_user

        if followeeId not in self.user_map:
            new_user = User()
            self.user_map[followeeId] = new_user

        self.user_map[followerId].following[followeeId] = self.user_map[followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_map[followerId].following:
            del self.user_map[followerId].following[followeeId]
