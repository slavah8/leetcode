class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        def at_most(nums, k):
            N = len(nums)
            distinct = 0
            freq = defaultdict(int)
            total = 0
            left = 0
            for right in range(N):
                x = nums[right]
                freq[x] += 1
                if freq[x] == 1:
                    distinct += 1
                
                while distinct > k:
                    y = nums[left]
                    freq[y] -= 1
                    if freq[y] == 0:
                        distinct -= 1
                    left += 1
                
                total += (right - left + 1)
            return total
        
        D = len(set(nums))
        at_most_d = at_most(nums, D)
        print(at_most_d)
        at_most_d_minus_1 = at_most(nums, D - 1)
        print(at_most_d_minus_1)
        return at_most_d - at_most_d_minus_1
        



