class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        left = 0
        N = len(nums)
        window = []
        result = []
        flag = False
        for right, x in enumerate(nums):
            
            window.append(x)
            if len(window) > k:
                window = window[1:]

            if len(window) == k:
                if window == sorted(window):
                    flag = False
                    for i in range(k - 1):
                        if window[i] + 1 != window[i + 1]:
                            flag = True
                    if flag:
                        result.append(-1)
                    else:
                        result.append(max(window))
                else:
                    result.append(-1)
                     
        return result
            
