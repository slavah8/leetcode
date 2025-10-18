class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        def reverse(s):
            s_list = list(s)
            l = 0
            r = len(s) - 1
            while l < r:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1
            
            return ''.join(s_list)

        N = len(s)
        words_list = []
        flip = 0
        for i in range(0, N, k):
            if flip == 0:
                words_list.append(reverse(s[i:i + k]))
                flip = 1
            else:
                words_list.append(s[i:i + k])
                flip = 0
        
        return ''.join(words_list)
        
