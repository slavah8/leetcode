MOD = 10 ** 9 + 7

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
    def createSortedArray(self, instructions: List[int]) -> int:
        max_val = max(instructions)
        ft = Fenwick(max_val)

        cost = 0

        for i, x in enumerate(instructions):
            less = ft.sum(x - 1)
            leq = ft.sum(x)
            greater = i - leq
            cost = (cost + min(less, greater)) % MOD
            ft.add(x, 1)
        
        return cost
        