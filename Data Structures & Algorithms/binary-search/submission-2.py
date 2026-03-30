class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ############# Iterative bin search: ################
        
        #l, r = 0, len(nums)-1
#
        #while l <= r:
        #    mid = l + ((r-l) // 2)
#
        #    if target < nums[mid]:
        #        r = mid - 1
        #    elif target > nums[mid]:
        #        l = mid + 1
        #    else:
        #        return mid
#
        #return -1

        ############# Recursive bin search: #################

        def bin_search(l, r):
            if l > r:
                return -1

            m = l + ((r-l) // 2)
            if nums[m] < target:
                return bin_search(m+1, r)
            elif nums[m] > target:
                return bin_search(l, m-1)
            else:
                return m
        
        return bin_search(0, len(nums)-1)
