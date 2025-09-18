class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        indegree_dictionary = {char : 0 for word in words for char in word}
        graph = defaultdict(list)

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_length = min(len(word1), len(word2))

            if word1[:min_length] == word2[:min_length] and len(word1) > len(word2):
                return ""

            for j in range(min_length):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    indegree_dictionary[word2[j]] += 1
                    break

        queue = deque()
        for char, indegree in indegree_dictionary.items():
            if indegree == 0:
                queue.append(char)

            
        topological_order = []
        while queue:
            char = queue.popleft()
            for new_char in graph[char]:
                indegree_dictionary[new_char] -= 1
                if indegree_dictionary[new_char] == 0:
                    queue.append(new_char)
            topological_order.append(char)
        if len(topological_order) != len(indegree_dictionary):
            return ''
        return ''.join(topological_order)
