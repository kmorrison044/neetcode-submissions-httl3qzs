class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        # Starting from right to left, the right_max is -1
        right_max = -1
        for i in range(n - 1, -1, -1):
            # The new potential max is the current value for the array
            # before transformation
            pot_max = arr[i]
            # The current value should be changed to the max value to the right
            # of it
            arr[i] = right_max
            # The new right_max is the maximum between the potential max and
            # the current value of right max
            right_max = max(right_max, pot_max)
        
        # Return modified original array.
        return arr