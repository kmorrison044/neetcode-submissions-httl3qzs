class User:
    def __init__(self):
        self.following = {}
        self.posts = deque()
        self.n = 10
    
    def add_post(self, tweetId):
        self.posts.append(tweetId)
        if len(self.posts) > 10:
            self.posts.popleft()

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
