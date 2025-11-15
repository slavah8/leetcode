class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        node_degree = defaultdict(int)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
            node_degree[u] += 1
            node_degree[v] += 1
        
        
        
        sorted_nodes = sorted(node_degree, key = lambda node: node_degree[node], reverse = True)
    
        # need to assign
        assign = n
        node_val = defaultdict(int)
        for node in sorted_nodes:
            node_val[node] = assign
            assign -= 1

        importance = 0
        for u, v in roads:
            importance += node_val[u] + node_val[v]
        
        return importance


        

