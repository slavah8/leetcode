class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if m * k > len(bloomDay):
            return -1

        # can we make m bouquets of k adjacent flowers in less than or equal to d days
        def can(d):
            need = m
            flowers = 0
            have = 0
            for x in bloomDay:
                if x <= d:
                    flowers += 1
                    if flowers == k:
                        have += 1
                        flowers = 0
                else:
                    flowers = 0
            return have >= need

        low = 1
        high = max(bloomDay)

        while low < high:
            mid = (low + high) // 2
            if can(mid):
                high = mid
                print(mid)
            else:
                low = mid + 1

        return low