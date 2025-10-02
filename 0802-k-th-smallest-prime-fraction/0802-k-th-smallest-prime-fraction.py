class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:


        # a/b > c/d if ad > bc
        # a/b < c/d if ad < bc


        N = len(arr)
        low = 0.0
        high = 1.0

        while True:
            mid = (low + high) / 2
            i = 0
            count = 0
            best_num, best_den = 0, 1
            for j in range(1, N):
                while i < j and arr[i] / arr[j] <= mid:
                    i += 1
                count += i
                #arr[i-1] / arr[j]< best_num/best_den 
                if i > 0 and best_num * arr[j] < arr[i-1] * best_den:
                    best_num, best_den = arr[i - 1], arr[j]
            if count == k:
                return [best_num, best_den]
            elif count < k:
                low = mid
            else:
                high = mid 
