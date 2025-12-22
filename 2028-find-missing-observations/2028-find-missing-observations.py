class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        m = len(rolls)

        total_rolls = m + n

        curr_sum = sum(rolls)
        curr_rolls = m
        print(curr_sum)
        print(curr_rolls)

        # curr_sum + x + y ... = mean
        # (curr_sum + x + y + z + ...) / total_rolls = mean
        # curr_sum + x + y + z + ... = mean * total_rolls
        # x + y + z ... = (mean * total_rolls) - curr_sum
        result = [0] * n
        missing_sum = (mean * total_rolls) - curr_sum
        if missing_sum < n * 1 or missing_sum > n * 6:
            return []
        
        x = missing_sum // n
        rem = missing_sum % n

        for i in range(n):
            result[i] = x
        
        for i in range(rem):
            result[i] += 1
        
        return result
        

            





        