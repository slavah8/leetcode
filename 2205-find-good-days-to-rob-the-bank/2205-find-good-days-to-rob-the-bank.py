class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        left = [1] * n

        for i in range(1, n):
            if security[i] <= security[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        
        right = [1] * n
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                right[i] = right[i + 1] + 1
            else:
                right[i] = 1
        print(left)
        print(right)
        
        ans = []
        if time == 0:
            return list(range(n))
        for i in range(time, n - time):
            if left[i] >= time + 1 and right[i] >= time + 1:
                ans.append(i)
        
        return ans
        
