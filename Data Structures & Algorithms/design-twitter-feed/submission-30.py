# Create a user class to store who the user is following
# Make a deque to quickly popleft when number of posts are
# greater than 10
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
        # Create a user map that maps uid to User objects
        self.user_map = {}
        # Keep track of times that the post is created
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add user to user map if we haven't seen this 
        # user before
        if userId not in self.user_map:
            new_user = User()
            self.user_map[userId] = new_user


        # Grab user object and add post
        user = self.user_map[userId]
        user.add_post((self.timestamp, tweetId))
        # Create max heap by decrementing timestamp
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Return empty array if user doesn't exist
        if userId not in self.user_map:
            return []
            
        # Grab user initialize heap
        user = self.user_map[userId]
        temp = []

        # Make user follow themselves
        user.following[userId] = user
        # Iterate through all following
        for u in user.following.values():
            # If no posts made by user, continue
            if not u.posts:
                continue 

            # Grab the most recent post from each user, and 
            # push to the heap, storing the time, tweetid,
            # user, and index of post (always decremented by 1
            # to get the next post)
            index = len(u.posts) - 1
            time, tid = u.posts[index]
            heapq.heappush(temp, (time, tid, u, index - 1))
        
        # Initialize the return list
        ret = []
        # Iterate until temp is become empty or we got the 10 most
        # recent posts
        while temp and len(ret) < 10:
            # Pop from heap
            time, tid, u, index = heapq.heappop(temp)
            # Append tweet to the ret list
            ret.append(tid)
            # If the index is greater than or equal to 0, add the next
            # tweet in queue from that user
            if index >= 0:
                time, tid = u.posts[index]
                heapq.heappush(temp, (time, tid, u, index - 1))
        
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add users to the user map if they don't exist
        if followerId not in self.user_map:
            new_user = User()
            self.user_map[followerId] = new_user

        if followeeId not in self.user_map:
            new_user = User()
            self.user_map[followeeId] = new_user

        # Grab user object and add followee to their following list
        self.user_map[followerId].following[followeeId] = self.user_map[followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Delete the user from the following list if the user exists in the user map
        # and exists in the following map for the user
        if followerId in self.user_map and followeeId in self.user_map[followerId].following:
            del self.user_map[followerId].following[followeeId]
