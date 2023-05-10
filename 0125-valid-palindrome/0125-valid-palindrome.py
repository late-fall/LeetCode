class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = ""
        for c in s:
            if c.isalnum():
                phrase += c.lower()
        
        return phrase == phrase[::-1]
            