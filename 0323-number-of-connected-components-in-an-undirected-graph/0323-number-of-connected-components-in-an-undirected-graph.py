class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        count = 0
        def dfs(i):
            if i in seen:
                return 
            seen.add(i)
            for curr in graph[i]:
                dfs(curr)
        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)  
        return count       