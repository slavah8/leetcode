class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        

        def cost(mm, ss):
            digits = f"{mm:02d}{ss:02d}"

            typed = digits.lstrip('0')

            if typed == '':
                typed = '0'
            
            cur = str(startAt)
            total = 0
            for ch in typed:
                if cur != ch:
                    total += moveCost
                    cur = ch
                total += pushCost
            return total
                

            
        
        INF = 10 ** 18
        best = INF
        for mm in range(100):
            ss = targetSeconds - mm * 60
            if 0 <= ss <= 99:
                cand = cost(mm, ss)
                best = min(best, cand)
        
        return best


