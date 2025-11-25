class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # abs(x - y) = k
        # x - y = k
        # -y = k + x
        # y = -k - x

        # x - y = -k
        # -y = -k - x
        # y = k + x
        count = 0
        def backtrack(i, subset, banned):
            nonlocal count
            if i == n:
                if len(subset) > 0:
                    count += 1
                return

            # add current num if possible
            
            x = nums[i]
            if x not in banned:
                banned[x + k] += 1
                banned[x - k] += 1
                subset.append(nums[i])
                backtrack(i + 1, subset, banned)
                subset.pop()
                banned[x + k] -= 1
                if banned[x + k] == 0:
                    del banned[x + k]
                banned[x - k] -= 1
                if banned[x - k] == 0:
                    del banned[x - k]


            # skip current num
            backtrack(i + 1, subset, banned)


        backtrack(0, [], defaultdict(int))
        return count