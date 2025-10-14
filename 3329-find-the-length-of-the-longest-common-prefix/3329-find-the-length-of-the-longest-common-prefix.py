class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False

def insert_number(root : TrieNode, x: int):
    node = root
    for char in str(x):
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.terminal = True

def lcp_len(root: TrieNode, x: int):
    depth = 0
    node = root
    for char in str(x):
        if char not in node.children:
            break
        node = node.children[char]
        depth += 1
    return depth

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        def total_digits(arr):
            return sum(len(str(v)) for v in arr)
        
        build, probe = (arr1, arr2)
        if total_digits(arr2) < total_digits(arr1):
            build, probe = arr2, arr1

        root = TrieNode()
        for x in build:
            insert_number(root, x)
        
        ans = 0
        for y in probe:

            ans = max(ans, lcp_len(root, y))
        
        return ans
        