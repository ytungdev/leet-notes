from typing import List

# Time : Beats 98.08 %
# Memo : Beats 68.80 %
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        i = 1
        res = n
        while i<n:
            if ratings[i] == ratings[i-1]:
                i+=1
                continue
            # up
            up = 0
            while ratings[i]>ratings[i-1]:
                up += 1
                res += up
                i += 1
                if i==n:
                    return res
            
            # down
            down = 0
            while i<n and ratings[i]<ratings[i-1]:
                down += 1
                res += down
                i += 1         
            # peak is overlapped
            res -= min(up,down)
        return res
    
# Time : Beats 75.80 %
# Memo : Beats 36.31 %
class Solution2:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1]*n
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1
        for j in range(n-2,-1,-1):
            if ratings[j] > ratings[j+1]:
                candies[j] = max(candies[j+1]+1, candies[j])
        
        return sum(candies)