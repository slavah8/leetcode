# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:

        low = 0
        high = 10 ** 4

        while low <= high:
            mid = (low + high) // 2
            if reader.get(mid) == (2 ** 31) - 1:
                high = mid - 1
            elif reader.get(mid) > target:
                high = mid - 1
            elif reader.get(mid) < target:
                low = mid + 1
            elif reader.get(mid) == target:
                return mid
        return -1 