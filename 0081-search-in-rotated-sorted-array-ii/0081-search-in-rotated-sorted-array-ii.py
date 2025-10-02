class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        # compare mid value with the ends to check which side is sorted
        # then condense search range as needed
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return True
            

            # if edges are equal to the middle we cant tell which side is sorted
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue
            
            # left half is strictly increasing
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # right half is strictly increasing
            elif nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            # when nums[mid] == nums[r] or nums[l] but not both
            else:
                if nums[mid] == nums[l]: # entire search space to the left is useless as they are all equal
                    l = mid + 1
                else: # search space to the right is all useless because they are all equal
                    r = mid - 1
        return False
                    
            
