from typing import List

# Time : Beats 66.65 %
# Memo : Beats 85.58 %
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def dfs(p, v, dist, adj):
            if dist < 0:
                return 0
            if dist == 0:
                return 1
            res = 1
            for a in adj[v]:
                if a != p:
                    res += dfs(v, a, dist-1, adj)
            return res
        
        def get_adj(edges):
            n = len(edges)+1
            adj = [[] for _ in range(n)]
            for s,d in edges:
                adj[s].append(d)
                adj[d].append(s)
            return adj
        
        adj1 = get_adj(edges1)
        adj2 = get_adj(edges2)
        
        target2 = max([dfs(None,i,k-1,adj2) for i in range(len(edges2)+1)])
        
        return [dfs(None, i, k, adj1) + target2 for i in range(len(edges1)+1)]