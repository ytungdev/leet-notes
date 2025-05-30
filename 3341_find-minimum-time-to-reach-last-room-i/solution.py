from typing import List
import heapq

# Time : Beats 97.21 %
# Memo : Beats 90.35 %
'''
optimised:
- Removed `dist`:
    - Time of last node is passed by state in heap
- Removed `if time < dist[u][v]`:
    - Each node will only be visited once, so this condition is always true
'''
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])

        inf = float('inf')
        visited = [[False]*n for y in range(m)]
        heap = []
        
        visited[0][0] = True
        heapq.heappush(heap,(0,0,0))

        while heap:
            t,i,j = heapq.heappop(heap)
            if i == m-1 and j == n-1:
                return t
            for u,v in [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]:
                if 0 <= u < m and 0<= v < n and not visited[u][v]:
                    visited[u][v] = True
                    heapq.heappush(heap, (max(t, moveTime[u][v]) + 1, u,v))

# Time : Beats 90.17 %
# Memo : Beats 98.20 %
class Solution1:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])

        inf = float('inf')
        dist = [[inf]*n for y in range(m)]
        visited = [[False]*n for y in range(m)]
        heap = []
        
        dist[0][0] = 0
        visited[0][0] = True
        heapq.heappush(heap,(0,0,0))

        while heap:
            t,i,j = heapq.heappop(heap)
            if i == m-1 and j == n-1:
                return t
            for u,v in [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]:
                if 0 <= u < m and 0<= v < n and not visited[u][v]:
                    visited[u][v] = True
                    time = max(t, moveTime[u][v]) + 1
                    if time < dist[u][v]:
                        dist[u][v] = time
                        heapq.heappush(heap, (time, u,v))