class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        
        balances = defaultdict(int)

        for frm, to, amt in transactions:
            balances[frm] -= amt
            balances[to] += amt

        
        debts = [v for v in balances.values() if v != 0]

        n = len(debts)
        print(debts)
        INF = 10 ** 10
        def backtrack(i):
            
            while i < n and debts[i] == 0:
                i += 1
            if i == n:
                return 0
            
            best = INF
            for j in range(i + 1, n):
                if debts[i] * debts[j] < 0: # must be opposite signs
                    old_j = debts[j]
                    debts[j] += debts[i]
                    best = min(best, 1 + backtrack(i + 1))
                    debts[j] = old_j
            
                    if old_j + debts[i] == 0:
                        break
            
            return best


        
        return backtrack(0)