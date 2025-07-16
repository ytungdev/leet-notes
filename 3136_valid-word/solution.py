from typing import List

# Time : Beats 100.0 %
# Memo : Beats 34.23 %
class Solution:
    def isValid(self, word: str) -> bool:
        # check 1 : len(word) >= 3
        # check 2 : contain only lower(1) and upper(2) alphabet and digits(3)
        # check 3 : have vowel
        # check 4 : have consonant

        vowel = ['a','e','i','o','u']
        conso = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
        
        # check 1
        n = len(word)
        if n < 3:
            return False
        
        have_vowel = False
        have_conso = False

        for i in range(n):
            
            if word[i].isdigit():
                continue
            if word[i].lower() in vowel:
                # check 3
                have_vowel = True
            elif word[i].lower() in conso:
                # check 4
                have_conso = True
            else:
                # check 2
                return False
        
        return have_vowel and have_conso
        