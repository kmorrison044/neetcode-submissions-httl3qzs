class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> numSet = Arrays.stream(nums)
                                    .boxed()
                                    .collect(Collectors.toSet());
        return nums.length != numSet.size();
    }
}