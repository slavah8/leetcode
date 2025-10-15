class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False
        self.pass_count = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        
        def insert(root, word):
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.pass_count += 1
            node.terminal = True

        root = TrieNode()
        for word in words:
            insert(root, word)
        
        
        answer = []
        for i, word in enumerate(words):
            node = root
            count = 0
            for char in word:
                node = node.children[char]
                count += node.pass_count
            answer.append(count)
        return answer


                


        