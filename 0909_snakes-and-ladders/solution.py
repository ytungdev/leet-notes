from typing import List
from collections import deque

# Time : Beats  9.25 %
# Memo : Beats 78.54 %
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        N = n**2
        inf = float('inf')
        seq = [0]
        for i in range(n):
            row = n-i-1
            for j in range(n):
                col = n-j-1 if i%2 else j
                seq.append(board[row][col])
        
        
        dp = [inf]*(N+1)
        dp[1]=0
        q = deque([1])
        visited = [False]*(N+1)
        while q :
            curr = q.popleft()
            if visited[curr]:
                continue
            visited[curr] = True
            for d in range(1,7):
                dest = curr+d
                if dest > N:
                    break
                if seq[dest] != -1:
                    dest = seq[dest]
                    
                dp[dest] = min(dp[dest], dp[curr]+1)
                if not visited[dest]:
                    q.append(dest)
            
        return -1 if dp[-1]==inf else dp[-1]