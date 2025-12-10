class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        count = 0

        string_num = str(num)
        n = len(string_num)

        for i in range(n - k + 1):
            j = i + k
            sub = int(string_num[i: j])
            print(sub)
            if sub == 0:
                continue
            if num % sub == 0:
                count += 1
            
        return count
        