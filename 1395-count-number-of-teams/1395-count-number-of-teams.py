class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0

        for j in range(n):
            # fix index j
            less_left = 0
            greater_left = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    less_left += 1
                else:
                    greater_left += 1
            
            less_right = 0
            greater_right = 0
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    less_right += 1
                else:
                    greater_right += 1
            
            ans += (less_left * greater_right) + (greater_left * less_right)
        return ans

