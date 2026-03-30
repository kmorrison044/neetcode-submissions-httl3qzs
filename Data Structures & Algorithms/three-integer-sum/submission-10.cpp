class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ret;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++)
        {
            if (i > 0 && nums[i] == nums[i-1])
            {
                continue;
            }
            int j = i + 1;
            int k = nums.size() - 1;

            while (j < k)
            {
                vector<int> check = {nums[i], nums[j], nums[k]};
                int three_sum = check[0] + check[1] + check[2];
                if (three_sum > 0)
                {
                    k -= 1;
                }
                else if (three_sum < 0)
                {
                    j += 1;
                }
                else
                {
                    ret.push_back(check);
                    j += 1;
                    k -=1 ;
                    while (nums[j] == nums[j-1] && j < k)
                    {
                        j += 1;
                    }
                }
            }
        }
        return ret;
    }
};
