class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        nums.sort()
        while nums:
            minn = nums[0]
            maxx = nums[-1]
            nums.remove(minn)
            nums.remove(maxx)
            add = (minn + maxx) / 2
            averages.append(add)
        return min(averages)