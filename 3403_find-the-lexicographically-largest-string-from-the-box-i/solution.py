from typing import List

# Time : Beats 95.36 %
# Memo : Beats  9.27 %
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word
        n = len(word)
        l = n+1-numFriends
        
        max_char = max(word)
        candidate = [i for i,char in enumerate(word) if char == max_char]
        for i in range(len(candidate)):
            candidate[i] = word[candidate[i]:candidate[i]+l]
        return max(candidate)

# Time : Beats 15.23 %
# Memo : Beats 50.33 %
# No native string comparison
class Solution2:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word
        n = len(word)
        l = n+1-numFriends
        
        
        hi = word[0]
        best = 0
        for i in range(n):
            if word[i] > hi:
                hi = word[i]
                best=i
        for i in range(1,n):
            if word[i] != hi:
                continue
            for j in range(0,n-i):
                if word[i+j] > word[best+j]:
                    best = i
                    break
                if word[i+j] < word[best+j]:
                    break
            
        return word[best:best+l]
                