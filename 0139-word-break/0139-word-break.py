class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        tested = set()
        que = []
        for word in wordDict:
            if s[:len(word)] == word:
                que.append(s[len(word):])
                                
        while que:
            item = que.pop(0)
            if len(item) == 0:
                return True
            for word in wordDict:
                i = len(word)
                if item[:i] == word:
                    if item[i:] not in tested:
                        que.append(item[i:])
                        tested.add(item[i:])
                    
        return False
        
        
        ##my struggle to solve using hashmap and DFS
#         words = {}
#         for w in wordDict:
#             if w[0] not in words:
#                 words[w[0]] = [w]
#             else:
#                 words[w[0]].append(w)
        
        # def dfs(s):
        #     print(s)
        #     if len(s) == 0:
        #         return True
        #     if s[0] not in words:
        #         return
        #     for word in wordDict:
        #         if s[:len(word)] == word:
        #             res = dfs(s[len(word):])
        #             if res:
        #                 return True
        # return dfs(s)