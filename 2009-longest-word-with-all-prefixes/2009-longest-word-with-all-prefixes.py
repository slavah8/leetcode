class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False
    

def insert(root: TrieNode, word : str):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.terminal = True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        for w in words:
            insert(root, w)
        
        
        best = ""
        longest = 0
        path = []
        def dfs(node, length):
            nonlocal longest, best
            if length > longest:
                longest = length
                best = ''.join(path)
            elif length == longest:
                curr = ''.join(path)
                if curr < best:
                    best = curr
            
            
            for char, child in node.children.items():
                if node.children[char].terminal:
                    path.append(char)
                    dfs(node.children[char], length + 1)
                    path.pop()
            
        
        dfs(root, 0)
        return best



        