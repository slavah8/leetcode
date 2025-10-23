class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        N = len(arr)
        if N == 1:
            return 1
        
        sign = [0] * (N - 1)

        for i in range(N - 1):
            if arr[i + 1] > arr[i]:
                sign[i] = 1 # uphill
            elif arr[i + 1] < arr[i]:
                sign[i] = -1 # downhill
            else:
                sign[i] = 0
        
        l = 0
        ans = 1
        print(sign)
        for r in range(N - 1):
            if sign[r] == 0:
                l = r + 1
            elif r > l and sign[r] == sign[r - 1]:
                l = r
            
            ans = max(ans, (r - l + 1) + 1)
        return ans

