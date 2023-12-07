class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = collections.deque([beginWord])
        res = 1
        while queue:
            print(queue)
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in wordList:
                            wordList.remove(next_word)
                            queue.append(next_word)
            res += 1
        return 0
#         if endWord not in wordList:
#             return 0
            
#         def dif_single(w1, w2):
#             cnt = 0
#             for i in range(len(w1)):
#                 if w1[i] != w2[i]:
#                     cnt += 1
#                     if cnt > 1:
#                         return False
#             return cnt == 1
        
#         wordList = set(wordList)
        
#         q = deque()
#         q.append(beginWord)
#         res = 1
        
#         while q:
#             for _ in range(len(q)):
#                 word = q.popleft()
#                 if endWord == word:
#                     return res
#                 for w in wordList:
#                     if dif_single(word, w) and w not in q:
#                         q.append(w)
#             for w in q:
#                 wordList.remove(w)
#             res += 1
        
#         return 0