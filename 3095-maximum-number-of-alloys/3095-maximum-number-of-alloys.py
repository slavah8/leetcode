class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        

        # check if any machine can make X alloys within given budget

        def can_make(X):
    
            for m in range(k):
                total = 0
                comp = composition[m]
                for j in range(n):
                    need = comp[j] * X # this much of the current metal to create X alloys
                    if need > stock[j]: # need to buy this metal
                        total += (need - stock[j]) * cost[j]
                        if total > budget:
                            break # stop early from this machine but still check other machines
                if total <= budget:
                    return True
            return False
        
        low = 0
        high = 10 ** 10
        # binary searching on the amount of alloys we can make
        while low < high:
            mid = (low + high + 1) // 2

            if can_make(mid):
                low = mid
            else:
                high = mid - 1
        return low

            


