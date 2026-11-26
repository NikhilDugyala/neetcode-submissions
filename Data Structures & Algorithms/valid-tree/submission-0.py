class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n<=len(edges):
            return False

        adj = [[] for i in range(n)]

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        def dfs(node, prev):

            if node in visit:
                return False
            
            visit.add(node)
            
            for i in adj[node]:
                if i==prev:
                    continue
                if not dfs(i, node):
                    return False

                visit.add(i)
            return True

        return dfs(0,-1) and (len(visit)==n)
            

                    
        