class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#         hashmap_s = {}
#         hashmap_t = {}
#         if len(s) != len(t):
#             return False
#         for c in s:
#             hashmap_s[c] = 1 + hashmap_s.get(c, 0)
#         for c in t:
#             hashmap_t[c] = 1 + hashmap_t.get(c, 0)
#         return hashmap_s == hashmap_t
    
#     # above memory and time complexity is (S +T)
    
#     memory issues can be solved by sorting it first. 
#     Interviews often assume sorting doesn't take extray memory usually. 
    
        return Counter(s) == Counter(t)