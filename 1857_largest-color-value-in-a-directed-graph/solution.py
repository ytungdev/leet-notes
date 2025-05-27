from typing import List
from collections import deque

# Time : Beats 98.38 %
# Memo : Beats 97.23 %
# Opt kahn's algorithm
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        colors = [ord(c)-97 for c in colors]
        
        adj = [[] for _ in range(n)]
        idg = [0]*n
        for e in edges:
            adj[e[0]].append(e[1])
            idg[e[1]] += 1

        q = deque()
        for v in range(n):
            if idg[v] == 0:
                q.append(v)

        i = 0
        dp = [{} for _ in range(n)]
        max_c = 0
        while q:
            v = q.popleft()
            c = colors[v]
            if c in dp[v]:
                dp[v][c] += 1
            else:
                dp[v][c] = 1
            
            max_c = max(dp[v][c], max_c)

            i += 1
            for a in adj[v]:
                idg[a] -= 1
                if idg[a] == 0:
                    q.append(a)
                for c, val in dp[v].items():
                    if c in dp[a]:
                        dp[a][c] = max(val, dp[a][c])
                    else:
                        dp[a][c] = val
        return max_c if i == n else -1

# Time : Beats 66.75 %
# Memo : Beats 87.07 %
# Kahn's algorithm
class Solution2:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        colors = [ord(c)-97 for c in colors]
        
        adj = [[] for _ in range(n)]
        idg = [0]*n
        for e in edges:
            adj[e[0]].append(e[1])
            idg[e[1]] += 1

        q = deque()
        for v in range(n):
            if idg[v] == 0:
                q.append(v)

        i = 0
        dp = [[0]*26 for _ in range(n)]
        max_c = 0
        while q:
            v = q.popleft()
            dp[v][colors[v]] += 1
            max_c = max(dp[v][colors[v]], max_c)

            i += 1
            for a in adj[v]:
                idg[a] -= 1
                if idg[a] == 0:
                    q.append(a)
                for c in range(26):
                    dp[a][c] = max(dp[v][c], dp[a][c])
        
        return max_c if i == n else -1
    

# Time : Beats 95.38 %
# Memo : Beats 65.82 %
# Opt 3-state DFS
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        def dfs(v):
            if state[v] == 2:
                # skip processing v
                return False
            if state[v] == 1:
                # cyclic detecteed
                return True
            
            # start processing v
            state[v]  = 1

            # process all adj[v]
            for a in adj[v]:
                cyclic = dfs(a)
                if cyclic:
                    return True
                for c in dp[a]:
                    if c in dp[v]:
                        dp[v][c] = max(dp[v][c], dp[a][c])
                    else:
                        dp[v][c] = dp[a][c]

            # all adj[v] processed, this node is processed
            color = colors[v]
            if color in dp[v]:
                dp[v][color] += 1
            else:
                dp[v][color] = 1
            max_c[v] = max(max_c[v], dp[v][color])
            state[v] = 2
            return False

        n = len(colors)
        colors = [ord(c)-97 for c in colors]
        adj = [[] for _ in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])
        
        
        state = [0]*n
        dp  = [{} for _ in range(n)]
        # dp[v][c] = max number of color c starting with vertex v

        max_c = [0]*n
        for v in range(n):
            # iterate all root
            if state[v] == 0:
                cyclic = dfs(v)
                if cyclic:
                    return -1
        
        return max(max_c)