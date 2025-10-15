class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:

        def insert(root, word):
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.terminal = True

        root = TrieNode()
        for word in words:
            insert(root, word)
        
        # dp[i:] = min number of valid strings to form target[i:]
        INF = 10 ** 10
        N = len(target)
        dp = [INF] * (N + 1)
        dp[N] = 0
        for i in range(N - 1, -1, -1):

            j = i
            node = root
            best = INF
            while j < N and target[j] in node.children:
                node = node.children[target[j]]
                best = min(best, 1 + dp[j + 1])
                j += 1
            dp[i] = best
        return -1 if dp[0] == INF else dp[0]

        