class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        

        
        result = []
        def dfs(num, length):
            if length == n:
                result.append(num)
                return
            
            last_digit = num % 10
            if last_digit + k < 10:
                dfs(num * 10 + (last_digit + k), length + 1)
            if last_digit - k >= 0:
                dfs(num * 10 + (last_digit - k), length + 1)

            
        for i in range(1, 10):
            dfs(i, 1)
        return list(set(result))
