class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hash_list = collections.defaultdict(int)
        hash_count = -1
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in hash_list:
                hash_count += 1
                hash_list[sorted_word] = hash_count
                res.append([word])
            else:
                res[hash_list[sorted_word]].append(word)
        
        return res