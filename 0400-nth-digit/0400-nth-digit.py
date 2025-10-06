class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1
        start = 1
        count = 9

        while n > length * count:
            n -= length * count
            length += 1
            count *= 10 # 9, 10 - 100 : 90, 100 - 1000 : 900 ...
            start *= 10 # 1 -> 10 -> 100 -> 1000

        # when loop ends, n lies inside the [start ...] block with 'length' digits/number
        idx = n - 1
        num = start + (idx // length)
        pos = idx % length
        return int(str(num)[pos])

