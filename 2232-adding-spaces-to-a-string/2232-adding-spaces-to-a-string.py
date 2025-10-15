class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
 

        i = 0
        j = 0
        N = len(s)
        result = []
        while i < N and j < len(spaces):
            if i == spaces[j]:
                result.append(' ')
                j += 1
            else:
                result.append(s[i])
                i += 1

        while j == len(spaces) and i < N:
            result.append(s[i])
            i += 1
        return ''.join(result)

