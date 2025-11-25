class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        upper = 10 ** 6
        def check(num):
            count = defaultdict(int)
            while num > 0:
                digit = num % 10
                count[digit] += 1
                num = num // 10

            for x, cnt in count.items():
                if x != cnt:
                    return False
            return True


        for num in range(n + 1, 10 ** 9):
            if check(num):
                return num