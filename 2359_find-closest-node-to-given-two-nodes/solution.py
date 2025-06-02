from typing import List

# Time : Beats 48.28 %
# Memo : Beats 46.55 %
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        inf = float('inf')
        
        def get_dist(node):
            dist = [inf]*n
            visited = [False]*n
            
            u = node
            d = 0
            dist[node] = 0
            while edges[u] != -1 and not visited[u]:
                visited[u] = True
                v = edges[u]
                d += 1
                dist[v] = min(d, dist[v])
                u = v
            return dist
                
        dist1 = get_dist(node1)
        dist2 = get_dist(node2)
        min_d = inf
        min_i = -1
        for i in range(n):
            if dist1[i] != inf and dist2[i] != inf:
                d = max(dist1[i],dist2[i])
                if d < min_d:
                    min_d = d
                    min_i = i
        return min_i