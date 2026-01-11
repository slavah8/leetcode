class Fenwick:

    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s
    
    def add(self, i, delta):
        while i <= self.n:
            self.bit[i] += 1
            i += i & -i
        

class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        

        left_smaller = [0] * n
        right_smaller = [0] * n

        ft = Fenwick(n)
        for i, x in enumerate(nums):
            left_smaller[i] = ft.sum(x - 1)
            ft.add(x, 1)
        
        ft = Fenwick(n)
        for i in range(n - 1, -1, -1):
            x = nums[i]
            right_smaller[i] = ft.sum(x - 1)
            ft.add(x, 1)
        
        ans = 0
        for i in range(n):
            if left_smaller[i] >= k and right_smaller[i] >= k:
                ans += 1
        
        return ans
        
