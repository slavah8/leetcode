class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0

        
        N = len(arr)
        best = 0
        for i in range(1, N - 1):
            if arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
                l = i - 1
                r = i + 1
            
                while l - 1 >= 0 and arr[l - 1] < arr[l]:
                    l -= 1
                
                while r + 1 < N and arr[r] > arr[r + 1]:
                    r += 1
            
                best = max(best, r - l + 1)
        return best

