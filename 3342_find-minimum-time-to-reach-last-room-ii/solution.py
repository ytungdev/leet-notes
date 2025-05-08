from typing import List
import heapq

# Time : Beats 94.50 %
# Memo : Beats 82,85 %
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])

        inf = float('inf')
        dist = [[inf]*n for y in range(m)]
        visited = [[False]*n for y in range(m)]
        heap = []
        
        dist[0][0] = 0
        visited[0][0] = True
        heapq.heappush(heap,(0,0,0,2))

        while heap:
            t,i,j,s = heapq.heappop(heap)
            if i == m-1 and j == n-1:
                return t
            for u,v in [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]:
                if 0 <= u < m and 0<= v < n and not visited[u][v]:
                    visited[u][v] = True
                    step = 2 if s == 1 else 1
                    time = max(t, moveTime[u][v]) + step
                    if time < dist[u][v]:
                        dist[u][v] = time
                        heapq.heappush(heap, (time, u,v, step))