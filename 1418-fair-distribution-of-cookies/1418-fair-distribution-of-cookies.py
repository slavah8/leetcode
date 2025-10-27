class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse = True)
        N = len(cookies)
        loads = [0] * k
        INF = 10 ** 15
        self.ans = INF

        def dfs(i):
            # all bags placed
            if i == len(cookies):
                self.ans = min(self.ans, max(loads))
                return

            # early prune if cant get better answer    
            if max(loads) >= self.ans:
                return
            
            bag = cookies[i]
            seen_zero = False
            for child in range(k):
                if loads[child] == 0 and seen_zero:
                    continue

                loads[child] += bag

                if loads[child] < self.ans:
                    dfs(i + 1)
        
                loads[child] -= bag
                
                if loads[child] == 0:
                    seen_zero = True
      
        
        dfs(0)
        return self.ans
