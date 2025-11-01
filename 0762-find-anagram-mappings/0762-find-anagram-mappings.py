class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        idx2 = defaultdict(int)

        for i, x in enumerate(nums2):
            idx2[x] = i
        
        mapping = []
        for i, x in enumerate(nums1):
            mapping.append(idx2[x])
        return mapping
