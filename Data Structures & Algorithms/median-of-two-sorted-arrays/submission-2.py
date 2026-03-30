class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # We just have to run binary search on the smaller array and then
        # we can adjust the larger array's indices to get the left portion
        # of the conceptually merged array. 
        A = nums1
        B = nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A)-1
        while True:
            i = l + ((r-l)//2)
            j = half - i - 2

            # Aleft is the largest value in the left conceptual array
            Aleft = A[i] if i >= 0 else float('-inf')
            # Bleft is the largest value in the left conceptual array
            Bleft = B[j] if j >= 0 else float('-inf')
            # Aright is the smallest value in the right conceptual array
            Aright = A[i+1] if (i+1) < len(A) else float('inf')
            # Bright is the smallest value in the right conceptual array
            Bright = B[j+1] if (j+1) < len(B) else float('inf')

            # We know that the values for the left partition must be less than
            # the values of the right partition. Check those values and calculate
            # median to find answer. If Aright is too large, then we must decrease
            # the right pointer to give Aleft less values and vice versa.
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

