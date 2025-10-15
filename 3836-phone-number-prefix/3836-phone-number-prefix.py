class TrieNode:
    def __init__(self):
        self.children = {}
        self.pass_count = 0
        self.terminal = False
    
class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:

        def insert(root, number):
            node = root
            depth = 0
            for char in number:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.pass_count += 1
                if node.terminal:
                    return False
            node.terminal = True
            return True
        
        root = TrieNode()
        numbers.sort()
        for number in numbers:
            if not insert(root, number):
                return False
        return True
        


        
