class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        m = N - k + 1

        win = [0] * m
        curr = sum(nums[:k])
        win[0] = curr

        for i in range(1, m):
            curr += nums[i + k - 1] - nums[i - 1]
            win[i] = curr
        print(win)

        best_left = [0] * m
        best = 0
        for i in range(m):
            if win[i] > win[best]:
                best = i
            best_left[i] = best
        
        best_right = [0] * m
        best = m - 1
        for i in range(m - 1, -1, -1):
            if win[i] >= win[best]:
                best = i
            best_right[i] = best
        
        best_total = -1
        ans = [0, 0, 0]

        for mid in range(k, m - k):
            left = best_left[mid - k]
            right = best_right[mid + k]
            total = win[left] + win[mid] + win[right]
            if total > best_total:
                ans = [left, mid, right]
                best_total = total
        return ans

