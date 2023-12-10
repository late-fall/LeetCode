class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = [x.lower() for x in s if x.isalnum()]
        
        l, r = 0, len(phrase) - 1
        
        print(phrase)
        
        while l < r:
            if phrase[l] != phrase[r]:
                return False
            l += 1
            r -= 1
        
        return True