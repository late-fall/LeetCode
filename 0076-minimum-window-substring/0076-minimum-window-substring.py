class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""
        
        countT, window = Counter(t), collections.defaultdict(int)
        
        need = len(countT)
        res, resLen = [-1,-1], float('inf')
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            
            if c in countT and window[c] == countT[c]:
                need -= 1
            
            while need == 0:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    need += 1
                l += 1
        
        return s[res[0]:res[1]+1] if resLen != float('inf') else ""
        
        
#         if len(t) > len(s):
#             return ""
#         sd, td = Counter(s), Counter(t)
#         if len(t) == len(s):
#             return s if sd == td else ""
        
#         l = 0
#         r = len(t) - 1
        
#         def checksub(sd, td):
#             for c in td:
#                 if td[c] > sd[c]:
#                     return False
#             return True
        
#         shortest = 10**5 + 1
#         res_l, res_r = -1, -1
        
#         sdic = Counter(s[l:r+1])
        
#         while r < len(s):
#             while s[l] not in td:
#                 sdic[s[l]] -= 1
#                 l += 1
#                 r += 1
#                 if r < len(s):
#                     sdic[s[r]] += 1
#                 if l == len(s):
#                     break
#             if checksub(sdic,td):
#                 prev_r = r
#                 if len(s[l:r+1]) < shortest:
#                     res_l = l
#                     res_r = r
#                     shortest = len(s[l:r+1])
#                 sdic[s[l]] -= 1
#                 l += 1
#                 r = l + len(t) - 1
#                 for i in range(prev_r, r, -1):
#                     sdic[s[i]] -= 1
#                 # sdic = Counter(s[l:r+1])
#                 continue
#             r += 1
#             if r < len(s):
#                 sdic[s[r]] += 1
        
#         return s[res_l:res_r+1]