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
        if (small.isEmpty() || num <= small.peek())
        {
            small.offer(num);
        }
        else
        {
            large.offer(num);
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
            return (small.peek() + large.peek()) / 2.0;
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
