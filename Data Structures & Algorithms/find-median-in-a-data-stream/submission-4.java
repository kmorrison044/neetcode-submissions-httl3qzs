class MedianFinder {
    private int n = 0;
    private Queue<Integer> large = new PriorityQueue<>();
    private Queue<Integer> small = new PriorityQueue<>((a, b) -> {
        return Integer.compare(b, a);
    });

    public MedianFinder() {
        
    }
    
    public void addNum(int num) {
        n++;
        if (!large.isEmpty() && num > large.peek())
        {
            large.offer(num);
        }
        else
        {
            small.offer(num);
        }

        if (large.size() > small.size() + 1)
        {
            small.offer(large.poll());
        }
        if (small.size() > large.size() + 1)
        {
            large.offer(small.poll());
        }
    }
    
    public double findMedian() {
        if (n % 2 == 0)
        {
            return (double) (small.peek() + large.peek()) / 2;
        }

        if (large.size() > small.size())
        {
            return large.peek();
        }
        else
        {
            return small.peek();
        }
        
    }
}
