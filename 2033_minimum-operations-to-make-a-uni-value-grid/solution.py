# Beats 91.67%

from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = grid[0]
        for row in grid[1:]:
            arr += row
        arr = sorted(arr) # O(NlogN)
        
        p = arr[len(arr)//2] # median
        memo = {} # memo[i]:step_i
        result = 0
        for i in arr: # O(N)
            if i in memo:
                result += memo[i]
            else:
                step = abs(p-i)/x
                if step.is_integer():
                    result += int(step)
                    memo[i] = int(step)
                else:
                    return -1
        return result
    

# Beats 92.98%
# return -1 ealier, if there is number that cannot be reached by x-sized steps

class Solution2:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = grid[0]
        for row in grid[1:]:
            arr += row
        arr = sorted(arr) # O(NlogN)

        if not ((sum(arr)-arr[0]*len(arr))/x).is_integer():
            return -1

        p = arr[len(arr)//2]
        memo = {} # memo[i]:step_i
        result = 0
        for i in arr:
            if i in memo:
                result += memo[i]
            else:
                step = abs(p-i)/x

                if step.is_integer():
                    result += int(step)
                    memo[i] = int(step)
                else:
                    return -1
        return result
    

# Beats 97.37%
# return -1 ealier during grid flattening
# complete remaining operation with list comprehension

class Solution3:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        mod = grid[0][0] % x
        arr = []
        for row in grid:
            for i in row:
                if i%x != mod:
                    return -1
                arr.append(i)
        arr = sorted(arr) # O(NlogN)
        med = arr[len(arr)//2]
        return sum(abs(med - i)//x for i in arr)