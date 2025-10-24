class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        
        result = []
        def dfs(num):
            
            if num > high:
                return
            
            if num >= low:
                result.append(num)
            if num == 0:
                return
            last = num % 10
            # from 12 you can either go to 121 or 123
            if last > 0:
                dfs(num * 10 + (last - 1))
            if last < 9:
                dfs(num * 10 + (last + 1))
        
        for x in range(10):
            dfs(x)
        return sorted(result)

