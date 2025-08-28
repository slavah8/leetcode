class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        def counting_sort(arr, exp):
            N = len(arr)
            out = [0] * N
            count = [0] * 10

            for x in arr:
                d = (x // exp) % 10
                count[d] += 1
            
            for i in range(1, 10):
                count[i] += count[i - 1]
            
            for i in range(N - 1, -1, -1):
                x = arr[i]
                d = (x // exp) % 10
                count[d] -= 1
                out[count[d]] = x
            return out
        
        N = len(nums)
        if N < 2:
            return 0

        arr = nums[:]
        max_val = max(arr)
        exp = 1

        while max_val // exp > 0:
            arr = counting_sort(arr, exp)
            exp *= 10
        
        ans = 0
        for i in range(1, N):
            gap = arr[i] - arr[i - 1]
            if gap > ans:
                ans = gap
        return ans

        