# Beat 29.8%
from typing import List

class UF:
    def __init__(self, N):
        self.__root = [i for i in range(N)]
        self.__cost = [-1] * N
        self.__size = [1] * N


    def find_root(self, p):
        if self.__root[p] != p:
            # path compression
            self.__root[p] = self.find_root(self.__root[p])
        return self.__root[p]

    def add_edge(self, p, q, w):
        p_root = self.find_root(p)
        q_root = self.find_root(q)
        
        self.__cost[p_root] &= w
        self.__cost[q_root] &= w
        
        if p_root != q_root:
            if self.__size[p_root] < self.__size[q_root]:
                self.__root[p_root] = q_root
                self.__size[q_root] += self.__size[p_root]
                self.__cost[q_root] &= self.__cost[p_root]
            else:
                self.__root[q_root] = p_root
                self.__size[p_root] += self.__size[q_root]
                self.__cost[p_root] &= self.__cost[q_root]
            
    def find_cost(self,p):
        root = self.find_root(p)
        return self.__cost[root]

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
                    ans = uf.find_cost(p)
            res.append(ans)
        return res

