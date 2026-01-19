class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        

        def convert(num):
            a, b = num.split('+')
            real = int(a)
            imag = int(b[:-1])

            return real, imag
        

        a, b = convert(num1)
        c, d = convert(num2)

        real_part = a * c - b * d 
        imag_part = a * d + b * c

        return f"{real_part}+{imag_part}i"
            