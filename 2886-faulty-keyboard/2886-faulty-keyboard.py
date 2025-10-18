class Solution:
    def finalString(self, s: str) -> str:
        curr = ''
        def reverse(s):
            s_list = list(s)
            l = 0
            r = len(s) - 1
            while l < r:
                s_list[l],s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1
                print(s_list)
            return ''.join(s_list)

        for char in s:
            if char == 'i':
                curr = reverse(curr)
            else:
                curr += char
        return curr