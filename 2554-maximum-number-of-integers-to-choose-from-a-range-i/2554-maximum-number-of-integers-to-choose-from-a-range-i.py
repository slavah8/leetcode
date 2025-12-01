class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        banned_set = set(banned)


        low = 0
        high = n

        # can i choose num amount of numbers that are not in banned and do not exceed maxSum
        def can(num):
            count = 0
            curr_sum = 0
            for x in range(1, n + 1):
                if x not in banned_set and x + curr_sum <= maxSum:
                    count += 1
                    curr_sum += x
                    if count >= num:
                        return True
                elif x + curr_sum >= maxSum:
                    break
            return count >= num
            
            
        while low <= high:
            mid = (low + high) // 2

            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans