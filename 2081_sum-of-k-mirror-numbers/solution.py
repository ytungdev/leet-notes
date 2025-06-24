from typing import List

# Time : Beats 79.65 %
# Memo : Beats 37.21 %
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        '''
        generate all 10-mirror nums `num`
            - generate `half`
                - gen odd-len then gen even-len
                - in range(0..10), range(10..100), range(100..1000)
            - `num` = concat(half,reverted(half))
        check is_k_mirror(k,num)
        add to `ret`
        end if `len(ret)` > n
        '''
        def is_k_mirror(k,num):
            arr = []
            while num:
                arr.append(num%k)
                num //= k
            for i in range(len(arr)//2):
                if arr[i] != arr[-1-i]:
                    return False
            return True
        cnt = 0
        ret = 0
        L = 1
        while cnt < n:
            R = L*10
            for parity in [1,0]:
                for half in range(L,R):
                    if cnt==n:
                        break
                    # abcba  : abc_ + b -> abcb_ + c ...
                    # abccba : abc_ + c -> abcb_ + b ...
                    full = half
                    rev = half if parity == 0 else half//10
                    while rev:
                        full = full*10 + rev%10
                        rev //= 10
                    if is_k_mirror(k,full):
                        ret += full
                        cnt += 1
            L = R
        return ret
