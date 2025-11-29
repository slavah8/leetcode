class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        diff = []
        for i in range(n):
            diff.append(nums1[i] - nums2[i])
        
        # nums1[i] + nums1[j] > nums2[i] + nums2[j]
        # nums1[i] - nums2[i] + nums1[j] - nums2[j]
        # diff[i] + diff[j] > 0
        diff.sort()
        print(diff)

        i = 0
        j = n - 1
        count = 0
        
        while i < j:    
            if diff[i] + diff[j] > 0:
                count += (j - i)
                j -= 1
            else:
                i += 1
        return count
                


            

            


