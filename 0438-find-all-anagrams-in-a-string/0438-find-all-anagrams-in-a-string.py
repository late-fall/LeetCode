class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
#         #NEETCODE
#         use hashmap
#         to count occurences of scount and p count
#         use sliding window
#         O(s-size of string), size of p once hashmap is limited to 26 (lower case letters)
        
#         use loop to determine if hashmap is the same
        
        plen = len(p)
        i = 0
        
        def getDict(substr):
            res = defaultdict(int)
            for c in substr:
                res[c] += 1
            return res
        
        def compareDict(a, b):
            for k in a:
                if a[k] != b[k]:
                    return False
            return True
        
        pdic = getDict(p)
        idic = getDict(s[0:plen])
        res = []
        if pdic == idic:
            res.append(0)
        while i + plen < len(s):
            idic[s[i+plen]] += 1
            idic[s[i]] -= 1
            i += 1
            if compareDict(idic,pdic):
                res.append(i)
        
        return res        
        
        # lp = list(p)
        # res = []
        # r = 0
        # l = 0
        # while r < len(s):
        #     if s[r] in lp:
        #         lp[lp.index(s[r])] = "_"
        #         r += 1
        #         if set(lp) == {"_"}:
        #             res.append(l)
        #             l += 1
        #             r = l
        #             lp = list(p)
        #     else:
        #         l += 1
        #         r = l
        #         lp = list(p)
        # return res
    
#         def checkAnagram(substr, test):
#             return sorted(substr) == sorted(test)
        
#         def findDifindex(substr, test):
#             lt = list(test)
#             for i, c in enumerate(substr):
#                 if c not in lt:
#                     return i
#                 else:
#                     lt[lt.index(c)] = "_"
                    
#         plen = len(p)
        
#         res = []
#         i = 0
#         while i < len(s) - plen:
#             if checkAnagram(s[i:plen+i], p):
#                 res.append(i)
#                 while plen + i < len(s) - 1 and s[plen+i] == s[i]:
#                     i += 1
#                     res.append(i)
#                 i += 1
#             else:
#                 i += max(1,findDifindex(s[i:plen+i], p))
        
#         return res