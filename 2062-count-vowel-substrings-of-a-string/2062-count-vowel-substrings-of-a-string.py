from collections import Counter

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
                
        count = 0 
        for i in range(len(word)):
            for j in range(len(word)):
                if j - i >= 4 and set(word[i:j+1]) == {'a','e','i','o','u'}:
                    count += 1
        
        return count