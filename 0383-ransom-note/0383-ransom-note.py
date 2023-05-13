class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_r, hash_m = {},{}
        
        for c in ransomNote:
            if c in hash_r:
                hash_r[c] += 1
            else:
                hash_r[c] = 1
        
        for c in magazine:
            if c in hash_m:
                hash_m[c] += 1
            else:
                hash_m[c] = 1
        
        for c in hash_r:
            if hash_r[c] > hash_m.get(c,0):
                return False
        return True