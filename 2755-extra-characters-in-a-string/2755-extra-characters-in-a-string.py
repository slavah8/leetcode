class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        def insert(root, word):
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.terminal = True
        
        root = TrieNode()
        for word in dictionary:
            insert(root, word)
        
        # dp[i:] defined as minimum number of extra characters for s[i:]
        N = len(s)
        INF = 10 ** 10
        dp = [INF] * (N + 1)
        dp[N] = 0

        for i in range(N - 1, -1, -1):
            # skip this character and pay cost of 1
            best = 1 + dp[i + 1]
            # or try to match this char with word in dictionary

            j = i
            node = root
            while j < N and s[j] in node.children:
                node = node.children[s[j]]
                j += 1
                if node.terminal:
                    best = min(best, dp[j])
            dp[i] = best
        return dp[0]
            


        