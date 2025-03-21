from typing import List


class UF:
    def __init__(self, N):
        self.__root = [i for i in range(N)]
        self.__size = [1] * N
        self.__cost = [-1] * N

    def find_root(self, p):
        if self.__root[p] != p:
            # path compression
            self.__root[p] = self.find_root(self.__root[p])
        return self.__root[p]
    
        

    def add_edge(self, p, q, w):
        p_root = self.find_root(p)
        q_root = self.find_root(q)
        print(f'join : {p,q,w}')

        if p_root == q_root:
            self.__cost[p_root] &= w
            return
    
        if self.__size[p_root] < self.__size[q_root]:
            p_root, q_root = q_root, p_root
        
        print(f'{q_root} -> {p_root}')
        
        self.__root[q_root] = p_root
        self.__cost[p_root] &= (self.__cost[q_root] & w)
        self.__size[p_root] += self.__size[q_root]
        self.print()


    def find_cost(self,p):
        return self.__cost[p]
    
    def print(self):
        print(f'uf:{self.__root}, ws:{self.__cost}, sz:{self.__size}')

class Solution:

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UF(n)
        res = []

        for p,q,w in edges:
            uf.add_edge(p,q,w)

        for p,q in query:
            if p==q:
                ans = 0
            else:
                if uf.find_root(p) != uf.find_root(q):
                    ans = -1
                else:
                    ans = uf.find_cost(uf.find_root(p))
            res.append(ans)
        uf.print()
        return res



sol = Solution()

test = [
    [5,[[0,1,7],[1,3,7],[1,2,1]],[[0,3],[3,4]], [1,-1]],
    [3,[[0,2,7],[0,1,15],[1,2,6],[1,2,1]],[[1,2]], [0]],
    [5,[[0,1,7],[3,4,7],[1,2,1]],[[0,3],[3,4]], [-1,7]],
    [4,[[2,3,1],[1,3,5],[1,2,6],[3,0,7],[1,3,7],[0,2,5],[0,1,7]],[[2,1],[1,2],[0,1],[2,0],[0,2],[1,2],[3,2],[0,3],[2,1],[1,2]], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    [5,[[0,1,7],[1,3,7],[1,2,1]],[[0,3],[3,4]], [1,-1]],
    [7, [[3,0,2],[5,4,12],[6,3,7],[4,2,2],[6,2,2]], [[6,0]], [0]]
]

for t in test:
    n, edges, query, expect = t
    print(f'e : {edges}, q : {query}')
    res = sol.minimumCost(n, edges, query)
    print(f'res : {res}, exp : {expect}\n{"-"*50}\n\n')

# n, edges, query, exp = test[-1]
# res = sol.minimumCost(n, edges, query)
# print(f'res : {res}, exp : {exp}')

'''
[6]--07--[3]--02--[0]
|
02
|
[2]--02--[5]--12--[4]
'''