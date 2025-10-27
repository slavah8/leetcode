class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        # bitmask on the required skills


        # dp(mask)
        m = len(req_skills)
        idx = {s: i for i, s in enumerate(req_skills)} # skill : bit index

        # person masks
        pmask = []
        for skills in people:
            mask = 0
            for s in skills:
                mask |= (1 << idx[s])
            pmask.append(mask)
        
        FULL = (1 << m) - 1

        # Let dp[mask] store the smallest team (list of indices) that covers exactly the skill-set mask.
        dp = [None] * (FULL + 1)
        dp[0] = []

        for i, p in enumerate(pmask):
            if p == 0:
                continue
            
            prev = dp[:]
            for mask in range(FULL + 1):
                team = prev[mask]
                if team is None:
                    continue

                new_mask = mask | p
                cand = team + [i]
                if dp[new_mask] is None or len(cand) < len(dp[new_mask]):
                    dp[new_mask] = cand
        return dp[FULL]

