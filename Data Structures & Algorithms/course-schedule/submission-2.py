class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}

        for course, preq in prerequisites:
            adj[course].append(preq)
            
        print(adj)
        visit = set()
        
        def dfs(node):
            if node in visit:
                return False
                
            if adj[node]==[]:
                return True
            
            visit.add(node)
            
            for pre in adj[node]:
                if not dfs(pre):
                    return False
            visit.remove(node)
            adj[node]=[]
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True