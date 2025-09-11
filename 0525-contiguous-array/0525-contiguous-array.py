class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        sum_arr = []
        for x in nums:
            if x == 0:
                sum_arr.append(-1)
            else:
                sum_arr.append(1)
        
        print(sum_arr)
        balance = 0
        best = 0
        first_index = collections.defaultdict()
        first_index[0] = -1
        
        for i, x in enumerate(sum_arr):
            balance += x
            if balance not in first_index:
                first_index[balance] = i
            else:
                best = max(best, i - first_index[balance])
        return best

                