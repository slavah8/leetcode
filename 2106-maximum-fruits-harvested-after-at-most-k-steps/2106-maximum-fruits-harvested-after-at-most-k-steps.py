class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        
        left_bound = startPos - k
        right_bound = startPos + k

        filtered = []
        for pos, amt in fruits:
            if pos < left_bound:
                continue
            if pos > right_bound:
                break
            filtered.append((pos, amt))

        pos = [pos for pos, _ in filtered]
        amt = [a for _, a in filtered]
        n = len(pos)
    
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + amt[i]
        print(prefix)

        def interval_cost(l, r):

            L = pos[l]
            R = pos[r]
            if R <= startPos:
                # everything is to the left
                return startPos - L

            # everything is to the right
            if L >= startPos:
                return R - startPos

            # back and forth
            # 2 cases either left first or right first
            # left first
            left_first = (startPos - L) * 2 + (R - startPos)
            # right first
            right_first = (R - startPos) * 2 + (startPos - L)
            return min(left_first, right_first)

        l = 0
        ans = 0
        for r in range(n):

            while l <= r and interval_cost(l, r) > k:
                l += 1

            if l > r:
                continue

            total = prefix[r + 1] - prefix[l]
            if total > ans:
                ans = total
                
        return ans

