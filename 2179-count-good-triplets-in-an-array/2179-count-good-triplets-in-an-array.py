class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    
    def add(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i
    
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)

        pos2 = [0] * n
        for i, v in enumerate(nums2):
            pos2[v] = i
        
        arr = [pos2[v] for v in nums1]

        left_less = [0] * n
        ft = Fenwick(n)

        for j in range(n):
            r = arr[j] + 1
            left_less[j] = ft.sum(r - 1)
            ft.add(r, 1)
        
        right_greater = [0] * n
        ft = Fenwick(n)

        for j in range(n - 1, -1, -1):
            r = arr[j] + 1
            right_count = n - j - 1
            right_leq = ft.sum(r)
            right_greater[j] = right_count - right_leq
            ft.add(r, 1)

        ans = 0
        for j in range(n):
            ans += left_less[j] * right_greater[j]
        
        return ans