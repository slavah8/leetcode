class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False
        self.pass_count = 0
        self.end_count = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.pass_count += 1
        node.terminal = True
        node.end_count += 1
        

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]

        return node.end_count
        

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.pass_count

        

    def erase(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
            node.pass_count -= 1
        node.end_count -= 1
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)