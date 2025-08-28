class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        N = len(nums)
        ans = [0] * N
        arr = [(num, i) for i, num in enumerate(nums)]

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            merged = []
            i = 0
            j = 0
            right_count = 0
            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    ans[left[i][1]] += right_count
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
                    right_count += 1

            while i < len(left):
                merged.append(left[i])
                ans[left[i][1]] += right_count
                i += 1
            
            while j < len(right):
                merged.append(right[j])
                j += 1
                
            return merged

        merge_sort(arr)
        return ans
