class Solution:
    def confusingNumberII(self, n: int) -> int:
        
        digits = [0, 1, 6, 8, 9]
        rot_map = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        ans = 0
        def is_confusing(x):
            old = x
            new = 0
            while x > 0:
                digit = x % 10
                if digit not in digits:
                    return False
                new = new * 10 + rot_map[digit]
                x = x // 10

            return old != new


        def dfs(curr):
            nonlocal ans
            for d in digits:
                nxt = curr * 10 + d

                if nxt > n or nxt == 0:
                    continue
                
                if is_confusing(nxt):
                    ans += 1

                dfs(nxt)

        dfs(0)
        return ans