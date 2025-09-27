class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        ones = 0
        for x in data:
            if x == 1:
                ones += 1
        
        left = 0
        N = len(data)
        ans = N
        zeroes_in_window = 0
        for right in range(N):
            if data[right] == 0:
                zeroes_in_window += 1
            
            while right - left + 1 > ones:
                left_num = data[left]
                if left_num == 0:
                    zeroes_in_window -= 1
                left += 1

            if right - left + 1 == ones:
                ans = min(ans, zeroes_in_window)
        return ans
            
            
