class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        S = sum(matchsticks)
        target = S / 4

        if S % 4 != 0:
            return False
        
        for x in matchsticks:
            if x > target:
                return False
        
        bucket = [0] * 4
        def dfs(i):
            if i == len(matchsticks):
                return True
            
            x = matchsticks[i]
            for b in range(4):

                if x + bucket[b] > target:
                    continue
                
                bucket[b] += x
                if dfs(i + 1):
                    return True
                bucket[b] -= x

                if bucket[b] == 0:
                    break
            return False

        return dfs(0)
            