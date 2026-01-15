class Fenwick:

    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
        # bit[i] stores the sum of a chunk ending at i of length lowbit(i)
        # i = 8, lowbit = 8 → stores arr[1..8]
        # bit[i]=sum(arr[i−lowbit(i)+1...i])
        # i = 6, lowbit = 2 → stores arr[5..6]

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
    def subarraysWithMoreOnesThanZeroes(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        n = len(nums)
        offset = n + 1
        size = 2 * n + 3

        ft = Fenwick(size)

        pref = 0
        ans = 0

        # insert pref=0 first
        ft.add(pref + offset, 1)
        
        for x in nums:
            pref += 1 if x == 1 else -1

            # count how many prefix sums are < current pref

            idx = pref + offset
            ans += ft.sum(idx - 1)
            idx %= MOD
            ft.add(pref + offset, 1)

        
        return ans % MOD

