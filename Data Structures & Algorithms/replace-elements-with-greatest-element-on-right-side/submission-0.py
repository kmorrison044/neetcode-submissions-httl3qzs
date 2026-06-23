class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 1:
            arr[0] = -1
            return arr
            
        temp = float("-inf")
        for i in range(n - 2, -1, -1):
            before = arr[i]
            arr[i] = max(temp, arr[i + 1])
            temp = before
        
        arr[n - 1] = -1
        return arr