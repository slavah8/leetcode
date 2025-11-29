class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def side_sum(peak, cnt):
            if cnt == 0:
                return 0
            
            if peak > cnt:
                first = peak - 1
                last = peak - cnt
                return (first + last) * cnt // 2
            
            used = peak - 1
            sum_desc = peak * (peak - 1) // 2
            extra_ones = cnt - used
            return sum_desc + extra_ones
        
        left_len = index
        right_len = n - index - 1

        low = 1
        high = maxSum
        answer = 1
        while low <= high:
            mid = (low + high) // 2
            left_sum = side_sum(mid, left_len)
            right_sum = side_sum(mid, right_len)
            total = left_sum + right_sum + mid
            if total <= maxSum:
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        return answer


            
        
        
