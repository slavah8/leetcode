class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == mid:
                if ans == -1:
                    ans = mid
                else:
                    ans = min(ans, mid)
                right = mid - 1
            elif arr[mid] > mid:
                right = mid - 1
            elif arr[mid] < mid:
                left = mid + 1
        return ans