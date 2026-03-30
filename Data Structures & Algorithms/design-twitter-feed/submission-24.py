class User:
    def __init__(self):
        self.following = {}
        self.posts = deque()
    
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
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user_map:
            return []
            
        user = self.user_map[userId]
        temp = []

        user.following[userId] = user
        for u in user.following.values():
            if not u.posts:
                continue 

            index = len(u.posts) - 1
            time, uid = u.posts[index]
            if len(temp) < 10:
                heapq.heappush(temp, (time, uid, u, index - 1))
            else:
                heapq.heappushpop(temp, (time, uid, u, index - 1))
        
        ret = []
        while temp and len(ret) < 10:
            time, uid, u, index = heapq.heappop(temp)
            ret.append(uid)
            if index >= 0:
                time, uid = u.posts[index]
                heapq.heappush(temp, (time, uid, u, index - 1))
        
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
        if followerId in self.user_map and followeeId in self.user_map[followerId].following:
            del self.user_map[followerId].following[followeeId]
