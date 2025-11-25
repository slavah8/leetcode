class Solution:
    def minSubarraySort(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)

        answer = []

        
        def count(window1, window2):
            if window1 == window2:
                return 0
            i = 0
            
            m = len(window1)
            longest_sorted = 0
            curr = 0

            start_sorted = 0
            while i < m:
                if window1[i] == window2[i]:
                    start_sorted += 1
                    i += 1
                else:
                    break
            end_sorted = 0
            j = m - 1
            while j > 0:
                if window1[j] == window2[j]:
                    end_sorted += 1
                    j -= 1
                else:
                    break
            return m - start_sorted - end_sorted
            


        l = 0
        window = []

        for r in range(n):
            
            x = nums[r]
            window.append(x)

            
            if r - l + 1 == k:
                length_sorted = count(window, sorted(window))
                answer.append(length_sorted)
                window = window[1:]
                l += 1
        return answer


            