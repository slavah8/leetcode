class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        MOD = 10 ** 9 + 7

        # 1) Generate all valid row masks (crack positions in [1..width-1])
        masks = []

        def dfs(pos, mask):
            # A row’s “crack positions” are the internal boundaries between bricks
            # set bit if there's a crack position

            if pos == width:
                masks.append(mask)
                return
            
            for b in bricks:
                nxt = b + pos

                if nxt > width:
                    continue
                
                new_mask = mask
                if nxt < width:
                    # crack position at nxt
                    new_mask |= (1 << (nxt - 1))
                dfs(nxt, new_mask)
        dfs(0, 0)
        if not masks:
            return 0
        
        m = len(masks)
        compat = [[] for _ in range(m)]
        for i in range(m):
            for j in range(m):
                if (masks[i] & masks[j]) == 0:
                    compat[i].append(j)

        # DP over height: dp[row_index][mask_idx]
        dp = [1] * m
        for _ in range(1, height):
            new_dp = [0] * m
            for i in range(m):
                ways = dp[i]
                if ways == 0:
                    continue

                for j in compat[i]:
                    new_dp[j] = (new_dp[j] + ways) % MOD
            dp = new_dp
        return sum(dp) % MOD
                    
                