
# Time : Beats 100.0 %
# Memo : Beats 79.78 %
class Solution3:
    def flowerGame(self, n: int, m: int) -> int:
        return (m*n)//2
        

# Time : Beats 100.0 %
# Memo : Beats 50.98 %
class Solution2:
    def flowerGame(self, n: int, m: int) -> int:
        res = (m//2)*(n//2)*2
        if n%2:
            res += m//2
        if m%2:
            res += n//2
        return res
        

# Time : Beats 100.0 %
# Memo : Beats 30.60 %
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        m_e = m//2
        m_o = m_e+1 if m%2 else m_e

        if n%2:
            return (n//2)*(m_e+m_o)+m_e
        else:
            return (n//2)*(m_e+m_o)

