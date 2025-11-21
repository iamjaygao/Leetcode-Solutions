class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create emplt sublist to save the course related to a preq
        graph = [[] for i in range(numCourses)]

        # initialize all indegree to 0
        indegree = [0] * numCourses

        # iterate all pairs, map the preq with it's course
        for cour, preq in prerequisites:
            graph[preq].append(cour)
            # update the number of 'cour''s precourse
            indegree[cour] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        result = []
        while q:
            curr = q.popleft()
            result.append(curr)
            for nxt in graph[curr]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        if len(result) == numCourses:
            return result 
        else:
            return []


