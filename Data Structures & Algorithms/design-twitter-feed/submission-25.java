class User 
{
    public Map<Integer, User> following = new HashMap<>();
    public Deque<int[]> posts = new ArrayDeque<>();

    public User()
    {

    }

    public void addPost(int[] item)
    {
        posts.offer(item);
        if (posts.size() > 10)
        {
            posts.poll();
        }
    }
}
class Twitter {
    private Map<Integer, User> userMap = new HashMap<>();
    private int timestamp = 0;

    public Twitter() {
        
    }
    
    public void postTweet(int userId, int tweetId) {
        User user = userMap.computeIfAbsent(userId, k -> new User());
        user.addPost(new int[] {timestamp, tweetId});
        timestamp++;
    }
    
    public List<Integer> getNewsFeed(int userId) {
        User user = userMap.get(userId);
        if (user == null)
        {
            return new ArrayList<>();
        }

        Queue<Object[]> q = new PriorityQueue<>((a, b) ->
            Integer.compare((int) b[0], (int) a[0])
        );

        // Queue<Object[]> q = new PriorityQueue<>((a, b) ->
        //     Integer.compare((int) a[0], (int) b[0])
        // );

        user.following.put(userId, user);
        user.following.forEach((key, u) -> {
            if (!u.posts.isEmpty())
            {
                int[] lastPost = u.posts.peekLast();
                int time = lastPost[0];
                int uid = lastPost[1];

                q.offer(new Object[]{time, uid, u, u.posts.size() - 2});
                if (q.size() > 10)
                {
                    q.poll();
                }
            }

        });

        List<Integer> ret = new ArrayList<>();
        while (!q.isEmpty() && ret.size() < 10)
        {
            Object[] top = q.poll();
            int time = (int) top[0];
            int tid = (int) top[1];
            User u = (User) top[2];
            int index = (int) top[3];

            ret.add(tid);

            if (index >= 0)
            {
                Object[] arr = u.posts.toArray();
                int[] nextPost = (int[]) arr[index];
                time = nextPost[0];
                tid = nextPost[1];
                q.offer(new Object[] {time, tid, u, index - 1});
            }
        }

        return ret;
    }
    
    public void follow(int followerId, int followeeId) {
        User follower = userMap.computeIfAbsent(followerId, k -> new User());
        User followee = userMap.computeIfAbsent(followeeId, k -> new User());

        follower.following.put(followeeId, followee);
    }
    
    public void unfollow(int followerId, int followeeId) {
        User follower = userMap.get(followerId);
        if (follower != null)
        {
            follower.following.remove(followeeId);
        }
    }
}
