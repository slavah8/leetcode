# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dimensions_list = binaryMatrix.dimensions()
        rows, cols = dimensions_list
        print(rows, cols)
        INF = 10 ** 10
        best = INF
        for row in range(rows):
            low = 0
            high = cols - 1
            while low <= high:
                mid = (low + high) // 2
                if binaryMatrix.get(row, mid) == 1:
                    best = min(best, mid)
                    high = mid - 1
                else:
                    low = mid + 1
        return best if best != INF else -1
            

