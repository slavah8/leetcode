class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        arr.sort()
        print(arr)
        INF = 10 ** 10
        low = 0
        high = max(arr)
        best = INF
        best_diff = INF

        def check(value: int) -> int:
            # sum of array after capping all elements at 'value'
            total = 0
            for x in arr:
                if x > value:
                    total += value
                else:
                    total += x
            return total
                    


        while low <= high:
            mid = (low + high) // 2
            print(mid)
            new_sum = check(mid)
            if new_sum > target:
                diff = abs(new_sum - target)
                if diff < best_diff or (diff == best_diff and mid < best):
                    best = mid
                    best_diff = diff
                high = mid - 1
            elif new_sum < target:
                diff = abs(new_sum - target)
                if diff < best_diff or (diff == best_diff and mid < best):
                    best = mid
                    best_diff = diff
                low = mid + 1
            else:
                return mid
        
        return best


            

