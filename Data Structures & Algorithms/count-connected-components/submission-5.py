class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        out = 0
        adj = [[] for i in range(n)]

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit=set()
        
        def dfs(node):
            visit.add(node)
            for i in adj[node]:
                if i in visit:
                    continue
                dfs(i)



        for i in range(n):
            if i not in visit:
                dfs(i)
                out+=1
        
        return out


        

        