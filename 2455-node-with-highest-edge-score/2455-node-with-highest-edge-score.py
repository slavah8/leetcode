class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        
        node_score = defaultdict(int)
        for node, pointing_to in enumerate(edges):
            node_score[pointing_to] += node
        print(node_score)  
        best = None
        best_score = -1
        for node, score in node_score.items():
            if score > best_score:
                best = node
                best_score = score
            elif score == best_score and node < best:
                best = node
        return best

        

