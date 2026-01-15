class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [-1] * n

        total = 0
        num = 1
        seen = set()
        for i in range(n):
            if i == n - 1:
                ans[i] = -total
            else:
                while num in seen:
                    num += 1
                ans[i] = num
                seen.add(num)
            total += num
                    
        
        return ans
            

