class Solution:
    def smallestNumber(self, n: int) -> int:
        
        binary = bin(n)
        print(binary)
        length = len(binary[2:])
        print(length)

        x = n
        while x.bit_count() != length:
            x += 1
        return x