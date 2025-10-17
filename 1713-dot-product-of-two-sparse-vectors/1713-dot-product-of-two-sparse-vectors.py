class SparseVector:
    def __init__(self, nums: List[int]):
        self.index_to_num = {}
        for i, x in enumerate(nums):
            if x != 0:
                self.index_to_num[i] = x


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for i, num in self.index_to_num.items():
            if i in vec.index_to_num:
                total += num * vec.index_to_num[i]
        return total



        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)