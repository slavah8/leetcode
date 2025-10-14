class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        

        N = len(s)
        result = []
        for i in range(N - 1):
            if s[i] == "+" and s[i + 1] == "+":
                t = s[:i] + "--" + s[i + 2:]
                result.append(t)
        return result