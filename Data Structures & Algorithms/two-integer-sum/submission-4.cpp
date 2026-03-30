class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mem_map;

        for (int i = 0; i < nums.size(); i++)
        {
            int diff = target - nums[i];

            if (mem_map.count(diff))
            {
                return {mem_map[diff], i};
            }

            mem_map[nums[i]] = i;
        }
    }
};
