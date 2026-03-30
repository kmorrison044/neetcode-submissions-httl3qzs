class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l, m, r):
            # Grab the array slices found in the previous step
            left, right = nums[l : m+1], nums[m + 1: r + 1]

            # i is the index we will use to change nums in place.
            # j and k are used to index the left and right arrays defined
            # above.
            i, j, k = l, 0, 0
            
            # Loop while we haven't incremented the left or right lists
            # fully
            while j < len(left) or k < len(right):
                # If we explored the whole left list, fill the rest of the space
                # in nums with the elements in the right list
                if j >= len(left):
                    while k < len(right):
                        nums[i] = right[k]
                        i += 1
                        k += 1
                
                # If we explored everything in the right list, fill the rest of the
                # space in nums with the elements in the left list
                if k >= len(right):
                    while j < len(left):
                        nums[i] = left[j]
                        i += 1
                        j += 1
                
                # Otherwise just check which number in right or left is smaller
                # and change nums in place to the element
                if j < len(left) and k < len(right):
                    if left[j] < right[k]:
                        nums[i] = left[j]
                        j += 1
                    else:
                        nums[i] = right[k]
                        k += 1
                    i += 1

        # First define the top level function for merge sort.
        # In this function, to save memory, we are only grabbing
        # the pointers where merges need to happen, and then passing
        # the pointers to the merge function to actually perform the merge.
        def mergeSort(l, r):
            if l >= r:
                return
            
            m = (l + r) // 2
            mergeSort(l, m)
            mergeSort(m + 1, r)
            merge(l, m, r)
        
        # Call mergeSort starting at 0 and going to the end of the list
        mergeSort(0, len(nums) - 1)
        return nums