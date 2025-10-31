class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        INF = 10 ** 15
        best = -INF

        n = len(energy)


        for r in range(k):
            if r >= n:
                break
            
            # steps = math.floor(n - 1 - r / k)
            steps = math.floor((n - 1 - r) / k)
            last = r + steps * k

            i = last
            gain = 0
            while i >= r:
                gain += energy[i]
                if gain > best:
                    best = gain
                i -= k

        return best 

