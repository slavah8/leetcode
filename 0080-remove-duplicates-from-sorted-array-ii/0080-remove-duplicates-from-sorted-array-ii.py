class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        left = 0
        right = 1
        
        N = len(nums)
        count = 1
        while left < N and right < N:
            if nums[right] != nums[left]:
                count = 1
                left = right
            elif nums[right] == nums[left]:
                count += 1
            
            if count > 2:
                while right < N and nums[right] == nums[left]:
                    del nums[right]
                    N -= 1
                    continue
                left = right
                count = 1
            
            right += 1

    
        print(nums)
        return len(nums)
            
            
            

            
            

                



            
