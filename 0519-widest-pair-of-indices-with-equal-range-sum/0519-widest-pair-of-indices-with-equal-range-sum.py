class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        earliest_index = {0 : 0}

        widest_length = 0
        prefix_sum = 0
        for idx in range(1, N + 1):
            diff = nums1[idx - 1] - nums2[idx - 1]
            prefix_sum += diff

            if prefix_sum not in earliest_index:
                earliest_index[prefix_sum] = idx
            else:
                # we've seen this sum before so we can take the range
                L = earliest_index[prefix_sum]
                length = idx - L
                widest_length = max(widest_length, length)
        
        return widest_length

