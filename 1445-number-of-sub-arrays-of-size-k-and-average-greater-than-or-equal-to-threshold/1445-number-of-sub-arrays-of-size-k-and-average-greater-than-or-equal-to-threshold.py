class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        # build first window
        # get first window average

        window_sum = 0
        for i in range(k):
            window_sum += arr[i]
        
        total = 0

        if window_sum / k >= threshold:
            total += 1
        
        N = len(arr)
        left = 0
        for right in range(k, N):
            left_num = arr[left]
            right_num = arr[right]
            window_sum -= left_num
            window_sum += right_num
            window_avg = window_sum / k
            if window_avg >= threshold:
                total += 1
            left += 1
        return total
