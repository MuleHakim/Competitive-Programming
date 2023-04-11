class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        destination = len(graph)-1
        graph_dict = defaultdict(list)
        for i in range(len(graph)):
            graph_dict[i] = graph[i]
        
        all_path = []
        def dfs(node,graph_dict,cur_path):
            cur_path.append(node)
            if node == destination:
                all_path.append(cur_path[:])
                return
            for neighbor in graph_dict[node]:
                dfs(neighbor, graph_dict, cur_path)
                cur_path.pop()
                
        dfs(0,graph_dict,[])
        return all_path