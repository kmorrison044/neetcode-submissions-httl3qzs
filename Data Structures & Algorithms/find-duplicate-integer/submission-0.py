class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Use Floyd's algorithm. Recognize that this is a linked list
        # cycle problem. When slow == fast, then we found the first
        # intersection. We have a second slow pointer (slow2) that starts
        # from the beginning again, and you loop through the linked list
        # again and whenever slow == slow2, then that is the index that 
        # contains the duplicate number. This is not intuitive at all
        # and would be really hard to solve if you haven't seen it before

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow