from typing import List


# Time : Beats 93.78 %
# Memo : Beats 65.55 %
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq_d = {}
        res=[]
        for i in range(0,10):
            freq_d[i] = 0
        for d in digits:
            freq_d[d] += 1

        # 1-9 *  100
        for a in range(1, 10):
            if freq_d[a] == 0:
                continue
            freq_d[a] -= 1
            # 0-9 * 10
            for b in range(0,10):
                if freq_d[b] == 0:
                    continue
                freq_d[b] -= 1
                # 0-8 * 1
                for c in range(0,10,2):
                    if freq_d[c] == 0:
                        continue
                    res.append(100*a + 10*b + c)
                freq_d[b] += 1
            freq_d[a] += 1
        return res

# Time : Beats 83.71 %
# Memo : Beats 45.52 %
class Solution2:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits_counter = {}
        res=[]
        start = 9
        end = 1
        for d in digits:
            if 0 < d < start:
                start = d
            if d > end:
                end = d
            digits_counter[d] = digits_counter.get(d,0) + 1
        
        # for n in range(100, 999,2):
        for n in range(start*100, (end+1)*100,2):
            test_counter = {}
            temp = n
            while temp >= 1:
                d = temp%10
                test_counter[d] = test_counter.get(d,0) + 1
                temp //= 10
            ok = True
            for digit, freq in test_counter.items():
                if freq > digits_counter.get(digit,0) or n%2:
                    ok = False
                    break
            if ok:
                res.append(n)
                
        return res