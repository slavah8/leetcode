# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        length = reader.length()
        L = 0
        R = length - 1

        while L < R:
            N = R - L + 1
            if N % 2 == 1: # odd so equal halves exclude the middle
                mid = L + (N // 2)
                summ = reader.compareSub(L, mid - 1, mid + 1, R)
                if summ == 0:
                    return mid
                elif summ == 1:
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                # even so split exactly 
                mid = L + (N // 2) - 1
                summ = reader.compareSub(L, mid, mid + 1, R)
                if summ == 1:
                    R = mid
                else:
                    L = mid + 1
        return L