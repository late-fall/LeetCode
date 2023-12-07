class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
            
        def dif_single(w1, w2):
            cnt = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    cnt += 1
                    if cnt > 1:
                        return False
            return cnt == 1
        
        wordList = set(wordList)
        
        q = deque()
        q.append(beginWord)
        res = 1
        
        while q:
            for _ in range(len(q)):
                wordCount = q.popleft()
                if endWord == wordCount:
                    return res
                for w in wordList:
                    if dif_single(wordCount, w) and w not in q:
                        q.append(w)
            for w in q:
                wordList.remove(w)
            res += 1
        
        return 0