class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()

        q = deque([(0, -1)])
        while q:
            node, par = q.popleft()
            if node in seen:
                return False
            seen.add(node)
            for curr in graph[node]:
                if curr == par:
                    continue
                else:
                    q.append((curr, node))
        return len(seen) == n