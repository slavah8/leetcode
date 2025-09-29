class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        N = len(arr)
        INF = 10 ** 10
        best_left = [INF] * N

        curr = 0
        left = 0
        best = INF
        for right, x in enumerate(arr):
            curr += x
            while curr > target: # shrink window
                num_left = arr[left]
                curr -= num_left
                left += 1
            
            if curr == target: # found valid window calculate length and store
                length = right - left + 1
                best = min(best, length)
            best_left[right] = best
        
        print(best_left)

        ans = INF
        left = 0
        curr = 0
        for right, x in enumerate(arr):
            curr += x
            while curr > target:
                left_num = arr[left]
                curr -= left_num
                left += 1
            
            if curr == target: # found valid window
                if left > 0 and best_left[left - 1] < INF:
                    length = right - left + 1
                    ans = min(ans, length + best_left[left - 1])
        
        return ans if ans != INF else -1
                